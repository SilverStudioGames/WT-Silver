### Masturbate ###

label hg_pf_strip_fingering_intro:
    if hg_masturbated.trigger == False:
        $ hg_masturbated.triggered() # .trigger = True, .counter += 1
        
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
        m "Do you ever touch yourself?"
        call her_main("What? why?", "upset", "wink", "base", "mid")
        m "Do you?"
        call her_main("[genie_name]!", "scream", "happyCl", "worried", "mid")
        m "It's a simple question [hermione_name]..."
        call her_main("......", "normal", "happyCl", "worried", "mid")
        call her_main("{size=-5}I do...{/size}", "angry", "happyCl", "worried", "mid", emote="05")
        m "Huh? What was that?"
        call her_main("I said that I do alright!!!", "scream", "happyCl", "worried", "mid")
        m "Hmmmm, I'm not sure I believe you..."
        call her_main("What? why would I lie?", "annoyed", "base", "worried", "R")
        m "I'm not sure..."
        m "But don't worry, I'm sure a quick little demonstration will erase any doubts..."
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("well I suppose I could.", "open", "narrow", "worried", "down")
        call her_main("But you better keep your hands to yourself...", "open", "narrow", "worried", "down")
        m "Witcher's promise."
        call her_main("...", "annoyed", "squint", "base", "mid")
    else: # Repeat
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
        m "Are you feeling horny?"
        call her_main("maybe A little, [genie_name].", "base", "narrow", "base", "mid_soft")
        m "Ah, well perhaps we can fix that..."
        call her_main("[genie_name]...", "open", "wink", "worried", "mid")
        g9 "Why don't you play with that slutty little pussy of yours!"
        call her_main("{heart}{heart}{heart}", "base", "narrow", "base", "mid_soft")
        call her_main(".............", "base", "base", "base", "R_soft")
        call her_main("Alright...", "base", "narrow", "worried", "down")
        call her_main("(I can't believe I'm going to do this... again...)", "soft", "narrow", "base", "down")

    return

### Tier 2 ###

