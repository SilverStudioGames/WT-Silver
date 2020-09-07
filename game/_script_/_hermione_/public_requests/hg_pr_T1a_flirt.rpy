
### Flirt With Classmate ###

label hg_pr_flirt:

    # Setup
    $ current_payout = 5

    if hg_pr_flirt.counter == 0:
        m "{size=-4}(Ask her to go flirt with some boys from Slytherin?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("Yes?", "soft", "base", "base", "R")

    #Intro.
    if hg_pr_flirt.counter == 0:
        m "What is your opinion on the boys of the Slytherin house?"
        call her_main("I detest them, [genie_name].", "angry", "base", "angry", "mid")
        m "Well, too bad. Because I want you to get really friendly with a few of them today."
        call her_main("If I must...", "soft", "base", "base", "R")
        her "Yes, I think I can manage to be civil with them for one day."
        m "Yes, and when I say \"get friendly with them...\""
        m "I actually mean that I need you to flirt with them..."
        call her_main("Flirt?!", "shock", "wide", "base", "stare")
        call her_main("[genie_name]!", "angry", "base", "angry", "mid")
        call her_main("I'm not even going to ask why you'd be interested in this, [genie_name]...", "annoyed", "squint", "base", "mid")
        call her_main("But why Slytherin?", "open", "base", "worried", "mid")
        her "If you need me to be flirtatious today, I think I can manage that..."
        her "But, please, can't it be another house?"
        call her_main("Gryffindor maybe?", "upset", "wink", "base", "mid")
        m "I am only trying to protect your reputation, [hermione_name]."
        call her_main("[genie_name]?", "soft", "base", "base", "mid")
        m "Do you value the opinion the Slytherin students have of you?"
        call her_main("I couldn't care less about the opinions of those Neanderthals.", "scream", "closed", "angry", "mid")
        m "What about the students of the Gryffindor house?"
        call her_main("Their opinion means the world to me--", "annoyed", "base", "worried", "R")
        call her_main("Oh, I see...", "base", "base", "base", "mid")
        m "Exactly... Just looking out for you [hermione_name]."
        her "*Ehm*... Thank you [genie_name]..."
    else:
        if her_tier >= 3:
            m "I need you to flirt with some boys from Slytherin today."
            her "I'll see what I can do, [genie_name]."
            m "Great. I'll be expecting your report today after classes."
        elif her_tier >= 2:
            m "I need you to go make some new friends at the Slytherin house."
            her "You mean you need me to flirt with the Slytherin boys again [genie_name]?"
            call her_main("Fine.", "upset", "base", "angry", "R")
            call her_main("If I have to, [genie_name]...", "normal", "squint", "angry", "mid")
        else:
            if hg_pr_flirt.counter == 1:
                m "I need you to go make some new friends at the Slytherin house."
                her "You mean you need me to flirt with the Slytherin boys again [genie_name]?"
                m "That's exactly what I need you to do today, [hermione_name]."
                m "Just do it properly this time."
                call her_main("Must I really do this [genie_name]?", "open", "base", "base", "mid")
                m "We have been through this, [hermione_name]."
                m "Going to the Slytherin boys is in your best interest."
                call her_main("Yes, I know, [genie_name].", "open", "closed", "angry", "mid")
                her "But why must I do this at all?"
                m "Nobody is forcing you, [hermione_name]..."
                call her_main("You don't need to remind me of that, [genie_name]...", "angry", "base", "angry", "mid")
                call her_main("Alright if I must... [genie_name]...", "normal", "squint", "angry", "mid")
            else:
                m "I need you to go make some new friends at the Slytherin house."
                her "You mean you need me to flirt with the Slytherin boys again, [genie_name]?"
                call her_main("Must I really do this [genie_name]?", "upset", "base", "worried", "mid")
                m "This again?"
                call her_main("Fine.........", "upset", "base", "angry", "R")
                call her_main("If I must... [genie_name]...", "normal", "squint", "angry", "mid")

    her "Well, I'd better go now. Classes are about to start..."
    call her_walk(action="leave")

    $ hg_pr_flirt.inProgress = True

    jump end_hermione_event

# End Event
label end_hg_pr_flirt:
    $ gryffindor += current_payout

    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_flirt.counter == 1:
        show screen blktone
        with d3

        call her_main("(........)", "disgust", "base", "worried", "down", flip=True, trans=d3)
        call her_main("(I'll need to read about this whole \"flirting\" thing...)", "annoyed", "base", "angry", "L")

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_flirt.inProgress = False

    # Increase Points

    if her_tier == 1:
        if her_reputation < 6:
            $ her_reputation += 1

        if her_whoring < 3:
            $ her_whoring += 1
    elif her_tier == 2:
        if her_reputation < 9:
            $ her_reputation += 1

        if her_whoring < 9:
            $ her_whoring += 1
    elif her_tier == 3:
        if her_reputation < 12:
            $ her_reputation += 1

        if her_whoring < 12:
            $ her_whoring += 1

    jump end_hermione_event

