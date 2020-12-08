"""Query client library."""

from socket import SOCK_DGRAM
from typing import Generator

from mcipc.common import BaseClient
from mcipc.query.proto import BasicStatsMixin
from mcipc.query.proto import FullStatsMixin
from mcipc.query.proto import HandshakeMixin


__all__ = ['Client']


class Client(BaseClient, HandshakeMixin, BasicStatsMixin, FullStatsMixin):
    """A Query client."""

    def __init__(self, host: str, port: int, *, timeout: float = None):
        """Initializes the base client with the socket
        type SOCK_DGRAM and sets the challenge token.
        """
        super().__init__(SOCK_DGRAM, host, port, timeout=timeout)
        self.challenge_token = None

    def __enter__(self):
        """Performs a handshake."""
        result = super().__enter__()

        if self.challenge_token is None:
            self.handshake()

        return result

    def _recv_chunks(self, buffer: int = 4096) -> Generator[bytes, None, None]:
        """Yields chunks of bytes from the socket."""
        while chunk := self._socket.recv(buffer):
            yield chunk

            if len(chunk) < buffer:
                return

    def _recv_all(self, buffer: int = 4096) -> bytes:
        """Receives all bytes from the socket."""
        return b''.join(self._recv_chunks(buffer=buffer))

    def communicate(self, request: bytes, *, buffer: int = 4096) -> bytes:
        """Sends and receives bytes."""
        self._socket.send(request)
        return self._recv_all(buffer=buffer)
