

### Let Cho Strip ###

label cc_pf_strip:

    # Start Event
    $ cc_pf_strip.start()

    # End Event Jump
    label end_cho_strip_event:

        if cho_tier == 2 and cho_whoring < 9: # Points til 9
            $ cho_whoring += 1

        if cho_tier == 3 and cho_whoring < 15: # Points til 15
            $ cho_whoring += 1

    $ cho.wear("all") # Reset clothes
    jump end_cho_event

# TODO: Add Fail events as Tier 1, currently named Tier 1 events become Tier 2.

### Tier 1 (pre Slytherin) ###

label cc_pf_strip_T2_intro_E1:
    m "It's time for your next favour, [cho_name]."
    call cho_main("Of course, [cho_genie_name].", "base", "base", "base", "mid")
    call cho_main("What would you like me to do?", "soft", "base", "base", "mid")
    m "First, come a bit closer..."
    call cho_main("Very well, Sir.", "base", "base", "base", "mid")

    call cho_walk("desk", "base")

    call cho_main(xpos="mid", ypos="base", trans=fade)
    call ctc

    m "How often do you typically exercise, Miss Chang?"
    call cho_main("As often as I can, [cho_genie_name]!", "soft", "base", "base", "mid")
    m "Which is... how often, exactly? Twice a week?"
    call cho_main("Three times a day, Sir!", "base", "narrow", "base", "mid")
    with hpunch
    g4 "What?!"
    g4 "(I don't even jerk off that often!)"
    m "I find that a bit hard to believe... You're not embellishing the truth, are you?"
    call cho_main("I'm not, Sir! It's necessary for someone in my position!", "open", "closed", "angry", "mid")
    call cho_main("I wake up every morning before dawn, then run around the Quidditch pitch until the sun rises!", "open", "narrow", "angry", "mid")
    call cho_main("My body's at the absolute peak of human condition!", "open", "narrow", "angry", "R")
    g4 "It is quite impressive..."
    call cho_main("Glad to hear it, [cho_genie_name].", "base", "happyCl", "base", "mid")
    m "I assume you get complimented often?"
    call cho_main("Sometimes...", "soft", "base", "base", "R")
    g9 "And I suspect you have many admirers?"
    call cho_main("Oh, *umm*... maybe?", "annoyed", "base", "base", "mid")
    call cho_main("But that's {b}not{/b} why I take such great care of my body, Sir!", "open", "narrow", "angry", "mid")
    m "Of course not..."
    call cho_main("Quidditch is a hard game for anyone, as I'm sure you know...", "open", "closed", "base", "mid")
    call cho_main("But that goes double for girls!{w=0.6} I have to train twice as hard as the boys if I want to stand a chance!", "open", "narrow", "angry", "mid")
    m "That's very commendable of you..."
    call cho_main("Thank you, Sir.", "base", "base", "base", "mid")

    # Ask her to strip.
    g9 "So, Why don't you show me what you are made of?{w=1.0} Let me have a proper look at you!"
    call cho_main("Sir?", "soft", "wink", "raised", "mid")
    m "I need you to remove your clothes."
    call play_music("stop")
    call cho_main("!!!", "soft", "wide", "base", "mid", cheeks="blush")
    call play_music("cho")
    m "Go on, girl. Start with the top..."
    call cho_main("No!", "scream", "happyCl", "angry", "mid", cheeks="blush", trans=hpunch)
    call cho_main("Why are you even asking me to do such a thing?!", "angry", "narrow", "angry", "mid")
    #m "Didn't you take your skirt off for me after the Hufflepuff match?"
    #call cho_main("{size=-4}Well, I probably shouldn't have done that..{/size}", "annoyed", "base", "worried", "R")
    #m "Sorry?"
    m "Have you already forgotten that I'm here to train you?"
    call cho_main("And I'm very thankful for that, Sir, but...", "open", "closed", "base", "mid")
    m "Am I not your trusted mentor?"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    m "Your strong advisor..."
    g9 "Your guardian angel!"
    call cho_main("I don't think taking off my clothes will be necessary for our training, [cho_genie_name].", "annoyed", "narrow", "angry", "R")
    m "I'm very disappointed I've got to say..."
    m "You aren't this shy about undressing in front of your team, are you?"
    call cho_main("Sir, that's entirely different!", "soft", "narrow", "angry", "mid")
    m "How so?"
    call cho_main("I'm just not comfortable doing this in front of you, Sir!", "soft", "closed", "worried", "mid")
    call cho_main("You're really old...", "soft", "narrow", "worried", "downR", cheeks="blush")
    m "Pardon me?"
    call cho_main("I meant... you're our headmaster! It just feels wrong to me!", "soft", "narrow", "worried", "mid")
    #m "It didn't bother you the last time you barged into my office..."
    #call cho_main("Well, we had just won the game and all that... Maybe my judgement...", "annoyed", "closed", "worried", "R")
    m "Are you one of those shy girls, Miss Chang?"
    call cho_main("No, Sir. I wouldn't say I'm shy, but...", "soft", "narrow", "worried", "downR")
    m "Well then prove me you aren't, girl!"
    g9 "Let me see it!"

    # Cho stays reluctant.
    call cho_main("Is there no other way I could repay the favour?", "annoyed", "narrow", "worried", "mid")
    m "Well, yes.{w=0.3} Several.{w} But we'll get to those later..."
    call cho_main("Later, Sir?", "soft", "base", "raised", "mid")
    g4 "Girl, I wouldn't be asking you this if it wasn't absolutely necessary for your training!"
    call cho_main("Of course, [cho_genie_name].", "annoyed", "base", "base", "down")
    m "All that's required of you is to co-operate..."
    call cho_main("(...)", "annoyed", "base", "worried", "mid", cheeks="blush")
    m "Now take of your top..."
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("Only my top?", "soft", "narrow", "worried", "mid")
    g9 "Would you like to take off {b}more?{/b}"
    call cho_main("I didn't mean it like that!", "angry", "narrow", "angry", "mid")
    m "[cho_name], it's only the two of us in here. No need to worry."
    call cho_main("I'm not worried about others, [cho_genie_name]!", "annoyed", "narrow", "angry", "mid")
    call cho_main("For as long as nobody else will find out...{w} You have to promise me that, Sir!", "soft", "narrow", "angry", "R")
    g9 "Promised! Now take it off!"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    m "*Ahem*{w=0.5} Slowly..."
    pause .5
    call cho_main("", "quiver", "happyCl", "worried", "mid", cheeks="blush")
    pause .8

    # Remove top.
    $ cho.strip("robe", "top")
    show screen cho_cloth_pile
    with d3
    pause .5

    call cho_main("", "quiver", "narrow", "worried", "mid", cheeks="blush")
    call ctc

    menu:
        "\"Your posture is remarkable!\"":
            call cho_main("I'm glad you noticed!", "smile", "base", "base", "mid") # Happy
            call cho_main("I'm relieved you actually show interest in my body status, Sir!", "base", "base", "base", "mid")
            m "(Oh, You have no idea, girl!)"
            call cho_main("I thought you just wanted to gush at my body like all the other teachers...", "soft", "narrow", "worried", "mid", cheeks="blush")
            m "Who?{w} Which other teachers are you talking about?{w} Snape?!"
            call cho_main("No, not Snape...", "annoyed", "narrow", "angry", "R")
            call cho_main("(...)", "annoyed", "base", "worried", "downR", cheeks="blush")
            call cho_main("Promise me you won't tell her!", "quiver", "narrow", "worried", "mid", cheeks="blush")
            m "Her?!"
            call cho_main("Madame Hooch, Sir.", "soft", "narrow", "worried", "mid", cheeks="blush")
            m "Ah, the old, grey haired lady..."
            call cho_main("Yes, she's been eyeing me a lot lately...", "annoyed", "base", "worried", "downR", cheeks="blush")
            call cho_main("Even more so after our recent game against Hufflepuff, I wonder why...", "mad", "narrow", "worried", "R", cheeks="blush")
            g9 "I can't blame her... Your body is very pleasant to look at!"
            call cho_main("Thank you, Sir.", "base", "base", "base", "mid", cheeks="blush")

        "\"You have marvellous abs!\"":
            g4 "Magnificent."
            g4 "Simply...{w} magnificent..."
            call cho_main("*Ehm*...", "annoyed", "narrow", "worried", "R", cheeks="blush") # Embarrassed
            g4 "As if Michelangelo himself carved them onto your flesh..."
            m "I must say I'm very impressed!"
            call cho_main("Thank you, Sir.", "soft", "narrow", "worried", "downR", cheeks="blush")

        "\"*Eh*, I've seen better, but that'll do.\"":
            $ cho_mood += 3
            call cho_main("What?!", "mad", "base", "angry", "mid") # Upset
            g4 "(Crap!)"
            m "What I meant to say is, you're in great shape but I still see room for improvements."
            m "I'm impressed nonetheless!"
            call cho_main("Thank you, I guess...", "annoyed", "narrow", "angry", "downR", cheeks="blush")

    m "Not every girl I get to see here has such fine...{w=1.0} contours..."
    call cho_main("Other girls?", "soft", "wide", "base", "mid")
    call cho_main("Sir, you aren't training anybody else in Quidditch besides me, are you?", "soft", "narrow", "angry", "mid")
    m "What? Of course not..."
    call cho_main("Then which other girls are you talking about?", "annoyed", "narrow", "angry", "mid")
    g4 "(Shit! I better just tell her the truth.)"
    m "Just...{w=1.0} Granger..."
    call cho_main("*Phewww*{w=1.0} You scared me there for a second, Sir...", "smile", "narrow", "worried", "mid")
    m "You... don't mind about it?"
    call cho_main("Please. Why should I care what Granger does for you in here?", "soft", "narrow", "angry", "R")
    call cho_main("I suspected she was one of those girls buying favours from her teachers!", "open", "closed", "angry", "mid")
    call cho_main("With how many points she's earned for her house lately... to win the house cup...", "open", "narrow", "angry", "R")
    call cho_main("But as long as you don't help any Gryffindor or Slytherin sluts win the Quidditch cup, everything will be fine.", "base", "narrow", "base", "mid")
    g9 "No worries, [cho_name]. I don't have plans to train other {i}sluts{/i} in quidditch."

    call cho_main("That's a relief...", "open", "closed", "base", "mid")
    call cho_main("Besides, she clearly doesn't hold a candle against me!", "open", "narrow", "base", "R")
    call cho_main("All she does is sit on her arse all day, studying in the library...", "soft", "narrow", "angry", "mid")
    m "(...)"
    call cho_main("You can't expect somebody who's as lazy as her to look as great as I do!", "soft", "closed", "base", "mid")

    menu:
        "\"Yeah, she's gross.\"":
            $ cho_mood = 0
            m  "Miss Granger's body is nothing compared to yours."
            call cho_main("I wholeheartedly agree, Sir!", "base", "narrow", "angry", "mid")
            m  "Her tits sag too much, and her fat hips are disgusting..."
            hide screen cho_main
            call blktone
            g4 "(Something deep inside me just died saying this...)"
            call hide_blktone
            call cho_main("She really is a...", "open", "closed", "raised", "mid")
            call cho_main("... stupid...", "angry", "closed", "angry", "mid")
            call cho_main("... fat...", "clench", "narrow", "angry", "mid")
            call cho_main("... cow, isn't she?", "quiver", "narrow", "angry", "mid", cheeks="blush")
            m "Speaking of Hermione..."
            g9 "Why don't you show me \"your\"{w} very much \"superior\"{w} hips?"
            call cho_main("Are you asking me to take off my skirt?", "soft", "wink", "raised", "mid", cheeks="blush")
            m "Yes, my dear."

        "\"Nope, you lose\"":
            $ cho_mood += 6

            call cho_main("What?!", "scream", "wide", "angry", "mid", trans=hpunch)
            call cho_main("", "angry", "narrow", "angry", "mid")
            m "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!"
            m "Besides, jealousy is quite unbecoming of a witch like yourself..."
            call cho_main("But she doesn't even do workouts!", "clench", "narrow", "angry", "mid")
            m "Let's just forget about her, shall we?"
            m "And continue where we left off..."
            call cho_main("And where would that be?", "annoyed", "narrow", "angry", "mid")
            m "Your Quidditch training, Miss Chang."
            call cho_main("I'm not sure I want to -- after what you've just said...", "annoyed", "narrow", "angry", "R")
            m "Why? What did I say?"
            call cho_main("That Granger's body is better?! We both know that isn't true.", "mad", "narrow", "angry", "mid")
            m "Do you expect me to apologise?"
            call cho_main("Yes!{w} Admit that I'm sexier!", "annoyed", "closed", "angry", "mid", cheeks="blush") # Snobby
            g9 "You are indeed, {b}very sexy{/b}, Miss Chang!"
            call cho_main("Thank you, Sir.", "base", "narrow", "base", "mid")
            m "Now take of that skirt, would you..."
            call cho_main("(...)", "annoyed", "narrow", "angry", "mid")


    call cho_main("Please don't tell anybody about what I'm doing in here, Sir.", "quiver", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("It could really tarnish my reputation.", "soft", "narrow", "worried", "R", cheeks="blush")
    m "I'd never think of it..."
    call cho_main("I will take off my skirt now!", "scream", "happyCl", "angry", "mid") # Scream
    call cho_main("", "horny", "narrow", "worried", "R", cheeks="blush")
    g9 "(!!!)"
    pause .4

    # Remove skirt.
    hide screen cho_main
    $ cho.strip("bottom")
    show screen cho_main
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "base", "mid", cheeks="blush")
    call ctc

    g4 "YES!"
    g4 "Look at those thighs!"
    g4 "Those tree trunks!"
    g9 "Even the great \"Chun-Li\" would be jealous of those!"
    call cho_main("I'm sorry Sir, who's that?", "soft", "wink", "raised", "mid")
    m "(...)"

    menu:
        "\"Never seen City Hunter?\"":
            call cho_main("\"City Hunter?\"{w=0.3} Can't say that I have.", "soft", "base", "raised", "mid")
            m "What about \"Police Story?\""
            call cho_main("No?", "soft", "wink", "raised", "mid")
            m "\"Drunken Master?\""
            call cho_main("(...)", "annoyed", "base", "base", "R")
            g4 "Please tell me you've at the very least seen \"Rush Hour?\""
            call cho_main("No, Sir.", "annoyed", "closed", "base", "mid")
            m "I'm in shock, over how little you care about your culture..."
            call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
            g4 "Not every man can pull off a cosplay like that!"
            call cho_main("I'm not following, Sir.", "annoyed", "narrow", "angry", "R")

        "\"She's my main...\"":
            g9 "I simply love playing with her..."
            m "Seeing that leg rise up when I press the right buttons..."
            call cho_main("What?!", "open", "narrow", "raised", "mid") # confused

    g9 "Speaking of which!{w} I don't believe we are done here just yet."
    call cho_main("We aren't? But I did exactly what you wanted!", "open", "base", "worried", "mid")
    g9 "You've still got some clothes on..."
    call cho_main("Sir, is this why you are helping me?", "open", "closed", "angry", "mid")
    call cho_main("Might this be all just part of a sick scheme to get to see me naked?", "annoyed", "narrow", "angry", "mid")
    m "(...)"

    menu:
        "\"It absolutely is!\"":
            $ cho_mood += 20
            $ cho_mad_about_stripping = True # Flag that enables different dialogue that is a bit more "lewd" in the next favor repeat.
            call cho_main("", "angry", "wide", "base", "mid") # Shock
            g9 "Now take off that bra of yours and show me those titties!"
            call cho_main("[cho_genie_name], how can you talk to me like that!", "scream", "closed", "angry", "mid", trans=hpunch)
            call cho_main("I'm your student!", "clench", "narrow", "angry", "mid")
            g9 "And a very pretty one at that!"
            call cho_main("You disgust me, Professor...", "soft", "narrow", "angry", "mid")

        "\"Of course not...\"":
            $ cho_mood += 6
            $ cho_mad_about_stripping = False
            call cho_main("Aye right...", "soft", "narrow", "raised", "mid") # Expression of disbelieve...
            call cho_main("And I'm supposed to believe that.", "open", "narrow", "base", "R")
            call cho_main("You're practically foaming out of your mouth just looking at me, Sir...", "soft", "narrow", "angry", "mid")
            g4 "I'm not...{w} that's just..."
            #if butterbeer_ITEM.owned > 0:
            g4 "Butterbeer..."
            call cho_main("This is as far as I will go, Sir!", "annoyed", "narrow", "angry", "mid")

    call cho_main("If you want a bimbo to strip for you, I suggest you call Hermione instead...", "annoyed", "narrow", "angry", "mid")
    pause .5

    hide screen cho_main
    $ cho.wear("all")
    hide screen cho_cloth_pile
    call cho_main("", "angry", "narrow", "angry", "mid")
    pause .8

    call cho_main("We are done here!", "angry", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "She'll do it next time, I'm sure..."

    jump end_cho_strip_event


label cc_pf_strip_T2_intro_E2:
    call cho_main("", "upset", "base", "base", "R")
    m "[cho_name], to continue your training where we left off..."
    g9 "I'd like you to, once again, undress!"
    call cho_main("Of course, Sir.", "annoyed", "base", "angry", "downR")

    call cho_walk("desk", "base")

    call cho_main("Down to my undergarments, [cho_genie_name]?", "soft", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call cho_main("Or would you like me to take off all of it?", "soft", "narrow", "base", "mid")
    m "*Ehm*... All of it?"
    call cho_main("Very well, Sir.", "soft", "closed", "base", "mid")
    g4 "(Please don't let this be a trick question.)"
    call cho_main("", "upset", "narrow", "base", "mid")
    pause .4

    # Remove top.
    $ cho.strip("robe", "top")
    show screen cho_cloth_pile
    show screen cho_main
    with d3
    pause .5

    call cho_main("", "upset", "narrow", "angry", "mid")
    call ctc

    call cho_main("I'm a very good trainee, [cho_genie_name]!", "soft", "narrow", "angry", "mid")
    g9 "Yes you are!"
    call cho_main("If my trainer requires me to take off my clothing and strip for him...", "soft", "closed", "base", "mid")
    call cho_main("Then I have no other choice but to indulge...", "soft", "narrow", "base", "R")
    call cho_main("I see nothing wrong with that...", "annoyed", "narrow", "angry", "mid")
    pause .4

    # Remove skirt.
    $ cho.strip("bottom")
    with d3
    pause .5

    call cho_main("", "annoyed", "narrow", "base", "mid")
    call ctc

    call cho_main("Would you perhaps like me to climb on top of your desk as well?", "soft", "narrow", "raised", "mid")
    call cho_main("And dance for you like some common harlot?", "soft", "narrow", "base", "R")

    # You saw Hermione strip before.
    if hg_strip.trigger:
        m "If it's not too much trouble..."
        call cho_main("Of course not, [cho_genie_name].", "soft", "closed", "base", "mid")
        g4 "(I'm having a bit of a deja vu!)" # In-game font doesn't support special characters. déjà vu!
    else:
        g9 "Yes please!"
        call cho_main("Whatever you say, Sir!", "soft", "closed", "base", "mid")
    call cho_main("Like I said, I'd go to any lengths just to please my trainer...", "soft", "narrow", "base", "mid")

    # Climbs desk.
    call hide_characters
    show screen blkfade
    with d5
    call play_sound("climb_desk")
    pause 1

    "To your surprise, the athletic petite girl rather playfully climbs on top of your desk."
    pause .5
    g9 "Nice!"
    pause .2

    call cho_chibi("stand", "on_desk", "on_desk", flip=False)
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call cho_main("After all, I promised I'd do anything to win that Quidditch cup...", "soft", "narrow", "angry", "mid")
    call cho_main("If stripping for you is what it takes, then...", "soft", "base", "angry", "down")
    call play_music("sad")
    call cho_main("Then...", "angry", "base", "worried", "down")
    call cho_main("I-I'll do it...", "soft", "narrow", "worried", "down", cheeks="blush")
    m "(Shit. Is she crying?)"
    m "(Can she even cry?)"
    m "Are you alright, girl?"
    call cho_main("No.{w} I'm already regretting climbing up here!!!", "mad", "closed", "worried", "mid")
    call cho_main("(What were you thinking, Cho?!)", "angry", "narrow", "worried", "down", cheeks="blush")
    m "You can come back down if it's too much for yo--"
    call cho_main("Shut up!", "scream", "closed", "angry", "mid", trans=hpunch) # Scream
    call cho_main("Can't you see what I'm trying to do here?", "angry", "narrow", "angry", "mid")
    m "Not really, no."
    call cho_main("I-I'm... testing my limits, Sir.", "angry", "narrow", "worried", "down", cheeks="blush")
    call cho_main("And I believe I've reached them!", "mad", "happyCl", "worried", "mid", cheeks="blush")
    m "For real? You are still wearing clothes..."
    call cho_main("I thought{w=0.2}, if I could go as far as embarrassing myself in front of my headmaster...", "soft", "narrow", "worried", "down", cheeks="blush")
    call cho_main("Doing the same in front of the school won't feel as bad in comparison.", "annoyed", "narrow", "worried", "down", cheeks="blush")
    call cho_main("Sir, I don't think I can do this after all.", "soft", "narrow", "worried", "mid")
    call cho_main("Could I get your permission to leave and never come back?", "angry", "narrow", "worried", "mid")

    menu:
        "\"Yes, but take off those clothes first...\"":
            call play_music("stop")
            call cho_main("Yes! Thank you, Sir!", "soft", "closed", "worried", "mid", cheeks="blush")
            call cho_main("Even after I've given up -- you're still believing in me!", "soft", "narrow", "worried", "mid", cheeks="blush")
            m "What?{w=0.2} *Ahem* I mean..."
            g9 "Of course!{w=0.2} I always did!"
            call cho_main("I may not like it. But this is all just part of my training...", "soft", "base", "worried", "R", cheeks="blush")
            m "*Uhhhh*... Sure..."
            call play_music("cho")
            call cho_main("It's one of many challenges I have to face before I can call myself a Quidditch champion!", "soft", "closed", "angry", "mid")
            call cho_main("This is just about facing my inner demons, isn't it?", "soft", "narrow", "angry", "mid")
            call cho_main("Overcoming my fears...", "soft", "narrow", "angry", "R")
            call cho_main("Failure, and embarrassment...", "soft", "closed", "base", "mid")
            call cho_main("(Come on Cho, you can do it!!!)", "horny", "happyCl", "worried", "mid", cheeks="blush")
            call cho_main("*Ehm*...", "horny", "narrow", "worried", "down", cheeks="blush")
            call cho_main("What would you like me to do first, [cho_genie_name]?", "soft", "narrow", "worried", "mid", cheeks="blush")
            call cho_main("Remove my bra...", "soft", "narrow", "base", "mid", cheeks="blush")
            call cho_main("Or take off my panties?", "horny", "narrow", "worried", "down", cheeks="blush")

        "\"Yes, you are dismissed...\"":
            $ cho_mood += 6
            call play_music("stop")
            call cho_main("What?!", "soft", "wide", "base", "mid")
            call cho_main("But Sir!", "soft", "base", "worried", "mid")
            m "You can go now..."
            call cho_main("You can't do that!", "scream", "narrow", "angry", "mid", trans=hpunch)
            call cho_main("", "angry", "narrow", "angry", "mid")
            g4 "Didn't you just beg me to do just that?"
            call play_music("sad")
            call cho_main("I begged you to help me win the Quidditch cup!", "clench", "narrow", "angry", "mid")
            call cho_main("And to be my trainer!{w} To be a {b}good{/b} trainer!", "soft", "narrow", "angry", "mid")
            call cho_main("How can I overcome my fear of losing if I can't even do... this!", "annoyed", "base", "worried", "down", cheeks="blush")
            call cho_main("You're supposed to encourage me!{w=0.6} Get me through any challenges I'm confronted with.", "soft", "narrow", "angry", "mid")
            m "Including stripping?"
            call cho_main("Including bloody stripping!", "scream", "closed", "angry", "mid", trans=hpunch)
            call cho_main("", "annoyed", "narrow", "angry", "mid")
            m "To my defence. I got some mixed messages from you earlier..."
            call cho_main("(...)", "annoyed", "narrow", "angry", "R") # Annoyed
            call play_music("stop")
            m "Very well then..."
            m "Take off your clothes, [cho_name]."
            call cho_main("Yes, Sir!", "soft", "closed", "base", "mid")
            call cho_main("Would you like me to take off my bra first?", "soft", "narrow", "angry", "mid")
            call cho_main("Or pull down my panties so you can get a nice look at my lower half?", "soft", "narrow", "base", "mid")

    m "(...)"
    menu:
        m "First, I'd like you to..."
        "\"Show me those big, juicy \"Quaffles\" of yours!\"":
            call play_music("cho")
            call cho_main("*uhhh*...", "upset", "wide", "base", "mid", cheeks="blush")
            g9 "Those two mean, hearty \"bludgers!\""
            call cho_main("Sir? Could it be that you are talking about my breasts?", "soft", "narrow", "worried", "mid", cheeks="heavy_blush")
            m "Yes indeed! Very good."
            m "I was hoping you would eventually catch on."
            m "Also because I ran out of balls to compare them to..."
            call cho_main("Promise me that you won't laugh when I show you my...", "soft", "narrow", "worried", "R", cheeks="blush")
            call cho_main("\"Bludgers!\"", "mad", "happyCl", "worried", "mid", cheeks="heavy_blush")
            m "Why would I ever laugh at a pretty girl like you, Miss Chang?"
            call cho_main("Because they...{w} aren't as big as Hermione's...", "soft", "narrow", "worried", "downR", cheeks="blush")
            call cho_main("Hers are more closer to {i}Quaffles{/i} than mine...", "soft", "base", "worried", "mid", cheeks="blush")
            m "And there will always be a pair of \"Beaters\" that prefer to play with your...{w} balls."
            call cho_main("Only two?...", "upset", "base", "worried", "downR", cheeks="blush")
            g9 "Don't forget to count those lucky enough to get hit by those \"bludgers!\""
            call cho_main("", "upset", "base", "raised", "mid")
            m "Speaking of which..."
            call cho_main("Yes?", "soft", "base", "worried", "mid", cheeks="blush")
            g4 "I'd like you to hit me with them!"
            call cho_main("With my breasts?", "open", "wide", "base", "mid", cheeks="blush")
            g9 "Yes! Hit me full force!{w} Take off that bra!"
            call cho_main("*Ugh!*...", "mad", "narrow", "base", "down", cheeks="blush")
            call cho_main("{size=-4}I can't believe I'm actually going to do this!{/size}", "mad", "happyCl", "worried", "mid", cheeks="blush")
            call cho_main("", "soft", "narrow", "worried", "mid", cheeks="blush")
            pause .4

            # Remove bra.
            $ cho.strip("bra")
            with d3
            pause .8

            call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
            call ctc

            g4 "Simply wonderful, Miss Chang."
            m "Those are some stellar breasts you got there."
            call cho_main("(...)", "base", "narrow", "worried", "downR", cheeks="blush")
            g4 "Some \"outstanding\" boobies!"
            call cho_main("...", "annoyed", "narrow", "base", "mid", cheeks="blush")
            m "Would you mind if I smack them?"
            call cho_main("What?! Of course I would mind!", "soft", "wide", "base", "mid", cheeks="heavy_blush")
            m "I just want to beat them around a bit..."
            call cho_main("", "annoyed", "narrow", "angry", "mid", cheeks="blush")
            g9 "After all, they are two soft, meaty \"bludgers!\""
            g9 "And I'm a \"beater!\""

            $ genie_quid_position = "beater"

            call cho_main("You are childish.{w} That's what you are...", "soft", "narrow", "angry", "mid")
            m "You're the one playing games."
            call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
            call cho_main("Fine...{w} But Only once!", "soft", "narrow", "angry", "R")
            call cho_main("Twice...{w} maybe...", "mad", "narrow", "worried", "downR", cheeks="blush")
            g9 "That's a hundred percent more than I had hoped for!"

            call slap_her
            call cho_main("*Ouch!*", "angry", "wide", "base", "mid", cheeks="blush")
            call slap_her
            call slap_her
            call slap_her
            call cho_main("Stop it!", "scream", "happyCl", "worried", "mid", cheeks="blush")
            call cho_main("That was more than twice!", "soft", "narrow", "angry", "mid", cheeks="blush")
            m "I stopped counting halfway through..."

        "\"Let me catch sight of that \"Snitch!\"\"":
            call play_music("cho")
            call cho_main("Don't you mean \"Snatch,\" Sir?", "annoyed", "narrow", "angry", "mid")
            g9 "Potato, Potato!"
            call cho_main("Your motives were nothing but for your own perverted gains, weren't they? From the very start.", "soft", "narrow", "base", "mid") # Annoyed
            m "More or less..."
            m "However, I never lied about wanting to help you win the Quidditch cup!"
            g4 "(Since I've bet a fortune on it...)"
            m "And I wouldn't be able to call myself a man if I was lying!"
            call cho_main("And you'd be called a dead man, if you try to trick me!", "clench", "narrow", "angry", "mid")
            m "Well technically I'm a geni--"
            call play_sound("kick")
            call cho_main("", "annoyed", "narrow", "angry", "mid", trans=vpunch)
            g4 "*Aaaaah*!"
            call nar(">Cho does a daunting stomp on your desk...")
            call cho_main("Don't think for a second I wouldn't do it! After all of this!", "scream", "narrow", "angry", "mid")
            call cho_main("", "angry", "narrow", "angry", "mid")
            call play_sound("gulp")
            g4 "*Gulp*"
            m "Yes, Ma'am."
            call cho_main("(...)", "upset", "closed", "base", "mid")
            call cho_main("", "upset", "narrow", "worried", "down", cheeks="blush")
            pause .4

            # Remove panties.
            $ cho.strip("panties")
            with d3
            pause .5

            call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
            call ctc

            call cho_main("Happy, Sir?", "soft", "narrow", "worried", "mid", cheeks="blush")
            m "Very."
            g9 "Finally I get the appeal of Quidditch."
            call cho_main("Really?", "soft", "base", "raised", "mid")
            m "Yes..."
            g9 "You see, I think I've become quite a bit of a seeker myself!"

            $ genie_quid_position = "seeker"

            call cho_main("(...)", "annoyed", "base", "base", "mid")
            m "And I believe I've just found my very own golden snatch!"
            call cho_main("", "annoyed", "narrow", "angry", "mid", cheeks="blush")
            m "You should consider yourself lucky, Miss Chang."
            call cho_main("Why?...", "soft", "narrow", "raised", "mid")
            g9 "It's very pretty."
            call cho_main("*Ugh*...", "mad", "narrow", "base", "down", cheeks="heavy_blush")


    call cho_main("Sir, will that be all then?", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("May I go now?", "soft", "narrow", "angry", "R")
    m "Haven't you forgotten something?"
    call cho_main("Didn't I do enough for you already?", "angry", "narrow", "angry", "mid")
    g9 "For me, you did more than enough!{w=0.6} I'm more than pleased with what you've shown me..."
    call cho_main("*Ugh*...", "disgust", "narrow", "base", "down", cheeks="blush") # Disgusted
    m "But, wasn't your goal earlier to undress entirely?"
    m "To prove to yourself that you {b}could{/b} do it?"
    call cho_main("{size=-4}I hoped you'd just forget about that...{/size}", "mad", "narrow", "worried", "down", cheeks="blush") # Small text.
    g9 "Well, I didn't!"
    m "I'm here to help you mature -- and boost your confidence."
    m "A body like yours is nothing you need to hide away!"
    call cho_main("", "base", "narrow", "worried", "mid", cheeks="blush")
    m "Don't you think so too?{w} After all the work you put into it?"
    g4 "It should be celebrated! And seen by everyone!"
    call cho_main("You're making me blush, [cho_genie_name]...", "horny", "narrow", "worried", "downR", cheeks="heavy_blush")
    g9 "You can do it, [cho_name]! Only one more piece to go..."
    call cho_main("Yes, Sir!", "angry", "closed", "worried", "mid", cheeks="blush")
    call cho_main("", "base", "narrow", "worried", "mid", cheeks="blush")
    pause .4

    # Cho strips completely.
    $ cho.strip("all")
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
    call ctc

    m "See, that wasn't very hard was it?"
    call cho_main("No...", "soft", "narrow", "base", "down", cheeks="blush")
    call cho_main("No! You're right!", "smile", "base", "base", "mid")
    m "And you have a very beautiful body -- if I might add."
    call cho_main("Thank you, Sir.", "soft", "narrow", "worried", "mid")
    m "I can see why Hermione is so jealous."
    call cho_main("", "upset", "base", "base", "mid", cheeks="blush")
    pause .8
    call cho_main("She is?", "scream", "wide", "base", "mid", cheeks="blush", trans=vpunch)
    call cho_main("", "horny", "base", "base", "down", cheeks="heavy_blush")
    m "Look who perked up all of a sudden."
    call cho_main("She should be jealous!{w=0.6} These thighs could break a broom in half if I tried hard enough.", "smile", "narrow", "angry", "mid", cheeks="blush")
    call ctc

    call play_sound("gulp")
    g4 "*Gulp!*"
    m "I don't doubt it."

    call cho_main("Thank you, [cho_genie_name].", "base", "closed", "base", "mid")
    m "For what?"
    call cho_main("For teaching me.", "soft", "narrow", "worried", "downR")
    call cho_main("I couldn't have imagined showing myself off like this before... but.", "horny", "narrow", "worried", "downR", cheeks="blush")
    m "Yes?"
    call cho_main("Well, your methods have clearly worked so far...", "soft", "narrow", "base", "R")
    call cho_main("And I feel more confident than ever!", "soft", "wide", "base", "mid")
    m "That's great news, and hey..."
    m "If distracting doesn't work, you could just crush your opponents with those thighs of yours."
    call cho_main("That's true...", "smile", "narrow", "base", "mid")
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    call cho_chibi("stand", "desk", "base", flip=False)

    pause 1

    hide screen blkfade
    with d5
    pause .2

    call cho_main("Will this be all then, Sir?", "soft", "base", "base", "R")
    m "Yes Miss Chang, great work today..."
    m "I doubt you'll have any problems distracting anyone with a body like that."
    m "You're dismissed."
    call cho_main("Thank you, [cho_genie_name].", "base", "happyCl", "base", "mid")
    call hide_characters
    hide screen bld1
    with d3
    pause .1

    call cho_walk("door", "base")

    call bld
    m "Miss Chang."
    hide screen bld1
    with d3
    pause .3

    call cho_chibi("stand", "door", "base", flip=False)
    with d3
    pause .2

    call cho_main("Yes?", "soft", "base", "raised", "mid", ypos="head", flip=False)
    m "Aren't you forgetting about something?"
    call cho_main("Sir?", "soft", "narrow", "base", "mid")
    m "You're still naked...{w} I wouldn't go out there if I were you..."
    call cho_main("Oh, yes of course!", "soft", "wide", "base", "mid", cheeks="blush", trans=hpunch)

    call cho_walk("desk", "base")
    pause .5
    call chibi_emote("thought", "cho")
    pause .8

    # Cho puts clothes back on.
    call play_sound("equip")
    hide screen cho_main
    $ cho.wear("all")
    hide screen cho_cloth_pile
    pause .8

    call cho_main("(...)", "disgust", "narrow", "worried", "down", cheeks="blush", xpos="right", ypos="base")
    call cho_main("*Uhm*...", "soft", "narrow", "worried", "mid", cheeks="blush")
    if game.daytime:
        call cho_main("Have a good day...", "soft", "base", "base", "R", cheeks="blush")
    else:
        call cho_main("Have a good night...", "soft", "base", "base", "R", cheeks="blush")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "She's so cute..."
    g9 "And sexy!"
    m "But also a bit intimidating..."

    jump end_cho_strip_event


label cc_pf_strip_T2_intro_E3:
    g9 "[cho_name], how would you like to do another striptease for me?"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    g9 "You did such a phenomenal job last time!"
    call cho_main("Another strip show?", "soft", "narrow", "angry", "R")
    g9 "Yes Indeed! Come a bit closer..."
    call cho_main("(...)", "angry", "narrow", "base", "down")

    call cho_walk("desk", "base")

    call cho_main("Sir, Those favours were never about my training, were they?", "soft", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    m "I never said they were!"
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    pause .8
    m "You keep me happy by doing favours for me, and in return, I will train you..."
    m "That was the deal."
    call cho_main("I never expected that they would require me to do...{w} this!", "annoyed", "base", "worried", "down")
    g9 "But you did it anyway! Commendable!"
    call cho_main("Please stop it with your compliments, Sir!", "open", "closed", "angry", "mid")
    call cho_main("And explain to me why those favours have to be so...", "annoyed", "narrow", "worried", "downR")
    call cho_main("{size=-4}perverted?{/size}", "soft", "narrow", "angry", "R", cheeks="blush") # Small text
    m "You see..."
    m "It can get pretty lonely in this room."
    m "There's not even a television set up here..."
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    pause .8

    # Remove top.
    $ cho.strip("robe", "top")
    show screen cho_cloth_pile
    with d3
    pause .5

    call cho_main("", "quiver", "narrow", "worried", "R", cheeks="blush")
    call ctc

    call cho_main("Does Granger do these sorts of things for you too?", "soft", "base", "worried", "mid", cheeks="blush")
    g9 "She does a lot of things for me. You need to be more specific!"
    call cho_main("I meant buying \"sexual favours.\"{w} Doing tasks that are, let's say, a little audacious...", "soft", "narrow", "worried", "downR", cheeks="blush")
    m "Are you talking about stripping, girl?"
    call cho_main("Yes, Sir.", "quiver", "narrow", "worried", "downR", cheeks="blush")
    pause .4

    # Remove skirt.
    hide screen cho_main
    $ cho.strip("bottom")
    show screen cho_main
    with d3
    pause .5

    call cho_main("", "horny", "base", "worried", "mid", cheeks="heavy_blush")
    call ctc

    # Check if Hermione has already stripped for you.
    if not hg_strip.trigger:

        # Cho demands that you get Hermione to strip, so Cho has something to blackmail her should anything happen.
        # Cho gets dressed again and storms off.

        m "Actually, she doesn't..."
        call cho_main("What? But I thought she'd--", "soft", "wide", "base", "mid")
        call cho_main("Why do you ask me to do these favours, and not Granger?", "open", "narrow", "angry", "mid", trans=hpunch)
        m "Let's just say, she isn't as progressive as you...{w} yet."
        call cho_main("You haven't even seen her naked?", "angry", "base", "base", "mid")
        call cho_main("What favours are you even buying from her?", "open", "base", "angry", "mid")
        m "Just chit-chats, mostly..."
        call cho_main("Make her strip too!", "clench", "narrow", "angry", "mid")
        g4 "It's not that easy, girl!"
        call cho_main("Well then get on with it!", "angry", "closed", "angry", "mid")
        call cho_main("What's the worst that could happen?", "soft", "narrow", "angry", "R")
        m "She could report me, and I'd get kicked out of this school most likely."
        m "She's reported me to that ministry before..."
        call cho_main("The \"Ministry of Magic?\"", "open", "base", "raised", "mid")
        call cho_main("If they were to regulate the school rules more strictly, my chance of winning the Quidditch cup would be back down to zero!", "angry", "wide", "worried", "mid", cheeks="blush")
        call cho_main("And if Granger ever was to find out about me stripping for our headmaster, it would mean the end of my Quidditch career for sure!", "mad", "base", "worried", "downR", cheeks="blush")
        m "So? What do you suggest we do?"
        call cho_main("Isn't it obvious?! Ask her to do more advanced favours!", "soft", "narrow", "angry", "mid")
        call cho_main("If I could get a hold of something to blackmail her with, she'd never dare to report to the ministry!", "clench", "narrow", "angry", "R")
        m "That doesn't sound too bad of an idea..."
        call cho_main("Until then, don't expect me to undress for you until you've solved this situation...", "soft", "narrow", "angry", "mid")
        m "(Bollocks...)"
        call cho_main("", "annoyed", "closed", "angry", "mid")
        pause .5

        $ cho.wear("all")
        hide screen cho_cloth_pile
        call cho_main("", "annoyed", "narrow", "angry", "mid")
        pause .8

        call cho_main("Good day, Sir!", "soft", "narrow", "angry", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        # Event failed, no progress.
        $ cc_pf_strip.fail()
        jump end_cho_event


    # After you got Hermione to strip.
    m "She does indeed."
    call cho_main("Really?!{w} You got that cow to take off her clothes?", "soft", "wide", "base", "mid")
    call cho_main("Did you get any proof of that?", "soft", "base", "worried", "mid")
    m "What?{w} Why would I need to do that?"
    call cho_main("To blackmail her!{w} To prove that she's in on this whole \"favour trading\" business too...", "open", "narrow", "angry", "mid")
    m "We had an eye witness, for what it's worth..."
    call cho_main("Seriously?! Who was it?", "smile", "base", "base", "mid")
    m "Snape..."
    call cho_main("What?! Professor Snape?", "scream", "wide", "base", "mid", trans=hpunch)
    call cho_main("", "smile", "wide", "base", "mid")
    m "He sort of just walked in on the action.{w} After all, the door wasn't locked..."
    call cho_main("That's too funny! I wish I could have been there when that happened!", "smile", "base", "base", "R")
    g9 "She was dancing on my desk, right here, butt naked!"
    call cho_main("That sounds sooo embarrassing!", "soft", "narrow", "worried", "up", cheeks="blush")
    m "As far as I know, that door isn't locked right now either..."
    m "Aren't you scared that Snape might walk in on you too?"
    call cho_main("*Hmm*..", "annoyed", "base", "base", "R")

    call hide_characters
    show screen blkfade
    with d3
    call play_sound("desk")
    pause 3

    ">You watch as Cho slowly climbs onto your desk..."

    call cho_chibi("stand", "on_desk", "on_desk")
    hide screen bld1
    hide screen blkfade
    with d3
    pause .8

    call cho_main("I'm not scared at all, Sir!", "smile", "narrow", "angry", "mid")
    call cho_main("", "horny", "narrow", "angry", "mid")
    pause .4

    # Remove bra.
    $ cho.strip("bra")
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "angry", "mid")
    call ctc

    call cho_main("It's just Professor Snape, after all...", "soft", "narrow", "base", "R")
    call cho_main("Everybody knows that he's a creep! Nobody would believe a word he says.", "open", "base", "angry", "down")
    m "So...{w} what if it's not Snape, but some other teacher that makes their way in here?"
    call cho_main("*Huh*?{w=0.5} Oh no!", "soft", "wide", "base", "mid")
    call cho_main("For a second I forgot we even had other teachers at this school!", "open", "wide", "worried", "L", cheeks="blush")
    call cho_main("What if Professor McGonagall stumbles in here while...{w} while I--", "angry", "happyCl", "worried", "mid", cheeks="heavy_blush")

    call play_sound("desk")
    call hide_characters
    show screen blkfade
    with d3
    pause 1.0

    call cho_chibi("stand", "desk", "base", flip=True)
    hide screen bld1
    hide screen blkfade
    with d3
    call teleport(position="cho", effect=False)
    pause .5

    call bld
    m "Don't worry. That won't happen."
    call cho_chibi("stand", "desk", "base")
    with d3
    pause .5

    call cho_main("Are you sure, Sir?", "soft", "narrow", "worried", "mid", cheeks="blush")
    m "You have my word..."
    call cho_main("O-{w=0.2}okay...", "soft", "narrow", "worried", "R", cheeks="blush")
    m "Now then, Miss Chang!{w} It's time for the grand finale..."
    g9 "Take off your panties!"
    call cho_main("(...)", "annoyed", "base", "worried", "down", cheeks="blush")
    call cho_main("Very well, Sir.", "base", "base", "base", "mid")
    pause .4

    # Remove panties + all else.
    $ cho.strip("all")
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "angry", "mid", cheeks="blush")
    call ctc

    g4 "I've got to say, once again I'm very impressed by you!"
    call cho_main("Glad to hear it, [cho_genie_name].", "smile", "narrow", "angry", "mid")
    call cho_main("You can have those, by the way.", "base", "narrow", "angry", "mid")
    call nar(">Cho throws her panties onto your desk.")
    call cho_main("You can keep them, for now...", "soft", "narrow", "base", "R")
    g9 "I appreciate the notion!"
    call cho_main("", "base", "narrow", "base", "mid")
    pause .8

    # Panties acquired message!
    if cho.is_equipped("panties"): # Cheats fallback
        call give_reward(">You have acquired Cho's panties!", cho.get_equipped("panties").get_icon())
    else:
        call give_reward(">You have acquired Cho's panties!", cho_panties_basic1.get_icon())
    $ has_cho_panties = True

    m "Well then, Miss Chang..."
    m "You may leave now.{w} Dismissed."
    call cho_main("Wait Sir!{w} I can't leave just yet!", "open", "wide", "base", "mid")
    m "Why not? Don't tell me you want some points now after all..."
    call cho_main("No Sir, but...{w} I don't believe we are done here...", "mad", "base", "worried", "downR", cheeks="blush")
    g9 "We aren't?"
    call cho_main("May I request something of you, Sir?", "soft", "narrow", "worried", "mid", cheeks="blush")
    m "Yes?{w} What is it?"

    # Cho asks you to summon Hermione.
    call cho_main("Could you please...", "soft", "base", "worried", "downR", cheeks="blush")
    call cho_main("*Ehm*...", "quiver", "narrow", "worried", "downR", cheeks="heavy_blush")
    call cho_main("Could you please summon Hermione?", "soft", "narrow", "worried", "mid", cheeks="heavy_blush")

    with hpunch
    g4 "What?"
    call cho_main("It's time someone throws \"high and mighty\" Granger off her high horse!", "open", "narrow", "angry", "mid")
    call cho_main("She's been a pain in my butt for years now...", "angry", "narrow", "angry", "downR")
    call cho_main("This is going to be my revenge!", "soft", "narrow", "angry", "mid")
    m "Are you sure that this is such a good idea? Aren't you scared she'll tattle about it?"
    call cho_main("No.{w} Granger is clever...", "soft", "closed", "base", "mid")
    call cho_main("She could destroy my reputation, sure...", "soft", "base", "base", "R")
    call cho_main("But, should that happen, I now have the means to take her down with me!", "base", "narrow", "angry", "mid")
    call cho_main("I'm not the only one stripping for you, after all.", "soft", "narrow", "base", "mid")
    m "I suppose you're right..."
    call cho_main("I can't believe how depraved Granger actually is...", "horny", "narrow", "angry", "down", cheeks="blush")
    call cho_main("Stripping for her headmaster.{w=0.6} What a slut...", "soft", "narrow", "angry", "mid", cheeks="blush")
    m "Aren't you doing exactly the same?"
    call cho_main("Yes, but I'm not a whore stripping for points, unlike her!", "open", "closed", "base", "mid")
    m "Still makes you a slut..."
    call cho_main("I'm untouchable! I'll show that {b}bitch{/b} she can't mess with me!", "angry", "narrow", "angry", "R")
    call cho_main("This is gonna be so much fun!", "smile", "narrow", "angry", "mid")

    call cho_walk(570, "base")
    pause 2.0

    call cho_main("Call her already!", "annoyed", "narrow", "angry", "R", ypos="head", flip=True)
    m "I'm on it..."

    hide screen bld1
    show screen blkfade
    with d3
    pause 1.0
    hide screen blkfade
    with d3

    # Summon Hermione.
    call play_sound("door")
    call her_chibi("stand", "door", "base")
    with d3
    pause .5

    call her_main("You wanted to see me, Sir?", "soft", "closed", "base", "mid", ypos="head", flip=False, trans=d3)
    call her_main("Cho?", "soft", "wide", "worried", "shocked")
    call cho_main("Hey there, Granger!", "horny", "narrow", "angry", "mid") # Grinning
    call her_main("What? Why are you--", "disgust", "wide", "worried", "shocked")

    call her_walk(660, "base")

    call cho_main("", "smile", "narrow", "angry", "L", xpos="mid", ypos="base", flip=True)
    call her_main("What the bloody hell is going on here?!", "scream", "closed", "base", "mid", xpos="base", ypos="base", trans=hpunch) # Scream
    call her_main("", "angry", "base", "angry", "mid")

    call cho_main("You know, just the usual...", "soft", "base", "base", "L")
    call cho_main("Like stripping for our dear headmaster!", "smile", "narrow", "angry", "L")
    call cho_main("I trust that you're more than familiar with it...", "soft", "closed", "base", "L")
    call her_main("You've told her?", "clench", "base", "angry", "mid")
    call cho_main("So you really {b}did{/b} do it!", "open", "wide", "base", "L")
    call her_main("It's none of your business what I do at this school! You slut!", "angry", "narrow", "angry", "R")
    call cho_main("Are you sure about that?{w=0.6} I believe there are some people that would think otherwise...", "grin", "narrow", "base", "mid")
    call cho_main("Your friends...{w} the other students...{w} our teachers...", "soft", "narrow", "angry", "L")
    call cho_main("Maybe even the ministry?", "smile", "narrow", "angry", "L")
    call her_main("You wouldn't dare!!!", "upset", "happy", "base", "mid")
    call cho_main("Indeed, I wouldn't.", "soft", "closed", "base", "mid")
    call cho_main("And neither would you!", "smile", "narrow", "angry", "L")
    call cho_main("Which is why we brought you here...", "open", "base", "base", "mid")
    call cho_main("To have some fun!", "base", "narrow", "angry", "mid")

    call her_main("Sir, I demand that you stop this nonsense!", "open", "base", "angry", "mid")
    call cho_main("I don't think that's very likely to happen, Granger...", "soft", "narrow", "angry", "mid")
    call cho_main("We both know what he would prefer...", "soft", "closed", "base", "mid")
    m "..."
    call cho_main("And who he prefers...", "smile", "narrow", "angry", "mid")
    call her_main("You think that he prefers you over me?{w} Please...", "soft", "narrow", "angry", "R")
    call cho_main("Why don't we just ask him?", "base", "narrow", "base", "mid")
    call cho_main("Tell us, Professor...", "soft", "narrow", "base", "R")
    call cho_main("How do you like the athletic, immaculate, nude body of your favourite student?", "smile", "narrow", "angry", "mid")
    call cho_main("It's so much better than Miss Granger's, isn't it?", "base", "narrow", "angry", "mid")
    call ctc

    $ cho_strip_complete = True # Enables wardrobe strip functions.
    $ d_flag_01 = False # Cho not on desk
    call cc_pf_strip_T2_hermione

    jump end_cho_strip_event


label cc_pf_strip_T2_E3: # Repeats
    m "[cho_name], why don't you come a bit closer?"
    call cho_main("Of course, [cho_genie_name]...", "base", "narrow", "base", "mid")

    call cho_walk("desk", "base")

    call cho_main("", "base", "base", "base", "R", xpos="mid", ypos="base", trans=fade)
    call ctc

    g9 "I'm in the mood for another striptease!"
    call cho_main("Funny you should say that, [cho_genie_name]...", "soft", "base", "raised", "downR")
    call cho_main("", "horny", "narrow", "angry", "mid")
    pause .4

    # Remove top & robe.
    call play_sound("equip")
    $ cho.strip("robe", "top")
    show screen cho_cloth_pile
    with d3
    pause .5

    call cho_main("Because so am I!", "base", "narrow", "angry", "mid")
    call cho_main("Enjoy yourself, Sir...", "soft", "closed", "base", "mid")
    call cho_main("", "base", "narrow", "angry", "mid")
    pause .4

    # Remove bottom.
    $ cho.strip("bottom")
    with d3
    pause .5

    g4 "*Argh!* You little minx!"
    call cho_main("Are we going to invite Granger again?", "soft", "narrow", "raised", "down")
    call cho_main("I would like to have some fun with her...", "smile", "narrow", "angry", "mid")
    call cho_main("Let her watch...", "horny", "narrow", "angry", "mid", cheeks="blush")
    pause .4

    # Remove bra.
    $ cho.strip("bra")
    with d3
    pause .5

    g9 "The more, the merrier!"
    call cho_main("", "base", "narrow", "angry", "mid")
    pause .4

    # Remove panties + all else.
    $ cho.strip("all")
    with d3
    call ctc

    call cho_main("Catch, [cho_genie_name]!", "soft", "base", "base", "mid")
    call nar(">Cho throws her panties at you.")

    # Panties acquired message!
    if cho.is_equipped("panties"): # Cheats fallback
        call give_reward(">You have acquired Cho's panties!", cho.get_equipped("panties").get_icon())
    else:
        call give_reward(">You have acquired Cho's panties!", cho_panties_basic1.get_icon())
    $ has_cho_panties = True

    g9 "Nice!"
    call cho_main("I'd like to have them back after this, mind you.", "soft", "base", "raised", "R")
    m "Of course..."
    call cho_main("Anything else you'd like, Sir?", "base", "base", "base", "mid")

    $ d_flag_01 = False # Cho on desk flag for this event
    menu:
        "\"Hop on my desk!\"":
            $ d_flag_01 = True
            call cho_main("Sounds like a fun idea, [cho_genie_name]!", "base", "happyCl", "base", "mid")
            call hide_characters
            show screen blkfade
            with d3
            call play_sound("desk")
            pause 2

            call cho_chibi("stand", "on_desk", "on_desk", flip=False)
            hide screen bld1
            hide screen blkfade
            with d3
            pause 1

            call cho_main("How is the view down there, Sir?", "base", "narrow", "base", "down")
            g9 "Couldn't be any better!"

            call hide_characters
            hide screen bld1
            with d3
            pause .2

            call cho_chibi("stand", "on_desk", "on_desk", flip=True) # Facing the door.
            with d3
            pause .8

        "\"Let Granger have a good look at you!\"":
            call cho_main("I'll make sure of it, Sir!", "soft", "narrow", "angry", "mid")

            call cho_walk(570, "base")

    call cho_main("Now, if you don't mind, Sir...", "soft", "base", "base", "R", xpos="mid", ypos="base", flip=True)
    call cho_main("I'd like you to call that Gryffindor slut to your office!", "soft", "base", "base", "L")
    g9 "On it!"
    pause .8
    call cho_main("(...)", "annoyed", "narrow", "angry", "L")
    m "(...)"

    call hide_characters
    hide screen bld1
    with d3
    pause .5

    # Hermione enters.
    call play_sound("door")
    call her_chibi("stand", "door", "base")
    with d3
    pause .5

    call chibi_emote("thought", "hermione")
    pause .8

    call her_walk(660, "base")

    call cho_main("", "horny", "narrow", "angry", "L", xpos="mid", ypos="base", flip=True)
    call her_main("You wanted to see me, Professor?", "soft", "closed", "base", "mid", xpos="base", ypos="base")
    g9 "Yes, but I wasn't the only one."
    call her_main("(...)", "annoyed", "narrow", "angry", "R")
    call cho_main("Hi, Granger!", "smile", "narrow", "angry", "L")
    call her_main("Let me guess, we are here to marvel at your insecurity again?", "soft", "closed", "base", "mid")
    call cho_main("Granger, instead of spitting out insults, why don't you join me and have some fun for once?", "soft", "base", "raised", "L")
    call cho_main("Strip down for your headmaster as well, like you usually do...", "smile", "narrow", "angry", "L")
    call cho_main("Or would it bother you too much, now that I'm here?", "horny", "narrow", "base", "L")
    call her_main("*glare*", "angry", "base", "angry", "mid")
    call cho_main("Maybe then you'd have a chance to win against me!{w} And earn some useless Gryffindor points while you're at it.", "soft", "base", "base", "L")
    call her_main("I don't think that will be necessary...", "soft", "closed", "base", "mid")
    call cho_main("Well, we all already know how this is going to turn out don't we, [cho_genie_name]?", "soft", "base", "base", "mid")
    call cho_main("My body is still better than Miss Granger's, isn't it?", "smile", "narrow", "angry", "L")
    call her_main("", "annoyed", "base", "angry", "mid")
    call ctc

    call cc_pf_strip_T2_hermione

    jump end_cho_strip_event


label cc_pf_strip_T2_hermione:

    menu:
        "\"Definitely!\"":
            $ her_mood += 10
            call her_main("What?!", "open", "wide", "base", "stare")
            call cho_main("See, I told you!{w=0.6} How could he pick a walking bush on legs over this!", "smile", "narrow", "angry", "L")
            call her_main("", "angry", "base", "angry", "mid")
            call cho_main("Now tell her. Tell her why my body is superior compared to hers.", "soft", "closed", "base", "mid")
            m "..."
            m "Well, you're more flexible for one..."
            call cho_main("That's right, I am!", "soft", "wide", "base", "mid")
            call her_main("*Humph*...", "annoyed", "narrow", "angry", "R")
            call cho_main("And? What else?", "smile", "narrow", "base", "L")
            g4 "And Cho's thighs are probably the most impressive ones I've seen in the last hund-- decade or more!"
            call her_main("Well in that case...", "soft", "closed", "base", "mid")
            call her_main("In that case I'll give you a great opportunity to stare at them indefinitely.", "angry", "base", "angry", "mid")
            call cho_main("What are you talking about, Granger?", "soft", "narrow", "raised", "L")

            # Hermione walks towards the desk to pick up Cho's clothing.
            call her_walk("desk", "base", speed=1.5)
            pause .2
            if not d_flag_01: # Cho not on desk
                call cho_chibi("stand",570,"base", flip=False) # Facing the desk.
                with d3
            pause .6

            call cho_main("What are you doing?", "soft", "narrow", "base", "L", ypos="head", flip=False)

            # Hermione picks them up and runs off.
            call bld("hide")
            pause .2
            call play_sound("equip")
            hide screen cho_cloth_pile
            pause .5

            call cho_main("My clothes!", "open", "wide", "base", "L")

            call play_sound("running")
            call her_walk("door", "base", speed=2)
            call her_chibi(flip=False)
            with d3
            pause .1
            call cho_chibi(flip=True)
            with d3

            call her_main("Hey seeker, looks like someone will have to seek their way to their dorm without any clothes tonight.", "open", "base", "angry", "mid", ypos="head", flip=False)
            call cho_main("Hey!", "clench", "narrow", "angry", "L", ypos="head", flip=True)

            # Hermione leaves out of the door.
            hide screen bld1
            call her_chibi("stand", "door", "base", flip=True)
            with d3
            pause .2

            call her_chibi("leave")

            # Cho runs out the door.
            if d_flag_01: # On desk
                call play_sound("climb_desk")
                show screen blkfade
                with d3
                pause 1

                hide screen bld1
                hide screen blkfade
                call cho_chibi("stand", "desk", "base", flip=True)
                with d3
                pause .2

                call cho_main("{size=+4}Give them back, you bitch!{/size}", "scream", "narrow", "angry", "L", ypos="head", flip=True, trans=hpunch)

                call play_sound("running")
                call cho_walk(action="leave", speed=2)

            else:
                hide screen bld1
                call cho_chibi("stand",570,"base", flip=True) # Facing the door.
                with d3
                pause .2

                call cho_main("{size=+4}Give them back, you bitch!{/size}", "scream", "narrow", "angry", "L", ypos="head", flip=True, trans=hpunch)

                call play_sound("running")
                call cho_walk(action="leave", speed=2)

            call bld
            m "Did she just?"
            m "(...)"
            m "I don't think she's coming back..."

            return

        "\"Not even close.\"":
            $ cho_mood += 15
            call cho_main("Not even clo--", "soft", "wide", "base", "mid")
            call her_main("", "smile", "base", "base", "R")
            call cho_main("Professor, could you please repeat that for me?", "clench", "closed", "angry", "mid")
            m "Hermione's body is superior."
            call her_main("No surprise there...", "base", "base", "base", "R")
            call cho_main("No!{w} It clearly isn't!", "scream", "narrow", "angry", "mid", trans=hpunch)
            call cho_main("Are you mad, old man?", "angry", "narrow", "angry", "mid")
            call her_main("Don't use that tone with the headmaster...", "soft", "closed", "base", "mid")
            call cho_main("Nobody asked you!", "mad", "narrow", "angry", "L")
            call her_main("He's the wisest wizard at our school...{w} Surely his word should be final...", "smile", "narrow", "base", "mid_soft")
            m "I'd use the word astute but I'll take wise..."
            call cho_main("Why are you siding with her all of a sudden?", "annoyed", "narrow", "angry", "mid")
            m "Good question."
            m "Miss Granger, why don't you show Miss Chang why your body is superior to hers..."
            g9 "Share with us your two most compelling arguments..."
            call her_main("Sir?", "soft", "wink", "base", "mid")
            call cho_main("He's talking about your {b}tits,{/b} you dimwit!", "angry", "closed", "angry", "mid", cheeks="blush")
            call her_main("(...)", "clench", "narrow", "base", "down", cheeks="blush") # Embarrassed
            call cho_main("", "annoyed", "narrow", "angry", "mid")
            g9 "Yes Miss Granger!{w=0.5} Your very round{w=0.5}, handsomely spheroid{w=0.5}, perfectly sized{w=0.5}, very voluptuous and--"
            call her_main("I got it, Professor!", "clench", "happyCl", "worried", "mid", cheeks="blush")
            call cho_main("(Cow tits...)", "annoyed", "narrow", "angry", "R", cheeks="blush")
            $ hermione.strip("robe", "accessory")
            call her_main("Here...", "base", "narrow", "base", "mid_soft")

            # Hermione shows her breasts.
            call play_sound("equip")
            $ hermione.strip("top", "bra")
            with d3
            pause .5

            call her_main("", "base", "narrow", "base", "mid_soft", cheeks="blush")
            call ctc

            call her_main("Have a good look.", "soft", "narrow", "base", "mid_soft")
            call cho_main("(...)", "annoyed", "narrow", "angry", "downR", cheeks="blush") # Tries to look away.
            call her_main("And you'd better take in what a {b}real pair{/b} looks like, slut.", "smile", "narrow", "angry", "R")
            call cho_main("I'd rather not, or I might barf...", "soft", "narrow", "angry", "R") #
            g9 "Very nice, Miss Granger!"

            menu:
                "\"Ten points to Gryffindor!\"":
                    $ gryffindor += 10
                    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
                    call her_main("Thank you.", "soft", "narrow", "base", "mid_soft")

                "\"Fifty points to Gryffindor!\"":
                    $ cho_mood += 10
                    $ gryffindor += 50
                    call cho_main("(Fifty?!)", "soft", "wide", "base", "mid") # Shocked
                    call her_main("Thank you.", "soft", "narrow", "base", "mid_soft")
                    call cho_main("", "clench", "closed", "angry", "mid", cheeks="heavy_blush")

            g9 "For exposing those magnificent breasts."

            call play_sound("equip")
            $ hermione.wear("all")
            with d3
            pause .5

            call her_main("Any time, Professor.", "soft", "narrow", "base", "mid_soft")
            call cho_main("(I bloody hate her!)", "angry", "narrow", "angry", "L", cheeks="heavy_blush")

            call her_main("If you don't mind, Sir.", "open", "base", "base", "R")
            call her_main("I'd like to leave now.", "soft", "base", "base", "mid")
            call cho_main("By all means, just go already.", "soft", "narrow", "angry", "R")
            call her_main("Did something not go as you expected?", "smile", "base", "base", "R")
            call her_main("Did you think having me here when you exposed yourself would make me jealous...", "soft", "closed", "base", "mid")
            call cho_main("(...)", "annoyed", "narrow", "angry", "L", cheeks="blush")
            call her_main("Thank you for inviting me, Professor.", "soft", "narrow", "base", "mid_soft")
            call her_main("I {b}did{/b} enjoy this little obscene \"freak-show\" you arranged for me...", "grin", "narrow", "base", "mid_soft")
            call cho_main("You'll regret this, Granger!", "clench", "narrow", "angry", "L", cheeks="heavy_blush")

            if game.daytime:
                call her_main("Have a nice day, Professor.", "soft", "closed", "base", "mid")
            else:
                call her_main("Have a good night, Professor.", "soft", "closed", "base", "mid")

            m "(...)"
            call her_main("See you in class Chang!", "grin", "narrow", "base", "R_soft")
            call cho_main("*Tzzzz*!", "angry", "closed", "angry", "mid", cheeks="blush")
            call cho_main("Cow...", "annoyed", "narrow", "angry", "R", cheeks="heavy_blush")

            # Hermione leaves.
            call her_walk(action="leave")

            # Cho stands close to your desk.
            call hide_characters
            show screen blkfade
            call cho_chibi("stand", "desk", "base", flip=False)
            with d3

            hide screen blkfade
            call cho_main("I thought you were on my side, Sir!", "soft", "narrow", "angry", "mid", xpos="mid", ypos="base", flip=False, trans=fade)
            m "I'm on nobody's side, because nobody is on my side..."
            call cho_main("You were supposed to have my back! Not Granger's!", "angry", "closed", "angry", "mid")
            call cho_main("That {b}whore{/b} doesn't deserve your praise!", "soft", "narrow", "angry", "mid")
            m "She made some good arguments..."
            g9 "\"A couple\" of good arguments, to be precise!"
            call cho_main("They're barely larger than mine...", "annoyed", "narrow", "base", "downR", cheeks="blush")
            call cho_main("You'll see, Sir.{w} I'm better than her.{w} And I'll prove it to you...", "soft", "narrow", "angry", "mid")
            g9 "Well, that is yet to be seen."

            # Cho gets dressed.
            show screen blkfade
            with d5
            $ cho.wear("all")
            hide screen cho_cloth_pile
            hide screen blkfade

            call cho_main("Sir, my *Ehm*...{w} my panties...", "open", "narrow", "angry", "R", cheeks="blush", xpos="mid", ypos="base", trans=fade)
            m "Oh, of course..."
            call cho_main("", "annoyed", "narrow", "angry", "mid", cheeks="blush")
            pause .5
            m "Give me just a moment..."
            $ renpy.sound.play("sounds/sniff.mp3")
            call nar(">You give Cho's panties one last sniff before handing them back to the girl.")
            g4 "There."
            call cho_main("(Pervert...)", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call cho_main("I think it's time for me to go now.", "soft", "closed", "angry", "mid")
            call cho_main("Until next time, [cho_genie_name].", "soft", "narrow", "angry", "mid")

            # Cho leaves.
            call cho_walk(action="leave")

            call bld
            g4 "Damn!"
            g9 "For somebody that does a lot of exercising, she smells really nice!"
            m "Maybe I should be a bit nicer to her next time..."

            $ has_cho_panties = False

            return


        "\"Let Hermione assess you, Cho.\"":
            $ her_mood += 6
            call cho_main("Her?", "soft", "wide", "base", "mid")
            call her_main("I couldn't care less about the way she looks!", "soft", "base", "angry", "mid")
            call cho_main("(...)", "annoyed", "narrow", "angry", "L")
            m "Are you sure about that? I've seen you staring..."
            call cho_main("", "base", "narrow", "angry", "L")
            call her_main("Because she just so happens to be standing there, butt naked!{w} In your office!", "angry", "closed", "angry", "mid")
            m "I'd like you to rate Miss Chang's figure, truthfully, and to the best of your ability."
            call her_main("Really? Do I have to?", "annoyed", "base", "base", "mid")
            g9 "You do! I'd really like to hear your opinion on Miss Chang's shamelessly exposed body!"
            call cho_main("*Mhmm*", "base", "closed", "base", "mid") # Self assured.
            call her_main("Fine...", "soft", "narrow", "angry", "R")
            call her_main("\"Poor,\" I'd say...", "soft", "closed", "base", "mid")
            call cho_main("How dare you!{w=0.6} You snobby skunk!", "scream", "narrow", "angry", "L", trans=hpunch)
            call her_main("", "base", "base", "base", "R")
            m "(Is that better or worse than \"troll?\")" # Snape explained school ratings during the match.
            call cho_main("Our Professor asked you to rate my body truthfully!", "mad", "narrow", "angry", "L")
            call her_main("Which I did!{w} And it's at \"dreadful\" now!", "soft", "closed", "base", "mid")
            call cho_main("\"Dreadful?!\"", "soft", "wide", "base", "mid")
            call cho_main("You're a {b}lying bitch,{/b} Granger!", "angry", "closed", "angry", "mid", cheeks="blush")
            call her_main("Sir, you can't let her talk to me like that!", "angry", "base", "angry", "mid")
            m "Bitch isn't even a proper curse word."
            m "You can say that on TV..."
            call cho_main("Granger, why don't you tell us which part of my immaculate body deserves such a poor rating?", "soft", "narrow", "angry", "L")
            call her_main("Very well...", "soft", "closed", "base", "mid")
            call her_main("For one, you are a {b}narcissistic bitch!{/b}{w} That makes the presumption her body is superior to all others...", "open", "base", "angry", "L")
            call cho_main("Because it is.", "smile", "narrow", "angry", "mid")
            call her_main("Not to mention that you have even fewer curves than some of the boys I know...", "grin", "base", "angry", "mid")
            call cho_main("", "annoyed", "narrow", "angry", "mid", cheeks="blush")
            call her_main("Maybe once your Quidditch endeavours all fail, you can apply for a profession to model male underwear...", "soft", "closed", "base", "mid")
            call cho_main("I wonder where you're getting {b}your{/b} undergarments from...", "soft", "closed", "base", "mid")
            call cho_main("Stealing them from Madam Pomfrey, are you?", "smile", "narrow", "angry", "mid")
            call her_main("I do not!!!", "open", "wide", "base", "stare")
            m "Girls, we all know what really counts is how we appear on the inside."
            call her_main("", "angry", "closed", "angry", "mid")
            call cho_main("Oh shut up!", "angry", "narrow", "angry", "mid")
            call her_main("Professor, you're the one who continuously asks us to expose ourselves!", "soft", "base", "angry", "mid")
            m "Well yes. I also never claimed that {b}I{/b} was pretty on the inside."
            m "You of all people should know better by now..."
            call her_main("Despicable...", "angry", "narrow", "angry", "R")
            call cho_main("Don't worry, Granger!", "soft", "narrow", "angry", "L")
            call cho_main("If you were to start doing hourly exercises, our Professor might even be attracted to you by the end of the year...", "soft", "closed", "raised", "mid")
            call her_main("Hourly exercises?", "soft", "wide", "base", "stare") # Shocked
            call cho_main("But I wouldn't say all hope is lost!", "smile", "narrow", "angry", "L")
            call cho_main("While your figure might be a bit repulsive to the eyes...", "soft", "closed", "base", "mid")
            call cho_main("I don't mind looking at those {b}huge melons{/b} of yours.", "soft", "narrow", "base", "L", cheeks="blush")
            call her_main("How dare you talk of them like that!", "angry", "narrow", "angry", "R")
            g9 "*Heh*... melons..."
            call her_main("Sir, I'd like to leave now.", "open", "base", "angry", "mid")

            call cho_main("Already missing your books, are you?", "annoyed", "narrow", "base", "L")
            call her_main("I am not.{w} And I don't appreciate being made fun of!", "angry", "closed", "angry", "mid")

            if game.daytime:
                call her_main("Good day, Sir.", "soft", "base", "angry", "mid")
                call cho_main("See ya around, Granger...", "smile", "narrow", "angry", "L")
                call her_main("*Hmpf*", "annoyed", "narrow", "angry", "R")

            else:
                call her_main("Good night, Sir.", "soft", "base", "angry", "mid")
                call cho_main("Nighty-night, Granger...", "soft", "narrow", "angry", "L")
                call her_main("*Tzzzzzh*!", "annoyed", "narrow", "angry", "R")

            # Hermione leaves.
            call her_walk(action="leave")

            show screen blkfade
            call cho_chibi("stand", "desk", "base", flip=False)
            with d3

            hide screen blkfade
            call cho_main("I have to say, [cho_genie_name], doing these favours is fun!", "smile", "narrow", "base", "mid", xpos="mid", ypos="base", flip=False, trans=fade)
            m "I'm glad you're enjoying yourself."
            call cho_main("Believe me, Sir. I am.", "smile", "narrow", "angry", "mid")
            call cho_main("", "horny", "narrow", "angry", "mid")
            pause .4

            # Cho gets dressed.
            call play_sound("equip")
            $ cho.wear("all")
            hide screen cho_cloth_pile
            with d3
            pause .5

            call cho_main("Now, if you excuse me...", "soft", "base", "base", "mid")

            if game.daytime:
                call cho_main("I have to head back to classes.", "soft", "base", "base", "R")
                m "I still got your--"
                call cho_main("See ya next time, [cho_genie_name]!", "smile", "narrow", "angry", "mid")
            else:
                call cho_main("I have to head back to my dorms.", "soft", "base", "base", "R")
                m "Don't you want your--"
                call cho_main("Sweet dreams, [cho_genie_name]!", "smile", "narrow", "angry", "mid")

            call cho_walk(action="leave")

            call bld
            g9 "Nice, I still got her panties!"

            if cho.is_equipped("panties"): # Cheats fallback
                call give_reward(">You have acquired Cho's panties!", cho.get_equipped("panties").get_icon())
            else:
                call give_reward(">You have acquired Cho's panties!", cho_panties_basic1.get_icon())
            $ has_cho_panties = True

            return



##############
### Tier 3 ###
##############


## Tier 3 - Event 1 ##

# Cho hops on your desk and she strips for you.
# You talk about the last match and Tonks' role in it.
# You tell Cho about Tonks' ability, and what she did to help winning the game.

label cc_pf_strip_T3_intro_E1:
    m "Come closer, [cho_name]."
    call cho_main("Yes, [cho_genie_name]...", "base", "narrow", "base", "mid")

    call cho_chibi("stand", "desk", "base")

    call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    g9 "Would you like to hop on my desk and strip for me again?"
    call cho_main("Strip for you, huh?", "soft", "narrow", "raised", "mid")
    call cho_main("Naturally you'd like me to undress to see if I've been keeping up with my workout? Staying in shape and all that...", "soft", "narrow", "angry", "mid")

    menu:
        "\"Of course...\"":
            call cho_main("[cho_genie_name], no need to continue the pretence...", "open", "closed", "base", "mid")
            call cho_main("We both know you don't really care about that stuff.", "open", "narrow", "base", "mid")
            call cho_main("All you want to do is ogle at my naked body.", "soft", "narrow", "angry", "mid")
            call cho_main("You're just like all the other teachers...", "annoyed", "narrow", "base", "R")
            m "You are one to say, you little slut!"
            m "You went through quite the effort to show the whole school your ass on that broom..."
            call cho_main("I only did that so we'd win!", "normal", "narrow", "angry", "mid")
            g9 "Keep telling yourself that, you little show-off!"
            g9 "Come here and hop on my desk already!"
            call cho_main("...", "annoyed", "narrow", "angry", "mid")

        "\"No, I just want a good, indecent strip-show!\"":
            g9 "I want to see that ass of yours bounce, baby!"
            call cho_main("At least you are honest with me...", "open", "closed", "base", "mid")
            call cho_main("I can't really blame you, you're just a man, after all...", "soft", "narrow", "base", "L")
            call cho_main("And I'm simply irresistible.", "smile", "narrow", "angry", "mid")
            g9 "That you are, you little slut!"
            g9 "Now hop onto my desk so I can have a good look at you."
            call cho_main("Yes, [cho_genie_name].", "base", "narrow", "angry", "mid")


    # Cho hops on your desk.
    call hide_characters
    show screen blkfade
    with d5
    call play_sound("climb_desk")
    pause 2

    call cho_chibi("stand", "on_desk", "on_desk", flip=False)
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call cho_main("", "base", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call ctc

    g9 "Yes! Strip for me, you naughty girl!"
    call cho_main("...", "horny", "narrow", "base", "down", cheeks="blush")
    pause .2

    # Remove top.
    call play_sound("equip")
    $ cho.strip("robe", "top", "bra")
    show screen cho_cloth_pile
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "angry", "mid", cheeks="blush")
    call ctc

    g9 "Marvelous as always."
    call cho_main("I'm glad you're enjoying yourself, [cho_genie_name]...", "base", "narrow", "angry", "down")
    g9 "That I do!"
    pause .2

    # Remove bottom.
    $ cho.strip("bottom")
    with d3
    pause .5

    call cho_main("", "base", "narrow", "base", "mid")

    if cho.is_equipped("panties"):
        call ctc

        g9 "And now those panties!"
        call cho_main("Of course, [cho_genie_name]...", "smile", "narrow", "base", "mid")
        pause .2

        # Remove panties.
        $ cho.strip("all")
        with d3
        pause .5

        call cho_main("...", "smile", "narrow", "angry", "downR", cheeks="blush")
        call cho_main("Here, [cho_genie_name]... You can have them.", "horny", "narrow", "angry", "mid", cheeks="blush")
        pause .5

        # Panties acquired message!
        if cho.is_equipped("panties"): # Cheats fallback
            call give_reward(">You have acquired Cho's panties!", cho.get_equipped("panties").get_icon())
        $ has_cho_panties = True

    else:
        pause .8

        # Remove panties.
        $ cho.strip("all")
        with d3
        pause .5

        call cho_main("", "horny", "narrow", "base", "mid", cheeks="blush")
        call ctc

    call cho_main("Do you like watching me, [cho_genie_name]?", "soft", "narrow", "base", "mid")
    call cho_main("You should know, Sir, I'm {b}incredibly{/b} thankful for your help.", "open", "closed", "base", "mid")
    call cho_main("Thanks to you, I get to do what I love...", "smile", "narrow", "base", "mid")
    m "Stripping?"
    call cho_main("No. Quidditch!", "annoyed", "narrow", "angry", "mid")
    call cho_main("Winning, to be precise...", "soft", "narrow", "base", "mid")
    g9 "Yes. I feel like a winner as well!"
    call cho_main("But, to tell you a secret...", "soft", "closed", "base", "mid")

    # mirror sprite
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=True)
    with d3
    pause .8

    call cho_main("", "smile", "narrow", "angry", "R", xpos=360, ypos="base", flip=True)
    pause .8

    call cho_main("I am starting to love doing {b}this{/b} as well.", "soft", "narrow", "base", "R", cheeks="blush")
    g9 "Yes, you little slut! Shake that ass for me!"
    call cho_main("I love the reaction I get from people...", "base", "base", "base", "up")
    call cho_main("From you... From Hermione...", "soft", "narrow", "base", "downR")
    call cho_main("Why don't we summon her? Maybe she'll join me this time...", "base", "narrow", "base", "downR")
    call cho_main("I think that could be fun.", "crooked_smile", "closed", "base", "mid")
    m "Hermione, you say?"
    g9 "How about we invite somebody else in her stead?"
    pause .2

    # mirror sprite
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .5

    call cho_main("Somebody else?", "upset", "base", "raised", "mid", xpos="mid", ypos="base", flip=False)
    g9 "Yes, to keep things interesting."
    call cho_main("*Hmm*...", "annoyed", "base", "raised", "mid")
    call cho_main("I suppose...", "soft", "base", "base", "R")
    m "Or are you only prepared to do it -- if you get to tease Miss Granger at the same time?"
    call cho_main("Alright, what's one student over another...", "soft", "narrow", "base", "R")
    m "It's not a student I'm thinking of."
    call cho_main("What do you mean, Sir?", "open", "base", "base", "mid")
    m "I want you to strip for one of your teachers!"
    call cho_main("A teacher?", "disgust", "wide", "base", "mid", cheeks="blush") # shocked
    call cho_main("No way I could do that!", "clench", "wide", "base", "mid", cheeks="blush")
    g9 "Look at it as just another challenge."
    call cho_main("", "annoyed", "base", "base", "mid")
    m "The teachers already got a good look at your assets during the last couple of games."
    m "And I know for a fact that a couple of them are quite interested in a closer look."
    call cho_main("Oh, yeah?", "soft", "base", "base", "down", cheeks="blush")
    call cho_main("Then who are you thinking of in particular?", "open", "base", "base", "R", cheeks="blush")

    $ cc_strip_no_snape = False # throwaway var used only in the next event.

    label .choice:

    menu:
        "\"Tonks\"":
            pass

        "\"Snape\"" if cc_strip_no_snape == False:
            $ cc_strip_no_snape = True # throwaway var used only in the next event.
            call cho_main("What?!", "clench", "wide", "base", "mid", cheeks="blush")
            call cho_main("You can't be serious!", "angry", "base", "angry", "mid") # angry
            call cho_main("[cho_genie_name], thanks to him we almost lost the match!", "open", "narrow", "angry", "mid")
            call cho_main("He gave those idiots a luck potion, remember?", "open", "closed", "angry", "mid")
            call cho_main("You should have thrown him out for that!", "clench", "narrow", "angry", "mid")
            m "All I care about is that he and his band of greenhorns lost the match against us..."
            call cho_main("...", "annoyed", "narrow", "angry", "mid")
            call cho_main("There is no way I'd ever strip for that greasy old bastard!", "open", "narrow", "angry", "mid")
            call cho_main("I'm not giving him the satisfaction.", "annoyed", "narrow", "angry", "R")
            m "Very well, forget about Snape."
            m "But what about..."
            jump cc_pf_strip_T3_intro_E1.choice


    call cho_main("Professor Tonks?", "quiver", "base", "base", "mid")
    m "You have yet to show her your gratitude for the help she provided..."
    m "She was such an important player during that last match, and greatly helped us secure that win."
    call cho_main("She did?", "upset", "base", "raised", "mid")
    call cho_main("I mean, she did get the Slytherins to join practice, but...", "annoyed", "base", "raised", "R")
    call cho_main("She wasn't even present for most of the actual game.", "soft", "base", "base", "R")
    g9 "Are you sure about that?"
    m "Well, you would have hardly been able to recognize her..."
    call cho_main("*Hmm*...?", "annoyed", "base", "raised", "mid")
    g9 "Curly long hair, and tits as big as honeydews."

    m "Didn't the way Hermione act, how she flirted with those Slytherin players, struck you as a bit odd?"
    g9 "You might even say... familiar?"
    call cho_main("Are you suggesting that Professor Tonks...", "mad", "base", "base", "mid")
    call cho_main("But how?", "clench", "base", "raised", "mid")
    m "Magic...{w=0.8} duh!"
    m "How about we call her on your next visit, then you can ask her yourself..."
    call cho_main("I suppose we could do that...", "crooked_smile", "base", "base", "mid", cheeks="blush")
    g9 "Splendid!"
    m "That should be all for today, [cho_name]."
    m "You're dismissed..."
    call cho_main("Yes, [cho_genie_name].", "base", "happyCl", "base", "mid")

    # Cho hops off your desk.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    call cho_chibi("stand", "desk", "base", flip=False)
    pause 1

    hide screen blkfade
    call cho_main("", "base", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    if game.daytime:
        call cho_main("I'll head back to classes, then.", "soft", "narrow", "base", "mid")
    else:
        call cho_main("I'll head back to our dorms, then.", "soft", "narrow", "base", "mid")

    m "Don't forget to put your clothes back on..."
    call cho_main("Right...", "disgust", "narrow", "base", "mid")
    pause .2

    # Cho puts her clothes back on.
    call play_sound("equip")
    $ cho.wear("all")
    hide screen cho_cloth_pile
    with d3
    pause .8

    call cho_main("Until next time, [cho_genie_name].", "base", "narrow", "base", "mid", cheeks="blush", xpos="right", ypos="base")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_strip_event


### Tier 3 - Event 2 ###

# Cho prompts genie to summon Tonks as she wants to know how she turned into Hermione
# Tonks enters and is immediately enticed by cho, she flirts with her a bit before cho starts asking questions.

label cc_pf_strip_T3_intro_E2:
    m "Alright, let's do this again."
    m "We're gonna get your teacher up here -- and you'll strip for us, understood?"
    call cho_main("Yes, [cho_genie_name].", "smile", "base", "base", "mid")
    m "You might want to change into your school clothing before she gets here..."
    call cho_main("Of course.", "base", "happyCl", "base", "mid")

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    # Equip Cho & Tonks default clothing.
    $ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ cho.equip(cho_outfit_default)
    $ tonks.equip(ton_outfit_default)

    call cho_chibi("stand", "desk", "base")

    hide screen blkfade
    call cho_main("*Ehm*...", "quiver", "narrow", "base", "downR", xpos="mid", ypos="base", trans=fade)
    call cho_main("The teacher you're about to summon, [cho_genie_name]...", "open", "narrow", "base", "mid")
    call cho_main("You're talking about Professor Tonks, right?", "soft", "narrow", "base", "mid") # suspicious
    m "Oh... of course."
    call cho_main("Well then, I'm ready.", "base", "base", "base", "mid")
    g9 "Ready to strip for your teacher?"
    call cho_main("I'm well aware of what I'm about to do, [cho_genie_name], and I'm not going to falter.", "annoyed", "narrow", "angry", "mid")
    call cho_main("Besides, it's not like I have any bits that she doesn't...", "open", "closed", "base", "mid")
    m "Not even trying to play coy anymore, are you?"
    call cho_main("Why should I? It's good practice.", "open", "narrow", "raised", "down") # confident
    g9 "Great positive thinking, [cho_name].{w=0.8} You'll make it far with that mindset."
    call cho_main("It's no big deal for me, [cho_genie_name].", "base", "narrow", "base", "mid")
    call cho_main("I'm not as prude and buttoned up as Hermione, you know...", "soft", "narrow", "base", "mid")
    call cho_main("And I'll finally get to know how Professor Tonks helped us during the Slytherin match!", "base", "happyCl", "base", "mid")
    g9 "Oh boy, you're in for a treat!"
    m "Just wait here at my desk while I summon her..."
    call cho_main("Yes, [cho_genie_name].", "base", "narrow", "base", "mid")
    call play_music("stop")

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    call cho_chibi(flip=True)

    # end blkfade
    hide screen blkfade
    with d5
    pause .8

    # Tonks enters.
    call play_sound("door")
    call ton_chibi("stand", "door", "base")
    with d3
    pause .5

    # thought emote
    call chibi_emote("thought", "tonks")
    pause .8

    # Tonks walks next to Cho.
    call ton_walk(540, "base")

    call play_music("tonks")
    call cho_main("", "soft", "narrow", "worried", "L", cheeks="blush", xpos="left", ypos="base", flip=True)
    if game.daytime:
        call ton_main("Hello, Professor.", "base", "base", "base", "mid", xpos="right", ypos="base")
    else:
        call ton_main("Good evening, Professor.", "base", "base", "base", "mid", xpos="right", ypos="base")

    call ton_main("Miss Chang. Didn't expect to see you here...", "base", "narrow", "base", "L")
    call ton_main("What a nice surprise.", "horny", "narrow", "base", "mid") # horny tongue
    call cho_main("...", "quiver", "narrow", "worried", "downR", cheeks="blush") # nervous
    call cho_main("*Ehm*...", "soft", "narrow", "worried", "down", cheeks="blush")
    m "Go on, Cho. She's not going to bite you..."
    call ton_main("*Hmm*?", "base", "base", "raised", "mid")
    g9 "Miss Chang was hoping she could repay you with a favour. For the help you provided against Slytherin."
    call ton_main("A favour, you say...", "crooked_smile", "narrow", "base", "mid")
    call cho_main("Y-yes, if that's okay with you, professor...", "horny", "narrow", "worried", "L", cheeks="blush") # blushing, still nervous
    call ton_main("Oh, anything for you, darling.", "base", "narrow", "base", "L")
    call ton_main("So, what will it be then?", "open", "base", "base", "mid")
    call ton_main("I presume you didn't invite me for a cup of tea, did you?", "base", "narrow", "base", "mid") # why remove?

    menu:
        "\"We need a second opinion on the girl's physique.\"":
            call ton_main("*Mhmm*?", "base", "base", "base", "mid")
            call ton_main("So naturally you thought of me to provide this... opinion?", "open", "narrow", "raised", "mid")
            m "You're quite the athletic witch yourself, are you not?"
            call ton_main("", "base", "narrow", "base", "mid")
            g9 "I'm certain there's no one better suited to judge the girl's body than yourself."
            call ton_main("Very well, professor...", "base", "base", "base", "mid")
            call ton_main("I'm not the one to question the headmaster's judgement.", "base", "narrow", "base", "mid")
            g9 "Great, then maybe you could give her your assessment -- from head to toe -- see if there's anything she could improve."
            call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="blush")
            call ton_main("Oh, I doubt I'll find anything to improve on this one...", "horny", "narrow", "base", "L", hair="horny") # horny
            m "Okay then..."
            m "Girl, You may start with the show."
            call ton_main("The show?!", "soft", "base", "raised", "mid")
            g9 "She'll have to take her clothes off, obviously!"
            call ton_main("Oh my!", "grin", "base", "shocked", "mid", hair="horny") # lip bite?
            m "Let's get started then, shall we."
            call ton_main("", "base", "narrow", "base", "L", hair="horny")
            g9 "Get on that desk, Miss Chang!"
            call cho_main("Okay.", "soft", "narrow", "worried", "downR", cheeks="blush")

        "\"She's going to strip for us...\"":
            call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="heavy_blush")
            call ton_main("Really?", "crooked_smile", "base", "shocked", "mid", hair="horny")
            call cho_main("...", "mad", "narrow", "worried", "downR", cheeks="blush") # embarrassed
            m "It's all just part of the girl's training..."
            g9 "To improve her confidence, and all that. And not shy away from a bit of nudity."
            call ton_main("I see... so this is why you've been such a daredevil on the pitch lately...", "horny", "narrow", "base", "L", hair="horny")
            call cho_main("...", "normal", "happyCl", "worried", "mid", cheeks="blush") #Blushes
            call ton_main("Well, if you think I can be of assistance, then you have my full support.", "base", "base", "base", "L")
            call cho_main("Thank you, Professor.", "soft", "narrow", "worried", "L", cheeks="blush")
            g9 "Great! Then get on that desk, Cho!"
            call cho_main("Okay.", "soft", "narrow", "worried", "down", cheeks="blush")


    # Cho starts stripping.
    call play_music("stop")
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    call play_sound("climb_desk")
    pause 1

    call cho_chibi("stand", 330, 360)
    call ton_chibi("stand", 410, "base")

    hide screen blkfade
    with d5
    pause .8

    call bld
    m "Excellent..."
    m "Now, what would you say are Miss Chang's best assets, Professor?"
    call bld("hide")
    pause .2

    # Cho turns around.
    call cho_chibi(flip=True)
    with d3
    pause .3

    call play_music("cho")
    call cho_main("", "quiver", "narrow", "worried", "L", cheeks="blush", xpos=330, ypos="base", flip=True)
    call ton_main("", "base", "narrow", "base", "L", xpos=460, ypos="base")
    g9 "Are you more into the girl's tits... or her ass?"
    call ton_main("*Hmm*--", "base", "narrow", "annoyed", "L", hair="horny")
    call cho_main("Professor!", "soft", "happyCl", "worried", "mid", cheeks="heavy_blush")
    m "It's a fair question..."
    call cho_main("...", "soft", "narrow", "worried", "L", cheeks="blush")
    call ton_main("If you're not comfortable with this, Miss Chang, then I'm not going to--", "open", "base", "base", "L")
    call cho_main("No!", "clench", "happyCl", "worried", "mid", cheeks="blush")
    call ton_main("*Hmm*?", "base", "narrow", "raised", "L")
    call cho_main("I mean...{w=0.5} It's fine...", "open", "narrow", "worried", "down", cheeks="blush")
    call cho_main("Feel free to answer him, Professor...", "soft", "narrow", "worried", "L", cheeks="blush")
    call play_sound("giggle")
    call ton_main("*giggles*", "base", "happyCl", "base", "mid")
    call ton_main("She's so cute when she's all flustered, isn't she?", "crooked_smile", "base", "base", "mid")
    call cho_main("...", "quiver", "happyCl", "base", "mid", cheeks="blush") #Heavy blush
    m "..."
    m "So, what's your opinion?"
    g9 "I'm sure Miss Cho is dying to know..."
    call ton_main("I don't know how I could possibly answer such a difficult question, Professor.", "soft", "narrow", "base", "mid")
    m "Then let me help you with your decision..."

    g9 "Cho, do your thing."
    call ton_main("", "base", "narrow", "base", "L")
    call cho_main("Of course, Sir...", "open", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("...", "angry", "narrow", "base", "down", cheeks="blush")
    pause .2

    # Remove top.
    call play_sound("equip")
    $ cho.strip("robe", "top")
    show screen cho_cloth_pile
    with d3
    pause .5

    call cho_main("", "horny", "happyCl", "worried", "mid", cheeks="blush")
    call ctc

    call ton_main("*Hmm*... Very promising.", "base", "narrow", "base", "L")
    call cho_main("...", "horny", "narrow", "worried", "down", cheeks="blush")
    pause .2

    # Remove bra.
    $ cho.strip("bra")
    with d3
    pause .5

    call ton_main("", "base", "narrow", "raised", "L", hair="horny")
    call cho_main("", "quiver", "narrow", "base", "downR", cheeks="heavy_blush")
    call ctc

    call ton_main("Merlin's burly bosom!", "grin", "narrow", "annoyed", "L", hair="horny")
    call cho_main("", "upset", "happyCl", "worried", "mid", cheeks="heavy_blush")
    g9 "How about now?"
    m "Ever seen such a perfectly shaped pair of quaffles before?"
    call ton_main("Did you just call them quaffles?", "soft", "narrow", "raised", "mid", hair="horny")
    call cho_main("...", "mad", "narrow", "worried", "downR", cheeks="blush")
    m "So, what's your opinion?"
    call ton_main("What would you like me to say, Professor?", "base", "narrow", "base", "mid", hair="horny")
    call ton_main("That I'd like to run my mouth all over those perky nipples of hers?", "horny", "narrow", "angry", "L", hair="horny")
    call cho_main("Professor!", "open", "happyCl", "worried", "mid", cheeks="heavy_blush") # closed eyes, worried, embarrassed.
    call ton_main("Sorry sweetie, but Professor Dumbledore wanted my honest opinion.", "open", "closed", "raised", "mid", hair="horny")
    call ton_main("Your breasts are quite perfect, Miss Chang.", "base", "narrow", "base", "L", hair="horny")
    call cho_main("...", "normal", "narrow", "worried", "L", cheeks="blush")
    call cho_main("I don't think they're big enough.", "open", "narrow", "worried", "downR", cheeks="heavy_blush") # sad
    call cho_main("", "normal", "narrow", "worried", "down", cheeks="heavy_blush")
    call ton_main("Big enough for what? Impress some idiot?", "open", "narrow", "annoyed", "L", hair="angry")
    call ton_main("No offense, Professor.", "soft", "narrow", "base", "mid")
    m "None taken..."
    call ton_main("You don't need large breasts. Especially not if you want to have a career in Quidditch.", "open", "base", "base", "L")
    call cho_main("", "annoyed", "narrow", "base", "L", cheeks="blush")
    call ton_main("Just have a look at mine... They're bothersome to fly with even at my size...", "soft", "base", "shocked", "down")
    call play_music("stop")
    pause .2

    # Tonks starts stripping.

    # Remove robe.
    call play_sound("equip")
    $ tonks.strip("robe")
    with d3
    pause .5

    call cho_main("", "disgust", "base", "raised", "L", cheeks="blush")
    call ton_main("", "base", "happyCl", "base", "mid")
    call ctc

    call cho_main("Professor, you don't have to--", "mad", "base", "raised", "L", cheeks="blush") #blush
    pause .2

    # Remove top and bra.
    call play_sound("equip")
    $ tonks.strip("top", "bra")
    with d3
    pause .5

    call ton_main("", "horny", "narrow", "annoyed", "L", hair="horny")
    call ctc

    call cho_main("P-{w=0.3}Professor!", "silly", "happyCl", "worried", "mid", cheeks="heavy_blush") #lip bite "glances away from Tonks #Heavy blush
    g9 "*He-he-he!*"
    call ton_main("No need to be shy, Miss Chang.", "base", "narrow", "base", "L", hair="horny")
    g9 "Yes, it's not like she has any bits you haven't seen before... is that not what you said, Cho?"
    call cho_main("R-Right.", "angry", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call cho_main("", "horny", "narrow", "worried", "L", cheeks="blush")
    m "So... what would you like to see next, Miss Tonks?"
    call ton_main("Her ass cheeks sure looked great on top of that broom...", "soft", "narrow", "base", "mid", hair="horny")
    call ton_main("I'd love to see them up close...", "base", "narrow", "base", "L", hair="horny")
    g9 "Couldn't agree more!"
    m "Cho, you heard your teacher's request."
    call cho_main("", "horny", "narrow", "worried", "mid", cheeks="blush")
    m "Turn around, and take off your skirt."
    call cho_main("Yes, Sir.", "clench", "narrow", "worried", "mid", cheeks="blush")
    pause .2

    # Cho faces Genie.
    hide screen cho_main
    with d5
    call cho_chibi(flip=False)
    call cho_main("", "quiver", "narrow", "worried", "down", cheeks="blush", xpos=260, ypos="base", flip=False, trans=d5)
    pause .8
    call ton_main("", "base", "narrow", "base", "down", hair="horny")
    m "Slowly..."
    pause .5

    # Remove bottom.
    $ cho.strip("bottom")
    with d5
    pause .5

    call cho_main("", "normal", "happyCl", "base", "mid", cheeks="blush")
    call ctc

    # Remove panties.
    m "And now your panties, Miss Chang."
    call ton_main("...", "horny", "narrow", "base", "down", hair="horny") # horny
    pause .2

    # Remove bottom.
    $ cho.strip("all")
    with d3
    pause .5

    call cho_main("", "horny", "narrow", "raised", "R", cheeks="heavy_blush")
    call ctc

    call play_music("cho")
    g9 "Quite firm, aren't they?"
    call play_sound("giggle")
    call ton_main("*giggles*", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("Yes, Indeed...", "grin", "narrow", "base", "mid", hair="horny")
    call ton_main("No wonder she's so steady on that broomstick.", "horny", "narrow", "angry", "down", hair="horny")
    call cho_main("...", "horny", "narrow", "base", "mid", cheeks="blush") # blushing
    call ton_main("Can't see anyone beating that, that's for sure.", "open", "narrow", "raised", "down", hair="horny")
    #call ton_main("Although, maybe in a physical--"

    m "So... what's your opinion, what do you prefer?"
    m "Her tits, or her ass?"
    call ton_main("*Hmm*...", "base", "narrow", "base", "down", hair="horny")
    call ton_main("You're not holding out on me, are you, Miss Chang?", "open", "narrow", "base", "L", hair="horny")
    call cho_main("What do you--", "angry", "narrow", "worried", "R", cheeks="blush")
    call ton_main("There's something missing...{w=0.5} I haven't seen everything yet, have I?", "crooked_smile", "narrow", "raised", "mid", hair="horny")
    g9 "But of course!"
    call ton_main("If I were to do any sort of judgement, I'd first need to see that cute little Snitch of yours.", "soft", "narrow", "base", "down", cheeks="blush", hair="horny")
    call cho_main("!!!", "clench", "wide", "base", "mid", cheeks="heavy_blush") # shock
    g9 "Miss Chang, why don't you turn around so Professor Tonks can give you a proper assessment."
    call cho_main("...", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush") # blush
    pause .2

    # Cho faces Tonks.
    hide screen cho_main
    with d5
    call cho_chibi(flip=True)
    call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="heavy_blush", xpos=330, ypos="base", flip=True, trans=d5)
    pause .8

    call ton_main("*Hmm*... Will you look at that...", "base", "narrow", "base", "down", hair="horny")
    call cho_main("...", "horny", "narrow", "worried", "L", cheeks="heavy_blush")
    call ton_main("Now, this is a level of confidence I haven't seen in a student before...", "horny", "narrow", "base", "mid", hair="horny")
    g9 "Yes, she's quite something, isn't she?"
    call cho_main("...", "base", "closed", "base", "mid", cheeks="blush") # blushing but faking confidence
    call ton_main("Although...", "base", "narrow", "base", "L", hair="horny")
    call ton_main("Does this snitch get frightened and dart away, once you try and get up close to it?", "grin", "narrow", "raised", "mid", hair="horny")
    call cho_main("..........", "base", "closed", "base", "mid", cheeks="blush") #not paying much attention/didn't know she was being addressed
    call ton_main("Miss Chang?", "open", "narrow", "raised", "L", hair="horny")
    call cho_main("Oh, sorry!", "crooked_smile", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call cho_main("Of course not, Professor -- I don't dart away from anything!", "soft", "narrow", "worried", "downR", cheeks="blush")

    ## Tonks wants to strip too. ##
    call ton_main("Excellent, since that question has been answered...", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("I assume you don't mind if I joined you on that desk, do you?", "horny", "narrow", "angry", "L", hair="horny")

    call play_music("stop")
    call cho_main("What?!", "soft", "wide", "raised", "mid", cheeks="blush") # blushing
    g9 "!!!"
    call ton_main("*Hmm*... Or is that snitch of yours going to dart off after all?", "soft", "narrow", "base", "down", hair="horny")
    call cho_main("", "angry", "happyCl", "worried", "mid", cheeks="blush")
    show screen blktone
    with d3
    m "(I sure hope the desk is sturdy enough...)"
    call hide_characters
    hide screen bld1
    hide screen blktone
    show screen blkfade
    with d5

    # Tonks chibi on desk next to Cho's. # Tonks is facing left

    call cho_chibi("stand", flip=True, 314, 366)
    call ton_chibi("stand", flip=False, 370, 360)

    call play_sound("climb_desk")
    pause 2

    hide screen blkfade
    with d5
    pause .8

    $ cho_zorder = 16 # in front of Tonks. 15 is default.
    call play_music("tonks")
    call ton_main("", "base", "narrow", "base", "L", hair="horny", xpos=345, ypos="base")
    call cho_main("T-Tonks!", "clench", "happyCl", "raised", "L", cheeks="heavy_blush", xpos=280, ypos="base", flip=True) #Closed eyes, embarrassed
    call ton_main("That's {b}Professor Tonks{/b} to you, Miss Chang.", "open", "narrow", "angry", "L", hair="angry") # stern look
    call cho_main("Sorry!", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call play_sound("giggle")
    call ton_main("*giggles*", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("I'm just kidding, you can call me whatever you like, sweetie...", "soft", "narrow", "base", "L", hair="horny")
    call ton_main("Catch that Snitch for me, will you...", "horny", "narrow", "base", "L", hair="horny")
    call cho_main("Snitch? What Snitch?", "soft", "narrow", "base", "L", cheeks="blush")
    call ton_main("Down here.", "grin", "narrow", "base", "down", hair="horny")
    call cho_main("", "annoyed", "narrow", "base", "down", cheeks="blush")
    pause .2

    # Remove bottom.
    $ tonks.strip("bottom","panties")
    with d3
    pause .5

    call ton_main("", "horny", "narrow", "base", "down", hair="horny")
    pause .8

    call cho_main("!!!", "normal", "wide", "raised", "down", cheeks="blush")
    g9 "Now that's what I'm talking about!"
    call cho_main("Professor!", "clench", "wide", "raised", "down", cheeks="heavy_blush")
    call ton_main("Believe me, I'm just getting started...", "base", "narrow", "base", "mid", hair="horny")
    pause .5

    # Remove other clothes.
    $ tonks.strip("all")
    with d3
    pause .5

    call ton_main("", "horny", "narrow", "base", "L", hair="horny")
    call cho_main("", "base", "narrow", "worried", "down", cheeks="heavy_blush")
    call ctc

    call cho_main("...", "angry", "narrow", "worried", "downR", cheeks="heavy_blush") # heavy blush
    g9 "Don't be shy, Miss Chang."
    call ton_main("*Hmm*... Yes, don't be shy.", "crooked_smile", "narrow", "base", "L", hair="horny")
    call ton_main("I've yet to give you my verdict.", "soft", "narrow", "raised", "down", hair="horny")
    call cho_main("...", "normal", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call ton_main("Now, up this close, it's obvious what your best feature is, Miss Chang...", "open", "narrow", "base", "down", hair="horny")
    call ton_main("I must say I simply love your--", "horny", "narrow", "base", "down", hair="horny")

    # Snape enters.
    call play_music("stop")
    call hide_characters
    hide screen bld1
    with d3

    call play_sound("door")
    call sna_chibi("stand", "door", "base")
    with d3
    pause .1

    call bld
    m "*Hmm*...?"
    with hpunch
    g4 "{b}Balls!{/b}"
    call sna_main("...", "snape_47", ypos="head") #smirk
    call ton_main("What? No I was talking about her--", "soft", "narrow", "base", "mid", ypos="head", flip=False)
    call play_sound("scratch")
    with hpunch
    call cho_main("Professor Snape?!", "open", "wide", "raised", "L", ypos="head", flip=True) # shock
    call sna_main("Oh-- now what do we have here?...", "snape_13", ypos="head")
    call bld("hide")
    pause .2

    # Tonks turns around.
    call ton_chibi(xpos=360, ypos=360, flip=True)
    with d3

    # Snape walks closer to the middle.
    call sna_walk(xpos="mid", ypos="base")
    pause .8

    # Position Cho's sprite behind Tonks.
    $ cho_zorder = 15 # reset to default.
    $ tonks_zorder = 16 # in front of Cho. 15 is default.
    call play_music("snape")
    call sna_main("", "snape_40", xpos=560, ypos="base")
    call cho_main("", "normal", "wide", "base", "L", xpos=275, ypos="base", flip=True)
    call ton_main("", "annoyed", "narrow", "annoyed", "L", xpos=390, ypos="base", flip=True)

    call ton_main("Severus?", "mad", "base", "base", "L", trans=d5)
    call ton_main("{size=-4}Get behind me, Cho...{/size}", "open", "narrow", "base", "R") #small text

    $ cho_chibi.zorder = 2 # default is 3
    call cho_chibi("stand", flip=True, 320, 366)
    call cho_main("{size=-4}Yes-- Thank you.{/size}", "disgust", "happyCl", "worried", "mid", cheeks="heavy_blush", xpos=295, ypos=17, flip=True, trans=d3) # Sprite is slightly lowered.

    call ton_main("What are you doing here?", "annoyed", "base", "angry", "stare")
    call ton_main("Have you been spying on us behind that door?", "soft", "narrow", "base", "up", hair="horny")
    call sna_main("Of course not...", "snape_46")
    call cho_main("P-{w=0.3}Professor...", "open", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call ton_main("", "base", "narrow", "base", "downR", hair="horny")

    call sna_main("Ah, Miss Chang... Hiding behind Professor Tonks, are we?", "snape_02")
    call sna_main("I take it you're here to repay our headmaster for his help with your sudden Quidditch success?", "snape_37")
    #call sna_main("But how come Professor Tonks--", "snape_01")
    call ton_main("Well, what if she is,{w=0.5} Snivellus?", "soft", "narrow", "annoyed", "R", hair="horny")
    call sna_main("", "snape_38")
    call ton_main("She isn't doing anything wrong... at least not by your standards.", "grin", "closed", "shocked", "mid", hair="horny")
    call sna_main("Did I accuse her of doing anything wrong?", "snape_09")
    call sna_main("On the contrary...", "snape_02")
    call ton_main("", "annoyed", "narrow", "raised", "up")
    call sna_main("As head of the slytherin house, I'd like to personally congratulate her on her fair play.", "snape_37")
    call sna_main("Your performance was quite remarkable, Miss Chang.", "snape_13")
    call sna_main("Putting your best {b}ass{/b}ets on display for everyone was quite the sight.", "snape_46")
    call cho_main("...", "angry", "narrow", "worried", "downR", cheeks="heavy_blush") # embarrassed
    call sna_main("How very -- {b}ass{/b}piring of you...", "snape_41")
    call cho_main("{size=-4}Please do something, Professor.{/size}", "soft", "base", "angry", "mid", cheeks="heavy_blush") #small text
    m "What?"
    m "(Oh, right... I should probably do something about this...)"

    menu:
        m "(...)"
        "\"Severus, I think you should leave.\"":
            call cho_main("", "normal", "base", "angry", "L", cheeks="blush")
            call sna_main("Already? But I just got here...", "snape_05")
            call ton_main("I can't recall us inviting you, Severus.", "soft", "narrow", "shocked", "L")
            call sna_main("Do I require some kind of appointment to see the headmaster?", "snape_09")
            call sna_main("If there's a schedule I could look at, then perhaps I could plan my visits for when Miss Chang is not busy working on her insecurities...", "snape_03")
            #call sna_main("If there's a schedule I could look at, then perhaps I could plan my visits for when you two aren't taking advantage of Miss Chang's insecurities...", "snape_03") # Alternative line instead of the one above?
            call cho_main("...", "angry", "narrow", "angry", "L", cheeks="blush") #Blush #closed eyes #embarrassed
            #m "How did you--"
            call ton_main("What do you want, Snape?", "upset", "narrow", "annoyed", "L")
            pass

        "\"Severus! Please, stay and watch.\"":
            if cc_strip_no_snape: # Cho clearly told you she won't strip for Snape.
                $ cho_mood += 30
                call cho_main("Are you mad?!", "clench", "base", "angry", "mid", trans=hpunch)
                call cho_main("Sir, I clearly told you before, I won't do this in front of Professor Snape!", "open", "base", "angry", "mid")
                call sna_main("So you actually considered inviting me...", "snape_20")
                call cho_main("", "normal", "base", "angry", "L", cheeks="blush")
                call sna_main("That's surprising, considering our current bet...", "snape_21")
                call sna_main("I must say though, I appreciate the gesture, Albus.", "snape_22")
                g9 "Bros before--"
                call ton_main("Quiet! Both of you!", "open", "closed", "base", "mid")
                call sna_main("*Tssz*...", "snape_46")
                call sna_main("Well, I can read the room...", "snape_09")
                call ton_main("Clearly...", "upset", "narrow", "raised", "L")
                call sna_main("As it happens, I can't stay for too much longer anyway.", "snape_03")
                pass

            else:
                $ cho_mood += 12
                call cho_main("Professor, you can't be serious!", "angry", "wide", "raised", "mid", cheeks="heavy_blush")
                m "Calm yourself, girl."
                m "There's no touching allowed anyway... Those are the rules."
                call ton_main("Really? You never told me--", "annoyed", "narrow", "raised", "mid", hair="horny") #pout
                call cho_main("Send him away!", "clench", "base", "angry", "mid", cheeks="heavy_blush")
                g4 "Whatever... no need to get all indignant about this."
                call sna_main("...", "snape_09")
                m "You more than happily strip for all your other teachers... so why not Snape?"
                call cho_main("All my other teachers? It was only you and Tonks that I agreed to do this for!", "clench", "wide", "raised", "mid")
                pass

    call sna_main("As much as I'd like to watch you make a fool of yourself for us, Miss Chang, I have more important things to do.", "snape_13")
    show screen blktone
    m "(More important than this?...)"
    hide screen blktone
    call sna_main("I merely came here to discuss a private matter with our headmaster.", "snape_24")
    call sna_main("About this... Misunderstanding that occurred during the last Quidditch game.", "snape_09")

    call cho_main("There is nothing more to discuss.", "open", "closed", "angry", "R")
    call cho_main("We won against you, fair and square, you cheat...", "clench", "narrow", "angry", "L")
    call sna_main("Hold your tongue, Miss Chang, or I'll have to dock some points from your house...", "snape_03")
    call sna_main("Or worse...", "snape_20") #smirks
    call cho_main("*Pfff*... only first years care about house points...", "annoyed", "narrow", "base", "R") # small text
    g9 "Not taking that loss easy, are you? Disappointed that we won -- against all odds?"
    call sna_main("*Tzzzs*... by sheer luck you did.", "snape_32")
    call cho_main("Says the one who literally gave his team liquid luck!", "disgust", "narrow", "angry", "L", cheeks="blush")
    call sna_main("Ten points from Ravenclaw!", "snape_31")
    $ ravenclaw -= 10
    call cho_main("{size=-4}Like I care...{/size}", "annoyed", "narrow", "angry", "down", cheeks="blush")
    call ton_main("Let the girl speak her mind, Severus!", "open", "closed", "shocked", "mid")
    call ton_main("Or shall I remind you that you were the one who barged in here uninvited...", "open", "narrow", "base", "L")
    call sna_main("*Hmph*...", "snape_35")
    call sna_main("Can't let her spew such lies in the headmaster's presence, can I?", "snape_03")
    m "The hell is that supposed to mean?"
    call sna_main("I merely gave those boys some encouragement.", "snape_04")
    call sna_main("There was no need to involve something as valuable as a luck potion...", "snape_09")
    call cho_main("What?!", "angry", "happyCl", "angry", "mid", cheeks="blush")

    # Cho stops hiding behind Tonks.
    call play_music("stop")
    $ cho_chibi.zorder = 3 # Reset to default.
    call cho_chibi("stand", flip=True, 314, 366)
    call ton_main("", "annoyed", "narrow", "raised", "downR")
    call cho_main("But the entire Slytherin team drank some! They were even bragging about it!", "clench", "narrow", "angry", "L", xpos=275, ypos="base", flip=True, trans=hpunch)

    call sna_main("Which is why Madam Hooch checked them -- right after the game ended.", "snape_03")
    call sna_main("And no evidence of doping was found.", "snape_37") #smirk
    call sna_main("Now, if you'll excuse me...", "snape_09")
    call sna_main("I'll leave you three to indulge further in your...{w=0.8} debaucheries...", "snape_47")
    call cho_main("No! You stay where you are!", "scream", "base", "angry", "L")
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    # Cho moves in front of Tonks.
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    $ cho_chibi.zorder = 2 # Behind Tonks, so her ponytail doesn't cover her head.
    call ton_chibi("stand", flip=True, 322, 360)
    call cho_chibi("stand", flip=True, 360, 360)
    with d3
    pause .5

    $ tonks_zorder = 15 # Reset to default.
    $ cho_zorder = 16 # In front of Tonks. Default is 15.
    call play_music("cho")
    call sna_main("", "snape_13")
    call ton_main("", "annoyed", "shocked", "raised", "stare", hair="horny", xpos=310, ypos="base", flip=True)
    call cho_main("First you're going to explain yourself!", "clench", "base", "angry", "L", xpos=415, ypos="base", flip=True, trans=hpunch)
    call ton_main("", "clench", "wide", "shocked", "L", hair="horny", cheeks="blush")
    call cho_main("You somehow tricked them! They played far better than usual.", "mad", "base", "angry", "L")
    call ton_main("", "horny", "narrow", "worried", "down", hair="horny", cheeks="heavy_blush")
    call sna_main("*Hmm*... Very well, Miss Chang.", "snape_20")

    # Space Jam
    call sna_main("You truly believe I'd waste such a valuable potion on those blokes?", "snape_18")
    call cho_main("", "annoyed", "base", "angry", "L")
    call sna_main("It takes three months to brew and distill only a tiny vial of Felix Felicis... and it's quite the tedious endeavour to do so.", "snape_12")
    call sna_main("That prize money would barely cover half of the materials...", "snape_03")
    call cho_main("Prize money? What prize money?!", "open", "base", "angry", "mid")
    m "Don't interrupt your teacher."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "..."
    call ton_main("", "base", "narrow", "worried", "L", hair="horny", cheeks="heavy_blush")
    call cho_main("", "annoyed", "narrow", "angry", "L")
    call sna_main("All I did was give them a vial of pumpkin juice...", "snape_41")
    call sna_main("Then I told them I mixed in some liquid luck.", "snape_13")
    call cho_main("What stupid kind of tactic is that?", "soft", "narrow", "angry", "mid")
    call sna_main("", "snape_39")
    call ton_main("", "base", "narrow", "base", "mid", hair="horny", cheeks="blush")
    g4 "Hold on a minute..."
    m "Are you seriously telling me you gave them pumpkin juice... and pretended it was \"{b}Michael's secret stuff{/b}\"?"
    call sna_main("Michael's...{w=0.3} what?", "snape_38")
    g4 "You ripped off {b}Space Jam{/b}!"
    call sna_main("I'm sorry?", "snape_25") # confused
    g4 "You ripped off the plot of Space Jam!"
    call sna_main("I have no idea what you're talking about...", "snape_44")
    call ton_main("Neither do I.", "annoyed", "base", "raised", "mid", hair="horny")
    call cho_main("Sir, is this about that basketball thing again?", "disgust", "narrow", "angry", "mid")
    #m "Well you clearly didn't watch the outcome, did you?"
    g9 "Even Bugs Bunny couldn't help him win. Serves you right!"
    call ton_main("Who's Bugs Bunny?", "soft", "narrow", "raised", "mid", hair="horny")
    g9 "Oh boy, let me tell you--"
    call sna_main("Anyway.", "snape_31")
    call cho_main("", "annoyed", "narrow", "angry", "L")
    call sna_main("Miss Chang, I wish you the very best of luck on your next match.", "snape_45")
    call ton_main("", "normal", "narrow", "base", "L", hair="horny")
    call sna_main("You lot look like you're going to need it...", "snape_42")
    call cho_main("*Hmph*...", "annoyed", "base", "angry", "L")
    m "(...)"
    call play_music("stop")
    call hide_characters
    hide screen bld1
    with d3
    pause .1

    # Snape walks to the door.
    call sna_walk("door", "base")
    pause .2

    call sna_chibi("stand", "door", "base", flip=False)
    with d3
    pause .5

    call sna_main("Until then, Albus... Miss Chang...", "snape_20", xpos="base", ypos="head")
    call sna_main("{cps=7}Nymphadora...{/cps}", "snape_41", xpos="base", ypos="head")
    call ton_main("Stop calling me--", "clench", "closed", "angry", "mid", hair="angry", ypos="head", flip=True)

    # Snape leaves.
    call sna_chibi("stand", "door", "base", flip=True)
    with d3
    call sna_chibi("leave")
    pause .5

    call bld
    m "Fucking guy..."
    m "Who does he think he is?"
    m "Besmirching a classic such as Space Jam, like it was nothing..."

    # The girls face Genie.
    hide screen cho_chibi
    hide screen tonks_chibi
    $ cho_chibi.zorder = 2
    call cho_chibi("stand", flip=False, 330, 364)
    call ton_chibi("stand", flip=False, 370, 360)
    with d3

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos=190, ypos="base", flip=False)
    call ton_main("Well, that was a bit uncalled for... even for him.", "open", "narrow", "annoyed", "R", xpos=350, ypos="base", flip=False, trans=d5)

    call ton_main("When did I step on his toes?", "upset", "base", "base", "mid")
    m "Maybe when you called him Snivellus--"
    call ton_main("I'm not even part of your silly bet...", "upset", "base", "shocked", "downR")
    call cho_main("Bet?", "angry", "narrow", "raised", "mid")
    m "Let's not concern ourselves with Snape. He's out of the picture anyway."
    call cho_main("What bet?", "open", "narrow", "angry", "mid")
    call ton_main("So, shall we wrap things up, Professor?", "base", "happyCl", "base", "mid")
    m "Yes please."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    call ton_main("Next time I can show Miss Chang my little trick.", "grin", "base", "annoyed", "L", hair="horny")
    call ton_main("If we aren't getting interrupted again, that is...", "annoyed", "narrow", "base", "mid")
    call cho_main("Alright.", "annoyed", "base", "base", "R") # bit disappointed.

    if game.daytime:
        call ton_main("Let's head back to classes, shall we.", "soft", "base", "base", "L", hair="horny")
    else:
        call ton_main("Let me escort you back to your common room. It's getting late.", "soft", "base", "base", "L", hair="horny")

    # Fade to black.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")

    # Reset zorder.
    $ cho_zorder = 15 # reset to default.
    $ tonks_zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    call play_sound("climb_desk")
    pause 2

    hide screen blkfade
    with d5
    pause .5

    call ton_main("Thank you for your time, Professor.", "base", "base", "base", "mid", ypos="head", flip=False)
    if game.daytime:
        call cho_main("Good day, Sir.", "base", "base", "base", "mid", ypos="head", flip=False)
    else:
        call cho_main("Good night, Sir.", "base", "base", "base", "mid", ypos="head", flip=False)
    g9 "Until next time."
    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    call play_sound("door")
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5


    # Reset clothing.
    $ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)

    $ tonks_busy = True
    $ snape_busy = True

    # End event.
    jump end_cho_strip_event


### Tier 3 - Event 3 ###

# Cho and Tonks strip on your desk again.
# Tonks gives Cho a demonstration of her Metamorphmagi ability.

label cc_pf_strip_T3_intro_E3:
    m "[cho_name], why don't we summon your teacher again?"
    call cho_main("So we can give you another strip show, [cho_genie_name]?", "soft", "narrow", "angry", "mid") # annoyed
    g9 "Well, if you insist on it..."
    call cho_main("", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    m "Surely you haven't forgotten the actual reason we summoned her..."
    call cho_main("Of course not...", "open", "closed", "base", "mid")
    call cho_main("I wanted to ask her about what she did during the Slytherin match...", "annoyed", "narrow", "base", "mid")
    call cho_main("But then Professor Snape busted in before I got a chance to.", "angry", "narrow", "angry", "R", cheeks="blush")
    m "Right... let's give it another go then, shall we?"
    call cho_main("But no Snape this time!", "soft", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("If you expect me to expose myself to Professor Snape again, then you're sadly mistaken!", "clench", "base", "angry", "mid", cheeks="blush")
    m "No more Snivellus... got it..."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "Wait here at my desk while I summon your Teacher."
    call cho_main("Yes, [cho_genie_name].", "soft", "narrow", "worried", "R", cheeks="blush")

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    # Equip Tonks default clothing.
    # (Cho's outfit doesn't change this time.)
    #$ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ her_outfit_last.save() # Store current outfit.
    #$ cho.equip(cho_outfit_default)
    $ tonks.equip(ton_outfit_default)
    $ hermione.equip(her_outfit_default)
    $ cho.strip("robe") # removes school robe.

    call cho_chibi("stand", "desk", "base", flip=True)

    call play_music("stop")
    hide screen blkfade
    with d5
    pause .8

    call nar("You attempt to summon Tonks to your office.")
    pause .2

    call bld
    m "..."
    call cho_main("...", "quiver", "narrow", "base", "L", ypos="head", flip=True)


    # Fireplace turns on.
    if not fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
        pause .2
        $ fire_in_fireplace = True
        $ fireplace_OBJ.foreground = "fireplace_fire"
        with d5
        pause .8

    m "..................?"
    call bld("hide")
    pause .5

    # Fire flashes green. # Tonks appears in the fireplace.
    $ renpy.sound.play("sounds/fire_woosh.mp3")
    $ fire_in_fireplace = True
    show screen gfx_effect(780, 280, img="smoke", zoom=0.5)
    pause .1
    show screen fireplace_greenfire
    call ton_chibi("stand", 642, 392, flip=False) # In fireplace
    with d5

    # Tonks walks next to Cho.
    call ton_walk(540, "base")
    pause .8

    # Fireplace turns off.
    stop bg_sounds #Stops playing the fire SFX.
    $ fire_in_fireplace = False
    hide screen fireplace_greenfire
    with d5
    pause .2

    call play_music("tonks")
    call cho_main("", "base", "narrow", "worried", "L", cheeks="blush", xpos="left", ypos="base", flip=True)
    call ton_main("You called?", "base", "narrow", "base", "mid", xpos="right", ypos="base")

    call cho_main("Hello, Professor.", "soft", "narrow", "worried", "L", cheeks="blush")
    g4 "What{w=0.3} {b}the fuck{/b} just happened?"
    call ton_main("Oh, my apologies... I forgot we don't usually use the school's floo powder network.", "grin", "base", "base", "mid")
    m "Network? Do I need to set a password on my fireplace now?"
    call cho_main("", "annoyed", "narrow", "base", "mid")
    m "Could anyone just poof in here as they please?"
    call ton_main("At the moment, yes.", "silly", "happyCl", "base", "mid")
    m "(So much for privacy in this place...)"
    call ton_main("You might want to renew the protective enchantments that were cast on it. It's quite the security flaw.", "upset", "base", "raised", "mid")
    m "I'll have the {b}IT{/b} guy sort it out... A simple firewall should do it..."
    call ton_main("Anyhow, I thought it'd be faster than walking those dreadful stairs.", "base", "base", "base", "mid")
    call ton_main("Even if it's a bit of a waste of powder...", "upset", "base", "shocked", "down")
    call cho_main("They are by no means dreadful, Professor Tonks.", "open", "narrow", "base", "L")
    call ton_main("", "base", "base", "raised", "L")
    call cho_main("Without a gym, there's only a limited number of ways to do any exercises here at school.", "open", "closed", "base", "mid")

    menu: # change
        m "(...)"
        "\".............\"": # Genie lets them speak
            call cho_main("I take divination lessons solely as an opportunity to climb the north tower once a week.", "base", "happyCl", "base", "mid")
            call ton_main("Of course you do...", "base", "base", "base", "L")
            call ton_main("(Those thick legs have to come from somewhere.)", "grin", "narrow", "base", "mid", hair="horny")
            call ton_main("I had a hunch that something special was in store for me today.", "horny", "narrow", "raised", "mid", hair="horny")

        "\"You could exercise with me!\"":
            g9 "I can give you a workout of the likes you've never seen!"
            call ton_main("", "base", "narrow", "annoyed", "mid", hair="horny")
            call cho_main("*Hmm*?", "soft", "base", "raised", "mid")
            g4 "I'll wear you out until your muscles are sorer than ever!"
            call cho_main("Really!?", "crooked_smile", "base", "base", "mid") # happy
            call ton_main("Now-now, Professor. Don't make promises you can't keep...", "soft", "narrow", "base", "mid", hair="horny")
            call cho_main("Why haven't you shown me any of these workouts, sir?", "open", "base", "angry", "mid")
            m "We'll get to it at some point I'm sure."
            call ton_main("I sure wouldn't mind seeing you try out his techniques as well.", "grin", "narrow", "base", "L", hair="horny")
            g9 "No objections here!"
            call cho_main("Wicked!", "grin", "happyCl", "base", "mid")

    call ton_main("Come on, Miss Chang...", "open", "narrow", "base", "L", hair="horny")
    call cho_main("", "annoyed", "base", "base", "L")
    call ton_main("Let's give our headmaster a good show!", "crooked_smile", "narrow", "base", "mid", hair="horny")
    call cho_main("But what about your--", "open", "base", "base", "L") # embarrassed
    call ton_main("All in due time, sweetie.", "open", "closed", "base", "L", hair="horny")
    call cho_main("Alright.", "grin", "base", "base", "mid")
    call ton_main("Now, after you...", "horny", "narrow", "base", "L", hair="horny")

    # Cho and Tonks hop onto the desk.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .1

    show screen blkfade
    with d5


    # Tonks chibi on desk next to Cho's. # Tonks is facing left

    call cho_chibi("stand", flip=True, 314, 366)
    call ton_chibi("stand", flip=False, 370, 360)

    call play_sound("climb_desk")
    pause 2

    call play_music("cho")
    hide screen blkfade
    with d5
    pause .8

    $ cho_zorder = 16 # in front of Tonks. 15 is default.
    call cho_main("", "base", "narrow", "base", "L", cheeks="heavy_blush", xpos=280, ypos="base", flip=True)
    call ton_main("...", "base", "narrow", "raised", "L", hair="horny", xpos=345, ypos="base")
    call ton_main("Are you watching closely, Professor?", "open", "narrow", "base", "mid", hair="horny")
    g9 "You bet!"
    call ton_main("I wouldn't want you to miss what's about to happen...", "base", "narrow", "base", "mid", hair="horny")

    # Cho and Tonks undress.
    $ temp_var = False
    if cho.is_any_worn("robe", "top", "bottom"):
        $ temp_var = True
        call ton_main("Let me help you with that, Miss Chang.", "soft", "narrow", "base", "L", hair="horny")
        call ton_main("", "base", "narrow", "base", "L", hair="horny")

    # Remove Cho's robe.
    if cho.is_worn("robe"):
        pause .2
        call play_sound("equip")
        $ cho.strip("robe")
        with d3
        pause .5
        call cho_main("", "base", "narrow", "base", "R", cheeks="blush")
        pause .8

    # Remove Cho's top.
    if cho.is_worn("top"):
        pause .2
        call play_sound("equip")
        $ cho.strip("top")
        show screen cho_cloth_pile
        with d3
        pause .5
        call cho_main("", "horny", "narrow", "raised", "R", cheeks="heavy_blush")
        pause .8

        call nar("Tonks swiftly pulls the girl's top over her chiselled frame.")

    # Remove Cho's bottom.
    if cho.is_worn("bottom"):
        call cho_main("...", "horny", "narrow", "base", "mid", cheeks="heavy_blush") # embarrassed
        pause .2
        $ cho.strip("bottom")
        show screen cho_cloth_pile
        with d3
        pause .5
        call cho_main("", "horny", "narrow", "raised", "R", cheeks="heavy_blush")
        pause .8

        call nar("A quick tugg by her teacher, and Cho's bottom clothing slipped down her muscular things.")

    if temp_var == True:
        call cho_main("Please, Professor...{w=0.4} not so fast.", "clench", "happyCl", "base", "mid", cheeks="heavy_blush") # embarrassed?
        g9 "..."
        call ton_main("*Hmm*... Okay then.", "base", "narrow", "raised", "mid", hair="horny")
        call ton_main("I'll go next, shall I?", "grin", "narrow", "base", "mid", hair="horny")
    else: # Cho was already in underwear or nude.
        call ton_main("Couldn't you have waited for me, Miss Chang?", "soft", "narrow", "base", "L", hair="horny")
        call ton_main("I would have loved to help you undress...", "base", "narrow", "base", "L", hair="horny")
        m "No, that's just the girl's regular dress code around my office."
        call cho_main("", "clench", "narrow", "base", "downR", cheeks="heavy_blush")
        call ton_main("Is that so...", "soft", "narrow", "raised", "mid", hair="horny")
        call ton_main("*Hmm*... I suppose I should follow suit, then?", "base", "narrow", "base", "mid", hair="horny")
        call cho_main("...", "horny", "narrow", "base", "R", cheeks="blush") # embarrassed

    g9 "Go right ahead!"
    call ton_main("I've been dying to get out of this stuffy coat.", "open", "base", "shocked", "down")
    call play_music("tonks")
    call ton_main("", "base", "base", "base", "down")
    pause .2

    # Tonks removes her coat.
    call play_sound("equip")
    $ tonks.strip("robe")
    with d3
    pause .8

    call ton_main("There... much better, don't you think?", "base", "narrow", "base", "mid")
    call cho_main("...", "base", "narrow", "worried", "downR", cheeks="heavy_blush") #embarrassed
    call ton_main("Miss Chang, could you switch places with me, please.", "open", "base", "shocked", "L")
    call cho_main("*Ehm*... Y-Yes. Of course...", "soft", "narrow", "worried", "L", cheeks="heavy_blush")

    # Tonks' sprite moves in front of Cho, both are facing Genie.
    call hide_characters
    hide screen bld1
    with d3
    pause .5

    $ tonks_chibi.zorder = 2 # default is 3
    call cho_chibi("stand", flip=False, 370, 360)
    call ton_chibi("stand", flip=False, 320, 360)
    with d3
    pause .5

    $ cho_zorder = 15 # reset to default.
    $ tonks_zorder = 16 # in front of Cho # Default is 15.
    call cho_main("", "horny", "narrow", "base", "mid", cheeks="heavy_blush", xpos=345, ypos="base", flip=False)
    call ton_main("...", "crooked_smile", "narrow", "base", "mid", hair="horny", xpos=215, ypos="base", flip=False)

    call ton_main("Miss Chang, would you be so kind and assist me with my shirt?", "soft", "base", "shocked", "down", hair="horny")
    call cho_main("Yes, Professor...", "smile", "narrow", "base", "down", cheeks="heavy_blush")
    pause .2
    call cho_main("", "base", "narrow", "raised", "down", cheeks="heavy_blush", xpos=315, ypos="base", flip=False, trans=d5) # moves closer to Tonks.
    pause .8
    call cho_main("", "horny", "narrow", "base", "down", cheeks="heavy_blush")
    pause .2

    # Remove Tonks top.
    call play_sound("equip")
    $ tonks.strip("top")
    with d3
    pause .5

    call ton_main("", "horny", "narrow", "base", "mid", hair="horny")
    pause .8

    call nar("With some effort, Cho manages to remove her teacher's shirt.")
    call ton_main("Thank you, sweetie.", "soft", "narrow", "raised", "downR", hair="horny")
    call cho_main("", "base", "narrow", "base", "mid", cheeks="heavy_blush")
    call ton_main("*Hmm*...", "annoyed", "base", "raised", "down", hair="horny")
    call ton_main("I guess my tight trousers are next...", "base", "narrow", "base", "mid", hair="horny")
    call cho_main("...", "horny", "narrow", "base", "down", cheeks="heavy_blush") # blush
    call ton_main("I'll take it from here...", "soft", "narrow", "shocked", "downR", hair="horny")
    pause .2

    # Tonks turns around facing Cho.
    call ton_chibi(flip=True)
    #$ tonks_zorder = 15 # Reset to default.
    #$ cho_zorder = 16 # in front of Tonks # Default is 15.
    #call cho_main("", "base", "narrow", "raised", "L", cheeks="heavy_blush", xpos=345, ypos="base", flip=False)
    call ton_main("Let me show you how it's done. {heart}", "crooked_smile", "narrow", "base", "down", hair="horny", xpos=280, ypos="base", flip=True, trans=d5)

    call cho_main("...", "horny", "narrow", "worried", "down", cheeks="heavy_blush") # lip bite
    call ton_main("With trousers like these, you should start slowly... that's how the headmaster likes it. {heart}", "horny", "narrow", "base", "mid", hair="horny", cheeks="heavy_blush")

    call nar("Tonks carefully tugs at the thin fabric of her leggings, and slowly pulls them past her cheeks...", "start")
    call nar("As the fabric bundles up between her fingers, reaching lower and lower past her thighs, she pulls them off in one swift motion.", "end")

    # Remove Tonks bottom.
    $ tonks.strip("bottom")
    with hpunch
    pause .5

    call ton_main("", "horny", "narrow", "raised", "mid", hair="horny", cheeks="blush")
    pause .8

    m "Not wearing any underwear, I see..."
    call ton_main("I'll avoid it when I can...", "crooked_smile", "narrow", "base", "mid", hair="horny")
    call ton_main("Even while I'm in uniform. {heart}", "grin", "wink", "raised", "mid", hair="horny") #wink
    call ton_main("", "base", "narrow", "base", "mid", hair="horny")
    m "Anything you'd like to say, Miss Chang?"
    g9 "It's not every day you get to see such a gorgeous woman strip for you..."
    m "(...)"
    pause .5

    # Slap Tonks' ass!
    call slap_her
    call cho_main("", "open", "wide", "base", "mid", cheeks="heavy_blush")
    call ton_main("!!!", "clench", "shocked", "base", "stare", hair="scared", cheeks="heavy_blush") # shocked
    call nar("You give Tonks a hard slap on her ass.")
    call cho_main("", "horny", "base", "base", "down", cheeks="heavy_blush")
    call ton_main("Ouch...{w=0.4} Professor!", "crooked_smile", "narrow", "annoyed", "mid", hair="horny", cheeks="heavy_blush")
    m "Right, should've warned you, shouldn't I..."

    menu:
        "-Slap it one more time!-":
            call slap_her
            call ton_main("...", "clench", "base", "shocked", "ahegao", hair="horny", cheeks="blush") #pout #blush
            g9 "Want another?"
            call ton_main("Yes, please. {heart}", "crooked_smile", "narrow", "base", "mid", hair="horny", cheeks="heavy_blush")

            menu:
                "Slap it again!":
                    call slap_her
                    call ton_main("*Mmm*... Spank me, Sir!", "horny", "narrow", "angry", "mid", hair="horny", cheeks="heavy_blush")

                    menu:
                        "-Again!-":
                            pass
                    call slap_her
                    call ton_main("More...{w=0.3} Harder!", "clench", "base", "angry", "mid", hair="angry", cheeks="heavy_blush")
                    call cho_main("...", "disgust", "happyCl", "worried", "mid", cheeks="heavy_blush") # blushing #lip bite #looking away

                    menu:
                        "-Slap it hard!-":
                            pass
                    call slap_her
                    call ton_main("", "clench", "base", "shocked", "ahegao", hair="scared", cheeks="heavy_blush")
                    pause .5
                    call slap_her
                    pause .3
                    call slap_her
                    pause .3
                    call slap_her
                    call cho_main("", "horny", "narrow", "worried", "mid", cheeks="heavy_blush")
                    call ton_main("*Hngh*...", "upset", "narrow", "base", "ahegao", hair="horny", cheeks="heavy_blush")
                    call ton_main("Thank you, Professor. {heart}{heart}{heart}", "crooked_smile", "narrow", "worried", "mid", hair="horny", cheeks="heavy_blush")
                    g9 "You're welcome."
                    call cho_main("...", "horny", "narrow", "base", "downR", cheeks="heavy_blush")

                "Cho, you do the honors!":
                    call cho_main("What?! I can't--", "open", "wide", "base", "mid", cheeks="heavy_blush")
                    pause .2

                    # Tonks turns around.
                    call ton_chibi(flip=False)
                    call ton_main("", "base", "base", "base", "mid", hair="horny", cheeks="blush", xpos=215, ypos="base", flip=False, trans=d5)
                    pause .5

                    call ton_main("It's fine, Cho. Just give it a little slap.", "soft", "narrow", "base", "downR", hair="horny", cheeks="blush")
                    call cho_main("...", "angry", "base", "raised", "down", cheeks="heavy_blush")
                    call slap_her
                    call ton_main("That's it! Try a little harder...", "horny", "narrow", "base", "downR", hair="horny", cheeks="blush")
                    call slap_her
                    call ton_main("One more time...", "soft", "narrow", "shocked", "up", cheeks="blush")
                    call slap_her
                    call ton_main("*Hngh*... ", "upset", "narrow", "shocked", "ahegao", hair="horny", cheeks="heavy_blush")
                    pause .2

                    # Tonks turns around.
                    call ton_chibi(flip=True)
                    call ton_main("", "base", "base", "base", "mid", xpos=280, ypos="base", flip=True, trans=d5)
                    pause .8

                    call ton_main("Thank you, sweetie.", "crooked_smile", "narrow", "base", "L", cheeks="heavy_blush")
                    call cho_main("...", "quiver", "narrow", "worried", "down", cheeks="heavy_blush")

        "-Don't slap it again...-":
            pass

    m "Tell me, Cho...{w=0.3} do you like your teacher's body?"
    call ton_main("", "base", "narrow", "base", "mid", hair="horny", cheeks="heavy_blush")
    call cho_main("Of course I do.", "open", "narrow", "base", "down", cheeks="heavy_blush")
    call ton_main("", "base", "narrow", "base", "down", hair="horny", cheeks="blush")
    call cho_main("She's very fit and athletic and pretty, just like me.", "crooked_smile", "happyCl", "base", "mid", cheeks="blush")
    m "That's not what I meant..."
    g9 "Does her body turn you on?"
    call ton_main("", "base", "narrow", "annoyed", "mid", hair="horny", cheeks="blush") # eager look at Cho.
    call cho_main("Professor!", "clench", "wide", "base", "mid", cheeks="heavy_blush")
    m "It's a simple question..."
    call cho_main("Do I really need to answer?", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call ton_main("Please, Miss Chang...", "open", "narrow", "base", "L", hair="horny", cheeks="blush")
    call ton_main("I'm quite curious about your thoughts as well. {heart}", "base", "narrow", "base", "L", hair="horny", cheeks="blush")
    call ton_main("We'll keep it our little secret, I promise...", "crooked_smile", "narrow", "annoyed", "down", hair="horny", cheeks="blush")
    call cho_main("*Hmm*...", "mad", "narrow", "worried", "down", cheeks="heavy_blush")
    call cho_main("Fine...{w=0.3} I do think you're quite attractive, Professor.", "soft", "narrow", "worried", "downR", cheeks="heavy_blush")
    #g9 "Thanks."
    #call cho_main("", "annoyed", "narrow", "base", "mid")
    #call ton_main("Very funny, Professor Dumbledore... But I believe she was talking to me.", "open", "narrow", "raised", "mid", hair="horny")
    call ton_main("...", "base", "narrow", "annoyed", "mid", hair="horny", cheeks="blush") # sharp look at Genie
    call cho_main("Especially for a teacher.", "clench", "narrow", "raised", "down", cheeks="heavy_blush")
    call ton_main("For a teacher?", "horny", "narrow", "base", "L", hair="horny")
    call cho_main("I mean--", "soft", "happyCl", "worried", "mid", cheeks="heavy_blush") #clench #worried
    call ton_main("*Ha-ha*... I'll have to add that to my resume.", "grin", "narrow", "base", "mid", hair="horny")
    call cho_main("", "base", "narrow", "worried", "down", cheeks="heavy_blush")

    call ton_main("Although, teachers shouldn't be employed for their looks, but for their competence, isn't that right?", "open", "narrow", "annoyed", "mid", hair="horny", cheeks="blush")
    m "What?"
    g4 "Oh-- I mean yes...{w=0.3} of course..."
    call play_sound("giggle")
    call ton_main("*giggles*...", "base", "happyCl", "base", "mid", hair="horny", cheeks="blush")
    call ton_main("Enough with the small talk -- let's get these clothes off!", "soft", "base", "annoyed", "mid", hair="horny", cheeks="blush")

    call play_music("stop")
    call ton_main("", "horny", "narrow", "base", "mid", hair="horny")
    pause .1

    # Tonks removes the rest of her clothes.
    $ tonks.strip("all")
    with hpunch
    pause .2

    call cho_main("", "clench", "narrow", "worried", "mid", cheeks="heavy_blush")
    pause .5

    call nar("Within a blink of an eye, Tonks has removed all of her remaining clothing.")
    # nar "One minute her clothes were there, and then they were gone! It was like magic!"
    call cho_main("...", "clench", "narrow", "worried", "downR", cheeks="heavy_blush")
    call ton_main("Get in front of me, Miss Chang.", "open", "narrow", "base", "L", hair="horny")

    call play_music("cho")
    if cho.is_worn("bra"):
        call ton_main("It's time you show your headmaster your cute little breasts as well.", "soft", "narrow", "base", "mid", hair="horny")
    else:
        call ton_main("Let's show your headmaster these cute little breasts of yours.", "soft", "narrow", "base", "mid", hair="horny")

    call cho_main("They aren't that little...", "annoyed", "narrow", "worried", "down", cheeks="heavy_blush") # annoyed
    call ton_main("No, you're right, sweetie...", "soft", "narrow", "base", "down", hair="horny")
    call ton_main("They're just about perfect.", "horny", "narrow", "raised", "down", hair="horny")
    call ton_main("Now stand here so the Headmaster can see your tits.", "crooked_smile", "narrow", "base", "mid", hair="horny", cheeks="blush")
    call cho_main("...", "annoyed", "happyCl", "base", "mid", cheeks="heavy_blush")
    pause .2

    # Cho moves in front.
    $ cho_zorder = 16 # in front of Tonks # Default is 15.
    $ tonks_zorder = 15 # reset to default.
    call cho_main("", "angry", "narrow", "base", "down", cheeks="heavy_blush", xpos=300, ypos="base", trans=d5)
    call ton_main("Let me help you with that, Cho.", "base", "narrow", "raised", "down", hair="horny")
    pause .8

    # Remove Cho's bra.
    if cho.is_worn("bra"):
        pause .2

        # Remove Cho top.
        $ cho.strip("bra")
        with d3
        pause .5

        call cho_main("", "base", "happyCl", "worried", "mid", cheeks="heavy_blush")
        pause .8

        call nar("The lust filled teacher effortlessly removes the bra of her student.")

    call cho_main("...", "crooked_smile", "narrow", "worried", "mid", cheeks="heavy_blush")
    call ton_main("Fucking perfect {heart} aren't they, Professor?...", "horny", "narrow", "base", "mid", hair="horny")
    call ton_main("Move next to me, Cho. I need you to stand -- right here {heart}{heart}{heart}", "open", "base", "base", "downR", hair="horny")
    call cho_main("*Ehm*... yes, Professor.", "soft", "narrow", "worried", "L", cheeks="heavy_blush")
    call hide_characters
    hide screen bld1
    with d3
    pause .5

    # Cho turns around, facing Tonks.
    call cho_chibi("stand", flip=True, 314, 366)
    call ton_chibi("stand", flip=False, 370, 360)
    with d3
    pause .5

    call cho_main("", "base", "narrow", "base", "mid", cheeks="heavy_blush", xpos=280, ypos="base", flip=True)
    call ton_main("...", "grin", "narrow", "base", "L", hair="horny", xpos=345, ypos="base", flip=False, trans=d5)

    call play_sound("giggle")
    call ton_main("*giggles*...", "grin", "narrow", "shocked", "mid", hair="horny")
    call ton_main("This is so much fun!", "base", "narrow", "base", "up", hair="horny", cheeks="blush")

    if cho.is_worn("panties"):
        call cho_main("...", "horny", "narrow", "worried", "L", cheeks="heavy_blush")
        call ton_main("Lets unveil this magnificent thing, next!", "crooked_smile", "narrow", "base", "down", hair="horny")
        call cho_main("Professor, not so fast--", "horny", "narrow", "worried", "down", cheeks="heavy_blush")
        pause .2

        # Remove Cho top.
        $ cho.strip("panties")
        with vpunch
        pause .5

        call cho_main("", "horny", "narrow", "raised", "down", cheeks="heavy_blush")
        pause .8

        call nar("Tonks takes hold of Cho's panties and tugs them down in one swift move.")
        call cho_main("Ah!", "mad", "happyCl", "worried", "mid", cheeks="heavy_blush") # startled?

    call ton_main("*Hmm*... I can't decide which teacher has the best view now...", "horny", "narrow", "base", "mid", hair="horny", cheeks="blush")
    g9 "Looking pretty good from where I'm sitting..."
    call cho_main("...", "smile", "narrow", "worried", "mid", cheeks="heavy_blush")
    call play_music("stop")


    ## Transformation Section ##
    m "Now then, Miss Chang..."
    g9 "I think this would be the perfect time to ask Professor Tonks your question."
    call cho_main("W-what...{w=0.4} Oh, yes!", "soft", "base", "raised", "mid", cheeks="heavy_blush")
    call ton_main("*Hmm*?", "base", "base", "raised", "L", hair="horny")
    call cho_main("Professor Dumbledore told me about how you helped me during the Slytherin game.", "open", "base", "base", "L", cheeks="blush")
    call ton_main("What? You already told her I'm a Metamorphmagi?", "clench", "wide", "worried", "mid", hair="horny")
    call cho_main("You are?!?", "open", "wide", "raised", "L", cheeks="blush")
    call cho_main("That's so cool!", "grin", "happyCl", "base", "mid", cheeks="heavy_blush")
    call ton_main("Did I just spoil the surprise myself?{w=0.5} Whoopsie!", "mad", "narrow", "worried", "downR", hair="horny", cheeks="heavy_blush")
    m "Well... I didn't exactly tell her that much."
    call ton_main("Well, what's done is done...", "upset", "narrow", "worried", "downR", hair="horny", cheeks="blush")

    call play_music("trance")
    #call ton_main("Can I have your word that you won't tell anyone, Cho?", "base", "base", "base", "mid")
    #call cho_main("Yes, you have my word! I promise I won't tell anyone!", "base", "base", "base", "mid")
    #call ton_main("*Hmm*... Well, seeing the circumstances I guess that's good--", "base", "base", "base", "mid")
    g9 "Show the girl your \"meta thing\" already!"
    call ton_main("My \"metamorphmagi\" ability.", "soft", "narrow", "base", "mid")
    call cho_main("She's shown it to us in classes before, Professor.", "crooked_smile", "base", "base", "mid", cheeks="blush")
    call cho_main("You were changing your nose into that of a pig, and then a duck, and then--", "silly", "happyCl", "base", "mid", cheeks="blush")
    call ton_main("Yes... Well, that's usually about as much as I show people.", "crooked_smile", "narrow", "raised", "L")
    call ton_main("Most aren't aware of what else I can do. It's far more beneficial to me if people are unaware...", "grin", "narrow", "shocked", "mid")
    call ton_main("You see, I can do far more than just change my nose, or the colour of my hair...", "soft", "narrow", "raised", "L")
    call cho_main("Wicked!... What else can you do?", "grin", "base", "base", "L", cheeks="blush")
    g9 "How about a busty, stuck-up Gryffindor slut!"
    call ton_main("Gladly.", "grin", "narrow", "base", "mid")
    stop music
    pause .8

    # Transforms into Hermione
    call play_sound("magic")
    hide screen tonks_main
    $ hermione.strip("all")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ hermione_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("hide")
    call her_chibi("stand", flip=False, 370, 360)
    call her_main("", "crooked_smile", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=d5)
    with morph
    pause .2

    call cho_main("", "open", "wide", "raised", "L", cheeks="heavy_blush")
    call ctc

    call play_music("trance")
    call cho_main("{b}Holy shit!{/b}", "open", "wide", "raised", "L", cheeks="heavy_blush")
    m "Watch your language, girl..."
    call her_main("", "soft", "narrow", "angry", "L")
    ton "Yes. Watch your foul mouth, Chang!"
    call cho_main("I-I'm sorry...", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush")
    m "I'm just kidding... Swear as much as you want -- It's not going to bring up the age-ratings..."
    call her_main("", "annoyed", "narrow", "base", "down")
    ton "*Hmm*..."
    call her_main("", "soft", "narrow", "annoyed", "down")
    ton "Miss Granger is a bit heavier in the bosom area than I'm used to..."
    call her_main("", "grin", "narrow", "angry", "L")
    ton "What do you think, Miss Chang... Do they look that much larger than my own?"
    call cho_main("I...", "clench", "narrow", "worried", "down", cheeks="heavy_blush")
    call cho_main("I'm sorry, this is so weird!", "open", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call her_main("", "grin", "narrow", "base", "down")
    ton "*Hmm*? I thought you'd like them..."
    call her_main("", "crooked_smile", "narrow", "angry", "L")
    ton "I've heard rumours that you're quite fond of these tits, Miss Chang."
    call cho_main("Sorry! It's not that... It's just... you look exactly like her!", "disgust", "narrow", "worried", "down", cheeks="heavy_blush")
    call cho_main("You even sound like her!", "soft", "narrow", "worried", "L", cheeks="heavy_blush")

    $ hermione.get_equipped("hair").set_color([[255, 87, 171, 255], [255, 210, 227, 255], [230, 141, 32, 255]])
    # Original: [[255, 105, 180, 255], [251, 205, 222, 255], [230, 141, 32, 255]]
    # Brown: [[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]]
    call her_main("", "crooked_smile", "happyCl", "base", "mid", cheeks="blush")
    call play_sound("giggle")
    ton "*giggles*..."

    $ hermione.get_equipped("hair").set_color([[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]])
    call her_main("", "base", "narrow", "base", "R")
    ton "Naturally... That's the intended effect."
    call cho_main("If I didn't know any better, I'd think you were her!", "horny", "narrow", "raised", "down", cheeks="heavy_blush")
    call her_main("", "crooked_smile", "closed", "angry", "mid")
    ton "*Mhmm*... Last time I looked like this in front of you, you couldn't tell either."
    call cho_main("What?! When was that?", "soft", "base", "worried", "L", cheeks="heavy_blush")
    m "Right after the last game, if I remember correctly."
    call her_main("", "base", "narrow", "base", "mid")
    ton "Oh, that wasn't the only time, Professor."
    m "It wasn't?"
    call her_main("", "grin", "narrow", "base", "mid")
    ton "I sometimes stroll around the school grounds, disguised as one of the girls... wearing nothing but a school robe..."

    if hg_pr_flash.counter > 1:
        call her_main("", "crooked_smile", "narrow", "base", "down")
        ton "And If you ever had a boy say he got some tits flashed at him by Miss Granger... then it was most likely me."
        call cho_main("That's awesome!", "grin", "base", "base", "L", cheeks="blush")
        m "Well, I did tell Hermione to do it herself before."
        call her_main("", "open", "wide", "base", "stare", cheeks="blush")
        ton "Seriously? I had no idea!"
        call cho_main("Me neither!", "soft", "wide", "raised", "mid", cheeks="blush")
        call her_main("", "base", "narrow", "base", "down")
        ton "I guess that's one less thing to worry about while I do it..."

    call cho_main("I hope you didn't do that kind of stuff while you looked like me, Professor!", "open", "narrow", "angry", "L", cheeks="blush")
    call her_main("", "annoyed", "base", "base", "R")
    ton "*Ehm*..."
    call cho_main("If I find out you've shown some boys my breasts, then--", "open", "closed", "angry", "mid", cheeks="blush")
    call her_main("", "smile", "happyCl", "worried", "mid", cheeks="blush")
    ton "Of course not, sweetie."
    call cho_main("...", "annoyed", "narrow", "angry", "L", cheeks="blush")
    call her_main("", "grin", "base", "base", "R", cheeks="blush") # small text
    ton "It was your ass I showed them..."
    call cho_main("W-What?!", "clench", "wide", "angry", "L", cheeks="heavy_blush")
    g9 "*He-he-he-he*!"
    call cho_main("", "clench", "base", "angry", "L", cheeks="heavy_blush")
    call her_main("", "soft", "closed", "base", "mid")
    ton "It's not like you haven't done that yourself already, have you?"
    call her_main("", "base", "narrow", "base", "L")
    ton "In front of the entire school, no less..."
    call cho_main("...", "annoyed", "narrow", "angry", "L", cheeks="heavy_blush") # blush
    call her_main("", "open", "closed", "base", "mid")
    ton "Well, that's enough fun for today."

    # Tonks transforms back.
    call play_sound("magic")
    hide screen hermione_main
    call her_chibi("hide")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ tonks_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("stand", flip=False, 370, 360)
    call ton_main("", "base", "narrow", "base", "mid", xpos=345, ypos="base", hair=[[152, 89, 48, 255], [195, 137, 89, 255]], flip=False, trans=None) # Hermione brown
    with morph
    pause .2

    call cho_main("", "clench", "base", "raised", "down", cheeks="heavy_blush")
    call ctc

    call ton_main("Let's do this again some other time, shall we.", "horny", "narrow", "raised", "mid", hair="horny")
    g9 "Gladly."
    call ton_main("And, Miss Chang... if you ever want to have some quiet time with Miss Granger... my office door is always open.", "grin", "narrow", "base", "L", hair="horny", cheeks="heavy_blush")
    call cho_main("I-- *Ehm*...", "soft", "narrow", "worried", "downR", cheeks="heavy_blush") # super embarrassed
    m "Maybe you could wait with that until Quidditch is over."
    m "She has to stay focused, you know..."
    call cho_main("...", "disgust", "narrow", "worried", "down", cheeks="heavy_blush")
    call ton_main("*Sigh*... Alright...", "open", "closed", "shocked", "mid", hair="horny")

    # Fade to black.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")
    $ hermione.wear("all")

    # Reset zorder.
    $ cho_zorder = 15 # reset to default.
    $ tonks_zorder = 15 # reset to default.
    $ hermione_zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    call play_sound("climb_desk")
    pause 2

    call play_music("stop")
    hide screen blkfade
    with d5
    pause .5

    call bld
    g9 "And Tonks, next time we do this, wear the clothes I usually ask you to wear around my office."
    call ton_main("With pleasure.", "base", "narrow", "base", "mid", hair="horny", ypos="head", flip=False)

    if game.daytime:
        call ton_main("I'll escort you back to classes, Miss Chang.", "open", "narrow", "base", "L", hair="horny")
        call ton_main("Have a good day, Professor.", "base", "narrow", "base", "mid", hair="horny")
    else:
        call ton_main("I'll escort you back to your dormitories, Miss Chang.", "open", "narrow", "base", "L", hair="horny")
        call ton_main("Have a good night, Professor.", "base", "narrow", "base", "mid", hair="horny")

    g9 "Until next time."
    call cho_main("...", "upset", "happyCl", "worried", "mid", cheeks="heavy_blush", ypos="head", flip=False)
    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    call play_sound("door")
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5


    # Reset clothing.
    #$ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)

    $ tonks_busy = True

    # End event.
    jump end_cho_strip_event


label cc_pf_strip_T3_repeat:
    m "I'm in the mood for another strip-show, [cho_name]."
    call cho_main("Of course you are, [cho_genie_name].", "base", "narrow", "raised", "mid")
    call cho_main("Who's going to watch me this time?", "soft", "narrow", "base", "mid")
    m "*Hmm*... how about--"

    menu:
        #"\"Miss Granger\"":
        #    jump cc_pf_strip_T3_hermione

        "\"Miss Tonks\"":
            call cho_main("Alright then...", "grin", "narrow", "base", "mid")
            jump cc_pf_strip_T3_tonks


    ## Chibi Pos - for multiple people ##

    #call ton_chibi("stand", flip=False, 380, 360)
    #call cho_chibi("stand", flip=True, 322, 360)

    #call cho_chibi("stand", flip=True, 320, 370)

    #call cho_chibi("stand", flip=True, 314, 366)
    #call cho_chibi("stand", flip=False, 370, 360)
