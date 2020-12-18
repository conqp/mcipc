"""RCON server configuration."""

from __future__ import annotations
from configparser import ConfigParser, SectionProxy
from logging import getLogger
from pathlib import Path
from typing import Dict, Iterator, NamedTuple, Tuple

from mcipc.enumerations import Edition
from mcipc.exceptions import InvalidConfig


__all__ = ['servers']


CONFIG = ConfigParser()
CONFIG_FILE = Path('/etc/mcipc.d/rcon.conf')
LOGGER = getLogger('RCON Config')


class Config(NamedTuple):
    """Represents server configuration."""

    edition: Edition
    host: str
    port: int
    passwd: str

    @classmethod
    def from_string(cls, string: str) -> Config:
        """Reads the credentials from the given string."""
        try:
            edition, string = string.split('://')
        except ValueError:
            edition = Edition.JAVA
            LOGGER.warning('No edition specified, defaulting to: %s', edition)
        else:
            edition = Edition.from_string(edition)

        try:
            host, port = string.split(':')
        except ValueError:
            raise InvalidConfig(f'Invalid socket: {string}.') from None

        try:
            port = int(port)
        except ValueError:
            raise InvalidConfig(f'Not an integer: {port}.') from None

        try:
            passwd, host = host.rsplit('@', maxsplit=1)
        except ValueError:
            passwd = None

        return cls(edition, host, port, passwd)

    @classmethod
    def from_config_section(cls, section: SectionProxy) -> Config:
        """Creates a credentials tuple from
        the respective config section.
        """
        try:
            edition = section['edition']
        except KeyError:
            edition = Edition.JAVA
            LOGGER.warning('No edition specified, defaulting to: %s', edition)
        else:
            edition = Edition.from_string(edition)

        host = section['host']
        port = section.getint('port')
        passwd = section.get('passwd')
        return cls(edition, host, port, passwd)


def entries(config_parser: ConfigParser) -> Iterator[Tuple[str, Config]]:
    """Yields entries."""

    for section in config_parser.sections():
        yield (section, Config.from_config_section(config_parser[section]))


def servers() -> Dict[str, Config]:
    """Returns a dictionary of servers."""

    CONFIG.read(CONFIG_FILE)
    return dict(entries(CONFIG))
