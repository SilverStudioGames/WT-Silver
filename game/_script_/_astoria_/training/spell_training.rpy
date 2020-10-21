

### Spell Training ###

### Astoria Imperio Training ###

label ag_st_imperio:

    if ag_st_imperio.points == 0: # Intro for 1st event.
        call ast_main(face="neutral", xpos="right", ypos="base", trans=fade)
        m "Ready for your first day of detention?"
        call ast_main("No...","annoyed","base","base","R")
        call ast_main("Do I really have to go there?","clench","base","base","mid")
        g9 "I could have you scrub the toilets instead..."
        call ast_main("Please don't, Sir!","clench","base","worried","mid")
        m "Tonks has some interesting lessons planned for you!{w=0.8} I'm sure you'll enjoy it."
        call ast_main("Oh yeah?","open","base","base","mid")
        call ast_main("Well, I doubt it...","annoyed","narrow","angry","R")
        call ast_main("At least it's not gonna be boring with her.","open","closed","base","mid")
        call ast_main("I once had to spend a whole day listening to McGonagall prattle on about the importance of a transfiguration spell.","annoyed","narrow","angry","R")
        call ast_main("When all it did was turn a stupid rat yellow!","annoyed","base","base","ahegao")
        call ast_main("I wanna learn something that's actually fun!","annoyed","narrow","base","down")
        m "Like an unforgivable curse?"
        call ast_main("Yes.","annoyed","base","base","mid")
        m "Good. Because your teacher has offered to teach one of them to you, properly."
        call ast_main("She offered to do...{w=0.8} what?","clench","base","base","mid")
        m "That's what I said!"
        call ast_main("I thought this was meant to be a punishment?","smile","base","base","L")
        call ast_main("That's wicked!","smile","narrow","angry","down")
        m "Off you go then. She's waiting for you..."
        m "Both of you return to my office once you are done."
        call ast_main("Of course!","smile","closed","base","mid")
        call ast_main("See ya later!","smile","base","base","mid") #smell ya later newbie! - gary oak

    elif ag_st_imperio.points == 3: # Intro for 4th event.
        call ast_main(face="annoyed", xpos="right", ypos="base", trans=fade)
        m "Time for another lesson, don't you think?"
        call ast_main("Do I really have to go there again?","open","narrow","base","R")
        call ast_main("I don't want to be yelled at by her...","annoyed","narrow","base","down")
        m "Nobody's gonna yell at you."
        call ast_main("If you say so, Professor.","annoyed","base","base","mid")
        m "Return here after your lesson."
        call ast_main("...","annoyed","base","base","R")

    else:
        call ast_main(face="happy", xpos="right", ypos="base", trans=fade)
        m "Ready for another curse lesson?"
        call ast_main("Yes, Professor.","smile","base","base","mid")
        g9 "I'm eager to see another demonstration of your progress!"
        m "Return to my office with your teacher afterwards."
        call ast_main("Until then, Professor!","smile","base","base","R")

    call play_sound("door")
    call hide_characters
    call ast_chibi("hide")
    hide screen bld1
    with d3

    # Setup
    $ ton_outfit_last.save() # Store current outfit.
    $ ast_outfit_last.save() # Store current outfit.

    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)

    $ ag_st_imperio.inProgress = True

    $ astoria_busy = True
    $ tonks_busy = True

    jump main_room


label end_ag_st_imperio:
    call hide_characters
    hide screen bld1
    with d3

    $ tonks.equip(ton_outfit_last) # Equip player outfit.
    $ astoria.equip(ast_outfit_last) # Equip player outfit.

    $ tonks_busy = True
    $ astoria_busy = True

    jump main_room


