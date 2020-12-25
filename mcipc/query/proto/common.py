"""Common protocol stuff."""

from __future__ import annotations
from enum import Enum
from functools import partial
from ipaddress import IPv4Address, IPv6Address, ip_address
from random import randint
from typing import IO, Iterable, Iterator, Union


__all__ = [
    'MAGIC',
    'NULL',
    'decodeall',
    'ip_or_hostname',
    'random_session_id',
    'IPAddressOrHostname',
    'Type'
]


MAGIC = b'\xfe\xfd'
NULL = b'\0'
SESSION_ID_MASK = 0x0F0F0F0F


IPAddressOrHostname = Union[IPv4Address, IPv6Address, str]


def decodeall(blocks: Iterable[bytes], encoding='latin-1') -> Iterator[str]:
    """Decodes all byte blocks with the given encoding."""

    return map(partial(bytes.decode, encoding=encoding), blocks)


def ip_or_hostname(string: str) -> IPAddressOrHostname:
    """Returns an IPv4 or IPv6 address if applicable, else a string."""

    try:
        return ip_address(string)
    except ValueError:
        return string


def random_session_id() -> BigEndianSignedInt32:
    """Returns a random session ID.
    See: https://wiki.vg/Query#Generating_a_Session_ID
    """

    random = randint(BigEndianSignedInt32.MIN, BigEndianSignedInt32.MAX)
    return BigEndianSignedInt32(random & SESSION_ID_MASK)


class BigEndianSignedInt32(int):
    """A big-endian, signed int32."""

    MIN = -2_147_483_648
    MAX = 2_147_483_647

    def __init__(self, *_):
        """Checks the boundaries."""
        super().__init__()

        if not self.MIN <= self <= self.MAX:
            raise ValueError('Signed int32 out of bounds:', self)

    def __bytes__(self):
        """Returns the int as bytes."""
        return self.to_bytes(4, 'big', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> BigEndianSignedInt32:
        """Reutns the int from the given bytes."""
        return super().from_bytes(bytes_, 'big', signed=True)

    @classmethod
    def read(cls, file: IO) -> BigEndianSignedInt32:
        """Reads a big endian int32 from a file-like object."""
        return cls.from_bytes(file.read(4))


class Type(Enum):
    """Request type."""

    HANDSHAKE = 9
    STAT = 0

    def __bytes__(self):
        """Reuturns the integer value as big endian."""
        return self.value.to_bytes(1, 'big')    # pylint: disable=E1101

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> Type:
        """Returns the type from the respective bytes."""
        return cls(int.from_bytes(bytes_, 'big'))

    @classmethod
    def read(cls, file: IO) -> Type:
        """Reads the type from a file-like object."""
        return cls.from_bytes(file.read(1))
