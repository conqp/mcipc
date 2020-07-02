"""An interactive console."""

from getpass import getpass

from mcipc.rcon.client import Client
from mcipc.rcon.exceptions import RequestIdMismatch, WrongPassword


__all__ = ['rconcmd']


EXIT_COMMANDS = {'exit', 'quit'}
MSG_QUERY_LATER = '\nOkay, I will ask again later.'
MSG_ABORTED = '\nAborted...'
MSG_LOGIN_ABORTED = '\nLogin aborted. Bye.'
MSG_EXIT = 'Bye.'
MSG_SESSION_TIMEOUT = 'Session timed out. Please login again.'
MSG_EXIT_USAGE = 'Usage: {} [<exit_code>].'
PS1 = 'RCON> '


def _read(prompt: str, typ: type = None):
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


def _read_or_none(prompt: str, typ: type = None):
    """Reads the input and returns None on abort."""

    try:
        return _read(prompt, typ=typ)
    except EOFError:
        print(MSG_QUERY_LATER)
        return None


def _login(client: Client, passwd: str):
    """Performs a login."""

    if passwd is None:
        passwd = getpass('Password: ')

    logged_in = False

    while not logged_in:
        try:
            logged_in = client.login(passwd)
        except WrongPassword:
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
    print(MSG_EXIT)
    return exit_code


def rconcmd(host: str, port: int, passwd: str, prompt: str = PS1) -> int:
    """Initializes the console."""

    try:
        host, port, passwd, prompt = _read_args(host, port, passwd, prompt)
    except KeyboardInterrupt:
        print(MSG_ABORTED)
        return 1

    with Client(host, port) as client:
        try:
            passwd = _login(client, passwd)
        except (EOFError, KeyboardInterrupt):
            print(MSG_LOGIN_ABORTED)
            return 1

        while True:
            try:
                command = input(prompt)
            except EOFError:
                print(f'\n{MSG_EXIT}')
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
                    print(MSG_EXIT_USAGE.format(command))
                    continue

            try:
                result = client.run(command, *args)
            except RequestIdMismatch:
                print(MSG_SESSION_TIMEOUT)

                try:
                    passwd = _login(client, passwd)
                except (EOFError, KeyboardInterrupt):
                    print(MSG_LOGIN_ABORTED)
                    return 2

            print(result)

    return 0
