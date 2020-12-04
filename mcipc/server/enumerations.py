"""Common enumerations."""

from __future__ import annotations
from enum import Enum
from socket import socket

from mcipc.server.datatypes import VarInt


__all__ = ['State']


class State(Enum):
    """Protocol state."""

    HANDSHAKE = VarInt(0)
    STATUS = VarInt(1)
    LOGIN = VarInt(2)

    @classmethod
    def from_socket(cls, sock: socket) -> State:
        """Reads the state from the respective connection."""
        return cls(VarInt.from_socket(sock))
