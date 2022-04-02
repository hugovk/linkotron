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

### Open a PEP

<!-- [[[cog
from pepotron.scripts.run_command import run
run("pep 8")
]]] -->

```console
$ pep 8
https://peps.python.org/pep-0008/
```

<!-- [[[end]]] -->

### Open release schedule PEP for a Python version

<!-- [[[cog run("pep 3.11") ]]] -->

```console
$ pep 3.11
https://peps.python.org/pep-0664/
```

<!-- [[[end]]] -->

### Open a PEP by searching for words in the title

<!-- [[[cog run('pep "dead batteries"') ]]] -->

```console
$ pep "dead batteries"
Score	Result
90	PEP 594: Removing dead batteries from the standard library
55	PEP 288: Generators Attributes and Exceptions
55	PEP 363: Syntax For Dynamic Attribute Access
55	PEP 476: Enabling certificate verification by default for stdlib http clients
52	PEP 349: Allow str() to return unicode strings

https://peps.python.org/pep-0594/
```

<!-- [[[end]]] -->

### Open a build preview of a python/peps PR

<!-- [[[cog run("pep 594 --pr 2440") ]]] -->

```console
$ pep 594 --pr 2440
https://pep-previews--2440.org.readthedocs.build/pep-0594/
```

<!-- [[[end]]] -->

### Open the PEPs website

<!-- [[[cog run("pep") ]]] -->

```console
$ pep
https://peps.python.org
```

<!-- [[[end]]] -->

<!-- [[[cog run("pep --pr 2440") ]]] -->

```console
$ pep --pr 2440
https://pep-previews--2440.org.readthedocs.build
```

<!-- [[[end]]] -->

### Help

<!-- [[[cog run("pep --help") ]]] -->

```console
$ pep --help
usage: pep [-h] [-u URL] [-p PR] [-n] [--clear-cache] [-v] [-V] [search]

pepotron: CLI to open PEPs in your browser

positional arguments:
  search             PEP number, or Python version for its schedule, or words
                     from title

options:
  -h, --help         show this help message and exit
  -u URL, --url URL  Base URL for PEPs (default: https://peps.python.org)
  -p PR, --pr PR     Open preview for python/peps PR
  -n, --dry-run      Don't open in browser
  --clear-cache      Clear cache before running
  -v, --verbose      Verbose logging
  -V, --version      show program's version number and exit
```

<!-- [[[end]]] -->
