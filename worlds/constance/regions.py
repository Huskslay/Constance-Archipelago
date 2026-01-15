from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Region

from .data import region_data, entrance_data

if TYPE_CHECKING:
    from .world import ConstanceWorld




# name, entrances, locations
region_list: list[tuple[str, str, str]] = [
    value for key, value in vars(region_data).items()
    if not key.startswith("_")
]
region_infos = {}
for i in range(len(region_list)):
    name = region_list[i][0]
    entrances = region_list[i][1]
    locations = region_list[i][2]

    region_infos[name] = {
        "Entrances": entrances,
        "Locations": locations
    }

# name, parent, connection
entrance_list: list[tuple[str, str, str]] = [
    value for key, value in vars(entrance_data).items()
    if not key.startswith("_")
]
entrance_infos = {}
for i in range(len(entrance_list)):
    name = entrance_list[i][0]
    parent = entrance_list[i][1]
    connection = entrance_list[i][2]

    entrance_infos[name] = {
        "Parent": parent,
        "Connection": connection
    }




def create_and_connect_regions(world: ConstanceWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ConstanceWorld) -> None:
    regions: list[Region] = []
    for region, region_info in region_infos.items():
        regions.append(Region(region, world.player, world.multiworld))
    world.multiworld.regions += regions

def connect_regions(world: ConstanceWorld) -> None:
    for entrance, entrance_info in entrance_infos.items():
        _parent = world.get_region(entrance_info["Parent"])
        _connection = world.get_region(entrance_info["Connection"])

        _parent.connect(_connection, name)