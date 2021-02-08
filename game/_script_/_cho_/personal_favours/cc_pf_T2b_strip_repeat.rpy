
##############
### Tier 3 ###
##############

## Tier 3 - Summon Tonks ##

label cc_pf_strip_T3_tonks:

    # Setup
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    $ tonks_cho_name = renpy.random.choice( ("Sweetie", "babe", "Honey") )
    # All character's clothes get saved in case we need to change any.
    # Cho and Tonks won't change their clothes.

    $ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ her_outfit_last.save() # Store current outfit.

    #$ cho.equip(cho_outfit_default)
    #$ tonks.equip(ton_outfit_default)
    $ hermione.equip(her_outfit_default)

    call cho_chibi("stand", "desk", "base", flip=False)

    hide screen blkfade
    call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=fade)

    # Intro
    if doppler_done == False and succubus_done == False: # First time only.
        m "About your teacher, Professor Tonks..."
        m "That ability she has, it's quite... interesting, don't you think?"
        call cho_main("It is! And exceptionally rare as well!", "grin", "happyCl", "base", "mid")
        call cho_main("I only ever heard about this type of transfiguration ability once -- during one of Professor McGonagall's lessons...", "open", "base", "raised", "mid")
        call cho_main("She seemed kind of annoyed by the fact that there are people with natural abilities to change their appearance like that.", "annoyed", "base", "base", "R")
        g9 "Well, not everyone can be as naturally handsome as me."
        call cho_main("That... Is not what I meant.", "open", "closed", "angry", "mid")
        m "I wonder if she's the only person here who has this \"Metamorphic\" ability..."
        call cho_main("I hope so...", "annoyed", "base", "base", "mid")
        m "You do?"
        call cho_main("You've seen the kind of thing she uses her ability for, haven't you?", "open", "narrow", "base", "mid")
        call cho_main("Surely when you decided to tell me her secret -- you considered what could happen if I told the other students about it?", "open", "closed", "base", "mid")
        g4 "I...{w=0.2} Of course!"
        call cho_main("Don't worry, I won't tell anyone...", "open", "narrow", "base", "mid")
        call cho_main("Though I'd suggest to keep it a secret from Granger at all cost!", "mad", "narrow", "angry", "mid")
        call cho_main("I'm confident she'd come up with some annoying rule to try and keep her teacher in check...", "annoyed", "narrow", "angry", "mid")
        m "Right..."
        call cho_main("Well, I'm glad to know that you trust me with something like this, [cho_genie_name].", "smile", "happyCl", "base", "mid")
        call cho_main("It'd be quite difficult for her to pretend to be someone else, if everybody knew about it.", "annoyed", "base", "base", "mid")
        m "..."
        call cho_main("I sure am glad there isn't another student with her abilities...", "annoyed", "narrow", "base", "R")
        g9 "*Ha-ha*, yeah..."
        m "Another student -- preferably female -- with her abilities...{w=0.5} That would be horrible..."
        g9 "(Not...)"
        call cho_main("Yes... If they somehow found out about Tonks, she'd surely receive all the blame.", "angry", "narrow", "raised", "mid")
        g4 "..."
        call cho_main("...", "annoyed", "narrow", "base", "mid")
        m "Let's just call her up here for now..."
        g9 "I'm sure she'll make it well worth it for you to continue keeping her secret safe."
        call cho_main("Yes, [cho_genie_name]...", "smile", "narrow", "base", "mid", cheeks="blush") #glancing away #blush

    # Repeat
    else:
        m "Let me summon her real quick."
        call cho_main("Yes, [cho_genie_name].", "base", "base", "base", "mid")

    call play_music("stop")
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    # You summon Tonks.
    call cho_chibi("stand", "desk", "base", flip=True)
    with d3
    pause .8

    # Tonks enters.
    call play_sound("door")
    call ton_chibi("stand", "door", "base")
    with d3
    pause .5

    # Tonks walks next to Cho.
    call ton_walk(540, "base")

    call play_music("tonks")
    call cho_main("", "base", "narrow", "worried", "L", cheeks="blush", xpos="left", ypos="base", flip=True)
    call ton_main("Hello, Professor.", "soft", "narrow", "base", "mid", xpos="right", ypos="base", flip=False)
    call ton_main("Miss Chang.", "base", "narrow", "raised", "L")

    # Intro
    if doppler_done == False and succubus_done == False: # First time only.
        m "Didn't fancy taking the fireplace this time?"
        call ton_main("Not today... I only use floo powder when I'm in a hurry.", "open", "base", "base", "mid")


    ## Tonks and Cho strip for you ##
    call ton_main("So...{w=0.3} What do you have planned for us today, Professor?", "base", "narrow", "base", "mid")
    m "*Hmm*..."
    g9 "Why don't you tell her what we're doing, Miss Chang?"
    call cho_main("You want me to--", "open", "narrow", "base", "mid")
    g9 "Don't see why not..."
    call cho_main("Of course, Sir.", "soft", "narrow", "base", "downR")

    if doppler_done == False and succubus_done == False: # First time only.
        call cho_main("...", "annoyed", "narrow", "worried", "down", cheeks="blush") # Embarrassed look down.
        call cho_main("The headmaster wants to see us strip for him again...", "open", "narrow", "worried", "L", cheeks="blush")
        if cho.is_worn("robe") or ( cho.is_worn("top") and cho.is_worn("bottom") ):
            pass
        else: # Cho is in her underwear or naked.
            m "Well... A bit of a show should do, seeing what your current state of undress is like..."
            call cho_main("You're the one that requested it...", "annoyed", "narrow", "angry", "down", cheeks="heavy_blush") # small text

        if tonks.is_worn("robe") or ( tonks.is_worn("top") and tonks.is_worn("bottom") ):
            pass
        else: #Tonks in in her underwear or naked.
            call ton_main("*Hmm*...{w=0.3} Who needs clothing anyway?", "horny", "narrow", "base", "L", hair="horny")
            call ton_main("But I'll give you a show if that's what you want...{heart}", "horny", "narrow", "base", "mid", hair="horny")
        g9 "..."

    else: # repeat
        call cho_main("The headmaster wants us to strip for him again.", "base", "narrow", "base", "mid", cheeks="blush")
        call ton_main("Does he now?", "horny", "narrow", "base", "L", hair="horny")
        if cho.is_worn("robe") or ( cho.is_worn("top") and cho.is_worn("bottom") ):
            pass
        else:
            m "Well, since you're not wearing much... I'd at least like a show..."
            call cho_main("Very well...", "annoyed", "narrow", "angry", "down", cheeks="heavy_blush") # small text

        if tonks.is_worn("robe") or ( tonks.is_worn("top") and tonks.is_worn("bottom") ):
            pass
        else: #Tonks in in her underwear or naked.
            call ton_main("Stripping's out of the question for me that's for sure...", "horny", "narrow", "base", "L", hair="horny")
            call ton_main("But I'll give you a good view at the very least...{heart}", "horny", "narrow", "base", "mid", hair="horny")

    call ton_main("Well in that case we shouldn't keep him waiting, should we?", "horny", "narrow", "base", "L", hair="horny")
    call ton_main("After you, [tonks_cho_name].", "horny", "narrow", "base", "L", hair="horny")
    call play_music("stop")

    # Cho and Tonks hop onto the desk.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .1

    show screen blkfade
    with d5


    # Tonks chibi on desk next to Cho's. # Tonks is facing left
    call cho_chibi("stand", flip=True, 314, 366)
    call ton_chibi("stand", flip=False, 370, 360)

    call play_sound("climb_desk")
    pause 2

    hide screen blkfade
    with d5
    pause .8

    call play_music("cho")
    $ cho_zorder = 16 # in front of Tonks # Default is 15.
    $ tonks_zorder = 15 # reset to default.
    call cho_main("", "base", "narrow", "base", "L", cheeks="heavy_blush", xpos=280, ypos="base", flip=True)
    call ton_main("...", "base", "narrow", "raised", "L", hair="horny", xpos=345, ypos="base")

    call ton_main("This feels quite familiar, doesn't it, Miss Chang?", "crooked_smile", "narrow", "raised", "L", hair="horny")
    call cho_main("...", "horny", "narrow", "base", "mid", cheeks="blush")
    call ton_main("Let's not waste any more time...", "horny", "narrow", "base", "L", hair="horny")

    call ton_main("Who of us would you like to start, Professor?", "base", "narrow", "base", "mid", hair="horny")
    m "*Hmm*..."

    menu:
        "\"Miss Chang will go first.\"":
            call cho_main("...", "horny", "narrow", "base", "mid", cheeks="blush")
            $ cho_position = 1 # Cho's current positon is in the middle.

            jump cc_pf_strip_T3_tonks.strip_cho

        "\"You go first, Miss Tonks!\"":
            call ton_main("*Hmm*...", "base", "narrow", "base", "L", hair="horny")
            call ton_main("Saving the best for last, are we?", "base", "narrow", "raised", "mid", hair="horny")
            call cho_main("...", "horny", "narrow", "base", "downR", cheeks="blush")
            $ cho_position = 1 # Cho's current positon is in the middle.

            jump cc_pf_strip_T3_tonks.strip_tonks

        #"\"How about Miss Granger?\"" if doppler_done == True and succubus_done == True:
            #jump cc_pf_strip_T3_tonks.strip_hermione



