"""command_init_test
"""
from ekrhizoc.cli.commands import COMMANDS


def test_commands():
    """test_commands
    """
    assert [C().name for C in COMMANDS] == ["crawl"]
