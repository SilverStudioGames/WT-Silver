
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
            sensitive (room_menu_active and not (game.day == 1 and desk_examined))

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
