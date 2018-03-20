"""RCON server credentials."""

from collections import namedtuple

from mcipc.config import servers

__all__ = ['InvalidCredentialsError', 'Credentials']


class InvalidCredentialsError(ValueError):
    """Indicates invalid credentials."""

    pass


class Credentials(namedtuple('Credentials', ('host', 'port', 'passwd'))):
    """Represents server credentials."""

    @classmethod
    def from_string(cls, string):
        """Returns host, port and password of the RCON server."""

        try:
            host, port = string.split(':')
        except ValueError:
            try:
                return servers()[string]
            except KeyError:
                raise InvalidCredentialsError(f'No such server: {string}.')

        try:
            port = int(port)
        except ValueError:
            InvalidCredentialsError(f'Not an integer: {port}.')

        try:
            passwd, host = host.split('@')
        except ValueError:
            passwd = None

        return cls(host, port, passwd)
