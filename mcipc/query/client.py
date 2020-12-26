"""Query client library."""

from socket import SOCK_DGRAM, socket
from typing import Union
from warnings import warn

from mcipc.query.proto import BasicStats
from mcipc.query.proto import BasicStatsRequest
from mcipc.query.proto import BigEndianSignedInt32
from mcipc.query.proto import FullStats
from mcipc.query.proto import FullStatsRequest
from mcipc.query.proto import HandshakeRequest
from mcipc.query.proto import Response


__all__ = ['Client']


WARN_TEMP = 'Client.{} is deprecated. Use Client.stats({}) instead.'


class Client:
    """A basic client, common to Query and RCON."""

    def __init__(self, host: str, port: int, *, timeout: float = None):
        """Sets host an port."""
        self._socket = socket(type=SOCK_DGRAM)
        self.host = host
        self.port = port
        self.timeout = timeout
        self.challenge_token = None

    def __enter__(self):
        """Conntects the socket."""
        self._socket.__enter__()
        self._socket.settimeout(self.timeout)
        self._socket.connect((self.host, self.port))

        if self.challenge_token is None:
            self.challenge_token = self.handshake()

        return self

    def __exit__(self, typ, value, traceback):
        """Delegates to the underlying socket's exit method."""
        return self._socket.__exit__(typ, value, traceback)

    @property
    def basic_stats(self) -> BasicStats:
        """Returns basic stats."""
        warn(WARN_TEMP.format('basic_stats', ''), FutureWarning, stacklevel=2)
        return self.stats()

    @property
    def full_stats(self) -> FullStats:
        """Returns full stats."""
        warn(WARN_TEMP.format('full_stats', 'full=True'), FutureWarning,
             stacklevel=2)
        return self.stats(full=True)

    def handshake(self) -> BigEndianSignedInt32:
        """Performs a handshake."""
        request = HandshakeRequest.create()

        with self._socket.makefile('wb') as file:
            file.write(bytes(request))

        with self._socket.makefile('rb') as file:
            response = Response.read(file)

        return response.challenge_token

    def stats(self, full: bool = False) -> Union[BasicStats, FullStats]:
        """Returns basic or full stats."""
        if full:
            request = FullStatsRequest.create(self.challenge_token)
        else:
            request = BasicStatsRequest.create(self.challenge_token)

        with self._socket.makefile('wb') as file:
            file.write(bytes(request))

        with self._socket.makefile('rb') as file:
            if full:
                return FullStats.read(file)

            return BasicStats.read(file)
