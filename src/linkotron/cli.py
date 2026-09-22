"""
linkotron: CLI to format links in a shorter format.
"""

from __future__ import annotations

import argparse

from . import __version__, shorten

try:
    import pyperclip as copier  # type: ignore[import-untyped]
except ImportError:
    try:
        import xerox as copier  # type: ignore[import-not-found]
    except ImportError:
        copier = None


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="text containing links to shorten (default: read from clipboard)",
    )
    parser.add_argument(
        "--no-copy", action="store_true", help="do not copy output to clipboard"
    )

    format_group = parser.add_argument_group("formatters")
    format_group = format_group.add_mutually_exclusive_group()
    for name, help_text in (
        ("md", "Markdown"),
        ("rst", "reStructuredText"),
        ("term", "terminal"),
    ):
        format_group.add_argument(
            f"-{name[0]}",
            f"--{name}",
            f"--{help_text.lower()}",
            action="store_const",
            const=name,
            dest="formatter",
            help=(
                "output in OSC 8 for terminal"
                if help_text.startswith("term")
                else f"output in {help_text}"
            ),
        )

    args = parser.parse_args()

    if args.input is None:
        if copier is None:
            parser.error("no input given and no clipboard support available")
        args.input = copier.paste()

        if not args.input:
            parser.error("no input given and clipboard is empty")

    output = shorten(line=args.input, formatter=args.formatter)
    if copier and not args.no_copy and output != args.input:
        copier.copy(output)
        print(f"Copied! {output}")
    else:
        print(f"{output}")


if __name__ == "__main__":
    main()
