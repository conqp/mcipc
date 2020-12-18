"""Implementation of the locate command."""

from mcipc.rcon.exceptions import NotALocation, LocationNotFound
from mcipc.rcon.proto import Client
from mcipc.rcon.response_types import Location


__all__ = ['locate']


def locate(client: Client, structure: str) -> Location:
    """Locates the respective structure."""

    response = client.run('locate', structure)

    try:
        return Location.from_response(response)
    except NotALocation:
        raise LocationNotFound(structure) from None
