"""RCON client library."""

from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.editions import Edition
from mcipc.rcon.ee import Client as EducationClient
from mcipc.rcon.je import Client as JavaClient
from mcipc.rcon.exceptions import CommandError
from mcipc.rcon.exceptions import InvalidArgument
from mcipc.rcon.exceptions import LocationNotFound
from mcipc.rcon.exceptions import UnknownCommand


__all__ = [
    'CLIENTS',
    'CommandError',
    'InvalidArgument',
    'LocationNotFound',
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
