"""Data types for the server protocol."""

from logging import getLogger
from typing import Callable

from mcipc.server.functions import rshift


__all__ = ['VarInt']


LOGGER = getLogger(__file__)


class VarInt(int):
    """Minecraft protocol VarInt type."""

    def __bytes__(self):
        """Returns the respective bytes."""
        if self == 0:
            return self.to_bytes(1, 'little')

        value = int(self)
        bytes_ = b''

        while True:
            temp = value & 0b01111111
            value = rshift(value, 7)

            if value:
                temp |= 0b10000000

            bytes_ += temp.to_bytes(1, 'little')

            if not value:
                break

        return bytes_

    @classmethod
    def read(cls, readfunc: Callable):
        """Reads a VarInt from the respective bytes."""
        bytes_count = 0
        result = 0

        while True:
            if bytes_count > 4:  # Compensate for start index 0.
                raise ValueError('VarInt is too big.')

            byte = readfunc(1)
            read = int.from_bytes(byte, 'little')
            value = read & 0b01111111
            shift = 7 * bytes_count
            result |= value << shift
            bytes_count += 1

            if (read & 0b10000000) == 0:
                break

        LOGGER.debug('Read %i bytes of VarInt.', bytes_count)
        return cls(result)
