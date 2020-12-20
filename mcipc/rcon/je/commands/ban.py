"""Banning, pardoning and kicking of players or IP addresses."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import IPAddressOrHostname


__all__ = ['ban', 'ban_ip', 'banlist', 'pardon']


def ban(self: Client, player: str, *reasons: str) -> str:
    """Adds a player to then ban list."""

    return self.run('ban', player, *reasons)


def ban_ip(self: Client, target: IPAddressOrHostname, *reasons: str) -> str:
    """Adds an IP address to the ban list."""

    return self.run('ban-ip', target, *reasons)


def banlist(self: Client, *ips_or_players: IPAddressOrHostname) -> str:
    """Displays the server's ban list."""

    return self.run('banlist', *ips_or_players)


def pardon(self: Client, target: str) -> str:
    """Removes entries from the banlist."""

    return self.run('pardon', target)
