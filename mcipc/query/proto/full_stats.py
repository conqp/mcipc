"""Full statistics protocol."""

from ipaddress import IPv4Address
from typing import NamedTuple

from mcipc.query.proto.common import MAGIC, random_session_id, Type


__all__ = ['Request', 'FullStats']


PADDING = 0
ZERO = b'\0'


def get_dict(bytes_):
    """Returns the end index and a dictionary
    of zero-separated key-value pairs.
    """

    item = b''
    dictionary = {}
    key = None
    is_key = True

    for index, integer in enumerate(bytes_):
        byte = bytes([integer])

        if byte == ZERO:
            if not item and is_key:
                return (index, dictionary)

            if is_key:
                key = item
                is_key = False
            else:
                dictionary[key] = item
                key = None
                is_key = True

            item = b''
        else:
            item += byte

    raise ValueError('Bytes string not properly terminated.', bytes_)


def items(bytes_):
    """Yields zero-byte-separated items."""

    item = b''

    for integer in bytes_:
        byte = bytes([integer])

        if byte == ZERO:
            if not item:
                return

            yield item
            item = b''
        else:
            item += byte


def plugins_to_dict(string):
    """Convers a plugins string into a dictionary."""

    try:
        mod, plugins = string.split(': ')
    except ValueError:  # No plugins.
        return {}

    plugins = plugins.split('; ')
    return {mod: tuple(plugins)}


def stats_from_dict(dictionary):
    """Yields statistics options from the provided dictionary."""

    yield dictionary[b'hostname'].decode('latin-1')
    yield dictionary[b'gametype'].decode()
    yield dictionary[b'game_id'].decode()
    yield dictionary[b'version'].decode()
    yield plugins_to_dict(dictionary[b'plugins'].decode('latin-1'))
    yield dictionary[b'map'].decode()
    yield int(dictionary[b'numplayers'].decode())
    yield int(dictionary[b'maxplayers'].decode())
    yield int(dictionary[b'hostport'].decode())
    yield IPv4Address(dictionary[b'hostip'].decode())


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
        payload += self.session_id.to_bytes(4, 'big')
        payload += self.challenge_token.to_bytes(4, 'big')
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
    host_ip: IPv4Address
    players: tuple

    @classmethod
    def from_bytes(cls, bytes_):
        """Creates the full stats object from the respective bytes."""
        type_ = int.from_bytes(bytes_[0:1], 'big')
        session_id = int.from_bytes(bytes_[1:5], 'big')
        index = 16  # Discard padding.
        index, stats = get_dict(bytes_[index:])
        index += 16 + 1     # Discard additional null byte.
        index += 10     # Discard padding.
        players = tuple(player.decode() for player in items(bytes_[index:]))
        return cls(Type(type_), session_id, *stats_from_dict(stats), players)

    def to_json(self, ip_type=str):
        """Returns a JSON-ish dict."""
        host_ip = ip_type(self.host_ip)
        return {
            'type': self.type.value, 'session_id': self.session_id,
            'host_name': self.host_name, 'game_type': self.game_type,
            'game_id': self.game_id, 'version': self.version,
            'plugins': self.plugins, 'map': self.map,
            'num_players': self.num_players, 'max_players': self.max_players,
            'host_port': self.host_port, 'host_ip': host_ip,
            'players': self.players}
