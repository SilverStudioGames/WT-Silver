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

        show screen main_room

        if mailbox.get_letters() and not owl_away:
            $ owl_OBJ.hidden = False
            call play_sound("owl")

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
