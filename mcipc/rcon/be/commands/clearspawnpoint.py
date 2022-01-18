"""Implementation of the clearspawnpoint."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['clearspawnpoint']


def clearspawnpoint(self: Client, player: Optional[str] = None) -> str:
    """Used to remove spawnpoints in the world."""

    return self.run('clearspawnpoint', player)
