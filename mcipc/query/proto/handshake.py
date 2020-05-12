"""Handshake protocol."""

from typing import NamedTuple

from mcipc.query.proto.common import MAGIC, random_session_id, Type


__all__ = ['Request', 'Response', 'HandshakeMixin']


class Request(NamedTuple):
    """A client → server handshake request packet."""

    magic: bytes
    type: Type
    session_id: int

    def __bytes__(self):
        """Converts the packet to bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += self.session_id.to_bytes(4, 'big', signed=True)
        return payload

    @classmethod
    def create(cls, session_id=None):
        """Returns a handshake request packet with a random session ID."""
        if session_id is None:
            session_id = random_session_id()

        return cls(MAGIC, Type.HANDSHAKE, session_id)


class Response(NamedTuple):
    """A server → client handshake response packet."""

    type: bytes
    session_id: int
    challenge_token: int

    @classmethod
    def from_bytes(cls, bytes_):
        """Creates the packet from bytes."""
        type_ = Type.from_bytes(bytes_[0:1])
        session_id = int.from_bytes(bytes_[1:5], 'big', signed=True)
        challenge_token = bytes_[5:-1].decode()
        return cls(type_, session_id, int(challenge_token))

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'type': self.type.value,
            'session_id': self.session_id,
            'challenge_token': self.challenge_token
        }


class HandshakeMixin:   # pylint: disable=R0903
    """Query client mixin for performing handshakes."""

    def handshake(self) -> Response:
        """Performs a handshake."""
        request = Request.create()
        return self.communicate(request, Response)
