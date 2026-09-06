"""Desktop JSONL adapter backed by the native Pico Runtime."""

from __future__ import annotations

import sys
import threading
from typing import Any

from .app_protocol import encode_event, make_event, parse_command_line
from .native_gateway import NativeGatewayRuntime
from .native_runtime import build_native_runtime


def _write_event(
    stdout: Any, event_type: str, *, session_id: str = "", run_id: str = "", payload: dict | None = None
) -> None:
    stdout.write(
        encode_event(
            make_event(
                event_type,
                session_id=session_id,
                run_id=run_id,
                payload=payload or {},
            )
        )
    )
    stdout.flush()


def _translate_gateway_event(event: dict[str, Any]) -> tuple[str, dict[str, Any]] | None:
    """Translate Gateway compatibility events to the desktop JSONL contract."""

    name = event.get("event")
    payload = dict(event.get("payload") or {})
    if name == "run.queued":
        return "user_message_received", {"message": payload.get("message", "")}
    if name == "run.completed":
        return "run_completed", {"final": payload.get("answer", ""), **payload}
    if name == "run.failed":
        return "run_failed", payload
    if name == "run.cancelled":
        return "run_canceled", {"reason": payload.get("error", "cancelled"), **payload}
    if name == "run.cancel_requested":
        return "run_status", {"phase": "cancel_requested", "label": "Cancel requested", **payload}
    if name == "stream_closed":
        return None
    if name == "reasoning_delta":
        return "run_status", {"phase": "reasoning", "label": payload.get("text", "")}
    if name == "media":
        return "media", payload
    if name == "interaction.requested":
        return "approval_requested", {
            "approval_id": payload.get("interaction_id", ""),
            "tool_name": payload.get("tool_name", "ask_user"),
            "args": payload.get("args", {}),
            "question": payload.get("question", ""),
            "choices": payload.get("choices", []),
            "risk_level": "interactive",
        }
    if name == "interaction.resolved":
        return "approval_resolved", {
            "approval_id": payload.get("interaction_id", ""),
            "decision": payload.get("decision", "rejected"),
            "reason": payload.get("reason", ""),
        }
    if name in {"run_status", "assistant_delta", "assistant_message", "tool_result"}:
        return name, payload
    return None


class _NativeAppThread:
    def __init__(self, host: Any) -> None:
        self.host = host
        self.runtime: NativeGatewayRuntime | None = None
        self.loop = None
        self.ready = threading.Event()
        self.error: BaseException | None = None
        self.thread = threading.Thread(target=self._run, name="codecub-native-runtime", daemon=True)

    def start(self) -> None:
        self.thread.start()
        self.ready.wait(timeout=60)
        if self.error is not None:
            self.thread.join(timeout=60)
            raise self.error
        if self.runtime is None:
            raise RuntimeError("native runtime thread did not start")

    def _run(self) -> None:
        import asyncio

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:

            async def initialize() -> None:
                self.runtime = NativeGatewayRuntime(self.host)
                await self.runtime.start()

            self.loop.run_until_complete(initialize())
            self.ready.set()
            self.loop.run_forever()
        except BaseException as exc:  # pragma: no cover - startup boundary
            self.error = exc
            self.ready.set()
        finally:
            if self.runtime is not None:
                try:
                    self.runtime.close()
                except BaseException:
                    if self.error is None:
                        self.error = RuntimeError("native runtime cleanup failed")
            if self.loop is not None and not self.loop.is_closed():
                self.loop.close()

    def close(self) -> None:
        runtime = self.runtime
        if runtime is not None:
            runtime.close()
        if self.loop is not None and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join(timeout=60)


def run_native_app_mode(args: Any, stdin: Any = None, stdout: Any = None) -> int:
    """Run the desktop JSONL protocol through one native runtime composition root."""

    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    host = build_native_runtime(args, interactive=True)
    app_thread = _NativeAppThread(host)
    output_lock = threading.Lock()

    try:
        app_thread.start()
        runtime = app_thread.runtime
        if runtime is None:  # pragma: no cover - startup boundary
            raise RuntimeError("native runtime thread did not expose a gateway")
        session = runtime.create_session(str(getattr(args, "resume", "") or ""))
        session_id = session["session_id"]

        def emit_from_runtime(event: dict[str, Any]) -> None:
            translated = _translate_gateway_event(event)
            if translated is None:
                return
            event_type, payload = translated
            with output_lock:
                _write_event(
                    stdout,
                    event_type,
                    session_id=session_id,
                    run_id=str(event.get("run_id", "") or ""),
                    payload=payload,
                )

        runtime.subscribe(session_id, emit_from_runtime)
        with output_lock:
            _write_event(
                stdout,
                "session_started",
                session_id=session_id,
                payload={
                    "cwd": str(host.paths.workspace),
                    "approval_policy": str(getattr(args, "approval", "ask") or "ask"),
                    "session_path": str(session.get("session_path", "")),
                },
            )

        for raw_line in stdin:
            if not str(raw_line).strip():
                continue
            try:
                command = parse_command_line(raw_line)
            except ValueError as exc:
                with output_lock:
                    _write_event(
                        stdout,
                        "run_failed",
                        session_id=session_id,
                        payload={"error_type": type(exc).__name__, "message": str(exc)},
                    )
                continue

            command_type = command["type"]
            if command_type == "close":
                with output_lock:
                    _write_event(stdout, "session_closed", session_id=session_id)
                return 0
            if command_type == "send_message":
                runtime.start_run(
                    session_id,
                    command["message"],
                    run_id=str(command.get("run_id", "") or ""),
                    busy_policy=str(command.get("busy_policy", "APPEND") or "APPEND"),
                )
                continue
            if command_type == "cancel_run":
                runtime.cancel_run(str(command.get("run_id", "") or ""), session_id)
                continue
            if command_type in {"approve_operation", "reject_operation"}:
                result = runtime.resolve_interaction(
                    str(command.get("approval_id", "") or ""),
                    command_type == "approve_operation",
                    run_id=str(command.get("run_id", "") or ""),
                    session_id=session_id,
                )
                if not result.get("accepted"):
                    with output_lock:
                        _write_event(
                            stdout,
                            "approval_resolved",
                            session_id=session_id,
                            run_id=str(command.get("run_id", "") or ""),
                            payload={
                                "approval_id": str(command.get("approval_id", "") or ""),
                                "decision": "rejected",
                                "reason": "unknown_interaction",
                            },
                        )
                continue
            if command_type == "import_legacy_pico":
                with output_lock:
                    _write_event(
                        stdout,
                        "legacy_import_completed",
                        session_id=session_id,
                        payload={"imported": 0, "skipped": True, "reason": "native session store is canonical"},
                    )
    finally:
        app_thread.close()

    return 0


__all__ = ["run_native_app_mode"]
