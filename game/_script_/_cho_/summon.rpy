
label summon_cho:
    #call play_music("cho")
    #call play_sound("door")

    $ active_girl = "cho"
    $ last_character = "cho"

    $ cho_busy = True
    #call update_cho_tier
    call update_cho

    if has_cho_panties:
        jump cho_panties_response_T2

    # Slytherin Quidditch Intro.
    if cho_tier == 2 and not cho_quid.E5_complete:
        jump cho_quid_E5

    # Clothes Events
    call cho_summon_setup

    label cho_requests:

    # Reset
    call reset_menu_position
    call cho_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Main Matches
        "-Start Hufflepuff Match-" (icon="interface/icons/small/huff.webp") if (cho_tier == 1 and hufflepuff_match == "ready"):
            if cho_reputation == 0:
                m "(If I want Cho to do anything in public with those {i}Muffletuffs{/i} I better do it before the Match.)"
                m "(Although maybe not...)"
                menu:
                    "Are you ready to begin the match?"
                    "Yes":
                        pass
                    "no":
                        jump cho_requests
            jump start_hufflepuff_match

        "-Start Slytherin Match-" (icon="interface/icons/small/slyt.webp") if (cho_tier == 2 and slytherin_match == "ready" and cho_quid.E7_complete):
            if cho_reputation <= 3:
                m "(If I want Cho to do anything in public with those {i}Slythershits{/i} I better do it before the Match.)"
                m "(Although maybe not...)"
                menu:
                    "Are you ready to begin the match?"
                    "Yes":
                        pass
                    "no":
                        jump cho_requests
            jump start_slytherin_match

        #"-Start Gryffindor Match-" (icon="interface/icons/small/gryf.webp") if (cho_tier == 3 and gryffindor_match == "ready"):
        #    jump start_gryffindor_match


        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not cho_chatted:
                if cho_mood <= 3:
                    $ cho_chatted = True
                    #call cho_chit_chat
                    jump cho_talk
                else:
                    call cho_main("I have nothing to say to you, [cho_genie_name]...",face="annoyed")
                    jump cho_requests
            else:
                jump cho_talk

        # Quidditch Training
        "-Training-" (icon="interface/icons/small/quidditch.webp") if cho_tier < 3 and not cho_quid.lock_training:
            if cho_mood > 0:
                m "Ready to get back to training?"
                if cho_mood >= 5:
                    call cho_main("No.{w=0.5} And I don't want to hear of it right now, Sir.",face="angry")
                else:
                    call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like training today.", "soft", "base", "worried", "down")
                call nar(">Cho is still upset with you.")
                jump cho_requests

            jump cho_training

        "-Training-" (icon="interface/icons/small/quidditch.webp", style="disabled") if cho_tier < 3 and cho_quid.lock_training:
            m "(She's as ready as one can be.)"
            jump cho_requests

        "-Sexual favours-" (icon="interface/icons/small/condom.webp") if cho_favors_unlocked:
            if cho_mood > 0:
                call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like it today...", "upset", "base", "worried", "mid")
                jump cho_requests
            else:
                jump cho_favor_menu

        "-Sexual favours-" (icon="interface/icons/small/condom.webp", style="disabled") if not cho_favors_unlocked:
            if cho_tier == 1:
                m "(I need to help her with her Quidditch training, before I can ask for something like this.)"
            else:
                m "(I should ask her about the next Quidditch match first. See who we're up against...)"
            jump cho_requests

        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if cho_wardrobe_unlocked:
            hide screen cho_main with d1
            $ gui.in_context("wardrobe")
            with d2
            jump cho_requests

        "-Hidden-" (style="disabled") if not cho_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump cho_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_cho_gift:
            call gift_menu
            jump cho_requests

        "-Gifts-" (style="disabled") if gave_cho_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump cho_requests

        # Dismiss
        "-Dismiss Her-":
            stop music fadeout 3.0

            if cho_mood == 0:
                call cho_main("Goodbye, [cho_genie_name].",face="happy")
            else:
                call cho_main("Goodbye, [cho_genie_name].",face="annoyed")

            call play_sound("door")

            jump end_cho_event



