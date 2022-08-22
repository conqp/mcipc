"""Test Item enum."""

from unittest import TestCase

from mcipc.rcon.item import Item


SAMPLES = {
    Item.AIR: ('minecraft:air', 'air'),
    Item.WATER: ('minecraft:water', 'water'),
    Item.POPPY: ('minecraft:poppy', 'poppy'),
    Item.ZOMBIFIED_PIGLIN_SPAWN_EGG: (
        'minecraft:zombified_piglin_spawn_egg',
        'zombified_piglin_spawn_egg'
    )
}


class TestItem(TestCase):
    """Test item serialization and deserialization."""

    def test_string_serialization(self):
        for item, (long_name, short_name) in SAMPLES.items():
            self.assertEqual(str(item), long_name)

    def test_string_deserialization_by_long_name(self):
        for item, (long_name, short_name) in SAMPLES.items():
            self.assertEqual(Item(long_name), item)

    def test_string_deserialization_by_short_name(self):
        for item, (long_name, short_name) in SAMPLES.items():
            self.assertEqual(Item(short_name), item)
