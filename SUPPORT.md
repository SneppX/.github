# Support

Use the channel that matches the problem.

| Question | Where to go |
|---|---|
| Bug or unexpected behaviour | Open a bug report in the affected repository. |
| Feature proposal | Open a feature request in the affected repository. |
| Usage question | Check the project documentation, then open an issue or discussion if enabled. |
| Security vulnerability | Use the private reporting process in [SECURITY.md](SECURITY.md). Do not publish vulnerability details in an issue. |
| Sponsorship | Read [SPONSORING.md](SPONSORING.md). |

## Before opening an issue

1. Read the documentation for the affected project.
2. Search existing open and closed issues.
3. Confirm the repository, branch, package version, and environment.
4. Include a minimal reproduction and relevant error output. Remove credentials and other sensitive data.

For SneppX-ALG, start with the [documentation](https://sneppx.github.io/sneppx-alg/) and [issue tracker](https://github.com/SneppX/sneppx-alg/issues).

## What maintainers can help with

- Reproducible bugs in project code.
- API behaviour and documented usage.
- Build, packaging, and installation problems.
- Performance reports with a reproducible benchmark.

General model-training advice and requests for bespoke work may be outside the scope of a small volunteer-maintained project.

## Response expectations

SneppX is maintained on a best-effort basis. Responses may take several days; no response-time guarantee is made.

## Common SneppX-ALG setup checks

### Python package import

From the repository root, install the package or set the source path. The package source is in bindings/python/SneppX_ALG/.

### CPU-only native build

CUDA is optional for a CPU-only build. Follow the current build guide in the affected repository and disable the CUDA option when configuring CMake.

Do not share API tokens, private keys, passwords, or unredacted environment dumps in public issues.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, testing, and contribution expectations.
