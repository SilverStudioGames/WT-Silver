########################################################
##                  Initialization                    ##
########################################################

init offset = -1

########################################################
##                  Special Screens                   ##
##         For information please refer to:           ##
## https://www.renpy.org/doc/html/screen_special.html ##
########################################################

screen say(who, what, side_image=None):
    zorder 30
    use hotkeys_say

    if hkey_chat_hidden:
        use invisible_button(action=SetVariable("hkey_chat_hidden", False))
    else:
        if not renpy.get_screen("choice"):
            use invisible_button(action=Function(ui.saybehavior), keysym="dismiss")

    if side_image:
        add side_image yalign 1.0 yanchor 1.0 zoom 0.5

    style_prefix interface_style

    window id "window":

        if hkey_chat_hidden:
            ypos 1000

        if _game_menu_screen:
            use quick_menu

        if who:
            window:
                style_prefix "say_who"
                text who id "who":
                    color (preferences.text_color_day if interface_color == "gold" else preferences.text_color_night)
                    outlines [(1, preferences.text_outline, 1, 0)]

        text what id "what":
            color (preferences.text_color_day if interface_color == "gold" else preferences.text_color_night)
            outlines [(1, preferences.text_outline, 1, 0)]

screen quick_menu():
    hbox:
        style_group "quick"
        xalign 1.0
        yoffset -30

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Preferences") action ShowMenu("preferences")

    if renpy.android:
        imagebutton idle "interface/frames/"+interface_color+"/arrow.webp" action Rollback() xoffset -120 yalign 0.5 yanchor 0.5
        imagebutton idle im.Flip("interface/frames/"+interface_color+"/arrow.webp", horizontal=True) action Skip(fast=True, confirm=True) xoffset 600 yalign 0.5 yanchor 0.5

screen choice(items):
    tag menu
    zorder 30

    # Dont add the fade if character or saybox is present (They have their own triggers for fading)
    if not any(itertools.imap(renpy.get_screen, ["say", "hermione_main", "cho_main", "luna_main", "snape_main", "astoria_main", "tonks_main", "susan_main", "letter"])):
        add "interface/bld.webp" at fade_hide(0.15)

    window at fade_show_hide(0.15):
        style "empty"
        xalign menu_x
        yalign menu_y

        vbox:
            style_prefix interface_style + "_menu"
            spacing 0
            $ choice_width = int(config.screen_width/2)

            $ max_progress = max([len(e.kwargs.get("progress", [])) for e in items])

            for i, entry in enumerate(items, 1):
                button:
                    xsize choice_width
                    ypadding 5
                    action entry.action
                    if i < 10 and entry.action:
                        keysym (str(i), "K_KP"+str(i))
                    sensitive bool(entry.action)
                    fixed:
                        fit_first "height"
                        text entry.caption:
                            xsize choice_width-120 # Leave enough margin for number and icon
                            align (0.5, 0.5)
                        if i < 10 and entry.action:
                            text "{size=-2}[i].{/size}" xpos 5 yalign 0.5

                        $ icon = entry.kwargs.get("icon", None)
                        if icon:
                            add icon xcenter 40 yalign 0.5

                        $ progress = entry.kwargs.get("progress", None)
                        if progress:
                            hbox:
                                spacing 2
                                xpos choice_width - 5
                                align (1.0, 0.5)
                                for i in xrange(0, max_progress):
                                    if i < len(progress):
                                        add progress[i]
                                    else:
                                        null width 21 # Assume icon width

screen input(prompt):
    zorder 30

    style_prefix "say"
    window:
        id "window"

        if prompt:
            window:
                style_prefix "say_who"
                text prompt:
                    align (0.5, 0.5)
                    color (preferences.text_color_day if interface_color == "gold" else preferences.text_color_night)
                    outlines [(1, preferences.text_outline, 1, 0)]

        input id "input":
            color (preferences.text_color_day if interface_color == "gold" else preferences.text_color_night)
            outlines [(1, preferences.text_outline, 1, 0)]

screen nvl(dialogue, items=None):
    null

