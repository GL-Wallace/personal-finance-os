#!/usr/bin/env python3
"""Validate the synthetic v0.7 fixture and its native-currency identities."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

from validate_ledger import compute_net_saving, parse_passive_policy, ticker_matches_policy


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "examples" / "synthetic-ledger-fixture.json"


def close(actual: float, expected: float, tolerance: float = 0.01) -> None:
    if not math.isclose(actual, expected, abs_tol=tolerance):
        raise AssertionError(f"expected {expected:.2f}, got {actual:.2f}")


def main() -> None:
    data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    policy = parse_passive_policy(data["rules"]["personal_constraints"])
    assert policy is not None
    assert policy["asset_key"] == "SYN-PASSIVE"
    assert policy["currency"] == "USD"
    target = float(policy["target"])
    close(target, 1234.0)

    totals: dict[str, float] = defaultdict(float)
    for position in data["balance_sheet"]["positions"]:
        expected = float(position["quantity"]) * float(position["current_price"])
        close(float(position["current_value_local"]), expected)
        totals[position["currency"]] += expected

    close(totals["CNY"], 79000.0)
    close(totals["USD"], 9000.0)
    close(totals["HKD"], 18500.0)

    for month in data["monthly_history"]:
        saving = compute_net_saving(
            month["salary_cny"], month["other_earned_cny"],
            month["living_expense_cny"], month["other_external_flow_cny"],
        )
        close(saving, float(month["net_saving_cny"]))

    current = data["monthly_history"][-1]
    close(float(current["cny_assets"]), totals["CNY"])
    close(float(current["usd_assets"]), totals["USD"])
    close(float(current["hkd_assets"]), totals["HKD"])

    qualifying = [
        event for event in data["investment_flow"]
        if event["action"] == "Passive Buy"
        and ticker_matches_policy(event["ticker"], policy["asset_key"])
        and event["currency"] == policy["currency"]
        and event["event_date"].startswith("2032-04")
    ]
    actual = sum(float(event["amount_local"]) for event in qualifying)
    close(actual, 1210.0)
    close(actual - target, -24.0)

    fx_events = [event for event in data["investment_flow"] if event["action"] == "FX Buy"]
    assert len(fx_events) == 1
    assert fx_events[0] not in qualifying

    # The contract intentionally supplies no cross-currency conversion basis.
    assert "fx_to_cny" not in data["balance_sheet"]
    assert "net_worth" not in current

    cash = next(
        float(position["current_value_local"])
        for position in data["balance_sheet"]["positions"]
        if position["ticker"] == "CASH-CNY"
    )
    average_expense = sum(
        float(month["living_expense_cny"]) for month in data["monthly_history"]
    ) / len(data["monthly_history"])
    close(cash / average_expense, 8.295454545, tolerance=0.000001)

    print("synthetic fixture: PASS")


if __name__ == "__main__":
    main()
