
label hg_ps_get_panties:
    # Public shaming: Panty thief
    hide screen hermione_main
    with d3
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"

    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump hermione_favor_menu

    m "[hermione_name]?"
    call her_main("I am listening, [genie_name].",xpos="right",ypos="base")
    m "I will need your panties..."

    if not hg_pf_admire_panties.is_event_complete(3, 1) or her_whoring < 6:
        jump too_much

    elif hg_ps_get_panties.points == 0:
        stop music fadeout 10.0

        call her_main("W-what?", "open", "base", "worried", "mid")
        her "My... panties...?"
        her "[genie_name], this is--"
        m "This is the favour I will be buying from you today, [hermione_name]..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my..."

        call play_music("chipper_doodle")

        call her_main("... panties, [genie_name]?", "angry", "base", "angry", "mid")
        m "Yes I do..."
        call her_main("May I ask what you are planning to do with them...?", "disgust", "narrow", "base", "mid_soft")
        m "*Ehm*... I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from Slytherin..."
        m "Are selling favours for house points, [hermione_name]?"
        call her_main("Yes I do!", "angry", "base", "angry", "mid")
        call her_main("(Those Slytherin tramps have no dignity.)", "annoyed", "narrow", "angry", "R")
        m "Well, there you go then!"
        call her_main("*huh*?", "disgust", "narrow", "base", "mid_soft")
        m "Beat them at their own game!"
        call her_main("What?", "open", "base", "base", "mid")
        m "Yes! Don't just put the Gryffindor house back on top..."
        m "But do it by beating them at their own game!"
        call her_main("[genie_name]...", "open", "base", "worried", "mid")
        m "As headmaster, I cannot play favourites. But you know how I feel about Gryffindor..."
        m "I wish I could give you the points but that would ruin the system..."
        hide screen hermione_main
        with d3

        if hermione.is_worn("panties"):
            $ hermione.strip("robe", "accessory")
            $ hermione.strip("panties")
            call nar(">Suddenly Hermione bends forward and takes off her panties.","start")
        else:
            if hermione.is_any_worn("robe", "top", "bottom"):
                call nar(">Suddenly Hermione reaches inside one of her hidden pockets.","start")
            else:
                call nar(">Suddenly Hermione reaches inside--","start")
                call nar(">Wait, she's not exactly clothed...{w=0.4} Well then...")
                call nar(">By some kind of magic, a pair of panties suddenly appears in her hand.")

        call nar(">She extends her arm to you, clutching a little piece of fabric in her fist.","end")
        m "??!"
        call her_main("Just take them, [genie_name]...", "mad", "base", "worried", "mid", tears="soft")
        call nar(">Slightly surprised, you take the panties from her hand.")
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, [genie_name]! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        call her_main("...........", "normal", "base", "base", "R",tears="soft")
        call her_main("I hope nobody will notice that I have no underwear on today...", "annoyed", "base", "worried", "R")
        call her_main("Oh, and I will be back tonight to pick them up, [genie_name].", "open", "base", "base", "mid")
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        call her_main(".............", "angry", "happyCl", "worried", "mid",emote="sweat")

    else:
        label dev:
        if hg_ps_get_panties.points > 0:
            her "Again, [genie_name]?"
            m "Yes, again..."

        her "Here..."

        if her_whoring >= 12:
            hide screen hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                call nar(">Suddenly Hermione bends forward and takes off her panties.", "start")
            else:
                if hermione.is_any_worn("top", "bottom"):
                    call nar(">Hermione pulls her panties out of her pocket.", "start")
                else:
                    call nar(">Suddenly Hermione reaches inside--","start")
                    call nar(">Wait, she's not exactly clothed...{w=0.4} Well then...")
                    call nar(">By some kind of magic, a pair of panties suddenly appears in her hand.")

            call nar(">She casually throws them on your desk.", "end")

            m "What?"
            call her_main("Yes, I had a feeling that you might ask for these today, [genie_name].", "base", "base", "base", "mid")
            m "A feeling?"
            call her_main("Well, to be completely honest I just do not bother to wear them much anymore...", "grin", "base", "base", "R")

            if hermione.is_equipped("panties"):
                her "Unless I'm asked to, that is..."

        else:
            hide screen hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                call nar(">Hermione takes off her panties without hesitation.", "start")
            else:
                if hermione.is_any_worn("top", "bottom"):
                    call nar(">Suddenly Hermione reaches inside one of her hidden pockets.", "start")
                else:
                    call nar(">Suddenly Hermione reaches inside--", "start")
                    call nar(">Wait, she's not exactly clothed...{w=0.4} Well...")
                    call nar(">Magically, a pair of panties suddenly appears in her hand.")

            call nar(">She casually throws the offending underwear on your desk.", "end")

        call her_main("Classes are about to start, so I'd better go now...", "soft", "base", "base", "mid")

    call her_walk(action="leave")

    if hermione.is_equipped("panties"): # Cheats fallback
        call give_reward(">You have acquired Hermione's panties!", hermione.get_equipped("panties").get_icon())
    else:
        call give_reward(">You have acquired Hermione's panties!", her_panties_base1.get_icon())
    $ hg_ps_get_panties.inProgress = True

    jump end_hermione_event