screen main_menu():
    tag menu
    zorder 5

    window:
        style "mm_root"

    text "{color=#fff}{size=-2}[title_version]{/size}{/color}" xpos 1024 ypos 228 outlines [ (1, "#000", 0, 0) ]
    if not is_release:
        vbox:
            pos (10, 10)
            text "{color=#c70000}EXPERIMENTAL VERSION{/color}" size 24 outlines [(2, "#000", 0, 0)]
            text "Expect bugs, crashes and other weird stuff." color "#fff" size 12 outlines [(2, "#000", 0, 0)]
            text "Proceed at your own risk, you have been warned!" color "#fff" size 12 outlines [(2, "#000", 0, 0)]
            text "You can find the most recent stable build on our {a=https://pastebin.com/6zbuZ5gS}pastebin{/a}" color "#fff" size 12 outlines [(2, "#000", 0, 0)]

    vbox:
        style_prefix "mm"
        spacing 10
        align (1.0, 1.0)
        offset (-40, -80)

        if update_available:
            frame:
                has vbox
                textbutton _("{size=-6}{color=#c70000}UPDATE AVAILABLE{/color}{/size}") action OpenURL("https://pastebin.com/6zbuZ5gS")

        frame:
            has vbox

            if not persistent.game_complete:
                textbutton _("New Game") action Start()
            else:
                textbutton _("New Game {size=+3}+{/size}") action Start()
            if config.developer:
                textbutton "Quick start" action Start("start_dev")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Quit") action Quit(confirm=False)

        frame:
            has vbox
            textbutton _("Credits") action Jump("credits")

    imagebutton:
        xpos 910
        ypos 560
        xalign 0.5
        yalign 0.5
        idle "logo/patreon.webp"
        hover "logo/patreon_hover.webp"
        action OpenURL("https://www.patreon.com/SilverStudioGames")

    imagebutton:
        xpos 660
        ypos 562
        xalign 0.5
        yalign 0.5
        idle "logo/discord.webp"
        hover "logo/discord_hover.webp"
        action OpenURL("https://discord.gg/7PD57yt")

screen navigation():
    window:
        style "gm_root"

    frame:
        style_group "gm_nav"
        margin (5,5)
        xalign 1.0
        yalign 1.0

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=not main_menu)

screen file_picker():
    frame:
        margin (5,5)

        has vbox
        hbox:
            if renpy.get_screen("load"):
                label _("Load game") xsize 160 yalign 0.5
            else:
                label _("Save game") xsize 160 yalign 0.5
            textbutton _("Auto") action FilePage("auto")
            textbutton _("Quick") action FilePage("quick")

            textbutton _("«") action FilePagePrevious(auto=False, quick=False)

            default p = 0
            $ p = max(0, int(FilePageName(str(p+10), str(p+10)))-10)
            for i in xrange(1+p, 11+p):
                textbutton str(i) action FilePage(i) xsize 60

            textbutton _("»") action FilePageNext() sensitive bool(FilePageName(0, 0))

        null height 5

        $ columns = 3
        $ rows = 6

        # Display a grid of file slots
        grid columns rows:
            transpose True
            xfill True

            for i in xrange(1, columns * rows + 1):
                $ is_compatible = check_save_compatibility(i)
                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot"))
                $ save_name = FileSaveName(i)

                button:
                    xfill True
                    ysize 52
                    padding (0,0)

                    if not is_compatible and renpy.get_screen("load"):
                        action Confirm("{color=#7a0000}Warning!{/color}\nThe save file you're trying to load is incompatible with the current version of the game and may result in broken gameplay and multiple errors.\nDo you still wish to proceed?", yes=FileAction(i), no=NullAction())
                    else:
                        action FileAction(i)

                    key "save_delete" action FileDelete(i, preferences.savedelwarn)

                    if is_compatible:
                        add FileScreenshot(i)
                    else:
                        add gray_tint(FileScreenshot(i))

                    if FileLoadable(i):
                        textbutton _("X"):
                            yalign 0.5
                            xalign 1.0
                            yfill True
                            margin (0,0)
                            action FileDelete(i, preferences.savedelwarn)

                        if not is_compatible:
                            text "[file_name]. [file_time!t]\n\n{color=#7a0000}NOT COMPATIBLE{/color}" xpos 70 style "night_button_text"
                        else:
                            text "[file_name]. [file_time!t]\n[save_name]" xpos 70 style "night_button_text"
                    else:
                        text "[file_name]. [file_time!t]" xpos 70 style "night_button_text"

screen save():
    tag menu
    zorder 5

    use navigation
    use file_picker

screen load():
    tag menu
    zorder 5

    use navigation
    use file_picker

