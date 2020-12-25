"""Handshake protocol."""

from __future__ import annotations
from contextlib import suppress
from typing import IO, NamedTuple

from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import NULL
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import BigEndianSignedInt32
from mcipc.query.proto.common import Type


__all__ = ['Request', 'Response']


class Request(NamedTuple):
    """A client → server handshake request packet."""

    magic: bytes = MAGIC
    type: Type = Type.HANDSHAKE
    session_id: BigEndianSignedInt32 = BigEndianSignedInt32()

    def __bytes__(self):
        """Converts the packet to bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += bytes(self.session_id)
        return payload

    @classmethod
    def create(cls) -> Request:
        """Creates a handshake with a random session ID."""
        return cls(session_id=random_session_id())


class Response(NamedTuple):
    """A server → client handshake response packet."""

    type: bytes
    session_id: BigEndianSignedInt32
    challenge_token: BigEndianSignedInt32

    @classmethod
    def read(cls, file: IO) -> Response:
        """Reads the response from a file-like object."""
        type_ = Type.read(file)
        session_id = BigEndianSignedInt32.read(file)
        # For challenge token, see: https://wiki.vg/Query#Handshake
        bytes_ = b''

        while True:
            byte = file.read(1)

            if byte == NULL:
                with suppress(ValueError):
                    challenge_token = BigEndianSignedInt32(bytes_.decode())
                    break

            bytes_ += byte

        return cls(type_, session_id, challenge_token)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'type': self.type.value,
            'session_id': self.session_id,
            'challenge_token': self.challenge_token
        }
