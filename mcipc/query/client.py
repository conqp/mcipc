"""Query client library."""

from socket import SOCK_DGRAM
from typing import Generator

from mcipc.common import BaseClient
from mcipc.query.proto.basic_stats import BasicStatsMixin
from mcipc.query.proto.full_stats import FullStatsMixin
from mcipc.query.proto.handshake import HandshakeMixin


__all__ = ['Client']


class Client(BaseClient, HandshakeMixin, BasicStatsMixin, FullStatsMixin):
    """A Query client."""

    def __init__(self, host: str, port: int, timeout: float = None):
        """Initializes the base client with the socket
        type SOCK_DGRAM and sets the challenge token.
        """
        super().__init__(SOCK_DGRAM, host, port, timeout=timeout)
        self._challenge_token = None

    def __enter__(self):
        """Performs a handshake."""
        super().__enter__()

        if self._challenge_token is None:
            self._challenge_token = self.handshake().challenge_token

        return self

    def _recv_chunks(self, buffer: int = 4096) -> Generator[bytes, None, None]:
        """Yields chunks of bytes from the socket."""
        while chunk := self._socket.recv(buffer):
            yield chunk

            if len(chunk) < buffer:
                return

    def _recv_all(self, buffer: int = 4096) -> bytes:
        """Receives all bytes from the socket."""
        return b''.join(self._recv_chunks(buffer=buffer))

    def communicate(self, packet, response_type=None, *, buffer: int = 4096):
        """Sends and receives a packet."""
        self._socket.send(bytes(packet))
        response = self._recv_all(buffer=buffer)

        if response_type is None:
            return response

        return response_type.from_bytes(response)
