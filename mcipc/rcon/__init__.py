"""RCON client library."""

from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.ee import Client as EducationClient
from mcipc.rcon.enumerations import Edition
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
    'CLIENTS',
    'CommandError',
    'InvalidArgument',
    'InvalidInteger',
    'InvalidNameOrUUID',
    'LocationNotFound',
    'NoPlayerFound',
    'UnexpectedTrailingData',
    'UnknownCommand',
    'BedrockClient',
    'Edition',
    'EducationClient',
    'JavaClient'
]


CLIENTS = {
    Edition.BEDROCK: BedrockClient,
    Edition.EDUCATION: EducationClient,
    Edition.JAVA: JavaClient
}
Client = JavaClient     # For backwards compatibility.
