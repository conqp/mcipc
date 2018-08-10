"""Server configuration parser."""

from collections import namedtuple
from configparser import ConfigParser
from pathlib import Path


__all__ = [
    'LOG_FORMAT',
    'FORTUNE',
    'InvalidCredentialsError',
    'CredentialsConfig']


LOG_FORMAT = '[%(levelname)s] %(name)s: %(message)s'
FORTUNE = Path('/usr/bin/fortune')


class InvalidCredentialsError(ValueError):
    """Indicates invalid credentials."""

    pass


class CredentialsConfig(ConfigParser):
    """Parses the RCON config file."""

    def __init__(self, filename):
        """Sets the file name."""
        super().__init__()
        self.filename = filename

    @property
    def servers(self):
        """Returns a dictionary of servers."""
        self.read(self.filename)
        return {
            section: Credentials.from_config_section(self[section])
            for section in self.sections()}


class Credentials(namedtuple('Credentials', ('host', 'port', 'passwd'))):
    """Represents server credentials."""

    __slots__ = ()

    @classmethod
    def from_string(cls, string):
        """Reads the credentials from the given string."""

        try:
            host, port = string.split(':')
        except ValueError:
            raise InvalidCredentialsError(f'Invalid socket string: {string}.')

        try:
            port = int(port)
        except ValueError:
            InvalidCredentialsError(f'Not an integer: {port}.')

        try:
            passwd, host = host.rsplit('@', maxsplit=1)
        except ValueError:
            passwd = None

        return cls(host, port, passwd)

    @classmethod
    def from_config_section(cls, section):
        """Creates a credentials tuple from
        the respective config section.
        """
        return cls(
            section['host'], int(section['port']), section.get('passwd'))
