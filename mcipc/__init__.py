"""An IPC library to communicate with Minecraft servers."""

from mcipc.query import Client as QueryClient
from mcipc.rcon import CLIENTS as RCON_CLIENTS
from mcipc.rcon import Client as RCONClient
from mcipc.rcon import BedrockClient as RCONBedrockClient
from mcipc.rcon import EducationClient as RCONEducationClient
from mcipc.rcon import JavaClient as RCONJavaClient
from mcipc.rcon import StructureNotFound
from mcipc.rcon import WrongPassword
from mcipc.rcon import rconcmd


__all__ = [
    'RCON_CLIENTS',
    'StructureNotFound',
    'WrongPassword',
    'QueryClient',
    'RCONClient',
    'RCONBedrockClient',
    'RCONEducationClient',
    'RCONJavaClient',
    'rconcmd'
]
