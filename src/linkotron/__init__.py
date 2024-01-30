"""
CLI to format links
"""
from __future__ import annotations

import importlib.metadata
import re
from typing import Any

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

    REPO_URL = re.compile(rf"^https://github.com/({USERNAME})/({REPO})/?$")
    PR_OR_ISSUE = re.compile(
        rf"^https://github.com/({USERNAME})/({REPO})/(pull|issues)/(\d+)/?$"
    )
    COMMIT = re.compile(
        rf"^https://github.com/({USERNAME})/({REPO})/commit/([0-9a-f]+)/?$"
    )
    COMMENT = re.compile(
        rf"^https://github.com/({USERNAME})/({REPO})/"
        r"(pull|issues)/(\d+)#issuecomment-\d+/?$"
    )


def shorten(line: str, *, formatter: str | None = None) -> str:
    """Shorten GitHub links"""
    match m := RegexMatcher(line):
        case Patterns.REPO_URL:
            short = f"{m[1]}/{m[3]}"
        case Patterns.PR_OR_ISSUE:
            short = f"{m[1]}/{m[3]}#{m[6]}"
        case Patterns.COMMIT:
            short = f"{m[1]}/{m[3]}#{m[5][:7]}"
        case Patterns.COMMENT:
            short = f"{m[1]}/{m[3]}#{m[6]} (comment)"
        case _:
            return line

    if formatter in ("md", "markdown"):
        return f"[{short}]({line})"
    elif formatter in ("rst", "restructuredtext"):
        return f"`{short} <{line}>`__"
    return short
