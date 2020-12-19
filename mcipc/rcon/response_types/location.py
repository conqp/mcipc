"""Locations."""

from __future__ import annotations
from typing import NamedTuple, Union


__all__ = ['Location']


class Location(NamedTuple):
    """A 3D location."""

    name: str
    x: int
    y: Union[int, None]
    z: int
    distance: int

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'name': self.name,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'distance': self.distance
        }
