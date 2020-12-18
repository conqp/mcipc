"""Game mode related commands."""

from mcipc.rcon.proto import Client
from mcipc.rcon.types import GameMode


__all__ = ['defaultgamemode', 'gamemode']


def defaultgamemode(self: Client, mode: GameMode) -> str:
    """Sets the default game mode."""

    return self.run('defaultgamemode', mode)


def gamemode(self: Client, mode: GameMode, target: str = None) -> str:
    """Sets the game mode."""

    return self.run('gamemode', mode, target)
