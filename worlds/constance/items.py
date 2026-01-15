from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Item

from .data import check_data

if TYPE_CHECKING:
    from .world import ConstanceWorld




class ConstanceItem(Item):
    game: str = "Constance"




def get_item_infos():
    # name, type, region, classification
    names_list: list[tuple[str, str, str, str]] = [
        value for key, value in vars(check_data).items()
        if not key.startswith("_") and key not in ["item_full_name", "location_full_name"]
    ]

    item_infos = {}
    for i in range(len(names_list)):
        full_name = check_data.item_full_name(names_list[i])
        _type = names_list[i][1]
        region = names_list[i][2]
        classification = names_list[i][3]

        item_infos[full_name] = {
            "Id": i,
            "Type": _type,
            "Region": region,
            "Classification": classification
        }
    return item_infos

def get_item_name_groups():
    # name, type, region, classification
    names_list: list[tuple[str, str, str, str]] = [
        value for key, value in vars(check_data).items()
        if not key.startswith("_") and key not in ["item_full_name", "location_full_name"]
    ]

    item_name_groups: dict[str, set[str]] = {}
    for i in range(len(names_list)):
        full_name = check_data.item_full_name(names_list[i])
        _type = names_list[i][1]

        if _type in item_name_groups:
            item_name_groups[_type].add(full_name)
        else: item_name_groups[_type] = {full_name}
    return item_name_groups

def get_item_name_to_id():
    # name, type, region, classification
    names_list: list[tuple[str, str, str, str]] = [
        value for key, value in vars(check_data).items()
        if not key.startswith("_") and key not in ["item_full_name", "location_full_name"]
    ]

    item_name_to_id: dict[str, int] = {}
    for i in range(len(names_list)):
        full_name = check_data.item_full_name(names_list[i])

        item_name_to_id[full_name] = i + 1

    return item_name_to_id





def is_progression(world: ConstanceWorld, item: str) -> bool:
    return "progression" in world.item_infos[item]["Type"]

def create_all_items(world: ConstanceWorld) -> None:
    itempool: list[ConstanceItem] = []
    for item, item_info in world.item_infos.items():
        itempool.append(world.create_item(item))

    world.multiworld.itempool += itempool