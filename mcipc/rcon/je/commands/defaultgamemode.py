"""Implementation of the defaultgamemode command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import GameMode


__all__ = ['defaultgamemode']


def defaultgamemode(self: Client, mode: GameMode) -> str:
    """Sets the default game mode."""

    return self.run('defaultgamemode', mode)
