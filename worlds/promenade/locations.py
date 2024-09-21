
from typing import Dict, List, NamedTuple

from BaseClasses import Location

from .access_requirement import AccessRequirements, AndRequirementContainer, ItemRequirement, OrRequirementContainer
from .names.region_names import BookRegionName, RegionName


class LocationData(NamedTuple):
    region: RegionName
    book_region: BookRegionName
    requirement: AccessRequirements = None


location_table: Dict[str, LocationData] = {
    # GREAT_ELEVATOR_1
    "Basketball for beginners": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_0, BookRegionName.GREAT_ELEVATOR_1),
    "Above the fluffly clouds": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_0, BookRegionName.GREAT_ELEVATOR_1),
    "The tree's puzzling jigsaw piece": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_0, BookRegionName.GREAT_ELEVATOR_1),
    "Da Pinchi's 'Flourishing flowers'": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_2, BookRegionName.GREAT_ELEVATOR_1),
    "Tiny huge house": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_2, BookRegionName.GREAT_ELEVATOR_1),

    # GREAT_ELEVATOR_2
    "Potage for Po": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_3, BookRegionName.GREAT_ELEVATOR_2),
    "Chicken for Ti": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_3, BookRegionName.GREAT_ELEVATOR_2, requirement=ItemRequirement.CHICKEN),
    "Guarded by the mole": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2),
    "Gliding to the unknown": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2, requirement=ItemRequirement.PAPER_PLANE),
    "It belongs in a museum A": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2, requirement=AndRequirementContainer(ItemRequirement.BOMB, ItemRequirement.ROCKET)),
    "It belongs in a museum B": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2, requirement=AndRequirementContainer(ItemRequirement.PAPER_PLANE, ItemRequirement.CHICKEN)),
    "It belongs in a museum C": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2, requirement=ItemRequirement.COSMIC_ONION), # Other onion can be found in the same level
    "It belongs in a museum D": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2, requirement=ItemRequirement.CHICKEN), # Tomoto can be found in previous hard linked level
    "Dashton's secluded home": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_4, BookRegionName.GREAT_ELEVATOR_2),

    # GREAT_ELEVATOR_3
    "Having a blast with Simon": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_5, BookRegionName.GREAT_ELEVATOR_3, requirement=ItemRequirement.HOOK),
    "Very late to a rendez-vous": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_5, BookRegionName.GREAT_ELEVATOR_3, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "The missing door": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_5, BookRegionName.GREAT_ELEVATOR_3, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG, ItemRequirement.DOOR)),
    "Basketball for experts": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_6, BookRegionName.GREAT_ELEVATOR_3, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Secret recipe": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_3, BookRegionName.GREAT_ELEVATOR_3), # Need hook only to see the recipe
    "The magic padlock's mystery": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_3, BookRegionName.GREAT_ELEVATOR_3, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "The golem's hidden challenge": LocationData(RegionName.GREAT_ELEVATOR_LEVEL_3, BookRegionName.GREAT_ELEVATOR_3, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),

    # Sandy stroll
    "Atop the mast": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "Defeat the grumpy bazookrakb": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "Inside the shipwreck": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "Under the village": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "3, 2, 1, go!": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "3, 2, 1, go! HARD": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "Late to rendez-vous": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "X marks the spot": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "The shoreline's puzzling jigsaw piece": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL),
    "Above the village": LocationData(RegionName.SANDY_STROLL, BookRegionName.SANDY_STROLL), # Maybe optional hook_or_bag requirement with an easy option
    
    # Cosmic cruise
    "Da Pinchi's 'Stamy sky'": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "A bucketful of urchins": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "To infinity and beyond": LocationData(RegionName.SANDY_STROLL, BookRegionName.COSMIC_CRUISE),
    "Run, jump and duck": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "Zero gravity basketball": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "The fastest man on earth": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "Golden in the inside": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "The bright professor": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "The dark side of the moon": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "Dungeon Cosmic cruise": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),
    "Dungeon Cosmic cruise bis": LocationData(RegionName.COSMIC_CRUISE, BookRegionName.COSMIC_CRUISE, requirement=ItemRequirement.HOOK),

    # Verdant voyage
    "Catching Pips": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "On top of the beanstalk": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "The thirsty flower": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "Gliding from leaves to leaves": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "The runaway chickens": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "Upstair with no stairs": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "Having fun with Simon": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "The needle show the way": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "Brock's rough wake-up": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE),
    "Dungeon Verdan voyage": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE, requirement=ItemRequirement.HOOK),
    "Dungeon Verdan voyage bis": LocationData(RegionName.VERDANT_VOYAGE, BookRegionName.VERDANT_VOYAGE, requirement=ItemRequirement.HOOK),

    # Canopy clamber
    "Sticky-plants in the shipwreck": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "Gently falling heliflowers": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "Barely out of reach in the treehouse": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "The path of the sticky plants": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "3, 2, 1, go!!": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "3, 2, 1, go!! HARD": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "Zooming with ziplines": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "Basketball among the treehouses": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "The groundchick's domain": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),
    "The heliflower's perilous path": LocationData(RegionName.CANOPY_CLAMBER, BookRegionName.CANOPY_CLAMBER, requirement=ItemRequirement.HOOK),

    # Jungle jaunt
    "Yummy popcorn": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT),
    "Behind the cracked stone": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=OrRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Cracked stone and proper timing": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=OrRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Toasted marshmallow for Ma": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT),
    "3, 2, 1, go!!!": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),
    "3, 2, 1, go!!! HARD": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),
    "With some help from the chipanzips": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),
    "Popcorn and fountains": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT),
    "Inside the wormhole": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT),
    "The labyrinth's lost room": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),
    "Dungeon Jungle jaunt": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),
    "Dungeon Jungle jaunt bis": LocationData(RegionName.JUNGLE_JAUNT, BookRegionName.JUNGLE_JAUNT, requirement=ItemRequirement.HOOK),

    # Grotto gallivant
    "Spitty-plants and triple jump": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Next door": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Guided by the needle": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Catching Dips": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Obstructed tunnel": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Obstructed ceiling": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Door to door": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Door to door": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT),
    "Mission: sneaky roberry": LocationData(RegionName.GROTTO_GALLIVANT, BookRegionName.GROTTO_GALLIVANT, requirement=ItemRequirement.HOOK),

    # Ridge ramble
    "The halfway point": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "The summit!": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "Windy basketball": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE),
    "Lady Screech and her groundchicks": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "3, 2, 1, go!!!!": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "3, 2, 1, go!!!! HARD": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "Catching zips": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "Revolting rotor": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "Colorful crossing": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),
    "Da pinchi's 'Sublime summit'": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.RIDGE_RAMBLE, requirement=ItemRequirement.HOOK),


    # Aerial amble
    "Jolly jungling": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=ItemRequirement.HOOK),
    "Debonair dancing": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=ItemRequirement.HOOK),
    "A headless ship": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=ItemRequirement.HOOK),
    "Defeat the angry bazoocrab": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=ItemRequirement.HOOK),
    "X marks the spot 1": LocationData(RegionName.THE_CAVE, BookRegionName.AERIAL_AMBLE),
    "X marks the spot 2": LocationData(RegionName.SANDY_STROLL, BookRegionName.AERIAL_AMBLE),
    "X marks the spot 3": LocationData(RegionName.RIDGE_RAMBLE, BookRegionName.AERIAL_AMBLE),
    "X marks the spot 4": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.AERIAL_AMBLE),
    "The captain's blossom": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Dungeon aerial amble": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Dungeon aerial amble bis": LocationData(RegionName.AERIAL_AMBLE, BookRegionName.AERIAL_AMBLE, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),

    # Frosty footpath
    "Chilly chest": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH, requirement=ItemRequirement.BAG),
    "Coming in hot!": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH),
    "A snowy ascend": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH),
    "Overthrow his icy tighness": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH),
    "3, 2, Go!": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH, requirement=ItemRequirement.BAG),
    "3, 2, Go! HARD": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH, requirement=ItemRequirement.BAG),
    "Defeat the snow armadillo": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH, requirement=ItemRequirement.BAG),
    "Da Pinchi's 'Frostry fir'": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH, requirement=ItemRequirement.BAG),
    "The snowcap's puzzling jigsaw piece": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH),
    "Relish for Ron": LocationData(RegionName.FROSTY_FOOTPATH, BookRegionName.FROSTY_FOOTPATH),

    # Troublesome tour
    "Banishing the shadowlones": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=ItemRequirement.BAG),
    "A jugsawed memory": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=ItemRequirement.BAG),
    "Catching rips": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR),
    "Beware of the cunning eyes": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Among the pretenders": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR),
    "Lost in the moody maze": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Overflow": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Lewi's nightmare": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Dungeon Troublesom tour": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),
    "Dungeon Troublesom tour bis": LocationData(RegionName.TROUBLESOME_TOUR, BookRegionName.TROUBLESOME_TOUR, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),

    # Ultimate trials
    "Ultimate acrobatics": LocationData(RegionName.ULTIMATE_TRIALS, BookRegionName.ULTIMATE_TRIALS, requirement=AndRequirementContainer(ItemRequirement.HOOK, ItemRequirement.BAG)),

    # Trials
    "Swift movement expertise": LocationData(RegionName.SWIFT_MOVEMENT_EXPERTISE, BookRegionName.GREAT_ELEVATOR_1),
    "Swift movement expertise TIMER": LocationData(RegionName.SWIFT_MOVEMENT_EXPERTISE, BookRegionName.GREAT_ELEVATOR_1),
    
    "Slinghop expterise": LocationData(RegionName.SLINGSHOT_EXPERTISE, BookRegionName.GREAT_ELEVATOR_2),
    "Slinghop expterise TIMER": LocationData(RegionName.SLINGSHOT_EXPERTISE, BookRegionName.GREAT_ELEVATOR_2),

    "The trial of expert": LocationData(RegionName.THE_TRIALS_OF_THE_EXPERT, BookRegionName.GREAT_ELEVATOR_2),
    "The trial of  expert TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_EXPERT, BookRegionName.GREAT_ELEVATOR_2),

    "The trials of the cannon": LocationData(RegionName.THE_TRIALS_OF_THE_CANNON, BookRegionName.SANDY_STROLL),
    "The trials of the cannon TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_CANNON, BookRegionName.SANDY_STROLL),

    "The trial of the rockets": LocationData(RegionName.THE_TRIALS_OF_THE_ROCKETS, BookRegionName.COSMIC_CRUISE),
    "The trial of the rockets TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_ROCKETS, BookRegionName.COSMIC_CRUISE),

    "The trial of thorns": LocationData(RegionName.THE_TRIALS_OF_THORNS, BookRegionName.VERDANT_VOYAGE),
    "The trial of thorns TIMER": LocationData(RegionName.THE_TRIALS_OF_THORNS, BookRegionName.VERDANT_VOYAGE),

    "The trial of ziplines": LocationData(RegionName.THE_TRIALS_OF_ZIPLINES, BookRegionName.CANOPY_CLAMBER),
    "The trial of ziplines TIMER": LocationData(RegionName.THE_TRIALS_OF_ZIPLINES, BookRegionName.CANOPY_CLAMBER),

    "The trial of chipanzips": LocationData(RegionName.THE_TRIALS_OF_CHIPANZIPS, BookRegionName.JUNGLE_JAUNT),
    "The trial of chipanzips TIMER": LocationData(RegionName.THE_TRIALS_OF_CHIPANZIPS, BookRegionName.JUNGLE_JAUNT),

    "The trial of the spitty-plants": LocationData(RegionName.THE_TRIALS_OF_THE_SPITTY_PLANTS, BookRegionName.GROTTO_GALLIVANT),
    "The trial of the spitty-plants TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_SPITTY_PLANTS, BookRegionName.GROTTO_GALLIVANT),

    "The trial of vertiginous heights": LocationData(RegionName.THE_TRIALS_OF_THE_VERTIGINOUS_HEIGHTS, BookRegionName.RIDGE_RAMBLE),
    "The trial of vertiginous heights TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_VERTIGINOUS_HEIGHTS, BookRegionName.RIDGE_RAMBLE),

    "The trial of the paper plane": LocationData(RegionName.THE_TRIALS_OF_THE_PAPER_PLANE, BookRegionName.AERIAL_AMBLE),
    "The trial of the paper plane TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_PAPER_PLANE, BookRegionName.AERIAL_AMBLE),

    "The trial of the snowballs": LocationData(RegionName.THE_TRIALS_OF_THE_SNOWBALLS, BookRegionName.FROSTY_FOOTPATH),
    "The trial of the snowballs TIMER": LocationData(RegionName.THE_TRIALS_OF_THE_SNOWBALLS, BookRegionName.FROSTY_FOOTPATH),

    "Memory lane": LocationData(RegionName.MEMORY_LANE, BookRegionName.ULTIMATE_TRIALS),
    "Memory lane TIMER": LocationData(RegionName.MEMORY_LANE, BookRegionName.ULTIMATE_TRIALS),

    "The tower": LocationData(RegionName.THE_TOWER, BookRegionName.ULTIMATE_TRIALS),
    "The tower TIMER": LocationData(RegionName.THE_TOWER, BookRegionName.ULTIMATE_TRIALS),

    # Octoretros
    "Octoretro: tennis": LocationData(RegionName.OCTORETRO_TENNIS, BookRegionName.GREAT_ELEVATOR_1),
    "Octoretro: tennis HARD": LocationData(RegionName.OCTORETRO_TENNIS, BookRegionName.GREAT_ELEVATOR_1),

    "Octoretro: the invader": LocationData(RegionName.OCTORETRO_THE_INVADER, BookRegionName.GREAT_ELEVATOR_2),
    "Octoretro: the invader HARD": LocationData(RegionName.OCTORETRO_THE_INVADER, BookRegionName.GREAT_ELEVATOR_2),

    "Octoretro: brick break": LocationData(RegionName.OCTORETRO_BRICK_BREAK, BookRegionName.GREAT_ELEVATOR_2),
    "Octoretro: brick break HARD": LocationData(RegionName.OCTORETRO_BRICK_BREAK, BookRegionName.GREAT_ELEVATOR_2),

    "Octoretro: bubble pop": LocationData(RegionName.OCTORETRO_BUBBLE_POP, BookRegionName.GREAT_ELEVATOR_3),
    "Octoretro: bubble pop HARD": LocationData(RegionName.OCTORETRO_BUBBLE_POP, BookRegionName.GREAT_ELEVATOR_3),

    "Octoretro: basketball": LocationData(RegionName.OCTORETRO_BASKETBALL, BookRegionName.GREAT_ELEVATOR_3),
    "Octoretro: basketball HARD": LocationData(RegionName.OCTORETRO_BASKETBALL, BookRegionName.GREAT_ELEVATOR_3),
}


class PromenadeLocation(Location):
    game: str = "Promenade"