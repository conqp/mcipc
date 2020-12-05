"""Common protocol stuff."""

from __future__ import annotations
from enum import Enum
from functools import partial
from ipaddress import ip_address, IPv4Address, IPv6Address
from random import randint
from typing import Iterable, Iterator, Union


__all__ = [
    'MAGIC',
    'decodeall',
    'ip_or_hostname',
    'BigEndianSignedInt32',
    'IPAddressOrHostname',
    'Type'
]


MAGIC = b'\xfe\xfd'
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


class BigEndianSignedInt32(int):
    """A big-endian, signed int32."""

    MIN = -2_147_483_648
    MAX = 2_147_483_647

    def __bytes__(self):
        """Returns the int as bytes."""
        return self.to_bytes(4, 'big', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> BigEndianSignedInt32:
        """Reutns the int from the given bytes."""
        return super().from_bytes(bytes_, 'big', signed=True)

    @classmethod
    def random_session_id(cls) -> BigEndianSignedInt32:
        """Returns a random session ID.
        See: https://wiki.vg/Query#Generating_a_Session_ID
        """
        return cls(randint(cls.MIN, cls.MAX) & SESSION_ID_MASK)


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
