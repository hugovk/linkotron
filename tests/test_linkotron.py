"""
Unit tests
"""

from __future__ import annotations

import pytest

import linkotron

from .data.expected import (
    EXPECTED_MD_DIFF,
    EXPECTED_MD_NO_CHANGE,
    EXPECTED_RST_DIFF,
    EXPECTED_TXT_DIFF,
)


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
    assert linkotron.shorten(" " + link + " ") == expected
    assert linkotron.shorten(" " + link + "/ ") == expected


@pytest.mark.parametrize("link, expected", [("some text", "some text")])
def test_shorten_no_link(link: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link) == expected


@pytest.mark.parametrize(
    "link, formatter, expected",
    [
        (
            "abc https://github.com/python/peps/pull/2399 xyz",
            "md",
            "abc [python/peps#2399](https://github.com/python/peps/pull/2399) xyz",
        ),
        (
            "abc https://github.com/python/peps/pull/2399 xyz",
            "rst",
            "abc `python/peps#2399 <https://github.com/python/peps/pull/2399>`__ xyz",
        ),
    ],
)
def test_shorten_into_format(link: str, formatter: str, expected: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link, formatter=formatter) == expected


@pytest.mark.parametrize(
    "link, formatter",
    [
        ("abc [python/peps#2399](https://github.com/python/peps/pull/2399) xyz", "md"),
        (
            "abc `python/peps#2399 <https://github.com/python/peps/pull/2399>`__ xyz",
            "rst",
        ),
    ],
)
def test_format_already_shortened(link: str, formatter: str) -> None:
    # Act / Assert
    assert linkotron.shorten(link, formatter=formatter) == link


@pytest.mark.parametrize(
    "input_filename, expected",
    [
        pytest.param("test.md", EXPECTED_MD_DIFF, id="md"),
        pytest.param("test.rst", EXPECTED_RST_DIFF, id="rst"),
        pytest.param("test.txt", EXPECTED_TXT_DIFF, id="txt"),
        pytest.param("test-no-change.md", EXPECTED_MD_NO_CHANGE, id="md-none"),
    ],
)
def test_shorten_files(input_filename: str, expected: str) -> None:
    # Arrange
    input_filename = "tests/data/" + input_filename

    # Act
    output = linkotron.shorten_file(input_filename, dry_run=True)

    # Assert
    assert output.strip() == expected.strip()
