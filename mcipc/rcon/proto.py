"""Low-level protocol stuff."""

from collections import namedtuple
from enum import Enum
from itertools import chain
from logging import getLogger
from random import randint
from socket import socket
from struct import pack, unpack


__all__ = [
    'RequestIdMismatch',
    'PacketType',
    'Packet',
    'RawClient']


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


def _rand_int32():
    """Returns a random int32."""

    return randint(0, 2_147_483_647 + 1)


class PacketType(Enum):
    """Available packet types."""

    LOGIN = 3
    COMMAND = 2
    COMMAND_RESPONSE = 0


class Packet(namedtuple('Packet', ('request_id', 'type', 'payload'))):
    """An RCON packet."""

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = pack('<i', self.request_id)
        payload += pack('<i', self.type.value)
        payload += self.payload
        payload += TAIL
        return pack('<i', len(payload)) + payload

    @classmethod
    def from_bytes(cls, bytes_):
        """Creates a packet from the respective bytes."""
        request_id, type_ = unpack('<ii', bytes_[:8])
        payload = bytes_[8:-2]
        tail = bytes_[-2:]

        if tail != TAIL:
            raise InvalidPacketStructureError('Invalid tail.', tail)

        return cls(request_id, PacketType(type_), payload)

    @classmethod
    def from_command(cls, command):
        """Creates a command packet."""
        return cls(_rand_int32(), PacketType.COMMAND, command.encode())

    @classmethod
    def from_login(cls, passwd):
        """Creates a login packet."""
        return cls(_rand_int32(), PacketType.LOGIN, passwd.encode())

    @property
    def text(self):
        """Returns the payload as text."""
        return self.payload.decode()


class RawClient(socket):
    """An RCON client."""

    def __init__(self, host, port):
        """Sets host an port."""
        super().__init__()
        self.host = host
        self.port = port

    def __enter__(self):
        """Sets up and conntects the socket."""
        super().__enter__()
        sock = self.socket
        LOGGER.debug('Connecting to socket %s.', sock)
        self.connect(sock)
        return self

    def __exit__(self, *args):
        """Disconnects the socket."""
        LOGGER.debug('Disconnecting from socket %s.', self.getsockname())
        return super().__exit__(*args)

    @property
    def socket(self):
        """Returns the respective socket."""
        return (self.host, self.port)

    def sendpacket(self, packet):
        """Sends an Packet."""
        bytes_ = bytes(packet)
        LOGGER.debug('Sending %i bytes.', len(bytes_))
        return self.send(bytes_)

    def recvpacket(self):
        """Receives a packet."""
        length, = unpack('<i', self.recv(4))
        payload = self.recv(length)
        return Packet.from_bytes(payload)

    def login(self, passwd):
        """Performs a login."""
        packet = Packet.from_login(passwd)
        self.sendpacket(packet)
        response = self.recvpacket()

        if response.request_id == packet.request_id:
            return True

        raise RequestIdMismatch(packet.request_id, response.request_id)

    def run(self, command, *arguments):
        """Runs a command."""
        command = ' '.join(chain((command,), arguments))
        packet = Packet.from_command(command)
        self.sendpacket(packet)
        response = self.recvpacket()

        if response.request_id == packet.request_id:
            return response.text

        raise RequestIdMismatch(packet.request_id, response.request_id)
