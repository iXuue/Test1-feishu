"""Official CodeCub entry point backed by Pico's native RuntimeAssembly."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from .native_app_mode import run_native_app_mode
from .native_gateway import NativeGatewayRuntime
from .native_runtime import build_native_runtime, decode_workspace_arg


def build_native_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="CodeCub native Pico Runtime entry point.",
    )
    parser.add_argument("prompt", nargs="*", help="Optional one-shot prompt.")
    parser.add_argument("--cwd", default=".", help="Workspace directory.")
    parser.add_argument("--cwd-b64", default="", help="UTF-8 base64 encoded workspace directory.")
    parser.add_argument("--config", default=None, help="Pico config file path.")
    parser.add_argument("--provider", default=None, help="Native Pico provider name.")
    parser.add_argument("--model", default=None, help="Model name override.")
    parser.add_argument("--host", default=None, help="Ollama endpoint.")
    parser.add_argument("--base-url", default=None, help="Provider API base URL.")
    parser.add_argument("--connection-profile-b64", default="", help="Desktop connection metadata.")
    parser.add_argument("--resume", default=None, help="Session id to resume or latest.")
    parser.add_argument("--approval", choices=("ask", "auto", "never"), default="ask")
    parser.add_argument("--secret-env-name", dest="secret_env_names", action="append", default=[])
    parser.add_argument("--max-steps", type=int, default=None)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--multi-agent", action="store_true")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--app-mode", action="store_true")
    parser.add_argument("--json-events", dest="app_mode", action="store_true")
    parser.add_argument("--doctor", action="store_true")
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--gateway", action="store_true")
    parser.add_argument("--gateway-host", default="127.0.0.1")
    parser.add_argument("--gateway-port", type=int, default=0)
    parser.add_argument("--gateway-token", default=None)
    parser.add_argument("--gateway-allow-unauthenticated", action="store_true")
    parser.add_argument("--version", action="store_true")
    return parser


def _session_key(host: Any, requested: str | None) -> str:
    manager = host.session_manager
    value = str(requested or "").strip()
    if not value:
        return "cli:direct"
    if value == "latest":
        recent = manager.find_most_recent_chat_id("cli")
        return f"cli:{recent or 'direct'}"
    resolved = manager.resolve_key(value)
    if resolved.status == "resolved" and resolved.key:
        return resolved.key
    return value if ":" in value else f"cli:{value}"


async def _run_native_prompt(args: Any) -> int:
    from pico.agent.spine_runner import AgentTurnRunner
    from pico.spine import ChatType, Origin, OriginPools, Scheduler, Source, Text, TurnRequest
    from pico.spine.delivery import Capabilities, DeliveryHub
    from pico.spine.teardown import teardown_spine

    host = build_native_runtime(args, interactive=False)
    session_id = _session_key(host, getattr(args, "resume", None))
    host.session_manager.get_or_create(session_id)
    answer_parts: list[str] = []

    class _CliOutlet:
        name = "cli"
        capabilities = Capabilities()

        async def deliver(self, out):
            if isinstance(out, Text):
                answer_parts.append(out.content)

    hub = DeliveryHub()
    hub.register(_CliOutlet())

    async def sink(event):
        if not isinstance(event, (type(None),)):
            if not hasattr(event, "source"):
                return
            await hub.dispatch(event)

    scheduler = Scheduler(AgentTurnRunner(host.agent_loop, stream=False), OriginPools(user=1, system=1), sink)
    try:
        await host.start()
        handle = scheduler.submit(
            TurnRequest(
                origin=Origin.USER,
                source=Source(channel="cli", chat_id="direct", sender_id="user", chat_type=ChatType.DM),
                text=" ".join(args.prompt).strip(),
                conversation=session_id,
            )
        )
        outcome = await handle.result()
        await hub.wait_idle("cli")
        if outcome is None:
            return 1
        print("".join(answer_parts))
        return 0
    finally:
        host.begin_close()
        await teardown_spine(scheduler, hub, grace=0.0)
        await host.close()


async def _run_native_repl(args: Any) -> int:
    from pico.cli._repl_spine import build_repl
    from pico.spine import ChatType, Origin, Source, TurnRequest

    host = build_native_runtime(args, interactive=True)
    session_id = _session_key(host, getattr(args, "resume", None))
    host.session_manager.get_or_create(session_id)
    channel, _, chat_id = session_id.partition(":")
    channel = channel or "cli"
    chat_id = chat_id or "direct"

    async def run() -> None:
        scheduler = None
        hub = None
        teardown = None
        runtime_task = None
        try:
            await host.start()
            scheduler, hub, teardown = build_repl(
                host.agent_loop,
                channel,
                print,
                render_notice=lambda text: print(f"  - {text}"),
                render_error=lambda text: print(text, file=sys.stderr),
                send_progress=True,
                send_tool_hints=True,
            )
            host.agent_loop.subagents.set_submit(scheduler.submit)
            runtime_task = asyncio.create_task(host.agent_loop.run())
            print("CodeCub native Pico Runtime (type exit to quit)")
            while True:
                try:
                    text = await asyncio.to_thread(input, "\ncodecub> ")
                except (EOFError, KeyboardInterrupt):
                    break
                if text.strip().lower() in {"exit", "quit", ":q"}:
                    break
                if not text.strip():
                    continue
                handle = scheduler.submit(
                    TurnRequest(
                        origin=Origin.USER,
                        source=Source(channel=channel, chat_id=chat_id, sender_id="user", chat_type=ChatType.DM),
                        text=text,
                        conversation=session_id,
                    )
                )
                await handle.result()
                await hub.wait_idle(channel)
        finally:
            host.begin_close()
            if teardown is not None:
                await teardown()
            host.agent_loop.stop()
            if runtime_task is not None:
                await asyncio.gather(runtime_task, return_exceptions=True)
            await host.close()

    await run()
    return 0


def _run_native_doctor(args: Any) -> int:
    from pico.cli._helpers import load_runtime_config

    try:
        workspace = Path(decode_workspace_arg(args)).expanduser().resolve()
        config = load_runtime_config(getattr(args, "config", None), str(workspace))
        model = str(getattr(args, "model", "") or config.agents.defaults.model)
        if getattr(args, "model", None):
            config.agents.defaults.model = args.model
        if getattr(args, "provider", None):
            config.agents.defaults.provider = args.provider
        result = {
            "healthy": True,
            "provider": config.get_provider_name(model),
            "model": model,
            "workspace": str(workspace),
            "native_runtime": True,
        }
    except Exception as exc:
        result = {"healthy": False, "native_runtime": True, "error": str(exc)}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result.get("healthy") else 1


def _run_native_gateway(args: Any) -> int:
    from .gateway import GatewayServer

    token = str(getattr(args, "gateway_token", None) or "").strip() or None
    host = build_native_runtime(args, interactive=True)

    async def serve() -> None:
        runtime = NativeGatewayRuntime(host)
        server = None
        try:
            await runtime.start()
            server = GatewayServer(
                runtime,
                host=str(getattr(args, "gateway_host", "127.0.0.1")),
                port=int(getattr(args, "gateway_port", 0)),
                auth_token=token,
                allow_unauthenticated=bool(getattr(args, "gateway_allow_unauthenticated", False)),
            )
            bound_host, bound_port = await server.start()
            print(json.dumps({"gateway": "ready", "host": bound_host, "port": bound_port}, sort_keys=True), flush=True)
            await server.serve_forever()
        finally:
            if server is not None:
                await server.close()
            await runtime.aclose()

    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        return 0
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_native_arg_parser().parse_args(argv)
    if args.version:
        from pico import __version__

        print(f"CodeCub native Pico Runtime {__version__}")
        return 0
    if args.probe and not args.doctor:
        raise SystemExit("--probe requires --doctor")
    if args.doctor:
        return _run_native_doctor(args)
    if args.gateway:
        return _run_native_gateway(args)
    if args.app_mode:
        return run_native_app_mode(args)
    if args.prompt:
        return asyncio.run(_run_native_prompt(args))
    return asyncio.run(_run_native_repl(args))


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["build_native_arg_parser", "main"]