label ag_st_imperio_E1:
    stop music fadeout 1.0
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("tonks")
    call ast_main("","annoyed","base","base","mid", xpos="right", ypos="base")
    call ton_main("Good evening, Professor.","base","happyCl","base","mid", xpos="base", ypos="base")
    m "You are back."
    call ton_main("Yes we are.", "soft", "wink", "base", "mid")
    call ast_main("......................","annoyed","narrow","base","L") # embarrassed
    g9 "Astoria!{w} How was your training?"
    call ast_main("................................","annoyed","narrow","base","R")
    call ton_main("It went very well, I'd say.", "crooked_smile", "happyCl", "base", "mid")
    call ton_main("I instructed her on how to cast the curse - properly.", "base", "closed", "base", "mid")
    call ton_main("The right wand movement... The correct pronunciation...", "open", "wide", "base", "R")
    call ton_main("There's a lot to it!", "grin", "wide", "base", "mid")
    call ton_main("One mishap with those - and the curse might backfire!", "normal", "shocked", "shocked", "mid")
    call ton_main("Sending you straight to St. Mungo's hospital - quacking like a duck!", "annoyed", "shocked", "base", "mid")
    m "..........."
    call ton_main("I'd say she was very lucky using it on Susan...", "mad", "base", "base", "mid")
    call ast_main("I knew exactly what I was doing...", "base", "closed", "angry", "mid")
    call ast_main("","clench","narrow","base","mid")
    call ton_main("Of course you did, princess.", "soft", "narrow", "base", "L") # Happy
    call ast_main(".................................", "annoyed", "narrow", "angry", "R") # annoyed

    call ton_main("Now, shall we get started?", "soft", "base", "base", "mid")
    call ast_main("Get started - with what?","open","narrow","base","R")
    call ton_main("Continuing your training, of course!", "base", "base", "base", "L")
    call ton_main("I'd like you to cast the Imperius curse now... On another person.","base","base","angry","L")
    call ast_main("Wait, what?","angry","base","base","mid")
    call ast_main("I thought I wasn't allowed to ever use it again?", "annoyed", "base", "worried", "R")
    call ton_main("You aren't... That is correct.", "open", "closed", "base", "mid")
    call ton_main("However, you are hereby given special permission!", "grin", "wide", "base", "L")
    call ast_main("Really?", "smile", "narrow", "base", "down") # happy
    call ton_main("Yes, dear!","base","base","base","L")
    call ton_main("I believe our Professor would have no objection to that...","open","closed","base","mid")
    call ton_main("Would you, Professor?","base","base","angry","mid")
    call ast_main("Please, Professor!","smile","base","base","mid")
    m "*Uhm*...{w=0.4} Sure...{w=0.6} Go ahead."
    call ton_main("Splendid!", "silly", "happyCl", "base", "mid")
    call ast_main("Yes!","smile","base","angry","L")

    call ton_main("You can cast it, as long as it's under the supervision of a teacher...", "open", "base", "raised", "down")
    call ton_main("And only within the walls of this room!", "normal", "base", "base", "downR") # stern
    call ast_main("Right here? In front of Professor Dumbledore?","open","base","base","mid")
    call ton_main("Naturally!", "base", "closed", "base", "mid")
    call ast_main("But who do I cast it on? Susan?","smile","base","base","R")
    call ton_main("Not this time, sweetheart.", "upset", "narrow", "base", "down", cheeks="blush")
    call ton_main("Today, I'd like you to cast it on me, if you don't mind...", "open", "wide", "base", "downR", cheeks="blush")
    call ast_main("Wicked!","grin","narrow","worried","down")
    call ton_main("Let's give this old man a quick demonstration of your talents, shall we...", "grin", "base", "shocked", "down")
    call ast_chibi("wand",530,"base")
    with d3
    call ast_main("","grin","narrow","base","mid")
    m ".............................."

    call ast_chibi("wand_casting",530,"base")
    with d3
    call ton_main("Just like we practised...","open","closed","base","mid")
    call ton_main("Do the movement with your wand, and then you say--","open","base","base","R")
    call ast_main("Imperio!","scream","narrow","angry","mid") # angry scream
    call ast_main("","clench","narrow","angry","mid")
    call ton_main("Yes...", "mad", "narrow", "base", "mid")
    call ton_main("....................", "annoyed", "narrow", "shocked", "stare")
    call ton_main("You don't have to scream the words, darling.", "open", "closed", "raised", "L")
    call ton_main("What's crucial is that your mind is focused and--", "normal", "closed", "base", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call ast_main("","clench","base","angry","L", xpos="base", ypos="base")
    call ton_main(".........................", "mad", "wide", "shocked", "ahegao", hair="scared", xpos="right", ypos="base") # shock
    call ton_main("*Aaaaaah*...","horny","base","base","ahegao", hair="horny") # inhales
    call ast_main("......................","clench","base","worried","L") # clenched teeth
    m "What's happening to her?"
    call ast_main("I just cast the spell on her...","open","closed","base","mid")
    call ast_main("Now she's under my command!","smile","base","base","mid")
    g9 "You don't say?"
    g9 "I love magic!"
    call ast_chibi("wand",530,"base")
    with d3
    call ast_main("What shall I do now, Professor?","clench","base","base","L")
    m "I don't know... Why are you asking me?"
    m "Did you not discuss this with her beforehand?"
    call ast_main("No. All we did was some theoretical practice of the spell...","open","base","base","down")
    call ast_main("I need to tell her to do something... or...","open","base","worried","mid")
    call ast_main("I don't know... Maybe say something?","clench","base","base","L")
    call ton_main("*Hmm*... Something...", "base", "base", "worried", "up")
    call ast_main("!!!","smile","base","base","L")
    m "What?"
    call ast_main("She did it!","smile","base","base","L")
    g4 "Something what?"
    call ast_main("No, she just said what I asked her to say!","smile","base","base","mid")
    m "Oh..."
    call ast_main("I believe it's working!","smile","closed","base","mid")

    call ast_main("*Uhm*... Professor Tonks, you can now speak freely!","horny","base","base","L")
    call ton_main("............................", "base", "closed", "base", "stare")
    call ton_main("Oh... can I?...", "open", "base", "base", "stare")
    call ton_main("Thank you...", "soft", "wide", "base", "stare")
    call ast_main("She can hear me!","smile","base","base","mid")
    call ton_main("You have a really cute voice...", "horny", "wide", "shocked", "stare")
    call ast_main("................","annoyed","base","worried","R")
    m "Try something else now."
    call ast_main("","annoyed","base","base","L")
    call ton_main("I feel so good!", "soft", "wide", "shocked", "stare", hair="horny")
    call ton_main("What is happening to me?", "mad", "base", "raised", "stare", cheeks="blush")
    call ton_main("Are you playing with me?", "open", "base", "worried", "stare", cheeks="blush")
    call ton_main("I want you to play with me!", "open_wide_tongue", "narrow", "shocked", "stare") # horny
    m "I think she's tripping..."
    call ast_main("No!{w=0.6} Keep{w=0.4} - standing{w=0.4} - still!","clench","closed","worried","mid")
    call ton_main("Ok.........", "soft", "base", "base", "stare")
    g9 "This is quite funny to watch!"
    g9 "Can you make her *oink*?"
    call ast_main("*oink*?","open","wink","base","mid")
    m "You know, like a pig..."
    call ast_main("Yes, we can try that!","clench","base","base","mid")
    call ast_main("Professor Tonks, I demand that you *oink*!","open","base","base","L")
    call ton_main("*Huh*?...", "open", "wide", "base", "stare")
    call ast_main("*oink*!","open","base","angry","L")
    call ton_main("...................", "normal", "wide", "base", "stare", cheeks="blush")
    call ast_main("Do it already!","angry","base","angry","L")
    call ast_main("*oink!*{w=0.8}-*oink*!{w=0.8}-*oink*!","clench","closed","angry","mid") # Angry
    g9 "*he-he-he!*"
    call ast_main("*oink*...{w=0.8} you pig!","scream","base","angry","L", trans=hpunch) # Screaming
    call ast_main("","clench","narrow","angry","L")
    m "I don't believe she's going to do it..."
    call ast_main("But!","clench","closed","base","mid")
    m "It's pointless, girl..."
    m "You can stop now..."
    call ast_main(".............................","annoyed","base","angry","down")

    # Tonks reverts back.
    pause.2
    call hide_characters
    call ast_chibi("reset",530,"base")
    hide screen bld1
    with fade
    pause.8

    call play_music("tonks")
    call ast_main("","annoyed","base","angry","mid", xpos="right", ypos="base")
    call ton_main("Oh my...", "soft", "base", "worried", "down", cheeks="blush", xpos="base", ypos="base")
    call ton_main("Well that was fun!", "base", "happyCl", "base", "down", cheeks="blush") # Happy
    call ast_main("No it wasn't!","clench","narrow","angry","mid")
    call ast_main("Why weren't you doing pig noises!?","scream","closed","angry","mid", trans=hpunch)
    call ast_main("You refused to do what I demanded!","annoyed","narrow","angry","R")
    call ton_main("Yes I did!", "soft", "base", "base", "L")
    call ton_main("It was quite easy, actually.", "normal", "base", "raised", "downR")
    call ast_main("*Hnghhh*!","clench","narrow","angry","down")
    call ton_main("Don't worry. You'll have better luck next time...", "base", "base", "shocked", "L")
    call ton_main("Just try a bit harder.", "soft", "wink", "base", "mid")
    call ast_main("...................................","annoyed","narrow","angry","down")
    call ton_main("Thank you for your assistance, Professor.", "base", "base", "base", "mid")
    call ton_main("Let Astoria know when to visit me again for our next training session...","base","base","base","mid")
    m "Very well."
    call ast_main("........................","annoyed","base","angry","R")
    call ton_main("Have a good night, Professor.","base","base","base","mid")

    call ton_walk("door", "base")
    call ton_chibi("stand","door","base", flip=False)
    with d3
    pause.2

    call ton_main("Come on, Astoria. I shall escort you back to your dormitory...", "soft", "base", "base", "L", ypos="head")
    call ast_main(".................................................","annoyed","base","base","down", ypos="head")

    # They both leave.
    call ast_walk(680, "base")

    call play_sound("door")
    call ast_chibi("hide")
    call ton_chibi("hide")
    with d3

    # Increase affection once (this is the first event)
    if ag_st_imperio.counter == 1:
        $ ast_whoring += 1

    jump end_ag_st_imperio


label ag_st_imperio_E2:
    stop music fadeout 1.0
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("tonks")
    call ast_main("","upset","base","base","mid", xpos="base", ypos="base")
    call ton_main("Hello, Professor.","base","happyCl","base","mid", xpos="right", ypos="base")
    call ast_main(".........................","upset","base","base","L")
    m "Back already?"
    call ton_main("Yes, I gave Astoria a couple more pointers on how to improve the persuasiveness of the curse...", "open", "wide", "base", "L")
    call ton_main("The trick is to not lose your temper after casting it!", "soft", "closed", "base", "mid")
    call ast_chibi("wand",530,"base")
    call ast_main(".........................","annoyed","base","base","down")
    call ton_main("This should be fun!", "grin", "happyCl", "base", "mid")
    m "Very good."

    call ton_main("Now, Astoria, just as last time - you will cast the Imperius curse on me...", "soft", "base", "base", "L")
    call ton_main("And I'll do my best to resist--","open","closed","base","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call ast_main("","clench","base","angry","L")
    call ton_main(".........................", "mad", "wide", "shocked", "ahegao") # shock

    g9 "Damn it, girl!"
    m "Give me a warning next time. You scared the crap out of me..."
    call ast_main("Sorry Professor!","smile","base","base","mid") # Cute face

    call ton_main("..........................", "normal", "wide", "base", "stare")
    call ton_main("*uhhhh*... I looooooove this!", "soft", "base", "base", "stare")
    call ton_main("It's like - I'm floating...", "open", "wide", "shocked", "stare")
    call ton_main("It feels... sooooooooooooo... goooooooooooood!", "open_wide_tongue", "base", "base", "ahegao")
    call ton_main("", "mad", "base", "base", "ahegao")
    call ast_chibi("wand",530,"base")
    m "(Is she getting off on this?)"

    call ast_main("What shall I have her do, Professor?","clench","wink","base","mid")

    m "..........."
    menu:
        "-Have her turn around-":
            call ast_main("Yes, that's a good idea!","smile","base","base","mid")
            call ton_main("................................", "normal", "wide", "base", "stare")
            call ast_main("Professor Tonks, I command you to turn around.","open","base","base","L")
            call ton_main("*Huh*?", "open", "wide", "raised", "stare")
            call ast_main("Turn around!","clench","base","angry","L")
            m "Remember what she said about your temper, Astoria..."
            call ast_main("Oh... yes Sir! Of course...","smile","closed","base","mid")
            call ast_main("Turn around.","open","narrow","base","L")
            call ton_main("......................", "soft", "wide", "base", "stare")

            # Tonks turns around. (mirror sprite)
            call ton_chibi("stand","desk","base", flip=True)
            call ton_main("","normal","base","base","stare",  flip=True)
            pause.8

        "-Ask her to remove her coat-":
            call ast_main("Yes, that should be easy.","smile","base","base","mid")
            call ton_main("................................", "normal", "wide", "base", "stare")
            call ast_main("Tonks, I command you to remove your coat.","open","closed","base","mid")
            call ton_main("*Huh*?", "open", "wide", "raised", "stare")
            call ast_main("Come on, do it!","annoyed","base","angry","L")
            m "Try saying the magic word..."
            call ast_main("Imperio? But I already did--","open","wink","base","mid")
            m "No... Ask her politely..."
            call ast_main("Oh! I got it!","smile","closed","base","mid")
            call ast_main("Professor Tonks, please remove your coat for me...","open","base","base","L")
            call ton_main("*Hmm*... okay...", "soft", "wide", "base", "stare")

            # Tonks removes her coat.
            call play_sound("equip")
            $ tonks.strip("robe")

            call ctc

            call ton_main("","normal","wide","base","stare", cheeks="blush", flip=False)
            pause.8


    call ast_main("Yes, she did it!","smile","base","base","L")
    call ast_main("What shall I have her do next?","base","base","base","mid")
    m "*Hmm*................."

    $ d_flag_01 = False

    label ag_st_imperio_E2_choices:

    menu:
        m "Make her..."
        "\"Do pig noises again!\"" if d_flag_01 == False: # Jumps back to choices.
            $ d_flag_01 = True

            call ast_main("Do a pig noise?","open","base","worried","mid")
            call ton_main("*oink*!", "open_wide", "happyCl", "base", "stare")
            call ast_main("She did it!","smile","closed","base","mid")
            call ton_main("", "normal", "happyCl", "base", "mid")
            g9 "Well done!"
            call ast_main("Do it again!","smile","base","angry","L")
            call ton_main("*oink*!", "open_wide", "shocked", "worried", "stare", cheeks="blush")
            call ast_main("*hi-hi-hi-hi*!","smile","closed","base","mid")
            call ton_main("", "normal", "wide", "worried", "stare", cheeks="blush")
            m "I believe that's enough--"
            call ast_main("Do it again piggy! Ten times!","clench","narrow","angry","L") # Angry
            call ton_main("*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*!", "open_wide_tongue", "wide", "base", "ahegao", cheeks="blush")
            m "......................."
            call ast_main("Agai--","scream","closed","angry","mid", trans=hpunch)
            g4 "That's enough, Astoria!"
            call ast_main("Fine...","annoyed","narrow","angry","R")

            # Tonks returns to normal
            call hide_characters
            call ton_chibi("stand","desk","base", flip=False)
            call ast_chibi("reset",530,"base")
            with fade
            pause.8

            call play_music("astoria")
            call ast_main("","open","base","base","down")
            call ton_main("Oh wow...", "mad", "base", "shocked", "down", cheeks="blush", flip="False")
            call ton_main("You made me squeal like a pig!", "mad", "happyCl", "base", "mid", cheeks="blush")
            call ton_main("You've made quite some progress, well done Astoria!", "grin", "narrow", "shocked", "R")
            call ast_main("Thank you!", "smile", "base", "base", "L")
            m "..."
            m "I have to say, I'm not that impressed..."
            call ton_main("You aren't?", "open", "wide", "shocked", "mid")
            call ast_main("But, Professor!", "clench", "base", "worried", "mid")
            m "Tonks, would you please do the noise again..."
            call ton_main("The noise, Professor?", "soft", "base", "raised", "mid")
            m "Yes. Squeal for me."
            call ton_main("Very well...", "open", "narrow", "shocked", "down")
            call ton_main("*oink*-*oink*!", "open", "happyCl", "base", "mid")
            g9 "See, I don't even have to use magic to make her do it!"
            call ton_main("Very funny, Sir...", "soft", "narrow", "base", "downR")
            m "I'd like us to try this again..."
            call ton_main("Right now? Are you sure?", "soft", "wide", "raised", "mid")
            g4 "(I want to see some tits - damn it! Or hear her talk dirty...)"
            m "Yes, cast that spell again, Astoria..."
            call ast_chibi("wand",530,"base")
            call ast_main("Very well, Sir...","smile","closed","base","mid")

            # Astoria casts imperio.
            stop music fadeout 2.0
            call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

            call hide_characters
            hide screen bld1
            with d3
            pause.2

            # chibi spell animation.
            call play_sound("spell")
            call ast_chibi("wand_imperio",530,"base")
            with hpunch
            pause.8

            call play_music("trance")
            call ast_main("","clench","base","angry","L")
            call ton_main("*Hmm*.............","base","base","base","ahegao")
            call ast_chibi("wand",530,"base")
            call ast_main("And now?","open","base","base","mid")

            jump ag_st_imperio_E2_choices

        "\"Let her say something naughty!\"": # Fails
            call ast_main("*Huh*?...","open","base","worried","mid")
            g9 "Wouldn't you like to hear your teacher say something shameful?"
            call ast_main("Yes!","smile","base","angry","L")
            call ast_main("And what exactly?","clench","base","base","mid")
            m "I don't know... You should think of something..."
            m "You're the one with the magic stick, after all..."
            call ton_main(".......................", "normal", "wide", "base", "stare")
            call ast_main("Okay... Professor Tonks...","open","base","worried","L")
            call ast_main("I want you to repeat after me...","open","closed","base","mid")
            call ton_main("...................................", "horny", "wide", "base", "stare")
            call ast_main("I... am... a...","open","base","worried","L")
            call ton_main("I am a--", "soft", "wide", "base", "stare")
            call ast_main("dirty!{w} filthy!{w} pig!","open","narrow","base","L")
            call ton_main("...................................", "soft", "base", "base", "stare", cheeks="blush")
            call ast_main("Go on, say it!","clench","narrow","base","L")
            call ast_main("I'm a dirty... filthy... pig!","open","closed","base","mid")
            call ton_main("*hi-hi*!...", "base", "happyCl", "shocked", "mid", cheeks="blush")
            call ast_main("SAY IT!","scream","base","angry","L") # Scream
            g4 "Time-out!"
            call ast_main("No! She has to do what she's told!","clench","narrow","angry","mid")
            m "She clearly isn't going to..."
            m "We should take a break here..."
            call ast_main(".......................","annoyed","narrow","angry","mid")

            # Tonks returns to normal.
            pause.2
            call hide_characters
            call ton_chibi("stand","desk","base", flip=False)
            call ast_chibi("reset",530,"base")
            hide screen bld1
            with fade
            pause.8

            call play_music("tonks")
            call ast_main("","annoyed","base","angry","mid")
            call ton_main("*huh*...", "disgust", "base", "base", "down", flip="False")
            call ton_main("Well that was something, wasn't it?", "soft", "closed", "base", "mid")
            call ast_main("..................................","annoyed","narrow","angry","L")
            m "You resisted her curse again."
            call ton_main("Yes...", "upset", "base", "base", "L")
            call ton_main("I'm sorry, honey!", "annoyed", "narrow", "worried", "R")
            call ast_main("..................................","annoyed","narrow","angry","down")
            call ton_main("You can't expect to succeed right away now, can you?", "normal", "closed", "raised", "mid")
            call ton_main("To master a spell it takes time - and regular practising...", "normal", "narrow", "base", "R")
            call ton_main("Or else anyone could do it.", "open", "closed", "shocked", "mid")
            call ton_main("We'll try again next time...", "base", "narrow", "raised", "R")
            call ast_main("............................","upset","narrow","base","down")
            call ton_main("Have a good night, Professor.", "soft", "base", "base", "mid")

            call ton_walk("door", "base")
            call ton_chibi("stand","door","base", flip=False)
            with d3
            pause.2

            call ton_main("After you, Astoria.","open","base","base","L", ypos="head")
            call ast_main("...........................","upset","base","base","L", ypos="head")

            # They both leave.
            call ast_walk(680, "base")

            call play_sound("door")
            call ast_chibi("hide")
            call ton_chibi("hide")
            with d3

            $ ast_mood += 12

            # Event fails.
            $ ag_st_imperio.fail()

            call bld
            m "I don't think we made much progress here..."
            $ tonks.wear("all") # wear all previously stripped clothing pieces
            jump main_room

        "\"Make her show us those tits!\"": # Succeeds
            call ast_main("What?","clench","base","base","mid")
            g9 "Have her show us her breasts!"
            call ast_main("Professor?!","open","closed","worried","mid")
            m "You did the same to Susan, didn't you?"
            call ast_main("Yes, but...","open","narrow","worried","mid")
            call ast_main("I doubt Professor Tonks would be ok with that!","clench","narrow","base","L")
            m "Did you have those concerns with Susan as well?"
            m "Just try it."
            m "She can refuse to do it if she doesn't want to..."
            call ast_main("I suppose...","annoyed","base","base","L")
            call ast_main("Professor Tonks, I'd like you to show us your...","open","base","base","mid")
            call ast_main("*Uhm*...","upset","base","base","down")
            call ast_main("Your breasts!","clench","closed","base","mid") # embarrassed
            call ton_main("Oh...", "open", "wide", "shocked", "up")
            call ton_main("............................", "soft", "wide", "worried", "stare")
            g4 "(Fingers crossed!)"
            call ton_main("............................", "clench", "narrow", "base", "stare") # Clenched teeth
            call ast_main("I think she's struggling!","smile","base","base","L")
            g4 "Very good, girl!"
            g4 "Pressure her more! I want to see those puppies!"
            call ast_main("Professor Tonks, show us your breasts! Now!","open","base","angry","L")
            m "(It was easier for her to resist doing pig noises...)"
            m "(Could it be that she {b}wants{/b} to show them to us?{w} And is resisting that inner urge?)"
            call ton_main("................................", "mad", "wide", "worried", "stare", hair="horny") # Really struggling!
            g4 "(What a slut!)" # Small text
            call ast_main("Come on, do it!","clench","narrow","angry","L")
            call ton_main("*Hnnnngh*!...", "mad", "wide", "worried", "ahegao", hair="horny")
            call cum_block
            call ton_main("*Aaaaahhh*...", "open_wide_tongue", "base", "worried", "ahegao", cheeks="blush") # Relieved
            g4 "(Did she just?!)"
            call ton_main("", "open", "narrow", "worried", "stare", cheeks="blush")
            m "..."
            m "Girl, I think your teacher is done for..."
            call ast_main("What?","clench","base","worried","mid")
            call ton_main("", "normal", "closed", "worried", "stare", cheeks="blush")
            m "She \"broke the curse.\" You can stop now..."
            call ast_main("*Aww*...","upset","narrow","base","down")
            call ast_main("If you say so, Professor...","annoyed","base","base","mid")

            # Tonks returns to normal.
            pause.2
            call hide_characters
            call ast_chibi("reset",530,"base")
            hide screen bld1
            with fade
            pause.8

            call play_music("astoria")
            call ast_main("","annoyed","base","base","mid")
            call ton_main("*Ouch*... That was painful!", "mad", "closed", "base", "mid", cheeks="blush", flip="False")
            call ton_main("You nearly got me there.", "disgust", "base", "shocked", "R", cheeks="blush")
            call ast_main("Did I really?","smile","base","base","mid")
            call ton_main("Yes, well done, Astoria!", "open", "base", "base", "down", cheeks="blush")
            call ast_main("Thank you!","smile","closed","base","mid")
            m "Was it really such a struggle for you to not get your breasts out?"
            call ton_main("*Uhm*...", "mad", "base", "base", "down", cheeks="heavy_blush")
            g9 "*He-he-he*!"
            call ton_main("Shall we wrap it up for today?", "upset", "base", "shocked", "downR", cheeks="blush")
            call ton_main("I'm sure next time you'll have better luck, Astoria.", "soft", "base", "shocked", "R")
            call ast_main("Okay.", "smile", "base", "base", "R")
            call ton_main("Have a good night, Professor!", "base", "happyCl", "base", "mid")
            m "Until next time..."

            # They both leave
            call play_sound("door")
            hide screen astoria_main
            call ast_chibi("leave")
            hide screen tonks_main
            call ton_chibi("leave")
            with d3

            call bld
            m "And they say I'm the big, bad pervert..."

            # Increase affection once (this is the second event)
            if ag_st_imperio.counter == 2:
                $ ast_whoring += 1

            jump end_ag_st_imperio


label ag_st_imperio_E3:
    stop music fadeout 1.0
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",500,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("tonks")
    call ast_main("","annoyed","base","base","mid", xpos="base", ypos="base")
    call ton_main("Well, Professor.","open","closed","base","mid", xpos="right", ypos="base")
    call ton_main("We're back...", "soft", "wink", "base", "mid")
    call ast_main("...","annoyed","base","base","L")
    m "Did you make any progress today?"
    call ton_main("Of course we did!", "base", "wide", "base", "mid")
    call ton_main("Professor, you aren't questioning my abilities as a teacher, are you?", "base", "closed", "annoyed", "mid")
    m "Of course not..."
    g9 "You're very skilled at what you do!"
    g9 "You've shown me many times."
    call ton_main("Thank you! {heart}", "base", "narrow", "base", "mid")
    call ast_main("*Ugh*...","clench","narrow","base","down") # Disgusted from the flirting?

    call ast_chibi("wand",530,"base")
    with d3
    call ton_main("I could teach you a thing or two as well, Professor.", "base", "base", "shocked", "down")

    call ast_chibi("wand_casting",530,"base")
    with d3
    call ton_main("Even the great Albus Dumbledore doesn't know everything about--", "soft", "closed", "angry", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call ast_main("","clench","base","angry","L")
    call ton_main("*Hngh*!...", "mad", "wide", "shocked", "ahegao") # shock
    call ton_main("*Hmm*...","base","base","base","ahegao", hair="horny")

    call ast_chibi("wand",530,"base")
    with d3
    call ast_main("Sir, I'm not here to listen to you two banter...","angry","closed","angry","mid")
    m "That's fair."
    m "Time is precious, after all..."
    call ton_main("...", "normal", "wide", "base", "stare")
    call ast_main("I've spent enough time today getting lectured by her...","annoyed","base","angry","L")
    m "Isn't she supposed to do that? Teach you?"
    call ast_main("I don't need to be taught!","annoyed","narrow","angry","mid")
    call ast_main("I already know how to cast the spell.","clench","base","angry","mid")
    m "Surely there is some room for you to improve."

    call ast_main("Professor Tonks, take off that coat!","open","closed","base","mid")
    call ton_main("...", "soft", "wide", "worried", "stare")
    call ton_main("...{fast}...", "base", "wide", "worried", "stare")

    # Remove coat.
    call play_sound("equip")
    $ tonks.strip("robe")

    call ctc

    call ton_main("","base","base","base","stare", cheeks="blush")
    pause.8

    call ast_main("See, I told you I could do it!","smile","narrow","base","mid")
    m "Great... Don't get cocky..."
    call ast_main("Don't you see, Professor?","annoyed","narrow","base","mid")
    call ast_main("I can make her do whatever I want!","smile","narrow","base","mid")
    call ast_main("I'm the greatest witch of all time!","clench","base","angry","L")
    call ton_main("...", "normal", "base", "raised", "stare")
    call ast_main("If I can pull off the Imperius curse on Professor Tonks...","open","closed","base","mid")
    call ast_main("Any of the other girls will be easy game for me!", "smile", "narrow", "angry", "down") # Game as in "prey".
    call ast_main("I'll make them rue the day they ever made fun of me!","clench","closed","angry","mid")
    call ton_main("...................................................", "annoyed", "wide", "shocked", "stare", hair="annoyed") # Angry at Astoria
    m "......................."
    call ast_main("Tomorrow, I shall have Susan walk through school - parading those ridiculous breasts of hers for all to see! That'll show her!","angry","narrow","angry","R")
    call ton_main("!!!", "upset", "wide", "shocked", "stare", hair="angry") # Very angry
    call ast_main("And then shove her into our common room - and all the boys will laugh at her cow udders!","annoyed","narrow","angry","R")
    call ton_main("*Tzzzzz*!...", "upset", "closed", "annoyed", "mid", hair="angry", emote="angry")
    call ton_main("That's enough!","scream","base","angry","R", trans=hpunch)

    # Tonks returns to normal, and puts her clothes back on.
    call play_sound("equip")
    $ tonks.wear("all")
    call ton_main("", "mad", "base", "angry", "down")
    pause.8

    call ast_chibi("reset",530,"base")
    call ast_main("What?","clench","base","worried","L")
    call ton_main("Astoria, you are dismissed!","open","closed","angry","mid")
    call ast_main("No! I still wanted to--", "angry", "base", "angry", "mid")
    call ton_main("Dismissed!", "normal", "closed", "angry", "mid")
    call ast_main("........................","annoyed","narrow","angry","R")
    call ast_main("*Tzzz!*...","clench","base","angry","mid")

    # Astoria leaves.
    call ast_walk(action="leave")

    call ton_main("The nerve on that girl, I can't believe it!", "open", "base", "angry", "R", hair="angry", xpos="mid", ypos="base")
    call ton_main("I'm beginning to think teaching her an \"unforgivable curse\" might've been a bad idea after all...", "normal", "closed", "annoyed", "mid")
    m "How so?"
    call ton_main("Didn't you hear her?","open","base","angry","mid")
    call ton_main("She's disregarding all of our advice!... Or at least planning to...", "mad", "base", "angry", "R")
    call ton_main("She's been ignoring my lessons all day!", "annoyed", "closed", "base", "mid")
    call ton_main("She's such a cute and stubborn girl...", "soft", "closed", "angry", "mid")
    call ton_main("We can't have her roaming the school - cursing people as she pleases!", "annoyed", "base", "annoyed", "mid")

    m "So, should we stop?"
    call ton_main("..................", "annoyed", "closed", "annoyed", "mid", hair="neutral")
    call ton_main("Only if she refuses to follow our rules...", "open", "narrow", "annoyed", "downR")
    call ton_main("As long as what we're doing stays within these walls, it shouldn't be too bad.", "normal", "base", "annoyed", "R")
    call ton_main("And besides, Imperio isn't the worst curse you could be a target of, all things considered...", "upset", "base", "annoyed", "down")
    m "I thought it was dangerous?"
    call ton_main("Only if you use it in such a way!", "open", "narrow", "annoyed", "down")
    call ton_main("The curse itself is quite harmless...", "annoyed", "closed", "base", "mid")
    call ton_main("And it feels really good when you're under its effect...", "soft", "base", "base", "R")
    m "It does?"
    call ton_main("*Mhmm*... yeah...", "horny", "base", "annoyed", "up", hair="horny")
    call ton_main("It's so goood! {heart}", "soft", "narrow", "worried", "ahegao")
    g9 "I think you're enjoying this a bit too much!"
    g9 "Just what would your students think if they knew their teacher gets off on being mind controlled?"
    call ton_main("Oh - be quiet you...", "annoyed", "wide", "annoyed", "up")
    call ton_main("................................", "upset", "wide", "worried", "stare")
    call ton_main("Is it that obvious?", "disgust", "base", "worried", "L")
    g9 "Can't fool a genie..."
    m "I'm a genius, it's in the name."
    m "G{w=0.3} E{w=0.3} N{w=0.5} I{w=0.5} U...{w=1.0}{nw}"
    g4 "G E N I U...{fast} hold on a second..." #This makes the line change expression mid sentence
    call ton_main("Anyway...", "normal", "base", "base", "down")
    call ton_main("I'll have to talk some sense into that girl before we can continue, that's for certain...", "annoyed", "wide", "annoyed", "downR")
    m "Of course..."

    call ton_main("I'm sorry I let this situation get out of hand...", "open", "closed", "worried", "mid")
    call ton_main("It won't happen again, I promise.", "disgust", "base", "worried", "mid")
    m "You did great..."
    g9 "But next time I'd like to see some tits!"
    call ton_main("Of course you would.", "base", "base", "annoyed", "R")
    call ton_main("You love 'em - don't you?", "base", "wide", "annoyed", "mid")
    g9 "That I do!"
    call ton_main("I should get going. It's getting late...", "normal", "base", "shocked", "down")
    m "Until next time..."
    call ton_main("Have a good night, [ton_genie_name].", "soft", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    m "..."
    g4 "G{w=0.3} E{w=0.3} N{w=0.5} I--"
    m "Fuck it..."

    $ ast_mood += 12

    # Increase affection once (this is the third event)
    if ag_st_imperio.counter == 3:
        $ ast_whoring += 1

    jump end_ag_st_imperio


label ag_st_imperio_E4:
    stop music fadeout 1.0

    call ton_walk(action="enter",xpos="desk",ypos="base")
    pause.5

    call ton_chibi("stand","desk","base", flip=True)
    with d3
    pause.1

    call ton_main("Astoria, would you come in here please...","open","closed","base","mid", ypos="head")
    ast "Do I have to?"
    call ton_main("Yes, we already talked about this...","open","base","base","R")
    ast "Fine, whatever..."
    hide screen bld1
    with d3
    pause.1

    #Astoria enters
    call ast_walk(action="enter",xpos=530,ypos="base") # Make sure it's slightly to the left of Tonks' chibi.
    pause.1

    call ton_chibi("stand","desk","base", flip=False)
    with d3
    pause.5

    call play_music("tonks")
    call ton_main("","base","base","base","L", xpos="right", ypos="base")
    call ast_main("...","annoyed","narrow","base","down", xpos="base", ypos="base")

    call ton_main("Astoria... isn't there something you'd like to say to our Headmaster?", "soft", "base", "shocked", "mid")
    m "..."
    call ast_main("Yes...","open","narrow","base","down")
    call ton_main("", "base", "base", "base", "R")
    call ast_main("Sir, I'm sorry about my behaviour during our last training session.","annoyed","base","base","L")
    m "Sure, no big deal--"
    call ast_main("It was wrong of me to scream at Professor Tonks like that, or scream at you...", "open", "narrow", "base", "L")
    m "Fine. Let's just get to--"
    call ton_main("And what else?","open","closed","base","mid")
    call ton_main("","base","base","base","L")
    call ast_main("I was disrespectful, selfish, and mean.","open","closed","base","mid")
    call ast_main("And I should be thankful that you are granting me this opportunity.","open","base","base","mid")
    m "..."
    call ast_main("I'm well aware of what is at stake here, and I shall follow the rules from now on.","clench","narrow","base","down")
    call ast_main("...","annoyed","narrow","base","down") # Looks away
    m "*Ahem* Could we please just get started?"
    g4 "(I'm dying to see some tits!)"
    call ast_main("........................","annoyed","base","base","R")
    call ton_main("Very good, Astoria.","base","happyCl","base","mid")
    call ton_main("I'm proud of you. {heart}", "grin", "base", "base", "R")
    call ast_main(".........................","annoyed","base","base","down") # embarrassed
    m "......................."

    call ton_main("So, let's begin...", "base", "wide", "base", "mid")
    call ast_chibi("wand",530,"base")
    with d3
    call ton_main("Astoria, try and focus on what we went through today...", "open", "base", "base", "down")
    call ton_main("Keep good track of your emotions after channelling the spell...","open","closed","base","mid")
    call ton_main("Anger and rage will cause you to lose control - and eventually break the connection with the target...", "normal", "base", "annoyed", "L")
    call ton_main("Do your best to be as thoughtful, nice, and endearing as you possibly can towards your target...","base","base","base","L")
    call ast_main("","annoyed","base","base","R")
    call ton_main("The stronger the emotional bond - the better.","open","closed","base","mid")
    call ton_main("So try to charm them a bit while you're at it!", "soft", "base", "base", "L")
    call ton_main("It is called a charm for a reason, after all!","base","happyCl","base","mid")
    call ast_main(".....................","annoyed","base","worried","down")
    m "...................."
    call ton_main("Not a very good joke - I gather...", "annoyed", "wide", "raised", "mid")
    m "I'm sorry. I was only half paying attention..."
    call ton_main("Very well...", "upset", "base", "shocked", "L")

    call ton_main("Now then, let's get on with it, shall we?", "base", "wink", "annoyed", "mid")
    call ast_main("...","annoyed","base","base","mid")
    call ast_chibi("wand_casting",530,"base")
    with d3
    call ton_main("Astoria, as soon as I'm ready, I'd like you to--","open","closed","base","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call ast_main("","annoyed","base","base","L")
    call ton_main(".........................", "mad", "wide", "shocked", "ahegao", hair="horny") # shock

    m "......................"
    call ton_main("*Aaaaah*...", "open", "base", "shocked", "ahegao", hair="horny", cheeks="blush")
    call ast_chibi("wand",530,"base")
    with d3
    call ast_main("I'm getting really good at this!","smile","base","angry","L")
    call ton_main(".......................", "normal", "wide", "base", "stare")
    call ast_main("What shall I have her do, Professor?","smile","base","base","mid")

    m "How about..."
    menu:
        "\"Make her turn around!\"": # She's facing Astoria
            call ast_main("Very well, Sir.","base","base","worried","mid")
            call ast_main("Professor, please turn around for me...","open","base","base","L")
            call ton_main("*Hmm*... Yes!", "base", "base", "worried", "stare")

            # Tonks turns around
            call hide_characters
            hide screen bld1
            with d3
            pause.1

            call ton_chibi("stand","desk","base", flip=True)
            with d3
            pause.5

            call ast_main("","clench","wink","worried","mid")
            call ton_main("","base","base","base","L", flip=True)
            pause.8

            call ton_main("........................", "horny", "wide", "base", "stare")
            call ast_main("*Uhm*...","clench","narrow","worried","R") # Astoria is uncomfortable

        "\"Let her face me!\"":
            call ast_main("Very well...","open","base","base","mid")

    call ast_main("And now?", "base", "base", "base", "mid")
    g9 "Her coat! Tell her to take it off!"
    call ast_main("Professor Tonks, please remove your coat for me.","open","base","worried","L")
    call ton_main("...","base","base","base","stare")

    # Remove coat.
    call play_sound("equip")
    $ tonks.strip("robe")
    call ton_main("", "base", "base", "base", "ahegao")
    pause.8

    g9 "You're doing great, Astoria!"
    g9 "It's like watching you teach a puppy new tricks..."
    call ton_main("..........................", "soft", "narrow", "base", "ahegao") # ahegao
    call ast_main("If you say so, Sir.","clench","base","base","down")
    m "Let's move on to the next trick, shall we?"
    g9 "Ask her to get those tits out!"
    call ast_main("Her what?!","clench","base","base","mid")
    m "Her breasts, girl..."
    m "Tell her to remove her top."
    call ast_main("Right now?","open","wink","base","mid")
    call ast_main("But...","clench","base","base","mid")

    if tonks_flip == -1: # Facing Astoria
        call ast_main("Can I at least tell her to turn around again?","clench","base","worried","R")
        m "Why? Scared of your teacher's enormous rack?"
        call ast_main("What?{w} As if!","annoyed","narrow","angry","R")
        g9 "I doubt she'd like to show them to you anyway..."
        call ton_main("......................", "soft", "base", "base", "ahegao", hair="horny") # Ahegao
        call ast_main("............","annoyed","base","worried","mid")
        m "Go on..."

    else: # Facing Genie
        call ast_main("I'm not sure if she'd be okay with that.","open","base","worried","mid")
        m "This again?"
        call ast_main("You'd have to close your eyes first, Professor!","open","closed","base","mid")
        m "What?"
        m "Are you giving orders to me now as well, girl?"
        call ast_main("Close your eyes!","angry","narrow","angry","mid")
        m "Not a chance!"
        call ast_main(".......................","annoyed","base","angry","R")
        call ast_main("It won't be my fault if she gets mad at you later!","open","narrow","base","down")
        m "Sure, whatever..."
        m "Go on already!"

    g9 "Let's get those tits out!"
    call ast_main("Professor Tonks, I need you to remove your...","open","base","worried","R")
    call ast_main("Your shirt...","clench","base","base","down")
    call ton_main("................", "normal", "base", "shocked", "stare")
    g9 "!!!"

    # Remove top.
    call play_sound("equip")
    $ tonks.strip("top")
    if tonks.is_worn("bra"): # Remove bra if True
        call ast_main("and your bra...","clench","base","base","down")
        call play_sound("equip")
        $ tonks.strip("bra")
    call ton_main("", "base", "wide", "shocked", "ahegao", cheeks="blush")
    call ast_main("","annoyed","closed","base","mid")
    call ctc

    if tonks_flip == -1: # Facing Astoria
        call ast_main("Is she... is she doing it?","clench","closed","worried","mid") # closed eyes
        call ton_main(".............", "grin", "wink", "base", "L", cheeks="blush") # horny
        g9 "Why don't you see for yourself?"
        g9 "Open your eyes, girl!"
        call ast_main("I don't want to...","open","closed","worried","mid")
        m "How rude..."
        g9 "It seems to me like your teacher would really like to show you something!"
        call ast_main("....................","clench","closed","base","mid") # eyes still closed
        call ton_main("", "base", "wide", "base", "stare", cheeks="blush")
        call ast_main("*Eeeeehig*...","clench","wink","base","mid") # Weird sound.
        call ast_main("....................","annoyed","narrow","worried","R")
        g9 "That wasn't too bad now, was it?"
        call ton_main(".......................", "base", "base", "base", "ahegao", hair="horny", cheeks="blush") # ahegao

    else:
        g9 "Now would you look at that!"
        call ton_main("................", "soft", "wide", "shocked", "stare") # horny
        m "Those are some great breasts your teacher has there!"
        call ton_main("................", "soft", "wide", "base", "stare", hair="horny") # ahegao
        call ast_main("I asked you not to look, Professor!","open","closed","angry","mid")
        g9 "I don't believe she minds, does she?"
        call ast_main("","clench","narrow","worried","R")
        call ton_main("................", "horny", "wide", "base", "stare", cheeks="blush") # ahegao

    m "*Hmm*..."
    m "We might be able to push her even further!"
    call ast_main("Further, Sir? How?","annoyed","wink","base","mid")
    g9 "By getting her to remove the rest of her clothing, of course!"
    call ton_main("..............", "horny", "base", "shocked", "ahegao", hair="horny", cheeks="heavy_blush") # angry/horny expression
    g9 "What do you think? Want to give it a try?"
    call ast_main("Would that really be necessary, Sir?","open","base","base","R")
    m "Yes.{w=0.3} it.{w=0.3} would."
    call ast_main("We--{w=0.5} we could try again next time, Professor...","clench","narrow","base","down")
    m "Next time?"
    m "Where did your enthusiasm go all of a sudden?"
    m "Weren't you so eager to practise this spell?"
    call ast_main("Yes, but...","annoyed","narrow","base","down")
    m "Yes?"
    call ast_main("I don't have to explain myself to you!", "annoyed", "narrow", "angry", "down")
    call ton_main("", "annoyed", "wide", "shocked", "ahegao", cheeks="blush")
    call ast_main("...","annoyed","narrow","angry","R")

    stop music fadeout 2.0
    m "..."
    call ast_main("I should go to bed...","open","narrow","base","R")
    m "Is that so..."
    call ast_main("I-- *Uhm*...{w=0.5} I'm tired, Sir.","open","narrow","base","mid")
    call ast_main("*yaaaaawn*!...","open","closed","worried","mid")
    call ast_main("See?","annoyed","base","base","mid")
    m "..."
    m "Very well..."
    m "You are dismissed."
    call ast_main("...","clench","narrow","worried","down") #embarrased

    # Astoria leaves and spell fades
    call hide_characters
    hide screen bld1
    with d3
    pause.5

    call ast_chibi("reset",530,"base", flip=True)
    with d3
    pause.2

    call ast_walk(action="leave")
    pause.5

    call ton_chibi("stand","desk","base", flip=False)
    with d3
    pause.8

    call play_music("tonks")
    call ton_main("Well, that was interesting...", "annoyed", "wide", "base", "downR", hair="neutral", xpos="mid", ypos="base", flip=False)
    m "Do you have any idea why she wanted to leave so abruptly?"
    call ton_main("I have a couple of theories, actually...", "soft", "closed", "base", "mid")
    m "*Mhmm*..."
    call ton_main("..................", "soft", "wide", "base", "down", hair="horny") # horny stare
    call ton_main("Would you like me to put my clothes back on?", "grin", "narrow", "raised", "mid")
    g9 "Don't feel pressured!"
    call ton_main("Very well, then...", "base", "narrow", "base", "mid")

    # screenshake
    with hpunch
    call nar(">Tonks gives her breasts a quick shake for you.")

    g9 "Sweet!"
    call ton_main("...............", "horny", "wink", "base", "L")
    call ton_main("She made some good progress today, unlike last time...", "base", "base", "shocked", "L")
    call ton_main("And she was very polite!","base","happyCl","base","mid")
    call ton_main("But she isn't quite there yet...", "upset", "base", "shocked", "down")

    m "Does she require more training?"
    call ton_main("Yes, actually...", "soft", "narrow", "shocked", "downR")
    call ton_main("She'll need a lot more training to pull off the Imperius curse properly...", "open", "closed", "base", "R")
    call ton_main("And, as you could see... it doesn't have much of an effect on me.", "soft", "base", "shocked", "down")
    call ton_main("I could have easily avoided doing everything she's told me today, if I wanted to...", "open", "closed", "base", "mid")
    g9 "But you didn't!"
    call ton_main("It wasn't my intention to break her spirit again... She was really trying!", "upset", "closed", "worried", "R")
    call ton_main("Now, as you know, I'm a trained Auror...", "normal", "wide", "shocked", "mid")
    m "A very \"talented\" one at that!"
    call ton_main("Are you just praising my tits, Sir?", "soft", "narrow", "annoyed", "mid")
    g9 "Every part of your body is worthy of praise!"
    call ton_main("Well... thank you, [ton_genie_name].", "base", "happyCl", "shocked", "mid")

    # Screenshake
    with hpunch
    call ton_main("", "horny", "narrow", "shocked", "mid")
    call nar(">Tonks gives her breasts another quick shake for you.")

    call ctc

    call ton_main("I suggest we do one more training session, and then call it from there...", "base", "wide", "base", "mid")
    m "Sounds good to me..."
    call ton_main("Believe me, it's gonna be a great one!", "soft", "wink", "base", "mid")
    g9 "Are we going to see more of your... talents?"
    call ton_main("How would you like to see {b}all{/b} this Auror has to offer?", "horny", "closed", "annoyed", "mid") # horny
    g9 "Looking forward to it!"
    call ton_main("Have a good night, [ton_genie_name]!","base","base","angry","mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    g9 "I hope she's planned something big!"

    # Increase affection once (this is the fourth event)
    if ag_st_imperio.counter == 4:
        $ ast_whoring += 1

    jump end_ag_st_imperio


label ag_st_imperio_E5:
    stop music fadeout 1.0
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("astoria")
    call ast_main("","smile","base","base","mid", xpos="base", ypos="base")
    call ton_main("Hi, Professor!", "base", "wide", "base", "mid", xpos="right", ypos="base")

    call ast_main("Hello!","smile","closed","base","mid", emote="happy") # Happy
    m "All cheered up today, Astoria?"
    call ast_main("Yes, Sir.","grin","base","base","mid")
    call ton_main("She should be. We made some real progress today.", "grin", "narrow", "base", "R")
    call ton_main("I'm very impressed with her, I've got to say!", "base", "base", "base", "mid")
    call ton_main("She's very close to mastering it!", "base", "happyCl", "base", "mid")
    call ast_main("Really?!","smile","base","base","R")
    g9 "Is that so?"
    g9 "Care for a demonstration?"
    call ast_main("","smile","base","base","mid")
    call ton_main("Of course.","base","base","base","mid")
    call ton_main("I'm confident she'll be able to make me do {b}anything{/b} you want today.","horny","base","base","L", hair="horny") # Horny stare
    g9 "Counting on it!"
    call ton_main("Make sure to give her some good suggestions, Professor!","open","base","angry","mid")
    g9 "Absolutely!"
    call ton_main("And Astoria...","open","base","raised","L")
    call ton_main("Today we are going to try to push me to the limit.","base","base","base","L")
    call ton_main("You will have me do whatever Professor Dumbledore commands, without question!", "soft", "wide", "annoyed", "L")
    call ast_main("I suppose...","annoyed","base","base","down")
    call ton_main("We will only stop with today's training once I'm able to... resist, am I clear?", "open", "closed", "base", "L")
    call ast_main("Okay, Professor...","annoyed","base","base","R")

    call ton_main("You may start now, Astoria...", "base", "narrow", "base", "L")
    call ast_chibi("wand",530,"base")
    with d3
    call ton_main("...................","base","closed","base","mid")
    call ast_chibi("wand_casting",530,"base")
    with d3
    call ast_main("...................","annoyed","base","base","down")
    call ton_main("Astoria? Would you cast the curse - please?","open","base","base","L")
    call ast_main("...................","clench","base","base","down")

    # Astoria casts imperio.
    stop music fadeout 2.0
    call ast_main("Imperio...{w=0.8}{nw}","open","closed","base","mid")

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call ast_chibi("wand_imperio",530,"base")
    call play_sound("spell")
    with hpunch
    pause.8

    call play_music("trance")
    call ast_main("","base","base","base","L")
    call ton_main("*Hmm*............", "soft", "base", "worried", "ahegao", hair="horny")

    g9 "(Here we go!)"
    call ast_main("..............","grin","base","base","L")
    call ast_chibi("wand",530,"base")
    with d3
    call ast_main("What should we start with, Professor?","open","base","worried","mid")
    m "Let's just try the same things as last time..."
    m "Ask her to take that coat off first."
    call ast_main("Very well...","base","base","base","mid")
    call ast_main("Professor, would you please take off your coat?","open","base","base","L")
    call ton_main("*Hmm*... My coat?...", "open", "base", "worried", "stare")
    call ton_main("...............", "normal", "wide", "base", "stare")
    call ton_main("Sure {heart}", "silly", "happyCl", "base", "mid")

    # Remove coat.
    call play_sound("equip")
    $ tonks.strip("robe")
    call ton_main("","base","base","base","ahegao")
    pause.8

    call ast_main("Yay!", "smile", "narrow", "base", "mid")
    call ast_main("Her shirt was next, right?","base","base","angry","mid")
    m "That is correct."
    call ast_main("Yes! Take off your shirt, Professor!","clench","base","angry","L") # menacing
    call ton_main("*Ahhh*................", "soft", "base", "base", "ahegao", cheeks="blush")

    # Remove top.
    call play_sound("equip")
    $ tonks.strip("top")
    $ tonks.strip("bra")
    call ton_main("","base","base","base","ahegao", cheeks="blush")
    pause.8

    call ast_main("She did it!", "smile", "base", "base", "mid", cheeks="blush")
    g9 "Well{w=0.5} {i}fucking{/i}{w=0.7} done!"
    m "Next, I'd like you to--"
    call ast_main("Ask her to take off her trousers!","grin","base","angry","L")
    g9 "Yes please!"
    call ast_main("Professor, please take off your trousers...","open","closed","base","mid")
    call ton_main("*hngh*...", "mad", "closed", "base", "ahegao", cheeks="blush")

    # Remove bottom.
    call play_sound("equip")
    $ tonks.strip("bottom")
    $ tonks.strip("panties")
    call ton_main("", "base", "base", "worried", "ahegao")
    pause.5
    call ast_main("","annoyed","narrow","angry","down")
    pause.8
    call ton_main("", "horny", "wide", "shocked", "ahegao", cheeks="blush")
    call ctc

    call ast_main("Oh wow...","angry","base","base","down")
    call ton_main("...................", "horny", "base", "base", "ahegao", cheeks="blush")
    call ast_main("Professor, how can it be that you're not wearing any underwear?!","angry","base","worried","down") # angry embarrassed
    m "Yes, Miss Tonks."
    g9 "Explain yourself!"
    call ton_main("*Hmm*.......", "normal", "base", "worried", "stare", cheeks="blush")
    call ast_main("Answer us!","clench","closed","angry","mid")
    call ton_main("I don't like to wear them...", "open", "wide", "worried", "stare", hair="sad", cheeks="blush")
    call ast_main("Why?!","open","narrow","angry","L") # angry
    call ton_main("I feel so much better without a bra on... or panties...", "soft", "wide", "base", "stare", hair="horny")
    call ast_main("You're a teacher! This is disgusting!","clench","closed","angry","mid", emote="angry")
    g4 "Dis-{w=0.8}gusting!"

    with hpunch
    call ton_main("{heart} {heart} {heart}", "soft", "happyCl", "worried", "ahegao", cheeks="blush")
    call ast_main("I can't believe my teacher is such a slut!","angry","narrow","angry","L")
    g4 "Des-{w=0.8}picable!"
    call ast_main("Are you a slut, Professor?","open","narrow","angry","L")
    call ton_main("...............", "normal", "shocked", "worried", "stare", cheeks="blush") # ahegao
    call ast_main("Are you?!","clench","base","angry","L")
    call ton_main("I am! {heart}", "soft", "base", "worried", "ahegao", hair="horny", cheeks="blush")
    call ast_main("I knew it!","smile","narrow","angry","L")
    call ast_main("That's why she has such difficulty resisting our commands!","open","base","worried","mid")
    m "Yes. She's clearly trying her hardest..."

    call ton_main("","normal","base","shocked","ahegao", hair="horny", cheeks="blush")
    call ast_main("Professor Dumbledore, you knew exactly what her weakness would be!","smile","base","base","mid")
    m "I did?"
    m "*ahem*... I mean, of course I did!"
    call ast_main("We're taking off her clothes, because that's what she enjoys! But could never do in school!","angry","narrow","angry","L")
    call ast_main("Which makes it easier for me to channel the Imperius curse...","grin","base","angry","mid")
    call ast_main("Because she's nothing but a weak-minded slut!","open","narrow","angry","L") # angry
    call ton_main("................", "soft", "narrow", "shocked", "ahegao", hair="horny", cheeks="blush") # ahegao
    m "You're on point!"

    call ast_main("Take off the rest of your clothes!","clench","base","angry","L") # angry
    g9 "Yes!"
    call ast_main("Take them off, you slut!","scream","closed","angry","mid", trans=hpunch) # scream
    call ton_main("........{heart}", "normal", "wide", "shocked", "stare", cheeks="blush")

    # Strip naked. Removes clothes and stockings.
    call play_sound("equip")
    $ tonks.strip("stockings")
    $ tonks.strip("gloves")
    call ton_main("", "grin", "base", "base", "ahegao", hair="horny", cheeks="blush")
    call ast_main("", "horny", "narrow", "angry", "L")
    call ctc

    call ast_main("Look, Professor!","smile","narrow","angry","L")
    call ast_main("I got her to be completely naked!","smile","base","angry","mid")
    g9 "Excellent work, [astoria_name]!"
    call ast_main("Thank you, Sir!","smile","closed","base","mid")
    call ton_main(".............", "silly", "happyCl", "base", "stare", cheeks="blush")

    #screenshake
    with hpunch
    call nar(">Tonks gives her tits a little sway...")

    g4 "*argh!* (I can't take it anymore!)"

    g4 "..."
    menu:
        "-Start masturbating!-":
            $ masturbating = True
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerk_off_behind_desk")
            with d5
            pause.8

            show screen bld1
            call nar(">You take out your cock and start jacking off.")

    call ton_main(",", "horny", "narrow", "raised", "L", cheeks="blush")
    call ast_main("What shall we do now?","open","base","base","L")
    "*fap-fap-fap*"
    call ton_main(",", "soft", "narrow", "shocked", "L", hair="horny", cheeks="blush")
    call ast_main("Professor?","annoyed","narrow","angry","mid")
    m "What?"
    m "Oh..."
    g9 "Get her to climb my desk!"
    g9 "Have her do a little dance for us."
    call ast_main("Did you hear him, Professor?","smile","closed","base","mid")
    call ast_main("Get on that desk, and start dancing!","open","narrow","angry","L")
    call ton_main("Yes...{heart}", "grin", "wink", "base", "mid", hair="horny")

    # Climb desk and dance.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    pause 2

    call nar(">After giving you a playful wink, Tonks suggestively climbs on top of your desk, getting a good glimpse of your rock-hard cock...")
    pause 1

    call ast_chibi("wand","desk","base") # Still in wand pose.
    call ton_chibi("stand","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    call bld
    g9 "This is getting better and better..."
    "*fap-fap-fap*"
    call ton_main("","horny","base","raised","down", xpos="mid", ypos="base")

    call ast_main("Move your hips!","open","narrow","base","L")
    call hide_characters
    hide screen bld1
    with d3
    pause.1

    # Tonks dances.
    call ton_chibi("stand","on_desk","on_desk", flip=True)
    with d3
    pause.8
    call ton_chibi("stand","on_desk","on_desk", flip=False)
    with d3
    pause.5

    call ast_main("","horny","base","angry","L")
    call ton_main("............", "grin", "base", "base", "mid")
    call ast_main("She's really doing everything I tell her!","smile","base","angry","mid")
    call ast_main("Look how easy it is, Professor!","smile","closed","base","mid", emote="hearts" ,trans=hpunch)

    call nar(">Astoria joyfully jumps up and down on the spot, making a happy squeal...")
    call hide_characters
    hide screen bld1
    with d3
    pause.1

    show screen astoria_wand_drop
    call ast_chibi("reset","desk","base") # No wand pose.
    pause.355
    $ renpy.play('sounds/wand_drop.mp3')
    pause.5

    show screen bld1
    call nar(">Unknowingly dropping her wand...")

    call ton_main("","upset","base","base","R")
    m "*Uhm*..."
    call ast_main("What's next, Professor?","smile","narrow","angry","mid")
    m "Next?"
    call ast_main("What else should we make her do?","clench","narrow","angry","L")
    call ast_main("Can I walk her around school like this?","grin","narrow","worried","L")
    m "What?"
    m "Are you serious?"
    call ast_main("Please!","upset","base","base","mid")
    call ton_main("..............", "soft", "base", "raised", "down")
    m "(That might be a good idea for another time...)"
    m "Not today, I'm afraid..."
    call ton_main("","annoyed","closed","base","mid")
    call ast_main("*Aww*...","annoyed","narrow","base","down")
    g9 "Don't worry, I have an even better idea!"
    g9 "Could you ask her to get under my table?"
    call ast_main("*Huh*?... To do what?","open","base","worried","mid")
    call ton_main("To give him a blowjob...", "open", "closed", "shocked", "mid") # Tonks answers for Genie
    call ast_main("Professor Tonks!{w} Are you serious?","scream","base","base","L") # shocked
    call ast_main("Why would she want to do that? That's disgusting!!!","clench","base","worried","mid")
    m "That-- *Uhm*..."
    m "That wasn't what I would have suggested, but..."
    m "I'm willing to give her a chance to try..."
    m "Try to resist that urge, I mean..."
    call ast_main("As long as I don't have to look at it...","angry","narrow","base","R")
    call ast_main("Professor Tonks, you can get under Professor Dumbledore's desk... and...","open","closed","base","mid")
    call ast_main("Do \"that\" thing...","angry","base","worried","mid")
    call ton_main(".............", "base", "base", "shocked", "down", emote="hearts")

    call hide_characters
    hide screen bld1
    with d3
    #show screen blkfade
    #with d5
    pause.2

    call play_sound("door")
    pause.8

    call sna_chibi("stand","door","base")

    hide screen blkfade
    with d5

    # Snape enters...
    call sna_main("Genie, I was wondering if you could help me with--","snape_35", ypos="head")
    stop music fadeout 2.0
    call play_sound("scratch")
    call sna_main("!!!","snape_11", ypos="head")
    hide screen bld1
    with d3
    pause.1
    call ton_chibi("stand","on_desk","on_desk", flip=True)
    with d3
    pause.5

    call ton_main("Shit!", "mad", "base", "angry", "L", hair="annoyed", xpos="left", flip=True)
    hide screen tonks_main
    hide screen bld1
    with d3
    pause.1
    call ast_chibi("stand","desk","base", flip=True)
    with d3
    pause.5

    call ast_main("*Huh*?!","annoyed","narrow","worried","L", xpos="mid", flip=True)
    call ast_main("*Aaaaaaaaaah!!!*.......................","scream","base","base","L", emote="shocked", trans=hpunch) # Screams
    hide screen astoria_main
    hide screen bld1
    with d3
    pause.1

    call play_sound("running")
    call ast_chibi("hide")
    call teleport("astoria", effect=False)
    call ast_chibi("stand",210,275+180, flip=True) # Next to Genie's chair.
    hide screen bld1
    with d3
    pause.1

    call gen_chibi("sit_behind_desk")
    with d3
    pause.5

    call bld
    call nar(">You quickly put away your priorly liberated cock.")
    g4 "What's going on?"
    call sna_main("Yes! I'd like to know that as well!","snape_43")
    g4 "Snape?!"
    if hg_strip.trigger == True: # Snape saw Hermione strip
        g4 "Damn it, not you again!"
        g4 "(You walking cock-block!)"

    else:
        g4 "Damn it, what are you doing here?"

    call sna_walk(620,"base")
    pause.2

    call play_music("snape")
    call sna_main("What on Earth is going on here?!","snape_08", xpos=580 ,ypos="base")
    call sna_main("You two better explain to me what I just witnessed!","snape_32")
    call ton_main("Stop being such a wuss, Severus!", "mad", "base", "angry", "L", hair="angry", xpos="mid", flip=True)
    call ton_main("We were just practising some spells with Miss Greengrass.", "annoyed", "base", "base", "R", hair="upset")
    call sna_main("And that required you to be undressed? In front of a student?","snape_10")
    call ton_main("Well... she was the cause of it...", "clench", "base", "base", "down", cheeks="blush")
    call sna_main("Caused you to strip?","snape_34")
    call sna_main("Which spells are you teaching that girl?!","snape_25")
    call sna_main("Don't tell me you--","snape_36") # Shocked
    call ton_main("The Imperius Curse.", "soft", "closed", "base", "mid", cheeks="blush")
    call sna_main("I can't believe you two...","snape_08")
    call ast_main("Am I in trouble now, Professor?","annoyed","base","base","L", xpos=10) # Asking Snape
    call sna_main("Keep quiet, girl!","snape_34")
    call sna_main("............","snape_04") # Snape sees the wand.

    call sna_main("Is that your wand lying on the ground there?","snape_03")
    call ast_main("My wand?","annoyed","base","base","down")
    call ast_main("Oh no, I must have dropped it when you came in, Sir.","clench","closed","worried","mid")
    call sna_main("Well, pick it back up!","snape_32")
    call sna_main("A Slytherin takes better care of her equipment...","snape_10")
    call ast_main("Yes. I'm sorry, Professor.","clench","closed","angry","mid", emote="sweat")

    call ast_walk(path=[(270, 290+180), (370,290+180), ("desk","base")])
    call ast_chibi("stand","desk","base", flip=False)
    with d3
    pause.1
    call play_sound("lock")
    hide screen astoria_wand_drop
    pause.5

    call sna_main("You may leave, Astoria.","snape_09", ypos="head")
    call ast_main("...","clench","base","base","down", ypos="head", flip=True)
    call sna_main("Miss Greengrass...","snape_04")
    call ast_main("Yes sir.","annoyed","base","base","down")

    #astoria leaves
    $ snape_chibi.zorder = 3
    $ astoria_chibi.zorder = 2

    call sna_chibi("stand",620,"base") # Updates Zorder.
    call ast_walk(action="leave")

    $ snape_chibi.zorder = 2 # Reset to default.

    # Tonks hops off your desk and walks closer to Snape.
    call play_sound("climb_desk")
    show screen blkfade
    with d5
    pause 1

    call ton_chibi("stand","desk","base", flip=True)
    hide screen blkfade
    with d5
    pause.5

    call ton_walk(550,"base")
    pause.8

    call ton_main("","annoyed","base","annoyed","L", xpos=275, ypos="base", flip=True)
    call sna_main(".........................","snape_05", xpos=580 ,ypos="base")

    call play_music("tonks")
    call ton_main("Like what you see?", "upset", "base", "raised", "L", hair="horny") # Bit flirty, maybe just to calm Snape down.
    call sna_main(".............................","snape_12") # blushing
    g4 "You couldn't have picked a worse time to burst in here..."
    call sna_main("I can imagine that...","snape_18")

    call sna_main("So, Nymphadora...","snape_04")
    call ton_main("*Tzzzzs*!......", "annoyed", "closed", "annoyed", "mid", hair="angry")
    call sna_main("Would you mind explaining to me why you were naked in the headmaster's office - with a student present?","snape_03")
    call sna_main("One of my students - at that.","snape_10")
    call ton_main("Are you jealous?", "soft", "narrow", "base", "L", hair="horny")
    call sna_main("............","snape_14")

    call sna_main("The question...","snape_18")
    call ton_main("It's this Astoria girl...", "soft", "base", "annoyed", "R", cheeks="blush")
    call ton_main("There's something wrong with her...", "open", "narrow", "base", "down")
    call ton_main("She's cursed you see!", "open", "wide", "worried", "L")
    call ton_main("A blood curse... very unfortunate.", "mad", "base", "worried", "down")
    call sna_main("A blood curse you say?","snape_09") #incredulous
    call sna_main("Now that sounds serious...","snape_05")
    call ton_main("Yes, very serious!", "clench", "wide", "worried", "down")
    call ton_main("Been in her family for generations even.", "disgust", "wide", "base", "mid")
    call sna_main("And what are the effects of this \"Blood curse\" exactly?","snape_04")
    call ton_main("Well... I believe that this curse has rendered her practically asexual!", "clench", "base", "worried", "L")
    call sna_main("What nonsense...","snape_07")
    m "........................."
    call ton_main("How dare you!", "mad", "closed", "angry", "L")
    call ton_main("I can recognise someone that's under a curse!", "open", "narrow", "angry", "down")
    call ton_main("I've been an auror for three years now, I'll have you know!", "mad", "base", "angry", "R")
    call sna_main("Working at that precious ministry of yours has really rubbed off on you, hasn't it?","snape_02")
    m "That's enough, Severus."
    call sna_main("...","snape_35")
    m "What business is conducted in this office is none of your concern."
    m "You're excused..."
    call sna_main("..................","snape_04")
    call sna_main("Very well...","snape_03")
    call sna_main("Genie...{w} Nymphadora...","snape_09")
    call ton_main("..................", "mad", "base", "angry", "L", hair="angry") # Angry stare

    #Snape leaves
    call sna_walk(action="leave")

    call ton_chibi("stand","mid","base", flip=False)
    with d3
    pause.2
    call ton_walk("desk","base")
    pause.5

    call ton_main("Thank you...", "normal", "base", "worried", "mid", hair="neutral", xpos="mid", ypos="base", flip=False)
    m "..."
    m "Now..."

    menu:
        "-Prompt her to be honest with herself-":
            call bld
            m "I think it's time for some honesty."
            call ton_main("Regarding?", "soft", "base", "shocked", "downR")
            m "Everything that we've been doing with the Astoria girl."
            call ton_main("Oh...","upset","base","worried","down")
            call ton_main("Well, we've been helping her haven't we?", "open", "base", "shocked", "down", cheeks="blush")
            call ton_main("She's such an uptight and oppressed cute little...{w=0.4} girl.", "upset", "closed", "raised", "down", cheeks="blush")
            call ton_main("...", "mad", "narrow", "base", "downR", cheeks="blush")
            call ton_main("How can I not help her, even if she's a Slytherin.", "upset", "closed", "base", "mid", cheeks="blush")
            m "[tonks_name]... You aren't convincing anyone."
            call ton_main("To think such an innocent girl could be the victim of such an--", "open", "closed", "base", "down", cheeks="blush")
            m "Tonks!"
            call ton_main("Alright...", "annoyed", "base", "annoyed", "down") #exasperated
            call ton_main("The blood curse may have been a little white lie on my part.", "annoyed", "narrow", "base", "down")
            m "And?"
            call ton_main("And the imperio training with Astoria may have been for my own benefit.", "soft", "narrow", "annoyed", "downR")
            m "..."
            call ton_main("Having her cast it on me was exclusively for my own personal enjoyment.", "annoyed", "base", "base", "down", cheeks="blush")
            m "(What a surprise...)"
            m "Why weren't you honest with me?"
            call ton_main("*Sigh*", "open", "narrow", "base", "R")
            call ton_main("Perhaps I've been taking this favour business... thing a bit too lightly.", "open", "narrow", "raised", "down", cheeks="blush")
            call ton_main("I've been telling myself that it's as much for the students benefit as it is my own.", "upset", "closed", "worried", "mid")
            call ton_main("\"I'll help them explore their sexuality, it'll do them good.\"", "annoyed", "closed", "base", "mid")
            m "We both know that is not the reason why we're doing this."
            call ton_main("Yes...", "upset", "base", "base", "down")
            call ton_main("A small voice in my head knows it...", "annoyed", "base", "base", "mid")
            call ton_main("And I can't help that I'm just so god...{w=0.4} damn...{w=0.3} horny!", "open_wide", "closed", "angry", "mid", hair="angry")
            call ton_main("All the bloody time!", "open_wide_tongue", "base", "base", "ahegao", hair="horny")
            call ton_main("See!", "annoyed", "base", "annoyed", "up", hair="horny")
            call nar(">You notice the bright pink colour of her hair - once again...")
            m "You should stop lying to yourself, it's not healthy..."
            m "I'm immortal - and even I know that!"
            m "Embrace why you chose to be a part of this, you've got a pretty good gig here."
            call ton_main("Yes, you're right.", "soft", "narrow", "base", "L")
            m "You're doing this for yourself, it's okay to be selfish."
            g4 "Think about how much you've endured at that ministry."
            call ton_main("...", "upset", "closed", "annoyed", "ahegao")
            g9 "Think of it as your reward! The students should be happy to have such a loving teacher as you."
            call ton_main("Thank you... sir.", "soft", "closed", "base", "mid")

        "-Call her out on her bullshit-":
            call bld
            m "I think there's someone who hasn't been very honest here..."
            call ton_main("Sorry?","upset","base","worried","mid")

            #Music changes and darker overlay on screen
            call play_music("playful_tension")
            show screen blktone
            with d3

            m "You seem to think you're above what we're doing here."
            m "That you're doing the students a favour rather than accepting it's for your benefit."
            m "Do you know what I think?"
            call ton_main("N-no...", "upset", "wide", "worried", "R")
            m "I think that you've been fabricating this curse, to get what you really wanted - all along."
            m "Not for the good of Miss Greengrass..."
            call ton_main("...", "mad", "base", "worried", "R", hair="upset")
            g4 "Someone's been a naughty girl... acting all innocent with the ones that welcomed her into their scheme..."
            m "Or perhaps you've been trying to justify your actions... to yourself?"
            m "Is that right?"
            call ton_main("That's...","upset","closed","worried","mid", hair="scared")
            m "I think we both know what this means, don't we?"
            m "Miss Tonks..."
            m "What this means is that you're no different than Snape and I."
            m "But you have yet to accept it..."
            m "And if you're unable to, well in that case..."
            call ton_main("I can! I have!", "open_wide", "closed", "worried", "mid")
            m "Are you sure? Because if you're not in on this one hundred percent. Perhaps this may have been a mistake."
            call ton_main("I...", "open", "base", "worried", "down")
            g4 "Say it!"

            $ menu_y = 0.7
            menu:
                "\"You're a selfish slut!\"":
                    call ton_main("Yes!", "mad", "wide", "shocked", "stare", hair="horny")
                    call ton_main("I'm a selfish slut!", "open_wide_tongue", "closed", "worried", "mid", hair="horny")
                "\"You're a filthy pervert!\"":
                    call ton_main("Yes!", "mad", "base", "worried", "mid", hair="horny")
                    call ton_main("I'm a filthy,{w=0.6} {b}fucking{/b}{w=0.4} pervert!", "open_wide_tongue", "closed", "worried", "mid", hair="horny")
                "\"You're nothing more than a whore!\"":
                    call ton_main("Yes!", "mad", "base", "worried", "mid", hair="horny")
                    call ton_main("I'm nothing but a cheap,{w=0.6} {b}fucking{/b}{w=0.4} whore!", "open_wide_tongue", "closed", "worried", "mid", hair="horny")
            call reset_menu_position

            call ton_main("... {w}This is what I want!", "mad", "wide", "annoyed", "down")
            m "Good, you're doing this for yourself, and nobody else..."
            m "You'd do good to remember that."
            call ton_main("Yes, Sir.", "base", "happyCl", "shocked", "mid", cheeks="blush")

            #Overlay goes away and music returns to normal
            call play_music("tonks")
            hide screen blktone
            with d3

    m "Now, with that out of the way..."
    m "Are you ready to take this to the next step?"
    m "Have you considered letting miss Greengrass cast the curse on a more susceptible subject?"
    call ton_main("...", "annoyed", "wide", "base", "R")
    m "Miss Tonks..."
    call ton_main("Fine, let's do it!", "mad", "closed", "annoyed", "down")
    g9 "Good."
    m "Do you have a student in mind... someone weak-minded, perhaps?"
    g9 "That Susan girl... How about her?"

    call ton_main("Susan Bones?", "open", "wide", "shocked", "stare")
    call ton_main("But, she's a Hufflepuff...{w=0.8} I used to be...", "open", "base", "worried", "up", hair="sad") # Tonks looks concerned (Blue)
    m "I don't see how that makes any difference..."
    m "Remember why we're doing this, you want Miss Greengrass to be able to curse you properly, correct?"
    call ton_main("Yes...", "soft", "base", "worried", "downR", cheeks="blush")
    m "Until then, I will go ahead with the training... alone."
    m "Any objections?"
    call ton_main("No sir...", "open", "base", "base", "down", hair="neutral", cheeks="blush")
    m "Make sure to obliterate her afterwards."
    call ton_main("Erase her memory?","open","base","base","mid")
    m "That's what I said."
    m "Well then, I believe we're done here..."
    call ton_main("Alright...", "annoyed", "base", "base", "down")
    call ton_main("I'm gonna need some \"me\" time now...", "open", "closed", "base", "ahegao", hair="horny")
    call ton_main("If you know what I mean...", "grin", "narrow", "raised", "down", hair="horny")
    call ton_main("I suppose I should wish you good luck with the training...", "soft", "base", "shocked", "L")
    g9 "Have a good night."
    call ton_main("Oh - I will, [ton_genie_name]!","base","base","raised","R")
    call ton_main("I sure will!", "horny", "base", "raised", "downR")

    call ton_walk(action="leave")

    call bld
    m "..."
    m "Snape..."
    m "That guy deprived me of a blowjob..."
    g4 "He owes me one!"

    call nar(">Astoria has \"mastered\" the imperio curse!")

    $ snape_busy = True
    $ tonks_busy = True
    $ astoria_busy = True

    $ tonks.wear("all") # Wear all stripped clothing

    # Increase affection once (this is the fifth event)
    if ag_st_imperio.counter == 5:
        $ ast_whoring += 1

    jump end_ag_st_imperio

# astoria wand drop animation screen
screen astoria_wand_drop():
    tag wand
    zorder 2

    add "characters/astoria/chibis/wand.webp":
        at transform:
            zoom 0.35
            rotate -25
            xanchor 0
            yoffset -60
            xpos 530-90
            ypos 400

            easeout_cubic 0.5 yoffset 0 rotate 0
            linear 0.15 rotate 5 yoffset -5
            linear 0.15 rotate 10 yoffset 10
            linear 0.15 rotate 15 yoffset 5
            linear 0.15 rotate 25 yoffset 15
