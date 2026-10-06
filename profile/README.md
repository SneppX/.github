# SneppX

Open-core AI ecosystem: secure, auditable, distributed AI.

## Product family

| Repo | What it is |
|---|---|
| [sneppx-alg](https://github.com/SneppX/sneppx-alg) | Universal open-source AI algorithm framework (tensor engine, autograd, moe/ssm, quantization, distributed training, 10-layer security) |
| sneppx-shield | AI security & compliance suite (SBOM, signed models, compliance reports) |
| sneppx-forge | Verified model registry & marketplace |
| sneppx-dist | Distributed training CLI |
| sneppx-edge | On-device inference SDK |
| sneppx-academy | Certification & courses |
| sneppx-audits | AI security audit & consulting services |
| sneppx-website | Organization site |
| sneppx-cloud | Managed training & inference platform (private, Dockerized FastAPI) |
| sneppx-dist-pro | Priority node scheduler (private) |
| sneppx-edge-fleet | Device telemetry + OTA rollout management (private) |
| sneppx-studio | Web IDE + experiment tracking (private) |
| sneppx-shield-pro | Enterprise AI Act audit packs (private) |
| sneppx-forge-enterprise | Private registry: RBAC + sealed key escrow (private) |
| sneppx-academy-pro | Paid certifications with signed credentials (private) |
| sneppx-hub | Public signed-model index (syncs from forge) |
| sneppx-bench | SneppX vs NumPy/PyTorch benchmark harness |
| sneppx-kernels | Reference GEMM/INT8 kernels |
| sneppx-datasets | Toy datasets for demos |
| sneppx-playground | Notebook templates |
| sneppx-cli-docs | MkDocs CLI reference (gh-deploy ready) |
| sneppx-agents-public | Curated OpenCode agent personalities |
| sneppx-templates | train/serve/edge starter templates |

## Support SneppX

SneppX is built in the open. If the stack helps you, sponsor the work:
`SPONSORING.md` in this repo describes tiers. Sponsor buttons are enabled on
all public repositories.

## Roadmap

### 2026 Q4 (shipped in v0.1.0)
- sneppx-shield: real Ed25519 signing, SBOM CLI (`--recursive`/`--no-hash`), `audit --ci` annotations, key-rotation docs.
- sneppx-forge: signed model registry + REST API (Bearer auth), Docker Compose server, remote `verify --remote`.
- sneppx-dist: platform backend detection (nccl/gloo), TCP `check`, launcher rendering (bash/powershell).
- sneppx-edge: symmetric + per-channel uint8 quantize, batched inference (`infer-batch`).
- sneppx-audits: multi-target evidence merge, SBOM digest discovery, JSON schema, GitHub Action.
- sneppx-academy: Module 01 published (tensor engine); Modules 02-04 drafted.
- All 14 services/products now ship Dockerized FastAPI apps + tests; every Python package carries `__version__` and per-file pytest.

### 2027 Q1
- sneppx-alg: v0.2 4-bit quantization runtime, true forward-mode tangent engine, C NCCL verify on real toolchain.
- sneppx-shield: Dilithium (PQ) signing backend, SBOM attestation format, OCI registry support.
- sneppx-forge: marketplace UI, model download distribution (signed blobs), license keys.
- sneppx-edge: per-device licensing daemon, Vulkan/Metal backends, 4-bit inference.
- sneppx-academy: certification with signed certificates end-to-end, enterprise training tier.
- sneppx-website: interactive docs, changelog, newsletter.

### 2027 Q2
- sneppx-cloud (private): managed training/inference platform MVP.
- Trade/audit practice: ISO 42001 / EU AI Act readiness reports as a service.

## Talks / contributing

Every repo has its own license: public repos are MIT, `sneppx-cloud`, the
`*-pro` tier, and `sneppx-edge-fleet`/`sneppx-studio` are proprietary. Open
issues and pull requests are welcome on public repos; security findings go to
[sneppx-audits](https://github.com/SneppX/sneppx-audits).
