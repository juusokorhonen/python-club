# README

## Installation instructions MacOS

    pyenv install 3.9.9
    pyenv local 3.9.9
    python -m pip install --upgrade virtualenv setuptools wheel pip
    python -m virtualenv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt -r requirements-dev.txt

## Installation instructions Windows

Install Python 3.9.10 from https://www.python.org/downloads/release/python-3910/

The following command line instructions are for MinGW and you need to adapt if 
using normal Windows terminal or WSL.

    py -3.9.10 -m pip install --upgrade virtualenv setuptools wheel pip
    py -3.9.10 -m virtualenv venv
    source venv/Scripts/activate
    python -m pip install -r requirements.txt -r requirements-dev.txt

## Files

### Simple Hello Qt application

01_hello.py
01_hello.qml

### Simple, but modular Qt application

qtcalculator/
    __init__.py
    __main__.py
    application_window.py
    calc.py
    main_engine.py
    views/
        main.qml
        components/
            Display.qml
            MyButton.qml
            NumberPad.qml

### Installation files for setuptools

pyproject.toml
setup.py
setup.cfg