"""Actual server wrapper."""

from subprocess import PIPE, Popen

from mcipc.srvwrap.event_processor import EventProcessor
from mcipc.srvwrap.ipc import IPCServer


__all__ = ['spawn']


def spawn(command, host, port, cwd=None):
    """Spawns a server wrapper."""

    server = Popen(command, cwd=cwd, stdin=PIPE, stdout=PIPE)
    event_processor = EventProcessor(server)
    event_processor.start()
    ipc_server = IPCServer(host, port, server, event_processor)
    ipc_server.start()
    result = server.wait()
    ipc_server.stop()
    event_processor.stop()
    return result
