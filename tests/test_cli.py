"""
CLI tests
"""

from __future__ import annotations

from unittest import mock

import pytest

from linkotron import cli


class FakeCopier:
    def __init__(self, contents: str = "") -> None:
        self.contents = contents

    def copy(self, text: str) -> None:
        self.contents = text

    def paste(self) -> str:
        return self.contents


def test_input_argument(capsys: pytest.CaptureFixture[str]) -> None:
    copier = FakeCopier()
    with (
        mock.patch.object(cli, "copier", copier),
        mock.patch("sys.argv", ["linky", "https://github.com/python/peps/pull/2399"]),
    ):
        cli.main()

    assert capsys.readouterr().out == "Copied! python/peps#2399\n"
    assert copier.contents == "python/peps#2399"


def test_no_copy(capsys: pytest.CaptureFixture[str]) -> None:
    copier = FakeCopier()
    with (
        mock.patch.object(cli, "copier", copier),
        mock.patch(
            "sys.argv",
            ["linky", "--no-copy", "https://github.com/python/peps/pull/2399"],
        ),
    ):
        cli.main()

    assert capsys.readouterr().out == "python/peps#2399\n"
    assert copier.contents == ""


def test_no_input_reads_clipboard(capsys: pytest.CaptureFixture[str]) -> None:
    copier = FakeCopier("https://github.com/python/peps/pull/2399")
    with (
        mock.patch.object(cli, "copier", copier),
        mock.patch("sys.argv", ["linky"]),
    ):
        cli.main()

    assert capsys.readouterr().out == "Copied! python/peps#2399\n"
    assert copier.contents == "python/peps#2399"


def test_no_input_empty_clipboard(capsys: pytest.CaptureFixture[str]) -> None:
    with (
        mock.patch.object(cli, "copier", FakeCopier("")),
        mock.patch("sys.argv", ["linky"]),
        pytest.raises(SystemExit, match="2"),
    ):
        cli.main()

    assert "clipboard is empty" in capsys.readouterr().err


def test_no_input_no_copier(capsys: pytest.CaptureFixture[str]) -> None:
    with (
        mock.patch.object(cli, "copier", None),
        mock.patch("sys.argv", ["linky"]),
        pytest.raises(SystemExit, match="2"),
    ):
        cli.main()

    assert "no clipboard support" in capsys.readouterr().err
