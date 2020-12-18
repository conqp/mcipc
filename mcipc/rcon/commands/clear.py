"""Clear command implementation."""

from mcipc.rcon.proto import Client


__all__ = ['clear_be', 'clear_je']


def clear_be(self: Client, player: str = None, item_name: str = None,
             data: int = None, max_count: int = None) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Bedrock Edition implementation.
    """

    return self.run('clear', player, item_name, data, max_count)


def clear_je(self: Client, targets: str = None, item: str = None,
             max_count: int = None) -> str:
    """Clears items from player inventory, including
    items being dragged by the player.
    Java Edition implementation.
    """

    return self.run('clear', targets, item, max_count)
