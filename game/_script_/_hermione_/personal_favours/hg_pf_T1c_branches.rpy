

label hg_pf_admire_breasts_transition:
    stop music fadeout 1.0
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3
    pause.2

    # Setup Pose
    $ hermione.strip("robe", "top", "bra", "accessory")
    call her_chibi("lift_top","mid","base")
    pause 2.0

    call her_main("", "angry", "happyCl", "base", "down", cheeks="blush", trans=d3)
    call ctc

    m "*Hmm*..."
    if her_tier <= 2:
        call her_main("{size=-5}(My breasts are completely exposed...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Come closer [hermione_name], let me take a better look..."

    # Move to desk
    hide screen bld1
    call her_chibi("stand","mid","base")
    with d3
    pause.2

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_show_tits")
    call ctc

    if her_tier <= 2:
        call her_main("............", "annoyed", "narrow", "angry", "R", cheeks="blush", xpos="mid", ypos="base")
        m "Very good..."
        call her_main(".....", "annoyed", "base", "angry", "mid", cheeks="blush")
        call ctc

        show screen blktone
        call her_main("....................................", "annoyed", "narrow", "annoyed", "mid")

    elif her_tier == 3:
        call her_main("", "base", "closed", "base", "mid", xpos="mid", ypos="base")

        m "Very good..."
        call play_music("playful_tension") # SEX THEME.
        her "...................................."

    else:
        call her_main("", "base", "narrow", "base", "mid_soft", cheeks="blush", xpos="mid", ypos="base")

        m "Very good..."
        call play_music("playful_tension") # SEX THEME.
        call her_main("............", "base", "narrow", "base", "mid_soft", cheeks="blush")
    call ctc
    return

### Tier 2 ###

label hg_pf_admire_breasts_T2:

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":     # Event will fail.
            jump hg_pf_admire_breasts_T2_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T2_promise

            jump end_hg_pf_admire_breasts

        "-Start jerking off-":                      # 2/3 branches will fail.
            jump hg_pf_admire_breasts_T2_masturbate

label hg_pf_admire_breasts_T2_promise: # Call label

    ">You take a long look at Hermione's naked tits..."

    #First time event.
    #if her_whoring >= 6 and her_whoring <= 8:
    call ctc

    menu:
        "-Nod your head in approval-":
            ">You Look at the girl's tits for a while and then nod in approval..."
            her "......................"

            return

        "-Shake your head in disapproval-":
            $ her_mood += 3
            ">You Look at the girl's tits for a while and then shake your head in disappointment..."
            her ".....................?!"

            return

label hg_pf_admire_breasts_T2_touch: # Not a Call label

    #Event Fails
    # if her_whoring >= 6 and her_whoring <= 8:
    hide screen hermione_main
    call blkfade
    call bld

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    m "Relax, [hermione_name]. Just stand still!"
    m "Oh... Those are some nice titties you've got..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("No, [genie_name], please! You mustn't do this...", "shock", "happyCl", "worried", "mid")
    m "This won't take long, just stand still."
    call her_main("[genie_name], I didn't agree to this!", "angry", "base", "angry", "mid", cheeks="blush")
    with hpunch
    call her_main("You must unhand me now!!!", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")

    # End Groping
    call blkfade

    ">Hermione pulls away from you and covers up hastily."
    $ hermione.wear("all")
    call her_chibi_scene("reset", "desk", "base")

    call her_main("I think I'd better go...", "angry", "happyCl", "worried", "mid", cheeks="blush", xpos="mid", ypos="base")
    m "Go ahead, [hermione_name]. You are not getting paid if you do..."
    call her_main("But I showed you my...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("And you touched me...", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("And I am getting nothing in return?", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")
    m "You are dismissed, [hermione_name]..."
    call her_main("*Grr*..........", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("{size=-5}(Burn in hell, you wretched old-{/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")

    call her_walk(action="leave")

    $ her_mood += 22

    jump end_hermione_event

label hg_pf_admire_breasts_T2_masturbate: # Not a Call label

    $ her_mood += 2
    $ her_jerk_off_counter += 1
    $ masturbating = True

    hide screen hermione_main
    with d3

    ">You take your cock out and start stroking it..."
    call blkfade

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]?!!", "angry", "wide", "base", "stare")
    m "Just stand still, [hermione_name]..."

    # Start Jerking Off.
    hide screen bld1
    hide screen blktone
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)

    if hg_jerkoff.trigger == False:
        $ achievement.unlock("busted")
        $ hg_pf_talk.change_icon(a="heart_half", b="heart_red")
    $ hg_jerkoff.triggered() # .trigger = True, .counter += 1

    call ctc

    call bld
    call nar(">You stare at Hermione's breasts with hunger...")
    call her_main("[genie_name], what are you...?", "shock", "happyCl", "worried", "mid")
    call nar(">You keep stroking your hard cock...")
    call her_main("[genie_name], no...", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("You must... Put it away...", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Stop whining [hermione_name]. I'm not touching you, am I?"
    call her_main("But...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("But I didn't agree to this!", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("I...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("I think I'd better leave now!", "angry", "happyCl", "worried", "mid", cheeks="blush")

    menu:
        "\"Leave now, and you'll get no points!\"":
            $ her_mood += 30

            call her_main("After {size=+5}this{/size}? Are you kidding me, [genie_name]?", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("I showed you my...", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("..........", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call her_main("I am not going to sell you a single favour anymore, [genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")
            call blkfade

            ">Hermione pulls away from you and covers up..."
            g4 "Don't you dare to leave me in this state, [hermione_name]!"

            $ hermione.wear("all")
            call her_chibi_scene("reset","desk","base", trans=fade)

            call her_main("I am not setting a foot into your office ever again, [genie_name]!", "angry", "squint", "base", "mid", cheeks="blush", xpos="mid", ypos="base")

            g4 "Come on, now. Just say something dirty! I'm almost there!"
            call her_main("You are a horrible person, [genie_name]...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")

            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            with hpunch
            call her_walk(action="leave")

            jump end_hermione_event

        "\"Alright, alright. That's enough for now.\"":
            $ her_mood += 9

            jump end_hg_pf_admire_breasts

        "-Start jerking your cock faster-":
            $ her_mood += 35

            ">You start jerking your cock furiously!"
            call her_main("No, [genie_name], stop!", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")
            ">You jerk it even faster!"
            call her_main("[genie_name], think I will be leaving now...", "annoyed", "narrow", "angry", "R", cheeks="blush")
            g4 "No, wait, I'm almost there!"

            call her_main("Ew! [genie_name]!", "angry", "squint", "base", "mid", cheeks="blush")
            $ hermione.wear("all")
            call her_chibi_scene("reset","desk","base", trans=fade)

            call her_main("I'm leaving!", "angry", "squint", "base", "mid", cheeks="blush")
            call her_walk(action="leave")

            jump end_hermione_event

label hg_pf_admire_breasts_T3:

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":
            call hg_pf_admire_breasts_T3_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T3_promise

        "-Start jerking off-":
            call hg_pf_admire_breasts_T3_masturbate


    jump end_hg_pf_admire_breasts

label hg_pf_admire_breasts_T3_promise:
    ">You take a long look at Hermione's naked tits..."
    # elif her_whoring >= 9 and her_whoring <= 11:
    call ctc

    menu:
        "\"A Nice set of tits you got there.\"":
            call her_main("", "annoyed", "closed", "base", "mid")
            call ctc

            her "Thank--"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("...........", "annoyed", "base", "base", "mid")
            call her_main("You are being inappropriate, [genie_name].", "annoyed", "narrow", "annoyed", "mid")

            return

        "\"*Hmm*... I've seen better.\"":
            $ her_mood += 7

            her "*Tsk*..."
            her "Are we done then?"

            return


label hg_pf_admire_breasts_T3_touch:
    # elif her_whoring >= 9 and her_whoring <= 11:
    hide screen hermione_main
    call blkfade

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    call bld
    m "Relax, [hermione_name]. Just stand still!"
    call her_main("I didn't agree to this, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("I don't think you should...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Don't you like it...?"
    call her_main("What?", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Don't you like it how I squeeze and pull on your breasts?"
    call her_main("...............", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Admit it, you like it a little bit..."
    call her_main("{size=-5}(So strange to see my breasts in someone else's hands...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("[genie_name], I am letting you do this to me to help my house out, nothing more!", "shock", "happyCl", "worried", "mid")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Please, unhand me now!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    show screen blkfade
    with d5

    ">Hermione pulls away from you suddenly and covers up."

    $ hermione.wear("all")
    call her_chibi_scene("reset", "desk", "base")

    hide screen blkfade
    with d5

    call her_main("You promised not to touch, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "It was hard to resist..."

    pause.8

    call her_main(".............", "soft", "base", "base", "R", cheeks="blush")
    call her_main("Can I get paid now please?", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="sweat")
    m "Sure..."

    $ her_mood += 9

    return


label hg_pf_admire_breasts_T3_masturbate:

    # elif her_whoring >= 9 and her_whoring <= 11:
    hide screen hermione_main
    call blkfade

    ">You take your cock out and start stroking it..."

    call her_main("[genie_name]?", "angry", "wide", "base", "stare")
    ">You stare at Hermione's breasts with hunger..."

    #Start Jerking Off.
    hide screen bld1
    hide screen blktone
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)
    call ctc

    call her_main("[genie_name], I didn't agree to this...", "shock", "happyCl", "worried", "mid")
    m "What are you complaining about, [hermione_name]?"
    m "I'm not even touching you..."
    call her_main("Yes, but you are... touching yourself, [genie_name].", "shock", "happyCl", "worried", "mid")
    call nar(">You pick up the pace...")
    m "just stand still, [hermione_name]."
    m "It will be over soon."
    call her_main("..................", "shock", "happyCl", "worried", "mid")
    call her_main("(It's so big...)", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Yes... Yes, like this..."
    m "Yes, with your tits all naked..."
    call her_main("..............", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("well, so be it...", "open", "base", "base", "R", cheeks="blush")
    call her_main("You can keep touching yourself, [genie_name]...", "open", "base", "base", "R", cheeks="blush")
    call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
    call her_main("Not to... *Ehm*...", "open", "base", "base", "R", cheeks="blush")
    call her_main("Not to discharge...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Not in front of me, [genie_name]...", "angry", "base", "angry", "mid")
    m "Fine, whatever..."
    m "Oh, you little slut. You nasty little slut!"
    call her_main(".......................", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call nar(">You start to stroke your cock even harder...")
    g4 "Yes, I know you want this! Yes!"
    call her_main("................", "angry", "happyCl", "worried", "mid", cheeks="blush")

    ">You are about to cum..."

    menu:
        "-Hold it as promised-":
            m "Oh, alright..."
            m "I'd better stop now I suppose..."
            g4 "(Fuck me that hurts...)"
            call her_main("...............", "angry", "happyCl", "worried", "mid", cheeks="blush")
            ">Hermione covers up..."
            $ hermione.wear("all")

            return

        "-Just start cumming-":
            g4 "*Argh*! You whore!"
            call her_main("Proff--?", "scream", "wide", "base", "stare", cheeks="blush")
            call cum_block
            g4 "*Argh*! YES!"
            hide screen bld1
            with d1

            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            call ctc



            call her_main("[genie_name], no, you promised!", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")
            g4 "Oh, this is great, yes..."

            call her_chibi_scene("grope_tits_cum_done")
            with d3

            call her_main("[genie_name], how could you...?", "angry", "squint", "base", "mid", cheeks="blush")
            m "Oh, this was quite amazing..."

            call her_main("", "disgust", "narrow", "base", "down", xpos="mid", ypos="base")
            call ctc

            her "My body..."
            her "It's been defiled..."
            m "Don't worry, I will give you your house points, [hermione_name]."
            m "You did good."

            her "................"
            her "I need to clean myself up..."

            hide screen hermione_main
            show screen blkfade
            with d5

            $ hermione.wear("all")
            $ hermione.set_cum(None)
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen blkfade
            with d5

            call her_main("", "angry", "base", "angry", "mid")
            call ctc

            her "How could you do this to me, [genie_name]?!"
            her "You gave me your word!"
            hide screen hermione_main
            with d3

            $ her_mood += 45

            return



### Tier 4 ###

label hg_pf_admire_breasts_T4:

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":
            call hg_pf_admire_breasts_T4_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T4_look

        "-Start jerking off-":
            call hg_pf_admire_breasts_T4_masturbate

    jump end_hg_pf_admire_breasts

label hg_pf_admire_breasts_T4_look: # Call label
    ">You take a long look at Hermione's naked tits..."
    # elif her_whoring >= 12:

    call ctc

    menu:
        "\"You have great tits, [hermione_name].\"":
            call her_main("You really think so [genie_name]?", "annoyed", "base", "base", "mid")
            call her_main("I am glad you like them, [genie_name]...", "base", "closed", "base", "mid")
        "\"Your tits are alright I suppose...\"":
            call her_main("*huh*?", "annoyed", "base", "base", "mid")
            her "Does this mean you don't like them, [genie_name]?"
            call her_main("I'm sorry...", "disgust", "narrow", "base", "down")

    call blktone
    ">You stare at her breasts for a while longer..."
    call hide_blktone
    call ctc

    m "Alright, you can cover up, [hermione_name]..."
    her "............."
    pause.5

    call blkfade

    ">Hermione covers up..."
    $ hermione.wear("all")
    #End Admiring
    hide screen hermione_main
    hide screen chair_left
    hide screen blktone
    hide screen bld1

    return

label hg_pf_admire_breasts_T4_touch: # Call label
    # Event Also Succeeds
    # elif her_whoring >= 12:
    hide screen hermione_main
    call blkfade

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    call bld
    m "Relax, [hermione_name]. Just stand still!"
    call her_main("But...", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("ah...{heart}", "shock", "happyCl", "worried", "mid")
    call her_main("I didn't agree to this...", "disgust", "narrow", "base", "down", cheeks="blush")
    m "But you like it, don't you?"

    if her_whoring >= 17:
        call her_main("I love it [genie_name]!{heart}", "open", "base", "base", "R", cheeks="blush")
    else:
        call her_main("I do not, [genie_name]!{heart}", "shock", "happyCl", "worried", "mid")

    call blktone
    ">You give her tits a couple of firm squeezes..."
    call hide_blktone

    if her_whoring >= 17:
        call her_main("[genie_name], you promised not to touch...", "base", "base", "base", "R", cheeks="blush")
        m "I know, I know... But it's hard to resist..."
        call her_main(".................{heart}{heart}{heart}", "base", "narrow", "base", "up", cheeks="blush")
    else:
        call her_main("[genie_name], you promised not to touch...", "angry", "happyCl", "worried", "mid", cheeks="blush")
        m "I know, I know... But it's hard to resist..."
        call her_main(".................", "angry", "base", "angry", "mid", cheeks="blush")

    call her_main(".................... ah...{heart}", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("[genie_name], you need to stop now...", "base", "narrow", "base", "up", cheeks="blush")
    m "Just a bit longer..."

    call nar(">You keep on massaging the girl's breasts...")

    call her_main("[genie_name]... please, stop this...", "open", "narrow", "base", "up", cheeks="blush")
    m "Why? Because you like it too much?"
    if her_whoring < 17:
        call her_main("No it's not that...", "base", "base", "base", "R", cheeks="blush")
    call her_main("I mean...", "open", "base", "base", "R", cheeks="blush")

    call nar(">You pull the tits in opposite directions and then squish them together...")

    call her_main("Ah...{heart} [genie_name], I really need to go...", "base", "narrow", "base", "up", cheeks="blush")
    if game.daytime:
        call her_main("That's right... the classes are about to start...", "open", "base", "base", "R", cheeks="blush")
    else:
        call her_main("It is getting late...", "open", "base", "base", "R", cheeks="blush")

    m "Well, alright..."
    show screen blkfade
    with d5

    ">You let go of the girl's breasts..."
    ">Hermione covers up..."

    $ hermione.wear("all")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_chibi_scene("reset", "desk", "base")

    hide screen blkfade
    with d5

    if her_whoring >= 17:
        call her_main("You will have to make it up to me for breaking your promise, [genie_name].", "base", "base", "base", "R", cheeks="blush")
    else:
        call her_main("Please don't think I forgot that you broke your promise, [genie_name].", "annoyed", "narrow", "angry", "R", cheeks="blush")

    m "Right..."

    return

label hg_pf_admire_breasts_T4_masturbate: # Call label
    # elif her_whoring >= 12:
    hide screen hermione_main
    call blkfade

    ">You take your cock out and start stroking it..."
    call her_main("[genie_name]?", "base", "narrow", "base", "up", cheeks="blush")
    ">You stare at Hermione's breasts with hunger..."

    # Start Jerking off.
    hide screen bld1
    hide screen blktone
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)
    call ctc

    if her_whoring < 17:
        call her_main("[genie_name], actually I never agreed to this...", "shock", "happyCl", "worried", "mid")
        m "What are you complaining about, [hermione_name]?"
        m "I'm not even touching you..."
        call her_main("Yes, but you are... touching yourself, [genie_name].", "shock", "happyCl", "worried", "mid")
        m "Just stand still, [hermione_name]."
        m "It will be over soon."
        call her_main("..................", "shock", "happyCl", "worried", "mid")
        m "Yes... Yes, like this..."
        m "Yes, your tits all exposed..."
        call her_main("..............", "disgust", "narrow", "base", "down", cheeks="blush")
        call her_main("well, so be it...", "open", "base", "base", "R", cheeks="blush")
        call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
        call her_main("Not to... *Ehm*...", "open", "base", "base", "R", cheeks="blush")
        call her_main("Not to discharge...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        call her_main("Not on me, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................", "disgust", "narrow", "base", "down", cheeks="blush")
        call nar(">You start to stroke your cock even harder...")
        g4 "Yes, I know you want this! Yes!"
        call her_main("................", "disgust", "narrow", "base", "down", cheeks="blush")

    else: # Different posing than above.
        call her_main("ah...", "base", "narrow", "base", "up", cheeks="blush")
        call her_main("It's so big...", "open", "base", "base", "R", cheeks="blush")
        call her_main("You just couldn't help yourself, could you [genie_name]?", "base", "base", "base", "R", cheeks="blush")
        call her_main("..................", "base", "narrow", "base", "up", cheeks="blush")
        m "Yes... Yes, just like that..."
        m "... with your tits all exposed..."
        call her_main("..............", "base", "narrow", "base", "up", cheeks="blush")
        call her_main("well, so be it...", "open", "base", "base", "R", cheeks="blush")
        call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
        call her_main("Not to... *Ehm*...", "open", "base", "base", "R", cheeks="blush")
        call her_main("Not to cum on me, [genie_name]...", "base", "narrow", "base", "up", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................", "base", "narrow", "base", "up", cheeks="blush")
        call nar(">You start to stroke your cock even harder...")
        g4 "Yes, I know you want this! Yes!"
        call her_main("................", "base", "narrow", "base", "up", cheeks="blush")

    # Genie cums.
    menu:
        g4 "Argh! (I'm about to cum!)"
        "-Hold it in-":
            m "Oh, alright..."
            m "I'd better stop now I suppose..."
            call her_main("...............", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("*Ehm*... I read that that is bad for you, [genie_name]...", "disgust", "narrow", "base", "down", cheeks="blush")
            m "*huh*?"
            call her_main("It is bad for your health to just hold it in like this...", "shock", "happyCl", "worried", "mid")
            call her_main("*Ehm*...", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("If you want to you can--", "base", "base", "base", "R", cheeks="blush")
            g4 "*Argh*! You whore!"
            call her_main("???", "mad", "wide", "base", "stare", cheeks="blush")
            g4 "*Argh*! YES!"

            call cum_block
            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            call bld
            call her_main("[genie_name], I didn't mean that you can release your... semen on me, [genie_name]...", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="sweat")
            g4 "Oh, this is great, yes..."
            call her_chibi_scene("grope_tits_cum_done")
            with d5

            call her_main("Well, what's done is done I suppose...", "base", "base", "base", "R", cheeks="blush")
            m "Oh, this was quite amazing..."

            call her_main("", "disgust", "narrow", "base", "down", xpos="mid", ypos="base")
            call ctc

            her "My body is all sticky though..."
            m "Don't worry, I will give you your house points, [hermione_name]."
            m "You did good."

            call her_main("Thank you [genie_name].", "base", "closed", "base", "mid")
            call her_main("Now I need to clean myself up...", "annoyed", "closed", "base", "mid")
            call ctc

            hide screen hermione_main
            show screen blkfade
            with d5

            $ hermione.set_cum(None)
            $ hermione.wear("all")
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen blkfade
            with d5

            call her_main("", "base", "base", "base", "mid")
            call ctc
            her "Well, this should do for now..."
            hide screen hermione_main

            return

        "-Just start cumming-":
            g4 "*Argh*! You whore!"
            call her_main("???", "mad", "wide", "base", "stare", cheeks="blush")
            g4 "*Argh*! YES!"

            call cum_block
            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            call ctc

            call her_main("ah...{heart} It's so hot...{heart}", "shock", "happyCl", "worried", "mid")
            call her_main("[genie_name], you promised...", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="sweat")
            g4 "Oh, this is great, yes..."

            call her_chibi_scene("grope_tits_cum_done")

            call her_main("Well, what's done is done I suppose...", "angry", "happyCl", "worried", "mid", cheeks="blush")
            m "Oh, this was quite amazing..."

            call her_main("", "disgust", "narrow", "base", "down", xpos="mid", ypos="base")
            call ctc

            her "My body is all covered in semen though..."
            m "Don't worry, it looks good on you."
            m "You did great."

            call her_main("Thank you [genie_name].", "base", "closed", "base", "mid")
            call her_main("Now I need to clean myself up...", "annoyed", "closed", "base", "mid")
            call ctc

            hide screen hermione_main
            call blkfade

            $ hermione.set_cum(None)
            $ hermione.wear("all")
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            call her_main("", "base", "base", "base", "mid")
            hide screen blkfade
            with d5
            call ctc

            her "Well, this should do for now..."
            hide screen hermione_main

            return
