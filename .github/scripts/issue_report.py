#!/usr/bin/env python3
"""The weekly issue report of an EMSuite repo (synced from EMSuite/EMSuite tools/github; edit it there).

Lists, in one standing issue titled REPORT_TITLE:
- open issues without a milestone;
- open issues without exactly one kind label;
- open issues in a closed milestone;
- issues labelled `blocked` whose "Depends on" issues are all closed;
- a docs/status.md that does not name the latest release tag.
When nothing is listed the standing issue is closed. Needs `gh` with GH_TOKEN and GITHUB_REPOSITORY.
"""
import base64
import json
import os
import re
import subprocess
import sys

KINDS = {"bug", "feature", "science", "performance", "robustness", "cleanup", "docs", "infra", "report"}
REPORT_TITLE = "Weekly issue report"
DEP = re.compile(r"\b(EMSuite/[A-Za-z0-9._-]+)#(\d+)\b")


def gh(*args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout if r.returncode == 0 else None


def gh_json(path):
    out = gh("api", "--paginate", "--slurp", path)
    pages = json.loads(out)
    return [x for page in pages for x in (page if isinstance(page, list) else [page])]


def depends_on(body: str):
    """The full references under a "Depends on" heading, as (repo, number)."""
    if not body:
        return []
    m = re.search(r"^#{2,3}\s*Depends on\s*$(.*?)(?=^#{1,3}\s|\Z)", body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return [(r, int(n)) for r, n in DEP.findall(m.group(1))] if m else []


def findings(issues, is_closed, status_md, latest_tag):
    """Pure: the report's sections from the open issues, a lookup for dependency state, docs/status.md and the tag."""
    out = {"no milestone": [], "not exactly one kind": [], "in a closed milestone": [], "blocked, all dependencies closed": []}
    for i in issues:
        if "pull_request" in i or i.get("title") == REPORT_TITLE:
            continue
        ref = f"#{i['number']} {i['title']}"
        labels = {l["name"] for l in i.get("labels", [])}
        ms = i.get("milestone")
        if not ms:
            out["no milestone"].append(ref)
        elif ms.get("state") == "closed":
            out["in a closed milestone"].append(f"{ref} ({ms.get('title')})")
        kinds = sorted(labels & KINDS)
        if len(kinds) != 1:
            out["not exactly one kind"].append(f"{ref} ({', '.join(kinds) or 'none'})")
        if "blocked" in labels:
            deps = depends_on(i.get("body") or "")
            if deps and all(is_closed(r, n) for r, n in deps):
                out["blocked, all dependencies closed"].append(ref)
    status = []
    if status_md is not None and latest_tag:
        bare = latest_tag.lstrip("v")
        if bare not in status_md:
            status.append(f"docs/status.md does not name the latest tag {latest_tag}")
    return out, status


def render(out, status):
    lines = []
    for k, v in out.items():
        if v:
            lines.append(f"### {k} ({len(v)})\n")
            lines += [f"- {x}" for x in v]
            lines.append("")
    if status:
        lines.append("### docs/status.md\n")
        lines += [f"- {x}" for x in status]
    return "\n".join(lines).strip()


def main() -> int:
    repo = os.environ["GITHUB_REPOSITORY"]
    issues = gh_json(f"repos/{repo}/issues?state=open&per_page=100")
    cache = {}

    def is_closed(r, n):
        if (r, n) not in cache:
            out = gh("api", f"repos/{r}/issues/{n}", "--jq", ".state", check=False)
            cache[(r, n)] = (out or "").strip() == "closed"
        return cache[(r, n)]

    raw = gh("api", f"repos/{repo}/contents/docs/status.md", "--jq", ".content", check=False)
    status_md = base64.b64decode(raw).decode("utf-8", "replace") if raw else None
    tag = gh("api", f"repos/{repo}/releases/latest", "--jq", ".tag_name", check=False)
    out, status = findings(issues, is_closed, status_md, (tag or "").strip())
    body = render(out, status)
    existing = [i for i in issues if i.get("title") == REPORT_TITLE and "pull_request" not in i]
    if body:
        text = f"Open work that breaks the suite's issue rules (milestone, one kind label, dependencies, status page), found by the weekly check.\n\n{body}\n"
        if existing:
            gh("issue", "edit", str(existing[0]["number"]), "--repo", repo, "--body", text)
        else:
            gh("issue", "create", "--repo", repo, "--title", REPORT_TITLE, "--body", text, "--label", "report")
        print(body)
    else:
        for i in existing:
            gh("issue", "close", str(i["number"]), "--repo", repo, "--comment", "Nothing to report this week.")
        print("Nothing to report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
