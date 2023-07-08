"""
linkotron: CLI to format GitHub links in a shorter format.
"""
from __future__ import annotations

import argparse

from . import __version__, shorten

try:
    import pyperclip as copier  # type: ignore[import]
except ImportError:
    try:
        import xerox as copier  # type: ignore[import]
    except ImportError:
        copier = None


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("input", help="Text containing GitHub links to shorten")
    parser.add_argument(
        "-m", "--md", "--markdown", action="store_true", help="Output Markdown"
    )
    parser.add_argument(
        "-r",
        "--rst",
        "--restructuredtext",
        action="store_true",
        help="Output reStructuredText",
    )
    parser.add_argument(
        "--no-copy", action="store_true", help="Do not copy output to clipboard"
    )
    args = parser.parse_args()

    if args.md:
        format_ = "markdown"
    elif args.rst:
        format_ = "restructuredtext"
    else:
        format_ = None

    output = shorten(line=args.input, format_=format_)
    if copier and not args.no_copy and output != args.input:
        copier.copy(output)
        print(f"Copied! {output}")
    else:
        print(f"{output}")


if __name__ == "__main__":
    main()
