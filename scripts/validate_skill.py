#!/usr/bin/env python3
"""Static validation for Personal Finance OS references and privacy rules."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_MISSION_TERMS = ["wage-led capital accumulation", "human capital", "financial-capital"]
REQUIRED_V07_TERMS = ["five-sheet", "native-currency", "04 Investment Flow", "monthly passive"]


def markdown_files() -> list[Path]:
    return sorted(ROOT.glob("*.md")) + sorted((ROOT / "references").glob("*.md")) + sorted(
        (ROOT / "examples").glob("*.md")
    )


def main() -> None:
    issues: list[str] = []
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not match:
        issues.append("SKILL.md frontmatter is missing")
    else:
        keys = [line.split(":", 1)[0].strip() for line in match.group(1).splitlines() if ":" in line]
        metadata = {
            line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
            for line in match.group(1).splitlines()
            if ":" in line
        }
        if set(keys) != {"name", "description"}:
            issues.append("SKILL.md frontmatter must contain only name and description")
        if metadata.get("name") != "personal-finance-os":
            issues.append("unexpected skill name")

    lower_skill = skill_text.lower()
    for term in REQUIRED_MISSION_TERMS:
        if term not in lower_skill:
            issues.append(f"mission term missing from SKILL.md: {term}")
    combined_contract = skill_text + (ROOT / "references" / "ledger-and-net-worth.md").read_text(encoding="utf-8")
    for term in REQUIRED_V07_TERMS:
        if term.lower() not in combined_contract.lower():
            issues.append(f"v0.7 contract term missing: {term}")

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).exists():
                issues.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")

    linked_references = set(re.findall(r"references/([a-z0-9-]+\.md)", skill_text))
    actual_references = {path.name for path in (ROOT / "references").glob("*.md")}
    for missing_reference in sorted(actual_references - linked_references):
        issues.append(f"reference is not linked directly from SKILL.md: {missing_reference}")

    principle_files = [
        ROOT / "references" / "philosophy-constitution.md",
        ROOT / "references" / "bogle-core-philosophy.md",
        ROOT / "references" / "buffett-munger-principles.md",
    ]
    principle_text = "\n".join(path.read_text(encoding="utf-8") for path in principle_files)
    expected_ids = [*(f"FC-{i:02d}" for i in range(1, 12)), *(f"BG-{i:02d}" for i in range(1, 11)), *(f"BM-{i:02d}" for i in range(1, 11))]
    for principle_id in expected_ids:
        if principle_text.count(f"`{principle_id}`") < 1:
            issues.append(f"principle card missing: {principle_id}")

    legacy_refs = [
        "03 Important Events", "04 Monthly Close", "six-sheet ledger",
        "four-sheet", "v0.4 workbook", "The workbook has no event log",
        "FX TO CNY", "CURRENT WEIGHT",
    ]
    active_docs = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
    )
    for phrase in legacy_refs:
        if phrase in active_docs:
            issues.append(f"legacy workbook reference remains: {phrase}")

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)
    print("skill static checks: PASS")


if __name__ == "__main__":
    main()