## Cho Strips ##
label .strip_cho:

    # Check their positions. If Cho stands to the right she'll get moved to the middle.
    if cho_position == 2: # to the right.
        call ton_main("Move between us, Cho.", "soft", "narrow", "shocked", "L", hair="horny")
        call ton_main("That way the headmaster can see you better.", "base", "narrow", "base", "mid", hair="horny")
        call cho_main("Yes, Professor.", "smile", "narrow", "base", "L", cheeks="blush")
        call hide_characters
        hide screen bld1
        with d5
        pause .2

        # Cho stands in the middle, between Genie and Tonks.
        $ cho_position = 1 # middle.
        $ cho_zorder = 16 # in front of Tonks # Default is 15.
        $ tonks_zorder = 15 # reset to default.
        call cho_chibi("stand", flip=True, 314, 366)
        call ton_chibi("stand", flip=False, 370, 360)
        call cho_main("", "base", "narrow", "base", "mid", cheeks="blush", xpos=280, ypos="base", flip=True)
        call ton_main("", "base", "narrow", "base", "mid", hair="horny", xpos=345, ypos="base", flip=False)
        with d5
    call ctc


    # Cho is wearing at least one clothing piece:
    if cho.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        pass
    else: # Cho is already naked.
        call ton_main("Well, since you're not really wearing much already...", "soft", "narrow", "base", "L", hair="horny")
        call ton_main("There isn't that much more for me to help her take off, is there?", "soft", "narrow", "base", "L", hair="horny")
        call cho_main("...", "base", "narrow", "base", "downR", cheeks="heavy_blush")
        pause .2
        $ cho.strip("all")
        with d3

        call cc_pf_strip_T3_tonks.spank_cho

        jump cc_pf_strip_T3_tonks.strip_check # label checks if both are nude.

    # Remove Top and Bottom.
    if cho.is_any_worn("robe", "top", "bottom"):
        call ton_main("Let me help you get out of these clothes, Miss Chang.", "soft", "narrow", "base", "L", hair="horny")
        call cho_main("Yes, Professor.", "base", "narrow", "base", "down", cheeks="heavy_blush")
        call ton_main("", "base", "narrow", "base", "down", hair="horny", xpos=300, ypos="base", flip=False, trans=d5) # moves closer to Cho.
        pause .2

        if cho.is_worn("robe"):
            call play_sound("equip")
            $ cho.strip("robe")
            with d3
            pause .5
            call cho_main("", "horny", "narrow", "raised", "down", cheeks="blush")
            call ctc
        if cho.is_worn("top"):
            call play_sound("equip")
            $ cho.strip("top")
            with d3
            pause .5
            call cho_main("", "horny", "narrow", "raised", "mid", cheeks="blush")
            pause .8
            call nar("Tonks swiftly pulls the girl's top over her chiselled frame.")
            pause .2
        if cho.is_worn("bottom"):
            $ cho.strip("bottom")
            with d3
            pause .5
            call cho_main("", "horny", "narrow", "base", "down", cheeks="blush")
            pause .8
            call nar("A quick tug by her teacher, and Cho's bottoms slips down her muscular thighs.")
            call ctc

    # Remove Bra and Panties.
    if cho.is_any_worn("bra", "panties"):
        call ton_main("I like your underwear Miss Chang... Very cute!", "soft", "narrow", "base", "L", hair="horny")
        call cho_main("", "horny", "narrow", "base", "down", cheeks="heavy_blush")
        call ton_main("", "base", "narrow", "base", "down", hair="horny", xpos=300, ypos="base", flip=False, trans=d5) # moves closer to Cho.

        if cho.is_worn("bra"):
            call ton_main("But...{w=0.3} That bra definitely has to come off.", "soft", "narrow", "angry", "down", hair="horny")
            pause .5
            $ cho.strip("bra")
            with d3
            pause .5
            call cho_main("", "base", "narrow", "raised", "L", cheeks="blush")
            pause .8
            call nar("Tonks effortlessly removes the bra of her student.")
            pause .2
        if cho.is_worn("panties"):
            call cho_main("...", "mad", "narrow", "base", "down", cheeks="blush")
            call ton_main("Wearing panties is so silly, let's take those off... {heart}", "crooked_smile", "narrow", "angry", "down", hair="horny")
            pause .5
            $ cho.strip("panties")
            with d3
            pause .5
            call cho_main("", "horny", "narrow", "base", "down", cheeks="heavy_blush")
            pause .8
            call nar("Eyes fixated onto Cho's lovely Snitch, Tonks slowly pulls the girl's panties down her thighs.")
            pause .2


    # Remove all Cho clothes.
    $ cho.strip("all")
    with d3
    call cho_main("", "base", "narrow", "base", "mid", cheeks="heavy_blush")
    call ctc

    call ton_main("", "base", "narrow", "base", "mid", hair="horny", xpos=345, ypos="base", flip=False) # Tonks moves to her original position.
    with d5

    $ random_number = renpy.random.randint(1, 3)

    if random_number == 1:
        call ton_main("Look at all these muscles!", "horny", "narrow", "raised", "down", hair="horny")
        call ton_main("I mean... I could easily get some muscles as well, but not without cheating...", "open", "closed", "base", "mid", hair="horny")
        call ton_main("I'm quite impressed, Miss Chang.", "base", "narrow", "base", "L", hair="horny")
        call cho_main("Thank you.", "soft", "narrow", "base", "L", cheeks="blush")
    elif random_number == 2:
        call ton_main("You look quite tasty, Miss Chang.", "horny", "narrow", "raised", "down", hair="horny")
        call cho_main("*Ehm*...", "clench", "narrow", "worried", "down", cheeks="heavy_blush")
        call cho_main("Thanks?", "soft", "narrow", "worried", "L", cheeks="heavy_blush")
    else:
        call ton_main("Looks like we're done here, Professor.", "horny", "narrow", "raised", "mid", hair="horny")
        m "Excellent!"
        g9 "I do love watching you two."

    call cc_pf_strip_T3_tonks.spank_cho

    jump cc_pf_strip_T3_tonks.strip_check


