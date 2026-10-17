#!/usr/bin/env python3
"""Fetch citation stats from the Google Scholar profile and write _data/scholar.yml.

The profile id is read from `scholar_userid` in _config.yml. The data file is only
rewritten when the stats change. If Google Scholar cannot be reached or blocks the
request, the existing file is left untouched so the site keeps the last known stats.

Run by .github/workflows/update-scholar-stats.yml; can also be run locally.
"""

import datetime
import html
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
OUTPUT = ROOT / "_data" / "scholar.yml"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)
FIELDS = ("citations", "h_index", "i10_index")
ROW_LABELS = {"citations": "citations", "h-index": "h_index", "i10-index": "i10_index"}


def warn(message):
    # Shown as an annotation on the workflow run; harmless when run locally.
    print(f"::warning::{message}")


def read_user_id():
    match = re.search(r"^scholar_userid:\s*([\w-]+)", CONFIG.read_text(encoding="utf-8"), re.M)
    if not match:
        sys.exit("scholar_userid not found in _config.yml")
    return match.group(1)


def fetch(url, attempts=3):
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en"})
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as error:  # network errors, HTTP 429/403, ...
            warn(f"Attempt {attempt}/{attempts} to fetch Google Scholar failed: {error}")
            if attempt < attempts:
                time.sleep(30 * attempt)
    return None


def parse(page):
    table = re.search(r'<table id="gsc_rsb_st".*?</table>', page, re.S)
    if not table:
        return None
    cells = lambda row: [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)]
    rows = [cells(row) for row in re.findall(r"<tr.*?</tr>", table.group(0), re.S)]
    since = re.search(r"Since (\d{4})", " ".join(rows[0])) if rows else None
    stats = {"since_year": int(since.group(1)) if since else None}
    for row in rows[1:]:
        key = ROW_LABELS.get(row[0].lower()) if row else None
        if key and len(row) >= 3:
            stats[key] = int(row[1].replace(",", ""))
            stats[f"{key}_since"] = int(row[2].replace(",", ""))
    if not all(stats.get(field) for field in FIELDS):
        return None
    return stats


def read_existing():
    if not OUTPUT.exists():
        return {}
    values = {}
    for line in OUTPUT.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(\w+):\s*(\d+)\s*$", line)
        if match:
            values[match.group(1)] = int(match.group(2))
    return values


def write(user_id, stats):
    lines = [
        "# Google Scholar profile stats, shown on the home page.",
        "# Updated weekly by .github/workflows/update-scholar-stats.yml (bin/update-scholar-stats.py).",
        f"user_id: {user_id}",
        f"updated: {datetime.date.today().isoformat()}",
    ]
    lines += [f"{key}: {stats[key]}" for key in ("since_year", *[f for field in FIELDS for f in (field, f"{field}_since")])]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    user_id = read_user_id()
    page = fetch(f"https://scholar.google.com/citations?user={user_id}&hl=en")
    stats = parse(page) if page else None
    if not stats:
        warn("Could not read stats from Google Scholar (blocked or page changed); keeping the existing _data/scholar.yml.")
        return
    existing = read_existing()
    if all(existing.get(key) == value for key, value in stats.items()):
        print(f"Stats unchanged: {stats}")
        return
    write(user_id, stats)
    print(f"Updated {OUTPUT.relative_to(ROOT)}: {stats}")


if __name__ == "__main__":
    main()
