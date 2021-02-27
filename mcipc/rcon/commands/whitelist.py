"""Implementation of the whitelist command."""

from functools import partial
from re import fullmatch

from mcipc.rcon.client import Client
from mcipc.rcon.functions import boolmap, parsed
from mcipc.rcon.proxy import CommandProxy


__all__ = ['WhitelistProxy', 'whitelist']


ADDED = 'Added (.+) to the whitelist'
TURNED_OFF = 'Whitelist is now turned off'
TURNED_ON = 'Whitelist is now turned on'
RELOADED = 'Reloaded the whitelist'
REMOVED = 'Removed (.+) from the whitelist'
LIST = 'There are (\\d+) whitelisted players: (.*)'


def parse_list(response: str) -> list[str]:
    """Returns a list of whitelisted players."""

    if match := fullmatch(LIST, response):
        return list(filter(None, map(str.strip, match.group(2).split(','))))

    return []


class WhitelistProxy(CommandProxy):
    """Proxy for whitelist commands."""

    @parsed(partial(boolmap, true=ADDED, default=False))
    def add(self, name: str) -> str:
        """Adds a player to the whitelist."""
        return self._run('add', name)

    @parsed(parse_list)
    def list(self) -> str:
        """Lists the whitelist."""
        return self._run('list')

    @parsed(partial(boolmap, true=TURNED_OFF, default=False))
    def off(self) -> str:
        """Turns the whitelist checking off."""
        return self._run('off')

    @parsed(partial(boolmap, true=TURNED_ON, default=False))
    def on(self) -> str:    # pylint: disable=C0103
        """Turns the whitelist checking on."""
        return self._run('on')

    @parsed(partial(boolmap, true=RELOADED, default=False))
    def reload(self) -> str:
        """Reloads the whitelist from the file."""
        return self._run('reload')

    @parsed(partial(boolmap, true=REMOVED, default=False))
    def remove(self, name: str) -> str:
        """Removes a player from the whitelist."""
        return self._run('remove', name)


def whitelist(self: Client) -> WhitelistProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.commands.whitelist.WhitelistProxy`
    """

    return WhitelistProxy(self, 'whitelist')
