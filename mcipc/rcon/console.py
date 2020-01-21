"""An interactive console."""

from enum import Enum
from getpass import getpass

from mcipc.rcon.client import Client
from mcipc.rcon.exceptions import InvalidCredentials, RequestIdMismatch


__all__ = ['rconcmd']


PS1 = 'RCON> '
EXIT_COMMANDS = {'exit', 'quit'}


class Message(Enum):
    """Command line interface messages."""

    QUERY_LATER = '\nOkay, I will ask again later.'
    ABORTED = '\nAborted...'
    LOGIN_ABORTED = '\nLogin aborted. Bye.'
    EXIT = 'Bye.'
    SESSION_TIMEOUT = 'Session timed out. Please login again.'
    EXIT_USAGE = 'Usage: {} [<exit_code>].'

    def __str__(self):
        """Returns the string value."""
        return self.value

    def format(self, *args, **kwargs):
        """Formats a message."""
        return str(self).format(*args, **kwargs)


def _read(prompt: str, typ=None):
    """Reads input and converts it to the respective type."""

    while True:
        raw = input(prompt)

        if typ is not None:
            try:
                return typ(raw)
            except (TypeError, ValueError):
                print(f'Invalid {typ}: {raw}.')
                continue

        return raw


def _read_or_none(prompt: str, typ=None):
    """Reads the input and returns None on abort."""

    try:
        return _read(prompt, typ=typ)
    except EOFError:
        print(Message.QUERY_LATER)
        return None


def _login(client: Client, passwd: str):
    """Performs a login."""

    if passwd is None:
        passwd = getpass('Password: ')

    logged_in = False

    while not logged_in:
        try:
            logged_in = client.login(passwd)
        except InvalidCredentials:
            print('Invalid password.')
            passwd = getpass('Password: ')

    return passwd


def _read_args(host: str, port: int, passwd: str, prompt: str) -> tuple:
    """Reads the necessary arguments."""

    while any(item is None for item in (host, port, passwd, prompt)):
        if host is None:
            host = _read_or_none('Host: ')

        if port is None:
            port = _read_or_none('Port: ', typ=int)

        if passwd is None:
            passwd = _read_or_none('Password: ')

        if prompt is None:
            prompt = _read_or_none('Prompt: ')

    return (host, port, passwd, prompt)


def _exit(exit_code=0):
    """Exits the interactive shell via exit command."""

    exit_code = int(exit_code)
    print(Message.EXIT)
    return exit_code


def rconcmd(host: str, port: int, passwd: str, prompt: str = PS1) -> int:
    """Initializes the console."""

    try:
        host, port, passwd, prompt = _read_args(host, port, passwd, prompt)
    except KeyboardInterrupt:
        print(Message.ABORTED)
        return 1

    with Client(host, port) as client:
        try:
            passwd = _login(client, passwd)
        except (EOFError, KeyboardInterrupt):
            print(Message.LOGIN_ABORTED)
            return 1

        while True:
            try:
                command = input(prompt)
            except EOFError:
                print(f'\n{Message.EXIT}')
                break
            except KeyboardInterrupt:
                print()
                continue

            try:
                command, *args = command.split()
            except ValueError:
                continue

            if command in EXIT_COMMANDS:
                try:
                    return _exit(*args)
                except (TypeError, ValueError):
                    print(Message.EXIT_USAGE.format(command))
                    continue

            try:
                result = client.run(command, *args)
            except RequestIdMismatch:
                print(Message.SESSION_TIMEOUT)

                try:
                    passwd = _login(client, passwd)
                except (EOFError, KeyboardInterrupt):
                    print(Message.LOGIN_ABORTED)
                    return 2

            print(result)

    return 0
