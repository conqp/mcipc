"""Parses Help response type."""

from mcipc.rcon.response_types import Command, Help


__all__ = ['parse']


def parse_command(text: str) -> Command:
    """Creates the command from a string."""

    try:
        command, arguments = text.split(maxsplit=1)
    except ValueError:
        command = text
        arguments = None

    return Command(command, arguments)


def parse(text: str) -> Help:
    """Creates the help object from a server response text."""

    commands = map(parse_command, filter(None, text.split('/')))
    return Help((command.command, command) for command in commands)
