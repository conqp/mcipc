"""More complex data structures."""

from json import dumps, loads
from logging import getLogger
from typing import Callable, NamedTuple

from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


__all__ = ['Handshake']


LOGGER = getLogger(__file__)


class Handshake(NamedTuple):
    """Server-bound handshake packet."""

    protocol: VarInt
    address: str
    port: int
    next_state: State

    @classmethod
    def read(cls, readfunc: Callable):
        """Creates a handshake object from the respective bytes."""
        size = VarInt.read(readfunc)
        LOGGER.debug('Read size: %s', size)
        version = VarInt.read(readfunc)
        LOGGER.debug('Read version: %s', version)
        version_length = len(bytes(version))
        payload_size = size - version_length - 1    # Do not read next state.
        payload = readfunc(payload_size)
        LOGGER.debug('Read payload: %s', payload)
        address = payload[4:-2].decode()
        port = int.from_bytes(payload[-2:], 'little')
        next_state = State.read(readfunc)
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
    def read(cls, readfunc: Callable):
        """Creates the SLP response from the respective payload."""
        total_size = VarInt.read(readfunc)
        LOGGER.debug('Read total size: %s', total_size)
        packet_id = VarInt.read(readfunc)
        LOGGER.debug('Read packet ID: %s', packet_id)
        json_size = VarInt.read(readfunc)
        LOGGER.debug('Read JSON size: %s', json_size)
        json_bytes = readfunc(json_size)
        LOGGER.debug('Read JSON bytes: %s', json_bytes)
        string = json_bytes.decode('latin-1')
        json = loads(string)
        return cls(packet_id, json)
