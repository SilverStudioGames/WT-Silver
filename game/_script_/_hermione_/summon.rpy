

label summon_hermione:
    #call play_music("hermione")
    #call play_sound("door")

    $ active_girl = "hermione"
    $ last_character = "hermione"

    $ hermione_busy = True

    call update_hermione
    call update_her_tier

    # Clothes Events
    call hermione_summon_setup

    label hermione_requests:

    # Reset
    call reset_menu_position
    call her_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not chitchated_with_her:
                if her_mood <= 3:
                    $ chitchated_with_her = True
                    call chit_chat
                    jump hermione_talk
                else:
                    her "I have nothing to say to you sir..."
                    jump hermione_requests
            else:
                jump hermione_talk


        # Tutoring
        "-Tutoring-" (icon="interface/icons/small/book.webp") if not game.daytime and her_tutoring < 15: #14 is last level.
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, maybe tomorrow..."
                jump hermione_requests
            elif her_mood >=3 and her_mood < 10:
                her "I am not in the mood today..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "Absolutely not, [genie_name]."
                her "I {i}might{/i} consider it once you've said sorry..."
                jump hermione_requests
            elif her_mood >=20:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            else:
                jump hg_tutor_start

        "-Tutoring-" (icon="interface/icons/small/book.webp", style="disabled") if game.daytime and her_tutoring < 15:
            call nar("> Tutoring is available during the night only.")
            jump hermione_requests


        # Favours
        "-Sexual favours-" (icon="interface/icons/small/condom.webp") if hermione_favors:
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, [genie_name], Maybe some other time..."
                jump hermione_requests
            elif her_mood >=  3 and her_mood < 10:
                her "I don't feel like it today..."
                her "Maybe in a couple of days..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "No thank you..."
                jump hermione_requests
            elif her_mood >= 20 and her_mood < 30:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            elif her_mood >= 30 and her_mood < 40:
                her "You can't be serious!"
                jump hermione_requests
            elif her_mood >= 40:
                her "Is this some twisted joke to you, sir?!"
                her "After what you did I don't feel like doing this ever again!"
                jump hermione_requests
            else:
                jump hermione_favor_menu


        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if hermione_wardrobe_unlocked: # Unlocks after first summoning her.
            hide screen hermione_main with d1
            $ gui.in_context("wardrobe")
            with d2
            jump hermione_requests

        # Card game
        "-Let's Duel-" (icon="interface/icons/small/cards.webp") if snape_second_win:
            jump hermione_cardgame_menu

        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_hermione_gift:
            call gift_menu
            jump hermione_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp", style="disabled") if gave_hermione_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump hermione_requests


        # Dismiss
        "-Dismiss her-":
            stop music fadeout 3.0

            if game.daytime:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "*Humph*!..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "*Tch*..."
                else:
                    her "Oh, alright. I will go to bed then."

            call play_sound("door")

            jump end_hermione_event



label update_her_tier:
    if her_tier == 1 and her_whoring >= 3:
        # Trigger: None
        $ her_level_up = 1
    elif her_tier == 2 and her_whoring >= 9 and hg_jerkoff.trigger == True:
        # Trigger: When you get caught jerking off.
        if game.difficulty >= 3 and imagination < 2: # Hardcore only
            return
        $ her_level_up = 2
    elif her_tier == 3 and her_whoring >= 12 and hg_strip.trigger == True:
        # Trigger: After she strips for you.
        if game.difficulty >= 3 and imagination < 3: # Hardcore only
            return
        $ her_level_up = 3
    elif her_tier == 4 and her_whoring >= 18 and hg_kiss.trigger == True:
        # Trigger: None
        if game.difficulty >= 3 and imagination < 4: # Hardcore only
            return
        $ her_level_up = 4
    elif her_tier == 5 and her_whoring >= 21 and hg_blowjob.trigger == True:
        # Trigger: First BJ
        if game.difficulty >= 3 and imagination < 5: # Hardcore only
            return
        $ her_level_up = 5

    return


label hermione_level_up(tier=None):

    call bld
    if tier == 1:
        show screen blktone
        with d3
        ">Hermione's second {i}favour tier{/i} is now available."
        ">You can move up {i}favour tiers{/i} by increasing her {i}whoring level{/i}, and by triggering {i}favour milestones{/i}."
        if game.difficulty >= 3: # Hardcore, books are required.
            ">In addition, it is also required of you to increase your {i}imagination level{/i} by reading {i}fictional books{/i}, to unlock Hermione's next tier of favours."
        ">Each tier unlocks a new set of favours, but favours of the previous tier will no longer be available."
        hide screen blktone
        with d3
        pause.5
        menu:
            "Would you like to increase Hermione's {i}favour tier{/i} now?"
            "-Yes, increase her tier-":
                pass
            "-No, stay on her current tier-":
                return

    elif tier == 2:
        m "(I wonder if she's ready for some more advanced favours now...)"
    elif tier == 3:
        m "(...)"
        m "(Would she know what a handjob is...?)"
    elif tier == 4:
        m "(I wonder if I can get her to suck me off today...)"
        g4 "(I'm dying to feel that mouth around my cock!)"
    elif tier == 5:
        m "(Yes, I think it's time...)"
        g4 "(I'm gonna put my \"P\" in her \"V\"!)"

    $ her_tier = tier+1
    $ her_level_up = None
    $ her_mood = 0

    pause.5
    call nar(">Hermione has reached {i}favour tier{/i} "+str(her_tier)+"!")

    call update_her_tier

    return

