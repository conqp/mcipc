"""Implementation of the stop command."""

from mcipc.rcon.client import Client


__all__ = ['stop']


def stop(self: Client) -> str:
    """Stops the server."""

    return self.run('stop')
