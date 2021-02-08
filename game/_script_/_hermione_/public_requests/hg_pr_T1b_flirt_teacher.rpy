

### Flirt With Teacher ###

label hg_pr_flirt_teacher:

    # Setup
    $ current_payout = 15

    if hg_pr_flirt_teacher.counter < 1:
        m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="right", ypos="base", trans=fade)
    m "[hermione_name], I want you to be especially flirtatious with your teachers today."

    #Intro
    if hg_pr_flirt_teacher.counter == 0:
        if hg_pr_flirt.counter > 0:
            call her_main("I will do my best, [genie_name]!", "base", "base", "base", "mid")
            call her_main("Now I understand why you asked me to flirt with these pesky Slytherin boys.", "open", "closed", "angry", "mid")
            call her_main("I am glad you finally decided to act, [genie_name]!", "open", "base", "base", "mid")
        else:
            call her_main("*huh*?!", "open", "base", "angry", "mid")
            call her_main("Why would I want to flirt with the teach--", "angry", "base", "angry", "mid")
            call her_main("O-oh... I see...", "grin", "base", "base", "R")
        m "*huh*?"
        call her_main("You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?", "normal", "squint", "angry", "mid")
        call her_main("I am honoured to pose as bait in this noble endeavour.", "open", "closed", "base", "mid")
        m "*Ehm*... Yeah, that's exactly what I'm doing."
        call her_main("Splendid! You can count on me, [genie_name]!", "smile", "squint", "angry", "mid")
    else:
        if her_tier >= 3:
            call her_main("As you wish, [genie_name].", "base", "squint", "base", "mid")
        elif her_tier >= 2:
            call her_main("I'll make sure to note every single detail, [genie_name].", "base", "squint", "angry", "mid")
            m "Looking forward to it..."
        else:
            call her_main("I shall provide you with a detailed report later tonight, [genie_name].", "normal", "squint", "angry", "mid")
            m "I will be waiting..."

    her "Well, I'd better go now. Classes are about to start..."

    call her_walk(action="leave")

    $ hg_pr_flirt_teacher.inProgress = True

    jump end_hermione_event


# End Event
label end_hg_pr_flirt_teacher:
    $ gryffindor += current_payout
    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave")

    $ hg_pr_flirt_teacher.inProgress = False

    # Unequip lockhart tattoo after the event
    if hermione.is_equipped("tattoo3") and hermione.get_equipped("tattoo3").id == "lockhart_tattoo":
        $ hermione.unequip("tattoo3")

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


