label start_wt:
    call play_music("prologue")
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
    show screen close_button(close_action=MainMenu())

    label choose_your_difficulty:
    menu:
        "Difficulty" ">How difficult do you want the game to be?"
        "-Play with easy difficulty-":
            menu:
                "Easy" "{cps=*2}>Increased gold and Slytherin-points gain.\nYou will always find items or gold in your cupboard.\nBad mood will decrease faster.\nBooks can be read in one go.{/cps}"
                "-Confirm-":
                    ">Game set to easy!"
                    call adjust_game_difficulty(1)
                "-Choose something else-":
                    jump choose_your_difficulty
        "-Play with normal difficulty-":
            menu:
                "Normal" "{cps=*2}>Balanced gold and Slytherin-points gain.\nRandom chance of finding items or gold in your cupboard.\nBad mood will decrease gradually.\nBooks take time to read.{/cps}"
                "-Confirm-":
                    ">Game set to normal!"
                    call adjust_game_difficulty(2)
                "-Choose something else-":
                    jump choose_your_difficulty
        "-Play with hardcore difficulty-" if persistent.game_complete:
            menu:
                "Hardcore" "{cps=*2}>Reduced gold and Slytherin-points gain.\nAll hints and guides are disabled.\nAdditional rewards and dialogue choices are added.{/cps}"
                "-Confirm-":
                    ">Game set to hardcore!"
                    call adjust_game_difficulty(3)
                "-Choose something else-":
                    jump choose_your_difficulty

    if persistent.game_complete and game_difficulty <= 2: # Offer for game+
        menu:
            "NEW GAME +" ">Would you like to carry over your gold and possessions from your previous playthrough?"
            "-Yes please-":
                # Code needed here for adding persistant items across games
                $ gold = gold + persistent.gold
                ">[persistent.gold] gold has been added to your founds."

                #$ candy_gift_list = persistent.candy_gift_list
                #$ drink_gift_list = persistent.drink_gift_list
                #$ mag_gift_list   = persistent.mag_gift_list
                #$ toy_gift_list   = persistent.toy_gift_list
                #">All previously bought gift items have been added to your possessions."

                #if persistent.wine >= 1:
                #    $ wine = wine + persistent.wine # WINE.
                #    ">[persistent.wine] bottles of Dumbledore's wine have been added to your possessions."

                #$ scroll_list_A = persistent.scroll_list_A
                #$ scroll_list_B = persistent.scroll_list_B
                #$ scroll_list_C = persistent.scroll_list_C
                #">Your unlocked scrolls have been added to your possessions."

            "-No need-":
                pass

    if game_difficulty <= 2:
        menu:
            "Cheats" "> Cheats can be found in the options menu at the top left of the screen.\nDisclaimer: Cheats may cause various bugs and instabilities."
            "-Activate Cheats-":
                $ cheats_active = True
            "-Disable Cheats-":
                $ cheats_active = False

    menu:
        "Animations" ">Would you like to use chibi animations, or CG images when available?\nThis can be changed in the preferences menu."
        "-Use chibis-":
            $ use_cgs = False
        "-Use CG images-":
            $ use_cgs = True

    if cheats_active or persistent.game_complete:
        menu:
            "Skip content" ">Would you like to skip early sections of the game?"
            "-Play the intro-": # {p}{size=-6}{color=#ffae19}new content!{/color}{/size}
                $ skip_to_hermione = False
            "-Skip to Hermione-" if cheats_active or persistent.game_complete:
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
    $ set_weather("clear")
    $ daytime = True
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
    show screen owl
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
