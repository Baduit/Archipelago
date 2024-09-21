from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .items import PromenadeItem, item_table
from .locations import location_table, PromenadeLocation
from .names.region_names import RegionName
from .regions import dynamic_entrance_list, static_entrance_list


class PokemonWebWorld(WebWorld):    
    item_descriptions  = {
        "todo": "todo",
    }


class Promenade(World):
    """2D Collectathon """
    game = "Promenade"
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 788569
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for id, name in enumerate(item_table.keys(), base_id)}
    location_name_to_id = {name: id for id, name in enumerate(location_table.keys(), base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "weapons": {"sword", "lance"},
    # }

    def create_item(self, item: str) -> Item:
        return PromenadeItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)

    def create_regions(self) -> None:
        for name in RegionName:
            region = Region(name.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

            locations = [ PromenadeLocation(self.player, location_name, None, region) for location_name, location_data in location_table.items() if location_data.region == name ]
            region.locations += locations

        for entrance_data in dynamic_entrance_list:
            start = self.multiworld.get_region(entrance_data.start.name, self.player)
            destination = self.multiworld.get_region(entrance_data.destination.name, self.player)

            # Condition is not set for the moment
            start.connect(destination)