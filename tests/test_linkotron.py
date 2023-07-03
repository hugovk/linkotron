"""
Unit tests
"""
from __future__ import annotations

import pytest

import linkotron


@pytest.mark.parametrize(
    "link, expected",
    [
        ("https://github.com/python/peps/issues/2", "python/peps#2"),
        ("https://github.com/python/peps/pull/2399", "python/peps#2399"),
        (
            "https://github.com/"
            "python/peps/commit/ceb81fd7b71f74aaa2295594f86501acbe620cda",
            "python/peps#ceb81fd",
        ),
        (
            "https://github.com/python/peps/pull/2399#issuecomment-1063409480",
            "python/peps#2399 (comment)",
        ),
        (
            "some text",
            "some text",
        ),
    ],
)
def test_shorten(link: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link) == expected


@pytest.mark.parametrize(
    "link, format_, expected",
    [
        (
            "https://github.com/python/peps/pull/2399",
            "md",
            "[python/peps#2399](https://github.com/python/peps/pull/2399)",
        ),
        (
            "https://github.com/python/peps/pull/2399",
            "rst",
            "`python/peps#2399 <https://github.com/python/peps/pull/2399>`__",
        ),
    ],
)
def test_shorten_into_format(link: str, format_: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link, format_=format_) == expected