label hermione_favor_menu:
    call update_her_favors
    call update_her_requests

    if slytherin >= gryffindor or ravenclaw >= gryffindor or hufflepuff >= gryffindor:

        label silver_requests_root:
        menu:
            "-Level Up-" (icon="interface/icons/small/levelup.webp") if her_level_up != None:
                call hermione_level_up(tier=her_level_up)
                jump hermione_favor_menu

            "-Personal favours-" (icon="interface/icons/small/heart_red.webp"):
                call tutorial("hearts")

                label .personal:
                python:
                    menu_choices = []
                    for i in hg_favor_list:
                        if i in []: # Not in the game yet.
                            menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                        elif i.start_tier > her_tier:
                            menu_choices.append(gui.menu_item("-Vague idea-", "vague", style="disabled"))
                        else:
                            menu_choices.append(i.get_menu_item())

                    menu_choices.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(menu_choices)

                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call favor_not_ready
                    jump .personal
                elif result == "na":
                    call not_available
                    jump .personal
                else:
                    $ renpy.jump(result)

            "-Public requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime:
                call nar(">Public requests are available during the day only.")
                jump silver_requests_root

            "-Public requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime:
                if her_reputation >= 16 and not public_whore_ending:
                    # Public whore ending choice
                    $ renpy.choice_for_skipping()
                    $ renpy.music.set_volume(0.5, 1.0)
                    nar "Attention!{w=1.0} If you continue tarnishing Hermione's reputation you will lock yourself towards certain game ending. (Public route)"
                    menu:
                        nar "Do you wish to continue?\n{size=-4}(You won't be asked again){/size}"
                        "Yes, I do.":
                            $ renpy.music.set_volume(1.0, 1.0)
                            $ public_whore_ending = True
                        "No, go back.":
                            $ renpy.music.set_volume(1.0, 1.0)
                            jump silver_requests_root

                label .public:
                python:
                    menu_choices = []
                    for i in hg_requests_list:
                        if i in []: # Not in the game yet.
                            menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                        elif i.start_tier > her_tier:
                            menu_choices.append(gui.menu_item("-Vague idea-", "vague", style="disabled"))
                        else:
                            menu_choices.append(i.get_menu_item())

                    menu_choices.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(menu_choices)

                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call favor_not_ready
                    jump .public
                elif result == "na":
                    call not_available
                    jump .public
                else:
                    $ renpy.jump(result)

            "-Public Shaming-" (icon="interface/icons/small/star_pink.webp", style="disabled") if not game.daytime:
                call nar(">Public Shaming events are available during the day only.")
                jump silver_requests_root

            "-Public Shaming-" (icon="interface/icons/small/star_pink.webp")if game.daytime:
                label not_now_ps:
                python:
                    menu_choices = []
                    for i in hg_ps_list:
                        if i.tier > her_tier:
                            menu_choices.append(gui.menu_item("-Vague idea-", "vague", style="disabled"))
                        else:
                            menu_choices.append(i.get_menu_item())
                    menu_choices.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(menu_choices)

                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call favor_not_ready
                    jump not_now_ps
                else:
                    $ renpy.jump(result)

            "-Never mind-":
                jump hermione_requests
    else:
        show screen hermione_main
        with d3
        if hermione_favors_convinced:
            call her_main("But we're in the lead already...", "base", "base", "base", "mid_soft")
            if her_whoring >=20 and hermione_favors_convinced == 2:
                call her_main("But I'll do anything for you, [genie_name]...", "smile", "happy", "base", "mid")
                jump silver_requests_root
            elif her_whoring >=18 and hermione_favors_convinced == 2:
                call her_main("I guess you do have a way with words,[genie_name]... I'll do it.", "soft", "wink", "base", "mid")
                jump silver_requests_root
            elif her_whoring >=16:
                call her_main("I have told you before, [genie_name], it was just a one time thing...", "open", "happy", "base", "mid")
                m "What about tomorrow though?"
                call her_main("What about tomorrow?","base","squint")
                g9 "I made a graph detailing the current daily average points Slytherin gain... doesn't look that great."
                m "Just think about it."
                jump hermione_favors_convinced_check
        else:
            her "The Gryffindor house is in the lead. I don't need to do this."
            if her_whoring >= 15:
                menu:
                    "-Change her mind-":
                        m "Are you sure it's not within your house best interests?"
                        call her_main("What do you mean?", "base", "happy", "base", "mid")
                        g9 "Think about the future..."
                        label hermione_favors_convinced_check:
                        if her_whoring >=20:
                            m "If you do it now it could secu--"
                            call her_main("I'll do it!", "smile", "happy", "base", "R")
                            m "Just like that?!"
                            call her_main("Yes... just like that.", "smile", "closed", "base", "mid")
                            g9 "That's my [hermione_name] right there!"
                            $ hermione_favors_convinced = 2
                            jump silver_requests_root

                        m "If you do it, you could secure the win for you household you know..."

                        if her_whoring >=18:
                            call her_main("You really know how to talk me through, [genie_name].", "soft", "narrow", "worried", "down")
                            call her_main("Okay I agree.", "open", "narrow", "base", "down")
                            $ hermione_favors_convinced = 2
                            jump silver_requests_root
                        elif her_whoring >=16 and not hermione_favors_convinced == 1:
                            call her_main("I guess you're right...", "open", "happy", "base", "mid_soft")
                            call her_main("I'll do it... but just this once okay?", "grin", "happyCl", "base", "mid")
                            $ hermione_favors_convinced = 1
                            jump silver_requests_root
                        else:
                            call her_main("I could...", "soft", "narrow", "base", "mid_soft")
                            call her_main("But I don't want to.", "normal", "closed", "base", "mid")
                            jump hermione_requests
                    "-Forget it-":
                        pass
            else:
                if sna_friendship <= 10:
                    m "What do you mean in the lead?"
                    g4 "Explain yourself, [hermione_name]!"
                    call her_main("With the current points distribution, I am certain getting the house cup for Gryffindor will be just a formality.", "smile", "closed", "base", "mid")
                    call her_main("Thank you, [genie_name], but I don't need any more points.", "smile", "base", "base", "mid")
                    g4 "(That little...)"
                    m "(Perhaps I should hangout with that Snape dude tonight, he might know what to do.)"
                    call her_main("Do you need anything else, [genie_name]?", "smile", "base", "base", "mid")
                else:
                    m "Right..."
                    m "(I guess another hangout with Snape is in order.)"
        jump hermione_requests


