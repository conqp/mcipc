"""Minecraft-specific client."""

from rcon import Client

from mcipc.rcon.functions import str_until_none


__all__ = ['Client']


class Client(Client):  # pylint: disable=E0102
    """An RCON client for Minecraft."""

    # pylint: disable=W0221
    def run(self, command: str, *arguments: str) -> str:
        """Runs the command with additional checks."""
        return super().run(*str_until_none(command, *arguments))
