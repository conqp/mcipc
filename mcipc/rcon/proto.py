"""Low-level protocol stuff.

See <http://wiki.vg/RCON> for details.
"""
from collections import namedtuple
from enum import Enum
from itertools import chain
from random import randint
from socket import socket
from struct import pack, unpack_from


__all__ = ['NotConnectedError', 'PacketType', 'Packet', 'RawClient']


class NotConnectedError(Exception):
    """Indicates that the client is not connected."""

    pass


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
        payload += self.payload.encode('ascii')
        payload += b'\0\0'
        return pack('<i', len(payload)) + payload

    @classmethod
    def from_command(cls, command):
        """Creates a command packet."""
        return cls(_rand_int32(), PacketType.COMMAND.value, command)

    @classmethod
    def from_response(cls, bytes_):
        """Creates a login packet."""
        request_id, type_ = unpack_from('<ii', bytes_, offset=4)
        playload = bytes_[12:-2]
        return cls(request_id, type_, playload.decode('ascii'))

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
            self._socket.connect(self.socket)

        return self

    def __exit__(self, *args):
        """Disconnects the socket."""
        if self._socket is not None:
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

        return self._socket.send(bytes(packet))

    def receive(self, bufsize=4096):
        """Receives a packet."""
        if self._socket is None:
            raise NotConnectedError()

        bytes_ = self._socket.recv(bufsize)
        return Packet.from_response(bytes_)

    def login(self, passwd):
        """Performs a login."""
        login_packet = Packet.from_login(passwd)
        self.send(login_packet)
        response = self.receive()
        return response.request_id == login_packet.request_id

    def run(self, command, *arguments):
        """Performs a login."""
        command = ' '.join(chain((command,), arguments))
        self.send(Packet.from_command(command))
        response = self.receive()
        return response.payload
