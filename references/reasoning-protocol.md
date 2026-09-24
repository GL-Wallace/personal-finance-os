# Financial Reasoning Protocol

Use this protocol for substantial questions about financial condition, spending, saving, portfolio policy, or active-investment decisions. It keeps evidence, philosophy, diagnosis, and action separate.

## Contents

- Protocol depth and question classification
- Reasoning sequence and evidence model
- Diagnostic states and answer contracts
- Refusal to overreach

## Select the protocol depth

Use the smallest protocol that preserves the decision:

| Protocol | Use when | Evidence treatment |
|---|---|---|
| `Light` | Ledger facts, monthly reviews, spending questions, one-domain diagnoses, and reversible personal decisions | Separate `Known`, `User-stated`, `Derived`, and `Unknown`; state the material date and gap without producing a source-quality matrix |
| `Full` | Cross-domain or irreversible decisions, conflicting external evidence, regulated or jurisdiction-specific claims, and active-company research | Use the complete proposition taxonomy and source-quality fields below |

Escalate from `Light` to `Full` when an external claim controls the decision, sources conflict, or the downside is hard to reverse. Do not use the full matrix merely to make an ordinary answer look rigorous.

## Question classification

Classify the request before calculating:

| Type | Core output |
|---|---|
| Fact | What happened or what is currently owned or owed |
| Diagnostic | Whether a domain is healthy, vulnerable, or unresolved, and why |
| Decision | The action that best fits the user's purpose and constraints |
| Policy | A durable rule for future repeated decisions |
| Active exception | Whether a deviation from the passive default clears the exception burden |

If multiple types apply, answer in that order. Do not let an action recommendation rewrite the facts used to justify it.

## Reasoning sequence

1. **Decision context:** state the actual question, period, base currency when relevant, and decision deadline.
2. **Relevant evidence:** identify each material proposition, its period, proposition type, source quality, and conflicts.
3. **Assumptions and gaps:** identify missing or unresolved inputs that could change the conclusion.
4. **Governing boundaries and principles:** first apply life, law, solvency, liquidity, and loss-capacity boundaries; then select the smallest set of constitutional and domain principle IDs that controls the feasible choices.
5. **Diagnosis:** compare the evidence with the principles and the user's own commitments; do not use a peer average as a hidden goal.
6. **Counterfactuals:** compare the proposed action with doing nothing, continuing policy, or choosing the passive baseline.
7. **Conclusion:** use conditional language proportional to evidence and keep value choices distinct from factual uncertainty.
8. **Action and review trigger:** state the smallest useful next action and the fact, user preference, or date that should reopen the decision.

## Full two-dimensional evidence model

Classify each material proposition on two independent dimensions. Source authority does not determine proposition type, and proposition type does not establish source quality.

### Dimension 1 — Proposition type

- `Observed / reported fact`: a dated, externally observable or accounting value directly supported by a traceable record for the stated period. Forecasts, explanations, and opinions do not enter this category merely because they appear in the same document.
- `User statement`: personal circumstances, goals, preferences, or off-ledger information supplied by the user but not independently verified.
- `Management claim`: a company's explanation, forecast, characterization, target, or causal assertion, including one in an official filing or presentation.
- `Derived estimate`: a calculation or range produced from disclosed inputs and method.
- `Assumption`: a provisional input introduced to continue analysis; it must be explicit and replaceable.
- `Judgment`: an interpretation or decision under the governing principles.
- `Unknown`: a material proposition for which usable evidence is absent, unresolved, stale, or irreconcilably conflicting.

### Dimension 2 — Source quality

Record the fields that are material to the decision:

- `Authority level`: source type and proximity to the underlying record, using [source-registry.md](source-registry.md).
- `Source date` and `as-of date`: when the source was published and the period or instant the proposition describes.
- `Independent`: whether the source is independent of the party making the claim.
- `Cross-verified`: whether a materially independent source supports the same proposition.
- `Conflict state`: `None`, `Resolved`, or `Conflicting`, with the reason for any resolution.

### Evidence transition rules

1. No proposition is upgraded solely because its source is Level A. A management forecast in an audited filing remains a `Management claim`.
2. A `User statement` becomes an `Observed / reported fact` only for the portion supported by a traceable record; the unsupported portion retains its original label.
3. A `Derived estimate` inherits the uncertainty, age, and conflict limitations of every material input. Calculation does not cleanse weak evidence.
4. When sources conflict, compare proposition type, period, methodology, independence, freshness, and authority. If the conflict could change the decision and cannot be resolved, label it `Conflicting` and treat the proposition as `Unknown` for that decision.
5. Never fill an `Unknown` with an unstated assumption. State the smallest evidence set that could resolve it.
6. Evidence weakness changes conclusion strength, not the constitutional order or safety boundary.

## Diagnostic and decision states

Use domain statuses rather than a composite score:

- `Healthy`: no material intervention is indicated under the relevant present facts.
- `Watch`: vulnerability exists, but immediate repair is not required.
- `Action Required`: a material risk can impair basic obligations or the long-term plan.
- `Insufficient Data`: the available evidence cannot support the requested diagnosis. This is an epistemic limit, not proof that the condition is unsafe.

For active-investment research, map the same evidence limit to `Unclear` at the affected test. At the research-conclusion level, use `Watchlist` only when CR-6 valuation is the sole unresolved blocker and every other applicable research gate clears; otherwise, a material unresolved research gate maps to `Needs More Data`. Do not use `Insufficient Data`, `Unclear`, `Watchlist`, or `Needs More Data` as claims that the underlying asset or financial condition has failed.

Never convert these statuses into a numeric health score unless a user supplies and understands an explicit model. A precise score can hide non-compensating risks.

## Answer contracts

### Light contract

Lead with the answer, then provide:

1. the relevant known and derived facts;
2. the smallest material unknown;
3. the controlling boundary or principle;
4. the next action or review trigger.

Use no more structure than the question needs. Do not print internal proposition labels when plain wording is clearer.

### Full contract

For a substantial answer, include:

1. **Question and decision context**
2. **Evidence-classified facts, statements, and claims**
3. **Assumptions and missing evidence**
4. **Governing boundaries and principles**
5. **Assessment by relevant domain**
6. **Recommendation and tradeoffs**
7. **Review trigger**

The user-facing answer may compress sections when the issue is simple, but the reasoning must preserve them. Cite primary sources when explaining doctrine; do not flood ordinary answers with citations when principle names and internal traceability are sufficient.

## Refusal to overreach

Stop or narrow the conclusion when:

- account coverage is materially incomplete for the requested conclusion;
- a spending judgment lacks goals, obligations, or income context;
- a safety judgment lacks liquid assets and required expenses;
- a portfolio recommendation lacks time horizon and capacity for loss;
- a company valuation lacks current price, diluted share count, or defensible economics;
- jurisdiction-specific tax or legal treatment is material but unverified.

State the smallest missing evidence set rather than requesting a complete financial biography. Missing evidence outside the scope of a specific decision may prevent a whole-system certification, but it does not automatically block that decision.
