"""Refresh the open-source project summary in README.md.

Looks up public pull requests authored by USER in repositories owned by
someone else and names the projects in two lines: merged upstream, and in
review. A project with any merged PR is listed only as merged. Closed PRs
that were not merged are ignored. Each name links to USER's PRs there.
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
# Display names, keyed by repository owner (lowercase).
PROJECT_NAMES = {
    "google": "Google ADK",
    "a2aproject": "A2A",
    "langchain4j": "LangChain4j",
    "strands-agents": "Strands Agents",
    "agentscope-ai": "AgentScope",
    "spring-projects": "Spring AI",
    "langchain-ai": "LangGraph.js",
}

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


def merged_at(item: dict) -> str | None:
    """Merge time, counting PRs merged outside GitHub (e.g. Google's Copybara).

    Those are closed rather than merged, and carry a "merged" label.
    """
    merged = (item.get("pull_request") or {}).get("merged_at")
    if merged:
        return merged
    labels = {label["name"].lower() for label in item.get("labels", [])}
    if item["state"] == "closed" and "merged" in labels:
        return item["closed_at"]
    return None


def collect(items: list[dict]) -> tuple[list[str], list[str]]:
    """Return owners with merged PRs and owners with only open PRs, newest first."""
    merged: dict[str, str] = {}
    open_: dict[str, str] = {}
    for item in items:
        repo = item["repository_url"].split("/repos/", 1)[1]
        owner = repo.split("/")[0].lower()
        if owner in EXCLUDED_OWNERS:
            continue
        when = merged_at(item)
        if when:
            merged[owner] = max(merged.get(owner, ""), when)
        elif item["state"] == "open":
            open_[owner] = max(open_.get(owner, ""), item["created_at"])
    merged_owners = sorted(merged, key=merged.__getitem__, reverse=True)
    open_owners = sorted(open_, key=open_.__getitem__, reverse=True)
    return merged_owners, [o for o in open_owners if o not in merged]


def link(owner: str) -> str:
    query = urllib.parse.quote(f"is:pr author:{USER} org:{owner}")
    name = PROJECT_NAMES.get(owner, owner)
    return f"[{name}](https://github.com/search?q={query}&type=pullrequests)"


def render(merged: list[str], open_: list[str]) -> str:
    lines = [START]
    if merged:
        lines.append("**Merged upstream:** " + " · ".join(map(link, merged)) + "<br />")
    if open_:
        lines.append("**In review:** " + " · ".join(map(link, open_)))
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
    print(f"merged: {', '.join(merged)}; in review: {', '.join(open_)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