## Spank Cho ##
label .spank_cho:
    # Cho should stand next to Genie for this.
    menu:
        m "(...)"
        "-Spank her!-":
            pass
        "-Don't spank her...-":
            return

    call slap_her
    call ton_main("", "crooked_smile", "narrow", "raised", "L", hair="horny")
    call cho_main("!!!", "clench", "wide", "base", "mid", cheeks="heavy_blush") # shocked
    call cho_main("Ouch... Professor!", "silly", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call play_sound("giggle")
    call ton_main("*Giggles*... {heart}{heart}{heart}", "silly", "happyCl", "base", "mid", hair="horny", cheeks="blush")
    call ton_main("...", "base", "narrow", "base", "mid", hair="horny")

    menu:
        m "(...)"
        "-Spank her again!-":
            call slap_her
            call ton_main("", "crooked_smile", "narrow", "base", "mid", hair="horny")
            call cho_main("Professor!", "clench", "wide", "raised", "mid", cheeks="heavy_blush")
            g9 "What? I know you like it."
            call cho_main("I do not...", "annoyed", "narrow", "angry", "mid", cheeks="heavy_blush")

            menu:
                "-Again!-":
                    pass
            call slap_her
            call cho_main("Sir!", "clench", "wide", "base", "mid", cheeks="heavy_blush")
            g9 "I need to get these cushions ready for your next flight!"
            g9 "Spank them tender so you're more comfortable on your broom-stick!"
            call cho_main("I don't think that will be necessary.", "open", "happyCl", "angry", "mid", cheeks="blush")

            menu:
                "-Slap it hard!-":
                    pass
            call slap_her
            call cho_main("", "clench", "wide", "raised", "mid", cheeks="heavy_blush")
            call ton_main("", "grin", "narrow", "base", "mid", hair="horny", cheeks="blush")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .3
            call slap_her
            call cho_main("*Owww*...", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush")
            call cho_main("That's enough...", "annoyed", "narrow", "angry", "mid", cheeks="blush")
            g9 "You'd probably enjoy it more if your other teacher were to spank you, wouldn't you?"
            call cho_main("...", "annoyed", "narrow", "base", "L", cheeks="blush")
            call ton_main("", "base", "narrow", "base", "L", hair="horny")
            call cho_main("*Ehm*...", "annoyed", "narrow", "raised", "mid", cheeks="heavy_blush")
            call play_sound("giggle")
            call ton_main("*Giggles*... {heart}{heart}{heart}", "base", "happyCl", "base", "mid", hair="horny", cheeks="heavy_blush")
            call ton_main("I won't be gentle on you either, Miss Chang.", "soft", "narrow", "base", "L", hair="horny")
            call cho_main("...", "horny", "narrow", "worried", "down", cheeks="heavy_blush")

            return

        "-Ask Tonks to spank her.-":
            g9 "Miss Tonks, If you may..."
            call ton_main("With pleasure!", "grin", "narrow", "angry", "mid", hair="horny")
            call cho_main("But-- Professor Tonks!", "clench", "base", "worried", "L", cheeks="heavy_blush")
            call ton_main("Don't worry, [tonks_cho_name]. You'll learn to love it! {heart}", "horny", "narrow", "base", "L", hair="horny")
            call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
            call ton_main("Now, turn around for me, please.", "soft", "narrow", "base", "L", hair="horny")
            call cho_main("...", "clench", "narrow", "worried", "down", cheeks="heavy_blush")
            pause .2

            # Cho turns around.
            call cho_chibi("stand", flip=False, 325, 366)
            call ton_chibi("stand", flip=False, 360, 360)
            call ton_main("", "base", "narrow", "base", "down", hair="horny", xpos=325, ypos="base", flip=False)
            call cho_main("", "disgust", "narrow", "worried", "down", cheeks="blush", xpos=235, ypos="base", flip=False, trans=d5)
            pause .5

            call slap_her
            call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="blush")
            call ton_main("Such a firm ass you have, Miss Chang!", "horny", "narrow", "raised", "down", hair="horny")
            call cho_main("", "mad", "narrow", "worried", "downR", cheeks="blush")
            call ctc

            m "..."
            call ton_main("Lovely indeed... {heart}", "grin", "narrow", "base", "down", hair="horny")
            m ".........."
            m "I don't hear any spanking."
            call ton_main("Don't worry, Sir. I'll get to that eventually... {heart}", "open", "narrow", "annoyed", "mid", hair="horny")
            m "Building up the suspense are--"
            call slap_her
            call cho_main("", "horny", "narrow", "worried", "downR", cheeks="heavy_blush")
            call ton_main("You should get a good feel of it first, before you--", "crooked_smile", "narrow", "annoyed", "down", hair="horny")
            call slap_her
            call cho_main("", "mad", "wide", "base", "mid", cheeks="heavy_blush")
            call ton_main("", "horny", "narrow", "angry", "down", hair="angry")
            pause .6
            call slap_her
            pause .3
            call slap_her
            pause .4
            call ton_main("", "horny", "narrow", "angry", "down", hair="horny")
            call cho_main("Please!", "clench", "happyCl", "base", "mid", cheeks="heavy_blush")
            call ton_main("What's wrong, Miss Chang?", "open", "narrow", "angry", "mid", hair="horny")
            call ton_main("You never get this flustered when you get hit by a bludger...", "open", "narrow", "angry", "down", hair="horny")
            call slap_her
            call ton_main("Surely a bit of a spanking isn't enough for you to...", "horny", "narrow", "base", "mid", hair="horny")
            call cho_main("...", "clench", "narrow", "worried", "down", cheeks="blush")
            call ton_main("Ask me nicely and I'll do it again, [tonks_cho_name].", "crooked_smile", "narrow", "base", "mid", hair="horny")
            g9 "Go on, Cho... Ask your teacher to spank you."
            call cho_main("...", "disgust", "narrow", "worried", "downR", cheeks="heavy_blush")
            call cho_main("Please spank me again, Professor.", "soft", "narrow", "worried", "R", cheeks="heavy_blush")
            call ton_main("Of course sweetie...{w=0.4} Since you're asking so nicely.", "base", "narrow", "base", "L", hair="horny")
            call ton_main("", "base", "narrow", "base", "down", hair="horny")
            call slap_her
            call cho_main("", "angry", "narrow", "worried", "up", cheeks="heavy_blush")
            pause .5
            call slap_her
            pause .4
            call slap_her
            call cho_main("", "horny", "happyCl", "worried", "mid", cheeks="heavy_blush")
            call ctc

            call cho_main("...", "horny", "narrow", "base", "R", cheeks="heavy_blush")
            call ton_main("*Hmm*...", "annoyed", "narrow", "shocked", "down", hair="horny")
            call ton_main("A well behaved girl like you should be rewarded. {heart}", "crooked_smile", "narrow", "raised", "L", hair="horny")
            call ton_main("Ten points for Ravenclaw, Miss Chang.", "soft", "narrow", "base", "L", hair="horny")
            $ ravenclaw += 10
            call cho_main("Thank you I guess--", "crooked_smile", "narrow", "worried", "R", cheeks="heavy_blush")
            call ton_main("", "horny", "narrow", "angry", "down", hair="horny")
            call slap_her
            call cho_main("!!!", "clench", "wide", "base", "mid", cheeks="heavy_blush")
            call cho_main("Ouch...", "horny", "narrow", "worried", "R", cheeks="heavy_blush")
            pause .2

            # Cho turns around.
            call cho_chibi("stand", flip=True, 314, 366)
            call ton_chibi("stand", flip=False, 370, 360)
            call ton_main("", "base", "narrow", "base", "mid", hair="horny", xpos=345, ypos="base", flip=False)
            call cho_main("", "annoyed", "narrow", "base", "mid", cheeks="blush", xpos=280, ypos="base", flip=True, trans=d5)
            pause .8

            return

    return



## Tonks Strips ##
label .strip_tonks:

    # Check their positions. If Tonks stands to the right she'll get moved to the middle.
    if cho_position == 1: # middle.
        call ton_main("Cho, would you mind if I stood between you two?", "open", "narrow", "base", "L", hair="horny")
        call ton_main("I'd like to give the headmaster a better view of my body.", "base", "narrow", "base", "mid", hair="horny")
        call cho_main("Not at all, Professor.", "smile", "narrow", "base", "L", cheeks="blush")
        call ton_main("Thank you, [tonks_cho_name].", "soft", "narrow", "shocked", "L", hair="horny")
        call hide_characters
        hide screen bld1
        with d5
        pause .2

        # Tonks stands in the middle, between Genie and Cho.
        $ cho_position = 2 # to the right.
        $ tonks_chibi.zorder = 2 # default is 3
        $ cho_zorder = 15 # reset to default.
        $ tonks_zorder = 16 # in front of Cho # Default is 15.
        call cho_chibi("stand", flip=False, 370, 360)
        call ton_chibi("stand", flip=True, 320, 360)
        with d3
        pause .5

        call cho_main("", "base", "narrow", "base", "mid", cheeks="blush", xpos=315, ypos="base", flip=False)
        call ton_main("", "base", "narrow", "base", "mid", hair="horny", xpos=280, ypos="base", flip=True)
        with d5
    call ctc


    # Tonks is wearing at least one clothing piece:
    if tonks.is_worn("robe") or tonks.is_worn("top") or tonks.is_worn("bottom") or tonks.is_worn("bra") or tonks.is_worn("panties"):
        call cho_main("...", "horny", "narrow", "base", "L", cheeks="blush")
        if tonks.is_worn("top"):
            call ton_main("You don't mind if Miss Chang helps me undress, do you, Professor?", "horny", "wink", "base", "mid", hair="horny")
            g9 "Of course not!"
        else:
            call ton_main("Just enjoy the show, Professor...", "horny", "wink", "base", "mid", hair="horny")
        pass
    else: # Tonks is already naked.
        call ton_main("Professor... It seems like I'm naked already...", "soft", "narrow", "base", "L", hair="horny")
        call ton_main("How shameful of me... Am I to get detention now?", "horny", "narrow", "base", "mid", hair="horny")
        g9 "Damn right you are!"
        call cho_main("...", "base", "narrow", "base", "downR", cheeks="heavy_blush")
        pause .2
        $ tonks.strip("all")
        with d3

        call cc_pf_strip_T3_tonks.spank_tonks

        jump cc_pf_strip_T3_tonks.strip_check # label checks if both are nude.

    # Remove Top and Bottom.
    if tonks.is_worn("robe") or tonks.is_worn("top") or tonks.is_worn("bottom"):
        call ton_main("Help me get out of these clothes, Miss Chang.", "soft", "narrow", "base", "L", hair="horny")
        call cho_main("Yes, Professor.", "soft", "narrow", "base", "down", cheeks="blush")
        call cho_main("", "horny", "narrow", "base", "down", cheeks="blush", xpos=315, ypos="base", flip=False, trans=d5) # Cho moves closer to Tonks.
        pause .2

        if tonks.is_worn("robe"):
            call play_sound("equip")
            $ tonks.strip("robe")
            with d3
            pause .5
            call ton_main("", "horny", "narrow", "raised", "down", hair="horny")
            call ctc
        if tonks.is_worn("top"):
            call play_sound("equip")
            $ tonks.strip("top")
            with d3
            pause .5
            call ton_main("", "horny", "narrow", "raised", "mid", hair="horny")
            pause .8
            call nar("Cho eagerly helps her teacher take off her top.")
            pause .2
        if tonks.is_worn("bottom"):
            call ton_main("Remember... Always take your time when undressing in front of somebody.", "soft", "narrow", "base", "L", hair="horny")
            call ton_main("", "base", "narrow", "base", "mid", hair="horny")
            call nar("Slowly, and with gracile movements, Tonks takes off her bottom piece of clothing.")
            $ tonks.strip("bottom")
            with hpunch
            pause .5
            call ton_main("", "horny", "narrow", "raised", "mid", hair="horny", cheeks="blush")
            pause .8
            call nar("And then flicks it out of sigh with one swift motion.")
            call ctc

    # Remove Bra and Panties.
    if tonks.is_worn("bra") or tonks.is_worn("panties"):
        call ton_main("*Hmm*... It's been a while since I had to remove underwear.", "annoyed", "narrow", "base", "down", hair="horny")
        call ton_main("Help me take them off, [tonks_cho_name].", "base", "narrow", "base", "down", hair="horny")
        call cho_main("Of course...", "smile", "narrow", "base", "down", cheeks="blush")
        call cho_main("", "horny", "narrow", "base", "down", cheeks="blush", xpos=315, ypos="base", flip=False, trans=d5) # Cho moves closer to Tonks.

        if tonks.is_worn("bra"):
            call ton_main("Let's get these tits out already!", "base", "narrow", "angry", "mid", hair="horny")
            pause .5
            $ tonks.strip("bra")
            with d3
            pause .5
            call ton_main("", "base", "narrow", "base", "mid", hair="horny")
            pause .8
            call nar("Tonks bares her impressive bosom for you both.")
            pause .2
        if tonks.is_worn("panties"):
            call ton_main("Oh my... what happened to my panties...", "soft", "narrow", "base", "down", hair="horny")
            call ton_main("I can't believe how wet they got!", "clench", "narrow", "shocked", "down", hair="horny")
            pause .5
            $ tonks.strip("panties")
            with d3
            pause .5
            call ton_main("", "horny", "narrow", "angry", "mid", hair="horny")
            pause .8
            call nar("Without much hesitation, Tonks panties are swiftly flung out of sight and out of mind.")
            pause .2

    # Remove all Cho clothes.
    call ton_main("", "base", "narrow", "base", "mid", hair="horny")
    $ tonks.strip("all")
    with d3
    call ctc

    call cho_main("", "base", "narrow", "base", "mid", cheeks="blush", xpos=315, ypos="base", flip=False) # Cho moves to her original position.
    with d5

    $ random_number = renpy.random.randint(1, 3)

    if random_number == 1:
        call ton_main("How immoral for a teacher to do this sort of thing in front of a student...", "open", "closed", "annoyed", "mid", hair="horny")
        call ton_main("You aren't going to report me for my wanton behaviour, are you, Miss Chang?", "soft", "narrow", "annoyed", "L", hair="horny")
        call cho_main("No. Of course not, Professor.", "base", "narrow", "base", "L", cheeks="heavy_blush")
        call ton_main("Good girl.", "horny", "narrow", "base", "L", hair="horny")
        call cho_main("...", "angry", "narrow", "base", "down", cheeks="blush")
    elif random_number == 2:
        call ton_main("Are you enjoying yourself, Professor?", "open", "narrow", "raised", "mid", hair="horny")
        g9 "With those tits in front of me? Always!"
    else:
        call ton_main("Did you like that, Professor?", "horny", "narrow", "raised", "mid", hair="horny")
        g9 "I bloody love it!"

    call cc_pf_strip_T3_tonks.spank_tonks

    jump cc_pf_strip_T3_tonks.strip_check


label .spank_tonks:
    # Tonks should stand next to Genie for this.
    menu:
        m "(...)"
        "-Spank her!-":
            pass
        "-Don't spank her...-":
            return

    call slap_her
    call ton_main("!!!", "clench", "shocked", "base", "stare", hair="scared", cheeks="heavy_blush") # shocked
    call ton_main("*Mmm*... You're so naughty, Professor!", "silly", "narrow", "angry", "mid", hair="horny", cheeks="blush")
    call ton_main("Right in front of a student and everything...", "base", "narrow", "base", "mid", hair="horny", cheeks="blush")
    call slap_her
    call ton_main("Ouch... {heart}{heart}{heart}", "silly", "happyCl", "base", "mid", hair="horny", cheeks="blush")
    call cho_main("...", "grin", "narrow", "base", "mid", cheeks="blush")

    menu:
        m "(...)"
        "-Spank her again!-":
            call slap_her
            call ton_main("*Mmm*... Spank me, Professor!", "horny", "narrow", "angry", "mid", hair="horny", cheeks="heavy_blush")

            menu:
                "-Again!-":
                    pass
            call slap_her
            call ton_main("Not so rough, Sir! {heart}", "soft", "narrow", "base", "mid", hair="horny", cheeks="heavy_blush")
            call cho_main("...", "horny", "narrow", "base", "down", cheeks="heavy_blush") # blushing #lip bite #looking away

            menu:
                "-Slap it hard!-":
                    pass
            call slap_her
            call ton_main("", "clench", "base", "shocked", "ahegao", hair="scared", cheeks="heavy_blush")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .3
            call slap_her
            call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
            call ton_main("*Hngh*...", "upset", "narrow", "base", "ahegao", hair="horny", cheeks="heavy_blush")
            call ton_main("Thank you, Professor. {heart}{heart}{heart}", "soft", "narrow", "worried", "mid", hair="horny", cheeks="heavy_blush")
            g9 "You're welcome."
            call cho_main("...", "horny", "narrow", "base", "downR", cheeks="heavy_blush")

            return

        "-Ask Cho to spank her.-":
            g9 "Miss Chang, would you be so kind and slap your teacher's ass for me?"
            call ton_main("", "base", "narrow", "base", "mid", hair="horny")
            call cho_main("Yes, Sir.", "open", "narrow", "angry", "mid", cheeks="blush")
            call ton_main("Do it, [tonks_cho_name]!", "base", "narrow", "base", "L", hair="horny")
            pause .2

            # Tonks turns around.
            call ton_chibi(flip=False)
            call ton_main("", "base", "base", "base", "mid", hair="horny", cheeks="blush", xpos=215, ypos="base", flip=False, trans=d5)
            pause .5

            call ton_main("Slap this naughty teacher's ass!", "crooked_smile", "narrow", "angry", "R", hair="horny", cheeks="blush")
            call cho_main("...", "base", "narrow", "angry", "down", cheeks="blush")
            call slap_her
            call ton_main("Surely you can do better than that, Cho.", "soft", "narrow", "base", "downR", hair="horny")
            call cho_main("", "annoyed", "narrow", "angry", "down", cheeks="blush")
            call slap_her
            call ton_main("*Hngh*...", "crooked_smile", "narrow", "base", "mid", hair="horny", cheeks="blush")
            call ton_main("Do I have to fetch a beaters bat so you can hit it properly, Miss Chang?", "open", "narrow", "annoyed", "downR", hair="angry")
            call ton_main("I thought I asked you to slap it harder!", "scream", "narrow", "angry", "downR", hair="angry")
            call cho_main("", "clench", "narrow", "angry", "down", cheeks="blush")
            call slap_her
            call ton_main("", "mad", "wide", "shocked", "stare", hair="scared")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .2
            call slap_her
            call ton_main("!!!", "clench", "narrow", "base", "ahegao", hair="horny", cheeks="heavy_blush")
            call cho_main("Good enough for you, Professor?", "open", "narrow", "angry", "L", cheeks="blush")
            call ton_main("*Ah*...{w=0.4} Yes, [tonks_cho_name]... I'd say that was quite--", "open", "narrow", "worried", "R", hair="horny")
            call cho_main("", "annoyed", "narrow", "angry", "down", cheeks="blush")
            call slap_her
            call ton_main("", "clench", "narrow", "base", "ahegao", hair="scared")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .2
            call slap_her
            call ton_main("", "horny", "narrow", "base", "ahegao", hair="horny", cheeks="heavy_blush")
            call ctc

            m "That's enough."
            call cho_main("Oh wow, it's really red now...", "grin", "narrow", "base", "down", cheeks="blush")
            call ton_main("Very good, Miss Chang. {heart}", "horny", "narrow", "worried", "R", hair="horny", cheeks="heavy_blush")
            pause .2

            # Tonks turns around.
            call ton_chibi(flip=True)
            call ton_main("", "base", "base", "base", "mid", hair="horny", cheeks="heavy_blush", xpos=280, ypos="base", flip=True, trans=dissolve)
            pause .8

            call ton_main("Ten points for Ravenclaw.", "soft", "narrow", "base", "L", hair="horny", cheeks="heavy_blush")
            $ ravenclaw += 10
            call ton_main("For this thorough ass spanking!", "horny", "narrow", "base", "mid", hair="horny", cheeks="heavy_blush")
            call cho_main("Thank you, Professor Tonks.", "crooked_smile", "narrow", "base", "down")

            return


# Check if Tonks and Cho are naked. Proceed to transformation section if they are.
label .strip_check:
    # Cho is wearing at least one clothing piece:
    if cho.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        jump cc_pf_strip_T3_tonks.strip_cho
    # Tonks is wearing at least one clothing piece:
    elif tonks.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        jump cc_pf_strip_T3_tonks.strip_tonks
    # Both are naked; Proceed with event.
    else:
        jump cc_pf_strip_T3_tonks.transformations



## Transformations ##
label .transformations:
    # Intro Event 1 - Doppler or Succubus choice.
    # Intro Event 2 - Doppler or Succubus choice.
    # Repeatable Event - Transformations.

    $ cho_zorder = 16 # in front of Tonks # Default is 15.
    $ tonks_zorder = 15 # reset to default.
    call cho_chibi("stand", flip=True, 314, 366)
    call ton_chibi("stand", flip=False, 370, 360)
    call ton_main("", "base", "narrow", "base", "L", hair="horny", xpos=345, ypos="base", flip=False)
    call cho_main("", "grin", "base", "base", "L", cheeks="blush", xpos=280, ypos="base", flip=True)
    with d5

    ## Intro Events 1 and 2:
    if doppler_done == False or succubus_done == False:

        # Ask Tonks if she's a Doppler or a Succubus.
        # After asking her both questions, the next time you do the event she'll do some tranformations.

        if doppler_done == True or succubus_done == True: # You have asked her if she was one of these before.
            call ton_main("You're getting quite good at this, Miss Chang.", "base", "narrow", "base", "L")
            call cho_main("Thank you, Professor.", "base", "narrow", "base", "L", cheeks="blush")
            m "She's learning from the best."
            if succubus_done:
                m "Who'd be better suited to teach her how to entice a man than a semen stealing she-devil!"
                call ton_main("Please, Professor. I've already told you I'm not a Succubus...", "open", "closed", "annoyed", "mid")
            else: # doppler_done
                m "Who'd be better suited to teach her how to entice a man than a shapeshifter!"
                call ton_main("Please, Professor. I've already told you I'm not this... doppler creature you spoke of.", "open", "closed", "annoyed", "mid")
            call ton_main("", "annoyed", "narrow", "annoyed", "mid")
            m "You can never be a hundred percent sure..."
            call cho_main("...", "quiver", "narrow", "raised", "mid")
            g9 "My theories have yet to be completely debunked!"
            call ton_main("Seriously?!", "upset", "base", "raised", "mid")
            call ton_main("Alright then... What do you want me to do to convince you this time?", "soft", "narrow", "base", "mid")
            m "Prove to me that you're not--"
            pass

        else:
            call ton_main("*Hmm*... not so nervous around me anymore, are you, Cho?", "crooked_smile", "narrow", "base", "L")
            call cho_main("Oh, I guess not. It seems like I got used to it...", "crooked_smile", "narrow", "worried", "R", cheeks="blush")
            call cho_main("It's fun doing this sort of thing at school... I'm quite enjoying it.", "smile", "narrow", "base", "downR", cheeks="blush")
            call ton_main("Well, there's somebody who enjoys it even more than we do, isn't that right, Professor?", "horny", "base", "raised", "mid", hair="horny")
            m "(...)"
            call ton_main("Professor?", "soft", "narrow", "base", "mid")
            call cho_main("", "annoyed", "narrow", "base", "mid", cheeks="blush")
            call ton_main("Something on your mind?", "annoyed", "base", "raised", "mid")
            m "Actually, there is..."
            m "Since your abilities are so rare... Can we be certain that you are in fact human?"
            call ton_main("Don't be silly...", "clench", "base", "shocked", "mid")
            m "You {b}are{/b} human, are you?"
            call ton_main("Of course I am, Professor!", "open", "closed", "annoyed", "mid")
            call ton_main("What else am I suppose to be?", "open", "narrow", "raised", "mid")
            pass

        menu:
            m "(...)"
            "\"A Doppler!\"" if doppler_done == False:
                jump .doppler_E1
            "\"A Succubus!\"" if succubus_done == False:
                jump .succubus_E1


    ## Repeatable ##
    else:
        pass

    call ctc

    g9 "Tonks, would you mind showing us your little trick again?"
    call ton_main("Of course. What's it gonna be, Professor?", "grin", "base", "base", "mid")
    call ton_main("Remember I can transform into anything... or anyone.", "soft", "narrow", "base", "mid") # suggestive
    call cho_main("...", "horny", "narrow", "base", "down", cheeks="blush")
    m "*Hmmm*... who do I want you to turn into... Let me think."

    menu:
        g9 "Yes, I want you to shapeshift into--"
        "\"Hermione!\"":
            jump cc_pf_strip_T3_tonks.hermione_E1
        "\"A Succubus!\"":
            jump cc_pf_strip_T3_tonks.succubus_E2



## Doppler Event 1 ##
label cc_pf_strip_T3_tonks.doppler_E1:
    if doppler_done == False:
        # Intro
        call ton_main("*Hmmm?*... What's a \"doppler\"?", "upset", "base", "base", "mid")
        m "What do you mean, what's a doppler?!"
        g4 "Aren't you part of the magical animal control... or whatever."
        call ton_main("The Auror division does a lot more than \"animal control\"...", "open", "narrow", "base", "mid")
        g4 "But you're incapable of identifying a doppler?"
        call ton_main("I guess... This is the first time I'm hearing of such a creature.", "annoyed", "base", "raised", "mid")
        call cho_main("I haven't heard of them either, Sir.", "soft", "narrow", "base", "mid")
        m "What sort of magic school are we running here? Aren't you getting taught any Witcher lore?"
        call cho_main("...", "annoyed", "base", "base", "mid")
        call ton_main("Very well, Professor. Why don't you tell us about them?", "upset", "narrow", "base", "mid")
        g9 "Oh, there's nobody better suited to do that than me, I'll have you know!"
        g9 "After all, I know a lot about the Witcher just from playing the games alone!"
        m "(Truth be told I skipped the first two, but they don't need to know that...)"
        call cho_main("What kind of \"games\" is he talking about, Professor?", "soft", "base", "worried", "L") # looking at Tonks. Small text
        call ton_main("I haven't the foggiest...", "mad", "base", "raised", "L") # looking back. Small text

    $ doppler_done = True
    g4 "Dopplers are hideous creatures, you see... Both in character, and in appearance."
    call cho_main("", "annoyed", "base", "base", "mid")
    call ton_main("", "upset", "narrow", "base", "mid")
    m "They often abuse their ability for selfish gains, and manipulate people into thinking they're somebody else entirely."
    call cho_main("That does sound quite suspicious, Professor...", "open", "narrow", "angry", "mid")
    call cho_main("After all, she's been abusing her powers to flaunt my bum at people!", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    g9 "That's true!"
    call ton_main("Surely you can't blame me for that... As I said, it wasn't anything they hadn't seen before.", "soft", "base", "base", "R", hair="horny")
    call cho_main("But-- Professor!", "annoyed", "narrow", "angry", "L", cheeks="heavy_blush")
    m "*Hmm*..."
    call ton_main("I'm not doing anything harmful, I promise.", "upset", "happyCl", "worried", "mid", hair="horny", cheeks="blush")
    call cho_main("...", "annoyed", "narrow", "angry", "mid", cheeks="blush") # annoyed

    call ton_main("So, what other \"Evidence\" do you have to further prove this theory?", "soft", "narrow", "base", "mid", hair="horny") #Amused
    m "Well, there's a big reason why Dopplers indulge themselves when they get the chance to."
    m "Since they're incredibly ugly creatures, it wouldn't surprise me in the slightest that they'd change their appearance into a highly attractive woman when given the chance."
    call cho_main("", "annoyed", "base", "base", "L", cheeks="blush")
    call ton_main("", "annoyed", "base", "base", "mid", hair="horny")
    m "Miss Tonks, your appearance, it's almost too perfect..."
    m "You didn't find some smoking hot woman in a magazine did you?"
    m "We all know those are highly edited..."
    call ton_main("So I'm smoking hot, huh?", "horny", "narrow", "base", "mid", hair="horny")
    call ton_main("You flatter me, but no... I've always looked like this.", "base", "happyCl", "base", "mid", hair="horny")
    m "*Hmmm*..."
    call cho_main("...", "annoyed", "base", "base", "mid", cheeks="blush") # blushing

    m "You can count yourself lucky that I haven't seen any bounties for a Doppler..."
    m "So, doppler or not... "
    m "You're off the hook for now."
    call ton_main("Well, I'm glad we cleared that up...", "base", "narrow", "base", "mid")
    call cho_main("", "annoyed", "base", "base", "mid", cheeks="blush")
    call ton_main("My ability is perfectly harmless, Professor.", "crooked_smile", "base", "base", "mid")
    g4 "You may say that, but we all know shape-shifting is the source of all kinds of evil sorcery!"
    call ton_main("No it's not...", "open", "closed", "annoyed", "mid")
    g4 "The last thing we need at this school is a rogue shapeshifter -- abusive of its powers..."
    call ton_main("...", "upset", "base", "base", "mid", hair="horny")

    m "Anyway... Promise me you won't start murdering people and steal their identities."
    call cho_main("", "angry", "base", "raised", "mid", cheeks="blush")
    call ton_main("What?! How could you even suggest that I would--", "clench", "shocked", "shocked", "mid", hair="scared") # shocked
    g4 "Identity theft is not a joke, Tonks! Millions of families suffer every year!"
    call ton_main("Yikes! Of course I won't do that, Professor!", "clench", "happyCl", "base", "mid")
    m "Good."
    call ton_main("...", "upset", "base", "worried", "mid")
    call cho_main("", "annoyed", "base", "base", "mid")
    m "How come you're the only one that can shapeshift?"
    call ton_main("It's just very uncommon.", "open", "narrow", "raised", "down")
    call ton_main("You can't fault me for having it... I was born with it.", "annoyed", "base", "base", "mid")
    m "Very well then, I shall believe that you're not a doppler..."
    m "(For now...)"
    call ton_main("Glad to hear it.", "mad", "base", "base", "mid")
    call cho_main("...", "soft", "narrow", "worried", "L")
    call ton_main("Anyhow, it's getting quite late, Professor.", "soft", "narrow", "base", "L")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event


## Succubus Event 1 ##
label cc_pf_strip_T3_tonks.succubus_E1:
    if succubus_done == False:
        # Intro
        call ton_main("*snort!*... For real?", "crooked_smile", "happyCl", "shocked", "mid")
        call cho_main("Oh, I've heard of those, Professor!", "grin", "happyCl", "base", "mid")
        call cho_main("They're demons in female form, that can visit you in your dreams and murder you!", "soft", "narrow", "angry", "mid")
        call ton_main("Very good, Miss Chang...", "crooked_smile", "base", "base", "L")
        call ton_main("Ten points for Ravenclaw!", "soft", "narrow", "base", "L")
        $ ravenclaw += 10
        call cho_main("Thank you.", "smile", "narrow", "base", "downR", cheeks="blush") # happy

    $ succubus_done = True
    call ton_main("I mean... I'm quite flattered, Professor...", "open", "narrow", "raised", "mid")
    call ton_main("Who doesn't want to be compared to a demonic, sex-driven temptress!", "soft", "narrow", "base", "mid", hair="horny")
    call cho_main("", "annoyed", "base", "base", "mid", cheeks="blush")
    g9 "I knew it! You're a Succubus!"
    call cho_main("", "annoyed", "base", "raised", "L", cheeks="blush")
    call ton_main("No I'm not, silly!", "open", "closed", "base", "mid")
    call ton_main("...", "annoyed", "base", "shocked", "L", hair="horny") # thinks
    call ton_main("Well, I do have similar shapeshifting abilities, that's true...", "soft", "base", "base", "down", hair="horny")
    call ton_main("And share some of their more raunchy characteristics...", "crooked_smile", "happyCl", "base", "mid", hair="horny")
    g9 "Not to mention a banger body!"
    call ton_main("Obviously.", "soft", "narrow", "base", "mid", hair="horny")
    call cho_main("...", "horny", "narrow", "base", "L", cheeks="blush") # blushing
    call ton_main("I may also act like one on the occasion...", "open", "base", "base", "R", hair="horny")

    # TODO: v v v Added this bit of writing. Needs review
    m "But you're still denying that you're an alluring sex-demon, even after that last demonstration?"
    call ton_main("I might have some unusual talents, that's all...", "open", "base", "base", "R", hair="horny")
    call ton_main("Why are you so scared of them anyway?", "open", "narrow", "base", "mid", hair="horny")
    call ton_main("What's the worst a succubus could do to you?", "horny", "narrow", "base", "mid", hair="horny")
    g4 "Do I really have to remind the two of you of what they do?"
    g4 "I won't let any demon suck the life-blood out of my penis!"
    call ton_main("", "normal", "base", "base", "mid", hair="horny")
    call cho_main("What?!", "clench", "base", "base", "mid") # bit shocked.
    call ton_main("Well, if I was one, I promise you I wouldn't do that...", "mad", "narrow", "base", "mid", hair="horny")
    call ton_main("Not as long as there's plenty of other essence to be gathered.", "horny", "narrow", "angry", "mid", hair="horny")
    call cho_main("Professors?!", "mad", "narrow", "base", "downR") # uncomfortable
    g9 "Then I better not run out of essence!"
    call cho_main("...", "disgust", "narrow", "base", "mid")
    g9 "Thought you could trick me, you semen loving sex-demon!"
    # TODO: ^ ^ ^ Added this bit of writing. Needs review

    call ton_main("I'm still human, and not a sex-demon...{w=0.5} Believe it or not.", "open", "narrow", "raised", "mid", hair="horny")
    m "If you say so..."
    call ton_main("If you'd met one before, you'd know the difference between me and a succubus right away...", "base", "narrow", "base", "mid", hair="horny")
    call ton_main("They are quite relentless when it comes to sex, you know. -- Even more so than I am!", "horny", "narrow", "annoyed", "mid", hair="horny")
    call cho_main("You have met a Succubus, Professor? But I thought they're extremely dangerous.", "mad", "base", "base", "mid")
    call ton_main("Oh yes! You have to be extremely careful around them...", "soft", "base", "base", "L", hair="horny")
    m "Don't tell me you--"
    call ton_main("Who do you think you're talking to, Professor.{w=0.5} Of course I did.", "base", "narrow", "base", "mid", hair="horny") # horny, confident
    call cho_main("No way!", "horny", "base", "base", "L", cheeks="heavy_blush")
    call ton_main("It was part of an auror job, obviously. Maybe I'll tell you about it some time.", "crooked_smile", "base", "base", "mid", hair="horny")
    call cho_main("Yes! I want to hear it!", "grin", "base", "base", "mid")
    call ton_main("Are you sure you'd want that, honey?", "soft", "narrow", "base", "L", hair="horny")
    call ton_main("It's quite the filthy story... You don't walk away from a Succubus unscarred unless you can impress her!", "horny", "narrow", "raised", "mid", hair="horny") # horny
    call cho_main("*Uhm*...", "disgust", "narrow", "worried", "downR", cheeks="heavy_blush")
    call play_sound("gulp")
    g4 "*gulp*..." # sound
    call ton_main("Of course I could tone it down for you guys.", "base", "happyCl", "base", "mid", hair="horny")
    g9 "No, please. We'd love to hear the full story!"
    call cho_main("...", "horny", "narrow", "base", "mid", cheeks="blush")
    call ton_main("Next time. I promise.", "base", "narrow", "base", "mid")
    call ton_main("Anyhow, it's getting quite late, Professor.", "soft", "narrow", "base", "L")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event


## Succubus Event 2 ##
label .succubus_E2:
    call ton_main("You want me to shapeshift into a Succubus?", "base", "narrow", "base", "mid")
    call cho_main("", "horny", "narrow", "base", "L")
    g9 "Hell yeah! I do love me some cosplay!"
    call ton_main("It's not...", "open", "base", "shocked", "R")
    call ton_main("Very well then...", "open", "closed", "base", "mid")

    # Tonks transforms into a Succubus
    stop music fadeout 0.5
    call cho_main("", "mad", "narrow", "base", "down", xpos=265, ypos="base", flip=True) # bit more to the left
    call ton_main("", "base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False) # bit more to the right
    with fade
    pause .5

    $ renpy.sound.play("sounds/magic3.mp3")
    $ tonks.equip(ton_outfit_succubus)
    call ton_main("", "horny", "narrow", "base", "mid", trans=flash)
    call ctc

    call play_music("trance")
    call ton_main("{heart}{heart}{heart}")
    g9 "Marvellous!"
    call cho_main("...", "horny", "narrow", "raised", "down", cheeks="blush") # blush
    call ton_main("*Giggles*", "horny", "narrow", "raised", "L", hair="horny") #sound
    call ton_main("What do you think?", "grin", "narrow", "base", "mid", hair="horny")
    call ton_main("Do you like it?", "horny", "narrow", "annoyed", "down", hair="horny")
    call cho_main("...", "horny", "narrow", "worried", "down", cheeks="blush")
    pause .8
    call ton_main("Miss Chang?", "soft", "narrow", "base", "L", hair="horny")
    call cho_main("Oh! Yes... Very impressive, Professor!", "soft", "narrow", "worried", "L", cheeks="heavy_blush")
    call ton_main("I don't think my skin tone is quite right... I believe they're usually more devilish looking.", "upset", "narrow", "base", "down", hair="horny")
    g4 "I can already feel my balls retract by fear."
    call ton_main("", "base", "narrow", "base", "mid", hair="horny")
    call cho_main("Your... What, Sir?", "clench", "wide", "base", "mid") #wide eyed
    call ton_main("Don't worry, Miss Chang... Unless you're in a state of high arousal then you have nothing to worry about.", "crooked_smile", "narrow", "base", "L", hair="horny")
    call cho_main("*Ehm*... If you say so, Professor.", "normal", "happyCl", "worried", "mid", cheeks="blush")
    call ton_main("Now the Professor on the other hand...", "mad", "narrow", "angry", "mid", hair="angry")
    call cho_main("", "mad", "base", "raised", "mid", cheeks="blush")
    call ton_main("He can call himself very lucky that I'm not a real Succubus.", "soft", "narrow", "base", "mid", hair="angry")
    m "I'm not ruling out the possibility..."
    call ton_main("*Tsk*...", "upset", "narrow", "base", "mid", hair="angry")
    m "Though I must say you're much more attractive than the last demon who visited me..."
    call ton_main("", "annoyed", "narrow", "raised", "mid", hair="angry")
    call cho_main("You were visited by a demon, Professor?", "soft", "narrow", "base", "mid")
    m "Yes... Although it was just your regular sleep paralysis demon."
    call ton_main("", "base", "narrow", "base", "mid", hair="angry")
    call cho_main("Oh...", "disgust", "narrow", "base", "down")
    g4 "A rather horrifying looking one at that... Not sexy in the slightest!"
    g9 "Mating with it proved itself to be quite difficult..."
    call ton_main("Of course you did...", "horny", "narrow", "angry", "mid", hair="angry")
    call cho_main("You... Wait, did you say {b}it{/b}, Sir?", "open", "base", "base", "mid") #wide eyed
    m "*Ahem*... So, how does one summon a Succubus anyway?"
    g9 "I'm sure you're an expert in the subject, Miss Tonks."
    call cho_main("{b}It{/b}, sir?!", "mad", "narrow", "raised", "mid")
    call ton_main("*Hmm*... I wouldn't call myself an expert...", "base", "narrow", "base", "mid")
    call cho_main("But what about your Auror Training professor?", "annoyed", "narrow", "base", "L") #annoyed pout
    call ton_main("", "base", "narrow", "base", "L") #Glances at Cho
    call cho_main("...", "base", "narrow", "base", "L", cheeks="blush") #embarrased
    call ton_main("Now I know I'm your Teacher, Miss Chang, but that doesn't mean I'm at an expert level of every subject before doing proper research...", "open", "narrow", "raised", "L")
    call cho_main("Oh... Of course, Professor... I didn't mean to--", "mad", "narrow", "worried", "down", cheeks="blush")
    call ton_main("Whilst we did cover Succubi during our training, the subject of summoning wasn't very in depth...", "soft", "narrow", "raised", "L")
    call cho_main("", "base", "narrow", "worried", "L", cheeks="blush")
    call ton_main("We mostly learned how to easily recognize and how to... Deal with various magical beings.", "open", "closed", "base", "mid")
    m "Right..."
    call ton_main("That said...", "grin", "narrow", "base", "mid")
    call ton_main("What I do know is that they usually come off as quite erratic and spontaneous.", "soft", "narrow", "shocked", "mid")
    call ton_main("In most cases you'd only encounter them if {b}they{/b} want you to...", "base", "narrow", "base", "mid")
    call ton_main("So summoning one would be quite difficult.", "base", "narrow", "base", "L")
    g9 "Well... Luckily I have the ability to summon you any time I want!"
    call ton_main("*Hmmm*... Be careful what you wish for, Professor...", "horny", "narrow", "base", "mid", hair="horny")
    call ton_main("I can be just as dangerous and seductive... {heart}", "horny", "narrow", "angry", "mid", hair="angry")
    call cho_main("", "horny", "narrow", "worried", "mid", cheeks="blush")
    g4 "See that hungry look in her eyes, Cho?"
    call cho_main("", "horny", "narrow", "worried", "L", cheeks="blush")
    g9 "This Succubus is out to steal all my semen!"
    call ton_main("Oh, don't tempt me, Professor...", "crooked_smile", "narrow", "angry", "mid", hair="horny")
    call cho_main("...", "base", "narrow", "worried", "down", cheeks="blush") # embarrassed

    #Tonks succubus encounter story
    call cho_main("*Ehm*...{w=0.5} So, did you actually confront a real Succubus, Professor?", "soft", "narrow", "base", "L", cheeks="blush")
    call ton_main("Oh, Yes indeed, Miss Chang!", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("It happened during my first year of Auror training, when I was still a complete novice.", "open", "narrow", "raised", "L")
    call ton_main("We were tracked down by one during a scouting mission... Unbeknownst to us, of course.", "crooked_smile", "narrow", "base", "mid")
    call cho_main("She tracked you down?", "mad", "base", "raised", "L", cheeks="blush")
    call ton_main("Yes... They can sense the arousal of humans from miles away... Even further if they haven't had any relief for some time.", "base", "narrow", "base", "L")
    m "Well, who can blame your partner with you around?"
    call ton_main("*giggles*", "base", "happyCl", "base", "mid", hair="horny") #sound
    call ton_main("Oh silly... She was after me, of course!", "soft", "narrow", "base", "mid", hair="horny")
    call cho_main("No way!?", "horny", "narrow", "raised", "L", cheeks="blush")
    call ton_main("I know what you're going to say, Professor... And yes... They don't usually go after females.", "open", "closed", "base", "mid", hair="horny")
    call cho_main("But she still came after you?", "soft", "narrow", "raised", "L", cheeks="blush")
    call cho_main("When did you and your partner notice her?", "mad", "narrow", "base", "L", cheeks="blush")
    call ton_main("Well... My partner didn't notice her exactly... I might've wandered a bit further away from our camp than I should have...", "soft", "narrow", "base", "downR", hair="horny")
    call ton_main("You know... To get some privacy.", "crooked_smile", "narrow", "base", "mid", hair="horny", cheeks="blush")
    call ton_main("She must've taken some great caution to be able to sneak up on me, but after a while of... *Ehm*...", "clench", "narrow", "base", "L", hair="horny")
    call ton_main("After some time I noticed her movements among the bushes.", "open", "closed", "base", "mid", hair="horny")
    call ton_main("Once I noticed her presence there was no doubt in my mind why she had snuck up on me...", "grin", "narrow", "base", "mid", hair="horny")
    m "Let me guess... She was--"
    call ton_main("She was going full force, pleasuring herself... Not even noticing that I had stopped and spotted her!", "grin", "narrow", "angry", "mid", hair="horny")
    call cho_main("Stopped what?", "annoyed", "base", "raised", "mid")
    g9 "Shush, Miss Chang... Don't interrupt the story!"
    call ton_main("Of course I had to be a hundred percent sure what creature she was, so I went to take out my wand to make some light, but...", "base", "narrow", "base", "L", hair="horny")
    call ton_main("Before I knew it she had flown right up next to me, grabbing my wrists.", "open", "narrow", "angry", "mid", hair="angry")
    call cho_main("And then you used your auror training to fight her!", "grin", "narrow", "angry", "L")
    call play_sound("giggle")
    call ton_main("*Giggles*...{w=0.4} No, we made out instead.", "horny", "narrow", "raised", "L", hair="horny") #sound
    call cho_main("You...{w} Made out with her!?", "clench", "wide", "base", "L")
    call ton_main("Of course! She couldn't get enough of me!", "grin", "happyCl", "base", "mid", hair="horny")
    call ton_main("After all... I'm quite skilled with my tongue.", "horny", "narrow", "base", "mid", hair="horny")
    call cho_main("Your--", "soft", "narrow", "worried", "L", cheeks="blush")
    g9 "Tongue!"
    call play_sound("giggle")
    call ton_main("*giggles*", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("Yes indeed... Would you like a demonstration?", "crooked_smile", "narrow", "base", "mid", hair="horny")

    menu:
        g9 "!!!"
        "\"Yes please!\"":
            call ton_main("Yeah, I bet you'd like that, Professor. {heart}", "horny", "narrow", "base", "mid", hair="horny")
            call ton_main("Maybe some other time.", "soft", "narrow", "base", "mid", hair="horny")
            call cho_main("...", "clench", "narrow", "worried", "down", cheeks="blush") # curious look

        "\"What do you say, Miss Chang?\"":
            call cho_main("With m-me?", "clench", "wide", "raised", "mid", cheeks="heavy_blush")
            call ton_main("No, silly... Well not today at least. {heart}", "soft", "narrow", "base", "L", hair="horny")
            call cho_main("...", "clench", "narrow", "worried", "down", cheeks="blush") # blushing

    # Tonks shows her tongue.
    call ton_main("You'll have to settle for a peek for now...", "horny", "narrow", "base", "mid", hair="horny")
    call cho_main("...", "horny", "narrow", "base", "L", cheeks="blush") #blush
    m "*Hmm?*..."
    call ton_main("*Ahh*...", "open_wide", "narrow", "base", "down", hair="horny")
    call cho_main("", "horny", "base", "raised", "L", cheeks="blush")
    call ton_main("*Ahhhhhhh*.........", "open_wide_tongue", "narrow", "angry", "down", hair="horny") # Tonks shows her tongue.
    call cho_main("Wow!", "open", "base", "raised", "L", cheeks="blush")
    g9 "..."
    call ton_main("Ae I chahn mhehk i ash ong ashh I whan...", "open_wide_tongue", "narrow", "angry", "mid", hair="horny")
    call ton_main("... shee!", "open_wide_tongue2", "narrow", "angry", "down", hair="horny") # Tongue all the way out.
    call cho_main("By Merlin's beard!", "clench", "narrow", "worried", "L", cheeks="heavy_blush") #blush
    g9 "Nice..."
    g9 "Although with a succubus I highly doubt there was just kissing going on..."
    call ton_main("*Hmm*... Yesh, thaht little devil...", "open_wide_tongue", "narrow", "angry", "mid", hair="horny")
    call ton_main("She was very quick to lock my head in place between her thighs, and then impaled herself on my tongue.", "open_wide_tongue", "narrow", "raised", "mid", hair="horny")
    call ton_main("Rode my tongue for a good hour, that freak...", "horny", "narrow", "angry", "mid", hair="horny")

    #g4 "You're calling her a freak? Your tongue is longer than my dick!"
    #cho "Professor?"
    #ton "Oh, sweetie... My dick could be longer than your dick..."
    #cho "What?!"
    #ton "Not that I have one currently..."
    #ton "But I could make it as long as I want!"
    #cho "..." #looking at floor
    #g4 "What else? Does it vibrate too? How are you even supposed to compete with that?"
    #ton "*giggles*" #sound
    #ton "I haven't tried that actually... That's not a bad idea."
    #cho "" #blush
    #m "..."
    #ton "Don't you worry professor... There's always the need for that masculine touch..."

    g9 "(Like you didn't enjoy every minute of it...)"
    call ton_main("Pleasuring her was quite exhausting to say the least...", "soft", "narrow", "base", "L", hair="horny")
    call ton_main("I licked her inside out until my whole face was covered in her devilish love-juices... {heart}", "horny", "narrow", "angry", "mid", hair="angry")
    call cho_main("", "clench", "narrow", "worried", "down", cheeks="heavy_blush") #Horny #looks at tonks
    call ctc

    call ton_main("Although... I did almost drown...", "upset", "base", "raised", "up", hair="horny") # thinking back
    call ton_main("Her thighs, practically glued to my cheeks meant there was no other way for her juices to flow than into my mouth...", "open", "narrow", "annoyed", "mid", hair="horny")
    call ton_main("Her essence becoming too much for me to handle as it eventually ran up my nose.", "horny", "narrow", "base", "down", hair="horny")
    m "Holy shit."
    call ton_main("I had no other choice but to swallow all of it...", "grin", "narrow", "base", "mid", hair="horny")
    call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call play_sound("gulp")
    g4 "*gulp*"
    call cho_main("", "horny", "narrow", "worried", "L", cheeks="blush")
    call ton_main("That little demon must've come at least twenty times that night. {heart}", "open_wide_tongue", "narrow", "raised", "L", hair="horny")
    call ton_main("I could give you a ride on this as well if you'd like, Miss Chang.", "open_wide_tongue2", "narrow", "angry", "L", hair="horny", cheeks="heavy_blush") # tongue out
    call cho_main("Professor--", "soft", "narrow", "worried", "mid", cheeks="heavy_blush") # embarrassed #looks at you
    m "Tonks, not before--"
    call ton_main("Yes, yes... Not before you win that silly Quidditch cup.", "mad", "closed", "angry", "mid", hair="angry", cheeks="heavy_blush")
    call cho_main("It's not silly!", "annoyed", "narrow", "angry", "L", cheeks="blush")
    call ton_main("Winning that cup won't feel as good as having my tongue inside you, Miss Chang... I can promise you that much.", "annoyed", "narrow", "angry", "L", hair="horny", cheeks="heavy_blush")
    call cho_main("...", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush") #Pout #blush
    call ton_main("Well then... I hope you two liked my little story. {heart}", "open", "closed", "base", "mid", hair="horny")
    call ton_main("And my new outfit of course... ", "crooked_smile", "narrow", "base", "down", hair="horny")

    # Unlock outfit message. Should only appear once.
    if ton_top_succubus.unlocked == False:
        call unlock_clothing(text=">New clothing items for Tonks have been unlocked!", item=ton_outfit_succubus)
        $ unlock_clothing_compat(item=ton_top_succubus2)

    call cho_main("", "horny", "narrow", "worried", "L", cheeks="heavy_blush")
    call ton_main("Maybe I could dress as a Succubus for Halloween. I'm sure the boys would love it...", "base", "narrow", "base", "mid", hair="horny")
    g9 "With or without the tits out?"
    call ton_main("*Hmm*... Haven't decided yet.", "upset", "narrow", "raised", "down", hair="horny")
    call cho_main("...", "clench", "narrow", "worried", "mid", cheeks="blush")
    call ton_main("Well, then... of we go Miss Chang...", "soft", "narrow", "base", "L", hair="horny")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event



## Hermione Transformation ##
label .hermione_E1:
    # Pink Hair: $ hermione.get_equipped("hair").set_color([[255, 87, 171, 255], [255, 210, 227, 255], [230, 141, 32, 255]])
    # Brown Hair: $ hermione.get_equipped("hair").set_color([[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]])
    call ton_main("Hermione again, *Hmm*?", "base", "base", "base", "mid")
    call ton_main("Seems to me like she's a bit of a favourite, isn't she?", "soft", "narrow", "raised", "mid")
    g9 "What can I say, she's got the best tits in the house!"
    call cho_main("Hey! That's not true!", "annoyed", "narrow", "base", "mid")
    m "It isn't? Then who's tits are better, Miss Chang?"
    g9 "Do tell me, I'd love to know!"
    call cho_main("Just forget I said anything...", "annoyed", "narrow", "base", "L")
    call ton_main("Well, I for one am not going to disagree with you, Professor.", "crooked_smile", "narrow", "base", "mid")
    call ton_main("Miss Granger's tits are quite nice indeed...", "horny", "narrow", "angry", "mid", hair="horny")
    call cho_main("...", "normal", "narrow", "base", "up")
    call ton_main("I mean we could do something else if you'd like, Miss--", "open", "base", "base", "L")
    g9 "No, No-- Do the thing!"
    call cho_main("", "annoyed", "narrow", "base", "L", cheeks="blush")
    call ton_main("Certainly... With pleasure.", "base", "happyCl", "base", "mid")
    stop music
    pause .8

    # Save custom Hermione name
    $ temp_name = hermione_name
    $ hermione_name = "Tonks"

    # Transforms into Hermione
    call play_sound("morph")
    hide screen tonks_main
    $ hermione.strip("all")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ hermione_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("hide")
    call her_chibi("stand", flip=False, 370, 360)
    call her_main("", "base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=d5)
    with morph
    pause .2

    call cho_main("", "horny", "narrow", "worried", "L", cheeks="heavy_blush")
    call ctc

    call play_music("trance")
    call her_main("Well then, here she is...", "smile", "narrow", "angry", "mid")
    call her_main("Feel free to touch me, Cho.", "base", "narrow", "annoyed", "R")
    call her_main("Unlike Hermione I won't bite you... Probably. {heart}", "smile", "narrow", "annoyed", "down")
    call cho_main("...", "mad", "narrow", "worried", "down", cheeks="blush") # blush
    call her_main("I simply love getting groped...", "soft", "narrow", "angry", "up")
    call cho_main("", "horny", "narrow", "worried", "L", cheeks="blush")
    g9 "That reminds me... Let's talk about how well you did during the last quidditch match..."
    m "You did quite a good job pretending to be Hermione."
    g9 "Wouldn't you say she did a good job commentating, Miss Chang?"
    call cho_main("Oh... Well I wouldn't know since I was more focused on playing, Sir...", "soft", "base", "base", "mid", cheeks="blush")
    call cho_main("But from what I could gather you did quite well, *uhm*... Professor.", "silly", "narrow", "worried", "L", cheeks="heavy_blush")
    m "Yes... She put so much effort into it... you must have been completely exhausted by the end..."
    call cho_main("", "horny", "narrow", "worried", "L", cheeks="blush")
    call her_main("... {heart}", "base", "happy", "base", "mid_soft", cheeks="blush") # blushing
    call cho_main("You were?", "smile", "narrow", "base", "L", cheeks="blush")
    m "Indeed... Addressing the entire school is no easy task, Miss Chang..."
    call her_main("...", "crooked_smile", "happyCl", "base", "mid") #Horny #Starts touching breasts (If Cho isn't looking)

    show screen blkfade
    with d5
    $ renpy.play("sounds/slick_02.mp3")
    with hpunch
    with kissiris
    $ hermione.set_pose("masturbate")
    $ hermione.set_body(armleft="on_pussy")
    call her_main("", "base", "narrow", "worried", "stare")
    hide screen blkfade
    with d5

    m "You have to Stay completely focused when you're tasked with commentating on everything that's happening."
    call cho_main("Surely commentating doesn't even come close to the amount of focus you need to spot the snitch...", "soft", "narrow", "raised", "mid")
    call cho_main("Or how would Granger be able to do it?", "annoyed", "narrow", "base", "R")
    m "Depends how easily you get distracted, I suppose..."
    m "Would you say that you're easily distracted... Miss Granger?"
    call her_main("*Mmm*...", "base", "narrow", "base", "stare_soft")
    m "Miss Granger?"
    call cho_main("...", "annoyed", "narrow", "base", "L") #annoyed
    call her_main("*Mmm*... Just thinking about it gets me all riled up again...", "open", "narrow", "worried", "mid")
    call cho_main("Professor, what are you...", "disgust", "narrow", "base", "L", cheeks="blush") #Looks at Tonks/Hermione
    call her_main("*Hmm*... Sorry, what did you say?", "open_tongue", "narrow", "base", "L")
    call cho_main("What are you doing?", "mad", "happyCl", "base", "mid", cheeks="blush")
    call play_sound("giggle")
    call her_main("*giggles*", "base", "narrow", "base", "mid", cheeks="blush") #sound
    call her_main("What does it looks like?", "grin", "narrow", "base", "L")
    call cho_main("You're touching your... Her--", "clench", "narrow", "raised", "down", cheeks="blush")
    call her_main("Yes... How could I not?", "base", "narrow", "base", "mid")
    call her_main("These breasts are just so...", "soft", "narrow", "base", "down")

    #pinch nipples.


    # Hands on pussy, tits
    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armleft="on_pussy", armright="on_tits")
    play bg_sounds "sounds/slickloop.mp3" fadein 2

    call her_main("*Mmmh*... So soft...", "base", "closed", "base", "mid")
    call her_main("And her nipples...", "soft", "narrow", "base", "down")
    call her_main("*Ah*...", "open_tongue", "narrow", "base", "stare_soft")
    call her_main("So sensitive...", "base", "narrow", "base", "up")
    call cho_main("*Ehm*...", "horny", "narrow", "worried", "down", cheeks="heavy_blush")
    call her_main("*Mhmm*... And I bet her nipples aren't the only--", "open", "narrow", "base", "down")
    call her_main("", "grin", "closed", "worried", "mid") #Hand in front of pussy
    pause .8
    $ renpy.play("sounds/slick_02.mp3")
    call her_main("*Ah*...", "open_tongue", "narrow", "base", "up") #Hand on pussy
    call cho_main("Tonks!", "mad", "narrow", "worried", "R", cheeks="heavy_blush")

    play bg_sounds "sounds/slickloop.mp3" fadein 2 #Continuous masturbate loop
    call her_main("*Mmmm*...", "base", "narrow", "base", "up")
    pause 1
    call her_main("*Hmm?*... Not even a peek?", "soft", "narrow", "base", "L")
    call her_main("Don't you want to see what Hermione looks like when... *Ah*... She masturbates?", "grin", "narrow", "worried", "down", cheeks="blush")
    call her_main("Are you sure you... *Ah*...{w=0.4} Want to miss this?", "open", "closed", "base", "mid", cheeks="blush")
    call cho_main("...", "clench", "narrow", "worried", "down", cheeks="heavy_blush") #glances at her
    call her_main("*Ah*...{w=0.3} That's it, Cho...", "smile", "narrow", "base", "L")
    call her_main("I knew you couldn't resist...", "soft", "narrow", "base", "up")
    call cho_main("", "horny", "narrow", "worried", "down", cheeks="heavy_blush") #Horny
    call ctc

    call her_main("*Ah*...{w=0.3} Look at me as I rub Granger's cute little slit.", "open_wide_tongue", "narrow", "angry", "up", cheeks="blush")
    call her_main("*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*...", "open_wide_tongue", "narrow", "worried", "up", cheeks="blush")
    call cho_main("", "horny", "narrow", "worried", "downR", cheeks="heavy_blush") #looks away
    call ctc

    call her_main("No! Keep watching me!", "annoyed", "narrow", "angry", "L")
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("*Ah*...{w=0.3} I'm getting close!", "soft", "narrow", "base", "up", cheeks="blush")
    play bg_sounds "sounds/slickloopveryfast.mp3"
    call cho_main("", "mad", "narrow", "base", "down", cheeks="heavy_blush") #still looking away
    call her_main("Watch me!", "open_wide_tongue", "narrow", "angry", "up", cheeks="blush")
    call cho_main("", "horny", "narrow", "raised", "down", cheeks="heavy_blush") #still looking away
    call her_main("Watch as Hermione cums for you!", "angry", "narrow", "base", "up", cheeks="blush")
    call cho_main("", "smile", "narrow", "base", "down", cheeks="heavy_blush") #embarrased #Looks at Tonks
    $ renpy.sound.play("sounds/slick_01.mp3")
    call her_main("*Nngh*...{w=0.4} *Aaah*!!!", "clench", "happy", "base", "ahegao", cheeks="blush")
    stop bg_sounds
    with kissiris
    call cho_main("", "horny", "base", "raised", "down", cheeks="heavy_blush") #wide eyed
    with kissiris
    $ renpy.sound.play("sounds/slick_01.mp3")
    call her_main("*Ah*!", "open_wide_tongue", "happy", "angry", "ahegao", cheeks="blush")
    stop bg_sounds fadeout 2
    call play_music("stop")
    call her_main("*Mmmh*...", "clench", "narrow", "base", "squint", cheeks="blush")
    call cho_main("...", "smile", "narrow", "base", "L", cheeks="heavy_blush")
    call her_main("*Ah*...{w=0.3} *Ah*...{w=0.5} *Ah*...{w=0.6} Good...{w=0.3} Good girl...", "open_tongue", "narrow", "base", "up", cheeks="blush")

    # Reset pose
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)
    with d5

    call play_music("tonks")
    call her_main("*Mmmh*... How I love masturbating in a body that I'm not quite familiar with...", "smile", "happyCl", "base", "mid")
    call her_main("It's like flying a new broom... There's nothing quite like the first test ride...", "base", "narrow", "base", "mid")
    call cho_main("...", "grin", "narrow", "base", "downR", cheeks="heavy_blush")
    call play_sound("giggle")
    call her_main("*giggles*", "base", "happyCl", "base", "mid", cheeks="blush") #Looks at cho

    # Tonks transforms back.
    call play_sound("magic")
    hide screen hermione_main
    call her_chibi("hide")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ tonks_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("stand", flip=False, 370, 360)
    call ton_main("", "base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=None)
    with morph
    pause .2

    call cho_main("", "horny", "base", "base", "L", cheeks="heavy_blush")
    call ctc

    call ton_main("Miss Granger's clit is quite sensitive... Who could have guessed?", "grin", "narrow", "raised", "mid")
    g9 "Noted."
    call ton_main("You'll do good to memorize this as well, Miss Chang. That knowledge might come in handy in the future.", "soft", "narrow", "base", "L")
    call cho_main("...", "smile", "narrow", "base", "down", cheeks="heavy_blush") # blushing
    call ton_main("Well then... this should be enough to last me for the day... Hopefully...", "grin", "narrow", "base", "mid")

    # Reset
    $ hermione_name = temp_name

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event



## End Event ##
label .end_event:

    # Fade to black.
    call play_music("stop")
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")
    $ hermione.wear("all")

    # Reset zorder.
    $ cho_zorder = 15 # reset to default.
    $ tonks_zorder = 15 # reset to default.
    $ hermione_zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    call play_sound("climb_desk")
    pause 2

    hide screen blkfade
    with d5
    pause .5

    call bld
    if game.daytime:
        call ton_main("We should get going, Miss Chang. Classes are about to start...", "open", "base", "base", "L", ypos="head", flip=False)
        call cho_main("Until next time, Professor.", "grin", "base", "base", "mid", ypos="head", flip=False)
    else:
        call ton_main("Let me escort you back to your dormitories, Miss Chang.", "open", "base", "base", "L", ypos="head", flip=False)
        call cho_main("Good night, Professor.", "grin", "base", "base", "mid", ypos="head", flip=False)

    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    call play_sound("door")
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5

    # Reset clothing.
    $ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)

    $ tonks_busy = True

    # End event.
    jump end_cho_strip_event






##############
### Tier 4 ###
##############

## Tier 4 - Summon Tonks ##


## Transformations ##

## Succubus - Tier 4 ##
#label cc_pf_strip_T4_tonks.succubus_E1:
#    m "Tell me, Miss Tonks."
#    g9 "Are you one of these Succubbi that like to hunt virgins?"
#    ton "*Ha-ha-ha*... Where did you hear that?" # cracks up.
#    m "I've read it in a-- *uhm*...{w=0.5} in a book."
#    m "If you're a virgin by the age of forty and one visits you, you might end up lucky!"
#    cho "Lucky... how?"
#    ton "I don't know... I'd have to do some research on that..."
#    ton "I was sure I knew everything there was to know about succubi..."
#    m "I suppose you might not be sophisticated enough to appreciate fine arts..."
#    ton "*Hmm*... Then perhaps It'd be worth covering during one of my lesson." #looking at cho
#    ton "Although I'd have to borrow that book of yours."

## Hermione - Tier 4 ##
#label cc_pf_strip_T4_tonks.hermione_E1:
    ton "Move aside, Chang!" # angry
    ton "The headmaster wants me to strip for him."
    g9 "That's right, Miss Granger."
    cho "..."

#    g9 "Seeing that she was being groped for the better part of it."
#    cho "Groped?-- What?" # confused
#    g9 "I her while she had to announce those points. It was quite funny!"
#    cho "You were molesting her, in front of everybody?"
#    g4 "I molested her -- with her consent!...{w} {size=-6}more or less.{/size}{w=0.3}{nw}"
#    m "She practicly begged me to continue."
#    ton "Was it that obvious, Professor?"
#    ton "I loved the way you fingered my pussy in front of everybody. {heart}"
#    cho "Merlin's beard, you're such a slut..." # judgemental


    # Hermione stands in the middle, between Genie and Cho.

    ton "Professor, how many house points may I get for this shameless act you're asking me to do?"
    g9 "You're requesting house points for this, Miss Granger?"
    ton "Naturally."
    m "*Hmmm*..."

    menu:
        "You shall receive five points.":
            ton "Only so little, Professor?"
            ton "Surely revealing my tits must be worth a lot more to you than that..."
            g9 "Five points, Miss Granger. And I demand to see a lot more than just your tits!"
            call cho_main("...", "smile", "narrow", "base", "mid", cheeks="blush")
            ton "So be it then..."
            ton "I'll do anything for my precious Gryffindor house!"
            g9 "Five points for Gryffindor, Miss Granger!"
            $ gryffindor += 5
            g4 "Now strip for us, you little slut."

        "You shall receive one hundred points!":
            ton "Seriously?"
            call cho_main("Professor, what are you doing?", "base", "narrow", "base", "mid")
            ton "Well, one hundred points seem to be sufficient, Professor..."
            call cho_main("...", "base", "narrow", "base", "mid")
            ton "I'd gladly bare my tits for that amount."
            g9 "Not just your tits, Miss Granger!"
            ton "Anything for you, Sir."
            call cho_main("I don't want Granger to get points from this! She isn't even here...", "base", "narrow", "base", "mid")
            m "Didn't you say you don't give a flying fuck about the house cup?"
            ton "*snort*... You said what?"
            call cho_main("I didn't say it like that!", "base", "narrow", "base", "mid")
            ton "*shsss*, Professor.{w=0.5} Just mumble a bit when giving out those points..."
            m "Very well, then..."
            g9 "One hundret points for this Gryffin-whore!"
            call cho_main("*Ha-ha*!", "base", "narrow", "base", "mid")
            ton "Thank you, Sir."
            ton "I know I deserve those Gryffin-whore points more than anyone!"
            ton "I'm the biggest slut in all of Hogwarts!"

        "No points for you, Granger.":
            ton "What? But Professor!"
            ton "You're asking me to expose myself for you, without getting any of those precious house points?"
            ton "How outragious!"
            m "Cho isn't asking for points either, Miss Granger. I'd say it's quite fair if you receive none as well..."
            ton "Well, I'm not a slag like Miss Chang here... Who loves stripping for her headmaster!"
            call cho_main("Hey!", "annoyed", "narrow", "angry", "L")
            ton "What? It's the truth, isn't it... You slut!"
            call cho_main("...", "annoyed", "narrow", "base", "mid")
            call cho_main("Sir, could you ask her to turn back again? She's starting to get on my nerves...", "open", "narrow", "base", "mid")
            g9 "Not a chance. She's doing great!"
            call cho_main("A bit too convincing for my likeing...", "annoyed", "narrow", "base", "L")
            ton "..."
            ton "Very well, then. I shall undress for you, Professor."
            ton "My friends will be so disappointed when they hear I'm doing this for free..."
            ton "But I simply can't help it, can I?"
            ton "I want to be the biggest slut in all of Hogwarts!"
