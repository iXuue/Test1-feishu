"""Durable, secret-free Maintainer state and idempotency records."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from .models import WorkflowState


def idempotency_key(*, event_id: str, repository: str, base_revision: str, command_type: str) -> str:
    raw = "\x1f".join((event_id, repository, base_revision, command_type)).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class MaintainerStateStore:
    def __init__(self, root: Path | None = None) -> None:
        configured = os.environ.get("PICO_MAINTAINER_STATE_DIR", "").strip()
        self.root = root or (Path(configured).expanduser() if configured else Path.home() / ".pico" / "maintainer-runs")

    def path_for(self, key: str) -> Path:
        return self.root / f"{key}.json"

    def load(self, key: str) -> dict[str, Any] | None:
        path = self.path_for(key)
        if not path.exists():
            return None
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"maintainer state must be an object: {path}")
        return payload

    def save(self, key: str, payload: dict[str, Any]) -> Path:
        self.root.mkdir(parents=True, exist_ok=True)
        path = self.path_for(key)
        fd, tmp_name = tempfile.mkstemp(prefix=f".{key}.", suffix=".tmp", dir=self.root)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
                json.dump(payload, handle, ensure_ascii=False, sort_keys=True, indent=2)
                handle.write("\n")
            os.replace(tmp_name, path)
        finally:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)
        return path


def transition(payload: dict[str, Any], state: WorkflowState, **fields: Any) -> dict[str, Any]:
    payload["state"] = state.value
    payload.update(fields)
    return payload


__all__ = ["MaintainerStateStore", "idempotency_key", "transition"]
