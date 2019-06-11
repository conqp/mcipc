"""Common functions for multiple CLI programs."""

from getpass import getpass
from logging import getLogger
from sys import exit    # pylint: disable=W0622

from mcipc.config import InvalidCredentialsError, Credentials
from mcipc.rcon.config import CONFIG


__all__ = ['get_creadentials']


LOGGER = getLogger(__file__)


def get_creadentials(server, logger=LOGGER):
    """Get the credentials for a server from the respective server name."""

    try:
        host, port, passwd = Credentials.from_string(server)
    except InvalidCredentialsError:
        try:
            host, port, passwd = CONFIG.servers[server]
        except KeyError:
            logger.error('No such server: %s.', server)
            exit(2)

    if passwd is None:
        try:
            passwd = getpass('Password: ')
        except (KeyboardInterrupt, EOFError):
            print()
            logger.error('Aborted by user.')
            exit(3)

    return (host, port, passwd)
