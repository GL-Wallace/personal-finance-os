# Philosophy and Evidence Source Registry

Use this registry when deriving or applying a philosophical rule or evaluating a company claim. It prevents quotations, anecdotes, secondary commentary, and current market stories from becoming unsupported doctrine or facts.

## Contents

- Source authority
- Bogle, Bogleheads, Buffett, and Munger roots
- Principle-card schema
- Company-research hierarchy and evidence-age rules

## Source authority

Authority level describes the source's type and proximity to the underlying record. It does **not** determine whether a proposition is a fact, claim, estimate, or judgment.

| Level | Source type | Permitted use |
|---|---|---|
| A | Author's books, official archives, audited filings, official shareholder letters, official meeting recordings, regulatory records, and direct company disclosures | Establish doctrine from the author's own work or report dated company records; classify forecasts, explanations, and opinions separately |
| B | Authorized compilations of talks and writings, official implementation manuals, and high-quality independent datasets with disclosed methods | Synthesize principles, practices, or corroborating evidence; verify exact material claims when feasible |
| C | Reputable complete transcripts, interviews, research, and biographies | Add context or empirical support after checking period, method, and conflicts |
| D | News, commentary, social media, quote collections, clips, and summaries | Discovery and context only; never the sole basis for a durable rule or material company proposition |

Use [reasoning-protocol.md](reasoning-protocol.md) to classify proposition type independently. A company presentation is Level A as a direct disclosure but is evidence only that management made the claim; it is not independent proof that the claim is true. Likewise, an audited filing can contain both reported historical figures and forward-looking management claims.

When sources conflict, do not mechanically choose the higher letter grade. First align the proposition, period, units, and methodology; then consider independence, freshness, directness, and authority. Report unresolved material conflicts and cap the affected conclusion rather than selecting the more convenient source.

## Canonical Bogle roots

