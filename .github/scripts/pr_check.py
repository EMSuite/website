#!/usr/bin/env python3
"""The PR checks of the EMSuite repos (synced from EMSuite/EMSuite tools/github; edit it there, not in a copy).

1. The title is a conventional commit, because the squash commit takes it and release-please builds the CHANGELOG
   from it: type(scope)!: text, with type one of TYPES.
2. The body names its issue (Fixes EMSuite/<repo>#n, or #n, or the issue's URL), except for chore(deps) PRs and
   release-please's Release PR.

Reads PR_TITLE, PR_BODY and PR_HEAD from the environment; exits 1 with the reason when a check fails.
"""
import os
import re
import sys

TYPES = ("feat", "fix", "perf", "docs", "test", "refactor", "ci", "chore", "build", "style", "revert")
TITLE = re.compile(r"^(?:%s)(?:\([^()\s][^()]*\))?!?: \S" % "|".join(TYPES))
ISSUE = re.compile(
    r"(?:(?:EMSuite/[A-Za-z0-9._-]+)?#\d+\b)"
    r"|(?:https://github\.com/EMSuite/[A-Za-z0-9._-]+/issues/\d+)",
    re.IGNORECASE,
)
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def title_ok(title: str) -> bool:
    return bool(TITLE.match(title.strip()))


def exempt_from_issue(title: str, head: str) -> bool:
    t = title.strip()
    return t.startswith("chore(deps)") or t.startswith("build(deps)") or head.startswith("release-please--")


def names_issue(body: str) -> bool:
    text = COMMENT.sub("", body or "")
    text = text.replace("EMSuite/<repo>#<n>", "")
    return bool(ISSUE.search(text))


def check(title: str, body: str, head: str) -> list:
    problems = []
    if not title_ok(title):
        problems.append(
            "The title is not a conventional commit: write type(scope): text with type one of "
            + ", ".join(TYPES) + " (the title becomes the CHANGELOG line).")
    if not exempt_from_issue(title, head) and not names_issue(body):
        problems.append("The body names no issue: add 'Fixes EMSuite/<repo>#<n>' (one issue, one PR).")
    return problems


def main() -> int:
    problems = check(os.environ.get("PR_TITLE", ""), os.environ.get("PR_BODY", ""), os.environ.get("PR_HEAD", ""))
    for p in problems:
        print(f"::error::{p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
