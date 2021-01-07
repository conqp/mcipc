"""Command proxies."""

from contextlib import suppress
from enum import Enum
from functools import wraps
from json import dumps
from re import fullmatch
from typing import Any, Callable, Iterable, Iterator, Tuple


__all__ = [
    'boolmap',
    'ensure_one',
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


def ensure_one(**kwargs: Any) -> Tuple[str, Any]:   # pylint: disable=R1710
    """Ensures that only one argument is set."""

    if sum(value is not None for value in kwargs.values()) != 1:
        raise ValueError('Must specify exactly one of:', kwargs.keys())

    for key, value in kwargs.items():
        if value is not None:
            return (key, value)


def parsed(parser: Callable[[str], Any]) -> Callable[[Callable], Callable]:
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


def str_until_none(*items: Any) -> Iterator[str]:
    """Yields the items converted to str until one item is None."""

    return map(stringify, until_none(items))


def stringify(value: Any) -> str:
    """Yields strings from the given object."""

    if isinstance(value, str):
        return value

    if isinstance(value, (bool, dict, list)):
        return dumps(value)

    if isinstance(value, tuple):
        return ' '.join(map(stringify, value))

    if isinstance(value, Enum) and '__str__' not in type(value).__dict__:
        return stringify(value.value)

    if isinstance(value, range):
        return f'{value[0]}..{value[-1]}'

    return str(value)


def until_none(items: Iterable[Any]) -> Iterator[Any]:
    """Yields items until one item is None."""

    for item in items:
        if item is None:
            break

        yield item
