# Contributing to SneppX

Thanks for your interest in contributing to the SneppX ecosystem! This document describes how to get started.

## Repository Map

| Repo | Purpose | Language |
|------|---------|----------|
| `sneppx-alg` | Core DL framework (tensor, autograd, nn, optim, distributed, security) | C11/C++20 + Python |
| `sneppx-shield` | AI security & compliance (SBOM, signatures, compliance reports) | Python |
| `sneppx-forge` | Verified model registry & marketplace | Python |
| `sneppx-dist` | Distributed training CLI | Python |
| `sneppx-edge` | On-device inference SDK | Python |
| `sneppx-academy` | Certification & courses | Markdown + Python |
| `sneppx-audits` | Security audit & consulting | Python |
| `sneppx-cloud` | Managed training/inference platform | Python |
| `sneppx-website` | Organization site | HTML/CSS/JS |

## Development Setup

### Python repos (shield, forge, dist, edge, audits, cloud)

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

- **Per-file pytest only** — the full test suite hangs on this machine
- Run: `python -m pytest tests/python/test_<module>.py -q -p no:cacheprovider`
- Safe test list in `sneppx-alg/AGENTS.md`

## License

All repos are MIT-licensed open core. Commercial/enterprise tiers are sold separately for `sneppx-cloud` and `sneppx-edge`.

## Questions?

Open an issue in the relevant repo or contact the SneppX org.
