import sys
import argparse
import logging
from pathlib import Path

from .weather import get_locations


def do_nothing(args: argparse.Namespace) -> int:
    return 0


def run_tests(args: argparse.Namespace):
    try:
        import pytest
    except ImportError:
        logging.error("Cannot run tests, pytest is not installed.")
        return -1
    logging.info("Running tests.")
    exit_code = pytest.main(["-x", Path(__file__).parent.resolve() / "../tests"])   # noqa: E501
    return exit_code


def process_get(args: argparse.Namespace) -> int:
    if "subcommand" not in args.__dict__:
        return -1

    if args.subcommand == "weather":
        locations = get_locations()
        print(", ".join(locations))
        return 0
    return -1


def cli():
    parser = argparse.ArgumentParser()

    loglevels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }

    def lowercase(value: str):
        return value.lower()

    parser.add_argument('-log', "--loglevel",
                        default="warning",
                        choices=loglevels.keys(),
                        type=lowercase,
                        help="Logging level to use. Example: 'debug'. Default: 'warning'.")   # noqa: E501

    commands = {
        'nothing': do_nothing,
        'get': process_get,
    }
    cmdparsers = parser.add_subparsers(dest="command", required=True)
    nothing_parser = cmdparsers.add_parser('nothing')   # noqa: F841
    get_parser = cmdparsers.add_parser('get')
    get_parser.add_argument("subcommand", help="What to get", choices=("weather", ))   # noqa: E501

    args = parser.parse_args()
    logging.basicConfig(level=loglevels[args.loglevel])

    sys.exit(commands[args.command](args))
