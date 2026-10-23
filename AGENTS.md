# .github — Agent Guide

## Purpose
This repository holds SneppX organization-wide community health files, issue templates, and default GitHub Actions workflows.

## Contents
- `profile/README.md` — Organization landing page displayed on github.com/SneppX
- `ISSUE_TEMPLATE/` — Structured GitHub issue forms (bug_report, feature_request, docs, question)
- `.github/workflows/` — Default org workflows (lint, stale, welcome, secret-scan, license-check)
- Community health standards: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `SPONSORING.md`

## Testing & Validation
All tests in this repository validate YAML syntax, template shapes, and markdown links:
```powershell
python -m pytest tests/ -q -p no:cacheprovider
```

## Commit Conventions
Follow Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`.

## Policy Constraints
- Do NOT add CI/CD build or deployment pipeline workflows to this repository.
- Workflows here are strictly for org-level community hygiene.
- All testing and validation are performed locally.
