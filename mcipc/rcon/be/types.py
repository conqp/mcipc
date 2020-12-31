"""Types for client -> Bedrock Edition server communication."""

from typing import Union

from mcipc.rcon.be.enumerations import Biome
from mcipc.rcon.be.enumerations import Enchantment
from mcipc.rcon.be.enumerations import EntityEquipmentSlot
from mcipc.rcon.be.enumerations import FillType
from mcipc.rcon.be.enumerations import Location
from mcipc.rcon.be.enumerations import MatchMode
from mcipc.rcon.be.enumerations import Mirror
from mcipc.rcon.be.enumerations import MusicRepeatMode
from mcipc.rcon.be.enumerations import Operator
from mcipc.rcon.be.enumerations import Order
from mcipc.rcon.be.enumerations import ReplaceMode
from mcipc.rcon.be.enumerations import RideRules
from mcipc.rcon.be.enumerations import Rotation
from mcipc.rcon.be.enumerations import SaveCommand
from mcipc.rcon.be.enumerations import Structure
from mcipc.rcon.be.enumerations import StructureAnimationMode
from mcipc.rcon.be.enumerations import StructureSaveMode
from mcipc.rcon.be.enumerations import TeleportRules
from mcipc.rcon.be.enumerations import TimeSpec


__all__ = [
    'Biome',
    'Enchantment',
    'EntityEquipmentSlot',
    'FillType',
    'Location',
    'MatchMode',
    'Mirror',
    'MusicRepeatMode',
    'Operator',
    'Order',
    'RelativeFloat',
    'ReplaceMode',
    'RideRules',
    'Rotation',
    'SaveCommand',
    'Structure',
    'StructureAnimationMode',
    'StructureSaveMode',
    'TeleportRules',
    'TimeSpec'
]


Biome = Union[Biome, str]
Enchantment = Union[Enchantment, str]
EntityEquipmentSlot = Union[EntityEquipmentSlot, str]
FillType = Union[FillType, str]
Location = Union[Location, str]
MatchMode = Union[MatchMode, str]
Mirror = Union[Mirror, str]
MusicRepeatMode = Union[MusicRepeatMode, str]
Operator = Union[Operator, str]
Order = Union[Order, str]
RelativeFloat = Union[float, str]
ReplaceMode = Union[ReplaceMode, str]
RideRules = Union[RideRules, str]
Rotation = Union[Rotation, str]
SaveCommand = Union[SaveCommand, str]
Structure = Union[Structure, str]
StructureAnimationMode = Union[StructureAnimationMode, str]
StructureSaveMode = Union[StructureSaveMode, str]
TeleportRules = Union[TeleportRules, str]
TimeSpec = Union[TimeSpec, str]