# Cho Favor Menu
label cho_favor_menu:
    call update_cho_favors

    menu:
        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp"):
            label .personal:
            python:
                menu_choices = []
                for i in cc_favor_list:
                    if i in []: # Not in the game yet.
                        menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                    elif i.start_tier > cho_tier:
                        menu_choices.append(gui.menu_item("-Not ready-", "na", style="disabled"))
                    else:
                        menu_choices.append(i.get_menu_item())

                menu_choices.append(("-Never mind-", "nvm"))
                result = renpy.display_menu(menu_choices)

            if result == "nvm":
                jump cho_favor_menu
            elif result == "vague":
                call favor_not_ready
                jump .personal
            elif result == "na":
                call not_available
                jump .personal
            else:
                $ renpy.jump(result)

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime or not cho_requests_unlocked:
            if not cho_requests_unlocked:
                call nar(">You haven't unlocked this feature yet.")
            elif not game.daytime:
                call nar(">Public requests are available during the game.daytime only.")
            jump cho_favor_menu

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime and cho_requests_unlocked:
            jump cho_requests_menu

        "-Never mind-":
            jump cho_requests

label update_cho_favors:
    python:
        for i in cc_favor_list:
            i.tier = cho_tier
    return

# Cho Requests Menu
label cho_requests_menu:
    call update_cho_requests
    python:
        menu_choices = []
        for i in cc_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                menu_choices.append(gui.menu_item())
            elif i.start_tier > cho_tier:
                menu_choices.append(gui.menu_item("-Not ready-", "na", style="disabled"))
            else:
                menu_choices.append(i.get_menu_item())
        menu_choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(menu_choices)

    if result == "nvm":
        jump cho_favor_menu
    elif result == "vague":
        call favor_not_ready
        jump cho_requests
    elif result == "na":
        call not_available
        jump cho_requests
    else:
        $ renpy.jump(result)

label update_cho_requests:
    # Set event tier to current Cho tier if they are different
    python:
        for i in cc_requests_list:
            i.tier = cho_tier
    return

label favor_not_ready:
    call nar(">You can't do this favour just yet.")
    return

label not_available:
    $ TBA_message("This feature is currently not available as of version %s." % title_version)
    return

# Cho Talk
label cho_talk:
    menu:
        #"-Working-":

        "-Discuss Quidditch Training-" (icon="interface/icons/small/quidditch.webp") if not cho_quid.lock_training:
            if cho_tier == 1:
                jump cc_ht_talk
            elif cho_tier == 2:
                jump cc_st_talk

            jump cho_talk

        # Naming
        "\"Address me only as\"" if not cho_quid.lock_training:
            menu:
                "\"Professor\"":
                    $ cho_genie_name = "Professor"
                "\"Coach\"":
                    $ cho_genie_name = "Coach"
                "\"Old Man\"":
                    $ cho_genie_name = "Old Man"
                "\"Daddy\"":
                    $ cho_genie_name = "Daddy"
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", cho_genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name == "":
                        jump cho_talk
                    $ cho_genie_name = temp_name
                    call cho_main("If I really have to...",face="annoyed")
                    jump cho_talk
                "\"Never mind\"":
                    jump cho_talk

            call cho_main("Of course, [cho_genie_name]...",face="neutral")
            jump cho_talk

        "\"From now on I will refer to you as\"" if not cho_quid.lock_training:
            menu:
                "\"Miss Chang\"":
                    $ cho_name = "Miss Chang"
                "\"Princess\"":
                    $ cho_name = "Princess"
                "\"Boy\"":
                    $ cho_name = "Boy"
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", cho_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name == "":
                        jump cho_talk
                    $ cho_name = temp_name
                    call cho_main("If you say so, [cho_genie_name].",face="neutral")
                    jump cho_talk
                "\"Never mind\"":
                    jump cho_talk

            call cho_main("Very well...",face="neutral")
            jump cho_talk

        "\"Never mind\"":
            jump cho_requests
