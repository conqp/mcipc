"""An interactive console."""

from getpass import getpass

from mcipc.rcon.client import Client
from mcipc.rcon.exceptions import InvalidCredentialsError
from mcipc.rcon.exceptions import RequestIdMismatchError


__all__ = ['rconcmd']


PS1 = 'RCON> '
EXIT_COMMANDS = ('exit', 'quit')


def _read(prompt: str, type_=None):
    """Reads input and converts it to the respective type."""

    while True:
        try:
            raw = input(prompt)
        except EOFError:
            continue

        if type_ is not None:
            try:
                return type_(raw)
            except (TypeError, ValueError):
                print(f'Invalid {type_}: {raw}.')
                continue

        return raw


def _login(client: Client, passwd: str):
    """Performs a login."""

    if passwd is None:
        passwd = getpass('Password: ')

    logged_in = False

    while not logged_in:
        try:
            logged_in = client.login(passwd)
        except InvalidCredentialsError:
            print('Invalid password.')
            passwd = getpass('Password: ')

    return passwd


def rconcmd(host: str = None, port: int = None, passwd: str = None, *,
            prompt: str = PS1) -> int:
    """Initializes the console."""

    if host is None:
        try:
            host = _read('Host: ')
        except KeyboardInterrupt:
            print('\nAborted...')
            return 1

    if port is None:
        try:
            port = _read('Port: ', type_=int)
        except KeyboardInterrupt:
            print('\nAborted...')
            return 1

    with Client(host, port) as client:
        try:
            passwd = _login(client, passwd)
        except (EOFError, KeyboardInterrupt):
            print('\nAborted...')
            return 1

        while True:
            try:
                command = input(prompt)
            except EOFError:
                print('\nAborted.')
                break
            except KeyboardInterrupt:
                print()
                continue

            command, *args = command.split()

            if command in EXIT_COMMANDS:
                break

            try:
                result = client.run(command, *args)
            except RequestIdMismatchError:
                print('Session timed out. Please login again.')

                try:
                    passwd = _login(client, passwd)
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue

            print(result)

    return 0