label hg_cum_on_panties_response:
    # Hermione responds the cum on her panties

    if her_tier == 2:
        call her_main("*Hmm*....?", "annoyed", "narrow", "worried", "down",xpos="right",ypos="base")
        call her_main("[genie_name]? What is this?", "angry", "base", "angry", "mid")
        her "What have you done to them?"
        call her_main("They are covered in something slimy...", "normal", "squint", "angry", "mid")

        menu:
            "\"An experiment went wrong\"":
                call her_main("An experiment went wrong, [genie_name]?", "open", "base", "base", "mid")
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? *He-he*..."
                call her_main(".....................?", "normal", "squint", "angry", "mid")
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                call her_main("................................", "angry", "base", "angry", "mid")
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [genie_name]!"
                her ".........................."

        call her_main("Well, these will require some serious cleaning before I can put them on again...", "annoyed", "narrow", "worried", "down")
        m "Or you could put them on now."
        call her_main("What?", "open", "base", "base", "mid")
        call her_main("I really would rather not, [genie_name]...", "soft", "base", "base", "R")

        menu:
            "\"Put them on or lose the points!\"":
                $ her_mood +=7
                call her_main("What?", "scream", "wide", "base", "mid")
                her "[genie_name], you are joking, right?"
                m "I am not..."
                call her_main("B-but...", "open", "base", "base", "mid")
                call her_main("........................................", "normal", "happyCl", "worried", "mid")
                call her_main("{size=-5}Must you always have your way, [genie_name]?{/size}", "angry", "base", "angry", "mid")
                m "What was that, [hermione_name]?"
                call her_main("It's nothing, [genie_name].", "scream", "closed", "angry", "mid")
                her "Putting my panties back on!"
                hide screen hermione_main
                call nar(">Hermione hesitantly puts on her panties.","start")

                if hermione.is_equipped("panties"):
                    $ hermione.wear("panties")
                else:
                    $ hermione.equip(her_panties_base1)

                call nar(">A tiny stream of cum trickles down her leg.")
                call nar(">Hermione looks very uncomfortable.","end")
                call her_main("......................", "angry", "happyCl", "worried", "mid",emote="sweat")

            "\"Well, suit yourself...\"":
                pass

        call her_main("And my payment?", "open", "base", "base", "mid")

    elif her_tier == 3:
        call her_main("My panties...", "annoyed", "narrow", "worried", "down",xpos="right",ypos="base")
        call her_main("What happened to them [genie_name]?", "annoyed", "narrow", "worried", "down")

        menu:
            "\"An experiment went wrong.\"":
                her "*Hmm*..."
                her "I see..."

            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."

        hide screen hermione_main
        call nar(">Hermione gives her cum-soaked underwear a quizzical look.")
        call her_main("Seems like these will require some serious cleaning before I can put them on again...", "annoyed", "narrow", "worried", "down")
        m "Why not put them on now?"
        call her_main("*Hmm*...?", "annoyed", "squint", "base", "mid")
        call her_main("Well, I suppose I could wear them one more time before putting them into laundry...", "annoyed", "narrow", "worried", "down")
        hide screen hermione_main
        call nar(">Hermione puts on the panties.")

        if hermione.is_equipped("panties"):
            $ hermione.wear("panties")
        else:
            $ hermione.equip(her_panties_base1)

        call her_main("(This feels funny...)", "angry", "happyCl", "worried", "mid",emote="sweat")
        call her_main("And my payment, [genie_name]?", "upset", "wink", "base", "mid")


    elif her_tier == 4:
        call her_main("My panties...", "annoyed", "narrow", "worried", "down",xpos="right",ypos="base")
        her "They are covered in something slimy..."
        her "And they smell funny..."
        call her_main("*Hmm*... That smell...", "annoyed", "base", "worried", "R")
        her "It's familiar somehow..."
        call her_main("What exactly did you do to them, [genie_name]?", "base", "base", "base", "mid")

        menu:
            "\"An experiment went wrong\"":
                her "An experiment, *huh*?"
                her "Of what nature?"
                call her_main("No, don't answer that... I think I know...", "smile", "base", "base", "R")

            "\"You gave them to me like this!\"":
                her "I don't think so, [genie_name]."
                her "But it's alright if you don't want to tell me, [genie_name]..."
                her "I think I know exactly what happened to them..."

            "\"I came all over them!\"":
                call her_main("I knew it...", "smile", "narrow", "base", "mid_soft")
                her "They reek of semen!"

        call her_main("*Hmm*...", "grin", "base", "base", "R")
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?", "smile", "narrow", "base", "mid_soft")

        menu:
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Well, if I must..."

            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"

        call her_main("I am only doing this to give my house a fair chance at winning the cup this year...", "base", "happyCl", "base", "mid")
        m "Right..."
        hide screen hermione_main
        call nar(">Hermione swiftly slides into her drenched panties...")

        if hermione.is_equipped("panties"):
            $ hermione.wear("panties")
        else:
            $ hermione.equip(her_panties_base1)

        m "You can go now."
        call her_main("What about my points?", "scream", "closed", "angry", "mid")
        m "You still want points after I just gave you a gift?"
        her "What gift?"
        m "You're wearing it."
        her "What, semen soaked panties?"
        m "If you'd prefer the points then just take them off."
        call her_main("well... I am already wearing them!", "annoyed", "base", "worried", "R")
        m "Then say \"thank you\" for the gift."
        call her_main("Thank you, [genie_name]...{w=0.3} for the gift.", "annoyed", "squint", "base", "mid")
        m "You can go now."
        her "Good night, [genie_name]."

    elif her_tier >= 5:
        call her_main("My panties...", "base", "narrow", "base", "up",xpos="right",ypos="base")
        her "You came all over them..."
        call her_main("*Hmm*...", "grin", "base", "base", "R")
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?", "smile", "narrow", "base", "mid_soft")

        menu:
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Yes [genie_name]..."
                call her_main("I am only doing this to give my house a fair chance at winning the cup this year.", "smile", "happyCl", "base", "mid")
                call her_main("I don't like how it feels at all...", "base", "narrow", "base", "up")
                m "Right..."
                hide screen hermione_main
                call nar(">Hermione swiftly slides her drenched panties on...")

                if hermione.is_equipped("panties"):
                    $ hermione.wear("panties")
                else:
                    $ hermione.equip(her_panties_base1)

                call her_main("...", "soft", "narrow", "annoyed", "up")
            "\"Why don't you clean them now?\"":
                call her_main("Clean them How? You don't have a wash basin in here.", "open", "base", "base", "mid")
                m "You're right, you'll have to use your mouth then."
                call her_main("My mouth?!", "scream", "wide", "base", "mid")
                m "What's the big deal? It wouldn't be the first time you've tasted my cum."
                call her_main("It's a bit different! I wore these panties before I gave them to you.", "scream", "closed", "angry", "mid")
                call her_main("Not to mention that your cum is all cold and slimy...", "scream", "happyCl", "worried", "mid")
                m "Well in that case hand them back."
                call her_main("What? Can't I just put them on?", "angry", "wink", "base", "mid")
                m "I'm afraid not, you clean them now or you hand them back."
                call her_main("{size=-4}Fine...{/size}", "angry", "narrow", "base", "down")
                m "What was that?"
                call her_main("I said I'll clean them ok!", "shock", "happyCl", "worried", "mid")
                m "Well..."
                call her_main("...", "angry", "narrow", "base", "down")
                call nar(">Hermione reluctantly puts her cum-soaked panties in her mouth.")
                $ renpy.play('sounds/gltch.mp3')
                call her_main("*Mmmmhhhhh*!", "full_panties", "slit", "worried", "ahegao")
                m "That's it, not as bad as you thought now is it?"
                call her_main("...", "full_panties", "slit", "low", "stare")
                m "Make sure you get them nice and clean now..."
                call play_sound("gulp")
                call her_main("*gulp*", "full_panties", "narrow", "worried", "down",cheeks="blush")
                m "That's it. Do you think they're clean yet?"
                call her_main("*Mmmhhhmmm*", "full_panties", "narrow", "base", "dead")
                m "Open your mouth, [hermione_name]."
                $ renpy.play('sounds/gltch.mp3')
                call her_main("*Ahhhhh*", "open_wide_tongue_panties", "narrow", "annoyed", "up")
                m "That's a good girl, your panties are now nice and clean."
                m "You can take them out now."
                call her_main("....", "angry", "happyCl", "worried", "up")

        m "You can go..."
        call her_main("yes, [genie_name]...", "angry", "narrow", "base", "down")
        m "After you say \"thank you\"..."
        call her_main("Thank you for what?", "angry", "wink", "base", "mid")
        m "For my cum."
        call her_main("...", "base", "narrow", "worried", "down")
        call her_main("Thank you for your cum, [genie_name]...", "grin", "narrow", "base", "dead")
        m "You may go now."
        her "Good night, [genie_name]."

    $ achievement.unlock("pantiesfap")
    jump back_from_soaked


