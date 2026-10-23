# Support

Thanks for using SneppX.

## Where to get help

| Question type | Where |
|---------------|-------|
| Bug or unexpected behaviour | Open a **bug report** in the affected repository |
| Feature idea | Open a **feature request** in the affected repository |
| Usage / "how do I..." | Open an issue, or use the repo's discussions if enabled |
| Security vulnerability | **Private only** — see [SECURITY.md](SECURITY.md). Do **not** open a public issue |
| Sponsorship / commercial work | See [SPONSORING.md](SPONSORING.md) |

## Before you ask

1. Read the docs: <https://sneppx.github.io/sneppx-alg/>
2. Search existing issues (open **and** closed)
3. Confirm you are on the latest `main`

## What we can and cannot help with

- **Yes:** framework behaviour, API questions, build/runtime problems,
  reproducible bugs, performance reports with a benchmark.
- **No:** general deep-learning or PyTorch questions, help debugging your
  model's accuracy, or bespoke feature requests with no broader maintainer
  interest. SneppX is a small project.

## Response time

This is a volunteer-driven open-source project — expect days rather than hours.

## Contributing

The fastest way to get something fixed is a pull request.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## Common Issues

### PYTHONPATH not set

**Symptom:** `ModuleNotFoundError: No module named 'SneppX_ALG'`

**Fix:**
```powershell
$env:PYTHONPATH = "bindings/python"
python -m pytest tests/python/test_tensor.py -q -p no:cacheprovider
```

### ImportError for SneppX_ALG

**Symptom:** ImportError even after setting PYTHONPATH.

**Fix:** Verify the path is correct relative to the repo root. The package
lives at `bindings/python/SneppX_ALG/`. Run from the repo root:
```powershell
$env:PYTHONPATH = "bindings/python"
python -c "import SneppX_ALG; print('OK')"
```

### Tests hang or take too long

**Symptom:** `python -m pytest tests/python/` hangs after a few tests.

**Fix:** Never run the full test suite at once on a CPU-only machine.
Run per-file only:
```powershell
python -m pytest tests/python/test_tensor.py -q -p no:cacheprovider
```
LLM inference tests (`test_llama_models.py`, `test_inference_server.py`)
**must not be run** on machines without a GPU � they will hang.

### Build fails with "CUDA not found"

**Symptom:** CMake errors about missing CUDA toolkit.

**Fix:** CUDA is optional. For CPU-only builds:
```powershell
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DSNEPPX_CUDA=OFF
```

### `ruff check` fails on pre-commit

**Symptom:** pre-commit hook rejects the commit.

**Fix:** Run ruff locally first:
```powershell
ruff check --fix .
```

## Response time

This is a volunteer-driven open-source project.
Expect responses in **days rather than hours**. PRs with a fix attached
are typically reviewed faster. For critical security issues, see [SECURITY.md](SECURITY.md).