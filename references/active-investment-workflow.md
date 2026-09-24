# Active-Investment Decision Workflow

Use this workflow for an individual company after applying the constitution and asset router. It produces an auditable decision record and, only when separately authorized and in scope, may produce a ledger update. Preserve the evidence labels and answer contract in [reasoning-protocol.md](reasoning-protocol.md).

## Contents

- Decision context and capital eligibility
- Company-research gates and conclusions
- Holding implementation
- Decision record and optional ledger write-back

## Stage 0 — Decision context

Record the action being considered, analysis date, evidence cutoff, holding status, decision horizon, and capital involved. These are required inputs, not research gates. If a material input is absent, the record is incomplete and no action conclusion may be issued.

## Stage 1 — Capital eligibility

Determine whether the capital may take active risk before judging the company. The purpose is error reduction in bounded capital, not finding reasons to interrupt the passive accumulation process. Record the passive counterfactual here and do not repeat it as a company-quality score.

| Gate | Criticality | Question | Required output |
|---|---|---|---|
| CE-1. Hard boundaries | `Critical` | Would the action preserve legal obligations, basic living needs, solvency, and required liquidity? | Relevant obligations, liquidity after action, boundary result |
| CE-2. Loss capacity | `Critical` | Can the user absorb permanent loss without breaking the life plan? | Loss scenario and consequence |
| CE-3. Active-risk budget | `Critical` | Is permanent loss bounded by an explicit user-approved budget? | Use at least one controlling measure: position cap as a percentage of financial assets, maximum permanent-loss amount, or equivalent months of sustainable surplus. Record current and proposed exposure and any workbook cap that exists |
| CE-4. Funding and counterfactual | `Required` | Is the funding source explicit, and would the action leave the passive accumulation process and higher boundaries intact? | Funding source, one passive-baseline comparison, and effect on regular long-term contributions |

Capital-eligibility result:

- Any `Critical` or `Required` `Fail` -> `Not Eligible`.
- Any material `Unclear` -> `Insufficient Data`.
- All gates `Pass` -> `Eligible`.

`Not Applicable` is not valid in Stage 1. A `Not Eligible` or `Insufficient Data` result prohibits initiation or addition but does not prevent informational company research. It must remain visible and cannot be cured by a strong company result.

A missing aggregate active ceiling is not by itself a CE-3 failure when another explicit budget controls the proposed permanent loss. If the user supplies only a tolerable loss amount or months-of-surplus limit, translate it into a position cap only through an explicit loss assumption and obtain user approval before writing a percentage into `01 Rules` `MAXIMUM WEIGHT` (currently column F). Without an explicit dated cross-currency valuation basis, current total-portfolio weight remains `Unknown`. If no usable budget exists, CE-3 is `Unclear`.

## Stage 2 — Company research

Use the Buffett–Munger principle cards in [buffett-munger-principles.md](buffett-munger-principles.md). Do not include portfolio weight or funding in these research gates.

| Gate | Criticality | Question | Required output |
|---|---|---|---|
| CR-1. Evidence | `Required` | Are material propositions current enough, properly classified, traceable, and reconciled? | Source table and unresolved gaps |
| CR-2. Comprehension | `Critical` | Are business economics and key failure modes inside the user's circle of competence? | Plain-language business model and `BM-01` result |
| CR-3. Business quality | `Required` | Are demand, advantage, unit economics, cash conversion, and reinvestment durable? | `BM-02` to `BM-04` results |
| CR-4. Stewardship | `Required` | Do governance, incentives, disclosure, and capital allocation protect per-share owners? | `BM-05` result and dilution analysis |
| CR-5. Resilience | `Critical` | Can the company withstand stress without forced capital or permanent impairment? | `BM-06` result and downside scenario |
| CR-6. Valuation | `Critical` | Is price below a conservative intrinsic-value range with adequate protection? | Scenario range, sensitivities, price source, `BM-07` result |
| CR-7. Inversion | `Required` | What would make the thesis wrong, and which biases may be operating? | Pre-mortem, falsifiers, `BM-09` result |

Record `BM-08` opportunity cost in Stage 1 and use `BM-10` discipline when setting caps and implementing a holding. Do not score either a second time as company quality.

### Gate semantics

- `Critical` — `Fail` normally denies the exception; `Unclear` normally caps research at `Needs More Data`. `Not Applicable` is never valid.
- `Required` — adverse evidence may produce `Fail`; absent, stale, or conflicting evidence produces `Unclear`. `Not Applicable` is valid only when the test is genuinely irrelevant and the reason is written.
- A valid `Not Applicable` is excluded from aggregation. It neither passes nor fails and does not prevent `Qualified exception`.
- No strength elsewhere can compensate for `Fail` or `Unclear` at a material gate.

