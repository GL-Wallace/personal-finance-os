# Portfolio Policy Method

Use this reference for allocation, index investing, contribution policy, rebalancing, fund selection, diversification, fees, taxes, and risk capacity.

Apply it after reading the Bogle core philosophy and, for implementation questions, the Bogleheads method. This file governs the user's written policy; it does not replace the financial-foundation checks or prescribe universal products.

**Boundary of this file:** it is the single home for the written-policy field list, product-selection criteria, contribution and rebalancing mechanics, and the policy-change test. The end-to-end implementation sequence and foundation procedures (reserve, debt, insurance, account filling) live in [bogleheads-implementation.md](bogleheads-implementation.md). Each topic is defined in exactly one file.

The policy must remain consistent with [philosophy-constitution.md](philosophy-constitution.md). In particular, a target allocation cannot justify investing money required for near-term obligations.

This method supports the capital-accumulation process; it is not a mandate to design or continuously optimize an ideal portfolio.

## Baseline

Start with the simplest diversified, low-cost portfolio consistent with the user's objective, horizon, liquidity needs, jurisdiction, and capacity to bear loss. Recent performance alone is not a reason to change a sound policy.

The default path is long-term ownership through broad, low-cost diversification. Any active, concentrated, speculative, or forecast-dependent allocation must be labeled and evaluated as an exception.

Do not prescribe a universal stock/bond allocation. First establish:

- Purpose and time horizon for the money
- Emergency reserves and near-term liabilities
- Ability and willingness to tolerate drawdowns
- Income stability and debt obligations
- Tax-advantaged account options and jurisdiction
- Existing exposures, including employer stock and property
- Contribution and withdrawal plans

## Policy modes

Choose the least complex mode that is executable:

- **Contribution-first policy:** goals, liquidity boundary, eligible broad-market assets, contribution behavior, maximum acceptable costs, and review triggers. Use when the user has not chosen target weights and does not need a mechanical rebalance rule.
- **Allocation policy:** add target weights or ranges and a rebalancing rule when multiple asset classes, withdrawals, liability matching, or risk control require them.

Do not force the user into the allocation mode merely because a conventional investment-policy statement contains target weights.

## Policy fields

A contribution-first policy specifies:

- Goals, time horizons, and the purpose of long-term ownership
- Required liquidity and conditions that pause or reduce contributions
- Eligible broad, low-cost products or product-selection criteria
- Contribution behavior and review cadence
- Maximum acceptable fees and avoidable tax or turnover costs
- Treatment of active capital, if any
- Conditions that permit a policy change

An allocation policy additionally specifies:

- Target allocation and acceptable bands
- Rebalancing rule and review cadence
- Withdrawal and liability-matching rules when relevant

In the v0.7 workbook, `01 Rules` stores named liquidity constraints, an optional user-defined monthly passive-contribution target, and per-position maximum weights in the active-exception table. It does not store target allocation, an aggregate active ceiling, or a rebalance threshold. Those signals remain `Unknown` rather than defaulting to zero. Because assets remain in native currencies and the table has no current-weight field, a percentage cap cannot be mechanically tested against total portfolio value without an explicit dated FX basis; report the cap and set current breach status to `Unknown` when that basis is absent.

## Product selection criteria

Evaluate products by their role in the policy, not by recent performance. Compare:

- Breadth and underlying exposure; asset-class diversification
- Geographic and sector concentration
- Fund overlap and look-through holdings; more funds do not create more diversification
- Expense ratio and all-in ownership cost, including transaction costs
- Tracking quality
- Turnover and potential tax drag; tax efficiency and account location
- Liquidity, structure, domicile, and currency exposure
- Securities-lending and counterparty considerations when material
- Operational and behavioral simplicity

Prefer the smallest set of products that implements the intended exposure reliably.

## Contribution and rebalancing policy

Prefer a written policy over market forecasts. A contribution-first policy may operate without target weights. When an allocation policy exists, it may specify target weights and bands, contribution schedule, order of accounts or tax wrappers, use of new cash flows before selling to rebalance, review cadence, and the conditions that justify a policy change.

Rebalance because allocation has moved outside the policy or the investor's circumstances have materially changed, not because a recent winner is expected to reverse. Consider taxes and trading costs before selling. The v0.7 workbook stores neither a target allocation nor a rebalance threshold, so no mechanical rebalance signal can be raised from the sheet. Describe each native-currency mix factually and raise a rebalance review only against a policy the user has actually stated. A monthly passive-contribution target governs contributions, not allocation and not market timing.

## Decision test

For every proposed change, compare:

1. Existing policy unchanged
2. Proposed policy after costs and taxes
3. The behavioral burden and new failure modes

Recommend the change only when its expected benefit is meaningful, understandable, and durable. Doing nothing is valid.

## Monitoring

Review periodically rather than reacting to daily prices. Track allocation, costs, diversification, cash needs, tax efficiency, and adherence to policy. Revisit risk capacity when goals, employment, family obligations, debt, or time horizon change materially.
