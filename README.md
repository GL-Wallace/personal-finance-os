# Personal Finance OS

A reusable Agent Skill for wage-led capital accumulation, source-governed personal-finance reasoning, native-currency asset-ledger interpretation, and Bogle-first long-term discipline.

## Governing idea

Personal Finance OS serves a person whose main wealth engine is employment income and human capital. It protects resilience, converts sustainable surplus into long-term productive assets, and tracks the gradual transition toward financial-capital participation. John C. Bogle's body of work governs the philosophy, Bogleheads supplies the default implementation, and Buffett–Munger reasoning reduces errors only in bounded active capital.

The Skill does not seek to construct or continuously optimize an outstanding portfolio.

## System layers

1. Philosophy constitution: life, legal obligations, solvency, and evidence quality set the boundaries.
2. Capital accumulation: protect the income engine, create sustainable surplus, and continue long-term ownership.
3. v0.7 ledger: five sheets separate rules, positions, economic-month saving, and actual investment events.
4. Bogle/Bogleheads default: low costs, broad diversification, regular contributions, simplicity, and discipline.
5. Active exception: source-governed Buffett–Munger error reduction after capital eligibility and passive comparison.

## v0.7 workbook contract

| Sheet | Purpose |
|---|---|
| `00 Dashboard` | Read-only native-currency position and latest close |
| `01 Rules` | Personal constraints and active-investment exceptions |
| `02 Balance Sheet` | Dated asset facts and local-currency values |
| `03 Monthly History` | Economic-month income, expense, saving, native-currency snapshots, and close state |
| `04 Investment Flow` | Actual buys, sells, FX, dividends, interest, and fees by event date |

The workbook deliberately does not consolidate CNY, USD, and HKD. The Skill therefore does not invent a total net worth, cross-currency portfolio weight, market/FX plug, or performance attribution without an explicit dated FX basis.

The workbook stores a user-defined monthly passive-contribution rule. The rule identifies its asset and currency in the label and its target amount in the value cell. A target is not evidence of execution: adherence comes only from matching `Passive Buy` events in `04 Investment Flow`, and variances remain visible rather than being backfilled.

## What it does

- Validates the five-sheet v0.7 structure, source formulas, economic-month close states, and event semantics
- Recomputes local-currency position values, CNY monthly saving, liquidity facts, and passive-policy adherence
- Keeps salary attribution, FX conversion, and investment execution separate
- Preserves uncertainty when liabilities, FX conversion bases, prices, or events are missing
- Applies Bogle's wider body of work as the governing financial philosophy and Bogleheads as the implementation method
- Supports a contribution-first policy without forcing target weights or rebalancing bands
- Routes active assets to an exception workflow and separates capital eligibility, research, and implementation
- Uses source-governed Buffett–Munger gates for individual companies without replacing the passive constitution
- Provides a blank ledger template, deterministic validators, and synthetic fixtures; public examples contain no personal financial data

## What it does not do

- Connect directly to banks or brokerages, execute trades, or move money
- Treat a policy target as proof of a purchase
- Add different currencies together without a dated conversion basis
- Infer investment return from asset changes that also contain contributions and withdrawals
- Promise returns, optimize continuously, or replace licensed financial, tax, accounting, or legal advice

## Intellectual foundation

The Bogle layer synthesizes *Stay the Course*, *Common Sense on Mutual Funds*, *Enough*, *Clash of the Cultures*, *John Bogle on Investing*, *Don't Count On It!*, and *The Little Book of Common Sense Investing*. *The Bogleheads' Guide to Investing* supplies practical implementation. This project uses original summaries and is not affiliated with or endorsed by the authors, publishers, Vanguard, Bogleheads, Berkshire Hathaway, or related organizations.

## Install and invoke

Install the repository as an Agent Skills-compatible skill with `SKILL.md` as its entry point, then invoke:

```text
$personal-finance-os Review my latest economic month, native-currency assets, liquidity, and execution of my Bogle-first accumulation policy.
```

Automatic invocation remains enabled for matching personal-finance requests. Copy `assets/finance-os-template.xlsx` before entering personal data. See [examples/prompts.md](examples/prompts.md), [examples/philosophy-test-cases.md](examples/philosophy-test-cases.md), and [references/privacy-and-data-boundary.md](references/privacy-and-data-boundary.md). Never commit a completed ledger, private spreadsheet link, credentials, or identifying financial data.

## Repository structure

- `SKILL.md`: router, operating rules, and safety boundaries
- `references/`: philosophy, ledger, implementation, and active-exception methods
- `examples/`: synthetic prompts, fixtures, and acceptance cases
- `assets/`: blank ledger template for private user copies
- `scripts/`: deterministic Skill, fixture, and XLSX validation
- `agents/openai.yaml`: client-facing metadata

## Roadmap

- v0.1-v0.4: philosophy constitution, active-exception gates, and prior ledger contracts
- v0.7: native-currency five-sheet contract and policy-to-execution reconciliation
- v1.0: stable interfaces and documented compatibility

## License and disclaimer

[MIT](LICENSE). Educational workflow and general information only; users remain responsible for verifying inputs, outputs, laws, costs, risks, and suitability.
