
### Quests ###

# Add any event triggers to this list.
# Only one event can play for each day/night (this might change.)
# Add date specific events at the start of the list (create the date if it's not there.)

label quests:

    #
    # DAY-BASED EVENTS
    #

    if day >= 1:
        if daytime:
            if not genie_intro.E1_complete:
                jump genie_intro_E1
        else:
            if ss_event_pause == 0 and not snape_intro.E1_complete:
                # Snape visits for the first time.
                jump snape_intro_E1

    if day >= 2:
        if not letter_hg_2.read:
            $ letter_hg_2.send_letter()
        if daytime:
            if not genie_intro.E3_complete:
                jump genie_intro_E3
        else:
            if ss_event_pause == 0 and not snape_intro.E2_complete:
                # Snape's second visit.
                jump snape_intro_E2

    if day >= 3:
        if daytime:
            pass
        else:
            if ss_event_pause == 0 and not snape_intro.E3_complete:
                # Day of the duel.
                jump snape_intro_E3

    if day >= 4:
        if not letter_min_work.read:
            $ letter_min_work.send_letter()
        if daytime:
            pass
        else:
            if ss_event_pause == 0 and not snape_intro.E5_complete:
                # You bother decide to just "roll with it"... Snape summon unlocked.
                jump snape_intro_E5

    if day >= 5:
        if daytime:
            if hg_event_pause == 0 and not hermione_intro.E1_complete:
                # Hermione shows up for the first time.
                jump hermione_intro_E1

    if day >= 6:
        if daytime:
            if hg_event_pause == 0 and ss_he.hermione_E1 and not hermione_intro.E2_complete:
                # Second visit from Hermione. Says she sent a letter to the Ministry.
                jump hermione_intro_E2

    if day >= 7:
        if hermione_intro.E2_complete and not letter_min_favors.read:
            $ letter_min_favors.send_letter()
        if daytime:
            pass
        else:
            if hg_event_pause == 0 and ss_he.hermione_E2 and not hermione_intro.E3_complete:
                # Takes place after first special event with Snape, where he just complains about Hermione.
                # Hermione might have failed a test...
                jump hermione_intro_E3

    if day >= 8:
        if daytime:
            pass
        else:
            if hg_event_pause == 0 and hermione_intro.E3_complete and not hermione_intro.E4_complete:
                # She failed a test and cries.
                jump hermione_intro_E4

    if day >= 9:
        if daytime:
            if hg_event_pause == 0 and hermione_intro.E4_complete and not hermione_intro.E5_complete:
                # Hermione asks to be tutored. Summon unlocked!
                jump hermione_intro_E5

    if day >= 10:
        if daytime:
            if nt_event_pause == 0 and hermione_intro.E5_complete and not tonks_intro.E1_complete:
                # Tonks visits for the first time.
                jump tonks_intro_E1
        else:
            if tonks_intro.E1_complete and not tonks_intro.E2_complete:
                # Tonks has found no evidence so far.
                jump tonks_intro_E2

    if day >= 11:
        if daytime:
            pass
        else:
            if nt_event_pause == 0 and ss_he.tonks_E1 and not tonks_intro.E3_complete:
                # Tonks becomes a teacher. Summon unlocked!
                jump tonks_intro_E3

    if day >= 13:
        if daytime:
            if hg_event_pause == 0 and hermione_intro.E5_complete and ss_he.tonks_E1 and nt_he.hermione_E1 and not hermione_intro.E6_complete:
                # Hermione wants to buy favours. Favours unlocked!
                jump hermione_intro_E6

    if day >= 16:
        if daytime:
            if her_tier >= 2 and not cho_intro.E1_complete:
                jump cho_intro_E1

    if day >= 24:
        if not persistent.xmas_2020 and not daytime and time.time() < 1609459200:
            # Valid until 00:00 1st January 2021 , then available from within mirror only.
            jump santas_little_helper

    if day >= 25:
        if not deck_unlocked:
            $ letter_deck.send_letter()

    #
    # CARDGAME - EVENTS
    #

    if day >= twins_cards_delay:
        if deck_unlocked and twins_first_win and not twins_cards_stocked:
            $ letter_cards_store.send_letter()

    if geniecard_level < 2 and snape_third_win and her_third_win and twins_second_win:
        $ letter_cardgame_t2.send_letter()

    #
    # CHO CHANG - EVENTS
    #

    if cc_event_pause == 0:
        if daytime:

            if hufflepuff_match == "start":
                $ hufflepuff_match = "return" # Triggers the return during the evening.
                jump hufflepuff_match
            elif slytherin_match == "start":
                $ slytherin_match = "return"
                jump slytherin_match
            #elif gryffindor_match == "start":
                #$ gryffindor_match = "return"
                #jump gryffindor_match


            if cho_tier == 1:
                # Lee Jordan gets knocked out cold
                if cho_quid.hufflepuff_training and not cho_quid.E3_complete:
                    jump cho_quid_E3

            elif cho_tier == 2:
                # Hermione refuses to commentate for Slytherin match.
                if cho_quid.slytherin_failed and not cho_quid.E6_complete:
                    jump cho_quid_E6
        else:
            # Introduction
            if cho_intro.E1_complete and not cho_intro.E2_complete:
                jump cho_intro_E2

            # Quidditch training matches
            if cho_quid.in_progress:
                $ cho_quid.in_progress = False

                if cho_tier == 1:
                    # Hufflepuff
                    jump cc_ht_return
                elif cho_tier == 2:
                    # Slytherin
                    jump cc_st_return
                #elif cho_tier == 3:
                    # Gryffindor
                    #jump cc_gt_return

            # Note: The return events now get jumped to right after the main match events.
            #if hufflepuff_match == "return" and not cho_quid.hufflepuff_complete:
            #    $ hufflepuff_match = "completed"
            #    jump hufflepuff_match_return
            #elif slytherin_match == "return" and not cho_quid.slytherin_complete:
            #    $ slytherin_match = "completed"
            #    jump slytherin_match_return
            #elif gryffindor_match == "return" and not cho_quid.gryffindor_complete:
            #    #$ gryffindor_match = "completed"
            #    #jump gryffindor_match_return

    #
    # SUSAN BONES - EVENTS
    #

    if sb_event_pause == 0:
        if daytime:
            # Introduction
            if nt_he.susan_E1 and not susan_intro.E1_complete:
                jump susan_intro_E1

    #
    # ASTORIA GREENGRASS - EVENTS
    #

    # Astoria events not triggered by a date.
    if ag_event_pause == 0:
        if daytime:
            # Introduction
            if astoria_intro.E2_hermione and astoria_intro.E2_snape and not astoria_intro.E3_complete:
                jump astoria_intro_E3
            if nt_he.astoria_E1 and not astoria_intro.E4_complete:
                jump astoria_intro_E4
        else:
            # Introduction
            if susan_intro.E1_complete and not astoria_intro.E1_complete:
                jump astoria_intro_E1

    #
    # SEVERUS SNAPE - EVENTS
    #

    if ss_event_pause == 0:
        if daytime:
            # Ending events
            if her_whoring >= 15 and ball_quest.E1_complete and not ball_quest.E2_complete:
                # Snape complains that appointing Hermione in the Autumn Ball committee was a mistake.
                jump ball_quest_E2

        else:
            # Ending events
            if ball_quest.started and not ball_quest.completed:
                jump ball_ending_E1

    #
    # NYMPHADORA TONKS - EVENTS
    #

    # Tonks events not triggered by a date.
    if nt_event_pause == 0:
        if daytime:
            python:
                for i in tonks_mail_list:
                    if i == "poster_1_gift":
                        letter_nt_1.send_letter()
                    if i == "poster_1_store":
                        poster_tonks_ITEM.hidden = False # Now available at the store.
                    tonks_mail_list.remove(i)
        else:
            pass

    #
    # HERMIONE GRANGER - EVENTS
    #

    if hg_event_pause == 0:
        if daytime:
            # Ending events
            if her_whoring >= 15 and not ball_quest.E1_complete:
                # Hermione wants to be in the Autumn Ball committee.
                jump ball_quest_E1

            if her_whoring >= 18 and ball_quest.E2_complete and not ball_quest.E3_complete:
                # Hermione cries about having no proper dress for the Ball.
                jump ball_quest_E3

            if her_whoring >= 18 and ball_quest.E3_complete and not ball_quest.E4_complete:
                # Hermione apologizes for the day (event) before.
                jump ball_quest_E4

            if collar == 5:
                $ hg_event_pause += 2
                jump collar_scene

    #
    # LUNA LOVEGOOD - EVENTS
    #

    if ll_event_pause == 0:
        if daytime:

            # Intro
            if her_whoring >= 21 and not hat_known:
                jump hat_intro

            if luna_reverted and luna_reverted_intro:
                jump luna_reverted_greeting_1

            # Unlock reverted favours.
            if luna_reverted:

                # Masturbate
                if lun_whoring >= 0 and ll_pf_masturbate not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_masturbate)
                    $ lun_tier = 2
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(2, 3)

                    $ ll_pf_masturbate.start()

                # Blowjob
                if lun_whoring >= 3 and ll_pf_blowjob not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_blowjob)
                    $ lun_tier = 3
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(4, 6)

                    $ ll_pf_blowjob.start()

        else:
            if luna_known and not luna_unlocked:
                jump hat_intro_3

            # Unlock reverted favours.
            if luna_reverted:

                # Sex
                if lun_whoring >= 9 and ll_pf_sex not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_sex)
                    $ lun_tier = 4
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(2, 4)

                    $ ll_pf_sex.start()

    # All quest events should somehow end with a jump to the main room day/night cycle
    # If no quest event is triggered, resume normally from the main room
    jump main_room


