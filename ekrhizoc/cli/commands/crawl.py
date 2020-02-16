"""
This module contains the crawl command
"""
from argparse import ArgumentParser, Namespace

from ekrhizoc.cli.base_command import BaseCommand


class CrawlCommand(BaseCommand):
    """
    Initialise crawl command

    Example:
        ekrhizoc crawl -s "http://nichelia.com"
    """

    def __init__(self):
        self.name = "crawl"

    def add_args(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s",
            "--seed",
            required=True,
            help="The seed URL (root, initial url to crawl from)",
        )

    def validate_args(self, args: Namespace) -> None:
        pass

    def execute(self, args: Namespace):
        self.crawl()

    def crawl(self) -> str:
        raise NotImplementedError(f"Method: crawl is undefined for command {self.name}")
