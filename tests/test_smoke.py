"""Smoke checks for the org-level repository."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".txt", ".rst"}


def test_org_profile_readme_exists_and_mentions_core_repo() -> None:
    profile = ROOT / "profile" / "README.md"
    assert profile.is_file(), "profile/README.md is missing"
    text = profile.read_text(encoding="utf-8")
    assert "sneppx-alg" in text, "org profile must reference the core repo"
    assert text.strip(), "org profile README is empty"


def test_no_mojibake_replacement_chars() -> None:
    """Guard against files saved in the wrong encoding (U+FFFD)."""
    offenders = []
    for path in ROOT.glob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            offenders.append((str(path), "not valid UTF-8"))
            continue
        if "\ufffd" in text:
            offenders.append((str(path), "contains U+FFFD"))
    # Also check docs/ and profile/
    for sub in ("docs", "profile"):
        sub_dir = ROOT / sub
        if not sub_dir.is_dir():
            continue
        for path in sub_dir.glob("*.md"):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                offenders.append((str(path), "not valid UTF-8"))
                continue
            if "\ufffd" in text:
                offenders.append((str(path), "contains U+FFFD"))
    assert not offenders, "mojibake detected: %r" % offenders


def test_community_health_files_present() -> None:
    for name in (
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "SUPPORT.md",
        "LICENSE",
        "README.md",
        "CHANGELOG.md",
        "SPONSORING.md",
        "CODEOWNERS",
    ):
        assert (ROOT / name).is_file(), "%s is missing" % name


def test_docs_index_not_empty() -> None:
    docs_index = ROOT / "docs" / "index.md"
    assert docs_index.is_file(), "docs/index.md is missing"
    assert len(docs_index.read_text(encoding="utf-8")) > 100, "docs/index.md is too short"


def test_codeowners_configured() -> None:
    codeowners = ROOT / "CODEOWNERS"
    assert codeowners.is_file(), "CODEOWNERS missing"
    assert "@ammar49-cyber" in codeowners.read_text(encoding="utf-8")


def test_sponsoring_mentions_github() -> None:
    sponsoring = ROOT / "SPONSORING.md"
    assert sponsoring.is_file(), "SPONSORING.md missing"
    assert "github" in sponsoring.read_text(encoding="utf-8").lower()

