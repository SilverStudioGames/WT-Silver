label start_wt:
    $ disable_game_menu()

    show screen blkfade
    with d3
    show image "images/rooms/_bg_/castle.webp"
    call update_interface_color("gray")
    hide screen blkfade
    with d3
    show screen close_button(action=MainMenu())

    menu:
        "Difficulty" ">How difficult do you want the game to be?"
        "-Easy-{size=-8}\nIncreased gold, item drop rate and Slytherin-points gains.\nMood will improve faster.\nCheats are available.{/size}":
            $ game.difficulty = 1
            $ game.cheats = True
        "-Normal-{size=-8}\nBalanced gold, item drop rate and Slytherin-points gains.\nMood will improve normally.\nCheats are available.{/size}":
            $ game.difficulty = 2
            $ game.cheats = True
        "-Hardcore-{size=-8}\nReduced gold, item drop rate and Slytherin-points gains.\nMood will not improve over time.\nNo cheats.{/size}":
            $ game.difficulty = 3
            $ game.cheats = False

    if persistent.game_complete:
        menu:
            "NEW GAME+" ">Would you like to carry over your hard earned gold from your previous playthrough?"
            "-Yes please-":
                $ game.gold += (persistent.gold or 0)
                ">[persistent.gold] gold has been added to your funds."

            "-No need-":
                pass

    menu:
        "Skip content" ">Would you like to skip early sections of the game?"
        "-Play the intro-":
            pass
        "-Skip the intro-":
            jump skip_to_hermione

    hide image "images/rooms/_bg_/castle.webp"
    hide screen close_button
    call screen loading
    $ enable_game_menu()

    jump genie_intro_E0

label genie_intro_E0:
    $ game.weather = "clear"
    $ game.daytime = False
    $ game.day = 0
    stop bg_sounds
    stop weather

    call update_interface_color
    call room("main_room")
    call gen_chibi("hide")
    call play_music("intro")
    $ desk_OBJ.idle = "desk_dumbledore"
    $ desk_OBJ.foreground = "letter_on_desk"
    hide screen blkfade
    with d5

    pause 0.5
    $ renpy.block_rollback()

    $ dumbledore_name = "Old Bearded Man"

    $ renpy.sound.play("sounds/snore1.mp3")
    dum1 "*Sounds of an old man sleeping like a baby*"
    pause 1
    $ renpy.sound.play("sounds/thunder_2.mp3")
    $ game.weather = "storm"
    call weather_sound
    with flashbulb
    dum3 "Oh my!"
    dum2 "A storm at this time? But my watch is never wrong."
    dum1 "*Hmmm*... How curious."
    dum2 "It begins to dawn, maybe I should--"

    $ dumbledore_name = "Albus Dumbledore"

    $ renpy.play("sounds/magic4.ogg")
    $ desk_OBJ.idle = "ch_gen sit_behind_desk"
    with flash

    pause 1.0

    jump day_start

label genie_intro_E1:
    $ game.weather = "rain"
    call weather_sound

    call bld
    g4 "Your majesty! Don't touch--"
    m "............................."
    m "I did it again, didn't I?"
    g4 "Teleported myself to who knows where..."
    m "What's up with those magical ingredients?"
    m "They seem to be way more potent than I thought."
    m "Well, whatever this place is I have no business here..."
    m "Better to undo the spell and return to my magic shop before princess Jasmine gets angry with me again..."
    m "....................."
    m "Although..."
    m "There is something odd about this place..."
    m "It's almost brimming with..."
    g4 "{size=+5}MAGIC?!{/size}"
    m "Yes... magic, I can feel it. So powerful and yet somehow..."
    m "... alien."
    m "Interesting..."
    m "I think I will stick around for a little bit..."

    $ achievement.unlock("start")
    $ genie_intro.E1_complete = True

    jump main_room_menu

label genie_intro_E2:
    call bld
    m "It's getting darker already..."
    m "Did I just spend an entire day examining this room?"
    call bld("hide")

    $ genie_intro.E2_complete = True

    # Next is Snape intro E1

    jump night_start

# Owl intro.
label genie_intro_E3:
    pause.2
    call play_sound("owl")
    call play_music("day")
    $ owl_OBJ.hidden = False
    with d1
    pause.6

    call bld
    m "An owl? Here?"
    call bld("hide")

    $ genie_intro.E3_complete = True

    jump main_room_menu

label skip_to_hermione:
    $ renpy.block_rollback()

    hide image "images/rooms/_bg_/castle.webp"
    hide screen close_button
    call screen loading
    $ enable_game_menu()

    call cheats.hermione_skip_intro

    jump day_start
