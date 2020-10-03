

label summon_snape:

    $ last_character = "snape"

    call play_music("snape")
    call play_sound("door")
    call sna_chibi("stand","mid","base")
    with d3

    call sna_main("Yes, what is it?","snape_01",xpos="base",ypos="base", trans=d3)

    label snape_ready:
        pass

    menu:
        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not chitchated_with_snape:
                $ chitchated_with_snape = True
                call snape_chitchat

            label .talk:
            menu:
                "-Ask him to help Tonks-" if astoria_intro.E1_complete and not astoria_intro.E3_complete:

                    if astoria_intro.E2_snape:
                        call sna_main("I'm still on the lookout, Genie.","snape_01")
                        call sna_main("If I find the little maggot that casts those spells...","snape_10")
                        jump .talk

                    $ snape_busy = True
                    $ astoria_intro.E2_snape = True
                    $ ag_event_pause = 2
                    jump astoria_intro_E2_snape

                "-Try solving the Quidditch Quarrel-" (icon="interface/icons/small/quidditch.webp") if cho_tier == 2 and cho_quid.E6_complete and not cho_quid.E9_complete and not cho_quid.E8_complete:
                    if daytime:
                        m "I wanted to talk to you about the upcoming Quidditch game."
                        call sna_main("I don't really have time right now...", "snape_05")
                        if wine_ITEM.number >= 1:
                            m "I got drinks."
                        else:
                            m "I'll get us drinks."
                        call sna_main("Tempting, but it'll have to be in the evening... work and all that.", "snape_06")
                        m "Fine."
                        jump .talk
                    else:
                        m "So about that upcoming Quidditch game..."

                        if wine_ITEM.number >= 1:
                            call sna_main("Whatever it is, it can wait, let's sit down first, shall we.", "snape_01")
                            call setup_fireplace_hangout(char="snape")
                            $ ss_he_drink.start()
                            $ ss_he_counter += 1
                            $ wine_ITEM.number -= 1

                            jump cho_quid_E9
                        else:
                            call sna_main("I hope you have some wine at least?", "snape_01")
                            m "I hoped you'd bring your own for once."
                            call sna_main("I see..", "snape_04")
                            call sna_main("I guess you don't need my help after all.", "snape_31")
                            m "(Bloody alcoholic..)"
                            jump .talk

                "-Never mind":
                    jump snape_ready


        # Fireplace Chats
        "-Let's hang-" (icon="interface/icons/small/toast.webp") if wine_ITEM.number >= 1 and not daytime:
            jump snape_hangout

        "{color=[menu_disabled]}-Let's hang-{/color}" (icon="interface/icons/small/toast.webp") if wine_ITEM.number < 1 or daytime:
            if daytime:
                m "(I'm not sharing my booze with Snape while he still has to teach classes...)"
                m "(I better ask him during the evening to get drunk...)"
            elif wine_ITEM.number < 1:
                m "(I don't have any more wine...)"
            jump snape_ready

        # Potions
        # "-Get a potion-" (icon="interface/icons/small/potion.webp") if her_whoring > 10:
        #     jump snape_potion_menu


        # Cardgame
        "-Let's Duel-" (icon="interface/icons/small/cards.webp") if deck_unlocked:
            jump snape_duel_menu

        # Dismiss
        "-Never mind-":
            stop music fadeout 1.0

            if daytime:
                sna "Alright, back to work then..."
            else:
                sna "Goodnight then."

            call play_sound("door")

            $ snape_busy = True

            jump main_room

