

### Tier 2 ###

label hg_pf_grope_ass_T2:
    stop music fadeout 5.0
    call her_chibi_scene("grope_ass_front", trans=d7)

    call her_main("[genie_name]!?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
    m "Relax, [hermione_name]. It will be the easiest {number=current_payout} points you've ever made, I promise."
    m "All I am going to do is squeeze your little butt a couple of times..."
    call her_main("No! I demand you to stop!", "scream", "closed", "angry", "mid", cheeks="blush")

    call her_chibi_scene("behind_desk_front", trans=d5)

    call her_main("This is inappropriate, [genie_name]................", "angry", "closed", "angry", "mid", cheeks="blush")
    m "Nobody needs to know how exactly you got the points..."
    call her_main("But...", "annoyed", "base", "angry", "mid")
    m "Do it for {i}gravenboor{/i}..."
    call her_main("(These {number=current_payout} points could really make a difference...)", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("(Darn it.....!)", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("(...............................)", "annoyed", "narrow", "angry", "R", cheeks="blush")

    call her_main("Can I at least turn around then, Sir?", "soft", "base", "angry", "mid", cheeks="blush")

    menu:
        m "*Hmm*..."

        "\"Yes. Turn around, [hermione_name].\"": # Can fail
            jump hg_pf_grope_ass_T2_back

        "\"No. Just stand still, [hermione_name].\"": # Fails
            jump hg_pf_grope_ass_T2_front

label hg_pf_grope_ass_T2_front:
    call her_chibi_scene("behind_desk_front", trans=d7)

    call her_main("(...)", "disgust", "narrow", "worried", "down", cheeks="blush", ypos="head")

    call her_chibi_scene("grope_ass_front", trans=d5)
    call ctc

    call her_main("(...)", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("I'm sorry, Sir. But I can't do this!", "soft", "narrow", "base", "down", cheeks="blush")
    m "What is the problem, [hermione_name]?"

    call her_chibi_scene("reset", "desk", "base", trans=fade)

    call her_main("I can't do it when I can see you looking at me...", "mad", "happyCl", "worried", "mid", cheeks="blush")
    m "That's the whole point [hermione_name], I want to look at you..."
    call her_main(".............", "annoyed", "base", "worried", "mid", cheeks="blush")
    call her_main("It's demeaning!", "angry", "closed", "angry", "mid", cheeks="blush")
    m "Wouldn't it be worse if I didn't want to look at you?"
    call her_main("*ARGH* Whatever!!!", "scream", "base", "angry", "mid", cheeks="blush")

    call her_main("Good day, Sir.", "disgust", "narrow", "angry", "R", cheeks="blush")

    call her_walk(action="leave")

    $ her_mood += 4

    jump end_hermione_event

label hg_pf_grope_ass_T2_back:
    call her_chibi_scene("behind_desk_front", trans=d7)

    call her_main("As you say, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush")

    call her_chibi_scene("behind_desk_back", trans=d5)
    call ctc

    call her_main(".............", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("...........................", "annoyed", "base", "angry", "mid", cheeks="blush")
    call her_main("[genie_name], I would like to be done with this sooner rather than later...", "soft", "closed", "angry", "mid", cheeks="blush")
    m "Don't rush me [hermione_name]... Let me savour the moment..."
    call her_main(".............................", "annoyed", "narrow", "angry", "R", cheeks="blush")

    menu:
        m "*Hmm*..."
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T2_continue

        "-Give her butt a slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("!!!!!!!!!!!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("[genie_name]!!?", "scream", "wide", "base", "stare", cheeks="blush")

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main(".......................", "annoyed", "narrow", "angry", "R", cheeks="blush")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("!!!!!!!!!!!!!", "scream", "wide", "base", "stare", cheeks="blush")
    call her_main("[genie_name], what are you doing!?", "angry", "closed", "angry", "mid", cheeks="blush")
    call her_main("You said all you were going to do is touch!", "angry", "base", "angry", "mid", cheeks="blush")

    menu:
        "\"Alright, alright... stop making a scene....\"":
            call her_main(".......................", "annoyed", "narrow", "angry", "R", cheeks="blush")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("Ouch! It hurts!", "angry", "closed", "angry", "mid", cheeks="blush")
    call her_main("This is so demeaning!", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("You said all you were going to do is touch...", "angry", "base", "angry", "mid", cheeks="blush")
    g4 "Just stand still, [hermione_name]!"
    call her_main("I don't think so, [genie_name]!", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("No amount of points are worth this humiliation!", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")
    call her_main("You are abusing your power, [genie_name]!", "scream", "base", "angry", "mid", cheeks="blush",emote="angry")
    g4 "What?"
    call her_main("I'm leaving!", "angry", "happyCl", "worried", "mid", cheeks="blush", ypos="head")

    call her_chibi_scene("reset", "desk", "base", trans=fade)

    # Event Fails
    menu:
        g4 "*Tsk*..."
        "\"I... I apologise...\"":
            m "...... It's not my fault......"
            call her_main("An apology won't be enough, [genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")
            m "What else do you want? More points?"
            call her_main("Yes, I believe I'm owed at least that much!", "angry", "base", "angry", "mid", cheeks="blush")
            m "{number=current_payout} is what we agreed on. You won't get any more than that."
            call her_main("*tzzh*... Fine!", "clench", "closed", "angry", "mid", cheeks="blush")
            call her_main("Keep your points.", "angry", "base", "angry", "mid", cheeks="blush")
            call her_main("All of them! I don't even want them anymore.", "scream", "closed", "angry", "mid", cheeks="blush")
            m "Are you sure about that?"
            call her_main("I'm leaving. Good day, Sir.", "angry", "base", "angry", "mid", cheeks="blush")

            call her_walk(action="leave")

            call bld
            m "(Whatever...)"

            $ her_mood += 15

            jump end_hermione_event

        "\"You are not getting any points for this!\"":
            call her_main("Ha! See if I care, [genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")

            call her_walk(action="leave")

            call bld
            g4 "*Tsk!* (You brat!)"

            $ her_mood += 20

            jump end_hermione_event

        "\"I'm subtracting points from you then!\"":
            call her_main("You can't be serious!?", "scream", "wide", "base", "stare", cheeks="blush")
            g4 "The Gryffindor house, minus ten points!"
            g4 "There! It's done!"
            call her_main("*Grr*...........", "angry", "base", "angry", "mid", cheeks="blush")
            call her_main("........................", "angry", "base", "angry", "mid", cheeks="blush")
            call her_main("This is not fair...", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
            m "What? Hey, wait, don't you start crying on me..."
            call her_main("I hate you, [genie_name]! I hate you!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")

            # Hermione runs out of the room.
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            call bld
            m ".............."

            menu:
                "\"Dammit. Now I feel like crap...\"":
                    g9 "But who could resist slapping that little behind of hers?"
                "\"She made me do this!\"":
                    m "Acting all wounded now..."
                    g9 "I bet she actually enjoyed the slapping and just won't admit it..."

            $ gryffindor -=10
            $ her_mood += 30

            jump end_hermione_event

label hg_pf_grope_ass_T2_continue:
    call her_chibi_scene("grope_ass_back")
    with d7
    call ctc

    call her_main("..............", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call nar("*squeeze* *squeeze* *squeeze*...")

    call her_main(".........................", "annoyed", "base", "angry", "mid", cheeks="blush")
    call her_main("(I can't believe this is really happening...)", "disgust", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("If you don't mind, Sir...", "soft", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("I'd like you to unhand me now...", "disgust", "base", "worried", "mid", cheeks="blush")
    m "What? Already?"
    call her_main("Yes! This has been demeaning enough!", "annoyed", "base", "angry", "mid", cheeks="blush")
    call her_main("Please let go of me, Sir.", "soft", "base", "angry", "mid", cheeks="blush")
    m "Fine..."
    call nar(">You give her butt one last squeeze...")
    call her_main("...................", "annoyed", "narrow", "angry", "R", cheeks="blush")

    jump end_hg_pf_grope

### Tier 3 ###

label hg_pf_grope_ass_T3:
    call her_chibi_scene("behind_desk_front", trans=d7)

    call her_main("Do you want me to turn around then, [genie_name]?", "base", "base", "base", "R", cheeks="blush", ypos="head")

    call play_music("playful_tension") # SEX THEME.

    menu:
        m "*Hmm*..."
        "\"Yes. Turn around, [hermione_name].\"":
            call her_main("As you say, [genie_name]...", "base", "base", "base", "R", cheeks="blush")

            jump hg_pf_grope_ass_T3_back

        "\"No. Just stand still, [hermione_name].\"":
            call her_main("As you say, [genie_name]...", "annoyed", "narrow", "angry", "R", cheeks="blush", ypos="head")

            jump hg_pf_grope_ass_T3_front

label hg_pf_grope_ass_T3_front:
    call her_chibi_scene("behind_desk_front")
    with d7
    call ctc

    call her_main("[genie_name], please hurry up, before someone discovers us like this...", "soft", "base", "base", "R", cheeks="blush", ypos="head")
    m "What's the problem, [hermione_name]?"
    m "You know you are doing this for your house."
    call her_main("I do know.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("But not everyone would see it that way...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("So let us be done with this as quick as possible...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Please...", "open", "base", "base", "R", cheeks="blush")
    m "Well, if you insist..."

    call her_chibi_scene("grope_ass_front")
    with d7

    call her_main("!!!", "mad", "wide", "base", "stare", cheeks="blush")
    m "What is it?"
    call her_main("N-nothing, [genie_name]. Your hands are cold, that's all...", "open", "base", "base", "R", cheeks="blush")

    call nar(">You run your hands up and down Hermione's legs...")
    call her_main(".........................", "annoyed", "narrow", "angry", "R", cheeks="blush")

    call nar(">And give her Ass a good squeeze...")
    call her_main(".................", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Don't look away, girl. I want you to look into my eyes."
    call her_main("I would rather not, [genie_name]...", "angry", "happyCl", "worried", "mid", cheeks="blush")

    menu:
        m "..."
        "\"Fine. Just keep on standing still then.\"":
            call her_main("Thank you, [genie_name]...", "angry", "happyCl", "worried", "mid", cheeks="blush", ypos="head")

            call nar(">You massage her ass-cheeks lightly...")
            call her_main("....................", "angry", "happyCl", "worried", "mid", cheeks="blush")

            call nar(">And keep enjoying the sensation of her butt under your hands...")
            call her_main(".....................", "angry", "happyCl", "worried", "mid", cheeks="blush")

            call nar(">Then You give Hermione's butt one last squeeze.")
            call her_main(".....................", "angry", "happyCl", "worried", "mid", cheeks="blush")

            jump end_hg_pf_grope

        "\"Open your eyes, or you'll lose the points!\"":
            $ her_mood += 10

            call her_main("*Tsk*! {size=-5}(You wretched old--{/size}", "angry", "happyCl", "worried", "mid", cheeks="blush", ypos="head")
            m "Did you say something, [hermione_name]?"
            call her_main("It's nothing, [genie_name].", "angry", "base", "angry", "mid")

            call nar(">You massage her ass-cheeks lightly...","start")
            call nar(">Hermione maintains eye contact as she's been told...","end")

            call her_main("....................", "angry", "base", "angry", "mid")
            call her_main("...............................", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "What did I tell you about looking away?"
            call her_main("Yes, I remember...", "angry", "happyCl", "worried", "mid", cheeks="blush")
            call her_main(".................................", "angry", "base", "angry", "mid")
            call her_main("...................................", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call her_main("..................................................", "annoyed", "narrow", "angry", "R", cheeks="blush")

            call nar(">You keep enjoying the sensation of her soft buttocks under your fingertips...")
            call her_main(".....................", "angry", "base", "angry", "mid")

            call nar(">Then You give Hermione's butt one last squeeze.")
            call her_main(".....................", "annoyed", "base", "angry", "mid", cheeks="blush")

            jump end_hg_pf_grope

label hg_pf_grope_ass_T3_back:
    call her_chibi_scene("behind_desk_back", trans=d7)
    call ctc

    call her_main(".............", "base", "narrow", "base", "up", cheeks="blush")

    menu:
        m "*Hmm*..."
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T3_continue

        "-Give her butt a slap-":
            call slap_her
            call her_main("!!!!!!!!!!!!!", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("[genie_name]....?", "base", "base", "base", "R", cheeks="blush")

            pass

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main("It's okay...", "base", "base", "base", "R", cheeks="blush")

            jump hg_pf_grope_ass_T3_continue

        "-Give her butt another slap-":
            call slap_her
            call her_main("!!!!!!!!!!!!!", "scream", "wide", "base", "stare", cheeks="blush")
            call her_main("[genie_name], what are you doing!?", "base", "base", "base", "R", cheeks="blush")
            call her_main("You said all you are going to do is touch!", "base", "base", "base", "R", cheeks="blush")

            pass

    menu:
        "\"Alright, alright...\"":
            call her_main("It's not a big deal...", "base", "base", "base", "R", cheeks="blush")

            jump hg_pf_grope_ass_T3_continue

        "-Give her butt yet another slap-":
            call slap_her

            call her_main("[genie_name], not so loud, please...", "silly", "narrow", "base", "up", cheeks="blush")
            call her_main("What if somebody hears us?", "silly", "narrow", "base", "up", cheeks="blush")
            m "Alright, alright... proceeding with groping then..."
            call her_main("................", "base", "base", "base", "R", cheeks="blush")

            jump hg_pf_grope_ass_T3_continue

label hg_pf_grope_ass_T3_continue:
    call her_chibi_scene("grope_ass_back")
    with d7
    call ctc

    call her_main("...................", "base", "base", "base", "R", cheeks="blush", ypos="head")
    m "You are being awfully quiet today, [hermione_name]."
    call her_main("Am I...?", "base", "base", "base", "R", cheeks="blush")

    if her_tier <= 5:
        call her_main("Well, you know me, [genie_name]...", "base", "narrow", "base", "up", cheeks="blush")
        call her_main("I'm just happy to be able to do my part for the Gryffindor house...", "base", "narrow", "base", "up", cheeks="blush")
    else:
        call her_main("Please don't mind it and continue...", "base", "narrow", "base", "up", cheeks="blush")
        call her_main("(... to grope me...)", "base", "narrow", "base", "mid_soft", cheeks="blush")

    call nar(">You keep on playing with Hermione's ass...","start")
    call nar(">And continue sliding your hands up and down her inner thighs...","end")

    call her_main("................", "base", "base", "base", "R", cheeks="blush")

    call her_main("!!!!!!?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
    m "What is it, [hermione_name]?"
    call her_main("It's nothing [genie_name]...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("It's just... ", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("This is so... inappropriate...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Relax, [hermione_name]. It's not like you are enjoying this..."
    call her_main("What? Of course not! This is depraved...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("I am making this sacrifice for the honour of my house...", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Yes, concentrate on that..."
    call her_main("....................", "angry", "base", "angry", "mid", cheeks="blush")
    call ctc

    call her_main("But, [genie_name]...", "open", "base", "base", "R", cheeks="blush")
    call her_main("Why are {size=+7}you{/size} doing this?", "open", "base", "base", "R", cheeks="blush")

    menu:
        m "*Hmm*..."
        "\"I have my reasons...\"":
            call her_main("Oh...", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("*Hmm*...", "annoyed", "narrow", "angry", "R", cheeks="blush")

        "\"In the name of science of course!\"":
            call her_main("Really?!", "soft", "wide", "base", "stare")
            call her_main("Is this research of some kind?", "soft", "wide", "base", "stare")
            m "Yeah, sure, I'm researching... *Err*..."
            m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
            call her_main("I see...", "soft", "wide", "base", "stare")
            call her_main("Well, if it is for research then I am glad to be of help...", "annoyed", "narrow", "angry", "R")

        "-Just squeeze her butt cheeks tighter-":
            call nar(">You give Hermione's butt cheeks a couple of extra firm squeezes.")
            call her_main("....................", "open", "base", "base", "R", cheeks="blush")
            call her_main("(Shall I just be quiet, then.....?)", "disgust", "narrow", "base", "down", cheeks="blush")

    call nar(">You keep on playing with Hermione's buttocks...","start")
    call nar(">You slide your hands up and down her inner thighs...","end")
    call her_main("................", "angry", "happyCl", "worried", "mid", cheeks="blush")

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            call nar(">You slowly slide one of your hands under the fabric of the girl's panties...")
            call her_main("[genie_name]... What are you...?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
            m "That's alright, just think about those {number=current_payout} points your house is about to receive..."
            call her_main(".............", "disgust", "narrow", "base", "down", cheeks="blush")

            pass

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            call nar(">You slowly slide one of your hands across her pussy..")
            call her_main("[genie_name]... What are you...?", "mad", "wide", "base", "stare", cheeks="blush", ypos="head")
            m "That's alright, just think about those {number=current_payout} points your house is about to receive..."
            call her_main(".............", "disgust", "narrow", "base", "down", cheeks="blush")

            pass

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    menu:
        "-Prod her pussy with one of your fingers-":
            call nar(">You slide one of your fingers down and place it against the girls slit...")
            call her_main("[genie_name]? No! What are you...?", "mad", "wide", "base", "stare", cheeks="blush")
            call nar(">Hermione tries to pull away from you...")
            $ her_mood += 3

            menu:
                "-Force your finger into her pussy!-":
                    ">You force one of your fingers into her pussy..."
                    ">It's very tight and warm..."
                    ">Also it is relatively dry... Doesn't look like Hermione's taking much pleasure in this..."

                    jump hg_pf_grope_ass_T3_fail

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butthole instead-":
            call nar(">You place your one of your thumbs against the girls butthole...")
            call her_main("[genie_name]? No! What are you doing!?", "mad", "wide", "base", "stare", cheeks="blush")
            call nar(">Hermione tries to pull away from you...")
            $ her_mood += 3

            menu:
                "-Force your thumb into her butthole-":
                    call nar(">You force one of your thumbs into her little butthole...")
                    with hpunch
                    call her_main("!!?", "angry", "wide", "base", "stare")
                    call nar(">It's very tight and warm inside...")

                    jump hg_pf_grope_ass_T3_fail

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope

label hg_pf_grope_ass_T3_fail:
    call her_main("NO! What have you done!!?", "angry", "happyCl", "worried", "mid", cheeks="blush", tears="soft_blink", ypos="head")
    call nar(">Hermione gives you an unexpectedly strong shove...")

    call her_chibi_scene("behind_desk_front", trans=hpunch)

    call her_main("Why would you do this to me, [genie_name]...?", "angry", "happyCl", "worried", "mid", cheeks="blush", tears="soft_blink")
    call her_main("I never agreed to... to...", "angry", "happyCl", "worried", "mid", cheeks="blush", tears="crying_blink")
    call her_main("You... you...", "angry", "happyCl", "worried", "mid", cheeks="blush", tears="crying_blink")
    call her_main("{size=+7}YOU RAPED ME!{/size}", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy", trans=hpunch)
    g4 "What? Don't be ridiculous, [hermione_name]! I did no such thing!"
    call her_main("Yes you did. {size=+4}Yes you did!{/size}", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
    g4 "I most certainly did not!"
    call her_main("No, you {size=+4}did{/size}, [genie_name]!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
    call her_main("Now, you will give me twenty--", "angry", "base", "angry", "mid", cheeks="blush", tears="soft")
    call her_main("No, a hundred house points or I am reporting you to the Ministry of magic!", "angry", "base", "angry", "mid", cheeks="blush", tears="soft")

    menu:
        m "(Ah, crap...)"
        "\"Alright, alright... One hundred points it is...\"":
            $ gryffindor += 100
            $ her_mood += 9

            m "One hundred points to Gryffindor !"
            m "There, it is done..."
            m "Now would you calm yourself down, [hermione_name]?"
            call her_main("No, I will not!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy", ypos="head")
            call her_main("I've just been raped!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
            g4 "Oh, snap out of it [hermione_name], I didn't rape you! All I did was--"
            call her_main("{size=+7}You raped me!!!{/size}", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy" , trans=hpunch)
            g4 "By the great desert sands, would you keep it down about the rapes?!"
            g4 "Someone may hear you!"
            call her_main("Good! I want them to hear!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")
            m "Why would you want that? I already paid you!"
            call her_main("Oh... right...", "angry", "base", "base", "mid", cheeks="blush", tears="mascara")
            call her_main("But I hate you! I hate you [genie_name]!", "scream", "closed", "angry", "mid", cheeks="blush", tears="mascara")

        "\"You're bluffing, [hermione_name]!\"":
            $ her_mood += 27

            call her_main("No, I'm not! I'm gonna do it!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy", ypos="head")
            g4 "By all means, go ahead..."
            g4 "There was no rape!"
            call her_main("I hate you, [genie_name]!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="messy")

    call her_chibi_scene("reset","desk","base", trans=fade)

    call her_walk("door", "base")

    call her_main("...........................", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")

    call her_chibi("leave")

    jump end_hermione_event

### Tier 4 ###

label hg_pf_grope_ass_T4:
    call her_chibi_scene("behind_desk_front", trans=d7)

    call her_main("Do you want me to turn around then, [genie_name]?", "base", "base", "base", "R", cheeks="blush", ypos="head")

    call play_music("playful_tension")

    menu:
        m "*Hmm*..."
        "\"Yes. Turn around, [hermione_name].\"":
            call her_main("As you say, [genie_name]...", "base", "base", "base", "R", cheeks="blush")
            jump hg_pf_grope_ass_T4_back

        "\"No. Just stand still, [hermione_name].\"":
            call her_main("As you say, [genie_name]...", "soft", "base", "base", "mid", cheeks="blush", ypos="head")
            jump hg_pf_grope_ass_T4_front

label hg_pf_grope_ass_T4_front:
    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    call her_main("...................", "base", "base", "base", "R", cheeks="blush", ypos="head")
    m "You seem more relaxed this time."
    call her_main("...................", "base", "narrow", "worried", "down", cheeks="blush")
    m "Could it be that you're enjoying this?"
    call her_main("I...", "soft", "narrow", "worried", "down", cheeks="blush")
    call her_main("I'm doing this to earn points for my house, it has nothing to do with personal enjoyment...", "soft", "narrow", "worried", "down", cheeks="blush") #looks down
    m "Is that so?"
    m "Then why aren't you looking into my eyes when you say that..."
    call her_main("I...", "disgust", "base", "base", "mid", cheeks="blush") # looks back up

    call her_chibi_scene("grope_ass_front", trans=d7)
    pause.8

    call her_main("!!!", "mad", "wide", "base", "stare", cheeks="blush")
    g9 "..."
    call her_main("........", "annoyed", "base", "angry", "mid", cheeks="blush")

    call nar(">You run your hands up and down Hermione's legs...")
    call her_main(".........................", "upset", "happyCl", "worried", "mid", cheeks="blush")

    call nar(">And give her Ass a good squeeze...")
    call her_main(".................", "soft", "base", "base", "mid", cheeks="blush")
    m "You're looking at me this time..."
    call her_main("Isn't that what you wanted, [genie_name]...", "open", "base", "worried", "mid", cheeks="blush")

    call nar(">You give her butt another firm squeeze as you gently move to massage her inner leg...")
    call her_main("I'll take that as a yes...", "base", "narrow", "annoyed", "up", cheeks="blush")

    if hermione.is_worn("panties"):
        call nar(">You continue to massage her inner thigh and occasionally gently brush against her panties...")
    else:
        call nar(">You continue to massage her inner thigh and occasionally gently brush against her pussy...")
    call her_main("Ah...", "soft", "narrow", "annoyed", "up", cheeks="blush")
    call her_main("...", "clench", "narrow", "annoyed", "up", cheeks="blush")
    g9 "..."

    call nar(">Maintaining eye contact, you move your hand down. A split second of disappointment is seen on Hermione's face...")
    m "Enjoying yourself?"
    call her_main("W-What...", "disgust", "narrow", "worried", "down", cheeks="blush")
    m "The massage... You seem less tense than last time."
    call her_main("Oh... I suppose it is quite nice...", "clench", "base", "base", "R", cheeks="blush")

    call nar(">You continue rubbing her inner thighs, Hermione's chest moving up and down faster and faster...")
    call her_main(".......", "clench", "narrow", "base", "down", cheeks="blush")
    m "Enjoying a bit too much perhaps?"
    call her_main("...", "base", "narrow", "base", "mid_soft", cheeks="blush")
    call her_main("What do you--", "soft", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    call nar(">You bring your hands out from between Hermione's legs and hold them up in front of her...")
    m "What would you call this then, [hermione_name]?"

    call nar(">Hermione embarrassingly looks at you, as you present her with a sticky substance gleaming across your upper hand...")
    call her_main("Oh...", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("Well, your hands were moving so close and--", "soft", "narrow", "worried", "down", cheeks="blush")

    call her_chibi_scene("grope_ass_front", trans=d7)
    pause.8

    call nar(">Before she can finish her sentence you put your hand back in place...")
    call her_main("...", "clench", "wide", "base", "stare", cheeks="blush")

    call nar(">You slowly brush your fingertips across her legs and move your hands to rest on her firm cheeks...")
    call her_main("...", "soft", "narrow", "annoyed", "up", cheeks="blush")

    call nar(">Hermione begins to relax once more as you softly massage them with your hands...")
    call her_main("...", "base", "narrow", "base", "down", cheeks="blush")
    m "I thought I asked you to look at me."
    call her_main("Oh, sorry...", "base", "narrow", "base", "mid_soft", cheeks="blush")

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_front", trans=d7)

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_front", trans=d7)

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T4_continue

label hg_pf_grope_ass_T4_back:
    call her_chibi_scene("behind_desk_back", trans=d7)
    pause.8

    call her_main("...", "base", "narrow", "annoyed", "up", cheeks="blush", ypos="head")
    m "How does it feel?"
    call her_main("How does what feel?", "open", "narrow", "base", "mid_soft")
    m "How does it feel to be presenting your butt to your headmaster?"
    call her_main("I don't know how to answer that, [genie_name]...", "clench", "narrow", "base", "down", cheeks="blush")
    call her_main("Do I have to give you a response?", "open", "base", "base", "mid", cheeks="blush")
    m "Well, you don't have to..."
    call her_main("It feels weird...{w} but...", "disgust", "narrow", "worried", "down", cheeks="blush")
    g9 "Butt?" #fucks sake

    call her_chibi_scene("grope_ass_back", trans=d7)
    pause.8

    call her_main("!!!", "mad", "wide", "base", "stare", cheeks="blush")
    call her_main("[genie_name]!", "clench", "base", "angry", "mid", cheeks="blush")
    m "Sorry..."
    call her_main("...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("You should've warned me...", "soft", "narrow", "angry", "R", cheeks="blush")

    call nar(">Hermione goes quiet as you begin massaging her butt cheeks...")
    call her_main("...", "base", "closed", "base", "mid", cheeks="blush")

    call nar(">You take your thumbs and move them gently from side to side as her soft butt cheeks open and close with every move...")
    m "Does this feel better?"
    call her_main("It...", "clench", "narrow", "worried", "down", cheeks="blush")
    call her_main("It feels fine...", "soft", "narrow", "worried", "down", cheeks="blush")
    m "I meant not having to look at me..."
    call her_main("Oh...{w} it doesn't matter to me how you want it...", "soft", "base", "base", "R", cheeks="blush")
    m "Is that so?"
    call her_main("Of cours--", "soft", "closed", "base", "mid", cheeks="blush")
    call her_main("!!!", "clench", "wide", "base", "stare", cheeks="blush")
    call nar(">As your hands spread out, you suddenly tighten them firmly around Hermione's Butt cheeks...")
    g9 "..."

    call nar(">Lessening your grip on her cheeks slightly, you then move down towards her inner thighs, and gently begin massaging her with your thumbs...")
    call her_main("...", "soft", "narrow", "annoyed", "up", cheeks="blush")

    if hermione.is_worn("panties"):
        call nar(">Moving your hands gently up and down, Hermione begins to relax as they occasionally brush against her panties...")
    else:
        call nar(">Moving your hands gently up and down, Hermione begins to relax as they occasionally brush against her pussy...")
    call her_main("Ah...", "open", "narrow", "annoyed", "up", cheeks="blush")
    call her_main("...", "base", "narrow", "annoyed", "up", cheeks="blush")
    g9 "..."

    call nar(">You continue in silence and notice Hermione's chest has begun moving up and down faster than before...")

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_back", trans=d7)

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_back", trans=d7)

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T4_continue

label hg_pf_grope_ass_T4_continue:

    if hermione.is_worn("panties"):
        call nar(">You slowly slide one of your hands under the fabric of the girl's panties...")
    else:
        call nar(">You slowly slide one of your hands across her pussy..")
    call her_main("[genie_name]... What are you...?", "open", "base", "base", "R", cheeks="blush", ypos="head")

    if her_tier <= 5:
        m "It's alright, just think about those {number=current_payout} points your house is about to receive..."
    else:
        m "It's alright, just try to relax and enjoy yourself"

    call her_main("As you say...", "open", "base", "base", "R", cheeks="blush")

    menu:
        "-Prod her pussy with one of your fingers-":
            ">You slide one of your fingers down and place it against the girl's little slit..."
            call her_main("[genie_name]?", "base", "base", "base", "R", cheeks="blush")

            menu:
                "-Force your finger into her pussy!-":
                    ">You force one of your fingers into her little pussy..."
                    ">It's very tight and warm..."
                    ">it is quite wet as well... Seems like Hermione's taking pleasure in this..."

                    call her_main("Ah...", "silly", "narrow", "base", "mid_soft", cheeks="blush")
                    call her_main("It's inside of me...", "disgust", "narrow", "worried", "down", cheeks="blush")
                    call her_main("No, [genie_name], you must stop now...", "disgust", "base", "base", "mid_soft", cheeks="blush")
                    m "Why? You don't like it?"
                    call her_main("It doesn't matter whether I like this or not, [genie_name].", "soft", "narrow", "base", "mid_soft", cheeks="blush")
                    call nar(">You take your fingers out and move them across her slit...")
                    call her_main("You know why I'm doing this...", "clench", "narrow", "worried", "down", cheeks="blush")
                    call her_main("....", "disgust", "narrow", "worried", "down", cheeks="blush")
                    call her_main("And it's wrong for me to let you do this to me for a meagre {number=current_payout} points...", "base", "narrow", "base", "mid_soft", cheeks="blush")
                    m "Heh... I see..."

                    menu:
                        "-Continue rubbing her-":
                            call nar(">As you continue rubbing her, Hermione closes her eyes and goes silent...")
                            call her_main("......", "clench", "happyCl", "worried", "mid", cheeks="blush")
                            call her_main("Ah...", "silly", "happyCl", "worried", "mid", cheeks="blush")
                            call nar(">With no more objections you move your index finger across her clit and begin rubbing it gently...")
                            call her_main("...", "soft", "closed", "base", "mid", cheeks="blush")
                            call nar(">Completely lost in the moment, Hermione moves around as you massage her.")
                            call nar(">In response to her movement you start rubbing her faster, and as you do so, she squeals and lets out a gentle moan.")
                            call her_main("*Hnnngh*", "clench", "happyCl", "worried", "mid", cheeks="blush") #still has eyes closed
                            call her_main("....", "disgust", "wide", "base", "stare", cheeks="blush") #Opens her eyes wide
                            m "Did you just?"
                            if her_tier <= 4:
                                call her_main("No...", "angry", "happyCl", "worried", "mid", cheeks="blush")
                                m "Well it sure looks like you just--"
                                call her_main("I think we're done here!", "soft", "happyCl", "worried", "mid", cheeks="blush", emote="angry")
                                m "I see..."
                                m "Well, in that case..."
                            else:
                                call her_main("Yes...", "angry", "narrow", "annoyed", "up", cheeks="blush")
                                call her_main("That felt really good!", "soft", "narrow", "base", "mid_soft", cheeks="blush")
                                g9 "Any time, [hermione_name]!"
                                call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft", cheeks="blush")

                            jump end_hg_pf_grope

                        "-Let the girl go...-":
                            jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butthole instead-":
            ">You place your one of your thumbs against the girl's little butthole..."
            call her_main("[genie_name]? What are you doing?", "base", "base", "base", "R", cheeks="blush")

            menu:
                "-Force your thumb into her butthole-":
                    ">You force one of your thumbs into her little butthole..."
                    with hpunch
                    call her_main("ah... your finger is up my...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
                    ">It's very tight and warm inside..."
                    call her_main("Ah...", "silly", "narrow", "base", "mid_soft", cheeks="blush")
                    call her_main("It's inside of me...")
                    call her_main("No, [genie_name], you must stop now...", "base", "narrow", "base", "mid_soft", cheeks="blush")
                    m "Why? You don't like it?"
                    call her_main("It doesn't matter whether I like this or not, [genie_name].")
                    call her_main("You know why I'm doing this...")
                    call her_main("And it is wrong for me to let you do this to me for a meagre {number=current_payout} points...")
                    ">Hermione pulls away from you..."
                    m "Heh... I see..."
                    m "Well, in that case..."

                    jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope
