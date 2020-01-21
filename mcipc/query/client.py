"""Query client library."""

from socket import SOCK_DGRAM

from mcipc.common import BaseClient
from mcipc.query.proto import handshake
from mcipc.query.proto.basic_stats import BasicStats, Request as BasicRequest
from mcipc.query.proto.full_stats import FullStats, Request as FullRequest


__all__ = ['Client']


class Client(BaseClient):
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

    def _recv_all(self, buffer: int = 4096) -> bytes:
        """Recevies all bytes."""
        bytes_ = b''

        while True:
            chunk = self._socket.recv(buffer)
            bytes_ += chunk

            if len(chunk) < buffer:
                break

        return bytes_

    def communicate(self, packet, response_type=None, *, buffer: int = 4096):
        """Sends and receives a packet."""
        self._socket.send(bytes(packet))
        response = self._recv_all(buffer=buffer)

        if response_type is None:
            return response

        return response_type.from_bytes(response)

    def handshake(self):
        """Performs a handshake."""
        request = handshake.Request.create()
        return self.communicate(request, handshake.Response)

    @property
    def basic_stats(self) -> BasicStats:
        """Returns basic stats"""
        request = BasicRequest.create(self._challenge_token)
        return self.communicate(request, BasicStats)

    @property
    def full_stats(self) -> FullStats:
        """Returns full stats"""
        request = FullRequest.create(self._challenge_token)
        return self.communicate(request, FullStats)
