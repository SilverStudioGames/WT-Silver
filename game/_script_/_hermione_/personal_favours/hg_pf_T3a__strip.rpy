### Hermione Dance ###

#TODO Add her_main(animation=bob) to parts where she's dancing

label hg_pf_strip:

    if hg_pf_strip.counter < 1:
        m "{size=-4}(Ask her to dance for me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu


    # Start Event
    $ current_payout = 35
    $ hg_pf_strip.start()

    # End Event
    label end_hg_pf_strip:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    call sna_chibi("hide")
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Points
    m "{number=current_payout} points to the Gryffindor house."
    call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")

    # Hermione leaves
    call her_walk("door", "base")
    call her_chibi("leave")

    # Increase level
    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    if her_tier == 4:
        if her_whoring < 18: # Points til 18
            $ her_whoring += 1

    jump end_hermione_event

### Fail Events ###

label hg_pf_strip_fail:
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...", "soft", "wide", "base", "stare")

    call her_main("... dance for you, [genie_name]?", "open", "wide", "base", "stare")

    $ hg_pf_strip.fail_intentional()

    jump too_much

label hg_pf_strip_T2_fail_intro: # Hermione starts dancing, but it will fail anyway.
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...", "open", "base", "worried", "mid")
    call her_main("... dance for you, [genie_name]?", "open", "wink", "base", "mid")
    m "Yes... You think you could manage that?"
    call her_main("*Ehm*... I suppose so...", "soft", "base", "base", "R")
    her "Am I getting paid for this?"
    m "Of course, [hermione_name]!"
    call her_main("So... Just a little dancing then...", "annoyed", "base", "worried", "R")
    m "Whenever you're ready..."
    her "................."
    hide screen hermione_main
    with d3

    call nar(">Hermione starts dancing...")

    stop music fadeout 1.0
    hide screen bld1
    call her_chibi("dance","mid","base")
    with d3
    pause.2

    m "*Hmm*..."
    call her_main("{size=-5}(...........................................){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head", flip=False)
    call her_main("{size=-5}(This is silly...){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call nar(">Hermione looks embarrassed but she keeps on \"dancing\"...")
    m "..................."
    call her_main("{size=-5}(...........................................){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Alright, you can start undressing now."

    call her_chibi("stand","mid","base") #Hermione stands still.
    with hpunch

    show screen blktone
    call her_main("??!", "mad", "wide", "base", "stare", cheeks="blush")
    m "Take off those clothes..."
    call her_main("You want me to...?", "disgust", "narrow", "base", "down", cheeks="blush")

    hide screen blktone
    call her_main("[genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("This is ridiculous on a whole other level!", "angry", "closed", "angry", "mid", cheeks="blush")
    call her_main("I won't let myself be forced to become some cheap stripper!!!", "mad", "wide", "base", "stare", cheeks="blush")
    m "Nobody is forcing you to do this."
    m "If you don't need the points, please feel free to leave."
    call her_main("Yes. I believe you're right Sir.", "soft", "closed", "angry", "mid")
    call her_main("Stripping for you won't be worth {b}any{/b} amount of points!", "angry", "base", "angry", "mid")
    call her_main("I will be leaving now!", "annoyed", "base", "angry", "mid")

    call her_walk(action="leave")

    $ her_mood += 5
    $ hg_pf_strip.fail()

    jump end_hermione_event

label hg_pf_strip_T2_fail_repeat:
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("And would you like me to take off my clothes as well?", "soft", "closed", "base", "mid")
    m "Yes?"
    call her_main("No! I will not!", "scream", "base", "angry", "mid")
    call her_main("And I'd appreciate it if you'd stop making such outrageous requests...", "annoyed", "base", "angry", "mid")
    m "You will get points for it..."
    call her_main("Shove those points up your--", "angry", "closed", "angry", "mid")
    call her_main("I will be leaving now...", "annoyed", "base", "angry", "mid")
    call her_main("Good day, Sir...", "annoyed", "narrow", "angry", "R")

    call her_walk(action="leave")

    $ her_mood += 5
    $ hg_pf_strip.fail()

    jump end_hermione_event

### Tier 3 ###

# Event 1 (i) - Hermione tries to stip for you but fails.
# Event 2 (i) - Hermione strips for you on your desk. Snape then enters.
# Event 3 (r) - Hermione strips for. You will get some event choices.

label hg_pf_strip_T3_intro_E1: # Complete
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...", "open", "base", "worried", "mid")
    call her_main("... dance for you, [genie_name]?", "open", "wink", "base", "mid")
    m "Yes... You think you could manage that?"
    call her_main("*Ehm*... I suppose so...", "soft", "base", "base", "R")
    her "Am I getting paid for this?"
    m "Of course, [hermione_name]!"
    call her_main("So... Just a little dancing then...", "annoyed", "base", "worried", "R")
    m "Whenever you're ready..."
    her "................."
    hide screen hermione_main
    with d3

    call nar(">Hermione starts dancing...","start")

    stop music fadeout 1.0
    hide screen bld1
    call her_chibi("dance","mid","base")
    with d3
    pause.2

    m "*Hmm*..."
    call her_main("{size=-5}(...........................................){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head", flip=False)
    call her_main("{size=-5}(This is silly...){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call nar(">Hermione looks embarrassed but she keeps on \"dancing\"...")
    m "..................."
    call her_main("{size=-5}(...........................................){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Alright, you can start undressing now."

    call her_chibi("stand","mid","base") #Hermione stands still.
    with hpunch

    call her_main("??!", "mad", "wide", "base", "stare", cheeks="blush")
    call her_main("I thought all I had to do was dance?", "angry", "base", "angry", "mid")
    call play_music("playful_tension") # SEX THEME.
    m "Really? That's adorable."
    m "Now start taking off those clothes."

    show screen blktone
    call her_main("You want me to... strip for you...?", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Yes. And I expect you to do it today, [hermione_name]."
    call her_main("[genie_name]!", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Don't you raise your voice at me, [hermione_name]!"
    call her_main(".....!!?", "mad", "wide", "base", "stare", cheeks="blush")
    m "Nobody is forcing you to do this."
    m "I am doing you a favour!"
    m "If you don't need the points, please feel free to leave."
    call her_main(".....................", "angry", "base", "angry", "mid")
    call her_main(".......................................", "disgust", "narrow", "base", "down", cheeks="blush")

    hide screen blktone
    call nar(">Hermione starts dancing again...")

    call her_chibi("dance","mid","base") #Chibi takes off the vest here btw but Hermione does not even if she's wearing it
    with d5

    call her_main("{size=-5}(...........................................){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "What are you waiting for then?"

    call her_main(".............................................................", "disgust", "narrow", "base", "down", cheeks="blush")
    call nar(">Hermione gives you a confused look...")

    pause .5
    show screen blktone
    call her_main("{size=-5}(Am I really going to do this?){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush", xpos="base", ypos="base", trans=fade)
    hide screen blktone

    $ hermione.strip("robe", "accessory")

    menu:
        m "......................."
        "\"Now, get rid of your bottoms!\"":
            call her_main(".................................", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call nar(">Hermione starts taking off her bottoms...","start")
            ">She seems very hesitant and takes her time..."
            call nar(">Finally she takes a deep breath and takes off her bottoms...","end")

            call her_main("{size=-5}(Here it comes then...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}(For the honour of Gryffindor....){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            pause .2

            $ hermione.strip("bottom")
            call ctc
            pause .5

            m "..............."
            call her_main("{size=-5}(.........................................){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call nar(">Hermione keeps on dancing...")
            m "Alright, your top is next!"
            call her_main("My top....?", "disgust", "narrow", "worried", "down", cheeks="blush")
            hide screen hermione_main
            with d3

            call nar(">Hermione looks extremely embarrassed...","start")
            call nar(">She clumsily shakes her body to and fro...","end")

        "\"Now, take off your top!\"":
            call her_main(".................................", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call nar(">Hermione starts taking off her top...","start")
            ">She seems very hesitant and takes her time..."
            call nar(">Finally she takes a deep breath and removes her top...","end")

            call her_main("{size=-5}(Alright, here it comes...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}(For the honour of the Gryffindor!){/size}", "angry", "base", "worried", "mid", cheeks="blush")
            pause .2

            $ hermione.strip("top")
            call ctc

            if hermione.is_worn("bra"):
                m "And your bra..."
                call her_main("...", "angry", "base", "angry", "mid")
                $ hermione.strip("bra")
                call her_main("{size=-5}(I...{w=0.4} I did it...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            else:
                call her_main("{size=-5}(I actually did it...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")

            # call her_chibi("dance","mid","base")


            call her_main("{size=-5}(He can see my breasts while I'm dancing for him...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}(This is so demeaning...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}(But I am doing this for my house...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")

            m "Not bad..."
            call her_main("{size=-5}(.........................................){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")

            call nar(">Hermione is topless now...","start")
            ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
            call nar(">It seems like she's desperately trying to prevent her breasts from bouncing or swaying...","end")

            m "Alright, your bottoms are next!"
            call her_main("....................", "angry", "happyCl", "worried", "mid", cheeks="blush")
            hide screen hermione_main
            with d3

            call nar(">Hermione looks extremely embarrassed...","start")
            call nar(">Her fingers shaking as she fumbles somewhat...","end")

    stop music fadeout 1.0
    m "What's the problem, [hermione_name]?"
    call play_music("sad")

    call her_main("I'm sorry, [genie_name]...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("I...{w=0.4} I'm trying...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("But my hands...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("Why is this so hard! *sob*", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("No, I can't do this, [genie_name]! *sob*", "open", "wide", "worried", "stare", cheeks="blush", tears="messy")
    m "What?"
    call her_main("I thought I could, but...", "angry", "squint", "base", "mid", cheeks="blush", trans=fade)
    call her_main("Stripping for points, [genie_name]?", "angry", "squint", "base", "mid", cheeks="blush")
    call her_main("People look up to me in this school!", "angry", "squint", "base", "mid", cheeks="blush")
    call her_main("I have a reputation...*sob*", "angry", "squint", "base", "mid", cheeks="blush")
    call her_main("And If I do this...", "scream", "base", "angry", "mid", cheeks="blush", tears="messy")
    show screen blkfade
    with d5

    ">Hermione quickly puts her clothes back on..."

    $ hermione.wear("all")
    call her_chibi("stand","desk","base")

    hide screen blkfade
    call her_main("[genie_name], I think I'd better go now... *Sob!*", "angry", "squint", "base", "mid", cheeks="blush", tears="messy", trans=fade)

    menu:
        "\"Alright. I had fun. Here are your points.\"":
            call her_main("Really? I didn't ruin it completely then?", "soft", "base", "base", "R", tears="soft")

            jump end_hg_pf_strip

        "\"Sure. You will receive no points though.\"":
            call her_main("[genie_name]... I may not be very good at this...", "open", "base", "base", "mid", tears="mascara_crying")
            call her_main("But I did my best... I think I deserve some--", tears="mascara_crying")
            m "Just make sure you try harder next time, [hermione_name]."
            call her_main("Next time?!", "open", "base", "base", "mid", tears="mascara_crying")
            call her_main("I assure you, [genie_name], there will be no next time...", "angry", "base", "angry", "mid", cheeks="blush", tears="mascara")
            m "We'll see..."
            call her_main("*Tsk*!", "disgust", "narrow", "base", "mid_soft", tears="mascara")

            call her_walk(action="leave")

            # Event does not fail. She just gets mad, but no whoring increase.
            $ her_mood += 25

            jump end_hermione_event

label hg_pf_strip_T3_intro_E2:
    call bld
    m "[hermione_name], I need you to dance for me."
    call her_main("That again, [genie_name]...?", "disgust", "narrow", "base", "mid_soft")
    m "You will get paid accordingly of course..."
    call her_main("............................", "annoyed", "narrow", "angry", "R")
    call her_main("And you expect me to... *Ehm*...", "annoyed", "narrow", "angry", "R")
    m "Take your clothes off. Naturally."
    stop music fadeout 1.0

    show screen blktone
    call her_main("......................", "annoyed", "narrow", "angry", "R")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Well, why not?", "disgust", "narrow", "base", "mid_soft")
    call her_main("Yes, I don't see why not!", "scream", "base", "angry", "mid", emote="angry")
    m "*Hmm*...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
    call her_main("After all, as a pupil I am meant to obey your every order, isn't that right, [genie_name]?!", "scream", "closed", "angry", "mid")
    m "...................."
    call her_main("If the Headmaster tells me to strip for him, Then I shall strip!!!", "scream", "closed", "angry", "mid")
    call her_main("Do I find this extremely inappropriate, disgraceful and humiliating?", "angry", "base", "angry", "mid")
    call her_main("Of course not. What nonsense!", "scream", "closed", "angry", "mid")
    m ".............."
    call her_main("Ha! Might as well do this the proper way!", "angry", "base", "angry", "mid")

    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3
    pause.2

    m "??!"

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
    pause 3
    g4 "!!!!!!"
    ">To your surprise Hermione just hops onto your desk and starts dancing frantically..."

    call her_chibi("dance","on_desk","on_desk")

    hide screen blkfade
    with fade
    pause.5

    call her_main("If I must degrade myself in order to protect the honour of my house...", "scream", "closed", "angry", "mid", xpos="mid", ypos="base")

    call her_main("So be it then!", "scream", "base", "angry", "mid", emote="angry")
    call her_main("Just...", "open", "narrow", "worried", "down")
    $ hermione.strip("robe", "accessory")
    call her_main("*groan*", "clench", "narrow", "base", "down")

    if hermione.is_any_worn("top"):
        call nar(">Hermione begins taking off her top...")
        call nar(">Pulling at the fabric in anger, making it more difficult than it should be...")
        call her_main("Why won't it....?!")
        call her_main("There!", "annoyed", "narrow", "annoyed", "mid")
        call nar(">Hermione finally manages to untangle herself and sends her top flying to the other side of the room...")

        $ hermione.strip("top")
        call ctc
        pause .5

    else:
        call nar(">The girl seems to contemplate about which piece of clothing she should take off first...")
        pause.1

    call her_main("My bottoms are next, right?", "scream", "closed", "angry", "mid")

    menu:
        m "..."
        "\"Yes, that's right. Take it off!\"":
            call her_main("Of course!")
            call her_main("Here it goes!", "open", "narrow", "worried", "down")
        "\"You need to calm down, [hermione_name].\"":
            call her_main("Well, {size=+7}EXCUSE ME{/size}, [genie_name]!")
            call her_main("You told me to strip for you, but you never told me your preferences in regards to the pace!")
            m "Well, I'm telling you now, [hermione_name]!"
            call her_main("Too late!", "angry", "base", "angry", "mid")

    $ hermione.strip("bottom")
    call ctc
    pause .5

    call nar(">Hermione sends her bottoms flying across the room, just like she did with her top a moment earlier...")

    m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
    m "{size=-4}(Maybe it was still too early to--{/size}"
    call her_main("Clothes?!!", "disgust", "narrow", "base", "mid_soft")
    call her_main("{size=+9}I don't need them!{/size}", "scream", "base", "angry", "mid", emote="angry")
    if hermione.is_worn("bra"):
        call nar(">Hermione keeps dancing angrily, and then...")
        call her_main("", "angry", "base", "angry", "mid")
        $ hermione.strip("bra")
        pause.2
        g4 "{size=-4}(When did she??!){/size}"
    call ctc

    call her_main("Are you enjoying this, [genie_name]?")
    call her_main("", "angry", "base", "angry", "mid")

    call her_main("Shall I shake my breasts for you like one of those harlots?", "scream", "closed", "angry", "mid")
    m "Well--"
    call her_main("Of course! Why wouldn't I degrade myself for your pleasure?!")
    call her_main("This is completely {size=+7}acceptable!{/size}", "scream", "base", "angry", "mid", emote="angry")
    call her_main("", "angry", "base", "angry", "mid")

    pause.2
    call nar(">Hermione is starting to shake her naked breasts rather clumsily...","start")
    call nar(">As you watch the girl's tits sway right and left you find yourself fighting the urge to...","end")

    menu:
        m "..."
        "-Grab them!-":
            g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
            g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "disgust", "wide", "base", "stare")
            pause.2
            call slap_her #Calls slapping sound and visual.
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

        "-Slap them!-":
            m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "disgust", "wide", "base", "stare")
            pause.2
            g9 "{size=-4}(Yes, just slap them around a little...){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

        "-Bite on them!":
            m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
            m "{size=-4}(No, it's not weird!){/size}"
            m "{size=-4}(Just a couple of gentle love-bites!){/size}"
            call kiss_her
            call her_main("", "shock", "wide", "base", "stare", tears="soft")
            pause.2
            g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
            call her_main("", "disgust", "happyCl", "worried", "mid", tears="soft_blink")
            pause.2
            call kiss_her
            call kiss_her
            pause.2

        "-Motorboat them!-":
            m "{size=-4}(I'm going to put my face right in between them!){/size}"
            call kiss_her
            call her_main("", "shock", "happyCl", "worried", "mid")
            pause.2
            g9 "{size=-4}(Yes, motor boating these titties is be the best!){/size}"
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

    call nar(">While you are having fun with her tits, Hermione keeps on dancing...","start")

    call her_main("(Dancing naked in front of the headmaster...)", "soft", "wide", "worried", "shocked")
    call her_main("(Letting him touch my breasts...)", "disgust", "wide", "worried", "shocked")
    call her_main("(If my parents knew about this they would lose their minds...)", "soft", "wide", "worried", "shocked")
    call her_main("(Especially my father...)", "annoyed", "closed", "base", "mid")
    ">Hermione is starting to shake her tits again..."
    call her_main("(Hermione Granger - the stripper...)")
    call her_main("(Forgive me father...)", "annoyed", "narrow", "base", "dead")

    ">Hermione puts her hands on her tits and starts squeezing them..."
    ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
    call her_main("(I used to be a top student...{w=0.4} Used to have standards...)")
    ">Hermione clutches her tits even harder and then gives them a couple of twists..."
    ">Almost looking as if she is mad at her own breasts and trying her best to punish them..."

    call nar(">You find the thought strangely arousing...","end")

    #TODO Hermione chibi: Stand in panties only (blinking?)
    call her_chibi("dance_pause","on_desk","on_desk")
    call ctc

    call her_main("Well, I hope you enjoyed yourself, [genie_name]!", "open", "narrow", "annoyed", "mid")
    m "What?"
    call her_main("I would like to get paid now...", "open", "closed", "angry", "mid")
    if hermione.is_worn("panties"):
        m "Aren't you forgetting something, [hermione_name]?"
        call her_main("[genie_name]...?", "open", "narrow", "annoyed", "mid")
        m "Your panties...?"
        call her_main("My panties?", "open", "wide", "base", "stare")
        call her_main("But, they always leave them on!")
        m "Who exactly are \"they\"?"
        m "Strippers in kid's cartoons?"
        m "Stripping is stripping, [hermione_name]!"
        m "Now take off your panties!"
        call her_main("................", "angry", "wide", "base", "stare")

        call nar(">Hermione looks at you horror-struck. All of her anger now gone...","start")
        call her_main(".................", "annoyed", "closed", "base", "mid")
        ">Without saying another word..."
        call nar(">She starts pulling down her panties...","end")

        $ hermione.strip("panties")

    #TODO Hermione chibi: Stand naked blinking (ch_hem blink_n)
    call her_chibi("dance_pause","on_desk","on_desk")
    call her_main("", "annoyed", "happyCl", "worried", "mid", cheeks="blush")
    pause.2

    g9 "......................................."

    hide screen blktone
    hide screen bld1
    hide screen hermione_main
    with d1

    stop music

    call sna_walk(action="enter", xpos="mid", ypos="base")

    call sna_main("Listen, Genie. I've been think--","snape_01", xpos="base", ypos="base")

    show screen hermione_main
    with d3

    $ renpy.play('sounds/scratch.wav')
    with hpunch

    call sna_main("............................................","snape_11")
    with hpunch

    call her_chibi("dance_pause","on_desk","on_desk", flip=True)
    call her_main("(Professor Snape???????!)", "angry", "wide", "base", "stare", flip=True)
    call sna_main("Miss Granger?","snape_12")

    call set_her_action("covering")
    call her_main("(No, no... This is not happening. Please...)", "shock", "happyCl", "worried", "mid", cheeks="blush", trans=d5)
    call play_music("playful_tension") # SEX THEME.
    m "...................................."

    menu:
        m "..."
        "\"Severus, I am busy right now.\"":
            call sna_main("Yes... I can see that...","snape_13")
            call her_main("{size=-7}(I want to die!){/size}", "angry", "happyCl", "worried", "mid")

        "\"Severus! Please, come join us.\"":
            $ her_mood += 20
            call sna_main("Seriously?","snape_14")
            call her_main("([genie_name], no, please.............................)", "angry", "happyCl", "worried", "mid")
            call sna_main("A very tempting offer indeed...","snape_13")
            call her_main("!!!!!!.......", "angry", "wide", "base", "stare")
            call sna_main("Well, maybe some other time...","snape_13")
            call her_main("{size=-5}(There will be no other time!){/size}", "angry", "happyCl", "worried", "mid")
            call her_main("{size=-5}(I will stop selling favours from now on, I swear!){/size}")

    call sna_main("I shall postpone our conversation then, Geni-- *ahem*! Albus.","snape_12")
    call sna_main("Miss Granger...","snape_13")
    call her_main(".................................", "angry", "happyCl", "worried", "mid")

    call hide_characters
    hide screen bld1
    with fade
    pause.2

    call sna_walk(action="leave")

    show screen blkfade
    with d5

    $ hermione.wear("bra", "panties", "bottom")
    ">Hermione hastily hops off your desk."
    ">She starts putting her clothes back on rather frantically..."

    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d5

    call her_main("My top! Where's my top?!", "scream", "happyCl", "worried", "mid", xpos="mid", ypos="base", flip=False)
    m "It's over there, by the fireplace..."

    hide screen hermione_main
    with d3
    pause.2

    call her_walk("mid", "base")

    call her_main("................................", "disgust", "narrow", "base", "down", ypos="head", flip=False)
    pause.2

    $ hermione.wear("all")

    call her_chibi("stand","mid","base", flip=True)
    pause.2

    call her_walk("desk", "base")

    call her_main("........................", "normal", "happyCl", "worried", "mid", xpos="base", ypos="base")
    stop music fadeout 2.0
    call her_main("Can I just get my points now, please?", "angry", "happyCl", "worried", "mid", emote="sweat")
    pause.5

    if hg_strip.trigger == False:
        $ achievement.unlock("herstrip")
        $ hg_pf_strip.change_icon(a="heart_half", b="heart_red")
    $ hg_strip.triggered() # .trigger = True, .counter += 1
    $ hg_pf_strip.title = "Strip for Me!"

    jump end_hg_pf_strip

label hg_pf_strip_T3_E2:
    m "[hermione_name], how about another strip?"
    call her_main("..............", "disgust", "narrow", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [genie_name]..."
    m "Why? You are getting quite good at it."
    call her_main(".........................", "annoyed", "narrow", "annoyed", "mid")
    call her_main("{number=current_payout} house points?", "open", "narrow", "worried", "down")
    m "Sure! The usual rate."
    call her_main("...................", "annoyed", "narrow", "angry", "R")

    if ss_he.hermione_strip: #Turns TRUE after Dance Event 2 and the next Date with Snape.
        m "(*Hmm*... Should I invite Snape to watch as well?)"

        menu:
            "-Yes! Hermione needs an audience!-":
                jump hg_pf_strip_T3_snape

            "-Nah. That's not a good idea...-":
                pass

    # Locks Door.
    call hide_characters
    hide screen bld1
    with d3
    pause.5

    call her_walk("door", "base")

    pause.2
    call chibi_emote("thought", "hermione")
    pause.5
    call play_sound("lock")
    call chibi_emote("hide", "hermione")
    pause.2

    m "??!"
    pause.2


    # Walks back.
    call her_chibi("stand","door","base")
    pause.1

    call her_walk("mid", "base")
    pause.2

    call her_main("Just in case...", "annoyed", "narrow", "angry", "R", ypos="head", flip=False)
    stop music fadeout 1.0

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call play_sound("climb_desk")
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    call her_main("Just for the record...", "open", "closed", "base", "mid", xpos="mid", ypos="base")
    call her_main("I still consider this a highly inappropriate favour to be buying from one of your students, [genie_name].", "annoyed", "squint", "base", "mid")
    m "Right. And an equally inappropriate favour to be selling to your headmaster. Wouldn't you agree?"
    call her_main("..........", "annoyed", "narrow", "angry", "R")
    $ hermione.strip("robe", "accessory")

    if hermione.is_worn("top"):
        call nar(">Hermione shifts her body towards you and starts taking off her top...")
        $ hermione.strip("top")
        pause .5
    if hermione.is_worn("bra"):
        call nar(">She takes off her bra somewhat clumsily...")
        $ hermione.strip("bra")

    pause .2
    call ctc

    g9 "Yes! The tits!"

    call play_music("playful_tension") # SEX THEME.
    call her_main("..............", "open", "narrow", "worried", "down")
    call her_main("What if my parents were to find out about this, [genie_name]?", "disgust", "narrow", "base", "down")
    call her_main("Mother would never understand...")
    call her_main("As for my father...", "upset", "wink", "base", "mid")

    menu:
        m "..."
        "{size=-3}\"Your father would be proud of you!\"{/size}":
            call her_main("I doubt it...")
            call her_main("Yes, I am doing this for the right reasons, but...")
            call her_main("He would never see it that way...", "annoyed", "base", "angry", "mid")
            call her_main("He must never know about this...")

        "{size=-3}\"Your father would spank you hard!\"{/size}":
            call her_main("He would not!", "shock", "wide", "base", "stare")
            call her_main("And I am too old for that any way...", "upset", "wink", "base", "mid")
            g9 "I would say that you are the perfect age for that..."
            call her_main("*huh*?")
            call her_main("I do not know what you mean, [genie_name].", "grin", "happyCl", "worried", "mid", emote="sweat")

        "{size=-3}\"Your father would disown you!\"{/size}":
            call her_main("You are probably right, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
            call her_main("(Oh father, I am so sorry...)", "angry", "base", "base", "mid", tears="soft")
            call her_main("he must never find out...", "angry", "base", "base", "mid", tears="soft")

        "{size=-3}\"Your father would love to watch you strip!\"{/size}":
            call her_main("He would not! He would be ashamed of me!", "normal", "happyCl", "worried", "mid")
            m "Are you sure about that?"
            call her_main("absolutely! My father is a man of integrity!", "scream", "happyCl", "worried", "mid")
            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
            call her_main(".....................", "annoyed", "narrow", "annoyed", "mid")
            call her_main("My father must never know about this...", "annoyed", "base", "worried", "R")


    call nar(">Hermione is starting to sway her hips rather seductively...")

    if hermione.is_worn("bottom"):
        call nar(">Whilst sliding her bottoms down...")
        $ hermione.strip("bottom")
    pause.3
    call ctc

    menu:
        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T3_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T3_watch

label hg_pf_strip_T3_watch:
    call nar(">You watch Hermione Dance...")
    call her_main("(Time for the finishing act I suppose...)", "angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")

    if hermione.is_worn("panties"):
        m "Yes, [hermione_name]! Take them off!"
        call her_main("........", "annoyed", "closed", "base", "mid")
        call nar(">Hermione bends over slightly and slides her panties down...")
        $ hermione.strip("panties")
        pause 1.0

    call nar(">You can see that she is doing her best to not fall off the desk...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")

    call ctc

    call her_main("..........", "disgust", "happyCl", "worried", "mid")
    call nar(">Hermione performs another set of rather awkward movements...","start")
    call nar(">if not for her naked tits bouncing all over the place this would be quite embarrassing...","end")

    g9 "................."
    call nar(">A few more clumsy movements before Hermione slumps on her butt...")

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call her_main("I'm sorry, Sir. Was this good enough?...", "disgust", "narrow", "base", "down", emote="sweat", ypos="head", flip=False)

    menu:
        m "..."
        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
            m "Good job [hermione_name]!"
            call her_main("..............", "disgust", "narrow", "worried", "down")
            m "You have a lot of talent for this!"
            call her_main("Thank you [genie_name].", "soft", "base", "worried", "R", emote="sweat")
        "{size=-3}\"*Hmm*... This was quite awful...\"{/size}":
            $ her_mood += 4
            call her_main("............", "annoyed", "base", "angry", "mid")
            m "You just need to practise more..."
            call her_main("Whatever.........", "annoyed", "narrow", "angry", "R")
        "{size=-3}\".................................................\"{/size}":
            call her_main(".......................", "silly", "happyCl", "worried", "mid", emote="sweat")
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

    hide screen bld1
    call ctc

    jump end_hg_pf_strip

label hg_pf_strip_T3_masturbate:
    show screen blkfade
    with d5

    call her_main("[genie_name]?!", "open", "wide", "base", "stare", ypos="head", flip=False)
    m "It's alright, [hermione_name]. Don't mind me..."

    call gen_chibi("jerk_off","behind_desk","base")
    call her_chibi("dance","on_desk","on_desk")
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call bld
    call her_main("B-but...", "angry", "wide", "base", "stare", ypos="head", flip=False)
    call her_main("Your...")
    m "Yes... Ah, yes, this is good..."
    call her_main("[genie_name]!!!", "scream", "happyCl", "worried", "mid")
    call her_main("I must insist that you put away your...", "angry", "happyCl", "worried", "mid")
    call her_main("... thing.")

    menu:
        m "..."
        "\"I said, keep on dancing, [hermione_name]!\"":
            stop music fadeout 1.0

            call her_main("No, [genie_name]!", "annoyed", "narrow", "angry", "R", ypos="head", flip=False)
            m "*huh*?"
            show screen blkfade
            with d5

            ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
            m "Oh, come on! Don't leave me like that!"
            $ hermione.wear("all")
            call her_chibi_scene("reset","desk","base", trans=fade)

            call her_main("The dance is over, [genie_name]!", "soft", "base", "angry", "mid")
            pause 1
            call her_main("I would like to get paid now!", "annoyed", "narrow", "annoyed", "mid")
            m "Stubborn [hermione_name]..."
            call nar(">You reluctantly put your cock away...")
            call her_main("I would like to get paid now.", "annoyed", "narrow", "annoyed", "mid")

            $ her_mood += 6

            jump end_hg_pf_strip

        "\"Fine. There is no need for drama!\"":
            call her_main("......................", "annoyed", "narrow", "angry", "R", ypos="head", flip=False)
            pause.1

            call gen_chibi("sit_behind_desk")
            call her_chibi("dance","on_desk","on_desk")
            hide screen blktone
            hide screen bld1
            with fade
            pause.5

            jump hg_pf_strip_T3_watch

### Tier 4 ###


# Event 1 (i) - Hermione tries her best at stripping.
# Event 2 (i) -
# Event 3 (r) -

label hg_pf_strip_T4_intro_E1:
    m "[hermione_name], how about another strip?"
    call her_main("..............", "disgust", "narrow", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [genie_name]..."
    m "Why? You are getting quite good at it."
    call her_main(".........................", "annoyed", "narrow", "annoyed", "mid")
    call her_main("{number=current_payout} house points?", "open", "base", "base", "mid")
    g9 "Sure!"
    call her_main("Very well, then...", "base", "base", "base", "R")

    jump hg_pf_strip_T4

label hg_pf_strip_T4_intro_E2:
    m "[hermione_name], would you like to provide me another strip show?"
    m "(I'm bored as fuck in here after all...)"
    call her_main("*Hmm*...", "annoyed", "base", "base", "R", xpos="base", ypos="base")
    call her_main("Sure! Why not...", "base", "happyCl", "base", "mid")
    g9 "Yes?"
    call her_main("I've been practising a bit more. Mainly on my dancing.", "soft", "narrow", "worried", "down")
    m "Very good... I'd love to see your progress."
    call her_main("Of course, [genie_name]...", "base", "narrow", "base", "mid_soft")

    jump hg_pf_strip_T4

label hg_pf_strip_T4_E2:
    m "[hermione_name], would you like to strip for me again?"
    if her_tier <= 5:
        call her_main("Of course, [genie_name]...", "base", "base", "base", "mid", xpos="base", ypos="base")
    else:
        call her_main("I'd love to, [genie_name]!", "open_tongue", "narrow", "annoyed", "up", xpos="base", ypos="base")

    jump hg_pf_strip_T4

label hg_pf_strip_T4:
    menu:
        m "(...)"
        "-Invite Snape to watch-" if ss_he.hermione_strip:
            jump hg_pf_strip_T4_snape

        "-Ask her to lock the door-":
            if her_tier <= 5:
                call her_main("Of course...", "base", "base", "base", "mid")
            else:
                call her_main("(How boring...)", "annoyed", "narrow", "annoyed", "up")

            call hide_characters
            hide screen bld1
            with d3
            pause.5

            call her_walk("door", "base")

            pause.5
            call play_sound("lock")

            # Walks back.
            call her_chibi("stand","door","base")
            pause.1

            call her_walk("mid", "base")
            pause.2

            call her_main("All done!", "smile", "closed", "base", "mid", trans=d3)

        "-Tell her to leave the door open-":
            if her_tier <= 4:
                call her_main("But, what if somebody walks in again!", "shock", "wide", "base", "stare")
                m "Nonsense. No such thing will happen..."
                call her_main("It happened once already!", "angry", "base", "angry", "mid")
                m "Stop being such a fuzzy and get over here..."
                call her_main("..................", "annoyed", "narrow", "angry", "R")

                stop music fadeout 1.0
                call her_walk("desk", "base", reduce=0.8)

                $ her_mood += 4
            else:
                call her_main("Yes, [genie_name].", "base", "narrow", "base", "mid_soft")

                stop music fadeout 1.0

    # Climb desk
    call blkfade
    call play_sound("climb_desk")
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide screen hermione_main
    hide screen blkfade
    with d5
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call her_main("...", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=d3)
    $ hermione.strip("robe", "accessory")
    m "Yes, very nice."
    call her_main("...", "annoyed", "narrow", "worried", "down")

    if hermione.is_worn("top"):
        call nar(">Hermione hastily starts pulling at her top...")

    m "Slowly, please..."
    m "There's no rush."

    if hermione.is_worn("top"):
        call her_main("I'm not!", "open", "base", "angry", "mid")
        call her_main("It's just... I...", "disgust", "narrow", "base", "down")
        g9 "Would you like some help with it?"
        if her_tier <= 5:
            call her_main("No...", "annoyed", "base", "angry", "mid")
            call her_main("I can do it, [genie_name].", "open", "closed", "base", "mid")
        else:
            call her_main("No, [genie_name].", "base", "narrow", "base", "mid_soft")
            call her_main("Just enjoy the show...", "soft", "narrow", "base", "mid_soft")
            g9 "I will, [hermione_name]."

    call her_main("...", "base", "narrow", "worried", "down")

    if hermione.is_worn("top"):
        call nar(">Hermione pulls her top over her head...")
        call nar(">And takes it off somewhat gracefully...")
        $ hermione.strip("top")
        pause.5

    if hermione.is_worn("bra"):
        call nar(">Hermione undoes her bra rather provocatively.")

        $ hermione.strip("bra")
        pause.5

    call ctc

    g9 "Yes! Shake those tits!"

    if her_tier <= 4:
        call her_main("Must you be so vulgar, [genie_name]?", "annoyed", "closed", "base", "mid")
        call her_main("..............", "annoyed", "narrow", "worried", "down")

        call her_main("[genie_name]?", "open", "base", "base", "mid")
        m "*huh*?"
        call her_main("Can I ask you a question?", "upset", "wink", "base", "mid")
        m "Go ahead..."
        call her_main("...............", "normal", "happyCl", "worried", "mid")
        call her_main("Have you ever been in love...?", "grin", "happyCl", "worried", "mid", emote="sweat")

        menu:
            m "..."
            "\"Don't be ridiculous! Love is a lie!\"":
                call her_main("I am sorry you think that way, [genie_name]!", "annoyed", "base", "worried", "R")
                call her_main("But you couldn't be more wrong!", "annoyed", "narrow", "annoyed", "mid")
                call her_main("I believe that true love is what makes the earth turn!", "base", "base", "base", "R")
                m "Actually the conservation of angular momentum is responsible for that."
                call her_main("*huh*?", "upset", "wink", "base", "mid")
                if hermione.is_worn("bottom"):
                    m "Never mind. Just take off your bottoms already?"
                else:
                    m "Never mind. Keep dancing!"
                call her_main("............", "annoyed", "narrow", "annoyed", "mid")

            "\"Be quiet and keep on dancing!\"":
                call her_main("But you said I could ask you a question...", "annoyed", "narrow", "annoyed", "mid")
                m "And you did, didn't you?"
                call her_main("!!!............", "open", "base", "base", "mid")
                call her_main("....................................", "annoyed", "narrow", "annoyed", "mid")
                if hermione.is_worn("bottom"):
                    m "Now, hush and take your bottoms off."
                else:
                    m "Now, hush and let me enjoy this."
                call her_main("........", "annoyed", "narrow", "angry", "R")

            "\"Yes... a very long time ago...\"":
                m "Yes... a very long time ago..."
                call her_main("!!!!!??..............................", "open", "base", "base", "mid")
                m "Her name was Eden..."
                call her_main("Was she beautiful?", "base", "base", "base", "mid")
                m "She was so much more than that..."
                m "She was smart, green and perfect..."
                call her_main("She was... \"green\"...?", "open", "narrow", "worried", "down")
                call her_main("Are you making fun of me, [genie_name]?", "angry", "base", "angry", "mid")
                m "Oh, you humans know nothing of true love..."
                call her_main(".....................................?", "soft", "base", "base", "mid")
                if hermione.is_worn("bottom"):
                    m "Err... I mean, take off your bottoms, [hermione_name]!"
                else:
                    m "Err... I mean, keep on dancing, [hermione_name]!"
                call her_main(".................", "annoyed", "narrow", "angry", "R")

            "\"I feel like I'm in love right now!\"":
                call her_main("You don't have to be vulgar, [genie_name].", "annoyed", "narrow", "angry", "R")
                m "Oh, but I mean it!"
                call her_main("[genie_name], please!", "disgust", "narrow", "base", "mid_soft")
                call her_main("I am one of your students!", "soft", "base", "base", "mid")
                call her_main("And you are older than my father!", "grin", "happyCl", "worried", "mid", emote="sweat")
                m "{size=-4}(You have no idea, girl.){/size}"
                call her_main("Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction...", "soft", "base", "base", "mid")
                call her_main("And when a man is experiencing sexual arousal, the same type of hormones--", "open", "closed", "base", "mid")
                m "[hermione_name]!"
                call her_main("Yes, [genie_name]?", "soft", "base", "base", "mid")
                m "Did you forget where you are?"
                call her_main("Oh, my apologies, [genie_name]... I get distracted sometimes.", "grin", "happyCl", "worried", "mid", emote="sweat")
                if hermione.is_worn("bottom"):
                    m "Take off your bottoms already, would you?!"
                else:
                    m "Get to the good stuff already, would you?!"
                call her_main("Right...", "annoyed", "base", "worried", "R")

    call nar(">Hermione is starting to sway her hips rather seductively...")

    if hermione.is_worn("bottom"):
        call nar(">Whilst sliding her bottoms down...")
        $ hermione.strip("bottom")
        pause.5
    call ctc

    menu:
        "-Ask her to masturbate-":
            if her_tier == 4:
                jump hg_pf_strip_T4_fingering
            elif her_tier == 5:
                jump hg_pf_strip_T5_fingering
            else: # Tier 6, and a fallback for cheaters!
                jump hg_pf_strip_T6_fingering

        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T4_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T4_watch

label hg_pf_strip_T4_watch:
    call blktone
    call nar(">You watch Hermione Dance...")
    call her_main("(Time for the finishing act I suppose...)", "angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")

    if hermione.is_worn("panties"):
        m "Yes, [hermione_name]! Take them off!"
        call her_main("........", "annoyed", "closed", "base", "mid")
        call nar(">Hermione bends over slightly and slides her panties down...")
        $ hermione.strip("panties")

    call nar(">You can see that she is doing her best to be graceful...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
    call ctc

    call her_main("..........", "base", "narrow", "base", "mid_soft")

    call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes...")
    m "{size=-4}(This looks quite impressive actually...){/size}"
    pause.5
    call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements...")
    call ctc

    m "{size=-4}(Did she practise this?){/size}"
    g9 "Oh, why would I care?"
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "open", "closed", "base", "mid")
    pause.5
    call nar(">Hermione performs another set of movements that could be considered classy...","start")
    call nar(">if not for her naked tits bouncing all over the place...","end")

    g9 "Yes, yes, you little harlot!"

    call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    ">And then Hermione slumps on her butt, completely exhausted."

    call hide_characters
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("Whew... This was rather exciting...", "silly", "happyCl", "worried", "mid", emote="sweat", ypos="head", flip=False)

    menu:
        m "..."
        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
            m "Good job [hermione_name]!"
            call her_main("Really?", "base", "narrow", "base", "mid_soft")
            m "Yes! You have a lot of talent for this!"
            call her_main("Thank you [genie_name].", "silly", "happyCl", "worried", "mid", emote="sweat")
        "{size=-3}\"*Hmm*... This was quite awful...\"{/size}":
            call her_main("Oh... I'm sorry...", "soft", "happy", "base", "R")
            m "That's OK... You just need to practise more..."
            call her_main("*Ehm*... I will keep that in mind, [genie_name]...", "open", "base", "base", "R")
        "{size=-3}\".................................................\"{/size}":
            call her_main(".......................", "silly", "happyCl", "worried", "mid", emote="sweat")
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

    hide screen bld1
    call ctc

    jump end_hg_pf_strip

label hg_pf_strip_T4_masturbate:
    show screen blkfade
    with d5

    call gen_chibi("jerk_off","behind_desk","base")
    hide screen blkfade
    with fade

    call her_main("But...", "angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")
    call her_main(".............................")
    call her_main("Well, alright, but only if you will promise me not to... finish, [genie_name].", "soft", "base", "angry", "mid")

    menu:
        m "..."
        "-Promise her to hold it-":
                $ d_flag_07 = True #Promised to hold it.
                call her_main("Well, alright then...", "open", "closed", "base", "mid")

        "-Give her no such promise-":
            $ d_flag_07 = False #Did not promise to hold it.
            m "\"Not to finish\"? That would be like torture!"
            m "Please keep your sadistic urges to yourself, [hermione_name]."
            call her_main("I don't have any... sadistic urges, [genie_name]!", "annoyed", "narrow", "angry", "R")
            call her_main("I just don't want to...")
            g9 "Yes... Those are some nice tits you have..."
            call her_main("............", "angry", "happyCl", "worried", "mid")
            g9 "A-ah... Yes..."
            call her_main("..........", "angry", "happyCl", "worried", "mid")
            call her_main("Fine! Have it your way, [genie_name]!", "angry", "happyCl", "worried", "mid")
            call her_main("{size=-5}(As usual...){/size}", "annoyed", "narrow", "angry", "R")


    call nar(">You keep on wanking while you watch Hermione's dance...")
    show screen blktone
    call her_main("Time for the finishing act I suppose...", "annoyed", "closed", "base", "mid")

    if hermione.is_worn("panties"):
        m "Yes, [hermione_name]! Take them off!"
        call her_main("........", "annoyed", "narrow", "base", "dead")
        call nar(">Hermione bends over slightly and slides her panties down...")
        $ hermione.strip("panties")

    call nar(">You can see that she is doing her best to be graceful...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
    call ctc

    call nar(">Nonetheless you decide to show her some appreciation...","start")
    call nar(">By stroking your cock even faster!","end")
    call her_main("..........", "annoyed", "narrow", "base", "dead")
    call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes.")
    m "{size=-4}(This looks quite impressive actually...){/size}"
    pause.5

    call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements.")
    call ctc

    m "{size=-4}(Did she practise this?){/size}"
    g9 "Oh, what do I care?"
    call nar(">You stroke your diamond-hard cock furiously.")
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "open", "closed", "base", "mid")

    pause.5

    call nar(">Hermione performs another set of movements that could be considered classy...","start")
    call nar(">if not for her naked tits bouncing all over the place.","end")

    g9 "Yes, yes, you little whore!"
    call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")
    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    ">And then Hermione slumps on her butt, completely exhausted."

    hide screen hermione_main
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("Whew... This was--", "open", "closed", "base", "mid", ypos="head", flip=False)
    with hpunch
    g4 "ARGH! YOU FUCKING CUNT!"

    call cum_block
    call gen_chibi("cum","behind_desk","base")
    $ hermione.set_cum(hair="light")
    pause 0.7
    $ hermione.set_cum(face="light")
    pause 1
    $ hermione.set_cum(breasts="light")
    call ctc

    call her_chibi("sit_naked_shocked","on_desk","on_desk")
    call gen_chibi("cum","behind_desk","base")

    call her_main("??!!!", "shock", "wide", "base", "stare")
    call her_main("[genie_name]!!!", "angry", "happyCl", "worried", "mid")

    call gen_chibi("cum_done","behind_desk","base")

    if d_flag_07: #Promised to hold it.
        call her_main("No, [genie_name]! You promised!", "angry", "happyCl", "worried", "mid", ypos="head", flip=False)
        g4 "Oh, man... This was pretty intense..."
        call her_main("You went back on your word, [genie_name]!", "scream", "happyCl", "worried", "mid")
        m "*huh*? What are you talking about?"
        call her_main("How could you do this to me, [genie_name]?", "shock", "base", "angry", "mid", tears="crying_blink")
        m "Oh, calm down, [hermione_name]."
        m "You earned your points today."
        m "Now, just get dressed and leave before somebody discovers you like this."
        call her_main("*sob*!........................", "shock", "narrow", "angry", "R", tears="messy")
        show screen blkfade
        with d5

        $ hermione.wear("all")
        stop music fadeout 5.0
        pause 1.5

        call her_main("... Can I just get paid now, [genie_name]... please?", "annoyed", "narrow", "angry", "R")

        $ her_mood += 20

        jump end_hg_pf_strip

    else:
        call her_main("it's so hot...", "angry", "happyCl", "worried", "mid", ypos="head", flip=False)
        call gen_chibi("hold_dick","behind_desk","base")
        m "Aha... Yeah... This feels great..."
        call her_main("You came all over me...", "soft", "happy", "base", "R")
        call her_main("I am your pupil and...")
        call her_main("You just came on me...", "grin", "narrow", "annoyed", "up")
        g9 "I know! Pretty exciting stuff, *huh*?!"
        call her_main("Nothing of that sort!", "open", "base", "base", "R")
        call her_main("You should have restrained yourself like a proper headmaster would!")
        m "Really? What did you expect me to do?"
        m "Aim at the wall or just put it back in my trousers and start cumming?"
        call her_main("........", "soft", "happy", "base", "R")
        call her_main("Still, you should not have...", "soft", "base", "angry", "mid")
        call her_main("I agreed to perform a striptease for you...", "open", "closed", "base", "mid")
        call her_main("But I didn't agree to be defiled like this.")
        m "I think I know where this is going..."

    call her_main("I demand to be paid extra!", "base", "base", "angry", "mid")
    m "Of course you do..."

    menu:
        m "..."
        "\"You get one extra point.\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("One extra point?", "soft", "base", "angry", "mid")
            call her_main("One meagre extra point for letting you do this to me?", "scream", "happyCl", "worried", "mid")
            call her_main("Now, that is just insulting, [genie_name]!", "soft", "base", "angry", "mid")
            m "One extra point, [hermione_name]. Take it or leave it."
            call her_chibi("sit_naked","on_desk","on_desk")

            call her_main(".............", "annoyed", "narrow", "angry", "R")
            call her_main("I'll take it.", "soft", "base", "angry", "mid")
            $ her_mood += 20
            $ current_payout += 1
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get ten extra points.\"":
            $ current_payout += 10
            call her_main("Ten extra points [genie_name]?", "soft", "base", "angry", "mid")
            call her_main("But that is not even nearly enough!")
            m "Ten extra points. Take 'em or leave 'em [hermione_name]."
            call her_chibi("sit_naked","on_desk","on_desk")

            call her_main("...............", "annoyed", "narrow", "angry", "R")
            call her_main("Well, alright... Better than nothing I suppose...", "soft", "base", "angry", "mid")
            $ her_mood += 10
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get twenty-five extra points.\"":
            $ current_payout += 25
            call her_chibi("sit_naked","on_desk","on_desk")

            call her_main("Yes, I believe this would be an appropriate amount.", "open", "closed", "base", "mid")
            m "are we good then?"
            call her_main("Yes, [genie_name]. Thank you.", "open", "closed", "base", "mid")
            hide screen bld1
            with d3
            call ctc
            show screen blkfade
            with d7
            pause.5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get fifty extra points.\"":
            $ current_payout += 50
            call her_main("Seriously?!", "angry", "wide", "base", "stare")
            call her_chibi("sit_naked","on_desk","on_desk")

            call her_main("Oh, I don't know what to say...", "open", "wide", "base", "stare")
            m "I enjoyed your performance [hermione_name]."
            call her_main("Thank you [genie_name]...", "base", "narrow", "base", "mid_soft")
            m "I also enjoyed plastering your agile little body with cum..."
            call her_main("[genie_name]......", "silly", "happyCl", "worried", "mid", emote="sweat")
            m "So, just allow me to show my appreciation."
            m "Fifty extra points. Well deserved, [hermione_name]."
            call her_main("Thank very much, [genie_name].", "silly", "happyCl", "worried", "mid", emote="sweat")
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You're not getting shit!\"":
            stop music fadeout 1.0
            call her_main("What? Not even my usual pay?", "shock", "wide", "base", "stare")

            menu:
                m "..."
                "\"Oh, no, you are still getting that.\"":
                    $ her_mood += 20
                    call her_main("How generous of you, [genie_name].", "soft", "base", "angry", "mid")
                    hide screen bld1
                    call ctc

                    show screen blkfade
                    with d5
                    $ hermione.wear("all")
                    jump end_hg_pf_strip

                "\"No, not even that!\"":
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("!!!?", "shock", "wide", "base", "stare")
                    call her_main("I danced for you, [genie_name]...")
                    call her_main("I degraded myself for your amusement...", "soft", "happy", "base", "R")
                    call her_main("I let you cum on me...", "open", "base", "base", "R")
                    with hpunch
                    call her_main("And I get NOTHING?!", "clench", "base", "angry", "mid", emote="angry")
                    m "You are dismissed, [hermione_name]!"
                    call her_main("Oh, this is a new low even for you, [genie_name]!", "soft", "base", "angry", "mid")
                    m "I said you are dismissed."
                    call her_main("*GROAN*!", "clench", "base", "angry", "mid", emote="angry")
                    hide screen bld1
                    call ctc

                    show screen blkfade
                    with d5
                    $ hermione.wear("all")

                    call gen_chibi("sit_behind_desk")
                    call her_chibi("stand","desk","base")
                    hide screen blkfade
                    with d5

                    call her_walk(action="leave")

                    $ her_mood += 30

                    jump end_hermione_event
