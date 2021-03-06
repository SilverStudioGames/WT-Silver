init python:
    def ui_dropped(drags, drops):
        drags[0].snap(clamp(drags[0].target_x, 20, 740), 0)
        return

    def text_points(points):
        if points < 1000:
            return str(points)
        else:
            return  str(round(points/1000.0, 1))+"{size=-2}k{/size}"

label house_points:
    # Debug
    #if config.debug:
        #$ total_points = slytherin+gryffindor+ravenclaw+hufflepuff

    # Temp variables
    $ toggle_ui_lock = True
    $ toggle_points = False
    $ toggle_menu = False

    # Outline settings
    #TODO Refactor interface_color dependent styles to definitions
    $ points_outline = [ (1, "#000", 0, 0) ]

    #If points variable value exceedes one thousand make it a decimal number instead and round to x.x
    #Remember, "slytherin_points" is a string! If you need points integer use i.e. "slytherin" variable instead.
    $ slytherin_points = text_points(slytherin)
    $ gryffindor_points = text_points(gryffindor)
    $ ravenclaw_points = text_points(ravenclaw)
    $ hufflepuff_points = text_points(hufflepuff)

    #Check who's in the lead
    $ housepoints = [slytherin, gryffindor, ravenclaw, hufflepuff]
    $ housepoints_sorted = sorted(housepoints, reverse=True)

    $ slytherin_place = housepoints_sorted.index(housepoints[0])+1
    $ gryffindor_place = housepoints_sorted.index(housepoints[1])+1
    $ ravenclaw_place = housepoints_sorted.index(housepoints[2])+1
    $ hufflepuff_place = housepoints_sorted.index(housepoints[3])+1

    # Set banners yanchor depending on the placement (ascending)
    $ housepoints_y = [None, 0.0, 0.25, 0.5, 0.75]

    return

#Top Bar UI
screen ui_top_bar():
    tag ui
    zorder 2

    if toggle_menu:
        use ui_menu

    add "interface/topbar/"+str(interface_color)+"/bar.webp" zoom 0.5
    use ui_stats
    use ui_points

    # Don't display buttons in certain rooms or on the first day
    if current_room not in ["clothing_store", "weasley_store", "room_of_requirement", "floor_seven"] and day > 1:
        # Menu button
        imagebutton:
            xpos 0
            idle "interface/topbar/buttons/"+str(interface_color)+"/ui_menu.webp"
            if room_menu_active:
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_menu.webp")
                if toggle_menu:
                    tooltip "Close menu"
                else:
                    tooltip "Open menu"
                action ToggleVariable("toggle_menu", True, False)

        # Sleep button
        imagebutton:
            xpos 1080
            xanchor 1.0
            idle "interface/topbar/buttons/"+str(interface_color)+"/ui_sleep.webp"
            if room_menu_active:
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_sleep.webp")
                if daytime:
                    action Jump("night_start")
                    tooltip "Doze Off (s)"
                else:
                    action Jump("day_start")
                    tooltip "Sleep (s)"

        hbox:
            if renpy.android:
                spacing 10
                xpos 800
            else:
                xpos 900

            # Achievements button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_achievements.webp"
                if room_menu_active:
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_achievements.webp")
                    tooltip "Achievements"
                    action Jump("achievement")

            # Stats button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_stats.webp"
                if room_menu_active:
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_stats.webp")
                    tooltip "Characters (c)"
                    action Jump("stats")

            # Inventory button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_inv.webp"
                if room_menu_active:
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_inv.webp")
                    tooltip "Inventory (i)"
                    action Jump("inventory")

            # Work button
            if letter_min_work.read:
                imagebutton:
                    idle "interface/topbar/buttons/"+str(interface_color)+"/ui_work.webp"
                    if room_menu_active:
                        hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_work.webp")
                        tooltip "Work (w)"
                        action Jump("paperwork")

        ## Toggle UI lock button
        #imagebutton:
        #    xpos 1047
        #    idle "interface/topbar/buttons/"+str(interface_color)+"/ui_%s.webp" % toggle_ui_lock
        #    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_%s.webp" % toggle_ui_lock)
        #    action ToggleVariable("toggle_ui_lock", False, True)

        #Debug
        #if config.debug:
            #hbox:
                #xpos 10 ypos 40
                #text "{size=-3}{color=#FFF}[total_points] [housepoints]\n[housepoints_y]\nToggle display:[persistent.toggle_points]\n\nSly:[slytherin_place]\nGry:[gryffindor_place]\nRav:[ravenclaw_place]\nHuf:[hufflepuff_place]\nUI lock:[toggle_ui_lock]{/color}{/size}"

        # if tooltip and preferences.tooltip and not renpy.android:
            # text "{color=#FFF}{size=+4}[tooltip]{/size}{/color}" xalign 0.5 text_align 0.5 ypos 540

