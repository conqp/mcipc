"""Common functions."""

from enum import Enum
from typing import Any, Union


__all__ = ['json_serializable']


JSON = Union[dict, list, float, int, str, bool, None]


def jsonify(value: Any) -> JSON:    # pylint: disable=R0911
    """Converts a value into a JSON-compliant value."""

    if value is None:
        return None

    if isinstance(value, dict):
        return {key: jsonify(value) for key, value in value.items()}

    if isinstance(value, list):
        return [jsonify(item) for item in value]

    if isinstance(value, (float, int, str, bool)):
        return value

    if isinstance(value, Enum):
        return jsonify(value.value)

    try:
        value = dict(value)
    except (TypeError, ValueError):
        return str(value)

    return {key: jsonify(value) for key, value in value.items()}


def get_json_item(instance: type, index_or_key: Union[int, str]) -> Any:
    """Returns the respective item by index or field name.
    In the case of a field name, the item will be converted
    into a JSON-ish value.
    """

    if isinstance(index_or_key, str):
        try:
            value = getattr(instance, index_or_key)
        except AttributeError:
            raise IndexError(index_or_key) from None

        return jsonify(value)

    return super().__getitem__(index_or_key)


def json_serializable(cls: type) -> type:
    """Extends a NamedTuple with methods to return a JSON-ish
    dict when passed to the dict() constructor.
    """

    if not hasattr(cls, 'keys'):
        if not (issubclass(cls, tuple) and hasattr(cls, '_fields')):
            raise TypeError('Type does not implement method keys(self):', cls)

        cls.keys = lambda self: self._fields

    cls.__getitem__ = get_json_item
    return cls
