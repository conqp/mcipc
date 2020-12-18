"""Datastructures to represent help on commands."""

from __future__ import annotations
from typing import NamedTuple


__all__ = ['Command', 'Help']


class Command(NamedTuple):
    """Represents a command / arguments tuple."""

    command: str
    arguments: str

    @classmethod
    def from_string(cls, text: str) -> Command:
        """Creates the command from a string."""
        try:
            command, arguments = text.split(maxsplit=1)
        except ValueError:
            command = text
            arguments = None

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
    def from_response(cls, text: str) -> Help:
        """Creates the help object from a server response text."""
        commands = map(Command.from_string, filter(None, text.split('/')))
        return cls((command.command, command) for command in commands)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {name: command.to_json() for name, command in self.items()}
