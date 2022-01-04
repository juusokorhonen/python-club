# Installation instructions

## Check python version

    python -V

Make sure that the version is at least 3.8.

## Select python version

### MacOS / Linux

Use `pyenv`.

    pyenv install 3.9.7
    pyenv local 3.9.7

### Windows

Download Python 3.9.9 from https://www.python.org/downloads/release/python-399/ and install.

Instead of `python` use the command `py -3.9` instead.

## Upgrade pip and install essentials

    # MacOS and Linux
    python -m pip install --upgrade pip setuptools wheel virtualenv

    # Windows
    py -3.9 -m pip install --upgrade pip setuptools wheel virtualenv

## Create virtualenv

Make sure you are in the correct folder (ie. here).

    # MacOS and Linux
    python -m virtualenv venv

    # Windows
    py -3.9 -m virtualenv venv

## Activate virtualenv

    # MacOS and Linux
    source venv/bin/activate

    # Git-Bash and WSL on Windows
    source venv/Scripts/activate

    # Command prompt in Windows
    venv\Scripts\activate

## Install requirements

    python -m pip install -r requirements.txt
