from ekrhizoc.cli.commands import commands


def test_commands():
    assert [C().name for C in commands] == ["crawl"]
