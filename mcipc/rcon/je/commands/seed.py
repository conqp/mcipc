"""Implementation of the seed command."""

from mcipc.rcon.client import Client


__all__ = ['seed']


def seed(self: Client) -> str:
    """Returns the server seed."""

    return self.run('seed')
