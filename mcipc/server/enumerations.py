"""Common enumerations."""

from __future__ import annotations
from enum import Enum
from typing import IO

from mcipc.server.datatypes import VarInt


__all__ = ['State']


class State(Enum):
    """Protocol state."""

    HANDSHAKE = VarInt(0)
    STATUS = VarInt(1)
    LOGIN = VarInt(2)

    @classmethod
    def read(cls, file: IO) -> State:
        """Reads the state from a file-like object."""
        return cls(VarInt.read(file))
