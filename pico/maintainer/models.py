"""Stable Maintainer domain values shared by adapters and workflow code."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class WorkflowState(StrEnum):
    RECEIVED = "received"
    ISSUE_CREATED = "issue_created"
    REPAIRING = "repairing"
    VERIFYING = "verifying"
    CANDIDATE_READY = "candidate_ready"
    PR_CREATED = "pr_created"
    VERIFICATION_FAILED = "verification_failed"
    BLOCKED = "blocked"
    DELIVERY_FAILED = "delivery_failed"


@dataclass(frozen=True)
class PlatformRepoRef:
    platform: str
    owner: str
    repo: str
    url: str

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.repo}"


@dataclass(frozen=True)
class PlatformIssueRef:
    platform: str
    owner: str
    repo: str
    issue_number: int
    url: str


@dataclass(frozen=True)
class PlatformPullRequestRef:
    platform: str
    owner: str
    repo: str
    pr_number: int
    url: str


@dataclass
class WorkflowResult:
    state: WorkflowState
    message: str
    trace_id: str
    issue: PlatformIssueRef | None = None
    pull_request: PlatformPullRequestRef | None = None
    details: dict[str, Any] = field(default_factory=dict)


def ref_to_dict(ref: PlatformRepoRef | PlatformIssueRef | PlatformPullRequestRef | None) -> dict[str, Any] | None:
    if ref is None:
        return None
    return {
        key: value
        for key, value in {
            "platform": ref.platform,
            "owner": ref.owner,
            "repo": ref.repo,
            "issue_number": getattr(ref, "issue_number", None),
            "pr_number": getattr(ref, "pr_number", None),
            "url": ref.url,
        }.items()
        if value is not None
    }


__all__ = [
    "PlatformIssueRef",
    "PlatformPullRequestRef",
    "PlatformRepoRef",
    "WorkflowResult",
    "WorkflowState",
    "ref_to_dict",
]
