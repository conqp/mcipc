"""Implementation of the gamemode command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import GameMode


__all__ = ['gamemode']


def gamemode(
        self: Client,
        mode: GameMode,
        target: Optional[str] = None
) -> str:
    """Sets the game mode."""

    return self.run('gamemode', mode, target)
