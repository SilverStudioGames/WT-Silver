default room_menu_active = False

# Main room menu screen (used to capture user interaction)
screen main_room_menu():
    tag room_menu
    on "show" action SetVariable("room_menu_active", True)
    on "hide" action SetVariable("room_menu_active", False)

# Main room screen
screen main_room():
    tag room
    zorder 0
    sensitive room_menu_active

    # Hotkeys
    if room_menu_active and day > 1 and not renpy.android:
        use hotkeys_main

    use weather

    # Walls
    if daytime:
        add "images/rooms/_bg_/main_room_day.webp" zoom 0.5
    else:
        add "images/rooms/_bg_/main_room_night.webp" zoom 0.5

    # Poster
    if poster_OBJ.room_image:
        add poster_OBJ.get_room_image() xpos poster_OBJ.xpos ypos poster_OBJ.ypos xanchor 0.5 yanchor 0.5

    # Trophy
    if trophy_OBJ.room_image:
        add trophy_OBJ.get_room_image() xpos trophy_OBJ.xpos ypos trophy_OBJ.ypos xanchor 0.5 yanchor 0.5

    # Candles
    add candle_left_OBJ.get_room_image() xpos candle_left_OBJ.xpos ypos candle_left_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    add candle_right_OBJ.get_room_image() xpos candle_right_OBJ.xpos ypos candle_right_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    if not daytime:
        add "candle_fire_01" xpos candle_left_OBJ.xpos-110 ypos candle_left_OBJ.ypos-117
        add "candle_fire_02" xpos candle_right_OBJ.xpos-110 ypos candle_right_OBJ.ypos-117

    # Door
    imagebutton:
        focus_mask True
        xanchor "center"
        yanchor "center"
        if daytime:
            xpos door_OBJ.xpos
            ypos door_OBJ.ypos
            idle door_OBJ.get_idle_image()
            hover door_OBJ.get_hover_image()
        else:
            xpos door_night_OBJ.xpos
            ypos door_night_OBJ.ypos
            idle door_night_OBJ.get_idle_image()
            hover door_night_OBJ.get_hover_image()
        if door_examined:
            tooltip "Summon"
        else:
            tooltip "Examine Door"
        action Jump("door")
        sensitive (room_menu_active and not (day == 1 and door_examined))

    # Cupboard
    add cupboard_OBJ.get_room_image() xpos cupboard_OBJ.xpos ypos cupboard_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5

    # Scrolls (interactive overlay)
    if renpy.android:
        imagemap:
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground cupboard_top_OBJ.get_idle_image()
            if store_intro_done:
                hover cupboard_top_OBJ.get_hover_image()
                hotspot (77, 81, 70, 76):
                    action Jump("read_scroll_menu")
                    sensitive room_menu_active
    else:
        imagebutton:
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_top_OBJ.get_idle_image()
            if store_intro_done:
                hover cupboard_top_OBJ.get_hover_image()
                tooltip "Scrolls"
                action Jump("read_scroll_menu")
                sensitive room_menu_active

    # Cupboard (interactive overlay)
    if renpy.android:
        imagemap:
            xpos cupboard_OBJ.xpos
            ypos cupboard_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground cupboard_OBJ.get_idle_image()
            if not searched:
                hover cupboard_OBJ.get_hover_image()
                hotspot (73, 156, 72, 133):
                    action Jump("cupboard")
                    sensitive room_menu_active
    else:
        imagebutton:
            xpos cupboard_OBJ.xpos
            ypos cupboard_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_OBJ.get_idle_image()
            if not searched:
                hover cupboard_OBJ.get_hover_image()
                if cupboard_examined:
                    tooltip "Rummage"
                else:
                    tooltip "Examine Cupboard"
                action Jump("cupboard")
                sensitive room_menu_active

    #TODO Move phoenix to separate screen (check if usage needed in mirror stories)
    # Phoenix
    imagebutton:
        xpos phoenix_OBJ.xpos
        ypos phoenix_OBJ.ypos
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle phoenix_OBJ.get_idle_image()
        if not phoenix_is_petted:
            hover phoenix_OBJ.get_hover_image()
            if bird_examined:
                if not phoenix_is_fed:
                    tooltip "Feed"
                else:
                    tooltip "Pet"
            else:
                tooltip "Examine the bird"
            action Jump("phoenix")
            sensitive room_menu_active

    # Phoenix deco
    if phoenix_deco_OBJ.room_image:
        add phoenix_deco_OBJ.get_room_image() xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5

    use phoenix_feather

    # Decorations
    # for i in deco_overlay_list:
    #    add deco_overlay_list[i].get_room_image() xpos i.xpos ypos i.ypos xanchor 0.5 yanchor 0.5


