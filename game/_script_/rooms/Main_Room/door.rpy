label door:
    if game.day == 1:
        if not door_examined:
            $ door_examined = True
            jump examine_door
        jump main_room_menu

    call update_character_map_locations

    call play_sound("scroll")
    jump door_menu

# Day 1 room interact quest
label examine_door:
    $ door_examined = True
    show screen chair_left
    show screen chair_right
    show screen desk
    call gen_chibi("stand","door","base")
    with d5

    m "A sturdy-looking door..."
    m "I wonder what's behind it."
    label examining_the_door:
    menu:
        "-Knock on the door-":
            show screen blktone(0.8)
            with d3
            call play_sound("knocking")
            "*Knock-knock-knock*"
            "..................."
            hide screen blktone
            with d3
            m "No reply..."
            jump examining_the_door
        "-Put your ear on it-":
            show screen blktone(0.8)
            with d3
            ">You put your ear on the door and listen intently..."
            m "I don't hear anything."
            hide screen blktone
            with d3
            jump examining_the_door
        "-Kick the door-":
            show screen blktone(0.8)
            with d3
            $ renpy.play('sounds/kick.ogg')
            pause.2
            with hpunch
            "*Thump!*"
            ".............................."
            hide screen blktone
            with d3
            m "This door could take a thousand kicks like that and it still wouldn't break..."
            m "It doesn't look like it's locked though..."
            jump examining_the_door
        "-Leave it alone-":
            m "Who knows what kind of dangers could be lurking behind that door?"
            m "I think I'll let it be for now..."
            pass

    call gen_chibi("sit_behind_desk")
    with d3

    jump main_room_menu
