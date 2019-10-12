

### Admire Breasts ###

label hg_pf_admire_breasts:

    m "{size=-4}(I feel like gazing upon those titties.){/size}"

    if hg_pf_admire_breasts.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu


    # Start Event
    $ current_payout = 10
    $ hg_pf_admire_breasts.start()


    # End Event
    label end_hg_pf_admire_breasts:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call set_her_action(None)
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_tier <= 2:
        call her_main("..................", "annoyed", "base", "worried", "R", xpos="mid", ypos="base", trans="fade")
    elif her_tier <= 5:
        call her_main("", "base", "base", "base", "R", xpos="mid", ypos="base", trans="fade")
    else:
        call her_main("", "base", "narrow", "annoyed", "up", xpos="mid", ypos="base", trans="fade")


    # Points
    $ gryffindor += current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    stop music fadeout 10.0

    if her_tier <= 2:
        call her_main("..................", "annoyed", "base", "worried", "R")
        call her_main("Thank you, [genie_name]...", "open", "base", "base", "R")
    elif her_tier <= 5:
        call her_main("..................", "annoyed", "base", "worried", "R")
        call her_main("Thank you, [genie_name]...", "soft", "base", "base", "mid")
    else:
        call her_main("..................", "base", "happyCl", "base", "mid")
        call her_main("Thank you, [genie_name]...", "soft", "narrow", "base", "mid_soft")

    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=3)

    if her_tier <= 1 and hg_pf_admire_breasts.points == 1:
        call her_main("........................", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    elif her_tier <= 2 and hg_pf_admire_breasts.points == 1:
        call her_main("(How humiliating... What have I become...?)", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    elif her_tier <= 2:
        call her_main("........................", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    elif her_tier <= 3 and hg_pf_admire_breasts.points == 1:
        call her_main("{size=-5}(That was so humiliating...){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main("{size=-5}(No, Hermione, you silly girl!){/size}", "angry", "base", "angry", "mid", cheeks="blush", ypos="head")
        call her_main("{size=-5}(We are doing this to protect the honour of our house!){/size}", "angry", "base", "angry", "mid", cheeks="blush", ypos="head")
        call her_main(".................................", "base", "narrow", "base", "up", cheeks="blush", ypos="head")
    elif aftersperm:
        call her_main("{size=-5}(That was so exhilarating...){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main("{size=-5}(I wonder if anyone will notice my uniform!){/size}", "open", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main("{size=-5}(What will people think of me?){/size}", "open", "narrow", "base", "up", cheeks="blush", ypos="head")
        call her_main(".................................", "base", "narrow", "base", "up", cheeks="blush", ypos="head")

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 1:
        if her_whoring < 3: # Points til 3
            $ her_whoring += 1

    elif her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    jump end_hermione_event



### Tier 1 ###

# Her Bra will stay on for this tier.
# Event 1 (i) - Hermione will remove her vest.
# Event 2 (i) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T1_intro_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name]?"
    call her_main("Yes, [genie_name]...", "normal", "base", "base", "mid")
    m "Has anyone ever told you what sweet-looking breasts you have?"
    stop music fadeout 1.0
    call her_main("!!!", "shock", "wide", "base", "stare")
    g9 "How much would it cost me for you to lift up your top?"
    call her_main("My top?!", "shock", "wide", "base", "stare")
    g9 "And show me what's underneath..."
    call her_main("Why would I-?!", "angry", "wide", "base", "mid")

    call her_main("[genie_name], I refuse to bare my breasts for you!", "open", "closed", "angry", "mid")
    call her_main("How could you even suggest such a thing?!", "angry", "base", "angry", "mid")
    m "Don't you want to earn some house points?"
    call her_main("Yes... But not in a way such as this!", "angry", "narrow", "angry", "R")

    m "I will award \"Gryffindor\" [current_payout] whole house points if you remove your top."
    g9 "Isn't that a steal?"
    call her_main("No it isn't!", "clench", "closed", "angry", "mid", emote="01")
    m "Please?"
    m "You can keep your bra on for all I care..."
    call her_main("And my shirt! I will not remove my shirt either!", "angry", "base", "angry", "mid")
    m "(...)"

    menu:
        "\"Very well, [hermione_name].\"":
            m "Take off your vest then..."

            pass

        "\"That won't be enough, [hermione_name]...\"":
            g4 "I'm not giving \"Gryffindor\" [current_payout] whole points because you took off a vest..."
            call her_main("But-", "open", "wide", "base", "stare")
            m "No buts! You are dismissed."
            call her_main("Please, [genie_name]. I need those points!", "disgust", "worriedCl", "worried", "mid")
            m "Then might I suggest you put in some work to earn them..."
            call her_main("(................)", "annoyed", "narrow", "angry", "R")
            m "Have a nice day, Miss Granger."
            call her_main("(................)", "annoyed", "base", "angry", "mid")
            call her_main("Fine! I'm leaving...", "open", "closed", "angry", "mid")
            call her_main("Good day, Sir.", "angry", "base", "angry", "mid")

            call her_walk(action="leave", speed=2.5)

            $ her_mood += 3
            $ hg_pf_admire_breasts.fail()

            jump main_room

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("(................)", "annoyed", "narrow", "angry", "R")
    pause.4

    # Change Top
    hide screen hermione_main
    $ h_top = "top_2_g"
    call update_her_uniform
    call her_main("", "annoyed", "narrow", "angry", "R")
    call ctc

    m "*Hmmmmm*"
    m "..........."
    call her_main("Sir?", "clench", "base", "angry", "mid")
    g4 "(I wonder what cup size those are.)"
    call her_main("Sir, I would like to have my points now.", "open", "closed", "angry", "mid")
    m "What? Oh yes. Of course..."

    call hide_characters
    show screen blkfade
    with d3

    # Reset Top
    $ h_top = "top_1_g"

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1_intro_E2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name], Is it just me?"
    g9 "Or is it getting really hot in here?!"
    call her_main("Sir...?", "open", "wink", "base", "mid")
    m "Take off your vest for me, would you..."
    call her_main("(...............)", "annoyed", "base", "angry", "mid")
    g9 "And your shirt! Take that off as well!"
    call her_main("Sir, this is a very inappropriate thing to ask of me!!!", "scream", "closed", "angry", "mid")
    m "Yeah, yeah... What else is new..."
    call her_main("Sir!!!", "clench", "wide", "base", "stare")
    m "Please. All I'm asking for is to get a little peek..."
    call her_main("A peek at what?", "open", "base", "angry", "mid")

    menu:
        "\"Your bra!\"":
            g9 "I bet it's really cute..."
            call her_main("(......................)", "clench", "closed", "angry", "mid")

            call her_main("How many points did you say I'd get for this?", "open", "base", "angry", "mid")
            m "[current_payout] points. Just like last time."
            call her_main("But last time I didn't need to show you my bra!", "clench", "base", "base", "mid")
            m "You're correct, Miss Granger."
            m "But as you've already pointed our correctly..."
            g9 "That was last time!"
            m "Now if you would like those points I suggest you remove that top of yours..."
            call her_main("(.............................)", "annoyed", "base", "angry", "mid")
            m "And I expect you to do it today, if you don't mind. I have... *uhm*..."
            m "I have other things to take care off."
            call her_main("Very well, Sir...", "open", "base", "angry", "mid")
            call her_main("I'll do it.", "annoyed", "base", "angry", "mid")

            pass

        "\"Your tits!\"":
            call her_main("W-what?", "shock", "wide", "base", "stare")
            g9 "Your breasts, Miss Granger. I would very much like to see them!"
            call her_main("M-My-... my breasts?!", "angry", "base", "angry", "mid")

            # Hermione gets angry
            call her_main("*Tztzzz!*...", "angry", "closed", "angry", "mid", emote="01")

            call her_main("Good day, Sir.", "scream", "base", "angry", "mid")

            call her_walk(action="leave", speed=2.5)

            $ her_mood += 6
            $ hg_pf_admire_breasts.fail()

            jump main_room

    call hg_pf_admire_breasts_T1

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1_E2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name], how would you like to lift up your top for me?"
    call her_main("Will I be getting points for this, Sir?", "annoyed", "base", "angry", "mid")
    g9 "Of course. [current_payout] points, as always."
    call her_main("(...............)", "annoyed", "base", "angry", "mid")
    call her_main("Very well then.", "angry", "base", "angry", "mid")

    call hg_pf_admire_breasts_T1

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1: # Call label
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main(".............", "annoyed", "base", "worried", "R")
    pause.4

    # Lift top
    $ hermione_wear_bra = True
    call set_her_action("lift_top")

    call her_main("", "annoyed", "base", "worried", "R")
    call ctc

    m "............."
    m "Very good, [hermione_name]."
    call her_main("Can I get my points then?", "disgust", "worriedCl", "worried", "mid")
    m "Of course..."

    return



### Tier 2 ###

# Hermione will bare her breasts after some convincing.
# Event 1 (i) - Choice: Pay Hermione more points to lift up her top without bra.
# Event 2 (i) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T2_intro_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name]?"
    call her_main("Yes, [genie_name]...", "normal", "base", "base", "mid")
    m "How much will it cost me to see your tits?"

    stop music fadeout 1.0
    call her_main("How much will it cost you to...?", "open", "base", "base", "mid")

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]!", "scream", "closed", "angry", "mid")
    m "Hm... I thought your house could use some extra points..."
    m "But I guess I was wrong..."
    call her_main(".........?", "open", "base", "base", "mid")
    m "Please don't mind me..."
    m "All I want to do is help you..."
    call her_main(".............", "annoyed", "base", "worried", "R")
    call her_main("200 house points, [genie_name].", "normal", "worriedCl", "worried", "mid")
    m "So if I give you 200 house points, [hermione_name]..."
    m "You will shamelessly bare your melons before me?"
    call her_main("[genie_name]! No need to be so vulgar!", "angry", "base", "angry", "mid")
    her "I think I'd better go..."

    menu:
        "\"Wait. 200 points are yours. Show me!\"":
            $ current_payout = 200
            call her_main("Really?", "open", "base", "base", "mid")
            m "Well?"
            call her_main("......................................", "annoyed", "base", "worried", "R")
            her "You have to promise me not to touch them, [genie_name]."
            m "Sure, sure..."
            call her_main("I am only doing this for the honour of my house, [genie_name]!", "scream", "worriedCl", "worried", "mid")

            pass

        "\"I will give you 5 points to see your tits.\"":
            call her_main("Five?!", "scream", "wide", "base", "mid")
            call her_main("[genie_name], I am not going to expose myself for a meagre five points!", "angry", "base", "angry", "mid",emote="01")
            m "Well, your tits sure aren't worth 200, [hermione_name]!"
            call her_main("(They aren't?)", "annoyed", "narrow", "worried", "down")
            call her_main("Maybe one hundred - then?", "annoyed", "narrow", "angry", "R")

            menu:
                "\"Fine. 100 it is! Bare them already!":
                    $ current_payout = 100
                    $ her_mood = 0

                    call her_main(".................", "annoyed", "wide", "base", "stare")
                    call her_main("A hundred points...", "annoyed", "base", "base", "R")
                    call her_main("So be it...", "smile", "happyCl", "base", "mid")

                    pass

                "\"25 house points that's my final offer!\"":
                    $ current_payout = 25
                    $ her_mood += 9

                    call her_main("...............", "annoyed", "narrow", "worried", "down")
                    call her_main("Well, so be it...", "clench", "narrow", "base", "down")

                    pass

        "\"Fine, leave. I don't care...\"":
            call her_main("Tsk!", "clench", "closed", "angry", "mid")

            call her_walk(action="leave", speed=2.5)

            $ her_mood += 12

            jump end_hermione_event

    jump hg_pf_admire_breasts_T2



label hg_pf_admire_breasts_T2_intro_E2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name], how would you like to show me your breasts again?"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("I'd rather not, [genie_name]...", "annoyed", "narrow", "annoyed", "mid")
    m "Are you sure?"
    g9 "You could earn 25 house points for it!"
    call her_main(".............", "annoyed", "base", "worried", "R")

    call her_main("Very well, [genie_name].", "angry", "base", "angry", "mid")
    call her_main("But you better keep your hands to yourself!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Don't you dare touch them!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("You need to promise me, [genie_name]!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Of course. I promise I won't touch..."

    $ current_payout = 25

    jump hg_pf_admire_breasts_T2



label hg_pf_admire_breasts_T2_E2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    g9 "[hermione_name], I would very much like to see your breasts again!"
    call her_main(".............", "annoyed", "base", "worried", "R")

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Very well, [genie_name].", "angry", "base", "angry", "mid")
    call her_main("But you are not allowed to touch them!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Promise me, [genie_name]!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Of course. I promise..."

    $ current_payout = 25

    jump hg_pf_admire_breasts_T2







### Tier 3 ###

# Hermione reluctantly show you her breasts.
# You can touch them. But I'd advice you not to.

# Event 1 (i) - Hermione will lift up her top.
# Event 2 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T3_intro_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "annoyed", "narrow", "angry", "R")
    m "I need to see your tits."
    call her_main("............", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Do you promise not to touch, [genie_name]?", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Of course."

    $ current_payout = 25

    jump hg_pf_admire_breasts_T3



label hg_pf_admire_breasts_T3_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "I need to see your tits, [hermione_name]."
    call her_main("Are you only going to watch, [genie_name]?", "angry", "worriedCl", "worried", "mid", cheeks="blush")
    m "Of course..."

    $ current_payout = 25

    jump hg_pf_admire_breasts_T3











### Tier 4 ###

# Hermione is more than ok with showing you her tits now.
# She doesn't mind if you touch them.

# Event 1 (i) - Hermione will lift up her top.
# Event 2 (r) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T4_intro_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "soft", "narrow", "base", "mid_soft")
    m "Did I ever tell you what magnificent tits you have?"
    call her_main("............", "clench", "narrow", "base", "down", cheeks="blush")
    call her_main("Why do you have to be so vulgar, [genie_name]?!", "clench", "worriedCl", "worried", "mid", cheeks="blush")
    m "Just take the compliment and show them to me..."
    call her_main("Yes, [genie_name]...", "base", "narrow", "worried", "down", cheeks="blush")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4



label hg_pf_admire_breasts_T4_E1:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "I need to see your tits, [hermione_name]."
    call her_main("Of course [genie_name].", "base", "narrow", "base", "up", cheeks="blush")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4



label hg_pf_admire_breasts_T4_E2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")

    m "I need to see your tits, [hermione_name]."
    call her_main("Of course [genie_name]", "base", "narrow", "base", "up", cheeks="blush")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4
