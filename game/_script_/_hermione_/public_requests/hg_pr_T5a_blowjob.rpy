
### Give Classmate A Blowjob ###

label hg_pr_blowjob:

    # Setup
    $ current_payout = 65

    if hg_pr_blowjob.counter == 0:
        m "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)

    #Intro.
    if hg_pr_blowjob.counter == 0:
        m "[hermione_name], I will be buying another favour from you today."
        call her_main("Thank you, [genie_name]. I really appreciate it.", "open", "closed", "base", "mid")
        m "Sure, Happy to help."
        m "I need you to go give a blowjob to one of your classmates."

        stop music fadeout 1.0
        call her_main("!!!", "shock", "wide", "base", "stare")
        her "... with my mouth?"

        if not hg_blowjob.trigger: # She will refuse unless she gave you a blowjob
            call her_main("But we--.. I..", "shock", "wide", "base", "stare")
            call her_main("I've never done it before!", "angry", "wide", "base", "mid")
            m "I guess it's time you've learnt what {i}giving head{/i} means."
            call her_main("Absolutely not!", "annoyed", "narrow", "angry", "R")
            her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
            call her_main("I'm leaving this instant.", "scream", "closed", "angry", "mid")

            call her_walk(action="leave")

            $ her_mood += 9

            m "(*Hmm*...)"
            m "(Perhaps I should show her the ropes first before sending her off to blow her classmates.)"

            jump end_hermione_event

        if her_reputation < 15:
            jump too_much_public

        call play_music("hermione") # Music
        m "Yes, that's how it's usually done..."
        call her_main("[genie_name], I...", "upset", "closed", "base", "mid")
        call her_main("I refuse to sell you a depraved favour like that, [genie_name].", "open", "narrow", "annoyed", "mid", cheeks="blush")
        call her_main("Can't I just kiss another girl instead?", "open", "happyCl", "worried", "mid")
        her "I do not mind that..."
        m "[hermione_name], please stop wasting my time..."
        m "If you are not in the mood to sell favours today..."
        m "Then there is the door."
        call her_main("But I need the points, [genie_name]. You know that.", "upset", "closed", "base", "mid")
        m "It's as the saying goes, [hermione_name]..."
        m "\"If you won't suck a dick for it - you don't need it.\""
        call her_main("*Tch*...", "angry", "base", "angry", "mid", cheeks="blush")
        her "............................"
        m ".........................................."
        call her_main("... Alright.", "annoyed", "narrow", "angry", "R")
        her "I'll do it..."
        m "Go do it, then!"
        m "Report back to me after your classes."
        call her_main("...", "angry", "base", "angry", "mid", cheeks="blush")
        her "....."
        her "......."
        m "You may leave, [hermione_name]."
        her "..."
    else:
        if her_tier >= 6:
            call play_music("hermione") # Music
            m "[hermione_name]..."
            m "Do you believe in horoscopes?"
            call her_main("Not even a little bit, [genie_name]...", "annoyed", "narrow", "angry", "R")
            m "Well, maybe you should..."
            call her_main("...?", "open", "base", "base", "mid")
            m "Because I got yours right here and it says..."
            m "\"Dedicate today to something you do well\"..."
            call her_main("Something I do well...?", "soft", "base", "base", "R")
            g9 "Go suck on some cocks, [hermione_name]."
            call her_main(".....................", "annoyed", "narrow", "annoyed", "mid") # :(
            m "Report back to me after your classes as usual..."
            call her_main("Of course...", "annoyed", "narrow", "angry", "R")
        else:
            m "Go give some lucky boy another blowjob, [hermione_name]."
            call her_main("...... Again?", "disgust", "narrow", "base", "mid_soft")
            m "Yes, again."
            call her_main("..........", "annoyed", "narrow", "annoyed", "mid")

    call her_walk(action="leave")

    $ hg_pr_blowjob.inProgress = True

    jump end_hermione_event

label end_hg_pr_blowjob:
    $ gryffindor += current_payout

    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."
    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_blowjob.counter == 1:
        show screen blktone
        with d3

        call her_main("(I did it...)", "base", "narrow", "base", "dead", flip=True, trans=d3)
        call her_main("(I sucked off one of my classmates...)", "angry", "narrow", "base", "dead")

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hermione.set_cum(None)
    $ hg_pr_blowjob.inProgress = False

    # Increase Points

    if her_tier == 5:
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

label hg_pr_blowjob_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you complete your assignment?"

    if hg_pr_blowjob.is_tier_complete():
        her "Yes, [genie_name]."

        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_blowjob

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_blowjob.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        m ".............."

    m "[hermione_name], how did it go?"

    return

### Tier 5 ###

