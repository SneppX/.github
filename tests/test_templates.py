"""Validation tests for pull request and issue templates."""

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
PR_TEMPLATE = ROOT / "PULL_REQUEST_TEMPLATE.md"
ISSUE_DIR = ROOT / "ISSUE_TEMPLATE"


def test_pr_template_exists_and_has_checklists() -> None:
    assert PR_TEMPLATE.is_file(), "PULL_REQUEST_TEMPLATE.md is missing"
    text = PR_TEMPLATE.read_text(encoding="utf-8")
    assert "- [ ]" in text, "PR template must contain actionable checklists"
    assert "Type of change" in text, "PR template must specify type of change"


def test_issue_config_disables_blank_issues() -> None:
    config_file = ISSUE_DIR / "config.yml"
    assert config_file.is_file(), "ISSUE_TEMPLATE/config.yml is missing"
    data = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    assert data.get("blank_issues_enabled") is False


def test_required_issue_forms_present() -> None:
    expected = {"bug_report.yml", "feature_request.yml", "docs.yml", "question.yml"}
    found = {p.name for p in ISSUE_DIR.glob("*.yml") if p.name != "config.yml"}
    for exp in expected:
        assert exp in found, f"Missing issue form: {exp}"
