"""More complex data structures."""

from __future__ import annotations
from json import dumps, loads
from logging import getLogger
from typing import IO, NamedTuple

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
    def read(cls, file: IO) -> Handshake:
        """Reads a handshake object from a file-like object."""
        size = VarInt.read(file)
        LOGGER.debug('Read size: %s', size)
        version = VarInt.read(file)
        LOGGER.debug('Read version: %s', version)
        version_length = len(bytes(version))
        payload_size = size - version_length - 1    # Do not read next state.
        payload = file.read(payload_size)
        LOGGER.debug('Read payload: %s', payload)
        address = payload[4:-2].decode()
        port = int.from_bytes(payload[-2:], 'little')
        next_state = State.read(file)
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
    def read(cls, file: IO) -> SLPResponse:
        """Read an SLP response from a file-like object."""
        total_size = VarInt.read(file)
        LOGGER.debug('Read total size: %s', total_size)
        packet_id = VarInt.read(file)
        LOGGER.debug('Read packet ID: %s', packet_id)
        json_size = VarInt.read(file)
        LOGGER.debug('Read JSON size: %s', json_size)
        json_bytes = file.read(json_size)
        LOGGER.debug('Read JSON bytes: %s', json_bytes)
        string = json_bytes.decode('latin-1')
        json = loads(string)
        return cls(packet_id, json)