label hg_pr_blowjob_T5_E1:

    call hg_pr_blowjob_intro

    call play_music("hermione") # Music
    m "You know the drill, [hermione_name]. Start talking."
    call her_main("I gave a blowjob, [genie_name]...", "disgust", "narrow", "base", "mid_soft")
    m "Good. Tell me more."
    call her_main("What is there to tell, [genie_name]?", "annoyed", "narrow", "angry", "R")
    her "I sucked off one of my classmates today..."
    her "And that's it..."
    m "*Hmm*... I see..."
    m "..............."
    call her_main("....................................", "angry", "narrow", "base", "down")
    m "Did you swallow?"
    call her_main("...........................", "annoyed", "narrow", "annoyed", "mid")
    m "[hermione_name], did you swallow the load properly?"
    call her_main("Yes I did, [genie_name].", "angry", "base", "angry", "mid")
    m "Well, I suppose that will do for now..."

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T5_E2:

    call hg_pr_blowjob_intro

    call her_main("[genie_name], I...", "angry", "narrow", "base", "down")
    her "I tried, but..."
    call play_music("despair") # Music
    call her_main("The boy turned me down, [genie_name]...", "mad", "base", "worried", "mid", tears="soft")
    call her_main("I cannot believe that actually happened...", "angry", "base", "base", "mid", tears="soft")
    her "I am one of the top students in this school!"
    her "One of the most popular ones too..."
    call her_main("And he turns me down?", "angry", "base", "angry", "mid", tears="soft")
    her "Why would he insult me like that?!"
    m "So you're insulted because that boy refused to put his cock in your mouth?"
    call her_main("Wouldn't you be, [genie_name]?", "angry", "base", "angry", "mid", tears="crying")
    m "I.. I never considered that option myself, but I think I would get over it rather quickly..."
    call her_main("He rejected me [genie_name]...", "angry", "base", "angry", "mid", cheeks="blush")
    her "Who does he think he is?!"
    call her_main("With all due respect, [genie_name], you wouldn't understand...", "open", "narrow", "annoyed", "mid", cheeks="blush")
    m "Well, in any case. I can't pay you for this."
    call her_main("Of course... I would not expect you to, [genie_name].", "annoyed", "narrow", "annoyed", "mid", tears="soft")
    her "I failed to complete my task and deserve no praise of any kind..."
    her "And should you pay me out of pity..."
    call her_main("Then That would only worsen the insult...", "annoyed", "narrow", "angry", "R")
    m "*Hmm*... In that case, maybe I should pay you anyway..."
    call her_main("No, [genie_name]. I would not accept it...", "annoyed", "narrow", "annoyed", "mid")
    m "*Hmm*... Well, this will be all then."
    her "Have a good night, [genie_name]."

    call her_walk(action="leave")

    $ hg_pr_blowjob.inProgress = False

    jump end_hermione_event


label hg_pr_blowjob_T5_E3:

    call hg_pr_blowjob_intro

    call her_main("I still find the idea of performing a favour like this unappealing, [genie_name].", "annoyed", "narrow", "angry", "R")
    call her_main("But it went surprisingly well...", "annoyed", "narrow", "annoyed", "mid")
    call play_music("playful_tension") # Music
    her "I gave a proper blowjob to this handsome boy from Ravenclaw..."
    call her_main("And he was such a gentleman about it...", "open", "narrow", "worried", "down")
    call her_main("He even warned me when he was about to cum.", "angry", "narrow", "base", "down")
    m "A true gentleman indeed."
    m "Did you swallow?"
    call her_main("Of course I did, [genie_name].", "upset", "closed", "base", "mid")
    her "I told you -- I gave the boy a {b}proper{/b} blowjob."
    call her_main("It's the least I could do for someone who treated me with respect for a change...", "angry", "narrow", "base", "down")
    m "Well, in that case."

    jump end_hg_pr_blowjob

### Tier 6 ###

