"""Implementation of the clear command."""

from mcipc.rcon.client import Client


__all__ = ['clear']


def clear(self: Client, targets: str = None, item: str = None,
          max_count: int = None) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Java Edition implementation.
    """

    return self.run('clear', targets, item, max_count)
