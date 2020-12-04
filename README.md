# mcipc
A Minecraft inter-process communication API implementing the [RCON](http://wiki.vg/RCON) and [Query](http://wiki.vg/Query) protocols.

## Requirements
[![Build Status](https://travis-ci.com/conqp/mcipc.svg?branch=master)](https://travis-ci.com/conqp/mcipc)  
`mcipc` requires Python 3.8 or higher.

## Documentation
[![Documentation Status](https://readthedocs.org/projects/mcipc/badge/?version=latest)](https://mcipc.readthedocs.io/en/latest/?badge=latest)  
Documentation is available on [readthedocs](https://mcipc.readthedocs.io/en/latest).

## Quick start

Install mcipc from the [AUR](https://aur.archlinux.org/packages/python-mcipc/) or via:

    pip install mcipc

### Query protocol
The `Query` protcol is used to query a Minecraft server for server information.  
The Minecraft query protocol has two query modes: *basic stats* and *full stats*.

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        basic_stats = client.basic_stats

    print(basic_stats)  # Get basic stats.
    print(full_stats)   # Get full stats.

### RCON protocol
The `RCON` protocol is used to remotely control a Minecraft server, i.e. execute
commands on a Minecraft server and receive the respective results.

    from mcipc.rcon import Client

    with Client('127.0.0.1', 5000) as client:
        client.login('mysecretpassword')    # Perform initial login.
        seed = client.seed                  # Get the server's seed.
        players = client.players            # Get the server's players info.
        mansion = client.locate('Mansion')  # Get the next mansion's location.

    print(seed)
    print(players)
    print(mansion)

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
