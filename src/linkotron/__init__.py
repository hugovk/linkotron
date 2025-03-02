"""
CLI to format links
"""

from __future__ import annotations

import re

from ._version import __version__ as __version__

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


# https://github.com/nedbat/adventofcode2022/blob/main/day07.py
class RegexMatcher:
    def __init__(self, text: str) -> None:
        self.text = text
        self.m: Any = None

    def __eq__(self, pattern: object) -> bool:
        if not isinstance(pattern, re.Pattern):
            return NotImplemented
        self.m = re.fullmatch(pattern, self.text)
        return bool(self.m)

    def __getitem__(self, group: int | str) -> str:
        return str(self.m[group])


class Patterns:
    # https://stackoverflow.com/a/59082561/724176
    USERNAME = "[a-zA-Z0-9]+([-_][a-zA-Z0-9]+)*"
    REPO = r"[a-zA-Z0-9]+([-_\.][a-zA-Z0-9]+)*[-_\.]?[a-zA-Z0-9]+"

    REPO_URL = re.compile(
        rf"^https://github.com/(?P<username>{USERNAME})/(?P<repo>{REPO})/?$"
    )
    PR_ISSUE_DISCUSSION = re.compile(
        rf"^https://github.com/(?P<username>{USERNAME})/(?P<repo>{REPO})/"
        r"(pull|issues|discussions)/(?P<number>\d+)/?$"
    )
    COMMIT = re.compile(
        rf"^https://github.com/(?P<username>{USERNAME})/(?P<repo>{REPO})/"
        r"commit/(?P<sha>[0-9a-f]+)/?$"
    )
    COMMENT = re.compile(
        rf"^https://github.com/(?P<username>{USERNAME})/(?P<repo>{REPO})/"
        r"(pull|issues|discussions)/(?P<number>\d+)"
        r"#(issuecomment-|discussion_r|discussioncomment-)\d+/?$"
    )


def shorten(line: str, *, formatter: str | None = None) -> str:
    """Shorten GitHub links"""
    match m := RegexMatcher(line):
        case Patterns.REPO_URL:
            short = f"{m['username']}/{m['repo']}"
        case Patterns.PR_ISSUE_DISCUSSION:
            short = f"{m['username']}/{m['repo']}#{m['number']}"
        case Patterns.COMMIT:
            short = f"{m['username']}/{m['repo']}#{m['sha'][:7]}"
        case Patterns.COMMENT:
            short = f"{m['username']}/{m['repo']}#{m['number']} (comment)"
        case _:
            return line

    if formatter in ("md", "markdown"):
        return f"[{short}]({line})"
    elif formatter in ("rst", "restructuredtext"):
        return f"`{short} <{line}>`__"
    return short
