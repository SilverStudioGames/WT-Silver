

### Tier 1 ###

label hg_pf_grope_breasts_T1:
    stop music fadeout 1.0
    call her_chibi_scene("grope_tits", trans=d7)
    pause.8

    call her_main("!!!", "normal", "wide", "worried", "shocked")
    call nar(">Hermione takes a hesitant step back...")

    call her_main("!!!?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head", trans=hpunch)
    hide screen bld1
    call ctc

    call nar(">Hermione tries to pull away from you, but you hold her firmly by her breasts...")

    call her_main("??!", "base", "narrow", "base", "up", cheeks="blush")
    call play_music("playful_tension") #SEX THEME.
    call her_main("[genie_name], what are you-?", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="05")
    call nar(">She tries to pull away again.")
    call nar(">You squeeze her tits like a vice.")

    call her_main("[genie_name], you're hurting me!", "angry", "squint", "base", "mid", cheeks="blush")
    g4 "Then stand still, [hermione_name]!"
    call her_main("B-but...", "soft", "wide", "base", "stare")
    m "All I want to do is squeeze your tits a little, then you will get your points!"
    call her_main("B-but... this is...", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Just stand still..."
    m "go to your happy place or something..."
    call her_main("M-my happy place...?", "angry", "wink", "base", "mid")
    call nar(">You feel the girl's shapely breasts in your palms...")

    call her_main("............................", "shock", "happyCl", "worried", "mid", ypos="head")

    menu:
        "-Squeeze her tits with all of your strength-":
            $ her_mood += 6
            call nar(">You put strength into your hold...")
            call her_main("my...........", "disgust", "narrow", "base", "down", cheeks="blush")
            call nar(">You squeeze her tits even harder...")
            call her_main("[genie_name], you're hurting them...", "shock", "happyCl", "worried", "mid")
            m "Be quiet [hermione_name]..."
            call her_main("Ouch..............", "disgust", "narrow", "base", "down", cheeks="blush")
            call nar(">You squeeze her ample tits with all your strength.")
            call her_main("Ah! It hurts!", "angry", "squint", "base", "mid", cheeks="blush")
            call her_main("They're gonna burst! Please stop it!", "angry", "squint", "base", "mid", cheeks="blush")
            m "They are not going to burst, you silly girl..."
            call nar(">You loosen your grip a little...")
            call her_main("It hurts...", "shock", "happyCl", "worried", "mid")
            m "You will be fine..."
            call her_main(".........", "annoyed", "narrow", "angry", "R", cheeks="blush")

            jump end_hg_pf_grope

        "-Give her tits a tender massage-":
            $ her_mood += 3
            call nar(">You start massaging Hermione's beasts through her clothes...")
            call her_main("[genie_name]...?", "shock", "happyCl", "worried", "mid")
            m "The points, [hermione_name]... You need the points. Concentrate on that."
            call her_main("Yes...", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call her_main("Yes, for the honour of the gryffindor house...", "angry", "happyCl", "worried", "mid", cheeks="blush")
            "*Squeeze-squeeze!*"
            call nar(">You keep massaging her tits...","start")
            call nar(">You give one of her breasts a few pinches trying to locate the nipple...","end")
            call her_main("[genie_name]... you're pinching me...?", "shock", "happyCl", "worried", "mid")
            call nar(">Your attempts prove to be fruitless though. The fabric of her clothes is quite thick...")
            call her_main("gryffindor ............", "angry", "happyCl", "worried", "mid", cheeks="blush")

            jump end_hg_pf_grope

        "-Let her go and give her the points-":
            m "Well if you gonna make a drama out of this, you might as well leave..."
            call nar(">You unhand the girl's breasts...")
            call her_main("Thank you...", "soft", "closed", "base", "mid", cheeks="blush")
            m "But you didn't earn them today..."
            call her_main("...............", "annoyed", "base", "angry", "mid", cheeks="blush")

            jump end_hg_pf_grope

### Tier 2 ###

label hg_pf_grope_breasts_T2: # Favor fails if you Slap them.
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_front", trans=d7)

    if hg_strip.trigger:
        menu:
            "\"First, lift up your top\"" if hermione.is_worn("top"):
                call her_main("Sir?!", "clench", "base", "base", "mid")
                m "What? It's not like I haven't seen them before..."
                call her_main("But!", "clench", "narrow", "base", "down")
                call play_music("playful_tension") # SEX THEME.
                m "I just want to massage them a little..."
                call her_main("...............................", "annoyed", "narrow", "base", "down")
                call her_main("Promise me you will be gentle with them.", "soft", "narrow", "base", "mid_soft")
                m "Sure..."

                $ hermione.strip("top")
                if hermione.is_worn("bra"):
                    m "Now your bra..."
                    $ hermione.strip("bra")

                call her_chibi_scene("behind_desk_show_tits", trans=d5)
                call ctc

            "\"Yes, let me feel them!\"":
                pass

    pause.5

    call bld
    menu:
        m "..."
        "-Grab them-":
            jump hg_pf_grope_breasts_T2_continue

        "-Slap them-":
            pass


    # Event fails
    call nar(">You give Hermione's tits a loud slap!")
    call slap_her

    $ her_mood += 10
    call her_main("!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("Ouch! It hurts! *SOB!*", "angry", "base", "worried", "mid", cheeks="blush")
    m "Did you like it though?"
    call her_main("Did I... \"like it\", [genie_name]..?", "annoyed", "narrow", "annoyed", "mid")
    call her_main("What girl in her right mind would like to be treated this way?")
    stop music fadeout 1.0

    $ hermione.wear("all")
    call her_chibi_scene("reset","desk","base", trans=fade)
    pause.5

    call her_main("You are a mean and demented old man!", "angry", "base", "angry", "mid", cheeks="blush", tears="soft", xpos="mid", ypos="base")
    m "............"

    call her_walk(action="leave")

    call bld
    m "Well, no points for Gryffindor then..."

    jump end_hermione_event

label hg_pf_grope_breasts_T2_continue:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    call her_main("..............................", "angry", "narrow", "base", "down")
    m "You have great tits, [hermione_name]..."
    call her_main("....................................", "angry", "narrow", "base", "down")
    m "You like it when I squeeze them like this?"
    call her_main("Excuse me, [genie_name], but you are confusing me with one of those lowly harlots again...", "upset", "closed", "base", "mid")
    call her_main("I am only letting you fondle me because I am getting paid for it...", "upset", "closed", "base", "mid")
    call her_main("Not because I enjoy it...", "upset", "closed", "base", "mid")
    m "I see..."
    m "So, you're more like a prostitute then..."
    call her_main("[genie_name]!", "angry", "wide", "base", "stare")
    call her_main("Prostitutes are paid to have sex with men...", "angry", "wide", "base", "stare")
    call her_main("I'd never do something like that!", "upset", "closed", "base", "mid")

    call nar(">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs.")

    call her_main("Ah...", "open", "happyCl", "worried", "mid")
    m "Enjoying yourself, [hermione_name]?"

    call her_main("[genie_name], I am only doing this-", "upset", "closed", "base", "mid")

    call nar(">You squeeze both of her tits with force...")

    call her_main("ah...", "shock", "happyCl", "worried", "mid")
    m "Tell me you like this, [hermione_name]!"
    call her_main("[genie_name], I am only letting you do this to me because-", "open", "happyCl", "worried", "mid")
    m "I know, I know..."
    m "You are starting to sound like a broken record."
    call her_main("....", "annoyed", "narrow", "annoyed", "mid")

    call nar(">You let go of the girl's breasts...")

    jump end_hg_pf_grope

### Tier 3 ###

label hg_pf_grope_breasts_T3:
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    call her_main("............", "base", "narrow", "worried", "down", cheeks="blush", ypos="head")

    call play_music("playful_tension") # SEX THEME.
    if hermione.is_worn("top") or hermione.is_worn("bra"):
        call nar(">Hermione shifts to start undoing her clothes...")

        menu:
            "\"That's right, take it off!\"":
                $ hermione.strip("top")

                if hermione.is_worn("bra"):
                    g9 "Show them to me at once!"
                    her "......."
                    $ hermione.strip("bra")
                pass

            "\"No, leave it on.\"":
                m "I want to massage them while you are fully dressed..."
                call her_main("Oh, I see...", "base", "base", "base", "R", cheeks="blush", ypos="head")
                jump hg_pf_grope_breasts_T3_clothed

    jump hg_pf_grope_breasts_T3_naked

label hg_pf_grope_breasts_T3_naked:
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_show_tits", trans=d7)
    call ctc

    call play_music("playful_tension") # SEX THEME.

    hide screen hermione_main
    show screen blktone
    call her_main(xpos="mid", ypos="base")
    call ctc

    menu:
        m "..."
        "-Grab them-":
            jump hg_pf_grope_breasts_T3_continue

        "-Slap them-":
            pass

    show screen blktone
    call nar(">You give Hermione's tits a loud slap!")
    call slap_her

    call her_main("!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("Ouch!", "angry", "base", "worried", "mid", cheeks="blush")
    call her_main("[genie_name], what did you do this for?")
    m "Dunno... Seemed like a good idea..."
    m "Did you like it?"
    call her_main("...Of course, not, [genie_name].", "annoyed", "closed", "base", "mid")
    m "Let's try this again, then."
    call her_main("What?", "annoyed", "base", "base", "mid")
    call slap_her

    call her_main("!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("Ouch! Stop hurting me!")
    m "Admit that you enjoy it and I will."
    call her_main("But I don't...", "disgust", "narrow", "base", "down")
    call her_main("And if you plan to keep on doing this to me, [genie_name]...")
    call her_main("...then I think I should leave.", "annoyed", "narrow", "annoyed", "mid")
    m "Fine, fine..."

    jump hg_pf_grope_breasts_T3_continue

label hg_pf_grope_breasts_T3_clothed:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    #">Hermione stands in front of you expectantly..."
    #">You reach out for her ample breasts..."
    #">And start massaging them firmly..."

    "*squeeze-squeeze-squeeze*"

    call her_main("................", "base", "narrow", "base", "up", cheeks="blush")

    menu:
        "\"Do you enjoy this, [hermione_name]?\"":
            call her_main("What...?", "base", "base", "base", "R", cheeks="blush")
            call her_main("Oh, I don't mind it...", "base", "base", "base", "R", cheeks="blush")
            "*squeeze-squeeze-squeeze*"
            call nar(">You keep massaging her soft tits...")

            if her_tier <= 5:
                call her_main("I mean, this isn't a big deal, as long as I am getting paid...", "base", "narrow", "base", "up", cheeks="blush")
                if hermione.is_worn("top"):
                    call nar(">You keep on massaging her tits through her clothes...")
                call her_main("A small price to pay for the honour of my house, really......{heart}", "soft", "base", "base", "R", cheeks="blush")
            else:
                m "Really? It seems to me as if you love it."
                call her_main("I wouldn't say that I love it...", "base", "narrow", "base", "up", cheeks="blush")
                if hermione.is_worn("top"):
                    call nar(">You keep on massaging her tits through her uniform...")
                m "What would you say then, [hermione_name]?"
                call her_main("I just like it, {size=-4}a lot{heart}{/size}", "base", "narrow", "base", "up", cheeks="blush")

            jump hg_pf_grope_breasts_T3_continue

        "-Pull on them abruptly with force-":
            call nar(">You give Hermione's tits a sudden but firm pull...","start")
            with vpunch
            call her_main("Ouch....", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="05")
            call nar(">You pull on her tits again. This time much stronger.","start")
            with vpunch
            call her_main("Ouch! [genie_name], what are you trying to do...?", "angry", "happyCl", "worried", "mid", cheeks="blush",emote="05")
            call nar(">You jerk the girl down by her tits with all your strength...","start")
            with vpunch
            with vpunch
            call nar(">Hermione almost loses balance...","end")
            call her_main("*Panting* What are you doing, [genie_name]...?", "open", "base", "base", "R", cheeks="blush")
            call her_main("You don't need to be so rough with me....{heart}", "base", "base", "base", "R", cheeks="blush")

            jump hg_pf_grope_breasts_T3_continue

label hg_pf_grope_breasts_T3_continue:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    call her_main("Ah...", "open", "narrow", "worried", "down")

    call nar(">You squeeze her tits a few more times, then give them a firm tug...")

    call her_main("Ah... [genie_name]...", "open", "base", "base", "mid")
    m "What? You do enjoy this, don't you?"
    call her_main("No... I...", "open", "base", "base", "mid")
    m "Don't you lie to your headmaster, [hermione_name]!"

    call nar(">You squeeze her tits again...")

    call her_main("Ah...", "open", "narrow", "worried", "down")
    call her_main("I am not lying, [genie_name]...", "open", "narrow", "worried", "down")
    call her_main("Why would I enjoy this?", "open", "base", "base", "mid")
    m "I don't know [hermione_name]. You tell me."

    call nar(">You keep massaging her breasts...")

    call her_main("Ah... I...", "open", "base", "base", "mid")
    m "Yes, what is it?"
    call her_main("It's... It's nothing, [genie_name]...", "angry", "base", "base", "mid")
    m "Oh, I think it's something."
    m "I think you like me squeezing your tits like this."
    call her_main("[genie_name], please...", "angry", "narrow", "base", "down")

    if daytime:
        call her_main("Classes are about to start...", "angry", "narrow", "base", "down")
    else:
        call her_main("It's getting late...", "angry", "narrow", "base", "down")

    call her_main("Can I go now, [genie_name]? Please?", "angry", "base", "base", "mid")

    m "Sure, go ahead..."
    pause 2
    call her_main("...............", "angry", "narrow", "base", "down")
    pause.2

    call her_main("[genie_name], your are still... Holding me...", "angry", "base", "base", "mid")
    m "Oh, right... my bad...."

    call nar(">You let go of Hermione's breasts...")

    jump end_hg_pf_grope

### Tier 4 ###

label hg_pf_grope_breasts_T4_naked: # No top.
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_show_tits", trans=d7)
    call ctc

    call play_music("playful_tension") # SEX THEME.

    hide screen hermione_main
    show screen blktone
    call her_main(xpos="mid", ypos="base")
    call ctc

    menu:
        m "..."
        "-Grab them-":
            return

        "-Slap them-":
            pass

    show screen blktone
    call nar(">You give Hermione's tits a loud slap!")
    call slap_her

    #elif her_whoring >= 15:
    call her_main("Ah!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("[genie_name], why did you do that?", "grin", "narrow", "base", "mid_soft", cheeks="blush")
    m "Dunno... Seemed like a good idea..."
    m "Did you like it?"
    call her_main("..........", "annoyed", "base", "base", "mid")
    call her_main("I am not a pervert...")
    call nar(">You give Hermione's tits another loud smack!")
    call slap_her

    call her_main("A-ah!!!", "silly", "narrow", "worried", "down", cheeks="blush")
    m "Tell me you like it!"
    her "[genie_name]... I..."
    call nar(">You unleash a whole series of slaps!")

    call slap_her
    call slap_her
    call slap_her

    call nar(">Hermione's tits bounce all over the place, completely out of control")
    call her_main("A-ah!!! Ah!!! A-a-aha!!!", "silly", "narrow", "annoyed", "up", cheeks="blush", tears="soft")
    m "You enjoy this. Admit it."
    call her_main("...........", "base", "narrow", "base", "dead", cheeks="blush", tears="soft")
    call nar(">You smack her tits again.")

    call slap_her
    call slap_her
    call slap_her

    call her_main("A-ah! Yes! I do, I do! A-ah...", "silly", "narrow", "annoyed", "up", cheeks="blush", tears="soft")
    call her_main("...does this mean I'm a pervert, [genie_name]?", "angry", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "What?"
    m "Stop being silly, [hermione_name]."
    m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
    her "......"
    her "Are you sure about that, [genie_name]?"
    m "Yes. Believe me, I know."
    call nar(">You give her tits one more slap!")
    call slap_her

    call her_main("A-ah... Yes... Thank you, [genie_name].", "silly", "narrow", "annoyed", "up", cheeks="blush", tears="soft")
    m "Well... Enough with the slapping for now..."

    return



### Tier 5 ###

label hg_pf_grope_breasts_T5_naked:
    call set_her_action("lift_top")
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    show screen blktone
    call her_main("Ah...", "soft", "narrow", "annoyed", "up")
    m "A bit sensitive today, aren't you?"
    call her_main("I suppose...", "base", "narrow", "base", "mid_soft")
    call her_main("Ah...", "open", "happyCl", "worried", "mid")
    m "You like it when I squeeze them like this?"
    call her_main("I do, [genie_name]... Ah...", "base", "narrow", "base", "mid_soft")
    m "Heh..."
    m "What if I pinch your nipples?"
    call her_main("!!!", "angry", "base", "base", "mid")
    call her_main("Ah! [genie_name]...", "open", "happyCl", "worried", "mid")
    m "And what if I do this?"
    call nar(">You grab the girl by her hard nipples and start pulling...")
    call her_main("Ah... Ah... Ah... [genie_name]...", "shock", "happyCl", "worried", "mid")
    m "What if I pull even harder?"
    with hpunch

    call her_main("Ah... [genie_name], please...", "scream", "wide", "base", "stare")
    call nar(">Hermione clutches the edge of your desk to keep herself from taking a step towards you...")
    m "Good girl..."
    call her_main("*Panting heavily*", "grin", "narrow", "base", "dead")
    m "Do you enjoy this?"
    call her_main("You are hurting me, [genie_name]...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "But do you enjoy it?"

    if her_whoring < 18:
        call her_main("Ah... Yes, [genie_name]... I don't know why, but I do...", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    else:
        call her_main("Ah... Yes, [genie_name]... I love it...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")

    m "Good girl..."
    call nar(">You let go of her nipples...")
    call her_main("Ah...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")

    show screen bld1
    call hide_blktone

    m "This will be all for today, [hermione_name]..."
    call her_main("Oh...?", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "What is it? You look disappointed."
    m "I will pay you of course..."
    call her_main("That's not it, [genie_name]...", "angry", "squint", "base", "mid", cheeks="blush")
    call her_main("It's...", "angry", "squint", "base", "mid", cheeks="blush")

    if daytime:
        call her_main("It's just that I still have some time left before I have to leave for the classes and...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    else:
        call her_main("It's not really that late yet, is it?", "shock", "base", "base", "R", cheeks="blush", tears="soft")

    call her_main("uhm...", "angry", "squint", "base", "mid", cheeks="blush")
    call her_main("...................", "angry", "squint", "base", "mid", cheeks="blush")
    m "You want me to hurt you some more, don't you?"

    if her_whoring < 18:
        call her_main("I don't \"want to\"... ", "shock", "base", "base", "R", cheeks="blush", tears="soft")
        call her_main("But if you insist [genie_name]...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
        m "Well, I do insist... apparently."
    else:
        call her_main("Yes please, [genie_name]!", "shock", "base", "base", "R", cheeks="blush", tears="soft")
        call her_main("I'll even let you do it for free...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
        m "Well, in that case..."

    call her_main("Ah...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")

    call nar(">You spend some more time with Hermione's breasts...")

    return
