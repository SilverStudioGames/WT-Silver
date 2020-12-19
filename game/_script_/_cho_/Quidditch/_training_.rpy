
### Cho Quidditch Tactics ###

label cho_training:

    # Automatic-Events

    # Quiz.
    if not cho_quiz.complete:
        jump cho_quiz

    # Training Intro 1.
    # Event fails. Cho will get mad and leaves.
    if not cho_quid.E1_complete:
        jump cho_quid_E1

    # Training Intro 2.
    if not cho_quid.E2_complete:
        jump cho_quid_E2

    # Setup

    show screen blkfade
    call hide_characters
    with d5

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    call cho_chibi("stand", "right", "base")

    show screen chair_left
    show screen desk
    call gen_chibi("stand", "desk", "base")

    hide screen bld1
    hide screen blkfade
    with d5
    pause .8

    # Menu
    label .choices:

    menu:
        "-Discuss Quidditch Training-":
            if cho_tier == 1:
                # Hufflepuff
                jump cc_ht_talk
            elif cho_tier == 2:
                # Slytherin
                jump cc_st_talk
            #elif cho_tier == 3:
                # Gryffindor
                #jump cc_gt_talk

            jump cho_training.choices

        "-Discuss Tactics-" if cc_pf_talk.is_tier_complete() and not cho_quid.lock_tactic:
            if cho_tier == 1:
                # Hufflepuff
                # Clothes:  Skirt, Robes
                if not hufflepuff_match == "intro_done":
                    $ hufflepuff_match = "intro_done"

                    m "I got it!"
                    call cho_main("Got what?", "soft", "base", "base", "mid")
                    m "I know how to get you that win against those Badgers!"
                    call cho_main("Really? How?", "soft", "base", "raised", "mid")
                    m "You told me how, yourself."
                    m "Panties are the key!"
                    call cho_main("Panties? What does panties have to do with Quidditch?", "soft", "wide", "raised", "mid")
                    m "Everything, girl!{w} For some they are the meaning of life!"
                    call cho_main("What are you suggesting exactly?", "clench", "base", "base", "mid", cheeks="blush")
                    m "My plan is that we use Cedric's obsession with panties to distract him during the game."
                    call cho_main("I don't really see how that would be--", "annoyed", "base", "base", "downR", cheeks="blush")
                    m "You'll have to wear a skirt of course."
                    call cho_main("A skirt?", "clench", "wide", "base", "mid", cheeks="heavy_blush") #shocked
                    g9 "Of course!"
                    g9 "If he's too focused on your panties there's no way he'll catch that snatch!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 3:
                        # Fail
                        call cho_main("Got a better plan? One that doesn't involve showing off my panties?", "annoyed", "base", "base", "mid")
                        m "..."
                        call cho_main("Didn't think so...", "open", "narrow", "raised", "mid")
                        m "(Damn... maybe I need to work on her confidence a bit...)"
                        g9 "(Some more favours should surely do it...)"

                        jump cho_training.choices

                if cho_whoring >= 3:
                    $ cho_quid.lock_practice = False

                    call cho_main("...", "normal", "narrow", "base", "downR", cheeks="blush")
                    call cho_main("You actually think that will work?", "open", "closed", "angry", "mid", cheeks="blush")
                    m "If what you're telling me about him is true I'm sure of it."
                    call cho_main("...", "clench", "closed", "base", "mid", cheeks="blush")
                    call cho_main("But what if it doesn't?", "annoyed", "base", "base", "down", cheeks="blush")
                    call cho_main("I need to win the game to make it to the finals!", "open", "base", "angry", "mid", cheeks="blush")
                    m "Then let's put this theory into practice..."
                    call cho_main("You want me to try it out during next practice against them?", "upset", "base", "raised", "mid", cheeks="blush")
                    m "You do practice matches against the other...{w=0.5} actually, that's a great idea!"
                    m "That way we'll know it works for sure!"
                    call cho_main("...", "disgust", "base", "base", "down", cheeks="blush")
                    call cho_main("Fine, but I'm not changing any of my other clothes, I'd rather not have anyone else staring at my panties...", "annoyed", "base", "angry", "mid", cheeks="blush")
                    m "Okay then..."
                    m "Get your broom and Quidditch-gear... and put that skirt on!"
                    call cho_main("Alright...", "annoyed", "base", "base", "mid", cheeks="blush")

                    #Cho returns with the Hufflepuff clothing combination
                    $ cho.equip(cho_outfit_quidditch_hufflepuff)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, now what?", "base", "base", "base", "mid", trans=fade)

                    m "Now let's try some flying positions..."
                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Excellent..."

                    jump cho_tactics
                else:
                    # Fail

                    call cho_main("I will do nothing of the sort!", "mad", "base", "angry", "mid")
                    m "Sorry?"
                    call cho_main("You want me to wear a skirt during quidditch?", "mad", "narrow", "angry", "mid")
                    call cho_main("The whole school will be there!", "clench", "wide", "base", "mid")
                    m "Don't focus on them, Cedric is your target!"
                    call cho_main("But they'll see my panties!", "mad", "base", "base", "down", cheeks="blush")
                    call cho_main("No, I will not be going through with this plan of yours...", "open", "base", "angry", "mid", cheeks="blush")
                    call cho_main("You better come up with something else!", "soft", "base", "angry", "mid", cheeks="blush")

                    # Cho gets upset and leaves
                    $ cho_mood += 6
                    call cho_walk(action="leave")

                    m "(Damn... maybe I need to work on her confidence a bit...)"
                    g9 "(Some more favours should surely do it...)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

            elif cho_tier == 2:
                # Slytherin
                # Clothes: Trousers, Pullover
                if not slytherin_match == "intro_done":
                    $ slytherin_match = "intro_done"

                    m "I got it!"
                    m "I've got the perfect idea on how to beat those snakes!"
                    call cho_main("...", "normal", "narrow", "raised", "mid")
                    m "Do we even say \"phrasing\" anymore?"
                    call cho_main("Just tell me your plan.", "open", "narrow", "raised", "mid")
                    m "It's all about the ass!"
                    call cho_main("The ass?", "upset", "base", "raised", "mid", cheeks="blush") #shocked
                    m "Yes, you told me how those brutes love a good ass spanking, now that's an ass fetish if I ever heard one!"
                    m "So this time we'll have those Slytherins get a good look of your ass!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 9:
                        # Fail
                        call cho_main("Got a better plan? One that doesn't involve flaunting my ass to those Slytherins?", "annoyed", "base", "base", "mid")
                        m "..."
                        call cho_main("Didn't think so...", "open", "narrow", "raised", "mid")
                        m "(Damn...)"
                        m "(Looks like she isn't confident enough yet...)"
                        m "(Some more favours should do the trick.)"

                        jump cho_training.choices

                if cho_whoring >= 9 and cc_pf_strip.is_event_complete(2, 3):
                    $ cho_quid.lock_practice = False

                    call cho_main("...", "soft", "base", "raised", "mid")
                    m "And yes, before you ask, I'm sure this will ensure the win."
                    call cho_main("Fine...", "upset", "base", "base", "R", cheeks="blush")
                    call cho_main("I can't believe I'm saying this...", "soft", "happyCl", "base", "mid", cheeks="blush")
                    call cho_main("I'll flaunt my ass... to those Slytherins.", "clench", "narrow", "base", "mid", cheeks="blush")
                    m "Excellent, then let's discuss some tactics..."
                    m "I'd like you to put on some trousers this time."
                    m "And get rid of your robes, they'll cover it too much."
                    call cho_main("Get rid of my--", "open", "wide", "angry", "mid", cheeks="heavy_blush") #Shocked
                    m "You can put on something else, just something that doesn't cover the goods."
                    call cho_main("Alright...{w=0.5} give me a minute to fetch my gear...", "angry", "closed", "base", "mid", cheeks="blush")

                    #Cho returns with the Slytherin clothing combination
                    $ cho.equip(cho_outfit_quidditch_slytherin)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, tell me what to do.", "base", "base", "base", "mid", trans=fade)

                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Great."

                    jump cho_tactics

                else:
                    # Fail

                    call cho_main("But, they're Slytherins!", "clench", "base", "angry", "mid")
                    m "And?"
                    call cho_main("You expect me to flaunt my ass to those brutes?", "mad", "base", "angry", "mid", cheeks="heavy_blush")
                    m "Are you telling me you don't think it will work?"
                    call cho_main("Of course it will work, they're dumb as hell.", "open", "base", "angry", "R", cheeks="blush")
                    call cho_main("But everyone will be able to see my butt!", "quiver", "base", "raised", "down")
                    g4 "That's the point."
                    call cho_main("But, but, but!", "open", "closed", "worried", "mid")
                    g9 "That's probably what the crowd will be chanting..."
                    call cho_main("Teasing Cedric is one thing... but the Slytherins...", "mad", "happyCl", "worried", "down")
                    call cho_main("I can't see my self doing...{w=0.4} this...", "base", "base", "base", "mid")
                    m "Well, that's your loss I guess..."
                    call cho_main("...", "normal", "happyCl", "base", "mid", cheeks="blush")
                    call cho_main("If that's all you have then I think I'm done here.", "open", "base", "worried", "down", cheeks="blush")

                    # Cho gets upset and leaves
                    $ cho_mood += 3
                    call cho_walk(action="leave")

                    m "(Damn...)"
                    m "(Looks like she isn't confident enough yet...)"
                    m "(Some more favours should do the trick.)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

            elif cho_tier == 3:
                # Gryffindor:
                # Clothes: No clothes decided on yet
                if not gryffindor_match == "intro_done":
                    $ gryffindor_match = "intro_done"

                    m "I got it!"
                    call cho_main("Finally...", "soft", "base", "raised", "R")
                    call cho_main("So, what's the plan?", "open", "base", "raised", "mid")
                    m "It's time to get intimate!"
                    call cho_main("Intimate?", "upset", "base", "raised", "mid")
                    m "Yes, touchy touchy!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 12:
                        # Fail
                        call cho_main("Got a better plan? One that doesn't involve me getting felt up?", "annoyed", "base", "base", "mid")
                        m "..."
                        call cho_main("Didn't think so...", "open", "narrow", "raised", "mid")
                        m "(She doesn't seem fully convinced...)"
                        m "(But after some more favours... Surely she'll be more keen with the idea.)"

                        jump cho_training.choices

                if cho_whoring >= 12:
                    $ cho_quid.lock_practice = False

                    call cho_main("What are you basing this plan of yours on?", "soft", "narrow", "base", "down", cheeks="blush")

                    if cc_pr_manipulate_girls.is_complete(): # has completed "Manipulate the girls!" public request?
                        m "Those girls sure are fond of you by now. If you could get close to them they'll surely lose focus on the game."
                        call cho_main("Although that doesn't solve an important issue...", "open", "base", "raised", "mid", cheeks="blush")
                    else:
                        m "It's obvious isn't it..."
                        call cho_main("No?", "annoyed", "base", "raised", "mid", cheeks="blush")
                        m "Those girls doing naughty things together."
                        m "If you get close to them they'll lose focus on the game!"
                        call cho_main("...", "normal", "closed", "base", "mid", cheeks="blush") #worried
                        call cho_main("And what about the boys?", "mad", "base", "raised", "mid", cheeks="blush")
                        m "What about them?"

                    call cho_main("Shouldn't their seeker... Harry, be our priority?", "annoyed", "narrow", "raised", "R") #annoyed
                    m "The same tactic is sure to work for him."
                    m "I'm sure Hermione will go mental and make him lose focus if you get close to him seeing that they're friends."
                    call cho_main("Now that's a plan!", "smile", "base", "base", "mid")
                    m "Great, it's settled then!"
                    # TODO: Add clothing writing if any
                    call cho_main("Let me fetch my gear and you can show me how you want me to fly.", "crooked_smile", "base", "base", "mid")

                    #Cho returns with the Gryffindor clothing combination
                    $ cho.equip(cho_outfit_quidditch_gryffindor)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, tell me what to do.", "base", "base", "base", "mid", trans=fade)

                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Great."

                    jump cho_tactics
                else:
                    # Fail

                    call cho_main("You want me to let their team feel me up?", "mad", "base", "raised", "mid", cheeks="blush")
                    m "Absolutely!"
                    m "And you should touch them a bit as well while you're at it!"
                    call cho_main("No way!", "soft", "wide", "base", "mid", cheeks="blush")
                    g4 "Why not?"
                    call cho_main("Teasing them is one thing but touching as well?", "angry", "base", "base", "mid", cheeks="blush")
                    call cho_main("With everyone watching.", "horny", "happyCl", "base", "mid", cheeks="heavy_blush") #blushes but imagining it
                    m "..."
                    call cho_main("No, I wont do it...", "horny", "base", "base", "downR", cheeks="blush")
                    m "But what if--"

                    # Cho gets upset and leaves
                    $ cho_mood += 3
                    call cho_walk(action="leave")

                    m "(She doesn't seem fully convinced...)"
                    m "(But after some more favours... Surely she'll be more keen with the idea.)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

        "{color=[menu_disabled]}-Discuss tactics-{/color}" if not cc_pf_talk.is_tier_complete() or cho_quid.lock_tactic:
            if cho_quid.lock_tactic:
                m "(We've already established a tactic for the next match)"
            else:
                m "(I don't know enough about the enemy team.)"
                m "(Cho and I should have a talk first.)"

            jump cho_training.choices

        "-Start Practice Match-" if daytime and not cho_quid.lock_practice:
            if cho_tier == 1:
                # Hufflepuff
                jump cc_ht_start
            elif cho_tier == 2:
                # Slytherin
                jump cc_st_start
            #elif cho_tier == 3:
                # Gryffindor
                #jump cc_gt_start

        "{color=[menu_disabled]}-Start Practice Match-{/color}" if not daytime or cho_quid.lock_practice:
            if cho_quid.lock_practice:
                if (cho_tier == 1 and cho_quid.hufflepuff_training) or (cho_tier == 2 and cho_quid.slytherin_training):
                    m "(She doesn't need any more practice.)"
                else:
                    call nar(">Cho isn't ready for practice yet.")
            else:
                call nar(">You can only do that during the day.")

            jump cho_training.choices

        "-Back-":
            call cho_main("Very well, [cho_genie_name].", "open", "base", "base", "mid", ypos="head", flip=False)

            hide screen cho_main
            show screen blkfade
            with d3

            $ cho.equip(cho_outfit_last)

            call cho_chibi("stand", "mid", "base")
            call gen_chibi("sit_behind_desk")

            call reset_menu_position

            hide screen blkfade
            call cho_main(face="happy", xpos="base", ypos="base", trans=fade)
            jump cho_requests

