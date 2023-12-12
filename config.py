import os
import subprocess
from libqtile import layout, hook, bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
import fontawesome as fa
from qtile_extras import widget
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
    Group("3", label=fa.icons["terminal"], spawn=terminal),
    Group("4", label=fa.icons["code"], spawn="code", matches=[Match(wm_class="code")]),
    Group("5", label=fa.icons["cog"]),
    Group("6", label=fa.icons["folder"], spawn="alacritty -e ranger"),
    Group("7", label=fa.icons["comments"], spawn="discord", matches=[Match(wm_class="discord")]),
    Group(
        "8",
        label=fa.icons["spotify"],
        spawn="spotify-launcher",
        matches=[Match(wm_class="spotify")],
    ),
]

keynames = [i for i in "12345678"]
for keyname, group in zip(keynames, groups):
    keys.extend(
        [
            Key([mod], keyname, lazy.group[group.name].toscreen()),
            Key([mod, "shift"], keyname, lazy.window.togroup(group.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=colors_gruvbox["green_l"],
        border_normal=colors_gruvbox["dark"],
        border_width=2,
        margin=14,
        border_on_single=True,
    ),
    layout.Max(margin=20),
    layout.Floating(border_focus=colors_gruvbox["green_l"]),
    layout.Stack(
        num_stacks=2,
        border_focus=colors_gruvbox["green_l"],
        border_normal=colors_gruvbox["dark"],
        border_width=2,
        margin=14,
    ),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
        border_focus=colors_gruvbox["green_l"],
        border_normal=colors_gruvbox["dark"],
        border_width=2,
        margin=14,
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


screens = [
    Screen(
        bottom=bottom_bar(),
        top=primary_bar(),
    ),
    Screen(
        bottom= bottom_bar(),
        top=secondary_bar(),
    ),
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
        Match(wm_class="yad"),  # YAD
        Match(title="alacritty_floating"),
    ],
    border_focus=colors_gruvbox["dark"],
)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
