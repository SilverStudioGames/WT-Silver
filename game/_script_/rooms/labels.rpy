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

        # Show main_room and (optional) objects
        show screen main_room
        #show screen chair_right
        # show screen fireplace

        # if fire_in_fireplace:
        #     show screen fireplace_fire
        # else:
        #     hide screen fireplace_fire

        # if phoenix_is_fed:
        #     show screen phoenix_food
        # else:
        #     hide screen phoenix_food

        if mailbox.get_letters() and not owl_away:
            show screen owl

        if mailbox.get_parcels():
            show screen package

        #call gen_chibi("sit_behind_desk")

        # User interface
        call update_ui_points
        show screen ui_top_bar

    if room == "weasley_store":
        show screen weasley_store_room

    if room == "potions_room":
        show screen potions_room

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
    if not desk_examined:
        show screen letter_on_desk
    with d3

    call reset_menu_position
    call music_block

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
    call room("main_room", stop_sound=False)
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
