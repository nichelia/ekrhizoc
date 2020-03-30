from ekrhizoc.bot.crawlers import CRAWLERS


def test_commands():
    assert [C().name for C in CRAWLERS] == ["universal-bfs"]
