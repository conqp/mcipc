"""Data types for the server protocol."""

from mcipc.server.functions import rshift


__all__ = ['VarInt']


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
    def from_connection(cls, connection):
        """Reads a VarInt from the respective bytes."""
        bytec = 0
        result = 0

        while True:
            byte = connection.recv(1)
            read = int.from_bytes(byte, 'little')
            value = read & 0b01111111
            shift = 7 * bytec
            result |= value << shift
            bytec += 1

            if (read & 0b10000000) == 0:
                break

        return cls(result)
