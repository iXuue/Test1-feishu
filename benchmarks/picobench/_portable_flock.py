"""Small cross-platform adapter for the benchmark artifact locks."""

from __future__ import annotations

try:
    import fcntl as _fcntl
except ImportError:  # pragma: no cover - exercised on Windows
    import portalocker as _portalocker

    LOCK_EX = _portalocker.LOCK_EX
    LOCK_NB = _portalocker.LOCK_NB
    LOCK_SH = _portalocker.LOCK_SH
    LOCK_UN = _portalocker.LOCK_UN

    def flock(handle, operation: int) -> None:
        # portalocker uses zero for LOCK_UN, so a bitwise test would route
        # unlock requests through lock(..., 0) and raise on Windows.
        try:
            if operation == LOCK_UN:
                _portalocker.unlock(handle)
            else:
                _portalocker.lock(handle, operation)
        except _portalocker.exceptions.AlreadyLocked as exc:
            raise BlockingIOError from exc
else:
    LOCK_EX = _fcntl.LOCK_EX
    LOCK_NB = _fcntl.LOCK_NB
    LOCK_SH = _fcntl.LOCK_SH
    LOCK_UN = _fcntl.LOCK_UN

    def flock(handle, operation: int) -> None:
        _fcntl.flock(handle.fileno() if hasattr(handle, "fileno") else handle, operation)


__all__ = ["LOCK_EX", "LOCK_NB", "LOCK_SH", "LOCK_UN", "flock"]
