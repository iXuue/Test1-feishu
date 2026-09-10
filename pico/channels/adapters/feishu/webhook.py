"""External Feishu-group webhook bridge.

This adapter is intentionally separate from :mod:`.channel`: a custom bot in an
external group can send messages through its webhook, but it cannot provide the
WebSocket event stream used by the app-bot adapter.  The bridge therefore accepts
messages from a Feishu Robot Assistant/Integration workflow over a small HTTP
callback and sends replies back through the custom bot webhook.

The callback accepts a deliberately small, user-configurable JSON envelope::

    {"event_id": "...", "message_id": "...", "chat_id": "...",
     "sender_id": "...", "text": "/fix-e2e ..."}

The workflow may use the aliases documented by ``extract_payload``.  No inbound
payload, URL, or secret is written to logs.
"""

from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import os
import time
from collections import OrderedDict
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any
from urllib.parse import urlsplit

import httpx
from loguru import logger

from pico.channels.intake import Intake
from pico.spine.delivery import Capabilities, TerminalDeliveryError

_DEFAULT_PATH = "/feishu/external"
_DEFAULT_HOST = "127.0.0.1"
_DEFAULT_PORT = 18791
_MAX_HEADER_BYTES = 16 * 1024
_MAX_BODY_BYTES = 128 * 1024
_DEDUP_CAP = 2048


@dataclass(frozen=True)
class FeishuWebhookSettings:
    """Environment-backed settings for the external-group integration."""

    url: str
    outbound_secret: str
    inbound_secret: str
    host: str = _DEFAULT_HOST
    port: int = _DEFAULT_PORT
    path: str = _DEFAULT_PATH
    allow_from: tuple[str, ...] = ("*",)

    @classmethod
    def from_env(cls) -> FeishuWebhookSettings | None:
        """Return settings only when the bridge has both URL and inbound secret.

        The outbound signing secret is optional because Feishu custom bots can be
        configured without signature verification.  The inbound secret is always
        required so exposing the callback does not create an unauthenticated Pico
        command endpoint.
        """

        url = os.environ.get("FEISHU_WEBHOOK_URL", "").strip()
        inbound_secret = os.environ.get("PICO_FEISHU_WEBHOOK_INBOUND_SECRET", "")
        if not url or not inbound_secret:
            return None
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("FEISHU_WEBHOOK_URL must be an absolute http(s) URL")

        raw_port = os.environ.get("PICO_FEISHU_WEBHOOK_PORT", str(_DEFAULT_PORT)).strip()
        try:
            port = int(raw_port)
        except ValueError as exc:
            raise ValueError("PICO_FEISHU_WEBHOOK_PORT must be an integer") from exc
        if not 1 <= port <= 65535:
            raise ValueError("PICO_FEISHU_WEBHOOK_PORT must be between 1 and 65535")

        raw_allow = os.environ.get("PICO_FEISHU_WEBHOOK_ALLOW_FROM", "*")
        allow_from = tuple(item.strip() for item in raw_allow.split(",") if item.strip()) or ("*",)
        path = os.environ.get("PICO_FEISHU_WEBHOOK_PATH", _DEFAULT_PATH).strip() or _DEFAULT_PATH
        if not path.startswith("/"):
            path = "/" + path
        return cls(
            url=url,
            outbound_secret=os.environ.get("FEISHU_WEBHOOK_SECRET", ""),
            inbound_secret=inbound_secret,
            host=os.environ.get("PICO_FEISHU_WEBHOOK_HOST", _DEFAULT_HOST).strip() or _DEFAULT_HOST,
            port=port,
            path=path,
            allow_from=allow_from,
        )


def _first(payload: dict[str, Any], *paths: tuple[str, ...]) -> Any:
    for path in paths:
        value: Any = payload
        for key in path:
            if not isinstance(value, dict) or key not in value:
                value = None
                break
            value = value[key]
        if value not in (None, ""):
            return value
    return None


def _text_value(value: Any) -> str:
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("{"):
            try:
                decoded = json.loads(text)
            except json.JSONDecodeError:
                return text
            if isinstance(decoded, dict):
                nested = decoded.get("text") or decoded.get("content")
                if isinstance(nested, str):
                    return nested.strip()
        return text
    if isinstance(value, dict):
        nested = value.get("text") or value.get("content")
        return nested.strip() if isinstance(nested, str) else ""
    return ""


