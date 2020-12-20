"""Implementation of the function command."""

from mcipc.rcon.client import Client


__all__ = ['function']


def function(self: Client, name: str) -> str:
    """Runs the given function."""

    return self.run('function', name)
