"""Implementation of the xp command."""

from mcipc.rcon.client import Client


__all__ = ['xp']


# pylint: disable=C0103
def xp(self: Client, amount: int, player: str) -> str:
    """Gives the player the specified amount of XP."""

    return self.run('xp', amount, player)
