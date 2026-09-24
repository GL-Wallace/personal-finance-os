#!/usr/bin/env python3
"""Read-only validator for a Personal Finance OS v0.7 XLSX export.

Reports aggregate checks only. It never writes the workbook or prints account
names, holding names, quantities, prices, cost bases, or personal notes.
"""

from __future__ import annotations

import argparse
import calendar
import json
import math
import re
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

try:
    from openpyxl import load_workbook
except ImportError as exc:  # pragma: no cover
    raise SystemExit("openpyxl is required to validate an XLSX export") from exc


REQUIRED_SHEETS = [
    "00 Dashboard", "01 Rules", "02 Balance Sheet",
    "03 Monthly History", "04 Investment Flow",
]
BALANCE_HEADERS = [
    "ACCOUNT", "ASSET NAME", "TICKER / CODE", "CURRENCY", "QUANTITY",
    "AVG COST PRICE", "CURRENT PRICE", "CURRENT VALUE LOCAL", "NOTES",
]
MONTH_HEADERS = [
    "ECONOMIC MONTH-END", "SALARY CNY", "OTHER EARNED CNY",
    "LIVING EXPENSE CNY", "OTHER EXTERNAL FLOW CNY", "NET SAVING CNY",
    "CNY ASSETS", "USD ASSETS", "HKD ASSETS", "CLOSE STATUS", "NOTES",
]
FLOW_HEADERS = [
    "EVENT DATE", "ACTION", "ASSET / PURPOSE", "TICKER", "CURRENCY",
    "AMOUNT LOCAL", "QUANTITY", "CNY PAID / RECEIVED (FX ONLY)", "NOTES",
]
EXCEPTION_HEADERS = [
    "ASSET", "TICKER", "CURRENCY", "STRATEGY ROLE", "HOLDING RATIONALE",
    "MAXIMUM WEIGHT", "EXIT CONDITION", "REVIEW DATE", "DECISION",
]
ALLOWED_ACTIONS = {
    "Passive Buy", "Passive Sell", "Active Buy", "Active Sell", "FX Buy",
    "FX Sell", "Dividend", "Interest", "Fee",
}
ALLOWED_CURRENCIES = {"CNY", "USD", "HKD"}
ALLOWED_CLOSE_STATES = {
    "Closed", "Awaiting Month-End Snapshot", "Awaiting Monthly Inputs",
    "Ready to Close",
}
PASSIVE_RULE_PATTERN = re.compile(
    r"^Monthly\s+(?P<asset>.+?)\s+Contribution\s+\((?P<currency>[A-Z]{3})\)$"
)


