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
    def from_bytes(cls, bytes_):
        """Creates a handshake object from the respective bytes."""
        version = VarInt.from_bytes(bytes_[1:4])
        address = bytes_[4:-3].decode()
        port = int.from_bytes(bytes_[-3:-1], 'little')
        next_state = VarInt.from_bytes(bytes_[-1:])
        return cls(version, address, port, State(next_state))



class SLPResponse(dict):
    """A server list ping response."""

    def __bytes__(self):
        """Returns the respective bytes."""
        string = dumps(self)
        payload = string.encode('latin-1')
        payload_size = len(payload)
        payload_size = VarInt(payload_size)
        payload_size = bytes(payload_size)
        payload = payload_size + payload
        payload = b'\x00' + payload     # Add packet ID.
        payload_size = len(payload)
        payload_size = VarInt(payload_size)
        payload_size = bytes(payload_size)
        return payload_size + payload

    @classmethod
    def from_bytes(cls, payload):
        """Creates the SLP response from the respective payload."""
        json_bytes = payload[5:]    # Skip total size, packet ID and JSON size.
        string = json_bytes.decode('latin-1')
        return cls(loads(string))
