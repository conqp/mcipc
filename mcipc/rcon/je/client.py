"""Client implementation for Java Edition."""

from mcipc.rcon.proto import Client


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """A high-level RCON client with methods for the Java Edition."""
