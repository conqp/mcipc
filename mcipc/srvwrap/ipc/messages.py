"""IPC messages."""

from json import loads, dumps


__all__ = ['IPCCommand', 'IPCResponse']


class JSON:
    """A JSON de-/serializable object."""

    def __str__(self):
        """Returns a JSON string."""
        return dumps(self.to_json())

    def __bytes__(self):
        """Returns JSON bytes."""
        return str(self).encode()

    @classmethod
    def from_json(cls, json):
        """Returns an instance from a JSON-ish dict."""
        raise NotImplementedError()

    @classmethod
    def from_string(cls, string):
        """Returns an instance from a JSON string."""
        return cls.from_json(loads(string))

    @classmethod
    def from_bytes(cls, bytes_):
        """Returns an instance from JSON bytes."""
        return cls.from_string(bytes_.decode())

    def to_json(self):
        """Returns a JSON-ish dict."""
        raise NotImplementedError()


class IPCCommand(JSON):
    """An IPC command."""

    __slots__ = ('command', 'args', 'regex', 'timeout')

    def __init__(self, command, *args, regex=None, timeout=3):
        """Sets command, arguments, regex and timeout."""
        self.command = command
        self.args = args
        self.regex = regex
        self.timeout = timeout

    @classmethod
    def from_json(cls, json):
        """Returns an instance from a JSON-ish dict."""
        return cls(
            json['command'], json.get('args', ()), regex=json.get('regex'),
            timeout=json.get('timeout', 3))

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {
            'command': self.command,
            'args': self.args,
            'regex': self.regex,
            'timeout': self.timeout}


class IPCResponse(JSON):
    """An IPC response."""

    __slots__ = ('message', 'code')

    def __init__(self, message, code=0):
        """Sets command, arguments, regex and timeout."""
        self.message = message
        self.code = code

    @classmethod
    def from_json(cls, json):
        """Returns an instance from a JSON-ish dict."""
        return cls(json['message'], code=json.get('code', 0))

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {'message': self.message, 'code': self.code}
