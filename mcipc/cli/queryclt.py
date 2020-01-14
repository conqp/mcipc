"""Query client CLI."""

from argparse import ArgumentParser
from json import dumps
from logging import DEBUG, INFO, basicConfig, getLogger
from socket import timeout
from sys import exit    # pylint: disable=W0622

from mcipc.cli.common import get_credentials
from mcipc.config import LOG_FORMAT
from mcipc.query import Client


__all__ = ['main']


LOGGER = getLogger('rconclt')


def get_args():
    """Parses and returns the CLI arguments."""

    parser = ArgumentParser(description='A Minecraft Query client.')
    parser.add_argument('server', help="the server's name")
    parser.add_argument(
        '-i', '--indent', type=int, default=2, help='indentation for JSON')
    parser.add_argument(
        '-t', '--timeout', type=float, help='connection timeout in seconds')
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
    return parser.parse_args()


def basic_stats(client, args):
    """Handles basic stats queries."""

    if not args.field:
        return dumps(client.basic_stats.to_json(), intent=args.indent)

    if args.field == 'motd':
        return client.basic_stats.motd

    if args.action == 'game-type':
        return client.basic_stats.game_type

    if args.action == 'map':
        return client.basic_stats.map

    if args.action == 'num-players':
        return client.basic_stats.num_players

    if args.action == 'max-players':
        return client.basic_stats.max_players

    if args.action == 'host-port':
        return client.basic_stats.host_port

    if args.action == 'host-ip':
        return client.basic_stats.host_ip

    raise ValueError('Invalid action.')


def full_stats(client, args):
    """Handles full stats queries."""

    if not args.field:
        return dumps(client.full_stats.to_json(), intent=args.indent)

    if args.field == 'host-name':
        return client.full_stats.host_name

    if args.action == 'game-type':
        return client.full_stats.game_type

    if args.action == 'game-id':
        return client.full_stats.game_id

    if args.action == 'version':
        return client.full_stats.version

    if args.action == 'plugins':
        return dumps(client.full_stats.plugins, intent=args.indent)

    if args.action == 'map':
        return client.full_stats.map

    if args.action == 'num-players':
        return client.full_stats.num_players

    if args.action == 'max-players':
        return client.full_stats.max_players

    if args.action == 'host-port':
        return client.full_stats.host_port

    if args.action == 'host-ip':
        return client.full_stats.host_ip

    if args.action == 'players':
        return client.full_stats.players

    raise ValueError('Invalid action.')


def main():
    """Runs the RCON client."""

    args = get_args()
    log_level = DEBUG if args.debug else INFO
    basicConfig(level=log_level, format=LOG_FORMAT)
    host, port, _ = get_credentials(
        args.server, require_password=False, logger=LOGGER)

    try:
        with Client(host, port, timeout=args.timeout) as client:
            if args.action == 'basic-stats':
                print(basic_stats(client, args), flush=True)
            elif args.action == 'full-stats':
                print(full_stats(client, args), flush=True)
    except timeout:
        LOGGER.error('Connection timeout.')
        exit(3)
