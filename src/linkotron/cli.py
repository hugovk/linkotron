"""
linkotron: CLI to format GitHub links in a shorter format.
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
    parser.add_argument("input", help="text containing GitHub links to shorten")
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

    output = shorten(line=args.input, formatter=args.formatter)
    if copier and not args.no_copy and output != args.input:
        copier.copy(output)
        print(f"Copied! {output}")
    else:
        print(f"{output}")


if __name__ == "__main__":
    main()
