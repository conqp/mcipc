"""Datastructures to represent help on commands."""

from typing import NamedTuple


__all__ = ['Command', 'Help']


class Command(NamedTuple):
    """Represents a command / arguments tuple."""

    command: str
    arguments: str

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

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {name: command.to_json() for name, command in self.items()}
