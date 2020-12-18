"""Types for RCON commands."""

from __future__ import annotations
from enum import Enum
from typing import NamedTuple, Union


__all__ = [
    'Ability',
    'Action',
    'Anchor',
    'Attribute',
    'Biome',
    'BossbarSlot',
    'CamerashakeType',
    'CloneMode',
    'Color',
    'CommandSelector',
    'Coordinate',
    'DatapackMode',
    'DatapackState',
    'DataType',
    'DebugCommand',
    'Difficulty',
    'Direction',
    'Enchantment',
    'FillMode',
    'GameMode',
    'IntRange',
    'JSON',
    'MaskMode',
    'Rotation',
    'ScanMode',
    'StorageType',
    'Style',
    'TargetSelector',
    'TargetSelectorPrefix',
    'TargetType',
    'TargetValue',
    'Vec2',
    'Vec3',
    'XPUnit'
]


Coordinate = Union[int, str]
JSON = Union[dict, float, int, list, str]


class Ability(Enum):
    """Player ability."""

    WORLDBUILDER = 'worldbuilder'
    MAYFLY = 'mayfly'
    MUTE = 'mute'


class Action(Enum):
    """Modifier action."""

    ADD = 'add'
    MULTIPLY = 'multiply'
    MULTIPLY_BASE = 'multiply_base'


class Anchor(Enum):
    """Available entity anchors."""

    EYES = 'eyes'
    FEET = 'feet'


class Attribute(Enum):
    """Boss bar attributes."""

    COLOR = 'color'
    MAX = 'max'
    NAME = 'name'
    PLAYERS = 'players'
    STYLE = 'style'
    VALUE = 'value'
    VISIBLE = 'visible'


class Biome(Enum):
    """Available biomes."""

    BADLANDS = 'badlands'
    BADLANDS_PLATEAU = 'badlands_plateau'
    BAMBOO_JUNGLE = 'bamboo_jungle'
    BAMBOO_JUNGLE_HILLS = 'bamboo_jungle_hills'
    BASALT_DELTAS = 'basalt_deltas'
    BEACH = 'beach'
    BIRCH_FOREST = 'birch_forest'
    BIRCH_FOREST_HILLS = 'birch_forest_hills'
    COLD_OCEAN = 'cold_ocean'
    CRIMSON_FOREST = 'crimson_forest'
    DARK_FOREST = 'dark_forest'
    DARK_FOREST_HILLS = 'dark_forest_hills'
    DEEP_COLD_OCEAN = 'deep_cold_ocean'
    DEEP_FROZEN_OCEAN = 'deep_frozen_ocean'
    DEEP_LUKEWARM_OCEAN = 'deep_lukewarm_ocean'
    DEEP_OCEAN = 'deep_ocean'
    DEEP_WARM_OCEAN = 'deep_warm_ocean'
    DESERT = 'desert'
    DESERT_HILLS = 'desert_hills'
    DESERT_LAKES = 'desert_lakes'
    DRIPSTONE_CAVES = 'dripstone_caves'
    END_BARRENS = 'end_barrens'
    END_HIGHLANDS = 'end_highlands'
    END_MIDLANDS = 'end_midlands'
    ERODED_BADLANDS = 'eroded_badlands'
    FLOWER_FOREST = 'flower_forest'
    FOREST = 'forest'
    FROZEN_OCEAN = 'frozen_ocean'
    FROZEN_RIVER = 'frozen_river'
    GIANT_SPRUCE_TAIGA = 'giant_spruce_taiga'
    GIANT_SPRUCE_TAIGA_HILLS = 'giant_spruce_taiga_hills'
    GIANT_TREE_TAIGA = 'giant_tree_taiga'
    GIANT_TREE_TAIGA_HILLS = 'giant_tree_taiga_hills'
    GRAVELLY_MOUNTAINS = 'gravelly_mountains'
    ICE_SPIKES = 'ice_spikes'
    JUNGLE = 'jungle'
    JUNGLE_EDGE = 'jungle_edge'
    JUNGLE_HILLS = 'jungle_hills'
    LUKEWARM_OCEAN = 'lukewarm_ocean'
    MODIFIED_BADLANDS_PLATEAU = 'modified_badlands_plateau'
    MODIFIED_GRAVELLY_MOUNTAINS = 'modified_gravelly_mountains'
    MODIFIED_JUNGLE = 'modified_jungle'
    MODIFIED_JUNGLE_EDGE = 'modified_jungle_edge'
    MODIFIED_WOODEN_BADLANDS_PLATEAU = 'modified_wooded_badlands_plateau'
    MOUNTAIN_EDGE = 'mountain_edge'
    MOUNTAINS = 'mountains'
    MUSHROOM_FIELD_SHORE = 'mushroom_field_shore'
    MUSHROOM_FIELDS = 'mushroom_fields'
    NETHER_WASTES = 'nether_wastes'
    OCEAN = 'ocean'
    PLAINS = 'plains'
    RIVER = 'river'
    SAVANNA = 'savanna'
    SAVANNA_PLATEAU = 'savanna_plateau'
    SHATTERED_SAVANNA = 'shattered_savanna'
    SHATTERED_SAVANNA_PLATEAU = 'shattered_savanna_plateau'
    SMALL_END_ISLANDS = 'small_end_islands'
    SNOWY_BEACH = 'snowy_beach'
    SNOWY_MOUNTAINS = 'snowy_mountains'
    SNOWY_TAIGA = 'snowy_taiga'
    SNOWY_TAIGA_HILLS = 'snowy_taiga_hills'
    SNOWY_TAIGA_MOUNTAINS = 'snowy_taiga_mountains'
    SNOWY_TUNDRA = 'snowy_tundra'
    SOUL_SAND_VALLEY = 'soul_sand_valley'
    STONE_SHORE = 'stone_shore'
    SUNFLOWER_PLAINS = 'sunflower_plains'
    SWAMP = 'swamp'
    SWAMP_HILLS = 'swamp_hills'
    TAIGA = 'taiga'
    TAIGA_HILLS = 'taiga_hills'
    TAIGA_MOUNTAINS = 'taiga_mountains'
    TALL_BIRCH_FOREST = 'tall_birch_forest'
    TALL_BIRCH_HILLS = 'tall_birch_hills'
    THE_END = 'the_end'
    THE_VOID = 'the_void'
    WARM_OCEAN = 'warm_ocean'
    WARPED_FOREST = 'warped_forest'
    WOODED_BADLANDS_PLATEAU = 'wooded_badlands_plateau'
    WOODED_HILLS = 'wooded_hills'
    WOODED_MOUNTAINS = 'wooded_mountains'


