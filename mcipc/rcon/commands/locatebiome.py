"""Implementation of the locatebiome command."""

from mcipc.rcon.exceptions import NotALocation, LocationNotFound
from mcipc.rcon.proto import Client
from mcipc.rcon.response_types import Location


def locatebiome(self: Client, biome: BiomeID) -> str:
    """Locates the given biome."""

    response = self.run('locatebiome', biome)

    try:
        return Location.from_response(response)
    except NotALocation:
        raise LocationNotFound(biome) from None
