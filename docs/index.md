# SneppX Organization Docs

This repository (`SneppX/.github`) holds org-wide community health files and
default GitHub workflows for all SneppX repositories.

## Contents

| File | Purpose |
|------|---------|
| `profile/README.md` | Org landing page shown on github.com/SneppX |
| `CONTRIBUTING.md` | How to contribute to any SneppX repository |
| `CODE_OF_CONDUCT.md` | Community standards (Contributor Covenant 2.1) |
| `SECURITY.md` | Security vulnerability disclosure policy |
| `SUPPORT.md` | Where to get help |
| `SPONSORING.md` | Sponsorship tiers and how funding is used |
| `PULL_REQUEST_TEMPLATE.md` | Default PR checklist |
| `CODEOWNERS` | Auto-assign reviewers for this repo |
| `ISSUE_TEMPLATE/` | Structured issue forms (bug, feature, docs, question) |
| `.github/workflows/` | Default org workflows (lint, secret-scan, stale, welcome) |
| `.github/FUNDING.yml` | GitHub Sponsors configuration |

## Default Workflows

Repositories in the SneppX org that do not define their own
`.github/workflows/` inherit these workflows automatically:

| Workflow | What it does |
|----------|-------------|
| `lint.yml` | Ruff linting (style, imports, type hints) |
| `secret-scan.yml` | GitLeaks secret scanning (full history) |
| `license-check.yml` | License header validation |
| `stale.yml` | Auto-label and close stale issues/PRs |
| `welcome.yml` | Welcome message for first-time contributors |

## Tests

```powershell
python -m pytest tests/ -q -p no:cacheprovider
```

Tests validate YAML structure, issue form shapes, workflow trigger presence,
and that relative Markdown links resolve to real files.
