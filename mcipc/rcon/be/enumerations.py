"""Enumerations specific to the Bedrock Edition."""

from enum import Enum


__all__ = [
    'Biome',
    'Enchantment',
    'EntityEquipmentSlot',
    'FillType',
    'Location',
    'MatchMode',
    'Mirror',
    'MusicRepeatMode',
    'Operator',
    'Order',
    'ReplaceMode',
    'RideRules',
    'Rotation',
    'SaveCommand',
    'Structure',
    'StructureAnimationMode',
    'StructureSaveMode',
    'TeleportRules',
    'TimeSpec'
]


class Biome(Enum):
    """Available biomes in the Bedrock Edition."""

    BADLANDS = 'mesa'
    BADLANDS_PLATEAU = 'mesa_plateau'
    BAMBOO_JUNGLE = 'bamboo_jungle'
    BAMBOO_JUNGLE_HILLS = 'bamboo_jungle_hills'
    BASALT_DELTAS = 'basalt_deltas'
    BEACH = 'beach'
    BIRCH_FOREST = 'birch_forest'
    BIRCH_FOREST_HILLS = 'birch_forest_hills'
    COLD_OCEAN = 'cold_ocean'
    CRIMSON_FOREST = 'crimson_forest'
    DARK_FOREST = 'roofed_forest'
    DARK_FOREST_HILLS = 'roofed_forest_mutated'
    DEEP_COLD_OCEAN = 'deep_cStructureAnimationModeold_ocean'
    DEEP_FROZEN_OCEAN = 'deep_frozen_ocean'
    DEEP_LUKEWARN_OCEAN = 'deep_lukewarm_ocean'
    DEEP_OCEAN = 'deep_ocean'
    DEEP_WARM_OCEAN = 'deep_warm_ocean'
    DESERT = 'desert'
    DESERT_HILLS = 'desert_hills'
    DESERT_LAKES = 'desert_mutated'
    ERODED_BADLANDS = 'mesa_bryce'
    FLOWER_FOREST = 'flower_forest'
    FOREST = 'forest'
    FROZEN_OCEAN = 'frozen_ocean'
    FROZEN_RIVER = 'frozen_river'
    GIANT_SPRUCE_TAIGA = 'redwood_taiga_mutated'
    GIANT_SPRUCE_TAIGA_HILLS = 'redwood_taiga_hills_mutated'
    GIANT_TREE_TAIGA = 'mega_taiga'
    GIANT_TREE_TAIGA_HILLS = 'mega_taiga_hills'
    GRAVELLY_MOUNTAINS = 'extreme_hills_mutated'
    GRAVELLY_MOUNTAINS_PLUS = 'extreme_hills_plus_trees_mutated'
    ICE_SPIKES = 'ice_plains_spikes'
    JUNGLE = 'jungle'
    JUNGLE_EDGE = 'jungle_edge'
    JUNGLE_HILLS = 'jungle_hills'
    LEGACY_FROZEN_OCEAN = 'legacy_frozen_ocean'
    LUKEWARM_OCEAN = 'lukewarm_ocean'
    MODIFIED_BADLANDS_PLATEAU = 'mesa_plateau_mutated'
    MODIFIED_JUNGLE = 'jungle_mutated'
    MODIFIED_JUNGLE_EDGE = 'jungle_edge_mutated'
    MODIFIED_WOODED_BADLANDS_PLATEAU = 'mesa_plateau_stone_mutated'
    MOUNTAIN_EDGE = 'extreme_hills_edge'
    MOUNTAINS = 'extreme_hills'
    MUSHROOM_FIELD_SHORE = 'mushroom_island_shore'
    MUSHROOM_FIELDS = 'mushroom_island'
    NETHER_WASTES = 'hell'
    OCEAN = 'ocean'
    PLAINS = 'plains'
    RIVER = 'river'
    SAVANNA = 'savanna'
    SAVANNA_PLATEAU = 'savanna_plateau'
    SHATTERED_SAVANNA = 'savanna_mutated'
    SHATTERED_SAVANNA_PLATEAU = 'savanna_plateau_mutated'
    SNOWY_BEACH = 'cold_beach'
    SNOWY_MOUNTAINS = 'ice_mountains'
    SNOWY_TAIGA = 'cold_taiga'
    SNOWY_TAIGA_HILLS = 'cold_taiga_hills'
    SNOWY_TAIGA_MOUNTAINS = 'cold_taiga_mutated'
    SNOWY_TUNDRA = 'ice_plains'
    SOUL_SAND_VALLEY = 'soul_sand_valley'
    STONE_SHORE = 'stone_beach'
    SUNFLOWER_PLAINS = 'sunflower_plains'
    SWAMP = 'swampland'
    SWAMP_HILLS = 'swampland_mutated'
    TAIGA = 'taiga'
    TAIGA_HILLS = 'taiga_hills'
    TAIGA_MOUNTAINS = 'taiga_mutated'
    TALL_BIRCH_FOREST = 'birch_forest_mutated'
    TALL_BIRCH_HILLS = 'birch_forest_hills_mutated'
    THE_END = 'the_end'
    WARM_OCEAN = 'warm_ocean'
    WARPED_FOREST = 'warped_forest'
    WOODED_BADLANDS_PLATEAU = 'mesa_plateau_stone'
    WOODED_HILLS = 'forest_hills'
    WOODED_MOUNTAINS = 'extreme_hills_plus_trees'