screen preferences():
    tag menu
    zorder 5

    use navigation

    if not renpy.android:
        $ columns = 4
        $ rows = 1
    else:
        $ columns = 3
        $ rows = 1

    grid columns rows:
        style_prefix "pref"
        xfill True
        spacing 5
        area (5, 5, config.screen_width-10, config.screen_height-10)

        vbox:
            spacing 5

            if not renpy.android:
                frame:
                    has vbox

                    label _("Display")
                    textbutton _("Default"):
                        action Preference("display", "window")
                        sensitive (renpy.get_physical_size() != (config.screen_width, config.screen_height))
                    grid 2 1:
                        xfill True
                        textbutton _("Windowed") action Preference("display", "any window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")



            frame:
                has vbox

                label _("Interface")
                if not renpy.android:
                    textbutton "Tooltips" action ToggleVariable("preferences.tooltip", True, False)
                    textbutton _("Custom Cursor") action [ToggleVariable("preferences.customcursor", True, False), ToggleVariable("config.mouse", { 'default' : [ ('interface/cursor.webp', 0, 0)] }, None) ]
                textbutton _("Nightmode") action [ToggleVariable("preferences.nightmode", True, False), Function(renpy.call_in_new_context, "update_interface_color")]

            frame:
                has vbox

                label _("Text size")
                bar value Preference("font size")
                textbutton _("Reset") action [Preference("font size", 1.0), SensitiveIf(preferences.font_size != 1.0)]
                label _("Text color")
                grid 2 1:
                    xfill True
                    textbutton _("Day {color=[preferences.text_color_day]}text{/color}") action Function(renpy.invoke_in_new_context, set_text_color) sensitive (not preferences.nightmode) text_size 16
                    textbutton _("Night {color=[preferences.text_color_night]}text{/color}") action Function(renpy.invoke_in_new_context, set_text_color, False) text_size 16
                textbutton _("Shadow") action ToggleVariable("preferences.text_outline", "#00000080", "#00000000")
                textbutton _("Default") action [SetVariable("preferences.text_color_day", "#402313"), SetVariable("preferences.text_color_night", "#341c0f"), SetVariable("preferences.text_outline", "#00000000")]

            frame:
                has vbox

                label _("Transitions")
                grid 2 1:
                    xfill True
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")

        vbox:
            spacing 5

            frame:
                has vbox

                label _("Skip")
                grid 2 1:
                    xfill True
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")

            frame:
                has vbox

                label _("After Choices")
                grid 2 1:
                    xfill True
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                has vbox

                label _("{size=-4}Auto-Forward Time{/size}")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

            if not main_menu:
                frame:
                    has vbox

                    label _("{size=-4}Animation preference{/size}")
                    grid 2 1:
                        xfill True
                        textbutton _("Chibis") action SetVariable("use_cgs", False) tooltip "{image=interface/chibi.webp}"
                        textbutton _("CGs") action SetVariable("use_cgs", True) tooltip "{image=interface/cg.webp}"

                frame:
                    has vbox

                    label _("Difficulty")
                    grid 3 1:
                        xfill True
                        textbutton _("Easy"):
                            text_size 14 text_color "#93b04c66" text_selected_color "#93b04c"
                            action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 1), SelectedIf(game_difficulty == 1)]
                        textbutton _("Normal"):
                            text_size 14
                            action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 2), SelectedIf(game_difficulty == 2)]
                        textbutton _("Hard"):
                            text_size 14 text_color "#b33e2766" text_selected_color "#b33e27"
                            action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 3), SelectedIf(game_difficulty == 3)] sensitive persistent.game_complete

                    textbutton _("With cheats") action ToggleVariable("cheats_active", True, False) sensitive (game_difficulty < 3)
                    textbutton _("Tutorials") action ToggleVariable("preferences.tutorials", True, False)

        vbox:
            spacing 5

            frame:
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

                label _("Weather Volume")
                bar value Preference("weather volume")

            if config.has_voice:
                frame:
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
            frame:
                has vbox

                label _("Saving & Loading")
                textbutton _("Autosave") action [
                    ToggleVariable("preferences.autosave", True, False),
                    Notify(("Autosave preference will take effect after restarting the game", left))
                ]
                textbutton _("Save Delete Warning") action ToggleVariable("preferences.savedelwarn", True, False)

        if not renpy.android:
            vbox:
                frame:
                    has vbox

                    label _("Hotkeys")
                    textbutton _("Map - [hkey_map]") action None
                    textbutton _("Work - [hkey_work]") action None
                    textbutton _("Books - [hkey_book]") action None
                    textbutton _("Characters - [hkey_stats]") action None
                    textbutton _("Inventory - [hkey_inventory]") action None
                    textbutton _("Sleep - [hkey_sleep]") action None
                    textbutton _("Jerk off - [hkey_fap]") action None
                    textbutton _("Summon - [hkey_summon]") action None

screen notify(message):
    layer "interface"
    sensitive False

    # Pass a tuple to customise notify transform (for positioning)
    if isinstance(message, tuple):
        $ m, t = message
    else:
        $ m, t = message, reset

    frame:
        style "empty"
        margin (5,5)
        at transform:
            t
            on show:
                alpha 0
                linear .25 alpha 1.0
            on hide:
                linear .5 alpha 0.0

        text m:
            color "#fff"
            outlines [(1, "#00000080", 1, 0)]

    timer 3.25 action Hide("notify")

screen skip_indicator():
    zorder 100

    text "{unicode}{size=66}▶▶{/size}{/unicode}\nSkipping" size 22 text_align 0.5 pos (50, 50) color "#fff" outlines [(1, "#00000080", 1, 0)] at blink

    if room_menu_active:
        if daytime:
            timer 10 action Jump("night_start")
        else:
            timer 10 action Jump("day_start")

screen confirm(message, yes_action, no_action):
    zorder 999
    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            text _(message):
                text_align 0.5
                xalign 0.5
                style "night_text"
                color "#9b8d84"

            hbox:
                spacing 100
                xalign .5
                textbutton _("Yes") action yes_action keysym "y"
                textbutton _("No") action no_action keysym "n"
    # Right-click and escape answer "no".
    key "game_menu" action no_action
