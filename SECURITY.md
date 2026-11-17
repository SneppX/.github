# Security Policy

SneppX takes vulnerability reports seriously. Please disclose suspected vulnerabilities privately so maintainers can investigate before technical details become public.

## Supported versions

Security fixes are currently developed against the main branch of [SneppX-ALG](https://github.com/SneppX/sneppx-alg). No backport or long-term-support schedule is promised for older releases.

| Version or source | Security support |
|---|---|
| main | Best-effort fixes and review |
| Published release tags | No guaranteed backports |
| Third-party forks | Maintained by their respective owners |

A component's presence in the repository does not imply that it has undergone an independent security audit or is suitable for production deployment. Review the component documentation and validation status before relying on it.

## Report a vulnerability privately

Use [GitHub's private security advisory form](https://github.com/SneppX/sneppx-alg/security/advisories/new) for SneppX-ALG vulnerabilities.

Please include, where possible:

- Affected repository, version, component, and file path.
- Impact and realistic attack conditions.
- Minimal reproduction steps or proof of concept.
- Suggested mitigation, if known.
- Whether and how you would like to be credited.

Do not open a public issue or discussion containing exploit details, credentials, personal information, or unpatched vulnerability information.

## Triage and disclosure

Reports are reviewed on a best-effort basis. The following are response targets, not service-level guarantees:

| Stage | Target |
|---|---|
| Acknowledgement | Within 5 business days |
| Initial triage | Within 10 business days |
| Fix and disclosure | Coordinated with the reporter, based on severity and remediation needs |

The maintainers will coordinate disclosure with the reporter where practical. Do not publish details before a fix or an agreed disclosure date.

## Scope

Reports may cover security-relevant behaviour in code, build systems, and release artifacts maintained under the SneppX organization.

Examples include memory-safety defects with a credible exploitation path, authentication or authorization bypasses, exposure of credentials or sensitive data, cryptographic implementation defects, unsafe update or artifact verification, and security controls that fail to enforce their documented guarantees.

General numerical errors, incorrect gradients, ordinary build failures, and documentation mistakes should normally be reported through the affected project's public issue tracker unless they create a security impact.

## Safe-harbor expectations

Good-faith research is welcome. Researchers should avoid privacy violations, service disruption, and data destruction; access only the systems and data needed to demonstrate the issue; stop testing if sensitive data is encountered; and allow reasonable time for investigation and remediation before public disclosure.

Maintainers will assess good-faith reports fairly and will not discourage responsible disclosure.
