# Security Policy

## Reporting a vulnerability

Do **not** open a public issue for security problems.

Use GitHub's private reporting flow: **Security → Report a vulnerability** on the repository page. Include:

- Affected version and platform
- A minimal reproduction
- Impact assessment

Expect an initial response within 7 days. We will coordinate disclosure timing with you.

## Scope

In scope: code execution, unsafe deserialization, command injection, path traversal, credential leakage in logs, and dependencies with known CVEs.

Out of scope: the legal status of RFID reading hardware in your jurisdiction; misuse of the tool against systems you do not own — those are described in [LEGAL_NOTICE.md](LEGAL_NOTICE.md).

## Misuse reports

If you find content in this repository that appears to facilitate unauthorized access, report it privately using the same channel. Maintainers will remove it and, where appropriate, notify affected parties.

## Repository boundary: public vs private

This repository is **public**. Everything committed here — including commit history, branches and tags — is permanently visible to anyone.

### Keep in the public repo

- Public product model names and protocol families
- Generic transport/decoding code, CLI, tests and documentation
- Compatibility notes that describe observed behavior, not supplier or batch internals
- Marketing copy and setup guides

### Never commit here — keep this in a private repository instead

1. **Commercial data** — purchase cost, wholesale price, margin, supplier or forwarder accounts, sourcing channels
2. **Customer and order data** — customer lists, orders, shipping addresses, tracking numbers, tax IDs (EORI / IOSS / VAT), invoices
3. **Secrets** — account passwords, API tokens, payment keys (Stripe / PayPal), SSH or signing private keys, webhook URLs
4. **Sensitive technical material** — firmware dumps, captured card data, key or algorithm implementations, full cloning or bypass procedures, batch-specific firmware differences

### History note

Deleting a file in a later commit does **not** remove it from git history. Sensitive material must never be committed in the first place; if it was committed by mistake, rotate the secret and rewrite history rather than relying on a follow-up delete.
