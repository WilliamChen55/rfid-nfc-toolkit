# Contributing

Thanks for helping improve the toolkit.

## Good first contributions

- Add a row to `data/compatibility.json` after testing a reader you own
- Report a firmware/transport quirk via the **Hardware compatibility** template
- Improve docs (`docs/`) or add a worked example under `examples/`
- Add unit tests for protocol helpers

## Scope

Accepted: device discovery, transport adapters, frame decoding, protocol utilities, CLI and documentation.

Not accepted: key recovery, credential recovery, encryption bypass, duplication or emulation of third-party credentials, or anything intended to defeat access control. PRs in that direction are closed without discussion.

## Workflow

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit run --all-files || true
pytest -q
ruff check src tests
```

1. Fork, then branch from `main`: `git checkout -b feat/my-change`
2. Keep commits focused; write a conventional-style subject (`feat:`, `fix:`, `docs:`, `test:`)
3. Add a `CHANGELOG.md` entry under *Unreleased*
4. Open a PR using the template; describe the hardware you tested on

## Code style

- Type hints on public functions
- `ruff` clean, line length 100
- No new runtime dependency without discussion in an issue first

## Data hygiene

Never commit real UIDs tied to a live access system, customer data, or third-party credentials. Use redacted or synthetic samples.

Commercial data, customer/order records, secrets and firmware dumps belong in a private repository — see the public/private boundary in [SECURITY.md](SECURITY.md).
