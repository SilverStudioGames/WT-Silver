### Masturbate ###

### Tier 4 (Intro) ###

label hg_pf_strip_T4_fingering:
    if not hg_masturbated.trigger:
        $ hg_masturbated.triggered()

        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
        m "Do you ever touch yourself?"
        call her_main("What? why?", "upset", "wink", "base", "mid")
        m "It's a simple question [hermione_name]..."
        call her_main("[genie_name]!", "scream", "happyCl", "worried", "mid")
        m "And I want you to speak truthfully..."
        call her_main("......", "normal", "happyCl", "worried", "mid")
        m "Well, [hermione_name]?"
        call her_main("{size=-5}I suppose I do...{/size}", "angry", "happyCl", "worried", "mid", emote="sweat")
        m "*huh*? What was that?"
        call her_main("I said that I do alright!!!", "scream", "happyCl", "worried", "mid")
        m "*Hmm*... I'm not sure I believe you."
        call her_main("What? why would I lie?", "annoyed", "base", "worried", "R")
        m "I'm not sure... maybe it's because you think it's what I want you to say..."
        call her_main("That doesn't make any--", "annoyed", "base", "worried", "mid")
        m "But don't worry, I'm sure a quick little demonstration will erase any doubts..."
        call her_main("So that's what you're after......", "annoyed", "narrow", "angry", "R")
        call her_main("*Sigh*...{w=0.4} I suppose I could...", "open", "narrow", "worried", "down")
        call her_main("But you better keep your hands to yourself...", "angry", "narrow", "worried", "mid")
        m "Witcher's promise."
        call her_main("...", "annoyed", "squint", "base", "mid")
    else: # Repeat
        m "[hermione_name]."
        g9 "Why don't you give that lovely pussy of yours a little rub."
        call her_main("Again?", "annoyed", "narrow", "base", "mid")
        call her_main("...", "disgust", "narrow", "base", "down")
        call her_main("F-Fine... Just keep your hands to yourself...", "open", "squint", "base", "R")

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "upset", "base", "base", "mid")
    call her_main("Do you want me to... start?", "soft", "wink", "base", "mid")
    m "When you're ready..."

    if hermione.is_worn("panties"):
        m "But why don't we get rid of those panties first."

    call her_main("...........", "disgust", "narrow", "base", "down")

    if hermione.is_worn("panties"): # Rest of the clothes is taken off during stripping.
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0

    if hermione.is_any_worn("clothes"):
        m "Now take off the rest."
        $ hermione.strip("all")
        pause .5

    call her_main("(I never would've imagined... To do this in front of my headmaster of all people...)", "normal", "happyCl", "worried", "mid")

    $ hermione.set_pose("masturbate")
    $ hermione.set_body(armleft="on_pussy")
    call her_main("", "soft", "closed", "worried", "mid", trans=d3)

    $ renpy.play("sounds/slick_02.mp3")
    with hpunch
    pause 1.0
    play bg_sounds "sounds/slickloop.mp3" fadein 2
    call ctc

    g9 "Nice..."
    call her_main("........", "upset", "wink", "base", "mid")
    m "............."
    call her_main(".............", "normal", "happyCl", "worried", "mid")
    stop bg_sounds
    call her_main("*Umm*... [genie_name]?")
    m "Yes, what is it?"
    call her_main("For how long did you want me to do this?", "open", "base", "worried", "mid")
    m "Until you finish [hermione_name]..."

    if game.daytime:
        call her_main("But my classes are about to start, [genie_name]...", "annoyed", "base", "worried", "mid")
    else:
        call her_main("But it's getting late, [genie_name]...", "annoyed", "base", "worried", "mid")

    call her_main("I'm not sure if I'll be able to... finish... in time.", "disgust", "narrow", "base", "down")
    m "Do you need the points or not?"
    call her_main("I do, [genie_name]! I'm sorry...", "open", "narrow", "worried", "down")
    call her_main("I'll keep going then...", "disgust", "narrow", "base", "down")
    play bg_sounds "sounds/slickloop.mp3" fadein 2
    m "(*Hmm*... Maybe I should encourage her a little.)"

    menu:
        m "..."
        "\"Yes... keep going, slut.\"":
            call her_main("[genie_name]!!!", "angry", "base", "angry", "mid")
            call her_main("How...{w=0.4} How dare you!", "upset", "base", "angry", "mid")
            m "what?"
            call her_main("I hardly think that kind of... *Ah*...{w=0.5} language is appropriate.", "open", "happyCl", "base", "mid")
            m "And masturbating in front of your headmaster is?"
            call her_main("Well...{w=0.4} this...{w=0.4} this is different.", "open", "narrow", "worried", "down")
            call her_main("I'm doing this for the honour of Gryffindor...")
            call her_main("To help my--... *ah*", "open", "closed", "worried", "down")
            play bg_sounds "sounds/slickloopfast.mp3"
            call nar(">You notice Hermione beginning to move her fingers a little faster.")
            #
            # TODO: Add wet layer for panties/pussy
            #
            call her_main("ah...{heart}{heart}{heart}", "soft", "narrow", "annoyed", "up")
            call her_main("My classmates win the house cup...", "angry", "wink", "base", "mid")
            g9 "As if that's the only reason..."
            call her_main("I..{w=0.4}*Ah*... of course it...--", "normal", "happyCl", "worried", "mid")

            $ hermione.set_body_zorder(armright=3)
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            call her_main("ah-a{heart}...", "open", "happyCl", "worried", "mid")
            call her_main("What..{w=0.4}*Ah*... other reason would there be for me to...", "angry", "narrow", "base", "down")
            m "It seems to me that you might be enjoying this a little too much..."
            call her_main("I am not, [genie_name]!", "open", "happyCl", "worried", "mid")
            m "Really?"
            call her_main("......................", "normal", "happyCl", "worried", "mid")
            m "Then why are your fingers moving so fast, slut?"
            call ctc

            call her_main("ah...{heart}", "open", "happyCl", "worried", "mid")
            m "ha! just Admit it, you do enjoy being called a slut!"
            call her_main("I do not!", "normal", "happyCl", "worried", "mid")
            call her_main("I'm just thinking about...{w=0.4}*Ah*...{w=0.4} how happy everyone will be when we win!", "shock", "happyCl", "worried", "mid")
            m "And what if they find out how you earned the points?"
            stop bg_sounds
            call her_main("what?!", "shock", "wide", "base", "stare")
            m "Then it wouldn't just be me degrading you..."
            play bg_sounds "sounds/slickloop.mp3"
            call her_main("...", "soft", "closed", "base", "R")
            m "It would be the entire school."
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("The entire...*ah*...{heart}", "silly", "narrow", "base", "dead", cheeks="blush")
            m "Every...{w=0.4} single...{w=0.4} student."
            play bg_sounds "sounds/slickloopveryfast.mp3"
            call her_main("ah...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up", cheeks="blush")
            call her_main("[genie_name], please... {w=0.4}*mmmh*...{w=0.4} don't tell anyone...", "soft", "narrow", "base", "mid_soft", cheeks="blush")
            call nar(">Hermione continues to rub herself with even more effort...")
            call her_main("They can't...{w=0.4}*Ah*...{w=0.4} They can't find out...", "soft", "narrow", "base", "R_soft", cheeks="blush")
            call her_main("If harry and ron knew...", "open", "narrow", "base", "down", cheeks="blush")
            call her_main("I'd... *ah*...{heart}", "soft", "closed", "annoyed", "up", cheeks="blush")
            m "You'd what [hermione_name]?"
            call her_main("I'd...", "open", "closed", "worried", "mid", cheeks="blush")
            call her_main("I'd...{heart}", "silly", "closed", "worried", "mid", cheeks="blush")
            call her_main("I...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up", cheeks="blush")

        "\"Play with your breasts\"":
            call her_main("My breasts...", "open", "narrow", "worried", "down")
            call her_main("I'm not sure if I should--", "open", "narrow", "base", "down")
            m "There's another ten points for Gryffindor in it for you..."
            $ current_payout += 10
            call her_main("...", "normal", "happy", "base", "R")
            call her_main("......", "soft", "happy", "base", "R")

            $ hermione.set_body_zorder(armright=3)
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            call her_main("*Ah*...{heart}", "open", "closed", "base", "R")
            m "There... Isn't that better?"
            call her_main("*Ah*... W-what...", "open", "wink", "worried", "mid")
            call her_main("......", "normal", "happyCl", "base", "mid")
            m "That's it..."
            call her_main("......", "normal", "narrow", "base", "mid", cheeks="blush")
            call her_main("[genie_name], do you mind if...", "soft", "narrow", "base", "L", cheeks="blush")
            m "What [hermione_name]?"
            call her_main("Could you... Call me names...", "open", "narrow", "base", "R", cheeks="blush")
            m "Such as?"

            call her_main("...{size=-5}A Slut...{/size} But only if it's not too much to ask...", "soft", "narrow", "base", "down", cheeks="blush")
            m "That's unbecoming of you to use such language, you little whore..."
            call her_main("Ah...{heart}{heart}", "open", "closed", "annoyed", "mid")
            m "What would your parents think if they saw this?"
            call her_main("I-{heart}", "open", "narrow", "worried", "up", cheeks="blush")
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("Ah...{heart} I don't know...", "soft", "closed", "base", "up", cheeks="blush")
            call her_main("To be perfectly honest [genie_name]... I don't think I care...{heart}{heart}{heart}", "silly", "narrow", "base", "up", cheeks="blush")
            m "Really?"

            call her_main("Really...{heart}", "silly", "narrow", "base", "mid_soft", cheeks="blush")
            m "Would you at least stop?"
            call her_main("*Ah*...{heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call her_main("Maybe...", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call her_main("I'm not sure...", "open", "narrow", "base", "R", cheeks="blush")
            m "So you wouldn't mind if they heard me calling you a slut?"
            call her_main("I...{w=0.4}*mmmh*... Of course I--", "normal", "happyCl", "worried", "mid", cheeks="blush")
            m "I bet if they appeared right now you wouldn't even stop touching yourself you filthy slut."
            call her_main("*Ah*...{heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            m "You're nothing but a disgrace and a whore..."
            call her_main("*Ah*...{w=0.4} I'm-{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")

            call her_main("{heart}{heart}{heart}", "grin", "narrow", "base", "up", cheeks="blush")

        "\"Spread em!\"":
            m "Excellent... Just make sure to give me a nice view of that wet pussy!"
            call her_main("[genie_name]!", "open", "base", "angry", "mid", cheeks="blush")
            m "What?"

            call her_main("It's not {size=-5}wet...{/size}", "annoyed", "narrow", "worried", "R", cheeks="blush")
            m "Are you sure? Because from where I'm sitting it looks nice and wet."
            call her_main("*Ah*...{heart}", "soft", "narrow", "base", "up", cheeks="blush")
            call her_main("It...{w=0.4} it's just sweat, [genie_name]...", "open", "narrow", "base", "R", cheeks="blush")
            m "if you say so..."
            call her_main("...............", "soft", "closed", "base", "up", cheeks="blush")
            m "Slut."
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("{heart}{heart}{heart}", "silly", "narrow", "base", "up_soft", cheeks="blush")
            call her_main("Sir... please...", "open", "narrow", "base", "mid_soft", cheeks="blush")

            $ hermione.set_body_zorder(armright=3)
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            play bg_sounds "sounds/slickloopveryfast.mp3"
            call nar(">Hermione starts fingering herself even faster.")
            m "Very good..."
            call her_main("...{heart}", "silly", "narrow", "base", "up", cheeks="blush")
            call her_main("Ah...{heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            m "That's it slut... Try going a little deeper..."
            call her_main("...", "open_tongue", "narrow", "base", "up", cheeks="blush")

            call her_main("...{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")

    play bg_sounds "sounds/slickloop.mp3"
    call her_main("Ah...", "soft", "narrow", "base", "R", cheeks="blush")
    m "almost there [hermione_name]?"
    call her_main("a-almost...", "annoyed", "base", "worried", "L", cheeks="blush")
    call her_main("I just need a bit longer...")
    m "well you better hurry..."
    call her_main("Ah... i know, [genie_name].", "angry", "happyCl", "worried", "mid")
    call her_main("...........", "normal", "closed", "base", "R", cheeks="blush")
    m "is everything alright?"
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("................", "annoyed", "narrow", "base", "down", cheeks="blush", tears="sweat")
    m "Why are you being so quiet [hermione_name]?"
    play bg_sounds "sounds/slickloop.mp3"
    call her_main("......", "annoyed", "base", "worried", "R_soft", cheeks="blush")
    call her_main("[genie_name]... I don't think I can...")
    m "what?"
    stop bg_sounds
    call her_main("... Finish...", "angry", "happyCl", "base", "down", cheeks="blush", tears="soft")

    menu:
        "-Chastise her-":
            m "Well then I guess Slytherin will have to win the house cup this year."
            call her_main("B-but--", "disgust", "narrow", "worried", "mid", cheeks="blush", tears="soft")
            m "Now, now [hermione_name], a deal's a deal."
            call her_main("but I'm trying [genie_name]...", "upset", "narrow", "worried", "down", tears="crying")
            m "try harder..."
            play bg_sounds "sounds/slickloopveryfast.mp3"
            call her_main("", eyes="happyCl", tears="tears_soft_sweat")
            call nar(">Hermione starts grinding furiously against her hand.")

            # Reset pose
            $ hermione.set_body_zorder(armright=0)
            $ hermione.set_body(armleft="down", armright="down")
            $ hermione.set_pose(None)

            stop bg_sounds
            call her_main("*SOB*! i can't...", "angry", "happyCl", "base", "down", cheeks="blush", tears="messy")
            m "Well then, zero points to Gryffindor..."
            call her_main("{size=-5}After everything I...{/size} Really [genie_name]?", "open", "base", "worried", "stare", cheeks="blush", tears="messy")
            call her_main("After I stood here and...", "scream", "base", "angry", "mid", cheeks="blush", tears="messy")
            call her_main("..........", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")

            call blkfade
            hide screen hermione_main
            call her_chibi("stand", "desk", "base")
            $ hermione.wear("all")
            stop music fadeout 2.0

            call hide_blkfade

            call her_main("I am not going to sell you a single favour anymore, [genie_name]!", "scream", "base", "low", "mid", cheeks="blush", tears="mascara")

            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            $ her_mood += 15

            pause 1.0
            m "..."
            m "We'll see about that."

            jump end_hermione_event

        "-Forgive her-":
            m "It's alright, [hermione_name]."
            call her_main("Really?", "open", "narrow", "worried", "mid", cheeks="blush", tears="crying")
            m "I'm sure you're just a little nervous."

            # Reset pose
            $ hermione.set_body_zorder(armright=0)
            $ hermione.set_body(armleft="down", armright="down")
            $ hermione.set_pose(None)

            call her_main("Thank you [genie_name].", "base", "base", "worried", "mid", cheeks="blush", tears="soft")
            call her_main("I promise to try harder next time.", "base", "happyCl", "worried", "mid", cheeks="blush")

    $ hermione.wear("all")
    jump end_hg_pf_strip

### Tier 5 ###

label hg_pf_strip_T5_fingering:

    $ hg_masturbated.triggered()

    m "[hermione_name]..."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I hope you're feeling horny."
    call her_main("Maybe a little, [genie_name].", "base", "narrow", "base", "mid_soft")
    m "Good, then we better do something about that..."
    call her_main("[genie_name]...", "open", "wink", "worried", "mid")
    g9 "Why don't you give that lovely pussy of yours a little rub."
    call her_main("{heart}{heart}{heart}", "base", "narrow", "base", "mid_soft")
    call her_main(".............", "base", "base", "base", "R_soft")
    call her_main("Alright...{w=0.4} if that's what you want...", "base", "narrow", "worried", "down")
    call her_main("(I can't believe I'm agreeing to do this...{w=0.4} again...)", "soft", "narrow", "base", "down")

    if hermione.is_worn("panties"):
        call nar(">Hermione bends over and takes off her panties.")
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0

    if hermione.is_any_worn("clothes"):
        m "Now take off the rest."
        $ hermione.strip("all")

    call her_main("(Okay then, here I go...)", "normal", "happyCl", "worried", "mid")

    show screen blkfade
    with d5
    $ hermione.set_pose("masturbate")
    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armleft="on_pussy")
    call her_main("", "soft", "closed", "worried", "mid", trans=d3)
    $ renpy.play("sounds/slick_02.mp3")
    with hpunch
    with kissiris
    call her_main("*Ah*...", "open", "squint", "worried", "R", cheeks="blush")
    call ctc
    hide screen blkfade
    with d5

    call play_music("playful_tension") # SEX THEME.
    g9 "Nice..."

    play bg_sounds "sounds/slickloop.mp3" fadein 2
    call her_main("*Mmhh*... {heart}", "open", "happyCl", "worried", "mid")
    call her_main("*Ah*...{w=0.4} {heart}-aha...", "open", "happyCl", "worried", "mid")
    m "..."
    call her_main("Ah-ah...", "open", "happyCl", "worried", "mid")
    m "......................"
    call her_main("*Ah*...{w=0.4} *ah*...{heart}", "open", "happyCl", "worried", "mid")
    call her_main("*Ah*...{w=0.4} [genie_name]?", "soft", "happy", "base", "R")
    m "What is it?"
    call her_main("Do you....{w=0.4}*Ah*...{w=0.4} like this?", "open", "happyCl", "worried", "mid")
    m "Do I like watching \"you\" finger your cute little pussy?"
    m "Of course, [hermione_name]. Why?"
    call her_main("{heart}{heart}{heart}", "normal", "happyCl", "worried", "mid")
    call her_main("*Ah*... You're just so quiet...", "open", "happyCl", "worried", "mid")
    m "Do you need a little more encouragement?"
    call her_main("*Ah*...{w=0.4} yes... please....{heart}", "open", "happyCl", "worried", "mid")
    m "*Tch*... Such a dirty whore..."
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("Yes [genie_name], *Ah*...{heart}", "grin", "narrow", "base", "up", cheeks="blush")
    call her_main("Please... *Ah*...{w=0.4} more...{heart}", "grin", "base", "angry", "mid", cheeks="blush")
    g4 "You deserve to be punished for being such a filthy slut!"
    call her_main("Yes, [genie_name]... punish me...", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("Make me your little slut...", "open", "narrow", "base", "up", cheeks="blush")
    play bg_sounds "sounds/slickloopveryfast.mp3"
    call her_main("I will... *Ah*...{w=0.4} {heart}do anything...{w=0.4} *Ah*...{heart}", "silly", "narrow", "base", "dead")
    m "Anything [hermione_name]?"
    call her_main("Ah-a...{heart} Yessss...", "silly", "narrow", "base", "up", cheeks="blush")
    m "Cum."
    #
    # TODO: CUM LAYERS
    #
    call her_main("{heart}{heart}{heart}!!!{heart}{heart}{heart}", "silly", "narrow", "base", "dead", cheeks="blush")
    with kissiris
    with hpunch
    $ renpy.play("sounds/slick_01.mp3")

    call her_main("*Ah*...{heart}...{heart}", "grin", "narrow", "annoyed", "up", cheeks="blush")
    with kissiris
    with hpunch
    $ renpy.play("sounds/slick_01.mp3")

    call her_main("*Ah*... *Ah*...{heart}", "silly", "base", "base", "ahegao", cheeks="blush")
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("...", "open_tongue", "closed", "base", "up", cheeks="blush")
    call her_main("...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "dead", cheeks="blush")
    call her_main("*Gah*...{w=0.4} *Ah*...{w=0.4} *Ah*...", "open_tongue", "narrow", "annoyed", "dead", cheeks="blush")
    play bg_sounds "sounds/slickloop.mp3"
    call her_main("[genie_name]...{heart}{heart}{heart}", "open", "narrow", "annoyed", "mid", cheeks="blush")
    call her_main(".............", "soft", "narrow", "annoyed", "up")
    stop bg_sounds
    call nar(">Hermione takes a minute to collect herself.")

    # Reset pose
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)

    $ hermione.wear("all")

    jump end_hg_pf_strip

### Tier 6 ###

label hg_pf_strip_T6_fingering:

    $ hg_masturbated.triggered()

    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind pleasuring yourself in front of me, do you?"
    if her_whoring <= 16:
        call her_main("As long as I am being paid...", "grin", "base", "base", "R")
        g9 "That's the spirit!"
    else:
        call her_main("I mean I have done it once today already...", "grin", "base", "base", "R")
        g9 "Once more for good luck then!"
        call her_main("If you insist...{heart}", "open", "base", "base", "R", cheeks="blush")

    call her_main("...", "base", "narrow", "base", "mid_soft")
    if hermione.is_worn("panties"):
        call nar(">Hermione hastily takes off her panties.")
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0

    if hermione.is_any_worn("clothes"):
        m "Now take off the rest."
        $ hermione.strip("all")

    call her_main("(...)", "base", "happyCl", "worried", "mid")

    show screen blkfade
    with d5
    $ hermione.set_pose("masturbate")
    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armleft="on_pussy")
    call her_main("", "soft", "closed", "worried", "mid", trans=d3)
    $ renpy.play("sounds/slick_02.mp3")
    with hpunch
    with kissiris
    call her_main("*Ah*...", "open", "squint", "worried", "R", cheeks="blush")
    call ctc
    hide screen blkfade
    with d5


    stop music fadeout 3.0
    play bg_sounds "sounds/slickloop.mp3" fadein 2

    call her_main("*Mmmh*...{heart}", "base", "narrow", "base", "down", cheeks="blush")
    call her_main("[genie_name]...{w=0.4} Do you...{w=0.4} like it when I do it like this?", "grin", "narrow", "base", "down", cheeks="blush")
    $ renpy.music.set_volume(0.3, 0.0)
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    m "Yes, I love it..."
    m "Try going a little deeper with your fingers."
    call her_main("Alright [genie_name]...", "base", "happyCl", "base", "mid", cheeks="blush")
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("*Ah*...{w=0.4} *Ah*...{w=0.4}{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("*Ah*...{w=0.6} [genie_name]...{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")

    menu:
        m "..."
        "\"Tell me what you're thinking about.\"":
            call her_main("*huh*?", "open", "wink", "worried", "mid", cheeks="blush")
            call her_main("Oh, *umm*... nothing...", "soft", "happyCl", "worried", "mid", cheeks="blush")
            m "[hermione_name]..."
            call her_main("[genie_name],{w=0.4} it's a bit weird...", "disgust", "narrow", "base", "down", cheeks="blush")
            g4 "Even more reason to tell me."
            call her_main("......", "annoyed", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("Fine...", "open", "base", "base", "R", cheeks="blush")
            call her_main("If you must know... I was thinking about the time I corrected professor Snape on the ingredients of a Hiccoughing potion.", "open", "narrow", "worried", "down", cheeks="blush")
            m "....."
            call her_main("*Ah*...{heart}", "soft", "narrow", "annoyed", "up", cheeks="blush")
            call her_main("It was...{w=0.4} *Ah*...{w=0.4} {heart} in front of the entire class as well.", cheeks="blush")
            call her_main("He refused to let me answer any questions for a week after that.", "base", "narrow", "worried", "down", cheeks="blush")
            call her_main("But it was worth it...", "soft", "happy", "base", "R", cheeks="blush")
            call her_main("The look on his face when he realised he was wrong...{heart}", "soft", "narrow", "annoyed", "up", cheeks="blush")
            call her_main("a-ah...{heart}", cheeks="blush")
            call her_main("It just felt so good!{heart}", "grin", "narrow", "base", "dead", cheeks="blush")
            m "This is what you're thinking of when masturbating?"
            call her_main("...", "normal", "narrow", "base", "dead", cheeks="blush")
            call her_main("Is that too weird?", "upset", "narrow", "base", "mid", cheeks="blush")
            m "(No wonder why she's being such a know it all... she's getting off from it.)"
            m "Let's just get back to business shall we?"
            call her_main(".................", "base", "narrow", "annoyed", "up", cheeks="blush")
            call nar(">Hermione goes quiet for a moment to enjoy herself, now fully focused on moving her fingers.","start")
            m "(Having a bit too much fun I think...)"

        "\"You really are a shameless slut, aren't you?\"":
            call her_main("Yes...", "soft", "narrow", "annoyed", "up")
            call her_main("ah... {heart}", "silly", "narrow", "base", "dead")
            call her_main("I don't know if has to do with the time I've spent with you...{heart}", "angry", "wink", "base", "mid")
            call her_main("Or if I've always been this way...{heart}", "angry", "narrow", "base", "down")
            call her_main("But... {heart} {w=0.4}*Ah*...{w=0.4} {heart} I'm a slut [genie_name]...{heart}", "soft", "narrow", "annoyed", "up")
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("A shameless slut...", "grin", "narrow", "base", "dead")
            call her_main("That pleasures herself...{heart} {w=0.4}*Ah*...", "soft", "narrow", "annoyed", "up")
            call her_main("Just to make her headmaster happy...", "grin", "narrow", "base", "dead")
            m "Oh, yes..."
            call her_main("That's it [genie_name]...", "base", "narrow", "worried", "up_soft")
            call her_main("Enjoy yourself while I stand here...", "silly", "narrow", "base", "dead")
            call her_main("*Ah*...{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("Fingering my pussy...", "silly", "narrow", "annoyed", "up")
            call her_main("*Ah*...{w=0.4} *Ah*...{heart}", "grin", "narrow", "annoyed", "up")
            call her_main("*Ah*...{w=0.4} Do you.... like this [genie_name]?", "shock", "happyCl", "worried", "mid")
            call her_main("Watching me {w=0.4}*Ah*...{w=0.4}{heart} degrade myself?", "silly", "narrow", "base", "dead")
            m "Very much, [hermione_name]. Just keep going..."
            call her_main("{heart}{heart}{heart}", "silly", "narrow", "base", "dead")

        "\"Play with your tits some more!\"":
            call her_main("*Hmm*?", "soft", "narrow", "annoyed", "up")
            call her_main("Okay...{w=0.4} if you insist...", "open", "base", "base", "R", cheeks="blush")

            $ hermione.set_body_zorder(armright=3)
            $ hermione.set_body(armright="on_tits")

            call her_main("*Ah*...{heart}", "angry", "wink", "base", "mid")
            m "Now pinch your nipples."
            call her_main("[genie_name]...", "open", "happy", "base", "mid", cheeks="blush")
            m "do it, [hermione_name]."
            call her_main("...", "open", "base", "base", "R", cheeks="blush")
            $ renpy.play("sounds/gasp2.mp3")
            call her_main("*Ah*...", "grin", "narrow", "base", "up", cheeks="blush")
            g9 "..."
            call nar(">You gaze at Hermione's breasts as she runs the tips of her fingers across her nipple...")
            call her_main("*Ah*...", "silly", "narrow", "base", "dead")
            g9 "So you do like playing with those big tits of yours."
            call her_main("I do, [genie_name]... {w=0.4}*Ah*...{heart}", "soft", "narrow", "annoyed", "up")
            call her_main("I don't know why...", "base", "base", "base", "R", cheeks="blush")
            call her_main("But I love it...{heart}{heart}", "open", "narrow", "worried", "down")
            m "You nasty slut!"
            call her_main("*Ah*...{w=0.4}{heart} ah-a...{heart}", "open_tongue", "narrow", "annoyed", "up")
            call her_main("I am...")
            call her_main("A nasty slut... {w=0.4}*Ah*...{heart}", "silly", "narrow", "base", "dead")
            m "You are a disgrace, [hermione_name]!"
            call her_main("Ah-ah...{heart}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")

    m "Why don't you come down and I'll help you finish?"
    call her_main("...", "base", "narrow", "worried", "down")

    # Hermione climbs off your desk.
    show screen blkfade
    with d5
    hide screen hermione_main
    call play_sound("climb_desk")
    stop bg_sounds
    ">Hermione slowly climbs down from the desk and stands in front of you."
    pause.5

    # Both hands down
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")

    call her_chibi_scene("behind_desk_show_tits") #TODO Replace with naked chibi

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call her_main("..............", "base", "narrow", "base", "up", cheeks="blush", trans=d3)

    menu:
        m "..."
        "-Grab her tits-":
            call nar(">You reach forward and grab a hold of Hermione's tits.")

            call her_chibi_scene("grope_tits")

            call her_main("[genie_name]!", "shock", "happyCl", "worried", "mid")
            call her_main("This wasn't part of the deal!", "open", "happyCl", "worried", "mid")
            call her_main("And I was almost about to--", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "Can't let you have all the fun by yourself can we [hermione_name]."
            call her_main("*Ah*...{w=0.4}{heart} Well, as long as it's just to make this end faster...", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I suppose I can...{w=0.4} *Ah*...{w=0.4}{heart} allow it...", "base", "narrow", "base", "down", cheeks="blush")
            call nar(">You give her tits a couple of firm squeezes...")
            m "Just admit that you love it."
            call her_main("*Ah*...{w=0.4} fine...{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}I like it...{/size}", "soft", "narrow", "annoyed", "up")
            m "What was that [hermione_name]?"
            call her_main(".......", "normal", "narrow", "annoyed", "up")
            call her_main("I love this...", "grin", "narrow", "base", "dead")
            call her_main("Standing here... all exposed...", "base", "narrow", "worried", "down_soft", cheeks="blush")
            call her_main("*Ah*...{w=0.4} while you play with me...{heart}", "grin", "narrow", "base", "up", cheeks="blush")
            m "Heh... Nice."
            call her_main("*Ah*...{heart}", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I sometimes wish I could spend all day in here...", "grin", "narrow", "angry", "dead", cheeks="blush")
            m "Perhaps we could arrange that some time..."
            call nar(">You keep on massaging the girl's breasts...")
            call her_main(".......")
            call her_main("[genie_name]... I...{w=0.4} Please...{w=0.4} I was so close...", "open", "base", "worried", "L", cheeks="blush")
            call her_main("*Ah*...{heart}", "base", "narrow", "worried", "down")
            call her_main("Could you touch me...{w=0.4} down there...", "open", "happy", "base", "mid", cheeks="blush")
            m "What was that [hermione_name]? You'll have to speak up."
            call her_main("Please finger me...", "open", "narrow", "base", "up", cheeks="blush")
            m "One more time, a little louder this time."
            call her_main("*Ah*...{heart} {size=+5}please finger my pussy!{/size}", "scream", "narrow", "base", "up", cheeks="blush")
            m "As you wish..."
            call her_chibi_scene("grope_ass_front")
            with vpunch
            $ renpy.play("sounds/slick_02.mp3")

            call nar(">You swiftly plunge two fingers into her dripping pussy.")

            call her_main("{heart}{heart}{size=+5}!!!{/size}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")

        "-Finger her-":
            call her_chibi_scene("grope_ass_front")
            call nar(">You run your hands up and down Hermione's legs...")
            call her_main("!!!", "open", "happyCl", "worried", "mid")
            call nar(">And slowly move your hands towards her pussy...")
            call her_main(".................", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]..."
            call her_main("{size=-7}[genie_name]...{/size}", "soft", "narrow", "annoyed", "up")
            m "Good girl."
            call her_main("....................", "open", "closed", "base", "mid", cheeks="blush")
            m "Just be quiet for a second..."
            call nar(">You enjoy the sensation of stroking the inside of Hermione's thighs...")
            call nar(">Kneading her gently and moving ever closer to her wet pussy...")
            m "I love your big... firm, ass..."
            call nar(">As you get closer to her pussy you suddenly move your hands around her back to squeeze her ass...")
            call her_main(".....................", "annoyed", "base", "annoyed", "dead", cheeks="blush")
            m "Your loins..."
            call nar(">You slide your fingers across the side of her body as you return to the front, and then gently begin rubbing your forefinger just above her clit.")
            call her_main(".....................{size=-8} [genie_name]...{/size}", "silly", "narrow", "base", "dead", cheeks="blush")
            m "What was that, [hermione_name]?"
            call her_main(".....................", "annoyed", "wink", "base", "mid", cheeks="blush")
            call her_main("... I...{w=0.4} {size=-5}... I need you...{w=0.4} inside of me...{/size}", "disgust", "narrow", "base", "down", cheeks="blush")
            m "You'll have to speak up if you expect me to hear you..."
            call her_main("I...{w=0.4} *Ah*...{w=0.4}{heart} need...", "open", "narrow", "base", "up", cheeks="blush")
            call nar(">You swiftly plunge two fingers into her drenched pussy.")
            $ renpy.play("sounds/slick_02.mp3")
            call her_main("!!!{heart}{heart}", "grin", "narrow", "annoyed", "up")
            call nar(">You start to pump your fingers inside her before she can do more than gasp.")
            play bg_sounds "sounds/slickloop.mp3"
            call her_main("{size=+10}{heart}{heart}!!!{heart}{heart}{/size}", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]. Just enjoy yourself."
            call her_main("..................................................", "base", "narrow", "base", "up", cheeks="blush")
            m "Do you like this?"
            m "You like it when I finger your pussy?"
            call her_main("I love it!{heart}{w=0.4} I love your fingers in my tight...{w=0.4} wet....{w=0.4} pussy!!{heart}", "silly", "narrow", "annoyed", "up")
            m "Well, I certainly think we can do better..."
            call nar(">with your other hand, you start rubbing your thumb against her clit.")
            call her_main("{size=+10}!!!{/size}", "open", "narrow", "base", "up", cheeks="blush")

    play bg_sounds "sounds/slickloopfast.mp3"
    call nar(">With little need to move, Hermione pounds herself down to the base of your fingers.")
    call her_main("*Ah*...{heart}{w=0.4} please...{w=0.4}{heart} keep...{heart}", "silly", "narrow", "base", "dead","blush")
    call her_main("Fingering my pussy!{heart}{heart}", "silly", "narrow", "annoyed", "up","blush")
    g9 "As you command!"
    call nar(">You force another finger into her pussy!")
    $ renpy.play("sounds/slick_02.mp3")
    play bg_sounds "sounds/slickloopveryfast.mp3"
    call her_main("*Ah*...{w=0.4} yes! {heart}iloveitiloveitiloveit!{heart}", "scream", "wide", "annoyed", "dead","blush")
    m "what do you love, [hermione_name]?"
    call her_main("ah!!{heart} I love your fingers in my pussy [genie_name]!{heart}", "open_wide_tongue", "happyCl", "annoyed", "dead","blush")
    call nar(">Hermione's legs begin to shake slightly as you finger her with renewed vigour.")
    m "are you about to--"
    call her_main("ah...{heart} yes!!", "mad", "narrow", "annoyed", "dead", cheeks="blush")
    call her_main("I'm about to cum [genie_name]!!{heart}", "grin", "narrow", "base", "dead", cheeks="blush")
    call her_main("From being fucked by your fingers!!{heart}{heart}", "open_tongue", "base", "base", "ahegao", cheeks="blush")
    m "Touch your tits [hermione_name]!"
    m "I want to see you play with them as you cum."

    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armright="on_tits")

    call her_main("*Ah*...{w=0.4} Yes...{w=0.4}*Ah*... my--", "soft", "narrow", "base", "dead", cheeks="blush")
    call her_main("[genie_name]{heart}... I'm...*Ah*...{w=0.4} I'm cumming!{heart}", "silly", "narrow", "annoyed", "dead", cheeks="blush")
    call her_main("{heart}{heart}{heart}!!!{heart}{heart}{heart}", "silly", "narrow", "base", "dead", cheeks="blush")
    with kissiris
    with hpunch
    $ renpy.play("sounds/slick_01.mp3")
    #
    # TODO: CUM LAYERS
    #
    call her_main("*Ah*...{w=0.4}{heart}...{heart}", "grin", "narrow", "annoyed", "dead", cheeks="blush")
    with kissiris
    with hpunch
    $ renpy.play("sounds/slick_01.mp3")
    call her_main("*Ah*...{w=0.4} *Ah*...{heart}", "silly", "narrow", "annoyed", "dead", cheeks="blush")
    with kissiris
    with hpunch
    $ renpy.play("sounds/slick_01.mp3")
    call her_main("*Mmmmmmh*!!!", "soft", "base", "annoyed", "dead", cheeks="blush")
    call her_main("........................", "grin", "base", "annoyed", "dead", cheeks="blush")
    stop bg_sounds

    if hermione.is_worn("bottom"):
        call nar(">You remove your hands from underneath Hermione's skirt, fingers drenched by her love juices.")
    else:
        call nar(">You remove your hands from Hermione's love canal, fingers drenched by her love juices.")

    call her_chibi_scene("behind_desk_front")
    show screen bld1
    with d3

    # Reset pose
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)

    m "This shall do for now [hermione_name]."

    call her_main("*Ah*...{w=0.4} *Ah*...{heart}", "open", "narrow", "annoyed", "dead", cheeks="blush")
    call her_main("Yes...{w=0.4} yes, [genie_name]{heart}", "silly", "narrow", "base", "mid_soft", cheeks="blush")

    $ hermione.wear("all")
    $ renpy.music.set_volume(1.0, 3.0)

    jump end_hg_pf_strip
