

### Tier 3 ###

# Invite Snape

label hg_pf_strip_T3_snape: # Fails
    hide screen blktone
    hide screen hermione_main
    with d3

    m "[hermione_name], before you start I have one more favour to ask of you."

    call her_main("Of course, [genie_name].", "open", "closed", "base", "mid", xpos="base", ypos="base")
    m "Do you think you could go and fetch professor Snape for me?"
    call her_main("... Professor Snape?", "annoyed", "squint", "base", "mid")
    her "May I ask, why, [genie_name]?"
    m "Oh, I just think you could use a bigger audience for your striptease performance."
    call her_main("My striptease performance...?!!", "shock", "wide", "base", "stare")
    call her_main("Are you completely out of your mind, [genie_name]?", "angry", "base", "angry", "mid")
    call her_main("Wasn't it enough that I've had to embarrass myself in front my teacher once before?", "open", "base", "angry", "mid")
    call her_main("And now you expect me to do it again... but willingly?!", "scream", "closed", "angry", "mid")
    m "Short answer... yes."
    call her_main("I'm leaving!", "angry", "base", "angry", "mid")

    call her_walk(action="leave")

    $ her_mood += 15
    $ hg_pf_strip.fail()

    jump end_hermione_event



### Tier 4 ###

# Invite Snape

