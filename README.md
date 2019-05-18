# mcipc

A Minecraft inter-process communication API implementing the [RCON](http://wiki.vg/RCON) and [Query](http://wiki.vg/Query) protocols.

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
* `host_ip`: The server's IP address (`ipaddress.IPv4Address`).

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
* `host_ip`: The server's IP address (`ipaddress.IPv4Address`).
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

## Scripts
This library also ships a couple of scripts intended as a proof-of-concept.

* `rconclt`: An `RCON` client.
* `rconshell`: An interactive `RCON` shell.

### `rconclt`
The script `rconclt` is an RCON client script to communicate with minecraft servers using the shell.  
To invoke a pre-defined server configuration (see below):

    rconclt my_server <command> [<args>...] [options]

## Configuration
`rconclt` can be configured in `/etc/mcipc.d/rcon.conf`:

    [my_server]
    host = 127.0.0.1
    port = 5000
    passwd = mysecretpassword

The `passwd` entry is optional.

## License
Copyright (C) 2018 Richard Neumann <mail at richard dash neumann period de>

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
