"""Exceptions."""

__all__ = ['CallbackExistsError']


class CallbackExistsError(Exception):
    """Indicates that an eponymous callback is already registered."""

    pass
