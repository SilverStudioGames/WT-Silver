

### Hermione Shows Her Backside ###

label hg_pf_look_at_ass: #LV.3 (Whoring = 9 - 11)

    call reset_menu_position

    if hg_pf_look_at_ass.points == 0:
        m "{size=-4}(I feel like checking out that ass.){/size}"
    else:
        m "{size=-4}(I feel like checking out that ass again.){/size}"

    if hg_pf_look_at_ass.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    $ current_payout = 40

    if hg_pf_look_at_ass.points == 0 and her_whoring < 15: # LEVEL 04 # FIRST TIME.

        call bld
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]...", "normal", "base", "base", "mid")
        m "How much will it cost for you to get naked and show me that perfect ass of yours?"
        stop music fadeout 1.0
        if her_whoring < 12:
            call her_main("Get naked and show you my...?", "angry", "wide", "worried", "shocked")
            jump too_much
        else:
            call her_main("Get naked and show you my...?", "open", "base", "base", "mid")

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("[genie_name]!", "scream", "closed", "angry", "mid")
        m "Come on..."
        m "It's not like I haven't seen it all before."
        call her_main("......", "open", "base", "base", "mid")
        call her_main(".............", "annoyed", "base", "worried", "R")
        call her_main("{number=current_payout} house points, [genie_name].", "normal", "happyCl", "worried", "mid")
        m "So if I give you {number=current_payout} house points, [hermione_name]..."
        m "You will shamelessly strip naked and present your lovely ass?"
        call her_main("[genie_name]! There's no reason to be so detestable!", "angry", "base", "angry", "mid")
        her "I think I want fifty points now..."

        menu:
            "\"Fine. 50 points are yours. Show me!\"":
                $ current_payout = 50
                call her_main("Really?", "open", "base", "base", "mid")
                m "Well?"
                call her_main("...", "annoyed", "base", "worried", "R")
                her "You have to promise me not to touch, [genie_name]..."
                m "Sure, sure..."
                call her_main("And you most certainly must not touch yourself!", "scream", "happyCl", "worried", "mid")

            "\"I will give you 40 points to see your ass.\"":
                call her_main("{number=current_payout}?", "annoyed", "squint", "angry", "mid")
                call her_main("Well alright then...", "annoyed", "narrow", "angry", "R")
                call her_main("but if you expect to touch me it'll cost you extra...", "annoyed", "narrow", "worried", "down")
                call her_main("at least one hundred points", "annoyed", "narrow", "angry", "R")

                menu:
                    "\"Fine. 100 it is! strip already!":
                        $ current_payout = 100
                        her "................."
                        call her_main("(I didn't think he'd agree to this...)", "annoyed", "base", "worried", "R")
                        call her_main("W-Well alright then...", "normal", "happyCl", "worried", "mid")
                    "\"40 house points it is then\"":
                        $ current_payout = 40
                        her "Well, so be it."
                        call her_main("but you better keep your hands you yourself...", "annoyed", "narrow", "angry", "R")

            "\"Fine, leave. I don't care...\"":
                her "Tsk!"

                call her_walk(action="leave")

                $ her_mood = +12

                jump end_hermione_event

        m "Alright, alright..."
        if hermione.is_worn("top") or hermione.is_worn("bottom") or hermione.is_worn("panties") or hermione.is_worn("bra"):
            g9 "Just get naked already!"
            call her_main("...","annoyed","narrow", "annoyed", "mid", xpos="mid", ypos="base")
            call her_main("{size=-5}(I can't believe I'm going to strip for him...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")

            if hermione.is_worn("top"):
                $ hermione.strip("top")
                
                call ctc
            
            if hermione.is_worn("bottom"):
                m "That's it [hermione_name], take off your bottoms..."
                call her_main("............", "annoyed", "narrow", "angry", "R", cheeks="blush")
                $ hermione.strip("bottom")
            
                call ctc
                
            if hermione.is_worn("bra"):
                m "Show me your titties too!"
                call her_main("............", "soft", "base", "base", "R", cheeks="blush")
                $ hermione.strip("bra")
                m "Very nice..."
                
                call ctc
                
            if hermione.is_worn("panties"):
                g9 "The grand finale..."
                call her_main(".....", "annoyed", "narrow", "angry", "R", cheeks="blush")
                
                $ hermione.strip("panties")
                
                call ctc
                
                if hermione.is_worn("pubes"):
                    g9 "Nice patch of hair you got there!"
                    call her_main("............", "annoyed", "narrow", "angry", "R", cheeks="blush")
                
        m "Now turn around..."
        call blkfade

        call her_main("", "annoyed", "narrow", "annoyed", "mid")
        call ctc
        her "...................................."

        call hg_show_ass

        jump end_hg_show_ass

    #Second and Third Event
    else: #Whoring 12+ or her_whoring (9+ and .points > 1)

        call her_main(xpos="right", ypos="base")
        pause.5

        if her_whoring < 15:
            m "[hermione_name]?"
            call her_main("Yes, [genie_name]?", "annoyed", "narrow", "angry", "R")
        m "I need to see your ass, [hermione_name]."

        if her_whoring < 15:
            call her_main("............", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call her_main("Do you promise not to touch, [genie_name]?", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "Of course."
        elif her_whoring < 18:
            call her_main("Are you only going to watch, [genie_name]?", "angry", "happyCl", "worried", "mid", cheeks="blush")
            m "Of course..."
        else:
            call her_main("anything for you [genie_name]", "base", "narrow", "base", "up", cheeks="blush")

        if hermione.is_worn("top") or hermione.is_worn("bottom") or hermione.is_worn("panties") or hermione.is_worn("bra"):
            g9 "Just get naked already!"
            call her_main("...","annoyed","narrow", "annoyed", "mid", xpos="mid", ypos="base")
            call her_main("{size=-5}(I can't believe I'm going to strip for him...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")

            if hermione.is_worn("top"):
                $ hermione.strip("top")
                
                call ctc
            
            if hermione.is_worn("bottom"):
                m "That's it [hermione_name], take off your bottoms..."
                if her_whoring < 18:
                    call her_main(".....", "annoyed", "narrow", "angry", "R", cheeks="blush")
                else:
                    call her_main("............", "soft", "base", "base", "R", cheeks="blush")
                $ hermione.strip("bottom")
            
                call ctc
                
            if hermione.is_worn("bra"):
                m "Show me your titties too!"
                if her_whoring < 18:
                    call her_main(".....", "annoyed", "narrow", "angry", "R", cheeks="blush")
                else:
                    call her_main("............", "soft", "base", "base", "R", cheeks="blush")
                $ hermione.strip("bra")
                m "Very nice..."
                
                call ctc
                
            if hermione.is_worn("panties"):
                g9 "The grand finale..."
                if her_whoring < 18:
                    call her_main(".....", "annoyed", "narrow", "angry", "R", cheeks="blush")
                else:
                    call her_main("............", "soft", "base", "base", "R", cheeks="blush")
                $ hermione.strip("panties")
                
                call ctc
                
                if hermione.is_worn("pubes"):
                    g9 "Nice patch of hair you got there!"
                    if her_whoring < 18:
                        call her_main(".....", "annoyed", "narrow", "angry", "R", cheeks="blush")
                    else:
                        call her_main("Thank you, [genie_name]", "soft", "base", "base", "R", cheeks="blush")

        m "Now turn around..."
        call blkfade

        call hg_show_ass

        jump end_hg_show_ass

### SHOW ASS ###

label hg_show_ass:
    label hg_pr_strip_rear_transition:
    call hide_characters
    show screen blkfade
    with d5
    call play_sound("climb_desk")
    pause 1
    
    #
    # TODO: Naked ass sprite
    #

    call her_chibi_scene("behind_desk_back", trans=fade)
    pause.8

    show screen hermione_ass
    with d5
    call ctc

    return

### Tier 2 ###

label hg_pr_strip_T2_rear:

    "Dev Note" "Not in 1.37 - Add T2 intro"

    call hg_pr_strip_rear_transition

    if her_whoring < 18:
        call her_main("....................................","annoyed","narrow", "annoyed", "mid", ypos="head")
    else:
        call her_main("....................................", "base", "closed", "base", "mid", ypos="head")
        call play_music("playful_tension") # SEX THEME.
    call ctc


    menu:
        "\"Grab her ass!\"":
            jump hg_pr_strip_T2_grope_rear

        "\"Keep your hands to yourself, Just look.\"":
            jump hg_pr_strip_T2_admire_rear

        "\"Start jerking off.\"":
            jump hg_pr_strip_T2_masturbate_rear



label hg_pr_strip_T2_admire_rear:
    call nar(">You take a long look at Hermione's naked ass...")
    call ctc

    menu:
        "-\"You have a fantastic ass girl\"-":
            m "you should start wearing shorter skirts to show it off a little..."
            call her_main(".....................", "base", "closed", "base", "mid", ypos="head")
        "-\"Your ass is alright...\"-":
            ">You Look at her ass some more whilst making some disapproving tuts..."
            call her_main(".....................", "annoyed", "squint", "angry", "mid", ypos="head")
            $ her_mood += 3

    call nar(">You stare at her ass for a while longer...")
    call ctc

    m "Alright, you can get dressed now [hermione_name]..."

    if her_whoring < 15 or her_mood > 1:
        call her_main(".............", "annoyed", "base", "base", "mid")
    else:
        call her_main(".............", "base", "closed", "base", "mid")

    jump end_hg_pf_strip


label hg_pr_strip_T2_grope_rear:
    hide screen hermione_ass
    hide screen bld1
    with d3
    pause.2

    call her_chibi_scene("grope_ass_back", trans=d5)

    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
    m "Relax, [hermione_name]. Just stand still!"

    show screen blktone
    show screen hermione_ass
    with fade
    call ctc

    m "Oh... This is a nice ass you've got here..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("No, [genie_name], please! You mustn't do this...", "shock", "happyCl", "worried", "mid")
    m "This won't take long, just stand still and look forward."
    call her_main("[genie_name], I didn't agree to this!", "angry", "base", "angry", "mid", cheeks="blush")
    with hpunch
    call her_main("You must let go of me now!!!", "scream", "base", "angry", "mid", cheeks="blush", emote="01")
    call hide_characters
    show screen blkfade
    with d5

    ">Hermione pulls away from you and covers up hastily."

    call set_her_action("none","update")

    call her_main("I think I'd better go...", "angry", "happyCl", "worried", "mid", cheeks="blush", ypos="head")
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    call bld
    m "Go ahead, [hermione_name]. You've earned your points.'"
    call her_main("Hmmmph...", "angry", "happyCl", "worried", "mid", cheeks="blush", xpos="mid", ypos="base")
    call her_main("You'd have gotten a better look if you could just keep your hands to yourself...", "angry", "base", "angry", "mid", cheeks="blush")
    m "That will be all [hermione_name]..."
    call her_main("......", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("{size=-5}(I guess letting him grab me isn't too bad...{/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")

    $ her_mood += 7

    jump end_hg_pf_strip


label hg_pr_strip_T2_masturbate_rear:
    call hide_characters
    show screen blkfade
    with d5

    $ hermione.strip("top")
    $ hermione.strip("bottom")

    call gen_chibi("jerk_off_behind_desk")
    call play_music("chipper_doodle")
    
    ">You take your cock out and start stroking it..."

    hide screen blkfade
    with d5

    $ her_mood += 2

    #TODO Fix usage of missing screen hermione_ass
    #show screen blktone
    #show screen hermione_ass
    call her_main("Are you enjoying the view [genie_name]", "angry", "wide", "base", "stare", ypos="head")
    m "yes I am [hermione_name]. just stand still and let me look a little longer..."

    call nar(">You stare at Hermione's ass with hunger...")
    call her_main("[genie_name], how much longer do I have to stand here?", "shock", "happyCl", "worried", "mid")
    call nar(">You keep stroking your hard cock...")
    m "Not too much longer now..."
    call her_main("[genie_name]...", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("You're not... touching yourself are you...?", "disgust", "narrow", "base", "down", cheeks="blush")
    m "ah... of course not [hermione_name]. you know I'd never do... such a thing..."
    call her_main("hmmm.....", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("well if you did do such a thing...", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("I'd hope that you would make the right decision...'", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("and not... {size=-5}cum...{/size} on me...", "angry", "happyCl", "worried", "mid", cheeks="blush")

    menu:
        "\"Of course not\"":
            call her_main("good.", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("I mean seeing as how I stripped naked and showed you my...", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("..........", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call her_main("not {size=-5}cumming{/size} on me is the least you could do...", "angry", "base", "angry", "mid", cheeks="blush")

            call nar(">Hermione starts looking at you from the corner of her eye ...")

            call her_main("Are you ready to...", "angry", "squint", "base", "mid", cheeks="blush")
            g4 "Almost there [hermione_name]!"
            call her_main("Do it, [genie_name]... cum for me...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")

        "-Start jerking your cock faster-":
            call nar(">You start jerking your cock furiously!")
            call her_main("...", "scream", "base", "angry", "mid", cheeks="blush", emote="01")
            call nar(">You jerk it even faster!")
            call her_main("you're going to do it aren't you...", "annoyed", "narrow", "angry", "R", cheeks="blush")
            g4 "almost there slut!"
            call her_main("make me stand here...", "angry", "squint", "base", "mid", cheeks="blush")
            call her_main("while you cum all over me!", "angry", "squint", "base", "mid", cheeks="blush")

    call hg_show_ass_cumming

    jump end_hg_pf_strip






### Tier 3 ###

label hg_pr_strip_T3_admire_rear:
    call nar(">You take a long look at Hermione's naked ass...")
    call ctc

    menu:
        "\"Nice little ass you got there.\"":
            call her_main("", "annoyed", "closed", "base", "mid", ypos="head")
            call ctc
            call her_main("Thank you [genie_name].", "base", "closed", "base", "mid")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("(Maybe he should grab it next time...)", "annoyed", "narrow", "annoyed", "mid")

        "\"Hm... I've seen better.\"":
            $ her_mood += 9
            call her_main("Tsk...", "clench", "base", "angry", "mid", ypos="head")
            call her_main("well in that case Are we done?", "open", "narrow", "annoyed", "mid")

    call nar(">You stare at her ass for a while longer...")
    call ctc

    m "Alright, you can get dressed now [hermione_name]..."

    if her_mood > 1:
        call her_main(".............", "annoyed", "base", "base", "mid")
    else:
        call her_main(".............", "base", "closed", "base", "mid")

    jump end_hg_pf_strip


label hg_pr_strip_T3_grope_rear:
    hide screen hermione_ass
    hide screen bld1
    with d3
    pause.2

    call her_chibi_scene("grope_ass_back", trans=d5)

    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
    m "Relax, [hermione_name]. Just stand still!"

    show screen blktone
    show screen hermione_ass
    with fade
    call ctc

    if current_payout < 100:
        $ her_mood += 3
        call her_main("I didn't agree to this, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush", ypos="head")
    else:
        call her_main("I know I agreed to this [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush", ypos="head")
        call her_main("But as the headmaster of this school...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("I don't know if you should be...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Don't you like it...?"
    call her_main("What?", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Don't you like it how I squeeze and pull your cheeks?"
    call her_main("...............", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Admit it, you like it a little bit..."
    m "Maybe even a lot..."
    call her_main("{size=-5}(It feels so weird to let him grope me...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("[genie_name], I am letting you do this to me to help my house!", "shock", "happyCl", "worried", "mid")
    call her_main("It doesn't matter how good it feels...", "shock", "happyCl", "worried", "mid")
    m "So you admit that it does feel good."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Please, let go of me now!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call hide_characters
    show screen blkfade
    with d5

    ">Hermione pulls away from you suddenly and covers up."

    call set_her_action("none","update")

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    if current_payout < 100:
        call her_main("You promised not to grab me, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "It was hard to resist..."
    else:
        call her_main("Even though I agreed to let you grab me, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        call her_main("you didn't need to be so rough...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "sorry, It was hard to resist..."
        call her_main("..........", "base", "closed", "base", "mid")


    if current_payout < 100:
        call her_main("well if you wanted to touch you should have offered to pay me more.", "soft", "base", "base", "R", cheeks="blush", xpos="right", ypos="base")
        call her_main("speaking of which Can I get paid now please?", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="05")
    else:
        call her_main("I'd like to get paid now please [genie_name].", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="05", xpos="right", ypos="base")
    m "Sure..."

    jump end_hg_pf_strip


label hg_pr_strip_T3_masturbate_rear:
    call hide_characters
    show screen blkfade
    with d5

    $ hermione.strip("top")
    $ hermione.strip("bottom")

    call gen_chibi("jerk_off_behind_desk")
    call play_music("chipper_doodle")
    
    ">You take your cock out and start stroking it..."

    hide screen blkfade
    with d5

    show screen blktone
    show screen hermione_ass
    call her_main("Are you enjoying the view [genie_name]", "angry", "wide", "base", "stare", ypos="head")
    m "I'm enjoying it immensely"
    call her_main("[genie_name], are you... touching yourself...", "shock", "happyCl", "worried", "mid")
    m "Don't blame me [hermione_name]..."
    call her_main("well who am I supposed to blame, [genie_name]?", "shock", "happyCl", "worried", "mid")
    call nar(">You pick up the pace...")
    m "Blame yourself [hermione_name]..."
    m "Or rather, blame that perfect little ass of yours!"
    call her_main("..................", "shock", "happyCl", "worried", "mid")
    call her_main("(his cock is so big...)", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Yes... Yes, like that..."
    m "Try shaking it a little..."
    call her_main("..............", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("Well, so be it...", "open", "base", "base", "R", cheeks="blush")
    call her_main("You can keep touching yourself, [genie_name]...", "open", "base", "base", "R", cheeks="blush")
    call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
    call her_main("Not to... em...", "open", "base", "base", "R", cheeks="blush")
    call her_main("Not to cum...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Not on me, [genie_name]...", "angry", "base", "angry", "mid")
    m "Are you sure..."
    m "I bet you'd love to have your ass covered in my cum, wouldn't you!"
    call her_main(".......................", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call nar(">You start to stroke your cock even harder...")
    g4 "Yes, I know you want this! Yes!"
    call her_main("................", "angry", "happyCl", "worried", "mid", cheeks="blush")

    call nar(">You are about to cum...")

    call hg_show_ass_cumming

    jump end_hg_pf_strip




### Tier 4 ###

label hg_pr_strip_T4_admire_rear:
    call nar(">You take a long look at Hermione's naked ass...")
    call ctc

    menu:
        "\"You have an amazing ass, [hermione_name].\"":
            call her_main("You really think so [genie_name]?", "annoyed", "base", "base", "mid", ypos="head")
            call her_main("I am glad you like it, [genie_name]...", "base", "closed", "base", "mid")
        "\"Your ass is ok... I suppose...\"":
            call her_main("Huh?", "annoyed", "base", "base", "mid", ypos="head")
            call her_main("Does this mean you don't like it, [genie_name]?", "annoyed", "base", "base", "mid")
            call her_main("I'm sorry... I'll try to work out some more.", "disgust", "narrow", "base", "down")

    call nar(">You stare at her ass for a while longer...")
    call ctc

    m "Alright, you can get dressed now [hermione_name]..."

    if her_mood > 1:
        call her_main(".............", "upset", "narrow", "worried", "down")
    else:
        call her_main(".............", "base", "narrow", "annoyed", "up")

    jump end_hg_pf_strip


label hg_pr_strip_T4_grope_rear:
    hide screen hermione_ass
    hide screen bld1
    with d3
    pause.2

    call her_chibi_scene("grope_ass_back", trans=d5)

    call her_main("[genie_name], what are you doing?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
    m "Relax, [hermione_name]. Just stand still!"

    show screen blktone
    show screen hermione_ass
    with fade
    call ctc

    call her_main("But...", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    call her_main("ah...{heart}", "shock", "happyCl", "worried", "mid")

    if current_payout < 100:
        call her_main("I didn't agree to this...", "disgust", "narrow", "base", "down", cheeks="blush")
    else:
        call her_main("please [genie_name], not so rough...{heart}", "shock", "happyCl", "worried", "mid")

    m "But you like it, don't you?"

    if her_whoring >= 21:
        call her_main("I love it [genie_name]!{heart}", "open", "base", "base", "R", cheeks="blush")
    else:
        call her_main("maybe... [genie_name]{heart}", "shock", "happyCl", "worried", "mid")

    call nar(">You give her cheeks a couple of firm squeezes...")

    if her_whoring >= 21 or current_payout == 100:
        if current_payout < 100:
            call her_main("[genie_name], you promised not to touch...", "base", "base", "base", "R", cheeks="blush")
            m "I know, I know... but admit it, you wanted me to..."
            call her_main(".................{heart}{heart}{heart}", "base", "narrow", "base", "up", cheeks="blush")
        else:
            call her_main("[genie_name], please...{heart}", "base", "base", "base", "R", cheeks="blush")
    else:
        call her_main("[genie_name], you promised not to touch...", "angry", "happyCl", "worried", "mid", cheeks="blush")
        m "I know, I know... but admit it, you wanted me to..."
        call her_main("ah{heart}... of course not [genie_name]{heart}", "angry", "base", "angry", "mid", cheeks="blush")

    call her_main("mmmm.......................{heart}", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("[genie_name], you need to stop now...", "base", "narrow", "base", "up", cheeks="blush")
    m "Just a bit longer..."

    call nar(">You keep on groping her ass cheeks...")

    call her_main("[genie_name]... please, stop this...", "open", "narrow", "base", "up", cheeks="blush")
    m "Why? Because you like it too much?"
    call her_main("No it's not that...", "base", "base", "base", "R", cheeks="blush")
    call her_main("I mean...", "open", "base", "base", "R", cheeks="blush")

    call nar(">You pull the cheeks apart in opposite directions and then squish them together...")

    call her_main("Ah...{heart} [genie_name], I really need to go... before I-", "base", "narrow", "base", "up", cheeks="blush")

    if daytime:
        call her_main("am late for class... they're about to start...", "open", "base", "base", "R", cheeks="blush")
    else:
        call her_main("am late to bed... It is getting very... late...", "open", "base", "base", "R", cheeks="blush")

    m "Well, alright..."
    call hide_characters
    show screen blkfade
    with d5

    ">You let go of the girl's ass..."
    ">Hermione covers up..."

    call set_her_action("none","update")

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    call play_music("chipper_doodle") # HERMIONE'S THEME.

    if current_payout < 100:
        if her_whoring >= 21:
            call her_main("Please don't think I forgot that you broke your promise, [genie_name].", "base", "base", "base", "R", cheeks="blush")
            call her_main("I expect you to make it up to me later...", "base", "base", "base", "R", cheeks="blush")
        else:
            call her_main("Please don't think I forgot that you broke your promise, [genie_name].", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "Right..."

    jump end_hg_pf_strip



label hg_pr_strip_T4_masturbate_rear:
    call hide_characters
    show screen blkfade
    with d5

    $ hermione.strip("top")
    $ hermione.strip("bottom")

    call gen_chibi("jerk_off_behind_desk")
    call play_music("chipper_doodle")
    
    ">You take your cock out and start stroking it..."

    hide screen blkfade
    with d5

    show screen blktone
    show screen hermione_ass
    call her_main("[genie_name]?", "base", "narrow", "base", "up", cheeks="blush", ypos="head")

    if her_whoring >= 21:
        call her_main("ah...", "base", "narrow", "base", "up", cheeks="blush")
        call nar(">Hermione looks back and sees you stroking your cock.")
        call her_main("It's so big...", "open", "base", "base", "R", cheeks="blush")
        call her_main("You just couldn't help yourself, could you [genie_name]?", "base", "base", "base", "R", cheeks="blush")
        call her_main("..................", "base", "narrow", "base", "up", cheeks="blush")
        m "Yes... Yes, like that..."
        m "Yes, shake that ass [hermione_name]..."
        call her_main("..............", "base", "narrow", "base", "up", cheeks="blush")
        call her_main("well, so be it...", "open", "base", "base", "R", cheeks="blush")
        call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
        call her_main("Not to... ehm...", "open", "base", "base", "R", cheeks="blush")
        call her_main("Not to cum... on me, [genie_name]...", "base", "narrow", "base", "up", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................", "base", "narrow", "base", "up", cheeks="blush")
        ">You start to stroke your cock even harder..."
        g4 "Yes, I know you want this! Yes!"
        call her_main("................", "base", "narrow", "base", "up", cheeks="blush")

    else:
        call her_main("[genie_name], actually I never agreed to this...", "shock", "happyCl", "worried", "mid")
        m "What are you complaining about, [hermione_name]?"
        m "I'm not even touching your ass..."
        call her_main("Yes, but you are... touching yourself, [genie_name].", "shock", "happyCl", "worried", "mid")
        m "Just stand still, you fat-assed bitch."
        m "It will be over soon."
        call her_main("..................", "shock", "happyCl", "worried", "mid")
        m "Yes... Yes, like that..."
        m "Yes, with your ass all naked..."
        call her_main("..............", "disgust", "narrow", "base", "down", cheeks="blush")
        call her_main("well, so be it...", "open", "base", "base", "R", cheeks="blush")
        call her_main("But you must promise me not to...", "soft", "base", "base", "R", cheeks="blush")
        call her_main("Not to... ehm...", "open", "base", "base", "R", cheeks="blush")
        call her_main("Not to discharge...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        call her_main("Not on me, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................", "disgust", "narrow", "base", "down", cheeks="blush")
        call nar(">You start to stroke your cock even harder...")
        g4 "Yes, I know you want this! Yes!"
        call her_main("................", "disgust", "narrow", "base", "down", cheeks="blush")

    call hg_show_ass_cumming

    jump end_hg_pf_strip









### GENIE STARTS CUMMING ###
label hg_show_ass_cumming:

    if her_whoring < 18:
        menu:
            "-Cum on the floor-":
                hide screen blktone
                call blkfade

                g4 "Argh! You fat-assed slut!"
                call her_main("Proff-- ??", "scream", "wide", "base", "stare", cheeks="blush", ypos="head")
                call gen_chibi("cum_behind_desk")
                call cum_block

                g4 "Argh! YES!"

                hide screen bld1
                call hide_blkfade
                call ctc

                call her_main("[genie_name]!", "scream", "base", "angry", "mid", cheeks="blush", emote="01")
                g4 "Oh, that's better..."
                call gen_chibi("cum_behind_desk_done")
                with d3

                call her_main("[genie_name], you came so much...", "angry", "squint", "base", "mid", cheeks="blush")

                hide screen hermione_ass
                hide screen bld1
                hide screen blktone
                with fade
                call ctc

                call bld
                m "Oh, this was quite amazing..."

                call her_main("", "disgust", "narrow", "base", "down", xpos="right", ypos="base")
                pause.5

                her "the floor..."
                her "It's covered...."
                m "all because of your ass, [hermione_name]."
                her "................"
                call her_main("I need to get dressed...", "open", "closed", "base", "mid")
                call ctc

                hide screen hermione_main
                call blkfade

                return

            "-cum on her ass-":

                hide screen blktone
                call blkfade

                g4 "Argh! You fat-assed whore!"
                call her_main("Proff-- ??", "scream", "wide", "base", "stare", cheeks="blush", ypos="head")
                call cum_block

                g4 "Argh! YES!"

                call gen_chibi("cum_close","on_girl","base")
                hide screen bld1
                call hide_blkfade
                call ctc

                $ hermione_ass_cum = True
                call her_main("[genie_name], no, you promised!", "scream", "base", "angry", "mid", cheeks="blush", emote="01")
                g4 "Oh, this is great, yes..."
                call gen_chibi("cum_close_done","on_girl","base")
                call ctc

                hide screen hermione_ass
                call gen_chibi("stand","desk","base")
                call her_chibi("stand","mid","base")
                hide screen bld1
                hide screen blktone
                with fade
                call ctc

                call bld
                m "Oh, this was quite amazing..."
                call her_main("", "disgust", "narrow", "base", "down", xpos="right", ypos="base")
                pause.5

                if her_whoring < 15:
                    call her_main("How could you do this to me, [genie_name]?!", "scream", "base", "angry", "mid")
                    call her_main("My ass is covered in cum!", "angry", "base", "angry", "mid")
                else:
                    call her_main("[genie_name], how could you...?", "angry", "squint", "base", "mid", cheeks="blush")
                    call her_main("My ass...", "disgust", "narrow", "worried", "down")
                    call her_main("It's covered....", "disgust", "narrow", "base", "down")

                m "Don't worry, I will give you your house points, [hermione_name]."
                m "You did good."
                her "................"
                call ctc

                hide screen hermione_main
                call blkfade

                if her_whoring < 15:
                    $ her_mood += 20
                else:
                    $ her_mood += 10

                return


    #Third Event.
    else: #18+

        menu:
            g4 "Argh! (I'm about to cum!)"

            "-Hold it in-":
                g4 "Oh, alright..."
                g4 "I'd better stop now I suppose..."
                call her_main("...............", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
                call her_main("Ehm... I mean I know I said not to cum on me...", "disgust", "narrow", "base", "down", cheeks="blush")
                m "Huh?"
                call her_main("But I wouldn't mind if you ...", "shock", "happyCl", "worried", "mid")
                call her_main("Came...", "disgust", "narrow", "base", "down", cheeks="blush")
                call her_main("On my ass--", "base", "base", "base", "R", cheeks="blush")
                g4 "Argh! You whore!"
                call her_main("???", "mad", "wide", "base", "stare", cheeks="blush")
                call cum_block

                g4 "Argh! YES!"

                $ hermione_ass_cum = True
                call gen_chibi("cum","on_girl","base")
                hide screen hermione_ass
                hide screen bld1
                hide screen blktone
                hide screen blkfade
                with d3
                call ctc

                show screen blktone
                show screen hermione_ass
                with fade

                call her_main("that's it [genie_name], release your... semen on me...", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="05")
                g4 "Oh, this is great, yes..."
                call her_main("ah{heart}, what's done is done I suppose...", "base", "base", "base", "R", cheeks="blush")

            "-Just start cumming-":
                g4 "Argh! You fat-assed whore!"
                call her_main("???", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
                call cum_block

                g4 "Argh! YES!"

                $ hermione_ass_cum = True
                hide screen hermione_ass
                call gen_chibi("cum","on_girl","base")
                hide screen bld1
                hide screen blktone
                hide screen blkfade
                with d3
                call ctc

                show screen blktone
                show screen hermione_ass
                with fade

                call her_main("ah...{heart} It's so hot...{heart}", "shock", "happyCl", "worried", "mid")
                call her_main("there's so much...{heart}", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="05")
                g4 "Oh, this is great, yes..."
                call her_main("ah...{heart}", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="05")

                call her_main("Well, what's done is done I suppose...", "angry", "happyCl", "worried", "mid", cheeks="blush")

        hide screen hermione_ass
        call gen_chibi("stand","desk","base")
        call her_chibi("stand","mid","base")
        hide screen blktone
        with fade
        pause.5

        call bld
        m "Oh, this was quite amazing..."
        call her_main("", "disgust", "narrow", "base", "down", xpos="right", ypos="base")
        pause.5
        her "My ass is covered though..."
        m "Don't worry, it still looks great, [hermione_name]."
        m "Maybe even better now..."
        call her_main("Thank you [genie_name].", "base", "closed", "base", "mid")
        call her_main("although I do need to clean myself up...", "annoyed", "closed", "base", "mid")
        call ctc

        hide screen hermione_main
        call blkfade

        return



### END SHOW ASS ###

label end_hg_show_ass:
    $ hermione_ass_cum = False

    hide screen hermione_main
    hide screen hermione_ass

    call set_her_action("none","update") #Resets clothing.

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen blkfade
    call her_main(xpos="right", ypos="base",trans=fade)

    if her_whoring < 24:
        if her_whoring < 18:
            call her_main("Can I have my payment now?", "base", "narrow", "base", "up", cheeks="blush")
            if current_payout < 100:
                $ her_mood +=7

        $ gryffindor +=current_payout
        m "The Gryffindor house gets {number=current_payout} points!"
        stop music fadeout 10.0

        call her_main("..................", "annoyed", "base", "worried", "R")
        her "Thank you, [genie_name]..."

    else:
        call her_main("..................", "base", "happyCl", "base", "mid")


    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."

    call her_walk("door", "base")

    #First event.
    if her_whoring < 15:
        call her_main("(How degrading... why do i keep agreeing to this...?)", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")

    #Second event.
    elif her_whoring < 18:
        call her_main("........................", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")

    #Third event.
    elif her_whoring >= 18 and aftersperm:
        call her_main("{size=-5}(That was so exhilarating...){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main("{size=-5}(i wonder what he'll ask me to do next...?){/size}", "open", "narrow", "base", "up", cheeks="blush", ypos="head")

    else:
        call her_main("{size=-5}(That was so exhilarating...) {/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main("{size=-5}(No, Hermione, you silly girl!) {/size}", "angry", "base", "angry", "mid", cheeks="blush", ypos="head")
        call her_main("{size=-5}(it was shameful! good girls don't get turned on by stripping for their headmaster!) {/size}", "angry", "base", "angry", "mid", cheeks="blush", ypos="head")
        call her_main(".................................", "base", "narrow", "base", "up", cheeks="blush", ypos="head")

    call her_chibi("leave")


    $ hg_pf_look_at_ass.level = 1 #Event hearts level (0-3)

    if her_whoring >= 12 and her_whoring < 15:
        $ hg_pf_look_at_ass.level = 1 #Event hearts level (0-3)

    if her_whoring >= 15 and her_whoring < 18:
        $ hg_pf_look_at_ass.level = 2 #Event hearts level (0-3)

    if her_whoring >= 18:
        $ hg_pf_look_at_ass.level = 3 #Event hearts level (0-3)


    if her_whoring < 15:
        $ her_whoring +=1

    $ hg_pf_look_at_ass.points += 1

    # Stats
    $ hg_pf_look_at_ass.counter += 1

    jump end_hermione_event
