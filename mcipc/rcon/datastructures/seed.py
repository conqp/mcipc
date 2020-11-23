"""Represents a seed."""

from __future__ import annotations
from re import compile  # pylint: disable=W0622


__all__ = ['Seed']


REGEX = compile('.*\\[(-?\\d+)\\]')


class Seed(int):
    """A seed value."""

    @classmethod
    def from_response(cls, text: str) -> Seed:
        """Returns a seed from a server response."""
        if (match := REGEX.fullmatch(text)) is None:
            raise ValueError('Unexpected seed response:', text)

        return cls(match.group(1))

    def to_json(self) -> int:
        """Returns a JSON-ish dict."""
        return int(self)
