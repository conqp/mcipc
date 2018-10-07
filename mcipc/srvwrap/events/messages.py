"""Exceptions that are internal messages."""


__all__ = ['MsgCancel']


class MsgCancel(Exception):
    """Signals the event handler to cancel the respective subscription."""

    pass
