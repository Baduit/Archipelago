from typing import Dict, NamedTuple

from BaseClasses import Item

class ItemData(NamedTuple):
    quantity: int

NB_OCTOPUS: int = 5
NB_COMPLETE_COG: int = 10
COMPLETE_COG_SIZE: int = 3
NB_COG: int = 180
NB_COG_PIECE: int = NB_COG - (NB_COMPLETE_COG * COMPLETE_COG_SIZE)

item_table: Dict[str, ItemData] = {
    "CogPiece": ItemData(NB_COG_PIECE),
    "CompleteCog": ItemData(NB_COMPLETE_COG),
    "Hook": ItemData(1),
    "Bag": ItemData(1),
    "YellowOctopus": ItemData(1),
    "GreenOctopus": ItemData(1),
    "OrangeOctopus": ItemData(1),
    "BlueOctopus": ItemData(1),
    "PinkOctopus": ItemData(1),
}


class PromenadeItem(Item):
    game: str = "Promenade"