"""Minecraft-specific client."""

from contextlib import suppress

from rcon import Client

from mcipc.rcon.exceptions import InvalidArgument
from mcipc.rcon.exceptions import NotApplicable
from mcipc.rcon.exceptions import UnknownCommand
from mcipc.rcon.functions import str_until_none


__all__ = ['Client']


EXCEPTIONS = (UnknownCommand, InvalidArgument)


def check_result(response: str) -> str:
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    for exception in EXCEPTIONS:
        with suppress(NotApplicable):
            raise exception.from_string(response)

    return response


class Client(Client):  # pylint: disable=E0102
    """An RCON client for Minecraft."""

    def run(self, command: str, *arguments: str):   # pylint: disable=W0221
        """Runs the command with additional checks."""
        return check_result(super().run(*str_until_none(command, *arguments)))
