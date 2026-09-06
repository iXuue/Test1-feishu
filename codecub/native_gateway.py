"""Native-backed implementation of CodeCub's transport-neutral Gateway port.

The TCP JSON-RPC protocol remains a CodeCub compatibility surface, but its
runtime ownership is native Pico: one ``RuntimeAssembly``, one
``AgentLoop``, one ``Scheduler`` and one ``DeliveryHub`` per host process.
"""

from __future__ import annotations

import asyncio
import threading
import uuid
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Callable

from pico.agent.spine_runner import AgentTurnRunner
from pico.proactive_engine.schedulers.cron.types import CronSchedule
from pico.spine import (
    BusyPolicy,
    ChatType,
    Deliverable,
    MediaOut,
    Notice,
    Origin,
    OriginPools,
    Reasoning,
    Scheduler,
    Source,
    Text,
    ToolEvent,
    TurnEnded,
    TurnFailed,
    TurnRequest,
    TurnStarted,
)
from pico.spine.delivery import Capabilities, DeliveryHub
from pico.spine.teardown import teardown_spine
from pico.tui_rpc.question_broker import QuestionBroker

from .gateway_contract import RuntimeGatewayError

EventCallback = Callable[[dict[str, Any]], None]


@dataclass
class _NativeSession:
    session_id: str
    subscribers: dict[str, EventCallback] = field(default_factory=dict)


class _NativeGatewayRunner(AgentTurnRunner):
    def __init__(self, agent_loop: Any, text_by_conversation: dict[str, str]) -> None:
        super().__init__(agent_loop, stream=True)
        self._text_by_conversation = text_by_conversation

    async def run(self, req: TurnRequest, emit, drain):
        text_sink: dict[str, str] = {}
        outcome = await self._loop.run_turn(
            req,
            emit,
            drain,
            stream=True,
            text_sink=text_sink,
        )
        if req.conversation is not None and text_sink.get("text") is not None:
            self._text_by_conversation[req.conversation] = text_sink["text"]
        return outcome


class _NativeGatewayOutlet:
    name = "gateway"
    capabilities = Capabilities(streaming=True)

    def __init__(self, runtime: "NativeGatewayRuntime") -> None:
        self._runtime = runtime

    async def deliver(self, out: Deliverable) -> None:
        self._runtime._publish_deliverable(out)

    async def send_stream_chunk(self, chat_id: str, stream_id: str, delta: str, *, done: bool = False) -> None:
        del chat_id
        if delta:
            self._runtime._emit_for_conversation(
                stream_id,
                "assistant_delta",
                {"text": delta},
            )
        if done:
            self._runtime._emit_for_conversation(stream_id, "stream_closed", {})


