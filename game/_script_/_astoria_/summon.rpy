
label summon_astoria:

    $ active_girl = "astoria"
    $ last_character = "astoria"

    $ astoria_busy = True

    #call update_ast_tier
    call update_astoria

    # Clothes Events
    call astoria_summon_setup

    label astoria_requests:

    # Reset
    call reset_menu_position
    call ast_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not chitchated_with_astoria:
                call astoria_chit_chat
                jump astoria_talk
            else:
                jump astoria_talk


        # Spells
        "-Spells-" (icon="interface/icons/small/spell.webp"):
            if ast_mood != 0:
                call ast_main("I don't want to today...","annoyed","narrow","base","R")
                jump astoria_requests
            else:
                jump astoria_spells

        "-Sexual favours-" (icon="interface/icons/small/condom.webp", style="disabled") if cho_favors_unlocked:
            $ TBA_message()
            jump astoria_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if astoria_wardrobe_unlocked:
            hide screen astoria_main with d1
            $ gui.in_context("wardrobe")
            with d2
            jump astoria_requests

        "-Hidden-" (style="disabled") if not astoria_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump astoria_requests


        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_astoria_gift:
            call gift_menu
            jump astoria_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp", style="disabled") if gave_astoria_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump astoria_requests


        # Dismiss
        "-Dismiss her-":
            stop music fadeout 3.0

            if game.daytime:
                call ast_main("I will go back to classes then, [ast_genie_name].", face="neutral")
            else:
                call ast_main("Oh, alright. Good night, [ast_genie_name].", face="neutral")

            call play_sound("door")

            jump end_astoria_event



label astoria_spells:
    call update_astoria_spells

    python:
        spell_menu = []

        for i in ag_spell_list:
            if not i.is_complete(): # Not trained yet.
                if game.daytime and not tonks_busy:
                    spell_menu.append(i.get_menu_item())
                else:
                    spell_menu.append(i.get_menu_item(disabled=True))

            else: # Spell trained and unlocked.
                spell_menu.append(i.get_menu_item())

        spell_menu.append(("-Never mind-", "nvm"))

        result = renpy.display_menu(spell_menu)

    if result == "nvm":
        jump astoria_requests
    elif result == "block":
        call block_spell_training
        jump astoria_spells
    elif result == "vague":
        call spell_not_known
        jump astoria_spells
    elif result == "busy":
        call person_is_busy
        jump astoria_spells
    else:
        $ renpy.jump(result)


label block_spell_training:
    if not game.daytime:
        m "It's too late for that..."
    elif tonks_busy:
        m "I don't think Tonks has time for that right now..."
    return

label person_is_busy:
    if game.daytime:
        m "Looks like she's taking classes right now."
    else:
        m "Seems like she's already asleep."
    return

label spell_not_known:
    call nar(">You haven't unlocked this spell yet.")
    return

