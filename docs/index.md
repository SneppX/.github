# SneppX `.github`

Organization-level defaults and profile for the SneppX GitHub organization.

This repository serves two purposes:

1. **Org-wide** — GitHub auto-serves the community-health files below to every
   repository in the org that does not define its own.
2. **Org defaults** — `.github/workflows/` supplies default Actions workflows to
   repositories that have no workflows of their own.

## What's here

| Path | Scope | Purpose |
|------|-------|---------|
| [profile/README.md](../profile/README.md) | org | rendered at https://github.com/SneppX |
| [SECURITY.md](../SECURITY.md) | org | vulnerability reporting policy |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | org | Contributor Covenant v2.1 |
| [SUPPORT.md](../SUPPORT.md) | org | where to get help |
| [ISSUE_TEMPLATE/](../ISSUE_TEMPLATE) | org | bug report + feature request forms, contact links |
| [PULL_REQUEST_TEMPLATE.md](../PULL_REQUEST_TEMPLATE.md) | org | PR checklist |
| [FUNDING.yml](../.github/FUNDING.yml) | org | Sponsor button (`github: ammar49-cyber`) |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | org | contribution guidelines |
| [SPONSORING.md](../SPONSORING.md) | org | sponsorship tiers |
| [README.md](../README.md) | repo | this repo's landing page |
| [CODEOWNERS](../CODEOWNERS) | **repo only** | review ownership for this repo |
| [.github/workflows/](../.github/workflows) | org | default lint / secret-scan / license-check |

> `CODEOWNERS` is a per-repository file — it does **not** apply org-wide.

Core project: [sneppx-alg](https://github.com/SneppX/sneppx-alg).

## Default workflows

Inherited only by repos that define no workflows of their own:

- **`lint.yml`** — `ruff check --exit-zero`; skips repos with no `.py` files and
  never fails the build.
- **`secret-scan.yml`** — `gitleaks detect` over full history (license-free
  binary, not `gitleaks-action`).
- **`license-check.yml`** — fails if no `LICENSE` file exists at the root.

## Local checks

```sh
python -m pytest tests/test_smoke.py -q -p no:cacheprovider
```