### Quidditch Tactics ###

label cho_tactics:

    # Menu
    label .choices:

    call hide_characters
    call bld

    $ menu_y = 0.8

    menu:
        m "(What directions should I give her?)"
        "\"Fly in front of me.\"" if cho_quid.position != "front":
            jump cho_tactics.change_front
        "\"Fly in front of me.\" {size=-6}(selected){/size}" if cho_quid.position == "front":
            pass

        "\"Fly above me.\"" if cho_quid.position != "above":
            jump cho_tactics.change_above
        "\"Fly above me.\" {size=-6}(selected){/size}" if cho_quid.position == "above":
            pass

        "\"Fly close to me.\"" if cho_quid.position != "close":
            jump cho_tactics.change_close
        "\"Fly close to me.\" {size=-6}(selected){/size}" if cho_quid.position == "close":
            pass

    m "(No, that probably won't work...)"

    jump cho_tactics.choices

    # Change Tactic
    #TODO This plays once cho has agreed to the tactic/clothing and during the first intro
    # Once you pick the right option the practice match option unlocks (Maybe we should have it say Try out tactic?)
    # The various options should go away once you've tried it once

    label .change_front:
        # The *ASS* position!
        $ cho_quid.position = "front"

        if cho_tier == 1:
            # Hufflepuff

            call cho_walk(600, 150+180)

            call cho_main("Is this good?", "open", "base", "raised", "mid", ypos="head", flip=False)
            m "*Hmm*... No, that robe is in the way... I can't seem to get a good view from this angle..."
            call cho_main("Good! Then the crowd shouldn't either!", "smile", "base", "base", "down", ypos="head", flip=False)
            m "Yes, probably..."
            m "How about instead you..."

        elif cho_tier == 2:
            # Slytherin

            call cho_walk(600, 150+180)

            call cho_main("How's this?", "open", "base", "raised", "mid", ypos="head", flip=False)
            m "Excellent, I told you getting rid of that coat would do it!"
            m "And those trousers sure emphasise the shape of your--"

            # Cho turns towards you

            call cho_main("Good, then it's settled!", "soft", "base", "base", "down", cheeks="blush", ypos="head", flip=False)
            m "But I didn't get a proper look yet!"
            call cho_main("...", "clench", "base", "base", "mid", cheeks="blush", ypos="head", flip=False)
            m "Alright, you can come down then..."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide screen cho_main
            with fade

            m "We'll test the tactics during the next practice like usual."
            call cho_main("Do we have to? I'm sure it will work even without trying it.", "clench", "base", "raised", "mid", cheeks="blush")
            m "Of course we do! You're the one that was so adamant last time..."
            m "So let's see those results!"
            call cho_main("Yeah... Great, just let me know when...", "normal", "closed", "base", "mid", cheeks="blush")
            g9 "I certainly shall."
            m "But this will do for today, [cho_name]."

            if daytime:
                call cho_main("I'll head back to class then.", "open", "base", "base", "R")
            else:
                call cho_main("I'll head back to my dorm then.", "open", "base", "base", "R")

            g9 "Until next time."

            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            jump end_cho_event

        elif cho_tier == 3:
            # Gryffindor

            call cho_walk(600, 150+180)

            m "No, this won't do, you're way to far away from me."
            call cho_main("Then where do you want me?", "annoyed", "base", "raised", "mid", ypos="head", flip=False)
            m "Let's see..."

        jump cho_tactics.choices

    label .change_above:
        # The ~Panties~ position!
        $ cho_quid.position = "above"

        if cho_tier == 1:
            # Hufflepuff

            m "Now, start with getting in front of me..."

            call cho_walk(550, 200+180)

            call cho_main("Like this?", "soft", "base", "base", "downR", ypos="head", flip=False)
            with hpunch
            g4 "Yes, and now...{w=0.4} Higher!"
            call cho_main("Is this not high enough to see my--", "annoyed", "base", "raised", "mid", ypos="head", flip=False)
            g4 "Fly right above my head!"
            g4 "Show me those panties!"
            call cho_main("Of course, [cho_genie_name]...", "base", "base", "base", cheeks="blush", "downR", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            call cho_main("How is this?", "soft", "base", "base", "down", cheeks="blush", ypos="head", flip=False)

            # TODO: Panty shot CG?

            # Genie looks up.
            call gen_chibi("stand_alt", "desk", "base")
            show screen bld1
            with d3

            g4 "Yes, fantastic!"
            g9 "You have very cute panties, girl!"
            call cho_main("*Ehm*...{w=0.5} Thank you, [cho_genie_name].", "annoyed", "base", "base", "down", cheeks="blush", ypos="head", flip=False)
            m "(I have created the ultimate up-skirt!)"
            m "(Nothing can stop us now...)"
            call cho_main("Can I come down now?", "soft", "base", "base", "downR", ypos="head", flip=False)
            g9 "Give me another minute."
            call cho_main("*Tsk*", "normal", "base", "raised", "L", cheeks="blush", ypos="head", flip=False)
            m "Okay, you can come down now."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide screen cho_main
            with fade

            call cho_main("Enjoyed the view?", "upset", "base", "angry", "mid", cheeks="blush") #angry/annoyed
            m "Very much so."
            call cho_main("Good!", "smile", "base", "base", "mid")
            call cho_main("Then I'm sure Cedric will like it too...", "base", "closed", "base", "mid")
            m "Who?"
            m "Oh yeah, that guy!"
            m "Yes, we should definitely try this during your next practice match against them."
            call cho_main("...", "normal", "base", "raised", "mid") #annoyed
            m "When is that again?"
            call cho_main("*Sigh* Just let me know when and I'll set one up with their captain.", "open", "narrow", "base", "R")
            m "Excellent."

            if daytime:
                call cho_main("If that is all, I'll head back to class.", "open", "base", "base", "mid")
                m "Yes, that shall do for today."
                call cho_main("Good day then, Sir...", "soft", "narrow", "base", "mid")
            else:
                call cho_main("If that is all, I'll head back to my dorm.", "open", "base", "base", "mid")
                m "Yes, that shall do for today."
                call cho_main("Good night then, Sir...", "soft", "narrow", "base", "mid")

            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho_quid.hufflepuff_prepared = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            jump end_cho_event

        elif cho_tier == 2:
            # Slytherin

            call cho_main("Above you, [cho_genie_name]?", "annoyed", "base", "raised", "mid", ypos="head", flip=False)
            m "Yes, above..."
            call cho_main("Okay...", "upset", "base", "base", "mid", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            m "Hold on, that's a bit too high I think..."
            call cho_main("You think?", "angry", "base", "raised", "mid", ypos="head", flip=False) #annoyed
            m "Yeah, how about instead you..."

        elif cho_tier == 3:
            #Gryffindor

            call cho_main("You want me to fly... above you?", "clench", "base", "raised", "mid", ypos="head", flip=False)
            m "You heard what I said..."
            call cho_main("Okay then...", "upset", "base", "base", "mid", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            g4 "Hey, how am I supposed to reach you from up there?"
            m "That's not how you get intimate!"
            call cho_main("Why did you tell me to fly above you then?", "annoyed", "base", "base", "down", ypos="head", flip=False)
            m "..."
            m "Sorry, I can't hear you from all the way up there."
            m "I think it might be better if you..."

        jump cho_tactics.choices

    label .change_close:
        # The ~intimate~ position!
        $ cho_quid.position = "close"

        if cho_tier == 1:
            # Hufflepuff

            call cho_main("Close? How would you be able to see my--", "annoyed", "base", "base", "mid", ypos="head", flip=False)
            m "Come closer!"

            call cho_walk(450, 240+180)

            m "Wait a second, I can't see your panties at all from this angle..."
            call cho_main("No shi--", "open", "narrow", "base", "mid", ypos="head", flip=False)
            m "Let's try this instead..."

        elif cho_tier == 2:
            # Slytherin

            call cho_main("Close?", "annoyed", "base", "base", "mid", ypos="head", flip=False)
            m "Yes close... did I stutter?"

            call cho_walk(450, 240+180)

            m "You smell nice..."
            call cho_main("Yeah, this is not going to work...", "disgust", "narrow", "base", "mid", ypos="head", flip=False)
            m "Fine, let's have you..."

        elif cho_tier == 3:
            # Gryffindor

            m "Come as close to me as you can..."
            call cho_main("Yes, [cho_genie_name].", "soft", "base", "base", "R", ypos="head", flip=False)

            call cho_walk(450, 240+180)

            call cho_main("How's this? Too close?", "soft", "wink", "raised", "mid", cheeks="blush", ypos="head", flip=False)
            m "No! It's the perfect distance!"
            m "They should even be able to smell you if you are this close!"
            call cho_main("I hope not!", "quiver", "closed", "worried", "mid", cheeks="blush", ypos="head", flip=False)
            g9 "Why? You smell lovely, girl!"
            call cho_main("*Ehm*...{w} Thank you, Sir.", "soft", "base", "worried", "mid", cheeks="blush", ypos="head", flip=False)

            call cho_main("Can I come down now?", "soft", "narrow", "base", "mid", cheeks="blush", ypos="head", flip=False)
            m "Of course."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide screen cho_main
            with fade

            m "You'll definitely distract those girls with this kind of move!"
            call cho_main("And boys...", "open", "base", "raised", "R")
            m "Oh yeah, them to!"
            call cho_main("Just let me know when to try it out against them.", "normal", "base", "raised", "mid")
            m "Certainly... Oh, and keep wearing that scent, whatever it is."
            call cho_main("It's just deodorant...", "clench", "base", "raised", "mid", cheeks="blush")
            m "Yes, that! Keep wearing it!"
            if daytime:
                call cho_main("If that is all, I'll head back to class.", "base", "narrow", "base", "R")
                m "Yes, that shall do for today."
                call cho_main("Good day then, Sir...", "soft", "narrow", "base", "mid")
            else:
                call cho_main("If that is all, I'll head back to my dorm.", "base", "narrow", "base", "R")
                m "Yes, that shall do for today."
                call cho_main("Good night then, Sir...", "soft", "narrow", "base", "mid")


            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            jump end_cho_event

        jump cho_tactics.choices
