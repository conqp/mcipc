"""Low-level protocol stuff."""

from typing import Union

from mcipc.query.proto.basic_stats import BasicStats, BasicStatsMixin
from mcipc.query.proto.basic_stats import Request as BasicStatsRequest
from mcipc.query.proto.full_stats import FullStats, FullStatsMixin
from mcipc.query.proto.full_stats import Request as FullStatsRequest
from mcipc.query.proto.handshake import HandshakeMixin, Response
from mcipc.query.proto.handshake import Request as HandshakeRequest


__all__ = [
    'BasicStatsMixin',
    'FullStatsMixin',
    'HandshakeMixin',
    'Request',
    'Response'
]


Request = Union[BasicStatsRequest, FullStatsRequest, HandshakeRequest]
Response = Union[BasicStats, FullStats, Response]
