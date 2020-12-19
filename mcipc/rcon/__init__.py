"""RCON client library."""

from mcipc.enumerations import Edition
from mcipc.rcon.console import rconcmd
from mcipc.rcon.exceptions import LocationNotFound
from mcipc.rcon.exceptions import RequestIdMismatch
from mcipc.rcon.exceptions import WrongPassword
from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.ee import Client as EducationClient
from mcipc.rcon.je import Client as JavaClient
from mcipc.rcon.proto import Client


__all__ = [
    'CLIENTS',
    'LocationNotFound',
    'RequestIdMismatch',
    'WrongPassword',
    'Client',
    'rconcmd'
]


CLIENTS = {
    Edition.BEDROCK: BedrockClient,
    Edition.EDUCATION: EducationClient,
    Edition.JAVA: JavaClient
}
