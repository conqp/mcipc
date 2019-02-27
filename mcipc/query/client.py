"""Query client library."""

from socket import SOCK_DGRAM

from mcipc.common import BaseClient
from mcipc.query.proto import basic_stats, full_stats, handshake


__all__ = ['Client']


class Client(BaseClient):
    """A Query client."""

    def __init__(self, host: str, port: int):
        """Sets the challenge token."""
        super().__init__(host, port, typ=SOCK_DGRAM)
        self._challenge_token = None

    def __enter__(self):
        """Performs a handshake."""
        super().__enter__()

        if self._challenge_token is None:
            self._challenge_token = self.handshake().challenge_token

        return self

    def _recv_all(self, buffer: int = 4096):
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

        if response_type is not None:
            return response_type.from_bytes(response)

        return response

    def handshake(self):
        """Performs a handshake."""
        request = handshake.Request.create()
        return self.communicate(request, handshake.Response)

    @property
    def basic_stats(self):
        """Returns basic stats"""
        request = basic_stats.Request.create(self._challenge_token)
        return self.communicate(request, basic_stats.BasicStats)

    @property
    def full_stats(self):
        """Returns full stats"""
        request = full_stats.Request.create(self._challenge_token)
        return self.communicate(request, full_stats.FullStats)
