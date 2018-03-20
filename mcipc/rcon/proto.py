"""Low-level protocol stuff."""

from collections import namedtuple
from enum import Enum
from itertools import chain
from logging import getLogger
from random import randint
from socket import socket
from struct import pack, unpack


__all__ = [
    'NotConnectedError',
    'RequestIdMismatchError',
    'PacketType',
    'Packet',
    'RawClient']


LOGGER = getLogger(__file__)
TAIL = b'\0\0'


class InvalidPacketStructureError(Exception):
    """Indicates an invalid packet structure."""
    
    pass


class NotConnectedError(Exception):
    """Indicates that the client is not connected."""

    pass


class RequestIdMismatchError(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent_request_id, received_request_id):
        """Sets the sent and received request IDs."""
        super().__init__(sent_request_id, received_request_id)
        self.sent_request_id = sent_request_id
        self.received_request_id = received_request_id


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
        payload += pack('<i', self.type)
        payload += self.payload.encode()
        payload += TAIL
        return pack('<i', len(payload)) + payload
    
    @classmethod
    def from_socket(cls, sock):
        """Reads a packet from the respective socket."""
        header = sock.recv(4)
        length = unpack('<i', header)
        body = sock.recv(length)
        request_id, type_ = unpack('<ii', body[:8])
        payload = body[8:-2]
        tail = body[-2:]
        
        if tail != TAIL:
            raise InvalidPacketStructureError('Invalid tail.', tail)
        
        return cls(request_id, type_, payload.decode())

    @classmethod
    def from_command(cls, command):
        """Creates a command packet."""
        return cls(_rand_int32(), PacketType.COMMAND.value, command)

    @classmethod
    def from_login(cls, passwd):
        """Creates a login packet."""
        return cls(_rand_int32(), PacketType.LOGIN.value, passwd)


class RawClient:
    """An RCON client."""

    def __init__(self, host, port):
        """Sets host an port."""
        self.host = host
        self.port = port
        self._socket = None

    def __enter__(self):
        """Sets up and conntects the socket."""
        if self._socket is None:
            sock = socket()
            self._socket = sock.__enter__()
            socket_ = self.socket
            LOGGER.debug('Connecting to socket %s.', socket_)
            self._socket.connect(socket_)

        return self

    def __exit__(self, *args):
        """Disconnects the socket."""
        if self._socket is not None:
            LOGGER.debug(
                'Disconnecting from socket %s.', self._socket.getsockname())
            result = self._socket.__exit__(*args)
            self._socket = None
            return result

        return None

    @property
    def socket(self):
        """Returns the respective socket."""
        return (self.host, self.port)

    def send(self, packet):
        """Sends an Packet."""
        if self._socket is None:
            raise NotConnectedError()

        bytes_ = bytes(packet)
        LOGGER.debug('Sent %i bytes.', len(bytes_))
        return self._socket.send(bytes_)

    def receive(self):
        """Receives a packet."""
        if self._socket is None:
            raise NotConnectedError()

        return Packet.from_socket(self._socket)

    def login(self, passwd):
        """Performs a login."""
        login_packet = Packet.from_login(passwd)
        self.send(login_packet)
        response = self.receive()

        if response.request_id == login_packet.request_id:
            return True

        raise RequestIdMismatchError(
            login_packet.request_id, response.request_id)

    def run(self, command, *arguments):
        """Runs a command."""
        command = ' '.join(chain((command,), arguments))
        command_packet = Packet.from_command(command)
        self.send(command_packet)
        response = self.receive()

        if response.request_id == command_packet.request_id:
            return response.payload

        raise RequestIdMismatchError(
            command_packet.request_id, response.request_id)
