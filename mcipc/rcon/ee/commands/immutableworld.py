"""Implementation of the immutableworld command."""

from mcipc.rcon.client import Client


__all__ = ['immutableworld']


def immutableworld(self: Client, value: bool) -> str:
    """Toggles the world to be able altered or cannot be altered."""

    return self.run('immutableworld', value)
