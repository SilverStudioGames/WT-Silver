

### Hermione Blowjob ###

label hg_pf_blowjob:

    if hg_pf_blowjob.counter == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"

    if hg_pf_blowjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 55
    $ mouth_full_of_cum = False
    $ hg_pf_blowjob.start()


    # End Event
    label end_hg_pf_blowjob:

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
        if mouth_full_of_cum:
            call her_main("", "full_cum", "base", "angry", "mid", cheeks="blush", tears="mascara", xpos="mid", ypos="base", trans=fade)
        else:
            call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        if mouth_full_of_cum:
            call her_main("", "full_cum", "base", "base", "mid", cheeks="blush", tears="mascara", xpos="mid", ypos="base", trans=fade)
        else:
            call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if her_tier < 6:
        m "Yes, [hermione_name]. {number=current_payout} points to Gryffindor."
        $ gryffindor += current_payout
    else:
        m "You can go now, [hermione_name]."

    if mouth_full_of_cum:
        call her_main("...", "full_cum", "narrow", "annoyed", "up", cheeks="blush", tears="mascara")
    else:
        call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")

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

    $ hg_blowjob.trigger = True

    jump end_hermione_event

### Fail Events ###

label hg_pf_blowjob_fail:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I plan to grant Gryffindor {number=current_payout} house points today..."
    m "If you suck me off..."

    $ hg_pf_blowjob.fail_intentional()

    jump too_much

### Tier 4 - Fails ###

# Event 1 (i) - Hermione refuses.
# Event 2 (r) - Repeat.

label hg_pf_blowjob_T4_fail_intro:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I plan to grant Gryffindor {number=current_payout} house points today..."
    m "If you suck me off..."
    call her_main("Suck you...{w=0.3} off?", "disgust", "wide", "base", "mid")
    call her_main("With my mouth?!", "disgust", "wide", "base", "stare")

    if hg_kiss.trigger:
        g9 "Wouldn't even be the first time you've done it!"
        call her_main("Yes, but...", "disgust", "narrow", "worried", "down")
        call her_main("That was something different entirely...", "disgust", "happyCl", "worried", "mid")
        m "How so?"
        call her_main("All I wanted was to get done with that favour early, so I...", "open", "narrow", "base", "down")
        call her_main("I helped...", "disgust", "base", "worried", "R")
        g9 "By sucking on my cock! Indeed you did!"
        call her_main("No! I was merely stroking it... and...", "silly", "happyCl", "worried", "mid")
        call her_main("I gave it a short kiss, but...", "disgust", "narrow", "worried", "down", cheeks="blush")
        call her_main("I'm sorry [genie_name], but I don't think I can do \"that!\"", "open", "base", "worried", "R", cheeks="blush")
    else:
        m "Preferably..."
        g9 "But I'm always open to try out new things!"
        call her_main("Are you out of your mind?!", "scream", "closed", "angry", "mid")

    call her_main("I should leave...", "disgust", "narrow", "base", "down", cheeks="blush")

    call her_walk(action="leave")

    call bld
    m "Tough luck..."

    $ her_mood += 6
    $ hg_pf_blowjob.fail()

    jump end_hermione_event

label hg_pf_blowjob_T4_fail_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I plan to grant Gryffindor {number=current_payout} house points today..."
    call her_main("And let me guess...", "open", "closed", "angry", "mid")
    call her_main("You'd like me to \"suck you off\" for it?", "open", "base", "angry", "mid")
    g9 "That is correct!"
    call her_main("I refuse...", "open", "closed", "base", "mid")
    m "It's only a blowjob, girl..."

    if hg_kiss.trigger:
        m "It's not like you haven't done it before..."
        call her_main("Are you talking about the kiss I gave it?", "open", "base", "angry", "mid")
        call her_main("That was something different entirely...", "open", "closed", "base", "mid")
        m "How so?"
        call her_main("I wanted to get done with that favour early, so I helped a bit.", "open", "narrow", "angry", "R")
        g9 "By sucking on my cock! Indeed you did!"
        call her_main("It was nothing more than a short kiss...", "annoyed", "base", "angry", "mid")
        m "Still counts as a blowjob..."

    call her_main("[genie_name], I've told you this last time...", "open", "closed", "base", "mid")
    call her_main("I refuse to do this sort of thing...", "normal", "base", "angry", "mid")
    call her_main("I have to go now...", "annoyed", "narrow", "angry", "R")

    call her_walk(action="leave")

    $ her_mood += 6
    $ hg_pf_blowjob.fail()

    jump end_hermione_event

### Tier 5 ###

# Event 1 (i) - Hermione is ok with it.
# Event 2 (i) - Hidden blowjob with Snape watching.
# Event 3 (r) - Normal blowjob with choices.

label hg_pf_blowjob_T5_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I plan to grant Gryffindor {number=current_payout} house points today..."
    m "If you suck me off..."
    call her_main("Oh...", "open", "narrow", "worried", "down")
    call her_main("Alright.", "base", "narrow", "worried", "down")
    m "Really? Just like that?"
    call her_main("Yes. I know I'm supposed to feel outraged...", "angry", "narrow", "base", "down")
    call her_main("But somehow I do not...", "angry", "base", "base", "mid")
    call her_main("I suppose I am just glad that I can help out my house...", "base", "narrow", "worried", "down")
    call her_main("And if to do that I must put your penis in my mouth, then so be it...", "upset", "closed", "base", "mid")
    m "Well, alright then."
    call her_main("Although, now when I say it out loud like this...", "angry", "narrow", "base", "down")
    m "Too late! You already said \"yes\"!"
    call her_main("I know...", "grin", "happyCl", "worried", "mid", emote="sweat")
    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_1


label hg_pf_blowjob_T5_intro_E2:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "How about another blowjob?"

    call play_music("playful_tension") # SEX THEME.
    call her_main("[genie_name], how dare you propose such a thing to one of your pupils!", "scream", "base", "angry", "mid", emote="angry")
    m "Wha--...?"
    call her_main("This is unbecoming of a man of your standing.", "scream", "base", "angry", "mid", emote="angry")
    call her_main("You should be ashamed of yourself [genie_name]!", "angry", "base", "angry", "mid")
    menu:
        m "???"
        "\"Fine. No points to you then! Leave!\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("[genie_name], calm down, please.", "grin", "happyCl", "worried", "mid", emote="sweat")
            m "You are dismissed, [hermione_name]."
            call her_main("[genie_name], please, I didn't mean any of the things I said.", "grin", "happyCl", "worried", "mid", emote="sweat")
            m "What?"

        "\"*Ehm*... I am sorry?\"":
            stop music fadeout 1.0
            call her_main("*Giggle*", "base", "base", "base", "mid")
            m "*huh*?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("I got you... [genie_name].", "grin", "happyCl", "worried", "mid", emote="sweat")
            m "What?"

        "-Two can play that game...-":
            stop music fadeout 1.0
            m "Oh nooooo... what am I ever going to do now."
            call her_main("........?", "soft", "base", "base", "mid")
            m "A student caught me in the act and will report me to the ministry of magic."
            m "I guess I'll have to sign a resignation and step down being a headmaster."
            call her_main("[genie_name]?!", "open", "wide", "worried", "mid")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            g9 "*he-he* If you could only see your face."
            call her_main("what..", "soft", "wide", "worried", "mid")
            m "I got you."
            call her_main("........", "annoyed", "base", "angry", "R")
            call her_main("*sigh*", "soft", "closed", "base", "mid")

    call her_main("Well, so much has happened lately...", "base", "base", "base", "mid")
    her "I had so many new experiences that kind of changed the way I look at things..."
    her "So I was just trying to imagine how the \"old me\" would've reacted to this."
    m "So..."
    g4 "You were messing with me then?"
    call her_main("*Ehm*... I'm sorry [genie_name], I didn't mean to...", "angry", "happyCl", "worried", "mid", emote="sweat")
    g4 "You nasty little slut! You must be punished!"
    g9 "I'll punish you with my cock!"
    call her_main("...............................", "angry", "happyCl", "worried", "mid", emote="sweat")

    jump hg_pf_hidden_blowjob # Snape

label hg_pf_blowjob_T5_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call play_music("playful_tension") # SEX THEME.
    m "How would you like to give me another blowjob, [hermione_name]?"
    call her_main("I suppose I can do that...", "base", "narrow", "worried", "down")
    g9 "Come here then!"

    jump hg_pf_blowjob_1

### Tier 6 ###

# Event 1 (i) - New event with a couple of choices.
# Event 2 (r) - Hidden blowjob (Snape, Tonks, or Luna.)
# Event 3 (r) - Blowjob with choices.

