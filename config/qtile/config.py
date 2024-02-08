import os
import subprocess
from libqtile import layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
import fontawesome as fa
from keybindings import *
from defaults import *
from bars import *


groups = [
    Group("1", label=fa.icons["home"]),
    Group(
        "2",
        label=fa.icons["chrome"],
        spawn="google-chrome-stable",
        matches=[Match(wm_class="google-chrome")],
    ),
    Group("3", label=fa.icons["terminal"], spawn="kitty"),
    Group("4", label=fa.icons["code"]),
    Group("5", label=fa.icons["cog"]),
    Group("6", label=fa.icons["folder"]),
    Group(
        "7",
        label=fa.icons["comments"],
        matches=[Match(wm_class="discord")],
    ),
    Group(
        "8",
        label=fa.icons["spotify"],
        matches=[Match(wm_class="spotify")],
    ),
]

keynames = [i for i in "12345678"]
for keynames, group in zip(keynames, groups):
    keys.extend(
        [
            Key([mod], keynames, lazy.group[group.name].toscreen()),
            Key([mod, "shift"], keynames, lazy.window.togroup(group.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=colors_cappuccino["Green"],
        border_normal=colors_cappuccino["Lavender"],
        border_width=2,
        margin=14,
        border_on_single=True,
    ),
    layout.Max(margin=20),
    layout.Floating(border_focus=colors_cappuccino["Green"]),
    layout.Stack(
        num_stacks=2,
        border_focus=colors_cappuccino["Green"],
        border_normal=colors_cappuccino["Lavender"],
        border_width=2,
        margin=14,
    ),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
        border_focus=colors_cappuccino["Green"],
        border_normal=colors_cappuccino["Lavender"],
        border_width=2,
        margin=14,
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]


screens = [
    Screen(top=def_bar()),
    Screen(top=sec_bar()),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="gnome-disks"),  # Gnome Disk Utility
        Match(wm_class="arandr"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="yad"),  # YAD
        Match(title="k_floats"),  # kitty
    ],
    border_focus=colors_cappuccino["Blue"],
    border_width=2,
    border_normal=colors_cappuccino["Lavender"],
)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/init")
    subprocess.Popen([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
