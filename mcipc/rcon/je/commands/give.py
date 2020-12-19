"""Implementation of the give command."""

from mcipc.rcon.proto import Client


__all__ = ['give']


def give(self: Client, target: str, item: str, count: int = None) -> str:
    """Gives an item to one or more players."""

    return give_be(self, target, item, count)
