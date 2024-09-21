from enum import auto, Enum

class BookRegionName(Enum):
    """
    Region listed in the ingame book
    """
    GREAT_ELEVATOR_1 = auto()
    GREAT_ELEVATOR_2 = auto()
    GREAT_ELEVATOR_3 = auto()
    SANDY_STROLL = auto()
    COSMIC_CRUISE = auto()
    VERDANT_VOYAGE = auto()
    CANOPY_CLAMBER = auto()
    JUNGLE_JAUNT = auto()
    GROTTO_GALLIVANT = auto()
    RIDGE_RAMBLE = auto()
    AERIAL_AMBLE = auto()
    FROSTY_FOOTPATH = auto()
    TROUBLESOME_TOUR = auto()
    ULTIMATE_TRIALS = auto()

class RegionName(Enum):
    """
    Regions used by locations
    It will be split into several region automatically depending on locations access condition in the region
    For example in the GREAT_ELEVATOR_1 not all locations require the hook so it will create a region
    GREAT_ELEVATOR_1 and a GREAT_ELEVATOR_1_hook
    """
    MENU = auto()

    GREAT_ELEVATOR_LEVEL_0 = auto()
    GREAT_ELEVATOR_LEVEL_1 = auto()
    GREAT_ELEVATOR_LEVEL_2 = auto()
    GREAT_ELEVATOR_LEVEL_3 = auto()
    GREAT_ELEVATOR_LEVEL_4 = auto()
    GREAT_ELEVATOR_LEVEL_5 = auto()
    GREAT_ELEVATOR_LEVEL_6 = auto()
    GREAT_ELEVATOR_LEVEL_7 = auto()
    GREAT_ELEVATOR_LEVEL_8 = auto() # Golden elevator

    SANDY_STROLL = auto()
    COSMIC_CRUISE = auto()
    VERDANT_VOYAGE = auto()
    CANOPY_CLAMBER = auto()
    JUNGLE_JAUNT = auto()
    GROTTO_GALLIVANT = auto()
    RIDGE_RAMBLE = auto()
    AERIAL_AMBLE = auto()
    FROSTY_FOOTPATH = auto()
    TROUBLESOME_TOUR = auto()
    ULTIMATE_TRIALS = auto()
    THE_CAVE = auto()

    # Techniquement, les donjons ça pourrait être aussi des locations à part entière et ça pourrait être randomisé aussi !

    SWIFT_MOVEMENT_EXPERTISE = auto()
    SLINGSHOT_EXPERTISE = auto()
    THE_TRIALS_OF_THE_EXPERT = auto()
    THE_TRIALS_OF_THE_CANNON = auto()
    THE_TRIALS_OF_THE_ROCKETS = auto()
    THE_TRIALS_OF_THORNS = auto()
    THE_TRIALS_OF_ZIPLINES = auto()
    THE_TRIALS_OF_CHIPANZIPS = auto()
    THE_TRIALS_OF_THE_SPITTY_PLANTS = auto()
    THE_TRIALS_OF_THE_VERTIGINOUS_HEIGHTS = auto()
    THE_TRIALS_OF_THE_PAPER_PLANE = auto()
    THE_TRIALS_OF_THE_SNOWBALLS = auto()
    MEMORY_LANE = auto()
    THE_TOWER = auto()

    OCTORETRO_TENNIS = auto()
    OCTORETRO_THE_INVADER = auto()
    OCTORETRO_BRICK_BREAK = auto()
    OCTORETRO_BUBBLE_POP = auto()
    OCTORETRO_BASKETBALL = auto()
    