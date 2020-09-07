"""Full statistics protocol."""

from ipaddress import IPv4Address, IPv6Address
from typing import Generator, NamedTuple, Tuple, Union

from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import ip_or_hostname
from mcipc.query.proto.common import Type


__all__ = ['Request', 'FullStats', 'FullStatsMixin']


PADDING = 0
NULL = b'\0'


def get_dict(bytes_) -> Tuple[int, dict]:
    """Returns the end index and a dictionary
    of zero-separated key-value pairs.
    """

    item = ''
    dictionary = {}
    key = None
    is_key = True

    for index, integer in enumerate(bytes_):
        byte = bytes([integer])

        if byte == NULL:
            if not item and is_key:
                return (index, dictionary)

            if is_key:
                key = item
                is_key = False
            else:
                dictionary[key] = item
                key = None
                is_key = True

            item = ''
        else:
            item += byte.decode('latin-1')

    raise ValueError('Bytes string not properly terminated.', bytes_)


def items(bytes_) -> Generator[str, None, None]:
    """Yields zero-byte-separated items."""

    item = ''

    for integer in bytes_:
        byte = bytes([integer])

        if byte == NULL:
            if not item:
                return

            yield item
            item = ''
        else:
            item += byte.decode('latin-1')


def plugins_to_dict(string) -> dict:
    """Convers a plugins string into a dictionary."""

    try:
        mod, plugins = string.split(': ')
    except ValueError:  # No plugins.
        return {}

    return {mod: plugins.split('; ')}


def stats_from_dict(dictionary):
    """Yields statistics options from the provided dictionary."""

    yield dictionary['hostname']
    yield dictionary['gametype']
    yield dictionary['game_id']
    yield dictionary['version']
    yield plugins_to_dict(dictionary['plugins'])
    yield dictionary['map']
    yield int(dictionary['numplayers'])
    yield int(dictionary['maxplayers'])
    yield int(dictionary['hostport'])
    yield ip_or_hostname(dictionary['hostip'])


class Request(NamedTuple):
    """Basic statistics request packet."""

    magic: bytes
    type: Type
    session_id: int
    challenge_token: int
    padding: int

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += self.session_id.to_bytes(4, 'big', signed=True)
        payload += self.challenge_token.to_bytes(4, 'big', signed=True)
        payload += self.padding.to_bytes(4, 'big')
        return payload

    @classmethod
    def create(cls, challenge_token, session_id=None):
        """Creates a new request with the specified challenge
        token and the specified or a random session ID.
        """
        if session_id is None:
            session_id = random_session_id()

        return cls(MAGIC, Type.STAT, session_id, challenge_token, PADDING)


class FullStats(NamedTuple):
    """Full statistics response."""

    type: Type
    session_id: int
    host_name: str
    game_type: str
    game_id: str
    version: str
    plugins: dict
    map: str
    num_players: int
    max_players: int
    host_port: int
    host_ip: Union[IPv4Address, IPv6Address, str]
    players: tuple

    @classmethod
    def from_bytes(cls, bytes_):
        """Creates the full stats object from the respective bytes."""
        type_ = Type.from_bytes(bytes_[0:1])
        session_id = int.from_bytes(bytes_[1:5], 'big', signed=True)
        index = 16  # Discard padding.
        index, stats = get_dict(bytes_[index:])
        index += 16 + 1     # Discard additional null byte.
        index += 10     # Discard padding.
        players = tuple(items(bytes_[index:]))
        return cls(type_, session_id, *stats_from_dict(stats), players)

    def to_json(self, ip_type=str) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'type': self.type.value,
            'session_id': self.session_id,
            'host_name': self.host_name,
            'game_type': self.game_type,
            'game_id': self.game_id,
            'version': self.version,
            'plugins': self.plugins,
            'map': self.map,
            'num_players': self.num_players,
            'max_players': self.max_players,
            'host_port': self.host_port,
            'host_ip': ip_type(self.host_ip),
            'players': self.players
        }


class FullStatsMixin:   # pylint: disable=R0903
    """Query client mixin for full stats."""

    @property
    def full_stats(self) -> FullStats:
        """Returns full stats"""
        request = Request.create(self._challenge_token)
        return self.communicate(request, FullStats)
