"""Command proxies."""

from contextlib import suppress
from enum import Enum
from functools import wraps
from json import dumps
from re import fullmatch
from typing import Callable, Iterable, Iterator

from mcipc.rcon.types import IntRange


__all__ = [
    'boolmap',
    'int_range_to_str',
    'parsed',
    'str_until_none',
    'stringify',
    'until_none'
]


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


def int_range_to_str(int_range: IntRange) -> str:
    """Returns a string for the Minecraft server."""

    start, end = int_range

    if start == end:
        if start is not None:
            return str(start)

        raise ValueError('Either start or end need to be specified.')

    return '..'.join(map(lambda i: '' if i is None else str(i), int_range))


def parsed(parser: Callable[[str], type]) -> Callable[[Callable], Callable]:
    """Updates a function to parse its result with a parser."""

    def decorator(function: Callable) -> Callable:
        """Decorator that wraps the function and updates its return type."""
        @wraps(function)
        def inner(*args, **kwargs):
            """Wrapper function thats parses the function's return value."""
            return parser(function(*args, **kwargs))

        try:
            annotations = parser.__annotations__
        except AttributeError:
            inner.__annotations__['return'] = parser
        else:
            with suppress(KeyError):
                inner.__annotations__['return'] = annotations['return']

        return inner

    return decorator


def str_until_none(*items: object) -> Iterator[str]:
    """Yields the items converted to str until one item is None."""

    return map(stringify, until_none(items))


def stringify(value: type) -> str:
    """Yields strings from the given object."""

    if isinstance(value, str):
        return value

    if isinstance(value, (bool, dict, list)):
        return dumps(value)

    if isinstance(value, tuple):
        return ' '.join(map(stringify, value))

    if isinstance(value, Enum):
        return stringify(value.value)

    return str(value)


def until_none(items: Iterable[type]) -> Iterator[type]:
    """Yields items until one item is None."""

    for item in items:
        if item is None:
            break

        yield item
