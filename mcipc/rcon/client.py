"""Minecraft-specific client."""

from rcon import source

from mcipc.rcon.functions import str_until_none


__all__ = ['Client']


class Client(source.Client, max_packet_size=4096):
    """An RCON client for Minecraft."""

    def run(self, command: str, *arguments: str) -> str:
        """Runs the command with additional checks."""
        return super().run(*str_until_none(command, *arguments))