def extract_payload(payload: dict[str, Any]) -> dict[str, str]:
    """Normalize workflow JSON into the fields needed by ``Intake.publish``.

    Direct fields are preferred, while nested Feishu event shapes are accepted as
    a convenience.  The workflow should still send an explicit ``text`` field;
    accepting aliases here does not imply that Pico can infer arbitrary Feishu
    workflow schemas.
    """

    event = payload.get("event") if isinstance(payload.get("event"), dict) else {}
    sender = event.get("sender") if isinstance(event.get("sender"), dict) else {}
    sender_id_obj = sender.get("sender_id") if isinstance(sender.get("sender_id"), dict) else {}

    raw_text = _first(
        payload,
        ("text",),
        ("content",),
        ("message", "text"),
        ("event", "text"),
        ("event", "message", "text"),
        ("event", "message", "content"),
    )
    event_id = _first(payload, ("event_id",), ("id",), ("event", "event_id"), ("header", "event_id"))
    message_id = _first(
        payload,
        ("message_id",),
        ("event", "message_id"),
        ("message", "message_id"),
        ("event", "message", "message_id"),
    )
    chat_id = _first(
        payload,
        ("chat_id",),
        ("conversation_id",),
        ("event", "chat_id"),
        ("message", "chat_id"),
        ("event", "message", "chat_id"),
    )
    sender_id = _first(
        payload,
        ("sender_id",),
        ("open_id",),
        ("event", "sender_id"),
        ("event", "sender", "sender_id"),
    )
    if isinstance(sender_id, dict):
        sender_id = sender_id.get("open_id") or sender_id.get("user_id")
    if sender_id is None:
        sender_id = sender_id_obj.get("open_id") or sender_id_obj.get("user_id")

    return {
        "text": _text_value(raw_text),
        "event_id": str(event_id or "").strip(),
        "message_id": str(message_id or "").strip(),
        "chat_id": str(chat_id or "external-group").strip(),
        "sender_id": str(sender_id or "external-workflow").strip(),
    }


