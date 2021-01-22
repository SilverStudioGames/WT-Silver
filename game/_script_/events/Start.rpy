label start_wt:
    show screen blkfade
    with d3
    pause 1

    hide screen blkfade
    show image "images/rooms/_bg_/castle.webp"
    with d9

    call update_interface_color("gray")
    $ menu_x = 0.5
    $ menu_y = 0.7

    $ disable_game_menu()
    show screen close_button(action=MainMenu())

    label choose_your_difficulty:
    menu:
        "Difficulty" ">How difficult do you want the game to be?"
        "-Easy-{size=-8}\nIncreased gold, item drop rate and Slytherin-points gains.\nMood will improve faster.{/size}":
            $ game.difficulty = 1
        "-Normal-{size=-8}\nBalanced gold, item drop rate and Slytherin-points gains.\nMood will improve normally.{/size}":
            $ game.difficulty = 2
        "-Hardcore-{size=-8}\nReduced gold, item drop rate and Slytherin-points gains.\nMood will not improve over time.\nHints and guides are disabled.{/size}" if persistent.game_complete:
            $ game.difficulty = 3

    if persistent.game_complete:
        menu:
            "NEW GAME+" ">Would you like to carry over your hard earned gold from your previous playthrough?"
            "-Yes please-":
                $ game.gold += (persistent.gold or 0)
                ">[persistent.gold] gold has been added to your funds."

            "-No need-":
                pass

    if game.difficulty <= 2:
        menu:
            "Cheats" "> Cheats can be found in the options menu at the top left of the screen.\nDisclaimer: Cheats may cause various bugs and instabilities."
            "-Activate Cheats-":
                $ game.cheats = True
            "-Disable Cheats-":
                $ game.cheats = False

    if game.cheats or persistent.game_complete:
        menu:
            "Skip content" ">Would you like to skip early sections of the game?"
            "-Play the intro-": # {p}{size=-6}{color=#ffae19}new content!{/color}{/size}
                $ skip_to_hermione = False
            "-Skip to Hermione-" if game.cheats or persistent.game_complete:
                $ skip_to_hermione = True

    hide screen close_button

    ### GAME STARTS HERE ###
    stop music fadeout 1
    hide image "images/rooms/_bg_/castle.webp"
    call screen loading
    with d7

    $ enable_game_menu()

    ### CHEATS / SKIPPING ###
    if skip_to_hermione:
        $ renpy.block_rollback()
        jump skip_to_hermione

    ### START ANIMATION ###
    call stop_sound_effects
    $ game.weather = "clear"
    $ game.daytime = False
    $ game.day = 0
    call update_interface_color
    call room("main_room")
    call gen_chibi("hide")
    show screen dumbledore
    show screen letter_on_desk
    hide screen blkfade
    with d3
    pause 1

    call teleport("desk", poof_label="swap_dumb_genie")
    call reset_menu_position

    $ renpy.block_rollback()
    jump day_start

label swap_dumb_genie:
    hide screen dumbledore
    call gen_chibi("sit_behind_desk")
    return

# First event in the game. Gennie finds himself at the desk.
label genie_intro_E1:

    call bld
    m "..................?"
    m "Your majesty?"
    m "......................................................."
    g4 "I did it again, didn't I?"
    g4 "Teleported myself to who knows where..."
    m "What's with those ingredients?"
    m "They seem to be way more potent than I thought."
    m "Well, whatever this place is I have no business here..."
    m "Better undo the spell and return to the shop before the princess gets angry with me again..."
    m "....................."
    m "Although..."
    m "There is something odd about this place... it's..."
    m "It's almost brimming with..."
    g4 "{size=+5}MAGIC?!{/size}"
    m "Yes... magic, I can feel it. So powerful and yet somehow..."
    m "... alien."
    m "Interesting..."
    m "I think I will stick around for a little bit..."

    $ achievement.unlock("start")
    $ genie_intro.E1_complete = True

    jump main_room

label genie_intro_E2:
    call bld
    m "It's getting darker already..."
    m "Did I just spend an entire day examining this room?"
    call bld("hide")

    $ genie_intro.E2_complete = True

    jump night_start

# Owl intro.
label genie_intro_E3:
    pause.2
    call play_sound("owl")
    $ owl_OBJ.hidden = False
    with d1
    pause.6

    call bld
    m "What? An owl?"
    call bld("hide")

    $ genie_intro.E3_complete = True

    jump main_room

label skip_to_hermione:
    call cheats.hermione_skip_intro

    jump day_start
