"""Regression guards for stale org references.

The 2026-10-18 refresh removed links pointing at deleted repositories
(`SneppX-Editor`, `sneppx-shield`, `sneppx-cloud`, `sneppx-academy`,
`sneppx-audits`, ...). Deleting a repo silently breaks every link to it, so
these tests make that class of bug fail loudly instead.

The `LIVE_REPOS` set is a deliberate hardcoded allowlist. If you add or delete
a repository in the org, update it here — a failing test is the point.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Repos that exist in github.com/SneppX as of 2026-10-18.
LIVE_REPOS = {".github", "sneppx-alg", "linux", "demo-repository"}

# Removed from the org on 2026-10-17. Any reference to these is a bug.
DEAD_REPOS = {
    "SneppX-Editor",
    "sneppx-shield",
    "sneppx-cloud",
    "sneppx-forge",
    "sneppx-dist",
    "sneppx-edge",
    "sneppx-academy",
    "sneppx-audits",
    "sneppx-website",
    "sneppx-serve",
    "sneppx-convert",
    "sneppx-eval",
    "sneppx-tune",
    "sneppx-monitor",
    "sneppx-safe",
    "sneppx-rl",
    "sneppx-registry",
    "sneppx-edu-labs",
}

CONTENT_GLOBS = ("*.md", "*.yml", "*.yaml")

# `github.com/SneppX/<repo>` and bare `SneppX/<repo>`.
REPO_REF = re.compile(r"github\.com/SneppX/(?P<repo>[\w.-]+)|SneppX/(?P<bare>[\w.-]+)")

_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def _content_files() -> list[Path]:
    """Every tracked markdown/YAML file, skipping vendored and VCS dirs."""
    found: list[Path] = []
    for pattern in CONTENT_GLOBS:
        for path in ROOT.rglob(pattern):
            if _SKIP_DIRS.intersection(path.parts):
                continue
            found.append(path)
    return sorted(set(found))


def _relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def test_content_files_discovered() -> None:
    """Sanity check: the glob must actually find the repo's own docs."""
    files = [_relative(p) for p in _content_files()]
    assert "README.md" in files
    assert "profile/README.md" in files
    assert "SECURITY.md" in files


# Backticked code spans hold CLI tool names (`sneppx-serve`, `sneppx-eval`) that
# legitimately share a name with a deleted repo. Masking them keeps the check
# focused on prose references, where a dead link actually hurts.
CODE_SPAN = re.compile(r"`[^`\n]*`")


def _mentions_dead(text: str, name: str) -> bool:
    """True if `name` appears outside code spans as a whole token.

    The lookaround also stops `sneppx-rl` matching inside `sneppx-rlhf`.
    """
    masked = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), text)
    return re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", masked) is not None


def test_no_dead_repo_references() -> None:
    """No file may reference a deleted repo from prose or a link."""
    offenders: list[str] = []
    for path in _content_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for dead in sorted(DEAD_REPOS):
            if _mentions_dead(text, dead):
                offenders.append(f"{_relative(path)} -> {dead}")
    assert not offenders, (
        "References to deleted repositories found. Remove them or, if the repo "
        "genuinely exists, add it to LIVE_REPOS and drop it from DEAD_REPOS:\n  "
        + "\n  ".join(offenders)
    )


def test_repo_references_point_at_live_repos() -> None:
    """Every explicit SneppX/<repo> reference must name a live repo."""
    offenders: list[str] = []
    for path in _content_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in REPO_REF.finditer(text):
            repo = match.group("repo") or match.group("bare")
            if repo is None:
                continue
            # `github.com/SneppX/*` is a deliberate catch-all link in SECURITY.md.
            if repo == "*":
                continue
            if repo not in LIVE_REPOS:
                offenders.append(f"{_relative(path)} -> SneppX/{repo}")
    assert not offenders, (
        "Links point at repos that are not in LIVE_REPOS. Fix the link or "
        "update LIVE_REPOS:\n  " + "\n  ".join(offenders)
    )
