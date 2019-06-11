"""An interactive RCON shell."""

from argparse import ArgumentParser
from logging import INFO, basicConfig, getLogger
from sys import exit    # pylint: disable=W0622

from mcipc.config import LOG_FORMAT
from mcipc.rcon.config import CONFIG
from mcipc.rcon.console import PS1, rconcmd


__all__ = ['get_args', 'main']


LOGGER = getLogger('rconshell')


def get_args():
    """Parses and returns the CLI arguments."""

    parser = ArgumentParser(description='An interactive RCON shell.')
    parser.add_argument('server', nargs='?', help="the server's name")
    parser.add_argument('-H', '--host', help="the server's host name")
    parser.add_argument('-p', '--port', type=int, help="the server's port")
    parser.add_argument('-P', '--prompt', default=PS1, help='the shell prompt')
    return parser.parse_args()


def main():
    """Runs the RCON shell."""

    args = get_args()
    basicConfig(level=INFO, format=LOG_FORMAT)
    server = args.server

    if server:
        try:
            host, port, passwd = CONFIG.servers[server]
        except KeyError:
            LOGGER.error('No such server: %s.', server)
            exit(4)
    else:
        host = port = passwd = None

    host = args.host or host
    port = args.port or port
    prompt = args.prompt
    exit_code = rconcmd(host, port, passwd, prompt)
    exit(exit_code)
