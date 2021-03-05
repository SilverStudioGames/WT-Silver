
label desk:
    if game.day == 1:
        if not desk_examined:
            $ desk_examined = True
            $ desk_OBJ.idle = "ch_gen sit_behind_desk"
            call bld
            m "A desk of some sort..."
            m "And a letter..."
            m "Mailed to a certain \"Albus Dumbledore\"."

            menu:
                m "Should I open it?"
                "-Read the letter-":
                    call bld
                    g9 "Of course I will!"
                "-Leave it be-":
                    call bld
                    g4 "Hell no!"
                    g9 "Of course I will read it!"

            # First letter from Hermione
            $ desk_OBJ.foreground = None
            $ letter_hg_1.open()

            m "Ehm........."
            m "What?"
            m "................................."
        else:
            m "I already have checked the desk."

        if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    #Define hints variable
    $ ball_hint = None

    # TODO: Refactor. Low priority.

    call update_character_map_locations


    #Screens
    call play_sound("scroll")
    show screen desk_menu
    with d1

    $ _choice = ui.interact()

    hide screen desk_menu
    #Do NOT add a transition here!


    #Hermione
    if _choice == "hermione" and hermione_busy:
        if game.daytime:
            call nar(">Hermione is taking classes.")
            jump main_room_menu
        else:
            call nar(">Hermione is already asleep.")
            jump main_room_menu
    elif _choice == "hermione" and not hermione_busy:
        if her_map_location == "forest":
            call nar(">Hermione is currently at the Forbidden Forest.\n>Would you like to go there?")
            menu:
                "-Yes, pay her a visit-":
                    jump hermione_map_BJ
                "-No, summon her to your office-":
                    pass

        jump summon_hermione

    #Luna
    elif luna_known and _choice == "luna" and luna_busy:
        if game.daytime:
            call nar(">Luna is taking classes.")
            jump main_room_menu
        else:
            call nar(">Luna is already asleep.")
            jump main_room_menu
    elif luna_known and _choice == "luna" and not luna_busy:
        jump summon_luna

    #Astoria
    elif astoria_busy and _choice == "astoria":
        if game.daytime:
            call nar(">Astoria is taking classes.")
            jump main_room_menu
        else:
            call nar(">Astoria is already asleep.")
            jump main_room_menu
    elif not astoria_busy and _choice == "astoria": #Summoning after intro events done.
        jump summon_astoria

    #Susan
    elif _choice == "susan" and susan_busy:
        if game.daytime:
            call nar(">Susan is taking classes.")
            jump main_room_menu
        else:
            call nar(">Susan is already asleep.")
            jump main_room_menu
    elif _choice == "susan" and not susan_busy:
        jump summon_susan

    #Cho
    elif _choice == "cho" and cho_busy:
        if game.daytime:
            call nar(">Cho is taking classes.")
            jump main_room_menu
        else:
            call nar(">Cho is already asleep.")
            jump main_room_menu
    elif _choice == "cho" and not cho_busy:
        jump summon_cho

    #Snape
    elif _choice == "snape" and snape_busy:
        call nar(">Professor Snape is unavailable.")
        if game.daytime:
            jump main_room_menu
        else:
            jump main_room_menu
    elif _choice == "snape" and not snape_busy:
        jump summon_snape

    #Tonks
    elif _choice == "tonks" and tonks_busy:
        call nar(">Tonks is unavailable.")
        if game.daytime:
            jump main_room_menu
        else:
            jump main_room_menu
    elif _choice == "tonks" and not tonks_busy:
        jump summon_tonks

    #Close
    elif _choice == "Close":
        jump main_room_menu
    elif _choice in {"floor_7th", "map_lake", "map_forest", "map_attic", "clothing_store", "item_store", "ravenclaw_dormitories", "gryffindor_dormitories"}:
        call gen_chibi("stand", "desk", "base")
        with d3
        call gen_walk(action="leave", speed=1.5)

    $ renpy.jump(_choice)

