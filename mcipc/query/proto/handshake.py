"""Handshake protocol."""

from __future__ import annotations
from typing import NamedTuple

from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import Type

from mcipc.common import BigEndianSignedInt32


__all__ = ['Request', 'Response', 'HandshakeMixin']


class Request(NamedTuple):
    """A client → server handshake request packet."""

    magic: bytes
    type: Type
    session_id: BigEndianSignedInt32

    def __bytes__(self):
        """Converts the packet to bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += bytes(self.session_id)
        return payload

    @classmethod
    def create(cls) -> Request:
        """Returns a handshake request packet with a random session ID."""
        return cls(MAGIC, Type.HANDSHAKE, random_session_id())


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
        request = Request.create()
        bytes_ = self.communicate(bytes(request))
        response = Response.from_bytes(bytes_)

        if set_challenge_token:
            self.challenge_token = response.challenge_token

        return response
