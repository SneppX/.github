"""Structural checks for the YAML in this repository.

Parsing alone is not enough: a workflow missing ``on:``/``jobs:`` or an issue
form missing ``body:`` parses fine as YAML but is rejected by GitHub, and
neither can be verified on a machine with no Actions runner. These tests cover
the parts GitHub cares about.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = ROOT / ".github" / "workflows"
ISSUE_DIR = ROOT / "ISSUE_TEMPLATE"
FUNDING = ROOT / ".github" / "FUNDING.yml"

# GitHub's own issue-form types.
FORM_TYPES = {
    "markdown",
    "input",
    "textarea",
    "dropdown",
    "checkboxes",
}


def _yaml_files() -> list[Path]:
    files = list(WORKFLOW_DIR.glob("*.yml"))
    files += list(ISSUE_DIR.glob("*.yml"))
    if FUNDING.is_file():
        files.append(FUNDING)
    return sorted(set(files))


def _load(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def test_yaml_files_discovered() -> None:
    """The globs must find the repo's real YAML, or the rest proves nothing."""
    rels = [_rel(p) for p in _yaml_files()]
    assert ".github/workflows/lint.yml" in rels
    assert ".github/workflows/secret-scan.yml" in rels
    assert ".github/workflows/stale.yml" in rels
    assert "ISSUE_TEMPLATE/bug_report.yml" in rels
    assert "ISSUE_TEMPLATE/feature_request.yml" in rels
    assert "ISSUE_TEMPLATE/config.yml" in rels


def test_all_yaml_parses() -> None:
    for path in _yaml_files():
        parsed = _load(path)
        assert isinstance(parsed, dict), f"{_rel(path)} did not parse to a mapping"


def test_expected_workflows_exist() -> None:
    names = {p.stem for p in WORKFLOW_DIR.glob("*.yml")}
    assert names == {"lint", "secret-scan", "license-check", "welcome", "stale", "tests"}, names


def test_workflow_trigger_present() -> None:
    for path in WORKFLOW_DIR.glob("*.yml"):
        wf = _load(path)
        # PyYAML reads the bare `on:` key as the boolean True (YAML 1.1).
        trigger = wf.get("on", wf.get(True))
        assert trigger, f"{_rel(path)} is missing an `on:` trigger"
        assert "jobs" in wf, f"{_rel(path)} is missing a `jobs:` block"


def test_workflow_jobs_have_runs_on() -> None:
    for path in WORKFLOW_DIR.glob("*.yml"):
        wf = _load(path)
        for job_name, job in wf.get("jobs", {}).items():
            assert job_name and job, f"{_rel(path)}: empty job {job_name!r}"
            assert "runs-on" in job, f"{_rel(path)}: job {job_name!r} has no runs-on"
            assert "steps" in job and job["steps"], f"{_rel(path)}: job {job_name!r} has no steps"





def test_external_actions_are_pinned_to_commit_shas() -> None:
    """Prevent mutable action tags from changing workflow code without review."""
    for path in WORKFLOW_DIR.glob("*.yml"):
        workflow = _load(path)
        for job_name, job in workflow.get("jobs", {}).items():
            for index, step in enumerate(job.get("steps", [])):
                action = str(step.get("uses", ""))
                if not action or action.startswith("./"):
                    continue
                ref = action.rsplit("@", 1)[-1] if "@" in action else ""
                assert re.fullmatch(r"[0-9a-f]{40}", ref), (
                    f"{_rel(path)}: job {job_name!r} step {index} "
                    f"must pin {action!r} to a full commit SHA"
                )


def test_gitleaks_release_archive_is_checksum_verified() -> None:
    """Verify the pinned scanner archive before executing its binary."""
    workflow = _load(WORKFLOW_DIR / "secret-scan.yml")
    install = next(
        step for step in workflow["jobs"]["gitleaks"]["steps"]
        if step.get("name") == "Install gitleaks"
    )
    env = install.get("env", {})
    digest = env.get("GITLEAKS_SHA256", "")
    assert re.fullmatch(r"[0-9a-f]{64}", digest), "Gitleaks SHA-256 must be pinned"
    command = install.get("run", "")
    assert "sha256sum --check --strict -" in command
    assert command.index("sha256sum --check --strict -") < command.index("tar -xzf")


def test_checkout_steps_do_not_persist_github_credentials() -> None:
    """Checkout steps should not leave the workflow token in local Git config."""
    for path in WORKFLOW_DIR.glob("*.yml"):
        workflow = _load(path)
        for job_name, job in workflow.get("jobs", {}).items():
            for index, step in enumerate(job.get("steps", [])):
                action = str(step.get("uses", "")).lower()
                if action.startswith("actions/checkout@"):
                    checkout = step.get("with", {})
                    assert checkout.get("persist-credentials") is False, (
                        f"{_rel(path)}: job {job_name!r} step {index} "
                        "must set persist-credentials: false"
                    )


