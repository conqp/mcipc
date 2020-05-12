"""Common protocol stuff."""

from enum import Enum
from random import randint


__all__ = ['MAGIC', 'random_session_id', 'Type']


MAGIC = b'\xfe\xfd'
SESSION_ID_MASK = 0x0F0F0F0F


def random_session_id() -> int:
    """Returns a random session ID.
    See: https://wiki.vg/Query#Generating_a_Session_ID
    """

    return randint(-2147483648, 2147483647 + 1) & SESSION_ID_MASK


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