label hg_pr_flirt_teacher_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")

    call her_main("Good evening, [genie_name].", "open", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call her_main("", "normal", "base", "base", "mid")
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    if hg_pr_flirt_teacher.is_tier_complete(): # If you have seen all events in this tier once, you get the choice to skip it.
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_flirt_teacher

            "\"Give me the details.\"":
                pass

    m "Tell me, [hermione_name], how many teachers did you flirt with?"

    if hg_pr_flirt_teacher.counter == 1:
        call her_main("*Ehm*... Okay...", "soft", "base", "base", "R")

    return

### Tier 1 ###

label hg_pr_flirt_teacher_T1_E1: # Flitwick

    call hg_pr_flirt_teacher_intro

    #if  her_whoring >= 3 and her_whoring < 6:

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Well, I tried flirting with Professor Flitwick...", "open", "base", "worried", "R")
    call her_main("But it didn't really work...", "annoyed", "squint", "angry", "mid")
    call her_main("..............................", "annoyed", "narrow", "angry", "R")
    m "How exciting..."
    m "Is this all you have for me today, [hermione_name]?"
    call her_main("Y-yes...", "open", "base", "worried", "mid")
    her "But [genie_name], I know for a fact that professor Flitwick is \"dirty\"!"
    her "Everyone knows that because of his height..."
    call her_main("He sometimes... *Ehm*...", "soft", "base", "base", "R")
    call her_main("He likes to look up under girl's skirts, [genie_name]!", "annoyed", "base", "worried", "R")
    m "Don't we all?"
    call her_main("What?", "open", "base", "base", "mid")
    m "I mean, don't we all hate it and must be outraged by a man like Professor Flick-stick?"
    call her_main("Er... It's \"Professor Flitwick\", [genie_name].", "normal", "squint", "angry", "mid")
    m "Right. Putting him on my \"Naughty list\" as we speak."
    call her_main("......................", "annoyed", "squint", "base", "mid")
    m "Well, I hate to admit it, but you did a lousy job of today's favour, [hermione_name]."
    call her_main("................................", "annoyed", "narrow", "angry", "R")

    menu:
        "\"Here are your points though.\"":
            call her_main("Really?", "angry", "base", "worried", "mid")
            call her_main("Thank you so much [genie_name]!", "smile", "happyCl", "base", "mid")

            jump end_hg_pr_flirt_teacher

        "\"No points for you!\"":

            call her_main("But [genie_name], I did my best!", "angry", "base", "worried", "mid")
            call her_main("You are going back on your promise [genie_name]!", "mad", "base", "worried", "mid", tears="soft")
            m "......................."
            stop music fadeout 1.0
            call her_main("How unbecoming of a school headmaster!", "scream", "happyCl", "worried", "mid")
            m "You are dismissed, [hermione_name]."
            call her_main("*Tsk*!", "angry", "base", "angry", "mid", emote="angry")

            call her_walk(action="leave")

            $ her_mood += 18

            $ hg_pr_flirt_teacher.inProgress = False

            jump end_hermione_event


label hg_pr_flirt_teacher_T1_E2: # Snape

    call hg_pr_flirt_teacher_intro

    call her_main("..................", "soft", "base", "base", "R")
    her "............................"
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]... I'm sorry... I just...", "open", "base", "worried", "mid")
    call her_main("............", "soft", "base", "base", "R")
    m "Did you do what I asked you to do?"
    call her_main("I tried, [genie_name]. I really did...", "open", "base", "base", "mid")
    m "Who did you try to flirt with?"
    call her_main(".........", "soft", "base", "base", "R")
    call her_main("Professor Snape, [genie_name].", "annoyed", "narrow", "angry", "R")
    call play_music("hermione") # HERMIONE'S THEME.
    m "Severus? Interesting..."
    m "How did it go?"
    call her_main("It was awful [genie_name]...", "normal", "squint", "angry", "mid")
    her "I am sorry, but I really hate professor Snape, [genie_name]!"
    m "(I'm pretty sure the feeling is mutual...)"
    m "Tell me what happened."
    call her_main("Nothing happened, [genie_name]. He just laughed at me...", "annoyed", "squint", "angry", "mid")
    call her_main("I may not have much feminine charm, but I tried to be nice...", "annoyed", "base", "worried", "R")
    call her_main("And he just started laughing in my face!", "scream", "closed", "angry", "mid")
    call her_main("... it is really scary to see professor Snape laugh...", "angry", "happyCl", "worried", "mid", emote="sweat")
    her "........"
    her "I am awful at flirting, I am sorry [genie_name]..."
    call her_main("But I know that professor Snape is \"dirty\"!", "angry", "base", "angry", "mid")
    her "If you were to send someone else, the outcome would be different, I just know it!"
    m "Someone else?"
    call her_main("Yes! Someone with more experience in this...", "upset", "wink", "base", "mid")
    her "Someone..."
    her "Someone... *Ehm*..."
    m "Sluttier?"
    call her_main("Yes, I suppose...", "disgust", "narrow", "base", "mid_soft")
    m "Don't you give up, [hermione_name]. We will make a slut *err*--"
    m "I mean a woman out of you yet!"
    call her_main("...................", "annoyed", "narrow", "annoyed", "mid")

    menu:
        "\"Here are your points, [hermione_name].\"":
            call her_main("", "base", "base", "worried", "mid")
            jump end_hg_pr_flirt_teacher

        "\"... I'm afraid you get no points this time.\"":
            call her_main("But I did my best...", "annoyed", "narrow", "angry", "R")
            call her_main("And I feel so humiliated now...", "angry", "happyCl", "worried", "mid", emote="sweat")
            call her_main("But I understand and won't argue with your decision...", "normal", "happyCl", "worried", "mid")

            call her_walk(action="leave")

            $ her_mood += 3

            $ hg_pr_flirt_teacher.inProgress = False

            jump end_hermione_event


