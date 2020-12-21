"""Implementation of the locatebiome command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import Biome


def locatebiome(self: Client, biome: Biome) -> str:
    """Locates the given biome."""

    return self.run('locatebiome', biome)
