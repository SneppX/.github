# Security Policy

## Supported Versions

Security fixes land on the `main` branch of
[`sneppx-alg`](https://github.com/SneppX/sneppx-alg). Until tagged LTS
releases exist, `main` is the only supported line.

| Component | Supported |
|-----------|-----------|
| `sneppx-alg` (`main`) | ✅ |
| Older tags and third-party forks | ❌ |

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
