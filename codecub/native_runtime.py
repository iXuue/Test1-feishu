"""Canonical native Runtime assembly used by CodeCub compatibility hosts.

This module is the only CodeCub production-side composition boundary.  It
translates the legacy launch arguments into Pico's typed configuration and
then delegates construction to ``pico.cli._runtime_assembly``.  The old
``codecub.runtime.Pico`` remains importable for compatibility, but production
CLI, Gateway and desktop hosts must not construct it.
"""

from __future__ import annotations

import base64
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def decode_workspace_arg(args: Any) -> str:
    """Decode the desktop-safe workspace argument without importing legacy CLI code."""

    encoded = str(getattr(args, "cwd_b64", "") or "").strip()
    if not encoded:
        return str(getattr(args, "cwd", ".") or ".")
    try:
        return base64.b64decode(encoded.encode("ascii"), validate=True).decode("utf-8")
    except Exception as exc:  # pragma: no cover - argparse boundary
        raise ValueError(f"invalid --cwd-b64: {exc}") from exc


def _load_dotenv(workspace: Path) -> None:
    """Load non-overriding ``.env`` values for the native provider path.

    The legacy loader used to live in ``codecub.cli``.  Keeping this small
    loader here prevents the canonical entry point from importing that module
    while preserving the desktop/project ``.env`` convention.
    """

    env_path = workspace / ".env"
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, separator, value = line.partition("=")
        key = key.strip()
        if not separator or not key or not (key[0].isalpha() or key[0] == "_"):
            continue
        if not all(char.isalnum() or char == "_" for char in key):
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ.setdefault(key, value)


def _apply_legacy_overrides(config: Any, args: Any) -> None:
    """Map supported CodeCub launch flags onto the native Config object."""

    defaults = config.agents.defaults
    provider = str(getattr(args, "provider", "") or "").strip().lower()
    model = str(getattr(args, "model", "") or "").strip()
    if provider:
        defaults.provider = provider
    if model:
        defaults.model = model
    if getattr(args, "max_new_tokens", None) is not None:
        defaults.max_tokens = max(1, int(args.max_new_tokens))
    if getattr(args, "max_steps", None) is not None:
        defaults.max_tool_iterations = max(1, int(args.max_steps))
    if getattr(args, "temperature", None) is not None:
        defaults.temperature = float(args.temperature)

    endpoint_name = provider or config.get_provider_name(defaults.model) or "custom"
    endpoint = getattr(config.providers, endpoint_name, None)
    if endpoint is None:
        endpoint = config.providers.custom
        defaults.provider = "custom"
    base_url = str(getattr(args, "base_url", "") or "").strip()
    host = str(getattr(args, "host", "") or "").strip()
    if base_url:
        endpoint.api_base = base_url
    elif host and endpoint_name == "ollama":
        endpoint.api_base = host

    # Native ExecTool owns the safety boundary.  The legacy approval flag is
    # accepted by the adapter for wire compatibility; it is not allowed to
    # reintroduce a second approval/runtime implementation.
    if not getattr(args, "multi_agent", False) and "spawn" not in config.tools.disabled_tools:
        config.tools.disabled_tools.append("spawn")


@dataclass
class NativeRuntimeHost:
    """The assembled native runtime plus the configuration used to create it."""

    assembly: Any
    config: Any
    pico_config: Any
    paths: Any
    cron_service: Any

    @property
    def agent_loop(self) -> Any:
        return self.assembly.agent_loop

    @property
    def session_manager(self) -> Any:
        return self.assembly.session_manager

    async def start(self) -> None:
        await self.assembly.start_memory_backend()

    def begin_close(self) -> None:
        self.assembly.begin_close()

    async def close(self) -> None:
        await self.assembly.close()


def build_native_runtime(
    args: Any,
    *,
    interactive: bool,
    cron_service: Any | None = None,
    session_manager: Any | None = None,
) -> NativeRuntimeHost:
    """Build one native RuntimeAssembly for a CodeCub host.

    No legacy agent, model client, session store, or legacy Spine is created
    here.  All hosts receive the same native ``AgentLoop`` and
    ``SessionManager`` implementation as the ``pico`` CLI/TUI/Gateway.
    """

    from pico.cli._helpers import load_runtime_config, make_provider
    from pico.cli._runtime_assembly import assemble_runtime
    from pico.config.paths import get_cron_dir, resolve_foreground_paths
    from pico.config.pico import load_pico_config
    from pico.proactive_engine.schedulers.cron.service import CronService

    workspace = Path(decode_workspace_arg(args)).expanduser().resolve()
    _load_dotenv(workspace)
    config = load_runtime_config(getattr(args, "config", None), str(workspace))
    _apply_legacy_overrides(config, args)
    paths = resolve_foreground_paths(config, workspace=str(workspace))
    pico_config = load_pico_config()
    provider = make_provider(config)
    cron = cron_service or CronService(get_cron_dir() / "jobs.json")
    assembly = assemble_runtime(
        config,
        pico_config,
        provider=provider,
        cron_service=cron,
        interactive=interactive,
        session_manager=session_manager,
        paths=paths,
    )
    return NativeRuntimeHost(
        assembly=assembly,
        config=config,
        pico_config=pico_config,
        paths=paths,
        cron_service=cron,
    )


__all__ = ["NativeRuntimeHost", "build_native_runtime", "decode_workspace_arg"]
