import argparse

from src.cli import create_parser


def test_create_parser() -> None:
    parser = create_parser()

    assert parser
    assert type(parser) == argparse.ArgumentParser

    actions = {action.dest for action in parser._actions}
    assert "files" in actions
    assert "report" in actions

