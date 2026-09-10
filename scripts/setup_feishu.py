"""Interactive setup and smoke test for the Feishu app-bot channel.

The repository already owns the Feishu WebSocket adapter and the Pico channel
configuration writer.  This script is only a safe operator-facing entry point:
it prompts for credentials locally, writes the existing user-level JSON config,
checks the optional SDK extra, and can launch the normal Gateway.

Usage::

    python scripts/setup_feishu.py
    python scripts/setup_feishu.py --test

App secrets are never printed.  They are held in memory only long enough to
write the user config or perform the local credential/WebSocket probe.
"""

from __future__ import annotations

import argparse
import asyncio
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

_SDK_SPEC = "lark-oapi>=1.5.0,<2.0.0"
_IGNORED_SECRET_PATTERNS = (".env", ".env.*", ".pico/")


def _repo_gitignore() -> Path:
    return REPO_ROOT / ".gitignore"


def _ensure_secret_files_ignored() -> bool:
    """Ensure common local-secret paths remain outside Git's tracked tree."""

    path = _repo_gitignore()
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = {line.strip() for line in existing.splitlines() if line.strip() and not line.lstrip().startswith("#")}
    missing = [pattern for pattern in _IGNORED_SECRET_PATTERNS if pattern not in lines]
    if missing:
        prefix = "" if not existing or existing.endswith(("\n", "\r")) else "\n"
        path.write_text(existing + prefix + "\n".join(missing) + "\n", encoding="utf-8")
        return True
    return False


def _sdk_installed() -> bool:
    return importlib.util.find_spec("lark_oapi") is not None


def _ensure_sdk() -> bool:
    """Install the existing optional extra when the official SDK is absent."""

    if _sdk_installed():
        return True

    uv = shutil.which("uv")
    if uv:
        command = [uv, "sync", "--extra", "channel-feishu"]
    else:
        command = [sys.executable, "-m", "pip", "install", _SDK_SPEC]

    print(f"[INFO] Feishu SDK missing; installing with {'uv' if uv else 'pip'}...")
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        print("[FAIL] Feishu SDK installation failed")
        return False
    if not _sdk_installed():
        print("[FAIL] Feishu SDK is still unavailable in the current Python environment")
        return False
    return True


def _current_feishu_config() -> Any:
    from pico.config.loader import load_config

    return load_config().channels.feishu


def _prompt_credentials() -> tuple[str, str]:
    import getpass

    current = _current_feishu_config()
    current_app_id = str(getattr(current, "app_id", "") or "")
    current_app_secret = str(getattr(current, "app_secret", "") or "")

    suffix = f" [{current_app_id}]" if current_app_id else ""
    app_id = input(f"Feishu App ID{suffix}: ").strip() or current_app_id
    if not app_id:
        raise ValueError("Feishu App ID cannot be empty")

    secret_prompt = "Feishu App Secret (press Enter to keep existing): " if current_app_secret else "Feishu App Secret: "
    app_secret = getpass.getpass(secret_prompt)
    app_secret = app_secret or current_app_secret
    if not app_secret:
        raise ValueError("Feishu App Secret cannot be empty")
    return app_id, app_secret


def _write_config(app_id: str, app_secret: str) -> Path:
    from pico.config.loader import get_config_path
    from pico.config.update_channels import enable_channel

    # Do not touch verification_token/encrypt_key: WebSocket mode does not need
    # them, and an existing operator value must survive a re-run.
    enable_channel(
        "feishu",
        {
            "app_id": app_id,
            "app_secret": app_secret,
            "group_policy": "mention",
        },
    )
    return get_config_path()


def _safe_failure(exc: BaseException, secret: str | None = None) -> str:
    """Return a diagnostic that cannot contain the supplied credential."""

    text = str(exc)
    if secret:
        text = text.replace(secret, "***")
    return text[:240] or type(exc).__name__


def _sdk_client(app_id: str, app_secret: str):
    import lark_oapi as lark

    return (
        lark.Client.builder()
        .app_id(app_id)
        .app_secret(app_secret)
        .log_level(lark.LogLevel.ERROR)
        .build()
    )


