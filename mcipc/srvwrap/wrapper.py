"""Actual server wrapper."""

from subprocess import PIPE, Popen

from mcipc.srvwrap.events import EventProcessor
from mcipc.srvwrap.ipc import IPCServer


__all__ = ['spawn']


def spawn(command, host, port, cwd=None):
    """Spawns a server wrapper."""

    server = Popen(command, cwd=cwd, stdin=PIPE, stdout=PIPE)

    with EventProcessor(server) as event_processor:
        with IPCServer(host, port, server, event_processor):
            return server.wait()
