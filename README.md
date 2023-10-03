# linkotron

[![PyPI version](https://img.shields.io/pypi/v/linkotron.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/linkotron/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/linkotron.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/linkotron/)
[![PyPI downloads](https://img.shields.io/pypi/dm/linkotron.svg)](https://pypistats.org/packages/linkotron)
[![Test](https://github.com/hugovk/linkotron/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/linkotron/actions)
[![Codecov](https://codecov.io/gh/hugovk/linkotron/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/linkotron)
[![Licence](https://img.shields.io/github/license/hugovk/linkotron.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

CLI to format GitHub links in a shorter format.

## Installation

### From PyPI

```bash
python3 -m pip install --upgrade linkotron
```

### With [pipx][pipx]

```bash
pipx install linkotron
```

[pipx]: https://github.com/pypa/pipx

### From source

```bash
git clone https://github.com/hugovk/linkotron
cd linkotron
python3 -m pip install .
```

## Usage

Run `linkotron` or `linky`, they do the same thing.

<!-- [[[cog
from linkotron.scripts.run_command import run
run("linky --help")
]]] -->

```console
$ linky --help
usage: linky [-h] [-V] [-n] [--no-copy] [-m | -r] input

linkotron: CLI to format GitHub links in a shorter format.

positional arguments:
  input                 text containing GitHub links to shorten

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -n, --dry-run         show but don't save changes
  --no-copy             do not copy output to clipboard

formatters:
  -m, --md, --markdown  output in Markdown
  -r, --rst, --restructuredtext
                        output in reStructuredText
```

<!-- [[[end]]] -->

### Linkify a repo

<!-- [[[cog
run("linky https://github.com/python/peps")
]]] -->

```console
$ linky https://github.com/python/peps
Copied! python/peps
```

<!-- [[[end]]] -->

### Linkify an issue

<!-- [[[cog
run("linky https://github.com/python/peps/issues/1012")
]]] -->

```console
$ linky https://github.com/python/peps/issues/1012
Copied! python/peps#1012
```

<!-- [[[end]]] -->

### Linkify a pull request

<!-- [[[cog
run("linky https://github.com/python/peps/pull/2399")
]]] -->

```console
$ linky https://github.com/python/peps/pull/2399
Copied! python/peps#2399
```

<!-- [[[end]]] -->

### Linkify a commit

<!-- [[[cog
run("linky https://github.com/hugovk/cpython/commit/28b23555030d58fdb52b74a547cc621c49690de0")
]]] -->

```console
$ linky https://github.com/hugovk/cpython/commit/28b23555030d58fdb52b74a547cc621c49690de0
Copied! hugovk/cpython#28b2355
```

<!-- [[[end]]] -->

### Linkify a comment

<!-- [[[cog
run("linky https://github.com/python/peps/pull/2399#issuecomment-1063409480")
]]] -->

```console
$ linky https://github.com/python/peps/pull/2399#issuecomment-1063409480
Copied! python/peps#2399 (comment)
```

<!-- [[[end]]] -->

### Formatting

#### Markdown

<!-- [[[cog
run("linky --md https://github.com/python/peps/pull/2399")
]]] -->

```console
$ linky --md https://github.com/python/peps/pull/2399
Copied! [python/peps#2399](https://github.com/python/peps/pull/2399)
```

<!-- [[[end]]] -->

#### reStructuredText

<!-- [[[cog
run("linky --rst https://github.com/python/peps/pull/2399")
]]] -->

```console
$ linky --rst https://github.com/python/peps/pull/2399
Copied! `python/peps#2399 <https://github.com/python/peps/pull/2399>`__
```

<!-- [[[end]]] -->

## Files

#### Plaintext file

Files without `.md` or `.rst` extensions:

<!-- [[[cog
run("linky tests/data/test.txt --dry-run")
]]] -->

```console
$ linky tests/data/test.txt --dry-run
--- tests/data/test.txt
+++ tests/data/test.txt
@@ -2,11 +2,11 @@

 One

-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc python/python-docs-theme#44 xyz

-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc python/python-docs-theme#bcb78b6 xyz

-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc python/python-docs-theme#44 (comment) xyz

 Two
```

<!-- [[[end]]] -->

#### Markdown file

Files with `.md` extensions:

<!-- [[[cog
run("linky tests/data/test.md --dry-run")
]]] -->

```console
$ linky tests/data/test.md --dry-run
--- tests/data/test.md
+++ tests/data/test.md
@@ -2,11 +2,11 @@

 ## One

-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc [python/python-docs-theme#44](https://github.com/python/python-docs-theme/pull/44) xyz

-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc [python/python-docs-theme#bcb78b6](https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14) xyz

-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc [python/python-docs-theme#44 (comment)](https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287) xyz


 ## Two
```

<!-- [[[end]]] -->

#### reStructuredText file

Files with `.rst` extensions:

<!-- [[[cog
run("linky tests/data/test.rst --dry-run")
]]] -->

```console
$ linky tests/data/test.rst --dry-run
--- tests/data/test.rst
+++ tests/data/test.rst
@@ -5,11 +5,11 @@
 One
 ===

-abc https://github.com/python/python-docs-theme/pull/44 xyz
+abc `python/python-docs-theme#44 <https://github.com/python/python-docs-theme/pull/44>`__ xyz

-abc https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14 xyz
+abc `python/python-docs-theme#bcb78b6 <https://github.com/python/python-docs-theme/commit/bcb78b690e44a6f1662c75dde030a7852299fd14>`__ xyz

-abc https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287 xyz
+abc `python/python-docs-theme#44 (comment) <https://github.com/python/python-docs-theme/pull/44#issuecomment-1676720287>`__ xyz

 Two
 ===
```

<!-- [[[end]]] -->
