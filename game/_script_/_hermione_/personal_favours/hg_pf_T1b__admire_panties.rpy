

### Admire Panties ###

label hg_pf_admire_panties:

    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"

    if hg_pf_admire_panties.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 10
    $ hg_pf_admire_panties.start()

    # End Event
    label end_hg_pf_admire_panties:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.wear("all")

    hide screen blkfade
    if her_tier <= 2:
        call her_main("..................", "annoyed", "base", "base", "R", xpos="mid", ypos="base", trans=fade)
    elif her_tier <= 5:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        call her_main("", "smile", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=fade)

    # Points
    if her_tier <= 3 and current_payout > 0:
        $ gryffindor += current_payout
        m "{number=current_payout} points to Gryffindor, [hermione_name]. Well done."

    if hg_pf_admire_panties.counter == 1: # First time
        call her_main("Another {number=current_payout} points...", "base", "narrow", "worried", "down")
        call her_main("Can't wait to tell the guys!", "smile", "happyCl", "base", "mid")
        call her_main("Except that I can't actually tell them about any of this...", "annoyed", "narrow", "angry", "R")

    pause 1.0
    if daytime:
        call her_main("Well, my classes are about to start...", "open", "closed", "base", "mid")
    else:
        call her_main("It's getting pretty late, [genie_name]...", "open", "closed", "base", "mid")
    call her_main("Will this be all?", "open", "base", "base", "mid")
    m "Yes, you can go now."

    # Hermione leaves
    call her_walk("door", "base")

    if her_tier > 3:
        her "What about my points?"
        her "Eh, Who cares. It's only {number=current_payout} points..."

    call her_chibi("leave")


    # Increase level
    if her_tier == 1:
        if her_whoring < 3: # Points til 3
            $ her_whoring += 1

    elif her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    elif her_tier == 3: # No panties!
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    jump end_hermione_event

### Tier 1 ###

# Hermione reluctantly lifts her skirt for you.
# Event 1 (i) - Hermione is shocked about your suggestion.
# Event 2 (r) - Hermione still can't believe what you ask her to do.

