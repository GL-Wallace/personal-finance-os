# Native-Currency Asset Ledger Method

Use this reference as the financial fact layer for the Personal Finance OS v0.7 workbook. The workbook is a five-sheet, balance-sheet-first system: current holdings, economic-month saving, and actual investment/FX events are recorded separately. It is not a transaction-level bank ledger and it does not produce one consolidated net-worth number.

The Skill may interpret and validate the workbook, and may write only when the user explicitly authorizes the specific edit. Workbook access never implies authority to trade, move money, or synchronize an institution.

## Governing semantics

- **Native currencies stay separate.** CNY, USD, and HKD asset totals must not be added together. A consolidated value, total portfolio weight, or cross-currency return is `Unavailable` unless the user supplies an explicit, dated FX basis outside the current contract.
- **The Balance Sheet is the position snapshot.** It records quantity, average cost, current price, and local-currency value as of one date.
- **Monthly History is an economic-month close.** It records aggregated CNY income, living expense, external flow, net saving, and frozen native-currency asset totals. It is not a trade log.
- **Investment Flow is the event record.** Purchases, sales, FX conversions, dividends, interest, and fees use their actual event dates. A purchase or FX conversion is an internal asset conversion, not income, spending, saving, or return.
- **Rules distinguish policy from evidence.** A contribution target is an intended behavior; Investment Flow shows what actually happened. Report variance rather than backfilling an event.
- **Dashboard is derived and read-only.** Independently recompute its material figures from source sheets.

## Five-sheet contract

| Sheet | Role | Write rule |
|---|---|---|
| `00 Dashboard` | Derived native-currency position, liquidity, and latest close | Never edit |
| `01 Rules` | Personal constraints and active-investment exceptions | User-maintained inputs; derived currency cells stay formulas |
| `02 Balance Sheet` | Current asset facts in local currency | Update at a dated snapshot; value column stays formula-driven |
| `03 Monthly History` | Economic-month inputs, saving, frozen native-currency asset totals, close state | Preserve closed rows; update the current row until it is closed |
| `04 Investment Flow` | Actual investment and FX events | Append actual events; never invent dates or source matching |

Do not require exactly five sheets if harmless additional tabs exist, but all five named tabs are required and their source headers must match. Do not add a new sheet merely to complete an analysis.

## `01 Rules`

Locate both sections by their labels, never by fixed row numbers. New personal constraints can move the exception table.

### Personal constraints

The table has `PERSONAL CONSTRAINT`, `VALUE`, and `PURPOSE` headers. The blank template includes named CNY reserve constraints and a placeholder monthly rule labeled `Monthly [TICKER] Contribution ([CCY])`. Replace both placeholders and enter a positive amount before treating the rule as active.

A monthly passive rule is user-defined, not a Skill default. Parse its asset key and currency from the completed label and its target from the value cell. It does not prove that an FX conversion or purchase occurred. Use matching `Passive Buy` rows in `04 Investment Flow` as execution evidence. If actual investment differs from the target, show the amount and variance and request or use the recorded explanation; do not alter history to make it match.

Target asset weights, an aggregate active ceiling, and a rebalance threshold are not part of the current contract. Keep dependent signals `Unknown` unless the user supplies an applicable policy.

### Active Investment Exceptions

Locate the banner `ACTIVE INVESTMENT EXCEPTIONS`, then the following header row:

`ASSET`, `TICKER`, `CURRENCY`, `STRATEGY ROLE`, `HOLDING RATIONALE`, `MAXIMUM WEIGHT`, `EXIT CONDITION`, `REVIEW DATE`, `DECISION`.

- Match each exception ticker to `02 Balance Sheet` column C. Column `CURRENCY` is derived from that match and must remain a formula.
- Policy write-back fields are `STRATEGY ROLE` through `DECISION` (columns D:I in the current layout).
- Blank or instruction-like entries mean unset, not zero. An exception with a missing rationale, cap, exit condition, or review date remains `Pending Review` for additions.
- The sheet has no current-weight column and the Balance Sheet is native-currency only. Therefore a percentage maximum cannot be mechanically tested as a total-portfolio weight without an explicit dated FX basis. Report the cap and exposure facts by currency; set breach status to `Unknown` rather than fabricating a denominator.
- An exception ticker absent from the Balance Sheet is stale; an active holding that should be governed as an exception but lacks a Rules row is a coverage gap. The Balance Sheet itself no longer carries an active flag, so classification comes from the Rules table and user context.

## `02 Balance Sheet`

Cell `B2` is the snapshot date. Header row 4 is:

| Column | Field | Rule |
|---|---|---|
| A | Account | Entered; never expose unnecessary account details |
| B | Asset name | Entered |
| C | Ticker / code | Entered join key |
| D | Currency | Entered native currency |
| E | Quantity | Entered |
| F | Avg cost price | Entered historical record in currency D |
| G | Current price | Entered snapshot-date price in currency D |
| H | Current value local | Formula: quantity × current price |
| I | Notes | Entered |

