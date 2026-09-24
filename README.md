# Personal Finance OS

Personal Finance OS is an Agent Skill for people in the **wage-led capital-accumulation stage**: employment income and human capital remain the primary wealth engine, while sustainable monthly surplus is gradually converted into long-term financial capital.

Its purpose is not to build or continuously optimize an outstanding portfolio. It provides a disciplined way to understand financial facts, protect the income engine, accumulate capital, and reduce avoidable investment errors.

## Governing framework

The system follows a clear decision hierarchy:

1. **Financial facts first.** A complete asset ledger establishes what is known, what is missing, and what can be calculated without invention.
2. **Life and solvency boundaries.** Legal obligations, essential spending, liquidity, and the continuity of the income engine take priority over return seeking.
3. **Bogle as the foundation.** Low cost, broad diversification, long holding periods, disciplined saving, stewardship, and humility about forecasts govern the default path.
4. **Bogleheads as implementation.** The philosophy is translated into simple, repeatable actions appropriate to the user's goals, jurisdiction, time horizon, and risk capacity.
5. **Buffett–Munger as an active-investing exception.** Active capital must first be eligible for risk, then satisfy a higher burden of evidence. It never overrides the passive constitution or financial-safety boundaries.

Active investing is therefore an exception that must justify itself against the passive alternative—not a parallel default.

## What the Skill helps with

- Diagnose the user's capital-accumulation stage and dependence on employment income
- Review income, living expenses, monthly saving, liquidity, and asset changes
- Distinguish contributions, transfers, investment events, valuation changes, and genuine investment performance
- Evaluate whether current financial behavior is sustainable and aligned with the purpose of wealth
- Apply Bogle and Bogleheads principles to long-term investment decisions
- Examine bounded active investments through source-governed Buffett–Munger reasoning
- State uncertainty explicitly when liabilities, prices, exchange rates, transactions, or other material facts are missing
- Produce a short, prioritized action list without manufacturing a reason to trade

## Asset ledger

The bundled workbook is a compact financial fact system rather than a transaction-level expense tracker.

| Sheet | Role |
|---|---|
| `00 Dashboard` | Read-only summary of the latest available financial facts |
| `01 Rules` | User-defined constraints and active-investment exceptions |
| `02 Balance Sheet` | Dated positions and values in their native currencies |
| `03 Monthly History` | Aggregated income, spending, saving, month-end assets, and close status |
| `04 Investment Flow` | Material buys, sells, foreign-exchange events, dividends, interest, and fees |

The workbook keeps CNY, USD, and HKD separate unless the user supplies an explicit dated exchange-rate basis. It does not invent consolidated net worth, portfolio weights, return attribution, or rebalancing signals.

The monthly passive-contribution policy is user-defined. A target in `01 Rules` is not proof of execution; only matching `Passive Buy` events in `04 Investment Flow` establish what was actually invested.

Copy `assets/finance-os-template.xlsx` before entering personal information. The bundled file must remain blank.

## Boundaries

Personal Finance OS does not:

- Connect directly to banks or brokerages
- Execute trades, move money, or authenticate to financial institutions
- Treat market forecasts, recent returns, or product popularity as decision foundations
- Promise returns or claim that a named investor would endorse a security
- Replace licensed financial, tax, accounting, insurance, or legal advice
- Publish or bundle a user's completed ledger or identifying financial data

## Intellectual foundation

The Bogle layer is an original synthesis of:

- *Stay the Course*
- *Common Sense on Mutual Funds*
- *The Little Book of Common Sense Investing*
- *Enough: True Measures of Money, Business, and Life*
- *The Clash of the Cultures: Investment vs. Speculation*
- *John Bogle on Investing: The First 50 Years*
- *Don't Count On It!*

*The Bogleheads' Guide to Investing* supplies the practical implementation framework. The active-investing exception draws only from attributable Berkshire Hathaway materials, shareholder letters, meeting records, and other registered primary sources described in `references/source-registry.md`.

This project uses original summaries. It is independent and is not affiliated with or endorsed by the authors, publishers, Vanguard, the Bogleheads organization, Berkshire Hathaway, or related entities.

## Use

Install the repository as an Agent Skills-compatible skill with `SKILL.md` as its entry point, then invoke it directly or through a matching personal-finance request.

```text
$personal-finance-os Review my latest month, financial resilience, capital-accumulation progress, and execution of my long-term policy.
```

Useful starting points:

- `assets/finance-os-template.xlsx` — blank five-sheet ledger
- `examples/prompts.md` — example requests
- `examples/philosophy-test-cases.md` — synthetic acceptance cases
- `references/privacy-and-data-boundary.md` — public/private data boundary

## Privacy and validation

Real ledgers, private spreadsheet links, credentials, account identifiers, and identifying financial records must remain outside this repository. Public examples use synthetic data that is not derived by perturbing a real ledger.

Before publishing a change, run:

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_fixture.py
python3 scripts/validate_template.py
python3 scripts/privacy_scan.py --current-tree
python3 scripts/privacy_scan.py --git-history
```

## Repository structure

- `SKILL.md` — routing, operating rules, and safety boundaries
- `references/` — philosophy, ledger, implementation, and active-exception methods
- `examples/` — synthetic prompts, fixtures, and acceptance cases
- `assets/` — blank ledger template
- `scripts/` — deterministic validation and privacy checks
- `agents/openai.yaml` — client-facing Skill metadata

## License and disclaimer

[MIT](LICENSE). Educational workflow and general information only. Users remain responsible for verifying inputs, outputs, applicable laws, costs, risks, and suitability.