def test_pull_request_target_workflows_do_not_execute_untrusted_checkout() -> None:
    """Privileged PR-target workflows must not run code from contributor branches."""
    for path in WORKFLOW_DIR.glob("*.yml"):
        workflow = _load(path)
        trigger = workflow.get("on", workflow.get(True))
        if not isinstance(trigger, dict) or "pull_request_target" not in trigger:
            continue
        for job_name, job in workflow.get("jobs", {}).items():
            for index, step in enumerate(job.get("steps", [])):
                where = f"{_rel(path)}: job {job_name!r} step {index}"
                action = str(step.get("uses", "")).lower()
                assert not action.startswith("actions/checkout@"), (
                    f"{where} checks out code in a privileged pull_request_target workflow"
                )
                assert "run" not in step, (
                    f"{where} executes shell code in a privileged pull_request_target workflow"
                )


def test_workflows_declare_least_privilege_token_permissions() -> None:
    """Every workflow must opt into explicit, narrowly scoped GITHUB_TOKEN access."""
    for path in WORKFLOW_DIR.glob("*.yml"):
        workflow = _load(path)
        permissions = workflow.get("permissions")
        assert isinstance(permissions, dict) and permissions, (
            f"{_rel(path)} must declare explicit top-level permissions"
        )
        for scope, access in permissions.items():
            assert access in {"read", "write", "none"}, (
                f"{_rel(path)} has invalid permission level {scope}={access!r}"
            )
        write_scopes = {
            scope for scope, access in permissions.items() if access == "write"
        }
        assert write_scopes <= {"issues", "pull-requests"}, (
            f"{_rel(path)} grants unexpected write permissions: {write_scopes}"
        )


def test_workflow_steps_valid() -> None:
    for path in WORKFLOW_DIR.glob("*.yml"):
        wf = _load(path)
        for job_name, job in wf.get("jobs", {}).items():
            for i, step in enumerate(job.get("steps", [])):
                where = f"{_rel(path)}: job {job_name!r} step {i}"
                assert isinstance(step, dict), where
                # Every step needs an action to run or shell to execute.
                assert ("uses" in step) or ("run" in step), f"{where} has neither `uses` nor `run`"


def test_issue_forms_have_required_shape() -> None:
    for name in ("bug_report.yml", "feature_request.yml"):
        path = ISSUE_DIR / name
        form = _load(path)
        for key in ("name", "description", "body"):
            assert key in form, f"{_rel(path)} is missing `{key}`"
        assert isinstance(form["body"], list) and form["body"], f"{_rel(path)}: body empty"


def test_issue_form_blocks_are_known() -> None:
    for name in ("bug_report.yml", "feature_request.yml"):
        form = _load(ISSUE_DIR / name)
        for i, block in enumerate(form["body"]):
            where = f"{_rel(ISSUE_DIR / name)} body[{i}]"
            assert "type" in block, f"{where} has no `type`"
            assert block["type"] in FORM_TYPES, f"{where}: unknown type {block['type']!r}"
            assert "attributes" in block, f"{where} has no `attributes`"


def test_issue_form_ids_unique_and_present() -> None:
    """GitHub requires a stable `id` on every field/markdown block with input."""
    for name in ("bug_report.yml", "feature_request.yml"):
        path = ISSUE_DIR / name
        ids: list[str] = []
        for i, block in enumerate(_load(path)["body"]):
            if block["type"] == "markdown":
                continue
            assert "id" in block, f"{_rel(path)} body[{i}] has no `id`"
            ids.append(block["id"])
        assert len(ids) == len(set(ids)), f"{_rel(path)}: duplicate ids in {ids}"


def test_issue_template_config_shape() -> None:
    cfg = _load(ISSUE_DIR / "config.yml")
    assert cfg.get("blank_issues_enabled") is False, (
        "blank issues should be disabled so the forms are used"
    )
    links = cfg.get("contact_links")
    assert isinstance(links, list) and links, "config.yml needs contact_links"
    for i, link in enumerate(links):
        assert link.get("name"), f"contact_links[{i}] missing name"
        assert link.get("url", "").startswith("http"), f"contact_links[{i}] missing a valid url"
        assert link.get("about"), f"contact_links[{i}] missing about"


def test_funding_yml_shape() -> None:
    assert FUNDING.is_file(), "FUNDING.yml drives the org-wide Sponsor button"
    data = _load(FUNDING)
    assert data.get("github"), "FUNDING.yml must name a GitHub Sponsors account"
