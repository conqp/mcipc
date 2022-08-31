"""Minecraft-specific client."""

from threading import Lock

from mcipc.rcon.functions import str_until_none

from rcon import source

__all__ = ["Client"]

LOCK = Lock()


class Client(source.Client):
    """An RCON client for Minecraft."""

    def run(self, command: str, *arguments: str) -> str:
        """Runs the command with additional checks."""

        with LOCK:
            return super().run(*str_until_none(command, *arguments))