label hg_pf_blowjob_T6_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Tell me, [hermione_name]..."
    g9 "Have you been behaving yourself lately?"
    call her_main("Me? Of course, [genie_name].", "open", "base", "base", "mid")
    call her_main("I'm always trying to behave my best at school--", "open", "base", "base", "R")

    call her_main("Oh...{w} I mean... No, Sir!", "soft", "narrow", "annoyed", "up")
    call play_music("playful_tension") # SEX THEME.
    call her_main("I've been a very, very bad girl, [genie_name]!", "soft", "narrow", "base", "mid_soft")
    g9 "..............."
    m "Tell me, what wrongs did you do, [hermione_name]?"
    call her_main("*Ehm*...", "disgust", "narrow", "worried", "down")
    call her_main("I sucked off my headmaster's cock...", "soft", "narrow", "worried", "down")
    g9 "Yes you did!"
    call her_main("And not just to earn those points...", "disgust", "happyCl", "worried", "mid")
    m "What? Why else?"
    call her_main("I did it because I like doing it...", "disgust", "narrow", "base", "R_soft")
    call her_main("I like sucking cock, [genie_name]!", "soft", "narrow", "base", "mid_soft", cheeks="blush")
    g4 "Yes! You dirty slut!"
    g4 "Girls like you need to be punished!"
    g9 "Don't you think so too, Miss Granger?"
    call her_main("...............................", "clench", "narrow", "base", "down", cheeks="blush")
    call her_main("Yes, [genie_name]...", "soft", "narrow", "base", "mid_soft", cheeks="blush")
    call her_main("I need to be punished!", "base", "narrow", "base", "mid_soft")
    g4 "Beg me for it, you slut!"
    call her_main("Please punish me with your cock, [genie_name]!", "soft", "narrow", "base", "mid_soft")
    call her_main("I beg you!", "soft", "narrow", "base", "mid_soft")
    g4 "Come here, you dirty little minx!"
    call her_main("{heart}{heart}{heart}", "base", "narrow", "annoyed", "up")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_2

label hg_pf_blowjob_T6_hidden_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call play_music("playful_tension") # SEX THEME.
    m "Suck my dick, [hermione_name]."
    call her_main("Anything for you, [genie_name]...", "base", "narrow", "base", "mid_soft")

    jump hg_pf_hidden_blowjob

label hg_pf_blowjob_T6_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call play_music("playful_tension") # SEX THEME.
    m "Suck my dick, [hermione_name]."
    call her_main("Anything for you, [genie_name]...", "base", "narrow", "base", "mid_soft")

    jump hg_pf_blowjob_2

### First Blowjob ###

