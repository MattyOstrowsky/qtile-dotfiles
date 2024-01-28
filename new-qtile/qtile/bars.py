from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from defaults import *
import os
import subprocess
from libqtile.lazy import lazy
import fontawesome as fa


widget_defaults = dict(
    foreground=colors_cappuccino["Text"], font=font_bold, fontsize=12, padding=4
)
extension_defaults = widget_defaults.copy()


def spacer_vert(decor: dict = {}):
    return widget.TextBox("|", foreground=colors_cappuccino["Overlay2"], **decor)


def parse_name(text):
    if text:
        for idx, char in enumerate(reversed(text)):
            if char in ["-", "–", "—"]:
                res = text[-idx:]
                return res[:-3] + "..." if len(res) >= 20 else res
        return " " + text
    else:
        return "Hey Booy!"


def decode_profile():
    text = subprocess.check_output(
        os.path.expanduser("~/.config/qtile/scripts/profile_perf"),
    )
    return str(text)[2:-3]


def get_kbd_bright():
    text = subprocess.check_output(
        os.path.expanduser("~/.config/qtile/scripts/kbd_bright_control"),
    )
    return "     " + str(text)[2:-3]


decor_inter = {
    "decorations": [
        RectDecoration(
            colour=colors_cappuccino["Base"], radius=12, filled=True, padding_y=4
        )
    ]
}
decor_group = {
    "decorations": [
        RectDecoration(
            colour=colors_cappuccino["Base"],
            radius=12,
            filled=True,
            padding_y=4,
            padding_x=4,
            group=True,
        )
    ]
}


def def_bar():
    return bar.Bar(
        [
            widget.Spacer(length=5, background=colors_cappuccino["Mantle"]),
            widget.TextBox(
                "   ",
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                fontsize=16,
                foreground=colors_cappuccino["Sapphire"],
                **decor_inter,
            ),
            spacer_vert(),
            widget.GroupBox(
                highlight_method="text",
                active=colors_cappuccino["Pink"],
                this_current_screen_border=colors_cappuccino["Green"],
                disable_drag=False,
                fontsize=14,
                inactive=colors_cappuccino["Subtext0"],
                **decor_inter,
            ),
            widget.WindowName(
                background=colors_cappuccino["Mantle"],
                foreground=colors_cappuccino["Overlay0"],
                format="{name}",
                parse_text=parse_name,
                width=140,
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Mantle"]),
            widget.Clock(
                format=f"   %d %a",
                fontsize=12,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 0"))
                    )
                },
            ),
            widget.TextBox(
                fa.icons["clock"],
                fontsize=12,
                padding=5,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 0"))
                    )
                },
            ),
            widget.Clock(
                format=f" %H:%M %p   ",
                fontsize=12,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 0"))
                    )
                },
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Mantle"]),
            widget.Systray(background=colors_cappuccino["Mantle"]),
            widget.Spacer(length=10, background=colors_cappuccino["Mantle"]),
            widget.CPU(
                font="Ubuntu Mono Bold",
                format="  {load_percent:5.1f}%",
                foreground=colors_cappuccino["Green"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
            ),
            spacer_vert(decor_group),
            widget.Memory(
                format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                measure_mem="G",
                foreground=colors_cappuccino["Blue"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
            ),
            spacer_vert(decor_group),
            widget.ThermalSensor(
                format="CPU {temp}°C",
                foreground=colors_cappuccino["Peach"],
                foreground_alert=colors_cappuccino["Red"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
                threshold=80.0,
            ),
            spacer_vert(decor_group),
            widget.NvidiaSensors(
                format="GPU {temp}°C   ",
                **decor_group,
                foreground=colors_cappuccino["Mauve"],
            ),
            widget.Spacer(length=10, background=colors_cappuccino["Mantle"]),
            widget.CheckUpdates(
                foreground=colors_gruvbox["red"],
                distro="Arch_checkupdates",
                display_format="    ",
                colour_have_updates=colors_cappuccino["Red"],
                colour_no_updates=colors_cappuccino["Green"],
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup update 0"))
                    )
                },
                no_update_string="   ",
                **decor_group,
            ),
            spacer_vert(decor_group),
            widget.GenPollText(
                **decor_group,
                padding=5,
                update_interval=1,
                func=decode_profile,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/qtile/scripts/profile_perf set"))
                    )
                },
            ),
            spacer_vert(decor_group),
            widget.Battery(
                **decor_group,
                charge_char="󰂄",
                discharge_char="",
                unknown_char="",
                format="{char} {percent:2.0%}",
                update_interval=5,
            ),
            spacer_vert(decor_group),
            widget.TextBox(
                fmt="⏻  ",
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup menu 0"))
                    )
                },
                foreground=colors_cappuccino["Teal"],
                fontsize=16,
                **decor_group,
            ),
            widget.Spacer(length=5, background=colors_cappuccino["Mantle"]),
        ],
        36,
        background=colors_cappuccino["Mantle"],
        margin=[4, 4, 4, 4],
    )


