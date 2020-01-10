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
    
    if hkey_chat_hidden:
        button style "empty" action SetVariable("hkey_chat_hidden", False)
        
    if side_image:
        add side_image yalign 1.0 yanchor 1.0 zoom 0.5
    
    style_prefix "say"
    window:
        id "window"
        if hkey_chat_hidden:
            ypos 1000
            
        use quick_menu
        use hotkeys_say

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
        
    if renpy.variant("android"):
        imagebutton idle "interface/frames/"+interface_color+"/arrow.png" action Rollback() xoffset -120 yalign 0.5 yanchor 0.5
        imagebutton idle im.Flip("interface/frames/"+interface_color+"/arrow.png", horizontal=True) action Skip(fast=True, confirm=True) xoffset 600 yalign 0.5 yanchor 0.5

screen choice(items):
    tag menu
    zorder 30

    # Dont add the fade if character or saybox is present (They have their own triggers for fading)
    if not any(itertools.imap(renpy.get_screen, ["say", "hermione_main", "cho_main", "luna_main", "snape_main", "astoria_main", "tonks_main", "susan_main", "letter"])):
        add "interface/bld.png" at fadeOutOnly
    window at fadeInOut:
        style "empty"
        xalign menu_x
        yalign menu_y

        vbox:
            style_prefix interface_style + "_menu"
            spacing 0
            $ choice_width = int(config.screen_width/2)

            for i, entry in enumerate(items, 1):
                $ caption_text, _, ico = entry.caption.partition("{icon=") # Icon must be at the end of caption

                button:
                    xsize choice_width
                    ypadding 5
                    action entry.action
                    if i < 10 and entry.action:
                        keysym (str(i), "K_KP"+str(i))
                    sensitive bool(entry.action)
                    fixed:
                        fit_first "height"
                        text caption_text:
                            xcenter choice_width/2
                            xsize choice_width-120 # Leave enough margin for number and icon
                            text_align 0.5
                        if i < 10 and entry.action:
                            text "{size=-2}[i].{/size}" xpos 5 yalign 0.5
                        if ico:
                            add ico[:-1] xcenter 40 yalign 0.5
    
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
        text "{color=#c70000}EXPERIMENTAL VERSION{/color}" xpos 10 yalign 0.01 size 24 outlines [(2, "#000", 0, 0)]
        text "Expect bugs, crashes and other weird stuff.\nProceed at your own risk, you have been warned!" xpos 10 yalign 0.05 color "#fff" size 12 outlines [(2, "#000", 0, 0)]
        text "You can find the most recent stable build on our {a=https://pastebin.com/6zbuZ5gS}pastebin{/a}" xpos 10 yalign 0.15 color "#fff" size 12 outlines [(2, "#000", 0, 0)]
    
    if update_available:        
        frame:
            style_group "mm"
            xalign .96
            yalign .575
            
            has vbox
            textbutton _("{size=-6}{color=#7a0000}UPDATE AVAILABLE{/color}{/size}") action OpenURL("https://pastebin.com/6zbuZ5gS")

    frame:
        style_group "mm"
        xalign .96
        yalign .75

        has vbox

        if not persistent.game_complete:
            textbutton _("New Game") action Start()
        else:
            textbutton _("New Game {size=+3}+{/size}") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm=False)

    frame:
        style_group "mm"
        xalign .96
        yalign .86

        has vbox
        textbutton _("Credits") action Jump("credits")
        
    imagebutton:
        xpos 910
        ypos 560
        xalign 0.5
        yalign 0.5
        idle "logo/patreon.png"
        hover "logo/patreon_hover.png"
        action OpenURL("https://www.patreon.com/SilverStudioGames")
        
    imagebutton:
        xpos 660
        ypos 562
        xalign 0.5
        yalign 0.5
        idle "logo/discord.png"
        hover "logo/discord_hover.png"
        action OpenURL("https://discord.gg/7PD57yt")
    
    if check_for_old_files():
        frame:
            style "empty"
            background "#000"
            xsize 1080
            ysize 600
            button style "empty" action NullAction()
            add "images/misc/old.png" yanchor 1.0 yalign 0.99 xpos 10
            text "{size=+40}WARNING!{/size}" xalign 0.5 xanchor 0.5 ypos 150 color "#7a0000"
            text "We have detected old unusable files in your game folder,\nplease close the game and perform a clean installation." xalign 0.5 xanchor 0.5 ypos 250 color "#FFF"
            textbutton "{size=+30}Quit{/size}" action Quit(confirm=False) xalign 0.5 xanchor 0.5 yalign 0.9

screen navigation():
    window:
        style "gm_root"

    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