label hg_pr_flirt_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "open", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call her_main("", "normal", "base", "base", "mid")
    m "[hermione_name]..."
    m "Did you complete your task?"
    call her_main("I did as you asked, [genie_name]...", "open", "base", "base", "R")
    call her_main("", "normal", "base", "base", "R")

    if hg_pr_flirt.is_tier_complete():
        menu:
            "\"Great. You earned your points.\"":
                jump end_hg_pr_flirt

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_flirt.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("So *ehm*...", "soft", "base", "base", "R")

    m "How many boys did you flirt with today, [hermione_name]?"

    return

### Tier 1 - LVL 0-3 ###

label hg_pr_flirt_T1_E1:

    call hg_pr_flirt_intro

    call her_main("Well...", "open", "base", "worried", "R")
    her "There was this one freshman boy..."
    her "........."
    m "I'm listening..."
    her "So... I went to him and I said \"Hey, handsome!\"."
    m "And?"
    call play_music("hermione") # Music
    call her_main("He stuck out his tongue and ran off, [genie_name].", "normal", "squint", "angry", "mid")
    m "Did you try to lure him in with a lollipop?"
    call her_main("I did not, [genie_name]...", "open", "base", "worried", "R")
    her "The thought never crossed my mind, but--"
    m "That was a joke, [hermione_name]."
    call her_main(".............", "annoyed", "squint", "angry", "mid")
    m "I told you to flirt with boys {size=+5}your{/size} age!"
    call her_main("I wanted to at first, but...", "normal", "squint", "angry", "mid")
    call her_main("I guess I got scared...", "annoyed", "narrow", "angry", "R")
    her "I mean I despise those Slytherins way too much to flirt with them, [genie_name]!"
    call her_main("I would have to fight my gag-reflex the entire time!", "angry", "base", "angry", "mid")

    menu:
        m "..."
        "\"Fine. Just try harder next time.\"":
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            her "I will, I promise!"

            jump end_hg_pr_flirt

        "\"Favour failed! No points for you!\"":
            stop music fadeout 1.0

            call her_main("I understand...", "normal", "squint", "angry", "mid")
            m "Get out of my sight..."
            call her_main("Yes, [genie_name]... Sorry, [genie_name]...", "annoyed", "squint", "angry", "mid")
            call her_walk(action="leave")

            $ hg_pr_flirt.inProgress = False

            jump end_hermione_event

label hg_pr_flirt_T1_E2:

    call hg_pr_flirt_intro

    call play_music("hermione") # Music
    call her_main("Well, I tried to compliment an upperclassman...", "open", "base", "worried", "R")
    m "Did he appreciate it?"
    call her_main("He called me a \"Gryffindor whore\", [genie_name]!", "angry", "base", "angry", "mid", emote="angry")
    m "I see..."
    m "What did you do then?"
    call her_main("Well, that was not the proper way to address a fellow \"Hogwarts\" student...", "open", "closed", "angry", "mid")
    her "So I told him that I would report him."
    m "A truly captivating story..."
    m "Anything else?"
    call her_main("Yes, there was also this one student at the library...", "annoyed", "squint", "angry", "mid")
    her "He was obviously struggling with a problem..."
    her "So I offered my help..."
    m "And?"
    call her_main("He called me a \"Patronising Gryffindor Whore\", [genie_name]...", "angry", "base", "angry", "mid", emote="angry")
    m "Did you threaten to report him as well?"
    call her_main("Of course, [genie_name].", "open", "closed", "angry", "mid")
    m "*sigh*"
    m "Anything else?"
    call her_main("Well, there was one more incident but the outcome was pretty much the same...", "annoyed", "squint", "angry", "mid")
    m "\"Gryffindor whore\"?"
    call her_main("......... yes, [genie_name].", "disgust", "narrow", "base", "mid_soft")
    m "You are doing it all wrong, [hermione_name]."
    call her_main("I am sorry, [genie_name]. I thought this would be easy...", "annoyed", "narrow", "angry", "R")

    menu:
        m "..."
        "\"Well, at least you are trying.\"":
            call her_main("I truly am...", "angry", "happyCl", "worried", "mid")
            call her_main("But Apparently flirting is not my forte...", "angry", "base", "worried", "down", emote="sweat")

            jump end_hg_pr_flirt

        "\"Favour failed! No points of you!\"":
            stop music fadeout 1.0
            call her_main("You are not going to pay me, [genie_name]?", "open", "base", "worried", "mid")
            call her_main("But, you promised!", "angry", "base", "base", "mid", tears="soft")
            m "And you promised to flirt with the boys, not get bullied."
            call her_main("................", "mad", "happyCl", "worried", "mid", tears="soft_blink")
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            $ her_mood += 10
            $ hg_pr_flirt.inProgress = False

            pause 1.0
            m "..."
            m "Now I feel bad for saying that..."

            jump end_hermione_event

