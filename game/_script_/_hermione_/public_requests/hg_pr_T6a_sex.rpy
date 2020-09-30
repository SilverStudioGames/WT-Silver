
### Have Sex With A Classmate ###

label hg_pr_sex:

    # Setup
    $ current_payout = 75

    if hg_pr_sex.counter == 0:
        m "{size=-4}(Tell her to fuck one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)

    #Intro.
    if hg_pr_sex.counter == 0:
        m "[hermione_name]..."
        m "Today I need you to have sex with a classmate of your choice."

        if not hg_sex.trigger: # She will refuse unless she slept with you
            call her_main("But we--.. I..", "shock", "wide", "base", "stare")
            call her_main("I've never done it before!", "angry", "wide", "base", "mid")
            m "So?"
            call her_main("{size=+5}\"So\"?!{/size}", "annoyed", "narrow", "angry", "R")
            call her_main("I'm leaving this instant.", "scream", "closed", "angry", "mid")

            call her_walk(action="leave")

            $ her_mood += 16

            m "(*Hmm*...)"
            m "(Maybe if I have popped her cherry first, she would be more willing...)"

            jump end_hermione_event

        if her_reputation < 18:
            jump too_much_public

        call play_music("hermione") # Music
        call her_main("..............", "angry", "base", "angry", "mid")
        call her_main("I had the feeling that we would get to this sooner or later...", "disgust", "narrow", "base", "mid_soft")
        call her_main("But...", "annoyed", "narrow", "angry", "R")
        her "..................."
        m "If you do this, Gryffindor will be getting {number=current_payout} points tonight."
        call her_main("Well, then I will do it, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
        m "Great. See you after your classes then."
        call her_main(".............", "upset", "closed", "base", "mid")
    else:
        m "[hermione_name]..."
        m "I need you to go have sex with another classmate of yours."
        call her_main("Again, [genie_name]?", "angry", "base", "base", "mid")
        m "Yes. And you will get {number=current_payout} points again as well."
        call her_main("Well, alright...", "annoyed", "narrow", "annoyed", "mid")

    call her_walk(action="leave")

    $ hg_pr_sex.inProgress = True

    jump end_hermione_event

label end_hg_pr_sex:
    $ gryffindor += current_payout
    m "Gryffindor gets {number=current_payout} points!"
    her "Thank you, [genie_name]."
    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_sex.counter == 2:
        show screen blktone
        with d3

        call her_main("(I did it... finally did it.)", "smile", "narrow", "base", "dead", flip=True, trans=d3)

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_sex.inProgress = False

    # Increase Points

    if her_tier == 6:
        if her_reputation < 24:
            $ her_reputation += 1

        if her_whoring < 24:
            $ her_whoring += 1

    jump end_hermione_event

label hg_pr_sex_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you do it?"

    if hg_pr_sex.is_tier_complete():
        her "Of course, [genie_name]."
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_sex

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_sex.counter == 1:
        call her_main("......", "base", "narrow", "base", "mid")

    m "Have you enjoyed yourself?"

    return

### Tier 6 ###

label hg_pr_sex_T6_intro_E1:

    call bld
    m "....."
    m ".........."
    m "She was supposed to be here, by now..."
    m "*Hmm*..."

    $ hg_pr_sex.inProgress = False
    $ hermione_busy = True
    $ hg_pr_sex_skip = True

    # Next Morning.
    jump day_start

label hg_pr_sex_T6_intro_E2:
    $ hg_pr_sex_skip = False

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    m "[hermione_name], you missed your debriefing yesterday."
    m "Explain yourself."
    call play_music("hermione") # Music
    call her_main("Yes, [genie_name], I apologise... *yawn*...", "open", "closed", "base", "mid", xpos="mid", ypos="base", trans=d3)
    m "Care to explain yourself?"
    call her_main("Of course, [genie_name].", "open", "happy", "base", "mid", cheeks="blush")
    call her_main("It is sort of embarrassing, though...", "base", "base", "base", "R", cheeks="blush")
    call her_main("I spent the last night with two of my friends...", "open", "happy", "base", "mid", cheeks="blush")
    m "A slumber party with some girlfriends, *huh*?"
    call her_main("Girlfriends?", "angry", "wink", "base", "mid")
    call her_main("No, [genie_name]. Harry and Ron are boys...", "open", "base", "base", "R", cheeks="blush")
    m "*Hmm*..."
    call her_main("Yes, we were best friends for such a long time...", "base", "base", "base", "R", cheeks="blush")
    call play_music("playful_tension") # Music
    call her_main("But last night the boys made me their little plaything...", "base", "narrow", "base", "mid_soft")
    call her_main("And I did not mind it one bit...", "grin", "narrow", "base", "dead")
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    call her_main(".................", "soft", "narrow", "annoyed", "up")
    call her_main("Will I get paid for this, [genie_name]?", "angry", "wink", "base", "mid")

    jump end_hg_pr_sex

label hg_pr_sex_T6_E3:

    call hg_pr_sex_intro

    call play_music("hermione") # Music
    call her_main("Yes I did, [genie_name].", "upset", "closed", "base", "mid")
    call her_main("And in the school library of all places...", "open", "narrow", "annoyed", "mid", cheeks="blush")
    her "At first I was kind of worried that we would make too much noise..."
    her "But the boy literally lasted only one minute, [genie_name]."
    m "Don't hold it against him, [hermione_name]."
    m "You are quite attractive, he probably got too excited..."
    call her_main("Nevertheless...", "upset", "closed", "base", "mid")
    her "A dozen or so of rather gingerly thrusts and he is cumming already?"
    her "As a girl, I cannot help but feel disappointed..."
    m "I see..."
    m "What did you do afterwards?"
    m "Pulled up your panties and went about your business as if nothing happened?"


    call her_main("My panties?", "open", "narrow", "worried", "down")
    call her_main("I rarely bother to wear them anymore, [genie_name].", "annoyed", "narrow", "angry", "R")

    if hermione.is_worn("panties"):
        her "Unless you ask me to wear them, [genie_name]."

    m "Oh really?"
    call her_main("Yes... I find not wearing any underwear very empowering.", "annoyed", "narrow", "annoyed", "mid")

    if hermione.is_worn("panties"):
        her "But if that's what makes you happy, so be it."

    m "Good for you, [hermione_name]."

    jump end_hg_pr_sex

label hg_pr_sex_T6_E4:

    call hg_pr_sex_intro

    call play_music("playful_tension") # Music
    call her_main("I did, [genie_name].", "upset", "closed", "base", "mid")
    call her_main("I took one of the Ravenclaw boys to the girl's restroom...", "base", "narrow", "worried", "down")
    her "... and let him have his way with me in one of the stalls."
    m "Well done, [hermione_name]."
    call her_main(".....................", "annoyed", "narrow", "angry", "R")
    m "I said you did great. What's the matter?"
    call her_main("*Ehm*... well...", "open", "base", "base", "R", cheeks="blush")
    her "I am getting paid well for performing such tasks..."
    her "So I have no right to complain, but..."
    m "*Hmm*...?"
    call her_main("My reputation is starting to suffer and it troubles me, [genie_name]...", "open", "base", "base", "mid", cheeks="blush")
    m "Your reputation?"
    call her_main("Well, yes... *ehm*...", "open", "base", "base", "R", cheeks="blush")
    m ".............."
    call her_main("No, sorry, please disregard what I just said, [genie_name].", "upset", "closed", "base", "mid")
    m "(At this point I'm not sure she has any reputation left.)"

    jump end_hg_pr_sex
