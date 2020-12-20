"""Client for the education edition."""

from mcipc.rcon.be.commands.ability import ability
from mcipc.rcon.be.commands.clear import clear
from mcipc.rcon.be.commands.clone import clone
from mcipc.rcon.be.commands.difficulty import difficulty
from mcipc.rcon.be.commands.effect import effect
from mcipc.rcon.be.commands.enchant import enchant
from mcipc.rcon.be.commands.fill import fill
from mcipc.rcon.be.commands.gamemode import gamemode
from mcipc.rcon.be.commands.give import give
from mcipc.rcon.be.commands.help import help    # pylint: disable=W0622
from mcipc.rcon.be.commands.list import list    # pylint: disable=W0622
from mcipc.rcon.be.commands.locate import locate
from mcipc.rcon.be.commands.mobevent import mobevent
from mcipc.rcon.be.commands.playsound import playsound
from mcipc.rcon.be.commands.replaceitem import replaceitem
from mcipc.rcon.be.commands.setblock import setblock
from mcipc.rcon.be.commands.setmaxplayers import setmaxplayers
from mcipc.rcon.be.commands.setworldspawn import setworldspawn
from mcipc.rcon.be.commands.spawnpoint import spawnpoint
from mcipc.rcon.be.commands.spreadplayers import spreadplayers
from mcipc.rcon.be.commands.stopsound import stopsound
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
from mcipc.rcon.ee.commands.agent import collect
from mcipc.rcon.ee.commands.agent import createagent
from mcipc.rcon.ee.commands.agent import destroy
from mcipc.rcon.ee.commands.agent import detect
from mcipc.rcon.ee.commands.agent import detectredstone
from mcipc.rcon.ee.commands.agent import dropall
from mcipc.rcon.ee.commands.agent import move
from mcipc.rcon.ee.commands.agent import remove
from mcipc.rcon.ee.commands.agent import tpagent
from mcipc.rcon.ee.commands.agent import transfer
from mcipc.rcon.ee.commands.agent import turn
from mcipc.rcon.ee.commands.classroommode import classroommode
from mcipc.rcon.ee.commands.code import code
from mcipc.rcon.ee.commands.geteduclientinfo import geteduclientinfo
from mcipc.rcon.ee.commands.immutableworld import immutableworld
from mcipc.rcon.ee.commands.position import position
from mcipc.rcon.commands.chat import me, say, tell
from mcipc.rcon.commands.execute import execute
from mcipc.rcon.commands.gamerule import gamerule
from mcipc.rcon.commands.kick import kick
from mcipc.rcon.commands.kill import kill
from mcipc.rcon.commands.op import deop, op
from mcipc.rcon.client import Client


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """Client for the Education Edition."""

    ability = ability
    classroommode = classroommode
    clear = clear
    clone = clone
    code = code
    collect = collect
    connect = connect
    createagent = createagent
    deop = deop
    destroy = destroy
    detect = detect
    detectredstone = detectredstone
    difficulty = difficulty
    dropall = dropall
    effect = effect
    enchant = enchant
    execute = property(execute)
    fill = fill
    gamemode = gamemode
    gamerule = gamerule
    geteduclientinfo = geteduclientinfo
    give = give
    help = help
    immutableworld = immutableworld
    kick = kick
    kill = kill
    list = list
    locate = locate
    me = me
    mobevent = mobevent
    move = move
    op = op
    playsound = playsound
    position = position
    remove = remove
    replaceitem = property(replaceitem)
    say = say
    setblock = setblock
    setmaxplayers = setmaxplayers
    setworldspawn = setworldspawn
    spawnpoint = spawnpoint
    spreadplayers = spreadplayers
    stopsound = stopsound
    summon = summon
    teleport = teleport
    tell = msg = w = tell
    testfor = testfor
    testforblock = testforblock
    testforblocks = testforblocks
    tickingarea = property(tickingarea)
    time = property(time)
    title = title
    toggledownfall = toggledownfall
    tpagent = tpagent
    transfer = transfer
    transferserver = transferserver
    turn = turn
    wb = wb
    weather = property(weather)
    worldbuilder = worldbuilder
    wsserver = wsserver
    xp = experience = xp
