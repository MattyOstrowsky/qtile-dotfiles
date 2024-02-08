from libqtile.config import Key
from libqtile.lazy import lazy
import os

mod = "mod4"
terminal = "kitty"

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Escape", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # volume
    Key(
        [mod],
        "F11",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/vol_control down")),
        desc="Increase System Volume",
    ),
    Key(
        [mod],
        "F12",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/vol_control up")),
        desc="Decrease System Volume",
    ),
    Key(
        [mod],
        "F1",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/bright_control down")),
        desc="Decrease Screen Brightness",
    ),
    Key(
        [mod],
        "F2",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/bright_control up")),
        desc="Increase Screen Brightness",
    ),
    Key(["control"], "m", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key(
        ["control"],
        "w",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/wifi_menu")),
        desc="Launch Wi-fi menu script",
    ),
    Key(
        ["control"],
        "b",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/blue_menu")),
        desc="Launch bluetooth menu script",
    ),
    Key(
        ["control"],
        "q",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/power_menu")),
        desc="Launch power menu script",
    ),
    Key(
        [mod],
        "F3",
        lazy.window.toggle_floating(),
    ),
    Key(
        [mod],
        "F4",
        lazy.window.toggle_maximize(),
    ),
    Key([mod, "shift"], "space", lazy.next_screen(), desc="Next monitor"),
]
