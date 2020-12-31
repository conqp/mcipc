"""RCON client library."""

from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.ee import Client as EducationClient
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
from mcipc.rcon.enumerations import Edition
from mcipc.rcon.enumerations import FillMode
from mcipc.rcon.enumerations import GameMode
from mcipc.rcon.enumerations import Hand
from mcipc.rcon.enumerations import MaskMode
from mcipc.rcon.enumerations import ScanMode
from mcipc.rcon.enumerations import SetblockMode
from mcipc.rcon.enumerations import StorageType
from mcipc.rcon.enumerations import Style
from mcipc.rcon.enumerations import TargetType
from mcipc.rcon.enumerations import TimeType
from mcipc.rcon.enumerations import XPUnit
from mcipc.rcon.errors import CommandError
from mcipc.rcon.errors import InvalidArgument
from mcipc.rcon.errors import InvalidInteger
from mcipc.rcon.errors import InvalidNameOrUUID
from mcipc.rcon.errors import LocationNotFound
from mcipc.rcon.errors import NoPlayerFound
from mcipc.rcon.errors import UnexpectedTrailingData
from mcipc.rcon.errors import UnknownCommand
from mcipc.rcon.je import Client as JavaClient


__all__ = [
    # Clients
    'CLIENTS',
    'BedrockClient',
    'EducationClient',
    'JavaClient',
    # Exceptions
    'CommandError',
    'InvalidArgument',
    'InvalidInteger',
    'InvalidNameOrUUID',
    'LocationNotFound',
    'NoPlayerFound',
    'UnexpectedTrailingData',
    'UnknownCommand',
    # Enums
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
    'MaskMode',
    'ScanMode',
    'SetblockMode',
    'StorageType',
    'Style',
    'TargetType',
    'TimeType',
    'XPUnit'
]


CLIENTS = {
    Edition.BEDROCK: BedrockClient,
    Edition.EDUCATION: EducationClient,
    Edition.JAVA: JavaClient
}
Client = JavaClient     # For backwards compatibility.