screen desk_menu():
    tag desk_interface

    zorder 5

    #Background
    add "interface/desk/_bg_.webp"

    if map_unlocked:
        use map_screen

    # Ugly hands
    # add "interface/desk/_hands_.webp" xpos 0 ypos -30

    use crystal_ball
    use watch

    #Book
    if item_store_intro_done:
        add "interface/desk/book.webp" xalign 1.0 xpos 1080 ypos 0
        imagebutton:
            xpos 1080
            ypos 0
            xalign 1.0
            idle "interface/desk/book.webp"
            hover "interface/desk/book_hover.webp"
            hovered SetVariable("ball_hint", "book")
            keysym "inventory"
            unhovered SetVariable("ball_hint", None)
            action Return("inventory")

    #Tissue Box
    add "interface/desk/tissues.webp" xalign 1.0 xpos 1080 ypos 320
    imagebutton:
        xpos 1080
        ypos 320
        xalign 1.0
        idle "interface/desk/tissues.webp"
        hover "interface/desk/tissues_hover.webp"
        hovered SetVariable("ball_hint", "jerk_off")
        keysym "fap"
        unhovered SetVariable("ball_hint", None)
        action Return("jerk_off")

    #Work
    if letter_work_unlock.read:
        imagebutton:
            xpos -10
            ypos 0
            xalign 0.0
            idle "interface/desk/work.webp"
            hover "interface/desk/work_hover.webp"
            hovered SetVariable("ball_hint", "work")
            keysym "work"
            unhovered SetVariable("ball_hint", None)
            action Return("paperwork")

    #Cards
    if deck_unlocked: #Or letter_cards_unlock.read #Day 26+
        imagebutton:
            xpos 0
            ypos 600
            xalign 0.0
            yalign 1.0
            idle "interface/desk/cards.webp"
            hover "interface/desk/cards_hover.webp"
            hovered SetVariable("ball_hint", "cards")
            unhovered SetVariable("ball_hint", None)
            action Return("deck_builder")

    #exit
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 510
        ypos 600
        idle "interface/desk/exit_mask.webp"
        hover "interface/desk/exit.webp"
        hovered SetVariable("ball_hint", "exit")
        unhovered SetVariable("ball_hint", None)
        action Return("Close")

    #Night Overlay
    if not game.daytime:
        add "interface/desk/_night_overlay_.webp"

    use close_button


screen crystal_ball():
    tag desk_interface

    zorder 8

    add "interface/desk/crystal_ball.webp" xpos 268 ypos 0
    if not ball_hint == None:
        add "interface/desk/hints/glow.webp" xpos 268+40
        add "interface/desk/hints/"+str(ball_hint)+ ".webp" xpos 268+125 xanchor 0.5

screen watch():
    #Day/Night Clock
    add "interface/desk/watch.webp" xpos 603 ypos 0
    imagebutton:
        xpos 603
        ypos 0
        idle "interface/desk/watch.webp"
        hover "interface/desk/watch_hover.webp"
        unhovered SetVariable("ball_hint", None)
        keysym "sleep"
        hovered If(game.daytime, SetVariable("ball_hint", "doze_off"), SetVariable("ball_hint", "sleep"))
        action If(game.daytime, Return("night_start"), Return("day_start"))

    $ watch_x = 603 +67
    $ watch_y = 35

    if game.weather == "rain":
        add "interface/desk/watch/rain.webp" xpos watch_x ypos watch_y
    elif game.weather in ("snow", "blizzard"):
        add "interface/desk/watch/snow.webp" xpos watch_x ypos watch_y
    elif game.weather == "storm":
        add "interface/desk/watch/storm.webp" xpos watch_x ypos watch_y
    else:
        if game.daytime:
            add "interface/desk/watch/sun.webp" xpos watch_x ypos watch_y
        else:
            add "interface/desk/watch/moon.webp" xpos watch_x ypos watch_y

    if game.daytime:
        add "interface/desk/watch/day.webp" xpos watch_x+40 ypos watch_y+6 xanchor 0.5
    else:
        add "interface/desk/watch/night.webp" xpos watch_x+40 ypos watch_y+6 xanchor 0.5

label paperwork:
    if letter_work_report in mailbox.get_letters():
        m "I need to get paid first."
        jump main_room

    call weather_sound

    if not renpy.music.is_playing("weather"):
        call music_block
    else:
        stop music fadeout 1.0

    call gen_chibi("paperwork")
    with d3
    ">You do some paperwork."

    call paperwork_progress_chapter

    if not game.daytime and game.moon:
        call paperwork_full_moon

    $ speedwriting_check = renpy.random.randint(1, 3)

    if speed_writing == 1 and speedwriting_check == 1:
        # 1/3 chance
        call paperwork_speedwriting

    if speed_writing == 2 and speedwriting_check > 1:
        # 2/3 chance
        call paperwork_speedwriting

    if speed_writing == 3:
        call paperwork_speedwriting

    if speed_writing >= 4:
        call paperwork_speedwriting
        call paperwork_concentration

    call gen_chibi("sit_behind_desk")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label paperwork_report_check:
    # Check if a report was completed
    if report_chapters >= 4:
        ">You've completed a report."
        $ report_chapters = 0
        $ reports_finished += 1
        $ stat_reports_counter += 1

    return

label paperwork_progress_chapter(message = ""):
    $ report_chapters += 1
    call notes

    if report_chapters == 1:
        "[message]>You finished one chapter so far."
    else:
        "[message]>You finished {number=report_chapters} chapters so far."

    call paperwork_report_check
    return

label paperwork_full_moon:
    call paperwork_progress_chapter(">The Full moon makes you feel more productive.\n")
    return

label paperwork_concentration:
    call paperwork_progress_chapter(">You maintain perfect concentration during your work and finish another chapter of the report.\n")
    return

label paperwork_speedwriting:
    call paperwork_progress_chapter(">You use your Speedwriting skills and finish another chapter of the report.\n")
    return
