"""Low-level protocol stuff."""

from __future__ import annotations
from enum import Enum
from logging import getLogger
from random import randint
from socket import SOCK_STREAM
from typing import NamedTuple

from mcipc.common import BaseClient
from mcipc.rcon.exceptions import InvalidPacketStructure
from mcipc.rcon.exceptions import RequestIdMismatch
from mcipc.rcon.exceptions import WrongPassword


__all__ = ['LittleEndianSignedInt32', 'Type', 'Packet', 'Client']


LOGGER = getLogger(__file__)
TAIL = b'\0\0'


class LittleEndianSignedInt32(int):
    """A little-endian, signed int32."""

    MIN = -2_147_483_648
    MAX = 2_147_483_647

    def __bytes__(self):
        """Returns the integer as signed little endian."""
        return self.to_bytes(4, 'little', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> LittleEndianSignedInt32:
        """Creates the integer from the given bytes."""
        return super().from_bytes(bytes_, 'little', signed=True)

    @classmethod
    def random_request_id(cls) -> LittleEndianSignedInt32:
        """Generates a random request ID."""
        return cls(randint(0, cls.MAX))     # A random non-negative int32.


class Type(Enum):
    """Available packet types."""

    LOGIN = 3
    COMMAND = 2
    RESPONSE = 0

    def __int__(self):
        """Returns the actual integer value."""
        return self.value

    def __bytes__(self):
        """Returns the integer value as little endian."""
        return int(self).to_bytes(4, 'little', signed=True)

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> Type:
        """Creates a type from the given bytes."""
        return cls(int.from_bytes(bytes_, 'little', signed=True))


class Packet(NamedTuple):
    """An RCON packet."""

    request_id: LittleEndianSignedInt32
    type: Type
    payload: str

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = bytes(self.request_id)
        payload += bytes(self.type)
        payload += self.payload.encode()
        payload += TAIL
        size = len(payload).to_bytes(4, 'little', signed=True)
        return size + payload

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> Packet:
        """Creates a packet from the respective bytes."""
        request_id = LittleEndianSignedInt32.from_bytes(bytes_[:4])
        type_ = Type.from_bytes(bytes_[4:8])
        payload = bytes_[8:-2].decode()

        if (tail := bytes_[-2:]) != TAIL:
            raise InvalidPacketStructure('Invalid tail.', tail, TAIL)

        return cls(request_id, type_, payload)

    @classmethod
    def from_args(cls, *args: str) -> Packet:
        """Creates a command packet."""
        request_id = LittleEndianSignedInt32.random_request_id()
        return cls(request_id, Type.COMMAND, ' '.join(args))

    @classmethod
    def from_login(cls, passwd: str) -> Packet:
        """Creates a login packet."""
        request_id = LittleEndianSignedInt32.random_request_id()
        return cls(request_id, Type.LOGIN, passwd)


class Client(BaseClient):
    """An RCON client."""

    def __init__(self, host: str, port: int, timeout: float = None):
        """Initializes the base client with the SOCK_STREAM socket type."""
        super().__init__(SOCK_STREAM, host, port, timeout=timeout)

    def communicate(self, packet: Packet) -> Packet:
        """Sends and receives a packet."""
        self._socket.send(bytes(packet))
        header = self._socket.recv(4)
        length = int.from_bytes(header, 'little')
        payload = self._socket.recv(length)
        response = Packet.from_bytes(payload)

        if response.request_id == packet.request_id:
            return response

        raise RequestIdMismatch(packet.request_id, response.request_id)

    def login(self, passwd: str) -> bool:
        """Performs a login."""
        packet = Packet.from_login(passwd)

        try:
            self.communicate(packet)
        except RequestIdMismatch as mismatch:
            if mismatch.received == -1:
                raise WrongPassword() from None

            raise

        return True

    def run(self, command: str, *arguments: str, raw: bool = False) -> str:
        """Runs a command."""
        packet = Packet.from_args(command, *arguments)
        response = self.communicate(packet)
        return response if raw else response.payload
