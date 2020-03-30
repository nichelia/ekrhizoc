"""crawl_test
"""
import time
from argparse import ArgumentParser

import pytest

from ekrhizoc.cli.commands.crawl import CrawlCommand


class TestCrawlCommand:
    """TestCrawlCommand
    """

    @pytest.mark.parametrize(
        "args, error",
        [
            (["--seed", "http://example.com"], False),
            (["-s", "http://example.com"], False),
            (["--seed", "http://example.com"], False),
            (["-s", "http://example.com"], False),
            (["--seed", "1"], False),
            (["--seed", None], False),
            (["--seed", "http://example.com", "--filename", "example"], False),
            (["-s", "http://example.com", "-f", "example"], False),
            (["--random", "http://example.com"], True),
            ([], True),
        ],
    )
    def test_add_args(self, args, error):
        """test_add_args
        """
        parser = ArgumentParser()
        CrawlCommand().add_args(parser)
        if error:
            with pytest.raises(SystemExit):
                parser.parse_args(args)
        else:
            parsed_args = parser.parse_args(args)
            assert parsed_args.seed == args[1]

            if "--filename" in args or "-f" in args:
                assert parsed_args.filename == args[3]
            else:
                # Defaults to datetime format
                assert time.strptime(parsed_args.filename, "%Y%m%d-%H%M%S")

    @pytest.mark.parametrize(
        "args, error",
        [
            (["-s", "http://example.com"], False),
            (["-s", "example.com"], True),
            (["-s", "None"], True),
            (["-s", None], True),
            (["-s", ""], True),
            (["-s", "http:///example.com"], True),
            (["-s", "http://www.example.com"], False),
            (["-s", "www.example.com"], True),
            (["-s", "1"], True),
            (["-s", "www4r$56exampleergegom"], True),
        ],
    )
    def test_validate_args(self, args, error):
        """test_validate_args
        """
        parser = ArgumentParser()
        command = CrawlCommand()
        command.add_args(parser)
        parsed_args = parser.parse_args(args)
        if error:
            with pytest.raises(Exception):
                command.validate_args(parsed_args)
        else:
            assert command.validate_args(parsed_args) != ""

    # TODO: Unit test for test_execute

    # TODO: Unit test for test_crawl
