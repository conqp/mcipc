"""Query client library."""

from socket import SOCK_DGRAM, socket
from typing import IO

from mcipc.query.proto import BasicStatsMixin
from mcipc.query.proto import BasicStatsRequest
from mcipc.query.proto import FullStatsMixin
from mcipc.query.proto import FullStatsRequest
from mcipc.query.proto import HandshakeMixin
from mcipc.query.proto import HandshakeRequest
from mcipc.query.proto import Request


__all__ = ['Client']


def read_handshake(file: IO) -> bytes:
    """Reads a handshake response."""

    header = file.read(4)
    body = b''

    while True:
        body += file.read(1)

        if b'\x00' in body:
            return header + body


def read_basic_stats(file: IO) -> bytes:
    """Reads a basic stats response."""

    header = file.read(4)
    body = b''

    while True:
        body += file.read(1)

        if len(body.split(b'\0')) == 7:
            return header + body


def read_full_stats(file: IO) -> bytes:
    """Read a full stats response."""

    result = b''

    while True:
        result += file.read(1)

        if result[-3:] == b'\x00\x00\x00':
            return result


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

    def communicate(self, request: Request, *, buffer: int = 4096) -> bytes:
        """Sends and receives bytes."""
        with self._socket.makefile('wb', buffering=buffer) as file:
            file.write(bytes(request))

        with self._socket.makefile('rb', buffering=buffer) as file:
            if isinstance(request, HandshakeRequest):
                return read_handshake(file)

            if isinstance(request, BasicStatsRequest):
                return read_basic_stats(file)

            if isinstance(request, FullStatsRequest):
                return read_full_stats(file)

        raise ValueError('Unknown request type:', request)
