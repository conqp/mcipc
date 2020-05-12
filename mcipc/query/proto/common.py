"""Common protocol stuff."""

from enum import Enum
from random import randint


__all__ = ['MAGIC', 'random_int32', 'Type']


MAGIC = b'\xfe\xfd'


def random_int32() -> int:
    """Returns a random int32."""

    return randint(-2147483648, 2147483647 + 1)


class Type(Enum):
    """Request type."""

    HANDSHAKE = 9
    STAT = 0

    def __bytes__(self):
        """Reuturns the integer value as big endian."""
        return self.value.to_bytes(1, 'big')    # pylint: disable=E1101

    @classmethod
    def from_bytes(cls, bytes_):
        """Returns the type from the respective bytes."""
        return cls(int.from_bytes(bytes_, 'big'))
