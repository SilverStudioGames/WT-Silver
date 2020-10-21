

### Hermione Titjob ###

label hg_pf_titjob:

    if hg_pf_titjob.counter == 0:
        m "{size=-4}(Should I ask her for a titjob?){/size}"
    else:
        g9 "{size=-4}(I feel like putting my cock between those tits again!){/size}"

    if hg_pf_titjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 45
    $ hg_pf_titjob.start()


    # End Event
    label end_hg_pf_titjob:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ hermione.set_cum(None)
    $ hermione.wear("all")
    $ hermione_zorder = 15 # Reset sprite zorder (affected by CGs)

    hide screen ccg

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
        her "Classes are about to start..."
    else:
        her "It's getting late..."
    her "I'd better go now..."


    # Hermione leaves
    call her_walk("door", "base")

    call her_chibi("leave")


    # Increase level
    if her_tier == 5:
        if her_whoring < 21: # Points til 21
            $ her_whoring +=1
    if her_tier == 6:
        if her_whoring < 24: # Points til 24
            $ her_whoring += 1

    jump end_hermione_event

### Fail Events ###

label hg_pf_titjob_fail:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Have you ever given somebody a \"titjob\"?"

    $ hg_pf_titjob.fail()

    jump too_much

### Tier 5 ###

# Event 1 (i) - Hermione wants 100 house points for it!
# Event 2 (r) - Reluctantly does it again.

label hg_pf_titjob_T5_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Now, [hermione_name]..."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Have you ever given someone a \"titjob?\""
    call her_main("A \"titjob?\"", "annoyed", "narrow", "annoyed", "mid")
    m "It's where you wrap those {i}fat tits{/i} of yours around a cock..."
    g9 "And then shake them up and down, up and--"
    call her_main("[genie_name]!", "angry", "base", "angry", "mid")
    m "Is that a yes?"
    call her_main("...............", "disgust", "narrow", "base", "mid_soft")
    call her_main("{size=-7}No...{/size}", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "*Hmm*?... What was that?"
    call her_main("Of course I haven't...", "open", "narrow", "angry", "R")
    g9 "Well then, today is your lucky day!"
    call her_main("Lucky?{w} In what way would you consider it lucky?", "disgust", "narrow", "base", "mid_soft")
    m "It's not every day that you get to learn something new."
    call her_main("I'm at a school... We get taught hundreds of things each day...", "annoyed", "base", "angry", "mid")
    call her_main("And giving \"titjobs\" isn't one of them...", "angry", "base", "angry", "mid")
    m "At least this is something you'll be able to use in the real world."
    call her_main("If you say so, [genie_name]...", "annoyed", "narrow", "angry", "R")
    call her_main("...", "annoyed", "narrow", "angry", "mid")
    call her_main("{size=-7}I want a hundred points for this...{/size}", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Speak up, [hermione_name]."
    call her_main("A hundred points!", "scream", "happyCl", "worried", "mid")
    call her_main("", "annoyed", "narrow", "angry", "R")

    label back_to_titjob_choices:
    menu:
        m "(...)"
        "\"You'll get fifteen house points.\"" if her_mood == 0:
            $ her_mood += 7
            call her_main("[genie_name], are you seriously expecting me to give you a titjob...", "angry", "closed", "angry", "mid")
            call her_main("For only a meagre fifteen points?!", "scream", "base", "angry", "mid")
            call her_main("", "clench", "base", "angry", "mid")
            m "Then how about twenty? Does that sound fair?"
            call her_main("I don't know who you think I am, but I'm not doing something like this for only fifteen points!", "open", "base", "angry", "mid")
            m "I promise I won't even cum on them..."
            call her_main("And you believe that \"that\" would change my mind?", "scream", "base", "angry", "mid")
            m "I sure hoped so..."
            call her_main("No.{w=0.5} You need to make me a better offer... or I'll be leaving...", "annoyed", "narrow", "angry", "R")
            m "Fair enough..."
            jump back_to_titjob_choices

        "\"You'll get forty-five house points.\"":
            call her_main("{number=current_payout} house points...?", "open", "wink", "base", "mid")
            call her_main("This could put Gryffindor back in the lead...", "annoyed", "narrow", "worried", "down")
            m "So... Is that a yes?"
            call her_main("It's a yes, [genie_name]...", "open", "closed", "base", "mid")
            call her_main("{number=current_payout} points sounds like a fair amount for--", "open", "base", "base", "R")
            g9 "For a titjob!"
            call her_main("(...)", "annoyed", "base", "angry", "mid")

        "\"You'll get one hundred house points.\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ current_payout = 100
            $ her_mood = 0
            call her_main("{number=current_payout} house points?!", "scream", "wide", "base", "mid")
            call her_main("This might be enough to put Gryffindor in the lead!", "smile", "wide", "base", "stare")
            m "So... Is that a yes?"
            call her_main("Yes, [genie_name]!", "smile", "happyCl", "base", "mid")
            call her_main("I shall do my best...", "soft", "narrow", "base", "mid_soft", emote="happy")

    jump hg_pf_titjob_1

label hg_pf_titjob_T5_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], would you like to earn some house points again?"
    call her_main("Of course, [genie_name]...", "base", "base", "base", "mid")
    call her_main("What would I have to do to earn them?", "open", "base", "base", "R")
    g9 "Nothing you aren't already experienced with!"
    m "I'm just going to rub my cock between those precious tits of yours..."
    call her_main("This again...", "angry", "closed", "angry", "mid")
    call her_main("(...)", "annoyed", "narrow", "angry", "R")
    call her_main("For {number=current_payout} house points?", "open", "base", "angry", "mid")
    m "{number=current_payout} house points, as always..."
    call her_main("(...)", "annoyed", "narrow", "angry", "R")
    call her_main("Very well, [genie_name]", "open", "closed", "base", "mid")
    call her_main("But you have to promise me that you'll make it quick...", "annoyed", "base", "angry", "mid")
    g9 "..............."

    jump hg_pf_titjob_1

### Tier 6 ###

# Event 1 (i) - Event with a couple of choices.
# Event 2 (i) - Some new interactions.
# Event 3 (r) - Repeat.

label hg_pf_titjob_T6_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "How do you feel about wrapping those nice tits of yours around my cock again?"
    call her_main("Only nice?", "upset", "closed", "base", "mid")
    m "Fine, fine."
    m "How do you feel about wrapping those perfect tits of yours around my cock again?"
    call her_main("Of course, [genie_name].", "base", "narrow", "base", "mid_soft")
    m "You like it when I call them perfect don't you?"
    call her_main(".............", "base", "narrow", "worried", "down")
    g9 "You don't have to answer, just bring those {b}perfect{/b} tits over here."
    call her_main("{heart}{heart}{heart}", "base", "happyCl", "worried", "mid")
    call her_main("yes, [genie_name]...", "grin", "base", "base", "R")

    jump hg_pf_titjob_2

label hg_pf_titjob_T6_intro_E2:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I would very much like to see those perfect fun-bags of yours again..."
    g9 "Wrapped around my cock!"
    call her_main("Oh...{w=0.4} Again?", "base", "narrow", "worried", "down")
    call her_main("For {number=current_payout} house points?", "soft", "narrow", "base", "mid_soft")
    m "Yes, [hermione_name]."
    call her_main("(...)", "annoyed", "base", "base", "R")
    call her_main("Very well then...", "smile", "happyCl", "base", "mid")
    g9 "Splendid!"

    jump hg_pf_titjob_2

label hg_pf_titjob_T6_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], how would you like wrapping those perfect tits of yours around my cock again?"
    call her_main("As long as I am getting paid...", "soft", "happy", "base", "R")
    g9 "Well, then... Time to earn those points!"
    call her_main("{heart}{heart}{heart}", "base", "narrow", "base", "up")

    jump hg_pf_titjob_2

