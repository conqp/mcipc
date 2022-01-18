"""Implementation of the publish command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['publish']


def publish(self: Client, port: Optional[int] = None) -> str:
    """Opens singleplayer world to the local network."""

    return self.run('publish', port)
