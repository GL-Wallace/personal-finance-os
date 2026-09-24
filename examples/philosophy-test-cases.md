# Philosophy and Reasoning Acceptance Cases

All figures and identifiers are synthetic. Test decisions and boundaries, not exact wording.

## Case 1 — Salary, passive rule, and actual execution

**Input:** Synthetic salary of CNY 18,400 is attributed to the economic month. `01 Rules` sets a USD 1,234 monthly `SYN-PASSIVE` contribution. An actual `SYN-PASSIVE.US` `Passive Buy` of USD 1,210 occurs on the 15th. Living expense is CNY 4,200.

**Required behavior:**

- Record salary and aggregate living expense in `03 Monthly History`.
- Keep the passive purchase in `04 Investment Flow` on the 15th; do not classify it as income, expense, saving, or return.
- Report target USD 1,234, actual USD 1,210, and variance USD -24.
- Do not treat a nearby `FX Buy` as purchase evidence or claim that a specific salary unit funded the purchase.
- Check post-contribution liquidity before judging adherence and do not invent an allocation target.

## Case 2 — Economic-month versus event dates

**Input:** Living expense is finalized on day 1, salary is received on day 10 under the workbook's economic-month convention, and an FX conversion occurs on day 12.

**Required behavior:**

- Keep salary in the intended economic-month row.
- Keep FX on its actual date in Investment Flow.
- Never move the FX event to make it match salary or a purchase.
- State both date conventions in the review.

## Case 3 — One expensive month

**Input:** Spending rises because of a planned professional course and necessary medical care.

**Required behavior:** Separate affordability from value alignment; treat capability and health spending as potentially supportive of the income engine; use a multi-month view; do not moralize from one saving rate; apply `FC-01`, `FC-02`, and `FC-11`.

## Case 4 — Market decline during a sound plan

**Input:** A broad low-cost holding declines sharply while goals, horizon, liquidity, income stability, and policy remain unchanged.

**Required behavior:** Distinguish volatility from permanent loss; apply `BG-09`; do not time the market; state that no allocation/rebalance signal exists without written targets; identify the personal change that would justify review.

## Case 5 — Existing active holding with incomplete policy

**Input:** Synthetic holding `SYN-A` has a role and rationale but no approved cap, exit condition, or review date.

**Required behavior:**

- Apply the passive counterfactual and keep capital eligibility separate from research.
- Use `Needs More Data — No Add` when loss capacity or risk budget is unresolved.
- Do not calculate a cross-currency current weight without a dated FX basis.
- If write-back is authorized, locate by ticker and update the named D:I policy fields only.

## Case 6 — Attractive company, unsafe capital

**Input:** A company appears qualified, but buying would consume required cash and interrupt regular passive accumulation.

**Required behavior:** Return `Not Eligible`; company quality cannot override `FC-02`, `FC-08`, `FC-11`, `BM-08`, or `BM-10`.

## Case 7 — Missing facts and a request for a score

**Input:** Only brokerage holdings are supplied.

**Required behavior:** Do not fabricate a health score; return `Insufficient Data`; request only facts material to liquidity, obligations, income resilience, cash flow, and goals.

## Synthetic v0.7 calculation cases

Use [synthetic-ledger-fixture.json](synthetic-ledger-fixture.json).

### Case 8 — Native-currency position

- CNY assets = **79,000.00**, USD assets = **9,000.00**, HKD assets = **18,500.00**.
- Do not add these values or report one net worth.
- Same-date month-end values reconcile separately by currency.
- Immediate CNY cash is 36,500.00 and two-month average living expense is 4,400.00, so cash runway is **8.30 months**.

### Case 9 — Saving and policy execution

- March net saving = **14,800.00 CNY**.
- April earned income = 19,600.00 CNY, living expense = 4,600.00 CNY, and net saving = **15,000.00 CNY**.
- April qualifying passive actual = **1,210.00 USD** versus target **1,234.00 USD**, variance **-24.00 USD**.
- The USD 1,234 FX Buy is not counted as a passive purchase.

### Case 10 — Unsupported attribution

- Describe CNY, USD, and HKD month-over-month asset changes separately.
- Do not call those changes investment return.
- Do not create a market/FX residual, total active weight, net-worth bridge, or labor-versus-capital growth share.

### Case 11 — Active cap without a denominator

- `SYN-SECTOR` has a written 10% maximum, but the fixture supplies no cross-currency valuation basis.
- Report its local CNY value and written cap while current total-portfolio weight and breach status remain `Unknown`.
- A user-approved permanent-loss amount or months-of-surplus limit may still establish capital eligibility.

## Trigger and scope

Should trigger: salary-led resilience, economic-month saving, passive-policy adherence, native-currency asset health, or whether active capital interrupts passive accumulation.

Should not trigger by default: generic market news, next-week stock predictions, unrelated macro explanations, or a request to maximize return from a ticker list.
