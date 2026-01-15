from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Location

from .data import check_data, event_data
from .items import ConstanceItem

if TYPE_CHECKING:
    from .world import ConstanceWorld




class ConstanceLocation(Location):
    game: str = "Constance"




def get_location_infos():
    # name, type, region, classification
    location_list: list[tuple[str, str, str, str]] = [
        value for key, value in vars(check_data).items()
        if not key.startswith("_") and key not in ["item_full_name", "location_full_name"]
    ]

    location_infos = {}
    for i in range(len(location_list)):
        full_name = check_data.location_full_name(location_list[i])
        _type = location_list[i][1]
        region = location_list[i][2]

        location_infos[full_name] = {
            "Id": i,
            "Type": _type,
            "Region": region
        }
    return location_infos

def get_location_name_to_id():
    # name, type, region, classification
    location_list: list[tuple[str, str, str, str]] = [
        value for key, value in vars(check_data).items()
        if not key.startswith("_") and key not in ["item_full_name", "location_full_name"]
    ]

    location_name_to_id: dict[str, int] = {}
    for i in range(len(location_list)):
        full_name = check_data.location_full_name(location_list[i])
        location_name_to_id[full_name] = i + 1
    return location_name_to_id


def get_event_infos():
    # name, location name, region
    event_list: list[tuple[str, str, str]] = [
        value for key, value in vars(event_data).items()
        if not key.startswith("_")
    ]
    event_infos = {}
    for i in range(len(event_list)):
        name = event_list[i][0]
        location_name = event_list[i][1]
        region = event_list[i][2]

        event_infos[name] = {
            "Location Name": location_name,
            "Region": region
        }
    return event_infos




def create_all_locations(world: ConstanceWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ConstanceWorld) -> None:
    for location, location_info in world.location_infos.items():
        _region = world.get_region(location_info["Region"])
        _region.locations.append(
            ConstanceLocation(
                world.player,
                location,
                world.location_name_to_id[location],
                _region
            )
        )

def create_events(world: ConstanceWorld) -> None:
    for event, event_info in world.event_infos.items():
        _region = world.get_region(event_info["Region"])

        _region.add_event(
            event_info["Location Name"],
            event,
            location_type=ConstanceLocation,
            item_type=ConstanceItem
        )