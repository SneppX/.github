"""Validate that relative links in the Markdown actually resolve.

External links go stale silently and cannot be checked offline, so they are
left to the `SneppX/<repo>` checks in `test_no_dead_links.py`. What this file
catches is the local equivalent: `docs/index.md` had a `[CODEOWNERS](CODEOWNERS)`
link that resolved to `docs/CODEOWNERS` — a 404 nobody noticed.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

_FENCE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(<?([^)>\s]+)>?\)")
_REF_DEF = re.compile(r"^\s*\[([^\]]+)\]:\s*(\S+)", re.MULTILINE)
_REF_USE = re.compile(r"!?\[[^\]]+\]\[([^\]]+)\]")


def _markdown_files() -> list[Path]:
    found: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if _SKIP_DIRS.intersection(path.parts):
            continue
        found.append(path)
    return sorted(set(found))


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def _strip_code(text: str) -> str:
    """Remove fenced and inline code so example links aren't validated."""
    return _INLINE_CODE.sub(" ", _FENCE.sub(" ", text))


def _is_external(target: str) -> bool:
    return bool(re.match(r"^(https?:|mailto:|tel:|data:)", target))


def test_markdown_files_discovered() -> None:
    rels = [_rel(p) for p in _markdown_files()]
    assert "README.md" in rels
    assert "docs/index.md" in rels
    assert "profile/README.md" in rels


def test_relative_inline_links_resolve() -> None:
    broken: list[str] = []
    for path in _markdown_files():
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        for target in _INLINE_LINK.findall(text):
            if target.startswith("#") or _is_external(target):
                continue
            # Drop the fragment: `SECURITY.md#reporting` only needs the file.
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            candidate = (path.parent / file_part).resolve()
            if not candidate.exists():
                rel = _rel(path)
                broken.append(f"{rel} -> {target}")
    assert not broken, "Broken relative Markdown links:\n  " + "\n  ".join(broken)


def test_reference_definitions_resolve() -> None:
    broken: list[str] = []
    for path in _markdown_files():
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        for _name, target in _REF_DEF.findall(text):
            if target.startswith("#") or _is_external(target):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            if not (path.parent / file_part).resolve().exists():
                broken.append(f"{_rel(path)} -> {target}")
    assert not broken, "Broken reference-style link definitions:\n  " + "\n  ".join(broken)


def test_reference_usages_are_defined() -> None:
    """`[text][ref]` with no matching `[ref]: url` renders as literal junk."""
    missing: list[str] = []
    for path in _markdown_files():
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        defined = {name.lower() for name, _ in _REF_DEF.findall(text)}
        for ref in _REF_USE.findall(text):
            if ref.lower() not in defined:
                missing.append(f"{_rel(path)} -> [{ref}]")
    assert not missing, "Reference links used but never defined:\n  " + "\n  ".join(missing)


def test_no_absolute_windows_or_file_paths() -> None:
    """Docs should stay portable — no `C:\\...` or `file://` paths."""
    offenders: list[str] = []
    for path in _markdown_files():
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        if re.search(r"[A-Za-z]:\\\\|file://", text):
            offenders.append(_rel(path))
    assert not offenders, "Non-portable absolute paths in:\n  " + "\n  ".join(offenders)


def test_cross_reference_content() -> None:
    profile = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    assert "sneppx.github.io/sneppx-alg" in profile, "profile must link to docs site"

    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "SECURITY.md" in contributing or "security" in contributing.lower(), "CONTRIBUTING must mention security"

    support = (ROOT / "SUPPORT.md").read_text(encoding="utf-8")
    assert "CONTRIBUTING.md" in support, "SUPPORT must reference CONTRIBUTING.md"

