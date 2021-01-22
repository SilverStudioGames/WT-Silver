

### Hermione Handjob ###

label hg_pf_handjob:

    if hg_pf_handjob.counter == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(I feel like getting another handjob!){/size}"

    if hg_pf_handjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 45
    $ hg_pf_handjob.start()


    # End Event
    label end_hg_pf_handjob:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Points
    if her_tier <= 5:
        m "Yes, [hermione_name]. {number=current_payout} to Gryffindor."
        $ gryffindor += current_payout
    else:
        m "You may leave now, [hermione_name]."

    call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")

    if game.daytime:
        her "I better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."

    # Hermione leaves
    call her_walk(action="leave")

    # Increase level
    if her_tier == 4:
        if her_whoring < 18: # Points til 18
            $ her_whoring += 1
    if her_tier == 5:
        if her_whoring < 21: # Points til 21
            $ her_whoring += 1

    jump end_hermione_event

### Fail Events ###

label hg_pf_handjob_fail:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Do you know what a \"handjob\" is?"

    $ hg_pf_handjob.fail()

    jump too_much

### Tier 4 ###

# Event 1 (i) - Hermione wants 100 house points for it!
# Event 2 (i) - Reluctantly does it again.
# Event 3 (r) -

label hg_pf_handjob_T4_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Do you know what a \"handjob\" is?"
    call her_main("Why?", "annoyed", "narrow", "annoyed", "mid")
    m "I feel like getting one..."
    call her_main("[genie_name]!", "angry", "base", "angry", "mid")
    m "Just another favour. No big deal, right?"
    call her_main("......", "disgust", "narrow", "base", "mid_soft")
    call her_main("{size=-7}I want a hundred house points for this...{/size}", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "*huh*? What was that?"
    call her_main("I want a hundred house points for this!!!", "scream", "happyCl", "worried", "mid")
    call her_main("", "clench", "happyCl", "worried", "mid")
    m "A Hundred house points, *huh*?"
    m "And you will stroke my cock and everything?"
    call her_main("{size=-7}Yes...{/size}", "disgust", "narrow", "base", "mid_soft")
    m "Sorry, I couldn't hear you..."
    call her_main("Yes, I said yes! I will stroke your stupid cock, [genie_name]!", "scream", "happyCl", "worried", "mid")
    call her_main("", "upset", "narrow", "angry", "R")

    label back_to_handjob_choices:

    menu:
        m "..."
        "\"You will get fifteen house points.\"":
            $ her_mood += 7
            call her_main("For fifteen house points I suppose I could let you molest me a little, but that is all you'll be getting, [genie_name].", "annoyed", "narrow", "angry", "R")
            her "I will not stoop as low as to sell handjobs for fifteen house points."
            her "That is just insulting, [genie_name]."

            jump back_to_handjob_choices

        "\"You will get forty-five house points.\"":
            $ her_mood += 3
            call her_main(".....", "annoyed", "narrow", "angry", "R")
            call her_main("{number=current_payout} house points...?", "open", "narrow", "worried", "down")
            her "This could put Gryffindor back in the lead..."
            m "Is that a \"yes\"?"
            call her_main("Yes, it is a yes, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
            m "Great!"
            pass

        "\"You will get one hundred house points.\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ current_payout = 100
            call her_main("{number=current_payout} points?!", "scream", "wide", "base", "mid")
            her "This will definitely put Gryffindor in the lead!"
            m "Is that a \"yes\" then?"
            call her_main("Of course!", "smile", "happyCl", "base", "mid")
            call her_main("If it will bring Gryffindor a hundred house points, I don't mind touching your... thing a little.", "smile", "happyCl", "base", "mid", emote="happy")
            pass

    jump hg_pf_handjob_1

label hg_pf_handjob_T4_intro_E2:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Do you know what a \"handjob\" is?"
    call her_main("You have asked me that already, [genie_name].", "disgust", "narrow", "base", "mid_soft")
    m "Ah, that's right."
    m "Well, I want you to play with my cock again."
    call her_main("[genie_name], you are being vulgar again...", "upset", "closed", "base", "mid")
    m "Fine, fine."
    m "[hermione_name], I would like to buy another favour from you today."
    call her_main("Of course, [genie_name].", "annoyed", "narrow", "angry", "R")
    g9 "The favour being you playing with my cock!"
    call her_main("..............", "disgust", "narrow", "base", "mid_soft")
    m "Oh, come on. For the honour of Gryffindor?"
    call her_main(".............", "angry", "base", "angry", "mid")
    g9 "Play with my cock for the honour of the Gryffindor, [hermione_name]!"
    call her_main("Stop saying that, [genie_name]...", "scream", "base", "angry", "mid", emote="angry")
    m "Come on [hermione_name], it's not like I'm asking you to do this for free."
    call her_main(".......", "annoyed", "narrow", "angry", "R")

    jump hg_pf_handjob_1

label hg_pf_handjob_T4_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "How would you like to give me another handjob?"

    call her_main("...............", "upset", "base", "angry", "mid")
    call her_main("Will I be getting paid for it, [genie_name]?", "open", "base", "angry", "mid")
    m "Of course. {number=current_payout} points."
    call her_main(".........................", "upset", "narrow", "angry", "R")

    jump hg_pf_handjob_1

### Tier 5 ###

# Event 1 (i) -
# Event 3 (r) -

label hg_pf_handjob_T5_intro_E1:
    call her_main("[genie_name]?", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind giving me another handjob, do you?"
    call her_main("*Ehm*...", "upset", "narrow", "worried", "down")
    call her_main("As long as I am getting paid...", "grin", "base", "base", "R")
    m "Well, then. Time to earn those points."

    jump hg_pf_handjob_2

label hg_pf_handjob_T5_intro_E2:
    call her_main("[genie_name]?", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind giving me another handjob, do you?"
    call her_main("I guess not, [genie_name]...", "grin", "narrow", "worried", "down")
    call her_main("...................", "clench", "base", "base", "R")

    jump hg_pf_handjob_2

label hg_pf_handjob_T5_repeat:
    call her_main("[genie_name]?", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind giving me another handjob, do you?"
    call her_main("Of course not, [genie_name]...", "grin", "base", "base", "R")

    jump hg_pf_handjob_2

### First Tier Handjob ###

label hg_pf_handjob_1:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand",560,"base")
    call gen_chibi("jerk_off",450,"base")

    hide screen blkfade
    with fade
    pause.8

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "disgust", "narrow", "worried", "down", xpos="base", ypos="head")
    m "Whenever you're ready, [hermione_name]."
    call her_main(".......................", "disgust", "happyCl", "worried", "mid", ypos="head")
    pause.1

    call her_chibi_scene("hj_pause", trans=d9)
    pause.8

    call nar(">Hermione puts her slender hands on your cock...")

    call bld
    m "Good. Now stroke it."
    call her_main("Right...", "angry", "happyCl", "worried", "mid", emote="sweat")

    call her_chibi_scene("hj", trans=d5)
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call bld
    g9 "Nice..."

    if hg_pf_handjob.counter == 1:
        call her_main("!!!", "shock", "wide", "base", "stare")
        call her_main("Are you about to finish, [genie_name]?!")
        m "About to finish?"
        m "Don't be ridiculous [hermione_name], we are just getting started."
        call her_main("Oh...", "angry", "happyCl", "worried", "mid", emote="sweat")
        call her_main("......")
        call her_main("You will give me a warning though, won't you, [genie_name]?", "upset", "wink", "base", "mid")
    else:
        call her_main("[genie_name]...?", "angry", "happyCl", "worried", "mid", emote="sweat")
        m "What is it?"
        call her_main("Will you warn me before... *uhm*... you know...", "angry", "happyCl", "worried", "mid", emote="sweat")

    $ d_flag_01 = False #If TRUE Genie promised to warn her.

    menu:
        m "..."
        "\"Of course I'll let you know when it's time.\"":
            $ d_flag_01 = True #If TRUE Genie promised to warn her.
            call her_main("Thank you, [genie_name].", "normal", "happyCl", "worried", "mid")
        "\"I myself don't always know when...\"":
            call her_main("Really? But I thought...", "open", "base", "base", "mid")
            call her_main("Well, never mind then...", "normal", "happyCl", "worried", "mid")

    call her_main("........", "open", "base", "base", "mid")
    m "............."
    call her_main(".............", "normal", "happyCl", "worried", "mid")
    call her_main("*ehh*... [genie_name]?")
    m "Yes, what is it?"
    call her_main("How long do you think this will take?", "open", "base", "base", "mid")
    m "Why?"

    if game.daytime:
        call her_main("Well, it's just that my classes are about to start...", "upset", "wink", "base", "mid")
    else:
        call her_main("Well, it's just that I have this paper that I need to finish...", "upset", "wink", "base", "mid")
        call her_main("It's due tomorrow, and it's getting pretty late...")

    m "Do you need the points or not?"
    call her_main("I do, [genie_name]! I'm sorry...", "base", "happyCl", "base", "mid")
    call her_main("I will just keep on stroking it then...")
    m "Well, there is something you could do to speed up the process..."
    call her_main("Really? What is it [genie_name]?", "base", "base", "base", "mid")

    menu:
        m "..."
        "\"Tell me how much of a whore you are!\"":
            call her_main("What?", "angry", "base", "angry", "mid")
            call her_main("But I'm not...")
            m "No need to be honest, [hermione_name]."
            m "Just make things up."
            call her_main("Really?", "upset", "wink", "base", "mid")
            m "Sure. Just have fun with it."
            call her_main("Well, in that case...", "open", "narrow", "worried", "down")
            call her_main("I am a... whore.")
            m "Heh... good. Go on."
            call her_main("I am a big whore...", "open", "narrow", "worried", "down")
            m "Yes, you are."
            call her_main("I am the biggest whore in England!", "annoyed", "narrow", "annoyed", "mid")
            call her_main("I try to act innocent, but in truth all I think about is cock!")
            m "Yes, you little slut!"
            call her_main("Yes! I am a slut!", "annoyed", "narrow", "angry", "R")
            call her_main("I crave cock all the time.")
            m "Very nice!"
            m "But, like I said, you don't have to be honest."
            call her_main("What?", "shock", "wide", "base", "stare")
            call her_main("[genie_name], those things I say are not true!", "upset", "wink", "base", "mid")
            g9 "Heh... I know. I'm just messing with you."
            call her_main("[genie_name]!", "disgust", "narrow", "base", "mid_soft")
            m "You are doing a great job, though. Keep at it!"
            call her_main(".....", "open", "narrow", "worried", "down")
            call her_main("I love cock...")
            call her_main("And I love... spunk...", "clench", "narrow", "base", "down")
            call her_main("And semen... and sperm...")
            call her_main("I love to drink sperm...")
            call her_main("I want you to feed me your sperm, [genie_name]!", "open_tongue", "narrow", "base", "mid_soft")
            g4 "!!!"
            call her_main("Or better yet, pump me full of it, [genie_name]!", "smile", "narrow", "base", "mid_soft")
            with hpunch
            g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

        "\"Stick your tongue out and look at me!\"":
            call her_main("What?", "base", "base", "base", "mid")
            m "Just do it, slut."
            call her_main("Like this?", "open_wide_tongue", "happy", "base", "R")
            m "Yes, good. Keep looking into my eyes and stroke my cock."
            call her_main(".....................", "open_wide_tongue", "base", "base", "mid")
            m "Yes... Good..."
            call her_main("...........", "open_wide_tongue", "base", "base", "mid")
            call her_main("...........")
            call her_main("I can't keep my mouth open for so long, [genie_name]. I will start to drool...", "open", "base", "base", "mid")
            m "But I want you to drool..."
            call her_main("What? But I will look silly!", "open", "base", "base", "mid")
            m "That's the point, [hermione_name]!"
            call her_main(".......", "annoyed", "base", "worried", "R")
            m "Don't you want to be done with this as soon as possible?"
            call her_main("............", "normal", "happyCl", "worried", "mid")
            call her_main("A-ha...", "open_wide_tongue", "base", "base", "mid")
            m "Good, [hermione_name]."
            call her_main("..............", "open_wide_tongue", "base", "base", "mid")
            m "Yes, keep on stroking my cock."
            call her_main("..................", "open_wide_tongue", "base", "base", "mid")
            g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
            call her_main(".................", "open_wide_tongue", "closed", "angry", "mid")
            m "No, keep on looking at me!"
            call her_main(".....................", "open_wide_tongue", "base", "base", "mid")
            m "Yes, you little slut!"
            call her_main("......................", "open_wide_tongue", "base", "angry", "mid")
            m "I want to cum in that mouth, yes..."
            call her_main("................", "open_wide_tongue", "base", "angry", "mid")
            with hpunch
            g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

        "\"Give my cock a kiss!\"":
            call her_main("Excuse me?", "angry", "base", "angry", "mid")
            m "You know, just a little kiss, right on the tip."
            call her_main(".............", "angry", "base", "angry", "mid")
            call her_main("... with my lips?", "shock", "wide", "base", "stare")
            m "Sure... That will speed things up, I'm telling you."
            call her_main("*sigh!*..............", "open", "narrow", "worried", "down")
            call her_main("Well, I might as well, I suppose...")

            call nar(">Hermione gives the tip of your engorged cock a tender kiss.")

            $ renpy.play('sounds/kiss.mp3')
            call her_chibi_scene("hj_kiss", trans=kissiris)
            pause 1

            if hg_kiss.trigger == False:
                $ achievement.unlock("herkiss")
                $ hg_pf_handjob.change_icon(a="heart_half", b="heart_red")
                call her_main("(It was my first kiss ever and I gave it away to a... cock...)", "disgust", "narrow", "worried", "down")
            $ hg_kiss.triggered() # .trigger = True, .counter += 1
            pause 2

            call her_chibi_scene("hj", trans=d5)
            pause.5

            call her_main("Like this?", "open", "narrow", "worried", "down")
            m "Wasn't that bad, was it?"
            call her_main("No, I suppose not...", "upset", "wink", "base", "mid")
            m "Can you do it again, then?"
            call her_main("I could...", "normal", "happyCl", "worried", "mid")
            m "Do it!"
            call her_main("Well, alright...", "open", "base", "base", "mid")

            $ renpy.play('sounds/kiss.mp3')
            call her_chibi_scene("hj_kiss", trans=kissiris)
            pause 3

            call nar(">Hermione gives your cock another kiss...")
            call ctc

            call nar(">This time she lingers a moment longer...")
            pause.5

            call her_chibi_scene("hj", trans=d5)
            pause.5

            m "Good... Now do it again and just stay there for a while."
            call her_main("You mean with my lips touching your... cock, [genie_name]?", "open", "base", "base", "mid")
            call her_main("No, I will look stupid...", "annoyed", "base", "worried", "R")
            m "Don't be silly, [hermione_name]. Nobody is watching."
            call her_main("You are, [genie_name].", "open", "narrow", "worried", "down")
            m "But that's the whole point!"
            call her_main("......", "annoyed", "narrow", "annoyed", "mid")
            m "It will make me cum in no time!"
            call her_main("...............", "annoyed", "narrow", "angry", "R")
            m "And then you can just get out and and take care of your business today."
            call her_main(".............", "disgust", "narrow", "base", "mid_soft")
            call her_main("Well, alright then...", "open", "narrow", "worried", "down")
            call nar(">Hermione reaches down with her lips again...","start")
            call nar(">She touches the tip of your cock with her lips and keeps them there...","end")

            $ renpy.play('sounds/kiss.mp3')
            call her_chibi_scene("hj_kiss", trans=kissiris)
            call ctc

            call bld
            m "Very good..."
            m "Now touch it with your tongue."
            call her_main("??!", "open_tongue", "closed", "base", "mid")
            m "That's the last thing I will be asking of you today."
            call her_main("............")
            call nar(">You feel the tip of Hermione's tongue warily rubbing against the head of your cock...")
            m "Yes, like this..."
            call nar(">Hermione wiggles her tongue a little...")
            call her_main("(It tastes weird...)", "disgust", "narrow", "worried", "down")
            m "Yes... Good..."

            call her_chibi_scene("hj", trans=d5)
            pause.8

            call her_main("So, did it work? Are you ready to... finish, [genie_name]?", "open", "narrow", "worried", "down")
            g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"

    menu:
        m "..."
        "-Give her a warning-":
            g4 "Here it comes, [hermione_name]! You better be ready!"
            call her_main("What? So soon?!", "shock", "wide", "base", "stare")
            g4 "{size=+5}Yeah, you did a great job!!!{/size}"
            g4 "{size=+5}You little whore!!!{/size}"
            call her_main("No, [genie_name], wait, I--", "angry", "base", "base", "mid")
            g4 "{size=+5}Too late for that, slut!{/size}"
            call her_main("*whimper*", "angry", "narrow", "base", "down")
            g4 "{size=+5}ARGH! YES!!!{/size}"
            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")

            stop music fadeout 1.0
            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.5

            call cum_block
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8

            show screen bld1
            if hermione.is_worn("top"):
                call nar(">Hermione suddenly slides your already dripping cock under her top...")
            else:
                call nar(">Hermione suddenly slides your already dripping cock in-between her breasts, your tip mere inches from her chin...")
            g4 "?!!"
            call nar(">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man.")
            call ctc

            call her_chibi_scene("hj_cum_in_done", trans=d5)

            call her_main(".......................", "angry", "wide", "base", "stare", xpos="right", ypos="base")
            m "..........................."
            call her_main(".......................", "angry", "wide", "base", "stare")
            m "....................?"
            call her_main(".......................", "angry", "narrow", "base", "down")
            m "... What the fuck just happened?"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("I don't know... I suppose I just panicked...", "angry", "happyCl", "worried", "mid", emote="sweat")

            if game.daytime:
                if hermione.is_worn("top"):
                    call her_main("My classes are about to start and I didn't want you to ruin my clothes, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
                    m "So you'll go to classes, looking like this?"
                    m "With your top all sperm-soaked from the inside?"
                else:
                    call her_main("My classes are about to start and I didn't want you to ruin my face, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
                    m "So you'll go to classes, looking like this?"
                    m "With your tits and chin all sperm-soaked?"
                call her_main("What choice do I have?", "angry", "narrow", "base", "down")
                call her_main("I can't just skip a class...")
            else:
                call her_main("At this hour The Gryffindor common room will be full of people...", "angry", "happyCl", "worried", "mid", emote="sweat")
                call her_main("I didn't want to have to return there all covered in your... spunk, [genie_name].")
                call her_main("Oh, it's getting pretty late...", "angry", "base", "base", "mid")
                m "So you will go to your dorm, looking like this?"

                if hermione.is_worn("top"):
                    m "With your top all sperm-soaked from the inside?"
                else:
                    m "With your tits and chin all sperm-soaked?"

                call her_main("What choice do I have?", "angry", "narrow", "base", "down")

            call ctc
            call blkfade

            ">Hermione releases your still pulsating cock."

            call her_chibi("stand","mid","base")
            call gen_chibi("stand","desk","base")
            hide screen bld1
            call hide_blkfade
            pause.5

            call her_main("*Eww*... Your sperm, [genie_name]...", "angry", "narrow", "base", "down")
            if hermione.is_worn("top"):
                call her_main("It's everywhere under my top...", "angry", "base", "base", "mid")
            else:
                call her_main("My breasts are so sticky, it's everywhere...", "angry", "base", "base", "mid")
            m "Just put it in your mouth next time."
            call her_main("I... don't think so, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
            call her_main("I really need to go. Can I just get paid now?")

        "-Just start cumming-":
            with hpunch
            g4 "ARGH!"
            call her_main("WHAT?!", "shock", "wide", "base", "stare")
            g4 "Take this!"

            call cum_block
            call her_chibi_scene("hj_cum_on", trans=d9)
            pause.8

            call cum_block
            $ hermione.set_cum(face="light")
            call bld
            g4 "{size=+5}*ARGH*! YES!!!{/size}"
            pause 1.0
            $ hermione.set_cum(breasts="light", body="light")
            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")

            call her_chibi_scene("hj_cum_on_done", trans=d5)
            call ctc



            call her_main(".......................", "angry", "wide", "base", "stare", xpos="right", ypos="base")
            m "Yes... I Feel so much better now..."
            call hide_characters
            show screen blkfade
            with d5

            call her_chibi("stand","mid","base")
            call gen_chibi("stand","desk","base")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            call her_main("..................", "disgust", "narrow", "worried", "down", tears="soft")
            m "Well, I think that's about it..."
            call her_main("[genie_name]! What have you done?!", "scream", "happyCl", "worried", "mid", trans=hpunch)
            m "What?"

            if d_flag_01: #If TRUE Genie promised to warn her.
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ her_mood += 11
                call her_main("You promised to give me a warning, [genie_name]!", "angry", "base", "angry", "mid")
                m "Oh, that's right... My bad."
                if hermione.is_worn("top"):
                    call her_main("My clothes are ruined...", "annoyed", "narrow", "angry", "R")
                else:
                    call her_main("My pretty face is ruined...", "annoyed", "narrow", "angry", "R")
                her "... I would like to get paid now."

            else:
                if game.daytime:
                    if hermione.is_worn("top"):
                        call her_main("My clothes are ruined now!", "annoyed", "narrow", "angry", "R")
                    else:
                        call her_main("I have cum on my face!", "annoyed", "narrow", "angry", "R")
                    call her_main("Classes are about to start and I can't go looking like this!", "open", "narrow", "worried", "down")
                    m "Of course you can, just wipe it off or something..."
                    m "Nobody will even notice."
                    call her_main("... I would like to get paid now.", "annoyed", "narrow", "annoyed", "mid")
                else:
                    if hermione.is_worn("top"):
                        call her_main("My clothes are ruined!", "annoyed", "narrow", "angry", "R")
                    else:
                        call her_main("I have cum on my face!", "annoyed", "narrow", "angry", "R")
                    her "Am I supposed to go back to the Gryffindor common room looking like this?!"
                    m "Why not? You look hot, [hermione_name]!"
                    call her_main("[genie_name]!!!", "annoyed", "narrow", "annoyed", "mid")
                    m "Alright, alright. Just wipe it off or something."
                    m "Nobody will even notice."
                    call her_main("... I would like to get paid now.", "annoyed", "narrow", "annoyed", "mid")

    jump end_hg_pf_handjob

### Third Handjob ###

label hg_pf_handjob_2:
    stop music fadeout 3.0
    call her_chibi_scene("hj", trans=fade)
    pause.8

    call her_main("Do you like it when I do it like this, [genie_name]?", "grin", "base", "base", "R", xpos="base", ypos="head")
    g9 "Actually, yes! Very nice!"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    with hpunch
    g4 "{size=+5}Yes, yes, like that...{/size}"
    m "*Hmm*... You are getting pretty good at this."
    call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
    call her_main("I figured the better I do this, the sooner it'll be over.")
    m "*Hmm*..."

    menu:
        m "..."
        "\"What do you think of my cock?\"":
            call her_main("*huh*?", "open", "base", "base", "mid")
            call her_main("Oh, that's right...")
            call her_main("I need to compliment your penis! I completely forgot about that!", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "Well, you don't have to--"
            call her_main("[genie_name], let me be honest with you...", "upset", "closed", "base", "mid")
            m "Yes?"
            call her_main("You have the biggest penis I have ever seen!", "smile", "base", "angry", "mid")
            m "Well I suppo--"
            call her_main("Not done yet!", "scream", "closed", "angry", "mid")
            m "Apologies."
            call her_main("Your penis is so big it almost scares me!", "angry", "narrow", "base", "down")
            g9 "You little minx. You know exactly what to say..."
            call her_main("And yet I lust for it...", "soft", "narrow", "annoyed", "up")
            call her_main("Any woman would be happy to have your huge penis inside of her!")
            m "... you're good!"
            call her_main("There is more!", "scream", "closed", "angry", "mid")
            m "By all means..."
            call her_main("I think your magnificent cock is a blessing to this world!", "scream", "closed", "angry", "mid")
            m "Well, I wouldn't go that far--"
            call her_main("Listen to me, [genie_name]!", "scream", "closed", "angry", "mid")
            call her_main("I think a statue dedicated to your magnificent penis shall be erected in every city!")
            call her_main("So that people of the world could worship your phallus freely!")
            m "OK, I think I've heard enough."
            call her_main("Too much?", "angry", "wink", "base", "mid")
            m "Yeah, just a bit."
            call her_main("Sorry...", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "No biggie. Just keep on stroking it."
            call her_main(".................", "soft", "narrow", "annoyed", "up")
            call nar(">Hermione keeps on stroking your cock.","start")
            call nar(">She is doing a great job of it too.","end")
            m "Yes, yes... just like that."

        "\"Call yourself a whore!\"":
            call her_main("Excuse me?", "open", "base", "base", "mid")
            call her_main("Oh, that's right! I'm supposed to degrade myself, right?", "annoyed", "squint", "base", "mid")
            m "Well, you don't have to, but..."
            call her_main("That's alright, I don't mind.", "upset", "closed", "base", "mid")
            call her_main("Alright then! I am a whore!", "base", "base", "base", "mid")
            m "Good. Glad we established that."
            m "Now I want you to say..."

            menu:
                m "..."
                "\"I am a worthless slut!\"":
                    call her_main("Of course.", "angry", "wink", "base", "mid")
                    call her_main("I am a worthless slut.", "soft", "narrow", "annoyed", "up")
                    call her_main("A dirty little slut, that's what I am.")
                    m "Yes! Good!"
                "\"I live to suck cock!\"":
                    call her_main("*Ehm*...", "angry", "wink", "base", "mid")
                    call her_main("I live to suck penis, er... I mean cock...", "base", "base", "base", "mid")
                    m "Really? Well why don't you suck on this one then?"
                    call her_main("[genie_name], I am just repeating after you...", "smile", "base", "angry", "mid")
                    m "Really? Could've fooled me..."
                    call her_main("....................", "angry", "wink", "base", "mid")
                    m ".................."
                "\"I love to swallow cum!\"":
                    call her_main("I love to... *Ehm*... swallow cum.", "angry", "wink", "base", "mid")
                    m "You hesitated there for a moment."
                    call her_main("Yes, I know...", "angry", "wink", "base", "mid")
                    call her_main("Let me try again...")
                    call her_main("I love to swallow cum!", "soft", "narrow", "annoyed", "up")
                    call her_main("It is truly the best to swallow cum!")
                    call her_main("I love it!")
                    call her_main("...................................", "grin", "narrow", "base", "dead")
                    call her_main("How was that, [genie_name]?", "angry", "wink", "base", "mid")
                    m "Perfect."

        "\"This is really good. Did you practise?\"":
            call her_main("*Hmm*?", "base", "happyCl", "base", "mid")
            call her_main("Sort of... Well not really...")
            call her_main("I had a talk with the girls, and...", "angry", "wink", "base", "mid")
            m "About handjobs?"
            call her_main("Among other things...", "smile", "happyCl", "base", "mid", emote="happy")
            m "So those girls of yours, they know a lot about such things?"
            call her_main("Actually, yes. I was surprised myself.", "shock", "wide", "base", "stare")
            call her_main("All sorts of weird sexual things seem to be happening in our school lately...", "grin", "base", "base", "R")
            call her_main("Can't say I approve of that...")
            call her_main("But they did teach me quite a few... tricks.", "base", "happyCl", "base", "mid")
            m "Really? Like what?"
            call her_main("Well, let's see...", "base", "narrow", "worried", "down")
            call her_main("If I put one of my hands here...")
            call her_main("And another one here...")
            m "Oh, I see... Yes, this feels quite good."
            call her_main("Does it?", "angry", "wink", "base", "mid")
            call her_main("So Ginny was right about this one...", "grin", "base", "base", "R")
            g4 "What did you just say?"
            call her_main("Ginny Weasley, she taught me this one.", "base", "happyCl", "base", "mid")
            m "Oh, right..."
            call her_main("She said any boy would fall in love with me if I did this to him...", "base", "narrow", "worried", "down")
            call her_main("There is also this thing when I form a ring with my fingers...")
            call her_main("And then I put one finger here...")
            m "*Hmm*... I don't feel anything..."
            call her_main("Really?", "angry", "narrow", "base", "down")
            call her_main("*Hmm*...")
            call her_main("Oh! That's right!", "base", "narrow", "worried", "down")
            call her_main("The finger goes here! Silly me!")
            with hpunch
            with kissiris
            g4 "Oh!!! By the great desert sands, yes!"
            call her_main("Really? That good?", "smile", "happyCl", "base", "mid", emote="happy")
            call her_main("What if I keep doing this but stick my finger here and press a little...", "base", "narrow", "worried", "down")
            g4 "[hermione_name], you are killing me!"
            call her_main("Really? Really?!", "smile", "happyCl", "base", "mid", emote="happy")
            call her_main("This is actually quite fun!")
            call her_main("Err... I mean...", "angry", "wink", "base", "mid")
            call her_main("I am only doing this to help my house of course...")
            m "Yes, yes... The Gryffindor honour and all that."
            m "You just keep massaging that spot..."
            m "Oh, yes..."
            call her_main("...............", "base", "narrow", "worried", "down")

    m "Yes... Keep stroking it."
    call her_main("..............", "angry", "wink", "base", "mid")

    if hg_pf_handjob.points == 1:
        jump hg_pf_handjob_2_cumming
    else:
        jump hg_pf_handjob_2_continue


label hg_pf_handjob_2_continue:
    call her_chibi_scene("hj", trans=d5)
    call ctc

    call bld
    m "Now I want you to say..."

    menu:
        m "..."
        "{size=-4}\"I fantasise about being touched by my father.\"{/size}":
            $ her_mood += 11
            call her_main("I do not!", "angry", "base", "angry", "mid")
            m "I know. Just say it."
            call her_main("My father? That's disgusting, [genie_name]!", "angry", "base", "angry", "mid", emote="angry")
            m "Humour me."
            call her_main("...........", "annoyed", "narrow", "annoyed", "mid")
            call her_main("Well...", "open", "narrow", "worried", "down")
            call her_main("Sometimes I fantasise about my father...")
            call her_main(".......")
            m "I see. And in those fantasies of yours..."
            m "He is touching you, right?"
            call her_main("My father...?", "angry", "base", "base", "mid")
            m "Yes... And you enjoy it, right?"
            call her_main("No. I cry and beg for him to stop!", "angry", "narrow", "base", "down")
            m "Heh... Nice."
            call her_main(".......", "angry", "narrow", "base", "down")
            m "Well, this wasn't that hard, was--"
            call her_main("I scream for my Mommy but she is still at work...", "mad", "base", "worried", "mid", tears="soft")
            m "*huh*?"
            call her_main("My daddy takes me to my room...", "normal", "happyCl", "worried", "mid")
            call her_main("He throws me on my bed!")
            call her_main("I cry \"No, daddy, please, I'm still a virgin!\"", "scream", "happyCl", "worried", "mid")

            call her_chibi_scene("hj_pause", trans=d5)
            pause.5

            call her_main("But He doesn't listen! He rips my panties off!", "grin", "narrow", "base", "dead")
            call her_main("I beg him to stop! I scream and I scream!", "angry", "base", "base", "mid", tears="soft")
            m "*Err*, [hermione_name]?"
            call her_main("Yes?", "angry", "base", "base", "mid", tears="soft")
            m "You are not stroking my cock anymore..."
            call her_main("Oh, I am sorry, [genie_name].", "grin", "happyCl", "worried", "mid", emote="sweat")
            call her_main("I got lost in thought...")

            call her_chibi_scene("hj", trans=d5)
            pause.5

            call her_main("But everything I just said is not true of course!", "open", "base", "base", "mid")
            call her_main("I never have fantasies like that!")
            m "Right."

        "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
            call her_main("What?!", "angry", "wide", "base", "stare")
            call her_main("That's disgusting.", "annoyed", "squint", "base", "mid")
            call her_main("Dogs carry {size=+5}STD{/size}s, [genie_name].", "open", "closed", "base", "mid")
            m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
            m "Meaning... They can only be spread to the same species."
            call her_main("............{size=-6}I knew that{/size}", "open", "squint", "base", "mid")
            g9 "Heh. Of course you would."
            m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
            call her_main("What does getting \"knotted\" mean?", "normal", "squint", "angry", "mid")
            m "*Ehm*... Well..."
            m "Ah, it doesn't matter."
            m "Just say the thing!"
            call her_main("Fine!", "normal", "base", "base", "mid")
            call her_main("Sometimes I get lonely and let my dog mount me.", "open", "squint", "base", "mid")
            m "That sounded so fake..."
            call her_main("Because we don't even own a dog!", "normal", "squint", "angry", "mid")
            m "Fine, whatever, let's just move on then..."

        "{size=-4}\"-Manual user input-\"{/size}" if not renpy.android:

            # The phrase in the brackets is the text that the game will display to prompt
            # the player to enter the name they've chosen.

            $ tmp_name = renpy.input("(Use keyboard to enter the phrase.)")
            $ tmp_name = tmp_name.strip()
            # The .strip() instruction removes any extra spaces the player may have typed by accident.
            #  If the player can't be bothered to choose a name, then we
            #  choose a suitable one for them:
            if tmp_name == "":
                $ tmp_name="I'm a whore"
                m "(...)"
                call her_main("I could just call myself a \"Whore\" again, as usual...", "annoyed", "base", "worried", "R")
                m "Yes. A great suggestion."
                call her_main("...............", "annoyed", "base", "base", "R")
                call her_main("[tmp_name]", "base", "base", "base", "mid")
                m "A bit louder..."
                call her_main("[tmp_name]!!!", "scream", "closed", "angry", "mid")
            elif one_of_three == 1:
                call her_main("I don't want to say that...", "annoyed", "base", "worried", "R")
                m "Oh, just do it, [hermione_name]."
                call her_main("...........", "annoyed", "base", "worried", "R")
                call her_main("[tmp_name]", "scream", "closed", "angry", "mid")
            elif one_of_three == 2:
                call her_main("*huh*?", "annoyed", "base", "worried", "R")
                call her_main("What does That have to do with anything?")
                m "Just say it."
                call her_main("......", "annoyed", "base", "worried", "R")
                m "Come on, humour me."
                call her_main("[tmp_name]", "scream", "closed", "angry", "mid")
            elif one_of_three == 3:
                call her_main("...........", "annoyed", "base", "worried", "R")
                call her_main("Do I really have to?")
                m "Just say it."
                call her_main("[tmp_name]", "scream", "closed", "angry", "mid")
            g9 "He-he..."

        "{size=-4}\"-Manual user input-\"{/size}" if renpy.android:
            if one_of_three == 1:
                call her_main("I don't want to say that...", "annoyed", "base", "worried", "R")
                m "Oh, just do it, [hermione_name]."
                call her_main("...........", "annoyed", "base", "worried", "R")
                call her_main("Manual user input...", "scream", "closed", "angry", "mid")
            elif one_of_three == 2:
                call her_main("*huh*?", "annoyed", "base", "worried", "R")
                call her_main("What does That have to do with anything?")
                m "Just say it."
                call her_main("......", "annoyed", "base", "worried", "R")
                m "Come on, humour me."
                call her_main("... Manual user input.", "scream", "closed", "angry", "mid")
            elif one_of_three == 3:
                call her_main("...........", "annoyed", "base", "worried", "R")
                call her_main("Do I really have to?")
                m "Just say it."
                call her_main("Manual user input.", "scream", "closed", "angry", "mid")
            g9 "He-he..."

    jump hg_pf_handjob_2_cumming

label hg_pf_handjob_2_cumming:
    call her_chibi_scene("hj", trans=d5)
    pause.8

    call bld
    m "*Hmm*..."
    m "I love that thing you do with the palm of your hand!"
    call her_main("You noticed...?", "angry", "wink", "base", "mid")
    call her_main("Shall I do it some more then?")

    call nar(">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently...")
    m "Oh yes!!!"

    stop music fadeout 1.0
    g4 "{size=-5}(I think this is it! Should I give her a warning?){/size}"

    menu:
        m "..."
        "\"(Yes, I must warn her.)\"":
            g4 "I think I'm about to--"
            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.8

            if hermione.is_worn("top"):
                call nar(">Hermione swiftly pulls her top up...","start")
                ">She then pushes your already dribbling cock against her belly and covers it up again, placing your cock a bit higher than you would have expected..."
            else:
                call nar(">She pushes your already dribbling cock against her belly, placing your cock a bit higher than you would have expected...","start")
            call nar(">You can feel her incredibly soft tits rubbing against the tip of your cock...","end")

            call cum_block
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8

            call bld
            g4 "{size=+5}ARGH! YES!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare", ypos="head")
            hide screen bld1
            call ctc

            call cum_block
            $ hermione.set_cum(breasts="light", body="light")
            g4 "*Argh*! You whore!"
            call nar(">The sensation of her skin under your engorged cock almost makes you lightheaded...")
            call her_main("Yes, [genie_name]! Just let it out!", "base", "narrow", "worried", "down", xpos="right", ypos="base")
            $ hermione.set_cum(breasts="heavy", face="light")
            g4 "*Argh*! Fucking slut!"
            call her_main("Ah!! It's so hot!", "smile", "narrow", "base", "mid_soft")
            call her_main("And it's getting everywhere! So much of it!", "soft", "narrow", "annoyed", "up")
            call her_main("...[genie_name].")
            $ hermione.set_cum(body="heavy")
            g4 "*Argh*!!!"
            m "............"
            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.8

            call bld
            m "I think I am done..."
            call her_main("Ah, alright...", "angry", "wink", "base", "mid")
            call her_main("..............", "base", "narrow", "worried", "down")
            call her_main("You came so much this time, [genie_name]...", "soft", "narrow", "annoyed", "up")
            call ctc

            call hide_characters
            show screen blkfade
            with d5

            ">Hermione releases your still pulsating cock."

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            if game.daytime:
                call her_main("Well, I think I'd better go now... my Classes are about to start.", "base", "base", "base", "mid", xpos="right", ypos="base")
            else:
                call her_main("Well, I think I'd better go now... It's getting late.", "base", "base", "base", "mid", xpos="right", ypos="base")

            if hermione.is_worn("top"):
                m "Will you be alright in those clothes?"
            else:
                m "Will you be alright with this much cum on you?"
            call her_main("What?", "open", "narrow", "worried", "down")
            call her_main("Oh. Yes, I will be fine...", "grin", "base", "base", "R")
            if hermione.is_worn("top"):
                call her_main("It may soak through a little here and there, but I doubt that anyone will notice.", "base", "happyCl", "base", "mid")
            else:
                call her_main("It may soak through a little here and there, but I doubt that anyone will notice if I wear a robe.", "base", "happyCl", "base", "mid")
            m "*Hmm*... You could just put it in your mouth next time, and avoid the trouble..."
            call her_main("And swallow your hot spunk like that, [genie_name]?", "angry", "wink", "base", "mid")
            if hermione.is_worn("top"):
                m "Would keep your clothes clean."
            else:
                m "Would keep your sweet tits clean."

            if hg_blowjob.trigger == False: # Hasn't done blowjobs yet.
                call her_main("With all due respect [genie_name]...", "upset", "closed", "base", "mid")
                call her_main("Not for the meagre {number=current_payout} points...", "angry", "wink", "base", "mid")
                call her_main("Speaking of which. Can I get may payment now please?")
            else:
                call her_main("Maybe next time...", "angry", "wink", "base", "mid")
                call her_main("Can I get may payment now please?", "angry", "wink", "base", "mid")

        "\"(Nah... no need.)\"":
            g4 "Here! Take this, whore!"

            call cum_block
            $ hermione.set_cum(face="light")
            call her_chibi_scene("hj_cum_on", trans=d5)
            pause.8
            g4 "*ARGH*!"
            $ hermione.set_cum(breasts="light", body="light")

            call her_main("WHAT?!", "shock", "wide", "base", "stare", ypos="head")
            g4 "Take this!"

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            g4 "{size=+5}*ARGH*! YES!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")
            hide screen bld1
            call ctc

            call her_main(".......................", "angry", "wide", "base", "stare")

            call her_chibi_scene("hj_cum_on_done", trans=d5)
            pause.8

            call bld
            m "Yes... I Feel so much better now..."

            call her_chibi("stand","mid","base")
            call gen_chibi("stand","desk","base")

            call her_main("", "soft", "base", "base", "mid", tears="soft", xpos="right", ypos="base")
            with fade
            call ctc

            her ".........."
            m "Well, I think that's about it..."

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("[genie_name]! What have you done?", "scream", "happyCl", "worried", "mid")
            m "What?"
            call her_main("You came all over me, [genie_name]...", "scream", "happyCl", "worried", "mid")
            call her_main("What a mess...", "angry", "narrow", "base", "down")
            call her_main("[genie_name], you should have warned me.", "upset", "closed", "base", "mid")
            m "It's your fault, [hermione_name]!"
            call her_main("My fault?", "angry", "base", "base", "mid")
            m "Yes! You got me going too well..."
            m "I forgot about everything else..."
            call her_main("Oh...", "angry", "wink", "base", "mid")
            her "Well, what's done is done..."
            if hermione.is_worn("top"):
                call her_main("I will just wipe it off and hope that nobody will notice...", "grin", "narrow", "base", "dead")
            else:
                call her_main("I will just wipe the worst off and wear a robe, I hope that nobody will notice...", "grin", "narrow", "base", "dead")
            call her_main("Can I get my payment now?", "angry", "wink", "base", "mid")

        "-Cum in her mouth!-" if hg_blowjob.trigger == True: # Has done blowjobs already.
            call bld
            m "Open your mouth, [hermione_name]!"
            call her_main("What?!", "open", "wide", "base", "stare", ypos="head")
            if hermione.is_worn("top"):
                g4 "Open your mouth, or I'll have to cover your clothes!"
            else:
                g4 "Open your mouth, or I'll have to cover your tits!"
            call her_main(".....................", "upset", "happyCl", "worried", "mid")

            call her_chibi_scene("hj_kiss", trans=kissiris)
            pause.8

            call nar(">Hermione swiftly puts the tip of your cock on her lips, as if to give it a kiss...","start")
            call nar(">The simple gesture makes your dick practically explode with pleasure and waves of cum.","end")

            call cum_block
            g4 "{size=+5}*ARGH*! YES!!!{/size}"
            call her_main("*Gulp!-Gulp!-Gulp*!", "full", "wide", "base", "stare")

            call cum_block
            g4 "*Argh*! You little whore!"
            g4 "Yes, you slut! Drink my cum! Drink all of it!"
            call her_main("*Gulp!-Gulp!-Gulp*!", "full_cum", "base", "worried", "mid")
            g4 "*Argh*... Yes!"
            call nar(">You notice that Hermione is barely able to keep up with the amount of hot cum your cock is pumping into her mouth.")
            call her_main("*Gulp!-Gulp!-Gulp*!", "full_cum", "happyCl", "worried", "mid")
            g4 "*Ahh*..."
            g4 "This feels great..."
            call her_main("*Gulp*! *Gulp*! *Gulp*!", "full_cum", "narrow", "annoyed", "up")
            m "I think that's it, [hermione_name]..."
            m "You can let go now..."
            m "...[hermione_name]?"

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")

            call her_main("", "full_cum", "narrow", "base", "dead", xpos="right", ypos="base", trans=fade)
            call ctc

            her "........................................."
            call her_main("*GULP*!!!", "cum", "happyCl", "worried", "mid")
            call her_main("*Gu-ah-a*...", "open_wide_tongue", "narrow", "base", "down")
            call her_main("I swallowed it all, [genie_name]!", "grin", "narrow", "base", "dead")
            m "Good girl..."
            call her_main("At one point I thought I was going to choke...", "open", "narrow", "base", "dead")
            call her_main("There was so much of it...", "soft", "narrow", "base", "dead")
            if hermione.is_worn("top"):
                m "Well, the deed is done, and your clothes are perfectly clean."
            else:
                m "Well, the deed is done, and your tits are perfectly clean."
            call her_main("Yes! I know! It's so much easier this way!", "base", "narrow", "worried", "down")

            if game.daytime:
                call her_main("I can just go to classes now as if nothing ever happened.", "angry", "wink", "base", "mid")
            else:
                call her_main("I can just go and spend some time with the guys in the common room now and nobody will know...", "base", "narrow", "worried", "down")

            m "Yes... With your belly full of semen..."
            call her_main("[genie_name]!", "angry", "base", "base", "mid")
            her "... Can I just get paid now, please, [genie_name]?"

    jump end_hg_pf_handjob
