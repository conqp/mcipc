"""Low-level protocol stuff."""

from typing import Union

from mcipc.query.proto.basic_stats import BasicStatsMixin
from mcipc.query.proto.basic_stats import Request as BasicStatsRequest
from mcipc.query.proto.full_stats import FullStatsMixin
from mcipc.query.proto.full_stats import Request as FullStatsRequest
from mcipc.query.proto.handshake import HandshakeMixin
from mcipc.query.proto.handshake import Request as HandshakeRequest


__all__ = ['BasicStatsMixin', 'FullStatsMixin', 'HandshakeMixin', 'Packet']


Packet = Union[BasicStatsRequest, FullStatsRequest, HandshakeRequest]