label hg_pr_flirt_teacher_T1_E3: # Filch

    call hg_pr_flirt_teacher_intro

    stop music fadeout 1.0
    call her_main("I tried to flirt with mister Filch, [genie_name]...", "open", "base", "worried", "R")
    m "I see. {size=-5}(No idea who that is.){/size}"
    call play_music("hermione") # HERMIONE'S THEME.
    call her_main("Yes, I know that technically mister Filch is not a teacher...", "open", "base", "worried", "mid")
    m "*huh*?"
    call her_main("But he is part of the school's staff...", "base", "base", "base", "mid")
    her "And we did hit it off quite well too!"
    her "He was surprisingly sweet."
    her "But I don't think he is \"dirty\", [genie_name]."
    m "Gotcha... mister Filth is off the list then."
    call her_main("It's \"mister Filch\", [genie_name]...", "normal", "squint", "angry", "mid")
    m "What did I say?"
    call her_main(".......", "normal", "squint", "angry", "R")
    call her_main("Can I get my points now?", "open", "base", "worried", "mid")

    jump end_hg_pr_flirt_teacher



### Tier 2 ###

label hg_pr_flirt_teacher_T2_E1: # Slughorn

    call hg_pr_flirt_teacher_intro

    #elif her_whoring >= 6 and her_whoring < 9:

    stop music fadeout 1.0
    call her_main("Well, professor Slughorn invited me over to one of his...", "open", "base", "worried", "R")
    her "Rather disturbing tea parties..."
    call play_music("hermione") # HERMIONE'S THEME.
    call her_main("There were plenty of girls...", "open", "closed", "base", "mid")
    her "But none of them were in my year..."
    call her_main("Almost every guest was a freshman...", "annoyed", "squint", "base", "mid")
    call her_main("We had tea and some cake...", "open", "closed", "base", "mid")
    her "Everything was pretty harmless..."
    m "Did you flirt with the man or not?"
    her "I did..."
    call her_main("Or at least I tried to...", "annoyed", "squint", "base", "mid")
    her "Professor Slughorn seemed to be more interested in the other girls..."
    m "You almost sound jealous, [hermione_name]."
    call her_main("What?!", "angry", "wide", "base", "stare")
    call her_main("That is preposterous!", "annoyed", "narrow", "angry", "R")
    m "Here are your points..."
    her "...................."

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T2_E2:

    $ hermione.equip(her_tattoo3_lockhart) # Tattoo

    call hg_pr_flirt_teacher_intro

    call play_music("hermione") # HERMIONE'S THEME

    if not hermione.is_worn("bottom"):
        call her_main("I had an amazing day, [genie_name]!", "smile", "happyCl", "base", "mid", emote="happy")
        m "Glad to--"
        m "[hermione_name]... What have you done to your leg?"
        call her_main("What do you...{w=0.4} Oh, that...", "mad", "base", "base", "down", cheeks="blush")
        m "Yes that..."
        call her_main("It's... it's nothing.", "open", "base", "base", "mid", cheeks="blush")

        if not hermione.is_worn("stockings"):
            m "The hell it is...{w=0.4} is that writing on your leg?"
            call her_main("I... yes...", "normal", "happyCl", "worried", "mid", cheeks="blush")
            m "Gil... Gilde--"
            call her_main("*sigh*... Gilderoy Lockhart... [genie_name].", "open", "narrow", "base", "down", cheeks="blush")
            m "Now that's dirty!"
            call her_main("What!?", "clench", "base", "worried", "mid")
            m "Tagging the students... why didn't I think of that!"
            call her_main("Sir, what are you on about?", "annoyed", "squint", "base", "mid")
            m "Why else would he put his name there?"
            call her_main("Sir, he's a famous author!", "normal", "squint", "angry", "mid", cheeks="blush")
            m "Doesn't give him the right to--"
            m "Oh... It's an autograph!"
            call her_main("I... what else would it be?", "clench", "squint", "worried", "mid", cheeks="blush")
            m "Nothing..."
            m "Here are your points..."
            call her_main("Thank you, [genie_name].", "annoyed", "base", "worried", "down", cheeks="blush")
        else:
            m "I can clearly see something..."
            m "Take that off and let me have a proper look."
            her "I..."
            call her_main("Well, alright, but don't get any ideas...", "angry", "base", "angry", "mid")
            pause.5
            call her_main("Here...", "disgust", "narrow", "base", "down",cheeks="blush")

            $ hermione.strip("bottom", "stockings")
            pause.5

            m "Gil... Gilde--"
            call her_main("*sigh*... Gilderoy Lockhart... [genie_name].", "open", "narrow", "base", "down", cheeks="blush")
            call her_main("He very kindly gave me his autograph after today's lesson...", "base", "narrow", "base", "down", cheeks="blush")
            m "And why would you want such a thing?"
            call her_main("He's a very popular and esteemed author, surely you know this...", "annoyed", "base", "base", "mid", cheeks="blush")
            g9 "Of course!"
            g9 "Who would say no to having their leg signed by \"The\" {i}Spocktart{/i}?"
            g9 "Not me, that's for sure!"
            call her_main("I didn't ask him to sign my leg specifically...", "angry", "base", "worried", "mid", cheeks="blush")
            m "I see...{w=0.4} Well, can't say I'm surprised..."
            call her_main("Sir?", "annoyed", "base", "worried", "mid", cheeks="blush")
            m "An esteemed author making dirty requests from a fan is more common than you thi--"

            jump hg_pr_flirt_teacher_T2_E2.angry
    else:
        call her_main("I had an amazing day, [genie_name]!", "smile", "happyCl", "base", "mid", emote="happy")
        m "Do tell, [hermione_name]..."
        call her_main("I had a class with professor Lockhart today...", "grin", "base", "base", "R")
        call her_main("[genie_name] He is so charming and smart and...", "base", "base", "base", "mid")
        call her_main("And perfect...", "base", "narrow", "base", "up")
        m "Please spare me your schoolgirl crush, [hermione_name]."
        call her_main("He was even kind enough to give me his autograph...", "smile", "happyCl", "base", "mid", emote="happy")
        m "How kind of him indeed..."
        call her_main("Yes, I can't wait to show it to the girls!", "grin", "base", "base", "R")
        call her_main("It was a bit weird that he wouldn't sign my notebook though...", "annoyed", "base", "base", "mid")
        m "He wouldn't--"
        call her_main("It's just going to fade away in the shower now...", "upset", "base", "worried", "mid")
        m "It's going to--"
        g9 "Show me!"
        call her_main("[genie_name]?", "open", "base", "worried", "mid", cheeks="blush")
        call her_main("I... It's just an autograph...", "base", "squint", "worried", "R", cheeks="blush")
        m "Just an autograph? It's {i}Lockfart{/i} we're talking about here, I have to see it!"
        call her_main("I...", "disgust", "base", "worried", "down", cheeks="blush")

        menu:
            "\"Show me or I won't pay you!\"":
                $ her_mood += 9

                call her_main("What?!", "scream", "base", "base", "mid")
                call her_main("...............", "annoyed", "narrow", "worried", "down")
                call her_main("..................", "annoyed", "base", "worried", "R")

                call her_main("Well, alright, but don't get any ideas...", "angry", "base", "angry", "mid")
                pause.5
                call her_main("Here...", "disgust", "narrow", "base", "down",cheeks="blush")

                $ hermione.strip("bottom", "stockings")
                pause.5

                m "*Hmm*..."
                call her_main("", "angry", "narrow", "annoyed", "mid", cheeks="blush", emote="angry")
                call ctc

                m "Well then, this {i}Goldenheart{/i} surely is \"dirty\"!"

                label .angry:

                call her_main("What do you mean?!", "clench", "happy", "base", "mid", cheeks="blush")
                m "Surely a piece of paper would've been--"

                call her_main("Professor Lockhart is nothing but an embodiment of everything pure and courageous!", "annoyed", "narrow", "annoyed", "mid")
                call her_main("You should not worry about professor Lockhart, [genie_name].", "base", "base", "worried", "R")
                call her_main("He is not \"dirty\".", "annoyed", "base", "worried", "L")
                m "Whatever you say [hermione_name]..."
                call her_main("............?", "annoyed", "narrow", "annoyed", "mid", emote="angry")
                m "Anyhow..."
                call ctc

            "\"Fine... Here are your points.\"":
                call her_main("Thank you for understanding, [genie_name].", "base", "happyCl", "base", "mid")

    $ hermione.wear("all")
    call unlock_clothing(text=">New tattoo for Hermione has been unlocked!", item=her_tattoo3_lockhart)
    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T2_E3: # Filch

    call hg_pr_flirt_teacher_intro

    call play_music("hermione") # HERMIONE'S THEME.
    call her_main("Well, I spent quite some time by flirting with mister Filch today.", "soft", "base", "base", "mid",xpos="right",ypos="base")
    call her_main("What a well-read and exceptionally well-mannered gentleman mister Filch is.", "open", "closed", "base", "mid")
    m "........"
    call her_main("But I don't think anyone knows him like that...", "soft", "base", "base", "R")
    her "I don't think anyone knows mister Filch like I do."
    call her_main("I feel like he really opened up to me, [genie_name].", "base", "base", "base", "mid")
    m "Right..."
    m "This, mister Fli{size=+7}nt{/size}--"
    call her_main("It's mister Filch, [genie_name].", "open", "closed", "angry", "mid")
    m "Yeah, whatever... Is he a teacher here then?"
    her "Mister Filch? A teacher? No, [genie_name]..."
    call her_main("He is the caretaker... Shouldn't you know your school personnel, [genie_name]?", "base", "base", "base", "mid")
    m "A caretaker...?"
    m "You mean he is a janitor?"
    call her_main("Well...", "open", "base", "worried", "R")
    m "[hermione_name], I did not send you out there to charm school janitors!"
    call her_main("But mister Filch is part of the school staff, [genie_name]!", "open", "base", "base", "mid")

    menu:
        "\"Just take your points and go!\"":
            call her_main(".........................", "normal", "base", "base", "mid")

            jump end_hg_pr_flirt_teacher

        "\"Favour failed! No points for you!\"":
            call her_main("But [genie_name]?", "normal", "squint", "angry", "mid")
            m "You are dismissed, [hermione_name]."
            call her_main(".........................................", "angry", "base", "angry", "mid")

            call her_walk(action="leave")

            $ her_mood +=15

            $ hg_pr_flirt_teacher.inProgress = False

            jump end_hermione_event



