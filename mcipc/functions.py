"""Common functions."""


__all__ = ['json_serializable']


JSON = (dict, list, float, int, str, bool, type(None))


def get_json_item(instance, index_or_key):
    """Returns the respective item by index or field name."""

    if isinstance(index_or_key, str):
        try:
            value = getattr(instance, index_or_key)
        except AttributeError:
            raise IndexError(index_or_key) from None

        if isinstance(value, JSON):
            return value

        try:
            return dict(value)
        except (TypeError, ValueError):
            return str(value)

    return super().__getitem__(index_or_key)


def json_serializable(cls: type) -> type:
    """Extends a class with methods to return a JSON-ish
    dict when passed to the dict() constructor.
    """

    cls.keys = lambda self: self._fields
    cls.__getitem__ = get_json_item
    return cls
