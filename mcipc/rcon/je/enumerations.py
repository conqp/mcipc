"""Enumerations specific to the Java Edition."""

from enum import Enum


__all__ = [
    'Biome',
    'CollisionRule',
    'Color',
    'Enchantment',
    'ParticleMode',
    'RenderType',
    'ScheduleMode',
    'SoundSource',
    'Structure',
    'TeamOption',
    'TimeSpec',
    'TimeUnit',
    'Visibility'
]


class Biome(Enum):
    """Available biomes in the Java Edition."""

    BADLANDS = 'badlands'
    BADLANDS_PLATEAU = 'badlands_plateau'
    BAMBOO_JUNGLE = 'bamboo_jungle'
    BAMBOO_JUNGLE_HILLS = 'bamboo_jungle_hills'
    BASALT_DELTAS = 'basalt_deltas'
    BEACH = 'beach'
    BIRCH_FOREST = 'birch_forest'
    BIRCH_FOREST_HILLS = 'birch_forest_hills'
    COLD_OCEAN = 'cold_ocean'
    CRIMSON_FOREST = 'crimson_forest'
    DARK_FOREST = 'dark_forest'
    DARK_FOREST_HILLS = 'dark_forest_hills'
    DEEP_COLD_OCEAN = 'deep_cold_ocean'
    DEEP_FROZEN_OCEAN = 'deep_frozen_ocean'
    DEEP_LUKEWARM_OCEAN = 'deep_lukewarm_ocean'
    DEEP_OCEAN = 'deep_ocean'
    DEEP_WARM_OCEAN = 'deep_warm_ocean'
    DESERT = 'desert'
    DESERT_HILLS = 'desert_hills'
    DESERT_LAKES = 'desert_lakes'
    DRIPSTONE_CAVES = 'dripstone_caves'
    END_BARRENS = 'end_barrens'
    END_HIGHLANDS = 'end_highlands'
    END_MIDLANDS = 'end_midlands'
    ERODED_BADLANDS = 'eroded_badlands'
    FLOWER_FOREST = 'flower_forest'
    FOREST = 'forest'
    FROZEN_OCEAN = 'frozen_ocean'
    FROZEN_RIVER = 'frozen_river'
    GIANT_SPRUCE_TAIGA = 'giant_spruce_taiga'
    GIANT_SPRUCE_TAIGA_HILLS = 'giant_spruce_taiga_hills'
    GIANT_TREE_TAIGA = 'giant_tree_taiga'
    GIANT_TREE_TAIGA_HILLS = 'giant_tree_taiga_hills'
    GRAVELLY_MOUNTAINS = 'gravelly_mountains'
    ICE_SPIKES = 'ice_spikes'
    JUNGLE = 'jungle'
    JUNGLE_EDGE = 'jungle_edge'
    JUNGLE_HILLS = 'jungle_hills'
    LUKEWARM_OCEAN = 'lukewarm_ocean'
    MODIFIED_BADLANDS_PLATEAU = 'modified_badlands_plateau'
    MODIFIED_GRAVELLY_MOUNTAINS = 'modified_gravelly_mountains'
    MODIFIED_JUNGLE = 'modified_jungle'
    MODIFIED_JUNGLE_EDGE = 'modified_jungle_edge'
    MODIFIED_WOODEN_BADLANDS_PLATEAU = 'modified_wooded_badlands_plateau'
    MOUNTAIN_EDGE = 'mountain_edge'
    MOUNTAINS = 'mountains'
    MUSHROOM_FIELD_SHORE = 'mushroom_field_shore'
    MUSHROOM_FIELDS = 'mushroom_fields'
    NETHER_WASTES = 'nether_wastes'
    OCEAN = 'ocean'
    PLAINS = 'plains'
    RIVER = 'river'
    SAVANNA = 'savanna'
    SAVANNA_PLATEAU = 'savanna_plateau'
    SHATTERED_SAVANNA = 'shattered_savanna'
    SHATTERED_SAVANNA_PLATEAU = 'shattered_savanna_plateau'
    SMALL_END_ISLANDS = 'small_end_islands'
    SNOWY_BEACH = 'snowy_beach'
    SNOWY_MOUNTAINS = 'snowy_mountains'
    SNOWY_TAIGA = 'snowy_taiga'
    SNOWY_TAIGA_HILLS = 'snowy_taiga_hills'
    SNOWY_TAIGA_MOUNTAINS = 'snowy_taiga_mountains'
    SNOWY_TUNDRA = 'snowy_tundra'
    SOUL_SAND_VALLEY = 'soul_sand_valley'
    STONE_SHORE = 'stone_shore'
    SUNFLOWER_PLAINS = 'sunflower_plains'
    SWAMP = 'swamp'
    SWAMP_HILLS = 'swamp_hills'
    TAIGA = 'taiga'
    TAIGA_HILLS = 'taiga_hills'
    TAIGA_MOUNTAINS = 'taiga_mountains'
    TALL_BIRCH_FOREST = 'tall_birch_forest'
    TALL_BIRCH_HILLS = 'tall_birch_hills'
    THE_END = 'the_end'
    THE_VOID = 'the_void'
    WARM_OCEAN = 'warm_ocean'
    WARPED_FOREST = 'warped_forest'
    WOODED_BADLANDS_PLATEAU = 'wooded_badlands_plateau'
    WOODED_HILLS = 'wooded_hills'
    WOODED_MOUNTAINS = 'wooded_mountains'


