"""Common functions."""


__all__ = ['rshift']


def rshift(integer, shift):
    """Logical right binary shift."""

    if integer >= 0:
        return integer >> shift

    return (integer + 0x100000000) >> shift
