"""Errors returned from Java Edition servers via RCON."""

from __future__ import annotations
from functools import lru_cache
from re import fullmatch


__all__ = [
    'CommandError',
    'InvalidArgument',
    'InvalidInteger',
    'UnknownCommand',
    'LocationNotFound',
    'check_result'
]


class CommandError(Exception):
    """Indicates an error with an RCON command."""


class InvalidArgument(CommandError):
    """Represents an invalid argument error."""


class InvalidInteger(CommandError):
    """Represents an invalid argument error."""


class UnknownCommand(CommandError):
    """Represents an unknown command error."""


class LocationNotFound(CommandError):
    """Indicates that the given location could not be found."""



ERRORS = {
    InvalidArgument: 'Incorrect argument for command(.*)<--\\[HERE\\]',
    InvalidInteger: 'Invalid integer(.*)<--\\[HERE\\]',
    UnknownCommand: ('Unknown or incomplete command, see '
                     'below for error(.*)<--\\[HERE\\]')
}


@lru_cache()
def get_exception(response: str) -> Exception:
    """Returns an exception based on a respnse string."""

    for exception, regex in ERRORS.items():
        if (match := fullmatch(regex, response)) is not None:
            return exception(*match.groups())

    return None


def check_result(response: str) -> str:
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    if (exception := get_exception(response)) is not None:
        raise exception     # pylint: disable=E0702

    return response
