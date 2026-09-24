# Monthly Review Method

Use this reference for an auditable v0.7 economic-month review. Read the native-currency ledger contract and the wage-led accumulation method first. Add financial-health or Enough reasoning only when the question requires it.

## Inputs

- `01 Rules`: named personal constraints, including any monthly passive-contribution rule, and active exceptions
- `02 Balance Sheet`: current dated position snapshot
- `03 Monthly History`: latest economic-month row, prior comparable rows, and close state
- `04 Investment Flow`: actual events for the reviewed calendar period and nearby settlement dates
- user context that could change liquidity, income resilience, or policy interpretation

Do not request itemized daily spending for a routine review. Living expense is a monthly aggregate. Request detailed evidence only to resolve a material discrepancy.

## Review sequence

1. State the economic month, actual event-date window, snapshot date, currencies, and account coverage.
2. Validate the close state. A month is complete only when inputs are present, the required native-currency snapshot has been frozen, and status is `Closed`.
3. Recompute earned income, living expense, external flow, net saving, and saving rate. Preserve the workbook's day-10 salary attribution convention.
4. Recompute CNY, USD, and HKD assets separately. If a same-date Balance Sheet and month-end row exist, reconcile each currency independently.
5. List material Investment Flow events by actual date and economic substance. Keep FX and purchases out of income, living expense, and net saving.
6. Parse the monthly passive-contribution rule from `01 Rules` and compare it with matching passive buys. Show the configured asset, currency, target, actual, variance, dates, and whether an explanation exists. An FX Buy is not purchase evidence.
7. Compare current facts with prior comparable months. Describe native-currency changes without calling them return or consolidating them.
8. Review cash floors, reserve coverage, income-engine risks, active exceptions, and upcoming obligations. Cross-currency maximum-weight checks remain `Unknown` without an explicit dated FX basis.
9. Recommend no more than three actions unless a detailed plan is requested.

## Suggested output

### Decision

Lead with `Continue`, `Watch`, `Action Required`, or `Insufficient Data`, and name the controlling reason.

### Economic-month cash flow

| Metric (CNY) | Current | Previous | Change | Evidence |
|---|---:|---:|---:|---|
| Salary + other earned | | | | |
| Living expense | | | | |
| Other external flow | | | | |
| Net saving | | | | Formula-recomputed |
| Saving rate | | | | Denominator stated |

### Passive-policy execution

| Policy | Target | Actual | Variance | Event dates | Status |
|---|---:|---:|---:|---|---|
| Configured monthly passive contribution | | | | | |

### Native-currency assets

| Currency | Current snapshot | Prior comparable close | Change | Interpretation limit |
|---|---:|---:|---:|---|
| CNY | | | | Includes flows and valuation |
| USD | | | | Includes flows and valuation |
| HKD | | | | Includes flows and valuation |

### Resilience and exceptions

Report immediate cash, defensive reserve/floor, cash runway, known obligations, and exception-record completeness. Do not invent target allocation, aggregate active ceiling, current total-portfolio weights, or rebalance signals.

### Data quality and next actions

Name stale prices, open months, missing frozen values, unexplained policy variance, unmatched exception tickers, and unsupported conclusions. `No change needed` is valid when the system is operating as intended.
