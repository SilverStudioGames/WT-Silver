
#hermione asks genie about who will be in-charge of the ball
label ball_quest_E1:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    call play_music("chipper_doodle")
    call her_main("[genie_name]?", "soft", "base", "base", "mid", xpos="right", ypos="base")
    m "Miss Granger, how can I help you?"
    call her_main("Sir, have you made your decision yet on who will be in charge of the \"ABOC\" this year?", "open", "base", "base", "mid")
    m "\"ABOC\"?"
    call her_main("The \"Autumn Ball Organization Committee\", sir...", "open", "closed", "base", "mid")
    m "*Ehm*... Sure..."
    call her_main("Please excuse me if I am being too direct with this, sir...", "normal", "squint", "angry", "mid")
    call her_main("But I think you should put {b}me{/b} in charge.", "open", "closed", "angry", "mid")
    call her_main("I did it last year and it was the best organised \"autumn ball\" Hogwarts has had in years.", "open", "closed", "base", "mid")
    call her_main("You said so yourself, sir. Do you remember?", "normal", "base", "base", "mid")
    m "Right, of course..."
    call her_main("So, is this a yes?", "base", "base", "base", "mid")
    call her_main("Does this mean I will be in charge again this year?", "base", "base", "base", "mid")

    menu:
        m "..."
        "\"You shall be in charge, miss Granger.\"":
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")

        "\"No. Professor Snape shall be in charge!\"":
            call her_main("Professor Snape, sir?", "open", "squint", "angry", "mid")
            call her_main("But, traditionally organizing and hosting the ball is the responsibility of the students...", "normal", "base", "angry", "mid")
            call her_main("Teachers are only present as the guests of honour...", "open", "closed", "angry", "mid")
            m "Of course...{w=0.4} I was just kidding."
            m "You shall be in charge, [hermione_name]..."

    m "There is one condition, though..."
    call her_main("Yes, [genie_name]?", "normal", "squint", "angry", "mid")

    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False # Masturbation flag

    label .choices:

    menu:
        m "..."
        "\"Take some of those clothes off\"":
            $ her_mood += 5
            $ d_flag_01 = True

        "\"You will have to sleep with me.\"" if not d_flag_02 and not hg_pf_sex.counter > 0:
            $ her_mood += 10
            $ d_flag_02 = True

            call her_main("I will have to... sleep...?", "angry", "wide", "base", "mid")
            call her_main("...................", "angry", "base", "angry", "mid", cheeks="blush")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("I am not stupid, sir... Quite the opposite in fact.", "angry", "closed", "angry", "mid", cheeks="blush")
            call her_main("And I understand that the nature of the favours I have been selling you lately...", "open", "base", "angry", "R", cheeks="blush")
            call her_main("... Might have led you to believe that I would be willing to...", "open", "squint", "angry", "mid", cheeks="blush")
            call her_main("... To let you have your way with me eventually, sir...", "disgust", "squint", "angry", "L_soft", cheeks="blush")
            m "Whaaa--? I would never--"
            call her_main("Please, let me finish, sir.", "scream", "base", "angry", "mid",emote="angry", cheeks="blush")
            m "Right..."
            call her_main("I know that you are a rather wise man yourself, sir.", "angry", "base", "angry", "mid", cheeks="blush")
            call her_main("So, please... understand this...", "disgust", "narrow", "base", "L_soft", cheeks="blush")
            call her_main("I may be willing to sacrifice my pride and even my dignity for the sake of my house...", "open", "closed", "angry", "mid", cheeks="blush")
            call her_main("But sleeping with my headmaster?", "open", "squint", "annoyed", "mid", cheeks="blush")
            call her_main("That is where I draw the line, sir.", "angry", "base", "angry", "mid", cheeks="blush")
            m "Fine... in that case..."

            jump ball_quest_E1.choices

        "\"Never mind. the Position is yours.\"":
            $ her_mood = 0

            call her_main("Really?", "smile", "base", "base", "mid")
            m "Yes."

            jump ball_quest_E1.end

    if d_flag_02:
        call her_main("Do I have to?", "annoyed", "base", "annoyed", "R", cheeks="blush")
        m "No [hermione_name]..."
        m "You don't have to take any clothes off..."
        call her_main("Finally you're being reasonable.", "open", "closed", "base", "mid")
        if hermione.is_worn("panties"):
            g9 "I only need you to pull those panties aside for easy access."
        else:
            g9 "I only need you to bend over my desk for easy access."
        call her_main("Sir! I thought I established this already... I'm not going to sleep with you!", "angry", "narrow", "angry", "mid", cheeks="blush")
        m "Then the answer is yes..."
        m "If you want to be in charge of My balls--"
        call her_main("The \"Autumn Ball\", sir...", "upset", "squint", "annoyed", "mid", cheeks="blush")
        call her_main("But this isn't a favour... this is THE Autumn Ball we're talking about...", "open", "squint", "angry", "mid")
        m "Then would you say the job of organizing it is... an honour?"
        call her_main("It is!", "open", "closed", "base", "mid")
        m "And you believe that you should be the one to do it?"
        call her_main("I do!", "open", "base", "base", "mid")
        m "Well then..."
        m "Show me what you're prepared to do for the privilege!"
    else:
        call her_main("What?!", "open", "base", "base", "mid")
        m "What?"
        call her_main("[genie_name]!", "angry", "base", "angry", "mid")
        m "What?"
        call her_main("You are abusing your power, sir. Again!", "disgust", "narrow", "base", "mid_soft")
        m "Seriously? After all those favours you sold me?"
        call her_main("Those were for the sake of my house, sir.", "annoyed", "narrow", "annoyed", "mid")
        m "Well this one is for the sake of the \"Autumn prom\"."
        call her_main("It's the \"Autumn Ball\", sir...", "upset", "closed", "base", "mid")
        m "Oh, come on..."
        m "Entrusting the thing to somebody else would be a crime, you know that."
        call her_main("..........", "annoyed", "narrow", "angry", "R")
        m "Don't you care about your classmates at all?"
        call her_main("What?", "open", "base", "base", "mid")
        m "Put your selfishness aside for once, would you?"
        call her_main("My... selfishness?", "annoyed", "base", "worried", "R")
        m "Your classmates deserve the best organised ball possible!"
        m "And only {size=+5}YOU{/size} can give them that!"
        call her_main("... that is true actually.", "angry", "narrow", "base", "down")
        m "People depend on you, girl!"
        call her_main("You... maybe you're right, [genie_name].", "open", "narrow", "worried", "down")
        call her_main("I must do this... Everyone depends on me.", "upset", "closed", "base", "mid")

    call her_main("Just give me a second please.", "annoyed", "narrow", "base", "R")
    hide screen hermione_main
    with d5

    m "............"

    call play_music("playful_tension") # SEX THEME.

    hide screen bld1
    hide screen hermione_main
    with d5

    #Walks to the door
    call her_walk("door", "base")

    #Locks the door
    pause.5
    call chibi_emote("thought","hermione")
    pause.5

    call chibi_emote("hide", "hermione")
    $ renpy.play('sounds/09_lock.wav')
    pause 1.5

    #Returns from the door
    m "......?"

    call her_walk("mid", "base")
    pause.2

    call her_main("Just in case...", "annoyed", "narrow", "angry", "R", cheeks="blush")

    $ d_flag_01 = False
    $ d_flag_02 = False

    m ".........................."
    call her_main("Okay then... what would you have me do?", "normal", "base", "worried", "mid")

    label .choices2:

    if d_flag_01 and d_flag_02:
        if hermione.is_any_worn("clothes"):
            m "Now take off everything else you're wearing."
            $ hermione.strip("all")

        jump ball_quest_E1.after_strip

    menu:
        m "..."
        "\"Take your top off.\"" if not d_flag_01:
            $ d_flag_01 = True

            call play_music("playful_tension") # SEX THEME.

            if not hermione.is_worn("top"):
                call her_main("Take off my what? I'm not exactly clothed, you know!", "angry", "base", "annoyed", "R")
                if not hermione.is_worn("bra"):
                    call her_main("Can't you see that my breasts are already on display?", "annoyed", "squint", "angry", "mid")
                    m "Right..."

                    jump ball_quest_E1.choices2
                else:
                    m "You are still wearing a bra, aren't you?"

                    jump ball_quest_E1.bra

            call her_main("............", "annoyed", "base", "worried", "R_soft", cheeks="blush")

            hide screen hermione_main
            with d5
            pause.3

            # TODO Animation doesn't work if this option is chosen second.
            # The standing chibi will reflect clothing state (once we have a topless chibi, that is)
            # call her_chibi("lift_top","mid","base")
            # with d3
            # pause 2.0
            $ hermione.strip("robe", "accessory")
            $ hermione.strip("top")

            show screen hermione_main
            with d5

            call ctc

            if hermione.is_worn("bra"):
                pause 2.0
                m "And your bra..."

                label .bra:

                call her_main("...", "annoyed", "base", "angry", "R_soft", cheeks="blush")
                $ hermione.strip("bra")
                pause.5

            call her_main("", "soft", "base", "base", "R_soft", cheeks="blush")
            call ctc

            m "Very good miss Granger..."
            m "Your ample tits are always a welcome sight..."
            call her_main("....................", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("", "normal", "base", "worried", "R_soft", cheeks="blush")

            jump ball_quest_E1.choices2

        "\"Take your bottoms off.\"" if not d_flag_02:
            $ d_flag_02 = True

            call play_music("playful_tension") # SEX THEME.
            $ hermione.strip("robe", "accessory")
            if not hermione.is_worn("bottom"):
                call her_main("I would if you'd let me wear any!", "angry", "base", "angry", "mid")
                if not hermione.is_worn("panties"):
                    call her_main("You have no idea how cold Hogwarts can be this time of year!", "annoyed", "base", "worried", "R")
                    m "......."

                    jump ball_quest_E1.choices2
                else:
                    g9 "You don't need any, in fact, you don't need your panties either!"
                    m "Take them off..."

                    jump ball_quest_E1.panties

            hide screen hermione_main
            with d5
            pause.3

            # TODO Animation doesn't work if this option is chosen second. Just use the standing chibi (ie. remove the commented code)
            # call her_chibi("lift_skirt","mid","base")
            # with d3
            # pause 2.0

            $ hermione.strip("bottom")

            show screen hermione_main
            with d5

            call ctc

            if hermione.is_worn("panties"):
                pause 2.0
                m "And your panties..."

                label .panties:

                call her_main("...", "normal", "base", "low", "R_soft", cheeks="blush")
                $ hermione.strip("panties")
                pause.5

            call her_main("", "annoyed", "base", "base", "R_soft", cheeks="blush")
            call ctc

            call her_main("..............................", "annoyed", "base", "angry", "R_soft", cheeks="blush")

            g4 "What are you doing, girl?!" with hpunch
            g4 "I am your headmaster! Do you have no shame?!"
            call her_main("What?! But--", "angry", "base", "angry", "mid", cheeks="blush")
            g9 "*He-he*... Relax, [hermione_name]. I'm just kidding."
            call her_main("[genie_name], that was just mean.", "scream", "happyCl", "angry", "mid", cheeks="blush")
            g9 "*He-he*..."
            call her_main(".....................................", "annoyed", "base", "worried", "R_soft", cheeks="blush")
            m "I do like your cute little pussy though..."
            call her_main("..... Thank you, sir.", "disgust", "base", "angry", "R_soft", cheeks="blush")

            jump ball_quest_E1.choices2

        "\"Never mind. The position is yours.\"" if d_flag_01 or d_flag_02:
            call her_main("Really?", "smile", "base", "base", "mid")

            jump ball_quest_E1.end

    label .after_strip:

    call her_chibi("stand")
    with d5
    pause 1.0

    g9 "Looking good [hermione_name]..."
    call her_main("Happy now?", "annoyed", "base", "worried", "R", cheeks="blush")
    call her_main("Will you let me have the \"privilege\" of being in charge of the \"ABOC\" this year?", "normal", "base", "worried", "mid")

    menu:
        "\"Of course... the Position is yours.\"":
            call her_main("Really?", "smile", "base", "base", "mid")

            jump ball_quest_E1.end

        "\"Touch yourself for me first...\"":
            $ hg_masturbated.triggered()
            $ d_flag_03 = True
            $ her_mood += 5

            call her_main("You want me to...", "shock", "wide", "base", "stare")
            m "Flick the bean..."
            m "Fondle those puppies..."
            call her_main("I...", "angry", "wide", "worried", "mid", cheeks="blush")
            m "Or did you not want to be in charge?"
            call her_main("Of... of course I do!", "angry", "base", "worried", "down", cheeks="blush")
            m "Then get on with it..."
            call her_main("...", "annoyed", "happyCl", "worried", "down", cheeks="blush")
            call her_main("Fine...", "disgust", "squint", "worried", "down", cheeks="blush")

            show screen blkfade
            with d5
            $ renpy.play("sounds/slick_02.mp3")
            with hpunch
            with kissiris
            $ hermione_xpos = 270
            $ hermione.set_pose("masturbate")
            $ hermione.set_body(armleft="on_pussy")
            call her_main("", "open", "squint", "worried", "mid")
            hide screen blkfade
            with d5

            pause 0.5

            call her_main("*Ah*...", "open", "squint", "worried", "R", cheeks="blush")
            g9 "Ni-i-i-ce!"
            play bg_sounds "sounds/slickloop.mp3" fadein 2
            call her_main("*mmmh*...", "open", "happyCl", "worried", "R", cheeks="blush")
            pause 0.4
            call her_main("", "soft", "closed", "base", "R", cheeks="blush")
            pause 0.4
            call ctc
            call her_main("*Sob*!", "soft", "squint", "worried", "R_soft", cheeks="blush", tears="soft")
            m "*huh*?"
            call her_main("Oh, please,{w=0.4} don't mind me, sir.", "open", "base", "base", "R", cheeks="blush", tears="crying")
            call her_main("Just enjoy the... {w=0.5}the view...", "upset", "happy", "base", "R", cheeks="blush", tears="soft")
            m "Are you... crying?"
            stop bg_sounds

            # Hand down
            $ hermione.set_body(armleft="down")

            call her_main("*Sob*! No, sir... *sob*!...", "angry", "happyCl", "worried", "mid", cheeks="blush", tears="crying_blink")
            call her_main("I... I enjoy touching myself...{w=0.5} In front of my headmaster *SOB*!", "angry", "squint", "worried", "R_soft", cheeks="blush", tears="crying")

            # Hands on pussy, tits
            $ hermione.set_body_zorder(armright=3)
            $ hermione.set_body(armleft="on_pussy", armright="on_tits")

            play bg_sounds "sounds/slickloop.mp3" fadein 2
            call her_main("*Ah*...", "open", "squint", "worried", "R", cheeks="blush")
            call her_main("These...{w=0.4} *Ah*...{w=0.5} are happy tears, sir.", "open", "narrow", "low", "R", cheeks="blush", tears="messy")
            call her_main("I...{w=0.5} *Ah*...{w=0.5}... I'm sorry...{w=0.5} I can't help it! *Sob*!", "angry", "happyCl", "worried", "mid_soft", cheeks="blush", tears="messy")
            m "Are you sure that you are okay with this?"
            call her_main("Yes...{w=0.4} *Ah*...{w=0.5} yes, sir, please.... *Sob*!", "soft", "squint", "worried", "mid", cheeks="blush", tears="messy")
            call her_main("Please keep looking as I...{w=0.3} pleasure myself *Sob*!", "open", "narrow", "base", "mid_soft", cheeks="blush", tears="messy")
            call her_main("", "open", "narrow", "angry", "stare_soft", cheeks="blush", tears="messy")
            pause.2

            g4 "(What the...?)"
            with hpunch
            call her_main("Sir, I am begging you!", "soft", "narrow", "angry", "mid", cheeks="blush", tears="messy")
            m "Kind of sounds like an order--"
            play bg_sounds "sounds/slickloopfast.mp3"
            call her_main("I need it!", "open", "narrow", "worried", "up_soft", cheeks="blush", tears="messy")
            call her_main("... I need to shamelessly present my naked body before you like this!", "soft", "narrow", "base", "up_soft", cheeks="blush", tears="messy")
            with hpunch
            m ".............?"
            call her_main("I need to feel this embarrassment and humiliation! *SOB*!", "silly", "narrow", "angry", "dead", cheeks="blush", tears="messy")
            play bg_sounds "sounds/slickloopveryfast.mp3"
            call her_main("The fate of the \"Autumn ball\" depends on this...", "silly", "base", "worried", "mid_soft", cheeks="blush", tears="messy")
            her "So, sir, please..."
            call her_main("Keep looking at my naked breasts, and my pussy...", "silly", "narrow", "worried", "mid", cheeks="blush", tears="messy")
            her "Look at me as I get wet for you..."
            call her_main("*mmmh*...", "open", "happyCl", "worried", "R", cheeks="blush", tears="messy") #disgusted #blushing
            call ctc


            with hpunch
            call her_main("*Ah*...{w=0.5} Yes! Make my skin burn with shame, sir... *Sob*!", "open", "narrow", "base", "up", cheeks="blush", tears="messy")
            m "*Ehm*... right... Okay..."
            m "Listen, I think this will do..."

            play bg_sounds "sounds/slickloop.mp3" fadein 2
            call her_main("*Ah*...{w=0.5} Are you sure, sir?", "open", "narrow", "base", "mid", cheeks="blush", tears="messy")
            call her_main("Are you sure that you've humiliated me enough, sir?", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="messy")
            m "...................."
            m "(Is she getting off on this or is she being sarcastic? I don't get it...)"
            call her_main("*mmmh*............", "open", "happyCl", "worried", "R", cheeks="blush", tears="messy")
            call ctc

            m "That's enough..."
            call her_main("", "annoyed", "base", "base", "mid", cheeks="blush", tears="messy")
            m "Just put your clothes back on, Miss Granger. You're making me feel uncomfortable."
            stop bg_sounds fadeout 4
            her "..."

            # Reset pose
            $ hermione.set_body_zorder(armright=0)
            $ hermione.set_body(armleft="down", armright="down")
            $ hermione.set_pose(None)

            call her_main("As you wish, sir...", "annoyed", "narrow", "angry", "R", cheeks="blush", tears="messy")

            stop music fadeout 3.0

    label .end:

    show screen blkfade
    with d5
    call her_chibi("stand","mid","base")
    call her_main("", "base", "happyCl", "base", "mid", xpos="right", ypos="base")
    $ hermione.wear("all")
    pause 2.0
    hide screen blkfade
    with d5

    call play_music("chipper_doodle")

    call her_main("So... does this mean I'm officially in charge of this year's \"Autumn Ball Organization Committee\" now?", "base", "happyCl", "base", "mid", xpos="right", ypos="base")
    m "That you are."
    her "Thank you sir! You will not regret this, I promise!"
    if d_flag_03:
        call blktone
        m "(That was weird... she sure changed her mood quick.)"
        m "(Maybe she gets off on being humiliated...)"
        m "(Guess I'll have to find out.)"
        call hide_blktone
    else:
        call blktone
        m "{size=-4}(Why would I?){/size}"
        m "{size=-4}(I couldn't care less about the whole thing...){/size}"
        call hide_blktone
    call her_main("Well, I'd better go now. I have so many arrangements to make!", "grin", "base", "base", "R")
    m "By all means, Miss Granger. Have a nice day."

    call her_walk(action="leave")
    pause.5

    call bld
    m "........................................"
    m "A ball, *huh*?"
    m "I wonder if I will have to show up for that..."

    $ ball_quest.E1_complete = True

    $ hermione_busy = True
    $ ss_event_pause += 2 # Next event happens in 2 days.

    jump main_room


#Snape confronts genie about his ABOC decision

label ball_quest_E2:
    stop music fadeout 1.0

    call sna_walk(action="enter", xpos="mid", ypos="base")
    pause.2

    call play_music("snape")
    call sna_main("Are you bloody insane?!","snape_01", xpos="base", ypos="base")
    m "You know, sometimes I think I may be..."

    call sna_main("You appointed {b}that{/b} girl as the head of the \"Autumn Ball Organization Committee\"?!!","snape_01")
    m "I'm guessing that's bad?"
    call sna_main("Bad?{w} {size=+5}BAD?!{/size}","snape_10")
    call sna_main("{size=+5}That's a catastrophe!{/size}","snape_15")
    call sna_main("last year's ball was completely horrible!","snape_16")
    m "Was it? I heard differently..."
    call sna_main("Oh really? And who told you that?","snape_10")
    m "not a very reliable source apparently..."
    call sna_main("Dammit... Dammit all to hell...","snape_08")
    call sna_main("I had big plans for the thing...","snape_07")
    m "Really? Like what?"
    call sna_main("Oh, that doesn't matter now...","snape_06")
    #sna "The girl is a complete control freak..."
    sna "Now the girl will use the prefects or the ghosts to keep an eye on me throughout entire thing..."
    m "Right, that reminds me..."
    m "Am I supposed to show up as well?"
    call sna_main("Show up?","snape_03")
    sna "You are expected to host the bloody thing!"
    call sna_main("But don't you worry! I'll figure something out!","snape_09")
    call sna_main("*Hmm*... I'll Probably have to host the ball instead...","snape_06")
    m "............"
    call sna_main("Well, the Autumn ball is about to happen and Hermione Granger is in charge...","snape_09")
    sna "There is no changing it now..."
    call sna_main("Sorry for the outburst...","snape_05")
    call sna_main("That girl brings out the worst in me...","snape_16")
    m "Don't sweat it..."
    call sna_main("You know what...?","snape_06")
    sna "I don't feel like working today..."
    call sna_main("Do we still have any of Dumbledore's wine left?","snape_05")
    m "I believe so..."
    call sna_main("Great! Pour me some...","snape_02")
    m "Seriously? You're just gonna bail on your class like that?"
    call sna_main("Yeah, big news -- I hate my job.","snape_03")
    sna "And since you are my boss..."
    call sna_main("I don't know why I even bother teaching those so-called students...","snape_06")
    m "To maintain the charade?"
    m "for the Same reason why I never leave this room...?"
    call sna_main("Right...","snape_05")
    sna "But you know what else could endanger our little enterprise?"
    call sna_main("Me losing it during class and strangling a couple of Gryffindor maggots with my bare hands...","snape_07")
    m "*Hmm*... I see your point..."
    call sna_main("Seriously, man... I need a drink...","snape_06")

    hide screen snape_main
    call blkfade

    call gen_chibi("hide")
    show screen with_snape(ani=False)
    hide screen chair_right

    $ fire_in_fireplace = True
    $ fireplace_OBJ.foreground = "fireplace_fire"
    call sna_chibi("hide")
    hide screen bld1
    call hide_blkfade

    call bld
    call nar(">Professor Snape spends the day in your chamber, drinking the stress away.")

    if sna_friendship < 100:
        call nar(">Your relationship with him has improved.")
        $ sna_friendship +=1

    $ ss_event_pause += 2
    $ hg_event_pause += 1

    $ ball_quest.E2_complete = True

    jump night_start


label ball_quest_E3:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    call play_music("chipper_doodle")
    call her_main("My parents sent me the wrong dress!", "angry", "base", "base", "mid", tears="soft", xpos="right", ypos="base")
    m "are You kidding me!?"
    call her_main("They sent me the dress I wore to the ball last year...", "angry", "base", "base", "mid", tears="soft")
    m "Those inconsiderate bastards!"
    call her_main("Are you making fun of me sir?", "mad", "base", "worried", "mid", tears="soft")
    m "Can you blame me?"
    call her_main("I will become the laughingstock of Hogwarts! *Sob*!", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("My reputation is as good as ruined! *Sob*!", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    m "Seriously? After all the favours you sold me you care about a thing like this?"
    call her_main("Wearing the same dress to the \"Autumn Ball\" for two years in a row would be more humiliating than any favour I sold you so far, sir.", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    with hpunch
    g4 "You've gotta be kidding me..."
    call her_main("Oh, you wouldn't understand...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    call her_main("You're just like my father!", "scream", "base", "angry", "mid", cheeks="blush", tears="messy")
    m "I beg your pardon?"
    call her_main("I mean... *Ehm*...", "open", "wide", "worried", "stare", cheeks="blush", tears="messy")
    her "Forgive me sir..."
    call her_main("I don't know why I am telling you all of this...", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    m "................"
    call her_main("......................*sob*!", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    call her_main("I think I'd better go now...*sob*", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    m "Well, don't let me keep you a moment longer, miss Granger..."

    call her_walk("door", "base")
    pause.3

    call her_main("(My life is ruined...)", "angry", "squint", "base", "mid", cheeks="blush", tears="messy", ypos="head", flip=False)
    pause.1

    call her_chibi("leave")

    call bld
    m "*Hmm*... I don't remember ever seeing the girl this desperate..."
    m "And that says a lot, all things considered..."
    m "I suppose Whoring herself out for house points is a significantly smaller problem than not having a proper prom dress..."
    m ".............."
    m "Schoolgirls..."

    $ hermione_busy = True
    $ hg_event_pause += 1

    $ ball_quest.E3_complete = True

    jump main_room


label ball_quest_E4:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    call play_music("chipper_doodle")
    call bld
    m "Miss Granger?"
    call her_main("Sorry to disturb you sir...", "open", "base", "worried", "mid", xpos="right", ypos="base")
    call her_main("I came to apologise for my...", "open", "base", "worried", "R")
    her "... my hysterical behaviour yesterday."
    m "Sure thing, don't worry about it."
    call her_main("Thank you, sir.", "open", "base", "base", "mid")
    call her_main("Still, I cannot help but feel awful for causing a scene...", "open", "closed", "angry", "mid")
    m "So the issue has been resolved then?"
    call her_main("Not really...", "open", "base", "worried", "mid")
    call her_main("Not at all actually...", "annoyed", "narrow", "angry", "R")
    m "*Hmm*...?"
    call her_main("But that is not a big deal...", "annoyed", "narrow", "worried", "down")
    her "I'm just overreacting..."

    call play_music("despair")
    call her_main("I won't be able to attend the ball this year... so what?", "annoyed", "narrow", "worried", "down")
    call her_main("I spent countless hours organising the event...", "normal", "happyCl", "worried", "mid")
    call her_main("I worked so hard... and...", "open", "base", "worried", "mid", tears="soft")
    call her_main("And now I will not even be able to... to... *Sob*!", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    call her_main("To... *SOB*!", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    call her_main("Excuse me sir!", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    hide screen hermione_main
    hide screen bld1
    with d3
    call gen_chibi("sit_behind_desk")
    with d1

    call her_walk(action="run", xpos="door", speed=2, reduce=True)
    call her_chibi("leave")

    call bld
    m "......................................."
    m "*Hmm*..."

    $ hermione_busy = True
    $ hg_event_pause += 1

    $ ball_quest.E4_complete = True

    jump main_room


label ball_quest_E5:
    hide screen hermione_main
    with d5

    stop music fadeout 1.0
    m "Here... This is for you..."

    call give_reward(">You give the ball gown to Hermione...","interface/icons/box_red_1.webp")

    call her_main("*Hmm*...? What is this?", "base", "base", "base", "mid")
    call her_main("{size=+7}A DRESS?!{/size}", "angry", "wide", "base", "stare")
    with hpunch
    m "I thought that you--"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]!", "angry", "base", "base", "mid", tears="soft")
    g4 "What? What happened? Don't tell me it's the wrong colour or something!"
    call her_main("It's perfect, sir...*sob*!", "angry", "base", "base", "mid", tears="soft")
    her "It's perfect... *sob*!... I love it."
    m "You sure don't look like it..."
    her "I am sorry, sir... *Sob*!"
    call her_main("I... I am just...", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("I am so happy...", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    her "Thank you, sir. Thank you so much."
    call her_main("I cannot believe that you would do something like that for me...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    m "Well, I did. Now stop crying."
    call her_main("I can't, sir. I am so happy and so grateful...", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
    call her_main("Do you want me to suck your cock, sir?", "open", "wide", "worried", "stare", cheeks="blush", tears="messy")
    m "What?"
    call her_main("Because I will do it!", "open", "wide", "worried", "stare", cheeks="blush", tears="messy")
    her "And I will swallow and everything!"
    call her_main("And you wouldn't have to pay me a single house point!", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    m "*Uhm*... Maybe some other time..."
    m "This is not the type of crying I find arousing..."
    call her_main("I'm sorry, sir. I'm such a mess...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    call her_main("But this is so unexpected...", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    her "You made me so happy, sir... *sob*!"
    call her_main("Thank you sir! *SOB*! Thank you! *SOB*!", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    m "Well... err... there, there..."
    m "Better stop crying before you stain that new dress of yours with those tears..."
    call her_main("My new dress! *SOB*!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
    m "Alright, you know what? Just get out of my office."
    m "Just take your dress and leave."
    call her_main("Of course... I am sorry, sir!", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand","mid","base")
    pause.3
    call her_chibi("stand","mid","base",flip=True)
    pause.2

    call her_walk(action="leave")

    call bld
    m "......................"
    m "Women..."

    $ hg_event_pause += 2

    $ ball_quest.gave_dress = True

    jump main_room
