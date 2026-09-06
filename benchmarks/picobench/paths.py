from __future__ import annotations

import hashlib
import os
from pathlib import Path


def storage_component(value: str) -> str:
    """Return a deterministic on-disk component that is safe on Windows."""
    # The experiment root is the main MAX_PATH contributor. Keep ordinary
    # suite/task identifiers readable unless an individual component is also
    # unusually large.
    if os.name != "nt" or len(value) <= 32:
        return value
    return hashlib.blake2s(value.encode("utf-8"), digest_size=6).hexdigest()


def experiment_root(output_root: Path, experiment_id: str) -> Path:
    """Keep logical experiment IDs while shortening their Windows directory name."""
    return Path(output_root) / storage_component(experiment_id)
