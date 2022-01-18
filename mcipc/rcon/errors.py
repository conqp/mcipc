"""Errors returned from Java Edition servers via RCON."""

from re import fullmatch

from mcipc.rcon.exceptions import InvalidArgument
from mcipc.rcon.exceptions import InvalidInteger
from mcipc.rcon.exceptions import InvalidNameOrUUID
from mcipc.rcon.exceptions import NoPlayerFound
from mcipc.rcon.exceptions import UnexpectedTrailingData
from mcipc.rcon.exceptions import UnknownCommand


__all__ = ['check_result']


ERRORS = {
    r'Incorrect argument for command(.*)<--\[HERE\]': InvalidArgument,
    r'Invalid integer(.*)<--\[HERE\]': InvalidInteger,
    r'Invalid name or UUID(.*)<--\[HERE\]': InvalidNameOrUUID,
    'No player was found': NoPlayerFound,
    (r'Expected whitespace to end one argument, but found trailing data'
     r'(.*)<--\[HERE\]'): UnexpectedTrailingData,
    (r'Unknown or incomplete command, see below for error'
     r'(.*)<--\[HERE\]'): UnknownCommand
}


def check_result(response: str) -> str:
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    for regex, exception in ERRORS.items():
        if (match := fullmatch(regex, response)) is not None:
            raise exception(*match.groups())

    return response
