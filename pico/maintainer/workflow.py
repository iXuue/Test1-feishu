"""Deterministic Feishu-to-GitHub Maintainer workflow."""

from __future__ import annotations

import asyncio
import json
import os
import subprocess
import uuid
from pathlib import Path
from typing import Any, Awaitable, Callable

from loguru import logger

from pico.spine.turn import TurnRequest

from .git import (
    MaintainerGitError,
    apply_patch,
    commit_and_push,
    create_worktree,
    current_branch,
    current_revision,
    is_clean,
    origin_url,
    parse_github_repo,
    prepare_patch,
    run_test,
)
from .github import GitHubAdapter, GitHubApiError, GitHubCredentialRequiredError
from .models import PlatformIssueRef, PlatformPullRequestRef, PlatformRepoRef, WorkflowResult, WorkflowState
from .state import MaintainerStateStore, idempotency_key, transition

Coder = Callable[[Path, str, Path], Awaitable[dict[str, Any]]]
AdapterFactory = Callable[[PlatformRepoRef], Any]
Publisher = Callable[[Path, str, str], None]
_EXTERNAL_WRITE_LOCK = asyncio.Lock()


class MaintainerWorkflow:
    """Own all repository and GitHub side effects behind one serialized workflow."""

    def __init__(
        self,
        *,
        coder: Coder,
        state_store: MaintainerStateStore | None = None,
        adapter_factory: AdapterFactory | None = None,
        publisher: Publisher = commit_and_push,
        workspace_override: Path | None = None,
        enforce_fixed_workspace: bool = True,
    ) -> None:
        self._coder = coder
        self._states = state_store or MaintainerStateStore()
        self._adapter_factory = adapter_factory or GitHubAdapter.from_env
        self._publisher = publisher
        self._workspace_override = workspace_override
        self._enforce_fixed_workspace = enforce_fixed_workspace

    async def handle(self, request: TurnRequest) -> str:
        result = await self.run(request)
        return result.message

    async def run(self, request: TurnRequest) -> WorkflowResult:
        trace_id = f"maintainer-{uuid.uuid4().hex}"
        extras = dict(request.source.extras)
        command_type = str(extras.get("maintainer_command") or "fix-e2e")
        legacy_e2e = command_type == "fix-e2e"
        description = str(extras.get("maintainer_description") or request.text).strip()
        event_id = str(extras.get("event_id") or extras.get("message_id") or "unknown-event")
        workspace = (
            self._workspace_override
            or Path(
                os.environ.get("MAINTAINER_WORKSPACE")
                or os.environ.get("MAINTAINER_E2E_WORKSPACE")
                or r"D:\Test1-main"
            ).expanduser()
        ).resolve()
        run_root = self._states.root / trace_id
        run_root.mkdir(parents=True, exist_ok=True)
        trace: dict[str, Any] = {
            "trace_id": trace_id,
            "feishu_event_id": event_id,
            "feishu_message_id": extras.get("message_id"),
            "feishu_chat_id": request.source.chat_id,
            "session_id": request.conversation or f"{request.source.channel}:{request.source.chat_id}",
            "turn_id": trace_id,
            "command_type": command_type,
            "workspace": str(workspace),
            "tool_calls": [],
            "test_command": "python -m pytest -q",
            "delivery_state": "reply_queued",
        }

        def blocked(code: str, detail: str) -> WorkflowResult:
            trace.update({"final_state": WorkflowState.BLOCKED.value, "blocked_code": code, "blocked_detail": detail})
            self._write_trace(run_root, trace)
            status = "FEISHU_TO_GITHUB_E2E_NOT_ACCEPTED" if legacy_e2e else "GITHUB_ISSUE_NOT_ACCEPTED"
            return WorkflowResult(
                WorkflowState.BLOCKED,
                f"{status}\nblocked={code}\ndetail={detail}",
                trace_id,
                details=trace,
            )

        if legacy_e2e and os.environ.get("E2E_TEST_MODE", "").lower() != "true":
            return blocked("E2E_TEST_MODE_REQUIRED", "set E2E_TEST_MODE=true in the local Gateway environment")
        if legacy_e2e and self._enforce_fixed_workspace and workspace != Path(r"D:\Test1-main").resolve():
            return blocked("INVALID_E2E_WORKSPACE", f"workspace must be D:\\Test1-main, got {workspace}")
        if not description:
            return blocked(
                "EMPTY_FIX_DESCRIPTION" if legacy_e2e else "EMPTY_ISSUE_DESCRIPTION",
                "the /fix-e2e command needs a bug description"
                if legacy_e2e
                else "the /issue command needs a problem description",
            )

        try:
            if not (workspace / ".git").exists():
                return blocked("WORKSPACE_NOT_A_GIT_REPOSITORY", str(workspace))
            if current_branch(workspace) != "main":
                return blocked("INVALID_BASE_BRANCH", current_branch(workspace) or "detached")
            if not is_clean(workspace):
                return blocked("DIRTY_BASE_WORKTREE", "main worktree must be clean before the run")
            base_revision = current_revision(workspace)
            remote = origin_url(workspace)
            owner, repo = parse_github_repo(remote)
        except (MaintainerGitError, OSError) as exc:
            return blocked("BASE_REVISION_UNAVAILABLE", str(exc))

        repo_ref = PlatformRepoRef("github", owner, repo, f"https://github.com/{owner}/{repo}")
        key = idempotency_key(
            event_id=event_id,
            repository=repo_ref.full_name,
            base_revision=base_revision,
            command_type=command_type,
        )
        trace.update({"github_repo": repo_ref.full_name, "base_revision": base_revision, "idempotency_key": key})
        old = self._states.load(key)
        # candidate_ready is only the permission boundary for external writes;
        # it is not an accepted terminal state. A retry must continue through
        # the guarded workflow instead of claiming that a PR already exists.
        if old and old.get("state") == WorkflowState.PR_CREATED.value:
            return self._result_from_state(old, trace_id)
        self._states.save(key, transition(trace.copy(), WorkflowState.RECEIVED))

        try:
            adapter = self._adapter_factory(repo_ref)
        except GitHubCredentialRequiredError:
            return blocked("GITHUB_CREDENTIAL_REQUIRED", "configure GITHUB_PERSONAL_ACCESS_TOKEN locally")

        async with _EXTERNAL_WRITE_LOCK:
            try:
                metadata = await adapter.get_repository()
                full_name = str(metadata.get("full_name", ""))
                if full_name.lower() != repo_ref.full_name.lower():
                    return blocked("GITHUB_REPOSITORY_MISMATCH", full_name or "unknown")
                if legacy_e2e and (not bool(metadata.get("fork")) or not metadata.get("parent")):
                    return blocked("GITHUB_FORK_REQUIRED", repo_ref.full_name)

                old_issue = self._issue_from_state(old or {})
                issue = old_issue or await adapter.find_issue_by_marker(key)
                if issue is None:
                    issue = await adapter.create_issue(
                        title=f"[Maintainer] {description[:120]}",
                        body=self._issue_body(trace, description, base_revision, key),
                    )
                trace.update({"github_issue_number": issue.issue_number, "github_issue_url": issue.url})
                self._states.save(key, transition(trace.copy(), WorkflowState.ISSUE_CREATED))

                repair = run_root / "repair-worktree"
                verifier = run_root / "verifier-worktree"
                candidate = run_root / "candidate-worktree"
                create_worktree(workspace, repair, base_revision)
                trace["repair_worktree"] = str(repair)
                self._states.save(key, transition(trace.copy(), WorkflowState.REPAIRING))

                prompt = self._repair_prompt(description, issue)
                coder_result = await self._coder(repair, prompt, run_root / "agent-state")
                trace["coder_result"] = {"reply": str(coder_result.get("reply", ""))[:2000]}
                trace["tool_calls"] = list(coder_result.get("tool_calls") or [])
                repair_test = run_test(repair)
                trace["repair_test_exit_code"] = repair_test.returncode
                trace["repair_test_output"] = (repair_test.stdout + repair_test.stderr)[-4000:]
                if repair_test.returncode != 0:
                    return self._failed(
                        key,
                        run_root,
                        trace,
                        WorkflowState.VERIFICATION_FAILED,
                        f"repair tests failed with exit code {repair_test.returncode}",
                        issue=issue,
                    )

                patch, changed_files = prepare_patch(repair, base_revision)
                patch_path = run_root / "repair.patch"
                patch_path.write_text(patch, encoding="utf-8")
                trace.update({"patch": str(patch_path), "changed_files": changed_files})
                self._states.save(key, transition(trace.copy(), WorkflowState.VERIFYING))

                create_worktree(workspace, verifier, base_revision)
                trace["verifier_worktree"] = str(verifier)
                apply_patch(verifier, patch)
                verifier_test = run_test(verifier)
                trace["verification_exit_code"] = verifier_test.returncode
                trace["verification_output"] = (verifier_test.stdout + verifier_test.stderr)[-4000:]
                if verifier_test.returncode != 0:
                    return self._failed(
                        key,
                        run_root,
                        trace,
                        WorkflowState.VERIFICATION_FAILED,
                        f"verifier tests failed with exit code {verifier_test.returncode}",
                        issue=issue,
                    )
                self._states.save(key, transition(trace.copy(), WorkflowState.CANDIDATE_READY))

                branch = f"agent/fix-issue-{issue.issue_number}"
                create_worktree(workspace, candidate, base_revision, branch=branch)
                apply_patch(candidate, patch)
                self._publisher(candidate, branch, f"fix: resolve issue #{issue.issue_number}")
                trace.update({"branch": branch, "base_branch": "main", "head_branch": branch})
                pr = await adapter.find_pull_request(head=branch, base="main")
                if pr is None:
                    pr = await adapter.create_pull_request(
                        title=f"Fix #{issue.issue_number}: {description[:100]}",
                        body=self._pr_body(trace, issue),
                        head=branch,
                        base="main",
                    )
                trace.update({"github_pr_number": pr.pr_number, "github_pr_url": pr.url, "final_state": WorkflowState.PR_CREATED.value})
                comment_marker = f"<!-- pico-maintainer-resolution:{key} -->"
                if not await adapter.find_issue_comment_by_marker(issue.issue_number, comment_marker):
                    await adapter.comment_issue(
                        issue.issue_number,
                        self._resolution_comment(trace, description, issue, pr, comment_marker),
                    )
                trace.update(
                    {
                        "github_issue_resolution_marker": comment_marker,
                        "github_issue_resolution_commented": True,
                    }
                )
                self._states.save(key, transition(trace.copy(), WorkflowState.PR_CREATED))
                self._write_trace(run_root, trace)
                return WorkflowResult(
                    WorkflowState.PR_CREATED,
                    self._success_message(trace, issue, pr),
                    trace_id,
                    issue=issue,
                    pull_request=pr,
                    details=trace,
                )
            except (GitHubApiError, MaintainerGitError, subprocess.TimeoutExpired, OSError) as exc:
                logger.warning("Maintainer workflow blocked: {}", exc)
                return self._failed(key, run_root, trace, WorkflowState.BLOCKED, str(exc))
            finally:
                close = getattr(adapter, "close", None)
                if close is not None:
                    result = close()
                    if hasattr(result, "__await__"):
                        await result

    def _failed(
        self,
        key: str,
        run_root: Path,
        trace: dict[str, Any],
        state: WorkflowState,
        message: str,
        *,
        issue: PlatformIssueRef | None = None,
    ) -> WorkflowResult:
        trace["final_state"] = state.value
        trace["failure"] = message
        self._states.save(key, transition(trace.copy(), state))
        self._write_trace(run_root, trace)
        status = "FEISHU_TO_GITHUB_E2E_NOT_ACCEPTED" if trace.get("command_type") == "fix-e2e" else "GITHUB_ISSUE_NOT_ACCEPTED"
        return WorkflowResult(
            state,
            f"{status}\nstate={state.value}\ndetail={message}",
            str(trace["trace_id"]),
            issue=issue,
            details=trace,
        )

    def _result_from_state(self, old: dict[str, Any], trace_id: str) -> WorkflowResult:
        issue = self._issue_from_state(old)
        pr = self._pr_from_state(old)
        state = WorkflowState(str(old.get("state", WorkflowState.BLOCKED.value)))
        return WorkflowResult(state, self._success_message(old, issue, pr), trace_id, issue=issue, pull_request=pr, details=old)

    @staticmethod
    def _issue_from_state(payload: dict[str, Any]) -> PlatformIssueRef | None:
        number = payload.get("github_issue_number")
        url = payload.get("github_issue_url")
        if not number or not url:
            return None
        owner, repo = str(payload.get("github_repo", "/")).split("/", 1)
        return PlatformIssueRef("github", owner, repo, int(number), str(url))

    @staticmethod
    def _pr_from_state(payload: dict[str, Any]) -> PlatformPullRequestRef | None:
        number = payload.get("github_pr_number")
        url = payload.get("github_pr_url")
        if not number or not url:
            return None
        owner, repo = str(payload.get("github_repo", "/")).split("/", 1)
        return PlatformPullRequestRef("github", owner, repo, int(number), str(url))

    @staticmethod
    def _issue_body(trace: dict[str, Any], description: str, base_revision: str, marker: str) -> str:
        return "\n".join(
            [
                "Created by Pico Maintainer Coding Agent.",
                "",
                f"Request: {description}",
                f"Trace ID: {trace['trace_id']}",
                f"Feishu event ID: {trace['feishu_event_id']}",
                f"Base revision: `{base_revision}`",
                f"Idempotency marker: `{marker}`",
            ]
        )

    @staticmethod
    def _repair_prompt(description: str, issue: PlatformIssueRef) -> str:
        return (
            "You are the repair agent for a Maintainer workflow. Work only in the current workspace.\n"
            "Do not create commits, branches, issues, pull requests, or network calls.\n"
            "Inspect the existing code and tests, reproduce the issue, make the smallest correct change, "
            "and run `python -m pytest -q` before finishing.\n\n"
            f"GitHub Issue: {issue.url}\nProblem: {description}\n"
        )

    @staticmethod
    def _pr_body(trace: dict[str, Any], issue: PlatformIssueRef) -> str:
        return "\n".join(
            [
                f"Fixes #{issue.issue_number}",
                "",
                f"Trace ID: `{trace['trace_id']}`",
                f"Changed files: {', '.join(trace.get('changed_files', [])) or '(none)' }",
                f"Repair test exit code: `{trace.get('repair_test_exit_code')}`",
                f"Verifier exit code: `{trace.get('verification_exit_code')}`",
            ]
        )

    @staticmethod
    def _resolution_comment(
        trace: dict[str, Any],
        description: str,
        issue: PlatformIssueRef,
        pr: PlatformPullRequestRef,
        marker: str,
    ) -> str:
        files = ", ".join(trace.get("changed_files", [])) or "(none)"
        return "\n".join(
            [
                marker,
                "已修改。",
                "",
                f"问题：{description}",
                f"修改文件：{files}",
                f"测试：{trace.get('test_command', 'python -m pytest -q')} "
                f"(repair={trace.get('repair_test_exit_code')}, verifier={trace.get('verification_exit_code')})",
                f"Pull Request：{pr.url}",
                f"Trace ID：{trace['trace_id']}",
            ]
        )

    @staticmethod
    def _success_message(trace: dict[str, Any], issue: PlatformIssueRef | dict[str, Any] | None, pr: PlatformPullRequestRef | dict[str, Any] | None) -> str:
        issue_url = issue.url if isinstance(issue, PlatformIssueRef) else str((issue or {}).get("github_issue_url", ""))
        pr_url = pr.url if isinstance(pr, PlatformPullRequestRef) else str((pr or {}).get("github_pr_url", ""))
        files = ", ".join(trace.get("changed_files", [])) or "(none)"
        status = "FEISHU_TO_GITHUB_E2E_ACCEPTED" if trace.get("command_type") == "fix-e2e" else "GITHUB_ISSUE_FIXED"
        return "\n".join(
            [
                status,
                "已修改",
                f"Issue: {issue_url}",
                f"PR: {pr_url}",
                f"Changed files: {files}",
                f"Test: {trace.get('test_command', 'python -m pytest -q')} (repair={trace.get('repair_test_exit_code')}, verifier={trace.get('verification_exit_code')})",
                f"Final state: {trace.get('final_state', WorkflowState.PR_CREATED.value)}",
                f"Trace: {trace.get('trace_id')}",
            ]
        )

    @staticmethod
    def _write_trace(run_root: Path, trace: dict[str, Any]) -> None:
        (run_root / "trace.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


__all__ = ["MaintainerWorkflow"]
