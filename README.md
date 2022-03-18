# pepotron

[![PyPI version](https://img.shields.io/pypi/v/pepotron.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/pepotron/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pepotron.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/pepotron/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pepotron.svg)](https://pypistats.org/packages/pepotron)
[![Test](https://github.com/hugovk/pepotron/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/pepotron/actions)
[![codecov](https://codecov.io/gh/hugovk/pepotron/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/pepotron)
[![GitHub](https://img.shields.io/github/license/hugovk/pepotron.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

CLI to open PEPs in your browser.

## Installation

### From PyPI

```bash
python3 -m pip install --upgrade pepotron
```

### From source

```bash
git clone https://github.com/hugovk/pepotron
cd pepotron
pip install .
```

## Usage

### Help

<!-- [[[cog
from scripts.run_command import run
run("pep --help")
]]] -->

```console
$ pep --help
usage: pep [-h] [-u URL] [-V] search

CLI to open PEPs in your browser

positional arguments:
  search             PEP number, or Python version for its schedule

options:
  -h, --help         show this help message and exit
  -u URL, --url URL  Base URL for PEPs (default: https://peps.python.org)
  -V, --version      show program's version number and exit
```

<!-- [[[end]]] -->

### Open a PEP

```console
$ pep 8
https://peps.python.org/pep-0008/
```

### Open release schedule PEP for a Python version

```console
$ pep 3.11
https://peps.python.org/pep-0664/
```
