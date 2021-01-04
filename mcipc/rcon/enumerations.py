"""Enumerations."""

from enum import Enum

from mcipc.rcon.item import Item


__all__ = [
    'Ability',
    'Action',
    'Anchor',
    'Attribute',
    'BossbarSlot',
    'CamerashakeType',
    'CloneMode',
    'Color',
    'DatapackMode',
    'DatapackState',
    'DataType',
    'DebugCommand',
    'Difficulty',
    'Direction',
    'Edition',
    'FillMode',
    'GameMode',
    'Hand',
    'Item',
    'MaskMode',
    'ScanMode',
    'SetblockMode',
    'StorageType',
    'Style',
    'TargetSelector',
    'TargetType',
    'TimeType',
    'XPUnit'
]


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


class Edition(Enum):
    """Represents the several Minecraft editions."""

    BEDROCK = 'Bedrock Edition'
    EDUCATION = 'Education Edition'
    JAVA = 'Java Edition'


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


class MaskMode(Enum):
    """Masking mode."""

    REPLACE = 'replace'
    MASKED = 'masked'
    FILTERED = 'filtered'


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


class TargetSelector(Enum):
    """A target selector."""

    AGENT = '@c'
    ALL_AGENTS = '@v'
    ALL_ENTITIES = '@e'
    ALL_PLAYERS = '@a'
    ISSUER = '@s'
    NEAREST_PLAYER = '@p'
    RANDOM_PLAYER = '@r'


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


class XPUnit(Enum):
    """Available experience units."""

    LEVELS = 'levels'
    POINTS = 'points'
