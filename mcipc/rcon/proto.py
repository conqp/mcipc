"""Low-level protocol stuff."""

from enum import Enum
from logging import getLogger
from random import randint
from socket import socket
from struct import pack, unpack
from typing import NamedTuple


__all__ = [
    'RequestIdMismatch',
    'PacketType',
    'Packet',
    'Client']


LOGGER = getLogger(__file__)
TAIL = b'\0\0'


class InvalidPacketStructureError(Exception):
    """Indicates an invalid packet structure."""

    pass


class RequestIdMismatch(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent, received):
        """Sets the sent and received request IDs."""
        super().__init__(sent, received)
        self.sent = sent
        self.received = received


def _rand_int32() -> int:
    """Returns a random unsigned int32."""

    return randint(0, 2_147_483_647 + 1)


class PacketType(Enum):
    """Available packet types."""

    LOGIN = 3
    COMMAND = 2
    COMMAND_RESPONSE = 0


class Packet(NamedTuple):
    """An RCON packet."""

    request_id: int
    type: PacketType
    payload: bytes

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = pack('<i', self.request_id)
        payload += pack('<i', self.type.value)
        payload += self.payload
        payload += TAIL
        return pack('<i', len(payload)) + payload

    @classmethod
    def from_bytes(cls, bytes_: bytes):
        """Creates a packet from the respective bytes."""
        request_id, type_ = unpack('<ii', bytes_[:8])
        payload = bytes_[8:-2]
        tail = bytes_[-2:]

        if tail != TAIL:
            raise InvalidPacketStructureError('Invalid tail.', tail)

        return cls(request_id, PacketType(type_), payload)

    @classmethod
    def from_command(cls, command: str):
        """Creates a command packet."""
        return cls(_rand_int32(), PacketType.COMMAND, command.encode())

    @classmethod
    def from_login(cls, passwd: str):
        """Creates a login packet."""
        return cls(_rand_int32(), PacketType.LOGIN, passwd.encode())

    @property
    def text(self) -> str:
        """Returns the payload as text."""
        return self.payload.decode()


class Client:
    """An RCON client."""

    def __init__(self, host: str, port: int):
        """Sets host an port."""
        self._socket = socket()
        self.host = host
        self.port = port

    def __enter__(self):
        """Conntects the socket."""
        self._socket.__enter__()
        self._socket.connect(self.socket)
        return self

    def __exit__(self, typ, value, traceback):
        """Delegates to the underlying socket's exit method."""
        self.close()
        return self._socket.__exit__(typ, value, traceback)

    @property
    def socket(self) -> tuple:
        """Returns a tuple of host and port."""
        return (self.host, self.port)

    def connect(self):
        """Conntects to the RCON server."""
        return self._socket.connect(self.socket)

    def close(self):
        """Disconnects from the RCON server."""
        return self._socket.close()

    def send(self, packet: Packet):
        """Sends an Packet."""
        return self._socket.send(bytes(packet))

    def recv(self) -> Packet:
        """Receives a packet."""
        length, = unpack('<i', self._socket.recv(4))
        payload = self._socket.recv(length)
        return Packet.from_bytes(payload)

    def login(self, passwd: str) -> bool:
        """Performs a login."""
        packet = Packet.from_login(passwd)
        self.send(packet)
        response = self.recv()

        if response.request_id == packet.request_id:
            return True

        raise RequestIdMismatch(packet.request_id, response.request_id)

    def run(self, command: str, *arguments: str) -> str:
        """Runs a command."""
        command = ' '.join((command,) + arguments)
        packet = Packet.from_command(command)
        self.send(packet)
        response = self.recv()

        if response.request_id == packet.request_id:
            return response.text

        raise RequestIdMismatch(packet.request_id, response.request_id)