# Genie at desk
screen genie_desk_interactive():
    tag genie_chibi # Uses same tag as chibi screens
    if renpy.android:
        add "ch_gen sit_behind_desk" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5
        imagemap:
            xpos 384
            ypos 370
            xanchor 0.5
            yanchor 0.5
            ground "images/rooms/main_room/desk_small_border.webp"
            hover yellow_tint("images/rooms/main_room/desk_small_border.webp")
            hotspot (0, 10, 128, 160):
                action Jump("desk")
                sensitive room_menu_active
    else:
        imagebutton:
            xpos 370
            ypos 336
            focus_mask True
            xanchor 0.5
            yanchor 0.5
            idle "ch_gen sit_behind_desk"
            hover "ch_gen sit_behind_desk_hover"
            if desk_examined:
                tooltip "Open desk"
            else:
                tooltip "Examine Desk"
            hovered Show("gui_tooltip", img="emo_exclaim", xx=195+140, yy=210)
            unhovered Hide("gui_tooltip")
            action Jump("desk")
            sensitive (room_menu_active and not (day == 1 and desk_examined))

screen gui_tooltip(img=None, xx=335, yy=210):
    add img xpos xx ypos yy
    zorder 3

# Phoenix
screen phoenix_feather():
    tag feather
    add "feather" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 2

screen phoenix_food():
    tag phoenix_food
    add "images/rooms/_objects_/phoenix/food.webp" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    zorder 2

# Fireplace
screen fireplace():
    tag fireplace
    zorder 1
    imagebutton:
        xpos fireplace_OBJ.xpos
        ypos fireplace_OBJ.ypos
        xanchor 0.5
        yanchor 0.5
        focus_mask True
        idle fireplace_OBJ.get_idle_image()
        hover fireplace_OBJ.get_hover_image()
        if not fireplace_examined:
            tooltip "Examine fireplace"
        elif is_puzzle_box_in_fireplace():
            tooltip "What's that glimmer?"
        elif fire_in_fireplace:
            tooltip "Extinguish fire"
        else:
            tooltip "Light fire"
        action Jump("fireplace")
        sensitive room_menu_active

    #TODO Replace usage of screen fireplace_fire with flag fire_in_fireplace. Show/hide fire animation with transform effect
    # showif fire_in_fireplace:
    #     add "fireplace_fire" xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos+25 xanchor 0.5 yanchor 0.5

    # Fireplace deco
    if fireplace_deco_OBJ.room_image:
        add fireplace_deco_OBJ.get_room_image() xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5

    # Puzzle box appears in fireplace
    if is_puzzle_box_in_fireplace():
        add "glow_effect" xpos 680 ypos 300 zoom 0.4 alpha 0.2

screen fireplace_fire():
    tag fireplace_fire
    zorder 2
    add "fireplace_fire" xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos+25 xanchor 0.5 yanchor 0.5

# Furniture
screen desk(x=370): # Desk only
    tag desk
    zorder 2
    add "images/rooms/main_room/desk_with_shadow.webp" xpos x ypos 336 xanchor 0.5 yanchor 0.5 zoom 0.5

screen dumbledore(): # Dumbledore and desk
    tag dumbledore
    add "images/rooms/main_room/dum.webp" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5 zoom 0.5

screen chair_left():
    tag chair_left
    zorder 0 # Show main_room first for correct order
    add "images/rooms/main_room/chair_left_with_shadow.webp" xpos 332 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5

screen chair_right():
    tag chair_right
    zorder 0 # Show main_room first for correct order
    add "images/rooms/main_room/chair_right.webp" xpos 793 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5

screen cupboard_open():
    tag cupboard
    add "images/rooms/_objects_/cupboard/cupboard_open.webp" xpos cupboard_OBJ.xpos ypos cupboard_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    if cupboard_deco:
        add "images/rooms/_objects_/cupboard/cupboard_open" +str(cupboard_deco)+ ".webp"  xpos cupboard_OBJ.xpos ypos cupboard_OBJ.ypos xanchor 0.5 yanchor 0.5

# Owl
screen owl():
    tag owl
    imagebutton:
        xpos owl_OBJ.xpos
        ypos owl_OBJ.ypos
        xanchor 0.5
        yanchor 1.0
        idle owl_OBJ.get_idle_image()
        hover owl_OBJ.get_hover_image()
        tooltip "Check mail\n{{size=-4}}{} new message{}{{/size}}".format(num_to_word(len(mailbox.get_letters())), "s" if len(mailbox.get_letters()) > 1 else "")
        action Jump("letter_open_all")
        sensitive room_menu_active
    # add owl_OBJ.get_room_image() xpos owl_OBJ.xpos ypos owl_OBJ.ypos xanchor 0.5 yanchor 1.0

    # Owl deco
    if owl_deco_OBJ.room_image and renpy.get_screen("owl"):
        add owl_deco_OBJ.get_room_image() xpos owl_OBJ.xpos ypos owl_OBJ.ypos xanchor 0.5 yanchor 1.0 zoom 0.5

# Package
screen package():
    tag package
    imagebutton:
        xpos package_OBJ.xpos
        ypos package_OBJ.ypos
        xanchor 0.5
        yanchor 1.0
        idle package_OBJ.get_idle_image()
        hover package_OBJ.get_hover_image()
        tooltip "Open package"
        action Jump("parcel_open_all")
        sensitive room_menu_active
    # add package_OBJ.get_room_image() xpos package_OBJ.xpos ypos package_OBJ.ypos xanchor 0.5 yanchor 1.0
