"""Named binary tags."""

from typing import Union

from mcipc.rcon.enumerations import Item, TargetSelector
from mcipc.rcon.functions import stringify


__all__ = ['NBT']


TargetType = Union[Item, TargetSelector, str]


class NBT:
    """Represents a named binary tag."""

    __slots__ = ('target', 'tags')

    def __init__(self, target: TargetType, **tags):
        """Stores the object name and optional tags."""
        self.target = target
        self.tags = tags

    def __repr__(self):
        """Returns a str representation for eval()."""
        items = ', '.join(f'{key}={val!r}' for key, val in self.tags.items())
        return f'{type(self).__name__}({self.target!r}, {items})'

    def __str__(self):
        """Returns a str representation for RCON."""
        items = ', '.join(
            f'{key}={stringify(val)}' for key, val in self.tags.items())
        return f'{self.target}[{items}]'
