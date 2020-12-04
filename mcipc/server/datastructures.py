"""More complex data structures."""

from __future__ import annotations
from json import dumps, loads
from logging import getLogger
from socket import socket
from typing import NamedTuple

from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


__all__ = ['Handshake', 'SLPResponse']


LOGGER = getLogger(__file__)


class Handshake(NamedTuple):
    """Server-bound handshake packet."""

    protocol: VarInt
    address: str
    port: int
    next_state: State

    @classmethod
    def from_socket(cls, sock: socket) -> Handshake:
        """Creates a handshake object from the respective bytes."""
        size = VarInt.from_socket(sock)
        LOGGER.debug('Read size: %s', size)
        version = VarInt.from_socket(sock)
        LOGGER.debug('Read version: %s', version)
        version_length = len(bytes(version))
        payload_size = size - version_length - 1    # Do not read next state.
        payload = sock.recv(payload_size)
        LOGGER.debug('Read payload: %s', payload)
        address = payload[4:-2].decode()
        port = int.from_bytes(payload[-2:], 'little')
        next_state = State.from_socket(sock)
        return cls(version, address, port, next_state)


class SLPResponse(NamedTuple):
    """A server list ping response."""

    packet_id: VarInt
    json: dict

    def __bytes__(self):
        """Returns the respective bytes."""
        json = dumps(self).encode('latin-1')
        json_size = len(json)
        json_size = VarInt(json_size)
        json_size = bytes(json_size)
        payload = json_size + json
        payload = bytes(self.packet_id) + payload
        payload_size = len(payload)
        payload_size = VarInt(payload_size)
        payload_size = bytes(payload_size)
        return payload_size + payload

    @classmethod
    def from_socket(cls, sock: socket) -> SLPResponse:
        """Creates the SLP response from the respective payload."""
        total_size = VarInt.from_socket(sock)
        LOGGER.debug('Read total size: %s', total_size)
        packet_id = VarInt.from_socket(sock)
        LOGGER.debug('Read packet ID: %s', packet_id)
        json_size = VarInt.from_socket(sock)
        LOGGER.debug('Read JSON size: %s', json_size)
        json_bytes = sock.recv(json_size)
        LOGGER.debug('Read JSON bytes: %s', json_bytes)
        string = json_bytes.decode('latin-1')
        json = loads(string)
        return cls(packet_id, json)
