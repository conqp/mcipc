"""Basic statistics protocol."""

from __future__ import annotations
from typing import IO, NamedTuple

from mcipc.functions import json_serializable
from mcipc.query.proto.common import MAGIC
from mcipc.query.proto.common import NULL
from mcipc.query.proto.common import decodeall
from mcipc.query.proto.common import ip_or_hostname
from mcipc.query.proto.common import random_session_id
from mcipc.query.proto.common import BigEndianSignedInt32
from mcipc.query.proto.common import IPAddressOrHostname
from mcipc.query.proto.common import Type


__all__ = ['Request', 'BasicStats']


class Request(NamedTuple):
    """Basic statistics request packet."""

    magic: bytes = MAGIC
    type: Type = Type.STAT
    session_id: BigEndianSignedInt32 = BigEndianSignedInt32()
    challenge_token: BigEndianSignedInt32 = BigEndianSignedInt32()

    def __bytes__(self):
        """Returns the packet as bytes."""
        payload = self.magic
        payload += bytes(self.type)
        payload += bytes(self.session_id)
        payload += bytes(self.challenge_token)
        return payload

    @classmethod
    def create(cls, challenge_token: BigEndianSignedInt32) -> Request:
        """Creates a new request with the given challenge token."""
        return cls(session_id=random_session_id(),
                   challenge_token=challenge_token)


@json_serializable
class BasicStats(NamedTuple):
    """Basic statistics response packet."""

    type: Type
    session_id: BigEndianSignedInt32
    motd: str
    game_type: str
    map: str
    num_players: int
    max_players: int
    host_port: int
    host_ip: IPAddressOrHostname

    @classmethod
    def read(cls, file: IO) -> BasicStats:
        """Reads the basic stats from a file-like object."""
        type_ = Type.read(file)
        session_id = BigEndianSignedInt32.read(file)
        body = b''

        while True:
            body += file.read(1)

            if len(body.split(NULL)) == 7:
                break

        *blocks, port_ip, _ = body.split(NULL)
        motd, game_type, map_, num_players, max_players = decodeall(blocks)
        num_players = int(num_players)
        max_players = int(max_players)
        host_port = int.from_bytes(port_ip[0:2], 'little')
        host_ip = ip_or_hostname(port_ip[2:].decode())
        return cls(
            type_, session_id, motd, game_type, map_, num_players, max_players,
            host_port, host_ip)
