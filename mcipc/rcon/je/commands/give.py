"""Implementation of the give command."""

from mcipc.rcon.client import Client


__all__ = ['give']


def give(self: Client, target: str, item: str, count: int = None) -> str:
    """Gives an item to one or more players."""

    return self.run('give', target, item, count)
