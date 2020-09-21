label hermione_summon_setup:
    $ hermione_wardrobe_unlocked = True

    $ random_number = renpy.random.randint(1, 10)

    # Reset doll state
    $ hermione.wear("all")
    $ hermione.set_cum(None)
    $ hermione_animation = None

    #
    # TODO: Remove obsolete variables and fix the code after clothes have been added.
    #
    # if weather == "clear":

        # if her_tier >= 3 and daytime and not hg_muggle_hot_ITEM.unlocked:
            # $ hg_muggle_hot_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_frilled_1"
                # $ h_bottom = "pants_jeans_short"
                # $ h_stockings = "stockings_cute"

                # call update_her_uniform

                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # g4 "(Wow! Look at her!)"
                # g9 "That's quite a sexy outfit, [hermione_name]!"
                # if her_whoring < 11:
                    # call her_main("*Uhm*... Thank you, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("I normally don't wear something like this.", "open", "base", "base", "mid")
                    # call her_main("(Showing so much cleavage...)", "disgust", "narrow", "worried", "down", cheeks="blush")
                    # call her_main("But the weather is just too hot today.", "base", "base", "base", "R")
                    # g9 "You should wear this more often!"
                # else:
                    # call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_hot_ITEM)


    # if weather == "overcast":

        # #One time event.
        # if not hg_accs_wool_g_ITEM.unlocked:
            # $ hg_accs_wool_g_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = True
                # $ hermione_wear_gloves      = True
                # $ hermione_wear_stockings   = True
                # $ h_neckwear = "scarf_striped_g"
                # $ h_gloves = "gloves_wool_1"
                # $ h_stockings = "stockings_striped_1"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "..."
                # m "[hermione_name]..."
                # m "What's with all these clothes you are wearing?"
                # call her_main("It's a bit cold outside, [genie_name]... and my...", "soft", "base", "base", "R", cheeks="blush")

                # if her_whoring < 11:
                    # call her_main("I better not mention it...", "disgust", "narrow", "worried", "down", cheeks="blush")
                # elif her_whoring < 18:
                    # call her_main("{size=-5}People can see my... my nipples...{/size}", "disgust", "narrow", "worried", "down", cheeks="blush")
                # else:
                    # call her_main("I can't have my nipples poking out all the time, [genie_name]! It's distracting!", "annoyed", "narrow", "angry", "R")

                # call her_main("", "soft", "base", "base", "mid")
                # pause.2
                # m "Alright... It looks cute on you."
                # m "You can keep it on for now."
                # call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")

                # $ h_request_wear_top = True
                # $ h_request_wear_bottom = True
                # $ h_request_wear_neckwear = True
                # $ h_request_wear_gloves = True
                # $ h_request_wear_stockings = True

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_accs_wool_g_ITEM)


    # # Raining
    # if weather == "rain":

        # if her_tier >= 2 and not hg_muggle_rainy_ITEM.unlocked:
            # $ hg_muggle_rainy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wet_clothes = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ h_top = "top_sweater_1"
                # $ h_bottom = "pants_jeans_long"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "disgust", "narrow", "worried", "down", xpos="base", ypos="base")
                # call ctc

                # m "Damn girl. You look drenched..."
                # call her_main("I'm sorry, [genie_name], but... It's raining cats and dogs out there!", "open", "base", "base", "mid")
                # call her_main("I couldn't find my robe so I just put on a sweater and some jeans...", "open", "base", "base", "R")
                # call her_main("I hope you don't mind my uniform not being up for standards. I didn't want it to get wet.", "disgust", "narrow", "worried", "down")
                # m "It's fine, [hermione_name]."
                # g9 "Besides, I wouldn't mind seeing you in jeans more often!"
                # call her_main("Thank you, [genie_name].", "normal", "base", "base", "R")
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_rainy_ITEM)

        # # Robe
        # else:

            # $ hermione_wear_robe = True
            # call update_her_uniform
            # call play_sound("door")
            # call her_chibi("stand","mid","base")
            # with d3

            # call play_music("hermione")
            # if her_mood > 1:
                # call her_main("", "annoyed", "base", "base", "R", xpos="base", ypos="base")
            # else:
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # if not h_request_wear_robe:
                # pause.5 #Shows Hermione with robe for a bit.

    # # Snow
    # if weather in ("snow", "blizzard"):

        # if her_tier >= 2 and not hg_muggle_cold_ITEM.unlocked:
            # $ hg_muggle_cold_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings = True
                # $ h_top = "top_pullover_1"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "New outfit?"
                # call her_main("Yes, [genie_name]. I brought it with me from home. It's a bit too cold for just my normal uniform...", "open", "base", "base", "R")
                # call her_main("Do you like it?", "soft", "base", "base", "mid")
                # g9 "I do, [hermione_name]. It's cute."
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_ITEM)

        # elif her_tier >= 3 and not hg_muggle_cold_sexy_ITEM.unlocked:
            # $ hg_muggle_cold_sexy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_pullover_2"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "That's quite the cute outfit, [hermione_name]."
                # call her_main("Thank you, [genie_name]. I made some changes to the old one...", "open", "base", "base", "R")
                # call her_main("Do you like it?", "soft", "base", "base", "mid")
                # g9 "Very much so, [hermione_name]. I love the breast window."
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_sexy_ITEM)

    if hermione_outfits_schedule:
        if not tutorial_is_done("schedule") and hermione_wardrobe_unlocked:
            $ hermione.create_outfit()
            $ her_outfit_last.save()

            default her_outfit_s_clearday = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1], True)
            default her_outfit_s_clearnight = DollOutfit([her_hair_base, her_top_casual1, her_bottom_jeans, her_panties_base1, her_bra_base1], True)
            default her_outfit_s_snow = DollOutfit([her_hair_base, her_top_pullover_1, her_bottom_jeans, her_panties_base1, her_bra_base1], True)
            default her_outfit_s_overcast = DollOutfit([her_hair_base, her_top_pullover_1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True)
            default her_outfit_s_rain = DollOutfit([her_hair_base, her_robe_school_1, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True)

            $ her_outfit_s_clearday.set_schedule(day=True) # Clear day
            $ her_outfit_s_clearnight.set_schedule(night=True) # Clear night
            $ her_outfit_s_snow.set_schedule(day=True, night=True, snowy=True) # Snow, Blizzard
            $ her_outfit_s_overcast.set_schedule(day=True, night=True, cloudy=True) # Storm, Overcast
            $ her_outfit_s_rain.set_schedule(day=True, night=True, rainy=True) # Rain

            $ hermione.equip_random_outfit()

            # Reset some variables for the sake of consistency
            $ her_mood = 0

            call play_sound("door")
            call her_chibi("stand","mid","base")
            with d3

            call play_music("hermione")

            call her_main("Hello, [genie_name].", "open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
            call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
            pause 1.0
            m "You look...{w=0.1} different."

            call tutorial("schedule")

            menu:
                "Turn ON Outfits Scheduling?\n\n{size=-4}(Don't worry, your previous outfit has been saved automatically){/size}"

                "Yes":
                    "Outfit scheduling turned {b}ON{/b}."
                "No":
                    $ hermione_outfits_schedule = False
                    $ tonks_outfits_schedule = False
                    $ cho_outfits_schedule = False
                    $ astoria_outfits_schedule = False
                    $ luna_outfits_schedule = False
                    # Susan

                    "Outfit scheduling turned {b}Off{/b}."

                    $ hermione.equip(her_outfit_last)
                    with fade

            return
        $ hermione.equip_random_outfit()

    call play_sound("door")
    call her_chibi("stand","mid","base")
    with d3

    #Hermione greeting.
    call play_music("hermione")

    if her_mood > 0:
        if 5 > her_mood >= 1:
            call her_main("Yes, [genie_name]?", "soft", "base", "worried", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > her_mood >= 5:
            call her_main("*sigh*... Yes, [genie_name]?", "annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > her_mood >= 10:
            call her_main("What is it, [genie_name]?", "open", "closed", "annoyed", "mid", xpos="base", ypos="base", trans=d3)
            call her_main("", "upset", "base", "annoyed", "mid")
        elif 30 > her_mood >= 20:
            call her_main("What do you want, \"[genie_name]\"?", "upset", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 40 > her_mood >= 30:
            call her_main("*Hmph*...", "normal", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 50 > her_mood >= 40:
            call her_main("*Tsk*", "angry", "base", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif her_mood >= 50:
            call her_main("I have nothing to tell you, sir!", "mad", "narrow", "angry", "L", xpos="base", ypos="base", trans=d3)

        call describe_mood("Hermione", her_mood)
        call tutorial("moodngifts")
    else:
        if daytime:
            call her_main("Good morning, [genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
             call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
