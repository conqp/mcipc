[![Documentation Status](https://readthedocs.org/projects/mcipc/badge/?version=latest)](https://mcipc.readthedocs.io/en/latest/?badge=latest)
[![Bugs](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=bugs)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Code Smells](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=code_smells)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Lines of Code](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=ncloc)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Maintainability Rating](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=sqale_rating)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Quality Gate Status](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=alert_status)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Reliability Rating](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=reliability_rating)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Security Rating](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=security_rating)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Technical Debt](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=sqale_index)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)
[![Vulnerabilities](https://sonarqube.richard-neumann.de/api/project_badges/measure?project=mcipc&metric=vulnerabilities)](https://sonarqube.richard-neumann.de/dashboard?id=mcipc)

# mcipc
A Minecraft inter-process communication API implementing the [RCON](http://wiki.vg/RCON) and [Query](http://wiki.vg/Query) protocols.

## News

### 2020-12-21 - mcipc-2.0
Great news: `mcipc` is now available in version 2.  
The version 2 update includes the outsourcing of the RCON protocol and client implementation into an [own project](https://github.com/conqp/rcon).  
This allowes for the RCON library to be used independently of mcipc, e.g. for other games which support the RCON protocol.  
Furthermore `mcipc`'s RCON client implementations have been overhauled. They now provide functions to interact with the respective server.  
It was therefor necessary to not have one implementation of `mcipc.rcon.Client`, but three:

*  `mcipc.rcon.be.Client` Client for Bedrock Edition servers.
*  `mcipc.rcon.ee.Client` Client for Education Edition servers.
*  `mcipc.rcon.je.Client` Client for Java Edition servers.

To provide some backwards compatibility, the `mcipc.rcon.Client` is now an alias for `mcipc.rcon.je.Client`.  
You'll find a full documentation of each client's capabilities, i.e. methods in the [documentation](https://mcipc.readthedocs.io/en/latest).

## Requirements
`mcipc` requires Python 3.8 or higher.  
It also depends on [rcon](https://github.com/conqp/rcon) which has been split from this project.  
If you install `mcicp` via `pip`, it will automatically be installed as a dependency.

## Documentation
Documentation is available on [readthedocs](https://mcipc.readthedocs.io/en/latest).

## Quick start

Install mcipc from the [AUR](https://aur.archlinux.org/packages/python-mcipc/) or via:

    pip install mcipc

### Query protocol
The `Query` protcol is used to query a Minecraft server for server information.  
The Minecraft query protocol has two query modes: *basic stats* and *full stats*.

```python
from mcipc.query import Client

with Client('127.0.0.1', 25565) as client:
    basic_stats = client.stats()            # Get basic stats.
    full_stats = client.stats(full=True)    # Get full stats.

print(basic_stats)
print(full_stats)
```

### RCON protocol
The `RCON` protocol is used to remotely control a Minecraft server, i.e. execute
commands on a Minecraft server and receive the respective results.

```python
from mcipc.rcon.je import Biome, Client     # For Java Edition servers.
#from mcipc.rcon.be import Client           # For Bedrock Edition servers.
#from mcipc.rcon.ee import Client           # For Education Edition servers.

with Client('127.0.0.1', 5000, passwd='mysecretpassword') as client:
    seed = client.seed                              # Get the server's seed.
    players = client.list()                         # Get the server's players info.
    mansion = client.locate('mansion')              # Get the next mansion's location.
    badlands = client.locatebiome(Biome.BADLANDS)   # Get the next location of a badlands biome.

print(seed)
print(players)
print(mansion)
print(badlands)
```

Example output of the above commands with a Java Edition client:

```python
-8217057902979500137
Players(online=1, max=20, players=[Player(name='coNQP', uuid=None, state=None)])
Location(name='mansion', x=-7216, y=None, z=-1952, distance=7479)
Location(name='minecraft:badlands', x=1512, y=None, z=3388, distance=3634)
```

## Credits
Many thanks to all contributers to the [Minecraft Wiki](https://minecraft.gamepedia.com/) and the [Wiki.vg](https://wiki.vg/Main_Page).

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
