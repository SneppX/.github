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
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if ".git" in path.parts:
            continue
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
    ):
        assert (ROOT / name).is_file(), "%s is missing" % name
