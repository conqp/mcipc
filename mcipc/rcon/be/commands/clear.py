"""Implementation of the clear command."""

from mcipc.rcon.client import Client


__all__ = ['clear']


def clear(self: Client, player: str = None, item_name: str = None,
          data: int = None, max_count: int = None) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Bedrock Edition implementation.
    """

    return self.run('clear', player, item_name, data, max_count)