label update_her_favors:
    python:
        for i in hg_favor_list:
            i.tier = her_tier

    return


label update_her_requests:
    python:
        for i in hg_requests_list:
            i.tier = her_tier

    return


label hermione_talk:
    menu:
        "-Working-" (icon="interface/icons/small/gold.webp"):
            label working_menu:
            menu:
                "-Work as a maid-" if game.daytime and hg_maid.unlocked:
                    jump job_1

                "-Work as a maid-" (style="disabled") if game.daytime and not hg_maid.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "-Work as a maid-" (style="disabled") if not game.daytime:
                    "This job is only available during the day."
                    jump working_menu

                #"-Work as a cheerleader for Gryffindor-" if game.daytime and (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                     #jump job_3

                #"-Work as a cheerleader for Gryffindor-" if game.daytime and not (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                    #m "(I'll need an outfit for hermione if I want her to work.)"
                    #jump working_menu

                #"-Work as a cheerleader for Gryffindor-" (style="disabled") if not game.daytime:
                    #"This job is only available during the day."
                    #jump working_menu

                #"-Work as a cheerleader for Slytherin-" if game.daytime and (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    #jump job_4

                #"-Work as a cheerleader for Slytherin-" if game.daytime and not (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    #m "(I'll need a slytherin cheerleader outfit for hermione if I want her to work.)"
                    #jump working_menu

                #"-Work as a cheerleader for Slytherin-" (style="disabled") if not game.daytime:
                    #"This job is only available during the day."
                    #jump working_menu

                "-Hidden-" (style="disabled") if game.daytime and not cardgame_work and not hg_poker.unlocked:
                    "You haven't unlocked this job opportunity yet."
                    jump working_menu

                "-Work by advertising the card game-" if game.daytime and cardgame_work and hg_poker.unlocked:
                    jump job_5
                "-Work by advertising the card game-" (style="disabled") if game.daytime and cardgame_work and not hg_poker.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    m "(Maybe the twins have something fitting for her in their stock.)"
                    jump working_menu

                "-Work by advertising the card game-" (style="disabled") if not game.daytime and cardgame_work:
                    "This job is only available during the day."
                    jump working_menu

                "-Never mind-":
                    jump hermione_talk


        ### Luna ###
        "-Ask for a new student-" (icon="interface/icons/small/luna.webp") if hat_known and not luna_known:
            jump hat_intro_2


        ### Astoria ###
        "-Ask her to help Tonks-" (icon="interface/icons/small/tonks.webp") if astoria_intro.E1_complete and not astoria_intro.E3_complete:
            if astoria_intro.E2_hermione:
                call her_main("I'm still looking for that student, [genie_name]!", "open", "closed", "base", "mid")
                call her_main("Trust in me, I will find that Slytherin scum!", "angry", "base", "angry", "mid")
                jump hermione_talk

            $ hermione_busy = True
            $ astoria_intro.E2_hermione = True
            $ ag_event_pause = 2
            jump astoria_intro_E2_hermione


        ### Cho ###
        "-Solve the matter with Cho-" (icon="interface/icons/small/cho.webp", style="disabled") if cho_intro.E2_complete and not ss_he.cho_E1:
            # Before talking to Snape.
            m "(I should ask Snape what to do about that Cho girl first. Just to be safe.)"
            m "(Might as well have a drink with him...)"
            jump hermione_talk

        "-Solve the matter with Cho-" (icon="interface/icons/small/cho.webp") if ss_he.cho_E1 and not cho_intro.E3_complete:
            # After talking to Snape.
            jump cho_intro_E3

        "-Ask her to commentate the game-" (icon="interface/icons/small/quidditch.webp") if cho_tier == 1 and cho_quid.E3_complete and not cho_quid.E4_complete:
            jump cho_quid_E4

        "-Ask her to commentate the game again-\n{size=-5}again...{/size}" (icon="interface/icons/small/quidditch.webp") if cho_tier == 2 and cho_quid.E6_complete and not cho_quid.E7_complete:
            jump cho_quid_E7

        # General.
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ genie_name = "Sir"
                    jump genie_change
                "-Dumbledore-":
                    $ genie_name = "Dumbledore"
                    jump genie_change
                "-Professor-":
                    $ genie_name = "Professor"
                    jump genie_change
                "-Old man-":
                    $ genie_name = "Old man"
                    jump genie_change
                "-Genie-":
                    if her_whoring >=5:
                        $ genie_name = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if her_whoring >=7:
                        $ genie_name = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if her_whoring >=10:
                        $ genie_name = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if her_whoring >=15:
                        $ genie_name = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if her_whoring >=20:
                        $ genie_name = "Daddy"
                        $ achievement.unlock("daddy")
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if her_whoring >=20:
                        $ genie_name = "Master"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump hermione_talk
                    if her_whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-From now on I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ temp_name = "Miss Granger"
                    jump hermione_change
                "-Girl-":
                    $ temp_name = "Girl"
                    if her_whoring >=1:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Nerd-":
                    $ temp_name = "Nerd"
                    if her_whoring >=3:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Hottie-":
                    $ temp_name = "Hottie"
                    if her_whoring >=5:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Angel-":
                    $ temp_name = "Angel"
                    if her_whoring >=7:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Minx-":
                    $ temp_name = "Minx"
                    if her_whoring >=9:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    $ temp_name = "Princess"
                    if her_whoring >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Pet-":
                    $ temp_name = "Pet"
                    if her_whoring >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Bitch-":
                    $ temp_name = "Bitch"
                    if her_whoring >=13:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slut-":
                    $ temp_name = "Slut"
                    if her_whoring >=15:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Cumslut-":
                    $ temp_name = "Cumslut"
                    if her_whoring >= 17:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Whore-":
                    $ temp_name = "Slytherin Whore"
                    if her_whoring >= 19:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    $ temp_name = "Mudblood"
                    if her_whoring >= 21:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", hermione_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump hermione_talk
                    if her_whoring >=21:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-Give her the ball dress-" if ball_quest.E4_complete and hg_ball.unlocked and not ball_quest.gave_dress:
            jump ball_quest_E5

        "-Start the autumn ball-" if ball_quest.gave_dress and not ball_quest.started:
            jump ball_ending_start

        "-Never mind":
            jump hermione_requests