label hg_pf_blowjob_1:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj_pause", trans=d9)
    pause.8

    call play_music("playful_tension") # SEX THEME.
    call her_chibi_scene("bj", trans=d9)
    call ctc

    call her_main("*Slurp*! *Gulp*! *Slurp*!","open_wide_tongue", xpos="base", ypos="head")
    m "Yes..."
    m "Try to take it deeper now..."
    call her_main("*Gulp*! *Gobble*! *Gobble*!")
    m "Yes, like that. Good."
    call her_main("*Slurp*! *Gltch*! *Gulp*!")
    m "Yes, that's a good girl."

    menu:
        m "*Hmm*..."
        "\"Whatever happened to your \"MRM\" thing?\"":
            call her_main("*Slurp*?")

            call her_chibi_scene("bj_pause")
            call her_main("Oh, well...", "angry", "narrow", "base", "down")
            call her_main("We are still active, but...")

            call her_chibi_scene("bj")
            call her_main("*Slurp*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("But we are not getting as popular and as much support as I thought we would...", "angry", "wink", "base", "mid")

            call her_chibi_scene("bj")
            call her_main("*Slurp*! *Gulp*! *Gulp*!", "open_wide_tongue", "narrow", "worried", "down")
            m "Oh... This is good..."
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            m "*Hmm*..."
            m "So you don't mind selling me sexual favours, letting me play with your tits and such..."
            call her_main("*Gobble*! *Gltch*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "And then condemn such behaviour in front of the other students."
            call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "narrow", "worried", "down")
            m "You perverted, little hypocrite."
            call her_main("*Gulp*--", "open_wide_tongue", "narrow", "base", "up")

            call her_chibi_scene("bj_pause")
            call her_main("That's not what we stand for, [genie_name].", "angry", "base", "base", "mid")
            m "What do you mean?"
            call her_main("The \"MRM\" is about gender equality.", "open", "closed", "base", "mid")
            call her_main("We are not as much against selling sexual favours to the teachers...")
            call her_main("As we are against the gender inequality that the selling of sexual favour creates...")
            m "*Hmm*..."
            m "This conversation is starting to bore me..."
            m "Suck on my cock some more before we continue."
            call her_main("Of course, [genie_name].", "soft", "narrow", "annoyed", "up")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Gobble*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            m "Yes, much better..."
            m "But you still disapprove of selling the favours, right?"
            call her_main("*Slurp*--", "open_wide_tongue", "narrow", "base", "up")

            call her_chibi_scene("bj_pause")
            call her_main("Yes, it is frowned upon...", "upset", "closed", "base", "mid")
            m "And yet, you are the biggest offender by far."
            call her_main("But what choice do I have?", "upset", "closed", "base", "mid")
            call her_main("I've been put in a very difficult position...")
            m "The cock, [hermione_name]."
            call her_main("Right, sorry...", "upset", "closed", "base", "mid")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Slurp*! *Gulp*! *Gltch*!", "open_wide_tongue", "narrow", "base", "up")
            call her_main("*Slurp*--", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("This one time we had a meeting right after I sold you another favour, [genie_name].", "angry", "base", "base", "mid")
            call her_main("I had to give a speech with my clothes all messy and stained.")
            call her_main("It felt awful that I had to do that...")
            m "You did enjoy it a little bit though..."
            call her_main("Well...", "angry", "narrow", "base", "down")
            m "Just admit it."
            call her_main("...............", "angry", "base", "base", "mid")
            m "Yes, I knew it. You took pleasure in it, you little perv."
            call her_main("I suppose it was embarrassing and exciting at the same time...", "angry", "narrow", "base", "down")
            call her_main("And it made me feel even worse about myself.")
            m "You poor thing."
            m "Cock back in the mouth."
            call her_main("Yes, [genie_name].", "angry", "base", "base", "mid")
            call her_chibi_scene("bj", trans=d3)
            pause.8

        "\"Your parents must be proud of you...\"":
            call her_main("*Slurp*--")

            call her_chibi_scene("bj_pause")
            call her_main("Yes, I believe they are...", "smile", "happyCl", "base", "mid")
            call her_main("With me being an excellent student despite being muggle-born and all...", "base", "happyCl", "base", "mid")
            call her_main("Although at first they were against sending me to some \"Bogus boarding school\".", "angry", "base", "base", "mid")
            call her_main("Took some effort to convince them that \"Hogwarts\" is a respectable institution.", "base", "happyCl", "base", "mid")
            m "Yes, a respectable institution indeed."
            m "Cock back in your mouth, [hermione_name]."

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Slurp*! *Gulp*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            m "Yes, just keep at it for a while..."
            call her_main("*Slurp*! *Gltch*! *Gulp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Good, good..."
            m "So, what would your folks say if they were to see you now, [hermione_name]?"
            call her_main("*Slurp*--", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("They would not understand of course...", "open", "narrow", "worried", "down")
            call her_main("But I do not care.")
            call her_main("I am not afraid to \"get my hands dirty\" and do what needs to be done.", "upset", "closed", "base", "mid")
            m "A bit rebellious, aren't you?"
            call her_main("*Hmm*... I suppose I am.", "angry", "wink", "base", "mid")
            m "Back to sucking then. Teach your folks a lesson."

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")

        "\"Tell me about the Gryffindor house.\"":
            call her_main("*Slurp*--")

            call her_chibi_scene("bj_pause")
            call her_main("What can I say that you don't already know, [genie_name]?", "soft", "base", "base", "R")
            m "Yes... *Ehm*... I know everything of course."
            m "But I want to see how much you know."
            m "To test your knowledge on the subject."
            call nar(">As soon as you mention \"test\" Hermione's eyes light up with excitement.")
            call her_main("OK. But I need a moment to gather my thoughts...", "smile", "happyCl", "base", "mid", emote="happy")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "narrow", "base", "up")
            m "Oh, yes... Take as much time as you need, [hermione_name]."
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            call her_main("*Gulp*--", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("The Gryffindor house was founded by Godric Gryffindor, thus the name.", "open", "narrow", "worried", "down")
            call her_main("The heraldic animal of Gryffindor is the lion...")
            call her_main("And its colours are red and gold.", "open", "closed", "base", "mid")

            call her_chibi_scene("bj")
            call her_main("*Gulp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("Professor Minerva McGonagall is the head of our house.", "open", "closed", "base", "mid")
            call her_main("The Gryffindor house emphasises the traits of courage...")
            call her_main("As well as \"daring, nerve and chivalry\"...")
            call her_main("And thus its members are generally regarded as brave but reckless...")

            call her_chibi_scene("bj")
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            call her_main("Gryffindor corresponds roughly to the element of fire...", "open", "closed", "base", "mid")
            call her_main("And for that reason the colours of red and gold were chosen.")

            call her_chibi_scene("bj")
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            m "*Hmm*..."
            m "Well, I thought I could turn this around somehow to make fun of you..."
            call her_main("*Slurp* ...?", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Well, with your house representing courage and righteousness and such..."
            m "And you being a nasty slut..."

            call her_chibi_scene("bj_pause")
            call her_main("[genie_name]!", "scream", "base", "angry", "mid", emote="angry")
            m "But to be honest..."
            m "\"Daring, nerve, fire, recklessness\"..."
            m "That sort of describes your personality quite well..."
            call her_main("[genie_name]...", "base", "base", "base", "mid")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            call her_main("*Gobble*!! *Gltch*!! *Gobble*!!!", "open_wide_tongue", "narrow", "base", "up")
            g4 "*Argh* {w=0.5}Good...{w=0.5} girl..."

    call bld
    m "Keep going..."
    call her_main("*Gobble*! *Slurp*! *Slurp*!")
    m "Good... Back and forth, back and forth... slut."
    call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_main("*Slurp*--", "open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause")
    call her_main("[genie_name]... I am a... whore.", "open", "narrow", "worried", "down")
    m "What?"

    call her_chibi_scene("bj")
    call her_main("*Slurp-Slurp-Slurp*!", "open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause")
    call her_main("I truly am a slut and deeply enjoy sucking your cock.", "angry", "base", "base", "mid")
    m "Oh, yes, yes... Say more things like that."

    call her_chibi_scene("bj", trans=d3)
    pause.8
    call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause")
    call her_main("Please, [genie_name]. Cum for me.", "soft", "narrow", "annoyed", "up")
    with hpunch
    g4 "*Argh*! You little...!!!"
    g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"

    menu:
        m "..."
        "-Warn her-":
            call her_main("Yes, I love to suck and--", "soft", "narrow", "annoyed", "up")
            g4 "Heads up, [hermione_name]! Here it comes!"
            call her_main("!!!", "angry", "wide", "base", "stare")

            call her_chibi_scene("bj", trans=d5)
            pause.8

            call bld
            call nar(">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion.")

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            call cum_block
            call bld
            g4 "{size=+7}*ARGH*!{/size}"
            call her_main("*Gulp!-Gulp!-Gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            g4 "And some more!"
            call her_main("*Gulp*! *Gulp*! *Gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")
            call bld("hide")
            call ctc

            call her_chibi_scene("bj_pause", trans=d5)
            pause.8

            call bld
            m "Well, I think that's it."
            call her_main("..............", "cum", "happyCl", "worried", "mid")
            m "Are you alright there, [hermione_name]?"
            call her_main("Yes, [genie_name]...", "grin", "narrow", "base", "dead")
            call her_main("You came so much...")
            m "You managed to swallow it all though."
            call her_main("Yes... I thought I would choke...", "grin", "narrow", "base", "dead")
            call her_main("But I made a promise to myself that I won't let go of your penis no matter what!")
            m "Good girl."
            call her_main("Thank you, [genie_name].", "grin", "narrow", "base", "dead")
            call her_main("But, still... You came so much...")
            call her_main("I almost feel as if I just got fed...", "soft", "narrow", "annoyed", "up")
            call her_main("My stomach is so full...")
            g9 "Yes, I fed you with my cum!"

            if game.daytime:
                call her_main("You did... I think I may skip lunch today...", "soft", "narrow", "annoyed", "up")
            else:
                call her_main("You did... I think I may skip supper tonight...", "soft", "narrow", "annoyed", "up")

            call her_main("Can I get paid now?", "angry", "wink", "base", "mid")

            $ achievement.unlock("headlib")

        "-Don't bother-":
            call her_main("Yes, I love to suck and--", "soft", "narrow", "annoyed", "up")

            call cum_block
            g4 "{size=+7}Whore!{/size}"
            $ hermione.set_cum(face="light")
            call her_main("!!?", "shock", "wide", "base", "stare")

            call her_chibi_scene("bj_cum_out", trans=d5)
            call ctc

            $ hermione.set_cum(face="heavy")
            call her_main("[genie_name]...", "shock", "wide", "base", "stare")
            g4 "Don't you move now, [hermione_name]."
            $ hermione.set_cum(breasts="light")
            g4 "Yes, just be still and take it."
            g4 "*Argh*! You little slut! You make me cum hard, [hermione_name]!"
            call her_main("..............", "angry", "base", "base", "mid", tears="soft")
            m "Whew..."

            call her_chibi_scene("bj_cum_out_done")
            call her_main("..............", "normal", "happyCl", "worried", "mid")
            m "Alright, I'm done..."
            call her_main(".................", "open", "base", "base", "mid")

            if game.daytime:
                her "My classes are about to start..."
            else:
                her "I just took a shower recently..."
                g9 "And I gave you another one."
            m "Just wipe it off and you'll be alright."
            call her_main("............", "open", "base", "base", "mid")
            m "Unless, you don't want to."
            call her_main("*huh*?", "angry", "happyCl", "worried", "mid", emote="sweat")
            m "And would rather go outside looking like this."
            m "Let everyone see what a nasty little slut you are."
            call her_main("Of course not, [genie_name]!", "angry", "happyCl", "worried", "mid", emote="sweat")

            stop music fadeout 1.0
            if game.daytime:
                m "You better go before you are late for your classes..."
            else:
                m "It's getting late..."

            call her_main("Yes...", "angry", "happyCl", "worried", "mid", emote="sweat")
            call her_main("Can I get paid before I leave, [genie_name]?", "upset", "wink", "base", "mid")

    jump end_hg_pf_blowjob

### Hidden Blowjob ###

label hg_pf_hidden_blowjob:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj", trans=d9)
    call ctc

    call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "narrow", "annoyed", "up", xpos="base", ypos="head")
    m "Yes, good girl..."
    call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")

    call play_sound("knocking")
    "*Knock-knock-knock*!"
    call her_main("{size=+7}!!!{/size}", "open_wide_tongue", "narrow", "base", "up")
    m "*Hmm*?!"

    if game.daytime:
        m "Who could that be?"
    else:
        m "Who could that be at this hour?"

    #Priority.
    if hg_blowjob.ss_counter == 0:
        jump hg_hidden_blowjob_snape

    elif hg_blowjob.nt_counter == 0:
        jump hg_hidden_blowjob_tonks

    elif luna_unlocked and luna_reverted and hg_blowjob.ll_counter == 0:
        jump hg_hidden_blowjob_luna

    $ hg_hidden_bj_list = []
    if hg_blowjob.ss_counter >= 1:
        $ hg_hidden_bj_list.append("snape")
    if hg_blowjob.nt_counter >= 1:
        $ hg_hidden_bj_list.append("tonks")
    if hg_blowjob.ll_counter >= 1:
        $ hg_hidden_bj_list.append("luna")

    #Random Pick.
    $ character_choice = renpy.random.choice(hg_hidden_bj_list)

    $ renpy.jump("hg_hidden_blowjob_" + character_choice)

label hg_hidden_blowjob_snape:
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    call her_main("([genie_name], what should I do?)", "shock", "wide", "base", "stare")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    call her_chibi_scene("bj", trans=d5)
    pause.8

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*!"

    sna "Are you there? I need to talk to you."
    call her_main("(It's professor Snape!)", "open_wide_tongue", "base", "base", "mid")
    call her_chibi_scene("bj_pause")
    call her_main("{size=-2}[genie_name], please, send him away, I beg you!{/size}", "angry", "base", "base", "mid")

    menu:
        m "..."
        "\"Please, come on in, Severus.\"":
            pass

        "\"I am busy right now, Severus.\"":
            call her_main("{size=-2}Thank you, [genie_name].{/size}", "angry", "base", "base", "mid")
            sna "Busy? With what?"
            sna "All you do is sit on you arse all day."
            sna "I really need to talk to you about something."
            m "I said I am busy, Severus."
            m "Understood? I.. am.. \"busy\"!"
            sna "Oh... You mean \"busy\" busy? Gotcha!"
            sna "Well, I'll talk to you later then."

            jump hg_pf_blowjob_1

    $ hg_blowjob.ss_counter += 1
    $ her_mood = 30

    stop music fadeout 1.0
    call her_main("{size=-2}[genie_name], no!{/size}", "angry", "base", "angry", "mid", emote="angry")

    call nar(">Hermione gives your balls a firm twist full of frustration.")
    g4 "Ouch!"

    call play_sound("door")
    hide screen bld1
    call sna_chibi("stand","door","base")
    with d3
    pause.8

    call sna_walk("mid", "base")
    pause.2

    call play_music("snape")
    call sna_main("Good, you are here.","snape_01", xpos="base", ypos="head")
    call her_chibi_scene("bj")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "slit", "worried", "ahegao")
    call sna_main("Listen, there is something I want to discuss...","snape_06")
    call sna_main("*Hmm*...?","snape_05")
    call sna_main("Genie? Are you alright?")
    call her_main("{size=-4}(Ginny!!? Is she here as well?!){/size}", "open_wide_tongue", "narrow", "base", "up")
    call her_main("{size=-4}(No, please! I will die of shame!){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    m "Yes, Severus, I am fine..."
    call her_main("{size=-4}(What? *Slurp*...? *Slurp*...? *Gulp*...?){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    call sna_main("What are you... looking at?","snape_05")
    m "*Ehm*... Just admiring...{w=0.5} the cupboard."
    m "Please, continue..."
    call sna_main("...............","snape_05")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "base", "up")
    m "Did you want to discuss something?"
    call sna_main("Yes. That Granger girl.","snape_06")
    call her_main("{size=-4}(*Slurp*...! *Gobble*...! *Gulp*...!){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    m "Oh... What about her?"
    call sna_main("You promised that you would take care of the little witch.","snape_04")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "slit", "worried", "ahegao")
    call sna_main("But she is still being a major pain in my arse!","snape_04")
    call sna_main("Her tactics have changed...")
    call sna_main("But the amount of grief she manages to bring me is the same...","snape_03")
    m "I see... ah..."
    call sna_main("I swear, that girl is driving me crazy!","snape_10")
    g4 "Yeah, she is driving me crazy as well... ah..."
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "base", "up")
    call sna_main("Will you take care of this then?","snape_04")
    m "Yes. She'll get what she deserves."
    call sna_main("Good. That is all I wanted to hear.","snape_06")

    if game.daytime:
        m "Well, have a good day, Severus."
        call sna_main("Yes, thank you.","snape_06")
    else:
        m "Good night, Severus."
        call sna_main("Right...","snape_06")

    stop music fadeout 1.0
    call hide_characters
    hide screen bld1
    with d3

    call sna_chibi("stand","mid","base", flip=True)
    with d3
    pause.2

    call sna_walk(action="leave")
    pause.8

    call play_music("playful_tension") # SEX THEME.
    call bld
    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
    ">Seeing her being so confused and vulnerable - and yet continuing to perform her task diligently - pushes you over the edge."
    g4 "(Here it comes!)"

    jump hg_hidden_blowjob_cumming

label hg_hidden_blowjob_luna:
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    call her_main("[genie_name], what should I do?", "shock", "wide", "base", "stare")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    lun "[lun_genie_name]? Are you there? I need to talk to you."
    if lun_genie_name not in ["Sir","Professor","Dumbledore"]:
        call her_main("([lun_genie_name]?!)", "soft", "squint", "base", "mid")
        call her_main("(Wait, it's Luna!)", "disgust", "wide", "base", "stare")
    else:
        call her_main("(It's Luna!)", "disgust", "wide", "base", "stare")
    call her_main("{size=-2}Please, [genie_name], send her away, I beg you!{/size}", "shock", "happyCl", "worried", "mid")

    menu:
        m "..."
        "\"Please, come on in, [luna_name].\"":
            pass

        "\"I am busy right now, [luna_name].\"":
            call her_main("Thank you, [genie_name].", "angry", "base", "base", "mid")
            lun "Oh... well, I'll visit you later then, [lun_genie_name]."
            if game.daytime:
                lun "Have a good day!"
            else:
                lun "Have a good night!"
            m "I definitely will, Miss Lovegood!"

            jump hg_pf_blowjob_1

    $ hg_blowjob.ll_counter += 1
    $ her_mood += 10

    stop music fadeout 1.0
    call her_main("{size=-2}[genie_name], no! Why would you let-{/size}", "angry", "base", "angry", "mid", emote="angry")
    m "Quiet, [hermione_name]! Unless you want to be noticed..."

    #Luna comes in
    call lun_walk("mid", action="enter")

    call lun_main("Hello, [lun_genie_name].","soft","base","base","down", xpos="base", ypos="head")
    call bld("hide")
    pause.2

    call her_chibi_scene("bj", trans=d5)
    pause.8

    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    g9 "Miss Lovegood! How can I help you?"
    call lun_main("I have a message for you, [lun_genie_name]... from Professor Sprout.","open","base","base","R")
    m "Professor Sprout?"
    m "(Who was that again?)"
    call lun_main("Yes, she's sent me to inform you about the school's latest yield of {i}Venomous Tentacula{/i}.","open","base","raised","mid")
    m "(Venomous Tentacles?)"
    call her_main("{size=-4}(Those things are nasty... *Slurp...* *Gulp...*){/size}", "open_wide_tongue", "narrow", "annoyed", "up")

    lun "Very feisty little plants, they are. And still quite young."
    lun "They'll wither if you don't take care of them properly..."
    m "So why tell me?"
    call lun_main("They have just started sucking!","smile_large","happyCl","raised","mid")
    with hpunch
    m "What?"
    call her_main("{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}", "open_wide_tongue", "narrow", "base", "up")
    call lun_main("Sucking, [lun_genie_name]!","base","seductive","base","mid")
    call lun_main("It's so cute! They suck at each other's tentacles with their little mouths!","soft","base","raised","up")
    m "(Plants with mouths?)"
    call lun_main("Normally they only do that shortly before they spread their spores.","open","base","base","R")
    call lun_main("Which means they are almost ready!","grin","happyCl","raised","mid")
    m "Ready? for what?"
    call lun_main("Pollination!","soft","seductive","base","mid")
    call lun_main("That's when they weave their tentacles into each other and shoot out their spores.","open_tongue","seductive","base","up")
    m "(How nasty!)"

    call lun_main("You won't believe how hard it is to get them to that stage...","pout","mad","mad","up")
    call lun_main("It's quite an achievement!","base","base","base","mid")

    m "I'm more than familiar with them!"
    call lun_main("You are?","soft","wink","raised","mid")
    g4 "Those young...{w=0.4} sucking...{w=0.4} *UGH*!{w=0.2} Troublemakers!"
    g4 "Yes. I've got one right here!"
    call lun_main("Oh! Can I see it, [lun_genie_name]?","grin","wide","raised","mid")
    m "I'm afraid not, [luna_name]."
    g9 "It's such a shy little thing. You'd better not get any closer!"
    call lun_main("*Aww*... Okay.","pout","base","sad","down")
    m "I know everything about those little devils..."
    m "At first there was just bitching and moaning about every tiny little thing I wanted to do..."
    m "But now, straight down on the knees... right in front of me."
    g4 "Sucking like crazy!"
    call lun_main("(So they do not only have a head but also knees... I didn't even know that!)","soft","base","raised","up")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "base", "up")

    call lun_main("Sprout told us to be careful, [lun_genie_name]. As you probably know, they like to spit... and bite...","soft","base","base","mid")
    m "Truly?"
    call lun_main("Yes. If you aren't careful, they'll hit you with their saliva, or bite at your limbs!","clench","annoyed","raised","down")
    call lun_main("Luckily, there is an easy way to make them stop such behaviour!","base","seductive","base","mid")
    m "I'm all ears..."
    call lun_main("They hate being spat on just as much as you, [lun_genie_name]. Maybe even more so!","soft","seductive","base","L")
    m "(Those are some weird fucking plants...)"
    call lun_main("She said that if a {i}Venomous Tentacula{/i} ever acts up--","open","closed","raised","mid")
    call lun_main("You should show dominance by spitting on it and put it in its place!","angry","angry","angry","down")
    call lun_main("Her words...","pout","base","raised","R")
    g9 "Like this?"
    call spit_on_her

    g4 "Take that, you nasty little slu-- *Uhh*, plant."
    call her_main("{size=-4}(What the... *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "slit", "worried", "ahegao")
    call lun_main("That's right, [lun_genie_name]!","grin","happyCl","raised","mid")
    g4 "This one wants more spit!"
    call spit_on_her
    call her_main("{size=-4}(Stop it! *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "base", "up")
    call lun_main("Professor Sprout said, sometimes, a bit of tough love is the only thing that can make them behave.","clench","angry","angry","down")
    m "She did?"
    g9 "Oh no, mine is fighting back!"
    call lun_main("Be careful, [lun_genie_name]! Or she'll bite you!","clench","closed","sad","mid")
    g4 "Don't worry, this one's getting a beating!"
    call slap_her
    call her_main("{size=-4}(Ouch!... *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    call slap_her
    call slap_her
    g4 "Had enough, you nasty little thing?"
    call slap_her
    g4 "Want some more?"
    call slap_her
    call slap_her

    call lun_main("You seem so well versed with plants!","grin","wide","raised","mid")
    call lun_main("I need to tell Professor Sprout, she'll be overjoyed to hear about your training methods!","grin","happyCl","raised","mid")
    m "Give her my thanks, [luna_name]. She's a smart lady, this Sprout!"
    g9 "Full of great ideas!"
    call lun_main("I will, [lun_genie_name].","smile","seductive","base","mid")

    if game.daytime:
        call lun_main("Have a nice day!","smile_large","happyCl","base","mid")
    else:
        call lun_main("Good night!","smile_large","happyCl","base","mid")

    #Luna leaves.
    call lun_walk(action="leave")

    stop music fadeout 1.0
    call bld
    m "Well that wasn't too bad, was it?"
    call her_main("{size=-4}(............................. *Slurp...* *Slurp...* *Gulp...*){/size}", "open_wide_tongue", "narrow", "annoyed", "up")

    call play_music("playful_tension") # SEX THEME.

    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."

    jump hg_hidden_blowjob_cumming

#Needs Friendship level parameter added for tonks chat variations if ton_friendship < X:
#Needs event label check for Tonks to ask if it's susan in there. replace if ag_st_imperio.tier >= 5:
#Add Tonks BJ counter
label hg_hidden_blowjob_tonks:
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    call her_main("[genie_name], what should I do?", "shock", "wide", "base", "stare")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    ton "[ton_genie_name]? Is it okay if I come in?"
    call her_main("(It's Professor Tonks!)", "clench", "happyCl", "worried", "mid")
    call her_main("{size=-2}Please, [genie_name], don't let her in!{/size}", "open", "base", "worried", "mid")
    call her_main("I don't want my teacher to see me like this!", "shock", "narrow", "worried", "down")

    menu:
        m "..."
        "\"Please, come on in.\"":
            pass

        "\"I am busy right now, [tonks_name].\"":
            call her_main("Thank you, [genie_name].", "soft", "base", "base", "mid")
            ton "Busy?"
            ton "Could it be..."
            ton "Is Snape with you?"
            if game.daytime:
                ton "Are you two having one of your silly little duels again?"
            else:
                ton "Don't stay up drinking again..."
                ton "We wouldn't want him making a fool of himself. Not in front of the students."
                ton "He made such a mess last time..."

            call her_chibi_scene("bj", trans=d5)
            pause.8

            call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "squint", "worried", "up")
            m "He isn't here, actually. But I will let him know..."
            ton "So, are you with a student then, *Hmm*?"
            call her_main("{size=-4}(.......... *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
            ton "Who is she?"

            if ag_st_imperio.tier >= 3:
                ton "Is it the blonde girl? Or..."
                call her_main("{size=-4}(Blonde!?! *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "squint", "worried", "up")
                call her_main("{size=-4}(*Slurp*... *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
            elif ag_st_imperio.tier >= 5:
                ton "You aren't shagging that busty red head, are you?"
                call her_main("{size=-4}(Busty who? *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "squint", "worried", "up")
                call her_main("{size=-4}(Is she talking about Susan? *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")

            m "That's non of your concern, Miss Tonks!"
            m "You may leave now..."
            call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "base", "up")

            if ton_friendship < 50:
                ton "You sure you don't need my assistance?"
                g4 "I said, leave!"
            else:
                ton "I can help you jack off, if that's what you're--"
                m "Maybe later, [tonks_name]."
            ton "Okay, [ton_genie_name]."
            ton "*Giggle...*"
            call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
            m "I think she's gone..."

            jump hg_pf_blowjob_1

    $ hg_blowjob.nt_counter += 1
    $ her_mood += 10

    # Setup
    $ ton_outfit_last.save() # Store current outfit.
    $ tonks.equip(ton_outfit_default)

    stop music fadeout 1.0
    call her_main("{size=-2}[genie_name], no! Please she will know that-{/size}", "angry", "base", "angry", "mid", emote="angry")
    m "*Shhhhsh*... Keep your voice down..."

    #Tonks comes in
    call bld("hide")
    pause.2

    call play_sound("door")
    call ton_chibi("stand","door","base")
    call chibi_emote("hearts", "tonks")
    with d3
    pause.5

    call chibi_emote("hide", "tonks")
    with d3
    pause.1

    call ton_walk("mid","base")

    if game.daytime:
        call ton_main("Hello, Sir.","base","base","base","mid", xpos="right", ypos="base", trans=d3)
    else:
        call ton_main("Good evening, Sir.", "base", "base", "shocked", "mid", xpos="right", ypos="base", trans=dissolve)

    call her_chibi_scene("bj", trans=d5)

    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    g9 "Tonks! What can I do for you?"
    call ton_main("I was wondering if we could--","open","base","raised","R")
    call ton_main("(...)", "annoyed", "narrow", "raised", "L")
    call ton_main("Am I interrupting something?", "soft", "base", "raised", "down")
    call her_main("(She's going to find out!!!)", "open_wide_tongue", "narrow", "annoyed", "up")
    m "Nothing important..."

    menu:
        "-Tell the truth-":
            m "Just stuffing Miss Granger's cute little mouth..."
            g9 "With my cock!"
            call her_chibi_scene("bj_pause", trans=d5)

        "-Lie-":
            m "... Just polishing...{w=0.5} the woodwork."
            call ton_main("Like I'm going to believe that...", "upset", "base", "base", "downR")
            call ton_main("Are you masturbating, [ton_genie_name]?","horny","base","raised","mid")

            if ton_friendship < 50:
                call ton_main("Or perhaps somebody else has their tongue wrapped around it?", "soft", "base", "raised", "L")
                call her_main("{size=-4}(*Blergchhhgh*... *Cough*... *Cough*... *Cough*...){/size}", "open_wide_tongue", "base", "worried", "ahegao")
                call ton_main("What was that?","base","base","raised","mid")
                call ton_main("Surely there's nobody at this school who would be able to pleasure you properly...", "grin", "base", "raised", "mid")
            else:
                call ton_main("Are you stroking your hard, {w=0.3}magnificent, {w=0.3}cock?","soft","base","base","stare")
                with hpunch
                call her_main("{size=-4}(*Blergchhhgh*... *Cough*... *Cough*... *Cough*...){/size}", "open_wide_tongue", "slit", "worried", "ahegao")
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("{size=-4}What??{/size}", "open_wide_tongue", "narrow", "base", "up")
                call ton_main("What was that?","open","base","raised","mid")
                call ton_main("[ton_genie_name]?!","grin","base","base","mid")
                m "*Ehm*-{w=0.5} My belly?"
                call ton_main("Sounded like somebody doesn't know how to deep throat a dick properly...","open","base","base","R")

            call her_main("(Excuse me?!)", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Don't be mean, she's doing her best..."
            call ton_main("So there is a girl behind you!", "horny", "wide", "raised", "down")
            call ton_main("Who is it? Tell me!", "soft", "shocked", "shocked", "mid")
            m "(...)"
            m "It's Miss Granger."

    call ton_main("Miss Granger?!", "open", "wide", "shocked", "stare")

    if her_reputation <= 15:
        call ton_main("*Hmm?*... I thought she'd be busy pretending to study in the library.","open","base","raised","mid")
        call her_main("(Pretending???)", "open_wide_tongue", "narrow", "base", "up")
    else:
        call ton_main("*Oh?* I could've sworn I just saw her in the library fluttering her eyelashes to some Slytherin boy...","open","base","raised","mid")
        call her_main("(What!!?)", "open_wide_tongue", "narrow", "annoyed", "up")
        with hpunch
        m "Ouch, I felt that..."

    if ton_friendship < 50:
        call ton_main("So she has her lips wrapped around you? {w=0.5}Right now???", "soft", "base", "shocked", "L")
    else:
        call ton_main("You're telling me that you are fucking her mouth? {w=0.5}Right now???","soft","base","shocked","mid")

    call ton_main("Oh I've got to see this...","horny","base","base","down")
    call ton_main("","horny","base","base","down", xpos="mid", trans=d3)
    pause.2
    g4 "Wait!"
    call ton_main("*Hmm*?","horny","base","raised","mid")

    m "You better not come any closer..."
    m "Or I fear she will bite me..."
    g4 "Or worse..."
    m "She'll stop with the sucking..."
    call her_main("(Damn right I will...)", "open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj", trans=d5)
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "slit", "worried", "ahegao")
    call ton_main("Very well...","base","base","raised","R", xpos="right", trans=d3)
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "squint", "worried", "up")

    call ton_main("Is that really, {w=0.5}Miss Hermione Granger,{w=0.5} back there?", "horny", "narrow", "base", "mid")
    call ton_main("That's so hard to believe!","open","base","raised","L")
    call ton_main("Or perhaps, you are just fucking with me, [ton_genie_name]...", "soft", "base", "base", "mid")
    m "I'm not fucking with you..."
    g9 "... I'm fucking her mouth."
    call ton_main("That's too good to be true!", "horny", "narrow", "base", "stare")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")

    call ton_main("Miss Granger, If that's really you back there, why don't you say hi to your favourite teacher?", "grin", "base", "raised", "down")
    m "(...)"
    call ton_main("I will reward you with fifty house points if you show yourself!","base","base","raised","down")
    with hpunch
    g4 "What?!"

    call her_chibi_scene("bj_pause", trans=d5)

    call her_main("(Oh wow, that's a lot of points!)", "open_wide_tongue", "narrow", "annoyed", "down_soft")

    call her_chibi_scene("bj", trans=d5)

    g4 "You can't give her that many points, [tonks_name]! She's already getting {number=current_payout} from me!"
    m "Do you even realise how many days I'll have to spend with Snape, of all people, to get even with Slytherin again, after this?"
    call ton_main("So what? The girl has clearly earned it!", "soft", "base", "annoyed", "mid")
    call ton_main("Sucking her headmaster's cock...", "horny", "base", "annoyed", "down")
    call ton_main("Fifty points could be yours, Miss Granger!","open","base","raised","down")
    call ton_main("You only have to stick your gorgeous head out and say hi to me, and of course...","open","base","base","R")
    call ton_main("I promise I won't tell anybody.","base","base","base","down")
    call ton_main("It will be our little secret.", "soft", "base", "shocked", "down")
    call her_main("(...)", "open_wide_tongue", "narrow", "annoyed", "up")
    m "Do what you must, girl..."
    call her_main("(...............)", "open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause", trans=d5)

    # Stop hiding sprite temporarily
    $ use_hermione_head = False
    call her_main("", "disgust", "narrow", "worried", "down", xpos="left", cheeks="blush", flip=True, trans=d3)

    pause 1.0

    call ton_main("Oh my!","horny","base","base","down")

    call her_main("H-Hello, professor Tonks.", "clench", "happyCl", "worried", "mid")

    call ton_main("Miss Granger, what a pleasant surprise.", "grin", "wide", "raised", "L")
    call ton_main("Are you having a good time back there?", "base", "wide", "base", "L")

    if her_reputation <= 15:
        call ton_main("It sure sounded like you were...","horny","base","raised","mid")
    else:
        call ton_main("You nasty little cock sucker.","horny","base","raised","mid")

    call her_main("(.......)", "soft", "narrow", "annoyed", "up")
    call her_main("I suppose so.........", "disgust", "narrow", "worried", "down")
    call ton_main("What a sight to see...","base","base","base","mid")

    $ use_hermione_head = True
    call her_main("", "open_wide_tongue", "squint", "worried", "up", xpos="base", flip=False)
    call her_chibi_scene("bj", trans=d5)

    if ton_friendship < 50:
        call ton_main("You're really going to town, aren't you...","base","base","base","down")
        call ton_main("You should make sure you breathe every once in a while dear girl.", "horny", "base", "base", "mid")
        g9 "If you need to have her vitals checked out afterwards - I'm sure we could come to an arrangement."
    else:
        call ton_main("I'd love to join you back there, Miss Granger...","base","base","base","down")
        call ton_main("Suck your Headmaster's dick with you!","horny","base","angry","mid")
        call her_main("{size=-4}(She'd do what?... *Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "worried", "up")
        g9 "You can both have it!"

    call ton_main("I'm sorry, [ton_genie_name]... I'm already pre-occupied with something...", "open", "narrow", "base", "R")
    if game.daytime:
        call ton_main("Teaching our second-years how to cast a simple deflection spell...","open","base","raised","down")
    else:
        call ton_main("I'm preparing some material for our second-years how to cast a simple deflection spell...","open","base","raised","down")
    call ton_main("We are already two sessions behind my planned class schedule.", "annoyed", "base", "base", "mid")
    call ton_main("I came to you to get consultation about some of the material I had prepared for them.", "open", "base", "shocked", "down")
    m "(Yeah right, more like she wanted some of my firewhisky...)"
    call ton_main("But since you have to take care of Miss Granger right now...","base","base","raised","down")
    call ton_main("I suppose it can wait.", "base", "base", "raised", "R")
    call ton_main("Who said teaching would be easy, am I right?", "open", "closed", "shocked", "mid")
    m "It's quite easy, actually."
    call ton_main("As a headmaster maybe... I'm sure your private tutelage is very popular...", "horny", "base", "raised", "down")
    m "It can get quite hard, taking care of all those girls."
    call ton_main("I can certainly see that...", "base", "base", "annoyed", "down")
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")

    call ton_main("Anyhow...","open","base","raised","R")
    call ton_main("Hermione, for your exceptional and benevolent effort of sucking your headmaster's cock, {w=0.5}I hereby reward the house Gryffindor...", "soft", "base", "base", "down")

    call her_chibi_scene("bj_pause", trans=d5)
    call ton_main("Sixty-nine points!", "grin", "wide", "base", "mid")
    $ gryffindor += 69

    call her_main("(Sixty-nine! That's even more than she agreed on!)", "shock", "wide", "base", "up")
    m "Didn't you say fifty earlier?"
    call ton_main("Yes, but sixty-nine is so much better!","horny","base","raised","mid")
    call ton_main("Don't you think so too, Miss Granger?","base","base","angry","down")
    call her_main("*Ehm*... Yes. Thank you, professor Tonks.", "disgust", "happyCl", "worried", "mid")
    m "Less talking, more sucking, [hermione_name]!"
    call her_main("Sorry, [genie_name]...", "soft", "narrow", "annoyed", "up")

    call her_chibi_scene("bj", trans=d5)
    call her_main("{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}", "open_wide_tongue", "narrow", "annoyed", "up")
    call ton_main("I'm going to have to go, [ton_genie_name].", "open", "closed", "shocked", "mid")
    call ton_main("Wish I could watch you two a little longer...", "soft", "base", "base", "L")
    call ton_main("But I have to head back to my office.", "open", "base", "base", "downR")
    m "What a shame."
    if ton_friendship < 50:
        call ton_main("Make sure she gets a good taste.","horny","base","base","mid")
    else:
        call ton_main("Make sure she swallows for me.","horny","base","base","mid")
    g9 "Every last drop!"

    if game.daytime:
        call ton_main("See you in class, {i}Parseltongue{/i}!","horny","base","angry","down")
    else:
        call ton_main("Have a good night, {i}Parseltongue{/i}!", "horny", "base", "annoyed", "down")

    call her_main("..........", "open_wide_tongue", "happyCl", "worried", "mid")

    #Tonks leaves.
    stop music fadeout 1.0

    call ton_walk(action="leave")
    pause.5

    $ tonks.equip(ton_outfit_last) # Equip custom outfit.

    call play_music("playful_tension") # SEX THEME.
    call bld
    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."

    jump hg_hidden_blowjob_cumming

label hg_hidden_blowjob_cumming:
    call her_chibi_scene("bj", trans=d5)
    pause.8

    call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "squint", "worried", "up", flip=False)
    ">Hermione keeps sucking on your cock with a rather fierce determination."
    ">Her technique is lacking but she makes up for it with the effort she puts in."

    m "Yes... I love your eager, little mouth, girl..."
    call her_main("*Gobble*! *Gobble*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause", trans=d5)
    call her_main("[genie_name]?", "soft", "narrow", "annoyed", "up")
    m "*Hmm*?"
    call her_main("Are you going to cum on my face today?", "soft", "narrow", "annoyed", "up")
    call her_main("Or do you plan to cum in my mouth?")

    menu:
        "\"I Plan to splatter your face with cum!\"":
            call her_main("I see...", "soft", "narrow", "annoyed", "up")
            m "Why do you ask?"
            call her_main("Oh... I just read in a book that semen contains a lot of antioxidants...", "grin", "narrow", "base", "dead")
            call her_main("It's good for the skin...")
            m "Great. One facial coming right up."
            m "Back to work now."

        "\"I Plan to fill your mouth with cum!\"":
            call her_main("I see...", "grin", "narrow", "base", "dead")
            m "Why do you ask?"
            call her_main("Well, I am trying to watch my calorie-intake...", "soft", "narrow", "annoyed", "up")
            call her_main("I just wonder how much calories your load contains, [genie_name].")
            call her_main("Maybe I should skip my next meal...")
            m "[hermione_name]."
            call her_main("Yes?", "soft", "narrow", "annoyed", "up")
            m "Dick back in the mouth."

        "\"I don't plan so far ahead.\"":
            call her_main("I see...", "soft", "narrow", "annoyed", "up")
            m "Don't you like surprises?"
            call her_main("Not really...", "soft", "narrow", "annoyed", "up")
            call her_main("I rather enjoy planning ahead actually...")
            m "Well some things in life are just unpredictable."
            m "There is only one way to find out for sure."

        "\"What would you like?\"":
            call her_main("If it is all the same to you, [genie_name]...", "soft", "narrow", "annoyed", "up")

            $ random_number = renpy.random.randint(1, 2)
            if random_number == 1:
                call her_main("I would like you to cum on my face, [genie_name].", "grin", "narrow", "base", "dead")
                call her_main("I read that it's good for the skin.")
            else:
                call her_main("I would like you to cum in my mouth.", "grin", "narrow", "base", "dead")
                call her_main("You usually cum so much so I think I will be able to just skip my next meal...")
                if game.daytime:
                    call her_main("And do some light workout instead.")
                else:
                    call her_main("And do some homework instead.")

            m "Well, we'll see about that."
            m "Back to sucking now."

    call her_chibi_scene("bj", trans=d5)
    call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
    m "*Hmm*..."
    m "You are getting better at this [hermione_name]."
    call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "narrow", "base", "up")
    m "Okay, say something nasty now..."
    call her_main("*Slurp*--?", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_chibi_scene("bj_pause", trans=d5)

    if her_tier <= 5:
        call her_main("*Uhm*...", "angry", "narrow", "base", "down")
        call her_main("I eat cockroaches?", "angry", "base", "base", "mid")
        m "What the fuck?"
        call her_main("T-they are pretty nasty, [genie_name]...", "angry", "base", "base", "mid")
        m "No, [hermione_name], I mean something dirty!"
        m "And don't you dare to say \"mud\"!"
        m "I mean dirty in a sexual way!"
        call her_main("Oh... *Ehm*...", "angry", "narrow", "base", "down")
        m "Ah, never mind, the moment is gone..."
        call her_main("*Ehm*... I'm sorry, [genie_name].", "angry", "base", "base", "mid")
        m "Yeah, whatever. Make it up to me by sucking my cock harder."
        call her_main("Of course, [genie_name].", "upset", "closed", "base", "mid")
    else:
        call her_main("I'm a cumslut, [genie_name].", "base", "squint", "base", "mid")
        call her_main("A slut for your cum.", "base", "narrow", "base", "mid_soft")
        m "That's it, [hermione_name]."
        call her_main("It's all I can think about [genie_name].", "base", "narrow", "worried", "down")
        call her_main("Sucking your dirty old cock...")
        m "Well you better get back to it then [hermione_name]"
        call her_main("Thank you, [genie_name].", "grin", "narrow", "base", "dead")
        m "You're welcome, cumslut."
        call her_main("...", "base", "narrow", "base", "up")

    call her_chibi_scene("bj", trans=d5)
    call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
    m "Yes, like this... Good..."
    call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
    m "You know what? I think we are almost there."
    call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
    m "Yes, definitely."
    call her_main("*Slurp*! *Gobble*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
    m "Alright, [hermione_name], this is the final stretch."
    g4 "Show me what you've got."
    call her_main("*Gobble-goble-slurp-goble*!", "open_wide_tongue", "narrow", "annoyed", "up")
    g4 "Yes, like that!"
    call her_main("{size=+5}*Gobble-gobble-slurp-gobble*!{/size}", "open_wide_tongue", "narrow", "base", "up")
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    g4 "*Ghr*!!!"

    menu:
        g4 "!!!"
        "-Cum in her mouth-":
            g4 "Here it comes, [hermione_name]! get ready to swallow, and fast!"
            call her_main("!!!", "open_wide_tongue", "narrow", "base", "up")

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            call bld
            g4 "{size=+7}ARGH!{/size}"
            g4 "Swallow my cum, slut!"
            call her_main("*Gulp!-Gulp!-Gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            g4 "Yes! Down your fucking throat!"
            call her_main("*Gulp-gulp-gulp-gulp-gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")

            stop music fadeout 1.0
            hide screen bld1
            call ctc

            call bld
            m "Well, I think that's it."
            m "You can let go now..."

            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("...........................", "full_cum", "narrow", "base", "dead")
            call her_main("................")
            call her_main("........")
            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            call her_main("*GULP*!", "cum", "happyCl", "worried", "mid")
            call her_main("*Gua-ha*...", "open_wide_tongue", "base", "base", "mid")
            m "You alright?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Yes, [genie_name]...", "grin", "narrow", "base", "dead")
            m "Going to skip your next meal?"
            call her_main("I think so...", "grin", "narrow", "base", "dead")
            call her_main("You always cum so much, [genie_name]...")
            m "Heh... And whose fault is that??"
            call her_main(".............", "grin", "narrow", "base", "dead") #Smile.
            call her_main("Can I get paid now?")

            if her_tier >= 6:
                if game.daytime:
                    m "What, even after I just gave you lunch?"
                else:
                    m "What, even after I fed you dinner?"
                call her_main(".............", "annoyed", "squint", "base", "mid") #Smile.
                call her_main("Fine, I suppose this was a worthy meal.")

        "-Cum on her face-":
            call her_chibi_scene("bj_pause", trans=d5)
            g4 "Ready for your facial, [hermione_name]?"
            call her_main("Yes, [genie_name]!", "grin", "narrow", "base", "dead")
            g4 "Here it comes then!"

            call cum_block
            call her_chibi_scene("bj_cum_out", trans=d5)
            pause.8

            $ hermione.set_cum(face="light")
            call bld
            g4 "{size=+7}Whore!{/size}"
            call her_main("!!?", "shock", "wide", "base", "stare")
            hide screen bld1
            call ctc

            $ hermione.set_cum(face="heavy")

            call her_main("[genie_name]...", "shock", "wide", "base", "stare")
            g4 "All over your fucking face!"
            call her_main("*Aaah*!", "grin", "narrow", "base", "dead")

            call her_chibi_scene("bj_cum_out_done", trans=d5)
            m "Well, I'm done."
            call her_main("....................................", "grin", "narrow", "base", "dead")
            m "I said it's over, [hermione_name]."
            call her_main("Yes, I heard you [genie_name]...", "grin", "narrow", "base", "dead")
            m "So... Aren't you going to clean up?"
            call her_main("In a moment...", "grin", "narrow", "base", "dead")
            call her_main("I'm giving my skin time to soak in the anti-oxidants...")
            m "*Hmm*... I find this quite hot..."
            m "Take your time, [hermione_name]..."
            call blkfade

            stop music fadeout 1.0
            ">A while later."

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blktone
            call hide_blkfade
            pause.5

            call her_main("I take it you enjoyed yourself, [genie_name]?", "angry", "wink", "base", "mid")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Yes I did, [hermione_name]."
            call her_main("Good, so Can I get paid now?", "grin", "narrow", "base", "dead")

            if her_tier >= 6:
                m "What, even after I just gave you a salon treatment?"
                m "Other women pay a lot of money for a good facial."
                call her_main(".............", "annoyed", "squint", "base", "mid") #Smile.
                call her_main("Fine, but my skin better look glamorous by tomorrow.")
                g9 "You can always come for a second dosage."

    jump end_hg_pf_blowjob

### Fourth Blowjob ###

label hg_pf_blowjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj", trans=d9)
    call ctc

    call play_music("playful_tension") #HERMIONE
    call her_main("*Slurp*! *Slurp*! *Gulp*!", "open_wide_tongue", "narrow", "annoyed", "up", xpos="base", ypos="head")
    m "Yes, good girl..."
    call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
    m "lick the shaft..."
    call her_main("*lick*! *Slurp*! *lick*!", "open_wide_tongue", "narrow", "base", "up")
    call nar(">Hermione keeps sucking on your cock like her life depends on it.","start")
    call nar(">Her technique is almost perfect and she is incredibly enthusiastic.","end")
    m "Yes... I love your eager, little mouth, slut..."
    call her_main("*Gobble*! *Gobble*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    call her_main("[genie_name]?", "base", "narrow", "worried", "down")
    m "*Hmm*?"
    call her_main("How would you like me to please you today?", "soft", "narrow", "annoyed", "up")

    menu:
        #"\"Take it down your throat!\"" if hg_pf_blowjob.points >= 2: # Second event (facefuck) happened.
        #    jump hg_pf_facefuck_1

        "\"Pretend I am your father.\"":
            call her_main("My father?", "angry", "wink", "base", "mid")
            m "Anything wrong with that?"
            call her_main("I suppose not...", "base", "narrow", "worried", "down")
            call her_main("I mean it's just pretending...", "grin", "narrow", "base", "dead")
            m "Great. Get that dick back in your mouth then."

            call her_chibi_scene("bj", trans=d5)
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "That's it, princess. Suck daddy's dick."
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            m "Tell me how much you want it."
            call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("So much daddy...", "soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("It's all I think about when we're home alone...", "base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *Gulp*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("When we're sitting together on the couch watching T.V...", "base", "narrow", "base", "up")
            call her_main("I just imagine that I am sucking your cock instead...", "base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*lick*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("I even wish that mum left you sometimes...", "annoyed", "narrow", "worried", "down")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *Slurp*! *lick*!", "open_wide_tongue", "narrow", "base", "dead")
            m "Why's that?"
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("So that I'm the only one to get your dick...", "soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("You'll come home every day...", "soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Throw me onto my bed...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("and use me...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("however you want...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("for as long as you want...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("you won't even ask...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("you'll just take me...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("even though I say no...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            m "That's it princess, Almost there..."
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Where do you want to cum today, daddy?", "soft", "narrow", "annoyed", "up")
            call her_main("Are you going to cover my face?", "soft", "narrow", "annoyed", "up")
            call her_main("Or make me swallow your big load?", "grin", "narrow", "base", "dead")
            call her_main("{size=-4}Even if I don't want to...{/size}", "grin", "narrow", "base", "dead")
            m "Let's find out shall we?"
            call her_main("Yes daddy...", "soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Yes, like that... Good girl..."
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Do it for daddy."
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Come on princess."
            call her_main("*Slurp*! *Gobble*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            m "Alright, [hermione_name], almost there."
            g4 "Make daddy proud!"
            call her_main("*Gobble-goble-slurp-goble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            g4 "Yes, like that!"
            call her_main("{size=+5}*Gobble-gobble-slurp-gobble*!{/size}", "open_wide_tongue", "narrow", "base", "dead")
            g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
            g4 "*Grr*!!!"

            menu:
                g4 "!!!"
                "-Cum in her mouth-":
                    g4 "Here it comes, [hermione_name]! Here comes daddy!"
                    call her_main("!!!", "open_wide_tongue", "narrow", "base", "up")

                    call cum_block
                    call her_chibi_scene("bj_cum_in", trans=d5)
                    pause.8

                    call bld
                    g4 "{size=+7}*ARGH*!{/size}"
                    g4 "Drown in my cum, whore!"

                    call her_main("*Gulp!-Gulp!-Gulp*!", "open_wide_tongue", "narrow", "annoyed", "up")
                    with hpunch
                    g4 "Yes! Down your fucking throat, slut!"
                    call her_main("*Gulp-gulp-gulp-gulp-gulp*!", "open_wide_tongue", "narrow", "base", "up")
                    stop music fadeout 1.0
                    call ctc

                    call her_chibi_scene("bj_pause", trans=d5)
                    pause.8

                    call bld
                    m "Well, I think that's it."
                    m "You can let go now..."
                    call her_main("...........................", "full_cum", "narrow", "base", "dead")
                    call her_main("................")
                    call her_main("........")

                    $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                    call her_main("*GULP*!", "cum", "happyCl", "worried", "mid")
                    call her_main("*Gua-ha*...", "open_wide_tongue", "base", "base", "mid")
                    m "How was that?"

                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("So tasty...", "grin", "narrow", "base", "dead")
                    m "Really?"
                    call her_main("Yes daddy...", "grin", "narrow", "base", "dead")
                    call her_main("It's always tasty with you...")
                    m "Heh... is that so?"
                    call her_main(".............", "grin", "narrow", "base", "dead")
                    call nar(">She leans forward and gives your wilting cock a small kiss.")
                    with kissiris
                    call her_main("Thanks, daddy!", "base", "narrow", "base", "mid_soft")

                "-Cum on her face-":
                    call her_chibi_scene("bj_pause", trans=d5)
                    g4 "Ready for your cum-load, princess?"
                    call her_main("Yes daddy!", "grin", "narrow", "base", "dead")
                    g4 "Here it comes then!"

                    call cum_block
                    call her_chibi_scene("bj_cum_out", trans=d5)
                    pause.8

                    $ hermione.set_cum(face="light")

                    call bld
                    g4 "{size=+7}Slut!{/size}"
                    call her_main("!!?", "shock", "narrow", "base", "dead")
                    call ctc

                    $ hermione.set_cum(face="heavy")

                    call her_main("Daddy...", "shock", "wide", "base", "stare")
                    g4 "That's it, princess!"
                    call her_main("*Aaah*!", "grin", "narrow", "base", "dead")

                    call her_chibi_scene("bj_cum_out_done", trans=d5)
                    pause.8

                    call bld
                    m "Well, I'm done."
                    call her_main("....................................", "grin", "narrow", "base", "dead")
                    m "I said it's over, [hermione_name]."
                    call her_main("Yes, I heard you, daddy...", "grin", "narrow", "base", "dead")
                    m "So... Aren't you going to clean up?"
                    call her_main("In a minute...", "grin", "narrow", "base", "dead")
                    call her_main("I'm just savouring the moment...")
                    m "*Hmm*..."
                    m "Take your time, [hermione_name]..."

                    stop music fadeout 1.0
                    call blkfade

                    ">A while later."

                    call her_chibi_scene("bj_pause", trans=d9)
                    pause.8

                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("I take it you enjoyed yourself, [genie_name]?", "angry", "wink", "base", "mid")
                    m "Yes I did, [hermione_name]."

        "\"Worship my cock.\"":
            call her_main("Worship it?", "angry", "wink", "base", "mid")
            m "Did I stutter?"
            call her_main("Well...", "base", "narrow", "worried", "down")
            call her_main("Okay...", "soft", "narrow", "annoyed", "up")
            m "Great. You can start by putting it back in your mouth."

            call her_chibi_scene("bj", trans=d5)
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "That's it.."
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "dead")
            m "Tell me how much you love my cock."
            call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("So much, [genie_name]...", "soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Slurp*! *Gobble*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("It's all I think about when I'm in class...", "base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *Gulp*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")

            if hg_pr_blowjob.counter == 0:
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("Sucking your perfect dick.", "base", "narrow", "base", "up")
                call her_main("No one else's...", "base", "narrow", "base", "up")
                call her_chibi_scene("bj", trans=d5)
                call her_main("*lick*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("Just your {w}perfect, {w}beautiful {w}{size=-4}cock{/size}!", "grin", "narrow", "base", "dead")
                call her_chibi_scene("bj", trans=d5)
                call her_main("*Gobble*! *Slurp*! *lick*!", "open_wide_tongue", "narrow", "annoyed", "up")
            else:
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("Even when you make me suck another boys dick...", "base", "narrow", "base", "up")
                call her_main("I still imagine that it's yours...", "base", "narrow", "base", "up")
                call her_chibi_scene("bj", trans=d5)
                call her_main("*lick*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "dead")
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("Imagine that it's your cum sliding down my throat...", "soft", "narrow", "annoyed", "up")
                call her_chibi_scene("bj", trans=d5)
                call her_main("*Gobble*! *Slurp*! *lick*!", "open_wide_tongue", "narrow", "base", "dead")
                call her_chibi_scene("bj_pause", trans=d5)
                call her_main("Or that it's your hot load shot across my face...", "grin", "narrow", "base", "dead")
                call her_chibi_scene("bj", trans=d5)
                call her_main("*Gobble*! *Slurp*! *lick*!", "open_wide_tongue", "narrow", "base", "up")

            m "Is that so?"
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Yes [genie_name]...", "soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Sometimes...", "soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("After you make me suck your tasty dick...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("I won't brush my teeth...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("just so I can go to sleep...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("with that perfect taste in my mouth...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("and when I do brush my teeth...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Your beautiful cock is all I can think about...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "worried", "down")
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Recently, I even started moaning whenever I'm brushing my teeth...", "grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            call her_main("*Gobble*! *lick*! *Gobble*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "That's it cock-slut, Almost there..."
            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("Where do you want to cum today [genie_name]?", "soft", "narrow", "annoyed", "up")
            call her_main("I know it's greedy of me to ask...", "angry", "narrow", "base", "down")
            call her_main("But can you cum in my mouth?", "angry", "wink", "base", "mid")
            call her_main("{size=-4}Please...{/size} I promise I won't waste a drop.", "soft", "narrow", "annoyed", "up")
            m "I think that can be arranged "
            call her_main("Thank you [genie_name]!", "smile", "happyCl", "base", "mid", cheeks="blush", emote="happy")
            call her_chibi_scene("bj", trans=d5)
            call nar(">Hermione devours your cock with renewed vigour.")
            call her_main("*Slurp*! *Gulp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Yes, like that... that's a good little slut..."
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "annoyed", "up")
            m "Deeper now."
            call her_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue", "narrow", "base", "up")
            m "Come on cum-whore."
            call her_main("*Slurp*! *Gobble*! *Gobble*!", "open_wide_tongue", "narrow", "worried", "down")
            m "Alright, [hermione_name], almost there."
            g4 "Deeper now!"
            call her_main("!!! *Gobble-goble-slurp-goble*! !!!", "open_wide_tongue", "narrow", "annoyed", "up")
            g4 "Yes, like that!"
            call her_main("{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}", "open_wide_tongue", "narrow", "annoyed", "up")
            g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
            g4 "*Ghr*!!!"
            g4 "Here it comes, [hermione_name]! Here's you reward!"
            call her_main("!!!", "open_wide_tongue", "narrow", "worried", "down")

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            call cum_block
            call bld
            g4 "{size=+7}ARGH!{/size}"
            g4 "Take my cum, slut!"
            call her_main("*Gulp!-Gulp!-Gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            g4 "Yes! Down your mouth you fucking cum dumpster!"
            call her_main("*Gulp-gulp-gulp-gulp-gulp*!", "open_wide_tongue_cum", "narrow", "annoyed", "up")

            stop music fadeout 1.0
            call her_chibi_scene("bj", trans=d5)
            call ctc

            call bld
            m "Well, I think that's it."
            m "You can let go now..."

            call her_chibi_scene("bj_pause", trans=d5)
            call her_main("...........................", "full_cum", "narrow", "base", "dead", tears="mascara", trans=fade)
            call her_main("................", "full_cum", "narrow", "base", "dead", tears="mascara")
            call her_main("........", "full_cum", "narrow", "base", "dead", tears="mascara")
            m "How was that?"
            call her_main("...", tears="mascara")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Are you going to swallow?"
            call her_main("*Shakes her head from side to side*", "full_cum", "narrow", "base", "dead", tears="mascara")

            if game.daytime:
                m "So you're going to go to class with a mouth full of my cum?"
            else:
                m "So you're going to go to sleep with a mouth full of my cum?"

            call her_main("*She nods her head up and down enthusiastically*", "full_cum", "narrow", "annoyed", "up", cheeks="blush", tears="mascara") #Smile.
            m "Good, like a proper slut should..."
            $ mouth_full_of_cum = True

    jump end_hg_pf_blowjob
