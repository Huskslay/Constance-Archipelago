from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, DefaultOnToggle


class SkipIntro(DefaultOnToggle):
    """
    Skip the intro to the game
    """

    display_name = "Skip Intro"


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class ConstanceOptions(PerGameCommonOptions):
    skip_intro: SkipIntro


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "General Options",
        [SkipIntro],
    ),
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "default": {
        "skip_intro": True
    }
}
