#!/usr/bin/env python3
"""Fail closed on personal-finance data, private links, credentials, or unsafe files."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_BINARY = {"assets/finance-os-template.xlsx"}
FORBIDDEN_SUFFIXES = {".csv", ".xls", ".xlsm", ".log", ".pem", ".key", ".p12"}
FORBIDDEN_PARTS = {"private", "personal-data", "exports", "local-ledgers", "credentials", "secrets"}
SAFE_EMAIL_DOMAINS = {"users.noreply.github.com"}
MAX_TEXT_BYTES = 2_000_000

CONTENT_PATTERNS = {
    "private Google spreadsheet URL": re.compile(
        r"https?://docs\.google\.com/spreadsheets/d/[A-Za-z0-9_-]+", re.I
    ),
    "private Google Drive file URL": re.compile(
        r"https?://drive\.google\.com/(?:file/d|open\?id=)/?[A-Za-z0-9_-]+", re.I
    ),
    "private-key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "Google API key": re.compile(r"AIza[A-Za-z0-9_-]{30,}"),
    "AWS access key": re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}"),
    "Slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    "JWT-like token": re.compile(
        r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"
    ),
    "real-workbook declaration": re.compile(
        "(?:these cases use the real " + "workbook|ledger facts were supplied by the " + "user)",
        re.I,
    ),
    "personal passive-policy default": re.compile(
        rf"(?:Monthly\s+{'VO' + 'O'}\s+Contribution|{'VO' + 'O'}\.US)", re.I
    ),
}
EMAIL_PATTERN = re.compile(r"[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})", re.I)


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=text)


def unsafe_path(path: str) -> str | None:
    item = Path(path)
    if any(part in FORBIDDEN_PARTS for part in item.parts):
        return "private-data directory"
    if item.name.startswith(".env"):
        return "environment file"
    if item.suffix.lower() == ".xlsx" and path not in ALLOWED_BINARY:
        return "unapproved workbook"
    if item.suffix.lower() in FORBIDDEN_SUFFIXES:
        return f"forbidden {item.suffix.lower()} file"
    return None


def scan_text(label: str, text: str) -> list[str]:
    issues: list[str] = []
    for finding, pattern in CONTENT_PATTERNS.items():
        if pattern.search(text):
            issues.append(f"{label}: {finding}")
    for match in EMAIL_PATTERN.finditer(text):
        domain = match.group(1).lower()
        if domain not in SAFE_EMAIL_DOMAINS:
            issues.append(f"{label}: non-noreply email")
    return issues


def current_tree() -> list[str]:
    issues: list[str] = []
    for path in git("ls-files", "--cached", "--others", "--exclude-standard", "-z").split("\0"):
        if not path:
            continue
        reason = unsafe_path(path)
        if reason:
            issues.append(f"{path}: {reason}")
            continue
        source = ROOT / path
        if not source.is_file() or source.stat().st_size > MAX_TEXT_BYTES:
            continue
        try:
            issues.extend(scan_text(path, source.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            continue
    return issues


def git_history() -> list[str]:
    issues: list[str] = []
    metadata = git("log", "--all", "--format=%H%x09%an%x09%ae")
    for line in metadata.splitlines():
        commit, _author, email = line.split("\t", 2)
        domain = email.rsplit("@", 1)[-1].lower() if "@" in email else ""
        if domain not in SAFE_EMAIL_DOMAINS:
            issues.append(f"{commit}: non-noreply author email")

    seen: set[str] = set()
    for line in git("rev-list", "--objects", "--all").splitlines():
        blob, _, path = line.partition(" ")
        if not path or blob in seen:
            continue
        seen.add(blob)
        reason = unsafe_path(path)
        if reason:
            issues.append(f"{blob} {path}: {reason}")
            continue
        size = int(git("cat-file", "-s", blob).strip())
        if size > MAX_TEXT_BYTES:
            continue
        raw = git("cat-file", "-p", blob, text=False)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        issues.extend(scan_text(f"{blob} {path}", text))
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--current-tree", action="store_true")
    mode.add_argument("--git-history", action="store_true")
    args = parser.parse_args()

    issues = current_tree() if args.current_tree else git_history()
    if issues:
        for issue in sorted(set(issues)):
            print(f"FAIL: {issue}")
        raise SystemExit(1)
    print("privacy scan: PASS")


if __name__ == "__main__":
    main()
