"""Server launcher."""

from json import dumps
from logging import getLogger
from socket import socket
from subprocess import CalledProcessError, check_call

from mcipc.server.datatypes import VarInt
from mcipc.server.server import StubServer


__all__ = ['ServerLauncher']


LOGGER = getLogger(__file__)


def get_response(text: str) -> bytes:
    """Returns the response text message."""

    json = {'text': text}
    string = dumps(json)
    payload = string.encode('latin-1')
    payload_length = len(payload)
    payload_length = VarInt(payload_length)
    payload_length = bytes(payload_length)
    payload = payload_length + payload
    payload = bytes(VarInt(0)) + payload
    payload_length = len(payload)
    payload_length = VarInt(payload_length)
    payload_length = bytes(payload_length)
    return payload_length + payload


class ServerLauncher(StubServer):
    """Server that launches the actual server."""

    def __init__(self, name: str, description: str,     # pylint: disable=R0913
                 max_players: int = 20, protocol: int = 485,
                 template: str = 'minecraft@{}.server'):
        """Sets server meta data."""
        super().__init__(
            description, max_players=max_players, protocol=protocol)
        self.name = name
        self.template = template

    @property
    def unit(self) -> str:
        """Returns the system unit to start."""
        return self.template.format(self.name)

    def _start_server(self) -> bool:
        """Starts the server."""
        command = ('/usr/bin/systemctl', 'start', self.unit)

        try:
            check_call(command)
        except CalledProcessError as cpe:
            LOGGER.debug(cpe)
            return False

        return True

    def _perform_login(self, connection: socket):
        """Performs a login."""
        if self._start_server():
            response = get_response('Server has been started.')
        else:
            response = get_response('Server could not be started.')

        connection.send(response)
