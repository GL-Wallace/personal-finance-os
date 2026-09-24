# Bogleheads Implementation Method

Use this reference to translate the Bogle philosophy into a practical personal-finance and portfolio process. The result must remain adaptable to the user's jurisdiction, taxes, goals, accounts, products, and risk capacity.

This is the implementation layer represented by `BH-GUIDE` and related Bogleheads educational material in [source-registry.md](source-registry.md). It is subordinate to [philosophy-constitution.md](philosophy-constitution.md): an implementation convention cannot override life, solvency, Enough, or the Bogle default.

**Boundary of this file:** it owns the implementation sequence, the foundation decision procedures below, and behavioral implementation. The written-policy field list, product-selection criteria, and rebalancing mechanics live in [portfolio-policy.md](portfolio-policy.md); the user's numeric policy lives in `01 Rules`. Do not duplicate those here — link to them.

## Implementation order

1. Define goals, time horizons, currency needs, and the role of money in the user's life.
2. Protect the income engine: health, employability, core skills, and the ability to replace employment income if disrupted.
3. Build adequate liquidity for emergencies and near-term obligations.
4. Review expensive debt, insurance gaps, and risks that could force asset sales.
5. Write the smallest usable policy before selecting products. A contribution-first policy is valid when target weights are not yet chosen.
6. Implement long-term ownership with broad, low-cost, transparent funds available in the user's jurisdiction.
7. Use tax-advantaged accounts and tax-aware asset placement when applicable.
8. Contribute sustainable surplus regularly according to the policy rather than forecasts.
9. Add a strategic allocation and rebalance rule only when they solve a real risk or implementation need; otherwise describe the current mix without inventing targets.
10. Review periodically, automate what is safe, and change policy only for durable personal reasons.

## Written policy

The authoritative policy field list and the conditions for changing it are defined in [portfolio-policy.md](portfolio-policy.md). The v0.7 `01 Rules` sheet stores named CNY reserve constraints, an optional user-defined monthly passive-contribution rule, and active-exception records. It does not store target allocation, an aggregate active ceiling, or a rebalance threshold. Parse rules by label rather than fixed cell address. When a policy element is absent, report `Unknown` and keep dependent signals inactive.

Do not invent a universal stock/bond split or assume a particular fund ticker is available, tax-efficient, or suitable everywhere.

For a wage-led accumulator, judge implementation first by continuity, cost, diversification, and resilience. Do not treat product count, frequent allocation changes, or active research activity as evidence of progress.

## Foundation decision procedures

These steps derive an answer from the user's inputs; they do not hard-code universal numbers.

### Emergency reserve

1. Take essential monthly expense from observed spending: use `03 Monthly History` column D, preferably averaged over the latest three populated months (state how many exist), and ask the user when essential spending cannot be separated from the total.
2. Set the coverage period by risk drivers, not a fixed rule: income volatility and time to replace income, single versus diversified household income, insurance waiting periods and deductibles, near-term non-deferrable obligations, and access to non-investment credit.
3. Express the result as a **range** of months and state the drivers; review it when any driver changes.
4. Hold the reserve in low-volatility, immediately accessible form. Volatile investments do not count at full value, and the reserve is separate from the investment portfolio.
5. Compare immediate CNY cash and the defensive reserve with the named floors in `01 Rules`. Report cash runway as a fact; do not invent a target-month benchmark.

### Expensive debt versus investing

Compare a certain cost with an uncertain return, in after-tax terms:

1. Compute the after-tax interest rate of each debt. Repaying it is a **guaranteed** return at that rate.
2. Compare with a deliberately conservative lower bound for long-term broad-market expected return, stated as a range the user accepts, never a precise forecast.
3. If the after-tax debt rate is clearly above the conservative bound, prioritize repayment before taxable investing. If clearly below, the policy portfolio may proceed. In the overlap band, decide on liquidity effect, behavioral cost, diversification of remaining debts, and the user's ability to stay invested through a drawdown; state which factor decided.
4. Non-rate exceptions always apply first: capture any employer matching contribution that would otherwise be forfeited, preserve the minimum reserve against forced debt or sale, and respect tax-advantaged contribution windows that close.
5. Distinguish debt principal (balance-sheet reduction) from interest and fees (financing cost). Never present a loan as income, and never treat required minimum payments as discretionary spending.

### Insurance and catastrophic risks

Check whether an uninsured loss could force asset sales or debt: health, disability, liability, property, and dependents' income needs under the user's jurisdiction. A gap here blocks the optimization steps above even when the portfolio looks strong.

### Tax-advantaged filling order

As a generic sequence, subject entirely to the user's jurisdiction: forfeitable employer match first, then the reserve and high-rate debt test, then tax-advantaged contribution room up to the policy, then taxable accounts. Do not state account names, limits, or tax treatment without jurisdiction-specific confirmation; mark them `Insufficient Data` when unknown.

## Product selection

Product criteria are defined once, in the Product selection criteria section of [portfolio-policy.md](portfolio-policy.md). Evaluate products by their role in the policy, never by recent performance, and prefer the smallest set of products that implements the intended exposure reliably.

## Behavioral implementation

Make the sound action easier to continue:

- Automate contributions when appropriate and authorized.
- Use a written review schedule rather than price alerts as the primary trigger.
- Define rebalancing rules before volatility arrives.
- Record why the policy exists and what would justify changing it.
- Treat headlines, forecasts, and relative-performance envy as inputs to examine, not commands to trade.

## Review conclusion

State whether the user should:

- Continue the current policy
- Repair a financial-foundation issue first
- Simplify or reduce costs
- Rebalance according to the written rule
- Update the policy because personal constraints changed
- Gather more data before acting

`Continue the current policy` is a positive conclusion, not a failure to provide advice.
