"""Implementation of the seed command."""

from mcipc.rcon.response_types import Seed
from mcipc.rcon.proto import Client


__all__ = ['seed']


def seed(self: Client) -> Seed:
    """Returns the server seed."""

    return Seed.from_response(self.run('seed'))
