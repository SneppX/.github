# Contributing to SneppX

Thanks for your interest in contributing to the SneppX ecosystem! This document describes how to get started.

## Repository Map

| Repo | Purpose | Language |
|------|---------|----------|
| `sneppx-alg` | Core DL framework (tensor, autograd, nn, optim, distributed, security) | C11/C++20 + Python |
| `SneppX/.github` | Org profile, community-health files, default workflows | Markdown / YAML |

All repositories under `SneppX/*` are MIT-licensed open core and follow the same
contribution standards described here. Per-repo specifics (build commands, test
commands, coding conventions) live in each repo's own `AGENTS.md` / `README.md`.

## Development Setup

### Python repositories

```powershell
# Clone and install in editable mode
git clone https://github.com/SneppX/<repo>.git
cd <repo>
pip install -e ".[dev]"
```

### sneppx-alg (C + Python)

```powershell
# Build C libraries (requires CMake + Ninja)
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release

# Python bindings (pure NumPy fallback works without C build)
$env:PYTHONPATH = "bindings/python"
python -m pytest tests/python/test_tensor.py -q -p no:cacheprovider
```

## Pull Request Process

1. Fork the repository and create a feature branch
2. Make your changes with clear commit messages
3. Run per-file pytest to verify no regressions
4. Open a PR with a clear description of the change

## Code Style

- **Python**: 4-space indentation, type hints where helpful
- **C**: `SNEPPX_` prefix for all public functions/types/macros
- **Commit messages**: `<area>: <description>` (e.g., `optim: add load_state_dict to SparseAdam`)

## Testing

- **Per-file pytest only** â€” runs fast on any machine; a full-suite run can be slow on resource-constrained setups
- Run: `python -m pytest tests/python/test_<module>.py -q -p no:cacheprovider`
- Safe test list in `sneppx-alg/AGENTS.md`

## License

All repositories are MIT-licensed open core.

## Questions?

Open an issue in the relevant repo or contact the SneppX org.

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `perf`, `style`

Examples:
- `feat(tensor): add einsum operation`
- `fix(autograd): correct gradient accumulation in backward pass`
- `docs(quickstart): add GPU setup section`
- `test(nn): add conv2d gradient check`
- `chore(deps): bump numpy minimum to 1.24`

## Reporting Security Issues

**Please do NOT open a public issue for a security vulnerability.**

See [SECURITY.md](SECURITY.md) for the full private disclosure policy and
the link to GitHub's advisory form.

## First-time Contributors

Looking for a good starting point? Browse issues labelled:

- [`good first issue`](https://github.com/SneppX/sneppx-alg/labels/good%20first%20issue) — small, well-scoped tasks
- [`help wanted`](https://github.com/SneppX/sneppx-alg/labels/help%20wanted) — contributions actively encouraged
- [`documentation`](https://github.com/SneppX/sneppx-alg/labels/documentation) — docs fixes and improvements

If you have a question before starting, open an issue using the **Question**
template — no need to ask for permission first.