For every populated position row, H must remain a formula equivalent to `=IF(OR(E5="",G5=""),"",E5*G5)`. Average cost is not evidence of prospective value and must not drive a hold, add, or sell decision. The workbook currently inventories assets, not liabilities. Do not interpret absence of a liability row as proof that the user has no debt.

## `03 Monthly History`

Header row 4 is:

`ECONOMIC MONTH-END`, `SALARY CNY`, `OTHER EARNED CNY`, `LIVING EXPENSE CNY`, `OTHER EXTERNAL FLOW CNY`, `NET SAVING CNY`, `CNY ASSETS`, `USD ASSETS`, `HKD ASSETS`, `CLOSE STATUS`, `NOTES`.

Economic-month convention:

- Day 1 can finalize the prior month's living-expense total.
- Salary received around day 10 is attributed to that economic month according to the workbook convention.
- Investment and FX events always remain on their actual dates in `04 Investment Flow`; do not shift them into the economic month to manufacture matching.

Net saving is `salary + other earned income - living expense + other external flow`. Column F must be formula-driven for current-contract rows. Columns G:I are native-currency month-end asset snapshots. While a month is open, formulas may preview these values only when `02 Balance Sheet!B2` equals the economic month-end. At close, freeze all three values and set status to `Closed`. Valid workflow states are `Awaiting Month-End Snapshot`, `Awaiting Monthly Inputs`, `Ready to Close`, and `Closed`.

The earliest imported legacy row may be incomplete. Treat it as historical coverage with limited confidence, not as proof of a contract failure. Closed v0.7 rows must have a month-end date, salary, living expense, formula-consistent net saving, and a valid close status; missing frozen asset totals must be disclosed as a historical data gap.

## `04 Investment Flow`

Header row 4 is:

`EVENT DATE`, `ACTION`, `ASSET / PURPOSE`, `TICKER`, `CURRENCY`, `AMOUNT LOCAL`, `QUANTITY`, `CNY PAID / RECEIVED (FX ONLY)`, `NOTES`.

Allowed actions are `Passive Buy`, `Passive Sell`, `Active Buy`, `Active Sell`, `FX Buy`, `FX Sell`, `Dividend`, `Interest`, and `Fee`. Allowed currencies are `CNY`, `USD`, and `HKD`.

- Event date is an actual date. If a legacy distribution has no exact date, preserve the uncertainty in Notes rather than inventing a day.
- Amount is a positive magnitude; action supplies the economic direction.
- Buy/sell events require a ticker, currency, amount, and normally quantity.
- FX rows require the acquired/disposed currency amount and the actual CNY paid or received when known.
- A passive-policy check uses `Passive Buy` plus the asset key and currency parsed from the active monthly rule, grouped by actual calendar month. Do not treat an FX Buy as purchase evidence.
- Dividends and interest are investment cash events, not earned income or external saving. Fees are costs, not living expense unless the user explicitly defines otherwise.

## Supported calculations

- Native-currency assets = sum H grouped by currency D.
- Immediate CNY cash = sum H for ticker `CASH-CNY`.
- CNY defensive reserve = `CASH-CNY` plus the designated low-risk reserve asset(s) defined by the current rules/workbook.
- Reserve/floor = CNY defensive reserve divided by `CNY Defensive Reserve Floor`.
- Immediate cash runway = immediate CNY cash divided by average of the latest up to three populated living-expense totals; state the number of months used.
- Net saving = B + C - D + E in Monthly History.
- Saving rate = net saving divided by salary plus other earned income; state the denominator and suppress when it is zero.
- Contribution adherence for a period = actual qualifying passive buys versus the configured monthly rule. Show asset, currency, target, actual, variance, evidence dates, and explanation status.
- Native-currency asset change = current closed G:I value minus the prior comparable closed value for the same currency. Do not label this investment return because it also includes purchases, sales, distributions, and valuation movement.

Unsupported without additional evidence: consolidated net worth across currencies; total-portfolio or active-position weights; a market/FX return plug or capital bridge; performance attribution separating contributions from market return; verified liabilities or off-ledger assets.

## Reconciliation sequence

1. Confirm the five required tabs and row-4 headers.
2. Locate Rules sections by label and parse constraints by name.
3. Validate the Balance Sheet snapshot date, numeric inputs, formula-driven local values, and native-currency totals.
4. Validate economic-month dates, chronology, saving formulas, and close states. For a same-date Balance Sheet/month-end pair, compare each currency total independently with G:I.
5. Validate Investment Flow dates, actions, currencies, and action-specific required fields.
6. Reconcile the configured passive target with actual qualifying buys by event month; keep policy, FX acquisition, and execution separate.
7. Match exception tickers and derived currencies. Do not calculate cross-currency weights without a dated FX basis.
8. Recompute Dashboard facts from the source sheets and flag mismatches; never repair source data by editing the Dashboard.

State coverage before conclusions. A missing account, stale price, open month, absent event, or unrecorded liability limits only the conclusions it affects. Pending transactions may differ from statements; snapshot prices are dated; distributions and FX can cause cash/position timing differences; cost basis and market value are different concepts; closed historical rows may predate the full v0.7 contract.
