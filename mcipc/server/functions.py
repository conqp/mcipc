"""Common functions."""


__all__ = ['rshift']


def rshift(integer: int, shift: int) -> int:
    """Logical right binary shift."""

    if integer >= 0:
        return integer >> shift

    return (integer + 0x100000000) >> shift
