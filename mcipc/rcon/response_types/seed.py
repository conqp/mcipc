"""Represents a seed."""

from __future__ import annotations
from re import fullmatch


__all__ = ['Seed']


REGEX = '.*\\[(-?\\d+)\\]'


class Seed(int):
    """A seed value."""

    @classmethod
    def from_response(cls, text: str) -> Seed:
        """Returns a seed from a server response."""
        if (match := fullmatch(REGEX, text)) is None:
            raise ValueError('Unexpected seed response:', text)

        return cls(match.group(1))

    def to_json(self) -> int:
        """Returns the seed as int for JSON serialization."""
        return int(self)
