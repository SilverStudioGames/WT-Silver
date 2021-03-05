
init -100 python:
    # Custom hotkeys

    config.keymap = dict(

        # Custom

        map = ["K_m"],
        work = ["K_w"],
        stats = ["K_c"],
        inventory = ["K_i"],
        sleep = ["K_s"],
        fap = ["K_f"],
        summon = ["K_d"],

        # Bindings present almost everywhere, unless explicitly disabled.
        rollback = ["K_PAGEUP", "repeat_K_PAGEUP", "K_AC_BACK", "mousedown_4"],
        screenshot = ["K_PRINT"],
        #toggle_afm = [],
        toggle_fullscreen = ["alt_K_RETURN", "alt_K_KP_ENTER", "K_F11"],
        game_menu = ["K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3"],
        hide_windows = ["mouseup_2", "h", "noshift_K_h"],
        help = ["K_F1", "meta_shift_/"],
        choose_renderer = ["alt_shift_K_g", "shift_K_g"],
        progress_screen = ["alt_shift_K_p", "meta_shift_K_p", "K_F2"],
        accessibility = ["shift_K_a"],

        # Accessibility.
        self_voicing = ["shift_K_v"],
        clipboard_voicing = ["alt_shift_K_c", "shift_K_c"],
        debug_voicing = ["alt_shift_K_v", "meta_shift_K_v"],

        # Say.
        rollforward = ["mousedown_5", "K_PAGEDOWN", "repeat_K_PAGEDOWN"],
        dismiss = ["mouseup_1", "K_RETURN", "K_SPACE", "K_KP_ENTER", "K_SELECT"],
        dismiss_unfocused = [],

        # Focus.
        focus_left = ["K_LEFT", "repeat_K_LEFT"],
        focus_right = ["K_RIGHT", "repeat_K_RIGHT"],
        focus_up = ["K_UP", "repeat_K_UP"],
        focus_down = ["K_DOWN", "repeat_K_DOWN"],

        # Button.
        button_ignore = ["mousedown_1"],
        button_select = ["mouseup_1", "K_RETURN", "K_KP_ENTER", "K_SELECT"],
        button_alternate = ["mouseup_3"],
        button_alternate_ignore = ["mousedown_3"],

        # Input.
        input_backspace = ["K_BACKSPACE", "repeat_K_BACKSPACE"],
        input_enter = ["K_RETURN", "K_KP_ENTER"],
        input_left = ["K_LEFT", "repeat_K_LEFT"],
        input_right = ["K_RIGHT", "repeat_K_RIGHT"],
        input_up = ["K_UP", "repeat_K_UP"],
        input_down = ["K_DOWN", "repeat_K_DOWN"],
        input_delete = ["K_DELETE", "repeat_K_DELETE"],
        input_home = ["K_HOME"],
        input_end = ["K_END"],
        input_copy = ["ctrl_noshift_K_INSERT", "ctrl_noshift_K_c"],
        input_paste = ["shift_K_INSERT", "ctrl_noshift_K_v"],

        # Viewport.
        viewport_leftarrow = ["K_LEFT", "repeat_K_LEFT"],
        viewport_rightarrow = ["K_RIGHT", "repeat_K_RIGHT"],
        viewport_uparrow = ["K_UP", "repeat_K_UP"],
        viewport_downarrow = ["K_DOWN", "repeat_K_DOWN"],
        viewport_wheelup = ["mousedown_4"],
        viewport_wheeldown = ["mousedown_5"],
        viewport_drag_start = ["mousedown_1"],
        viewport_drag_end = ["mouseup_1"],
        viewport_pageup = ["K_PAGEUP", "repeat_K_PAGEUP"],
        viewport_pagedown = ["K_PAGEDOWN", "repeat_K_PAGEDOWN"],

        # These keys control skipping.
        skip = ["K_LCTRL", "K_RCTRL"],
        stop_skipping = [],
        toggle_skip = ["K_TAB"],
        fast_skip = [">", "shift_K_PERIOD"],

        # Bar.
        bar_activate = ["mousedown_1", "K_RETURN", "K_KP_ENTER", "K_SELECT"],
        bar_deactivate = ["mouseup_1", "K_RETURN", "K_KP_ENTER", "K_SELECT"],
        bar_left = ["K_LEFT", "repeat_K_LEFT"],
        bar_right = ["K_RIGHT", "repeat_K_RIGHT"],
        bar_up = ["K_UP", "repeat_K_UP"],
        bar_down = ["K_DOWN", "repeat_K_DOWN"],

        # Delete a save.
        save_delete = ["K_DELETE"],

        # Draggable.
        drag_activate = ["mousedown_1"],
        drag_deactivate = ["mouseup_1"],

        # Debugging and development.
        editor = ["K_F5"],
        reload_game = ["shift_K_r"],
        console = ["shift_K_o", "alt_shift_K_o", "K_BACKQUOTE"],
        console_older = ["K_UP", "repeat_K_UP"],
        console_newer = ["K_DOWN", "repeat_K_DOWN"],
        #director = ["noshift_K_d"],
        #launch_editor = ["E", "shift_K_e"],
        #dump_styles = [],
        #developer = ["shift_K_d", "alt_shift_K_d"],
        #quit = [],
        #iconify = [],
        #inspector = ["I", "shift_K_i"],
        full_inspector = ["alt_shift_K_i"],
        dismiss_hard_pause = ["K_PAUSE", "K_BREAK"],

        # Ignored (kept for backwards compatibility).
        toggle_music = ["m"],
        viewport_up = ["mousedown_4"],
        viewport_down = ["mousedown_5"],

        # Profile commands.
        performance = ["K_F3"],
        image_load_log = ["K_F4"],
        profile_once = ["K_F8"],
        memory_profile = ["K_F7"],
    )

    def _hide_windows():
        global _windows_hidden
        _windows_hidden = not _windows_hidden
        renpy.restart_interaction()

    _default_keymap = renpy.Keymap(
        rollback = renpy.rollback,
        screenshot = _screenshot,
        toggle_fullscreen = renpy.toggle_fullscreen,
        #toggle_afm = _keymap_toggle_afm,
        toggle_skip = _keymap_toggle_skipping,
        fast_skip = _fast_skip,
        game_menu = _invoke_game_menu,
        hide_windows = _hide_windows,
        #launch_editor = _launch_editor,
        reload_game = _reload_game,
        #developer = _developer,
        quit = renpy.quit_event,
        #iconify = renpy.iconify,
        help = _help,
        choose_renderer = ShowMenu("preferences", page="visuals"),
        console = _console.enter,
        profile_once = _profile_once,
        memory_profile = _memory_profile,
        self_voicing = Preference("self voicing", "toggle"),
        clipboard_voicing = Preference("clipboard voicing", "toggle"),
        debug_voicing = Preference("debug voicing", "toggle"),
        progress_screen = _progress_screen,
        #director = director.Start(),
        performance = ToggleScreen("_performance"),
        accessibility = ShowMenu("preferences", page="accessibility"),
        editor = ToggleScreen("editor"),
        )

    config.underlay = [ _default_keymap ]

# Add hotkeys to main_room screen (_main_room_.rpy)
screen hotkeys_main():
    tag hotkeys_main

    if map_unlocked:
        key "map" action Jump("desk")
    if letter_work_unlock.read:
        key "work" action Jump("paperwork")

    key "stats" action Jump("stats")
    key "inventory" action Jump("inventory")
    key "fap" action Jump("jerk_off")
    key "summon" action Jump("door")
    key "sleep" action If(game.daytime, Jump("night_start"), Jump("day_start"))
