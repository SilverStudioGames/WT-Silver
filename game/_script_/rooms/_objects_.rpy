default main_room = Room("main_room")

default fireplace_OBJ = RoomObject(main_room, "fireplace", pos=(693, 277), idle="fireplace_idle_shadow", focus_mask="fireplace_hover", foreground="fireplace_fire", action=ToggleVariable("fireplace_OBJ.foreground", "fireplace_fire", None))
default cupboard_OBJ = RoomObject(main_room, "cupboard", pos=(260, 280), idle="cupboard_idle", action=Jump("cupboard"), tooltip="Rummage")
default phoenix_OBJ = RoomObject(main_room, "phoenix", pos=(557, 272), idle="phoenix_idle", hover="phoenix_hover", focus_mask="phoenix_idle", foreground="phoenix_feather", action=Jump("phoenix"), tooltip="Interact")
default door_OBJ = RoomObject(main_room, "door", pos=(898, 315), idle="door_idle", focus_mask="door_hover", action=Jump("door"), tooltip="Summon")
default candleL_OBJ = RoomObject(main_room, "candle_left", pos=(350, 160), idle="candle_left", focus_mask="candle_left", foreground="candle_fire", action=ToggleVariable("candleL_OBJ.foreground", "candle_fire", None))
default candleR_OBJ = RoomObject(main_room, "candle_right", pos=(833, 225), idle="candle_right", focus_mask="candle_right", foreground="candle_fire", action=ToggleVariable("candleR_OBJ.foreground", "candle_fire", None))
default desk_OBJ = RoomObject(main_room, "desk", pos=(370, 336), idle="ch_gen sit_behind_desk", hover="ch_gen sit_behind_desk_hover", focus_mask="ch_gen sit_behind_desk", action=Jump("desk"), hovered=Show("gui_tooltip", img="emo_exclaim", xx=335, yy=210), unhovered=Hide("gui_tooltip"), tooltip="Desk", zorder=1)

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
            pos obj.pos
            anchor obj.anchor
            idle obj.get_idle()
            hover obj.get_hover()
            foreground obj.foreground
            background obj.background
            focus_mask obj.focus_mask
            tooltip obj.tooltip
            hovered obj.hovered
            unhovered obj.unhovered
            action obj.action
