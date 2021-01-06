"""Types for type hints."""

from ipaddress import IPv4Address, IPv6Address
from typing import Tuple, Union

from mcipc.rcon.enumerations import Ability
from mcipc.rcon.enumerations import Action
from mcipc.rcon.enumerations import Anchor
from mcipc.rcon.enumerations import Attribute
from mcipc.rcon.enumerations import BossbarSlot
from mcipc.rcon.enumerations import CamerashakeType
from mcipc.rcon.enumerations import CloneMode
from mcipc.rcon.enumerations import Color
from mcipc.rcon.enumerations import DatapackMode
from mcipc.rcon.enumerations import DatapackState
from mcipc.rcon.enumerations import DataType
from mcipc.rcon.enumerations import DebugCommand
from mcipc.rcon.enumerations import Difficulty
from mcipc.rcon.enumerations import Direction
from mcipc.rcon.enumerations import FillMode
from mcipc.rcon.enumerations import GameMode
from mcipc.rcon.enumerations import Hand
from mcipc.rcon.enumerations import Item
from mcipc.rcon.enumerations import MaskMode
from mcipc.rcon.enumerations import ScanMode
from mcipc.rcon.enumerations import SetblockMode
from mcipc.rcon.enumerations import StorageType
from mcipc.rcon.enumerations import Style
from mcipc.rcon.enumerations import TargetSelector
from mcipc.rcon.enumerations import TimeType
from mcipc.rcon.enumerations import XPUnit
from mcipc.rcon.nbt import NBT


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
    'Entity',
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
    'TargetValue',
    'TimeType',
    'Vec2',
    'Vec3',
    'XPUnit'
]


IntOrStr = Union[int, str]
Coordinate = Union[IntOrStr, float]
IntRange = Union[range, str]
IPAddressOrHostname = Union[IPv4Address, IPv6Address, str]
JSON = Union[bool, dict, float, int, list, str]
Rotation = Union[Tuple[IntOrStr, IntOrStr], str]
Vec2 = Union[Tuple[Coordinate, Coordinate], str]
TargetValue = Vec3 = Union[Tuple[Coordinate, Coordinate, Coordinate], str]
# Enumeration / str unions.
Ability = Union[Ability, str]
Action = Union[Action, str]
Anchor = Union[Anchor, str]
Attribute = Union[Attribute, str]
BossbarSlot = Union[BossbarSlot, str]
CamerashakeType = Union[CamerashakeType, str]
CloneMode = Union[CloneMode, str]
Color = Union[Color, str]
DatapackMode = Union[DatapackMode, str]
DatapackState = Union[DatapackState, str]
DataType = Union[DataType, str]
DebugCommand = Union[DebugCommand, str]
Difficulty = Union[Difficulty, str]
Direction = Union[Direction, str]
Entity = Union[Item, NBT, TargetSelector, str]
FillMode = Union[FillMode, str]
GameMode = Union[GameMode, str]
Hand = Union[Hand, str]
MaskMode = Union[MaskMode, str]
ScanMode = Union[ScanMode, str]
SetblockMode = Union[SetblockMode, str]
StorageType = Union[StorageType, str]
Style = Union[Style, str]
TimeType = Union[TimeType, str]
XPUnit = Union[XPUnit, str]
