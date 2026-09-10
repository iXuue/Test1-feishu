"""Explicit Git operations used by the Maintainer workflow."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


class MaintainerGitError(RuntimeError):
    pass


@dataclass(frozen=True)
class GitResult:
    returncode: int
    stdout: str
    stderr: str


_IGNORED_GENERATED_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def _is_patch_candidate(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if normalized == ".coverage" or normalized.endswith("/.coverage"):
        return False
    return not any(part in _IGNORED_GENERATED_PARTS for part in normalized.split("/"))


def run_git(repo: Path, *args: str, check: bool = True) -> GitResult:
    executable = shutil.which("git")
    if executable is None:
        raise MaintainerGitError("git executable is not available")
    proc = subprocess.run(
        [executable, *args],
        cwd=str(repo),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    result = GitResult(proc.returncode, proc.stdout, proc.stderr)
    if check and proc.returncode != 0:
        raise MaintainerGitError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return result


def current_revision(repo: Path) -> str:
    return run_git(repo, "rev-parse", "HEAD").stdout.strip()


def current_branch(repo: Path) -> str:
    return run_git(repo, "branch", "--show-current").stdout.strip()


def is_clean(repo: Path) -> bool:
    return not run_git(repo, "status", "--porcelain").stdout.strip()


def origin_url(repo: Path) -> str:
    return run_git(repo, "remote", "get-url", "origin").stdout.strip()


def parse_github_repo(url: str) -> tuple[str, str]:
    normalized = url.strip().removesuffix("/").removesuffix(".git")
    match = re.search(r"github\.com[/:]([^/]+)/([^/]+)$", normalized, re.IGNORECASE)
    if not match:
        raise MaintainerGitError("origin must point to a GitHub repository")
    return match.group(1), match.group(2)


def create_worktree(repo: Path, target: Path, revision: str, *, branch: str | None = None) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise MaintainerGitError(f"refusing to overwrite existing worktree path: {target}")
    if branch:
        run_git(repo, "worktree", "add", "-B", branch, str(target), revision)
    else:
        run_git(repo, "worktree", "add", "--detach", str(target), revision)


def prepare_patch(worktree: Path, revision: str) -> tuple[str, list[str]]:
    # Intent-to-add makes newly created files visible to git diff without
    # committing or changing the user's base checkout.
    tracked = [
        line.strip()
        for line in run_git(worktree, "diff", "--name-only", revision).stdout.splitlines()
        if line.strip() and _is_patch_candidate(line.strip())
    ]
    untracked = [
        line.strip()
        for line in run_git(worktree, "ls-files", "--others", "--exclude-standard").stdout.splitlines()
        if line.strip() and _is_patch_candidate(line.strip())
    ]
    if untracked:
        run_git(worktree, "add", "-N", "--", *untracked)
    paths = sorted(set(tracked) | set(untracked))
    if not paths:
        raise MaintainerGitError("repair agent produced no patch")
    patch = run_git(worktree, "diff", "--binary", "--no-ext-diff", revision, "--", *paths).stdout
    changed = [
        line.strip()
        for line in run_git(worktree, "diff", "--name-only", revision, "--", *paths).stdout.splitlines()
        if line.strip()
    ]
    if not patch.strip():
        raise MaintainerGitError("repair agent produced no patch")
    return patch, changed


def apply_patch(worktree: Path, patch: str) -> None:
    executable = shutil.which("git")
    if executable is None:
        raise MaintainerGitError("git executable is not available")
    proc = subprocess.run(
        # Do not require the worktree and index to have byte-identical line
        # endings. Windows repositories commonly use core.autocrlf=true,
        # which makes --index reject an otherwise applicable patch.
        [executable, "apply", "--whitespace=nowarn", "-"],
        cwd=str(worktree),
        input=patch,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        raise MaintainerGitError(f"git apply failed: {proc.stderr.strip()}")


def commit_and_push(worktree: Path, branch: str, message: str) -> None:
    run_git(worktree, "add", "-A")
    run_git(worktree, "commit", "-m", message)
    run_git(worktree, "push", "--set-upstream", "origin", branch)


def run_test(worktree: Path, command: tuple[str, ...] = ("python", "-m", "pytest", "-q")) -> GitResult:
    proc = subprocess.run(
        list(command),
        cwd=str(worktree),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=600,
    )
    return GitResult(proc.returncode, proc.stdout, proc.stderr)


__all__ = [
    "GitResult",
    "MaintainerGitError",
    "apply_patch",
    "commit_and_push",
    "create_worktree",
    "current_branch",
    "current_revision",
    "is_clean",
    "origin_url",
    "parse_github_repo",
    "prepare_patch",
    "run_git",
    "run_test",
]