label hg_pf_strip_T2_fingering:

    call hg_pf_strip_fingering_intro

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "upset", "base", "base", "mid")
    call her_main("Do you want me to... start?", "soft", "wink", "base", "mid")
    m "Yes, my dear."
    
    if hermione.is_worn("panties"):
        m "But why don't you get rid off your panties first."
        
    call her_main("...........", "disgust", "narrow", "base", "down")
    
    if hermione.is_worn("panties"): # Rest of the clothes is taken off during stripping.
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0
    
    call her_main("(I can't believe I'm going to do this...)", "normal", "happyCl", "worried", "mid")

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
    call her_main("umm... [genie_name]?")
    m "Yes, what is it?"
    call her_main("How long do I have to keep doing this?", "open", "base", "base", "mid")
    m "Until you finish [hermione_name]..."

    if daytime:
        call her_main("But my classes are about to start, [genie_name]...", "soft", "base", "base", "mid")
    else:
        call her_main("But it's getting late, [genie_name]...", "soft", "base", "base", "mid")

    call her_main("I'm not sure if I'll be able to finish... in time.", "disgust", "narrow", "base", "down")
    m "Do you need the points or not?"
    call her_main("I do, [genie_name]! I'm sorry...", "open", "narrow", "worried", "down")
    call her_main("I'll just keep ...going...", "disgust", "narrow", "base", "down")
    play bg_sounds "sounds/slickloop.mp3" fadein 2
    m "(Hmmm, I might have to give her a little encouragement.)"

    menu:
        m "..."
        "\"That's it slut, keep going.\"":
            $ hermione.set_body(armleft="down")
            stop bg_sounds
            call her_main("[genie_name]!!!", "angry", "base", "angry", "mid")
            $ hermione.set_body(armleft="on_pussy")
            play bg_sounds "sounds/slickloop.mp3" fadein 2
            call her_main("How dare you!")
            m "what?"
            call her_main("I hardly think that language is appropriate.", "upset", "wink", "base", "mid")
            m "And masturbating in front of your headmaster is?"
            call her_main("Well... this is different.", "open", "narrow", "worried", "down")
            call her_main("I'm doing this for the honour of gryffindor...")
            call her_main("To help my--... *ah*", "open", "closed", "worried", "down")
            play bg_sounds "sounds/slickloopfast.mp3"
            call nar(">You notice how she's starting to grind her hips a little faster.")
            #
            # TODO: Add wet layer for panties/pussy
            #
            call her_main("ah...{heart}{heart}{heart}", "soft", "narrow", "annoyed", "up")
            call her_main("My classmates win the house cup...", "angry", "wink", "base", "mid")
            m "Are you sure that's the only reason slut?"
            call her_main("I don't know--", "normal", "happyCl", "worried", "mid")
            
            $ hermione.body.body["armright"][1] = 3 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")
            
            call her_main("ah-a{heart}...", "open", "happyCl", "worried", "mid")
            call her_main("I don't know what you mean, [genie_name]...", "angry", "narrow", "base", "down")
            m "It seems to me that you might be enjoying this a little too much..."
            call her_main("I am not, [genie_name]!", "open", "happyCl", "worried", "mid")
            m "Really?"
            call her_main("......................", "normal", "happyCl", "worried", "mid")
            m "Then why is your pussy so wet slut?"
            call ctc

            call her_main("ah...{heart}", "open", "happyCl", "worried", "mid")
            m "ha! just Admit it, you enjoy being called a slut!"
            call her_main("I do not!", "normal", "happyCl", "worried", "mid")
            call her_main("Aha...{heart}", "open", "happyCl", "worried", "mid")
            call her_main("I'm just thinking about how happy everyone will be when we win!", "shock", "happyCl", "worried", "mid")
            m "and what if they find out how you earned the points?"
            stop bg_sounds
            call her_main("what?!", "shock", "wide", "base", "stare")
            m "then it wouldn't just be me degrading you..."
            play bg_sounds "sounds/slickloop.mp3"
            call her_main("...", "soft", "closed", "base", "R")
            m "It would be the whole school."
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("ah...{heart}", "silly", "narrow", "base", "dead")
            m "Little. miss. slut."
            play bg_sounds "sounds/slickloopveryfast.mp3"
            call her_main("ah...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up")
            call her_main("[genie_name], please... don't tell anyone...", "soft", "narrow", "base", "mid_soft")
            call nar(">Hermione keeps on grinding her hips against her hand...")
            call her_main("they can't find out...", "soft", "narrow", "base", "R_soft")
            call her_main("if harry and ron knew...", "open", "narrow", "base", "down")
            call her_main("i'd... ah...{heart}", "soft", "closed", "annoyed", "up")
            m "You'd what [hermione_name]?"
            call her_main("I'd...", "open", "closed", "worried", "mid")
            call her_main("I'd...{heart}", "silly", "closed", "worried", "mid")
            call her_main("I...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up")

        "\"Play with your breasts\"":
            call her_main("my breasts...", "open", "narrow", "worried", "down")
            call her_main("I'm not sure if I should--", "open", "narrow", "base", "down")
            m "There's another ten points for Gryffindor in it for you..."
            $ current_payout += 10
            call her_main("...", "normal", "happy", "base", "R")
            call her_main("......", "soft", "happy", "base", "R")
            
            $ hermione.body.body["armright"][1] = 3 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            call her_main("ah...{heart}", "open", "closed", "base", "R")
            m "There... Isn't that better?"
            call her_main("Ah... W-what...", "open", "wink", "worried", "mid")
            call her_main("......", "normal", "happyCl", "base", "mid")
            m "That's it..."
            call her_main("[genie_name], do you mind if...", "soft", "narrow", "base", "L", cheeks="blush")
            m "What [hermione_name]?"
            call her_main("Could you... Call me names...", "open", "narrow", "base", "R", cheeks="blush")
            m "Such as?"

            call her_main("...{size=-5}Slut...{/size}Only if it's not too much...", "soft", "narrow", "base", "down", cheeks="blush")
            m "That's unbecoming of you to use such language, you little whore..."
            call her_main("Ah...{heart}{heart}", "open", "closed", "annoyed", "mid")
            m "What would your parents think if they saw this?"
            call her_main("i-{heart}", "open", "narrow", "worried", "up", cheeks="blush")
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("Ah...{heart} I don't know...", "soft", "closed", "base", "up", cheeks="blush")
            call her_main("To be perfectly honest [genie_name]... I don't think I care...{heart}{heart}{heart}", "silly", "narrow", "base", "up", cheeks="blush")
            m "Really?"

            call her_main("Really...{heart}", "silly", "narrow", "base", "mid_soft", cheeks="blush")
            m "Would you at least stop?"
            call her_main("Ah...{heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call her_main("Maybe....", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call her_main("I'm not sure...", "open", "narrow", "base", "R", cheeks="blush")

            call her_main("{heart}{heart}{heart}", "grin", "narrow", "base", "up", cheeks="blush")

        "\"Dig deeper!\"":
            m "Good... Just keep playing with that slutty little pussy of yours!"
            call her_main("[genie_name]!", "open", "base", "angry", "mid", cheeks="blush")
            m "What?"
            call her_main("It's not {size=-5}slutty...{/size}", "annoyed", "narrow", "worried", "R", cheeks="blush")
            m "Are you sure? Because from where I'm sitting it looks nice and wet."
            call her_main("Ah...{heart}", "soft", "narrow", "base", "up", cheeks="blush")
            call her_main("It's just sweat, [genie_name]...", "open", "narrow", "base", "R", cheeks="blush")
            m "Whatever you say..."
            call her_main("...............", "soft", "closed", "base", "up", cheeks="blush")
            m "Slut."
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("{heart}{heart}{heart}", "silly", "narrow", "base", "up_soft", cheeks="blush")
            call her_main("Sir... please...", "open", "narrow", "base", "mid_soft", cheeks="blush")
            
            $ hermione.body.body["armright"][1] = 3 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            play bg_sounds "sounds/slickloopveryfast.mp3"
            call nar(">Hermione starts fingering herself faster.")
            m "Very good..."
            call her_main("...{heart}", "silly", "narrow", "base", "up", cheeks="blush")
            call her_main("Ah...{heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            m "That's it slut. Try going a little deeper...."
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
    call her_main("...finish...", "angry", "happyCl", "base", "down", cheeks="blush", tears="soft")

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
            $ hermione.body.body["armright"][1] = 0 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armleft="down", armright="down")
            $ hermione.set_pose(None)
            
            stop bg_sounds
            call her_main("*SOB!* i can't...", "angry", "happyCl", "base", "down", cheeks="blush", tears="messy")
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
            $ hermione.body.body["armright"][1] = 0 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armleft="down", armright="down")
            $ hermione.set_pose(None)
            
            call her_main("Thank you [genie_name].", "base", "base", "worried", "mid", cheeks="blush", tears="soft")
            call her_main("I promise to try harder next time.", "base", "happyCl", "worried", "mid", cheeks="blush")
            
    $ hermione.wear("all")
    jump end_hg_pf_strip

