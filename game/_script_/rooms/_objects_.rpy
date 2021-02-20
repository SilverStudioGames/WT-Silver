default main_room = Room("main_room")

default fireplace_OBJ = RoomObject(main_room, "fireplace", pos=(693, 277), idle="fireplace_idle_shadow", focus_mask="fireplace_hover", foreground=None, action=Jump("fireplace"))
default cupboard_OBJ = RoomObject(main_room, "cupboard", pos=(260, 280), idle="cupboard_idle", action=Jump("cupboard"), tooltip="Rummage")
default phoenix_OBJ = RoomObject(main_room, "phoenix", pos=(557, 272), idle="phoenix_idle", hover="phoenix_hover", focus_mask="phoenix_idle", background="phoenix_feather", action=Jump("phoenix"), tooltip="Interact")
default door_OBJ = RoomObject(main_room, "door", pos=(898, 315), idle="door_idle", focus_mask="door_hover", action=Jump("door"), tooltip="Summon")
default candleL_OBJ = RoomObject(main_room, "candle_left", pos=(350, 160), idle="candle_left", focus_mask="candle_left", foreground=None, action=ToggleVariable("candleL_OBJ.foreground", "candle_fire", None))
default candleR_OBJ = RoomObject(main_room, "candle_right", pos=(833, 225), idle="candle_right", focus_mask="candle_right", foreground=None, action=ToggleVariable("candleR_OBJ.foreground", "candle_fire", None))
default desk_OBJ = RoomObject(main_room, "desk", pos=(370, 336), idle="ch_gen sit_behind_desk", hover="ch_gen sit_behind_desk_hover", focus_mask="ch_gen sit_behind_desk", action=Jump("desk"), hovered=Show("gui_tooltip", img="emo_exclaim", xx=335, yy=210), unhovered=Hide("gui_tooltip"), tooltip="Desk", zorder=1)
default poster_OBJ = RoomObject(main_room, "poster", pos=(364, 285), idle=Null(127, 166), action=Jump("enlarge_poster"), zorder=-1)
default trophy_OBJ = RoomObject(main_room, "trophy", pos=(670, 164), idle=Null(), action=None, zorder=-1)
default chair_OBJ = RoomObject(main_room, "chair", pos=(793, 300), idle="chair_right", action=None, zorder=0)

default owl_OBJ = RoomObject(main_room, "owl", pos=(455, 289), idle="owl_letter", hover="owl_letter_hover", action=Jump("letter_open_all"), tooltip="Check Mail", hidden=True, anchor=(0.5, 1.0))
default parcel_OBJ = RoomObject(main_room, "parcel", pos=(402, 290), idle="parcel", action=Jump("parcel_open_all"), tooltip="Check Parcel", hidden=True, anchor=(0.5, 1.0))

default room_menu_active = False

screen main_room_menu():
    tag room_menu
    on "show" action SetVariable("room_menu_active", True)
    on "hide" action SetVariable("room_menu_active", False)

screen main_room():
    tag room
    zorder 0
    sensitive room_menu_active

    default objects = sorted(main_room.objects, key=lambda x: x.zorder)

    # Hotkeys
    if room_menu_active and game.day > 1 and not renpy.android:
        use hotkeys_main

    use weather

    # Walls
    if game.daytime:
        add "main_room_idle_day"
    else:
        add "main_room_idle_night"

    for obj in objects:
        imagebutton:
            anchor obj.anchor
            pos obj.pos
            idle obj.get_idle()
            hover obj.get_hover()
            foreground obj.foreground
            background obj.background
            focus_mask obj.focus_mask
            tooltip obj.tooltip
            hovered obj.hovered
            unhovered obj.unhovered
            action obj.action

label enlarge_poster:
    show screen blktone
    show screen poster
    with d3

    call ctc

    hide screen blktone
    hide screen poster
    with d3

    jump main_room_menu

screen poster():
    zorder 25
    tag poster

    add poster_OBJ.decoration.image align (0.5, 0.5)
