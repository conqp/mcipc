"""More complex data structures."""

from json import dumps, loads
from typing import NamedTuple

from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


__all__ = ['Handshake']


class Handshake(NamedTuple):
    """Server-bound handshake packet."""

    protocol: VarInt
    address: str
    port: int
    next_state: State

    @classmethod
    def from_connection(cls, connection, size):
        """Creates a handshake object from the respective bytes."""
        version = VarInt.from_connection(connection)
        version_length = len(bytes(version))
        payload = connection.recv(size - version_length)
        address = payload[4:-3].decode()
        port = int.from_bytes(payload[-3:-1], 'little')
        next_state = int.from_bytes(payload[-1:], 'little')
        return cls(version, address, port, State(next_state))



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
    def from_connection(cls, connection):
        """Creates the SLP response from the respective payload."""
        _ = VarInt.from_connection(connection)  # Discard total size.
        packet_id = VarInt.from_connection(connection)
        json_size = VarInt.from_connection(connection)
        json_bytes = connection.recv(json_size)
        string = json_bytes.decode('latin-1')
        json = loads(string)
        return cls(packet_id, json)