class NativeGatewayRuntime:
    """Implement the GatewayServer runtime port on top of native Pico Spine."""

    def __init__(self, host: Any, *, user_workers: int = 4, system_workers: int = 2) -> None:
        if user_workers <= 0 or system_workers <= 0:
            raise ValueError("runtime worker counts must be greater than zero")
        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError as exc:  # pragma: no cover - construction guard
            raise RuntimeError("NativeGatewayRuntime must be created inside its home event loop") from exc
        self.host = host
        self._sessions: dict[str, _NativeSession] = {}
        self._run_sessions: dict[str, str] = {}
        self._run_ids_by_conversation: dict[str, deque[str]] = defaultdict(deque)
        self._text_by_conversation: dict[str, str] = {}
        self._lock = threading.RLock()
        self._closed = False
        self._started = False
        self._worker_capacities = {"user": user_workers, "system": system_workers}
        self._interaction_context: dict[str, dict[str, Any]] = {}
        self._question_broker = QuestionBroker(self._send_question_frame)
        self._runtime_task: asyncio.Task | None = None
        self._hub = DeliveryHub(send_max_retries=3)
        self._hub.register(_NativeGatewayOutlet(self))
        self._scheduler = Scheduler(
            _NativeGatewayRunner(host.agent_loop, self._text_by_conversation),
            OriginPools(user=user_workers, system=system_workers),
            self._sink,
        )

    async def start(self) -> None:
        if self._started:
            return
        if self._closed:
            raise RuntimeGatewayError("runtime gateway is closed")
        try:
            await self.host.start()
            ask_user = getattr(getattr(self.host.agent_loop, "tools", None), "get", lambda _name: None)("ask_user")
            if ask_user is not None and hasattr(ask_user, "set_broker"):
                ask_user.set_broker(self._question_broker)
            self.host.cron_service.on_job = self._on_cron_job
            await self.host.cron_service.start()
            self._runtime_task = asyncio.create_task(self.host.agent_loop.run())
            await asyncio.sleep(0)
            self._started = True
        except BaseException:
            try:
                await self._close_async()
            except BaseException:
                # Preserve the startup exception. The close path is independently
                # idempotent and will be retried by the owning host if needed.
                pass
            raise

    async def start_automation(self) -> None:
        if not self._started:
            await self.start()

    async def stop_automation(self) -> None:
        self.host.cron_service.stop()

    async def _on_cron_job(self, job: Any) -> str | None:
        with self._lock:
            session_id = str(job.payload.to or "").strip() or next(iter(self._sessions), "")
        if not session_id or session_id not in self._sessions:
            return None
        run_id = "run_" + uuid.uuid4().hex
        request = TurnRequest(
            origin=Origin.CRON,
            source=Source(
                channel="gateway",
                chat_id=session_id,
                sender_id="cron",
                chat_type=ChatType.DM,
            ),
            text=job.payload.message,
            conversation=session_id,
            busy=BusyPolicy.APPEND,
        )
        handle = self._submit_local(session_id, run_id, request)
        outcome = await handle.result()
        return self._text_by_conversation.pop(session_id, "") if outcome is not None else None

    def _call_home(self, callback: Callable[[], Any]) -> Any:
        try:
            current = asyncio.get_running_loop()
        except RuntimeError:
            current = None
        if current is self._loop:
            return callback()

        if self._loop.is_closed() or not self._loop.is_running():
            raise RuntimeGatewayError("native runtime home event loop is not running")

        async def invoke() -> Any:
            return callback()

        return asyncio.run_coroutine_threadsafe(invoke(), self._loop).result(timeout=60)

    def _new_session_id(self) -> str:
        return "gateway:" + uuid.uuid4().hex[:12]

    def create_session(self, session_id: str = "") -> dict[str, Any]:
        return self._call_home(lambda: self._create_session_local(session_id))

    def _create_session_local(self, session_id: str = "") -> dict[str, Any]:
        requested = str(session_id or "").strip() or self._new_session_id()
        with self._lock:
            self._ensure_open()
            if requested in self._sessions:
                raise RuntimeGatewayError(f"session already exists: {requested}")
            self.host.session_manager.get_or_create(requested)
            self._sessions[requested] = _NativeSession(requested)
        return self._session_info_local(requested)

    def resume_session(self, session_id: str) -> dict[str, Any]:
        return self._call_home(lambda: self._resume_session_local(session_id))

    def _resume_session_local(self, session_id: str) -> dict[str, Any]:
        requested = str(session_id or "").strip()
        if not requested:
            raise RuntimeGatewayError("session_id is required")
        with self._lock:
            self._ensure_open()
            if requested not in self._sessions:
                self.host.session_manager.get_or_create(requested)
                self._sessions[requested] = _NativeSession(requested)
        return self._session_info_local(requested)

    def session_info(self, session_id: str) -> dict[str, Any]:
        return self._call_home(lambda: self._session_info_local(session_id))

    def _session_info_local(self, session_id: str) -> dict[str, Any]:
        session = self._get_session(session_id)
        session_path = getattr(self.host.session_manager, "_get_session_path", lambda _key: "")(session.session_id)
        return {
            "session_id": session.session_id,
            "workspace": str(self.host.paths.workspace),
            "session_path": str(session_path),
            "active_runs": {
                cid: ids[0] for cid, ids in self._run_ids_by_conversation.items() if ids and cid == session.session_id
            },
            "extension_registry": {},
            "automation": self.host.cron_service.status(),
        }

    def close_session(self, session_id: str) -> dict[str, Any]:
        return self._call_home(lambda: self._close_session_local(session_id))

    def _close_session_local(self, session_id: str) -> dict[str, Any]:
        session = self._get_session(session_id)
        self._scheduler.cancel_conversation(session.session_id)
        with self._lock:
            self._sessions.pop(session.session_id, None)
        return {"session_id": session.session_id, "closed": True}

    def start_run(
        self,
        session_id: str,
        message: str,
        *,
        run_id: str = "",
        busy_policy: str = "APPEND",
        identity: Any = None,
    ) -> dict[str, Any]:
        del identity
        return self._call_home(lambda: self._start_run_local(session_id, message, run_id, busy_policy))

    def _start_run_local(self, session_id: str, message: str, run_id: str, busy_policy: str) -> dict[str, Any]:
        session = self._get_session(session_id)
        normalized = str(message or "").strip()
        if not normalized:
            raise RuntimeGatewayError("message must not be empty")
        try:
            policy = BusyPolicy(str(busy_policy or "APPEND").lower())
        except ValueError as exc:
            raise RuntimeGatewayError("busy_policy must be APPEND, INJECT, or INTERRUPT") from exc
        selected = str(run_id or "run_" + uuid.uuid4().hex)
        with self._lock:
            if selected in self._run_sessions:
                raise RuntimeGatewayError(f"run already exists: {selected}")
        request = TurnRequest(
            origin=Origin.USER,
            source=Source(
                channel="gateway",
                chat_id=session.session_id,
                sender_id="user",
                chat_type=ChatType.DM,
            ),
            text=normalized,
            conversation=session.session_id,
            busy=policy,
        )
        self._submit_local(session.session_id, selected, request)
        self._emit_for_conversation(session.session_id, "run.queued", {"message": normalized}, selected)
        return {"session_id": session.session_id, "run_id": selected, "status": "QUEUED"}

    def _submit_local(self, session_id: str, run_id: str, request: TurnRequest):
        handle = self._scheduler.submit(request)
        with self._lock:
            self._run_sessions[run_id] = session_id
            self._run_ids_by_conversation[session_id].append(run_id)
        asyncio.create_task(self._watch_run(session_id, run_id, handle))
        return handle

    async def _watch_run(self, session_id: str, run_id: str, handle: Any) -> None:
        outcome = await handle.result()
        if outcome is None:
            with self._lock:
                known = run_id in self._run_sessions
            if known:
                await self._hub.wait_idle("gateway")
                self._emit_for_conversation(
                    session_id,
                    "run.cancelled",
                    {"status": "CANCELLED", "answer": "", "error": "cancelled"},
                    run_id,
                )
        with self._lock:
            self._run_sessions.pop(run_id, None)
            queue = self._run_ids_by_conversation.get(session_id)
            if queue:
                try:
                    queue.remove(run_id)
                except ValueError:
                    pass
                if not queue:
                    self._run_ids_by_conversation.pop(session_id, None)

    def cancel_run(self, run_id: str, session_id: str = "") -> dict[str, Any]:
        return self._call_home(lambda: self._cancel_run_local(run_id, session_id))

    def _cancel_run_local(self, run_id: str, session_id: str = "") -> dict[str, Any]:
        selected = str(run_id or "").strip()
        if not selected:
            raise RuntimeGatewayError("run_id is required")
        with self._lock:
            owner = self._run_sessions.get(selected) or str(session_id or "").strip()
        if not owner:
            return {"session_id": "", "run_id": selected, "accepted": False}
        accepted = self._scheduler.cancel_conversation(owner) > 0
        self._emit_for_conversation(owner, "run.cancel_requested", {"reason": "remote_request"}, selected)
        return {"session_id": owner, "run_id": selected, "accepted": accepted}

    def inject_run(self, session_id: str, message: str, identity: Any = None) -> dict[str, Any]:
        return self.start_run(session_id, message, busy_policy=BusyPolicy.INJECT.value, identity=identity)

    def interrupt_run(self, session_id: str, message: str, run_id: str = "", identity: Any = None) -> dict[str, Any]:
        return self.start_run(
            session_id,
            message,
            run_id=run_id,
            busy_policy=BusyPolicy.INTERRUPT.value,
            identity=identity,
        )

    def resolve_interaction(
        self, interaction_id: str, value: Any, *, run_id: str = "", session_id: str = ""
    ) -> dict[str, Any]:
        return self._call_home(
            lambda: self._resolve_interaction_local(
                interaction_id,
                value,
                run_id=run_id,
                session_id=session_id,
            )
        )

    def _resolve_interaction_local(
        self,
        interaction_id: str,
        value: Any,
        *,
        run_id: str = "",
        session_id: str = "",
    ) -> dict[str, Any]:
        selected_id = str(interaction_id or "").strip()
        if not selected_id:
            raise RuntimeGatewayError("interaction_id is required")
        answer = "approved" if value is True else "rejected" if value is False else str(value or "")
        accepted = self._question_broker.reply(selected_id, answer)
        with self._lock:
            context = self._interaction_context.pop(selected_id, None) if accepted else None
        if accepted and context is not None:
            selected_session = str(context.get("session_id", "") or session_id)
            selected_run = str(context.get("run_id", "") or run_id)
            self._emit_for_conversation(
                selected_session,
                "interaction.resolved",
                {
                    "interaction_id": selected_id,
                    "decision": "approved" if value is True else "rejected" if value is False else "answered",
                    "reason": "" if value is not False else "user_rejected",
                },
                selected_run,
            )
        return {"interaction_id": selected_id, "accepted": accepted}

    def subscribe(self, session_id: str, callback: EventCallback) -> Callable[[], None]:
        return self._call_home(lambda: self._subscribe_local(session_id, callback))

    def _subscribe_local(self, session_id: str, callback: EventCallback) -> Callable[[], None]:
        session = self._get_session(session_id)
        subscription_id = uuid.uuid4().hex
        with self._lock:
            session.subscribers[subscription_id] = callback

        def unsubscribe() -> None:
            with self._lock:
                session.subscribers.pop(subscription_id, None)

        return unsubscribe

    def cron_create(self, session_id: str, raw: dict[str, Any]) -> dict[str, Any]:
        return self._call_home(lambda: self._cron_create_local(session_id, raw))

    def _cron_create_local(self, session_id: str, raw: dict[str, Any]) -> dict[str, Any]:
        session = self._get_session(session_id)
        values = dict(raw or {})
        expression = str(values.get("cron", "") or "").strip()
        if not expression:
            raise RuntimeGatewayError("cron expression is required")
        job = self.host.cron_service.add_job(
            str(values.get("name", values.get("id", "gateway-reminder"))),
            CronSchedule(kind="cron", expr=expression),
            str(values.get("message", "")),
            deliver=False,
            channel="gateway",
            to=session.session_id,
            topic_tag=str(values.get("topic_tag", "") or "") or None,
        )
        return {"id": job.id, "name": job.name, "session_id": session.session_id}

    def cron_list(self, session_id: str) -> dict[str, Any]:
        return self._call_home(lambda: self._cron_list_local(session_id))

    def _cron_list_local(self, session_id: str) -> dict[str, Any]:
        self._get_session(session_id)
        return {"jobs": [self._cron_public(job) for job in self.host.cron_service.list_jobs()]}

    def cron_cancel(self, session_id: str, job_id: str) -> dict[str, Any]:
        return self._call_home(lambda: self._cron_cancel_local(session_id, job_id))

    def _cron_cancel_local(self, session_id: str, job_id: str) -> dict[str, Any]:
        self._get_session(session_id)
        for job in self.host.cron_service.list_jobs(include_disabled=True):
            if job.id == job_id:
                self.host.cron_service.remove_job(job_id)
                return {"id": job_id, "status": "cancelled"}
        raise RuntimeGatewayError(f"unknown cron job: {job_id}")

    @staticmethod
    def _cron_public(job: Any) -> dict[str, Any]:
        return {
            "id": job.id,
            "name": job.name,
            "enabled": job.enabled,
            "message": job.payload.message,
            "cron": job.schedule.expr,
            "next_run_at_ms": job.state.next_run_at_ms,
        }

    def health(self) -> dict[str, Any]:
        return self._call_home(self._health_local)

    def _health_local(self) -> dict[str, Any]:
        with self._lock:
            active = len(self._run_sessions)
            sessions = len(self._sessions)
        return {
            "status": "closed" if self._closed else "ok",
            "mode": "native_pico_runtime",
            "sessions": sessions,
            "active_runs": active,
            "worker_pools": dict(self._worker_capacities),
            "automation_jobs": len(self.host.cron_service.list_jobs(include_disabled=True)),
        }

    def capabilities(self) -> list[str]:
        return [
            "gateway.auth",
            "health",
            "capabilities",
            "session.create",
            "session.resume",
            "session.close",
            "run.start",
            "run.cancel",
            "run.inject",
            "run.interrupt",
            "interaction.resolve",
            "run.subscribe",
            "cron.create",
            "cron.list",
            "cron.cancel",
        ]

    async def _sink(self, event: Any) -> None:
        conversation = str(getattr(event, "conversation_id", "") or "")
        if isinstance(event, TurnStarted):
            self._emit_for_conversation(conversation, "run_status", {"phase": "running", "label": "Running"})
            return
        if isinstance(event, TurnFailed):
            await self._hub.close_stream(conversation)
            await self._hub.wait_idle("gateway")
            name = "run.cancelled" if event.cancelled else "run.failed"
            self._emit_for_conversation(
                conversation,
                name,
                {"status": "CANCELLED" if event.cancelled else "FAILED", "answer": "", "error": event.error},
            )
            return
        if isinstance(event, TurnEnded):
            await self._hub.close_stream(conversation)
            await self._hub.wait_idle("gateway")
            answer = self._text_by_conversation.pop(conversation, "")
            self._emit_for_conversation(
                conversation, "run.completed", {"status": "COMPLETED", "answer": answer, "error": ""}
            )
            return
        await self._hub.dispatch(event)

    def _publish_deliverable(self, out: Deliverable) -> None:
        conversation = str(out.conversation_id or "")
        if isinstance(out, Text):
            self._emit_for_conversation(conversation, "assistant_message", {"text": out.content})
        elif isinstance(out, MediaOut):
            self._emit_for_conversation(
                conversation,
                "media",
                {
                    "items": [
                        {
                            "path": str(media.path),
                            "mime": str(media.mime),
                            "kind": str(media.kind),
                        }
                        for media in out.media
                    ]
                },
            )
        elif isinstance(out, ToolEvent):
            self._emit_for_conversation(
                conversation,
                "tool_result",
                {
                    "tool_name": out.name,
                    "result": out.result_preview,
                    "status": "error" if out.failed else "ok",
                    "phase": out.phase.value,
                },
            )
        elif isinstance(out, Reasoning):
            self._emit_for_conversation(conversation, "reasoning_delta", {"text": out.content})
        elif isinstance(out, Notice):
            self._emit_for_conversation(
                conversation, "run_status", {"phase": out.kind.value, "label": out.detail or ""}
            )

    def _emit_for_conversation(
        self, conversation: str, event_name: str, payload: dict[str, Any], run_id: str = ""
    ) -> None:
        with self._lock:
            queue = self._run_ids_by_conversation.get(conversation, ())
            selected_run = str(run_id or (queue[0] if queue else ""))
            session = self._sessions.get(conversation)
            callbacks = tuple(session.subscribers.values()) if session else ()
        event = {
            "event": event_name,
            "session_id": conversation,
            "run_id": selected_run,
            "payload": dict(payload or {}),
        }
        for callback in callbacks:
            try:
                callback(event)
            except Exception:
                continue

    def _get_session(self, session_id: str) -> _NativeSession:
        selected = str(session_id or "").strip()
        with self._lock:
            session = self._sessions.get(selected)
        if session is None:
            raise RuntimeGatewayError(f"unknown session: {selected}")
        return session

    def _ensure_open(self) -> None:
        if self._closed:
            raise RuntimeGatewayError("runtime gateway is closed")

    async def _send_question_frame(self, frame: dict[str, Any]) -> None:
        params = dict(frame.get("params") or {})
        conversation = str(params.get("conversation_id", "") or "")
        interaction_id = str(params.get("request_id", "") or "")
        with self._lock:
            queue = self._run_ids_by_conversation.get(conversation, ())
            run_id = queue[0] if queue else ""
            self._interaction_context[interaction_id] = {
                "session_id": conversation,
                "run_id": run_id,
                "question": str(params.get("question", "") or ""),
                "choices": list(params.get("choices") or []),
            }
        self._emit_for_conversation(
            conversation,
            "interaction.requested",
            {
                "interaction_id": interaction_id,
                "kind": "question",
                "tool_name": "ask_user",
                "args": {
                    "question": str(params.get("question", "") or ""),
                    "choices": list(params.get("choices") or []),
                },
                "question": str(params.get("question", "") or ""),
                "choices": list(params.get("choices") or []),
            },
            run_id,
        )

    async def _close_async(self) -> None:
        if self._closed:
            return
        self._closed = True
        cleanup_error: BaseException | None = None
        begin_close = getattr(self.host, "begin_close", None)
        try:
            if callable(begin_close):
                begin_close()
        except BaseException as exc:
            cleanup_error = exc
        try:
            self._question_broker.cancel_all()
        except BaseException as exc:
            cleanup_error = cleanup_error or exc
        try:
            self.host.cron_service.stop()
        except BaseException as exc:
            cleanup_error = cleanup_error or exc
        try:
            await teardown_spine(self._scheduler, self._hub, grace=0.0)
        except BaseException as exc:
            cleanup_error = cleanup_error or exc
        try:
            self.host.agent_loop.stop()
        except BaseException as exc:
            cleanup_error = cleanup_error or exc
        if self._runtime_task is not None and not self._runtime_task.done():
            try:
                await asyncio.gather(self._runtime_task, return_exceptions=True)
            except BaseException as exc:
                cleanup_error = cleanup_error or exc
        try:
            await self.host.close()
        except BaseException as exc:
            cleanup_error = cleanup_error or exc
        self._started = False
        if cleanup_error is not None:
            raise cleanup_error

    async def aclose(self) -> None:
        """Await the native teardown from the home event loop."""

        await self._close_async()

    def close(self) -> None:
        try:
            current = asyncio.get_running_loop()
        except RuntimeError:
            current = None
        if current is self._loop:
            self._loop.create_task(self._close_async())
            return
        if self._loop.is_running():
            asyncio.run_coroutine_threadsafe(self._close_async(), self._loop).result(timeout=60)
        elif not self._loop.is_closed():
            self._loop.run_until_complete(self._close_async())


__all__ = ["NativeGatewayRuntime"]
