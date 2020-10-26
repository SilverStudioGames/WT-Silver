
label summon_tonks:

    $ active_girl = "tonks"
    $ last_character = "tonks"

    $ tonks_busy = True

    call update_ton_tier
    call update_tonks

    call play_music("tonks")
    call play_sound("door")

    # Clothes Events
    call tonks_summon_setup

    label tonks_requests:

    # Reset
    call reset_menu_position
    call ton_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not chitchated_with_tonks:
                call tonks_chit_chat
                jump tonks_talk
            else:
                jump tonks_talk


        # Favours
        "-Sexual favours-" (icon="interface/icons/small/condom.webp"):
            jump tonks_favor_menu

        # Fireplace Chats
        "-Let's hang-" (icon="interface/icons/small/toast.webp") if (wine_ITEM.owned > 0 and nt_he_drink.counter == 0) or (firewhisky_ITEM.owned > 0 and nt_he_drink.counter > 0):
            jump tonks_hangout

        "-Let's hang-" (icon="interface/icons/small/toast.webp", style="disabled") if (firewhisky_ITEM.owned < 1 and nt_he_drink.counter > 0):
            m "(I don't have any firewhisky...)"
            jump tonks_requests

        "-Let's hang-" (icon="interface/icons/small/toast.webp", style="disabled") if (wine_ITEM.owned < 1 and nt_he_drink.counter == 0):
            m "(I don't have any wine...)"
            jump tonks_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if tonks_wardrobe_unlocked:
            hide screen tonks_main with d1
            $ gui.in_context("wardrobe")
            with d2

            # Hair fix
            $ tonks_haircolor = tonks.get_equipped("hair").color
            jump tonks_requests

        "-Hidden-" (style="disabled") if not tonks_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump tonks_requests


        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_tonks_gift:
            call gift_menu
            jump tonks_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp", style="disabled") if gave_tonks_gift:
            m "I already gave her a gift today."
            jump tonks_requests

        # Dismiss
        "-Never mind-":
            stop music fadeout 3.0

            if game.daytime:
                ton "Alright, back to work then..."
            else:
                ton "Sweet dreams, [ton_genie_name]."

            call play_sound("door")

            jump end_tonks_event


# Tonks level up
label update_ton_tier:
    if ton_tier == 1 and nt_he.favors_E2:
        $ ton_level_up = 1

    return

label tonks_level_up(tier=None):

    call bld
    if tier == 1:
        g9 "(Time to teach those students something useful!)"

    $ ton_tier = tier+1
    $ ton_level_up = None

    pause.5
    call nar(">Tonks has reached level "+str(ton_tier)+"!")

    call update_ton_tier

    return


# Tonks Requests Menu
label tonks_favor_menu:
    # call update_tonks_favors

    menu:
        "-Level Up-" (icon="interface/icons/small/levelup.webp") if ton_level_up != None:
            call tonks_level_up(tier=ton_level_up)
            jump tonks_requests

        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp", style="disabled"):
            call not_available
            jump tonks_favor_menu
            #
            # Uncomment once favours are ready
            #

            # label .personal:
            # python:
                # menu_choices = []
                # for i in nt_favor_list:
                    # if i in []: # Not in the game yet.
                        # menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                    # elif i.start_tier > ton_tier:
                        # menu_choices.append(gui.menu_item("-Not ready-", "vague", style="disabled"))
                    # else:
                        # menu_choices.append(i.get_menu_item())

                # menu_choices.append(("-Never mind-", "nvm"))
                # result = renpy.display_menu(menu_choices)
            # if result == "nvm":
                # jump tonks_favor_menu
            # elif result == "vague":
                # call favor_not_ready
                # jump .personal
            # elif result == "na":
                # call not_available
                # jump .personal
            # else:
                # $ renpy.jump(result)

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime and tonks_requests_unlocked:
            jump tonks_requests_menu

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime or not tonks_requests_unlocked:
            if not tonks_requests_unlocked:
                call nar(">You haven't unlocked this feature yet.")
            elif not game.daytime:
                call nar(">Public requests are available during the day only.")
            jump tonks_favor_menu

        "-Never mind-":
            jump tonks_requests

label tonks_requests_menu:
    call update_ton_requests
    python:
        menu_choices = []
        for i in nt_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
            elif i.start_tier > ton_tier:
                menu_choices.append(gui.menu_item("-Not ready-", "vague", style="disabled"))
            else:
                menu_choices.append(i.get_menu_item())
        menu_choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(menu_choices)

    if result == "nvm":
        jump tonks_favor_menu
    elif result == "vague":
        call favor_not_ready
        jump tonks_requests_menu
    elif result == "na":
        call not_available
        jump tonks_requests_menu
    else:
        $ renpy.jump(result)

