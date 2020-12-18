"""Implementations of Minecraft commands for RCON."""

from mcipc.rcon.commands.ability import ability
from mcipc.rcon.commands.advancement import advancement
from mcipc.rcon.commands.agent import collect
from mcipc.rcon.commands.agent import createagent
from mcipc.rcon.commands.agent import destroy
from mcipc.rcon.commands.agent import detect
from mcipc.rcon.commands.agent import detectredstone
from mcipc.rcon.commands.agent import dropall
from mcipc.rcon.commands.agent import move
from mcipc.rcon.commands.agent import remove
from mcipc.rcon.commands.agent import tpagent
from mcipc.rcon.commands.agent import transfer
from mcipc.rcon.commands.agent import turn
from mcipc.rcon.commands.attribute import attribute
from mcipc.rcon.commands.ban import ban, ban_ip, banlist, kick, pardon
from mcipc.rcon.commands.bossbar import bossbar
from mcipc.rcon.commands.camerashake import camerashake
from mcipc.rcon.commands.chat import me, tell, say, tellraw, send_url
from mcipc.rcon.commands.classroommode import classroommode
from mcipc.rcon.commands.clear import clear_be, clear_je
from mcipc.rcon.commands.clone import clone_be, clone_je
from mcipc.rcon.commands.data import data
from mcipc.rcon.commands.datapack import datapack
from mcipc.rcon.commands.debug import debug
from mcipc.rcon.commands.difficulty import difficulty
from mcipc.rcon.commands.effect import effect_be, effect_je
from mcipc.rcon.commands.enchant import enchant
from mcipc.rcon.commands.event import event
from mcipc.rcon.commands.execute import execute
from mcipc.rcon.commands.experience import experience, xp_be, xp_je
from mcipc.rcon.commands.fill import fill_be, fill_je
from mcipc.rcon.commands.fog import fog
from mcipc.rcon.commands.forceload import forceload
from mcipc.rcon.commands.function import function
from mcipc.rcon.commands.gamemode import defaultgamemode, gamemode
from mcipc.rcon.commands.gamerule import gamerule
from mcipc.rcon.commands.geteduclientinfo import geteduclientinfo
from mcipc.rcon.commands.give import give_be, give_je
from mcipc.rcon.commands.help import help_
from mcipc.rcon.commands.immutableworld import immutableworld
from mcipc.rcon.commands.item import item
from mcipc.rcon.commands.kill import kill
from mcipc.rcon.commands.list import list_
from mcipc.rcon.commands.locate import locate
from mcipc.rcon.commands.locatebiome import locatebiome
from mcipc.rcon.commands.op import deop, op
from mcipc.rcon.commands.seed import seed
from mcipc.rcon.commands.spawn import clearspawnpoint
from mcipc.rcon.commands.spawn import setworldspawn
from mcipc.rcon.commands.spawn import spawnpoint
from mcipc.rcon.commands.teleport import teleport


__all__ = ['BEDROCK_COMMANDS', 'EDUCATION_COMMANDS', 'JAVA_COMMANDS']
__credits__ = (
    'Many thanks to all contributers of the Minecraft '
    'wiki on https://minecraft.gamepedia.com/.'
)


BEDROCK_COMMANDS = {

}
EDUCATION_COMMANDS = {

}
JAVA_COMMANDS = {
    'advancement': property(advancement),
    'attribute': attribute,
    'ban': ban,
    'ban_ip': ban_ip,
    'banlist': banlist,
    'bossbar': property(bossbar),
    'clear': clear_je,
    'clone': clone_je,
    'data': property(data),
    'datapack': property(datapack),
    'debug': debug,
    'defaultgamemode': defaultgamemode,
    'deop': deop,
    'difficulty': difficulty,
    'effect': property(effect_je),
    'enchant': enchant,
    'execute': property(execute),
    'experience': property(experience),
    'fill': fill,
    'forceload': property(forceload),
    'function': function,
    'gamemode': gamemode,
    'gamerule': gamerule,
    'give': give_je,
    'help': help_,
    'kick': kick,
    'kill': kill,
    'list': list_,
    'locate': locate,
    'locatebiome': locatebiome,
    'loot': loot,
    'me': me,
    'msg': tell,
    'op': op,
    'pardon': pardon,
    'particle': particle,
    'players': property(list_),
    'playsound': playsound,
    'publish': publish,
    'recipe': recipe,
    'reload': reload,
    'replaceitem': replaceitem,
    'save_all': save_all,
    'save_on': save_on,
    'save_off': save_off,
    'say': say,
    'schedule': schedule,
    'scoreboard': scoreboard,
    'seed': property(seed),
    'send_url': send_url,
    'setblock': setblock,
    'setidletimeout': setidletimeout,
    'setworldspawn': setworldspawn,
    'spawnpoint': spawnpoint,
    'spectate': spectate,
    'spreadplayers': spreadplayers,
    'stop': stop,
    'stopsound': stopsound,
    'summon': summon_je,
    'tag': tag,
    'team': team,
    'teammsg': teammsg,
    'teleport': teleport,
    'tell': tell,
    'tellraw': tellraw,
    'time': time,
    'title': title,
    'tp': teleport,
    'trigger': trigger,
    'w': tell,
    'weather': weather,
    'whitelist': whitelist,
    'worldborder': worldborder,
    'worldbuilder': worldbuilder,
    'xp': property(xp_je)
}
