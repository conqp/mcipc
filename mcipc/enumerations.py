"""Common enumerations."""

from __future__ import annotations
from enum import Enum


__all__ = ['Edition']


class Edition(Enum):
    """Represents the several Minecraft editions."""

    BEDROCK = 'Bedrock Edition'
    EDUCATION = 'Education Edition'
    JAVA = 'Java Edition'

    def __str__(self):  # pylint: disable=E0307
        return self.value

    @classmethod
    def from_string(cls, string: str) -> Edition:
        """Creates an edition from a string."""
        try:
            return cls(string)
        except ValueError:
            return cls[string.upper()]