label update_ton_requests:
    # Set event tier to current Tonks tier if they are different
    python:
        for i in nt_requests_list:
            i.tier = ton_tier

    return

label tonks_talk:
    menu:
        # TODO: Finish up
        #"-Ask about outfit upgrades-" (icon="interface/icons/small/wardrobe.webp"):
            #call clothing_upgrades
            #jump tonks_requests

        "-Ask for help with Quidditch-" (icon="interface/icons/small/quidditch.webp") if cho_tier == 2 and cho_quid.E6_complete and not cho_quid.E8_complete:
            m "Got a moment?"
            call ton_main("Sure, just make it quick...","open","base","base","mid")
            m "I have a problem with--"
            call ton_main("[ton_genie_name], aren't you forgetting about something?","open","closed","base","mid")
            call ton_main("You should offer a lady a drink, before burdening her with your problems...","base","base","base","mid")
            m "(Is there {b}any{/b} teacher in this school that has no problems with alcohol...?)"

            if firewhisky_ITEM.owned >= 1:
                m "I got drinks."
                call ton_main("What are we waiting for then?","horny","base","base","mid")

                jump tonks_hangout
            else:
                m "I'm out of firewhisky."
                call ton_main("That's a shame, I guess our talk will have to wait.","open","base","base","R")
                call ton_main("", "base","base","base","R")

                jump tonks_talk

        "-Get naked!-" if tonks_strip_happened and (not tonks.is_worn("top") or not tonks.is_worn("bottom") or not tonks.is_worn("robe")):
            m "Get naked, [tonks_name]!"
            call ton_main("Of course, [ton_genie_name].","horny","base","base","ahegao")
            hide screen tonks_main
            with d3

            $ tonks.strip("all")
            pause.8

            call ton_main("Do you like it, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("The exposed body of one of your subordinates?","open_wide_tongue","base","raised","ahegao")
            g4 "I do, [tonks_name]!"
            g9 "You should teach like that!"
            call ton_main("*Hmm*...","base","base","base","R")
            call ton_main("I like the way you think, [ton_genie_name]!","horny","base","base","mid")
            jump tonks_requests

        "-Get dressed-" if tonks_strip_happened and not tonks.is_any_worn("top", "bottom", "robe"):
            m "Put on some clothes, would you..."
            m "This is a school, after all."
            call ton_main("Of course, [ton_genie_name].","base","base","base","mid")
            hide screen tonks_main
            with d3

            $ tonks.wear("all")
            pause.8

            call ton_main("...","base","base","base","mid")
            jump tonks_requests

        "-Address me only as-":
            menu:
                "-Sir-":
                    label .sir: # Local label unavailable from global scope
                    $ ton_genie_name = "Sir"
                    call ton_main("Of course, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Dumbledore-":
                    label .dumbledore:
                    $ ton_genie_name = "Dumbledore"
                    call ton_main("Sure thing, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Professor-":
                    label .professor:
                    $ ton_genie_name = "Professor"
                    call ton_main("Alright, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk

                "-Old man-":
                    label .old_man:
                    $ ton_genie_name = "Old man"
                    call ton_main("I have to say, for your age you are in a really great shape...", "soft", "base", "base", "down")
                    m "That's part of the benefits of being immortal. Your body doesn't age..."
                    call ton_main("You're lucky then... I've had men that were a couple hundred years old, whose bodies were quite fragile...","open","base","base","R")
                    m "All mortals? How did they get that old?"
                    call ton_main("Ever heard of the \"Philosopher's stone?\"", "base", "narrow", "base", "mid")
                    m "*Ah!* Is it a tiny, red, stone-looking gem, that lengthens the owner's life?"
                    m "It's called the \"sorcerer's stone\" in my world, however."
                    call ton_main("Really? Why is that?","open","base","raised","mid")
                    m "I have no clue..."
                    call ton_main("Didn't you say you were an \"all knowing\" being?","open","base","angry","mid")
                    call ton_main("I guess you really are an \"old man\", Genie...","base","base","base","mid")
                    m "..............."
                    jump tonks_talk

                "-Genie-":
                    label .genie:
                    $ ton_genie_name = "Genie"
                    call ton_main("Of course.","base","base","base","mid")
                    g9 "Sweet."
                    call ton_main("Will I get my three wishes too?","open","base","base","mid")
                    call ton_main("Or would I have to rub your \"thing\" first?","horny","base","base","mid", hair="horny")
                    m "My lamp?"
                    call ton_main("I was talking about your--","base","base","base","R")
                    with hpunch
                    g4 "My lamp!!!"
                    g4 "Shit, where even is that thing?"
                    g4 "I must have lost it when I got to this place!"
                    call ton_main("Do you even need it? Didn't you say you were a free Genie now?", "open", "base", "raised", "mid")
                    g4 "Of course I still need it! What sort of question is that, woman?!"
                    call ton_main("(................)", "mad", "base", "base", "down")
                    g4 "How would you like to suddenly be robbed of your house?!"
                    call ton_main("(I guess I can jerk him off some other time...)", "mad", "base", "worried", "R")
                    m "If you find a golden, shiny looking lamp, return it to me..."
                    call ton_main("Sure, [ton_genie_name]...","upset","base","base","R")
                    jump tonks_talk

                "-Lord Voldemort-":
                    label .lord_voldemort:
                    $ ton_genie_name = "Lord Voldemort"
                    call ton_main("Bold of you to say his name out loud... Who even told you about the dark lord?","open","base","angry","mid")
                    m "I've read the stories..."
                    call ton_main("So you know this wizard did some terrible things in his lifetime?","open","base","angry","R")
                    m "Did he corrupt young witches for his own twisted pleasure?"
                    call ton_main("You could say that... He corrupted many witches and wizards alike.","upset","base","base","mid")
                    m "....................."
                    m "So he was \"Bi\" is what you're saying?"
                    call ton_main("What? No.", "open", "wide", "shocked", "stare")
                    call ton_main("I mean, I'm not really sure if someone like him would have even be capable of loving anything...", "mad", "base", "worried", "R")
                    call ton_main("All that mattered to him was power, and achieving his own immortality...","open","base","angry","mid")
                    m "Both fairly overrated once you have it, if you ask me..."
                    call ton_main("You don't say...","base","base","raised","mid")
                    m "I bet all he secretly wanted was to have a wife, and a kid that loved him..."
                    call ton_main("Voldemort, having a child? Are you serious?", "open", "wide", "shocked", "stare")
                    m "Of course not."
                    m "Once you're immortal, the last thing you need is some annoying brat on your mind..."
                    g9 "All we really want to do is waste a majority of our existence with mindless sex!"
                    call ton_main("Oh my...","horny","base","base","mid", hair="horny")
                    m "And sometimes a bit of kinky role-play..."
                    m "Are you going to call me \"Lord Voldemort\" now or what?"
                    call ton_main("Fine... I will call you, [ton_genie_name], if it makes you happy...","base","base","base","mid")
                    g9 "Yippee!"
                    jump tonks_talk

                "-Daddy-":
                    label .daddy:
                    $ ton_genie_name = "Daddy"
                    call ton_main("Well, you do look about thrice as old as me...","base","base","raised","mid")
                    call ton_main("Crazy to think you geezers get to bang all those young, sexy, innocent witches here...","open","base","base","R")
                    m "(Geezers?)"
                    m "But I thought you didn't mind it?"
                    call ton_main("Oh, I don't mind at all, [ton_genie_name]!","horny","base","base","mid")
                    jump tonks_talk

                "-Master-" (style="disabled") if ton_friendship < 60:
                    label .master_fail:
                    call ton_main("No.","base","base","base","R")
                    m "What?- Why not?"
                    call ton_main("Because... that title has to be earned!","horny","base","angry","mid")
                    m "Seriously?"
                    call ton_main("Yes. Show me that you're worth to be my master, and I'll gladly become your bitch!","open","base","angry","mid")
                    g4 "!!!"
                    call ton_main("Until then you can forget about it...","base","base","base","mid")
                    m "...................."
                    jump tonks_talk
                "-Master-" if ton_friendship >= 60:
                    label .master:
                    $ ton_genie_name = "Master"
                    call ton_main("Yes, [ton_genie_name].","open","base","base","mid")
                    m "(...)"
                    call ton_main("","base","base","raised","mid")
                    call ctc
                    m "(...?)"
                    m "You have permission to speak?"
                    call ton_main("Thank you, [ton_genie_name].","base","base","base","down")
                    g9 "(I could get used to that.)"
                    jump tonks_talk

                "-Custom Input--" (style="disabled") if ton_friendship < 60:
                    m "(I don't think she's yet ready for that)"
                    jump tonks_talk

                "-Custom Input-" if ton_friendship >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)", ton_genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("sir", "dumbledore", "professor", "old man", "genie", "lord voldemort", "daddy", "master"):
                        if temp_name.lower() == "master" and ton_friendship < 60:
                            jump tonks_talk.master_fail
                        $ renpy.jump("tonks_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump tonks_talk
                    else:
                        $ ton_genie_name = temp_name
                        call ton_main("*Hmm*... [ton_genie_name]... I like it.","horny","base","raised","mid")
                    jump tonks_talk

                "-Never mind-":
                    jump tonks_talk


        "-From now on I will address you as-":
            menu:
                "-Tonks-":
                    label .tonks: # Local label unavailable from global scope.
                    $ tonks_name = "Tonks"
                    call ton_main("Sure, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Nymphadora-":
                    $ tonks_name = "Nymphadora"
                    label .nymphadora:
                    call ton_main("*Ugh*--", "mad", "base", "angry", "R")
                    call ton_main("Really, [ton_genie_name]?","open","base","angry","mid")
                    call ton_main("I hate that name...","open","base","worried","R")
                    m "Well you better get used to hearing it then, [tonks_name]..."
                    call ton_main("................","upset","base","angry","R")
                    jump tonks_talk
                "-Nympho-":
                    label .nympho:
                    $ tonks_name = "Nympho"
                    call ton_main("You think I'm a nympho, [ton_genie_name]?","horny","base","raised","mid")
                    call ton_main("Like a filthy, sex craved maniac? Who wouldn't shy away from fulfilling every single one of her fantasies?", "grin", "base", "shocked", "mid")
                    call ton_main("It fits quite well, actually.", "base", "base", "base", "R")
                    jump tonks_talk
                "-Fuck Puppet-":
                    label .fuck_puppet:
                    $ tonks_name = "Fuck Puppet"
                    call ton_main("A fuck puppet?","open","base","raised","mid")
                    call ton_main("So you want me to be your personal toy?","horny","base","base","mid")
                    m "Wouldn't anyone."
                    call ton_main("Such a charmer...", "base", "base", "raised", "R")
                    call ton_main("Of course, [ton_genie_name]... you can call me that if you like.","horny","base","base","mid")
                    jump tonks_talk
                "-Bitch-":
                    label .bitch:
                    $ tonks_name = "Bitch"
                    call ton_main("*Hi-hi*","base","base","base","R")
                    call ton_main("If only you knew...", "horny", "base", "raised", "R")
                    m "(...)"
                    g4 "(What does she mean by that?)"
                    jump tonks_talk

                "-Cunt-" (style="disabled") if ton_friendship < 60:
                    label .cunt_fail:
                    call ton_main("[ton_genie_name], I'm used to getting insulted by my many previous lovers...","base","base","raised","mid")
                    call ton_main("Truth be told I bloody love it!","open_wide_tongue","base","base","ahegao")
                    call ton_main("But we aren't close enough for that yet, don't you think?","open","base","worried","mid")
                    call ton_main("Maybe we should wait with that until we know each other a bit better.","base","base","worried","R")
                    m "Of course.{w} And I will respect that."
                    call ton_main("I'm glad.{w} You are a very polite man, [ton_genie_name]...","base","base","base","mid")
                    m "..........................."
                    jump tonks_talk
                "-Cunt-" if ton_friendship >= 60:
                    label .cunt:
                    $ tonks_name = "Cunt"
                    call ton_main("*Uuuh*, [ton_genie_name]...","base","base","raised","mid")
                    call ton_main("You better not call me that in front of a student...","open","base","base","mid")
                    g9 "What if I do?"
                    call ton_main("Do it, I dare you!","horny","base","base","mid", hair="horny")
                    jump tonks_talk

                "-Custom Input--" (style="disabled") if ton_friendship < 60:
                    m "(I don't think she's yet ready for that)"
                    jump tonks_talk

                "-Custom Input-" if ton_friendship >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)", tonks_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name.lower() in ("tonks", "nymphadora", "nympho", "fuck puppet", "bitch", "cunt"):
                        if temp_name.lower() == "cunt" and ton_friendship < 60:
                            jump tonks_talk.cunt_fail
                        $ renpy.jump("tonks_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump tonks_talk
                    else:
                        $ tonks_name = temp_name
                        call ton_main("*Hmm*...","base","base","base","R")
                        call ton_main("Alright.","base","base","base","mid")
                        m "Really? You don't mind?"
                        call ton_main("Not at all, [ton_genie_name].","horny","base","raised","mid")
                        call ton_main("I've been called quite many things by my lovers!","base","base","base","R")
                        g9 "I'm your lover now?"
                        call ton_main("Never say never.","base","base","base","mid")
                    jump tonks_talk
                "-Never mind-":
                    jump tonks_talk

        "-Never mind-":
            jump tonks_requests