class BossbarSlot(Enum):
    """A target slot off a boss bar."""

    VALUE = 'value'
    MAX = 'max'


class CamerashakeType(Enum):
    """Camera shake types."""

    POSITIONAL = 'positional'
    ROTATIONAL = 'rotational'


class CloneMode(Enum):
    """Clone modes."""

    FORCE = 'force'
    MOVE = 'move'
    NORMAL = 'normal'


class Color(Enum):
    """Boss bar colors."""

    BLUE = 'blue'
    GREEN = 'green'
    PINK = 'pink'
    PURPLE = 'purple'
    RED = 'red'
    WHITE = 'white'
    YELLOW = 'yellow'


class DatapackMode(Enum):
    """Available modes."""

    AFTER = 'after'
    BEFORE = 'before'
    FIRST = 'first'
    LAST = 'last'


class DatapackState(Enum):
    """Available states."""

    AVAILABLE = 'available'
    ENABLED = 'enabled'


class DataType(Enum):
    """Data types."""

    BYTE = 'byte'
    DOUBLE = 'double'
    FLOAT = 'float'
    INT = 'int'
    LONG = 'long'
    SHORT = 'short'


class DebugCommand(Enum):
    """Available debug commands."""

    START = 'start'
    STOP = 'stop'
    REPORT = 'report'


class Difficulty(Enum):
    """Available difficulties."""

    PEACEFUL = 'peaceful'
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'


class Direction(Enum):
    """Specifies the direction of Agent to destroy."""

    FORWARD = 'forward'
    BACK = 'back'
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


