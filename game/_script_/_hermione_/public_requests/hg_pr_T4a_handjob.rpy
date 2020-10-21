
### Give Classmate A Handjob ###

label hg_pr_handjob:

    # Setup
    $ current_payout = 55

    if hg_pr_handjob.counter == 0:
        m "{size=-4}(Tell her to give a handjob to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)

    #Intro
    if hg_pr_handjob.counter == 0:

        if her_reputation < 12:
            m "[hermione_name], I want you to do something different today..."
            call her_main("...?", "normal", "squint", "angry", "mid")
            m "I want you to give a handjob to one of your classmates."

            jump too_much_public

        m "[hermione_name], I want you to do something different today..."
        call her_main("...........", "soft", "base", "base", "mid")
        g9 "I want you to go out there and have sex with one of your classmates."

        stop music fadeout 0.5
        with hpunch

        call her_main("{size=+5}What?!!{/size}", "shock", "wide", "base", "stare")
        call play_music("hermione") # Music
        call her_main("Now you have done it, [genie_name]! You crossed the line!", "angry", "base", "angry", "mid")
        her "I know I did sell you a couple of rather questionable favours in the past..."
        m "{size=-4}*Heh* a couple she says...{/size}"
        with vpunch
        call her_main("{size=+5}--But THIS?!{/size}", "scream", "base", "angry", "mid", emote="angry")
        her "I cannot believe that you would ask one of your pupils to... to..."
        call her_main("We are done here, [genie_name]!", "angry", "base", "angry", "mid", emote="angry")
        m "Alright, alright, calm down, would you?"
        call her_main("I most certainly will not, [genie_name]! This is beyond inappropriate!", "scream", "closed", "angry", "mid")
        m "Alright, fine, maybe I really did cross some sort of line this time..."
        call her_main("You think [genie_name]?! You think!!?", "angry", "base", "angry", "mid")
        m "Yes, I apologise..."
        call her_main(".........", "annoyed", "narrow", "annoyed", "mid")
        m "How about we try something less... engaging instead?"
        call her_main("............", "upset", "closed", "base", "mid")
        m "I'll be willing to grant Gryffindor {number=current_payout} points."
        m "All I ask in return is..."
        call her_main("..........?", "angry", "base", "angry", "mid", cheeks="blush")
        m "... that you go out there and give some lucky boy a handjob..."
        call her_main("!!!......", "angry", "base", "angry", "mid")
        m "Oh, come on... Just a harmless handjob."
        call her_main("...", "disgust", "narrow", "base", "mid_soft")
        m "{number=current_payout} house points..."
        call her_main("..............", "annoyed", "narrow", "angry", "R")
        call her_main("I am glad that you came to your senses, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
        m "Oh, but of course. Thank you for keeping me in check."
        m "Are you up for it then?"
        call her_main("I am willing to give it a try...", "annoyed", "narrow", "angry", "R")
        m "Splendid... See you tonight then."
    else:
        if her_tier >= 6:
            m "[hermione_name]..."
            m "What do you think about giving one of your classmates another handjob?"
            call her_main("I don't mind, [genie_name].", "annoyed", "narrow", "worried", "down")
            m "Really?"
            call her_main("Yes... I mean, it's just a handjob...", "grin", "base", "base", "R")
            m "Great. Go have fun then!"
            m "And report back to me after your classes, as usual."
            call her_main("Of course, [genie_name].", "base", "happyCl", "base", "mid")
        elif her_tier >= 5:
            m "Ready to go have sex with one of your classmates yet?"

            stop music fadeout 1.0

            call her_main("What?", "scream", "wide", "base", "mid")
            call her_main("Of course not! I would never--", "scream", "closed", "angry", "mid")
            m "How about a handjob then?"
            call play_music("hermione") # Music
            call her_main("...............", "annoyed", "narrow", "angry", "R")
            m "Oh come on. You did it before."
            call her_main("*Hmm*..........", "annoyed", "narrow", "annoyed", "mid")
            her "{number=current_payout} house points?"
            m "Naturally."
            call her_main("Well, alright... I'll see what I can do...", "angry", "narrow", "base", "down")
        else:
            m "Today's favour shall be..."
            call her_main(".........", "angry", "base", "base", "mid")
            m "A Handjob to the boy of your choosing!"
            call her_main("... again?", "angry", "narrow", "base", "down")
            m "Sure, why not?"
            m "And another {number=current_payout} house points for the Gryffindor house of course."
            call her_main("..........", "annoyed", "base", "worried", "R")
            m "So... Are you up for that, [hermione_name]?"
            call her_main("I will see what I can do...", "annoyed", "narrow", "angry", "R")
            m "Splendid!"

    call her_walk(action="leave")

    $ hg_pr_handjob.inProgress = True

    jump end_hermione_event

label end_hg_pr_handjob:
    $ gryffindor += current_payout #55
    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."
    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_handjob.counter == 1:
        show screen blktone
        with d3

        call her_main("..........", "upset", "narrow", "angry", "R", flip=True, trans=d3)
        call her_main("(Do I really have to do this?)", "upset", "closed", "angry", "mid")
        call her_main("*sigh*", "soft", "closed", "angry", "mid")

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_handjob.inProgress = False

    # Increase Points

    if her_tier == 4:
        if her_reputation < 18:
            $ her_reputation += 1

        if her_whoring < 18:
            $ her_whoring += 1

    elif her_tier == 5:
        if her_reputation < 21:
            $ her_reputation += 1

        if her_whoring < 21:
            $ her_whoring += 1

    elif her_tier == 6:
        if her_reputation < 24:
            $ her_reputation += 1

        if her_whoring < 24:
            $ her_whoring += 1

    jump end_hermione_event

label hg_pr_handjob_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you lend a hand to the needy?"
    her "Yes, [genie_name]..."

    if hg_pr_handjob.is_tier_complete():
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_handjob

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_handjob.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        m ".............."

    m "[hermione_name], how did it go?"

    return

### Tier 4 ###

label hg_pr_handjob_T4_E1:

    call hg_pr_handjob_intro

    call play_music("hermione") # Music
    call her_main("Quite awful... of course...", "annoyed", "squint", "angry", "mid")
    m "Just tell me what happened, [hermione_name]..."
    call her_main("I made a complete fool out of myself, that's what happened, [genie_name].", "disgust", "narrow", "base", "mid_soft")
    her "....."
    m "..."
    call her_main("..........", "annoyed", "base", "worried", "R")
    call her_main("I don't want to talk about it...", "annoyed", "narrow", "angry", "R")
    her "You told me to go and touch a boy's penis and I did just that, [genie_name]."
    call her_main("Please, just let me have my points now, [genie_name]...", "open", "base", "base", "mid")
    m "I did not tell you to \"go and touch a boy's penis\", [hermione_name]."
    m "I told you to give one of your classmates a proper handjob."
    call her_main("Well, yes... that was what I meant of course...", "annoyed", "narrow", "annoyed", "mid")
    m "Did you make him cum, then?"
    call her_main("[genie_name]?", "open", "base", "base", "mid")
    m "Did his \"wee-wee\" shoot white stuff at you, [hermione_name]?"
    call her_main("Well...", "annoyed", "base", "worried", "R")
    call her_main("No, it did not...", "normal", "happyCl", "worried", "mid")
    m "Poor guy... Must've blue-balled him."

    menu:
        m "..."
        "\"Well, this doesn't count then.\"":
            stop music fadeout 4.0
            call her_main("What?", "angry", "wide", "base", "stare")
            her "But, [genie_name], I..."
            m "If you didn't make him cum then that wasn't a proper handjob. Period."
            call her_main("But... But what was it then...?", "angry", "base", "base", "mid")
            m "How should I know? A cock massage?"
            call her_main("*Aww*...", "angry", "narrow", "base", "down")
            her "But I really tried my best..."
            m "No handjob - no payment, [hermione_name]."
            call her_main(".....", "angry", "base", "base", "mid")
            m "You are free to go, [hermione_name]."
            call her_main(".........", "annoyed", "narrow", "angry", "R")
            call her_walk(action="leave")

            $ her_mood +=9
            $ hg_pr_handjob.inProgress = False

            jump end_hermione_event

        "\"You shall only get half the payment then.\"":
            $ current_payout = 27

            call her_main("Oh...?", "open", "base", "base", "mid")
            m "Is that a Problem, [hermione_name]?"
            call her_main("N-No [genie_name]... It's only fair I suppose...", "angry", "narrow", "base", "down")
            m "Of course it is!"

            jump end_hg_pr_handjob

        "\"Well, you did try. Here are your points.\"":
            call her_main("Really?", "angry", "base", "base", "mid")
            call her_main("Thank you, [genie_name]!", "open", "narrow", "worried", "down")
            call her_main("I promise, I will try harder next time!", "base", "base", "base", "mid")
            call her_main("*Ehm*... Should you request a similar favour in the future, I mean...", "upset", "wink", "base", "mid")

            jump end_hg_pr_handjob

label hg_pr_handjob_T4_E2:

    call hg_pr_handjob_intro

    call play_music("playful_tension") # Music
    call her_main("It went well, [genie_name]...", "open", "base", "base", "mid")
    her "I asked one if the Gryffindor boys to let me do \"it\" to him..."
    call her_main("To my surprise he agreed eagerly.", "open", "base", "base", "mid", cheeks="blush")
    m "Shocker..."
    call her_main("So we hid behind one of those huge tapestries in the east wing...", "open", "closed", "base", "mid", cheeks="blush")
    call her_main("And I... wanked him until he came...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    her "........."
    call her_main("And I asked him to keep the whole thing a secret, but...", "angry", "base", "base", "mid", cheeks="blush")
    m "What's the matter, [hermione_name]?"
    m "Doubting the honesty of your fellow Gryffindor?"
    call her_main("Of course not, [genie_name].", "upset", "closed", "base", "mid")
    call her_main("...........................", "angry", "narrow", "base", "down", cheeks="blush")
    call her_main("Still... Performing this sort of task could really damage my reputation...", "angry", "base", "base", "mid", cheeks="blush")
    m "Is this your way of asking for a raise, [hermione_name]?"
    m "{number=current_payout} points is as high as I can go with this one."
    call her_main("Oh... Of course...", "angry", "narrow", "base", "down")
    m "Unless, you've changed your mind about having sex with one of your classmates?"
    call her_main("What?", "shock", "wide", "base", "stare")
    call her_main("[genie_name], I am not a prostitute!", "angry", "narrow", "base", "down", cheeks="blush")
    m "Well, in that case..."

    jump end_hg_pr_handjob

label hg_pr_handjob_T4_E3:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    m "[hermione_name], how did it--"
    $ hermione.set_cum(hair="light")
    show screen blktone
    with d3
    call her_main("", "angry", "narrow", "angry", "R", xpos="mid", ypos="base", trans=d3)
    m "...-go."

    call play_music("hermione") # Music
    call her_main("Awful, [genie_name]. Simply awful...", "scream", "happyCl", "worried", "mid")
    m "You've got something... in your hair there..."
    call her_main("*huh*?", "open", "base", "angry", "mid")
    call her_main("Oh, no! I thought I got it all off...", "angry", "happyCl", "base", "mid", cheeks="blush")
    her "One moment..."

    show screen blkfade
    with d3
    pause.5
    $ hermione.set_cum(None)
    call her_main("", "upset", "closed", "base", "mid")
    hide screen blkfade
    with d3

    m "*Hmm*... So I suppose you have completed your task?"
    call her_main("I did, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "What's the problem, then?"
    call her_main("..........", "annoyed", "base", "worried", "R")
    call her_main("All boys are jerks! That is the problem, [genie_name]!", "scream", "closed", "angry", "mid")
    call her_main("I gave this one boy a good wanking...", "open", "narrow", "worried", "down")
    her "And do you know how he thanked me?"
    call her_main("He got his spunk all over me...", "scream", "base", "angry", "mid", emote="angry")
    call her_main("And he did that on purpose, I know he did!", "scream", "closed", "angry", "mid")
    call her_main("Nasty, good for nothing Ravenclaws...", "annoyed", "base", "worried", "R")
    m "Well, I'd say a job well done."

    jump end_hg_pr_handjob

### Tier 5 ###

label hg_pr_handjob_T5_E1:

    call hg_pr_handjob_intro

    call play_music("hermione") # Music
    call her_main("*Ehm*...", "open", "base", "base", "mid")
    her "Not yet, [genie_name]..."
    m "Not yet?"
    call her_main("Yes... Let me explain, [genie_name]...", "annoyed", "base", "worried", "R")
    call her_main("*Ehm*... Well...", "open", "base", "base", "mid")
    her "I was jerking this one boy off, in one of the empty classrooms..."
    her "And that nasty ghost Peeves walked in..."
    call her_main("Or rather flew in on us...", "annoyed", "base", "worried", "R")
    call her_main("And as soon as he realised what I was doing to the boy...", "open", "base", "base", "mid")
    her "He started to yell obscenities at us..."
    her "So we had to leave in a hurry..."
    m "I see..."
    call her_main("That is not all, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "Go on..."
    call her_main("Well, I sort of made a promise to the boy...", "open", "narrow", "worried", "down")
    her "I promised to meet him after my classes and..."
    call her_main("... and finish what I have started...", "annoyed", "narrow", "annoyed", "mid")
    m "I see..."
    m "Did you?"
    call her_main("No, [genie_name]. Not yet at least...", "angry", "base", "base", "mid")
    her "I am supposed to meet him as soon as we are done here, [genie_name]."
    m "*Hmm*..."
    call her_main("So if you could just give those points in advance...", "angry", "narrow", "base", "down")
    her "I would go meet with the boy right away and..."
    call her_main("And give him a proper handjob...?", "open", "base", "base", "R", cheeks="blush")

    menu:
        "\"No. You failed this favour, [hermione_name].\"":
            stop music fadeout 3.0

            call her_main("B-but...", "open", "base", "base", "mid", cheeks="blush")
            call her_main("But I gave him my word...", "angry", "wide", "base", "stare")
            her "I swore on Godric Gryffindor's name..."
            call her_main("And now I will have to give him a wank no matter what...", "angry", "narrow", "base", "down")
            m "Well, I didn't force you to give him that promise, did I?"
            call her_main("......", "angry", "base", "base", "mid")
            call her_main("This is just not fair!", "scream", "happyCl", "worried", "mid")

            call her_walk(action="leave")

            $ her_mood += 20
            $ hg_pr_handjob.inProgress = False

            jump end_hermione_event

        "\"Alright, I think I can trust you.\"":
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            her "I knew you would understand."
            m "Just make sure you finish your job properly this time."
            call her_main("Of course, [genie_name]. I will give him the wank of his life, I promise!", "base", "happyCl", "base", "mid")

            jump end_hg_pr_handjob

label hg_pr_handjob_T5_E2:

    call hg_pr_handjob_intro

    call play_music("hermione") # Music
    call her_main("I did, [genie_name]...", "open", "closed", "base", "mid")
    call her_main("Although I am still not sure how I feel about all of this...", "annoyed", "base", "worried", "R")
    m "Your personal feelings are of no concern to me, [hermione_name]."
    m "Just tell me how it went."
    call her_main("Well, there is not much to tell. [genie_name]...", "open", "base", "base", "mid")
    call play_music("playful_tension") # Music
    her "Today I gave another handjob to one of my classmates..."
    call her_main("Me, Hermione Granger...", "open", "narrow", "worried", "down")
    call her_main("Giving free handjobs in the school's restroom...", "angry", "narrow", "base", "down")
    m "Wait. What do you mean by \"free\"?"
    call her_main("Oh, of course... I get paid with house points for this...", "angry", "base", "base", "mid")
    her "But nobody knows about that..."
    her "And to everyone else this just looks like some harlot who does this for fun..."
    call her_main("They must think I am a slut...", "open", "narrow", "worried", "down")
    call her_main("..............", "clench", "narrow", "base", "down")
    call her_main("Do you think I'm a slut, [genie_name]?", "open", "happy", "base", "mid", cheeks="blush")

    menu:
        m "(*Hmm*..)"
        "\"What? Of course not, [hermione_name]!\"":
            call her_main("..............", "base", "base", "base", "R", cheeks="blush")
            call her_main("You are right, [genie_name]...", "base", "narrow", "worried", "down")
            her "I am making this sacrifice for the glory of the Gryffindor house."
            call her_main("I am not taking pleasure in this sort of activity...", "soft", "narrow", "annoyed", "up")
            call her_main("Because if I would...", "annoyed", "narrow", "angry", "R")
            her "That would mean I really am a slut..."
            call her_main("And I am not...", "angry", "narrow", "base", "down")
            her "......"
            her "I am not a slut..."

        "\"A slut? No... Not yet.\"":
            call her_main("\"Not yet\"??!", "angry", "base", "base", "mid")
            call her_main("..........", "angry", "narrow", "base", "down")
            call her_main("Well, of course!", "scream", "wide", "base", "mid")
            call her_main("You are right, as usual, [genie_name]!", "soft", "base", "base", "mid")
            m "*huh*?"
            call her_main("I have done a few... naughty things...", "open", "base", "base", "mid")
            her "But that does not mean anything!"
            call her_main("...........", "annoyed", "narrow", "angry", "R")

        "\"Yes, that's exactly what you are.\"":
            call her_main("I was afraid that you would say that, [genie_name]...", "mad", "happyCl", "worried", "mid", tears="soft_blink")
            her "But you are wrong, [genie_name]."
            call her_main("You of all people should understand that I take no pleasure in this...", "angry", "base", "base", "mid", tears="soft")
            call her_main("I just do what needs to be done...", "normal", "base", "base", "R", tears="soft")
            $ her_mood = 10

    call her_main("[genie_name], can I just get paid now, please?", "soft", "base", "base", "R")
    m "Get paid? But you didn't tell me how it went yet?"
    her "I did not?"
    call her_main("[genie_name], I gave a handjob to one of my classmates today...", "open", "base", "base", "mid", cheeks="blush")
    her "I wanked his cock until he came..."
    call her_main("Is that not what you told me to do?", "disgust", "narrow", "base", "mid_soft")
    m "That's exactly what I told you to do, [hermione_name]."
    call her_main("Then I would like to get paid now, please.", "annoyed", "closed", "base", "mid")
    m "........"
    m "Fine..."

    jump end_hg_pr_handjob

label hg_pr_handjob_T5_E3:

    call hg_pr_handjob_intro

    call play_music("hermione") # Music
    call her_main("Yes, [genie_name]. I did.", "open", "closed", "base", "mid")
    m "Great. Tell me more."
    call play_music("playful_tension") # Music
    call her_main("Well, today was a rather busy day...", "open", "base", "base", "mid")
    her "And I had to catch up on some studying..."
    her "So I really had no time to plan this out properly, like I normally would..."
    her "I pretty much just approached the first boy I saw..."
    call her_main("And asked him if he wants me to jerk him off.", "annoyed", "narrow", "angry", "R")
    her "a Few minutes later I was already stroking his hard cock in the restroom stall..."
    m "How very efficient of you..."
    call her_main("Thank you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
    call her_main("So, as I was saying...", "annoyed", "narrow", "angry", "R")
    her "I stroked his cock until he came..."
    call her_main("But after that he said: \"Good job, slut\" and just left me there...", "disgust", "narrow", "base", "mid_soft")
    call her_main("Such a mean thing to do...", "annoyed", "narrow", "angry", "R")
    call her_main("It made me feel so cheap... and used.", "upset", "closed", "base", "mid")
    her "But it gets worse..."
    her "......."
    call her_main("I think on some level it also made me feel good somehow...", "angry", "narrow", "base", "down")
    her "All these favours I have been selling to you lately, [genie_name]..."
    call her_main("... it's starting to affect me.", "angry", "base", "base", "mid")
    her "[genie_name], what is happening to me?"

    menu:
        "\"This is nothing. Stop overthinking it!\"":
            call her_main(".......", "open", "happy", "base", "mid", cheeks="blush")
            call her_main("You are probably right, [genie_name]. As usual...", "base", "base", "base", "R", cheeks="blush")
            her "This does not have to mean anything..."

        "\"That is a natural response...\"":
            call her_main("It is?", "open", "happy", "base", "mid", cheeks="blush")
            m "Of course."
            m "You are a girl and he is a boy..."
            m "You got excited and it made you feel good..."
            call her_main("*Hmm*...", "base", "base", "base", "R", cheeks="blush")
            m "Now if you were to give a handjob and feel completely indifferent about it..."
            m "... that would be... unnatural."
            call her_main("I think you are right, [genie_name].", "open", "happy", "base", "mid", cheeks="blush")
            call her_main("As usual.", "base", "base", "base", "R", cheeks="blush") # :)

        "\"Yes! All goes according to plan!\"":
            call her_main("What?", "angry", "wide", "base", "stare")
            m "What?"
            call her_main("[genie_name], did you just say \"All goes according to plan\"?", "angry", "base", "angry", "mid", cheeks="blush")
            m "Did I?"
            m "Oh, yes, of course."
            m "Ensuring that Gryffindor gets the house cup this year."
            m "That's the plan And thanks to your hard work, [hermione_name]..."
            m "All goes according to my-- I mean, our plan..."
            call her_main("*Hmm*...", "upset", "closed", "base", "mid")

            $ her_mood += 5

    jump end_hg_pr_handjob

### Tier 6 ###

label hg_pr_handjob_T6_intro_E1:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum(hair="light")

    show screen blktone
    with d3
    call her_main("[genie_name]...", "open", "base", "worried", "mid", xpos="mid", ypos="base", trans=d3)
    m "[hermione_name]..."
    call her_main("I did a bad thing today, [genie_name]...", "open", "base", "worried", "R")
    m "Did you now? Do tell..."
    call play_music("playful_tension") # Music
    her "Yes, I did a bad thing... a very bad thing..."
    call her_main("A very bad and foolish thing...", "annoyed", "squint", "angry", "mid")
    her "..."
    m "...................."
    her "......................"
    call her_main("I wanked off one of my best friend's brother...", "angry", "base", "base", "mid", tears="soft")
    m "Interesting..."
    call her_main("Seemed like such a great idea at first...", "angry", "base", "base", "mid", tears="soft")
    her "And Ron was so up for it..."
    call her_main("But if Ginny were to find out... She...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    call her_main("She would most certainly kill me, [genie_name]...", "angry", "base", "base", "mid", tears="soft")
    m "A handjob, *huh*? Are you sure that was all you did?"
    call her_main("[genie_name]?", "angry", "base", "base", "mid", tears="soft")
    m "There is something in your hair..."
    call her_main("What? But I swallowed it all... err...", "soft", "base", "base", "mid", tears="soft")
    call her_main("I mean...", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("*Sigh*", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    her "... I sucked him off, [genie_name]."
    her "I did not plan to... but..."
    call her_main("Ron is always so nice to me...", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("And I wanted to thank him...*Sob*!", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    call her_main("And now Ginny will kill me! *Sob*!", "angry", "base", "base", "mid", tears="soft")
    her "She will kill me, [genie_name]!"
    call her_main("And if she does not I will probably die of shame anyway.", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    her "No, no, no... How will I ever face her...?"
    m "Calm down, [hermione_name]."
    m "I assure you, this is not something a boy would be eager to brag about to his sister."
    call her_main("It is not?", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "Don't be silly, [hermione_name]."
    call her_main("*Hmm*...", "normal", "base", "base", "R", tears="soft")
    call her_main("You are probably right, [genie_name]...", "soft", "base", "base", "mid", tears="soft")
    her "And I made Ron give me his word that he will keep the whole incident a secret..."
    call her_main("So, I think I should just trust him to keep his word...", "open", "base", "worried", "R")
    call her_main("..........", "soft", "base", "base", "R")
    her "..."
    call her_main("Will I get paid for this, [genie_name]?", "base", "base", "base", "mid")
    m "Of course."

    jump end_hg_pr_handjob

label hg_pr_handjob_T6_E2:

    call hg_pr_handjob_intro

    call play_music("hermione") # Music
    call her_main("Yes, I did [genie_name]...", "base", "squint", "base", "mid")
    her "More than once actually..."
    m "More than once?"
    call her_main("Five times, [genie_name]...", "base", "narrow", "base", "mid_soft")
    her "I... got carried away a little I suppose..."
    m "What do you mean \"five times\", [hermione_name]?"
    m "Like... at once?"
    call her_main("No silly. I mean I wanked off five boys today in total, [genie_name].", "base", "squint", "base", "mid")
    m "Very impressive nonetheless, [hermione_name]."
    call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")
    m "You don't expect me to multiply your payment by seven or anything, do you?"
    call her_main("Of course not, [genie_name].", "base", "base", "base", "R", cheeks="blush")
    m "Then why did you do it? Five times no less!"
    call her_main("Well, it sort of just happened...", "open", "happy", "base", "mid", cheeks="blush")
    her "I was jerking off this one boy..."
    her "And another boy walked in on us..."
    her "He called his friends..."
    call her_main("One thing lead to another...", "base", "narrow", "base", "mid_soft")
    m "And you ended up jerking off five cocks..."
    call her_main("... yes.", "soft", "narrow", "annoyed", "up")
    m "At the same time?"
    call her_main("*Mhmm*!", "base", "narrow", "annoyed", "mid_soft")
    g9 "And they came on you?!"
    call her_main("You have no idea.", "base", "base", "base", "mid_soft")
    g9 "Well done, miss Granger, absolutely fantastic!"
    call her_main("", "base", "narrow", "base", "mid_soft")

    jump end_hg_pr_handjob

label hg_pr_handjob_T6_E3:

    call hg_pr_handjob_intro

    call her_main("Yes I did, [genie_name].", "base", "base", "base", "mid")
    call her_main("But, *Ehm*...", "open", "base", "worried", "mid")
    m "...?"
    call her_main("Well, I did not just wank off one of my classmates...", "open", "base", "base", "mid")
    her "I........."
    call her_main("...............", "clench", "narrow", "base", "down")
    m "Spit it out, [hermione_name]. The suspense is killing me."
    call play_music("playful_tension") # Music
    call her_main("I sort of did it during class...", "open", "narrow", "worried", "down")
    m "Impressive..."
    call her_main("Sir, you don't understand.  Let me try and explain.", "angry", "narrow", "base", "down")
    her "I don't even know what came over me."

    hide screen blktone
    hide screen hermione_main
    show screen dual_hand_job # CG
    with d5

    call her_main("I was trying to act as nonchalant as I could...", xpos="base", ypos="head")
    her "But, I suddenly had this incredibly pleasant urge to do it during Professor Snape's class."
    her "I couldn't even take notes with my other hand..."
    her "It was wrapped around another thick hot cock too."
    m "You gave two boys handjobs at the same time?!"
    call her_main("Yes Sir.", "angry", "wink", "base", "mid")
    call her_main("And I think I gave them the wank of their life too...", "base", "narrow", "worried", "down")
    her "Because they did not just cum."
    her "Their cocks simply exploded with spunk."
    m "You enjoyed it, didn't you?"
    call her_main("To be completely honest with you, sir... I did.", "grin", "narrow", "base", "dead")
    call her_main("It was exciting.", "smile", "base", "angry", "mid")
    call her_main("God, there was so much.  My hands looked like a candle had dripped hot wax all over them.", "grin", "narrow", "base", "dead")
    call her_main("I didn't know what to do I couldn't just go about the rest of class with huge globs of cum all over my hands.", "angry", "narrow", "base", "down")
    her "So I decided to rub it all over the inside of my thighs to keep from having to stain my clothes."
    call her_main("Every time I walked I could smell their cum from between my legs.", "silly", "narrow", "annoyed", "up")
    m "That's quite an interesting story miss Granger."

    show screen blktone
    hide screen dual_hand_job
    with d5

    call her_main("I definitely want them both at the same time.", "silly", "narrow", "base", "dead")
    m "..."
    call her_main("Yeah, two huge cocks exploding massive loads of cum everywhere.", "silly", "narrow", "annoyed", "up")
    m "........"
    call her_main(".......", "silly", "narrow", "annoyed", "up")
    m "*Ehm*....."
    call her_main("Oh god, I'm sorry [genie_name], I was thinking of something else.", "angry", "wide", "base", "stare")
    m "Yes... sure, okay."
    call her_main("", "base", "base", "base", "mid")

    jump end_hg_pr_handjob
