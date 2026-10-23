# Security Policy

## Supported Versions

Security fixes land on the `main` branch of
[`sneppx-alg`](https://github.com/SneppX/sneppx-alg). Until tagged LTS
releases exist, `main` is the only supported line.

| Component | Supported |
|-----------|-----------|
| `sneppx-alg` (`main`) | ✅ |
| Older tags and third-party forks |  - " -  |

## Reporting a Vulnerability

**Please do NOT open a public issue for a security vulnerability.**

Report privately with GitHub's advisory form:
<https://github.com/SneppX/sneppx-alg/security/advisories/new>

Include:

- Affected repository / module / file path
- Impact and a minimal reproduction
- Suggested fix or mitigation, if you have one
- Your preferred credit name (or "no credit")

### What to expect

| Stage | Target |
|-------|--------|
| Acknowledgement | within 5 working days |
| Triage + initial assessment | within 10 working days |
| Fix / mitigation | coordinated with the reporter, severity-dependent |
| Disclosure | coordinated disclosure by default |

## Scope

**In scope:** code, build artifacts, and release artifacts under
`github.com/SneppX/*`.

**Out of scope:**

- Third-party forks kept for reference (e.g. [`linux`](https://github.com/SneppX/linux))
- Vulnerabilities in upstream dependencies with no SneppX-specific trigger
- Issues that require physical access, or local privilege escalation
  without a SneppX-specific impact
- Denial of service that depends on unrealistic resource exhaustion

## Preferred Languages

English.

## Supported Versions Table

| Version | Supported |
|---------|-----------|
| `sneppx-alg` 1.5.x (main) | ? Supported |
| `sneppx-alg` < 1.5.0 | ? Not supported |
| Third-party forks | ? Not supported |

Security fixes are applied to `main` only. No backport releases are planned until
an LTS branch is declared.

## Step-by-step Private Disclosure

1. **Do not** open a public GitHub issue or discussion.
2. Navigate to the [GitHub Security Advisories form](https://github.com/SneppX/sneppx-alg/security/advisories/new).
3. Fill in the title, description, and affected version (use `main` if unsure).
4. Include: affected module / file path, reproduction steps, impact assessment,
   and any suggested fix or mitigation.
5. Submit  - " you will receive an acknowledgement within **5 business days**.

## What qualifies as a security issue?

**Security issues** (use private advisory):
- Remote code execution, privilege escalation, or authentication bypass
- Cryptographic weaknesses in the S0-S9 security layers
- Memory safety issues (buffer overflow, use-after-free) with exploitation potential
- Credential or key material leakage

**Regular bugs** (open a public issue):
- Wrong numerical output, incorrect gradient, broken test
- Build failures, import errors, documentation mistakes
- Performance regressions without a security impact

## Safe Harbor

SneppX supports good-faith security research. If you act in good faith to:
- Avoid harm to users, systems, or data
- Report promptly and allow reasonable time to fix before disclosure
- Not exploit the vulnerability beyond what is needed to demonstrate it

 - then SneppX will not pursue legal action against you and will publicly
acknowledge your contribution (unless you prefer anonymity).