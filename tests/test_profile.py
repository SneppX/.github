"""Validation tests for the organization profile README."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "profile" / "README.md"


def test_profile_file_exists() -> None:
    assert PROFILE.is_file(), "profile/README.md is missing"


def test_profile_has_substance() -> None:
    text = PROFILE.read_text(encoding="utf-8")
    assert len(text.strip()) > 500, "profile README should be comprehensive, not a stub"


def test_profile_contains_repo_links() -> None:
    text = PROFILE.read_text(encoding="utf-8")
    assert "github.com/SneppX/" in text or "https://github.com/SneppX" in text


def test_profile_has_roadmap_section() -> None:
    text = PROFILE.read_text(encoding="utf-8")
    assert "## Roadmap" in text or "roadmap" in text.lower()


def test_profile_has_sponsorship_or_support() -> None:
    text = PROFILE.read_text(encoding="utf-8")
    assert "sponsor" in text.lower() or "support" in text.lower()
