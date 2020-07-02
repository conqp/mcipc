"""Low-level protocol stuff."""

from enum import Enum
from logging import getLogger
from random import randint
from socket import SOCK_STREAM
from typing import NamedTuple

from mcipc.common import BaseClient
from mcipc.rcon.exceptions import InvalidPacketStructure
from mcipc.rcon.exceptions import RequestIdMismatch
from mcipc.rcon.exceptions import WrongPassword


__all__ = ['Type', 'Packet', 'Client']


LOGGER = getLogger(__file__)
TAIL = b'\0\0'


def random_request_id() -> int:
    """Returns a random, positive int32."""

    return randint(0, 2147483647 + 1)


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
        return int(self).to_bytes(4, 'little')


class Packet(NamedTuple):
    """An RCON packet."""

    request_id: int
    type: Type
    payload: str

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = self.request_id.to_bytes(4, 'little', signed=True)
        payload += bytes(self.type)
        payload += self.payload.encode()
        payload += TAIL
        size = len(payload).to_bytes(4, 'little')
        return size + payload

    @classmethod
    def from_bytes(cls, bytes_: bytes):
        """Creates a packet from the respective bytes."""
        request_id = int.from_bytes(bytes_[:4], 'little', signed=True)
        type_ = int.from_bytes(bytes_[4:8], 'little')
        payload = bytes_[8:-2]
        tail = bytes_[-2:]

        if tail != TAIL:
            raise InvalidPacketStructure('Invalid tail.', tail)

        return cls(request_id, Type(type_), payload.decode())

    @classmethod
    def from_args(cls, *args: str):
        """Creates a command packet."""
        return cls(random_request_id(), Type.COMMAND, ' '.join(args))

    @classmethod
    def from_login(cls, passwd: str):
        """Creates a login packet."""
        return cls(random_request_id(), Type.LOGIN, passwd)


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
        except RequestIdMismatch:
            raise WrongPassword()

        return True

    def run(self, command: str, *arguments: str, raw: bool = False) -> str:
        """Runs a command."""
        packet = Packet.from_args(command, *arguments)
        response = self.communicate(packet)
        return response if raw else response.payload
