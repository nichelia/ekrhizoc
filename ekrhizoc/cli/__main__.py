from argparse import ArgumentParser, Namespace
from typing import Callable, Dict

from ekrhizoc.cli.base_command import BaseCommand
from ekrhizoc.cli.commands import commands


def main() -> None:
    """
    Entry point to CLI
    Register all available CLI command modules as subcommands
    to `ekrhizoc` command.
    
    """
    instantiated_commands = [C() for C in commands]
    subcommands_map = {
        get_command_name(command): command for command in instantiated_commands
    }

    parser = configure_parser(subcommands_map)

    # Show help message if no subcommand is given
    args = parser.parse_args()
    if not getattr(args, "subcommand", False):
        return parser.print_help()

    # Map command name to run method
    subcommand = subcommands_map[args.subcommand]
    run(subcommand, args)
    return


def run(command: BaseCommand, args: Namespace) -> Callable:
    self_cleaning_class = getattr(command, "self_cleaning", False)
    try:
        if self_cleaning_class:
            with command as com:
                return com.run(args)
        return command.run(args)
    except SystemError as e:
        print(e)


def get_command_name(subcommand: BaseCommand) -> str:
    """
    Return a name for the command.
    Use object name value otherwise module name.
    """
    if "".__eq__(subcommand.name):
        return subcommand.__module__.split(".")[-1].replace("_", "-")

    return subcommand.name


def configure_parser(subcommands_map: Dict[str, BaseCommand]) -> ArgumentParser:
    """
    Add all subcommands to our CLI parser.
    """
    parser = ArgumentParser(
        prog="ekrhizoc", description="Command parser for ekrhizoc module"
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    for name, subcommand in subcommands_map.items():
        subparser = subparsers.add_parser(name)
        subcommand.add_args(subparser)

    return parser


if __name__ == "__main__":
    main()
