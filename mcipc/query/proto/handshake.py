"""Handshake protocol."""

from __future__ import annotations
from typing import NamedTuple

from mcipc.common import BigEndianSignedInt32
from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import Type


__all__ = ['Request', 'Response', 'HandshakeMixin']


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


class Response(NamedTuple):
    """A server → client handshake response packet."""

    type: bytes
    session_id: BigEndianSignedInt32
    challenge_token: BigEndianSignedInt32

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> Response:
        """Creates the packet from bytes."""
        type_ = Type.from_bytes(bytes_[0:1])
        session_id = BigEndianSignedInt32.from_bytes(bytes_[1:5])
        # For challenge token, see: https://wiki.vg/Query#Handshake
        challenge_token = BigEndianSignedInt32(bytes_[5:-1].decode())
        return cls(type_, session_id, challenge_token)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'type': self.type.value,
            'session_id': self.session_id,
            'challenge_token': self.challenge_token
        }


class HandshakeMixin:   # pylint: disable=R0903
    """Query client mixin for performing handshakes."""

    def handshake(self, *, set_challenge_token: bool = True) -> Response:
        """Performs a handshake."""
        request = Request(session_id=random_session_id())
        bytes_ = self.communicate(bytes(request))
        response = Response.from_bytes(bytes_)

        if set_challenge_token:
            self.challenge_token = response.challenge_token

        return response
