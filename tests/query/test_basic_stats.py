"""Tests the basic_stats module."""

from ipaddress import IPv4Address
from unittest import TestCase

from mcipc.query.proto.common import Type, random_session_id
from mcipc.query.proto.basic_stats import BasicStats


class TestBasicStats(TestCase):
    """Tests the BasicStats named tuple."""

    def setUp(self):
        """Creates a BasicStats."""
        self.type = Type.STAT
        self.session_id = random_session_id()
        self.ip_address = IPv4Address('127.0.0.1')
        self.basic_stats = BasicStats(
            self.type,
            self.session_id,
            'Message of the day',
            'survival',
            'world',
            1,
            20,
            25565,
            self.ip_address
        )
        self.json = {
            'type': int(self.type.value),
            'session_id': int(self.session_id),
            'motd': 'Message of the day',
            'game_type': 'survival',
            'map': 'world',
            'num_players': 1,
            'max_players': 20,
            'host_port': 25565,
            'host_ip': str(self.ip_address)
        }

    def test_json_serialization(self):
        """Tests JSON serialization of BasticStats."""
        self.assertEqual(dict(self.basic_stats), self.json)
