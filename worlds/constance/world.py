from typing import Any
from collections.abc import Mapping

from BaseClasses import ItemClassification
from worlds.AutoWorld import World

from .web_world import ConstanceWebWorld
from .options import ConstanceOptions
from . import items, locations, regions, rules

class ConstanceWorld(World):
    """
    <Insert Constance descr>
    """
    game = "Constance"

    web = ConstanceWebWorld()

    options_dataclass = ConstanceOptions
    options: ConstanceOptions

    origin_region_name = "V01"
    item_name_to_id = items.get_item_name_to_id()
    item_infos = items.get_item_infos()
    item_name_groups = items.get_item_name_groups()

    location_name_to_id = locations.get_location_name_to_id()
    location_infos = locations.get_location_infos()
    event_infos = locations.get_event_infos()



    def create_item(self, item: str) -> items.ConstanceItem:
        classification = ItemClassification.progression if items.is_progression(self, item) else ItemClassification.filler
        return items.ConstanceItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> items.ConstanceItem:
        return items.ConstanceItem(event, ItemClassification.progression, None, self.player)



    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)



    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "skip_intro"
        )