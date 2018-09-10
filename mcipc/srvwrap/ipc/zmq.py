"""ZMQ extension for IPC server / client."""

from contextlib import suppress

from zmq import REP, REQ, RCVTIMEO, LINGER, Context     # pylint: disable=E0611
from zmq.error import ZMQError


__all__ = ['ZMQServer', 'ZMQClient']


class _ZMQ:
    """ZMQ client / server base class."""

    def __init__(self, mode, addr, port, proto='tcp'):
        """Initializes the ZMQ handler"""
        self.mode = mode
        self.addr = addr
        self.port = port
        self.proto = proto.lower()
        self._socket = None

    @property
    def url(self):
        """Returns the URL."""
        return '{}://{}:{}'.format(self.proto, self.addr, self.port)

    def _initsock(self):
        """Initializes the socket."""
        if self._socket is None:
            self._socket = Context().socket(self.mode)

    def receive(self):
        """Receives byte stream from the socket."""
        return self._socket.recv()

    def send(self, data, autoencode=True):
        """Sends a string to the socket."""
        if autoencode:
            try:
                data = data.encode()
            except AttributeError:
                with suppress(AttributeError):
                    data = data.__bytes__()

        return self._socket.send(data)


class ZMQServer(_ZMQ):
    """Class that listens on a socket."""

    def __init__(self, addr, port):
        """Create a new listener"""
        super().__init__(REP, addr, port)

    def __enter__(self):
        """Bind to the specified socket."""
        self.bind()
        return self

    def __exit__(self, *_):
        """Closes the socket."""
        self.close()

    def bind(self):
        """Binds the socket."""
        self._initsock()

        if self.port is None:
            self.port = self._socket.bind_to_random_port(self.url)
        else:
            self._socket.bind(self.url)

    def close(self):
        """Closes the socket."""
        with suppress(ZMQError):
            self._socket.close()


class ZMQClient(_ZMQ):
    """Class to connect to a server's socket."""

    def __init__(self, addr, port):
        """Initializes handler in client mode"""
        super().__init__(REQ, addr, port)

    def __enter__(self):
        """Connect to the specified socket."""
        self.connect()
        return self

    def __exit__(self, *_):
        """Disconnect from the socket."""
        self.disconnect()

    def connect(self):
        """Connects to the socket."""
        self._initsock()
        self._socket.connect(self.url)

    def disconnect(self):
        """Disconnects to the socket."""
        with suppress(ZMQError):
            self._socket.disconnect(self.url)

    def query(self, string, timeout=None, linger=None):
        """Queries a message and returns the result."""
        if timeout is not None:
            self._socket.setsockopt(RCVTIMEO, timeout)

        if linger is not None:
            self._socket.setsockopt(LINGER, linger)

        self.send(string)
        return self.receive()
