
# The game starts here
label start:
    call game_init
    jump start_wt

# Quickstart for developer mode
label start_dev:
    call game_init
    $ game.difficulty = 2
    $ game.cheats = True
    $ use_cgs = True

    call screen loading

    jump skip_to_hermione

label game_init:
    $ wardrobe_init()
    $ achievement_fix()
    $ parse_mods()

    if not renpy.android:
        show screen tooltip
    return

init python:
    renpy.music.register_channel("bg_sounds", "sfx", True)
    renpy.music.register_channel("weather", "weather", True)
