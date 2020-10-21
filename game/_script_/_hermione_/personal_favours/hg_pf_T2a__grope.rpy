

### Hermione Groping ###

label hg_pf_grope:

    m "{size=-4}(I will grope her a little. Pretty harmless stuff.){/size}"

    if hg_pf_grope.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 15
    $ hg_pf_grope.start()


    # End Event
    label end_hg_pf_grope:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    ">You let go of Hermione..."

    $ hermione.wear("all")
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    m "This will do for now."
    if her_tier <= 3:
        call her_main("................", "annoyed", "narrow", "angry", "R", cheeks="blush")
    else:
        call her_main("................", face="horny", cheeks="blush")


    # Points
    if her_tier <= 5:
        $ gryffindor += current_payout
        m "The Gryffindor house gets {number=current_payout} points!"
    else:
        m "You may leave now, [hermione_name]."

    if her_tier <= 2:
        call her_main("..................", "annoyed", "base", "worried", "R")
        her "Thank you, [genie_name]..."
    elif her_tier <= 4:
        call her_main("..................", "base", "base", "base", "R")
        call her_main("Thank you, [genie_name]...", "soft", "base", "base", "mid")
    else:
        call her_main("..................", "soft", "narrow", "annoyed", "up")
        call her_main("Thank you, [genie_name]...", "soft", "narrow", "base", "mid_soft")

    if game.daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."

    # Hermione leaves
    call her_walk("door", "base")

    if her_tier > 5:
        call her_main("(What about my points?)", "disgust", "narrow", "base", "down", cheeks="blush", xpos="base", flip=True)
        if her_whoring < 24:
            call her_main("(I'll just ask him about it next time...)", "annoyed", "narrow", "angry", "R")
        else:
            call her_main("(Eh, who cares...)", "base", "narrow", "base", "up", cheeks="blush")
        pause.5

    call her_chibi("leave")


    # Increase level
    if her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    jump end_hermione_event

### Tier 1 - Events Fail ###

# Those events still prgress, but Hermione will run off and get mad.
# The heart icons for these events are 'black'

label hg_pf_grope_T1_fail_intro:
    m "[hermione_name], would you mind if I play with your tits a little?"
    call her_main("Play with...?", "shock", "wide", "base", "stare")
    call her_main("My tits?!", "angry", "wide", "base", "mid")
    g9 "Or your butt! I haven't fully decided yet!"

    $ hg_pf_grope.fail()

    jump too_much

label hg_pf_grope_T1_fail_repeat:
    g9 "[hermione_name], I'd like to grope you a little!"
    call her_main("This again...?", "angry", "base", "angry", "mid")
    call her_main("I've told you before, [genie_name], absolutely not!!", "scream", "closed", "angry", "mid")
    call her_main("By Merlin's beard...", "angry", "base", "angry", "mid")
    m "Please?"
    call her_main("I'm leaving! Good day, Sir!", "soft", "closed", "base", "mid")

    call her_walk(action="leave")

    $ her_mood += 6

    $ hg_pf_grope.fail()

    jump end_hermione_event

### Tier 2 ###

# Event 1 (i) - Hermione is shocked about you groping her.
# Event 2 (i) - Hermione is still shocked.

