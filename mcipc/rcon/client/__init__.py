"""RCON client implementations."""

from mcipc.enumerations import Edition
from mcipc.rcon.client.bedrock import Client as BedrockClient
from mcipc.rcon.client.education import Client as EducationClient
from mcipc.rcon.client.java import Client as JavaClient


__all__ = ['CLIENTS', 'BedrockClient', 'EducationClient', 'JavaClient']


CLIENTS = {
    Edition.BEDROCK: BedrockClient,
    Edition.EDUCATION: EducationClient,
    Edition.JAVA: JavaClient
}