def _verify_app_credentials(app_id: str, app_secret: str) -> None:
    """Ask the official SDK for a tenant token without printing the token."""

    from lark_oapi.api.auth.v3 import InternalTenantAccessTokenRequest, InternalTenantAccessTokenRequestBody

    client = _sdk_client(app_id, app_secret)
    body = (
        InternalTenantAccessTokenRequestBody.builder()
        .app_id(app_id)
        .app_secret(app_secret)
        .build()
    )
    request = InternalTenantAccessTokenRequest.builder().request_body(body).build()
    response = client.auth.v3.tenant_access_token.internal(request)
    if not response.success():
        raise RuntimeError("Feishu credential request was rejected")


def _verify_websocket(app_id: str, app_secret: str) -> None:
    """Open and close one real SDK WebSocket connection.

    ``lark_oapi.ws.Client.start`` is intentionally a forever-running loop.  The
    SDK's connection primitive is used here so ``--test`` can prove the endpoint
    handshake without starting a second Agent/Gateway process.
    """

    import lark_oapi as lark
    import lark_oapi.ws.client as ws_client

    client = lark.ws.Client(app_id, app_secret, log_level=lark.LogLevel.ERROR)
    loop = asyncio.new_event_loop()
    previous_loop = ws_client.loop
    ws_client.loop = loop

    async def probe() -> None:
        await client._connect()  # SDK connection primitive; start() is long-running by design.
        if client._conn is None:
            raise RuntimeError("Feishu WebSocket did not expose an active connection")
        await client._disconnect()

    try:
        loop.run_until_complete(probe())
    finally:
        ws_client.loop = previous_loop
        loop.close()


def _validate_configured_channel() -> tuple[str, str]:
    config = _current_feishu_config()
    app_id = str(getattr(config, "app_id", "") or "")
    app_secret = str(getattr(config, "app_secret", "") or "")
    if not getattr(config, "enabled", False):
        raise ValueError("Feishu channel is not enabled")
    if not app_id or not app_secret:
        raise ValueError("Feishu App ID/App Secret are incomplete")
    return app_id, app_secret


def run_test() -> int:
    if not _ensure_sdk():
        return 1
    try:
        app_id, app_secret = _validate_configured_channel()
        print("[OK] App ID configured")
        print("[OK] App Secret configured")
        print("[OK] Feishu channel configuration valid")
        print("[OK] Feishu SDK installed")
        _verify_app_credentials(app_id, app_secret)
        print("[OK] App ID / App Secret accepted by Feishu")
        _verify_websocket(app_id, app_secret)
        print("[OK] Connected to Feishu")
        return 0
    except Exception as exc:
        print(f"[FAIL] Feishu connection test failed: {_safe_failure(exc, locals().get('app_secret'))}")
        return 1


def _start_gateway() -> int:
    print("[INFO] Starting the normal Pico Gateway...")
    return subprocess.run([sys.executable, "-m", "pico", "gateway"], cwd=REPO_ROOT, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Configure Pico's Feishu WebSocket channel")
    parser.add_argument("--test", action="store_true", help="Test the saved credentials and one WebSocket handshake")
    args = parser.parse_args()

    if args.test:
        return run_test()

    try:
        app_id, app_secret = _prompt_credentials()
        config_path = _write_config(app_id, app_secret)
        changed_gitignore = _ensure_secret_files_ignored()
        if changed_gitignore:
            print("[OK] Secret file ignore rules added to .gitignore")
        else:
            print("[OK] Secret file ignored by git")
        print("[OK] App ID configured")
        print("[OK] App Secret configured")
        print(f"[OK] Feishu channel configuration valid ({config_path})")
        if not _ensure_sdk():
            return 1
        print("[OK] Feishu SDK installed")
    except (KeyboardInterrupt, EOFError):
        print("\n[ABORTED] Feishu setup cancelled")
        return 1
    except Exception as exc:
        print(f"[FAIL] Feishu setup failed: {_safe_failure(exc, locals().get('app_secret'))}")
        return 1

    answer = input("Start Feishu connection now? [Y/n] ").strip().lower()
    if answer in ("", "y", "yes"):
        return _start_gateway()
    print("[INFO] Configuration saved. Start later with: python -m pico gateway")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