label hg_ps_get_panties_complete:
    # Hermione returns to get her panties back

    $ hermione.strip("panties")

    call her_walk(action="enter", xpos="mid", ypos="base")

    call her_main("Good evening, [genie_name]...", "base", "base", "base", "mid",xpos="right",ypos="base")
    call play_music("chipper_doodle")

    menu:
        "\"Here are your panties.\"":
            if her_panties_soaked:
                jump hg_cum_on_panties_response
            else:
                her "And my payment?"

        "\"How was your day, [hermione_name]?\"":
            if her_tier == 2:
                $ sc34CG(1, 10, trans=None)
                call her_main("Oh...", "soft", "base", "base", "mid",xpos="base",ypos="base", trans=d5)
                her "Quite ordinary actually..."
                call her_main("Although... I couldn't help but worry that somebody would notice somehow...", "soft", "base", "base", "R")
                call her_main(".....", "annoyed", "base", "worried", "R")
                hide screen sccg
                call her_main("Can I have my panties back now?", "open", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
                m "Of course..."
                hide screen hermione_main
                with d3
                call nar(">You give Hermione her panties back.")
                if her_panties_soaked:
                    jump hg_cum_on_panties_response
                else:
                    call her_main("And my payment?", "open", "base", "base", "mid")

            elif her_tier == 3:
                $ sc34CG(1, 5, trans=None)
                call her_main("Oh...", "soft", "base", "base", "mid",xpos="base",ypos="base", trans=d5)
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                call her_main("I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"...", "open", "closed", "base", "mid")
                call her_main("I felt bad that I had to give the speech without any underwear on...", "annoyed", "narrow", "angry", "R")
                hide screen sccg
                call her_main(xpos="right",ypos="base",trans=fade)

                menu:
                    "\"You little hypocrite!\"":
                        $ her_mood +=5
                        call her_main("[genie_name]?", "open", "base", "base", "mid")
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behaviour..."
                        #m "What would you call this?"
                        #call her_main("I know you are right, [genie_name]...", "annoyed", "narrow", "angry", "R")
                        call her_main("(But we need the points...)", "annoyed", "narrow", "angry", "R")
                        call her_main("Can I have my payment now please?", "disgust", "narrow", "base", "mid_soft")
                        m "What about your panties?"
                        call her_main("Oh, them too of course...", "angry", "happyCl", "worried", "mid",emote="sweat")
                        if her_panties_soaked:
                            jump hg_cum_on_panties_response

                    "\"It's for the greater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        call her_main("I shall remain a symbol of righteousness to my peers, no matter what!", "open", "closed", "base", "mid")
                        call her_main("Can I have my panties back now, please?", "open", "base", "base", "mid")
                        if her_panties_soaked:
                            jump hg_cum_on_panties_response
                        else:
                            her "And my payment."

            elif her_tier >= 4:
                $ sc34CG(1, 11, trans=None)
                call her_main("Another ordinary day at hogwarts...", "open", "closed", "base", "mid",xpos="base",ypos="base", trans=d5)
                her "Nothing worth mentioning happened today..."
                call her_main("Although I have to admit...", "annoyed", "base", "worried", "R")
                her "It was oddly empowering to have no underwear on..."
                her "*Hmm*..."
                hide screen sccg
                call her_main("Can I have my panties back now please?", "base", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
                m "Of course..."
                hide screen hermione_main
                with d3
                call nar(">You give Hermione her panties back.")
                if her_panties_soaked:
                    jump hg_cum_on_panties_response
                else:
                    call her_main("And my payment?", "base", "base", "base", "mid")

    label back_from_soaked:
    if not her_panties_soaked or her_tier < 4:
        m "Yes, yes..."
        $ gryffindor +=15
        m "Fifteen points to Gryffindor, [hermione_name]. Well deserved."
        her "Thank you, [genie_name]..."
        m "You can go now."
        her "Good night, [genie_name]."
        #m "Yes, good night..."

    call her_walk(action="leave")

    $ hg_ps_get_panties.counter += 1
    $ hg_ps_get_panties.points += 1

    $ hg_ps_get_panties.inProgress = False
    $ her_panties_soaked = False

    jump end_hermione_event
