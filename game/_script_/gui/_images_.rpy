#
# GUI images
#

image gui_fade:
    Solid("#000")
    alpha 0.0

    on appear:
        alpha 0.5
    on show:
        linear 0.3 alpha 0.5
    on hide:
        linear 0.3 alpha 0.0

image game_menu:
    contains:
        zoom 0.5
        "gui/main_menu/00.webp"
        pause 3
        "gui/main_menu/01.webp"
        pause.1
        "gui/main_menu/02.webp"
        pause.1
        "gui/main_menu/01.webp"
        pause.1
        "gui/main_menu/00.webp"
        pause 6
        "gui/main_menu/01.webp"
        pause.1
        "gui/main_menu/02b.webp"
        pause.1
        "gui/main_menu/01b.webp"
        pause.1
        "gui/main_menu/00b.webp"
        pause 3
        "gui/main_menu/01b.webp"
        pause.1
        "gui/main_menu/02b.webp"
        pause.1
        "gui/main_menu/01b.webp"
        pause.1
        "gui/main_menu/00b.webp"
        pause 6
        "gui/main_menu/01b.webp"
        pause.1
        "gui/main_menu/02b.webp"
        pause.1
        "gui/main_menu/02.webp"
        pause.1
        "gui/main_menu/01.webp"
        pause.1
        repeat

    contains:
        xpos -17
        ypos -151
        zoom 2.0
        "candle_fire"

    contains:
        xpos -255
        ypos 100
        zoom 0.8
        "gui/main_menu/fire00.webp"
        pause.1
        "gui/main_menu/fire01.webp"
        pause.1
        "gui/main_menu/fire02.webp"
        pause.1
        "gui/main_menu/fire03.webp"
        pause.1
        "gui/main_menu/fire04.webp"
        pause.1
        "gui/main_menu/fire05.webp"
        pause.1
        "gui/main_menu/fire06.webp"
        pause.1
        "gui/main_menu/fire07.webp"
        pause.1
        repeat

image main_menu:
    contains:
        "game_menu"

    # contains:
    #     xalign 1.0
    #     yalign 0.5
    #     xoffset -210
    #     "game_title"

image game_title:
    size (339, 242)

    contains:
        #zoom 0.9
        "gui/logos/title.webp"

    #TODO Add sparkle to game logo
    # #sparkle
    # contains:
    #     subpixel True
    #     xpos 798-682
    #     ypos 200
    #     xanchor 0.5
    #     yanchor 0.5
    #     zoom 0.0
    #     "gui/main_menu/sparkle.webp"
    #     linear 0.8 zoom 1.0
    #     linear 0.5 zoom 0.0
    #     pause 5
    #     repeat

    # #shine silver (synchronized)
    # contains:
    #     subpixel True
    #     xpos 848-682
    #     ypos 230-12
    #     xanchor 0.5
    #     yanchor 0.5
    #     zoom 0.0
    #     "gui/main_menu/sparkle.webp"
    #     pause 1.3
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 870-682
    #     ypos 205-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 914-682
    #     ypos 227-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 948-682
    #     ypos 233-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 999-682
    #     ypos 226-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0
    #     pause 12.6
    #     repeat

image candle_fire:
    "gui/main_menu/candle/fire_01.webp"
    pause.1
    "gui/main_menu/candle/fire_02.webp"
    pause.1
    "gui/main_menu/candle/fire_03.webp"
    pause.1
    "gui/main_menu/candle/fire_04.webp"
    pause.1
    "gui/main_menu/candle/fire_05.webp"
    pause.1
    "gui/main_menu/candle/fire_06.webp"
    pause.1
    "gui/main_menu/candle/fire_07.webp"
    pause.1
    "gui/main_menu/candle/fire_08.webp"
    pause.1
    "gui/main_menu/candle/fire_09.webp"
    pause.1
    "gui/main_menu/candle/fire_10.webp"
    pause.1
    repeat

image discord_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/discord.webp"

image discord_hover:
    zoom 0.55
    "gui/logos/discord.webp"

image patreon_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/patreon.webp"

image patreon_hover:
    zoom 0.55
    "gui/logos/patreon.webp"

image silverstudiogames_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/silverstudiogames.webp"

image silverstudiogames_hover:
    zoom 0.55
    "gui/logos/silverstudiogames.webp"


# Sliders

image slider_horizontal_idle_thumb = Solid(gui.idle_color, xsize=gui.thumb_size)

image slider_horizontal_hover_thumb = Solid(gui.hover_color, xsize=gui.thumb_size)

image slider_horizontal_idle_bar = Solid(gui.muted_color)

image slider_horizontal_hover_bar = Solid(gui.hover_muted_color)

image slider_vertical_idle_thumb = Solid(gui.idle_color, ysize=gui.thumb_size)

image slider_vertical_hover_thumb = Solid(gui.hover_color, ysize=gui.thumb_size)

image slider_vertical_idle_bar = Solid(gui.muted_color)

image slider_vertical_hover_bar = Solid(gui.hover_muted_color)


# Scrollbars

image scrollbar_horizontal_idle_thumb = Solid(gui.accent_color)

image scrollbar_horizontal_hover_thumb = Solid(gui.hover_color)

image scrollbar_horizontal_idle_bar = Solid(gui.muted_color)

image scrollbar_horizontal_hover_bar = Solid(gui.hover_muted_color)

image scrollbar_vertical_idle_thumb = Solid(gui.accent_color)

image scrollbar_vertical_hover_thumb = Solid(gui.hover_color)

image scrollbar_vertical_idle_bar = Solid(gui.muted_color)

image scrollbar_vertical_hover_bar = Solid(gui.hover_muted_color)


# Bars

image bar_idle_fill = Solid(gui.idle_color)

image bar_hover_fill = Solid(gui.hover_color)

image bar_idle_empty = Solid(gui.muted_color)

image bar_hover_empty = Solid(gui.hover_muted_color)
