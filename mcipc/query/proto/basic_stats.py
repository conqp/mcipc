"""Basic statistics protocol."""

from ipaddress import IPv4Address, IPv6Address
from typing import NamedTuple, Union

from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import ip_or_hostname
from mcipc.query.proto.common import Type


__all__ = ['Request', 'BasicStats', 'BasicStatsMixin']


class Request(NamedTuple):
    """Basic statistics request packet."""

    magic: bytes
    type: Type
    session_id: int
    challenge_token: int

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += self.session_id.to_bytes(4, 'big', signed=True)
        payload += self.challenge_token.to_bytes(4, 'big', signed=True)
        return payload

    @classmethod
    def create(cls, challenge_token, session_id=None):
        """Creates a new request with the specified challenge
        token and the specified or a random session ID.
        """
        if session_id is None:
            session_id = random_session_id()

        return cls(MAGIC, Type.STAT, session_id, challenge_token)


class BasicStats(NamedTuple):
    """Basic statistics response packet."""

    type: Type
    session_id: int
    motd: str
    game_type: str
    map: str
    num_players: int
    max_players: int
    host_port: int
    host_ip: Union[IPv4Address, IPv6Address, str]

    @classmethod
    def from_bytes(cls, bytes_):    # pylint: disable=R0914
        """Creates the packet from the respective bytes."""
        type_ = Type.from_bytes(bytes_[0:1])
        session_id = int.from_bytes(bytes_[1:5], 'big', signed=True)

        try:
            motd, *blocks, port_ip, _ = bytes_[5:].split(b'\0')
        except ValueError:
            raise ValueError('Unexpected amount of Null terminated strings.')

        motd = motd.decode('latin-1')
        strings = [block.decode('latin-1') for block in blocks]

        try:
            game_type, map_, num_players, max_players = strings
        except ValueError:
            raise ValueError('Unexpected amount of string fields.')

        num_players = int(num_players)
        max_players = int(max_players)
        host_port = int.from_bytes(port_ip[0:2], 'little')
        host_ip = ip_or_hostname(port_ip[2:].decode())
        return cls(
            type_, session_id, motd, game_type, map_, num_players, max_players,
            host_port, host_ip)

    def to_json(self, ip_type=str) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'type': self.type.value,
            'session_id': self.session_id,
            'motd': self.motd,
            'game_type': self.game_type,
            'map': self.map,
            'num_players': self.num_players,
            'max_players': self.max_players,
            'host_port': self.host_port,
            'host_ip': ip_type(self.host_ip)
        }


class BasicStatsMixin:  # pylint: disable=R0903
    """Query client mixin for basic stats."""

    @property
    def basic_stats(self) -> BasicStats:
        """Returns basic stats"""
        request = Request.create(self._challenge_token)
        return self.communicate(request, BasicStats)
