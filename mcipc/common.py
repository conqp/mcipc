"""Stuff, common to Query and RCON."""

from __future__ import annotations
from random import randint
from socket import socket, SocketKind   # pylint: disable=E0611
from typing import Tuple


__all__ = [
    'BaseClient',
    'BigEndianSignedInt32',
    'LittleEndianSignedInt32',
    'SignedInt32'
]


class BaseClient:
    """A basic client."""

    def __init__(self, typ: SocketKind, host: str, port: int, *,
                 timeout: float = None):
        """Sets host an port."""
        self._socket = socket(type=typ)
        self.host = host
        self.port = port
        self.timeout = timeout

    def __enter__(self):
        """Conntects the socket."""
        self._socket.__enter__()
        self.connect()
        return self

    def __exit__(self, typ, value, traceback):
        """Delegates to the underlying socket's exit method."""
        self.close()
        return self._socket.__exit__(typ, value, traceback)

    @property
    def socket(self) -> Tuple[str, int]:
        """Returns a tuple of host and port."""
        return (self.host, self.port)

    def connect(self):
        """Conntects to the RCON server."""
        self._socket.settimeout(self.timeout)
        return self._socket.connect(self.socket)

    def close(self):
        """Disconnects from the RCON server."""
        return self._socket.close()


class SignedInt32(int):
    """A signed int32."""

    MIN = -2_147_483_648
    MAX = 2_147_483_647

    def __new__(cls, *args, **kwargs):
        """Creates a new integer with boundary checks."""
        if cls.MIN <= (i := super().__new__(cls, *args, **kwargs)) <= cls.MAX:
            return i

        raise ValueError('Signed int32 out of bounds:', int(i))

    @classmethod
    def random(cls, min: int = MIN, max: int = MAX, *,  # pylint: disable=W0622
               mask: int = None) -> SignedInt32:
        """Generates a random signed int32 with an optional bit mask."""
        if mask is None:
            return cls(randint(min, max))

        return cls(randint(min, max) & mask)


class BigEndianSignedInt32(SignedInt32):
    """A big-endian, signed int32."""

    def __bytes__(self):
        """Returns the int as bytes."""
        return self.to_bytes(4, 'big', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> BigEndianSignedInt32:
        """Reutns the int from the given bytes."""
        return super().from_bytes(bytes_, 'big', signed=True)


class LittleEndianSignedInt32(SignedInt32):
    """A little-endian, signed int32."""

    def __bytes__(self):
        """Returns the integer as signed little endian."""
        return self.to_bytes(4, 'little', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> LittleEndianSignedInt32:
        """Creates the integer from the given bytes."""
        return super().from_bytes(bytes_, 'little', signed=True)
