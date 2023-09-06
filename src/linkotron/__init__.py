"""
CLI to format links
"""

from __future__ import annotations

import difflib
import importlib.metadata
import re
from collections.abc import Iterable
from typing import Any

from termcolor import colored

__version__ = importlib.metadata.version(__name__)


# https://github.com/nedbat/adventofcode2022/blob/main/day07.py
class RegexMatcher:
    def __init__(self, text: str) -> None:
        self.text = text
        self.m: Any = None

    def __eq__(self, pattern: Any) -> bool:
        self.m = re.fullmatch(pattern, self.text)
        return bool(self.m)

    def __getitem__(self, num: int) -> str:
        return str(self.m[num])


class Patterns:
    # https://stackoverflow.com/a/59082561/724176
    USERNAME = "[a-zA-Z0-9]+([-_][a-zA-Z0-9]+)*"
    REPO = r"[a-zA-Z0-9]+([-_\.][a-zA-Z0-9]+)*[-_\.]?[a-zA-Z0-9]+"

    REPO_URL = re.compile(rf"^(.*)(https://github.com/({USERNAME})/({REPO})/?)(.*)$")
    PR_OR_ISSUE = re.compile(
        rf"(.*)(https://github.com/({USERNAME})/({REPO})/(pull|issues)/(\d+))/?(.*)"
    )
    COMMIT = re.compile(
        rf"(.*)(https://github.com/({USERNAME})/({REPO})/commit/([0-9a-f]+))/?(.*)"
    )
    COMMENT = re.compile(
        rf"(.*)(https://github.com/({USERNAME})/({REPO})/"
        r"(pull|issues)/(\d+)#issuecomment-\d+)/?(.*)"
    )


def shorten(line: str, *, formatter: str | None = None) -> str:
    """Shorten GitHub links"""
    match m := RegexMatcher(line):

        case Patterns.COMMIT:
            prefix = m[1]
            long = m[2]
            short = f"{m[3]}/{m[5]}#{m[7][:7]}"
            suffix = m[8]
        case Patterns.COMMENT:
            prefix = m[1]
            long = m[2]
            short = f"{m[3]}/{m[5]}#{m[8]} (comment)"
            suffix = m[9]
        case Patterns.PR_OR_ISSUE:
            prefix = m[1]
            long = m[2]
            short = f"{m[3]}/{m[5]}#{m[8]}"
            suffix = m[9]
        case Patterns.REPO_URL:
            prefix = m[1]
            short = f"{m[3]}/{m[5]}"
            long = m[2]
            suffix = m[7]
        case _:
            return line

    if formatter in ("md", "markdown"):
        proposed = f"[{short}]({long})"
        if line.startswith(proposed, m.m.start(2) - len(f"[{short}](")):
            # Line already contains shortened URL, don't insert a new one
            return line
        return f"{prefix}{proposed}{suffix}"
    elif formatter in ("rst", "restructuredtext"):
        proposed = f"`{short} <{long}>`__"
        if line.startswith(proposed, m.m.start(2) - len(f"`{short} <")):
            # Line already contains shortened URL, don't insert a new one
            return line
        return f"{prefix}{proposed}{suffix}"
    return short


def _color_diff(diff: Iterable[str]) -> Iterable[str]:
    for line in diff:
        if line.startswith("+"):
            yield colored(line, "green")
        elif line.startswith("-"):
            yield colored(line, "red")
        else:
            yield line


def shorten_file(filename: str, dry_run: bool) -> str:
    with open(filename) as f:
        old_lines = f.readlines()

    formatter = None
    if filename.endswith(".md"):
        formatter = "markdown"
    elif filename.endswith(".rst"):
        formatter = "restructuredtext"

    changes = 0
    new_lines = []
    for line in old_lines:
        line = line.rstrip("\n")
        new_line = shorten(line=line, formatter=formatter)
        if new_line != line:
            changes += 1
        new_lines.append(new_line + "\n")

    if changes and not dry_run:
        with open(filename, "w") as f:
            f.writelines(new_lines)

    if changes:
        diff = _color_diff(
            difflib.unified_diff(
                old_lines, new_lines, fromfile=filename, tofile=filename
            )
        )
        return "".join(diff)
    else:
        return colored(f"no change for {filename}", "yellow")
