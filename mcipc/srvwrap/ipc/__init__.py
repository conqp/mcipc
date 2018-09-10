"""IPC server and client."""

from os import linesep
from queue import Empty, Queue
from re import compile  # pylint: disable=W0622

from mcipc.srvwrap.common import Daemon
from mcipc.srvwrap.events import MsgCancel
from mcipc.srvwrap.ipc.errors import IPCError
from mcipc.srvwrap.ipc.messages import IPCCommand, IPCResponse
from mcipc.srvwrap.zmq import ZMQServer


__all__ = ['IPCServer']


QUEUE = Queue()


def get_data(regex):
    """Retrieves data into the queue."""

    regex = compile(regex) if regex else None

    def match_event(event):
        """Reads the respective events and matches
        it against the regular expression.
        """

        text = event.decode().rstrip(linesep)

        if regex is None or regex.fullmatch(text):
            QUEUE.put(event)
            raise MsgCancel()

    return match_event


class IPCServer(Daemon):
    """An IPC server."""

    def __init__(self, host, port, process, event_processor):
        """Sets host and port."""
        super().__init__()
        self.host = host
        self.port = port
        self.process = process
        self.event_processor = event_processor

    def _run(self):
        """Runs the ZMQ server."""
        with ZMQServer(self.host, self.port) as server:
            while not self._terminate:
                try:
                    data = server.receive()
                except KeyboardInterrupt:
                    break

                response = self._process(data)
                server.send(bytes(response))

        self._thread = None

    def _process(self, data):
        """Processes the respective data."""
        try:
            command = IPCCommand.from_bytes(data)
        except IPCError as error:
            return error

        callback = get_data(command.regex)

        with self.event_processor.register(callback):
            self.process.stdin.write(bytes(command))
            self.process.stdin.flush()

            try:
                response = QUEUE.get(timeout=command.timeout)
            except Empty:
                return IPCError.NO_RESPONSE

            return IPCResponse(response)