label genie_change:
    call her_main("Okay, from now on I'll call you [genie_name].", "base", "base", "base", "mid")
    jump hermione_talk

label genie_change_fail:
    call her_main("I'm not calling you that!", "scream", "closed", "angry", "mid")
    jump hermione_talk

label hermione_change:
    if temp_name == "Miss Granger":
        if her_whoring <=0:
            call her_main("Sure, [genie_name].", "base", "base", "base", "mid")
        else:
            call her_main("You don't have to be so formal, [genie_name], you know?", "base", "closed", "base", "mid")
            call her_main("", "base", "base", "base", "mid")
    elif temp_name == "Girl":
        if her_whoring >=1 and her_whoring < 3:
            call her_main("This girl thing again?", "annoyed", "happy", "base", "mid")
            call her_main("*sigh*...", "soft", "happy", "base", "R")
        elif her_whoring >=3:
            call her_main("Fine... I don't mind.", "soft", "base", "base", "R")
    elif temp_name == "Nerd":
        if her_whoring >=3 and her_whoring < 5:
            call her_main("*sigh* I just enjoy books, that's all.", "annoyed", "narrow", "worried", "down")
            m "I'm sure you'll find other things to enjoy soon enough..."
            call her_main("Like what exactly?", "normal", "narrow", "base", "mid_soft")
            m "Nothing to worry about, things will work out..."
            g9 "Nerd..."
            call her_main("*tsk* ...", "soft", "narrow", "base", "R_soft")
            call her_main("", "normal", "narrow", "base", "R_soft")
        elif her_whoring >= 5 and her_whoring < 19:
            call her_main("I can be a bit nerdy sometimes I suppose..", "angry", "happyCl", "base", "mid", emote="sweat")
            call her_main("", "base", "base", "base", "mid")
        elif her_whoring >= 19:
            call her_main("I don't read as much as I used to anymore.", "grin", "narrow", "base", "R_soft", emote="sweat")
            call her_main("", "base", "narrow", "base", "mid_soft")
    elif temp_name == "Hottie":
        if her_whoring >=5 and her_whoring < 7:
            call her_main("[genie_name]?!", "angry", "wide", "angry", "mid", cheeks="blush")
            m "What? That's true, you're hot."
            call her_main("That's inappropriate.", "annoyed", "base", "worried", "R", cheeks="blush")
            her "But I'll let it slide, I guess."
        elif her_whoring >=7 and her_whoring < 19:
            call her_main("Thank you, [genie_name].", "soft", "wink", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")
        elif her_whoring >=19:
            call her_main("... Glad you think so.", "smile", "wink", "base", "mid", cheeks="blush")
            call her_main("","base","happy", cheeks="blush")
    elif temp_name == "Good Girl":
        if her_whoring >=5 and her_whoring < 7:
            call her_main("Well, I do try my best, [genie_name].", "base", "closed", "base", "mid")
            call her_main("", "base", "base", "base", "mid")
        elif her_whoring >=7 and her_whoring < 19:
            call her_main("I'm not sure if I'd qualify, but fine.", "annoyed", "wink", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")
        elif her_whoring >=19:
            call her_main("I could act like a good girl if you really want me to...", "smile", "wink", "base", "mid", cheeks="blush")
            call her_main("","base","happy", cheeks="blush")
    elif temp_name == "Angel":
        if her_whoring >=7 and her_whoring < 9:
            call her_main("What's going on with with these silly nicknames of yours all of a sudden?", "normal", "squint", "angry", "mid")
            m "What do you mean by silly?"
            call her_main("Ugh, forget I said anything...", "open", "narrow", "base", "down",cheeks="blush")
            call her_main("", "normal", "base", "base", "R", cheeks="blush")
        elif her_whoring >=9 and her_whoring < 19:
            call her_main("I like it...", "soft", "narrow", "base", "R_soft",cheeks="blush")
            call her_main("", "base", "narrow", "base", "R_soft",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("I'm surprised I didn't grow wings yet.", "base", "narrow", "worried", "mid_soft",cheeks="blush")
    elif temp_name == "Little Girl":
        if her_whoring >=7 and her_whoring < 9:
            call her_main("What's going on with with these silly nicknames of yours all of a sudden?", "normal", "squint", "angry", "mid")
            m "What do you mean by silly?"
            call her_main("It makes it sound as if I'm your...", "soft", "base", "worried", "R")
            call her_main("Ugh, forget I said anything...", "open", "narrow", "base", "down",cheeks="blush")
            call her_main("", "normal", "base", "base", "R", cheeks="blush")
        elif her_whoring >=9 and her_whoring < 19:
            call her_main("Bit of an odd request but...", "normal", "narrow", "base", "down")
            call her_main("I like it...", "soft", "narrow", "base", "R_soft",cheeks="blush")
            call her_main("", "base", "narrow", "base", "R_soft",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("Yes, [genie_name].", "base", "narrow", "worried", "mid_soft",cheeks="blush")
    elif temp_name == "Bad Girl":
        if her_whoring >=9 and her_whoring < 11:
            call her_main("I guess I am a bit.", "soft", "narrow", "worried", "down")
            call her_main("I did fail that test after all...", "disgust", "narrow", "base", "down")
            call her_main("", "normal", "narrow", "worried", "mid_soft")
            call her_main("", "normal", "base", "base", "mid")
        elif her_whoring >=11 and her_whoring < 17:
            call her_main("I may be a little bit naughty at times.", "base", "happy", "base", "R",cheeks="blush")
        elif her_whoring >=17:
            call her_main("I may be a little bit naughty at times.", "base", "happy", "base", "R",cheeks="blush")
            call her_main("", "base", "base", "base", "mid", cheeks="blush")
    elif temp_name == "Minx":
        if her_whoring >=9 and her_whoring < 11:
            call her_main("I guess I am a bit.", "soft", "narrow", "worried", "down")
            call her_main("", "normal", "narrow", "worried", "mid_soft")
        elif her_whoring >=11 and her_whoring < 17:
            call her_main("I may be a little bit naughty at times.", "base", "happy", "base", "R",cheeks="blush")
        elif her_whoring >=17:
            call her_main("I may be a little bit naughty at times.", "base", "happy", "base", "R",cheeks="blush")
            call her_main("", "base", "base", "base", "mid", cheeks="blush")
    elif temp_name == "Princess":
        if her_whoring >= 11 and her_whoring < 13:
            call her_main("That would make you my prince wouldn't it?", "open", "base", "base", "R",cheeks="blush")
            call her_main("", "base", "base", "base", "mid", cheeks="blush")
        elif her_whoring >= 13:
            call her_main("Yes... My prince.","smile","happy")
            m "..."
            call her_main("I-I mean, [genie_name].", "smile", "happyCl", "base", "mid", emote="sweat")
            call her_main("", "base", "base", "base", "mid")
    elif temp_name == "Pet":
        if her_whoring >= 11 and her_whoring < 13:
            call her_main("You want to call me....{w=0.5} a pet?", "normal", "squint", "angry", "mid")
            m "Yes."
            call her_main(".... {w=0.5}.... {w=0.5}.... {w=0.5}....", "normal", "happy", "base", "mid")
            call her_main("", "normal", "squint", "base", "mid")
            m ".... {w=0.5}.... {w=0.5}...."
            call her_main("May I at least know why?", "open", "squint", "base", "mid")
            m "No."
            call her_main("....", "annoyed", "base", "worried", "mid")
        elif her_whoring >= 13:
            call her_main("*Meow*","smile","happyCl")
            call her_main("","smile","happy")
            m "Don't do that..."
            call her_main("Such a party pooper.","annoyed","happyCl")
            call her_main("", "base", "base", "base", "mid")
    elif temp_name == "Bitch":
        if her_whoring >=13 and her_whoring < 15:
            call her_main("Isn't this a bit inappropriate [genie_name]?", "mad", "narrow", "worried", "down")
            m "And doing favours for house points isn't?"
            call her_main("Fine...", "base", "narrow", "base", "down", cheeks="blush")
        elif her_whoring >= 15 and her_whoring < 17:
            call her_main("...", "normal", "narrow", "worried", "down", cheeks="blush")
            m "Any objections?"
            call her_main("...", "soft", "base", "worried", "R",cheeks="blush")
            g9 "Okay then..."
        elif her_whoring >= 17:
            call her_main("Alright.", "base", "happyCl", "base", "mid",cheeks="blush")
            call her_main("","base","happy",cheeks="blush")
    elif temp_name == "Slut":
        if her_whoring >=15 and her_whoring < 17:
            call her_main("[genie_name]?!", "shock", "wide", "worried", "stare")
            call her_main("You can't just call someone that!", "mad", "wide", "base", "stare")
            m "It'll just be between us..."
            call her_main("...", "disgust", "squint", "base", "mid")
            m "Nothing to add?"
            call her_main("", "clench", "closed", "base", "mid", emote="angry")
            m "So you'll let me call you that or not?"
            call her_main("{size=+5}FINE!{/size}", "clench", "closed", "angry", "mid", emote="angry")
            m "..."
            call her_main("", "normal", "narrow", "angry", "R")
        elif her_whoring >= 17:
            call her_main("I guess if you have to call me that sure...", "base", "narrow", "base", "down",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("I don't mind...", "smile", "happyCl", "base", "mid",cheeks="blush")
    elif temp_name == "Cumslut":
        if her_whoring >= 17 and her_whoring < 19:
            call her_main("A cumslut?!", "open", "wide", "worried", "stare")
            m "Something wrong?"
            call her_main("You have to even ask?", "soft", "narrow", "worried", "down", cheeks="blush")
            call her_main("This is so degrading...", "normal", "narrow", "base", "down",cheeks="blush")
            call her_main("\"But I kinda am a slut begging for cum aren't I...\"", "base", "happyCl", "base", "mid",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("...", "soft", "narrow", "base", "up")
            call her_main("\"When did I start enjoying it so much...\"", "open", "narrow", "base", "up",cheeks="blush")
            call her_main("\"That taste, the texture..\"", "open", "narrow", "annoyed", "up",cheeks="blush")
            call her_main("\"..So warm, sticky and...\"", "silly", "narrow", "base", "up",cheeks="blush")
            m "Are you okay there, [temp_name]?"
            call her_main("Wha--", "mad", "wide", "base", "stare")
            call her_main("Of course I am!", "smile", "base", "base", "R",cheeks="blush")
    elif temp_name == "Slytherin Whore":
        if her_whoring >=19 and her_whoring < 21:
            call her_main("Do you really have to call me that, [genie_name]?", "disgust", "base", "worried", "mid")
            call her_main("Referring to me as a bitch or a slut for your own amusement is one thing...", "mad", "narrow", "worried", "down",cheeks="blush")
            call her_main("You're aware of how much I loathe Slytherin.", "open", "narrow", "worried", "mid_soft")
            call her_main("And I'm definitely not a whore...", "soft", "closed", "base", "mid")
            her "I refuse!"
            menu:
                "-Say it's fine-":
                    m "Fine, I won't call you that..."
                    call her_main("You won't?", "open", "base", "base", "mid")
                    call her_main("", "soft", "base", "base", "mid")
                    m "Of course..."
                    call her_main("I am glad we're on the same page on this one, [genie_name].", "open", "closed", "base", "mid")
                    call her_main("", "base", "closed", "base", "mid")
                    m "In fact, from this point forward you don't have to call me [genie_name] or exchange any favours..."
                    call her_main("", "soft", "base", "base", "mid", emote="confused")
                    m "Let's just void this whole... deal of yours shall we."
                    call her_main("B-but, [genie_name]?!", "mad", "wide", "base", "mid", emote="shocked")
                    call her_main("", "mad", "wide", "base", "mid")
                    m "I must apologise {b}Miss Granger{/b}, I thought we had come to some kind of agreeable arrangement by now..."
                    call her_main("But I--", "mad", "wide", "worried", "stare")
                    m "I should have known better to believe that this sort of thing would work out..."
                    call her_main("Maybe I coul--","clench","happyCl")
                    m "I thought we both had what we wanted..."
                    call her_main("Liste--", "soft", "narrow", "worried", "down")
                    call her_main("", "normal", "closed", "angry", "mid")
                    m "Might as well hand in my resignation with the ministry and--"
                    with hpunch
                    call her_main("{size=+10}I AM A SLYTHERIN WHORE!!!{/size}", "scream", "closed", "angry", "mid",cheeks="blush")
                    call her_main("", "normal", "closed", "base", "mid")
                    m "..."
                    call her_main("Now please, [genie_name]... Let's just forget this conversation ever happened.", "disgust", "base", "worried", "mid")
                    m "Are you sure that's what you want, [temp_name]?"
                    call her_main("... Yes.", "disgust", "narrow", "worried", "down", emote="sweat")
                    m "\"This girl really is beyond redemption...\""
                    call her_main("", "base", "narrow", "worried", "down")
                "-Threaten her-":
                    g4 "Either accept my offer or Gryffindor lose five hundred points..."
                    with hpunch
                    call her_main("FIVE HUNDRED?!", "shock", "wide", "base", "stare")
                    call her_main("[genie_name]... This is blackmailing!", "scream", "closed", "angry", "mid")
                    call her_main("", "mad", "closed", "angry", "mid")
                    m "It is?"
                    call her_main("What else would it be?", "mad", "base", "angry", "mid",cheeks="blush")
                    g9 "Negotiations..."
                    call her_main("You...", "clench", "closed", "angry", "mid",cheeks="blush")
                    m "That's not an answer..."
                    call her_main("{size=-10}Okay..{/size}", "soft", "narrow", "angry", "R",cheeks="blush")
                    m "What was that? I didn't hear you."
                    call her_main("I said yes, you can call me a Slytherin whore... or whatever.", "normal", "narrow", "annoyed", "mid", cheeks="blush")
                    call her_main("Happy now?!", "open", "closed", "angry", "mid", cheeks="blush")
                    g9 "Very."
                    call her_main("{size=-6}You are the worst.{/size}", "normal", "narrow", "base", "R_soft", cheeks="blush")
                    $ her_mood += 15
        elif her_whoring >= 21:
            call her_main("Please, [genie_name], couldn't you call me something else instead?", "open", "base", "worried", "mid")
            m "But where's fun in that?"
            call her_main("Why do I even bother... *sigh*", "soft", "narrow", "base", "R_soft",cheeks="blush")
    elif temp_name == "Mudblood":
        if her_whoring >= 21:
            call her_main("A{w=0.5}...{w=0.5} {size=+6}{b}{cps=20}mud{w=0.5}blood{/cps}{/b}?!{/size}", "shock", "wide", "base", "stare")
            call her_main("Did I hear you right, [genie_name]?!", "normal", "wide", "base", "mid")
            menu:
                "-Confirm-":
                    pass
                "-!!!{b}ABORT ABORT ABORT{/b}!!!-":
                    g4 "What? Of course not!"
                    m "I said.."
                    g4 "(I have to think fast)"
                    menu:
                        "-Mass flood-":
                            g4 "I said mass flood!"
                            call her_main("Mass flood?", "soft", "base", "base", "mid")
                            m "Are you deaf or something?"
                            if game.weather == "rain":
                                call her_main("I was pretty sure you said--", "open", "base", "base", "mid")
                                call her_main("", "normal", "base", "base", "R")
                                m "Look outside the window, it's raining is it not?"
                                call her_main("I{w=0.5}...{w=0.5} Yes, you are right [genie_name].", "normal", "closed", "base", "mid")
                                m "Of course I am."
                                call her_main("So what did you want to talk about?", "base", "base", "base", "mid")
                            else:
                                call her_main("[genie_name], but it's not raining..", "normal", "closed", "base", "mid")
                                call her_main("", "disgust", "narrow", "base", "down", cheeks="blush")
                                g9 "Last time I had my dick in you it felt like a mass flood."
                                call her_main("[genie_name]...", "disgust", "closed", "base", "mid", cheeks="blush")
                                g9 "What? It's true, I swear!"
                                call her_main("...", "soft", "narrow", "worried", "down", cheeks="blush")
                        "-Mad stud-":
                            g4 "I said mad stud!"
                            call her_main("Mad stud?", "soft", "base", "base", "mid")
                            g9 "My dick, your ass, bud."
                            call her_main("really...", "disgust", "narrow", "base", "mid_soft", cheeks="blush")
                            call her_main("You can be so childish sometimes, [genie_name]...", "annoyed", "narrow", "base", "R_soft", cheeks="blush")
                        #"-Leaf bud-":
                        #    jump hermione_talk
                    jump hermione_talk
            call her_main("Why would you even suggest calling me such a thing..", "scream", "squint", "angry", "mid")
            call her_main("It's like the most offensive thing you could call someone like...", "shock", "squint", "angry", "mid", tears="soft")
            call her_main("like...", "open", "happyCl", "worried", "mid", tears="soft_blink")
            call her_main("Someone like...", "open", "narrow", "worried", "down", tears="mascara_crying")
            call her_main("me...", "disgust", "narrow", "worried", "down", tears="mascara_soft")
            call her_main("", "disgust", "happyCl", "worried", "mid", tears="mascara")
            menu:
                "-Try to calm her down-":
                    call her_main("", "disgust", "narrow", "worried", "mid_soft", tears="mascara")
                    m "Now, now, there's no need to cry."
                    m "Do you know why I call you these things miss Granger?"
                    call her_main("... no?", "disgust", "narrow", "worried", "mid_soft", tears="mascara")
                    m "It's so that you'll come to know that words are just words and they only hurt if you let them."
                    call her_main("...", "normal", "narrow", "worried", "mid_soft", tears="mascara")
                    m "Once you truly understand that nothing will hold you back."
                    g9 "And you'll be at your utmost potential."
                    call her_main("You really think so?", "open", "narrow", "worried", "mid_soft", tears="mascara")
                    call her_main("", "normal", "narrow", "worried", "mid_soft", tears="mascara")
                    m "Yes, in fact I do."
                    call her_main("Thank you, [genie_name].", "normal", "closed", "base", "mid", tears="mascara")
                    call her_main("I can do it, I know I can.", "base", "narrow", "worried", "mid_soft", tears="mascara")
                    $ her_mood = 0
                "-Tell her she deserves it-":
                    g4 "You deserve to be called a slut, a whore and a mudblood... just look at you."
                    call her_main("...", "scream", "happyCl", "worried", "mid", tears="mascara_soft_blink")
                    call her_main("", "disgust", "happyCl", "worried", "mid", tears="mascara_soft")
                    g4 "You walk into my office and sell your body for the sole reason that it will make Gryffindor happy to win the house cup."
                    call her_main("...", "open", "happyCl", "worried", "mid", tears="mascara_soft_blink")
                    call her_main("", "disgust", "happyCl", "worried", "mid", tears="mascara_soft")
                    g4 "Bending over onto my desk and let yourself be taken like a some common harlot..."
                    call her_main("I...", "disgust", "narrow", "worried", "mid_soft", tears="mascara_soft")
                    g4 "Letting your headmaster thrust himself upon you and taking my load like your life depended on it..."
                    call her_main("...", "normal", "happyCl", "worried", "mid", tears="mascara_soft")
                    call her_main("", "normal", "narrow", "worried", "mid_soft", tears="mascara")
                    m "I bet you don't even care about the points anymore..."
                    call her_main("Well...", "normal", "narrow", "worried", "down", tears="mascara")
                    call her_main("", "normal", "narrow", "annoyed", "up", tears="mascara")
                    m "You are nothing more than a whore..."
                    call her_main("", "base", "narrow", "annoyed", "up", tears="mascara")
                    g9 "{size=+4}{b}MY{/b}{/size} whore!"
                    call her_main("", "base", "narrow", "base", "up", tears="mascara")
                    m "And I {b}will{/b} call you however I want!"
                    call her_main("Yes, [genie_name], I understand.", "silly", "narrow", "base", "up", tears="mascara")
                    call her_main("I am your toy{w=0.6}, your fuckslut{w=0.6}, your cocksleeve, your--", "grin", "narrow", "base", "dead", tears="mascara")
                    m "Yes, that you are but it's enough..."
                    call her_main("I fully belong to you... [genie_name].", "silly", "narrow", "base", "dead", tears="mascara")
                    call her_main("", "grin", "narrow", "base", "dead", tears="mascara")
                    $ her_mood = 0
    $ hermione_name = temp_name
    jump hermione_talk

label hermione_change_fail:
    if temp_name == "Girl":
        call her_main("I would prefer if we kept using our formal names and titles, [genie_name].", "open", "closed", "base", "mid")
        call her_main("", "normal", "base", "base", "mid")
    elif temp_name == "Nerd":
        call her_main("I would prefer if you didn't, [genie_name].", "open", "closed", "angry", "mid")
        call her_main("{size=-4}And I'm not a nerd...{/size}", "annoyed", "base", "worried", "mid")
        if her_whoring >= 1:
            call her_main("\"I think...\"", "annoyed", "base", "worried", "R")
    elif temp_name == "Good Girl":
        call her_main("I'm not letting you call me that, [genie_name]!", "open", "closed", "angry", "mid")
        if her_whoring >= 3:
            call her_main("\"Although it's kinda cute he said that...\"", "base", "base", "base", "R")
    elif temp_name == "Little Girl":
        call her_main("I won't let you call me that, [genie_name]!", "open", "closed", "angry", "mid")
        if her_whoring >= 5:
            call her_main("\"I hope they'd grow out more...\"", "disgust", "narrow", "worried", "down")
            call her_main("*sigh*", "annoyed", "closed", "base", "mid")
            call her_main("", "normal", "base", "base", "R")
    elif temp_name == "Bad Girl":
        call her_main("I am not a [temp_name]!", "open", "base", "angry", "mid")
        if her_whoring >= 7:
            call her_main("\"Or am I...?\"", "disgust", "base", "base", "R")
            call her_main("", "normal", "base", "base", "R")
    elif temp_name == "Princess":
        call her_main("This is inappropriate, [genie_name]!", "open", "base", "angry", "mid")
        if her_whoring >= 9:
            call her_main("\"It sounds nice though...\"", "base", "base", "base", "R")
    elif temp_name == "Pet":
        call her_main("Are you joking, [genie_name]?", "open", "base", "worried", "mid")
        if her_whoring >= 11:
            call her_main("\"Why would he even suggest that?\"", "annoyed", "base", "base", "R")
    else:
        call her_main("I won't let you call me that!", "shock", "closed", "angry", "mid")
        call her_main("", "normal", "base", "angry", "mid")
    jump hermione_talk