label astoria_talk:
    menu:
        "-Ask about Slytherin Quidditch Team-" (icon="interface/icons/small/quidditch.webp") if cho_tier == 2 and cho_quid.lock_practice and cho_quid.E6_complete and not cho_quid.E8_complete:
            # TODO: Posing
            m "Could you help me with something?"
            ast "Depends what it is."
            ast "And what's in it for me..."
            m "Well, the Slytherin Quidditch team refuses to practise against the Ravenclaws."
            ast "And?"
            m "I was wondering if there's something you could do about it."
            ast "Like what?"
            m "I don't know... ask them nicely?"
            ast "Yeah right, those guys would never listen to me..."
            ast "And can't you do something about it. You're the headmaster!"
            m "Well, I can't technically force them to do anything. If I could then that would make things way easier..."
            ast "Ask Snape then, he's the head of Slytherin... If they'd listen to anyone it'd be him."
            if cho_quid.E9_complete:
                m "I already did..."
            else:
                m "I could..."
            m "Well, I'll try and think of something..."
            ast "You do that."

            jump astoria_talk

        "-Address me only as-":
            menu:
                "-Sir-":
                    label .sir:
                    $ ast_genie_name = "Sir"
                    call ast_main("Very well, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Dumbledore-":
                    label .dumbledore:
                    $ ast_genie_name = "Dumbledore"
                    call ast_main("Of course, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Professor-":
                    label .professor:
                    $ ast_genie_name = "Professor"
                    call ast_main("Of course, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Old man-":
                    label .old_man:
                    $ ast_genie_name = "Old man"
                    call ast_main("Alrighty, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Genie-":
                    label .genie:
                    $ ast_genie_name = "Genie"
                    call ast_main("What?! You are a genie? For real?", face="happy")
                    call ast_main("That's so cool!", face="happy")
                    m "(Oh right. Nobody is supposed to know that.)"
                    m "It's just my name, [astoria_name]..."
                    call ast_main("Oh... okay, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Lord Voldemort-":
                    label .lord_voldemort:
                    $ ast_genie_name = "Lord Voldemort"
                    call ast_main("Voldemort? Like that mean, evil wizard?", face="disgusted")
                    call ast_main("You aren't him, are you?", face="disgusted")
                    m "No, just role-playing..."
                    call ast_main("Oh, alrighty then!", face="happy")
                    call ast_main("[ast_genie_name].", face="happy")
                    jump astoria_talk
                "-Daddy-":
                    label .daddy:
                    $ ast_genie_name = "Daddy"
                    call ast_main("Daddy? Don't you think that's a little weird?", face="disgusted")
                    m "Not at all!"
                    call ast_main("*Hmph*...", face="angry")
                    call ast_main("Alright, why not. Nobody knows about it anyways.", face="neutral")
                    jump astoria_talk
                "-Master-" (style="disabled") if ast_whoring < 18:
                    label .master_fail:
                    $ ast_genie_name = "Dumby" # Tricked
                    call ast_main("*Ha-ha-ha-ha*-- you want me to call you master?", face="happy")
                    call ast_main("That's so dumb!", face="happy")
                    call ast_main("Oh I know!", face="happy")
                    call ast_main("How about I'll call you \"Dumby\" instead? It fits you really well.", face="happy")
                    m "(...)"
                    call ast_main("*Ha-ha-ha-ha*--", face="happy")
                    m "Are you done now?"
                    call ast_main("Yes... I'm sorry... {w=1.0}Dumby...", face="happy")
                    g4 "(Damn brat! We'll see who will be laughing later.)"
                    jump astoria_talk
                "-Master-" if ast_whoring >= 18:
                    label .master:
                    $ ast_genie_name = "Master"
                    call ast_main("*Ha-ha-ha-ha*-- you want me to call you master?", face="happy")
                    call ast_main("That's so silly!", face="happy")
                    m "(...)"
                    call ast_main("Well alright... M-master--", face="happy")
                    call ast_main("*Ha-ha-ha-ha*--{w=1.0}{nw}", face="happy")
                    with hpunch
                    g4 "Shut it... or there will be consequences!"
                    call ast_main("I'm sorry... It won't happen again, master...", face="neutral")
                    jump astoria_talk
                "-Custom Input-" (style="disabled") if ast_whoring < 18:
                    m "(I don't think she's yet ready for that)"
                    jump astoria_talk

                "-Custom Input-" if ast_whoring >= 18:
                    $ temp_name = renpy.input("(Please enter the name.)", ast_genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("sir", "dumbledore", "professor", "old man", "genie", "lord voldemort", "daddy", "master"):
                        if temp_name.lower() == "master" and ast_whoring < 18:
                            jump astoria_talk.master_fail
                        $ renpy.jump("astoria_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump astoria_talk
                    else:
                        $ ast_genie_name = temp_name
                        call ast_main("*Uhm*... ok. I will call you [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk


        "-From now on I will refer to you as-":
            menu:
                "-Miss Greengrass-":
                    label .miss_greengrass:
                    $ astoria_name = "Miss Greengrass"
                    call ast_main("Sure, [ast_genie_name].", face="happy")
                    jump astoria_talk
                "-Girl-":
                    label .girl:
                    $ astoria_name = "Girl"
                    call ast_main("Ok, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Princess-":
                    label .princess:
                    $ astoria_name = "Princess"
                    call ast_main("I really do feel like a princess!", face="happy")
                    call ast_main("After all, I can do whatever I want!", face="angry")
                    jump astoria_talk
                "-Cutie-":
                    label .cutie:
                    $ astoria_name = "Cutie"
                    call ast_main("Fine... If you really have to, [ast_genie_name].", face="disgusted")
                    jump astoria_talk
                "-Slave-" (style="disabled") if ast_whoring < 18:
                    label .slave_fail:
                    call ast_main("I'm not your slave, [ast_genie_name]!", face="angry")
                    m "Of course you aren't! We are just playing a game, that's all..."
                    call ast_main("Well, I don't like your games!", face="angry")
                    call ast_main("Forget it!", face="angry")
                    jump astoria_talk
                "-Slave-" if ast_whoring >= 18:
                    label .slave:
                    $ astoria_name = "Slave"
                    call ast_main("I'm not your slave, [ast_genie_name]!", face="angry")
                    m "Of course you aren't! We are just playing a game, that's all..."
                    call ast_main("Oh I like games!", face="happy")
                    call ast_main("Alrighty then!", face="happy")
                    jump astoria_talk

                "-Custom Input-" (style="disabled") if ast_whoring < 18:
                    m "(I don't think she's yet ready for that)"
                    jump astoria_talk

                "-Custom Input-" if ast_whoring >= 18:
                    $ temp_name = renpy.input("(Please enter the name.)", astoria_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("miss greengrass", "girl", "princess", "cutie", "slave"):
                        if temp_name.lower() == "slave" and ast_whoring < 18:
                            jump astoria_talk.slave_fail
                        $ renpy.jump("astoria_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump astoria_talk
                    else:
                        $ astoria_name = temp_name
                        call ast_main("That's a bit much, don't you think, [ast_genie_name]?", face="disgusted")
                        m "Not at all!"
                        m "I will only call you that when we are alone, promised!"
                        call ast_main("Well... Okay then...", face="neutral")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk

        "-Never mind":
            jump astoria_requests
