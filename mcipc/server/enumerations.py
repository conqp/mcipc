"""Common enumerations."""

from enum import Enum

from mcipc.server.datatypes import VarInt


__all__ = ['State']


class State(Enum):
    """Protocol state."""

    HANDSHAKE = VarInt(0)
    STATUS = VarInt(1)
    LOGIN = VarInt(2)

    @classmethod
    def from_connection(cls, connection):
        """Reads the state from the respective connection."""
        var_int = VarInt.from_connection(connection)
        return cls(var_int)
