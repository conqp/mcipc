"""Server configuration parser."""

from configparser import ConfigParser
from pathlib import Path
from typing import NamedTuple


__all__ = [
    'LOG_FORMAT',
    'FORTUNE',
    'InvalidCredentials',
    'CredentialsConfig'
]


LOG_FORMAT = '[%(levelname)s] %(name)s: %(message)s'
FORTUNE = Path('/usr/bin/fortune')


class InvalidCredentials(ValueError):
    """Indicates invalid credentials."""


class CredentialsConfig(ConfigParser):  # pylint: disable=R0901
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


class Credentials(NamedTuple):
    """Represents server credentials."""

    host: str
    port: int
    passwd: str

    @classmethod
    def from_string(cls, string):
        """Reads the credentials from the given string."""
        try:
            host, port = string.split(':')
        except ValueError:
            raise InvalidCredentials(f'Invalid socket string: {string}.')

        try:
            port = int(port)
        except ValueError:
            raise InvalidCredentials(f'Not an integer: {port}.')

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
        host = section['host']
        port = section.getint('port')
        passwd = section.get('passwd')
        return cls(host, port, passwd)
