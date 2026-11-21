# Contributing to `SneppX/.github`

This guide explains how to contribute specifically to the `.github` repository, which manages organization-wide defaults, templates, and workflows.

## Scope of Changes

This repository manages:
- **Organization Profile:** Content on the GitHub landing page (`profile/README.md`)
- **Default Workflows:** Workflows under `.github/workflows/` inherited across the org
- **Issue Forms:** Templates under `ISSUE_TEMPLATE/` (bug reports, feature requests, docs, questions)
- **Community Standards:** `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `SPONSORING.md`

## Testing Changes Locally

All tests in this repository ensure templates, links, and YAML structure are compliant:

```powershell
python -m pytest tests/ -q -p no:cacheprovider
```

Or test specific components using Python directly:
```powershell
python -c "import sys; sys.path.append('tests'); import test_smoke, test_templates, test_profile, test_markdown_links; print('All checks pass')"
```

## Adding or Editing Workflows
- Keep workflows focused on repository health, security, and linting.
- Keep automation limited to repository maintenance and validation. Do not add
  deployment or release pipelines to this community-health repository.
- Test YAML syntax and workflow structure with `tests/test_yaml_structure.py`.
- Remember that workflows here run only in this repository; project repositories
  must explicitly call reusable workflows if they want to share automation.

## Submitting Pull Requests
- Use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, `test:`).
- Verify all relative markdown links resolve using `test_markdown_links.py`.
- Update `CHANGELOG.md` for notable changes.












































































































