# Potion Menu
label snape_potion_menu:
    hide screen snape_main
    with fade

    call sna_main("I notice you're making a bit of progress on Miss Granger.","snape_37", ypos="head")
    call sna_main("I've got some potions here that normally aren't available to students.","snape_47")
    call sna_main("These might help speed up the process...","snape_47")

    menu:
        "-Lactantium-" if potion_inv.has("p_milk_potion"):
            ">You already have a Lactantium potion."
            jump snape_ready
        "-Lactantium-" if not potion_inv.has("p_milk_potion"):
            if potion_scene_11_progress == 0:
                call sna_main("Ah yes, a unique concoction of mine. I have a bottle on hand at all times.","snape_37")
                call sna_main("Just in case...","snape_41")
                call sna_main("Here, take it!","snape_02")
                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            elif potion_scene_11_progress == 1:
                call sna_main("Good work on getting her to take it.","snape_37")
                call sna_main("Her breasts did look magnificently full in class.","snape_41")
                call sna_main("*mmmm*, and I think she was even leaking a little...","snape_41")
                call sna_main("Get her to take another!","snape_46")
                call sna_main("Here, I'll even give you a milker for the slut!","snape_02")
                ">Snape hands you an odd leather and metal harness."
                m "What is--"
                ">Snape quickly pushes another milky potion into your hands."
                ">Milking potion received!"
                call sna_main("Don't worry about it, just get her to put it on. It's enchanted so it will handle the rest...","snape_40")
                call sna_main("but I want it back before you leave!","snape_34")
                call sna_main("I spent a fortune on the self cleaning model...","snape_46")
                $ potion_inv.add("p_milk_potion")
            else:
                call sna_main("*Mmmm*, I wish I could be there to see you milk her...","snape_41")
                m "..."
                m "(That's probably not a good idea...)"
                call sna_main("All that {b}delicious{/b} milk...","snape_40")
                m "(definitely not a good idea.)"
                call sna_main("...","snape_41")
                call sna_main("Well anyway, I was wondering...","snape_37")
                call sna_main("Want me to augment the potion?","snape_37")
                m "Augmented?"
                m "I never asked for this..."
                call sna_main("I know... I'm offering it...","snape_34")
                m "Oh yeah, sorry. What sort of augmentation?"
                call sna_main("Well I can leave the potion as it is...","snape_38")
                call sna_main("Or I can add an extra little something to it.","snape_40")
                m "Such as?"
                call sna_main("Well...","snape_37")
                label snape_potion_choice:
                    pass
                menu:
                    "-Normal potion-":
                        $ potion_version = 1
                        call sna_main("Here you are mister Adventurous...","snape_35")

                    "-Futa potion-":
                        call sna_main("What? Are you sure you want this one?","snape_44")
                        call sna_main("I mean I figured you were a bit of a pervert...","snape_02")
                        call sna_main("but I didn't think...","snape_45")
                        call sna_main("Oh well, if you want it, it's yours...","snape_02")
                        menu:
                            "-give it to me-":
                                $ potion_version = 2
                                call sna_main("really?","snape_44")
                                call sna_main("you're more Adventurous than I thought!","snape_02")
                                call sna_main("Here, I'll even give you an extra attachment for the milker!","snape_46")
                                ">Snape hands you a different cannister with a soft plastic opening in the bottom. It looks almost like an anus."
                                call sna_main("I also put an undetectable extension charm on the cannister... Promise to tell me what happens!","snape_45")
                            "-no-":
                                call sna_main("Too bad...","snape_35")
                                jump snape_potion_choice

                    "-Permanent breast expansion-":
                        call sna_main("The milk production will still only last a day...","snape_02")
                        call sna_main("But her big boobs will be permanent...","snape_37")
                        if hermione_perm_expand_breasts:
                            call sna_main("Drinking this potion again will undo the permanent effect","snape_02")
                        call sna_main("Are you sure you want this?","snape_02")
                        call sna_main("She might not like it...","snape_46")
                        menu:
                            "-yes-":
                                $ potion_version = 3
                                call sna_main("Fantastic!!!","snape_45")
                            "-no-":
                                call sna_main("Too bad...","snape_35")
                                jump snape_potion_choice

                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            jump snape_ready

        "-Veritaserum-" if potion_inv.has("p_veritaserum"):
            ">You already have a Veritaserum potion."
            jump snape_ready
        "-Veritaserum-" if not potion_inv.has("p_veritaserum"):
            call sna_main("Truth potion.","snape_01")
            call sna_main("This is dangerous stuff Genie...","snape_01")
            call sna_main("Use it to make anyone tell the truth.","snape_47")
            call sna_main("Just not me!","snape_36")
            ">Snape hands you the tiny vial filled with a strange gold liquid."
            ">Veritaserum received!"
            $ potion_inv.add("p_veritaserum")
            jump snape_ready

        "-Voluptatem-" if potion_inv.has("p_voluptatem"):
            ">You already have a bottle of Voluptatem."
            jump snape_ready
        "-Voluptatem-" if not potion_inv.has("p_voluptatem"):
            m "Volupwhatem?"
            call sna_main("This is actually an experimental potion of mine...","snape_01")
            call sna_main("I'm not sure if this is ready for testing on humans yet.","snape_35")
            ">Snape hands you the small bottle filled with a swirling pink and purple liquid."
            ">Voluptatem received!"
            $ potion_inv.add("p_voluptatem")
            jump snape_ready

        "\"Never mind.\"":
            jump snape_ready