class Enchantment(Enum):
    """Available enchantments."""

    AQUA_AFFINITY = 'aqua_affinity'
    BANE_OF_ARTHROPODS = 'bane_of_arthropods'
    BLAST_PROTECTION = 'blast_protection'
    CHANNELING = 'channeling'
    CLEAVING = 'cleaving'
    CURSE_OF_BINDING_BE = 'binding'
    CURSE_OF_BINDING_JE = 'binding_curse'
    CURSE_OF_VANISHING_BE = 'vanishing'
    CURSE_OF_VANISHING_JE = 'vanishing_curse'
    DEPTH_STRIDER = 'depth_strider'
    EFFICIENCY = 'efficiency'
    FEATHER_FALLING = 'feather_falling'
    FIRE_ASPECT = 'fire_aspect'
    FIRE_PROTECTION = 'fire_protection'
    FLAME = 'flame'
    FORTUNE = 'fortune'
    FROST_WALKER = 'frost_walker'
    IMPALING = 'impaling'
    INFINITY = 'infinity'
    KNOCKBACK = 'knockback'
    LOOTING = 'looting'
    LOYALTY = 'loyalty'
    LUCK_OF_THE_SEA = 'luck_of_the_sea'
    LURE = 'lure'
    MENDING = 'mending'
    MULTISHOT = 'multishot'
    PIERCING = 'piercing'
    POWER = 'power'
    PROJECTILE_PROTECTION = 'projectile_protection'
    PROTECTION = 'protection'
    PUNCH = 'punch'
    QUICK_CHARGE = 'quick_charge'
    RESPIRATION = 'respiration'
    RIPTIDE = 'riptide'
    SHARPNESS = 'sharpness'
    SILK_TOUCH = 'silk_touch'
    SMITE = 'smite'
    SOUL_SPEED = 'soul_speed'
    SWEEPING = 'sweeping'
    THORNS = 'thorns'
    UNBREAKING = 'unbreaking'


class FillMode(Enum):
    """Available fill modes."""

    DESTROY = 'destroy'
    HOLLOW = 'hollow'
    KEEP = 'keep'
    OUTLINE = 'outline'
    REPLACE = 'replace'


class GameMode(Enum):
    """Available game modes."""

    ADVENTURE = 'adventure'
    CREATIVE = 'creative'
    SPECTATOR = 'spectator'
    SURVIVAL = 'survival'


class IntRange:
    """An integer range."""

    __slots__ = ('start', 'end')

    def __init__(self, start: int = None, end: int = None):
        """Sets start and end."""
        self.start = start
        self.end = end

    def __str__(self):
        """Returns a string for the Minecraft server."""
        if self.start == self.end:
            if self.start is not None:
                return str(self.start)

            raise ValueError('Either start or end need to be specified.')

        items = map(lambda item: '' if item is None else str(item), self)
        return '..'.join(items)


class MaskMode(Enum):
    """Masking mode."""

    REPLACE = 'replace'
    MASKED = 'masked'
    FILTERED = 'filtered'


class Rotation(NamedTuple):
    """Represents a rotation."""

    yaw: Coordinate
    pitch: Coordinate


class ScanMode(Enum):
    """Available scan modes."""

    ALL = 'all'
    MASKED = 'masked'


class StorageType(Enum):
    """Storage types."""

    RESULT = 'result'
    SUCCESS = 'success'


class Style(Enum):
    """Available boss bar styles."""

    NOTCHED_6 = 'notched_6'
    NOTCHED_10 = 'notched_10'
    NOTCHED_12 = 'notched_12'
    NOTCHED_20 = 'notched_20'
    PROGRESS = 'progress'


class TargetSelector:
    """A target selector."""

    __slots__ = ('prefix', 'args')

    def __init__(self, prefix: TargetSelectorPrefix = None, args: dict = None):
        """Sets the prefix and properties."""
        self.prefix = prefix
        self.args = {} if args is None else args

    def __str__(self):
        """Returns a Minecraft command string."""
        items = []

        if self.prefix is not None:
            items.append(self.prefix.value)

        if args := ','.join(f'{key}={value}' for key, value in self.args):
            items.append(f'[{args}]')

        if not items:
            raise ValueError('Cannot stringify an empty target selector.')

        return ''.join(items)


class TargetSelectorPrefix(Enum):
    """Available target selector prefixes."""

    NEAREST_PLAYER = '@p'
    RANDOM_PLAYER = '@r'
    ALL_PLAYERS = '@a'
    ALL_ENTITIES = '@e'
    CALLER = '@s'   # Entity executing the command.
    PLAYER_AGENT = '@c'
    ALL_AGENTS = '@v'


class TargetType(Enum):
    """A target type."""

    BLOCK = 'block'
    ENTITY = 'entity'
    STORAGE = 'storage'


class Vec2(NamedTuple):
    """A 2D vector."""

    x: Coordinate
    z: Coordinate


class Vec3(NamedTuple):
    """A 3D vector."""

    x: Coordinate
    y: Coordinate
    z: Coordinate


class XPUnit(Enum):
    """Available experience units."""

    LEVELS = 'levels'
    POINTS = 'points'


CommandSelector = Union[TargetSelector, str]
TargetValue = Union[Vec3, str]
