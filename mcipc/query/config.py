"""Query server configuration."""

from __future__ import annotations
from configparser import ConfigParser, SectionProxy
from os import getenv, name
from pathlib import Path
from typing import Iterator, NamedTuple

from mcipc.query.exceptions import InvalidConfig


__all__ = ['CONFIG']


CONFIG = ConfigParser()

if name == 'posix':
    CONFIG_FILE = Path('/etc/query.conf')
elif name == 'nt':
    CONFIG_FILE = Path(getenv('LOCALAPPDATA')).joinpath('query.conf')
else:
    raise NotImplementedError(f'Unsupported operating system: {name}')


class Config(NamedTuple):
    """Represents server configuration."""

    host: str
    port: int

    @classmethod
    def from_string(cls, string: str) -> Config:
        """Reads the credentials from the given string."""
        try:
            host, port = string.split(':')
        except ValueError:
            raise InvalidConfig(f'Invalid socket: {string}.') from None

        try:
            port = int(port)
        except ValueError:
            raise InvalidConfig(f'Not an integer: {port}.') from None

        return cls(host, port)

    @classmethod
    def from_config_section(cls, section: SectionProxy) -> Config:
        """Creates a credentials tuple from
        the respective config section.
        """
        host = section['host']
        port = section.getint('port')
        return cls(host, port)


def entries(config_parser: ConfigParser) -> Iterator[tuple[str, Config]]:
    """Yields config entries."""

    for section in config_parser.sections():
        yield (section, Config.from_config_section(config_parser[section]))


def servers() -> dict[str, Config]:
    """Returns a dictionary of servers."""

    CONFIG.read(CONFIG_FILE)
    return dict(entries(CONFIG))
