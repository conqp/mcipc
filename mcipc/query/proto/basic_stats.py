"""Basic statistics protocol."""

from typing import NamedTuple

from mcipc.query.proto.common import MAGIC, random_session_id, Type


__all__ = ['Request', 'Response']


class Request(NamedTuple):
    """Basic statistics request packet."""

    magic: bytes
    type: Type
    session_id: int
    challenge_token: int

    def __bytes__(self):
        """Returns the packet as bytes."""
        raise NotImplementedError()

    @classmethod
    def create(cls, challenge_token, session_id=None):
        """Creates a new request with the specified challenge
        token and the specified or a random session ID.
        """
        if session_id is None:
            session_id = random_session_id()

        return cls(MAGIC, Type.STAT, session_id, challenge_token)


class Response(NamedTuple):
    """Basic statistics response packet."""
