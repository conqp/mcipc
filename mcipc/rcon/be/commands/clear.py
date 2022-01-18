"""Implementation of the clear command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['clear']


def clear(
        self: Client,
        player: Optional[str] = None,
        item_name: Optional[str] = None,
        data: Optional[int] = None,
        max_count: Optional[int] = None
) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Bedrock Edition implementation.
    """

    return self.run('clear', player, item_name, data, max_count)
