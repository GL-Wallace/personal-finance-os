# Privacy and Data Boundary

Use this reference whenever a ledger is created, copied, exported, logged, tested, or prepared for publication.

## Data separation

- Keep philosophy, workflows, schemas, validators, the blank template, and synthetic fixtures inside the Skill.
- Keep every real user ledger in user-controlled private storage and outside the Skill directory.
- Copy `assets/finance-os-template.xlsx` before use. Never edit the bundled master with personal data.
- Treat spreadsheet IDs, private URLs, account labels, balances, quantities, cost bases, transaction dates, notes, and portfolio combinations as personal financial data.

## Minimum collection

Request only facts needed for the current decision. Do not request account numbers, government identifiers, credentials, authentication codes, seed phrases, private keys, or exact addresses. Accept redacted account names and aggregated monthly spending.

## Public artifacts

- Use placeholder labels in the blank template.
- Use synthetic identifiers, dates, amounts, tickers, and narratives in examples and tests.
- Preserve accounting identities when generating synthetic data, but do not scale, shift, or lightly perturb a real ledger.
- Never copy user values into documentation, fixtures, logs, screenshots, issue reports, or error messages.
- Never store a Google Sheet ID, private Drive URL, access token, or exported real ledger in the repository.

## Safe reporting

Validators may report counts, statuses, reconciliation differences, and sheet or row locations. They must not print account names, holding names, quantities, prices, cost bases, personal notes, or complete position lists unless the user explicitly requests a private local report.

## Publication check

Before publication, run:

```text
python3 scripts/privacy_scan.py --current-tree
python3 scripts/privacy_scan.py --git-history
```

Any finding involving credentials, private links, work email, real-ledger declarations, or prohibited files blocks publication. A clean current tree does not prove that Git history is clean.
