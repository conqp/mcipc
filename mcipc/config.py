"""Server configuration parser."""

from configparser import ConfigParser
from pathlib import Path

__all__ = ['SERVERS_INI', 'FORTUNE', 'servers']


SERVERS_INI = Path('/etc/mcipc.d/servers.conf')
_SERVERS = ConfigParser()
FORTUNE = Path('/usr/bin/fortune')


def servers():
    """Yields the respective servers."""

    _SERVERS.read(str(SERVERS_INI))

    return {
        section: (_SERVERS[section]['host'], int(_SERVERS[section]['port']),
                  _SERVERS[section].get('passwd'))
        for section in _SERVERS.sections()}
