"""Query client library."""

from socket import SOCK_DGRAM, socket

from mcipc.query.proto import BasicStatsMixin
from mcipc.query.proto import BasicStatsRequest
from mcipc.query.proto import FullStatsMixin
from mcipc.query.proto import FullStatsRequest
from mcipc.query.proto import HandshakeMixin
from mcipc.query.proto import HandshakeRequest
from mcipc.query.proto import Request


__all__ = ['Client']


class BaseClient:
    """A basic client, common to Query and RCON."""

    def __init__(self, host: str, port: int, *, timeout: float = None):
        """Sets host an port."""
        self._socket = socket(type=SOCK_DGRAM)
        self.host = host
        self.port = port
        self.timeout = timeout

    def __enter__(self):
        """Conntects the socket."""
        self._socket.__enter__()
        self._socket.settimeout(self.timeout)
        self._socket.connect((self.host, self.port))
        return self

    def __exit__(self, typ, value, traceback):
        """Delegates to the underlying socket's exit method."""
        return self._socket.__exit__(typ, value, traceback)


class Client(BaseClient, HandshakeMixin, BasicStatsMixin, FullStatsMixin):
    """A Query client."""

    def __init__(self, host: str, port: int, *, timeout: float = None):
        """Initializes the base client with the socket
        type SOCK_DGRAM and sets the challenge token.
        """
        super().__init__(host, port, timeout=timeout)
        self.challenge_token = None

    def __enter__(self):
        """Performs a handshake."""
        result = super().__enter__()

        if self.challenge_token is None:
            self.handshake()

        return result

    def _recv_handshake(self, buffer: int = 4096) -> bytes:
        """Receives a handshake response."""
        header = self._socket.recv(4)
        body = b''

        while True:
            body += self._socket.recv(buffer)

            if b'\x00' in body:
                return header + body

    def _recv_basic_stats(self, buffer: int = 4096) -> bytes:
        """Receives a basic stats response."""
        header = self._socket.recv(4)
        body = b''

        while True:
            body += self._socket.recv(buffer)

            if len(body.split(b'\0')) == 7:
                return header + body

    def _recv_full_stats(self, buffer: int = 4096) -> bytes:
        """Receives a full stats response."""
        result = b''

        while True:
            result += self._socket.recv(buffer)

            if result[-3:] == b'\x00\x00\x00':
                return result

    def communicate(self, request: Request, *, buffer: int = 4096) -> bytes:
        """Sends and receives bytes."""
        self._socket.send(bytes(request))

        if isinstance(request, HandshakeRequest):
            return self._recv_handshake(buffer=buffer)

        if isinstance(request, BasicStatsRequest):
            return self._recv_basic_stats(buffer=buffer)

        if isinstance(request, FullStatsRequest):
            return self._recv_full_stats(buffer=buffer)

        raise ValueError('Unknown request type:', request)