def is_formula(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("=")


def number(value: Any, field: str, *, blank_zero: bool = True) -> float:
    if value in (None, ""):
        if blank_zero:
            return 0.0
        raise ValueError(f"{field} must be numeric")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be numeric or blank")
    return float(value)


def calendar_date(value: Any, field: str) -> date:
    if isinstance(value, datetime):
        value = value.date()
    if not isinstance(value, date):
        raise ValueError(f"{field} must be a real date")
    return value


def month_end(value: Any) -> date:
    value = calendar_date(value, "economic month-end")
    if value.day != calendar.monthrange(value.year, value.month)[1]:
        raise ValueError("ECONOMIC MONTH-END is not the final calendar date")
    return value


def compute_net_saving(salary: Any, other: Any, expense: Any, external: Any) -> float:
    return number(salary, "salary") + number(other, "other earned") - number(
        expense, "living expense"
    ) + number(external, "other external flow")


def find_row_by_first_cell(sheet: Any, label: str, start: int = 1) -> int | None:
    for row in range(start, sheet.max_row + 1):
        if str(sheet.cell(row, 1).value or "").strip() == label:
            return row
    return None


def parse_passive_policy(constraints: dict[str, Any]) -> dict[str, Any] | None:
    """Parse a user-defined monthly passive contribution rule by label."""
    for label, value in constraints.items():
        match = PASSIVE_RULE_PATTERN.fullmatch(label)
        if not match or "[" in label or "]" in label:
            continue
        target = number(value, "monthly passive contribution", blank_zero=False)
        if target <= 0:
            raise ValueError("monthly passive contribution policy must be positive")
        return {
            "label": label,
            "asset_key": match.group("asset").strip(),
            "currency": match.group("currency"),
            "target": target,
        }
    return None


def ticker_matches_policy(ticker: str, asset_key: str) -> bool:
    """Match either an exact ticker or a market-suffixed form such as FUND.US."""
    ticker_key = ticker.strip().upper()
    policy_key = asset_key.strip().upper()
    return ticker_key == policy_key or ticker_key.startswith(f"{policy_key}.")


def validate(path: Path) -> dict[str, Any]:
    formulas = load_workbook(path, data_only=False, read_only=False)
    values = load_workbook(path, data_only=True, read_only=False)
    issues: list[str] = []
    warnings: list[str] = []

    missing = [name for name in REQUIRED_SHEETS if name not in formulas.sheetnames]
    if missing:
        issues.append("one or more required v0.7 sheets are missing")
        return {"status": "FAIL", "issues": issues, "warnings": warnings,
                "missing_sheet_count": len(missing)}
    if formulas.sheetnames[:5] != REQUIRED_SHEETS:
        warnings.append("the five required sheets are not the first five tabs in canonical order")

    dashboard_v = values["00 Dashboard"]
    rules_f, rules_v = formulas["01 Rules"], values["01 Rules"]
    balance_f, balance_v = formulas["02 Balance Sheet"], values["02 Balance Sheet"]
    month_f, month_v = formulas["03 Monthly History"], values["03 Monthly History"]
    flow_f, flow_v = formulas["04 Investment Flow"], values["04 Investment Flow"]

    if [balance_f.cell(4, c).value for c in range(1, 10)] != BALANCE_HEADERS:
        issues.append("02 Balance Sheet row 4 headers do not match the v0.7 contract")
    if [month_f.cell(4, c).value for c in range(1, 12)] != MONTH_HEADERS:
        issues.append("03 Monthly History row 4 headers do not match the v0.7 contract")
    if [flow_f.cell(4, c).value for c in range(1, 10)] != FLOW_HEADERS:
        issues.append("04 Investment Flow row 4 headers do not match the v0.7 contract")

    constraint_header = find_row_by_first_cell(rules_f, "PERSONAL CONSTRAINT")
    exception_banner = find_row_by_first_cell(rules_f, "ACTIVE INVESTMENT EXCEPTIONS")
    constraints: dict[str, Any] = {}
    if constraint_header is None or exception_banner is None or exception_banner <= constraint_header:
        issues.append("01 Rules section labels are missing or out of order")
        exception_header = None
    else:
        for row in range(constraint_header + 1, exception_banner):
            label = str(rules_v.cell(row, 1).value or "").strip()
            if label:
                constraints[label] = rules_v.cell(row, 2).value
        exception_header = exception_banner + 1
        if [rules_f.cell(exception_header, c).value for c in range(1, 10)] != EXCEPTION_HEADERS:
            issues.append("01 Rules active-exception headers do not match the v0.7 contract")

    try:
        passive_policy = parse_passive_policy(constraints)
    except ValueError as exc:
        issues.append(str(exc))
        passive_policy = None
    if passive_policy is None:
        warnings.append(
            "monthly passive contribution policy is absent or still uses template placeholders"
        )

    try:
        snapshot_date = calendar_date(balance_v["B2"].value, "balance-sheet snapshot date")
    except ValueError as exc:
        issues.append(str(exc))
        snapshot_date = None

    currency_totals: dict[str, float] = defaultdict(float)
    balance_tickers: set[str] = set()
    position_count = 0
    row = 5
    while balance_f.cell(row, 1).value not in (None, ""):
        position_count += 1
        currency = str(balance_v.cell(row, 4).value or "").strip()
        if currency not in ALLOWED_CURRENCIES:
            issues.append(f"balance-sheet row {row} has an unsupported currency")
        try:
            expected = number(balance_v.cell(row, 5).value, "quantity") * number(
                balance_v.cell(row, 7).value, "current price"
            )
            cached = number(balance_v.cell(row, 8).value, "current value")
            if not math.isclose(expected, cached, abs_tol=0.02):
                issues.append(f"balance-sheet row {row} value does not equal quantity × price")
            currency_totals[currency] += cached
        except ValueError as exc:
            issues.append(f"balance-sheet row {row}: {exc}")
        if not is_formula(balance_f.cell(row, 8).value):
            issues.append(f"balance-sheet row {row} current value is not a formula")
        ticker = str(balance_v.cell(row, 3).value or "").strip()
        if ticker:
            balance_tickers.add(ticker)
        row += 1

    exception_count = 0
    orphan_exceptions = 0
    if exception_header is not None:
        row = exception_header + 1
        while rules_f.cell(row, 1).value not in (None, ""):
            exception_count += 1
            ticker = str(rules_v.cell(row, 2).value or "").strip()
            if ticker and ticker not in balance_tickers:
                orphan_exceptions += 1
            if not is_formula(rules_f.cell(row, 3).value):
                issues.append(f"active-exception row {row} currency is not a formula")
            row += 1
    if orphan_exceptions:
        warnings.append(f"{orphan_exceptions} active-exception rows have no matching balance-sheet ticker")

    month_count = 0
    closed_month_count = 0
    previous_date: date | None = None
    monthly_assets: dict[date, dict[str, float]] = {}
    row = 5
    while month_f.cell(row, 1).value not in (None, ""):
        month_count += 1
        try:
            current_date = month_end(month_v.cell(row, 1).value)
            if previous_date and current_date <= previous_date:
                issues.append(f"monthly-history row {row} is not strictly chronological")
            previous_date = current_date
        except ValueError as exc:
            issues.append(f"monthly-history row {row}: {exc}")
            current_date = None

        status = str(month_v.cell(row, 10).value or "").strip()
        legacy_incomplete = row == 5 and not status
        if status and status not in ALLOWED_CLOSE_STATES:
            issues.append(f"monthly-history row {row} has an invalid close state")
        if status == "Closed":
            closed_month_count += 1
        if legacy_incomplete:
            warnings.append("earliest monthly-history row uses legacy incomplete-close semantics")
        else:
            if not is_formula(month_f.cell(row, 6).value):
                issues.append(f"monthly-history row {row} net saving is not a formula")
            if status == "Closed" and (
                month_v.cell(row, 2).value in (None, "") or month_v.cell(row, 4).value in (None, "")
            ):
                issues.append(f"closed monthly-history row {row} lacks salary or living expense")
            try:
                expected = compute_net_saving(
                    month_v.cell(row, 2).value, month_v.cell(row, 3).value,
                    month_v.cell(row, 4).value, month_v.cell(row, 5).value,
                )
                cached = month_v.cell(row, 6).value
                if cached not in (None, "") and not math.isclose(
                    expected, number(cached, "net saving"), abs_tol=0.02
                ):
                    issues.append(f"monthly-history row {row} net saving does not reconcile")
            except ValueError as exc:
                issues.append(f"monthly-history row {row}: {exc}")

        asset_values = month_v.cell(row, 7).value, month_v.cell(row, 8).value, month_v.cell(row, 9).value
        if status == "Closed" and any(v in (None, "") for v in asset_values):
            warnings.append(f"closed monthly-history row {row} lacks one or more frozen currency totals")
        if current_date and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in asset_values):
            monthly_assets[current_date] = dict(zip(("CNY", "USD", "HKD"), map(float, asset_values)))
        row += 1

    same_date_status = "NOT_CHECKED_NO_SAME_DATE"
    if snapshot_date in monthly_assets:
        same_date_status = "PASS"
        for currency in ("CNY", "USD", "HKD"):
            if not math.isclose(currency_totals.get(currency, 0.0), monthly_assets[snapshot_date][currency], abs_tol=0.02):
                same_date_status = "FAIL"
                issues.append("same-date native-currency asset totals do not reconcile")
                break

    event_count = 0
    passive_actual_by_month: dict[str, float] = defaultdict(float)
    row = 5
    while flow_f.cell(row, 1).value not in (None, ""):
        event_count += 1
        try:
            event_date = calendar_date(flow_v.cell(row, 1).value, "investment-flow event date")
        except ValueError as exc:
            issues.append(f"investment-flow row {row}: {exc}")
            event_date = None
        action = str(flow_v.cell(row, 2).value or "").strip()
        currency = str(flow_v.cell(row, 5).value or "").strip()
        ticker = str(flow_v.cell(row, 4).value or "").strip()
        if action not in ALLOWED_ACTIONS:
            issues.append(f"investment-flow row {row} has an invalid action")
        if currency not in ALLOWED_CURRENCIES:
            issues.append(f"investment-flow row {row} has an invalid currency")
        try:
            amount = number(flow_v.cell(row, 6).value, "event amount", blank_zero=False)
            if amount <= 0:
                issues.append(f"investment-flow row {row} amount must be positive")
        except ValueError as exc:
            issues.append(f"investment-flow row {row}: {exc}")
            amount = 0.0
        if action in {"Passive Buy", "Passive Sell", "Active Buy", "Active Sell"}:
            if not ticker:
                issues.append(f"investment-flow row {row} buy/sell event lacks a ticker")
            if flow_v.cell(row, 7).value in (None, ""):
                warnings.append(f"investment-flow row {row} buy/sell event lacks quantity")
        if action in {"FX Buy", "FX Sell"} and flow_v.cell(row, 8).value in (None, ""):
            warnings.append(f"investment-flow row {row} FX event lacks CNY paid/received")
        if (
            passive_policy
            and action == "Passive Buy"
            and ticker_matches_policy(ticker, passive_policy["asset_key"])
            and currency == passive_policy["currency"]
            and event_date
        ):
            passive_actual_by_month[event_date.strftime("%Y-%m")] += amount
        row += 1

    dashboard_status = "PASS"
    for cell, currency in (("B6", "CNY"), ("B7", "USD"), ("B8", "HKD")):
        cached = dashboard_v[cell].value
        if isinstance(cached, (int, float)) and not math.isclose(
            float(cached), currency_totals.get(currency, 0.0), abs_tol=0.02
        ):
            dashboard_status = "FAIL"
            issues.append("dashboard native-currency total does not reconcile to the balance sheet")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "contract": "Personal Finance OS v0.7",
        "position_count": position_count,
        "economic_month_count": month_count,
        "closed_month_count": closed_month_count,
        "investment_event_count": event_count,
        "active_exception_count": exception_count,
        "native_currency_totals": {k: round(currency_totals.get(k, 0.0), 2) for k in ("CNY", "USD", "HKD")},
        "same_date_currency_reconciliation": same_date_status,
        "dashboard_reconciliation": dashboard_status,
        "monthly_passive_policy": (
            {
                "label": passive_policy["label"],
                "asset_key": passive_policy["asset_key"],
                "currency": passive_policy["currency"],
                "target": round(passive_policy["target"], 2),
            }
            if passive_policy
            else None
        ),
        "passive_buys_by_actual_month": {
            k: round(v, 2) for k, v in sorted(passive_actual_by_month.items())
        },
        "issues": issues,
        "warnings": warnings,
    }
    formulas.close()
    values.close()
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path, help="Path to a v0.7 XLSX export")
    args = parser.parse_args()
    if not args.workbook.is_file():
        parser.error("workbook path does not exist or is not a file")
    try:
        report = validate(args.workbook)
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2) from exc
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
