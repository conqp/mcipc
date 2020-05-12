"""Common protocol stuff."""

from enum import Enum
from random import randint


__all__ = ['MAGIC', 'random_session_id', 'Type']


MAGIC = b'\xfe\xfd'


def random_session_id():
    """Returns a random session ID."""

    return randint(0, 32)


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