### Tier 3 ###

label hg_pf_strip_T3_fingering:

    call hg_pf_strip_fingering_intro
    
    if hermione.is_worn("panties"):
        call nar("Hermione bends over and takes off her panties.")
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0

    $ hermione.set_pose("masturbate")
    $ hermione.body.body["armright"][1] = 3 # Hacky hacky, sucky sucky, CG better.
    $ hermione.set_body(armleft="on_pussy", armright="on_tits")
    play bg_sounds "sounds/slickloop.mp3" fadein 2
    call her_main("........", "soft", "narrow", "annoyed", "up")

    call ctc

    call play_music("playful_tension") # SEX THEME.
    g9 "Nice..."
    call her_main("........", "grin", "narrow", "annoyed", "up")

    call her_main("A-ha... {heart}ah...", "open", "happyCl", "worried", "mid")
    call her_main("Ah... {heart}-aha...", "open", "happyCl", "worried", "mid")
    m "..."
    call her_main("Ah-ah...", "open", "happyCl", "worried", "mid")
    m "......................"
    call her_main("Ah... ah...{heart}", "open", "happyCl", "worried", "mid")
    call her_main("Ah... [genie_name]?", "soft", "happy", "base", "R")
    m "What is it?"
    call her_main("Ah... Do you.... like this?", "open", "happyCl", "worried", "mid")
    m "Do I like watching \"you\" finger your slutty little pussy?"
    m "Very much so, [hermione_name]. Why?"
    call her_main("{heart}{heart}{heart}", "normal", "happyCl", "worried", "mid")
    call her_main("Ah... You're just so quiet...", "open", "happyCl", "worried", "mid")
    m "Do you need a little more encouragement?"
    call her_main("Ah... yes... please....{heart}", "open", "happyCl", "worried", "mid")
    m "Tch... You nasty whore!"
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("yes [genie_name], ah...{heart}", "grin", "narrow", "base", "up", cheeks="blush")
    call her_main("please... ah... more...{heart}", "grin", "base", "angry", "mid", cheeks="blush")
    g4 "You need to be punished for being such a slut!"
    call her_main("yes, [genie_name]... punish me...", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("make me your little slut....", "open", "narrow", "base", "up", cheeks="blush")
    play bg_sounds "sounds/slickloopveryfast.mp3"
    call her_main("I will... ah... {heart}do anything... ah...{heart}", "silly", "narrow", "base", "dead")
    m "Anything [hermione_name]?"
    call her_main("Ah-a...{heart} yessss...", "silly", "narrow", "base", "up", cheeks="blush")
    m "Cum."
    #
    # TODO: CUM LAYERS
    #
    call her_main("{heart}{heart}{heart}!!!{heart}{heart}{heart}", "silly", "narrow", "base", "dead", cheeks="blush")
    call cum_block
    
    call her_main("Ah...{heart}...{heart}", "grin", "narrow", "annoyed", "up")
    call her_main("Ah... ah...{heart}", "silly", "narrow", "annoyed", "up")
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("...{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up")
    call her_main("*heavy panting*", "open_wide_tongue", "narrow", "annoyed", "up")
    play bg_sounds "sounds/slickloop.mp3"
    call her_main("[genie_name]...{heart}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_main(".............", "soft", "narrow", "annoyed", "up")
    stop bg_sounds
    call nar(">Hermione takes a minute to collect herself.")
    
    # Reset pose
    $ hermione.body.body["armright"][1] = 0 # Hacky hacky, sucky sucky, CG better.
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)
    
    $ hermione.wear("all")
    
    jump end_hg_pf_strip

### Tier 4 ###

label hg_pf_strip_T4_fingering:

    $ hg_masturbated.triggered()
    
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind pleasuring yourself in front of me, do you?"
    if her_whoring <= 16:
        call her_main("As long as I am being paid...", "grin", "base", "base", "R")
        m "That's the spirit!"
    else:
        call her_main("I mean I have done it once today already...", "grin", "base", "base", "R")
        m "Once more for good luck then!"
        call her_main("If you insist...{heart}", "open", "base", "base", "R", cheeks="blush")

    call her_main("...", "base", "narrow", "base", "mid_soft")
    if hermione.is_worn("panties"):
        call nar("She hastily takes off her panties.")
        pause 1.0
        $ hermione.strip("panties")
        pause 1.0
        
    $ hermione.set_pose("masturbate")
    $ hermione.body.body["armright"][1] = 3 # Hacky hacky, sucky sucky, CG better.
    $ hermione.set_body(armleft="on_pussy", armright="on_tits")
    play bg_sounds "sounds/slickloop.mp3" fadein 2
    
    call ctc

    stop music fadeout 3.0
    call her_main("Do you like it when I do it like this, [genie_name]?", "grin", "base", "base", "R")
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    m "Yes, I love it..."
    m "Try going a little deeper with your fingers."
    call her_main("Alright [genie_name]...", "base", "happyCl", "base", "mid")
    play bg_sounds "sounds/slickloopfast.mp3"
    call her_main("Ah... ah...{heart}", "open", "happyCl", "worried", "mid")
    call her_main("Ah... [genie_name]...{heart}", "open", "happyCl", "worried", "mid")

    menu:
        m "..."
        "\"What are you thinking about?\"":
            call her_main("Huh?", "open", "wink", "worried", "mid", cheeks="blush")
            call her_main("Oh, um... nothing...", "soft", "happyCl", "worried", "mid", cheeks="blush")
            m "[hermione_name]..."
            call her_main("[genie_name], please, it's too embarrassing...", "disgust", "narrow", "base", "down", cheeks="blush")
            g4 "Well now I have to hear it."
            call her_main("OK... but you have to promise not to tell anyone!", "open", "base", "base", "R", cheeks="blush")
            m "Witcher's honour."
            call her_main("......", "annoyed", "narrow", "annoyed", "mid", cheeks="blush")
            m "[hermione_name]..."
            call her_main("Alright. If you must know... I'm remembering the time I corrected professor Snape about the ingredients of a Hiccoughing potion.", "open", "narrow", "worried", "down", cheeks="blush")
            m "....."
            call her_main("ah...{heart}", "soft", "narrow", "annoyed", "up", cheeks="blush")
            call her_main("It was ah... {heart} in front of the entire class as well.")
            call her_main("He refused to let me answer any questions for a week after that.", "base", "narrow", "worried", "down", cheeks="blush")
            call her_main("But it was worth it...", "soft", "happy", "base", "R", cheeks="blush")
            call her_main("The look on his face when he realised he was wrong...{heart}", "soft", "narrow", "annoyed", "up", cheeks="blush")
            call her_main("a-ah...{heart}", cheeks="blush")
            call her_main("It just felt so good!{heart}", "grin", "narrow", "base", "dead", cheeks="blush")
            m "OK, I think that's enough..."
            call her_main("Was it too much?", "angry", "wink", "base", "mid")
            m "Let's just get back to business shall we?"
            call her_main(".................", "soft", "narrow", "annoyed", "up")
            call nar(">Hermione keeps on plunging her fingers into herself.","start")
            call nar(">She is doing a great job of it too.","end")
            m "Yes, yes... just like that."

        "\"You really are a shameless slut, aren't you?\"":
            call her_main("Yes...", "soft", "narrow", "annoyed", "up")
            call her_main("ah... {heart}", "silly", "narrow", "base", "dead")
            call her_main("I don't know if it's the time I'm spending with you...{heart}", "angry", "wink", "base", "mid")
            call her_main("Or if i've always been this way...{heart}", "angry", "narrow", "base", "down")
            call her_main("But... {heart} ah... {heart} I'm a slut [genie_name]...{heart}", "soft", "narrow", "annoyed", "up")
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("A shameless slut...", "grin", "narrow", "base", "dead")
            call her_main("That pleasures herself...{heart} ah...", "soft", "narrow", "annoyed", "up")
            call her_main("Just to make her headmaster happy...", "grin", "narrow", "base", "dead")
            m "Oh, yes..."
            call her_main("That's it [genie_name]...", "base", "narrow", "worried", "up_soft")
            call her_main("Enjoy yourself while I stand here...", "silly", "narrow", "base", "dead")
            call her_main("Ah...{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("Fingering my pussy...", "silly", "narrow", "annoyed", "up")
            call her_main("Ah... ah...{heart}", "grin", "narrow", "annoyed", "up")
            call her_main("Ah... Do you.... like this [genie_name]?", "shock", "happyCl", "worried", "mid")
            call her_main("Watching me Ah...{heart} degrade myself?", "silly", "narrow", "base", "dead")
            m "Very much, [hermione_name]. Just keep going..."
            call her_main("{heart}{heart}{heart}", "silly", "narrow", "base", "dead")

        "\"Play with your tits some more!\"":
            call her_main("Hm?", "soft", "narrow", "annoyed", "up")
            call her_main("alright... if you insist...", "open", "base", "base", "R", cheeks="blush")
            call her_main("ah...{heart}", "angry", "wink", "base", "mid")
            m "Now pinch your nipples."
            call her_main("[genie_name]...", "open", "happy", "base", "mid", cheeks="blush")
            m "do it, [hermione_name]."
            call her_main("...", "open", "base", "base", "R", cheeks="blush")
            call her_main("Mmmm...", "grin", "narrow", "base", "up", cheeks="blush")
            m "That's it..."
            call nar(">You stare at Hermione's breasts with hunger...")
            call her_main("ah...", "silly", "narrow", "base", "dead")
            m "So do you like playing with those tits of yours, [hermione_name]?"
            call her_main("I do, [genie_name]... ah...{heart}", "soft", "narrow", "annoyed", "up")
            call her_main("I don't know why...", "base", "base", "base", "R", cheeks="blush")
            call her_main("But I love it...{heart}{heart}", "base", "narrow", "worried", "down")
            m "You nasty slut!"
            call her_main("Ah...{heart} ah-a...{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("I am...")
            call her_main("A nasty slut... Ah...{heart}", "silly", "narrow", "base", "dead")
            m "You are a disgrace, [hermione_name]!"
            call her_main("Ah-ah...{heart}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")

    m "Why don't you come down and I'll help you finish?"
    call her_main("...", "base", "narrow", "worried", "down")

    # Hermione climbs off your desk.
    show screen blkfade
    with d5
    hide screen hermione_main
    call play_sound("climb_desk")
    ">Hermione slowly climbs down from the desk and stands in front of you."
    pause.5

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
            call nar(">You reach forward and grab a hold of her supple breasts.")
            call her_chibi_scene("grope_tits")
            
            $ hermione.body.body["armright"][1] = 0 # Hacky hacky, sucky sucky, CG better.
            $ hermione.set_body(armright="down")

            call her_main("[genie_name]!", "shock", "happyCl", "worried", "mid")
            call her_main("This wasn't part of the deal!", "open", "happyCl", "worried", "mid")
            call her_main("I don't think we should...", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "Don't worry [hermione_name], You can keep playing with yourself."
            m "This is just to hurry things along."
            call her_main("Ah...{heart} Well, as long as it's just to make this end faster...", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I suppose I can... ah{heart} allow it...", "base", "base", "base", "R", cheeks="blush")
            call nar(">You give her tits a couple of firm squeezes...")
            m "Just admit that you love it."
            call her_main("Ah... fine...{heart}", "open", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}I like it...{/size}", "soft", "narrow", "annoyed", "up")
            m "What was that [hermione_name]?"
            call her_main(".......")
            call her_main("I love this...", "grin", "narrow", "base", "dead")
            call her_main("Standing here... playing with myself...", "base", "narrow", "worried", "down")
            call her_main("Ah... while you play with me...{heart}", "grin", "narrow", "base", "up", cheeks="blush")
            m "Heh... Nice."
            call her_main("Ah...{heart}", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I sometimes wish I could spend all day in here...", "grin", "base", "angry", "mid", cheeks="blush")
            m "Perhaps we could arrange that some time..."
            call nar(">You keep on massaging the girl's breasts...")
            call her_main(".......")
            call her_main("[genie_name]... I know it's greedy of me...", "soft", "base", "base", "R", cheeks="blush")
            call her_main("ah...{heart}", "base", "narrow", "worried", "down")
            call her_main("but could you touch me... down there...", "open", "happy", "base", "mid", cheeks="blush")
            m "What was that [hermione_name]? You'll have to speak up."
            call her_main("Please finger me...", "open", "narrow", "base", "up", cheeks="blush")
            m "Once more time, a little louder this time."
            call her_main("Ah...{heart} {size=+5}please finger my cunt!{/size}", "grin", "narrow", "base", "up", cheeks="blush")
            call her_chibi_scene("grope_ass_front")
            with vpunch
            call nar(">You swiftly plunge two fingers into her dripping pussy.")
            
            $ hermione.set_body(armleft="down")
            
            call her_main("{heart}{heart}{size=+5}!!!{/size}{heart}{heart}", "silly", "narrow", "annoyed", "up")

        "-Finger her-":
            call her_chibi_scene("grope_ass_front")
            call nar(">You run your hands up and down Hermione's legs...")
            call her_main("!!!", "open", "happyCl", "worried", "mid")
            call nar(">And slowly move your hands towards her pussy...")
            call her_main(".................", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]..."
            call her_main("{size=-7}[genie_name]...{/size}", "soft", "narrow", "annoyed", "up")
            m "Shhh. Just play with your tits."
            call her_main("...fine, [genie_name]...", "base", "narrow", "base", "up", cheeks="blush")
            m "Good girl."
            call her_main("....................", "base", "closed", "base", "mid")
            m "Just be quiet..."
            call nar(">you enjoy the sensation of gently stroking the inside of her thighs...")
            m "as my hands explore you"
            m "your thighs..."
            call nar(">your start kneading the flesh of her thighs, moving ever closer to her dripping cunt")
            m "your big, firm ass"
            call nar(">You move around and squeeze her ass gently...")
            call her_main(".....................", "grin", "narrow", "annoyed", "up")
            m "your loins..."
            call nar(">You move one hand back around, and start circling just above her clit.")
            call her_main(".....................{size=-8}[genie_name]...{/size}", "silly", "narrow", "base", "dead")
            m "What was that, [hermione_name]?"
            call her_main(".....................", "annoyed", "wink", "base", "mid", cheeks="blush")
            call her_main("...i... {size=-5}...i need you... inside of me...{/size}", "disgust", "narrow", "base", "down", cheeks="blush")
            m "You'll have to speak up if you expect me to hear you..."
            call her_main("I... ah...{heart} need...", "open", "narrow", "base", "up", cheeks="blush")
            call nar(">You swiftly plunge two fingers into her drenched snatch.")
            call her_main("!!!{heart}{heart}", "grin", "narrow", "annoyed", "up")
            call nar(">you start to pump your fingers inside her before she can do more than gasp")
            call her_main("{size=+10}{heart}{heart}!!!{heart}{heart}{/size}", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]. Just enjoy yourself."
            call her_main("..................................................", "base", "narrow", "base", "up", cheeks="blush")
            m "do you like this?"
            m "you like it when i finger your cunt?"
            call her_main("i love it!{heart} i love your fingers in my tight, wet pussy!!{heart}", "silly", "narrow", "annoyed", "up")
            m "well, i think we can do better."
            call nar(">with your other hand, you start rubbing the base of your palm against her clit.")
            call her_main("{size=+10}!!!{/size}", "open", "narrow", "base", "up", cheeks="blush")

    play bg_sounds "sounds/slickloopveryfast.mp3"
    call nar(">you don't even need to move as she pounds herself against your fingers.")
    call her_main("ah...{heart} please...{heart} keep...{heart}", "silly", "narrow", "base", "dead","blush")
    call her_main("fingering my cunt!{heart}{heart}", "silly", "narrow", "annoyed", "up","blush")
    g9 "As you command!"
    call nar(">you force another finger into her pussy!")
    call her_main("ah yes... {heart}iloveitiloveitiloveit", "grin", "narrow", "annoyed", "up","blush")
    m "what do you love, [hermione_name]?"
    call her_main("ah!!{heart} I love your fingers in my pussy [genie_name]!{heart}", "open_wide_tongue", "narrow", "annoyed", "up","blush")
    call nar(">her movements are becoming more frantic")
    m "are you cumming, [hermione_name]?"
    call her_main("ah...{heart} yes!!", "grin", "narrow", "annoyed", "up")
    call her_main("I'm cumming [genie_name]!!{heart}", "grin", "narrow", "base", "dead")
    call her_main("I'm cumming from being fucked with your fingers!!{heart}{heart}", "grin", "narrow", "base", "up", cheeks="blush")
    m "show me your tits [hermione_name]!"
    m "I want to see you cum while you play with them."
    
    $ hermione.body.body["armright"][1] = 3
    $ hermione.set_body(armright="on_tits")
    
    call her_main("{heart}{heart}{heart}!!!{heart}{heart}{heart}", "silly", "narrow", "base", "dead", cheeks="blush")
    call cum_block
    #
    # TODO: CUM LAYERS
    #
    call her_main("Ah...{heart}...{heart}", "grin", "narrow", "annoyed", "up")
    call her_main("Ah... ah...{heart}", "silly", "narrow", "annoyed", "up")
    call her_main("...........", "silly", "narrow", "annoyed", "up")
    call her_main("........................", "silly", "narrow", "annoyed", "up")
    stop bg_sounds

    call nar(">You release her...")
    call her_chibi_scene("behind_desk_show_tits")
    show screen bld1
    with d3
    m "This will do for now [hermione_name]."
    
    # Reset pose
    $ hermione.body.body["armright"][1] = 0 # Hacky hacky, sucky sucky, CG better.
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)
    
    call her_main("[genie_name]{heart}", "silly", "narrow", "base", "mid_soft", cheeks="blush")
    
    $ hermione.wear("all")

    jump end_hg_pf_strip