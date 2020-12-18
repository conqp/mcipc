"""Client implementation for Java Edition."""

from mcipc.rcon.commands import JAVA_COMMANDS
from mcipc.rcon.functions import attributes
from mcipc.rcon.proto import Client


__all__ = ['Client']


@attributes(JAVA_COMMANDS)
class Client(Client):   # pylint: disable=E0102
    """A high-level RCON client with methods for the Java Edition."""
