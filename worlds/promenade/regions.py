from typing import List, Tuple, NamedTuple, TypeAlias

from .access_requirement import AccessRequirements, AndRequirementContainer, CogRequirement, ItemRequirement, OrRequirementContainer
from .names.region_names import RegionName


class EntranceData(NamedTuple):
    start: RegionName
    destination: RegionName
    requirement: AccessRequirements = None


# Entrances that can't be changed
static_entrance_list: List[EntranceData] = [
    EntranceData(RegionName.MENU, RegionName.THE_CAVE),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_0, RegionName.GREAT_ELEVATOR_LEVEL_1, CogRequirement(3)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_1, RegionName.GREAT_ELEVATOR_LEVEL_0),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_1, RegionName.GREAT_ELEVATOR_LEVEL_2, CogRequirement(6)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_2, RegionName.GREAT_ELEVATOR_LEVEL_1),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_2, RegionName.GREAT_ELEVATOR_LEVEL_3, CogRequirement(15)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.GREAT_ELEVATOR_LEVEL_2),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.GREAT_ELEVATOR_LEVEL_4, CogRequirement(36)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_4, RegionName.GREAT_ELEVATOR_LEVEL_3),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_4, RegionName.GREAT_ELEVATOR_LEVEL_5, CogRequirement(57)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_5, RegionName.GREAT_ELEVATOR_LEVEL_4),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_5, RegionName.GREAT_ELEVATOR_LEVEL_6, CogRequirement(78)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_6, RegionName.GREAT_ELEVATOR_LEVEL_5),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_6, RegionName.GREAT_ELEVATOR_LEVEL_7, CogRequirement(99)),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_7, RegionName.GREAT_ELEVATOR_LEVEL_6),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_7, RegionName.GREAT_ELEVATOR_LEVEL_8, ItemRequirement.BIG_BOSS_BEATEN),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_8, RegionName.GREAT_ELEVATOR_LEVEL_7),

    EntranceData(RegionName.SANDY_STROLL, RegionName.COSMIC_CRUISE, ItemRequirement.HOOK),
    EntranceData(RegionName.COSMIC_CRUISE, RegionName.SANDY_STROLL),
    
    EntranceData(RegionName.VERDANT_VOYAGE, RegionName.CANOPY_CLAMBER, ItemRequirement.HOOK),
    EntranceData(RegionName.CANOPY_CLAMBER, RegionName.VERDANT_VOYAGE),
]