label hg_pf_admire_panties_T1_intro_E1:
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."
    call her_main("My... panties...?", "open", "base", "base", "mid")
    call her_main("[genie_name]!", "angry", "base", "angry", "mid")
    m "I know, I know, this a little weird..."
    call her_main("{size=+7}A little !?{/size}", "shock", "wide", "base", "stare")
    her "This is completely inappropriate!"
    m "Listen, we need to go through this phase before we get to the good stuff, alright?"
    call her_main("The \"good stuff\"? [genie_name], I don't understand...", "angry", "base", "base", "mid")
    m "What don't you understand, [hermione_name]?"
    m "Do you need these points or not?"
    call her_main("I do...", "disgust", "base", "base", "down")
    m "Show them to me then..."
    call her_main(".............", "angry", "base", "angry", "mid")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1_E1:
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."
    call her_main("This again?", "angry", "base", "angry", "mid")
    m "Yes. Show them to me..."
    call her_main(".............", "angry", "base", "angry", "mid")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1: # Call label
    call hide_characters
    hide screen bld1
    with d3

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("bottom")
    call her_chibi("lift_skirt","mid","base")
    with d3

    call ctc

    call play_music("playful_tension")
    show screen blktone
    call her_main(".....................", "angry", "base", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    call ctc

    menu:
        "-Stare at her face-":
            ">You study Hermione's face--"
            ">Wondering what's going through her mind right now."
            call her_main(".......................", "angry", "narrow", "annoyed", "mid", emote="angry")

        "-Stare at her panties-":
            ">It's plain girlish underwear, nothing that an ordinary girl wouldn't wear."

    if hg_pf_admire_panties.counter > 1: # Second time
        call her_main(".......................", "angry", "narrow", "base", "R", emote="angry")
    else: # First time
        call her_main(".......................", "angry", "narrow", "annoyed", "mid", emote="angry")

    call ctc
    return

### Tier 2 ###

# Hermione lifts her skirt for you.
# Event 1 (i) - Hermione is embarrassed about what she's about to do.
# Event 2 (r) - Hermione is still not happy.

label hg_pf_admire_panties_T2_intro_E1:
    call her_main("So, what will it be, [genie_name]?")
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."

    if hg_pf_admire_panties.counter == 1:
        call her_main("My Panties?!", "clench", "base", "worried", "mid")
    else:
        call her_main("Oh... again?", "annoyed", "base", "worried", "R")

    m "Just do it..."
    call her_main("..................", "annoyed", "base", "worried", "R")

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T2_E1:
    call her_main("What will it be, [genie_name]?")
    m "I'd like you to show me your panties again."
    call her_main("..................", "annoyed", "base", "worried", "R")
    call her_main("Alright...", "open", "base", "worried", "R")

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T2: # Call label

    call hide_characters
    hide screen bld1
    with d3

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("bottom")
    call her_chibi("lift_skirt","mid","base")
    with d3

    call play_music("playful_tension")
    show screen blktone
    call her_main("Here, [genie_name]...", "base", "base", "base", "mid", xpos="mid", ypos="base")
    call ctc

    menu:
        "\"You don't look too embarrassed...\"":
            call her_main("That's not true...", "base", "happy", "base", "mid")
            call her_main("But it is a small price to pay if it means the Gryffindor house keeps the cup this year.", "base", "base", "base", "R")
            her "I know everyone will be so happy..."

        "\"I like your panties...\"":
            call her_main("Thank you, [genie_name]...", "base", "happy", "base", "mid")

        "-Keep looking into her eyes-":
            call her_main("..............................", "soft", "base", "base", "mid")
            her "...........................?"
            call her_main("................................", "grin", "base", "base", "R")
            call her_main("[genie_name], please... You are embarrassing me.", "grin", "happyCl", "worried", "mid",emote="sweat")
    call ctc
    return

### Tier 3 ###

# Event 1 (i) - Hermione is not wearing her panties.
# Event 2 (r) - No panties. You get to call her a slut.
# Event 3 (r) - Panties may or may not be equipped. Hermione asks to remove them or keep them on.

label hg_pf_admire_panties_T3_intro_E1:
    if hg_pf_admire_panties.counter == 1:
        m "[hermione_name], I'd like you to show me your panties, if that's not too much trouble."
    else:
        m "[hermione_name], I'd like you to show me your panties again, if that's not too much trouble."
    call her_main("Oh...", "open", "narrow", "worried", "down")
    call her_main("Okay...", "base", "narrow", "base", "down", cheeks="blush")

    call hide_characters
    hide screen bld1
    with d3

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("bottom", "panties")
    call her_chibi("lift_skirt","mid","base")
    with d3
    pause.8

    call her_main("..........................", "base", "base", "base", "R", cheeks="blush", ypos="head", flip=False)
    g4 "!!?"

    show screen blktone
    call her_main("", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=fade)
    call ctc

    # No Panties!
    g4 "Where are your panties, [hermione_name]?"
    call her_main("Oh, lately I just don't feel like wearing them...", "base", "narrow", "worried", "down", cheeks="blush")

    menu:
        "\"You little slut!\"":
            her "*Hmm*..."
            call her_main("I suppose I am...", "base", "narrow", "base", "mid_soft")
            her "Do I get extra points for that?"

            menu:
                "\"Absolutely!\"":
                    $ current_payout += 10
                    m "Ten additional points to Gryffindor!"
                    call her_main("Thank you, [genie_name]!", "base", "happyCl", "worried", "mid")
                    call ctc

                "\"Absolutely not!\"":
                    $ her_mood +=5
                    call her_main("Why not!?", "scream", "closed", "angry", "mid")
                    m "Sluts aren't getting paid."
                    m "That's what makes them sluts."
                    call her_main("Well are you even going to pay me {number=current_payout} points?", "annoyed", "base", "angry", "mid")
                    m "Are you a slut or are you a prostitute?"
                    her "{size=-4}... a slut {/size}"
                    m "Good girl."
                    $ current_payout = 0 # No points for sluts
                    call ctc

        "\"Good! {number=current_payout} points!\"":
            pass

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T3_E1:
    m "[hermione_name], I'd like you to show me your panties again if possible."
    call her_main("Oh...", "open", "narrow", "worried", "down")
    call her_main("Well, that might be an issue...", "base", "narrow", "base", "down", cheeks="blush")

    call hide_characters
    hide screen bld1
    with d3

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("bottom", "panties")
    call her_chibi("lift_skirt","mid","base")
    with d3
    pause.8

    show screen blktone
    call her_main("", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")
    call ctc

    # No Panties!
    g9 "No panties again, [hermione_name]?"
    call her_main("Well... what's the point if they're just going to be in the way all the time...", "base", "narrow", "worried", "down", cheeks="blush")

    menu:
        "\"You little slut!\"":
            her "*Hmm*..."
            call her_main("I suppose I am...", "base", "narrow", "base", "mid_soft")
            her "Do I get extra points this time?"

            menu:
                "\"Absolutely!\"":
                    m "Absolutely!"
                    $ current_payout += 10
                    m "Ten additional points to Gryffindor!"
                    call her_main("Thank you, [genie_name]!", "base", "happyCl", "worried", "mid")
                    call ctc

                "\"Absolutely not!\"":
                    $ her_mood +=5
                    call her_main("Why not!?", "scream", "closed", "angry", "mid")
                    m "Sluts aren't getting paid."
                    m "That's what makes them sluts."
                    call her_main("Well are you even going to pay me {number=current_payout} points?", "annoyed", "base", "angry", "mid")
                    m "Are you a slut or are you a prostitute?"
                    her "{size=-4}... a slut {/size}"
                    m "Good girl."
                    $ current_payout = 0 # No points for sluts
                    call ctc

        "\"Good! {number=current_payout} points!\"":
            pass


    call her_main("I could put my panties back on for you, if you'd like that, Sir?", "open", "base", "base", "R")

    menu:
        "\"Yes, put them back on!\"":
            call her_main("Alright, [genie_name].", "base", "narrow", "base", "mid_soft")
            hide screen hermione_main
            with d3
            ">Hermione puts on her panties."

            if hermione.is_worn("panties") == False:
                $ hermione.wear("panties")
            else:
                $ hermione.equip(her_panties_base1)
            call her_chibi("lift_skirt")

            call her_main("", "base", "narrow", "base", "mid_soft")
            call ctc

            call her_main("I hope you like them...", "soft", "base", "base", "R")

        "\"No, keep them off!\"":
            call her_main("Of course, [genie_name].", "soft", "narrow", "annoyed", "up")
            $ hermione.unequip("panties")
            call ctc

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T3_E2:

    m "[hermione_name], show me those cute panties of yours again."
    call her_main("Oh...", "open", "narrow", "worried", "down")
    call her_main("Okay...", "base", "narrow", "base", "down", cheeks="blush")

    call hide_characters
    hide screen bld1
    with d3

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("bottom")
    call her_chibi("lift_skirt","mid","base")
    with d3
    pause .8

    show screen blktone
    call her_main("", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")
    call ctc

    # No Panties.
    if not hermione.is_worn("panties"):
        g9 "Where are your panties, [hermione_name]?"
        call her_main("I have them here in my pocket...", "open", "base", "base", "R")
        call her_main("Most of the time I just leave them in the Gryffindor common room...", "open", "base", "base", "R")
        call her_main("But I got them with me this time.", "open", "base", "base", "R")
        call ctc

        call her_main("If you'd like, Sir, I could put my panties back on for you.", "soft", "narrow", "base", "mid_soft")

        menu:
            "\"Yes, put them back on!\"":
                call her_main("Alright, [genie_name].", "base", "narrow", "base", "mid_soft")
                hide screen hermione_main
                with d3
                ">Hermione puts on her panties."

                if hermione.is_worn("panties") == False:
                    $ hermione.wear("panties")
                else:
                    $ hermione.equip(her_panties_base1)

                call her_chibi("lift_skirt")
                call her_main("", "base", "narrow", "base", "mid_soft")
                call ctc

                call her_main("I hope you like them...", "soft", "base", "base", "R")

            "\"No, keep them off!\"":
                call her_main("Of course, [genie_name].", "soft", "narrow", "annoyed", "up")
                $ hermione.unequip("panties")
                call ctc

    else:
        call her_main("Do you like them, [genie_name]?", "base", "narrow", "base", "mid_soft")
        m "Indeed I do, [hermione_name]..."
        call ctc

        call her_main("I could take them off, if you'd like that, [genie_name].", "open", "base", "base", "R")

        menu:
            "\"Yes, Take them off!\"":
                call her_main("Alright, [genie_name].", "soft", "narrow", "annoyed", "up")
                m "And keep them off from now on!"
                call her_main("Whatever you want, [genie_name].", "base", "narrow", "base", "mid_soft")
                hide screen hermione_main
                with d3
                call nar(">Hermione takes off her panties.")

                $ hermione.unequip("panties")
                call her_chibi("lift_skirt")

                call her_main("", "base", "narrow", "base", "mid_soft")
                call ctc

                call her_main("I hope you like it, [genie_name]...", "angry", "wink", "base", "mid")

            "\"No, keep them on!\"":
                call her_main("Sure, [genie_name].", "base", "narrow", "base", "mid_soft")
                call ctc

    jump end_hg_pf_admire_panties
