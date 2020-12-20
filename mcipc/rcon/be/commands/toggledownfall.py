"""Implements the toggledownfall command."""

from mcipc.rcon.client import Client


__all__ = ['toggledownfall']


def toggledownfall(self: Client) -> str:
    """Toggles downfall."""

    return self.run('toggledownfall')
