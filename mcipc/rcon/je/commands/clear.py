"""Implementation of the clear command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['clear']


def clear(
        self: Client,
        targets: Optional[str] = None,
        item: Optional[str] = None,
        max_count: Optional[int] = None
) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Java Edition implementation.
    """

    return self.run('clear', targets, item, max_count)