screen ui_points():
    tag ui
    drag:
        drag_name "ui_points"
        draggable not toggle_ui_lock
        dragged ui_dropped
        drag_handle(0, 0, 1.0, 1.0)
        xpos 540 ypos 0
        xanchor 0.5
        frame:
            style "empty"
            xsize 162
            ysize 64
            xanchor 0.5

            if not persistent.toggle_points and not toggle_points:
                add "interface/topbar/slytherin.webp" yanchor housepoints_y[slytherin_place]
                add "interface/topbar/gryffindor.webp" yanchor housepoints_y[gryffindor_place]
                add "interface/topbar/ravenclaw.webp" yanchor housepoints_y[ravenclaw_place]
                add "interface/topbar/hufflepuff.webp" yanchor housepoints_y[hufflepuff_place]
            else:
                # Add empty banners
                add "interface/topbar/slytherin_empty.webp" yanchor 0
                add "interface/topbar/gryffindor_empty.webp" yanchor 0
                add "interface/topbar/ravenclaw_empty.webp" yanchor 0
                add "interface/topbar/hufflepuff_empty.webp" yanchor 0
                # Show points
                text "{size=-5}{color=#FFF}[slytherin_points]{/color}{/size}" outlines points_outline xpos 17 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[gryffindor_points]{/color}{/size}" outlines points_outline xpos 58 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[ravenclaw_points]{/color}{/size}" outlines points_outline xpos 98 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[hufflepuff_points]{/color}{/size}" outlines points_outline xpos 139 ypos 30 xanchor 0.5
                # Show placement number
                text "{size=16}{color=#FFF}[slytherin_place]{/color}{/size}" outlines points_outline xpos 17 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[gryffindor_place]{/color}{/size}" outlines points_outline xpos 58 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[ravenclaw_place]{/color}{/size}" outlines points_outline xpos 98 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[hufflepuff_place]{/color}{/size}" outlines points_outline xpos 139 ypos 10 xanchor 0.5

            if toggle_ui_lock and room_menu_active or renpy.get_screen("room_of_requirement_menu") or renpy.get_screen("floor_7th_menu"):
                imagebutton:
                    idle "interface/topbar/hover_zone.webp"
                    tooltip "House Points\n{size=-2}Click to toggle{/size}"
                    hovered SetVariable("toggle_points", True)
                    unhovered SetVariable("toggle_points", False)
                    action ToggleVariable("persistent.toggle_points", True, False)

screen ui_stats():
    tag ui
    drag:
        drag_name "ui_stats"
        draggable not toggle_ui_lock
        dragged ui_dropped
        xpos 200
        frame:
            style "empty"
            xsize 217
            ysize 26

            add "interface/topbar/"+str(interface_color)+"/stats.webp" xalign 0.5 yalign 1.0

            # Add overlay token icon if needed
            if renpy.get_screen("weasley_store_room") and store_category == 3:
                add "interface/topbar/icon_token.webp" ypos 8 xpos 118

            hbox:
                xpos 40 ypos 11
                text "{size=-4}[daygold_colour][day]{/color}{/size}" outlines daygold_outline
            hbox:
                xpos 140 ypos 11
                # Display tokens in token shop
                if renpy.get_screen("weasley_store_room") and store_category == 3:
                    text "{size=-4}[daygold_colour][tokens]{/color}{/size}" outlines daygold_outline
                else:
                    text "{size=-4}[daygold_colour][gold]{/color}{/size}" outlines daygold_outline

