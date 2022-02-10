import argparse

from epps.cli import do_nothing, process_get


def test_nothing():
    bogus_args = argparse.Namespace()
    return_code =  do_nothing(bogus_args)
    assert isinstance(return_code, int)
    assert return_code == 1


def test_running_tests():
    bogus_args = argparse.Namespace()
    assert process_get(bogus_args) == -1

    bogus_args.subcommand = "weather"
    assert process_get(bogus_args) == 0

    bogus_args.subcommand = "foobar"
    assert process_get(bogus_args) == -1
