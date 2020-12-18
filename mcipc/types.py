"""Common data types."""

from __future__ import annotations
from ipaddress import IPv4Address, IPv6Address
from random import randint
from typing import Union


__all__ = [
    'BigEndianSignedInt32',
    'IPAddressOrHostname',
    'LittleEndianSignedInt32',
    'SignedInt32'
]


IPAddressOrHostname = Union[IPv4Address, IPv6Address, str]


class SignedInt32(int):
    """A signed int32."""

    MIN = -2_147_483_648
    MAX = 2_147_483_647

    def __init__(self, *_):
        """Checks the boundaries."""
        super().__init__()

        if not self.MIN <= self <= self.MAX:
            raise ValueError('Signed int32 out of bounds:', self)

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