### First Tier Titjob ###

label hg_pf_titjob_1:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    show screen chair_left
    show screen desk
    call her_chibi("stand",560,"base")
    call gen_chibi("jerk_off",450,"base")

    hide screen blkfade
    with fade
    pause.8

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "disgust", "narrow", "worried", "down")
    if hg_pf_titjob.counter == 1:
        call her_main("(It's so big...)", "disgust", "narrow", "base", "down")
    m "Get to it, [hermione_name]..."
    call her_main("Right...", "angry", "happyCl", "worried", "mid", emote="sweat")
    $ hermione.strip("robe", "accessory")

    if hermione.is_any_worn("top", "bra"):
        call her_main("Let me get undressed first...", "disgust", "base", "worried", "down")
        $ hermione.strip("top", "bra")
        pause 1.0

    call her_main("", "annoyed", "narrow", "annoyed", "mid")
    pause.5

    # Setup
    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 5
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        $ hermione_zorder = -1
        hide screen hermione_main
        show screen ccg
        with fade

    hide screen hermione_main
    with d3
    call nar(">Hermione awkwardly wraps her tits around your cock...")

    call her_chibi_scene("tj_pause", trans=d5)
    call ctc
    #pause.8

    call bld
    m "That's a start.{w=0.4} Now, up and down..."
    call her_main("Alright...", "angry", "happyCl", "worried", "mid", emote="sweat", xpos="base", ypos="head")

    call her_chibi_scene("tj", trans=d5)
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call bld
    g9 "*Mmmm*..."
    $ ccg1 = 6
    if hg_pf_titjob.counter == 1:
        call her_main("...", "base", "base", "base", "mid")
        call her_main("Does it...{w=0.4} feel good?", "base", "happy", "base", "mid")
        m "Good?"
        m "It feels amazing."
        call her_main("Oh...", "base", "happy", "base", "mid")
        call her_main("......")
        call her_main("Thank you [genie_name].", "base", "base", "base", "R")

    call her_main("............", "annoyed", "narrow", "worried", "down")
    call her_main("[genie_name]...?", "soft", "base", "base", "mid")
    m "What is it?"
    $ ccg1 = 7
    call her_main("Promise me you won't cum on my... face...", "upset", "wink", "base", "mid")

    $ d_flag_01 = False #If TRUE Genie promised to warn her.
    menu:
        m "..."
        "\"I promise not to cover that sweet little face of yours...\"":
            $ d_flag_01 = True #If TRUE Genie promised to warn her.
            $ ccg1 = 6
            call her_main("Thank you, [genie_name].", "base", "happy", "base", "mid")
        "\"*Hmm*... We'll see how I feel later.\"":
            $ ccg1 = 8
            call her_main("*Hmph*...", "annoyed", "narrow", "annoyed", "mid")
            call her_main("At least try and avoid my hair...", "normal", "happyCl", "worried", "mid")

    $ ccg1 = 5
    call her_main(".............", "disgust", "narrow", "worried", "down")
    m "............."
    call her_main(".............", "normal", "happyCl", "worried", "mid")
    call her_main("Err... [genie_name]?")
    m "Yes, what is it?"
    call her_main("Are you almost...{w=0.3} there?", "open", "base", "base", "mid")
    m "Why?"
    $ ccg1 = 7
    if game.daytime:
        call her_main("Well, it's just that...{w=0.3} my classes are about to start...", "upset", "wink", "base", "mid")
    else:
        call her_main("Well, it's just that...{w=0.3} I promised I would meet with Ginny tonight...", "upset", "wink", "base", "mid")
        call her_main("She's already pretty upset with how much time I'm spending in here...")
    m "Do you need the points or not?"
    $ ccg1 = 6
    call her_main("I do, [genie_name]! I'm sorry...", "grin", "happyCl", "worried", "mid")
    call her_main("I'll just keep stroking it then...")
    m "Well, there is a way to finish this up a bit faster..."
    call her_main("Really? What is it, [genie_name]?", "base", "base", "base", "R")

    menu:
        m "..."
        "\"Tell me how much you love your tits!\"":
            $ ccg1 = 5
            call her_main("What?", "upset", "wink", "base", "mid")
            $ ccg1 = 6
            call her_main("My breasts?", "disgust", "narrow", "worried", "down")
            m "You know,{w=0.5} how good they feel..."
            m "How many eyes are drawn to you thanks to them..."
            call her_main("Oh,{w=0.3} okay then...", "base", "base", "base", "mid")
            call her_main("Well...{w=0.4} There was this one time in the library...", "smile", "base", "base", "R")
            call her_main("It was completely empty, except for me and this first year boy sitting right across from me...")
            m "*Heh*... good.{w=0.3} Go on..."
            call her_main("It was quite hot that day, so... I decided to take my vest off.", "base", "happy", "base", "mid")
            g9 "Yes! And somehow you got even hotter!"
            call her_main("The boy was trying to act all sly about it, but I could tell he snuck a peek at them any chance he got...", "base", "base", "base", "R")
            call her_main("At that point I began undoing a couple of buttons... Slowly at first, not enough for him to suspect anything...", "base", "narrow", "base", "mid_soft")
            g9 "*Hmm*... You little flaunter."
            $ ccg1 = 9
            call her_main("By the third button, he couldn't take his eyes off me...", "base", "narrow", "worried", "down")
            call her_main("And when I got to the fourth... I saw him move his hands under the desk...")
            m "Really?"
            call her_main("Yes... I swear I could even hear him...{w=0.3}\"doing it\"...", "base", "narrow", "base", "up")
            $ ccg1 = 10
            call her_main("I'm sure he could get a good glimpse of my bra...", "open", "base", "base", "R")
            g9 "Do you have no shame?"
            $ ccg1 = 5
            call her_main("[genie_name]! I was just trying to cool off...", "base", "narrow", "worried", "down")
            m "I'm just kidding, keep going..."
            call her_main("..............", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 9
            call her_main("By the sixth button my entire bra was unveiled...")
            call her_main("And he must have had a really good view of my cleavage...", "base", "base", "base", "mid")
            call her_main("And my...{w=0.3} tits...", "soft", "narrow", "base", "mid_soft")
            call her_main("He didn't even try to hide what he was doing and just kept staring at them... touching himself...")
            $ ccg1 = 10
            call her_main("Then suddenly I felt something sticky on my legs as he shot several ropes of cum under the table!", "open_tongue", "narrow", "annoyed", "up")
            g4 "!!!"
            call her_main("Come on, [genie_name]! Cover me as well! Cover my tits in your cum!", "grin", "base", "angry", "mid")

        "\"Stick out your tongue!\"":
            $ ccg1 = 5
            call her_main("[genie_name]?", "open", "wink", "base", "mid")
            g4 "Just do it, slut!"
            $ ccg1 = 11
            call her_main("*Ehm*...{w=0.4} *Ike* *ees*?", "open_wide_tongue", "narrow", "worried", "down")
            m "Yes, good..."
            m "Now tilt your head down a bit... as far as it'll go."
            call her_main(".....................", "open_wide_tongue", "base", "base", "mid")
            m "Yes...{w=0.3} Good..."
            call her_main("...........", "open_wide_tongue", "base", "base", "mid")
            call her_main("...........")
            $ ccg1 = 9
            call her_main("I *khant* *eef* *ay* *outh* *oen*...", "open_tongue", "base", "base", "mid")
            call her_main("I *eel* *ool*...", "open_wide_tongue", "narrow", "worried", "down")
            g4 "Yes! Drool all over those perfect tits of yours!"
            call her_main("*Erth-ect*?", "open_tongue", "base", "base", "mid")
            m "As perfect as any mortal, [hermione_name]!"
            $ ccg1 = 11
            call her_main(".......", "base", "narrow", "base", "up")
            m "Try to get it as close to the tip of my cock as you can..."
            call her_main("............", "normal", "happyCl", "worried", "mid")
            call her_main("A-ha...", "open_wide_tongue", "base", "base", "mid")
            m "Good, [hermione_name]."
            call her_main("..............", "open_wide_tongue", "base", "base", "mid")
            m "Yes, keep on stroking my cock."
            call nar(">You thrust up as she pushes her tits down causing the tip of your cock to touch her wet tongue.")
            call her_main("..................", "open_wide_tongue", "base", "base", "mid")
            g4 "That's good..."
            call her_main(".................", "open_wide_tongue", "base", "base", "mid")
            pause.2

            call her_chibi_scene("tj_mouth", trans=d5)
            call ctc

            call nar(">Your thrusts ends up going into her drooling mouth.")
            g4 "That's it, slut! Taste it!"
            call her_main(".....................", "open_wide_tongue", "wide", "angry", "stare")
            m "Yes, you big-titted whore!"
            call her_main("......................", "open_wide_tongue", "happyCl", "angry", "mid")
            g4 "Get ready slut..."
            call her_main("................", "open_wide_tongue", "narrow", "worried", "up")

    with hpunch
    g4 "{size=-4}(Here it comes!){/size}"

    menu:
        m "..."
        "-Cum in her mouth!-":
            $ her_mood += 3
            call bld
            g4 "Here it comes, [hermione_name]!"
            $ ccg1 = 13

            call her_chibi_scene("tj_pause", trans=d5)

            call her_main("What? already?!", "shock", "wide", "base", "stare")
            g4 "{size=+5}Yeah, your tits felt great!!!{/size}"
            g4 "{size=+5}You little whore!!!{/size}"
            call her_main("No, [genie_name], wait, not on my face!", "angry", "base", "base", "mid")
            g4 "{size=+5}Then open wide, slut!!{/size}"
            call her_main("Not my mou--", "scream", "wide", "base", "stare")
            call nar(">You grab the back of Hermione's head and force your cock into her open mouth...")
            $ ccg1 = 12

            stop music fadeout 1.0
            call cum_block
            call her_chibi_scene("tj_cum_in", trans=d5)
            pause.8

            call her_main("!!!", "open_wide_tongue", "wide", "base", "stare")
            call cum_block

            $ hermione.set_cum(breasts="light")

            g4 "{size=+5}ARGH! YES!!! Take it!{/size}"
            call her_main(".....................", "open_wide_tongue_cum", "happyCl", "worried", "mid")
            call bld("hide")
            call ctc

            call her_chibi_scene("tj_cum_in_done", trans=d5)

            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "*Mmm*... That felt great..."
            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "How are you feeling?"
            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "[hermione_name]?"
            pause.2

            call her_chibi_scene("tj_pause", trans=d5)
            pause.5

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 15
            call her_main("*Ptui*...", "open_wide_tongue_cum", "base", "angry", "mid", trans=hpunch)

            $ hermione.set_cum(face="light")

            $ ccg1 = 16
            call her_main("Why on earth did you cum in my mouth?", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "You did say not to cum on your face..."
            pause.2

            $ ccg1 = 17

            call her_chibi_scene("tj_cum_on_done", trans=d5)
            pause.5

            call nar(">Hermione lets go of your still pulsating cock...")
            call her_main("*Ugh*...{w=0.4} You came so much!", "angry", "happyCl", "worried", "mid", emote="sweat")
            call her_main("I had to swallow most of it...", "disgust", "narrow", "base", "down", emote="sweat")
            g9 "You did a great job, [hermione_name]!"
            call her_main("I don't want to hear it...", "angry", "narrow", "angry", "R", emote="sweat")
            if game.daytime:
                call her_main("I can't go to class like this...", "angry", "happyCl", "worried", "mid", emote="sweat")
                call her_main("I'm covered in semen...", "disgust", "narrow", "base", "down", emote="sweat")
            else:
                call her_main("At this hour the Gryffindor common room will be full of students...", "angry", "happyCl", "worried", "mid", emote="sweat")
                call her_main("And I'm smelling like spunk!", "scream", "happyCl", "worried", "mid")
                call her_main("I can only hope I'll be able to run past them without anybody noticing...", "disgust", "narrow", "worried", "down")

            m "I mean... You could have swallowed."
            m "Then there wouldn't have been any clean up."
            call her_main("Swallow? All of that?", "angry", "narrow", "base", "down")
            call her_main("I don't think I have enough room in my stomach...")
            call her_main("Could I please have my points now, [genie_name]?", "soft", "base", "angry", "mid")

        "-Cover her tits!-":
            with hpunch
            call bld
            g4 "ARGH!"
            $ ccg1 = 13

            call her_chibi_scene("tj_pause", trans=d5)

            call her_main("WHAT?!", "shock", "wide", "base", "stare")
            g4 "Take this slut!"

            stop music fadeout 1.0
            call cum_block
            call her_chibi_scene("tj_cum_on", trans=d5)
            pause.8

            $ hermione.set_cum(breasts="light")

            call bld
            g4 "{size=+5}ARGH! YES!!!{/size}"

            call her_main("....................", "shock", "happyCl", "worried", "mid")
            call cum_block
            $ hermione.set_cum(body="light", breasts="heavy")
            $ ccg1 = 18
            call ctc

            call her_chibi_scene("tj_cum_on_done", trans=d5)

            call her_main(".......................", "angry", "wide", "base", "stare")
            m "Well, I think that's about it..."
            call her_main("..........", "soft", "base", "base", "mid",tears="soft")

            $ ccg1 = 17
            call her_main("[genie_name]! How could you cum this much?!", "scream", "happyCl", "worried", "mid")
            call her_main("(It's like he dumped a bucket load all over my chest...)", "disgust", "narrow", "base", "down")
            if game.daytime:
                call her_main("I can't attend classes looking like this!", "angry", "happyCl", "worried", "mid")
            else:
                call her_main("How am I supposed to go back to the Gryffindor common room like this?!", "angry", "happyCl", "worried", "mid")
            m "Just wipe it off..."
            call her_main("...........................", "angry", "narrow", "worried", "down")
            call her_main("I would like to get paid now, [genie_name]...", "annoyed", "narrow", "angry", "R")

    $ achievement.unlock("hertits")

    jump end_hg_pf_titjob

### Second Tier Titjob ###

label hg_pf_titjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    # Setup
    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 6
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        $ hermione_zorder = -1
        hide screen hermione_main
        show screen ccg
        with d3

    $ ccg1 = 20
    $ hermione.strip("robe", "accessory")

    if hermione.is_any_worn("top", "bra"):
        call her_main("Let me get undressed first...", "disgust", "base", "worried", "down")
        $ hermione.strip("top", "bra")
        pause 1.0

    call nar(">Hermione wraps her plump tits around your cock...")

    call her_chibi_scene("tj", trans=fade)
    call ctc

    call her_main("Do you enjoy it when I move them like this, [genie_name]?", "grin", "base", "base", "R", xpos="base", ypos="head")
    call nar(">Hermione starts alternating her breasts as she tit-fucks you.")
    g9 "Actually...{w=0.3} Yes! Very much!"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("...", "base", "narrow", "base", "mid_soft")
    m "Yes, just like that..."
    m "*Hmm*... You're getting pretty good at this."
    $ ccg1 = 21
    call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
    call her_main("I figured with how kind you've been it's the least I could do...")

    menu:
        m "..."
        "\"What do you think of my cock?\"":
            $ ccg1 = 22
            call her_main("*huh*?", "open", "base", "base", "mid")
            call her_main("Your cock?", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "What do you think about--"
            $ ccg1 = 23
            call her_main("It's magnificent!", "upset", "closed", "base", "mid")
            m "go on..."
            call her_main("[genie_name], If you say that I have the perfect tits...", "soft", "narrow", "annoyed", "up")
            call nar(">She squeezes her tits around your cock.")
            $ ccg1 = 22
            call her_main("This, has to be the perfect cock!", "grin", "narrow", "base", "dead")
            g9 "Perfect you say?"
            call her_main("The size...", "soft", "narrow", "worried", "down")
            call her_main("The shape...", "base", "narrow", "worried", "down")
            call her_main("Everything about it...", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 24
            call nar(">Hermione tilts her head down and licks the tip of your cock.")
            call her_main("...........", "open_tongue", "narrow", "annoyed", "up")
            $ ccg1 = 23
            call her_main("Perfect taste...", "soft", "narrow", "annoyed", "up")
            m "..."
            $ ccg1 = 25
            call her_main("I think your perfect cock should be shared around the school.", "scream", "closed", "angry", "mid")
            m "Well, I wouldn't go that far--"
            call her_main("Listen to me, [genie_name]!", "angry", "closed", "angry", "mid")
            call her_main("I think it should be worshipped as part of the school curriculum!", "soft", "narrow", "annoyed", "up")
            $ ccg1 = 24
            call her_main("Girls will be required to come in and bask in its glory!", "open_tongue", "narrow", "annoyed", "up")
            m "OK, I think I've heard enough."
            $ ccg1 = 21

            call her_chibi_scene("tj_pause", trans=d5)
            pause.8

            call her_main("Too much?", "angry", "wink", "base", "mid")
            m "Yeah, just a bit."
            call her_main("Sorry [genie_name], I got a bit carried away...", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "No worries. Just keep on massaging it with those big tits of yours."

            call her_chibi_scene("tj", trans=d5)
            pause.8

            call her_main(".................", "soft", "narrow", "annoyed", "up")
            call nar(">Hermione keeps on stroking your cock.","start")
            $ ccg1 = 25
            call nar(">Letting some spit dribble down to help lubricate it.","end")
            $ ccg1 = 21
            m "Yes, yes...{w=0.3} That's it, slut!"

        "\"Call yourself a big-titted whore!\"":
            $ ccg1 = 22
            call her_main("Excuse me?", "open", "base", "base", "mid")
            $ ccg1 = 23
            call her_main("Oh...{w=0.5} I am a big-titted whore!", "soft", "narrow", "annoyed", "up")
            m "Good. Glad we established that."
            m "Now I want you to say..."

            menu:
                m "..."
                "\"I am a shameless cumslut!\"":
                    $ ccg1 = 22
                    call her_main("Of course.", "base", "narrow", "worried", "down")
                    $ ccg1 = 24
                    call her_main("I am a shameless cumslut.", "soft", "narrow", "annoyed", "up")
                    $ ccg1 = 21
                    call her_main("A dirty little slut who's addicted to the taste of my headmaster's cum...", "grin", "narrow", "base", "dead")
                    m "Yes! Good!"

                "\"I love being covered in cum!\"":
                    $ ccg1 = 24
                    call her_main("I love being covered in cum!", "soft", "narrow", "annoyed", "up")
                    call her_main("hot...")
                    call her_main("sticky...")
                    call her_main("smelly...")
                    call her_main("cum...")
                    $ ccg1 = 23
                    call her_main("...................................", "grin", "narrow", "base", "dead")
                    $ ccg1 = 21
                    call her_main("How was that, [genie_name]?", "angry", "wink", "base", "mid")
                    m "Perfect."

        "\"This is really good. Did you practise?\"":
            $ ccg1 = 22
            call her_main("*Hmm*?...", "base", "happyCl", "base", "mid")
            $ ccg1 = 21
            call her_main("Sort of...{w=0.3} Well not on another cock...", "angry", "wink", "base", "mid")
            m "On what then?"
            $ ccg1 = 22
            call her_main("Well, I spoke to Ginny...", "grin", "base", "base", "R")
            m "A friend of yours?"
            call her_main("Yes. I asked if she had any tips for this sort of thing...", "base", "base", "base", "R")
            $ ccg1 = 21
            call her_main("She said the best way to improve was to practise...", "base", "happy", "base", "mid")
            m "Practise on what?"
            $ ccg1 = 22
            call her_main("On Ginny.", "smile", "base", "base", "R")
            $ ccg1 = 23
            call her_main("Well,{w=0.5} on her arm...", "angry", "wink", "base", "mid")
            m "You tit-fucked your friend's arm?"
            $ ccg1 = 25
            call her_main("Just as practice!", "grin", "happyCl", "worried", "mid", emote="sweat")
            $ ccg1 = 22
            call her_main("She even gave me some tips...")
            $ ccg1 = 23
            call her_main("How does this feel?", "base", "narrow", "worried", "down")
            m "*Mmm*... Yes, this feels quite good."
            call her_main("Does it?", "angry", "wink", "base", "mid")
            $ ccg1 = 21
            call her_main("Ginny seemed to enjoy it quite a bit as well...", "base", "narrow", "base", "up")
            g4 "She did?"
            $ ccg1 = 22
            call her_main("Of course she did!", "base", "happyCl", "base", "mid")
            $ ccg1 = 23
            call her_main("Who wouldn't love feeling my perfect tits...", "base", "closed", "base", "mid")
            call her_main("Although I think she might have enjoyed it...", "open", "narrow", "worried", "down")
            $ ccg1 = 22
            call her_main("A little too much...", "soft", "happy", "base", "R")
            m "How so?"
            call her_main("Well...", "soft", "happy", "base", "R")
            call her_main("She might have started...")
            $ ccg1 = 23
            call her_main("Playing with herself...", "grin", "narrow", "annoyed", "up")
            with hpunch
            with kissiris
            g4 "Yes, keep going slut!"
            call her_main("As I was \"practising\" on her arm, she might have...", "open", "base", "base", "R")
            $ ccg1 = 24
            call her_main("Orgasmed...", "soft", "narrow", "annoyed", "up")
            g4 "[hermione_name], you little slut!"
            $ ccg1 = 23
            call her_main("It was just practice, nothing else!", "grin", "happyCl", "worried", "mid", emote="sweat")
            call her_main("Err... I mean...", "angry", "wink", "base", "mid")
            $ ccg1 = 21
            call her_main("It's not like I enjoyed it or anything...", "angry", "narrow", "base", "down")
            m "Yes, yes... you're not a slut at all..."
            m "*Mmm*...{w=0.4} Why don't you spit on it a little..."
            m "Oh, yes..."
            $ ccg1 = 24
            call her_main("...............", "base", "narrow", "worried", "down")

    if hg_pf_titjob.points == 1:
        jump hg_pf_titjob_2_cumming
    else: # Repeat
        jump hg_pf_titjob_2_continue

label hg_pf_titjob_2_continue:
    call her_chibi_scene("tj", trans=d5)

    call bld
    m "Yes... Keep stroking it."
    $ ccg1 = 23
    call her_main("..............", "angry", "wink", "base", "mid", ypos="head")
    m "Now I want you to say..."

    menu:
        m "..."
        "{size=-4}\"I love teasing my father with my big tits.\"{/size}":
            $ ccg1 = 25
            call her_main("I do not!", "angry", "narrow", "base", "down", ypos="head")
            m "I know. Just say it."
            $ ccg1 = 22
            call her_main("My father? That's gross, [genie_name]! How could you suggest that I would want to fu--", "soft", "narrow", "annoyed", "up")
            m "Come on...{w=0.3} Just make something up."
            call her_main("...........", "angry", "wink", "base", "mid")
            call her_main("Fine...", "open", "narrow", "worried", "down")
            $ ccg1 = 21
            call her_main("Sometimes when I hug him...")
            call her_main(".......")
            m "Go on [hermione_name]..."
            $ ccg1 = 22
            call her_main("I press my tits against him...", "soft", "narrow", "annoyed", "up")
            m "Do you think he enjoys it?"
            call her_main("I'm not sure...", "annoyed", "base", "base", "mid")
            call her_main("I think so...", "soft", "happy", "base", "R")
            $ ccg1 = 23
            call her_main("It always seems like he's trying to cover his crotch afterwards...", "base", "closed", "base", "mid")
            call her_main("He keeps reminding me I'm too old for hugs...", "annoyed", "closed", "base", "mid")
            call her_main("But I don't care... I make sure to give him a big one every night before I go to bed anyway...")
            call her_main("So when I've gone to bed he can't help but think of me...", "base", "narrow", "worried", "down")
            call her_main("And how good my tits felt...", "grin", "narrow", "base", "dead")
            $ ccg1 = 24
            call her_main("Pressed against him...", "soft", "narrow", "annoyed", "up")
            m "That's it slut."
            $ ccg1 = 22
            call her_main("If I feel like teasing him a bit more I will give him a kiss on the forehead...", "soft", "happy", "base", "R")
            $ ccg1 = 23
            call her_main("Making sure that he can see down my blouse...", "grin", "happyCl", "worried", "mid", emote="sweat")
            call her_main("{heart}{heart}{heart}")
            $ ccg1 = 25
            call her_main("But all of that is not true of course!", "open", "base", "base", "mid")
            $ ccg1 = 22
            call her_main("None of that happens! It was just for you to imagine!")
            m "Right..."

        "{size=-4}\"I love teasing my schoolmates with my perfect tits.\"{/size}":
            $ ccg1 = 23
            call her_main("I love teasing my schoolmates with my perfect tits...", "soft", "narrow", "annoyed", "up", ypos="head")
            m "Of course you do..."
            call her_main("I love the jealous looks from the other girls...", "base", "narrow", "worried", "down")
            m "Why wouldn't they be jealous..."
            $ ccg1 = 21
            call her_main("I especially love teasing Ron and harry during breakfast...", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 22
            call her_main("Sometimes I'll walk around with only one button done up...", "base", "squint", "base", "mid")
            $ ccg1 = 23
            call her_main("Other times I'll just wear my top with nothing on underneath...")
            m "And how does that make you feel?"
            call her_main("So good...", "silly", "narrow", "base", "dead")
            call her_main("This one time, when walking back from your office at night, I was barely even covering them...", "angry", "wink", "base", "mid")
            call her_main("I rounded a corner and--", "soft", "narrow", "annoyed", "up")
            $ ccg1 = 24
            call her_main("A second year boy ran head first into them...", "grin", "narrow", "annoyed", "up")
            m "Head first into your first class tits?"
            call her_main("All I could see was the top of his head...", "grin", "narrow", "base", "dead")
            m "What did he do?"
            call her_main("He immediately attempted to pull away...")
            m "attempted?"
            $ ccg1 = 22
            call her_main("Well...{w=0.4} I may have held him there...", "base", "narrow", "base", "mid_soft")
            call her_main("Just for a little bit...", "base", "narrow", "worried", "down")
            $ ccg1 = 23
            call her_main("To make sure he knew it was okay...", "base", "squint", "base", "mid")
            m "I'm sure that's why, you little slut."
            $ ccg1 = 22
            call her_main("I think I might have broken him though...", "base", "narrow", "worried", "down")
            $ ccg1 = 21
            call her_main("Because once I'd let him go he didn't say anything... He just took a few slow steps backwards, turned and scurried away.", "soft", "narrow", "annoyed", "up")
            m "I bet I know where he went..."
            $ ccg1 = 23
            call her_main("So do I...", "soft", "narrow", "annoyed", "up")

    jump hg_pf_titjob_2_cumming

label hg_pf_titjob_2_cumming:
    call her_chibi_scene("tj", trans=d5)

    call bld
    m "*Hmm*..."
    m "I love your perfect tits!"
    $ ccg1 = 22
    call her_main("Thank you [genie_name].", "soft", "narrow", "annoyed", "up", ypos="head")
    $ ccg1 = 23
    call her_main("Shall I rub them some more then?")
    call nar(">Hermione presses her tits together against your cock and begins rubbing it rapidly...")
    m "Oh, yes!!!"
    stop music fadeout 1.0
    g4 "{size=-5}(Almost there! Ready or not...){/size}"

    menu:
        m "..."
        "-Cum in her mouth-":
            call bld
            g4 "Take this, whore!"
            $ ccg1 = 25
            call her_main("What are you--", "angry", "wink", "base", "mid", ypos="head")

            call her_chibi_scene("tj_mouth", trans=d5)
            pause.8

            call bld
            call nar(">With a final thrust, the sensation of Hermione's wet mouth drives you over the edge.")
            call cum_block
            g4 "{size=+5}*ARGH*! YES!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 26

            call her_chibi_scene("tj_cum_in", trans=d5)
            pause.8

            call her_main("!!!!!!!!!!!", "full", "wide", "base", "stare")
            g4 "*Argh*! You whore!"
            call her_main("{heart}{heart}{heart}", "full_cum", "narrow", "base", "dead")
            call cum_block

            g4 "*Argh*! you big-titted slut! Take it all!"
            call her_main("...............", "full_cum", "narrow", "base", "dead")
            m "............"

            call her_chibi_scene("tj_cum_in_done", trans=d5)
            pause.8

            call bld
            m "Okay, I think I am done..."
            call her_main("..............", "full_cum", "narrow", "base", "dead")
            call her_main("........", "full_cum", "narrow", "base", "dead")
            call her_main("...", "full_cum", "narrow", "base", "dead")

            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            $ ccg1 = 27
            call her_main("*GULP*", "cum", "happyCl", "worried", "mid") #play noise here

            call her_chibi_scene("tj_idle", trans=d5)
            pause.8

            call bld
            call nar(">Hermione releases your cock from between her tits.")

            if game.daytime:
                call her_main("Well then, I think I'd better go... my classes are about to begin.", "base", "base", "base", "mid")
            else:
                call her_main("Well then, I think I'd better go... It's getting late.", "base", "base", "base", "mid")
            m "So you're fine with swallowing now?"
            call her_main("What?", "open", "narrow", "worried", "down")
            call her_main("Oh. I suppose so...", "grin", "base", "base", "R")
            call her_main("I mean... it doesn't taste that bad and I don't have to clean up afterwards.", "base", "happyCl", "base", "mid")
            m "*Hmm*... You sure you wouldn't like people seeing your tits covered in cum..."
            call her_main("What? Walk around school covered in your cum, [genie_name]?", "angry", "wink", "base", "mid")

            if her_tier < 6:
                call her_main("With all due respect, [genie_name]...", "upset", "closed", "base", "mid")
                call her_main("I don't plan on getting a reputation as a cum-loving whore...", "angry", "wink", "base", "mid")
                call her_main("Not like those Slytherin girls...", "angry", "narrow", "angry", "R")
            else:
                call her_main("*Hmm*...", "soft", "happy", "base", "R")
                call her_main("Maybe if you ask nicely...", "soft", "narrow", "base", "mid_soft")
            call her_main("Will that be all, [genie_name]?", "base", "closed", "base", "mid")

        "-Cum on her tits-":
            call her_chibi_scene("tj_pause", trans=d5)

            call bld
            g4 "Here! Take this you big-titted whore!"
            with hpunch
            g4 "*ARGH*!"
            $ ccg1 = 25
            call her_main("What? Already?!", "shock", "wide", "base", "stare", ypos="head")
            g4 "Yeah, your tits felt great slut!"
            call cum_block

            call her_chibi_scene("tj_cum_on", trans=d9)
            pause.8

            $ ccg1 = 30
            $ hermione.set_cum(breasts="light")

            call bld
            g4 "{size=+5}*ARGH*! YES!!!{/size}"

            $ hermione.set_cum(breasts="heavy")

            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")

            $ ccg1 = 31
            call her_main(".......................", "angry", "wide", "base", "stare")

            $ ccg1 = 32
            call her_chibi_scene("tj_cum_on_done", trans=d9)
            pause.8

            call bld
            m "*Aghhh*... I feel so much lighter now..."
            $ ccg1 = 33
            call her_main(".......................", "base", "narrow", "base", "down")

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 35
            call her_main("[genie_name]!", "open", "happyCl", "worried", "mid")
            m "What?"
            call her_main("You've covered my chest in cum...", "angry", "happyCl", "worried", "mid")
            $ ccg1 = 34
            call her_main("There's so much...", "open", "base", "base", "R")
            m "It's your fault, [hermione_name]!"
            call her_main("My fault?", "angry", "base", "base", "mid")
            m "Yes! It's those perfect tits of yours..."
            m "They just felt too good..."
            $ ccg1 = 36
            call her_main("Oh...", "shock", "wide", "base", "stare")
            call her_main("Well, If that's the reason then I suppose it's not too bad...", "soft", "narrow", "base", "down")
            $ ccg1 = 37
            call her_main("I'll just wipe it off and hope that nobody will notice...", "upset", "closed", "base", "mid")
            m "You could lick them clean..."
            if her_tier < 6:
                call her_main("You want me to lick your cum off my tits?", "soft", "narrow", "annoyed", "up")
                call her_main("I don't think so, [genie_name]...", "soft", "narrow", "annoyed", "up")
            else:
                call her_main("*Hmm*...", "soft", "happy", "base", "R")
                call her_main("Next time maybe... If you ask nicely...", "grin", "happyCl", "base", "mid_soft")
            call her_main("Will that be all, [genie_name]?", "base", "closed", "base", "mid")

    jump end_hg_pf_titjob
