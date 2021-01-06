"""Common functions."""


__all__ = ['dictmodel']


def _getitem(instance, index_or_key):
    """Returns the respective item by index or field name."""

    if isinstance(index_or_key, str):
        try:
            return getattr(instance, index_or_key)
        except AttributeError:
            raise IndexError(index_or_key) from None

    return super().__getitem__(index_or_key)


def dictmodel(cls: type):
    """Extends a class with methods for the dict constructor."""

    cls.keys = lambda self: self._fields
    cls.__getitem__ = _getitem
    return cls