def sec_bar():
    return bar.Bar(
        [
            widget.Spacer(length=5, background=colors_cappuccino["Mantle"]),
            widget.TextBox(
                "   ",
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                fontsize=16,
                foreground=colors_cappuccino["Sapphire"],
                **decor_inter,
            ),
            spacer_vert(),
            widget.GroupBox(
                highlight_method="text",
                active=colors_cappuccino["Pink"],
                this_current_screen_border=colors_cappuccino["Green"],
                disable_drag=False,
                fontsize=14,
                inactive=colors_cappuccino["Subtext0"],
                **decor_inter,
            ),
            widget.WindowName(
                background=colors_cappuccino["Mantle"],
                foreground=colors_cappuccino["Overlay0"],
                format="{name}",
                parse_text=parse_name,
                width=140,
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Mantle"]),
            widget.Clock(
                format=f"   %d %a",
                fontsize=12,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 1"))
                    )
                },
            ),
            widget.TextBox(
                fa.icons["clock"],
                fontsize=12,
                padding=5,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 0"))
                    )
                },
            ),
            widget.Clock(
                format=f" %H:%M %p   ",
                fontsize=12,
                **decor_group,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup date 1"))
                    )
                },
            ),
            widget.Spacer(length=bar.STRETCH, background=colors_cappuccino["Mantle"]),
            widget.CPU(
                font="Ubuntu Mono Bold",
                format="  {load_percent:5.1f}%",
                foreground=colors_cappuccino["Green"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
            ),
            spacer_vert(decor_group),
            widget.Memory(
                format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
                measure_mem="G",
                foreground=colors_cappuccino["Blue"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
            ),
            spacer_vert(decor_group),
            widget.ThermalSensor(
                format="CPU {temp}°C",
                foreground=colors_cappuccino["Peach"],
                foreground_alert=colors_cappuccino["Red"],
                mouse_callbacks={"Button1": lazy.spawn("kitty --title k_floats btop")},
                **decor_group,
                threshold=80.0,
            ),
            spacer_vert(decor_group),
            widget.NvidiaSensors(
                format="GPU {temp}°C   ",
                **decor_group,
                foreground=colors_cappuccino["Mauve"],
            ),
            widget.Spacer(length=10, background=colors_cappuccino["Mantle"]),
            widget.Spacer(
                length=10, background=colors_cappuccino["Mantle"], **decor_group
            ),
            widget.Battery(
                **decor_group,
                charge_char="󰂄",
                discharge_char="",
                unknown_char="",
                format="{char} {percent:2.0%}",
                update_interval=5,
            ),
            spacer_vert(decor_group),
            widget.TextBox(
                fmt="⏻  ",
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        (os.path.expanduser("~/.config/eww/scripts/popup menu 1"))
                    )
                },
                foreground=colors_cappuccino["Teal"],
                fontsize=16,
                **decor_group,
            ),
            widget.Spacer(length=5, background=colors_cappuccino["Mantle"]),
        ],
        36,
        background=colors_cappuccino["Mantle"],
        margin=[4, 4, 4, 4],
    )
