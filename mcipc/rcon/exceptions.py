"""RCON exceptions."""

from __future__ import annotations
from contextlib import suppress
from re import fullmatch


__all__ = [
    'CommandError',
    'InvalidArgument',
    'NotALocation',
    'RequestIdMismatch',
    'StructureNotFound',
    'UnknownCommand',
    'WrongPassword',
    'check_error'
]


CMD_ERR = 'Unknown or incomplete command, see below for error(.*)<--\\[HERE\\]'
ARG_ERR = 'Incorrect argument for command(.*)<--\\[HERE\\]'


class NotALocation(ValueError):
    """Indicates that the given text is not a valid location value."""


class RequestIdMismatch(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent: int, received: int):
        """Sets the sent and received request IDs."""
        super().__init__(sent, received)
        self.sent = sent
        self.received = received


class StructureNotFound(ValueError):
    """Indicates that the given structure could not be found."""

    def __init__(self, structure):
        """Sets the invalid structure's name."""
        super().__init__(structure)
        self.structure = structure


class WrongPassword(Exception):
    """Indicates a wrong RCON password."""


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


def check_error(string: str):
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    for exception in (UnknownCommand, InvalidArgument):
        with suppress(NotApplicable):
            raise exception.from_string(string)
