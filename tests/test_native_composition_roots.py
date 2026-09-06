"""Acceptance tests for the native CodeCub composition roots."""

from __future__ import annotations

import asyncio
import io
import json
from pathlib import Path

from codecub.gateway import GatewayServer
from codecub.native_app_mode import run_native_app_mode
from codecub.native_gateway import NativeGatewayRuntime
from pico.spine import Text
from pico.spine.events import Usage
from pico.spine.runner import TurnOutcome

ROOT = Path(__file__).parents[1]


def test_official_entries_point_to_native_root():
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    desktop = (ROOT / "desktop" / "resources" / "backend" / "codecub_backend_entry.py").read_text(encoding="utf-8")
    assert 'codecub = "codecub.cli:main"' in pyproject
    assert "from codecub.native_cli import main" in desktop
    assert "codecub.cli" not in desktop

    cli = (ROOT / "codecub" / "cli.py").read_text(encoding="utf-8")
    assert "from .native_cli import main as native_main" in cli


class _FakeLoop:
    def __init__(self) -> None:
        self.running = True
        self.tools = {}

    async def run_turn(self, request, emit, drain, *, stream, text_sink):
        del request, drain, stream
        text_sink["text"] = "native answer"
        await emit(Text(content="native answer"))
        return TurnOutcome(Usage(1, 2, 3), explicit_reply=True)

    async def run(self):
        while self.running:
            await asyncio.sleep(0.001)

    def stop(self):
        self.running = False


class _FakeSessionManager:
    def __init__(self) -> None:
        self.sessions = set()

    def get_or_create(self, key):
        self.sessions.add(key)
        return object()

    def _get_session_path(self, key):
        return Path("D:/native-state") / f"{key.replace(':', '_')}.jsonl"


class _FakeCron:
    on_job = None

    async def start(self):
        return None

    def stop(self):
        return None

    def status(self):
        return {"enabled": True, "jobs": 0, "next_wake_at_ms": None}

    def list_jobs(self, include_disabled=False):
        del include_disabled
        return []


class _FakeHost:
    def __init__(self):
        self.agent_loop = _FakeLoop()
        self.session_manager = _FakeSessionManager()
        self.paths = type("Paths", (), {"workspace": Path("D:/native-workspace")})()
        self.cron_service = _FakeCron()

    async def start(self):
        return None

    async def close(self):
        return None


def test_native_gateway_uses_native_scheduler_and_delivery_path():
    async def scenario():
        host = _FakeHost()
        runtime = NativeGatewayRuntime(host, user_workers=1, system_workers=1)
        await runtime.start()
        session = runtime.create_session("gateway:test")
        events = []
        runtime.subscribe(session["session_id"], events.append)

        result = runtime.start_run(session["session_id"], "hello")
        assert result["status"] == "QUEUED"
        for _ in range(100):
            if any(item["event"] == "run.completed" for item in events):
                break
            await asyncio.sleep(0.005)

        completed = next(item for item in events if item["event"] == "run.completed")
        assert completed["payload"]["answer"] == "native answer"
        assert any(item["event"] == "assistant_message" for item in events)
        assert any(item["event"] == "run_status" for item in events)
        await runtime._close_async()


def test_native_gateway_interaction_resolves_the_native_question_broker():
    async def scenario():
        host = _FakeHost()

        class _AskUser:
            def __init__(self) -> None:
                self.broker = None

            def set_broker(self, broker) -> None:
                self.broker = broker

        ask_user = _AskUser()
        host.agent_loop.tools["ask_user"] = ask_user
        runtime = NativeGatewayRuntime(host, user_workers=1, system_workers=1)
        await runtime.start()
        session = runtime.create_session("gateway:interaction")
        events = []
        runtime.subscribe(session["session_id"], events.append)

        pending = asyncio.create_task(
            runtime._question_broker.await_question(
                session["session_id"],
                prompt="Continue?",
                choices=["yes", "no"],
            )
        )
        for _ in range(100):
            request_id = runtime._question_broker.pending_req(session["session_id"])
            if request_id:
                break
            await asyncio.sleep(0)
        else:
            raise AssertionError("question broker did not publish a pending request")

        requested = next(item for item in events if item["event"] == "interaction.requested")
        assert requested["payload"]["interaction_id"] == request_id
        resolved = runtime.resolve_interaction(request_id, True, session_id=session["session_id"])
        assert resolved == {"interaction_id": request_id, "accepted": True}
        assert await pending == "approved"
        assert any(item["event"] == "interaction.resolved" for item in events)
        assert ask_user.broker is runtime._question_broker
        await runtime.aclose()

    asyncio.run(scenario())


