"""Types for client -> Java Edition server communication."""

from typing import Union

from mcipc.rcon.je.enumerations import Biome
from mcipc.rcon.je.enumerations import CollisionRule
from mcipc.rcon.je.enumerations import Color
from mcipc.rcon.je.enumerations import Enchantment
from mcipc.rcon.je.enumerations import ParticleMode
from mcipc.rcon.je.enumerations import RenderType
from mcipc.rcon.je.enumerations import ScheduleMode
from mcipc.rcon.je.enumerations import SoundSource
from mcipc.rcon.je.enumerations import Structure
from mcipc.rcon.je.enumerations import TeamOption
from mcipc.rcon.je.enumerations import TimeSpec
from mcipc.rcon.je.enumerations import TimeUnit
from mcipc.rcon.je.enumerations import Visibility


__all__ = [
    'Biome',
    'CollisionRule',
    'Color',
    'Enchantment',
    'ParticleMode',
    'RenderType',
    'ScheduleMode',
    'SoundSource',
    'Structure',
    'TeamOption',
    'TeamValue',
    'Time',
    'TimeSpec',
    'TimeUnit',
    'Visibility'
]


Biome = Union[Biome, str]
CollisionRule = Union[CollisionRule, str]
Color = Union[Color, str]
Enchantment = Union[Enchantment, str]
ParticleMode = Union[ParticleMode, str]
RenderType = Union[RenderType, str]
ScheduleMode = Union[ScheduleMode, str]
SoundSource = Union[SoundSource, str]
Structure = Union[Structure, str]
TeamOption = Union[TeamOption, str]
Time = Union[str, int, float]
TimeSpec = Union[TimeSpec, str]
TimeUnit = Union[TimeUnit, str]
Visibility = Union[Visibility, str]
TeamValue = Union[CollisionRule, Color, Visibility, dict, bool, str]
