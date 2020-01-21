"""Datastructures to represent help on commands."""

from logging import getLogger
from typing import Iterable, NamedTuple, Tuple


LOGGER = getLogger(__file__)


class Command(NamedTuple):
    """Represents a command / arguments tuple."""

    command: str
    arguments: str

    @classmethod
    def from_tuple(cls, tpl: Tuple[str]):
        """Creates the command from a tuple."""
        try:
            command, arguments, *superfluous = tpl
        except ValueError:
            command, = tpl
            arguments = None
            superfluous = None

        if superfluous:
            items = len(superfluous) + 2
            raise ValueError(f'Expected one or two items. Got {items}.')

        return cls(command, arguments)

    @property
    def usage(self) -> str:
        """Returns a docopt-compliant usage string."""
        usage = f'Usage: {self.command}'

        if self.arguments:
            usage += f' {self.arguments}'

        return usage

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'command': self.command, 'arguments': self.arguments}


class Help(dict):
    """command: arguments key pairs."""

    @classmethod
    def from_sequence(cls, sequence: Iterable):
        """Creates the help from the respective sequence."""
        commands = (Command.from_tuple(item) for item in sequence)
        return cls((command.command, command) for command in commands)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {name: command.to_json() for name, command in self.items()}
