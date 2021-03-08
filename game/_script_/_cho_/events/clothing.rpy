label cho_summon_setup:

    $ cho_wardrobe_unlocked = True

    # Reset doll state
    $ cho.wear("all")
    $ cho.set_cum(None)
    $ cho_animation = None

    # Unlock favours at tier 3
    # this will probably move to a cho_quid_E# event once we've implemented Gryffindor lead-up events
    if cho_tier == 3:
        $ cho_favors_unlocked = True

    # Clear Weather.
    if game.weather == "clear":

        # Hot muggle outfit.
        if cho_strip_complete and not cho_outfit_trainee.unlocked:
            $ cho.unequip("all")
            $ cho.equip(cho_outfit_trainee)

            call play_sound("door")
            call cho_chibi("stand", "mid", "base")
            with d3

            call play_music("cho")
            call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", animation=move_fade)
            $ cho_animation = None
            call ctc

            g9 "Got a new outfit, [cho_name]?"
            call cho_main("Yes, [cho_genie_name].", "smile", "base", "raised", "R")
            call cho_main("I thought about our Quidditch training a bit more, and how effective it is.", "open", "base", "base", "downR")
            call cho_main("So I figured, maybe, if I applied those training methods to my daily school life...", "soft", "base", "worried", "mid")
            call cho_main("It will help me get even more popular...", "quiver", "base", "raised", "down")
            g9 "You most certainly will, [cho_name]! I can promise you that!"
            call cho_main("I hope so too...", "soft", "base", "raised", "mid")
            call cho_main("Do you like my new outfit?", "smile", "closed", "raised", "mid")
            g9 "Absolutely!"
            call cho_main("Thank you.", "base", "base", "base", "mid")

            #Unlocks rewards.
            call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item=cho_outfit_trainee)

            call cho_main(xpos="base", ypos="base", trans=fade)

            return

        # Party outfit.
        elif cho_strip_complete and cho_whoring >= 14 and not cho_outfit_party.unlocked:
            $ cho.unequip("all")
            $ cho.equip(cho_outfit_party)

            call play_sound("door")
            call cho_chibi("stand", "mid", "base")
            with d3

            call play_music("cho")
            call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", animation=move_fade)
            $ cho_animation = None
            call ctc

            g9 "Wow girl, what are you wearing?"
            call cho_main("It's my party outfit...", "soft", "base", "raised", "down")
            m "(...)"
            call cho_main("Is it too much?", "quiver", "base", "raised", "mid")
            m "Too much? Are you really asking me that?"
            m "If I'm truly honest with you--"
            g4 "Your body, in an outfit like that--"
            g9 "Really shows off your best assets."
            call cho_main("Oh...", "base", "base", "raised", "down", cheeks="blush")
            call cho_main("You see, that sort of reaction is just what I wanted to get from the boys...", "soft", "base", "base", "downR", cheeks="blush")
            call cho_main("Stare at my assets any time you want, [cho_genie_name]!", "base", "narrow", "angry", "mid")
            g4 "*Hngh*!!!"

            #Unlocks rewards.
            call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item=cho_outfit_party)

            call cho_main(xpos="base", ypos="base", face="horny", trans=fade)

            return

    if cho_outfits_schedule:
        $ cho.equip_random_outfit()

    call play_sound("door")
    call cho_chibi("stand", "mid", "base")
    with d3

    #Cho greeting.
    call play_music("cho")

    if cho_mood > 0:
        if 5 > cho_mood >= 1:
            call cho_main("Yes, [cho_genie_name]?", "annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > cho_mood >= 5:
            call cho_main("*sigh*... Yes, [cho_genie_name]?", "open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
        elif 20 > cho_mood >= 10:
            call cho_main("What is it, [cho_genie_name]?", "annoyed", "base", "angry", "mid", xpos="base", ypos="base",trans=d3)
        elif 30 > cho_mood >= 20:
            call cho_main("What do you want, \"[cho_genie_name]\"?", "angry", "narrow", "angry", "mid", xpos="base", ypos="base",trans=d3)
        elif 40 > cho_mood >= 30:
            call cho_main("*Hmph*...", "upset", "base", "angry", "R", xpos="base", ypos="base",trans=d3)
        elif 50 > cho_mood >= 40:
            call cho_main("*Tsk*", "soft", "narrow", "angry", "R", xpos="base", ypos="base",trans=d3)
        elif cho_mood >= 50:
            call cho_main("I can't believe you've done this!", "scream", "wide", "angry", "mid", xpos="base", ypos="base",trans=d3)
            call cho_main("", "upset", "wide", "angry", "mid")

        call describe_mood("Cho", cho_mood)
        call tutorial("moodngifts")
    else:
        if game.daytime:
            call cho_main("Good morning, [cho_genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
            call cho_main("Good evening, [cho_genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)

    return
