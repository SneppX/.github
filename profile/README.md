# SneppX

Open-core AI ecosystem: secure, auditable, distributed AI.

## Repositories

| Repo | What it is |
|---|---|
| [sneppx-alg](https://github.com/SneppX/sneppx-alg) | Universal open-source AI algorithm framework in C/C++ & CUDA  - " tensor engine, autograd, MoE/SSM transformers, LLM model zoo (LLaMA / Mistral / Qwen / DeepSeek), quantization, distributed training, and a 10-layer AI security stack (v1.5.2) |
| [linux](https://github.com/SneppX/linux) | Linux kernel source tree  - " kept for systems-level work and kernel-module experiments |
| [.github](https://github.com/SneppX/.github) | This repo  - " organization profile, community-health files, and default workflows |

## sneppx-alg

The core of the organization: ~183K LOC of C11 + C++20 + x86_64 ASM + CUDA with
Python bindings (`SneppX_ALG`, MIT-licensed).

- **Pipeline**: HSS (state-space SSM)  - ' SER (MoE routing)  - ' ARC (adversarial
  guard)  - ' NPE (16-register neural VM, 32 opcodes)  - ' FM (federated / fractal
  memory)
- **Security (10 layers, S0 - "S9)**: post-quantum crypto (Kyber / Dilithium /
  SPHINCS+, FIPS 203/204/205), memory hardening, obfuscation, monitoring,
  network security, AI sanitizer, key vault, secure updates, formal
  verification, pentesting
- **Capabilities**: tensor engine + autograd (40+ ops, higher-order AD),
  optimizers (SGD / AdamW / RAdam / Schedule-Free), trainer, inference engine,
  quantization (INT8 / INT4 / FP8 / AWQ / GPTQ), distributed training (ZeRO-1/2/3,
  pipeline / tensor / expert parallelism, FSDP, elastic), model zoo with
  `from_pretrained()` for LLaMA 2/3, Mistral, Qwen2, DeepSeek V2
- **Tooling**: 6 CLI tools  - " `sneppx-train`, `sneppx-serve`, `sneppx-experiment`,
  `sneppx-eval`, `sneppx-quantize`, `sneppx-rlhf`  - " plus FastAPI serving

Docs: https://sneppx.github.io/sneppx-alg/

## Support SneppX

SneppX is built in the open. If the stack helps you, sponsor the work:
[`SPONSORING.md`](https://github.com/SneppX/.github/blob/main/SPONSORING.md)
describes tiers. Sponsor buttons are enabled on public repositories.

## Roadmap

### Shipped (v1.5.2, 2026-10-23)

- sneppx-alg: tensor engine, autograd with higher-order AD, `nn` / `optim` /
  loss libraries, sparse tensors, state-dict serialization, CTC loss,
  quantization, distributed collectives, and the Python `F.*` functional
  namespace.
- sneppx-alg: 10 security layers (S0 - "S9), post-quantum crypto, signed updates,
  formal verification, model zoo presets, HTTP REST API, 300+ tests.
- sneppx-alg: site UX improvements (smooth scroll, TOC highlight, keyboard
  shortcuts, back-to-top), playground localStorage persistence, contributing
  docs page.
- Org: community health 100%, GitHub Sponsors enabled, default workflows
  (license-check, lint, secret-scan).

### 2026 Q4

- sneppx-alg: true forward-mode tangent engine, C NCCL verification on a real
  toolchain, FIPS KAT validation for PQC, Linux/macOS build polish.
- Org: first external contributors onboarded via `good first issue` program.

### 2027 Q1

- Trade/audit practice: ISO 42001 / EU AI Act readiness reports as a service.

## Talks / contributing

`sneppx-alg` is MIT-licensed. Open issues and pull requests are welcome.
Security findings should be reported privately via the security advisories on
[sneppx-alg](https://github.com/SneppX/sneppx-alg/security/advisories/new).
