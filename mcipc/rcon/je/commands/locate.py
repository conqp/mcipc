"""Implementation of the locate command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.je.types import Structure
from mcipc.rcon.response_types.location import parse


__all__ = ['locate']


@parsed(parse)
def locate(client: Client, structure: Structure) -> str:
    """Locates the respective structure."""

    return client.run('locate', structure)
