"""Query client CLI."""

from argparse import ArgumentParser, Namespace
from json import dumps
from logging import DEBUG, INFO, basicConfig, getLogger
from socket import timeout
from sys import exit, stdout    # pylint: disable=W0622
from typing import Tuple

from mcipc.query.exceptions import InvalidConfig
from mcipc.query.client import Client
from mcipc.query.config import Config, servers


__all__ = ['main']


DEFAULT_INDENT = 2 if stdout.isatty() else None
LOGGER = getLogger('queryclt')
LOG_FORMAT = '[%(levelname)s] %(name)s: %(message)s'


def get_args() -> Namespace:
    """Parses and returns the CLI arguments."""

    parser = ArgumentParser(description='A Minecraft Query client.')
    parser.add_argument('server', help='the server to connect to')
    parser.add_argument(
        '-i', '--indent', type=int, default=DEFAULT_INDENT, metavar='int',
        help='indentation for JSON output')
    parser.add_argument(
        '-t', '--timeout', type=float, metavar='seconds',
        help='connection timeout in seconds')
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='print additional debug information')
    subparsers = parser.add_subparsers(dest='action')
    # Basic stats.
    basic_stats_parser = subparsers.add_parser(
        'basic-stats', help='returns basic stats')
    basic_stats_field = basic_stats_parser.add_subparsers(dest='field')
    basic_stats_field.add_parser('motd', help='returns the message of the day')
    basic_stats_field.add_parser('game-type', help='returns the game type')
    basic_stats_field.add_parser('map', help='returns the map name')
    basic_stats_field.add_parser(
        'num-players', help='returns the amount of online players')
    basic_stats_field.add_parser(
        'max-players', help='returns the maximally allowed players')
    basic_stats_field.add_parser(
        'host-port', help='returns the port of the server')
    basic_stats_field.add_parser(
        'host-ip', help='returns the IP address of the server')
    # Full stats.
    full_stats_parser = subparsers.add_parser(
        'full-stats', help='returns full stats')
    full_stats_field = full_stats_parser.add_subparsers(dest='field')
    full_stats_field.add_parser(
        'hostname', help='returns the host name of the server (same as motd)')
    full_stats_field.add_parser('game-type', help='returns the game type')
    full_stats_field.add_parser('game-id', help='returns the game ID')
    full_stats_field.add_parser('version', help='returns the game version')
    full_stats_field.add_parser('plugins', help='returns the plugins in use')
    full_stats_field.add_parser('map', help='returns the map name')
    full_stats_field.add_parser(
        'num-players', help='returns the amount of online players')
    full_stats_field.add_parser(
        'max-players', help='returns the maximally allowed players')
    full_stats_field.add_parser(
        'host-port', help='returns the port of the server')
    full_stats_field.add_parser(
        'host-ip', help='returns the IP address of the server')
    full_stats_field.add_parser(
        'players', help='returns a list of online players')
    # Checks stats.
    check_parser = subparsers.add_parser(
        'check', help='checks for certain conditions')
    check_parser.add_argument(
        '--max-players', type=int, metavar='players',
        help='set upper boundary for online players')
    check_parser.add_argument(
        '--min-players', type=int, metavar='players',
        help='set lower boundary for online players')
    check_parser.add_argument(
        '--players-online', nargs='+', metavar='player',
        help='specify players that must be online')
    check_parser.add_argument(
        '--players-offline', nargs='+', metavar='player',
        help='specify players that must be offline')
    return parser.parse_args()


def get_credentials(server: str) -> Tuple[str, int]:
    """Get the credentials for a server from the respective server name."""

    try:
        return Config.from_string(server)
    except InvalidConfig:
        try:
            return servers()[server]
        except KeyError:
            LOGGER.error('No such server: %s.', server)
            exit(2)


def get_basic_stats(client: Client, args: Namespace):   # pylint: disable=R0911
    """Handles basic stats queries."""

    basic_stats = client.stats(full=False)

    if not args.field:
        return dumps(basic_stats.to_json(), indent=args.indent)

    if args.field == 'motd':
        return basic_stats.motd

    if args.field == 'game-type':
        return basic_stats.game_type

    if args.field == 'map':
        return basic_stats.map

    if args.field == 'num-players':
        return basic_stats.num_players

    if args.field == 'max-players':
        return basic_stats.max_players

    if args.field == 'host-port':
        return basic_stats.host_port

    if args.field == 'host-ip':
        return basic_stats.host_ip

    raise ValueError('Invalid action.')


def get_full_stats(client: Client, args: Namespace):    # pylint: disable=R0911
    """Handles full stats queries."""

    full_stats = client.stats(full=True)

    if not args.field:
        return dumps(full_stats.to_json(), indent=args.indent)

    if args.field == 'hostname':
        return full_stats.host_name

    if args.field == 'game-type':
        return full_stats.game_type

    if args.field == 'game-id':
        return full_stats.game_id

    if args.field == 'version':
        return full_stats.version

    if args.field == 'plugins':
        return dumps(full_stats.plugins, indent=args.indent)

    if args.field == 'map':
        return full_stats.map

    if args.field == 'num-players':
        return full_stats.num_players

    if args.field == 'max-players':
        return full_stats.max_players

    if args.field == 'host-port':
        return full_stats.host_port

    if args.field == 'host-ip':
        return full_stats.host_ip

    if args.field == 'players':
        return dumps(full_stats.players, indent=args.indent)

    raise ValueError('Invalid action.')


def check(client: Client, args: Namespace) -> bool:
    """Checks whether the specified conditions are met."""

    stats = client.stats(full=True)

    if args.max_players is not None and stats.num_players > args.may_players:
        return False

    if args.min_players is not None and stats.num_players < args.min_players:
        return False

    if args.players_online is not None and any(
            player not in stats.players for player in args.players_online):
        return False

    if args.players_offline is not None and any(
            player in stats.players for player in args.players_offline):
        return False

    return True


def main():
    """Runs the RCON client."""

    args = get_args()
    log_level = DEBUG if args.debug else INFO
    basicConfig(level=log_level, format=LOG_FORMAT)
    host, port = get_credentials(args.server)

    try:
        with Client(host, port, timeout=args.timeout) as client:
            if args.action == 'basic-stats':
                print(get_basic_stats(client, args), flush=True)
            elif args.action == 'full-stats':
                print(get_full_stats(client, args), flush=True)
            elif args.action == 'check':
                exit(0 if check(client, args) else 1)
    except KeyboardInterrupt:
        print()
        LOGGER.error('Aborted by user.')
        exit(1)
    except ConnectionRefusedError:
        LOGGER.error('Connection refused.')
        exit(3)
    except timeout:
        LOGGER.error('Connection timeout.')
        exit(4)
