"""Implementation of the worldbuilder and wb commands."""

from mcipc.rcon.client import Client


__all__ = ['wb', 'worldbuilder']


def wb(self: Client) -> str:
    """Toggles the world builder feature."""

    return self.run('wb')


def worldbuilder(self: Client) -> str:
    """Toggles the world builder feature."""

    return self.run('worldbuilder')