label hg_pf_strip_T4_snape:
    if hg_strip.ss_counter == 0:
        $ hg_strip.ss_counter += 1

        hide screen blktone
        hide screen hermione_main
        with d3

        m "[hermione_name], before you start I have one more favour to ask of you."

        call her_main("Of course, [genie_name].", "open", "closed", "base", "mid", xpos="base", ypos="base")
        m "Do you think you could go and fetch professor Snape for me?"
        call her_main("... Professor Snape?", "annoyed", "squint", "base", "mid")
        her "May I ask, why, [genie_name]?"
        m "Oh, I just think you could use a bigger audience for your striptease performance."
        call her_main("My striptease performance...?!!", "shock", "wide", "base", "stare")
        call her_main("With all due respect, [genie_name]...", "angry", "base", "angry", "mid")
        call her_main("{size=-5}(Which I have oh so little left for you...){/size}", "normal", "squint", "angry", "mid")
        call her_main("I refuse to degrade myself for professor Snape's amusement!", "scream", "closed", "angry", "mid")
        m "No, no, you got it all wrong, [hermione_name]."
        call her_main("*Hmm*...?", "soft", "base", "base", "mid")
        m "I want to prove that professor Snape is dirty, and I need your help."
        call her_main("!!!", "shock", "wide", "base", "stare")
        m "Yes, I want to catch him in the act!"
        call her_main("[genie_name], I didn't realise...", "open", "base", "worried", "mid")
        call her_main("I see now...", "base", "base", "base", "mid")
        her "I am sorry for doubting you [genie_name]..."
        m "No biggie. Now go find professor Snape and bring him here."
        call her_main("Right away [genie_name]!", "smile", "base", "angry", "mid")

    else:
        hide screen blktone
        hide screen hermione_main
        with d3

        m "[hermione_name], before you start I have one more favour to ask of you."

        call her_main("Of course, [genie_name].", "open", "closed", "base", "mid", xpos="base", ypos="base")
        m "Do you think you could go and fetch professor Snape again?"
        call her_main("... professor Snape?", "annoyed", "squint", "base", "mid")
        her "may I ask, why, [genie_name]?"
        m "Oh, I just want you to dance for us."
        call her_main("!!!", "open", "base", "base", "mid")
        m "I want to prove that professor Snape is dirty, and I need your help."
        call her_main("But didn't we already establish that last time I did this?", "annoyed", "base", "worried", "R")
        m "Well, *Ehm*... sure..."
        m "But I will need more proof if I am to take this issue to the ministry of magic!"
        call her_main(".....", "angry", "base", "angry", "mid")
        m "So, what do you say [hermione_name]?"
        m "One more dance for the greater good?"
        call her_main("Well, alright...", "disgust", "narrow", "base", "mid_soft")
        m "Good. Go find professor Snape then."

    call her_walk(action="leave")

    show screen blkfade
    with d5

    stop music fadeout 1.0
    pause 2
    ">Hermione returns with Snape a few moments later."

    call play_sound("door")
    call her_chibi("stand","desk","base")
    call sna_chibi("stand","mid","base")
    hide screen blkfade
    with d5
    pause.5

    call play_music("dark_fog")
    call sna_main("Genie... err, I mean Albus, you wanted to see me?","snape_01", xpos="base", ypos="base")
    m "Yes. Are you in the mood for a little striptease?"
    call sna_main("Oh...?","snape_05")
    sna "Miss Granger here will be performing I assume?"
    call her_main("..............", "angry", "happyCl", "worried", "mid", emote="sweat", xpos="mid", ypos="base")
    m "Yes, our little minx is more than happy to take off her clothes for our entertainment."
    call her_main("............", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Aren't you [hermione_name]?"
    pause.5

    call her_main(None, "angry", "happy", "worried", "R")
    pause 1

    call her_main(None, "angry", "happy", "worried", "mid")
    pause 1.5

    show screen snape_main
    call her_main("Yes, [genie_name].", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Let's get started then!"
    hide screen hermione_main
    with d3
    pause.2
    call sna_main("","snape_13")
    pause.8

    $ hermione.strip("robe", "accessory")
    hide screen snape_main
    show screen blkfade
    with d5

    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
    pause 3
    call her_chibi("dance","on_desk","on_desk")
    call sna_chibi("stand","desk_close","desk_close")

    # call her_main(animation=bob)
    call her_main(".............", "open", "closed", "base", "mid", ypos="head", flip=False)
    call sna_main("......................","snape_05")
    m ".........................."

    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    call bld
    m "So... Severus... How's life?"
    call sna_main("Well, you know... same old, same old...","snape_09")
    call sna_main(" The Students are causing me grief...","snape_06")
    call sna_main("In fact, miss Granger here managed to cause me more stress than any other student...","snape_03")
    pause.2
    call her_main("...............................", "grin", "base", "base", "R", xpos="mid", ypos="base")
    m "Oh, I am sure she is very sorry about that..."
    call her_main("{size=-4}(Not even a little bit!){/size}", "base", "happyCl", "base", "mid")
    m "And will make up for it today, won't you, [hermione_name]?"
    pause.2

    call her_main("*Ehm*... Yes, [genie_name].", "base", "happy", "base", "mid")
    pause.2

    call nar(">Hermione starts to sway her hips seductively.")

    if hermione.is_worn("top"):
        call nar(">Hermione reaches to take off her top...")
        $ hermione.strip("top")

    call ctc

    call her_main("...................", "open", "narrow", "worried", "down")
    call sna_main("*Hmm*... You are being suspiciously quiet, Miss Granger.","snape_05")
    call her_main("{size=-4}(Oh no! Is he onto us?){/size}", "shock", "wide", "base", "stare")
    call her_main("I'm just doing what the headmaster told me to, Professor Snape...", "grin", "happyCl", "worried", "mid", emote="sweat")
    call sna_main("Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day during classes?","snape_03")
    m "Severus..."
    call sna_main("No Albus, I want to hear what little miss perfect has to say.","snape_03")
    call her_main("I just want you to have a good time, Professor Snape...", "grin", "happyCl", "worried", "mid", emote="sweat")
    call sna_main("Oh! It's \"Professor Snape\" now, is it?","snape_03")
    call sna_main("What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!","snape_10")
    g9 "{size=-5}({i}snape'o'doodle{/i}, heh... that's funny.){/size}"
    call her_main(".............", "grin", "happyCl", "worried", "mid", emote="sweat")
    call sna_main("Yes, I know what you are calling me behind my back, you wretched girl!","snape_08")
    call her_main("Well, maybe that's because you deserve it... {i}Snivellus!{/i}", "scream", "base", "angry", "mid", emote="angry")
    call sna_main("{size=+2}What did you just say?!{/size}","snape_10")
    call sna_main("How dare you....?")
    call sna_main("Who do you think you are? You filthy mudbl--","snape_15")
    call her_main("[genie_name], one of your staff members is verbally abusing me!", "scream", "closed", "angry", "mid")
    call her_main("Are you going to allow this?")
    call sna_main("Verbally abusing...?! You have some nerve, girl!","snape_08")
    call sna_main("Albus, will you allow her to talk back to a teacher like that?","snape_10")
    call her_main("[genie_name]!", "scream", "closed", "angry", "mid")
    call sna_main("Albus!","snape_10")

    menu:
        m "..."
        "\"[hermione_name], show some respect!\"":
            $ her_mood += 9
            call her_main("What?", "annoyed", "base", "angry", "mid")
            call her_main("But [genie_name]!")
            m "[hermione_name], you {size=+4}will{/size} calm down now."
            call her_main("*Tsk*!", "disgust", "narrow", "base", "mid_soft")
            if hermione.is_worn("bottom"):
                m "And take off your bottoms already, would you?"
                call her_main(".......", "annoyed", "narrow", "angry", "R")
            call sna_main("...........","snape_13")

        "\"Severus, you started this.\"":
            $ sna_friendship -= 5
            call sna_main("What? Me?!","snape_10")
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call sna_main("Albus, you are spoiling the girl! She must be taught a lesson!","snape_08")
            m "............... Severus."
            g4 "Did you hit your head?!"
            call sna_main("I beg your pardon?","snape_03")
            g4 "The girl is already stripping for you!"
            g4 "What punishment are you talking about?"
            call sna_main("*Tsk*... How about a flogging?","snape_16")
            g4 "Severus!"
            call sna_main("Alright, alright, I see your point...","snape_17")
            m "[hermione_name], are you going to strip or are you going to climb on my desk to give us a better view?"
            call her_main("*Ehm*...", "open", "narrow", "worried", "down")
            if hermione.is_worn("bottom"):
                m "Take of your bottoms, [hermione_name]!"
                call her_main("Yes, [genie_name]...", "soft", "base", "base", "mid")

        "\"Both of you, calm the fuck down.\"":
            m "You, tall-dark-and-handsome, calm down a bit, would you?"
            call sna_main("I beg your pardon?","snape_03")
            call her_main("Yes! You tell him profess--", "annoyed", "narrow", "angry", "R")
            m "You as well, you perverted little minx!"
            if hermione.is_worn("bottom"):
                m "Calm down and take your bottoms off already."
            else:
                m "Calm down and keep doing what you were paid to do!"
            call her_main("I am not perverted...", "annoyed", "narrow", "annoyed", "mid")
            if hermione.is_worn("bottom"):
                m "Your bottoms, [hermione_name]!"
                call her_main("......", "annoyed", "narrow", "angry", "R")
            call sna_main(".............","snape_13")

        "-Unleash your rage {size=-2}(Hardcore){/size}-" if game_difficulty >= 3: #Hardcore difficulty dialogue.
            $ her_mood += 18
            $ sna_friendship -= 10
            m "Both of you..."
            stop music
            with hpunch
            g4 "Shut the fuck up!!!"
            g4 "You!... You good for nothing, ugly-faced, crooked-nosed-wannabe-wizard!"
            with hpunch
            call sna_main("(...)","snape_11")
            call her_main("(... yikes!)", "angry", "wink", "base", "mid")
            call sna_main("(What did he just say to me?!)","snape_08")
            g4 "Shut your stupid mouth or I will send you flying out that bloody window!"
            g4 "That bitch is already stripping for you, so what more do you want?!"
            call her_main("That B-Bitc--", "shock", "wide", "base", "stare")
            g4 "And you... stripper-whore!"
            g4 "Do what you are paid for and start stripping already!!!"
            call her_main("......", "angry", "closed", "angry", "mid", emote="angry")
            call sna_main(".............","snape_05")
            call her_main("...", "mad", "squint", "angry", "mid")

    pause.5

    if hermione.is_worn("bottom"):
        call nar(">Hermione swiftly takes off her bottoms, showing off her muggle-born ass.")
        $ hermione.strip("bottom")
        call ctc

        sna "*Hmm*..."
        call her_main("........................", "open", "narrow", "worried", "down")
        m "Yes, much better!"

    if hermione.is_worn("bra") and hermione.is_worn("panties"):
        call nar(">Hermione keeps on dancing, now wearing nothing but her underwear.")
    elif hermione.is_worn("bra"):
        call nar(">Hermione keeps on dancing, now wearing nothing but her bra.")
    elif hermione.is_worn("panties"):
        call nar(">Hermione keeps on dancing, now wearing nothing but her panties.")

    menu:
        m "..."
        "\"Severus, what about that Potter boy?\"":
            call her_main("(.....?)", "soft", "base", "base", "mid")
            call sna_main("What about him?","snape_09")
            m "Is he still causing you grief?"
            call sna_main("Oh...","snape_09")
            call sna_main("Not really, no...")
            call sna_main("To be honest I never really had a problem with the boy himself...","snape_06")
            sna "Although I did plan to make his life here miserable because of his father..."
            call sna_main("But lately I have way more interesting projects to occupy myself with...","snape_02")
            call her_main("...................", "soft", "base", "base", "mid")

        "\"Severus, what about the Weasels?\"":
            call sna_main("Weasels?","snape_05")
            call sna_main("Oh you mean Weasley's...","snape_09")
            call sna_main("What about them?","snape_09")
            m "Are they still causing you trouble?"
            call sna_main("Yes... More than ever.","snape_09")
            m "*Hmm*...?"
            m "You seem surprisingly indifferent about that..."
            call sna_main("That's because I know that they will get what they deserve eventually...","snape_05")
            m "Revenge? Cool! What do you have in mind?"
            call her_main("!!!", "soft", "base", "base", "mid")
            call sna_main("*Hmm*... Can't discuss this with \"the enemy\" present.","snape_06")
            call her_main("*Tsk*!", "annoyed", "narrow", "angry", "R")
            call sna_main("All I can say is that it involves their beloved little sister Ginny...","snape_13")
            m "Ginny? *Hmm*... What a curious name for a girl..."
            m "............."
            m "So, you plan to fuck her then?"
            call sna_main("!!?","snape_08")
            call sna_main("Albus, please, not in front of the girl!","snape_17")
            m "Alright, alright..."
            call her_main("{size=-5}(Ginny...){/size}", "open", "narrow", "worried", "down")

        "\"How would you grade Hermione's butt?\"":
            call sna_main("miss Granger's buttocks?","snape_05")
            call her_main("!!!............", "annoyed", "narrow", "angry", "R")
            m "Yes! As you would grade a paper."
            call sna_main("*Hmm*...","snape_13")
            pause.1
            call nar(">Professor Snape gives Hermione's buttocks an appraising look...")
            call her_main(".........?", "upset", "wink", "base", "mid")
            call sna_main("I would say...","snape_13")
            call her_main("............?!", "base", "narrow", "worried", "down")
            call sna_main("Yes... \"Dreadful.\"","snape_09")
            call her_main("(What?!)", "shock", "wide", "base", "stare")
            call sna_main("Unsatisfactory...","snape_09")
            sna "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
            call her_main("!!!!!!!!!!", "angry", "narrow", "annoyed", "mid", emote="angry")

    if hermione.is_worn("bra"):
        m "Why don't you take off your bra now, [hermione_name]?"
        call her_main(".............", "open", "narrow", "worried", "down")
        call nar(">Hermione undoes her bra and then slowly takes it off.")
        pause .5
        $ hermione.strip("bra")

        call ctc
    else:
        call nar(">Hermione cups her breasts playfully, squeezing them in the process.")

    m "Alright! We Finally get to the good stuff!"
    call sna_main("*Hmm*...","snape_13")
    call her_main("........", "annoyed", "closed", "base", "mid")

    menu:
        m "..."
        "-Start jerking off-":
            jump hg_pf_strip_T4_snape_masturbate

        "-Just keep on watching-":
            jump hg_pf_strip_T4_snape_watch

label hg_pf_strip_T4_snape_watch:
    call play_music("dark_fog")

    call her_main("I will just keep on dancing then...", "open", "closed", "base", "mid")

    # call her_main(animation=bob)
    call her_chibi("dance","on_desk","on_desk")
    call ctc

    call nar(">Hermione squeezes her breasts and shakes her hips slightly...")

    m "Yes, [hermione_name]. Very good."
    call sna_main("*Ahem*! Acceptable performance, miss Granger.","snape_12")
    call her_main("....", "open", "closed", "base", "mid")
    m "Heh..."
    m "So... how would you grade her tits?"
    call her_main("......", "annoyed", "closed", "base", "mid")
    call sna_main("*Hmm*......","snape_20")
    call her_main("........", "annoyed", "closed", "base", "mid")
    call sna_main("\"B+\"!","snape_12")
    call her_main("!!!", "open", "wide", "base", "stare")
    m "Really?"
    call sna_main("Yes. I do give credit where it's due.","snape_12")
    call her_main("(Professor...)", "angry", "wide", "base", "stare")
    call her_main("(Time for my finishing act then!)", "open", "closed", "base", "mid")
    pause.1

    if hermione.is_worn("panties"):
        call nar(">Hermione bends over and slides her panties down.","start")
        ">Her movements lack grace..."
        call nar(">But a pretty pussy is always a welcome sight nonetheless...","end")
        pause.5

        $ hermione.strip("panties")

        call ctc

        call sna_main("Yes... Yes...","snape_20")
    sna "Now shake those B+ titties for me, you harlot!"
    call her_main(".......", "angry", "happyCl", "worried", "mid")

    pause.5

    call nar(">All of a sudden Hermione breaks into a series of rather complex pirouettes.")
    call sna_main("Yes, such grace...","snape_19")
    call sna_main("That lithe, flexible body!","snape_20")
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "open", "closed", "base", "mid")
    call nar(">Hermione seems very focused on her dancing routine.")
    call sna_main("Yes, and now another pirouette!","snape_19")
    call sna_main("Magnificent!")
    show screen blkfade
    with d5

    ">Hermione performs another set of movements and pirouettes..."
    ">Gives a little curtsy bow to the imaginary audience..."
    ">And then exhaustedly slumps down on her butt."

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    show screen bld1
    call sna_main("Good job, you harlot!","snape_22")
    call her_main(".............", "soft", "happy", "base", "R", animation=None)

    if daytime:
        call sna_main("Well, my class is about to start so I will be leaving now.","snape_22")
        sna "Don't you have potion class with me today, Miss Granger?"
        call her_main("Yes, [genie_name]...", "annoyed", "narrow", "base", "dead")
        call sna_main("Well, don't be late, girl...","snape_22")
        call sna_main("Albus...","snape_02")
        g9 "See you soon, Severus."
    else:
        call sna_main("Well, it is getting rather late. I think I will be leaving now.","snape_22")
        sna "Good night, Albus."
        m "Severus."
        call sna_main("Harlot.","snape_22")
        call her_main("Professor...", "annoyed", "narrow", "base", "dead")

    call ctc

    call hide_characters
    show screen blkfade
    with d5

    ">Professor Snape leaves..."
    stop music fadeout 1.0
    call her_main("....................", "annoyed", "narrow", "base", "dead", ypos="head", flip=False)
    pause.5

    call her_main("May I... may I get paid now... [genie_name]...?", "normal", "happyCl", "worried", "mid")

    jump end_hg_pf_strip

label hg_pf_strip_T4_snape_masturbate:
    call play_music("playful_tension")
    pause.2

    call hide_characters
    show screen blkfade
    with d5
    pause.2

    call her_main("[genie_name]?!", "open", "wide", "base", "stare", ypos="head", flip=False)
    m "It's alright, [hermione_name]. Don't mind me..."
    call sna_main("Oh, we're doing it like this then?","snape_12", ypos="head")
    call sna_main("Well, don't mind if I do...","snape_12")
    call her_main("!!!", animation=None)

    show screen chair_left
    call gen_chibi("jerk_off","behind_desk","base")
    show screen desk
    call her_chibi("dance_pause","on_desk","on_desk")
    call sna_chibi("jerk_off","desk_close", "desk_close")
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("No, guys... *Err*... I mean, sirs! *Ehm*... professors!", "angry", "wide", "base", "stare", xpos="mid", ypos="base")
    m "Don't you mind us [hermione_name], just keep on doing your thing."
    call her_main("But...")
    call her_main("No! I refuse to dance with those things pointed at me!", "angry", "happyCl", "worried", "mid")
    call her_main("You need to put them away or the dance is over!")
    m "You aren't in any position to give us orders, [hermione_name]."
    call her_main("that was not an order, [genie_name]. It was an ultimatum.", "clench", "base", "angry", "mid", emote="angry")

    menu:
        m "..."
        "\"Alright Severus, let's be civil...\"":
            hide screen hermione_main
            with d3
            pause.2
            call sna_main("I see Miss Granger manages to remain exceptionally stubborn in any situation...","snape_03")
            call hide_characters
            hide screen bld1
            with d5

            call gen_chibi("sit_behind_desk")
            call sna_chibi("stand","desk","base")
            with fade
            pause.3

            jump hg_pf_strip_T4_snape_watch

        "\"(Psst, Hermione! Remember why we are doing this!)\"":
            pass


    if her_tier < 5: # Hermione is NOT ok with it.
        call her_main("Oh...", "open", "wide", "base", "stare")
        call her_main("No, I can't! This is just not worth it!", "angry", "happyCl", "worried", "mid")
        call hide_characters
        show screen blkfade
        with d5

        $ hermione.wear("all")
        ">Hermione jumps off the desk and starts to put her clothes back on."
        call sna_main("Well, this was awfully anticlimactic...","snape_03")
        g4 "You don't say..."
        call sna_main("May as well leave now I suppose. I will talk to you later, Albus.","snape_03")
        m "Yes, later, Severus."
        call sna_main("Miss Granger...","snape_04")
        call her_main("Professor...", "angry", "happyCl", "worried", "mid", ypos="head", flip=False)

        call sna_chibi("hide")
        call her_chibi("stand","desk","base")
        call play_sound("door")
        ">Professor Snape leaves."
        stop music fadeout 1.0
        hide screen blkfade
        with d5

        call her_main("....................", "annoyed", "narrow", "base", "dead", xpos="mid", ypos="base")
        call ctc

        call her_main("... Can I get paid now... [genie_name]...?", "normal", "happyCl", "worried", "mid")

        jump end_hg_pf_strip


    else: # Hermione IS ok with it.
        call her_main("Oh, right...", "shock", "wide", "base", "stare")
        call sna_main("What was that?","snape_05")
        call her_main("Please don't mind what I just said...", "silly", "happyCl", "worried", "mid", emote="sweat")
        call sna_main("*Hmm*...?","snape_05")
        call her_main("I do not mind you touching yourself in front of me...", "silly", "happyCl", "worried", "mid", emote="sweat")
        call her_main("Yes, I do not mind it at all...")
        call her_main("I will just keep on dancing then...")

        call her_chibi("dance","on_desk","on_desk")
        # call her_main(animation=bob)

        call nar(">You keep on jerking off while you're watching Hermione dance.","start")
        call nar(">Hermione squeezes her breasts and shakes her hips slightly.","end")

        m "Yes, [hermione_name]. Very good."
        call sna_main("*Khem*! Acceptable performance, miss Granger.","snape_12")
        call her_main("....................", "angry", "happyCl", "worried", "mid")
        m "Heh..."
        m "So, how would you grade her tits?"
        call her_main("......", "open", "wide", "base", "stare")
        call sna_main("*Hmm*......","snape_13")
        call her_main("........", "annoyed", "narrow", "angry", "R")
        call sna_main("\"B+\"!","snape_12")
        call her_main("!!!", "open", "wide", "base", "stare")
        m "Really?"
        call sna_main("Yes. I do give credit where credit is due.","snape_12")
        call her_main("(Professor...)", "annoyed", "closed", "base", "mid")
        call her_main("(Time for my finishing act then!)", "open", "closed", "base", "mid")
        pause.1

        if hermione.is_worn("panties"):
            pause.5
            $ hermione.strip("panties")
            call nar(">Hermione bends over and slides her panties down.","start")
            ">Her movements lack grace..."
            ">But a pretty pussy is always a welcome sight nonetheless..."
            call nar(">You show your appreciation by stroking your cock even faster...","end")
            call ctc

        call sna_main("Yes... Yes!!!","snape_18")
        call sna_main("Now shake those B+ titties for me, you harlot!")
        call her_main(".......", "angry", "happyCl", "worried", "mid")
        pause.5

        call nar(">All of a sudden Hermione breaks into a series of rather complex pirouettes.")
        call sna_main("Yes, such grace...","snape_19")
        call sna_main("That lithe, flexible body!","snape_20")
        call her_main(".........", "grin", "narrow", "annoyed", "up")
        call sna_main("Oh, yes!","snape_20")
        call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "grin", "narrow", "annoyed", "up")
        call nar(">Hermione seems very focused on her dancing routine.")
        call sna_main("Yes, and now another pirouette!","snape_19")
        call sna_main("Magnificent!")
        call sna_main("I would applaud you but one of my hands is very busy at the moment.","snape_13")
        m "{size=-4}(Was that an attempt at a joke?){/size}"
        m "{size=-4}(Man, horny Snape is weird...){/size}"

        call her_main(animation=None)
        call hide_characters
        show screen blkfade
        with d5

        ">Hermione performs another set of movements and pirouettes..."
        ">Gives a little curtsy bow to the imaginary audience..."
        ">And then exhaustedly slumps down on her butt."

        call her_chibi("sit_naked","on_desk","on_desk")

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with d5
        call ctc

        call her_main("Whew... This was--", "open", "closed", "base", "mid")
        with hpunch

        g4 "ARGH! YOU FUCKING WHORE!"
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum","behind_desk","base")
        pause.2

        $ hermione.set_cum(face="light")
        pause 0.7
        $ hermione.set_cum(breasts="light")
        pause 1
        $ hermione.set_cum(hair="light")


        call her_main("??!!!", "shock", "wide", "base", "stare")
        call her_main("", "angry", "happyCl", "worried", "mid")
        hide screen bld1
        with d3
        call ctc

        call sna_main("Good job, you harlot!","snape_18")
        call sna_main("Here is your reward!","snape_21")

        call cum_block
        call sna_chibi("cum","desk_close","desk_close")
        pause.2

        $ hermione.set_cum(face="heavy")
        pause 0.7
        $ hermione.set_cum(breasts="heavy", body="heavy")
        pause 1
        $ hermione.set_cum(crotch="light")

        call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")
        hide screen bld1
        with d3
        call ctc

        call sna_main("Oh... Yes...","snape_21")
        g4 "Little slut!"
        call her_main("...............................", "grin", "narrow", "annoyed", "up")

        call sna_main("Ha-ha-ha! This is magnificent!","snape_21")
        g9 "I know, right!?"

        call gen_chibi("cum_done","behind_desk","base")
        call sna_chibi("cum_done","desk_close","desk_close")

        call sna_main("Yes... We should do this more often.","snape_22")
        call her_main(".................", "grin", "narrow", "annoyed", "up")

        call sna_main("Your performance was acceptable, miss Granger...","snape_20")
        call her_main("Thank you.........", "annoyed", "narrow", "base", "dead")
        call sna_main("But if I were to grade it...","snape_19")
        call her_main("...........", "annoyed", "narrow", "base", "dead")
        call sna_main("*Hmm*....","snape_22")
        call her_main("............", "annoyed", "narrow", "base", "dead")
        call sna_main("{size=+5}F+!{/size}","snape_10")
        stop music

        call her_main("{size=+5}WHAT?!!!{/size}", "shock", "wide", "base", "stare")
        call sna_main("Yes... Quite a few things could use some improvement actually.","snape_09")
        call play_music("chipper_doodle")
        call her_main("I cannot believe this!", "clench", "base", "angry", "mid", emote="angry")
        pause.5

        call hide_characters
        show screen blkfade
        with d5

        ">Hermione furiously jumps off your desk."
        pause 2
        hide screen hermione_main

        call sna_chibi("hold_dick","mid","base")
        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","desk","base", flip=True)

        hide screen bld1
        hide screen blktone
        hide screen blkfade
        with d5
        call ctc

        call her_main("I demand a higher grade than that!", "soft", "base", "angry", "mid", xpos="right", ypos="base", flip=True)
        call sna_main("You do not demand a grade miss Granger, you earn it.","snape_09")
        call her_main("I did earn it!", "open", "base", "base", "R")
        call her_main("And could you at least have the decency to stop touching yourself, professor!", "annoyed", "narrow", "angry", "R")
        call sna_main("*Tch*...","snape_12")
        hide screen hermione_main
        with d3

        m "(Are they for real?)"
        hide screen bld1
        with d3
        pause.2

        show screen blkfade
        with d5

        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
        ">Then he beats a hasty retreat before Hermione has a chance to start another argument."
        pause 1

        call sna_chibi("stand","mid","base", flip=True)
        hide screen blkfade
        with d5

        call sna_walk(action="leave")
        pause.5

        call her_chibi("stand","desk","base")
        pause.2

        call her_main("Well...", "annoyed", "base", "worried", "R", xpos="mid", ypos="base", flip=False)
        her "Was our mission a success, [genie_name]?"

        menu:
            m "..."
            "\"*huh*? What mission?\"":
                $ her_mood += 7
                call her_main("I only agreed to this so that you could catch professor Snape in the act, [genie_name]!", "scream", "happyCl", "worried", "mid")
                call her_main("So that we would have definite proof that he is \"dirty\"!", "normal", "happyCl", "worried", "mid")
                m "Oh, that mission..."
                m "Yes. Mission accomplished!"
            "\"Yes! Thanks to you!\"":
                pass

        m "Good job, [hermione_name]."
        call her_main("I am happy to have been of help, [genie_name]!", "normal", "happyCl", "worried", "mid")
        pause.5
        show screen blkfade
        with d5

        call her_main("... Can I get paid now, please?", "angry", "happyCl", "worried", "mid", emote="sweat", ypos="head", flip=False)

        jump end_hg_pf_strip
