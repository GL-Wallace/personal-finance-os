# Active Investing Exception

Use this reference only for a deliberate deviation from the Bogle/Bogleheads baseline. Its purpose is to reduce avoidable errors in bounded active capital, not to search continuously for outperformers. First classify the asset with [asset-type-router.md](asset-type-router.md). Do not apply company-analysis logic to a sector fund, an active mutual fund, or a speculative asset.

The exception path is subordinate to [philosophy-constitution.md](philosophy-constitution.md). An attractive company cannot override legal obligations, required liquidity, loss capacity, the user's life purpose, or an active-risk cap.

## Exception burden

The active idea must be compared once with continuing the user's simple, low-cost, diversified policy. It must justify:

- Concentration and permanent-loss risk
- Fees, spreads, taxes, turnover, and liquidity costs
- Research and monitoring burden
- Complexity and new behavioral failure modes
- The probability that the apparent edge is already reflected in price
- Portfolio overlap and opportunity cost

Label speculative elements explicitly. Do not reclassify speculation as long-term investment merely because the user intends to hold it.

## Three separate stages

For an individual company, use the source-governed Buffett–Munger principles in [buffett-munger-principles.md](buffett-munger-principles.md) and execute [active-investment-workflow.md](active-investment-workflow.md). The method uses non-compensating gates, not a weighted score.

1. **Capital eligibility:** determine whether the contemplated capital may take active risk without crossing legal, life, solvency, liquidity, loss-capacity, or portfolio-policy boundaries. Record the passive counterfactual here.
2. **Company research:** determine whether the company earns a bounded exception to the passive default on evidence, comprehension, business quality, stewardship, resilience, valuation, and inversion.
3. **Holding implementation:** determine what to do with an existing position from the research result, current weight, written caps, hard boundaries, and any thesis invalidation.

A result in one stage must not silently decide another. A company can be a `Qualified exception` while its position must be `Reduce to policy`; strong company research cannot make ineligible capital eligible.

For other active assets, use the asset-specific questions in the router while retaining the same capital-eligibility test, exception burden, and separation between research and implementation.

## Capital-eligibility results

- **Eligible:** the proposed active capital clears all hard boundaries, has a named funding source, fits at least one explicit user-approved risk-budget measure, preserves the passive accumulation process, and has been compared with the passive baseline.
- **Not Eligible:** a hard boundary or written active-risk limit would be breached. Company quality cannot cure this result.
- **Insufficient Data:** a fact that could change eligibility is unknown. Name the smallest evidence needed; do not assume eligibility.

Capital eligibility controls initiation and additions. A later deterioration in liquidity, solvency, loss capacity, or policy fit also feeds the implementation stage for an existing holding.

Treat an approved percentage cap, maximum permanent-loss amount, or months-of-sustainable-surplus limit as a valid active-risk budget when it genuinely bounds the contemplated loss. An aggregate active ceiling is optional; its absence does not waive the need for a usable budget and does not automatically prohibit a small, otherwise bounded decision.

## Company-research conclusions

- **Do Nothing:** adverse evidence means the passive baseline remains superior; the case has failed, not merely remained incomplete.
- **Needs More Data:** material evidence other than price protection is missing, stale, or irreconcilably conflicting.
- **Too Hard:** the business economics or a key permanent-loss path cannot be understood or bounded reliably, even after the relevant evidence is identified.
- **Watchlist:** comprehension and every non-valuation research gate clear, but current price protection is the sole blocker. Do not use `Watchlist` for general evidence gaps.
- **Qualified exception:** every critical research gate passes and every required gate is either `Pass` or validly `Not Applicable`. This permits consideration; it does not require purchase or override capital eligibility.

`Not Applicable` is a gate result, not a research conclusion. It is valid only for a genuinely irrelevant required test, with a written reason, and is excluded rather than treated as either `Pass` or `Fail`.

## Holding-implementation actions

For an existing holding, report one implementation action separately from the company-research conclusion:

- **No Add:** commit no new capital while research is unresolved, the company is not qualified, or capital is not eligible, unless a stronger reduction or exit action applies.
- **Maintain within policy:** the company remains qualified, no invalidation is present, and the position is within all hard boundaries and written caps.
- **Reduce to policy:** the thesis may remain valid, but the current position breaches a hard boundary or written cap. Reduce only as far as needed to restore the boundary; a zero active-risk allowance can require full reduction.
- **Exit on invalidation:** observable evidence establishes that the thesis has failed or the asset no longer qualifies as an investment. A prewritten falsifier is strong evidence but is not the only possible proof of invalidation.

Apply implementation actions in this order: confirmed invalidation; hard-boundary or policy breach; unresolved or unqualified research; qualified and within policy. This makes combinations such as `Qualified exception — Reduce to policy` and `Needs More Data — No Add` explicit and valid.

| Company-research conclusion | Proposed position | Existing holding when no stronger action applies |
|---|---|---|
| `Do Nothing` | Do not buy | `No Add`; use `Exit on invalidation` only when the evidence also establishes invalidation |
| `Needs More Data` | Do not buy until the named evidence arrives | `No Add` until resolved |
| `Too Hard` | Do not buy | `No Add`, then present the user with a reasoned reduce-or-exit choice unless a boundary or invalidation already determines the action |
| `Watchlist` | Do not buy at the current price | `No Add` while price protection is the sole blocker |
| `Qualified exception` | May buy only if capital is `Eligible` and the approved cap, funding source, and falsifiers are explicit | `Maintain within policy`, unless weight or another boundary requires `Reduce to policy` |

Never infer an implementation action solely from price movement or cost basis. For a non-urgent exit or reduction, present material liquidity, tax, and execution consequences for the user's decision. Legal, solvency, or required-liquidity boundaries may remove that discretion.

## Monitoring and invalidation

Write the thesis and observable invalidation conditions before investing. Monitor operating evidence, not just price. Price decline alone does not invalidate the thesis, and appreciation does not validate it.

Review owner earnings, capital returns, margins, cash conversion, debt, share count, capital allocation, competitive position, management credibility, portfolio weight, and the opportunity cost of returning to the passive baseline. Include ledger write-back fields only when write-back is separately authorized and in scope under the active-investment workflow.