class Enchantment(Enum):
    """Available enchantments in the Bedrock Edition."""

    AQUA_AFFINITY = 'aqua_affinity'
    BANE_OF_ARTHROPODS = 'bane_of_arthropods'
    BLAST_PROTECTION = 'blast_protection'
    CHANNELING = 'channeling'
    CLEAVING = 'cleaving'
    CURSE_OF_BINDING = 'binding'
    CURSE_OF_VANISHING = 'vanishing'
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


class EntityEquipmentSlot(Enum):
    """Available entity equipment slots."""

    ARMOR_CHEST = 'armor.chest'
    ARMOR_FEET = 'armor.feet'
    ARMOR_HEAD = 'armor.head'
    ARMOR_LEGS = 'armor.legs'
    CONTAINER_SLOT = 'container.{}'.format
    ENDERCHEST_SLOT = 'enderchest.{}'.format
    HORSE_ARMOR = 'horse.armor'
    HORSE_CHEST = 'horse.chest'
    HORSE_SADDLE = 'horse.saddle'
    HORSE_SLOT = 'horse.{}'.format
    HOTBAR_SLOT = 'hotbar.{}'.format
    INVENTORY_SLOT = 'inventory.{}'.format
    VILLAGER_SLOT = 'villager.{}'.format
    WEAPON = 'weapon'
    WEAPON_MAINHAND = 'weapon.mainhand'
    WEAPON_OFFHAND = 'weapon.offhand'


class FillType(Enum):
    """Available fill types."""

    IF_GROUP_FITS = 'if_group_fits'
    UNTIL_FULL = 'until_full'


class Location(Enum):
    """Available locations."""

    BELOWNAME = 'belowname'
    LIST = 'list'
    SIDEBAR = 'sidebar'


class MatchMode(Enum):
    """Available block matching modes."""

    ALL = 'all'
    MASKED = 'masked'


class Mirror(Enum):
    """Available mirror modes."""

    X = 'x'
    Z = 'z'
    XZ = 'xz'
    NONE = 'none'


class MusicRepeatMode(Enum):
    """Available music repeat modes."""

    LOOP = 'loop'
    PLAY_ONCE = 'play_once'


class Operator(Enum):
    """Available operators."""

    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    MODULO = '%'
    ASSIGN = '='
    MIN = '<'
    MAX = '>'
    SWAP = '><'


class Order(Enum):
    """Available orderings."""

    ASCENDING = 'ascending'
    DESCENDING = 'descending'


class ReplaceMode(Enum):
    """Available replace modes."""

    DESTROY = 'destroy'
    KEEP = 'keep'


class RideRules(Enum):
    """Available ride rules."""

    NO_RIDE_CHANGE = 'no_ride_change'
    REASSIGN_RIDES = 'reassign_rides'
    SKIP_RIDERS = 'skip_riders'


class Rotation(Enum):
    """Available rotation modes."""

    DEG_0 = '0_degrees'
    DEG_90 = '90_degrees'
    DEG_180 = '180_degrees'
    DEG_270 = '270_degrees'


class SaveCommand(Enum):
    """Available save commands."""

    HOLD = 'hold'
    QUERY = 'query'
    RESUME = 'resume'


class Structure(Enum):
    """Available structures in the Bedrock Edition."""

    BASTION_REMNANT = 'bastionremnant'
    BURIED_TREASURE = 'buriedtreasure'
    END_CITY = 'endcity'
    FORTRESS = 'fortress'
    WOODLAND_MANSION = 'mansion'
    MINESHAFT = 'mineshaft'
    MONUMENT = 'monument'
    OCEAN_RUINS = 'ruins'
    PILLAGER_OUTPOST = 'pillageroutpost'
    RUINED_PORTAL = 'ruinedportal'
    SHIPWRECK = 'shipwreck'
    STRONGHOLD = 'stronghold'
    DESERT_PYRAMID = 'temple'
    IGLOO = 'temple'
    JUNGLE_PYRAMID = 'temple'
    SWAMP_HUT = 'temple'
    VILLAGE = 'village'


class StructureAnimationMode(Enum):
    """Available structure animations."""

    BLOCK_BY_BLOCK = 'block_by_block'
    LAYER_BY_LAYER = 'layer_by_layer'


class StructureSaveMode(Enum):
    """Available structure save modes."""

    DISK = 'disk'
    MEMORY = 'memory'


class TeleportRules(Enum):
    """Available teleportation rules."""

    TELEPORT_RIDE = 'teleport_ride'
    TELEPORT_RIDER = 'teleport_rider'


class TimeSpec(Enum):
    """Available time specifications."""

    DAY = 'day'
    NIGHT = 'night'
    NOON = 'noon'
    MIDNIGHT = 'midnight'
    SUNRISE = 'sunrise‌'
    SUNSET = 'sunset‌'
