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

## Workflows in this repository

The workflows under `.github/workflows/` run only in `SneppX/.github`.
GitHub does not automatically inherit ordinary Actions workflows from an
organization's `.github` repository. A project repository must define its own
workflow or explicitly call a reusable workflow. The current workflows are:

| Workflow | What it checks or does |
|----------|------------------------|
| `tests.yml` | Repository tests for links, templates, and YAML structure |
| `lint.yml` | Ruff linting when Python files are present |
| `secret-scan.yml` | Gitleaks scanning of the repository history |
| `license-check.yml` | Presence of a supported root-level license file |
| `stale.yml` | Marks inactive issues and pull requests as stale |
| `welcome.yml` | Greets first-time issue and pull-request contributors |

## Tests

```powershell
python -m pytest tests/ -q -p no:cacheprovider
```

Tests validate YAML structure, issue form shapes, workflow trigger presence,
and that relative Markdown links resolve to real files.




























