label hg_pr_flirt_T1_E3:

    call hg_pr_flirt_intro

    call her_main("Well, the Slytherin quidditch team was practising in the stadium today...", "open", "base", "worried", "R")
    her "I thought I could sneak into the bleachers and cheer them on..."
    call her_main("But...", "annoyed", "narrow", "angry", "R")
    m "Yes?"

    call play_music("hermione") # Music

    call her_main("A whole flock of those Slytherin harlots was already there, [genie_name].", "angry", "base", "angry", "mid")
    her "They were cheering and yelling..."
    call her_main("And one of them even exposed herself inappropriately to the players, [genie_name]...", "angry", "base", "angry", "mid")
    her "I cannot believe our school accepts such behaviour..."
    m "So... how did this captivating drama end?"
    call her_main("I just left [genie_name]...", "annoyed", "narrow", "angry", "R")

    menu:
        m "*Hmm*..."
        "\"Well, here are your points.\"":
            m "Maybe you didn't do exactly as was asked of you, you at least tried."
            call her_main("Thank you, [genie_name]...", "open", "closed", "base", "mid")

            jump end_hg_pr_flirt

        "\"Favour failed! No points for you!\"":
            stop music fadeout 1.0
            call her_main("I don't feel like I deserved any this time anyway...", "annoyed", "happyCl", "worried", "R")
            call her_main("Can I leave now, [genie_name]?", "annoyed", "base", "worried", "mid")
            m "Dismissed!"
            call her_walk(action="leave")

            $ hg_pr_flirt.inProgress = False

            jump end_hermione_event

### Tier 2 - LVL 3-6 ###

