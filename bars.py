from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from defaults import *
import os
import subprocess
from libqtile.lazy import lazy
import fontawesome as fa


widget_defaults = dict(
    background=colors_gruvbox["dark"],
    foreground=colors_gruvbox["fg_0"],
    font=font_bold,
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()
def parse_name(text):
    if text:
        for idx, char in enumerate(reversed(text)):
            if char in ["-", "–", "—"]:
                res = text[-idx:]
                return res[:-3] + "..." if len(res) >= 20 else res
        return " " + text
    else:
        return "Hey Booy!"


def right_rounded():
    right = {
        "decorations": [PowerLineDecoration(path="rounded_right", size=14, shift=12)]
    }
    return widget.TextBox(background=colors_gruvbox["transparent"], **right)


def left_rounded():
    left = {
        "decorations": [PowerLineDecoration(path="rounded_left", size=14, shift=12)]
    }
    return widget.TextBox(background=colors_gruvbox["dark"], **left)

def bottom_bar():
    return bar.Bar(
            [
                widget.WindowTabs(
                    background=colors_gruvbox["transparent"], font=font_regular
                ),
                widget.Spacer(
                    length=bar.STRETCH, background=colors_gruvbox["transparent"]
                ),
                widget.CurrentLayout(background=colors_gruvbox["transparent"]),
            ],
            20,
            background=colors_gruvbox["transparent"],
        )
def primary_bar():
    return bar.Bar(
            [
                right_rounded(),
                widget.TextBox(
                    "",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                    padding=5,
                    fontsize=16,
                ),widget.TextBox("|"),
                widget.GroupBox(
                    highlight_method="text",
                    active=colors_gruvbox["aqua"],
                    this_current_screen_border=colors_gruvbox["yellow_l"],
                    disable_drag=True,
                    fontsize=14,
                ),
                left_rounded(),
                widget.WindowName(
                    background=colors_gruvbox["transparent"],
                    foreground=colors_gruvbox["dark_2"],
                    format="{name}",
                    parse_text=parse_name,
                    width=140,
                ),
                widget.Spacer(length=425, background=colors_gruvbox["transparent"]),
                right_rounded(),
                widget.Clock(
                    format=f" %d %a ", fontsize=12
                ),widget.TextBox(fa.icons['clock'], fontsize=14),
                widget.Clock(
                    format=f" %H:%M %p ", fontsize=12
                ),
                left_rounded(),
                widget.Spacer(
                    length=bar.STRETCH, background=colors_gruvbox["transparent"]
                ),
                widget.Systray(background=colors_gruvbox["transparent"]),
                right_rounded(),
                widget.TextBox("", foreground=colors_gruvbox["red"], fontsize=14),
                widget.CPU(
                    format="{load_percent:>4}%",foreground=colors_gruvbox["yellow"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },
                ),
                widget.TextBox("|"),
                widget.ThermalSensor(foreground=colors_gruvbox["purple"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },),
                widget.TextBox("|"),
                widget.Memory(
                    format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                    measure_mem="G",foreground=colors_gruvbox["blue"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },
                ),
                widget.TextBox("|"),
                widget.Net(format="{down} ↓↑ {up}",foreground=colors_gruvbox["aqua"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },),
                left_rounded(),
                widget.Spacer(length=10, background=colors_gruvbox["transparent"]),
                right_rounded(),
                widget.CheckUpdates(
                    foreground=colors_gruvbox["red"],
                    distro="Arch_checkupdates",
                    display_format="{updates}",
                    colour_have_updates=colors_gruvbox["red"],
                    colour_no_updates=colors_gruvbox["green"],
                    mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -e yay")
                    },
                    no_update_string=" ",
                ),
                widget.TextBox("|"),
                widget.GenPollText(
                    update_interval=5,
                    max_chars=10,
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            os.path.expanduser("~/.config/qtile/Scripts/blue_menu")
                        )
                    },
                    func=lambda: " {}".format(
                        subprocess.check_output(
                            os.path.expanduser("~/.config/qtile/Scripts/blue_text")
                        ).decode("utf-8")
                    ),
                ),
                widget.TextBox("|"),
                widget.GenPollText(
                    update_interval=5,
                    max_chars=10,
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            os.path.expanduser("~/.config/qtile/Scripts/wifi_menu")
                        )
                    },
                    func=lambda: " {}".format(
                        subprocess.check_output(
                            os.path.expanduser("~/.config/qtile/Scripts/wifi_text")
                        ).decode("utf-8")
                    ),
                ),
                widget.TextBox("|"),
                widget.TextBox(""),
                widget.PulseVolume(
                    volume_app="pamixer",
                    get_volume_command="pamixer --get-volume",
                    mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
                ),
                widget.TextBox("|"),
                widget.TextBox("盛"),
                widget.Backlight(backlight_name="intel_backlight"),
                widget.TextBox(
                    "|",
                ),
                widget.GenPollText(
                    update_interval=5,
                    func=lambda: "{}%".format(
                        subprocess.check_output(
                            os.path.expanduser("~/.config/qtile/Scripts/bat_poll")
                        ).decode("utf-8")
                    ),
                ),
                widget.TextBox("|", background=colors_gruvbox["dark"]),
                widget.TextBox(
                    fa.icons["power-off"],
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            (os.path.expanduser("~/.config/qtile/Scripts/power_menu"))
                        )
                    },foreground=colors_gruvbox["yellow_l"],fontsize=14
                ),
                left_rounded(),
            ],
            26,
            background=colors_gruvbox["transparent"],
            margin=[4, 4, 4, 4],
        )


def secondary_bar():
    return bar.Bar(
            [
                right_rounded(),
                widget.TextBox(
                    "",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                    padding=5,
                    fontsize=16,
                ),widget.TextBox("|"),
                widget.GroupBox(
                    highlight_method="text",
                    active=colors_gruvbox["aqua"],
                    this_current_screen_border=colors_gruvbox["yellow_l"],
                    disable_drag=True,
                    fontsize=14,
                ),
                left_rounded(),
                widget.WindowName(
                    background=colors_gruvbox["transparent"],
                    foreground=colors_gruvbox["dark_2"],
                    format="{name}",
                    parse_text=parse_name,
                    width=140,
                ),
                widget.Spacer(length=425, background=colors_gruvbox["transparent"]),
                right_rounded(),
                widget.Clock(
                    format=f" %d %a ", fontsize=12
                ),widget.TextBox(fa.icons['clock'], fontsize=14),
                widget.Clock(
                    format=f" %H:%M %p ", fontsize=12
                ),
                left_rounded(),
                widget.Spacer(
                    length=bar.STRETCH, background=colors_gruvbox["transparent"]
                ),
                right_rounded(),
                widget.TextBox("", foreground=colors_gruvbox["red"], fontsize=14),
                widget.CPU(
                    format="{load_percent:>4}%",foreground=colors_gruvbox["yellow"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },
                ),
                widget.TextBox("|"),
                widget.ThermalSensor(foreground=colors_gruvbox["purple"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },),
                widget.TextBox("|"),
                widget.Memory(
                    format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                    measure_mem="G",foreground=colors_gruvbox["blue"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },
                ),
                widget.TextBox("|"),
                widget.Net(format="{down} ↓↑ {up}",foreground=colors_gruvbox["aqua"],mouse_callbacks={
                        "Button1": lazy.spawn("alacritty -t alacritty_floating --hold -o 'window.dimensions.columns=100' -o 'window.dimensions.lines=30' -e htop ")
                    },),
                left_rounded(),
            ],
            26,
            background=colors_gruvbox["transparent"],
            margin=[4, 4, 4, 4],
        )

