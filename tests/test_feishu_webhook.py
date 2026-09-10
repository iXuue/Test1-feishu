from __future__ import annotations

import asyncio
import json

import httpx
import pytest

from pico.channels.adapters.feishu.webhook import (
    FeishuWebhookBridge,
    FeishuWebhookChannel,
    FeishuWebhookSettings,
    _signature,
    extract_payload,
)


def _settings(**overrides) -> FeishuWebhookSettings:
    values = {
        "url": "https://open.feishu.cn/open-apis/bot/v2/hook/test",
        "outbound_secret": "outbound-secret",
        "inbound_secret": "inbound-secret",
        "host": "127.0.0.1",
        "port": 18791,
    }
    values.update(overrides)
    return FeishuWebhookSettings(**values)


def test_extract_payload_accepts_workflow_and_nested_feishu_shapes() -> None:
    assert extract_payload(
        {
            "event_id": "evt-1",
            "message_id": "msg-1",
            "chat_id": "oc-1",
            "sender_id": "ou-1",
            "text": "/fix-e2e hello",
        }
    ) == {
        "event_id": "evt-1",
        "message_id": "msg-1",
        "chat_id": "oc-1",
        "sender_id": "ou-1",
        "text": "/fix-e2e hello",
    }
    assert extract_payload(
        {
            "event": {
                "event_id": "evt-2",
                "message": {"message_id": "msg-2", "chat_id": "oc-2", "content": '{"text":"hello"}'},
                "sender": {"sender_id": {"open_id": "ou-2"}},
            }
        }
    ) == {
        "event_id": "evt-2",
        "message_id": "msg-2",
        "chat_id": "oc-2",
        "sender_id": "ou-2",
        "text": "hello",
    }


def test_feishu_signature_matches_custom_bot_formula() -> None:
    assert _signature("1700000000", "secret") == "fiWS2+gh28DOydAv7hzONH/mDn9+b1Y4Y5ivXWXy8vA="


def test_settings_from_env_requires_inbound_and_outbound(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_WEBHOOK_URL", "https://example.com/hook")
    monkeypatch.delenv("PICO_FEISHU_WEBHOOK_INBOUND_SECRET", raising=False)
    assert FeishuWebhookSettings.from_env() is None

    monkeypatch.setenv("PICO_FEISHU_WEBHOOK_INBOUND_SECRET", "inbound")
    settings = FeishuWebhookSettings.from_env()
    assert settings is not None
    assert settings.port == 18791
    assert settings.path == "/feishu/external"


@pytest.mark.asyncio
async def test_bridge_auth_dedup_and_intake_submission() -> None:
    channel = FeishuWebhookChannel(_settings(port=0))
    submitted: list[tuple[str, str, str]] = []

    async def submit(req) -> None:
        submitted.append((req.text, req.source.chat_id, req.message_id or ""))

    channel.intake.set_submit(submit)
    bridge = FeishuWebhookBridge(channel)
    await bridge.start()
    port = bridge.bound_port
    assert port is not None

    body = json.dumps(
        {"event_id": "evt-1", "message_id": "msg-1", "chat_id": "oc-1", "sender_id": "ou-1", "text": "hello"}
    ).encode()
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    writer.write(
        b"POST /feishu/external HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"Content-Type: application/json\r\n"
        b"X-Pico-Webhook-Secret: wrong\r\n"
        + f"Content-Length: {len(body)}\r\n\r\n".encode()
        + body
    )
    await writer.drain()
    assert b"401 Unauthorized" in await reader.read()
    writer.close()
    await writer.wait_closed()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://127.0.0.1:{port}/feishu/external",
            headers={"X-Pico-Webhook-Secret": "inbound-secret"},
            content=body,
        )
        duplicate = await client.post(
            f"http://127.0.0.1:{port}/feishu/external",
            headers={"X-Pico-Webhook-Secret": "inbound-secret"},
            content=body,
        )
    assert response.status_code == 202
    assert duplicate.status_code == 202
    assert duplicate.json()["duplicate"] is True
    assert submitted == [("hello", "oc-1", "msg-1")]
    await bridge.close()


@pytest.mark.asyncio
async def test_channel_sends_signed_text_without_logging_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["json"] = json.loads(request.content)
        return httpx.Response(200, json={"code": 0})

    transport = httpx.MockTransport(handler)
    real_client = httpx.AsyncClient
    monkeypatch.setattr(httpx, "AsyncClient", lambda **kwargs: real_client(transport=transport, **kwargs))
    channel = FeishuWebhookChannel(_settings())
    await channel.send("external-group", "hello")
    payload = captured["json"]
    assert isinstance(payload, dict)
    assert payload["msg_type"] == "text"
    assert payload["content"] == {"text": "hello"}
    assert payload["timestamp"]
    assert payload["sign"]
