#!/usr/bin/env python3
"""Auto-discover the top contributed-to repos (by PR count) across a fixed
set of orgs, and render them as a horizontal bar chart SVG.

Reads GITHUB_TOKEN and USERNAME from the environment. No third-party deps.
"""

import json
import os
import urllib.request
from collections import Counter

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ["USERNAME"]

# Orgs already known to have contributions worth surfacing. Add to this list
# as new orgs come up rather than searching all of GitHub.
ORGS = [
    "open-telemetry",
    "prometheus",
    "liquibase",
    "Apicurio",
    "gofr-dev",
    "jenkinsci",
]

# Brand color per org, reused from the badges already in the README.
ORG_COLORS = {
    "open-telemetry": "#425CC7",
    "prometheus": "#E6522C",
    "liquibase": "#2962FF",
    "Apicurio": "#6E56CF",
    "gofr-dev": "#00ADD8",
    "jenkinsci": "#D24939",
}

TOP_N = 5
OUT_PATH = "profile-3d-contrib/top-prs.svg"

GRAPHQL_URL = "https://api.github.com/graphql"
SEARCH_QUERY = """
query($searchQuery: String!, $after: String) {
  search(query: $searchQuery, type: ISSUE, first: 100, after: $after) {
    issueCount
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on PullRequest {
        repository { nameWithOwner }
      }
    }
  }
}
"""


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": USERNAME,
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def count_prs_by_repo(org):
    counts = Counter()
    after = None
    while True:
        search_query = f"org:{org} type:pr author:{USERNAME}"
        data = graphql(SEARCH_QUERY, {"searchQuery": search_query, "after": after})
        search = data["data"]["search"]
        for node in search["nodes"]:
            repo = node.get("repository", {}).get("nameWithOwner")
            if repo:
                counts[repo] += 1
        if not search["pageInfo"]["hasNextPage"]:
            break
        after = search["pageInfo"]["endCursor"]
    return counts


# A handful of repo names are too long to fit the chart's label column at a
# readable font size; give those a shorter display alias.
DISPLAY_ALIASES = {
    "open-telemetry/opentelemetry-cpp": "otel-cpp",
    "open-telemetry/opentelemetry-go": "otel-go",
    "open-telemetry/opentelemetry-go-contrib": "otel-go-contrib",
    "open-telemetry/opentelemetry-go-compile-instrumentation": "otel-compile-instr",
    "open-telemetry/opentelemetry-collector": "otel-collector",
    "open-telemetry/opentelemetry-collector-contrib": "otel-collector-contrib",
    "open-telemetry/opentelemetry-configuration": "otel-configuration",
    "open-telemetry/semantic-conventions": "otel-semconv",
    "jenkinsci/opentelemetry-plugin": "jenkins-otel-plugin",
    "jenkinsci/ssh-agents-plugin": "jenkins-ssh-agents",
}


def short_name(repo_full_name):
    """Return a compact display label, e.g. open-telemetry/opentelemetry-cpp -> otel-cpp."""
    if repo_full_name in DISPLAY_ALIASES:
        return DISPLAY_ALIASES[repo_full_name]
    return repo_full_name.split("/", 1)[1]


def render_svg(entries):
    row_height = 40
    padding = 24
    label_width = 200
    bar_area_width = 300
    width = padding * 2 + label_width + bar_area_width
    height = padding * 2 + row_height * len(entries)
    max_count = max(count for _, count in entries) if entries else 1

    bars = []
    for i, (repo, count) in enumerate(entries):
        org = repo.split("/", 1)[0]
        color = ORG_COLORS.get(org, "#8b949e")
        y = padding + i * row_height
        bar_width = (count / max_count) * (bar_area_width - 40)
        bars.append(f"""
    <text x="{padding}" y="{y + row_height / 2 + 5}" fill="#e6edf3" font-size="13" font-family="'JetBrains Mono', ui-monospace, monospace">{short_name(repo)}</text>
    <rect x="{padding + label_width}" y="{y + 8}" width="{bar_width:.1f}" height="20" rx="3" fill="{color}" />
    <text x="{padding + label_width + bar_width + 8}" y="{y + row_height / 2 + 5}" fill="#8b949e" font-size="13" font-family="'JetBrains Mono', ui-monospace, monospace">{count}</text>""")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect x="0" y="0" width="{width}" height="{height}" rx="6" fill="#0d1117" />
  {''.join(bars)}
</svg>"""


def main():
    totals = Counter()
    for org in ORGS:
        totals.update(count_prs_by_repo(org))

    top = totals.most_common(TOP_N)
    if not top:
        print("No PRs found across configured orgs; leaving existing SVG untouched.")
        return

    svg = render_svg(top)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH} with {len(top)} repos: {top}")


if __name__ == "__main__":
    main()
