from ekrhizoc.bot.crawlers import crawlers


def test_commands():
    assert [C().name for C in crawlers] == ["universal-bfs"]
