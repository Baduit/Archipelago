from __future__ import annotations

from enum import auto, Enum
from typing import List, NamedTuple, TypeAlias

class ItemRequirement(Enum):
    NONE = auto()
    HOOK = auto()
    BAG = auto()
    CHICKEN = auto()
    PAPER_PLANE = auto()
    BOMB = auto()
    ROCKET = auto()
    DOOR = auto()
    COSMIC_ONION = auto()
    BIG_BOSS_BEATEN = auto()
    YELLOW_OCTOPUS = auto()
    GREEN_OCTOPUS = auto()
    ORANGE_OCTOPUS = auto()
    BLUE_OCTOPUS = auto()
    PINK_OCTOPUS = auto()
        

class CogRequirement(NamedTuple):
    value: int


class AndRequirementContainer(NamedTuple):
    requirements: List[ItemRequirement | CogRequirement]


class OrRequirementContainer(NamedTuple):
    requirements: List[AndRequirementContainer | ItemRequirement | CogRequirement]


AccessRequirements: TypeAlias = OrRequirementContainer | AndRequirementContainer | ItemRequirement | CogRequirement | None