label hg_pr_flirt_T2_E1:

    call hg_pr_flirt_intro

    call her_main("Well, there was this one guy at the library...", "open", "base", "worried", "R")
    her "He was obviously struggling with some assignment, so I offered my help..."
    m "And?"
    call play_music("hermione") # Music
    call her_main("Well, to my surprise he accepted it...", "smile", "happyCl", "base", "mid")
    her "He let me finish the assignment for him..."
    call her_main("While I was working he made a couple of inappropriate comments, but I just smiled in response...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "So, basically, he was the one doing the flirting..."
    call her_main("well... I guess.", "grin", "happyCl", "worried", "mid", emote="sweat")
    call her_main("But, despite my better judgment, I did encourage his improper behaviour...", "base", "base", "base", "mid")
    m "By being quiet?"
    her "Yes, [genie_name]..."
    her "I mean, this does amount to something, right?"
    m "*Meh*..."
    m "What else do you have for me?"
    call her_main("Right...", "annoyed", "narrow", "angry", "R")
    her "Later in a corridor these two other guys complimented my appearance in a very vulgar manner..."
    call her_main("But I just smiled at them...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "You were on the receiving end again, then..."
    m "This is not what I ordered you to do, [hermione_name]."
    call her_main("I know, [genie_name]!", "angry", "happyCl", "worried", "mid", emote="sweat")
    call her_main("But I am so busy. Between the \"MRM\" meetings and the classes...", "annoyed", "narrow", "angry", "R")
    her "I barely have any time--"
    # TODO: Check if this part fits the current story line, Johnny.
    m "Is this all you got for me this time then?"
    call her_main("No, [genie_name].", "annoyed", "narrow", "angry", "R")
    her "On my way here I ran into Draco Malfoy, [genie_name]."
    m "No way!!! (No idea who that is...)"
    her "I forced myself to be friendly with him and..."
    call her_main("We ended up having a decent conversation for a change.", "base", "happyCl", "base", "mid")
    m "I see... That \"Dark-oh\" guy..."
    m "Was he looking at your legs at all?"
    call her_main("What?", "open", "base", "base", "mid")
    m "Did he stare at your legs or not, [hermione_name]?"
    call her_main("*Ehm*... He might have...", "upset", "wink", "base", "mid")
    m "What about your tits?"
    call her_main("[genie_name]!!!", "angry", "base", "angry", "mid")
    m "Fine. You get your points. Keep up the good work."
    call her_main("", "annoyed", "base", "worried", "R")

    jump end_hg_pr_flirt


label hg_pr_flirt_T2_E2:

    call hg_pr_flirt_intro

    call her_main("Well...", "open", "base", "worried", "R")
    her "This morning I did flirt with this one guy..."
    call her_main("Then after the second period there was this other guy...", "soft", "base", "base", "R")
    call her_main("And then something bizarre happened...", "angry", "base", "worried", "mid")
    call play_music("playful_tension") # Music
    her "This angry-looking guy from Slytherin came up to me and asked me out on a date..."
    call her_main("I told him \"no\" at first, but we ended up taking a walk together.", "soft", "base", "base", "R")
    m "Did you enjoy yourself, [hermione_name]?"
    call her_main("I think I did, [genie_name]... To my own astonishment...", "open", "base", "base", "mid")
    call her_main("There was something about his \"devil-may-care\" attitude...", "base", "base", "base", "mid")
    call her_main("He was so confident and calm and...", "base", "happyCl", "base", "mid")
    call her_main("I still loathe the Slytherin house of course!", "angry", "happyCl", "worried", "mid", emote="sweat")
    call her_main("But...", "annoyed", "narrow", "worried", "down")
    her "Maybe some of the students got there by mistake?"
    call her_main("Could the \"sorting hat\" make... miscalculations?", "open", "base", "worried", "R")

    menu:
        "\"Just take your points and go!\"":
            call her_main("................", "normal", "squint", "angry", "mid")

        "\"The almighty hat is never wrong!\"":
            call her_main("Yes, of course... Everybody knows that...", "soft", "base", "base", "R")
            if not hat_known:
                m "(What hat again? I have no fucking clue what's she's blabbing about.)"
                m "(Doesn't hurt playing along...)"

        "\"Could what make what?\"":
            call her_main("Oh, never mind me, [genie_name].", "soft", "base", "base", "R")
            her "Everyone knows that the \"Sorting Hat\" is never wrong."

    jump end_hg_pr_flirt


label hg_pr_flirt_T2_E3:

    call hg_pr_flirt_intro

    call play_music("hermione") # Music
    call her_main("Five guys, [genie_name]!", "smile", "happyCl", "base", "mid")
    m "Really?"
    call her_main("Yes!", "base", "happyCl", "base", "mid")
    call her_main("This one guy this morning.", "base", "happyCl", "base", "mid")
    her "Then another two right after the first period."
    her "And then another one before the third period."
    call her_main("And after that, I had a surprisingly pleasant conversation with one more.", "grin", "base", "base", "R")
    call her_main("That last one was quite smart and well-mannered too.", "base", "happyCl", "base", "mid")
    her "............................"
    her "................"
    call her_main("But I still refuse to change my opinion about the Slytherin house, [genie_name].", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "I'm not asking you to, [hermione_name]."
    her "I am only doing this to help my own house!"
    call her_main("The proud house of \"Gryffndor\"!", "scream", "happyCl", "worried", "mid")
    m "Alright, alright. Calm down, [hermione_name]."
    call her_main("", "base", "happyCl", "base", "mid")

    jump end_hg_pr_flirt

### Tier 3 - LVL 6-X ###

label hg_pr_flirt_T3_E1:

    call hg_pr_flirt_intro

    call play_music("hermione") # Music
    call her_main("Eleven boys, [genie_name]!", "smile", "happyCl", "base", "mid")
    m "Eleven? Really? Your personal best, [hermione_name]."
    call her_main("Yes.", "base", "happyCl", "base", "mid")
    call her_main("Let's see...", "grin", "base", "base", "R")
    her "Those two handsome guys right before the first period started..."
    call her_main("Then I exchanged a few rather inappropriate messages with this other guy, during the first period.", "smile", "narrow", "base", "mid_soft")
    call her_main("After that there was this one other guy...", "grin", "base", "base", "R")
    call her_main("Then those three guys...", "annoyed", "narrow", "worried", "down")
    call her_main("Then one more right before the last period...", "base", "happyCl", "base", "mid")
    call her_main("And finally this last guy that walked me right to your tower, [genie_name]...", "smile", "happyCl", "base", "mid")
    m "So, eleven then?"
    m "Those Slytherin boys are really starting to like you, *huh*?"
    call her_main("I suppose so...", "base", "happyCl", "base", "mid")
    call her_main("Well, not all of them were nice to me at first...", "annoyed", "narrow", "worried", "down")
    call her_main("But I use this one trick to \"tame\" them.", "smile", "narrow", "base", "mid_soft")
    m "A trick you say?"
    call her_main("Yes... Whenever a boy from Slytherin is being mean to me or calls me a name...", "open", "base", "base", "R")
    call her_main("Like so!", "base", "happyCl", "base", "mid")
    her "I just swallow my pride and smile in response."
    m "*Hm*..."
    m "So, if for example, somebody were to call you a \"whore\" you would just smile at them?"
    call her_main("Well, yes, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Yeah, I'm sure that wins them over."
    m "Great job, [hermione_name]."
    call her_main("", "grin", "base", "base", "R")

    jump end_hg_pr_flirt

label hg_pr_flirt_T3_E2:

    call hg_pr_flirt_intro

    call play_music("hermione") # Music
    call her_main("Two dates, seven quite pleasant conversations...", "smile", "happyCl", "base", "mid")

    if hg_pr_kiss.counter >= 1:
        call her_main("And I even let this one guy kiss me on the lips...", "soft", "base", "base", "R", cheeks="blush")
    else:
        call her_main("And I even let this one guy kiss me on the cheek...", "grin", "base", "base", "R")

    m "Quite impressive, [hermione_name]."
    call her_main("I think so too, [genie_name]. Thank you.", "base", "happyCl", "base", "mid")
    call her_main("Oh, and there was also this little freshman kid...", "smile", "happyCl", "base", "mid")
    her "I tried to flirt with him too, but we ended up just chatting..."
    call her_main("He kept calling me \"Miss Hermione\"...", "base", "happyCl", "base", "mid")
    her "So adorable..."
    m "Well, I didn't send you to harass people, [hermione_name]."
    call her_main("I didn't harass--", "disgust", "narrow", "base", "mid_soft")
    call her_main("[genie_name]! Seven flirts and two dates amount to something, don't they?", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Oh, absolutely."
    call her_main("Then I would like to receive my payment now...", "scream", "closed", "angry", "mid")
    call her_main("", "normal", "happyCl", "worried", "mid")

    jump end_hg_pr_flirt

label hg_pr_flirt_T3_E3:

    call hg_pr_flirt_intro

    call her_main("[genie_name], I am sorry, but...", "normal", "happyCl", "worried", "mid")
    call play_music("hermione") # Music
    call her_main("I hate those Slytherin tramps, [genie_name]!", "angry", "base", "angry", "mid")
    m "Tell me what happened."
    call her_main("I don't want to talk about it...", "annoyed", "narrow", "angry", "R")
    m "Tell me what happened, [hermione_name]!"
    call her_main("I don't want to talk about it, [genie_name].", "angry", "base", "angry", "mid", emote="angry")
    call her_main("Please don't make me...", "annoyed", "narrow", "angry", "R")

    menu:
        "\"Fine. I'll let it go for today.\"":
            call her_main("Thank you, [genie_name].", "normal", "happyCl", "worried", "mid")
            m "No luck with the flirting today then?"
            call her_main("Oh, quite the opposite, [genie_name].", "angry", "happyCl", "worried", "mid", emote="sweat")
            call play_music("playful_tension") # Music
            her "One of the boys actually took me to the Slytherin common room today..."
            call her_main("There were at least a dozen of them there...", "normal", "base", "base", "mid")
            call her_main("All of the boys knew who I was...", "open", "closed", "angry", "mid")
            her "I was the centre of attention at first..."
            call her_main("And it felt sort of wonderful...", "base", "narrow", "base", "up")
            call play_music("hermione") # Music
            call her_main("Then a bunch of those Slytherin harlots stumbled in and...", "disgust", "narrow", "base", "mid_soft")
            m "And?"
            call her_main("Well, they started saying stuff and doing things...", "annoyed", "narrow", "angry", "R")
            g9 "\"Doing Things\"? What kind of things?"
            her "Anyway, I had to leave..."
            m "I see..."
            m "Well, I say you deserve your points anyway, [hermione_name]."
            call her_main("", "base", "happyCl", "base", "mid")

            jump end_hg_pr_flirt

        "\"Tell me now, or lose the points!\"":
            call her_main("[genie_name], please, I don't want to discuss this with you, [genie_name].", "disgust", "narrow", "base", "mid_soft")
            m "No one is forcing you, [hermione_name]."
            m "You are free to leave."
            call her_main("{size=-4}(Stubborn old man!){/size}", "angry", "base", "angry", "mid")
            call her_walk(action="leave")

            $ her_mood += 10
            $ hg_pr_flirt.inProgress = False

            jump end_hermione_event
