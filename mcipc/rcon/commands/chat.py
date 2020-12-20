"""Chat-realted commands."""

from mcipc.rcon.client import Client


__all__ = ['me', 'say', 'send_url', 'tell', 'tellraw']


def genurl(url: str, text: str) -> dict:
    """Returns a URL message as a JSON-ish dict."""

    return {
        'text': text or url,
        'clickEvent': {
            'action': 'open_url',
            'value': url
        }
    }


def me(self: Client, message: str) -> str:  # pylint: disable=C0103
    """Sends a message from RCON in first-person perspective."""

    return self.run('me', message)


def say(self: Client, message: str) -> str:
    """Broadcast a message to all players."""

    return self.run('say', message)


def tell(self: Client, player: str, message: str) -> str:
    """Whispers a message to the respective player."""

    return self.run('tell', player, message)


def tellraw(self: Client, player: str, obj: dict) -> str:
    """Sends a message represented by a JSON-ish dict."""

    return self.run('tellraw', player, obj)


def send_url(self: Client, player: str, url: str, text: str = None) -> str:
    """Sends a URL to the specified player.
    If no text is specified, it will default to the original URL.
    """

    return tellraw(self, player, genurl(url, text))
