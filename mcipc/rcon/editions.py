"""Common enumerations."""

from enum import Enum


__all__ = ['Edition']


class Edition(Enum):
    """Represents the several Minecraft editions."""

    BEDROCK = 'Bedrock Edition'
    EDUCATION = 'Education Edition'
    JAVA = 'Java Edition'
