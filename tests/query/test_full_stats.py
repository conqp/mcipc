"""Tests the full_stats module."""

from ipaddress import IPv4Address
from unittest import TestCase

from mcipc.query.proto.common import Type, random_session_id
from mcipc.query.proto.full_stats import FullStats


class TestFullStats(TestCase):
    """Tests the FullStats named tuple."""

    def setUp(self):
        """Sets up test data."""
        self.type = Type.STAT
        self.session_id = random_session_id()
        self.ip_address = IPv4Address('127.0.0.1')
        self.full_stats = FullStats(
            self.type,
            self.session_id,
            'My Server',
            'survival',
            'Message of the day',
            '1.16.4',
            {},
            'world',
            2,
            20,
            25565,
            self.ip_address,
            ['coNQP', 'foo']
        )
        self.json = {
            'type': int(self.type.value),
            'session_id': int(self.session_id),
            'host_name': 'My Server',
            'game_type': 'survival',
            'game_id': 'Message of the day',
            'version': '1.16.4',
            'map': 'world',
            'plugins': {},
            'num_players': 2,
            'max_players': 20,
            'host_port': 25565,
            'host_ip': str(self.ip_address),
            'players': ['coNQP', 'foo']
        }

    def test_json_serialization(self):
        """Tests JSON serialization of FullStats."""
        self.assertEqual(dict(self.full_stats), self.json)
