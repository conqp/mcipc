"""Implementation of the locatebiome command."""

from mcipc.rcon.client import Client
from mcipc.rcon.exceptions import NotALocation, LocationNotFound
from mcipc.rcon.je.parsers.location import parse
from mcipc.rcon.je.types import Biome
from mcipc.rcon.response_types import Location


def locatebiome(self: Client, biome: Biome) -> Location:
    """Locates the given biome."""

    response = self.run('locatebiome', biome)

    try:
        return parse(response)
    except NotALocation:
        raise LocationNotFound(biome) from None
