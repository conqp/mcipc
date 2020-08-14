# mcipc

A Minecraft inter-process communication API implementing the [RCON](http://wiki.vg/RCON) and [Query](http://wiki.vg/Query) protocols.

## Requirements
`mcipc` requires Python 3.8 or higher.

## Usage

### Query protocol
The `Query` protcol is used to query a Minecraft server for server information.  
The Minecraft query protocol has two query modes: *basic stats* and *full stats*.

#### Basic stats
To get *basic stats* from a Minecraft server, it must enable the `Query` protocol.  
You can enable the query protocol on a Minecraft server by setting `enable-query = true` in the server's `server.properties` file.
To specify a deviating port, you can set `query.port = <port>` in the same file.  
The following example assumes a server running on `127.0.0.1` and on the default query port `25565`:

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        basic_stats = client.basic_stats

    print(basic_stats)

The type of `basic_stats` is a named tuple with the following properties:

* `type`: The packet type (`Type`, protocol information).
* `session_id`: The query's session ID (`int`, protocol information).
* `motd`: The server's message of the day (`str`).
* `game_type`: The game type (`str`).
* `map`: The current map (`str`).
* `num_players`: The amount of online players (`int`).
* `max_players`: The amount of maximally allowed players (`int`).
* `host_port`: The server's port (`int`).
* `host_ip`: The server's IP address or hostname (`ipaddress.IPv4Address` or `ipaddress.IPv6Address` or `str`).

#### Full stats
For retrieving full stats of a server, the same premises apply.

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        full_stats = client.full_stats

    print(full_stats)

The type of `full_stats` is a named tuple with the following properties:

* `type`: The packet type (`Type`, protocol information).
* `session_id`: The query's session ID (`int`, protocol information).
* `host_name`: The server's message of the day (`str`, same as BasicStats.motd).
* `game_type`: The game type (`str`).
* `game_id`: The game ID (`str`).
* `version`: The game version (`str`).
* `plugins`: The used plugins (`dict`).
* `map`: The current map (`str`).
* `num_players`: The amount of online players (`int`).
* `max_players`: The amount of maximally allowed players (`int`).
* `host_port`: The server's port (`int`).
* `host_ip`: The server's IP address or hostname (`ipaddress.IPv4Address` or `ipaddress.IPv6Address` or `str`).
* `players`: The names of online players (`tuple` of `str`).

### RCON protocol
The `RCON` protocol is used to remotely control a Minecraft server, i.e. execute
commands on a Minecraft server and receive the respective results.  
To enable `RCON` on a Minecraft server, you must set `enable-rcon = true` in the
server's `server.properties` file.
Furthermore, you need to specify a port for the RCON server by setting `rcon.port = <port>`
and a password by setting `rcon.password = <password>` in the same file.  
The following example assumes a server running on `127.0.0.1` and on the RCON port `5000` with password `'mysecretpassword'`:

    from mcipc.rcon import Client

    with Client('127.0.0.1', 5000) as client:
        client.login('mysecretpassword')    # Perform initial login.
        seed = client.seed                  # Get the server's seed.
        players = client.players            # Get the server's players info.
        mansion = client.locate('Mansion')  # Get the next mansion's location.

    print(seed)
    print(players)
    print(mansion)


The type of `seed` is `Seed` which is derived from `int` and can be used just like the latter.  
The type of `players` is `Players`, a named tuple:

* `online`: The amount of online players (`int`).
* `max`: The amount of maximally allowed players (`int`).
* `names`: The names of online players (`tuple` of `str`).

The type of `mansion` is `Location` which describes the x-y-z location of the next located object.

* `x`: x-coordinate (`int`).
* `y`: y-coordinate (`int` or `None`).
* `z`: z-coordinate (`int`).

*HINT:* The y-component of a location may be `None`, which represents the special Minectaft vector component `'~'`.

### Available client commands
For a full documentation of available client commands, please refer to

    help(Client)
    
within an interactive python shell.

### Handling connection timeouts.
Since version 1.2.1, you can specify an optional `timeout=<sec>` parameter on both `Query` and `RCON` clients.  
If a timeout is reached during a connection attempt, it will raise a `socket.timeout` exception.  
The following example will raise a connection timeout after 1.5 seconds:

    try:
        with Client('127.0.0.1', 5000, timeout=1.5) as client:
            <do_stuff>
    except socket.timeout as timeout:
        <handle_connection_timeout>

## Scripts
This library also ships a couple of scripts intended as a proof-of-concept.

* `queryclt`: A `Query` client.
* `rconclt`: An `RCON` client.
* `rconshell`: An interactive `RCON` shell.

### `queryclt`
`queryclt` is a Query client script to communicate with minecraft servers via the Query protocol using the shell.  
To communicate with a server, run:

    queryclt <server> <stats_type> [<args>...] [options]

The placeholder `<server>` can either be a pre-defined server's name (see [below](#Configuration)) or server socket identified by `<host>:<port>`.

### `rconclt`
`rconclt` is an RCON client script to communicate with minecraft servers via the RCON protocol using the shell.  
To communicate with a server, run:

    rconclt <server> <command> [<args>...] [options]
    
The placeholder `<server>` can either be a pre-defined server's name (see [below](#Configuration)) or server socket identified by `[<password>@]<host>:<port>`.\
If no password was specified in either the pre-defined server entry or the server socket, the script will interactively ask for the server's password.

## Configuration
`queryclt` servers can be configured in `/etc/mcipc.d/query.conf`.\
`rconclt` servers can be configured in `/etc/mcipc.d/rcon.conf`.\
The configuration file format is:

    [<server_name>]
    host = <hostname_or_ip_address>
    port = <port>
    passwd = <password>

The `passwd` entry is optional for `rcon.conf` and unnecessary for `query.conf`.

## License
Copyright (C) 2018-2020 Richard Neumann <mail at richard dash neumann period de>

mcipc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

mcipc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with mcipc.  If not, see <http://www.gnu.org/licenses/>.


## Legal
Minecraft content and materials are trademarks and copyrights of
Mojang and its licensors. All rights reserved.
This program is free software and is not affiliated with Mojang.
