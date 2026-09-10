from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from pico.agent.tools.execution import ToolEffect
from pico.cli._gateway_spine import GatewayTurnRunner
from pico.maintainer.git import parse_github_repo, run_git
from pico.maintainer.github import GitHubAdapter, GitHubCredentialRequiredError
from pico.maintainer.models import PlatformIssueRef, PlatformPullRequestRef, PlatformRepoRef, WorkflowState
from pico.maintainer.safety import MaintainerToolClass, classify_effect, external_write_allowed
from pico.maintainer.state import MaintainerStateStore, idempotency_key, transition
from pico.maintainer.workflow import MaintainerWorkflow
from pico.spine.message import ChatType, Source
from pico.spine.turn import Origin, TurnRequest


@pytest.mark.asyncio
async def test_issue_command_is_routed_to_maintainer_handler() -> None:
    calls = []

    class AgentMustNotRun:
        async def run_turn(self, *_args, **_kwargs):
            raise AssertionError("issue command must bypass the normal AgentLoop")

    async def maintainer_handler(request):
        calls.append(request)
        return "GITHUB_ISSUE_FIXED"

    runner = GatewayTurnRunner(
        AgentMustNotRun(),
        readback_texts={},
        sources={},
        maintainer_handler=maintainer_handler,
    )
    emitted = []
    request = TurnRequest(
        origin=Origin.USER,
        source=Source(
            channel="feishu",
            chat_id="oc_test",
            sender_id="ou_test",
            chat_type=ChatType.GROUP,
            extras={"maintainer_command": "issue"},
        ),
        text="README 增加一行 hello github",
        message_id="msg-test",
    )

    async def emit(event):
        emitted.append(event)

    outcome = await runner.run(request, emit, lambda: [])

    assert calls == [request]
    assert emitted[0].content == "GITHUB_ISSUE_FIXED"
    assert outcome.explicit_reply is True


def test_idempotency_key_is_stable_and_changes_with_base_revision():
    first = idempotency_key(
        event_id="evt-1",
        repository="iXuue/Test1",
        base_revision="abc",
        command_type="fix-e2e",
    )
    same = idempotency_key(
        event_id="evt-1",
        repository="iXuue/Test1",
        base_revision="abc",
        command_type="fix-e2e",
    )
    changed = idempotency_key(
        event_id="evt-1",
        repository="iXuue/Test1",
        base_revision="def",
        command_type="fix-e2e",
    )
    assert first == same
    assert first != changed


def test_state_store_is_secret_free_and_atomic(tmp_path):
    store = MaintainerStateStore(tmp_path)
    payload = transition({"trace_id": "trace-1", "token": "must-not-be-added"}, WorkflowState.RECEIVED)
    path = store.save("key", payload)
    assert json.loads(path.read_text(encoding="utf-8"))["state"] == "received"
    assert store.load("key")["trace_id"] == "trace-1"


def test_parse_github_repo_accepts_https_and_ssh():
    assert parse_github_repo("https://github.com/iXuue/Test1.git") == ("iXuue", "Test1")
    assert parse_github_repo("git@github.com:iXuue/Test1.git") == ("iXuue", "Test1")


def test_tool_safety_categories_require_verified_candidate_for_external_writes():
    assert classify_effect(ToolEffect.READ) is MaintainerToolClass.READ_ONLY
    assert classify_effect(ToolEffect.WRITE) is MaintainerToolClass.LOCAL_WRITE
    assert classify_effect(ToolEffect.EXTERNAL) is MaintainerToolClass.EXTERNAL_WRITE
    assert external_write_allowed(candidate_ready=False) is False
    assert external_write_allowed(candidate_ready=True, speculative=True) is False
    assert external_write_allowed(candidate_ready=True) is True


@pytest.mark.asyncio
async def test_github_adapter_maps_issue_and_pr_without_real_network():
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path.endswith("/issues") and request.method == "POST":
            return httpx.Response(
                201,
                json={"number": 7, "html_url": "https://github.com/iXuue/Test1/issues/7"},
            )
        if request.url.path.endswith("/pulls") and request.method == "POST":
            return httpx.Response(
                201,
                json={"number": 8, "html_url": "https://github.com/iXuue/Test1/pull/8"},
            )
        if request.url.path.endswith("/issues/7/comments") and request.method == "GET":
            return httpx.Response(200, json=[{"body": "<!-- marker -->"}])
        return httpx.Response(200, json={"full_name": "iXuue/Test1", "fork": True, "parent": {"full_name": "neubig/starter-repo"}})

    client = httpx.AsyncClient(base_url="https://api.github.com", transport=httpx.MockTransport(handler))
    adapter = GitHubAdapter(PlatformRepoRef("github", "iXuue", "Test1", "https://github.com/iXuue/Test1"), "local-test-token", client=client)
    issue = await adapter.create_issue(title="test", body="body")
    assert await adapter.find_issue_comment_by_marker(7, "marker") is True
    pr = await adapter.create_pull_request(title="test", body="body", head="agent/fix-issue-7", base="main")
    await client.aclose()

    assert issue.issue_number == 7
    assert pr.pr_number == 8
    assert requests[0].headers["authorization"] == "Bearer local-test-token"


