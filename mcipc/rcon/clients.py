"""Available RCON clients."""

from mcipc.enumerations import Edition
from mcipc.rcon.be import Client as BedrockClient
from mcipc.rcon.ee import Client as EducationClient
from mcipc.rcon.je import Client as JavaClient


__all__ = ['CLIENTS']


CLIENTS = {
    Edition.BEDROCK: BedrockClient,
    Edition.EDUCATION: EducationClient,
    Edition.JAVA: JavaClient
}
