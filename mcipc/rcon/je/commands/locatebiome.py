"""Implementation of the locatebiome command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.je.types import Biome
from mcipc.rcon.response_types.location import parse


__all__ = ['locatebiome']


@parsed(parse)
def locatebiome(self: Client, biome: Biome) -> str:
    """Locates the given biome."""

    return self.run('locatebiome', biome)
