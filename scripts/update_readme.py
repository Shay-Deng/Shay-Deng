"""Refresh the open-source contribution list in README.md.

Lists public pull requests authored by USER in repositories owned by someone
else, grouped into merged and open. Closed-without-merge PRs are left out.
Only the block between the oss:start / oss:end markers is rewritten.

Standard library only. Set GITHUB_TOKEN for a higher API rate limit.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

USER = "Shay-Deng"
# Owners whose PRs should not appear (own repos, take-home exercises).
EXCLUDED_OWNERS = {USER.lower(), "omnilink-systems-inc"}

README = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- oss:start -->"
END = "<!-- oss:end -->"


def search_prs() -> list[dict]:
    query = f"is:pr author:{USER} is:public -user:{USER}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-updater",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    items: list[dict] = []
    page = 1
    while True:
        params = urllib.parse.urlencode(
            {"q": query, "per_page": 100, "page": page, "sort": "created"}
        )
        request = urllib.request.Request(
            f"https://api.github.com/search/issues?{params}", headers=headers
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
        items.extend(data["items"])
        if len(items) >= data["total_count"] or not data["items"]:
            return items
        page += 1


def cell(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("|", "\\|")
        .strip()
    )


def collect(items: list[dict]) -> tuple[list[dict], list[dict]]:
    merged, open_ = [], []
    for item in items:
        repo = item["repository_url"].split("/repos/", 1)[1]
        if repo.split("/")[0].lower() in EXCLUDED_OWNERS:
            continue
        row = {
            "repo": repo,
            "number": item["number"],
            "title": item["title"],
            "url": item["html_url"],
            "draft": item.get("draft", False),
            "created": item["created_at"][:10],
            "merged": (item.get("pull_request") or {}).get("merged_at"),
        }
        if row["merged"]:
            merged.append(row)
        elif item["state"] == "open":
            open_.append(row)
    merged.sort(key=lambda r: r["merged"], reverse=True)
    open_.sort(key=lambda r: r["created"], reverse=True)
    return merged, open_


def table(rows: list[dict], date_label: str, date_key: str) -> list[str]:
    lines = [f"| Project | Pull request | {date_label} |", "| :-- | :-- | :-- |"]
    for r in rows:
        draft = " <sub>(draft)</sub>" if r["draft"] else ""
        lines.append(
            f"| [{r['repo']}](https://github.com/{r['repo']}) "
            f"| [#{r['number']}]({r['url']}) {cell(r['title'])}{draft} "
            f"| {r[date_key][:10].replace('-', '&#8209;')} |"
        )
    return lines


def render(merged: list[dict], open_: list[dict]) -> str:
    projects = {r["repo"] for r in merged + open_}
    lines = [
        START,
        f"<sub>{len(merged)} merged &nbsp;·&nbsp; {len(open_)} in review "
        f"&nbsp;·&nbsp; {len(projects)} projects &nbsp;·&nbsp; "
        "updated daily by <code>scripts/update_readme.py</code></sub>",
        "",
    ]
    if merged:
        lines += ["**Merged**", "", *table(merged, "Merged", "merged"), ""]
    if open_:
        lines += ["**In review**", "", *table(open_, "Opened", "created"), ""]
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    merged, open_ = collect(search_prs())
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        print(f"markers {START} / {END} not found in README.md", file=sys.stderr)
        return 1
    updated = pattern.sub(lambda _: render(merged, open_), text, count=1)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
    print(f"{len(merged)} merged, {len(open_)} open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