### Quests flags ###

# Genie
default genie_intro = quest_class(
    E1_complete = False,
    E2_complete = False,
    E3_complete = False,
)

# Snape
default snape_intro = quest_class(
    E1_complete   = False, # 1st visit
    E2_complete   = False, # 2nd visit
    E3_complete   = False, # 3rd visit, before the duel.
    duel_complete = False, # Duel
    E4_complete   = False, # After the duel.
    E5_complete   = False, # 4th visit, summon unlocked.
)

# Hermione
default hermione_intro = quest_class(
    E1_complete = False, # 1st visit
    E2_complete = False, # 2nd visit, MRM + informed the Ministry.
    E3_complete = False, # 3rd visit, did she fail a test?
    E4_complete = False, # 4th visit, she's crying. Failed a test.
    E5_complete = False, # 5th visit, asks to be tutored, summon unlocked.
    E6_complete = False, # 6th visit, asks to buy favours, favours unlocked.
)

# Tonks
default tonks_intro = quest_class(
    E1_complete = False, # 1st visit
    E2_complete = False, # 2nd visit
    E3_complete = False, # 3rd visit, summon unlocked.
)

# Cho
default cho_intro = quest_class(
    E1_complete = False, # 1st visit
    E2_complete = False, # 2nd visit
    E3_intro    = False, # You talked to Hermione once, but event failed.
    E3_complete = False, # 3rd visit, summon unlocked.
)

