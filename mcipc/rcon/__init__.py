"""RCON client library."""

from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.editions import Edition
from mcipc.rcon.ee import Client as EducationClient
from mcipc.rcon.je import Client as JavaClient


__all__ = [
    'CLIENTS',
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
