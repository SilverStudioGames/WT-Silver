#Override renpy hotkeys
# Screenshot - Prnt Scrn
# Fullscreen - F11
# Reload - shift+R
init python:
    config.keymap['screenshot'] = ['K_PRINT']
    config.keymap['toggle_fullscreen'] = ['K_F11']
    config.keymap['reload_game'] = ['shift_K_r']
    config.keymap['console'].append('K_BACKQUOTE')
    config.keymap['self_voicing'] = []
    config.keymap['director'] = []
    config.keymap['hide_windows'] = []

    if config.developer:
        config.keymap['expression_editor'] = ['K_F5']

        config.underlay.append(renpy.Keymap(
            expression_editor = ToggleScreen("editor")
            ))

    # Initialize hotkey variables and functions
    # List of available inputs: http://www.pygame.org/docs/ref/key.html
    hkey_map = "m"
    hkey_work = "w"
    hkey_book = "b"
    hkey_stats = "c"
    hkey_inventory = "i"
    hkey_sleep = "s"
    hkey_fap = "f"
    hkey_summon = "d"
    hkey_ui_lock = "L"

    hkey_hide = "h"
    hkey_mhide = "mouseup_2"

    #Temp vars
    hkey_input = ""
    hkey_chat_hidden = False

# Add hotkeys to main_room screen (_main_room_.rpy)
screen hotkeys_main():
    tag hotkeys_main

    if map_unlocked:
        key hkey_map action Jump("desk")
    if letter_work_unlock.read:
        key hkey_work action Jump("paperwork")
    if store_intro_done:
        key hkey_book action Jump("read_book_menu")
    key hkey_stats action Jump("stats")
    key hkey_inventory action Jump("inventory")
    key hkey_fap action Jump("jerk_off")
    key hkey_summon action Jump("door")

    if daytime:
        key hkey_sleep action Jump("night_start") #Skip to night
    else:
        key hkey_sleep action Jump("day_start") #Skip to next day

    key hkey_ui_lock action ToggleVariable("toggle_ui_lock", False, True)

# Add hotkeys to say screen (screens.rpy)
screen hotkeys_say():
    tag hotkeys_say
    if renpy.android:
        key "game_menu" action ToggleVariable("hkey_chat_hidden", False, True)
    else:
        key hkey_hide action ToggleVariable("hkey_chat_hidden", False, True)
        key hkey_mhide action ToggleVariable("hkey_chat_hidden", False, True)
