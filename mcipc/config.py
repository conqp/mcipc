"""Server configuration parser."""

from collections import namedtuple
from configparser import ConfigParser
from pathlib import Path


__all__ = [
    'SERVERS_INI',
    'FORTUNE',
    'InvalidCredentialsError',
    'servers',
    'Credentials']


_SERVERS = ConfigParser()
SERVERS_INI = Path('/etc/mcipc.d/servers.conf')
FORTUNE = Path('/usr/bin/fortune')


class InvalidCredentialsError(ValueError):
    """Indicates invalid credentials."""

    pass


def servers(name=None):
    """Yields the respective servers."""

    _SERVERS.read(str(SERVERS_INI))

    servers_ = {
        section: (_SERVERS[section]['host'], int(_SERVERS[section]['port']),
                  _SERVERS[section].get('passwd'))
        for section in _SERVERS.sections()}

    if name is None:
        return servers_

    return servers_[name]


class Credentials(namedtuple('Credentials', ('host', 'port', 'passwd'))):
    """Represents server credentials."""

    __slots__ = ()

    @classmethod
    def from_string(cls, string):
        """Reads the credentials from the given string."""

        try:
            host, port = string.split(':')
        except ValueError:
            try:
                return servers(string)
            except KeyError:
                raise InvalidCredentialsError(f'No such server: {string}.')

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
