"""Implementation of the wsserver and connect commands."""

from mcipc.rcon.client import Client


__all__ = ['connect', 'wsserver']


def connect(self: Client, server_uri: str) -> str:
    """Connect to designated WebSocket server."""

    return self.run('connect', server_uri)


def wsserver(self: Client, server_uri: str) -> str:
    """Connect to designated WebSocket server."""

    return self.run('wsserver', server_uri)
