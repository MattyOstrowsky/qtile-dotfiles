from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from defaults import *
import os
import subprocess
from libqtile.lazy import lazy
import fontawesome as fa


widget_defaults = dict(
    foreground=colors_cappuccino["Text"],
    font=font_bold,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def spacer_vert():
    return widget.TextBox(
        "|",
        background=colors_cappuccino["Base"],
        foreground=colors_cappuccino["Overlay2"],
    )


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
        "decorations": [
            PowerLineDecoration(path="rounded_right", size=8, shift=25, filled=True)
        ]
    }
    return widget.TextBox(background=colors_cappuccino["Crust"], **right)


def decode_profile():
    text = subprocess.check_output(
        os.path.expanduser("~/.config/qtile/scripts/profile_perf"),
    )
    return str(text)[2:-3]


def left_rounded():
    left = {"decorations": [PowerLineDecoration(path="rounded_left", size=8, shift=12)]}
    return widget.TextBox(background=colors_cappuccino["Base"], **left)


def def_bar():
    return bar.Bar(
        [
            right_rounded(),
            widget.TextBox(
                " ",
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                padding=5,
                fontsize=16,
                background=colors_cappuccino["Base"],
                foreground=colors_cappuccino["Sapphire"],
            ),
            spacer_vert(),
            widget.GroupBox(
                highlight_method="text",
                active=colors_cappuccino["Pink"],
                this_current_screen_border=colors_cappuccino["Green"],
                disable_drag=False,
                fontsize=14,
                background=colors_cappuccino["Base"],
                inactive=colors_cappuccino["Subtext0"],
            ),
            left_rounded(),
            widget.WindowName(
                background=colors_cappuccino["Crust"],
                foreground=colors_cappuccino["Overlay0"],
                format="{name}",
                parse_text=parse_name,
                width=140,
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.Clock(
                format=f" %d %a", fontsize=12, background=colors_cappuccino["Base"]
            ),
            widget.TextBox(
                fa.icons["clock"],
                fontsize=14,
                padding=5,
                background=colors_cappuccino["Base"],
            ),
            widget.Clock(
                format=f" %H:%M %p ", fontsize=12, background=colors_cappuccino["Base"]
            ),
            left_rounded(),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Crust"]),
            widget.Systray(background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.Backlight(
                backlight_name="intel_backlight",
                background=colors_cappuccino["Base"],
                mouse_callbacks={"Button1": lazy.spawn("arandr")},
            ),
            spacer_vert(),
            widget.Volume(
                fmt="  {}",
                background=colors_cappuccino["Base"],
                mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
            ),
            left_rounded(),
            widget.Spacer(length=10, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.CPU(
                format="{load_percent:>4}%",
                foreground=colors_cappuccino["Green"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
            ),
            spacer_vert(),
            widget.Memory(
                format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                measure_mem="G",
                foreground=colors_cappuccino["Blue"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
            ),
            spacer_vert(),
            widget.ThermalSensor(
                format="CPU {temp}°C",
                foreground=colors_cappuccino["Peach"],
                foreground_alert=colors_cappuccino["Red"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
                threshold=80.0,
            ),
            spacer_vert(),
            widget.NvidiaSensors(
                format="GPU {temp}°C",
                background=colors_cappuccino["Base"],
                foreground=colors_cappuccino["Mauve"],
            ),
            spacer_vert(),
            widget.Battery(
                background=colors_cappuccino["Base"],
                format="{watt:.2f}W",
                update_interval=1,
                foreground=colors_cappuccino["Pink"],
            ),
            left_rounded(),
            widget.Spacer(length=10, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.CheckUpdates(
                foreground=colors_gruvbox["red"],
                distro="Arch_checkupdates",
                display_format="  {updates}",
                colour_have_updates=colors_cappuccino["Red"],
                colour_no_updates=colors_cappuccino["Green"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats yay")},
                no_update_string=" ",
                background=colors_cappuccino["Base"],
            ),
            spacer_vert(),
            widget.GenPollText(
                background=colors_cappuccino["Base"],
                padding=5,
                update_interval=1,
                func=decode_profile,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/qtile/scripts/profile_perf set"))
                    )
                },
            ),
            spacer_vert(),
            widget.Battery(
                background=colors_cappuccino["Base"],
                charge_char="󰂄",
                discharge_char="",
                unknown_char="",
                format="{char} {percent:2.0%}",
                update_interval=5,
            ),
            spacer_vert(),
            widget.TextBox(
                fa.icons["power-off"],
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup menu 0"))
                    )
                },
                foreground=colors_cappuccino["Teal"],
                fontsize=16,
                background=colors_cappuccino["Base"],
                padding=6,
            ),
            left_rounded(),
        ],
        30,
        background=colors_cappuccino["Crust"],
        margin=[4, 4, 4, 4],
    )


def sec_bar():
    return bar.Bar(
        [
            right_rounded(),
            widget.TextBox(
                " ",
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                padding=5,
                fontsize=16,
                background=colors_cappuccino["Base"],
                foreground=colors_cappuccino["Sapphire"],
            ),
            spacer_vert(),
            widget.GroupBox(
                highlight_method="text",
                active=colors_cappuccino["Pink"],
                this_current_screen_border=colors_cappuccino["Green"],
                disable_drag=False,
                fontsize=14,
                background=colors_cappuccino["Base"],
                inactive=colors_cappuccino["Subtext0"],
            ),
            left_rounded(),
            widget.WindowName(
                background=colors_cappuccino["Crust"],
                foreground=colors_cappuccino["Overlay0"],
                format="{name}",
                parse_text=parse_name,
                width=140,
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.Clock(
                format=f" %d %a", fontsize=12, background=colors_cappuccino["Base"]
            ),
            widget.TextBox(
                fa.icons["clock"],
                fontsize=14,
                padding=5,
                background=colors_cappuccino["Base"],
            ),
            widget.Clock(
                format=f" %H:%M %p ", fontsize=12, background=colors_cappuccino["Base"]
            ),
            left_rounded(),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.Backlight(
                backlight_name="intel_backlight",
                background=colors_cappuccino["Base"],
                mouse_callbacks={"Button1": lazy.spawn("arandr")},
            ),
            spacer_vert(),
            widget.Volume(
                fmt="  {}",
                background=colors_cappuccino["Base"],
                mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
            ),
            left_rounded(),
            widget.Spacer(length=10, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.CPU(
                format="{load_percent:>4}%",
                foreground=colors_cappuccino["Green"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
            ),
            spacer_vert(),
            widget.Memory(
                format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                measure_mem="G",
                foreground=colors_cappuccino["Blue"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
            ),
            spacer_vert(),
            widget.ThermalSensor(
                format="CPU {temp}°C",
                foreground=colors_cappuccino["Peach"],
                foreground_alert=colors_cappuccino["Red"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                background=colors_cappuccino["Base"],
                threshold=80.0,
            ),
            spacer_vert(),
            widget.NvidiaSensors(
                format="GPU {temp}°C",
                background=colors_cappuccino["Base"],
                foreground=colors_cappuccino["Mauve"],
            ),
            spacer_vert(),
            widget.Battery(
                background=colors_cappuccino["Base"],
                format="{watt:.2f}W",
                update_interval=1,
                foreground=colors_cappuccino["Pink"],
            ),
            left_rounded(),
            widget.Spacer(length=10, background=colors_cappuccino["Crust"]),
            right_rounded(),
            widget.Battery(
                background=colors_cappuccino["Base"],
                charge_char="󰂄",
                discharge_char="",
                unknown_char="",
                format="{char} {percent:2.0%}",
                update_interval=5,
            ),
            spacer_vert(),
            widget.TextBox(
                fa.icons["power-off"],
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup menu 1"))
                    )
                },
                foreground=colors_cappuccino["Teal"],
                fontsize=16,
                background=colors_cappuccino["Base"],
                padding=6,
            ),
            left_rounded(),
        ],
        30,
        background=colors_cappuccino["Crust"],
        margin=[4, 4, 4, 4],
    )