class CollisionRule(Enum):
    """Available collision rules."""

    ALWAYS = 'always'
    NEVER = 'never'
    PUSH_OTHER_TEAMS = 'pushOtherTeams'
    PUSH_OWN_TEAM = 'pushOwnTeam'


class Color(Enum):
    """Available colors."""

    AQUA = 'aqua'
    BLACK = 'black'
    BLUE = 'blue'
    DARK_AQUA = 'dark_aqua'
    DARK_BLUE = 'dark_blue'
    DARK_GRAY = 'dark_gray'
    DARK_GREEN = 'dark_green'
    DARK_PURPLE = 'dark_purple'
    DARK_RED = 'dark_red'
    GOLD = 'gold'
    GRAY = 'gray'
    GREEN = 'green'
    LIGHT_PURPLE = 'light_purple'
    RED = 'red'
    RESET = 'reset'
    YELLOW = 'yellow'
    WHITE = 'white'


class Enchantment(Enum):
    """Available enchantments in the Java Edition."""

    AQUA_AFFINITY = 'aqua_affinity'
    BANE_OF_ARTHROPODS = 'bane_of_arthropods'
    BLAST_PROTECTION = 'blast_protection'
    CHANNELING = 'channeling'
    CLEAVING = 'cleaving'
    CURSE_OF_BINDING = 'binding_curse'
    CURSE_OF_VANISHING = 'vanishing_curse'
    DEPTH_STRIDER = 'depth_strider'
    EFFICIENCY = 'efficiency'
    FEATHER_FALLING = 'feather_falling'
    FIRE_ASPECT = 'fire_aspect'
    FIRE_PROTECTION = 'fire_protection'
    FLAME = 'flame'
    FORTUNE = 'fortune'
    FROST_WALKER = 'frost_walker'
    IMPALING = 'impaling'
    INFINITY = 'infinity'
    KNOCKBACK = 'knockback'
    LOOTING = 'looting'
    LOYALTY = 'loyalty'
    LUCK_OF_THE_SEA = 'luck_of_the_sea'
    LURE = 'lure'
    MENDING = 'mending'
    MULTISHOT = 'multishot'
    PIERCING = 'piercing'
    POWER = 'power'
    PROJECTILE_PROTECTION = 'projectile_protection'
    PROTECTION = 'protection'
    PUNCH = 'punch'
    QUICK_CHARGE = 'quick_charge'
    RESPIRATION = 'respiration'
    RIPTIDE = 'riptide'
    SHARPNESS = 'sharpness'
    SILK_TOUCH = 'silk_touch'
    SMITE = 'smite'
    SOUL_SPEED = 'soul_speed'
    SWEEPING = 'sweeping'
    THORNS = 'thorns'
    UNBREAKING = 'unbreaking'


class ParticleMode(Enum):
    """Available particle modes."""

    FORCE = 'force'
    NORMAL = 'normal'


class RenderType(Enum):
    """Available render types."""

    HEARTS = 'hearts'
    INTEGER = 'integer'


class ScheduleMode(Enum):
    """Available schedule modes."""

    APPEND = 'append'
    REPLACE = 'replace'


class SoundSource(Enum):
    """Available sound sources."""

    MASTER = 'master'
    MUSIC = 'music'
    RECORD = 'record'
    WEATHER = 'weather'
    BLOCK = 'block'
    HOSTILE = 'hostile'
    NEUTRAL = 'neutral'
    PLAYER = 'player'
    AMBIENT = 'ambient'
    VOICE = 'voice'


class Structure(Enum):
    """Available structures in the Java Edition."""

    BASTION_REMNANT = 'bastion_remnant'
    BURIED_TREASURE = 'buried_treasure'
    END_CITY = 'endcity'
    FORTRESS = 'fortress'
    WOODLAND_MANSION = 'mansion'
    MINESHAFT = 'mineshaft'
    MONUMENT = 'monument'
    NETHER_FOSSIL = 'nether_fossil'
    OCEAN_RUINS = 'ocean_ruin'
    PILLAGER_OUTPOST = 'pillager_outpost'
    RUINED_PORTAL = 'ruined_portal'
    SHIPWRECK = 'shipwreck'
    STRONGHOLD = 'stronghold'
    DESERT_PYRAMID = 'desert_pyramid'
    IGLOO = 'igloo'
    JUNGLE_PYRAMID = 'jungle_pyramid'
    SWAMP_HUT = 'swamp_hut'
    VILLAGE = 'village'


class TeamOption(Enum):
    """Available team options."""

    COLLISION_RULE = 'collisionRule'
    COLOR = 'color'
    DEATH_MESSAGE_VISIBILITY = 'deathMessageVisibility'
    DISPLAY_NAME = 'displayName'
    FRIENDLY_FIRE = 'friendlyFire'
    NAMETAG_VISIBILITY = 'nametagVisibility'
    PREFIX = 'prefix'
    SEE_FRIENDLY_INVISIBLES = 'seeFriendlyInvisibles'
    SUFFIX = 'suffix'


class TimeSpec(Enum):
    """Available time specifications."""

    DAY = 'day'
    NIGHT = 'night'
    NOON = 'noon'
    MIDNIGHT = 'midnight'


class TimeUnit(Enum):
    """Available time units."""

    DAY = 'd'
    SECOND = 's'
    TICK = 't'


class Visibility(Enum):
    """Available visibility types."""

    NEVER = 'never'
    HIDE_FOR_OTHER_TEAMS = 'hideForOtherTeams'
    HIDE_FOR_OWN_TEAM = 'hideForOwnTeam'
    ALWAYS = 'always'
