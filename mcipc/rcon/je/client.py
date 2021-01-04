"""Client implementation for Java Edition."""

from mcipc.rcon.client import Client
from mcipc.rcon.commands.chat import me, say, tell, tellraw, send_url
from mcipc.rcon.commands.execute import execute
from mcipc.rcon.commands.function import function
from mcipc.rcon.commands.gamerule import gamerule
from mcipc.rcon.commands.kick import kick
from mcipc.rcon.commands.kill import kill
from mcipc.rcon.commands.op import deop, op
from mcipc.rcon.commands.reload import reload
from mcipc.rcon.commands.tag import tag
from mcipc.rcon.commands.whitelist import whitelist
from mcipc.rcon.errors import check_result
from mcipc.rcon.je.commands.advancement import advancement
from mcipc.rcon.je.commands.attribute import attribute
from mcipc.rcon.je.commands.ban import ban, ban_ip, banlist, pardon
from mcipc.rcon.je.commands.bossbar import bossbar
from mcipc.rcon.je.commands.clear import clear
from mcipc.rcon.je.commands.clone import clone
from mcipc.rcon.je.commands.data import data
from mcipc.rcon.je.commands.datapack import datapack
from mcipc.rcon.je.commands.debug import debug
from mcipc.rcon.je.commands.defaultgamemode import defaultgamemode
from mcipc.rcon.je.commands.difficulty import difficulty
from mcipc.rcon.je.commands.effect import effect
from mcipc.rcon.je.commands.enchant import enchant
from mcipc.rcon.je.commands.experience import experience, xp
from mcipc.rcon.je.commands.fill import fill
from mcipc.rcon.je.commands.forceload import forceload
from mcipc.rcon.je.commands.gamemode import gamemode
from mcipc.rcon.je.commands.give import give
from mcipc.rcon.je.commands.help import help    # pylint: disable=W0622
from mcipc.rcon.je.commands.item import item
from mcipc.rcon.je.commands.list import list    # pylint: disable=W0622
from mcipc.rcon.je.commands.locate import locate
from mcipc.rcon.je.commands.locatebiome import locatebiome
from mcipc.rcon.je.commands.loot import loot
from mcipc.rcon.je.commands.particle import particle
from mcipc.rcon.je.commands.playsound import playsound
from mcipc.rcon.je.commands.publish import publish
from mcipc.rcon.je.commands.recipe import recipe
from mcipc.rcon.je.commands.replaceitem import replaceitem
from mcipc.rcon.je.commands.save import save_all, save_off, save_on
from mcipc.rcon.je.commands.schedule import schedule
from mcipc.rcon.je.commands.scoreboard import scoreboard
from mcipc.rcon.je.commands.seed import seed
from mcipc.rcon.je.commands.setblock import setblock
from mcipc.rcon.je.commands.setidletimeout import setidletimeout
from mcipc.rcon.je.commands.setworldspawn import setworldspawn
from mcipc.rcon.je.commands.spawnpoint import spawnpoint
from mcipc.rcon.je.commands.spectate import spectate
from mcipc.rcon.je.commands.spreadplayers import spreadplayers
from mcipc.rcon.je.commands.stop import stop
from mcipc.rcon.je.commands.stopsound import stopsound
from mcipc.rcon.je.commands.summon import summon
from mcipc.rcon.je.commands.team import team
from mcipc.rcon.je.commands.teammsg import teammsg, tm
from mcipc.rcon.je.commands.teleport import teleport
from mcipc.rcon.je.commands.time import time
from mcipc.rcon.je.commands.title import title
from mcipc.rcon.je.commands.trigger import trigger
from mcipc.rcon.je.commands.weather import weather
from mcipc.rcon.je.commands.worldborder import worldborder


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """A high-level RCON client with methods for the Java Edition."""

    # pylint: disable=W0221
    def run(self, command: str, *arguments: str) -> str:
        """Runs a command and checks the return value for errors."""
        return check_result(super().run(command, *arguments))

    advancement = property(advancement)
    attribute = attribute
    ban = ban
    ban_ip = ban_ip
    banlist = banlist
    bossbar = property(bossbar)
    clear = clear
    clone = clone
    data = property(data)
    datapack = property(datapack)
    debug = debug
    defaultgamemode = defaultgamemode
    deop = deop
    difficulty = difficulty
    effect = property(effect)
    enchant = enchant
    execute = property(execute)
    experience = experience
    fill = fill
    forceload = property(forceload)
    function = function
    gamemode = gamemode
    gamerule = gamerule
    give = give
    help = help
    item = property(item)
    kick = kick
    kill = kill
    list = list
    locate = locate
    locatebiome = locatebiome
    loot = property(loot)
    me = me
    op = op
    pardon = pardon
    particle = particle
    players = property(list)
    playsound = playsound
    publish = publish
    recipe = property(recipe)
    reload = reload
    replaceitem = property(replaceitem)
    save_all = save_all
    save_off = save_off
    save_on = save_on
    say = say
    schedule = property(schedule)
    scoreboard = property(scoreboard)
    seed = property(seed)
    send_url = send_url
    setblock = setblock
    setidletimeout = setidletimeout
    setworldspawn = setworldspawn
    spawnpoint = spawnpoint
    spectate = spectate
    spreadplayers = spreadplayers
    stop = stop
    stopsound = stopsound
    summon = summon
    tag = tag
    team = property(team)
    teammsg = teammsg
    teleport = teleport
    tell = msg = w = tell
    tellraw = tellraw
    time = property(time)
    title = title
    tm = tm
    trigger = property(trigger)
    weather = property(weather)
    whitelist = property(whitelist)
    worldborder = property(worldborder)
    xp = xp
