"""
Unit tests
"""
from __future__ import annotations

import pytest

import linkotron


@pytest.mark.parametrize(
    "link, expected",
    [
        ("https://github.com/python/peps", "python/peps"),
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
    ],
)
def test_shorten(link: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link) == expected
    assert linkotron.shorten(link + "/") == expected


@pytest.mark.parametrize("link, expected", [("some text", "some text")])
def test_shorten_no_link(link: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link) == expected


@pytest.mark.parametrize(
    "link, formatter, expected",
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
def test_shorten_into_format(link: str, formatter: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link, formatter=formatter) == expected
