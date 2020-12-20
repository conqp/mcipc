"""Implementation of the clearspawnpoint."""

from mcipc.rcon.client import Client


__all__ = ['clearspawnpoint']


def clearspawnpoint(self: Client, player: str = None) -> str:
    """Used to remove spawnpoints in the world."""

    return self.run('clearspawnpoint', player)
