"""Stub server launcher."""

from argparse import ArgumentParser, Namespace
from logging import getLogger
from socket import socket
from subprocess import CalledProcessError, check_call
from sys import exit    # pylint: disable=W0622

from mcipc.server import get_response, StubServer


__all__ = ['main']


DESCRIPTION = 'Starts a stub server'
LOGGER = getLogger(__file__)
DEFAULT_PLAYERS = 20
DEFAULT_PROTO = 485
DEFAULT_UNIT_TEMPLATE = 'minecraft@{}.server'


def get_args() -> Namespace:
    """Parses the command line arguments."""

    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument('socket', help='the socket to listen on')
    parser.add_argument('name', help='the server name')
    parser.add_argument('description', help='server description')
    parser.add_argument('-p', '--players', type=int, default=DEFAULT_PLAYERS,
                        help='amount of player slots')
    parser.add_argument('-P', '--protocol', type=int, default=DEFAULT_PROTO,
                        help='protocol version')
    parser.add_argument('-t', '--template', default=DEFAULT_UNIT_TEMPLATE,
                        help='systemd unit template')
    return parser.parse_args()


class ServerLauncher(StubServer):
    """Server that launches the actual server."""

    def __init__(self, name: str, description: str,     # pylint: disable=R0913
                 max_players: int = DEFAULT_PLAYERS,
                 protocol: int = DEFAULT_PROTO,
                 template: str = DEFAULT_UNIT_TEMPLATE):
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
        command = ('/bin/systemctl', 'start', self.unit)

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


def main():
    """Main program."""

    args = get_args()

    try:
        host, port = args.socket.split(':')
    except ValueError:
        LOGGER.error('Invalid socket: %s', args.socket)
        exit(1)

    try:
        port = int(port)
    except ValueError:
        LOGGER.error('Invalid port: %s', port)
        exit(2)

    server = ServerLauncher(
        args.name, args.description, max_players=args.players,
        protocol=args.protocol, template=args.template)

    try:
        server.spawn(host, port)
    except OSError as error:
        LOGGER.error(str(error))
        exit(3)
    except KeyboardInterrupt:
        LOGGER.info('Shutting down...')