label hg_pr_blowjob_T6_intro_E1:

    call hg_pr_blowjob_intro

    call her_main("Splendid, [genie_name]. Simply splendid.", "base", "happyCl", "base", "mid")
    m "Really? Do tell."
    call play_music("playful_tension") # Music
    call her_main("Today I did something I wanted to do for such a long time now...", "base", "narrow", "base", "up")
    her "But never could muster up enough courage for..."
    m "*Hmm*...?"
    call her_main("Today I sucked off my two best friends in the entire world!", "soft", "narrow", "annoyed", "up")
    call her_main("And it was every bit as exciting as I thought it would be.", "base", "narrow", "worried", "down")
    call her_main("I made their cocks all sloppy with saliva...", "grin", "narrow", "base", "dead")
    her "I sucked on their balls too..."
    call her_main("But the best part was to see their faces...", "silly", "narrow", "annoyed", "up")
    her "The boys could not believe it was actually happening..."
    call her_main("To be honest, neither could I...", "silly", "narrow", "base", "dead")
    her "I, Hermione Granger -- the girl they knew for years..."
    call her_main("Sucking on their cocks...", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_main("Like some nasty slut...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "Are you in love with those boys, [hermione_name]?"
    call her_main("I don't know, [genie_name]... But I surely like their cocks...", "base", "happyCl", "base", "mid")
    her "Could I get paid now please?"
    m "Sure..."

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T6_E2:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum(hair="heavy", face="heavy")

    show screen blktone
    with d3
    call her_main("", "angry", "base", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    pause 1.0

    m "[hermione_name]..."
    m "You look like hell..."
    call play_music("hermione") # Music
    call her_main("[genie_name], I... Yes, thanks to that Slytherin boy...", "scream", "closed", "angry", "mid", tears="mascara")
    g4 "Slytherin...{w=0.4} Seriously?!"
    call her_main("Yes, [genie_name].", "annoyed", "narrow", "annoyed", "mid", tears="mascara")
    her "That nasty boy from Slytherin seemed to take a fancy to my face..."
    call her_main("Or...{w=0.5} My mouth rather I suppose...", "open", "narrow", "worried", "down", tears="mascara")
    her "And--"
    play sound "sounds/burp.mp3"
    call her_main("*Burp*!...", "shock", "happyCl", "worried", "mid", tears="mascara")
    call her_main("{i}Excuse moi{/i}.", "angry", "narrow", "base", "down", tears="mascara")
    call her_main("He came so much I was barely able to swallow it all...", "scream", "base", "angry", "mid", emote="angry", tears="mascara")
    her "Bloody bastard!"
    call her_main("You think I could file a complaint, [genie_name]?", "angry", "base", "angry", "mid", cheeks="blush", tears="mascara")
    m "*Hmm*... I suppose..."
    m "But keep in mind that the moment we bring the ministry into this..."
    m "All this \"favour selling business\" will have to stop immediately."
    call her_main("Oh...?", "open", "base", "base", "R", cheeks="blush", tears="mascara")
    her ".................."
    call her_main("Please, never mind what I just said then...", "base", "happyCl", "base", "mid", tears="mascara")
    m "Are you sure? You look pretty messed up."
    her "No, no. It's nothing really..."
    her "After all I was the one who offered him a free blowjob..."
    her "He just got a bit rough with me closer to the end, that's all..."
    her "I think I am just overreacting..."
    m "I see..."
    her "Can I just--"
    play sound "sounds/burp.mp3"
    call her_main("*Burp*!...", "shock", "wide", "base", "stare", tears="mascara")
    call her_main("Excuse me, [genie_name].", "angry", "narrow", "base", "down", tears="mascara")
    call her_main("{size=-3}(He just kept on cumming... My stomach feels so full...){/size}", "angry", "happyCl", "worried", "mid", emote="sweat", tears="mascara")
    call her_main("Can I get my payment now, please?", "open", "base", "base", "mid", tears="mascara")

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T6_E3:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum("heavy")

    show screen blktone
    with d3
    call her_main("", "base", "narrow", "base", "up", xpos="mid", ypos="base", trans=d3)
    pause 1.0

    her "Good evening, [genie_name]..."
    g4 "Hermione?!"
    g4 "What happened to you, [hermione_name]?"
    g4 "All I asked you to do was to give a blowjob to one of your classmates."
    call play_music("hermione") # Music
    call her_main("That... That was exactly what I did, [genie_name].", "angry", "narrow", "base", "down")
    m "[hermione_name], you are covered in cum head to toe."
    call her_main("I am?", "soft", "narrow", "annoyed", "up")
    her "Oh... Did I forget to clean myself up?"
    call her_main("How embarrassing...", "base", "narrow", "base", "mid_soft")
    her "That thing at the boy's restroom sort of escalated I suppose..."
    her "Before I knew what happened I was surrounded with hard throbbing cocks..."
    call her_main("Oh... Just talking about it makes me shiver with excitement... *err*..", "silly", "narrow", "base", "dead")
    call her_main("... I mean, with fear... no, not fear...", "grin", "narrow", "annoyed", "up")
    call her_main("Embarrassment...? No, that's not it... *Hmm*...", "base", "base", "base", "R", cheeks="blush")
    m "Are you asking me?"
    call her_main("Oh, excuse me, [genie_name]... I feel a little lightheaded...", "grin", "narrow", "base", "dead")
    her "I think I need to go lie down for a while..."
    m "Don't miss the shower room this time."
    call her_main("The shower room? Why?", "base", "narrow", "base", "mid_soft")
    m "Forget I said anything..."

    jump end_hg_pr_blowjob