screen ui_menu():
    tag ui

    button style "empty" action SetVariable("toggle_menu", False) keysym "game_menu"

    button:
        ypos 34
        xsize 102
        ysize 204
        action NullAction()
        style "empty"
    frame:
        style "empty"
        style_prefix interface_style
        ypos 34
        xsize 102
        ysize 204

        add "interface/topbar/"+str(interface_color)+"/menu.webp"

        vbox:
            xanchor 0.5
            xalign 0.5
            ypos 15
            textbutton "Save" action ShowMenu("save") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            textbutton "Load" action ShowMenu("load") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if cheats_active and game_difficulty <= 2 and day > 1:
                textbutton "Cheats" action [SetVariable("toggle_menu", False), Jump("cheats")] background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if day > 1 and renpy.android:
                textbutton "Preferences" action ShowMenu("preferences") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if day > 1 and persistent.game_complete:
                textbutton "Gallery" action [SetVariable("toggle_menu", False), Jump("scene_gallery")] background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if day > 1:
                textbutton "Decorate" action [SetVariable("toggle_menu", False), Jump("decorate_room_menu")] background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]

            #if day > 1 and config.developer:
            #    textbutton "{size=-11}Show Chars{/size}" action [SetVariable("toggle_menu", False), Jump("summon_characters")] background "#000"

        hbox:
            pos (50, 185)
            anchor (0.5, 0.5)
            spacing 10
            # Discord
            imagebutton:
                idle Transform("interface/topbar/icon_discord.webp", alpha=0.5)
                hover "interface/topbar/icon_discord.webp"
                tooltip "Visit {color=#c1c1c1}SilverStudioGames{/color}\ndiscord"
                action OpenURL("https://discord.gg/7PD57yt")
                yanchor 0.5
            # Patreon
            imagebutton:
                idle Transform("interface/topbar/icon_patreon.webp", alpha=0.5)
                hover "interface/topbar/icon_patreon.webp"
                tooltip "Visit {color=#c1c1c1}SilverStudioGames{/color}\npatreon"
                action OpenURL("https://www.patreon.com/SilverStudioGames")
                yanchor 0.5
            # Bugfixes
            imagebutton:
                idle Transform("interface/topbar/icon_bug.webp", alpha=0.5)
                hover "interface/topbar/icon_bug.webp"
                tooltip "Open bugfix menu"
                action [SetVariable("toggle_menu", False), Jump("bugfix_menu")]
                yanchor 0.5

### Ingame Options Menu ###

label options_menu:
    menu:
        "-Change Game Difficulty-" if game_difficulty <= 2:
            menu:
                "-Enable Easy Difficulty-":
                    call adjust_game_difficulty(1)
                    "Game set to easy difficulty!"
                    "Increased gold reward from reports and other sources!"
                    "Rummaging through your cupboard is more rewarding!"
                    "Snape will be more generous with Slytherin-points!"
                    "Hermione won't stay mad at you for as long!"
                    jump main_room_menu
                "-Enable Normal Difficulty-":
                    call adjust_game_difficulty(2)
                    "Game set to normal difficulty!"
                    jump main_room_menu
                "-Back-":
                    jump main_room_menu
        "-Replace Chibi animations with CG images-" if not use_cgs:
            ">The last two of Hermione's personal favours will use CG images."
            $ use_cgs = True
            jump main_room_menu
        "-Replace CG images with Chibi animations-" if use_cgs:
            ">The last two of Hermione's personal favours will now use chibi animations."
            $ use_cgs = False
            jump main_room_menu
        "-Never mind-":
            jump main_room_menu

label bugfix_menu:
    menu:
        "-Reset Everyone's Appearance-":
            call reset_luna_base
            call reset_luna_clothing
            call reset_susan_clothing

            $ hermione.wear("all")
            $ hermione.equip(her_outfit_default)
            $ hermione.rebuild()
            $ cho.wear("all")
            $ cho.equip(cho_outfit_default)
            $ cho.rebuild()
            $ astoria.wear("all")
            $ astoria.equip(ast_outfit_default)
            $ astoria.rebuild()
            $ tonks.wear("all")
            $ tonks.equip(ton_outfit_default)
            $ tonks.rebuild()
            ">Appearance of each girl set back to default."
            jump bugfix_menu
        "-Reset Cho public and personal favours-" if cho_unlocked:
            python:
                for ev in cc_favor_list:
                    ev.reset()
                for ev in cc_requests_list:
                    ev.reset()
            "> Events have been successfully reset."
            jump bugfix_menu
        "-Back-":
            pass
    jump main_room_menu

