"""Transport-neutral Gateway runtime contract shared by legacy and native hosts."""

from __future__ import annotations


class RuntimeGatewayError(RuntimeError):
    """A Gateway command cannot be fulfilled by its selected runtime host."""


__all__ = ["RuntimeGatewayError"]