### Tier 3 ###

label hg_pr_flirt_teacher_T3_E1: # Filch

    call hg_pr_flirt_teacher_intro

    #elif her_whoring >= 9:

    stop music fadeout 1.0
    call her_main(".............................", "normal", "happyCl", "worried", "mid")
    her "....................................."
    m "[hermione_name]?"
    call her_main("[genie_name], I...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "What is it? What happened?"
    call her_main("Well...", "annoyed", "base", "worried", "R")
    her "It's mister Filch, [genie_name]..."
    m "The janitor?"
    call her_main("I flirted with him a little...", "open", "base", "base", "mid")
    her "And it went great at first..."
    call her_main(".......................", "annoyed", "base", "worried", "R")
    m "................?"
    call her_main("And then...", "open", "base", "base", "mid")
    call her_main("Not sure if I should...", "annoyed", "base", "worried", "R")
    m "[hermione_name], if you are not going to speak up, you may as well leave."
    call play_music("hermione") # HERMIONE'S THEME.
    call her_main("He showed me his \"thing\", [genie_name]!", "scream", "happyCl", "worried", "mid")
    m "His what?"
    call her_main("His... manhood, [genie_name].", "angry", "happyCl", "worried", "mid", emote="sweat")
    g9 "Way to go, Janitor-guy!"
    call her_main("What?!", "scream", "wide", "base", "mid")
    m "*Khem* I mean, this is unspeakable!"
    call her_main("Yes... Vile crooked thing all covered in veins...", "angry", "base", "base", "mid", tears="soft")
    m "Spare me the grisly details, [hermione_name]."
    call her_main("Why would he do such a thing?", "mad", "happyCl", "worried", "mid", tears="soft_blink")
    her "One second we were just talking and then..."
    m "Well, your noble  sacrifice shall not go unnoticed, [hermione_name]!"
    m "{number=current_payout} points to Gryf--"
    call her_main("Professor, please wait.", "soft", "base", "base", "mid", tears="soft")
    m "*huh*?"
    call her_main("Well, aren't you going to do something about this?", "open", "base", "base", "mid")
    m "Well..."
    call her_main("What if I am not the first victim...?", "angry", "base", "angry", "mid")
    her "Some unfortunate freshman could be traumatised for life!"
    m "And who wouldn't be really?"
    call her_main("Does this mean you will take action, [genie_name]?", "open", "base", "base", "mid")
    m "*Ehm*... Yeah, sure..."
    m "There! Putting it on my {i}to-do-list{/i}..."
    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
    m "Yes, first thing tomorrow."
    call her_main("Thank you [genie_name].", "open", "closed", "base", "mid")
    call her_main("Can I have my points now?", "smile", "happyCl", "base", "mid")

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T3_E2: # Snape +CG

    call hg_pr_flirt_teacher_intro

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Professor Snape!", "angry", "base", "angry", "mid", emote="angry")
    m "*Ehm*... Yeah, I'm pretty sure it's Dumbledore or something..."
    call her_main("[genie_name], please, you need to listen to me!", "open", "base", "base", "mid")
    m "Yes, yes, [hermione_name], I'm listening."
    call her_main("I just confirmed that professor Snape is corrupted and {i}dirty{/i}, [genie_name]!", "open", "closed", "angry", "mid")
    m "Tell me what happened."
    call her_main("Well, during classes today...", "open", "base", "base", "mid")
    call her_main("I have been doing my best to attract professor Snape's attention...", "open", "base", "base", "R")
    call her_main("I have been giving him \"dreamy looks\"...", "open", "narrow", "worried", "down")
    call her_main("And I've been eyeing his crotch...", "soft", "base", "base", "R")
    m "You..."
    m "Eyed his crotch?"
    call her_main("Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly...", "open", "closed", "angry", "mid")
    m "Where do you get this stuff?"
    call her_main("Women's magazines...", "open", "base", "worried", "R")
    call her_main("Well, anyway, it worked, [genie_name].", "normal", "squint", "angry", "mid")

    hide screen hermione_main
    show screen snape_groping
    # TODO
    with fade
    call ctc

    call her_main("As soon as the class was over, professor Snape grabbed my buttocks, [genie_name]!", "angry", "base", "angry", "mid", ypos="head", flip=False)
    g9 "The fiend!"
    m "Did you enjoy it, though?"
    call her_main("[genie_name], I am only doing this--", "scream", "closed", "angry", "mid")
    m "Go Gryffindors! Honour and all that. Yes, I remember."

    call ctc

    call her_main("", "normal", "closed", "angry", "R", xpos="mid", ypos="base")

    hide screen snape_groping
    with fade

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T3_E3: # Lockhart

    call hg_pr_flirt_teacher_intro

    stop music fadeout 1.0
    call her_main("Professor Lockhart!", "annoyed", "squint", "angry", "mid")
    m "Got it! Adding him to the \"Naughty list\"!"
    call her_main("No, [genie_name], it's not that...", "open", "base", "worried", "mid")
    call her_main("Or...", "annoyed", "narrow", "angry", "R")
    her "I'm not sure..."
    call her_main("I used to adore him...", "open", "base", "worried", "mid")
    call her_main("But he...", "soft", "base", "base", "R")
    her "He just..."
    call her_main("How is this possible?", "mad", "happyCl", "worried", "mid", tears="soft_blink")
    her "I can't believe this..."
    call play_music("playful_tension") # SEX THEME.
    m "{size=-4}(*Argh*! The suspense is killing me!){/size}"
    g4 "What was it, [hermione_name]? Speak up!"
    call her_main("*huh*?", "open", "base", "base", "mid")
    m "What did Professor Lockhart do to you?"
    call her_main("*Ehm*... Nothing, [genie_name]...", "soft", "base", "base", "R")
    m "Nothing?!"
    call her_main("Yes, I sort of cornered mister Lockhart today...", "open", "base", "worried", "mid")
    call her_main("And I also may have sort of made a pass at him...", "open", "base", "base", "mid")
    m "Seriously?"
    call her_main("Yes... Not sure what had gotten into me, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
    g9 "Way to go, [hermione_name]!"
    call her_main("Hear me out first [genie_name], please!", "scream", "happyCl", "worried", "mid")
    m "My apologies. Please continue."
    call her_main("Well, I always knew that mister Lockhart was a true gentleman and...", "open", "base", "base", "mid")
    her "And... and I just wanted to clear his name from any suspicions once and for all..."
    call her_main("...............", "annoyed", "base", "worried", "R")
    her "Well mister Lockhart did not reject me..."
    m "You are killing me [hermione_name]!"
    m "He didn't reject you, he didn't do anything to you..."
    m "What the hell happened then?"
    call her_main(".............", "normal", "happyCl", "worried", "mid")
    call play_music("hermione") # HERMIONE'S THEME.
    call her_main("I made him cry, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "..............{w=0.5}wait what?"
    call her_main("He gave me a bewildered look and then started to sob...", "angry", "base", "worried", "mid")
    her "He looked like he was genuinely afraid of me, [genie_name]."
    call her_main("I think...", "annoyed", "base", "worried", "R")
    her "I think mister Lockhart might be afraid of women..."
    m "Afraid of women?"
    m "What is that supposed to mean?"
    call her_main("That he is into boys, [genie_name]?", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Oh... To each their own I guess."
    call her_main("............", "upset", "wink", "base", "mid")
    m "..........."
    m "Well, I bet it was a traumatising experience for you, [hermione_name]."
    call her_main("It was, [genie_name]...", "open", "base", "base", "mid")
    m "Well, I hope these points will make you feel better."

    jump end_hg_pr_flirt_teacher