label hg_pf_grope_T2_intro_E1:
    stop music fadeout 2.0
    m "Come closer [hermione_name]... Hop around my desk..."
    call her_main("*Ehm*... very well, Sir.", "disgust", "narrow", "base", "down")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    call her_main("[genie_name].....?", "annoyed", "base", "worried", "R", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("What? What do you mean, [genie_name]--", "soft", "wide", "base", "stare")
            call nar(">You reach out swiftly and grab both of her tits through her clothes...")

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand on her butt cheeks...")

            jump hg_pf_grope_ass_T2

label hg_pf_grope_T2_E1:
    stop music fadeout 2.0
    m "Come closer [hermione_name]... Hop around my desk..."
    call her_main("...............", "annoyed", "base", "angry", "mid")

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("[genie_name].....?", "annoyed", "narrow", "angry", "R", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("!!!", "soft", "wide", "worried", "shocked")
            call her_main("S-Sir?!", "disgust", "happyCl", "worried", "mid")
            call nar(">You reach out swiftly and grab both of her tits through her clothes...")

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand on her butt cheeks...")

            jump hg_pf_grope_ass_T2

### Tier 3 ###

# Event 1 (i) - Hermione tries to talk you out of it.
# Event 2 (i) - Hermione is indignant.

label hg_pf_grope_T3_intro_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "How would you like to earn some house points today?"
    call her_main("And what would I need to do to earn them?", "annoyed", "narrow", "annoyed", "mid")
    m "Oh nothing too out of the ordinary."
    m "You just stand here while I grope you for a bit..."
    call her_main("[genie_name]... I'd prefer it if you wouldn't make me such offers...", "annoyed", "narrow", "annoyed", "mid")
    m "Why? Too hard to resist?"
    her "Nothing like that, [genie_name]."
    m "Well, how about you come closer and bare your tits for me...?"
    g9 "I feel like playing with them a little..."
    call her_main("!!!", "open", "base", "base", "mid")
    m "Or your butt..."
    g9 "I'd like to give it a good squeeze."

    call her_main("[genie_name]! Don't you think this is too much?", "disgust", "narrow", "base", "mid_soft")
    m "You think?"
    her "I am not one of those harlots from Slytherin, you know..."
    m "I know... You are from {i}Gryfonmon{/i}... or something..." #<- GRYFFINDOR MISSPELLED ON PURPOSE
    call her_main("And if I don't feel like it, I don't have to sell you a single favour, [genie_name]!", "annoyed", "base", "worried", "R")
    m "Of course..."
    call her_main("...................", "annoyed", "narrow", "angry", "R")
    m "I'll give you {number=current_payout} house points for this."
    call her_main(".......................", "disgust", "narrow", "base", "mid_soft")
    her "All you are going to do is watch, [genie_name]?"
    m "Well, I feel more like touching, actually..."
    her "...................................."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("[genie_name].....?", "annoyed", "narrow", "angry", "R", ypos="head")
    m "..."

    menu:
        "\"I'm gonna play with your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("[genie_name].....?", "disgust", "happyCl", "worried", "mid")

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand on her butt cheeks...")

            jump hg_pf_grope_ass_T3

label hg_pf_grope_T3_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "How would you like to earn some house points today?"
    call her_main("And what would I need to do to earn them?", "annoyed", "narrow", "annoyed", "mid")
    g9 "Get squeezed!"
    call her_main("squeezed......?", "annoyed", "narrow", "angry", "R")
    m "Come here, I'll show you."

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("[genie_name].....?", "annoyed", "narrow", "angry", "R", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("[genie_name].....?", "disgust", "happyCl", "worried", "mid")

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand on her butt cheeks...")

            jump hg_pf_grope_ass_T3

### Tier 4 ###

# Event 1 (i) - Hermione ejoys it.
# Event 2 (i) - Hermione asks if you are going to grope her tits or her ass.
# Event 2 (i) - Hermione ejoys it.

label hg_pf_grope_T4_intro_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "Would you like to join me again?"
    g9 "Behind my desk."
    call her_main("Are you going to grope me again, [genie_name]?", "soft", "narrow", "base", "mid_soft")
    g9 "You just read my mind!"
    call her_main("...................", "disgust", "narrow", "base", "down")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("[genie_name].....?", "base", "narrow", "worried", "down", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("..........", "base", "narrow", "worried", "down")

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand on her butt cheeks...")
            jump hg_pf_grope_ass_T4

label hg_pf_grope_T4_intro_E2:
    m "[hermione_name]. Come here and join me..."
    g9 "I feel like playing with you a little."
    call her_main("Yes, Sir...", "soft", "base", "base", "R")

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("[genie_name].....?", "soft", "narrow", "worried", "down", ypos="head")
    m "Yes?"
    call her_main("Are you going to grope my breasts again?", "soft", "base", "base", "mid")
    call her_main("Or my bum?....", "soft", "narrow", "base", "mid_soft")
    m "*Hmm*..."

    menu:
        "\"I'm gonna play with your tits today.\"":
            call her_main("Of course, Sir.", "base", "narrow", "worried", "down")

            if not hermione.is_worn("top") and hermione.is_worn("bra"):
                call nar(">You reach out swiftly and grab both of her tits through her bra...")
            elif hermione.is_worn("top") and not hermione.is_worn("bra"):
                call nar(">You reach out swiftly and grab both of her tits through her clothes...")
            else:
                call nar(">You reach out swiftly and grab both of her tits...")

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt today.\"":
            call her_main("Of course, Sir.", "base", "narrow", "worried", "down")
            call nar(">You reach out and place your hand on her butt cheeks...")
            jump hg_pf_grope_ass_T4

label hg_pf_grope_T4_E2:
    g9 "[hermione_name]. Come here and let me grope you!"
    call her_main("Of course, [genie_name]...", "base", "narrow", "base", "mid_soft")

    call her_chibi_scene("behind_desk_front", trans=fade)

    call her_main("Are you going to grope my breasts today, Sir?", "soft", "narrow", "base", "R_soft", ypos="head")
    call her_main("Or my bum?....", "soft", "narrow", "base", "mid_soft")

    m "*Hmm*... What would you like?"
    if one_of_three == 1:
        call her_main("I wouldn't mind it if you massaged my breasts a little...", "soft", "narrow", "base", "R_soft")
    elif one_of_three == 2:
        call her_main("I wouldn't mind it if you caressed my bum a bit, Sir...", "soft", "narrow", "worried", "down")
    else:
        call her_main("I wouldn't mind either today, Sir.", "soft", "narrow", "base", "R_soft")

    m "Very well then..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("Yes, Sir.", "base", "narrow", "annoyed", "up")

            if not hermione.is_worn("top") and hermione.is_worn("bra"):
                call nar(">You reach out swiftly and grab both of her tits through her bra...")
            elif hermione.is_worn("top") and not hermione.is_worn("bra"):
                call nar(">You reach out swiftly and grab both of her tits through her clothes...")
            else:
                call nar(">You reach out swiftly and grab both of her tits...")

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt now.\"":
            call her_main("Yes, Sir.", "soft", "narrow", "annoyed", "up")
            call nar(">You reach out and place your hand on her butt cheeks...")

            jump hg_pf_grope_ass_T4