label scene_gallery:
    menu:
        "-Watch Ball Ending 1-" if persistent.ending_01:
            $ renpy.call_replay("ball_ending_E2", { "public_whore_ending": False })
        "-Watch Ball Ending 2-" if persistent.ending_02:
            $ renpy.call_replay("ball_ending_E2", { "public_whore_ending": True })
        "-Never mind-":
            pass
    jump main_room_menu

label decorate_room_menu:

    $ item_list = [wall_deco_list, fireplace_deco_list, cupboard_deco_list+misc_deco_list+misc_hat_list]

    show screen bottom_menu("decorate_room_menu", (
        ("Posters", "deco_wall"), ("Trophies", "ui_quest_items"), ("Miscellaneous", "deco_cupboard")
    ), item_list, "ui_delete")
    with d3

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, tuple):
        if _return[1].number > 0 or _return[1].unlocked:
            call use_deco_item(_return[1])
            $ achievement.unlock("decorator")
        else:
            ">You haven't unlocked this decoration yet."

    elif _return == "func":
        hide screen bottom_menu
        with d3
        menu:
            ">Remove all decorations?"
            "-Yes-":
                # Loop through all decorations and deactivate them
                python:
                    for i in xrange(len(wall_deco_list)):
                        wall_deco_list[i].active = False
                    for i in xrange(len(fireplace_deco_list)):
                        fireplace_deco_list[i].active = False
                    for i in xrange(len(cupboard_deco_list)):
                        cupboard_deco_list[i].active = False
                    for i in xrange(len(misc_deco_list)):
                        misc_deco_list[i].active = False
                    for i in xrange(len(misc_hat_list)):
                        misc_hat_list[i].active = False

                    poster_OBJ.room_image = ""
                    trophy_OBJ.room_image = ""
                    cupboard_deco = ""
                    cupboard_deco_OBJ.room_image = ""
                    phoenix_deco_OBJ.room_image = ""
                    fireplace_deco_OBJ.room_image = ""
                    owl_deco_OBJ.room_image = ""
                    owl_OBJ.room_image = "owl_idle"
                    owl_OBJ.idle_image = "owl_letter"
                    owl_OBJ.hover_image = "owl_hover"
            "-No-":
                pass
        jump decorate_room_menu

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3
        jump main_room_menu

    jump .interact

label use_deco_item(item=None): # Add the 'item' decoration to the room. Remove it when 'item' is currently displayed as a deco.
    if item.type == "poster":
        # Loop through all posters and deactivate them
        python:
            for i in xrange(len(wall_deco_list)):
                wall_deco_list[i].active = False

        if poster_OBJ.room_image == item.id:
            $ poster_OBJ.room_image = ""
        else:
            $ poster_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "trophy":
        python:
            for i in xrange(len(fireplace_deco_list)):
                fireplace_deco_list[i].active = False

        if trophy_OBJ.room_image == item.id:
            $ trophy_OBJ.room_image = ""
        else:
            $ trophy_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "cupboard":
        if cupboard_deco_OBJ.room_image == item.id:
            $ cupboard_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ cupboard_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "pinup":
        if cupboard_deco == item.id:
            $ cupboard_deco = ""
            $ item.active = False
        else:
            $ cupboard_deco = item.id
            $ item.active = True
    elif item.type == "phoenix":
        if phoenix_deco_OBJ.room_image == item.id:
            $ phoenix_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ phoenix_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "fireplace":
        if fireplace_deco_OBJ.room_image == item.id:
            $ fireplace_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ fireplace_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "owl":
        if owl_deco_OBJ.room_image == item.id:
            $ owl_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ owl_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "mail":
        if owl_OBJ.room_image == item.id:
            $ owl_OBJ.room_image = "owl_idle"
            $ owl_OBJ.idle_image = "owl_letter"
            $ owl_OBJ.hover_image = "owl_letter_hover"
            $ item.active = False
        else:
            $ owl_OBJ.room_image = item.id
            $ owl_OBJ.idle_image = "owl_letter_black"
            $ owl_OBJ.hover_image = "owl_letter_hover_black"
            $ item.active = True
    return
