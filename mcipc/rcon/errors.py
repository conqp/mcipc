"""Errors returned from Java Edition servers via RCON."""

from functools import lru_cache, partial
from re import fullmatch


__all__ = [
    'CommandError',
    'InvalidArgument',
    'InvalidInteger',
    'InvalidNameOrUUID',
    'LocationNotFound',
    'NoPlayerFound',
    'UnexpectedTrailingData',
    'UnknownCommand',
    'check_result'
]


class CommandError(Exception):
    """Indicates an error with an RCON command."""


class InvalidArgument(CommandError):
    """Represents an invalid argument error."""


class InvalidInteger(CommandError):
    """Represents an invalid argument error."""


class InvalidNameOrUUID(CommandError):
    """Indicates an invalid name or UUID."""


class LocationNotFound(CommandError):
    """Indicates that the given location could not be found."""


class NoPlayerFound(CommandError):
    """Indicates that no player was found."""


class UnexpectedTrailingData(CommandError):
    """Indicates unexpected trailing data."""


class UnknownCommand(CommandError):
    """Represents an unknown command error."""


ERRORS = {
    'Incorrect argument for command(.*)<--\\[HERE\\]': InvalidArgument,
    'Invalid integer(.*)<--\\[HERE\\]': InvalidInteger,
    'Invalid name or UUID(.*)<--\\[HERE\\]': InvalidNameOrUUID,
    'No player was found': NoPlayerFound,
    ('Expected whitespace to end one argument, but found trailing data'
     '(.*)<--\\[HERE\\]'): UnexpectedTrailingData,
    ('Unknown or incomplete command, see below for error'
     '(.*)<--\\[HERE\\]'): UnknownCommand
}


@lru_cache()
def get_exception(response: str) -> Exception:
    """Returns an exception based on a respnse string."""

    for regex, exception in ERRORS.items():
        if (match := fullmatch(regex, response)) is not None:
            return partial(exception, *match.groups())

    return None


def check_result(response: str) -> str:
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    if (exception := get_exception(response)) is not None:
        raise exception()

    return response
