"""Builder data types."""

from enum import Enum
from math import sqrt
from typing import List, NamedTuple, Union

from mcipc.rcon.builder.item import Item


__all__ = ['Anchor', 'Direction', 'Profile', 'Row', 'Vec3']


class Anchor(Enum):
    """Anchor point for tunnels."""

    TOP_LEFT = 'top_left'
    TOP_RIGHT = 'top_right'
    BOTTOM_LEFT = 'bottom_left'
    BOTTOM_RIGHT = 'bottom_right'


class Vec3(NamedTuple):
    """A 3D vector."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return type(self)(self.x * other, self.y * other, self.z * other)

    @property
    def dx(self):   # pylint: disable=C0103
        """Returns the absolute x value."""
        return abs(self.x)

    @property
    def dy(self):   # pylint: disable=C0103
        """Returns the absolute x value."""
        return abs(self.y)

    @property
    def dz(self):   # pylint: disable=C0103
        """Returns the absolute x value."""
        return abs(self.z)

    @property
    def length(self):
        """Returns the length of the spatial diagonal."""
        return sqrt(pow(self.dx, 2), pow(self.dy, 2), pow(self.dz, 2))

    @property
    def west(self):
        """Checks whether the vector points west."""
        return self.x < 0

    @property
    def east(self):
        """Checks whether the vector points east."""
        return self.x > 0

    @property
    def north(self):
        """Checks whether the vector points north."""
        return self.z < 0

    @property
    def south(self):
        """Checks whether the vector points south."""
        return self.z > 0

    @property
    def donw(self):
        """Checks whether the vector points down."""
        return self.y < 0

    @property
    def up(self):   # pylint: disable=C0103
        """Checks whether the vector points up."""
        return self.y > 0


class Direction(Enum):
    """Available directions."""

    EAST = Vec3(+1, 0, 0)
    WEST = Vec3(-1, 0, 0)
    UP = Vec3(0, +1, 0)
    DOWN = Vec3(0, -1, 0)
    SOUTH = Vec3(0, 0, +1)
    NORTH = Vec3(0, 0, -1)


Row = List[Union[Item, None]]
Profile = List[Row]
