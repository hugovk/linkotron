"""
linkotron: CLI to format GitHub links in a shorter format.
"""

from __future__ import annotations

import argparse
import difflib
import os.path
from collections.abc import Iterable

from termcolor import colored, cprint

from . import __version__, shorten

try:
    import pyperclip as copier  # type: ignore[import-not-found]
except ImportError:
    try:
        import xerox as copier  # type: ignore[import-not-found]
    except ImportError:
        copier = None


def color_diff(diff: Iterable[str]) -> Iterable[str]:
    for line in diff:
        if line.startswith("+"):
            yield colored(line, "green")
        elif line.startswith("-"):
            yield colored(line, "red")
        else:
            yield line


def do_file(filename: str, dry_run: bool) -> None:
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

    if changes:
        diff = color_diff(
            difflib.unified_diff(
                old_lines, new_lines, fromfile=filename, tofile=filename
            )
        )
        print("".join(diff))
    else:
        cprint(f"no change for {filename}", "yellow")

    if changes and not dry_run:
        with open(filename, "w") as f:
            f.writelines(new_lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("input", help="text containing GitHub links to shorten")
    parser.add_argument(
        "-n", "--dry-run", action="store_true", help="show but don't save changes"
    )
    parser.add_argument(
        "--no-copy", action="store_true", help="do not copy output to clipboard"
    )

    format_group = parser.add_argument_group("formatters")
    format_group = format_group.add_mutually_exclusive_group()
    for name, help_text in (
        ("md", "Markdown"),
        ("rst", "reStructuredText"),
    ):
        format_group.add_argument(
            f"-{name[0]}",
            f"--{name}",
            f"--{help_text.lower()}",
            action="store_const",
            const=name,
            dest="formatter",
            help=f"output in {help_text}",
        )

    args = parser.parse_args()

    if os.path.isfile(args.input):
        do_file(args.input, args.dry_run)
        return

    output = shorten(line=args.input, formatter=args.formatter)
    if copier and not args.no_copy and output != args.input:
        copier.copy(output)
        print(f"{colored('Copied!', 'yellow')} {colored(output, 'green')}")
    else:
        cprint(f"{output}", "green")


if __name__ == "__main__":
    main()
