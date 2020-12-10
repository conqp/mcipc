"""An interactive RCON shell."""

from argparse import ArgumentParser, Namespace
from logging import INFO, basicConfig, getLogger
from socket import timeout
from sys import exit    # pylint: disable=W0622

from mcipc.cli.errors import CONNECTION_REFUSED
from mcipc.cli.errors import CONNECTION_TIMEOUT
from mcipc.cli.rconclt import get_credentials
from mcipc.config import LOG_FORMAT
from mcipc.rcon.console import PS1, rconcmd


__all__ = ['get_args', 'main']


LOGGER = getLogger('rconshell')


def get_args() -> Namespace:
    """Parses and returns the CLI arguments."""

    parser = ArgumentParser(description='An interactive RCON shell.')
    parser.add_argument('server', nargs='?', help='the server to connect to')
    parser.add_argument('-p', '--prompt', default=PS1, metavar='PS1',
                        help='the shell prompt')
    return parser.parse_args()


def main():
    """Runs the RCON shell."""

    args = get_args()
    basicConfig(level=INFO, format=LOG_FORMAT)

    if server := args.server:
        host, port, passwd = get_credentials(server)
    else:
        host = port = passwd = None

    try:
        exit_code = rconcmd(host, port, passwd, args.prompt)
    except ConnectionRefusedError:
        LOGGER.error('Connection refused.')
        exit(CONNECTION_REFUSED)
    except timeout:
        LOGGER.error('Connection timeout.')
        exit(CONNECTION_TIMEOUT)

    exit(exit_code)
