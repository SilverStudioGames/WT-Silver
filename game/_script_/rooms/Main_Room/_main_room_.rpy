
screen gui_tooltip(img=None, xx=335, yy=210):
    add img xpos xx ypos yy
    zorder 3

label main_room:
    call room("main_room", stop_sound=False)
    call reset_menu_position
    call music_block
    call gen_walk(action="enter", xpos="desk", ypos="base", speed=1.5)
    call gen_chibi("sit_behind_desk")
    with d3

    if game.daytime:
        jump day_resume
    else:
        jump night_resume

# Return to main_room at menu point (after quests and events)
# Used to return from main room interactions
label main_room_menu:
    hide screen bld1
    with d3

    call reset_menu_position

    if game.daytime:
        jump day_resume
    else:
        jump night_resume