screen file_picker():
    frame:
        style "file_picker_frame"

        has vbox
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous") action FilePagePrevious()
            textbutton _("Auto") action FilePage("auto")
            textbutton _("Quick") action FilePage("quick")

            for i in xrange(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("Next") action FilePageNext()

        $ columns = 3
        $ rows = 6

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in xrange(1, columns * rows + 1):
                $ is_compatible = check_save_compatibility(FileCurrentPage(), str(i))
                
                if renpy.get_screen("load"):
                    $ current_action = Confirm("{color=#7a0000}Warning!{/color}\nThe save file you're trying to load is incompatible with the current version of the game and may result in broken gameplay and multiple errors.\nDo you still wish to proceed?", yes=FileAction(i), no=NullAction())
                else:
                    $ current_action = FileAction(i)
                
                if is_compatible == True or is_compatible == None:
                    button:
                        xfill True
                        action FileAction(i)
                        has hbox

                        # Add the screenshot.
                        add FileScreenshot(i)

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        
                        if save_name != "":
                            textbutton _("X"):
                                yalign 0.5
                                xpos 235
                                yfill True
                                ymaximum 50
                                action FileDelete(i, preferences.savedelwarn)
                            text "[file_name]. [file_time!t]\n[save_name!t]" xpos -40 yalign 0.5 style "night_button_text"
                        else:
                            text "[file_name]. [file_time!t]" xoffset 1 style "night_button_text"
                            
                        key "save_delete" action FileDelete(i, preferences.savedelwarn)
                else:
                    button:
                        xfill True
                        action current_action
                            
                        has hbox

                        # Add the screenshot.
                        add grayTint(FileScreenshot(i))

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        
                        if save_name != "":
                            textbutton _("X"):
                                yalign 0.5
                                xpos 235
                                yfill True
                                ymaximum 50
                                action FileDelete(i, preferences.savedelwarn)
                            text "[file_name]. [file_time!t]\n\n{color=#7a0000}NOT COMPATIBLE{/color}" xpos -40 yalign 0.5 style "night_text"
                        else:
                            text "[file_name]. [file_time!t]" xoffset 1 style "night_text"
                            
                        key "save_delete" action FileDelete(i, preferences.savedelwarn)

screen save():
    tag menu

    use navigation
    use file_picker

    zorder 5

screen load():
    tag menu

    use navigation
    use file_picker

    zorder 5

screen preferences():
    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a four-wide grid.
    if not renpy.variant('android'):
        $ columns = 4
        $ rows = 1
    else:
        $ columns = 3
        $ rows = 1
    grid columns rows:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            if not renpy.variant('android'):
                frame:
                    style_group "pref"
                    has vbox

                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    
            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")
            ####
            frame:
                style_group "pref"
                has vbox
                
                label _("Interface")
                if not renpy.variant('android'):
                    textbutton "Tooltips" action ToggleVariable("preferences.tooltip", True, False)
                    textbutton _("Custom Cursor") action [ToggleVariable("preferences.customcursor", True, False), ToggleVariable("config.mouse", { 'default' : [ ('interface/cursor.png', 0, 0)] }, None) ]
                textbutton _("Nightmode") action [ToggleVariable("preferences.nightmode", True, False), Function(renpy.call_in_new_context, "update_interface_color")]
            frame:
                style_group "pref"
                has vbox

                label _("Text colour")
                if not preferences.nightmode:
                    textbutton _("Day {color=[preferences.text_color_day]}text{/color}") action Function(renpy.invoke_in_new_context, set_text_color)
                textbutton _("Night {color=[preferences.text_color_night]}text{/color}") action Function(renpy.invoke_in_new_context, set_text_color, False)
                textbutton _("Shadow") action ToggleVariable("preferences.text_outline", "#00000080", "#00000000")
                textbutton _("Default") action [SetVariable("preferences.text_color_day", "#402313"), SetVariable("preferences.text_color_night", "#341c0f"), SetVariable("preferences.text_outline", "#00000000")]
                
            if not main_menu:
                frame:
                    style_group "pref"
                    has vbox
                    
                    label _("Difficulty")
                    hbox:
                        xalign 0.5
                        textbutton _("Easy"):
                            text_size 14 text_color "#93b04c66" text_selected_color "#93b04c" xsize 80
                            action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 1), SelectedIf(game_difficulty == 1)]
                        textbutton _("Normal"):
                            text_size 14 xsize 80
                            action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 2), SelectedIf(game_difficulty == 2)]
                        if persistent.game_complete:
                            textbutton _("Hard"):
                                text_size 14 text_color "#7a000066" text_selected_color "#7a0000" xsize 80
                                action [Function(renpy.call_in_new_context, "adjust_game_difficulty", 3), SelectedIf(game_difficulty == 3)]

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                    
            frame:
                style_group "pref"
                has vbox
                
                label _("{size=-4}Animation preference{/size}")
                textbutton _("Chibis") action SetVariable("use_cgs", False)
                textbutton _("Sprites") action SetVariable("use_cgs", True)

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
            frame:
                style_group "pref"
                has vbox
                
                label _("Saving&Loading")
                textbutton _("Autosave") action [ToggleVariable("preferences.autosave", True, False), ToggleVariable("config.has_autosave", True, False), ToggleVariable("config.autosave_on_choice", True, False)]
                textbutton _("Save Del. Warning") action ToggleVariable("preferences.savedelwarn", True, False)
        if not renpy.variant('android'):
            vbox:#Hotkeys
                frame:
                    style_group "pref"
                    has vbox

                    label _("Hotkeys")
                    textbutton _("Map - [hkey_map]") action None
                    textbutton _("Work - [hkey_work]") action None
                    textbutton _("Books - [hkey_book]") action None
                    textbutton _("Characters - [hkey_stats]") action None
                    textbutton _("Inventory - [hkey_inventory]") action None
                    textbutton _("Sleep - [hkey_sleep]") action None
                    textbutton _("Jerk off - [hkey_fap]") action None
    zorder 5
    
screen notify(message):
    zorder 100

    text message:
        at _notify_transform
        color "#fff" 
        outlines [(1, "#00000080", 1, 0)]

    timer 3.25 action Hide('notify')
    
screen skip_indicator():
    zorder 100

    add "ui_rewind"
    
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