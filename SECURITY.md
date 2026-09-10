# Security Policy

## Scope

This repository ships Markdown instructions, references, and a bounded shell
preflight under `zensical/`. It does not ship credentials or a network service.
Security concerns include malicious or misleading instructions, unsafe commands
or shell-script changes, prompt-injection content in references, and
supply-chain changes to the published payload.

## Reporting

Once a public GitHub repository is configured, report vulnerabilities through
its private GitHub Security Advisory channel. Do not include secrets or
personal data in a public issue. Until that channel exists, keep the report
private and identify the affected commit, file, and behavior.

## Maintainer response

Maintainers will acknowledge a report, reproduce it with synthetic data where
possible, assess whether the runtime payload or maintainer tooling is affected,
and publish a corrective change or mitigation. Do not run third-party skill
scripts during review without explicit authorization.

## Review boundary

The skill should request only the filesystem, shell, and network access needed
for the target repository and current documentation. A successful build is not
evidence that a deployment or external integration is safe.

Last reviewed: 2026-09-09.
