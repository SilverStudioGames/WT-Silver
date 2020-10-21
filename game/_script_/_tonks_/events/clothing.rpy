label tonks_summon_setup:

    #TODO I was thinking this event could trigger after certain events for now: some days after Astoria imperio training and some days after Cho/Tonks strip event (would that mess up with other story stuff happening around that time?)
    #TODO add a variable for which event it has triggered from (for dialog variation in this event)
    #TODO remove friendship check (not really relevant to her lewdness level atm plus it could mess up other checks)
    #TODO Added a choice if she should stay naked or put on clothes, move wardrobe functions to each option
    $ tonks_wardrobe_unlocked = True

    # Reset doll state
    $ tonks.wear("all")
    $ tonks.set_cum(None)
    $ tonks_animation = None

    $ random_number = renpy.random.randint(1, 20)
    if 5 > random_number > 0 and tonks.is_worn("top") and ton_friendship >= 50:

        if not tonks_strip_happened: #First time.
            $ tonks_strip_happened = True

            $ tonks.strip("all")
            call ton_walk(action="enter", xpos="mid", ypos="base")

            call play_sound("scratch")
            with hpunch
            g4 "!!!"

            call ton_main("","base","base","base","mid", hair="horny", xpos="mid", ypos="base", trans=d5)
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You're naked!"
            call ton_main("Indeed I am.","open","base","raised","mid")
            call ton_main("Is that a problem, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("Am I going to get fired for inappropriate behaviour?","open","base","base","R")
            call ton_main("Are you going to report me to the ministry?","horny","base","raised","mid")
            m "..."
            m "Have you been drinking?"
            call ton_main("Maybe...","base","base","base","mid")

        else: #Repeated Event.

            $ tonks.strip("all")
            call ton_walk(action="enter", xpos="mid", ypos="base")

            call play_music("chipper_doodle")
            call ton_main("","base","base","base","mid", hair="horny", xpos="mid", ypos="base", trans=d5)
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You're naked again."
            call ton_main("Yes... I just felt like it.","base","base","raised","stare")
            m "(She's smashed...)"
            m "Miss Tonks, you should be more careful."

        m "One of the girls could have seen you..."
        call ton_main("Oh, I would love for them to see me like this...","horny","base","raised","mid")
        call ton_main("Why don't you invite one to your office?","horny","base","base","mid")

        if ag_st_imperio.counter > 0:
            m "You'd like that wouldn't you..."
            ton "Very much!"
            m "Like that Astoria girl you're so infatuated with?"
            m "Want me to call her up here to have her shame you on your bad behaviour?"
            ton "Oh, yes please!"

        #TODO if triggered after last Cho strip favour with tonks done (Gryffindor tier)
        # Note: No such event exists in the game yet (?)
            #m "Would you like me to bring Miss Chang up here so you rub your bodies together?"
            #ton "Yes please!"
            #m "You sure you're ready to find out just how flexible she is?"
            #ton "Yes!"

        m "I bet you'd love that..."
        m "(Although that's probably not the best idea in her current state...)"
        g9 "(Doesn't mean I can't tease her a bit though...)"

        menu:
            "-Play nice-":
                g9 "How about a bonus instead?"
                call ton_main("A bonus? For showing my body to my own boss?","open","base","raised","mid")
                call ton_main("How much am I worth to you, [ton_genie_name]?","base","base","raised","mid")

                menu:
                    "-Zero gold-" if game.gold <= 0:
                        m "Zero gold."
                        call ton_main("Seriously?","angry","base","raised","mid")
                        m "Yes, I'm a cheap bastard."
                        call ton_main("I can see that...","upset","base","base","mid")

                    "-One gold-" if game.gold > 0:
                        m "A single gold coin, if anything..."
                        call ton_main("(Bastard... How humiliating.)","base","base","raised","ahegao")
                        call ton_main("Thank you so much, [ton_genie_name].","base","base","base","mid")
                        m "Don't mention it, [tonks_name]."
                        $ game.gold -= 1

                    "-Twenty gold-" if game.gold >= 20:
                        m "How does twenty gold sound?"
                        call ton_main("(*Hmm*... I kind of expected more.)","base","base","base","R")
                        call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")
                        g9 "No, [tonks_name]... Thank you."
                        $ game.gold -= 20

                    "-A hundred gold-" if game.gold >= 100:
                        m "Does one hundred gold sound nice to you?"
                        g9 "With a body like that, you could earn a fortune at a strip club!"
                        call ton_main("Really...","horny","base","raised","mid")
                        call ton_main("You think a noble teacher like me, an ex-auror, would quit her highly regarded job to become a cheap stripper?","open","base","base","mid")
                        m "Well, no. I still want to keep you as a teacher."
                        m "I merely suggested that you could."
                        call ton_main("Maybe the duelling stage could find some extra use...","base","base","base","R")
                        call ton_main("Perhaps some extra curricular activities for a couple of my favourite students could be arranged...","open","base","raised","mid")
                        g9 "I'm sure they would all love to watch their perverted teacher strip!"
                        $ game.gold -= 100

                m "Now..."

            "-Scold her-":
                m "You know I have to, Miss [tonks_name]."
                m "Walking into your boss' office, completely naked?"
                m "Behaviour like that from a teacher... that's just unspeakable!"
                call ton_main("I'm terribly sorry, [ton_genie_name]...","open","base","base","down")
                m "What will you do next? Climb under my desk and suck my cock?"
                g4 "Spread your legs for one of your students?"
                call ton_main("...","base","base","raised","stare")
                g4 "How's this befitting for a teacher... strutting into the headmaster's office in your birthday suit."
                g9 "That surely calls for some punishment, don't you think?"
                call ton_main("You are so right, [ton_genie_name]!","base","base","worried","mid")

                #TODO This section will be under some whoring check later
                # m "I should make you the school's cum-dumpster instead. How would you like that position?"
                # m "Boys lining up in front of the school toilets, waiting their turn to dump their cum into their teacher's mouth, day after day!"
                # call ton_main("You're making me so wet, [ton_genie_name]!","base","base","base","ahegao")
                # call ton_main("Maybe some day I'll get bored of my current position here at Hogwarts... you never know...","horny","base","raised","mid")
                # m "I'm not done with your punishment, Miss [tonks_name]!"
                if not tonks_strip_happened:
                    m "You went to this school, didn't you? Which house were you in?"
                    call ton_main("Me? I was in Hufflepuff.","open","base","raised","mid")
                    m "Very well then."
                    m "Minus ten points from Hufflepuff!"
                    $ hufflepuff -=10
                    call ton_main("What? But [ton_genie_name]! I'm not even a student--", "open", "wide", "shocked", "mid", trans=hpunch)
                else:
                    m "Then that's another minus ten points from Hufflepuff!"
                    ton "Again? But please, sir!"
                    ton "What will they say once I get back to the common room?"
                    m "What?"
                    ton "Oh... I'm a teacher now aren't I... silly me."

                m "Also--"

        menu:
            "-Those clothes stay off!-":
                $ tonks.unequip("all")

                ton "*Hmm*?"
                m "That's right... since they're so bothersome, why bother wearing them at all?"
                m "When you're in here with me I want you on full display!"
                ton "Of course sir..." #Horny
                call ton_main("If you want me to put my clothes back on at any time, just let me know...","base","base","base","mid")

            "-Get dressed!-":
                m "No teacher of mine will strut around naked...{w} unless I say so!"
                ton "Yes sir..."
                m "Now, put your clothes back on..."
                ton "*Ehm*... Okay..."

                call play_sound("magic")
                $ tonks.wear("all")
                call ton_main(trans=morph)

                if tonks_morph_known:
                    m "...{w} You used your meta-whatsit ability just then didn't you?"
                    ton "You can tell?"
                    m "Whatever, just wear your actual clothing next time..."
                else:
                    m "Much better..."
                    ton "..." #smirks #looking down (She's just morphed so she looks like she has clothes)

        m "Now, get back to your room and think about what you've done..."
        ton "Of course sir..." #look down, blush
        m "On second thought, stay here, we're not done yet."

        call ton_main(xpos="base", ypos="base", trans=fade)

        return

    if tonks_outfits_schedule:
        $ tonks.equip_random_outfit()

    call play_sound("door")
    call ton_chibi("stand","mid","base")
    with d3

    #Tonks greeting.
    call play_music("tonks")

    if ton_mood > 0:
        if 5 > ton_mood >= 1:
            call ton_main("Yes, [ton_genie_name]?", "open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
            call ton_main("", "base", "base", "base", "R")
        elif 10 > ton_mood >= 5:
            call ton_main("I have classes to teach, please be quick.", "upset", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > ton_mood >= 10:
            call ton_main("Make it quick, [ton_genie_name]...", "upset", "base", "base", "R", xpos="base", ypos="base", trans=d3)
        elif 30 > ton_mood >= 20:
            call ton_main("What do you want, \"[ton_genie_name]\", I'm busy.", "mad", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 40 > ton_mood >= 30:
            call ton_main("...............", "upset", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 50 > ton_mood >= 40:
            call ton_main("Please stop wasting my time.", "upset", "closed", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif ton_mood >= 50:
            call ton_main("You have the nerve to call me here after what you did.", "upset", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)

        call describe_mood("Tonks", ton_mood)
        call tutorial("moodngifts")
    else:
        call ton_main("You called, [ton_genie_name]?","base","base","base","mid", xpos="base", ypos="base", trans=d3)
    return
