from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class ConstanceWebWorld(WebWorld):
    game = "Constance"

    theme = "partyTime"
    tutorials = []

    option_groups = option_groups
    options_presets = option_presets
