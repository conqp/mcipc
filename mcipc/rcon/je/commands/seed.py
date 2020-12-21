"""Implementation of the seed command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.response_types.seed import parse


__all__ = ['seed']


@parsed(parse)
def seed(self: Client) -> str:
    """Returns the server seed."""

    return self.run('seed')
