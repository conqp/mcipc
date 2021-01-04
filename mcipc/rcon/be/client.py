"""Client implementation for Bedrock Edition."""

from mcipc.rcon.be.commands.ability import ability
from mcipc.rcon.be.commands.camerashake import camerashake
from mcipc.rcon.be.commands.clear import clear
from mcipc.rcon.be.commands.clearspawnpoint import clearspawnpoint
from mcipc.rcon.be.commands.clone import clone
from mcipc.rcon.be.commands.difficulty import difficulty
from mcipc.rcon.be.commands.effect import effect
from mcipc.rcon.be.commands.enchant import enchant
from mcipc.rcon.be.commands.event import event
from mcipc.rcon.be.commands.fill import fill
from mcipc.rcon.be.commands.fog import fog
from mcipc.rcon.be.commands.gamemode import gamemode
from mcipc.rcon.be.commands.give import give
from mcipc.rcon.be.commands.help import help    # pylint: disable=W0622
from mcipc.rcon.be.commands.list import list    # pylint: disable=W0622
from mcipc.rcon.be.commands.locate import locate
from mcipc.rcon.be.commands.mixer import mixer
from mcipc.rcon.be.commands.mobevent import mobevent
from mcipc.rcon.be.commands.music import music
from mcipc.rcon.be.commands.particle import particle
from mcipc.rcon.be.commands.playanimation import playanimation
from mcipc.rcon.be.commands.playsound import playsound
from mcipc.rcon.be.commands.replaceitem import replaceitem
from mcipc.rcon.be.commands.ride import ride
from mcipc.rcon.be.commands.save import save
from mcipc.rcon.be.commands.schedule import schedule
from mcipc.rcon.be.commands.scoreboard import scoreboard
from mcipc.rcon.be.commands.setblock import setblock
from mcipc.rcon.be.commands.setmaxplayers import setmaxplayers
from mcipc.rcon.be.commands.setworldspawn import setworldspawn
from mcipc.rcon.be.commands.spawnpoint import spawnpoint
from mcipc.rcon.be.commands.spreadplayers import spreadplayers
from mcipc.rcon.be.commands.stopsound import stopsound
from mcipc.rcon.be.commands.structure import structure
from mcipc.rcon.be.commands.summon import summon
from mcipc.rcon.be.commands.teleport import teleport
from mcipc.rcon.be.commands.testfor import testfor
from mcipc.rcon.be.commands.testforblock import testforblock
from mcipc.rcon.be.commands.testforblocks import testforblocks
from mcipc.rcon.be.commands.tickingarea import tickingarea
from mcipc.rcon.be.commands.time import time
from mcipc.rcon.be.commands.title import title
from mcipc.rcon.be.commands.toggledownfall import toggledownfall
from mcipc.rcon.be.commands.transferserver import transferserver
from mcipc.rcon.be.commands.weather import weather
from mcipc.rcon.be.commands.worldbuilder import wb, worldbuilder
from mcipc.rcon.be.commands.wsserver import connect, wsserver
from mcipc.rcon.be.commands.xp import xp
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
from mcipc.rcon.client import Client


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """RCON client for the Bedrock Edition."""

    ability = ability
    camerashake = property(camerashake)
    clear = clear
    clearspawnpoint = clearspawnpoint
    clone = clone
    connect = connect
    deop = deop
    difficulty = difficulty
    effect = effect
    enchant = enchant
    event = property(event)
    execute = property(execute)
    fill = fill
    fog = fog
    function = function
    gamemode = gamemode
    gamerule = gamerule
    give = give
    help = help
    kick = kick
    kill = kill
    list = list
    locate = locate
    me = me
    mixer = mixer
    mobevent = mobevent
    music = property(music)
    op = op
    particle = particle
    playanimation = playanimation
    playsound = playsound
    reload = reload
    replaceitem = property(replaceitem)
    ride = ride
    save = save
    say = say
    schedule = property(schedule)
    scoreboard = property(scoreboard)
    send_url = send_url
    setblock = setblock
    setmaxplayers = setmaxplayers
    setworldspawn = setworldspawn
    spawnpoint = spawnpoint
    spreadplayers = spreadplayers
    stopsound = stopsound
    structure = property(structure)
    summon = summon
    tag = tag
    teleport = teleport
    tell = msg = w = tell
    tellraw = tellraw
    testfor = testfor
    testforblock = testforblock
    testforblocks = testforblocks
    tickingarea = property(tickingarea)
    time = property(time)
    title = title
    toggledownfall = toggledownfall
    tp = teleport
    transferserver = transferserver
    wb = wb
    weather = property(weather)
    whitelist = property(whitelist)
    worldbuilder = worldbuilder
    wsserver = wsserver
    xp = experience = xp
