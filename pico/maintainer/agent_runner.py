"""Run the existing Pico AgentLoop against a repair worktree."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pico.config.paths import RuntimePaths
from pico.spine.events import Text, ToolEvent
from pico.spine.message import ChatType, Source
from pico.spine.turn import Origin, TurnRequest


class AgentLoopCoder:
    """Factory-backed coder that reuses Pico Runtime and Tool contracts."""

    def __init__(self, config: Any, pico_config: Any, *, provider: Any, router: Any = None) -> None:
        self.config = config
        self.pico_config = pico_config
        self.provider = provider
        self.router = router

    async def __call__(self, worktree: Path, prompt: str, state_dir: Path) -> dict[str, Any]:
        from pico.cli._runtime_assembly import assemble_runtime

        disabled = set(self.config.tools.disabled_tools)
        disabled.update({"message", "spawn", "ask_user", "cron", "web_search", "web_fetch", "tool_search", "tool_call"})
        safe_tools = self.config.tools.model_copy(
            update={"restrict_to_workspace": True, "disabled_tools": sorted(disabled), "mcp_servers": {}}
        )
        safe_config = self.config.model_copy(
            update={"workspace_path": str(worktree), "tools": safe_tools}
        )
        runtime = assemble_runtime(
            safe_config,
            self.pico_config,
            provider=self.provider,
            cron_service=None,
            router=self.router,
            interactive=False,
            paths=RuntimePaths(workspace=worktree, state=state_dir),
        )
        text_sink: dict[str, str] = {}
        tool_calls: list[dict[str, Any]] = []
        try:
            await runtime.start_memory_backend()
            source = Source(
                channel="maintainer",
                chat_id=worktree.name,
                sender_id="pico-maintainer",
                chat_type=ChatType.DM,
                extras={"maintainer": True},
            )
            request = TurnRequest(
                origin=Origin.USER,
                source=source,
                text=prompt,
                conversation=f"maintainer:{worktree.name}",
            )

            async def emit(event: Any) -> None:
                if isinstance(event, Text) and event.content:
                    text_sink["text"] = event.content
                elif isinstance(event, ToolEvent):
                    tool_calls.append(
                        {
                            "phase": event.phase.value,
                            "name": event.name,
                            "failed": event.failed,
                        }
                    )

            await runtime.agent_loop.run_turn(request, emit, lambda: [], stream=False, text_sink=text_sink)
            return {"reply": text_sink.get("text", ""), "tool_calls": tool_calls}
        finally:
            await runtime.close()


__all__ = ["AgentLoopCoder"]