# Entrances that could be randomized, the destination here are the default values
dynamic_entrance_list: List[EntranceData] = [
    EntranceData(RegionName.THE_CAVE, RegionName.GREAT_ELEVATOR_LEVEL_0),
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_0, RegionName.THE_CAVE),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_1, RegionName.SANDY_STROLL),
    EntranceData(RegionName.SANDY_STROLL, RegionName.GREAT_ELEVATOR_LEVEL_1),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.VERDANT_VOYAGE),
    EntranceData(RegionName.VERDANT_VOYAGE, RegionName.GREAT_ELEVATOR_LEVEL_3),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_4, RegionName.JUNGLE_JAUNT),
    EntranceData(RegionName.JUNGLE_JAUNT, RegionName.GREAT_ELEVATOR_LEVEL_4),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_5, RegionName.CANOPY_CLAMBER),
    EntranceData(RegionName.CANOPY_CLAMBER, RegionName.GREAT_ELEVATOR_LEVEL_5),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_6, RegionName.FROSTY_FOOTPATH),
    EntranceData(RegionName.FROSTY_FOOTPATH, RegionName.GREAT_ELEVATOR_LEVEL_6),

    # trials
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_1, RegionName.SWIFT_MOVEMENT_EXPERTISE, OrRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    EntranceData(RegionName.SWIFT_MOVEMENT_EXPERTISE, RegionName.GREAT_ELEVATOR_LEVEL_1),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.SLINGSHOT_EXPERTISE, ItemRequirement.HOOK),
    EntranceData(RegionName.SLINGSHOT_EXPERTISE, RegionName.GREAT_ELEVATOR_LEVEL_3),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.THE_TRIALS_OF_THE_EXPERT, ItemRequirement.BOMB),
    EntranceData(RegionName.THE_TRIALS_OF_THE_EXPERT, RegionName.GREAT_ELEVATOR_LEVEL_3),

    EntranceData(RegionName.SANDY_STROLL, RegionName.THE_TRIALS_OF_THE_CANNON),
    EntranceData(RegionName.THE_TRIALS_OF_THE_CANNON, RegionName.SANDY_STROLL),

    EntranceData(RegionName.COSMIC_CRUISE, RegionName.THE_TRIALS_OF_THE_ROCKETS, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TRIALS_OF_THE_ROCKETS, RegionName.COSMIC_CRUISE),

    EntranceData(RegionName.VERDANT_VOYAGE, RegionName.THE_TRIALS_OF_THORNS),
    EntranceData(RegionName.THE_TRIALS_OF_THORNS, RegionName.VERDANT_VOYAGE),

    EntranceData(RegionName.CANOPY_CLAMBER, RegionName.THE_TRIALS_OF_ZIPLINES, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TRIALS_OF_ZIPLINES, RegionName.CANOPY_CLAMBER),

    EntranceData(RegionName.JUNGLE_JAUNT, RegionName.THE_TRIALS_OF_CHIPANZIPS, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TRIALS_OF_CHIPANZIPS, RegionName.JUNGLE_JAUNT),

    EntranceData(RegionName.GROTTO_GALLIVANT, RegionName.THE_TRIALS_OF_THE_SPITTY_PLANTS),
    EntranceData(RegionName.THE_TRIALS_OF_THE_SPITTY_PLANTS, RegionName.GROTTO_GALLIVANT),

    EntranceData(RegionName.RIDGE_RAMBLE, RegionName.THE_TRIALS_OF_THE_VERTIGINOUS_HEIGHTS, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TRIALS_OF_THE_VERTIGINOUS_HEIGHTS, RegionName.RIDGE_RAMBLE),

    EntranceData(RegionName.AERIAL_AMBLE, RegionName.THE_TRIALS_OF_THE_PAPER_PLANE, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TRIALS_OF_THE_PAPER_PLANE, RegionName.AERIAL_AMBLE),

    EntranceData(RegionName.FROSTY_FOOTPATH, RegionName.THE_TRIALS_OF_THE_SNOWBALLS, ItemRequirement.BAG),
    EntranceData(RegionName.THE_TRIALS_OF_THE_SNOWBALLS, RegionName.FROSTY_FOOTPATH),

    EntranceData(RegionName.ULTIMATE_TRIALS, RegionName.MEMORY_LANE, ItemRequirement.HOOK),
    EntranceData(RegionName.MEMORY_LANE, RegionName.ULTIMATE_TRIALS),

    EntranceData(RegionName.ULTIMATE_TRIALS, RegionName.THE_TOWER, ItemRequirement.HOOK),
    EntranceData(RegionName.THE_TOWER, RegionName.ULTIMATE_TRIALS),

    # octoretros
    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_1, RegionName.OCTORETRO_TENNIS, ItemRequirement.ORANGE_OCTOPUS),
    EntranceData(RegionName.OCTORETRO_TENNIS, RegionName.GREAT_ELEVATOR_LEVEL_1),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_3, RegionName.OCTORETRO_THE_INVADER, AndRequirementContainer(ItemRequirement.YELLOW_OCTOPUS, ItemRequirement.HOOK)),
    EntranceData(RegionName.OCTORETRO_THE_INVADER, RegionName.GREAT_ELEVATOR_LEVEL_3),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_4, RegionName.OCTORETRO_BRICK_BREAK, AndRequirementContainer(ItemRequirement.BLUE_OCTOPUS, ItemRequirement.HOOK)),
    EntranceData(RegionName.OCTORETRO_BRICK_BREAK, RegionName.GREAT_ELEVATOR_LEVEL_4),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_5, RegionName.OCTORETRO_BUBBLE_POP, AndRequirementContainer(ItemRequirement.GREEN_OCTOPUS, ItemRequirement.HOOK)),
    EntranceData(RegionName.OCTORETRO_BUBBLE_POP, RegionName.GREAT_ELEVATOR_LEVEL_5),

    EntranceData(RegionName.GREAT_ELEVATOR_LEVEL_6, RegionName.OCTORETRO_BASKETBALL, AndRequirementContainer(ItemRequirement.PINK_OCTOPUS, ItemRequirement.HOOK)),
    EntranceData(RegionName.OCTORETRO_BASKETBALL, RegionName.GREAT_ELEVATOR_LEVEL_6),
]