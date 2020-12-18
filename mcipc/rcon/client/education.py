"""Client for the education edition."""

from mcipc.rcon.commands import EDUCATION_COMMANDS
from mcipc.rcon.functions import attributes
from mcipc.rcon.proto import Client


__all__ = ['Client']


@attributes(EDUCATION_COMMANDS)
class Client(Client):   # pylint: disable=E0102
    """Client for the Education Edition."""
