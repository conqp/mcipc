"""Full statistics protocol."""

from __future__ import annotations
from typing import IO, Iterator, NamedTuple

from mcipc.functions import json_serializable
from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import NULL
from mcipc.query.proto.common import ip_or_hostname
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import BigEndianSignedInt32
from mcipc.query.proto.common import IPAddressOrHostname
from mcipc.query.proto.common import Type


__all__ = ['Request', 'FullStats']


PADDING = b'\x00\x00\x00\x00'


def read_stats(file: IO) -> dict:
    """Returns the end index and a dictionary
    of zero-separated key-value pairs.
    """

    item = ''
    dictionary = {}
    key = None
    is_key = True

    while True:
        byte = file.read(1)

        if byte == NULL:
            if not item and is_key:
                return dictionary

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


def read_players(file: IO) -> Iterator[str]:
    """Yields zero-byte-separated items."""

    item = ''

    while True:
        byte = file.read(1)

        if byte == NULL:
            if not item:
                return

            yield item
            item = ''
        else:
            item += byte.decode('latin-1')


def plugins_to_dict(string: str) -> dict:
    """Convers a plugins string into a dictionary."""

    try:
        mod, plugins = string.split(': ')
    except ValueError:  # No plugins.
        return {}

    return {mod: plugins.split('; ')}


def stats_from_dict(dictionary: dict):
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

    magic: bytes = MAGIC
    type: Type = Type.STAT
    session_id: BigEndianSignedInt32 = BigEndianSignedInt32()
    challenge_token: BigEndianSignedInt32 = BigEndianSignedInt32()
    padding: bytes = PADDING

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += bytes(self.session_id)
        payload += bytes(self.challenge_token)
        payload += self.padding
        return payload

    @classmethod
    def create(cls, challenge_token: BigEndianSignedInt32) -> Request:
        """Creates a new request with the given challenge token."""
        return cls(session_id=random_session_id(),
                   challenge_token=challenge_token)


@json_serializable
class FullStats(NamedTuple):
    """Full statistics response."""

    type: Type
    session_id: BigEndianSignedInt32
    host_name: str
    game_type: str
    game_id: str
    version: str
    plugins: dict
    map: str
    num_players: int
    max_players: int
    host_port: int
    host_ip: IPAddressOrHostname
    players: list[str]

    @classmethod
    def read(cls, file: IO) -> FullStats:
        """Read a full stats response."""
        type_ = Type.read(file)
        session_id = BigEndianSignedInt32.read(file)
        file.read(11)   # Discard padding.
        stats = read_stats(file)
        file.read(10)   # Discard padding.
        players = list(read_players(file))
        return cls(type_, session_id, *stats_from_dict(stats), players)
