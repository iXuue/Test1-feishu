"""Repository platform adapter boundary."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Protocol

from .models import PlatformIssueRef, PlatformPullRequestRef


class RepoPlatformAdapter(Protocol):
    """The only interface the Maintainer workflow uses for repository APIs."""

    async def get_repository(self) -> Mapping[str, Any]: ...

    async def find_issue_by_marker(self, marker: str) -> PlatformIssueRef | None: ...

    async def create_issue(self, *, title: str, body: str) -> PlatformIssueRef: ...

    async def get_issue(self, issue_number: int) -> PlatformIssueRef: ...

    async def comment_issue(self, issue_number: int, body: str) -> None: ...

    async def create_pull_request(
        self,
        *,
        title: str,
        body: str,
        head: str,
        base: str,
    ) -> PlatformPullRequestRef: ...

    async def get_pull_request(self, pr_number: int) -> PlatformPullRequestRef: ...

    async def find_pull_request(self, *, head: str, base: str) -> PlatformPullRequestRef | None: ...


__all__ = ["RepoPlatformAdapter"]
