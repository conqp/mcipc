"""Implementation of the transferserver command."""

from mcipc.rcon.client import Client


__all__ = ['transferserver']


def transferserver(self: Client, server: str, port: int) -> str:
    """Transfer player to another server."""

    return self.run('transferserver', server, port)
