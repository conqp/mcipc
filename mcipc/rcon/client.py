"""Minecraft-specific client."""

from contextlib import suppress

from rcon import Client

from mcipc.rcon.exceptions import InvalidArgument
from mcipc.rcon.exceptions import NotApplicable
from mcipc.rcon.exceptions import UnknownCommand
from mcipc.rcon.functions import str_until_none


__all__ = ['MinecraftClient']


EXCEPTIONS = (UnknownCommand, InvalidArgument)


def check_result(response: str) -> str:
    """Raises an appropriate exceptions if
    the string is considered erroneous.
    """

    for exception in EXCEPTIONS:
        with suppress(NotApplicable):
            raise exception.from_string(response)

    return response


class MinecraftClient(Client):  # pylint: disable=R0903
    """An RCON client for Minecraft."""

    def run(self, command: str, *arguments: str):
        """Runs the command with additional checks."""
        return check_result(super().run(*str_until_none(command, *arguments)))
