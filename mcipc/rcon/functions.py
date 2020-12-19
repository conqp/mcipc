"""Command proxies."""

from __future__ import annotations
from enum import Enum
from json import dumps
from re import fullmatch
from typing import Callable, Dict, Generator, Iterable, Iterator


__all__ = [
    'attributes',
    'boolmap',
    'str_until_none',
    'stringify',
    'until_none'
]


def attributes(attribute_map: Dict[str, Callable]) -> Callable[type, type]:
    """Decorator factory."""

    def decorator(cls: type) -> type:
        """Decorates the respective class."""
        for key, value in attribute_map.items():
            if hasattr(cls, key):
                raise ValueError(f'{cls} already has an attribute "{key}".')

            setattr(cls, key, value)

        return cls

    return decorator


def boolmap(text: str, true: str = None, false: str = None, *,
            default: bool = None) -> bool:
    """Parses a boolean value from a text with the given regex strings."""

    if true is not None and fullmatch(true, text) is not None:
        return True

    if false is not None and fullmatch(false, text) is not None:
        return False

    if default is None:
        raise ValueError(f'Unexpected text returned: {text}')

    return default


def str_until_none(*items: object) -> Iterator[str]:
    """Yields the items converted to str until one item is None."""

    return map(stringify, until_none(items))


def stringify(value: type) -> str:
    """Yields strings from the given object."""

    if isinstance(value, str):
        return value

    if isinstance(value, bool):
        return 'true' if value else 'false'

    if isinstance(value, dict):
        return dumps(value)

    if isinstance(value, (list, tuple)):
        return ' '.join(map(stringify, value))

    if isinstance(value, Enum):
        return stringify(value.value)

    return str(value)


def until_none(items: Iterable[type]) -> Generator[type, None, None]:
    """Yields items until one item is None."""

    for item in items:
        if item is None:
            break

        yield item
