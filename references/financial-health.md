# Financial Health Diagnosis

Use this reference to judge a financial system, not merely the size of its assets. Read the ledger reference first when the diagnosis depends on balances or flows. Keep whole-system health certification separate from permission for a specific decision.

## Domains

| Domain | Core question | Typical evidence | Failure to avoid |
|---|---|---|---|
| Coverage and data quality | Is the known financial position complete enough for the stated scope? | Account coverage, dates, currencies, unresolved residuals | Calling an incomplete balance sheet healthy |
| Liquidity | Can required near-term spending be met without debt or forced sale? | Liquid assets, required expenses, planned large outflows | Treating volatile investments as guaranteed cash |
| Solvency and obligations | Are debts and fixed commitments supportable? | Debt balances, rates, minimum payments, due dates | Treating principal repayment as consumption or ignoring refinancing risk |
| Cash-flow resilience | Can the system withstand income disruption or expense shock? | Income stability, essential spending, insurance, alternative liquidity | Using a generic emergency-fund multiple as an automatic verdict |
| Income engine and human capital | Can the user keep producing income without unacceptable dependence on one employer, skill, health condition, or industry? | Employment stability, replacement time, health, capability investment, income concentration | Treating salary as a permanent bond or cutting useful capability spending to maximize one month's saving rate |
| Accumulation continuity | Is repeatable surplus created without impairing present stability, and is the passive long-term process continuing? | Multi-month net saving, irregular expenses, post-saving liquidity, stated contribution behavior | Assuming the highest investment rate is always healthiest or inferring an exact fund contribution from ending holdings |
| Portfolio resilience | Can the asset mix survive volatility without breaking the life plan? | Horizon, concentration, currency, policy, loss capacity | Equating recent return with health |
| Behavioral sustainability | Can the user follow the policy under stress? | Prior reactions, complexity, automation, decision frequency | Treating stated risk tolerance as proven behavior |
| Goal alignment | Does the financial structure serve actual life priorities? | Goals, time horizons, Enough, planned transitions | Optimizing net worth while neglecting the purpose of wealth |

## Diagnosis rules

1. State the scope before assigning status: whole system, named domain, or specific decision.
2. Diagnose each relevant domain as `Healthy`, `Watch`, `Action Required`, or `Insufficient Data`.
3. `Insufficient Data` is an epistemic limit, not evidence that the condition is unsafe. It blocks only the conclusion or action for which the missing fact could be decisive.
4. Do not average an `Action Required` liquidity problem against strong long-term assets.
5. Use ratios as evidence, not universal commands. Explain the assumption behind any benchmark.
6. Separate a stock-market decline from permanent impairment and from a liquidity failure.
7. Separate economic-month saving from investment events and native-currency asset changes. Attribute market or currency return only when supporting data exists; the v0.7 workbook alone cannot produce that split.
8. When the user invests most income, test post-contribution liquidity, irregular annual expenses, income stability, capability spending, and the consequence of a severe drawdown before praising the savings rate.
9. Separate the strength of the income engine from the size of the current portfolio. A large portfolio does not repair a fragile earning process when near-term plans still depend on salary.
10. Recommend the smallest repair that restores resilience or accumulation continuity; do not automatically stop a sound long-term policy.

## Whole-system health certification

Use this mode only when judging the user's financial system as a whole. Show every material domain, including coverage and data quality. The overall judgment is the worst domain result, never an average, vote, or weighted blend:

1. If any domain is `Action Required`, the overall judgment names that domain and states `Action Required` overall. Wording such as "overall healthy apart from..." is prohibited.
2. Otherwise, if any material domain is `Insufficient Data`, the overall judgment is capped at `Insufficient Data`. Strengths in diagnosed domains may be noted but cannot certify the whole system.
3. Otherwise, if any domain is `Watch`, the overall judgment is `Watch` and names the watch item most likely to become `Action Required`.
4. Only when every material domain is `Healthy` may the whole system be certified `Healthy`.

For whole-system certification, incomplete balance-sheet coverage is always material because unknown accounts or obligations can change multiple domains. A partial assessment must be labeled partial and must not be described as overall `Healthy`.

## Specific-decision permission

Use this mode when the user asks whether to take a defined action. First state the action, amount, timing, funding source, reversibility, and relevant horizon. Then identify only the domains and facts that could materially change that action.

Return one of:

- **Permitted under stated conditions:** relevant hard boundaries are supported and no relevant domain is `Action Required`.
- **Not Permitted:** the action would cross a legal, solvency, required-liquidity, loss-capacity, or other controlling boundary.
- **Insufficient Data:** a missing or conflicting fact could change permission; name the smallest evidence needed.

A missing fact outside the decision's causal path may prevent whole-system certification without blocking the specific decision. For example, an unresolved dormant account can cap an overall diagnosis while leaving a small, reversible purchase permissible if its funding, obligations, liquidity, and downside are adequately known.

This is not permission to ignore uncertainty. If an omitted account could contain debt, alter required liquidity, change the funding source, or otherwise reverse the decision, it remains relevant and blocks permission. Local permission also does not imply that the whole system is `Healthy`.

## Output

For a whole-system diagnosis, provide a domain table with status, evidence, reasoning, and next trigger. Then state:

- the strongest part of the system;
- the first vulnerability that could break the long-term plan;
- the single highest-priority repair or confirmation;
- which missing fact prevents a stronger conclusion;
- the explicitly labeled whole-system judgment.

For a specific decision, provide the decision scope, relevant domains, hard-boundary checks, assumptions or unknowns, permission result, conditions, and review trigger. Do not issue a numeric health score in either mode.
