# SneppX organization defaults

This repository contains the public SneppX organization profile and shared community-health documents.

## Organization profile

GitHub displays [profile/README.md](profile/README.md) on the [SneppX organization page](https://github.com/SneppX).

## Shared community files

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Sponsoring](SPONSORING.md)

GitHub can use supported community-health files from this repository as organization-level defaults when a project repository does not provide its own version.

## Workflows

The workflows in .github/workflows run only in this repository. GitHub does not automatically inherit ordinary Actions workflows from an organization's .github repository. Reusable workflows must be called explicitly by each project repository.

## Project repositories

- [SneppX-ALG](https://github.com/SneppX/sneppx-alg)
- [VSTodo](https://github.com/SneppX/vstodo)
- [SneppX-OV](https://github.com/SneppX/sneppxov)


## Automated formatting commits

Project repositories may use formatter automation to prepare changes on dedicated
`automation/format-<run-id>` branches. These branches are validation candidates;
they must not silently rewrite the default branch.

Automated formatting commits follow the Conventional Commits style and include
the affected scope plus a unique run identifier. For example:

- `style(python): apply automated formatting [format-12345]`
- `style(native,config): normalize source and build files [format-12346]`
- `style(docs): standardize documentation formatting [format-12347]`

Each formatter run must produce a distinct commit message. A formatter must
leave its branch available for review, and its commit must pass the repository's
required checks against that exact commit before it is considered ready to merge.
