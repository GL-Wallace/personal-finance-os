# Example Prompts

Replace placeholders with redacted data.

## Monthly review

```text
Use $personal-finance-os to review my latest economic month. Recompute CNY net
saving, reconcile CNY/USD/HKD asset totals separately, and compare actual
Passive Buy events with the matching monthly rule in 01 Rules. Keep salary
attribution and investment event dates separate. Give at most three actions.
```

## Wage-led accumulation

```text
Review whether my wage-led accumulation is becoming more resilient. Assess
income continuity, living expense, net saving, cash floors, and execution of
the passive contribution rule. Describe native-currency asset changes without
adding currencies or calling them investment return.
```

## Policy-execution variance

```text
Read the monthly passive-contribution label and target from 01 Rules. For each
calendar month in 04 Investment Flow, total only matching Passive Buy events.
Show the configured asset, currency, target, actual, variance, event dates, and
any recorded explanation.
```

## Data-quality check

```text
Validate this v0.7 workbook before analysis. Check the five required sheets,
source formulas, economic-month close states, same-date native-currency
reconciliation, event-action fields, and exception rows. Do not expose account
names or personal notes in the report.
```

## Portfolio policy

```text
Evaluate whether this proposed policy is simpler, low cost, broadly diversified,
and sustainable. Do not invent target weights or a rebalancing rule. Treat the
configured monthly amount as a contribution rule, not an allocation target.
```

## Individual company exception

```text
Treat this company as a proposed exception to my Bogle/Bogleheads default.
Separate capital eligibility, source-governed Buffett–Munger research, and
holding implementation. Do not use a total score. If current weight requires
cross-currency consolidation and no dated FX basis exists, report it as Unknown.
```

## Financial health and Enough

```text
Diagnose liquidity, solvency, cash-flow resilience, income-engine resilience,
accumulation continuity, portfolio resilience, behavioral sustainability, and
goal alignment without one composite score. Evaluate spending through
affordability, purpose, opportunity cost, sustainability, and Enough.
```