| ID | Source | Decision use | Authoritative location |
|---|---|---|---|
| `BGL-STC` | *Stay the Course* (John Wiley & Sons, 2018) | Institutional history, long-horizon discipline, simplicity, mission | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-CSMF` | *Common Sense on Mutual Funds* (John Wiley & Sons, 2010 edition listed by the archive) | Fund economics, cost, tax, diversification, selection, persistence | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-LB` | *The Little Book of Common Sense Investing* (John Wiley & Sons, 2017 edition listed by the archive) | Concise indexing and cost-matters case; not a substitute for the broader corpus | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-ENOUGH` | *Enough* (John Wiley & Sons, 2010 edition listed by the archive) | Sufficiency, money, business, life, stewardship | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-COC` | *The Clash of the Cultures* (John Wiley & Sons, 2012) | Investment versus speculation, ownership, financial-industry incentives | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-JBOI` | *John Bogle on Investing: The First 50 Years* (McGraw-Hill, 2000) | Return sources, costs, governance, owner orientation | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-DCI` | *Don't Count On It!* (John Wiley & Sons, 2010) | Forecast humility, historical evidence, promises, false precision | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-BSC` | *The Battle for the Soul of Capitalism* (Yale University Press, 2005) | Fiduciary duty, owners' capitalism, agency conflict | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-CHAR` | *Character Counts* (McGraw-Hill, 2002) | Character, trust, responsibility, institutional conduct | [Bogle Archive](https://boglecenter.net/bogle-archive/) |
| `BGL-ARCH` | John C. Bogle speeches, papers, testimony, and letters | Resolve themes across works and preserve original context | [Official archive](https://boglecenter.net/bogle-archive/) |
| `BGL-BLOG` | The Bogle eBlog | Late speeches, memos, and public commentary | [John C. Bogle site](https://johncbogle.com/wordpress/) |

Books are primary intellectual sources. Record edition and chapter or section when a principle depends on a specific passage. Do not invent page numbers or reproduce extended copyrighted text.

## Bogleheads implementation roots

| ID | Source | Decision use | Authority boundary |
|---|---|---|---|
| `BH-GUIDE` | Taylor Larimore et al., *The Bogleheads' Guide to Investing* | Practical sequence for saving, allocation, product selection, taxes, and discipline | Implementation guide; does not outrank the Bogle constitution |
| `BH-CENTER` | John C. Bogle Center for Financial Literacy resources | Continuing financial-literacy and Bogleheads educational material | Secondary implementation context; distinguish named contributors from Bogle himself |

## Canonical Buffett–Munger roots

| ID | Source | Decision use | Official location |
|---|---|---|---|
| `BRK-LTR` | Berkshire Hathaway shareholder letters | Owner orientation, business quality, capital allocation, valuation, risk, temperament | <https://www.berkshirehathaway.com/letters/letters.html> |
| `BRK-OM` | Berkshire Hathaway Owner's Manual | Long-term ownership, per-share intrinsic value, candor, leverage, acquisition discipline | <https://www.berkshirehathaway.com/owners.html> |
| `BRK-AR` | Berkshire Hathaway annual reports and meeting materials | Application of the principles to actual businesses and capital allocation | <https://www.berkshirehathaway.com/reports.html> |
| `DJCO` | Daily Journal official investor materials | Munger's governance, incentives, patience, and decision examples | <https://ir.dailyjournal.com/> |
| `PCA` | *Poor Charlie's Almanack*, authorized compilation | Mental models, inversion, incentives, and psychological misjudgment | <https://www.stripe.press/poor-charlies-almanack> |

These sources define an intellectual lineage, not a personality imitation exercise. Summarize in original language; do not reproduce extended copyrighted passages.

## Principle-card schema

Every durable rule must contain:

```yaml
id: stable-id
authority: constitutional | default | implementation | active-exception
principle: original-language statement
scope: [decisions it governs]
source_roots: [registry IDs]
source_locator: [edition plus chapter/section, or document title/date when the rule is explained to the user]
operational_rule: [observable effect on the answer]
exception_or_boundary: [when the rule does not decide the case]
prohibited_inference: [common overreach]
```

Reject a proposed card when it is only a slogan, lacks a primary root, duplicates an existing rule, or cannot change a decision. The owning `FC`, `BG`, or `BM` table supplies authority, scope, rule, boundary or hard-stop, prohibited inference, and source roots. When a principle materially controls a user-facing conclusion, add a specific locator from the source itself; a general archive homepage is a discovery root, not passage-level evidence. Never invent a chapter, page, speech title, or meeting date.

## Company-research hierarchy

For a specific company, collect evidence in this order while seeking independent corroboration where it could change the decision:

1. Audited annual reports and regulatory filings
2. Interim reports and regulatory announcements
3. Official earnings materials, investor presentations, and product disclosures
4. Direct competitor and customer filings for cross-checks
5. Independent industry data with disclosed methodology
6. Reputable reporting for context

For every material proposition, record: `proposition`, `proposition type`, `period or as-of date`, `source`, `source date`, `authority level`, `independent`, `cross-verified`, `conflict state`, and `uncertainty`. Never mix a historical ledger price with a live market price or present management guidance as realized performance.

## Evidence-age rules

These defaults are mechanical review triggers, not universal claims that every input expires at the same speed. Override a default only with a stated, decision-relevant reason.

1. **Price provenance.** A price, NAV, or exchange rate without both a source and an as-of date makes the valuation test `Unclear` automatically, regardless of how confident the surrounding analysis feels.
2. **Ledger prices are dated evidence.** A price read from `02 Balance Sheet` (unit price column H) is the stated snapshot price as of the snapshot date in `B2`, never a current market price. Using it as current makes the valuation test `Unclear` even when the balance sheet itself reconciles perfectly.
3. **Filing freshness.** Treat an audited annual report older than **6 months** without a later interim report or regulatory announcement as a default update trigger. Cap current-fact and valuation tests at `Unclear` when the uncovered period could materially change the decision. A stated reason may justify a different interval for slow- or fast-changing inputs, but confidence alone may not.
4. **Fast-changing inputs.** Share count, capital structure, cash position, and other decision-sensitive inputs must use the latest material disclosure. A superseding placement, convertible issuance, acquisition, disposal, or financing event makes the older input stale.
5. **Analysis date must be stated.** Without an explicit analysis date and evidence cutoff, freshness cannot be assessed and no valuation conclusion may be reached.
6. **Effect of stale evidence.** Name the stale input and the smallest update that would clear it. Staleness limits the conclusion; it is not evidence that the company failed.

## Source discipline

- Separate proposition type from authority level on every material item.
- Use per-share measures when dilution is material.
- Reconcile non-IFRS measures to audited figures before relying on them.
- Keep the analysis date visible; current price, share count, and filings can expire quickly.
- Prefer independent corroboration for management claims that control a gate.
- Missing, stale, or materially conflicting data makes the affected gate `Unclear`; never fill the gap with an estimate presented as fact. If CR-6 valuation is the sole unresolved blocker and every other applicable research gate clears, conclude `Watchlist`. If another material research gate is unresolved, conclude `Needs More Data`.
- Do not attribute a synthesized rule to Bogle, Buffett, or Munger as if it were a verbatim statement.
- When a book, speech, or meeting appears to conflict with another, preserve context and follow the constitutional hierarchy rather than selecting the more convenient quotation.