def _signature(timestamp: str, secret: str) -> str:
    """Create the signature required by a Feishu custom bot webhook."""

    string_to_sign = f"{timestamp}\n{secret}".encode("utf-8")
    digest = hmac.new(string_to_sign, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


class FeishuWebhookChannel:
    """A Channel-shaped outbound sender plus the normal Pico ``Intake`` gate."""

    name = "feishu_webhook"
    capabilities = Capabilities(streaming=False)

    def __init__(self, settings: FeishuWebhookSettings) -> None:
        self.settings = settings
        self.intake = Intake(
            self.name,
            SimpleNamespace(allow_from=settings.allow_from),
        )

    async def start(self) -> None:
        """The HTTP listener is owned by ``FeishuWebhookBridge``."""

    async def stop(self) -> None:
        """The sender is stateless; the bridge owns listener cleanup."""

    async def send(self, chat_id: str, content: str, media: list[str] | None = None) -> None:
        if media:
            raise TerminalDeliveryError("external Feishu webhook does not support media delivery")
        if not content.strip():
            return

        timestamp = str(int(time.time()))
        body: dict[str, Any] = {
            "msg_type": "text",
            "content": {"text": content},
        }
        if self.settings.outbound_secret:
            body["timestamp"] = timestamp
            body["sign"] = _signature(timestamp, self.settings.outbound_secret)

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(self.settings.url, json=body)
        except httpx.TransportError:
            # DeliveryHub owns retry/backoff for transport failures.
            raise
        except Exception as exc:
            raise TerminalDeliveryError("Feishu webhook transport failed") from exc

        if response.status_code >= 500:
            raise RuntimeError(f"Feishu webhook returned HTTP {response.status_code}")
        if response.status_code >= 400:
            raise TerminalDeliveryError(f"Feishu webhook rejected HTTP {response.status_code}")
        try:
            result = response.json()
        except ValueError as exc:
            raise TerminalDeliveryError("Feishu webhook returned invalid JSON") from exc
        if isinstance(result, dict) and result.get("code", 0) not in (0, "0", None):
            raise TerminalDeliveryError("Feishu webhook rejected the message")


class FeishuWebhookBridge:
    """Small authenticated HTTP callback that feeds the existing ``Intake``."""

    def __init__(self, channel: FeishuWebhookChannel) -> None:
        self.channel = channel
        self._server: asyncio.AbstractServer | None = None
        self._seen: OrderedDict[str, None] = OrderedDict()

    async def start(self) -> None:
        self._server = await asyncio.start_server(
            self._handle,
            self.channel.settings.host,
            self.channel.settings.port,
            limit=_MAX_HEADER_BYTES,
        )

    async def close(self) -> None:
        if self._server is None:
            return
        self._server.close()
        await self._server.wait_closed()
        self._server = None

    @property
    def bound_port(self) -> int | None:
        if not self._server or not self._server.sockets:
            return None
        return int(self._server.sockets[0].getsockname()[1])

    async def _handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            method, path, headers, body = await self._read_request(reader)
            if method != "POST" or path != self.channel.settings.path:
                await self._respond(writer, 404, {"ok": False, "error": "not_found"})
                return
            if not self._authorized(headers):
                await self._respond(writer, 401, {"ok": False, "error": "unauthorized"})
                return
            try:
                payload = json.loads(body.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                await self._respond(writer, 400, {"ok": False, "error": "invalid_json"})
                return
            if not isinstance(payload, dict):
                await self._respond(writer, 400, {"ok": False, "error": "json_object_required"})
                return

            normalized = extract_payload(payload)
            if not normalized["text"]:
                await self._respond(writer, 400, {"ok": False, "error": "text_required"})
                return
            dedup_key = normalized["message_id"] or normalized["event_id"]
            if dedup_key and dedup_key in self._seen:
                await self._respond(writer, 202, {"ok": True, "duplicate": True})
                return
            if dedup_key:
                self._seen[dedup_key] = None
                while len(self._seen) > _DEDUP_CAP:
                    self._seen.popitem(last=False)

            await self.channel.intake.publish(
                sender_id=normalized["sender_id"],
                chat_id=normalized["chat_id"],
                content=normalized["text"],
                metadata={
                    "event_id": normalized["event_id"],
                    "message_id": normalized["message_id"],
                    "chat_type": "group",
                    "source": "feishu_robot_assistant",
                },
                session_key=f"{self.channel.name}:{normalized['chat_id']}",
            )
            await self._respond(writer, 202, {"ok": True, "accepted": True})
        except ValueError as exc:
            await self._respond(writer, 400, {"ok": False, "error": str(exc)})
        except (asyncio.IncompleteReadError, ConnectionError):
            return
        except Exception:
            logger.exception("external Feishu webhook request failed")
            await self._respond(writer, 500, {"ok": False, "error": "internal_error"})
        finally:
            writer.close()
            try:
                await writer.wait_closed()
            except Exception:
                pass

    async def _read_request(
        self, reader: asyncio.StreamReader
    ) -> tuple[str, str, dict[str, str], bytes]:
        request_line = await reader.readline()
        if not request_line or len(request_line) > 4096:
            raise ValueError("invalid_request_line")
        try:
            method, path, _version = request_line.decode("ascii").strip().split()
        except (UnicodeDecodeError, ValueError) as exc:
            raise ValueError("invalid_request_line") from exc

        headers: dict[str, str] = {}
        header_bytes = len(request_line)
        while True:
            line = await reader.readline()
            header_bytes += len(line)
            if header_bytes > _MAX_HEADER_BYTES:
                raise ValueError("headers_too_large")
            if line in (b"\r\n", b"\n", b""):
                break
            try:
                key, value = line.decode("iso-8859-1").split(":", 1)
            except ValueError as exc:
                raise ValueError("invalid_header") from exc
            headers[key.strip().lower()] = value.strip()

        raw_length = headers.get("content-length", "0")
        try:
            content_length = int(raw_length)
        except ValueError as exc:
            raise ValueError("invalid_content_length") from exc
        if content_length < 0 or content_length > _MAX_BODY_BYTES:
            raise ValueError("body_too_large")
        body = await reader.readexactly(content_length)
        return method.upper(), path, headers, body

    def _authorized(self, headers: dict[str, str]) -> bool:
        supplied = headers.get("x-pico-webhook-secret", "")
        if not supplied:
            auth = headers.get("authorization", "")
            if auth.lower().startswith("bearer "):
                supplied = auth[7:].strip()
        return bool(supplied) and hmac.compare_digest(supplied, self.channel.settings.inbound_secret)

    async def _respond(self, writer: asyncio.StreamWriter, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        reason = {202: "Accepted", 400: "Bad Request", 401: "Unauthorized", 404: "Not Found", 500: "Internal Server Error"}.get(
            status,
            "Error",
        )
        writer.write(
            f"HTTP/1.1 {status} {reason}\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n\r\n".encode("ascii")
            + body
        )
        await writer.drain()


__all__ = [
    "FeishuWebhookBridge",
    "FeishuWebhookChannel",
    "FeishuWebhookSettings",
    "extract_payload",
]