default cho_quid = quest_class(
    E1_complete = False, # Hufflepuff - Intro 1
    E2_complete = False, # Hufflepuff - Intro 2
    E3_complete = False, # Lee Jordan gets hit by a bludger
    E4_complete = False, # Genie asks Hermione to commentate
    E5_complete = False, # Slytherin - Intro 1
    E6_complete = False, # Hermione refuses to commentate.
    E7_complete = False, # Blackmail Hermione.
    E8_complete = False, # Ask Tonks for help (Hangout)
    E9_complete = False, # Ask Snape for help (Hangout)(Optional)

    hufflepuff_prepared = False, # Ready for practice match? (Requirements: tactic)
    hufflepuff_training = False, # Finished Hufflepuff practice match?
    hufflepuff_complete = False, # Finished Hufflepuff event chain?

    slytherin_failed = False, # Has failed first training match?
    slytherin_prepared = False, # Ready for practice match? (Requirements: tactic, blackmail Hermione, Tonks' help)
    slytherin_training = False, # Finished Slytherin practice match?
    slytherin_complete = False, # Finished Slytherin event chain?

    position = "", # Valid choices: "front", "above", "close"

    lock_training = False,
    lock_practice = True,
    lock_tactic = False,
    in_progress = False,
)

default cho_quiz = quest_class(
    E1_complete = False,
    E2_complete = False,

    correct_answers = 0,
    checkpoint = False,
    lost = False,
    complete = False,

    hint = "" # Set after reading Quidditch Book
)

# Susan
default susan_intro = quest_class(
    E1_complete = False, # Susan visits.
)

# Astoria
default astoria_intro = quest_class(
    E1_complete = False, # Tonks visits.
    E2_hermione = False, # Tell Hermione to look for her.
    E2_snape    = False, # Tell Snape to look for her.
    E3_complete = False, # Hermione finds her.
    E4_complete = False, # Unlock Astoria.
)

# Ball Quest
default ball_quest = quest_class(
    E1_complete = False,
    E2_complete = False,
    E3_complete = False,
    E4_complete = False,
    gave_dress  = False,
    started     = False,
    completed   = False,
)


### Hangout Events ###

# Snape
default ss_he = quest_class(
    hermione_E1 = False, # I hate her!
    hermione_E2 = False, # Let's ruin her!
    tonks_E1    = False, # Discuss Tonks with Snape.
    tonks_E2    = False, # Inform him that Tonks has joined you both.
    tonks_E3    = False, # Tonks is teaching DAtDA. Snape might use Veritaserum on her...
    cho_E1      = False, # You tell Snape that you have met Cho.
    cho_E2      = False, # Get some help with Quidditch.

    hermione_strip = False, # You invite Snape to watch Hermione strip.
)

# Tonks
default nt_he = quest_class(
    hermione_E1 = False, # Help with/unlock Hermione's favours.
    susan_E1    = False, # Tonks is worried about Susan.
    astoria_E1  = False, # Tonks suggests to teach Astoria the Imperius curse.

    favors_E1   = False, # Unlock Public Requests.
    favors_E2   = False, # Advance to Tier 2.
)
