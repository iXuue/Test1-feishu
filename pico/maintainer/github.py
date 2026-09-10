"""GitHub REST implementation of the repository platform adapter."""

from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any

import httpx

from .models import PlatformIssueRef, PlatformPullRequestRef, PlatformRepoRef


class GitHubCredentialRequiredError(RuntimeError):
    code = "GITHUB_CREDENTIAL_REQUIRED"

    def __init__(self) -> None:
        super().__init__(self.code)


class GitHubApiError(RuntimeError):
    def __init__(self, method: str, path: str, status: int, message: str) -> None:
        self.method = method
        self.path = path
        self.status = status
        super().__init__(f"GitHub API {method} {path} failed with HTTP {status}: {message}")


class GitHubAdapter:
    """Small, typed REST adapter with no GitHub calls outside this module."""

    platform = "github"

    def __init__(
        self,
        repo: PlatformRepoRef,
        token: str,
        *,
        api_base: str = "https://api.github.com",
        client: httpx.AsyncClient | None = None,
    ) -> None:
        if not token:
            raise GitHubCredentialRequiredError()
        self.repo = repo
        self._token = token
        self._owns_client = client is None
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        self._client = client or httpx.AsyncClient(
            base_url=api_base.rstrip("/"),
            headers=headers,
            timeout=30.0,
        )
        if client is not None:
            self._client.headers.update(headers)

    @classmethod
    def from_env(cls, repo: PlatformRepoRef, *, client: httpx.AsyncClient | None = None) -> "GitHubAdapter":
        token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN", "").strip()
        if not token:
            raise GitHubCredentialRequiredError()
        return cls(repo, token, client=client)

    async def close(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        response = await self._client.request(method, path, **kwargs)
        if response.is_error:
            try:
                payload = response.json()
                message = str(payload.get("message", "request failed"))
            except ValueError:
                message = "request failed"
            raise GitHubApiError(method, path, response.status_code, message)
        if not response.content:
            return {}
        payload = response.json()
        return payload

    def _repo_path(self) -> str:
        return f"/repos/{self.repo.owner}/{self.repo.repo}"

    async def get_repository(self) -> Mapping[str, Any]:
        return await self._request("GET", self._repo_path())

    async def find_issue_by_marker(self, marker: str) -> PlatformIssueRef | None:
        payload = await self._request("GET", f"{self._repo_path()}/issues", params={"state": "all", "per_page": 100})
        items = payload if isinstance(payload, list) else []
        for item in items:
            if item.get("pull_request") or marker not in str(item.get("body", "")):
                continue
            return PlatformIssueRef(
                self.platform,
                self.repo.owner,
                self.repo.repo,
                int(item["number"]),
                str(item["html_url"]),
            )
        return None

    async def create_issue(self, *, title: str, body: str) -> PlatformIssueRef:
        payload = await self._request("POST", f"{self._repo_path()}/issues", json={"title": title, "body": body})
        return PlatformIssueRef(
            self.platform,
            self.repo.owner,
            self.repo.repo,
            int(payload["number"]),
            str(payload["html_url"]),
        )

    async def get_issue(self, issue_number: int) -> PlatformIssueRef:
        payload = await self._request("GET", f"{self._repo_path()}/issues/{issue_number}")
        return PlatformIssueRef(
            self.platform,
            self.repo.owner,
            self.repo.repo,
            int(payload["number"]),
            str(payload["html_url"]),
        )

    async def comment_issue(self, issue_number: int, body: str) -> None:
        await self._request("POST", f"{self._repo_path()}/issues/{issue_number}/comments", json={"body": body})

    async def find_issue_comment_by_marker(self, issue_number: int, marker: str) -> bool:
        payload = await self._request(
            "GET",
            f"{self._repo_path()}/issues/{issue_number}/comments",
            params={"per_page": 100},
        )
        items = payload if isinstance(payload, list) else []
        return any(marker in str(item.get("body", "")) for item in items)

    async def create_pull_request(
        self,
        *,
        title: str,
        body: str,
        head: str,
        base: str,
    ) -> PlatformPullRequestRef:
        payload = await self._request(
            "POST",
            f"{self._repo_path()}/pulls",
            json={"title": title, "body": body, "head": head, "base": base},
        )
        return PlatformPullRequestRef(
            self.platform,
            self.repo.owner,
            self.repo.repo,
            int(payload["number"]),
            str(payload["html_url"]),
        )

    async def get_pull_request(self, pr_number: int) -> PlatformPullRequestRef:
        payload = await self._request("GET", f"{self._repo_path()}/pulls/{pr_number}")
        return PlatformPullRequestRef(
            self.platform,
            self.repo.owner,
            self.repo.repo,
            int(payload["number"]),
            str(payload["html_url"]),
        )

    async def find_pull_request(self, *, head: str, base: str) -> PlatformPullRequestRef | None:
        payload = await self._request("GET", f"{self._repo_path()}/pulls", params={"state": "all", "per_page": 100})
        items = payload if isinstance(payload, list) else []
        for item in items:
            head_ref = (item.get("head") or {}).get("ref")
            base_ref = (item.get("base") or {}).get("ref")
            if head_ref != head or base_ref != base:
                continue
            return PlatformPullRequestRef(
                self.platform,
                self.repo.owner,
                self.repo.repo,
                int(item["number"]),
                str(item["html_url"]),
            )
        return None


__all__ = ["GitHubAdapter", "GitHubApiError", "GitHubCredentialRequiredError"]
