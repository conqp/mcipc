"""Types for RCON commands."""

from __future__ import annotations
from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from typing import NamedTuple, Union


__all__ = [
    'Ability',
    'Action',
    'Anchor',
    'Attribute',
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
    'FillMode',
    'GameMode',
    'Hand',
    'IntRange',
    'IPAddressOrHostname',
    'JSON',
    'MaskMode',
    'Rotation',
    'ScanMode',
    'SetblockMode',
    'StorageType',
    'Style',
    'TargetSelector',
    'TargetSelectorPrefix',
    'TargetType',
    'TargetValue',
    'TimeType',
    'Vec2',
    'Vec3',
    'XPUnit'
]


Coordinate = Union[int, str]
IPAddressOrHostname = Union[IPv4Address, IPv6Address, str]
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


class Hand(Enum):
    """Available hands."""

    MAINHAND = 'mainhand'
    OFFHAND = 'offhand'


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


class SetblockMode(Enum):
    """Available modes to set blocks."""

    DESTROY = 'destroy'
    KEEP = 'keep'
    REPLACE = 'replace'


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


class TimeType(Enum):
    """Available time types."""

    DAYTIME = 'daytime'
    GAMETIME = 'gametime'
    DAY = 'day'


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
