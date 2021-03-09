label door:
    if game.day == 1:
        if not door_examined:
            $ door_examined = True
            $ door_OBJ.idle = "door_idle"
            call gen_chibi("stand","door","base")
            with d5

            m "A sturdy-looking door..."
            m "I wonder what's behind it."
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone
                    with d3
                    call play_sound("knocking")
                    "*Knock-knock-knock*"
                    "..................."
                    hide screen blktone
                    with d3
                    m "No reply..."
                "-Put your ear on it-":
                    show screen blktone
                    with d3
                    ">You put your ear on the door and listen intently..."
                    m "I don't hear anything."
                    hide screen blktone
                    with d3
                "-Kick the door-":
                    show screen blktone
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Thump!*"
                    $ renpy.sound.play("sounds/MaleGasp.mp3")
                    g4 "Blimey! That hurts!"
                    ".............................."
                    hide screen blktone
                    with d3
                    m "This door could take a thousand kicks and it still wouldn't break..."
                "-Smell the door-":
                    show screen blktone
                    with d3
                    $ renpy.sound.play("sounds/sniff.mp3")
                    m "...{w} Smells like a door..."
                    hide screen blktone
                    with d3
                "-Leave it alone-":
                    m "Who knows what kind of dangers could be lurking behind that door?"
                    m "I think I'll let it be for now..."

            call gen_chibi("sit_behind_desk")
            with d3
        else:
            m "I should leave this door alone for now."

        if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    call update_character_map_locations

    call play_sound("scroll")
    jump summon
