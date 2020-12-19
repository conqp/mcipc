"""Implementation of the position command."""

from mcipc.rcon.client import Client


__all__ = ['position']


def position(self: Client) -> str:
    """Toggles player coordinates to be displayed on the HUD."""

    return self.run('position')
