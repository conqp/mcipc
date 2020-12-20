"""Commands for the Java Edition."""

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
