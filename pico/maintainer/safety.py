"""Maintainer-facing normalization of Pico Tool effects."""

from __future__ import annotations

from enum import StrEnum

from pico.agent.tools.execution import ToolEffect


class MaintainerToolClass(StrEnum):
    READ_ONLY = "READ_ONLY"
    LOCAL_WRITE = "LOCAL_WRITE"
    EXTERNAL_WRITE = "EXTERNAL_WRITE"


def classify_effect(effect: ToolEffect) -> MaintainerToolClass:
    if effect is ToolEffect.READ:
        return MaintainerToolClass.READ_ONLY
    if effect is ToolEffect.EXTERNAL:
        return MaintainerToolClass.EXTERNAL_WRITE
    return MaintainerToolClass.LOCAL_WRITE


def external_write_allowed(*, candidate_ready: bool, speculative: bool = False) -> bool:
    """External repository writes are legal only after independent verification."""

    return candidate_ready and not speculative


__all__ = ["MaintainerToolClass", "classify_effect", "external_write_allowed"]