### Company-research conclusion

Apply these rules in order:

1. If CR-2 fails, or a key permanent-loss path cannot be understood or bounded after the relevant evidence is identified -> `Too Hard`.
2. If any non-valuation critical gate fails, or adverse evidence fails a required gate -> `Do Nothing`.
3. If any material gate other than CR-6 is `Unclear` -> `Needs More Data` and name the smallest resolving evidence set.
4. If all other applicable gates clear and CR-6 alone is `Fail` or `Unclear` because current price protection is inadequate or indeterminate -> `Watchlist`.
5. If every critical gate is `Pass` and every required gate is `Pass` or validly `Not Applicable` -> `Qualified exception`.

Missing, stale, or conflicting evidence should be `Unclear`, not `Fail`. `Watchlist` is valuation-only; it must not hide a general evidence gap. Do not use a numeric total score.

## Stage 3 — Holding implementation

For an existing holding, determine implementation separately from Stage 2. Apply these rules in order:

1. Observable evidence establishes that the thesis has failed or the asset no longer qualifies as an investment -> `Exit on invalidation`.
2. The holding breaches a legal, solvency, required-liquidity, approved active-risk budget, or position-cap boundary -> `Reduce to policy`, even if research says `Qualified exception`.
3. Research is `Do Nothing`, `Needs More Data`, `Too Hard`, or `Watchlist`, or new capital is not `Eligible` -> `No Add`, unless rule 1 or 2 applies.
4. Research is `Qualified exception`, capital boundaries hold, and weight is within policy -> `Maintain within policy`.

A prewritten falsifier is not the sole route to invalidation. Conversely, price decline, cost basis, or a failed research gate alone does not prove invalidation. When timing is discretionary, present material tax, liquidity, and execution consequences to the user; do not turn them into reasons to ignore a hard boundary.

## Decision record

Produce this compact record:

```text
Company / ticker:
Analysis date and evidence cutoff:
Decision under consideration:
Holding status and capital involved:
Observed / reported facts:
User statements:
Management claims:
Derived estimates:
Assumptions and unknowns:
Source quality and conflicts:
Capital-eligibility gates and result:
Passive counterfactual:
Company-research gates (Pass / Unclear / Fail / Not Applicable):
Intrinsic-value range and current price source:
Permanent-loss paths:
Thesis:
Falsifiable invalidation conditions:
Current exposure and approved risk-budget measure:
Company-research conclusion:
Holding-implementation action, if applicable:
Next evidence and review trigger:
```

## Optional ledger write-back

Do not write to the ledger unless the user has separately authorized write-back and it is within the current task scope. When authorized, write only to sheets defined in [ledger-and-net-worth.md](ledger-and-net-worth.md); never add a sheet and never write to `00 Dashboard`.

Locate the `ACTIVE INVESTMENT EXCEPTIONS` banner and its header row dynamically. Match the ticker in column B against `02 Balance Sheet` column C; never assume a fixed row number. The v0.7 policy fields occupy `STRATEGY ROLE` through `DECISION` (currently D:I), while `CURRENCY` remains a derived formula.

| Ledger field | Write-back rule |
|---|---|
| `Strategy Role` (column D) | Short role label that distinguishes passive core from the exception |
| `Holding Rationale` (column E) | One sentence stating the owner-economics thesis, not a price narrative |
| `Maximum Weight` (column F) | User-approved cap; never infer it from current exposure |
| `Exit Condition` (column G) | Two to five observable falsifiers or a policy breach |
| `Review Date` (column H) | Scheduled evidence review, not a price target date |
| `Decision` (column I) | Research conclusion plus implementation action, such as `Needs More Data — No Add` |

Route other authorized write-backs by content:

| Content | Target sheet and location |
|---|---|
| Actual buy, sell, dividend, fee, or FX event | Append `04 Investment Flow` using the real event date and action semantics |
| Next snapshot quantity, average cost, current price, or note | `02 Balance Sheet` columns E:G or I; column H stays its formula |
| New active holding needing an exception record | Add an exception row in `01 Rules`; A/B are identifiers, C stays its currency formula, complete D:I |
| Material close note | Column K of the applicable `03 Monthly History` row |
| New policy parameter | Add only after the user approves its label, value, purpose, and placement in the Personal Constraint table |

Never put purchases, sales, distributions, or FX conversions into Monthly History income or external-flow totals. A research review that changes no policy and records no actual event writes nothing automatically. Blank or instruction-like text is an unset field, not a valid policy.
