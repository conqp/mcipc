"""RCON exceptions."""

from __future__ import annotations
from re import fullmatch


__all__ = [
    'CommandError',
    'InvalidArgument',
    'LocationNotFound',
    'NotALocation',
    'UnknownCommand'
]


CMD_ERR = 'Unknown or incomplete command, see below for error(.*)<--\\[HERE\\]'
ARG_ERR = 'Incorrect argument for command(.*)<--\\[HERE\\]'


class LocationNotFound(ValueError):
    """Indicates that the given location could not be found."""

    def __init__(self, name):
        """Sets the invalid location's name."""
        super().__init__(name)
        self.name = name


class NotALocation(ValueError):
    """Indicates that the given text is not a valid location value."""


class NotApplicable(Exception):
    """Indicates that the given command is not applicable."""


class CommandError(Exception):
    """Indicates an error with an RCON command."""

    def __init__(self, command: str):
        """Sets the faulty command."""
        super().__init__(command)
        self.command, *self.args = command.split()

    @classmethod
    def from_string(cls, string: str) -> CommandError:
        """Creates the error from the given return value."""
        # pylint: disable=E1101
        if (match := fullmatch(cls.REGEX, string)) is not None:
            return cls(*match.groups())

        raise NotApplicable()


class UnknownCommand(CommandError):
    """Represents an unknown command error."""

    REGEX = CMD_ERR


class InvalidArgument(CommandError):
    """Represents an invalid argument error."""

    REGEX = ARG_ERR
