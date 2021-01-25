init python:
    def text_points(points):
        if points < 1000:
            return str(points)
        else:
            return  str(round(points/1000.0, 1))+"{size=-2}k{/size}"

label update_ui_points:
    # Debug

    # Temp variables
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

screen ui_top_bar():
    tag ui
    zorder 2

    if toggle_menu:
        use ui_menu

    add gui.format("interface/topbar/{}/bar.webp") zoom 0.5
    use ui_stats
    use ui_points

    # Don't display buttons in certain rooms or on the first day
    if current_room not in ["clothing_store", "weasley_store", "room_of_requirement", "floor_seven"] and game.day > 1:
        # Menu button
        imagebutton:
            xpos 0
            idle gui.format("interface/topbar/buttons/{}/ui_menu.webp")
            if room_menu_active:
                hover image_hover(gui.format("interface/topbar/buttons/{}/ui_menu.webp"))
                if toggle_menu:
                    tooltip "Close menu"
                else:
                    tooltip "Open menu"
                action ToggleVariable("toggle_menu", True, False)

        # Sleep button
        imagebutton:
            xpos 1080
            xanchor 1.0
            idle gui.format("interface/topbar/buttons/{}/ui_sleep.webp")
            if room_menu_active:
                hover image_hover(gui.format("interface/topbar/buttons/{}/ui_sleep.webp"))
                if game.daytime:
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
                idle gui.format("interface/topbar/buttons/{}/ui_achievements.webp")
                if room_menu_active:
                    hover image_hover(gui.format("interface/topbar/buttons/{}/ui_achievements.webp"))
                    tooltip "Achievements"
                    action Jump("achievement")

            # Stats button
            imagebutton:
                idle gui.format("interface/topbar/buttons/{}/ui_stats.webp")
                if room_menu_active:
                    hover image_hover(gui.format("interface/topbar/buttons/{}/ui_stats.webp"))
                    tooltip "Characters (c)"
                    action Jump("stats")

            # Inventory button
            imagebutton:
                idle gui.format("interface/topbar/buttons/{}/ui_inv.webp")
                if room_menu_active:
                    hover image_hover(gui.format("interface/topbar/buttons/{}/ui_inv.webp"))
                    tooltip "Inventory (i)"
                    action Jump("inventory")

            # Work button
            if letter_work_unlock.read:
                imagebutton:
                    idle gui.format("interface/topbar/buttons/{}/ui_work.webp")
                    if room_menu_active:
                        hover image_hover(gui.format("interface/topbar/buttons/{}/ui_work.webp"))
                        tooltip "Work (w)"
                        action Jump("paperwork")

screen ui_points():
    tag ui

    fixed:
        xalign 0.5
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

        if room_menu_active or renpy.get_screen("room_of_requirement_menu") or renpy.get_screen("floor_7th_menu"):
            imagebutton:
                idle "interface/topbar/hover_zone.webp"
                tooltip "House Points\n{size=-2}Click to toggle style display{/size}"
                hovered SetVariable("toggle_points", True)
                unhovered SetVariable("toggle_points", False)
                action ToggleVariable("persistent.toggle_points", True, False)

screen ui_stats():
    tag ui
    fixed:
        xpos 200
        frame:
            style "empty"
            style_prefix gui.theme("ui_stats")
            xsize 217
            ysize 26

            add gui.format("interface/topbar/{}/stats.webp") xalign 0.5 yalign 1.0

            hbox:
                xpos 40 ypos 11
                text "{size=-4}[game.day]{/size}"
            hbox:
                xpos 140 ypos 11
                # Display tokens in token shop
                text "{size=-4}[game.gold]{/size}"

style light_ui_stats_text:
    color "#000"
    outlines [(1, "#e4ba7080", 0, 0)]

style dark_ui_stats_text:
    color "#fff"
    outlines [(1, "#00000080", 0, 0)]

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
        style_prefix gui.theme()
        ypos 34
        xsize 102
        ysize 204

        add gui.format("interface/topbar/{}/menu.webp")

        vbox:
            xanchor 0.5
            xalign 0.5
            ypos 15
            textbutton "Save" action ShowMenu("save") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            textbutton "Load" action ShowMenu("load") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if game.cheats and game.difficulty <= 2 and game.day > 1:
                textbutton "Cheats" action [SetVariable("toggle_menu", False), Jump("cheats")] background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if game.day > 1 and renpy.android:
                textbutton "Preferences" action ShowMenu("preferences") background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]
            if game.day > 1 and persistent.game_complete:
                textbutton "Gallery" action [SetVariable("toggle_menu", False), Jump("scene_gallery")] background None xalign 0.5 text_outlines [ (2, "#00000080", 1, 0) ]

            #if game.day > 1 and config.developer:
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
                tooltip "PLACEHOLDER"
                action NullAction()
                yanchor 0.5

label scene_gallery:
    menu:
        "-Watch Ball Ending 1-" if persistent.ending_01:
            $ renpy.call_replay("ball_ending_E2", { "public_whore_ending": False })
        "-Watch Ball Ending 2-" if persistent.ending_02:
            $ renpy.call_replay("ball_ending_E2", { "public_whore_ending": True })
        "-Never mind-":
            pass
    jump main_room_menu
