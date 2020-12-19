"""Client implementation for Bedrock Edition."""

from mcipc.rcon.commands import BEDROCK_COMMANDS
from mcipc.rcon.functions import attributes
from mcipc.rcon.proto import Client


__all__ = ['Client']


@attributes(BEDROCK_COMMANDS)
class Client(Client):   # pylint: disable=E0102
    """RCON client for the Bedrock Edition."""
