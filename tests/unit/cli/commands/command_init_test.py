from ekrhizoc.cli.commands import COMMANDS


def test_commands():
    assert [C().name for C in COMMANDS] == ["crawl"]