def test_native_gateway_start_failure_rolls_back_host_resources():
    async def scenario():
        class _FailingHost(_FakeHost):
            def __init__(self):
                super().__init__()
                self.closed = False

            async def start(self):
                raise RuntimeError("backend start failed")

            async def close(self):
                self.closed = True

        host = _FailingHost()
        runtime = NativeGatewayRuntime(host, user_workers=1, system_workers=1)
        try:
            await runtime.start()
        except RuntimeError as exc:
            assert str(exc) == "backend start failed"
        else:
            raise AssertionError("startup failure must propagate")
        assert host.closed is True
        assert runtime._closed is True

    asyncio.run(scenario())


def test_native_gateway_close_finishes_host_cleanup_after_spine_failure(monkeypatch):
    async def scenario():
        import codecub.native_gateway as native_gateway

        host = _FakeHost()
        host.closed = False

        async def close_host():
            host.closed = True

        host.close = close_host

        async def fail_teardown(*args, **kwargs):
            del args, kwargs
            raise RuntimeError("spine teardown failed")

        monkeypatch.setattr(native_gateway, "teardown_spine", fail_teardown)
        runtime = NativeGatewayRuntime(host, user_workers=1, system_workers=1)
        await runtime.start()
        try:
            await runtime.aclose()
        except RuntimeError as exc:
            assert str(exc) == "spine teardown failed"
        else:
            raise AssertionError("spine teardown failure must propagate")
        assert host.closed is True

    asyncio.run(scenario())


def test_native_gateway_health_reports_configured_capacity_without_semaphore_internals():
    async def scenario():
        runtime = NativeGatewayRuntime(_FakeHost(), user_workers=3, system_workers=2)
        await runtime.start()
        assert runtime.health()["worker_pools"] == {"user": 3, "system": 2}
        await runtime.aclose()

    asyncio.run(scenario())


def test_native_gateway_marshals_session_calls_from_a_foreign_thread():
    import threading

    async def scenario():
        runtime = NativeGatewayRuntime(_FakeHost(), user_workers=1, system_workers=1)
        await runtime.start()
        result = {}

        def worker():
            result["session"] = runtime.create_session("gateway:thread")
            result["health"] = runtime.health()

        thread = threading.Thread(target=worker)
        thread.start()
        while thread.is_alive():
            await asyncio.sleep(0.001)
        thread.join()
        assert result["session"]["session_id"] == "gateway:thread"
        assert result["health"]["sessions"] == 1
        await runtime.aclose()

    asyncio.run(scenario())


def test_native_app_event_translation_preserves_media_and_interaction_shapes():
    from codecub.native_app_mode import _translate_gateway_event

    media = _translate_gateway_event(
        {"event": "media", "payload": {"items": [{"path": "out.png", "mime": "image/png", "kind": "image"}]}}
    )
    assert media == ("media", {"items": [{"path": "out.png", "mime": "image/png", "kind": "image"}]})

    requested = _translate_gateway_event(
        {
            "event": "interaction.requested",
            "payload": {"interaction_id": "i-1", "tool_name": "ask_user", "args": {"question": "?"}},
        }
    )
    assert requested == (
        "approval_requested",
        {
            "approval_id": "i-1",
            "tool_name": "ask_user",
            "args": {"question": "?"},
            "question": "",
            "choices": [],
            "risk_level": "interactive",
        },
    )


def test_gateway_transport_accepts_native_runtime_port():
    async def scenario():
        runtime = NativeGatewayRuntime(_FakeHost(), user_workers=1, system_workers=1)
        await runtime.start()
        server = GatewayServer(runtime, auth_token="secret")
        await server.start()
        reader, writer = await asyncio.open_connection(*server.address)
        try:
            writer.write(b'{"jsonrpc":"2.0","id":1,"method":"gateway.auth","params":{"token":"secret"}}\n')
            await writer.drain()
            assert json.loads((await reader.readline()).decode())["result"]["authenticated"] is True
        finally:
            writer.close()
            await writer.wait_closed()
            await server.close()

    asyncio.run(scenario())


def test_native_app_mode_translates_desktop_jsonl_to_native_events(monkeypatch):
    import codecub.native_app_mode as native_app_mode

    host = _FakeHost()
    monkeypatch.setattr(native_app_mode, "build_native_runtime", lambda args, interactive: host)

    class _Input:
        def __init__(self, output):
            self.output = output
            self.lines = ['{"type":"send_message","message":"hello"}\n']
            self.closed = False

        def __iter__(self):
            return self

        def __next__(self):
            if self.lines:
                return self.lines.pop(0)
            for _ in range(1000):
                if '"type":"run_completed"' in self.output.getvalue():
                    self.closed = True
                    return '{"type":"close"}\n'
                import time

                time.sleep(0.001)
            raise AssertionError("native app mode did not complete a run")

    stdout = io.StringIO()
    assert (
        run_native_app_mode(
            type("Args", (), {"resume": None, "approval": "never"})(),
            stdin=_Input(stdout),
            stdout=stdout,
        )
        == 0
    )
    events = [json.loads(line) for line in stdout.getvalue().splitlines()]
    assert events[0]["type"] == "session_started"
    assert any(event["type"] == "assistant_message" for event in events)
    assert any(event["type"] == "run_completed" for event in events)
