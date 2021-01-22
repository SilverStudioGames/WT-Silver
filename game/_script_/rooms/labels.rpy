# Set the scene for a given room
label room(room=None, hide_screens=True, stop_sound=True):

    # Hide all screens (only room related screens are shown)
    if hide_screens:
        call hide_screens

    # Stop sound effects (necessary when changing rooms)
    if stop_sound:
        call stop_sound_effects

    $ renpy.stop_predict("images/rooms/{}/*.webp".format(current_room))
    $ current_room = room
    $ renpy.start_predict("images/rooms/{}/*.webp".format(current_room))

    if room == "main_room":
        # Update sound effects
        call weather_sound
        call fireplace_sound

        show screen main_room

        if mailbox.get_letters() and not owl_away:
            $ owl_OBJ.hidden = False

        if mailbox.get_parcels():
            $ parcel_OBJ.hidden = False

        # User interface
        call update_ui_points
        show screen ui_top_bar

    if room == "weasley_store":
        show screen weasley_store_room

    if room == "clothing_store":
        show screen clothing_store

    if room == "floor_seven":
        show screen floor_7th_screen
        if not first_time_7th:
            show screen floor_7th_door

    if room == "room_of_requirement":
        show screen room_of_requirement

    if room == "quidditch_pitch":
        show screen quid_pitch_back
        show screen quid_pitch_mid
        show screen quid_pitch_front

    if room == "quidditch_stands":
        call quidditch_stands(reset=True)

    return

# Return to main_room at resume point (after quests, before events)
# If game.daytime change was deferred during an event, return to the start of the current game.daytime
# Used to return from event sequences
label main_room:
    call room("main_room", stop_sound=False)
    call reset_menu_position
    call music_block
    call gen_walk(action="enter", xpos="desk", ypos="base", speed=1.5)
    call gen_chibi("sit_behind_desk")
    with d3

    if defer_daytime_change:
        if game.daytime:
            jump day_start
        else:
            jump night_start
    else:
        if game.daytime:
            jump day_resume
        else:
            jump night_resume

# Return to main_room at menu point (after quests and events)
# Used to return from main room interactions
label main_room_menu:
    #call room("main_room", stop_sound=False)
    hide screen bld1
    with d3

    call reset_menu_position
    call music_block

    if game.daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label fireplace_sound:
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 0.5 fadein 0.5 if_changed
    else:
        stop bg_sounds fadeout 0.5
    return
