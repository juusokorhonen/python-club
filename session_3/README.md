# Python package stub

This is a stub for a Python package that is installable and features also 
both manual and automatic testing/linting.

You can use this as a base for your projects.

![Tests](https://github.com/<username>/<repository>/actions/workflows/tests.yml/badge.svg)

## Installation

What this package does is not really relevant. However, if you still wish to
try it out, you need to do the following.

1. Install ECCodes

    - MacOS : `brew install eccodes`
    - Conda : `conda install -c conda-forge eccodes`
    - Other systems : See [https://confluence.ecmwf.int/display/ECC/ecCodes+installation]

2. (Optional) Install virtualenv
    
    python -m virtualenv venv
    source venv/bin/activate

3. Install requirements:

    python -m pip install -r requirements.txt -r requirements-dev.txt

4. Test that eccodes works:

    python -m eccodes selfcheck

5. Install package locally in editable mode:

    python -m pip install -e .

6. Run tests

    python -m pytest

7. Run the CLI

    epps-cli -h

## Files

Below as descriptions of some files.

### Makefile

Makefile works on unix-like systems only. You can run commands, such as:

    make prepare-dev
    make dev-install
    make tests
    make lint
    make typechecks
    make codestyle
    make snapshot
    make dist

You need to modify this file to suit your needs. 