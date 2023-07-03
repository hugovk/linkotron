"""
linkotron: CLI to format GitHub links in a shorter format.
"""
from __future__ import annotations

import argparse

from linkotron import __version__, shorten


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
    args = parser.parse_args()

    if args.md:
        format_ = "markdown"
    elif args.rst:
        format_ = "restructuredtext"
    else:
        format_ = None

    print(shorten(line=args.input, format_=format_))


if __name__ == "__main__":
    main()
