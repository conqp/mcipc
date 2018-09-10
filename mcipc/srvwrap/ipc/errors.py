"""IPC error messages."""

from enum import Enum
from json import loads, dumps


__all__ = ['IPCError']


class IPCError(Exception, Enum):
    """A generic IPC error."""

    INVALID_UNICODE = ('Invalid unicode.', 1)
    INVALID_JSON = ('Invalid JSON.', 2)
    NO_RESPONSE = ('No response retrieved from server.', 3)

    def __init__(self, message, code):
        """Sets message and code."""
        Exception.__init__(self)
        self.message = message
        self.code = code

    def __str__(self):
        """Returns the error as string."""
        return dumps(self.to_json())

    def __bytes__(self):
        """Returns the error as bytes."""
        return str(self).encode()

    @classmethod
    def from_json(cls, json):
        """Returns an instance from a JSON-ish dict."""
        return cls(json['message'], json['code'])

    @classmethod
    def from_string(cls, string):
        """Returns an instance from the respective string."""
        return cls.from_json(loads(string))

    @classmethod
    def from_bytes(cls, bytes_):
        """Returns an instance from the respective bytes."""
        return cls.from_string(bytes_.decode())

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {'message': self.message, 'code': self.code}