def test_github_adapter_requires_the_requested_environment_variable(monkeypatch):
    monkeypatch.delenv("GITHUB_PERSONAL_ACCESS_TOKEN", raising=False)
    with pytest.raises(GitHubCredentialRequiredError):
        GitHubAdapter.from_env(PlatformRepoRef("github", "iXuue", "Test1", "https://github.com/iXuue/Test1"))


@pytest.mark.asyncio
async def test_fix_e2e_is_disabled_without_test_mode(tmp_path, monkeypatch):
    monkeypatch.delenv("E2E_TEST_MODE", raising=False)

    async def coder(*_args):
        raise AssertionError("coder must not run while test mode is disabled")

    request = TurnRequest(
        origin=Origin.USER,
        source=Source(
            channel="feishu",
            chat_id="oc_test",
            sender_id="ou_test",
            chat_type=ChatType.GROUP,
            extras={"message_id": "msg-1", "event_id": "evt-1", "maintainer_description": "fix it"},
        ),
        text="fix it",
        message_id="msg-1",
    )
    result = await MaintainerWorkflow(coder=coder, state_store=MaintainerStateStore(tmp_path)).run(request)
    assert result.state is WorkflowState.BLOCKED
    assert "E2E_TEST_MODE_REQUIRED" in result.message


@pytest.mark.asyncio
async def test_local_e2e_repair_and_verifier_are_isolated(tmp_path, monkeypatch):
    monkeypatch.delenv("E2E_TEST_MODE", raising=False)
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "value.py").write_text("VALUE = 0\n", encoding="utf-8")
    tests_dir = repo / "tests"
    tests_dir.mkdir()
    (tests_dir / "test_value.py").write_text(
        "from value import VALUE\n\ndef test_value():\n    assert VALUE == 1\n",
        encoding="utf-8",
    )
    run_git(repo, "init", "-b", "main")
    run_git(repo, "config", "user.name", "Maintainer Test")
    run_git(repo, "config", "user.email", "maintainer@example.invalid")
    run_git(repo, "remote", "add", "origin", "https://github.com/iXuue/Test1.git")
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", "baseline")

    class FakeGitHub:
        async def get_repository(self):
            return {"full_name": "iXuue/Test1", "fork": False, "parent": None}

        async def find_issue_by_marker(self, _marker):
            return None

        async def create_issue(self, *, title, body):
            return PlatformIssueRef("github", "iXuue", "Test1", 11, "https://github.com/iXuue/Test1/issues/11")

        async def get_issue(self, _issue_number):
            raise AssertionError("not needed")

        def __init__(self):
            self.comments: list[tuple[int, str]] = []

        async def find_issue_comment_by_marker(self, _issue_number, marker):
            return any(marker in body for _, body in self.comments)

        async def comment_issue(self, issue_number, body):
            self.comments.append((issue_number, body))

        async def find_pull_request(self, *, head, base):
            return None

        async def create_pull_request(self, *, title, body, head, base):
            return PlatformPullRequestRef("github", "iXuue", "Test1", 12, "https://github.com/iXuue/Test1/pull/12")

        async def get_pull_request(self, _pr_number):
            raise AssertionError("not needed")

    async def coder(worktree: Path, _prompt: str, _state_dir: Path):
        (worktree / "value.py").write_text("VALUE = 1\n", encoding="utf-8")
        return {"reply": "fixed", "tool_calls": [{"name": "edit_file", "phase": "complete", "failed": False}]}

    def local_publisher(worktree: Path, _branch: str, message: str):
        run_git(worktree, "add", "-A")
        run_git(worktree, "commit", "-m", message)

    fake_github = FakeGitHub()
    request = TurnRequest(
        origin=Origin.USER,
        source=Source(
            channel="feishu",
            chat_id="oc_test",
            sender_id="ou_test",
            chat_type=ChatType.GROUP,
            extras={
                "event_id": "evt-local",
                "message_id": "msg-local",
                "maintainer_command": "issue",
                "maintainer_description": "fix value",
            },
        ),
        text="fix value",
        message_id="msg-local",
    )
    result = await MaintainerWorkflow(
        coder=coder,
        state_store=MaintainerStateStore(tmp_path / "state"),
        adapter_factory=lambda _repo: fake_github,
        publisher=local_publisher,
        workspace_override=repo,
        enforce_fixed_workspace=False,
    ).run(request)

    assert result.state is WorkflowState.PR_CREATED
    assert result.pull_request is not None
    assert (repo / "value.py").read_text(encoding="utf-8") == "VALUE = 0\n"
    assert Path(result.details["repair_worktree"]).exists()
    assert Path(result.details["verifier_worktree"]).exists()
    assert result.details["verification_exit_code"] == 0
    assert result.details["github_issue_resolution_commented"] is True
    assert len(fake_github.comments) == 1
    assert "已修改" in fake_github.comments[0][1]
    assert result.pull_request is not None
    assert result.pull_request.url in fake_github.comments[0][1]
