

### Cho Blowjob ###

label cc_pf_blowjob:

    if cc_pf_blowjob.counter == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"

    if cc_pf_blowjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_favor_menu.personal

    # Setup
    $ warned_her = False

    $ cc_pf_blowjob.start()

    # End Event Jump
    label end_cc_pf_blowjob:

    $ cho.set_cum(None)

    if cho_tier == 3:
        if cho_whoring < 12: # Points til 16
            $ cho_whoring += 1

    jump end_cho_event

label cc_pf_blowjob_T3_intro_E1:

    if cho_bj_choice == None:
        m "[cho_name], ready to reward your coach for a job well done?"
        call cho_main("Of course... a deal's a deal.", "open", "narrow", "base", "mid")
        m "Great, in that case I think a blowjob is in order!"
        call cho_main("A blowjob?!!", "disgust", "wide", "base", "mid")
        m "And some hand action as well of course!"
        call cho_main("Sir, I didn't think it'd come to this... I already showed you my naked body and everything...", "clench", "narrow", "base", "down")
        m "There are other tactics you could use that aren't just about showing off your body in public you know..."
        call cho_main("Oh, yeah? Like what?", "angry", "narrow", "raised", "mid")
        m "Your dream is to become a professional is it not?"
        call cho_main("I... yes... I suppose it is.", "soft", "narrow", "base", "R")
        m "Then we should do our best to prepare you for what's out there!"
        m "I won't be your coach forever... Once you're looking for a proper team, you'll be in fierce competition with the other women athletes."
        m "Women that will stop at nothing to get what they want."
        m "So, as your coach, it's my responsibility to prepare you!"
        call cho_main("And a blowjob is necessary for this?", "angry", "narrow", "raised", "mid")

        if cc_pr_spy_girls.is_event_complete(3, 1):
            m "You've seen the girls on the Gryffindor team... you think they would hesitate with something as simple as a blowjob?"
            call cho_main("...", "disgust", "closed", "base", "down", cheeks="blush") #Pout
            m "I see how it is..."
            m "I sure didn't think a simple blowjob would dissuade you from pursuing your dreams."
        else:
            m "Well... I can tell you this much. A woman looking to make it professionally should have enough confidence not to get stopped by something as simple as a blowjob."

        call cho_main("...", "normal", "narrow", "base", "downR", cheeks="blush") # angry
        call cho_main("Alright, I'll do it...", "open", "happyCl", "angry", "downR", cheeks="blush")
        g9 "That's more like it!"
        call cho_main("Don't get me wrong sir... I don't believe a word of what you just said is even remotely true.", "upset", "base", "base", "mid", cheeks="blush")
        call cho_main("But you've helped me get this far...", "annoyed", "narrow", "base", "down", cheeks="blush")
        call cho_main("So if a blowjob is what it takes, then so be it...", "soft", "base", "base", "downR", cheeks="blush")
        g9 "That's the kind of determination I've been looking for..."
        g9 "Let's find out how a skilled Quidditch player handles this type of wood..."
        call cho_main("...", "disgust", "narrow", "base", "mid") #smile #looks away
        call cho_main("Okay, then... I'm ready.", "angry", "narrow", "base", "mid", cheeks="blush")
        g4 "(At last!)"

        $ renpy.sound.play("sounds/zipper.mp3")
        hide screen bld1
        hide screen cho_main
        call gen_chibi("jerk_off_behind_desk")
        with d5

        call cho_walk("desk_close", "base")
        pause 0.5

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_shock")
        if game.daytime:
            $ camera.set_overlay("day_overlay")
        else:
            $ camera.set_overlay("night_overlay")
        $ camera.set(zoom=1.0, pos=(950, -750), initialize=True)
        show screen animatedCG
        with fade

        call gen_chibi("sit_behind_desk") # reset

        # Start CG with Cho kneeling in front of Genie.
        # Cho is dressed.

        # Note: Cho does not require posing here because it happens during the CG scene.
        $ renpy.checkpoint()

        pause 0.5
        $ camera.set(pos=(0, -750), t=3.5, pause=True)
        $ camera.set(pos=(150, 400), t=2)
        cho "By Merlin's beard!" #Wide eyed looking at dick #open mouth
        gen "Something wrong?"
        $ camera.set_image("mid_surprised")
        cho "N-No...{w=0.4} It's just...{w=0.4} this close...{w=0.4} it's so much larger than--" #Looking at dick
        gen "Good, then stop staring and put your hand on it..."
        $ camera.set_image("mid_surprised_blush")
        cho "Okay..." #Blush #Normal mouth
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("up_worried")

        pause 0.6

        $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)
        #Cho puts her hand on genies dick and looks up at him

        cho "..." #worried eyes
        gen "What? Don't tell me this is the first time you've done this..."
        $ camera.set_image("away_blush")
        cho "O-{w=0.3}of course I've done it before!"
        gen "Then get that arm moving, use those muscles!"
        $ camera.set_image("up")
        cho "..." # annoyed

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Yes, that's it...{w=0.4} stroke that cock you little Ravenclaw slut..."

        $ camera.set_image("up_annoyed")

        cho "[cho_genie_name]!"# Stops moving hand #Annoyed #Looks up at genie
        gen "What?"
        gen "You're doing a great job [cho_name], keep it going just like that..."

        $ camera.set_image("mid_annoyed")

        cho "*Hmph*..." #annoyed

        $ camera.set_image("away_blush")

        cho "Fine..."

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Such a firm grip..."
        gen "Must be from riding that broom so much..."
        gen "Although your rhythm could do with some work..."

        $ camera.set_image("cho_hj mid annoyed")

        cho "*tsk*..." #Annoyed

        call ctc

        gen "That's better..."
        gen "Now then... Let's find out what you can do with that mouth of yours, shall we?"

        $ camera.set_image("up_wide")

        cho "Already?" #Wide eyed
        $ camera.set_image("up_worried")
        cho "Can't I just keep jerking you off?"
        gen "You agreed to a blowjob did you not?"
        $ camera.set_image("mid_worried")
        cho "I...{w=0.4} well that was before you showed me your..." #Looks back down
        $ camera.set_image("away_blush")
        cho "How is this even..." #Cuts to dialog Menu choice
    else: # Alternate intro if first event has failed
        m "Ready to continue with your training?"
        call cho_main("Of course!", "open", "base", "base", "mid")
        m "Then you know what is required..."
        call cho_main("You want me to touch your...", "soft", "base", "base", "downR", cheeks="blush")
        call cho_main("...", "horny", "closed", "base", "mid", cheeks="blush")
        call cho_main("Fine... I'll do it.", "angry", "base", "base", "mid", cheeks="blush")

        hide screen cho_main
        with d3

        call cho_walk("desk_close", "base")
        pause 1.0

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_surprised")
        $ camera.set(zoom=1.0, pos=(0, -750), initialize=True)
        show screen animatedCG
        with fade

        $ camera.set(pos=(150, 400), t=2.0, pause=True)

        $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)
        cho "Okay... I'm ready."
        $ camera.set_image("mid_surprised_blush")
        cho "..." #blush
        gen "Go on then, I don't have all day..."
        $ camera.set_image("mid_blush")
        cho "R-Right..." #Pout
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("mid_annoyed")
        cho "..." #annoyed
        gen "There you go... much easier the second time, isn't it?"
        gen "Now, get those muscles moving..."

        $ camera.set_image("cho_hj mid")
        call ctc

        gen "That's it... you keep stroking, slut..."

        $ camera.set_image("cho_hj mid annoyed")
        cho "*Hmph*..." #Annoyed

        call ctc

        gen "Good..."
        gen "You're doing way better than last time... Perhaps you've had some time to think things over?"

        $ camera.set_image("cho_hj mid")

        call ctc

        cho "..."

        gen "I take that as a yes... So, let's put that mouth to good use then, shall we?"

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("up_shock")

        cho "Already?"
        gen "No, tomorrow... yes of course now!"
        $ camera.set_image("mid_worried")
        cho "Can't I just keep jerking you off?" #pout
        gen "This again..."

    jump cc_pf_blowjob_1

label cc_pf_blowjob_1:
    menu:
        "-A deal's a deal...-": # FAIL
            gen "That's not what we agreed on."
            gen "Get those lips on there..."

            if cho_bj_choice == None:
                $ camera.set_image("up_wide")
            else:
                $ camera.set_image("up_worried")

            cho "[cho_genie_name]!" #shocked
            gen "It's time to push those limits [cho_name]... we've been over this."
            gen "Open up..."

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            cho "But... it's... how is it even going to fit?!"
            $ camera.set_image("mid")
            gen "It will fit, you're the most flexible girl in the castle. If anyone could do it it's you..."
            cho "..."
            gen "Now, put your hand back..."
            $ camera.set_image("mid_worried")
            cho "..."
            cho "Al-Alright...!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("up_worried")
            #Cho puts her hand back on
            gen "Good... now put your lips around the tip..."

            $ camera.set_image("away_blush")
            cho "Oh-okay..."
            cho "(You can do this... push your boundaries!)"
            cho "He-here I go..."

            #Cho opens her mouth and moves in towards genies cock #Genie cock twitches
            #She moves in closer and closes her eyes with her mouth wide open and just as she barely touches it she jumps back
            $ camera.set_image("cho_bj lick fail")
            pause 1 # Pauses at last frame.
            cho "No, I can't... I can't do it!"

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            if cho_bj_choice == "failed":
                cho "It still won't fit!"
                gen "[cho_name]... You're here to push your limits, stop with the whining!"
                $ camera.set_image("up_worried")
                cho "I-I'm sorry [cho_genie_name]..."
                cho "I... I can't...{w=0.4} It's all happening too fast!"
                gen "[cho_name]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away
                $ cho_mood += 3 # Annoyed that you failed it again, sucker
            else:
                cho "It won't fit!"
                gen "[cho_name]... You're here to push your limits."
                $ camera.set_image("up_worried")
                cho "I-I'm sorry [cho_genie_name]..."
                cho "I... need some time to think..."
                gen "[cho_name]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away

            # Genie standing with his dick out, all alone, blue balled, all aloooooooone
            call gen_chibi("dick_out", 230, "base")
            show screen chair_left
            show screen desk

            hide screen animatedCG
            with fade

            #Cuts to Office and Cho walks quickly out of the room
            call cho_walk(action="leave")

            m "(Damn...{w=0.4} Am I that type of coach that keep pushing their pupils too hard?)"
            m "(Speaking of hard, this thing isn't going to go away by itself...)"
            m "(Well... if there's anything I got good at in that lamp...)"
            if cho_bj_choice == "failed":
                m "(Perhaps I should go a bit more easy on her next time...)"

            $ cc_pf_blowjob.fail()
            $ cho_bj_choice = "failed"

            call gen_chibi("sit_behind_desk")
            hide screen chair_left
            hide screen desk
            with fade

            jump end_cho_event

        "-Take it slow...-": #Cho strokes and licks genie then goes back to stroking until climax
            gen "Okay... just keep stroking it for now..."

            if cho_bj_choice == None:
                $ camera.set_imagepath("cho_bj/hj/")
                $ camera.set_image("up_wide")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it!"
                $ camera.set_image("mid")
            else:
                $ camera.set_imagepath("cho_bj/kneel/")
                $ camera.set_image("up")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it, show me that stamina of yours!" #Should I use a different word than stamina? Works well I think.
                $ camera.set_image("mid")

            cho "Of course!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("mid_blush")
            cho "(I'll show you my stamina, alright!)" #Blushing

            $ camera.set_image("cho_hj mid")

            call ctc

            gen "*Ah*...{w=0.3} That's it... you're finally getting the hang of this."
            gen "You should've told me Quidditch players were this good at handjobs sooner."

            $ camera.set_image("cho_hj up blush")
            cho "..." #Looks up at genie #Blushes

            call ctc

            gen "And... look at you... stroking your coach's cock..."

            $ camera.set_image("cho_hj mid blush")

            cho "..."#Looks back down at cock #still stroking

            call ctc

            gen "Willing to do anything to win that cup..."

            $ camera.set_image("cho_hj mid")

            gen "Begging to receive her coach's cum."
            gen "Now, put your mouth on it [cho_name]..."
            $ camera.set_image("up_wide")
            #Cho stops handjob
            cho "But I thought..."
            gen "If you want to outdo your competition you need to push through your limits [cho_name]..."
            $ camera.set_image("up_worried")
            gen "Give it a little lick, I promise it won't bite."
            cho "..." #Annoyed
            $ camera.set_image("away_blush")
            cho "Fine..." #Blushes #Annoyed
            $ camera.set_image("cho_bj lick success")
            pause 1.5
            gen "See? That wasn't bad, was it?"
            $ camera.set_image("up_annoyed")
            cho "I--..." # Grim look at Genie
            $ camera.set_image("mid")
            cho "(I guess not...)" #Looks back on cock
            gen "Go on..."
            $ camera.set_image("mid_annoyed")
            cho "Fine!" #annoyed
            $ camera.set_image("mid_worried")
            cho "..." #Worried
            $ camera.set_image("cho_bj lick start")
            pause .7
            $ camera.set_image("cho_bj lick")
            cho "*lick-slurp-lick*"

            call ctc

            gen "*Ah* Good job [cho_name]..."
            gen "I suppose that will be enough for n--"
            $ camera.set_image("up_annoyed", trans=d3)
            cho "No! I want--"
            $ camera.set_image("away_blush")
            cho "I mean... {w=0.5} you deserve your reward [cho_genie_name]."
            cho "At least let me finish you off with my hand..."
            $ camera.set_image("mid_blush")
            gen "That's what I wanted to hear [cho_name], you're learning..."
            gen "Get going then..."

            $ camera.set_image("cho_hj mid blush")

            call ctc

            gen "*Hmm*... That's it, grip it firmly just like that..."

            call ctc

            gen "*Ah*...{w=0.4} Not bad... Not bad at all..."
            gen "Now... a little bit faster [cho_name]..."
            gen "I think you too deserve a reward..."

            $ camera.set_image("cho_hj mid blush fast")

            cho "Okay..." #Blush

            $ camera.set_image("cho_hj up blush")
            cho "[cho_genie_name]... Will you tell me when--"
            gen "Faster [cho_name]!"
            cho "Oh... of course!"

            $ camera.set_image("cho_hj mid blush fast")
            call ctc

            gen "(Now that's my [cho_name]!)"
            gen "(I'm at my limit, should I warn her?)"

            menu:
                "-Warn her-":
                    $ warned_her = True

                    gen "That's it, almost there...!"

                    call ctc

                    gen "Get ready for your reward [cho_name]!"
                    menu:
                        "-Cum on her face-":
                            $ camera.set(zoom=0.45, pos=(150, 70), t=2.0)
                            gen "*ARGH*!"

                            with vpunch
                            $ camera.set_image("cho_hj cum face")
                            pause 1.42
                            $ camera.set_image("cum") # Still image

                            call ctc

                            gen "*Ah*..."
                            cho "Are...{w=0.5} are you done?"
                            gen "*Ah*...{w=0.4} yes, you can open your eyes now..."

                            $ camera.set_image("cum_eye")

                            cho "..." #Opens eyes

                            $ camera.set_image("cum_eye_blush")

                            cho "So...{w=0.4} much..." #blush

                            $ camera.set_imagepath("cho_bj/kneel/")
                            $ camera.set_image("cum_eye")

                            #Cho takes hand off penis and puts to her side
                            cho "And so sticky..." #blush

                            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)

                            # Set cum on doll
                            $ cho.set_cum(face="heavy", hair="light")

                        "-Cum on her tits-":
                            gen "Get back a little, quick!"

                            $ camera.set_image("away", trans=d3)
                            $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)

                            gen "*ARGH!* Here it comes, you slut!"

                            with vpunch
                            $ camera.set_image("cho_hj cum tits")

                            pause 2
                            $ camera.set_image("cum_tits")

                            call ctc

                            gen "*Ah*..."

                            $ camera.set_image("look_cum_tits")

                            cho "You..." #Looks down on breasts
                            cho "My breasts..."

                            $ camera.set_image("look_blush_cum_tits")

                            cho "So much..." #blush

                            gen "That...{w=0.4} was...{w=0.4} amazing!"
                            gen "That is some talent you have there [cho_name]..."

                            $ camera.set_image("dreamy_cum_tits")

                            cho "...{heart}{heart}" #blush #looking at penis
                            gen "[cho_name]?"

                            $ camera.set_image("dreamy_up_cum_tits")

                            cho "Oh... Thank you [cho_genie_name]." #looks up at genie
                            gen "Now, get on your feet and let me have a proper look at you..."

                            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)
                            #Cuts back to office screen  (sound of cloth etc as genie puts dick away and Cho moves)
                            # Set cum on doll
                            $ cho.set_cum(breasts="heavy")

                "-Don't-":
                    $ warned_her = False
                    $ cho_mood += 4

                    gen "(You better be ready slut...)"

                    $ camera.set_image("cho_hj up blush")

                    cho "[cho_genie_name], are you about to--"

                    gen "*ARGH*!"

                    $ camera.set_image("cho_hj mid")
                    $ camera.set(zoom=0.45, pos=(150, 70), t=2.0)
                    cho "*huh*?!" #Wide eyed

                    with vpunch
                    $ camera.set_image("cho_hj cum face tits")
                    pause 0.9
                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("cum_face_tits")

                    call ctc

                    gen "*Ah*..."
                    cho "..." # Wide eyed
                    cho "M-{w=0.3}my face!" #Angry
                    cho "You just came on my face!"
                    gen "*Ahh* At last..."

                    $ camera.set_image("cum_face_tits_glance", trans=d3)

                    $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)

                    #Cuts back to office screen (sound of cloth etc as genie puts dick away and Cho moves)
                    # Set cum on doll
                    $ cho.set_cum(face="heavy", hair="light", breasts="heavy")

    hide screen animatedCG
    with fade

    # After CG, in the office.

    if warned_her:
        m "Well done [cho_name], you've started pushing those limits on your own."
        m "Also, You've got a little something right there..."
        call cho_main("Very funny [cho_genie_name]...", "clench", "narrow", "base", "mid", cheeks="blush", trans=d3)
        m "Your confidence is showing itself more and more every day."
        call cho_main("I... {w=0.5} You deserved it [cho_genie_name]...{w=0.5} for helping me this far...", "upset", "narrow", "base", "downR", cheeks="blush")
        call cho_main("For teaching me... all this stuff...", "angry", "closed", "base", "mid", cheeks="blush") #Blush
        m "(I'm a bloody saint I've waited that long...)"
        m "You're very welcome."
    else:
        gen "That...{w=0.4} was...{w=0.4} amazing!"
        call cho_main("Why didn't you warn me?!", "clench", "base", "angry", "down", trans=d3) #Angry
        call cho_main("My clothes are all ruined now too...", "angry", "closed", "angry", "mid")
        call cho_main("There's cum all over them!", "mad", "narrow", "angry", "down")
        call cho_main("I can't believe you just came all over me like that...", "annoyed", "base", "angry", "downR", cheeks="blush") #pout
        m "Should have put it in your mouth then..."
        call cho_main("...", "disgust", "narrow", "base", "mid", cheeks="blush") #pout

    call cho_main("Is this what you do to Hermione as well?", "upset", "narrow", "base", "down", cheeks="blush")

    if hg_kiss.trigger:
        m "Maybe."
        call cho_main("I knew it...", "smile", "wide", "base", "mid", cheeks="blush")
        m "Miss Granger knows how to properly dispose--"
        call cho_main("She swallows?!?", "clench", "wide", "base", "mid", cheeks="blush") #Shocked #Big text
        call cho_main("I mean...", "disgust", "base", "base", "downR", cheeks="blush")
        call cho_main("Of course she does...", "angry", "base", "base", "down", cheeks="blush") #small text #Blush
    else:
        m "Of course not..."
        call cho_main("I knew--", "smile", "happyCl", "base", "mid", cheeks="blush")
        call cho_main("Wait, she doesn't do stuff like that?", "clench", "narrow", "base", "mid", cheeks="blush")
        m "No."
        call cho_main("So I am your first?", "smile", "narrow", "base", "downR", cheeks="blush") # blush
        m "In one way or the other."
        call cho_main("What's that supposed to mean?!", "upset", "base", "angry", "mid", cheeks="blush") # angry
        call cho_main("Whatever...", "annoyed", "base", "angry", "R", cheeks="blush") # pout

    call cho_main("Are you...{w=0.4} Are we done?", "open", "narrow", "base", "downR", cheeks="blush") #Blush
    m "Yes, for now..."

    if game.daytime:
        call cho_main("Alright... In that case I better head back to class.", "open", "base", "base", "R")
    else:
        call cho_main("Alright... I'll head off to bed then.", "open", "base", "base", "R")
    m "Until next time."

    call cho_walk(action="leave")

    m "[cho_name]!"
    m "......"
    m "(Probably should've asked her to clean herself first...)"
    m "(Oh well, she'll find out one way or another.)"

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E2:
    m "Ready for an oral exam [cho_name]?"
    call cho_main("A what?", "open", "base", "raised", "mid")
    m "Time to put that mouth to good use..."
    call cho_main("My mouth to--", "horny", "base", "base", "downR", cheeks="heavy_blush") #Blush
    m "Any problems?"
    call cho_main("No... of course not [cho_genie_name]...", "normal", "base", "base", "mid", cheeks="blush")
    m "Excellent!"
    call cho_main("Just...{w=0.4} tell me what to do [cho_genie_name]...", "open", "base", "base", "R", cheeks="blush")

    call cho_walk("desk_close", "base")
    pause 1.0

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    # Note: Cho does not require posing here because it happens during the CG scene.

    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("mid")
    if game.daytime:
        $ camera.set_overlay("day_overlay")
    else:
        $ camera.set_overlay("night_overlay")
    $ camera.set(zoom=1.0, pos=(150, 400), initialize=True)
    show screen animatedCG
    with fade

    $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)

    gen "..."
    cho "..." #looking at dick
    gen "Go on then..."

    $ camera.set_image("mid_blush")

    cho "Of course..." #Blush
    #Cho puts hand on genies dick

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("mid_blush")

    gen "Just start with some stroking like you did before..."

    $ camera.set_image("up_blush")

    cho "Yes, [cho_genie_name]..."

    $ camera.set_image("cho_hj mid")

    call ctc

    gen "That's it... stroke your coach's cock..."
    gen "Good...{w=0.5} back and forth...{w=0.5} just like I taught you..."

    $ camera.set_image("cho_hj mid blush")

    cho "(He's so big...)" #Blushes

    gen "Very good... Now take that shirt off for me will you..."

    $ camera.set_image("away_blush")

    cho "Okay..." #Blushes #moves back to base position
    #Takes off shirt

    call play_sound("cloth")
    $ camera.set_image("topless_mid", trans=Fade(0.5, 2.0, 0.5))

    gen "Excellent... Now continue stroking, [cho_name]."

    $ camera.set_image("topless_up")

    cho "Alright..."
    #Resumes handjob

    $ camera.set_image("cho_hj topless mid")

    call ctc

    cho "......."
    cho "(I'm actually doing this...)"
    cho "(I'm stroking my coach's hard cock, just so I can win the quidditch cup...)"
    cho "(But...{w=0.4} If this is what it takes...{w=0.3} Then so be it!)"
    cho "(It won't be long until I have that cup in my hands...)"

    $ camera.set_image("cho_hj topless mid smile")

    cho "(I can already taste the victory!)"

    gen "You're being awfully quiet [cho_name]... it's very unlike you..."

    $ camera.set_image("topless_away_blush")

    cho "S-Sorry [cho_genie_name]..."

    $ camera.set_image("topless_up_worried")

    cho "It's just...{w=0.4} I just keep thinking...{w=0.4} how without your help I would've been out of the competition by now..."
    gen "(And without your help I'd be sitting here with a limp dick right about now.)"

    $ camera.set_image("topless_away_blush")

    cho "I...{w=0.4} I'm sorry I doubted your methods at first [cho_genie_name]..."
    gen "I knew you'd come around..."

    $ camera.set_image("topless_up_blush")

    cho "{heart}"

    $ camera.set_image("topless_mid_blush")

    cho "I'm just glad that there was some small way for me to repay you..." #looks at genies dick

    $ camera.set_image("cho_hj topless mid smile")

    gen "*Ah*... yes of course... It's nothing really."

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Oh please..."
    cho "Pleasuring you is little to nothing compared to what you've done for me so far..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "Giving you a bit of a reward is the least I could do..." #Blush

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "(*Argh*.. At this rate she'll make me bust!)"

    call ctc

    gen "Now you're getting into it..."
    gen "Speaking of...{w=0.2} Time to put that mouth to work..."

    $ camera.set_image("topless_up_worried")

    cho "Already?"
    gen "Not this again."
    gen "Didn't you say you wanted to {i}reward{/i} me a second ago?"

    $ camera.set_image("topless_away_blush")

    cho "Sorry, you're right [cho_genie_name]..."
    cho "Just...{w=0.4} Tell me what to do..." #blush

    $ camera.set_image("topless_mid")

    gen "Start by putting those lips around the tip, then slowly work your mouth further down the shaft..."

    $ camera.set_image("topless_up")

    cho "I...{w=0.4} Yes, [cho_genie_name]..." #Looks at genie

    $ camera.set_image("topless_mid_blush")

    cho "..." #blush
    cho "Here it goes..."

    #$ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck closed success")
    pause 5.1

    #Cho closes her eyes as she moves in, her mouth spreading open as she works it around the tip of genies penis
    #Once her mouth worked past the tip she pulls out and open her eyes, looking up at genie

    $ camera.set_image("topless_up")

    cho "How...{w=0.4} how was that [cho_genie_name]?"
    gen "Good start, but you shouldn't close your eyes... And keep going until you find your limit, then hold it there for a bit..."
    gen "The further down the better..."

    $ camera.set_image("topless_mid")

    cho "Okay..."

    $ camera.set_image("cho_bj topless suck closed fail")
    pause 0.5

    gen "Eyes open, [cho_name]..."

    $ camera.set_image("cho_bj topless suck closed fail exit")
    cho "Oh!{w=0.4} Sorry [cho_genie_name]!"

    $ camera.set_image("topless_up_blush")

    #Cho opens her eyes and looks at Genies penis."
    cho "I'll keep them open..." #small text

    $ camera.set_image("cho_bj topless suck start")
    pause 0.8
    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("topless_suck_up")

    cho "*Khow ish dhat*?"

    #Cho goes in again with her eyes open this time, her mouth spreading open as it slowly goes over the tip."
    #As her mouth continues past the tip she stops and looks up at genie for some approval but he stays silent, her eyes closes slightly as she resumes by slowly going down further
    gen "*Ah*... That's it...{w=0.5} Keep going, [cho_name]!" #This line should auto play as she goes further down
    #As she continues further down, her pupils move up a bit more until she hits her gag reflex (slow zoom in effect)
    #Quickly retracting she moves her head back and her eyes open again (Loop going backwards fast if animated, zoom effect quickly goes back to normal)

    $ camera.set_image("cho_bj topless suck medium up")
    call ctc
    $ camera.set_image("cho_bj topless suck closed exit")
    pause 3

    cho "*Gah*...{w=0.4}{nw}"

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_cough")

    cho "*Cough*{w=0.2} *Cough*"

    $ camera.set_image("topless_mid")

    gen "Easy there girl..."

    $ camera.set_image("topless_up")

    cho "Was...{w=0.4} Was that better, [cho_genie_name]?" #Cho looks up at genie
    gen "Excellent!{w=0.3} Although... maybe a bit too far... You barely held it there for a second."

    $ camera.set_image("topless_away_blush")

    cho "Oh... Yes, I thought it might've been..."
    gen "(This girl is like a on and off switch...)"
    gen "In any case... I think you got it..."
    gen "So... Let's get that head bobbing, [cho_name]!"

    $ camera.set_image("topless_away_pout")

    #Cho looks back down at dick
    cho "Are...{w=0.4} are you going to cum on me again [cho_genie_name]?"
    gen "I wouldn't worry about that yet... just focus on your task..."

    $ camera.set_image("topless_mid")

    cho "... {w=0.5}Okay then..."
    #Cho starts jerking genie off again

    $ camera.set_image("cho_hj topless mid")
    call ctc

    gen "You'll have to do more than just--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck start")
    cho "*oomph*{w=1.0}{nw}"
    $ camera.set_image("cho_bj topless suck")

    #Cho moves in and starts sucking genie off properly (Not as deep as she attempted)

    call ctc

    gen "That's more like it... work that tongue..."

    # Cho looks up
    $ camera.set_image("cho_bj topless suck medium up")
    call ctc

    gen "Fuck yes... you naughty girl..."

    #Cho pulls out and starts jerking genie off slowly
    $ camera.set_image("cho_bj topless suck closed exit")
    pause 3.0
    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("cho_hj topless up blush")
    call ctc

    cho "Am I doing it right, [cho_genie_name]?"
    gen "Yes, It feels--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless lick start")
    pause 0.65
    $ camera.set_image("cho_bj topless lick")

    #Cho starts licking the tip a couple of times #looking at dick
    gen "*Whoa*!"

    call ctc

    cho "(*huh*... This is just like quidditch, all I have to do is find a good tactic against him. {heart})" #looks up at genie still licking
    cho "(Guess he's not immune to his own tricks... {heart})"

    $ camera.set_image("cho_bj topless lick exit")
    pause 0.9
    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_up_blush")

    #Cho pulls back and smiles
    cho "I can't believe you're making your student suck your cock..."
    cho "Surely that's not something a coach should be doing..."
    gen "Well, I--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck start")
    pause 2.85
    $ camera.set_image("cho_bj topless suck medium up")

    #Blowjob starts again
    gen "(Fuck me, this girl is a natural!)"

    call ctc

    gen "You--{w=0.4} you're a fast learner [cho_name]..."

    $ camera.set_image("cho_bj topless suck deep")

    #Faster Blowjob
    cho "{heart}{heart}{heart}"

    gen "[cho_name], if you do that-- oh fuck!"

    menu:
        "-Warn her-":
            gen "[cho_name]... I think..."
            gen "There's....{w=0.5} one more thing...{w=0.5} I could teach you today..."

            $ camera.set_image("cho_bj topless suck medium up")
            cho ".............?"

            gen "Time to make your coach proud... Get ready!"

            call ctc

            menu:
                "\"I'll even give you some house points!\"":
                    $ cho_bj_choice = "points"
                    #Cho pulls back

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "(House points!?)" # angry #Wide eyed #Big text


                    $ camera.set_image("cho_bj topless suck closed exit")
                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    gen "{cps=5}Fuuuuuuuuu{/cps}--{w=0.5}{nw}"

                    with vpunch
                    $ camera.set_image("cho_hj topless cum face tits")
                    gen "Fuuuuuuuuu{fast}uck!"

                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_angry_cum_face_tits")

                    call ctc

                    show screen blkfade
                    with d5

                    cho "My eye!" #Big text
                    cho "I got some in my eye!" #Big text
                    gen "*Ah*...{w=0.4} Why'd you pull back!"

                    # Set cum on doll and strip her
                    $ cho.set_cum(face="heavy", hair="light", breasts="heavy")
                    $ cho.strip("robe", "top", "bra")

                    hide screen animatedCG
                    hide screen blkfade
                    with fade

                    #Office screen (Cho has cum on her face and tits)

                    call cho_main("\"House points\", really?!", "angry", "base", "angry", "mid", cheeks="blush", trans=d3)
                    call cho_main("You want me to swallow your semen for house points?!", "mad", "base", "angry", "mid", cheeks="blush")
                    m "The points were just going to be a bonus."
                    call cho_main("A bonus on top of?", "open", "base", "angry", "mid", cheeks="blush")
                    m "Not having to clean up..."
                    m "Although I guess you didn't see it that way since you--"
                    call cho_main("...", "clench", "closed", "angry", "mid", cheeks="blush") #Angry
                    m "Pulled...{w=0.5} back..."
                    call cho_main("I'm not selling my body for points!", "scream", "base", "angry", "mid", cheeks="blush")
                    m "Of course..."
                    call cho_main("I can't believe you...", "disgust", "base", "angry", "down", cheeks="blush") #Small text

                    call cho_walk("door", "base")

                    call cho_main("{size=-3}Who does he think I am?{w=0.4} I'm not Hermione!{/size}", "annoyed", "closed", "angry", "mid", cheeks="blush", flip=True, trans=d3)
                    m "[cho_name]."

                    call cho_chibi("stand", "door", flip=False)
                    call cho_main("I don't want to hear any of your excuses [cho_genie_name]!", "scream", "narrow", "angry", "mid", cheeks="blush", flip=False, trans=d3)
                    call cho_chibi("stand", "door", flip=True)
                    hide screen cho_main
                    with d5
                    m "At least let m--"

                    call cho_walk(action="leave")
                    $ renpy.play('sounds/door_down.mp3')
                    with hpunch

                    pause 1.0
                    m "..."
                    pause 0.5

                    call cho_walk(action="enter")
                    with d5

                    pause 1.0

                    m "Don't say I didn't try to--"
                    call cho_main("Shut... up!", "angry", "base", "angry", "mid", cheeks="blush", trans=d3)
                    $ renpy.sound.play("sounds/cloth_sound2.mp3")
                    $ cho.wear("all")
                    with fade

                    pause 1.0
                    call cho_walk("door", "base")
                    call cho_walk(action="leave")
                    $ renpy.play('sounds/door_down.mp3')
                    with hpunch

                    m "..."
                    m "(She'll get over it...)"
                    m "(I think.)"

                    $ cho_mood += 12

                "\"Taste that cum in your mouth!\"":
                    $ cho_bj_choice = "taste"

                    cho "(T-taste?! But... We never discussed this!)"

                    $ camera.set_image("cho_bj topless suck medium up")
                    cho "*Mhmmmm Mmhmmmm*!"

                    #Cho stops for a second to consider and then starts going again
                    call ctc

                    gen "*ah* That's it [cho_name]!"

                    $ camera.set_image("cho_bj topless suck closed")

                    cho "(Oh god...)" #blush
                    gen "Here it comes!"

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "(No, wait!)"
                    cho "*Mmmmmhmmm*!!!"
                    gen "{size=+4}*ARGH!*{/size}"

                    with vpunch
                    $ camera.set_image("cho_bj topless cum mouth")

                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    pause 2

                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_cum_mouth")

                    call ctc

                    $ camera.set_image("topless_mid_surprised_cum_mouth")

                    #Cho opens her mouth and lets the cum dribble out
                    cho "*sho*...{w=0.4} *sho mush*...."

                    $ camera.set_image("topless_away_blush_cum_mouth")

                    cho "(Although...{w=0.4} it doesn't taste as bad as I--)"
                    gen "Nicely done [cho_name], I knew you'd have it in you!"

                    # Make her lisp the name, if the name is unsupported fallback and replace 's' occurences with 'sh'
                    $ _replacement_names = {
                        "master": "mashter",
                        "daddy": "dhadhy",
                        "old man": "oldh mhan",
                        "professor": "phrofeshor",
                        "coach": "choach"
                        }

                    $ _name = cho_genie_name.replace(cho_genie_name, _replacement_names.get(cho_genie_name, cho_genie_name.replace("s", "sh")))

                    $ camera.set_image("topless_up_cum_mouth")

                    cho "*phank you, [_name]*"
                    gen "Didn't your parents teach you to not speak with your mouth full?"

                    $ camera.set_image("topless_away_blush_cum_mouth")

                    cho "............"
                    gen "Now, get on your feet so I can have a look at you..."

                    # Set cum on doll and strip her
                    $ cho.set_cum(face="light")
                    $ cho.strip("robe", "top", "bra")

                    hide screen animatedCG
                    with fade

                    # TODO: Add Cho doll flip when at door etc, cum layers
                    #Cho has no shirt, cum on her face and down her tits

                    m "Well, will look at that... You look great with a fresh coat of paint!"
                    call cho_main("Did you have to cum this much...", "disgust", "narrow", "base", "down", cheeks="blush", trans=d3)
                    m "I can't exactly control it..."
                    m "If you don't swallow, you'll have to deal with the mess."
                    call cho_main("Swallow [cho_genie_name]'s--", "upset", "base", "base", "downR", cheeks="blush") #Blush
                    call cho_main("I don't know...", "soft", "narrow", "base", "downR", cheeks="blush") #Blush
                    m "In any case, you've excelled today [cho_name]."
                    call cho_main("I think I need to lie down for a bit...", "open", "narrow", "base", "down", cheeks="blush")
                    call cho_main("This was exhausting...{w=0.4} Even for me.", "open", "narrow", "base", "mid", cheeks="blush")
                    if hg_kiss.trigger:
                        call cho_main("I don't know how Granger could do this for so long.", "soft", "narrow", "base", "down")
                        g9 "(*Heh*, practice makes perfect...)"

                    if game.daytime:
                        m "No time for a lie down I'm afraid..."
                        call cho_main("What, don't tell me you're already--", "clench", "wide", "base", "mid", cheeks="blush")
                        m "You've got class to get to."
                        call cho_main("Oh...{w=0.4} Right...", "open", "base", "base", "down", cheeks="blush")
                        call cho_main("Good day then...", "soft", "base", "base", "mid", cheeks="blush")
                    else:
                        m "A lie down you say..."
                        call cho_main("Don't you get any ideas...", "disgust", "narrow", "base", "mid", cheeks="blush")
                        m "I most certainly was not!"
                        call cho_main("Yeah right.", "annoyed", "base", "base", "R", cheeks="blush")
                        m "{size=-4}Pervert...{/size}"
                        m "Well, you've earnt a lie down I suppose..."
                        call cho_main("Good night then...", "open", "narrow", "base", "mid")
                        m "Good night, [cho_name]."

                    call cho_walk("mid", "base")
                    m "[cho_name]!"

                    call cho_chibi("stand", "mid", "base", flip=False)

                    call cho_main("Yes [cho_genie_name]?", "open", "base", "raised", "mid", trans=d3)
                    m "Your top..."
                    call cho_main("Oh... Of course!", "clench", "happyCl", "base", "mid", cheeks="blush") #Blush

                    $ renpy.sound.play("sounds/cloth_sound2.mp3")
                    $ cho.wear("all")
                    with fade

                    call cho_main("...", "soft", "base", "base", "down", cheeks="blush") #Cho puts on top
                    call cho_main("Thank you, [cho_genie_name]...", "open", "base", "base", "downR", cheeks="blush")

                    call cho_walk(action="leave")

                    m "...{w=0.5}Silly girl."
                    #Cho leaves
                    #End Scene #Marks at completed

                "\"Swallow that cum!\"":
                    $ cho_bj_choice = "swallow"

                    $ camera.set_image("cho_bj topless suck closed exit")
                    pause 3
                    $ camera.set_imagepath("cho_bj/hj/")
                    $ camera.set_image("topless_up_cringe")

                    #Cho's eyes goes wide and pulls out
                    cho "But [cho_genie_name]--" #Big text
                    gen "*argh*! Get back there at once or forget about your stupid quidditch cup!"

                    $ camera.set_image("topless_away_pout")

                    cho "Y-yes, sir!"
                    $ camera.set_image("topless_mid_angry")
                    cho "(I'll show this stupid cock... You're not the boss of me!)"

                    $ camera.set_imagepath("cho_bj/bj/")
                    $ camera.set_image("cho_bj topless suck deep start")
                    pause 2.0
                    $ camera.set_image("cho_bj topless suck deep")

                    gen "Yeeees, you fucking slut!"
                    cho "*Mmmmhh* {heart}{heart}"

                    call ctc

                    gen "Get ready, I'm almost..."

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "*mhmhm*?!-- (Now?!--)"

                    gen "{size=+4}*ARGH*!{/size}"

                    with vpunch
                    $ camera.set_image("cho_bj topless cum swallow")
                    pause 1
                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    pause 1
                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_cum_swallow")

                    call ctc

                    $ camera.set_image("topless_mid_surprised_cum_swallow")

                    cho "I...{w=0.4} I just swallowed..."
                    cho "My coach's cum..."
                    gen "Well done, [cho_name], you sucked me dry."

                    $ camera.set_image("topless_away_cum_swallow")

                    cho "I...{w=0.4} Thanks... I guess."

                    # Strip doll (no cum necessary it seems)
                    $ cho.strip("top", "bra", "robe")

                    hide screen animatedCG
                    with fade

                    g9 "Now this is the kind of initiative I'm talking about!"
                    call cho_main("...", "disgust", "narrow", "base", "down", cheeks="blush", trans=d3) #blank stare
                    m "[cho_name]?"
                    call cho_main("Yes...{w=0.5} sorry...{w=0.5} thank you [cho_genie_name].", "angry", "base", "base", "downR", cheeks="blush")
                    call cho_main("Is that all?", "soft", "narrow", "base", "down", cheeks="blush")
                    if game.daytime:
                        m "That will be all for today..."
                    else:
                        m "That will be all for tonight..."
                    call cho_main("Okay, good...", "angry", "narrow", "base", "down", cheeks="blush")
                    #Cho walks out of door still without shirt on
                    call cho_walk(action="leave")
                    m "[cho_name]!"
                    #Cho comes back through the door
                    call cho_walk(action="enter")
                    with d5

                    call cho_main("Yes [cho_genie_name]?", "soft", "base", "base", "mid", cheeks="blush", trans=d3)
                    m "..."
                    call cho_main("Oh, of course!", "clench", "base", "base", "down", cheeks="blush") #Wide eyed

                    #Cho puts on her shirt
                    $ renpy.sound.play("sounds/cloth_sound2.mp3")
                    $ cho.wear("all")
                    with fade

                    if game.daytime:
                        call cho_main("Bye then!", "open", "happyCl", "base", "downR", cheeks="blush")
                    else:
                        call cho_main("Good night then!", "base", "base", "base", "mid")

                    call cho_walk(action="leave")

                    m "(Heh. She's silly... but adorable.)"
                    m "(Not the worst of combinations.)"
                    #Cho leaves
                    #End Scene #Marks at completed

        "-Just cum down her throat-":
            $ cho_bj_choice = "throat"
            gen "That did it, you slut!"

            $ camera.set_image("cho_bj topless suck medium up")

            cho "*Hmmf*?" #looks at genie
            gen "{size=+4}*ARGH*!{/size}"

            with vpunch
            $ camera.set_image("cho_bj topless cum swallow")

            cho "*Mphhhh*!!!{w=1.0}{nw}"

            $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)

            gen "*Ahhh* I needed that..."

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("topless_mid_cough_cum_swallow")

            cho "*Cough*-*Cough*-...*Ah*...{w=0.4}*Ah*..."
            gen "That was awesome... great job--"

            $ camera.set_image("topless_up_angry_cum_swallow")

            cho "What...{w=0.4} the hell...{w=0.4} is wrong with you?!?!" #screen shake
            gen "What do you--"

            $ camera.set_image("topless_up_angry2_cum_swallow")

            cho "Why didn't you warn me! I almost choked!"
            cho "I never agreed to this--"
            gen "It's sort of expected with a blowjob..."

            $ camera.set_image("topless_closed_angry_cum_swallow")

            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0)

            cho "You asshole!"

            show screen blkfade
            with d5

            cho "For a first blowjob?! It is not!"
            gen "I mean...{w=0.4} wait did you say first... does that mean you still want to do--"
            $ cho.wear("all")
            $ renpy.sound.play("sounds/cloth_sound2.mp3")
            cho "I can't believe you..."

            hide screen animatedCG
            hide screen blkfade
            with fade

            #Cut to office screen #Cho has put on her top
            m "As I said, it's kind of expected from the whole blowjob thing..."
            call cho_main("You...{w=0.4} you're joking right?", "clench", "narrow", "angry", "mid", cheeks="blush", trans=d3)
            m "Deadly serious..."
            m "Unless I fancy covering your face that is..."
            call cho_main("Unless you--", "soft", "wide", "angry", "mid", cheeks="blush") #disgust
            call cho_main("*Humph*!", "upset", "base", "angry", "mid", cheeks="blush")

            # Gets upset
            $ cho_mood += 12

            call cho_main("I'm going to go take a shower now if you don't mind!", "mad", "base", "angry", "mid", cheeks="blush")
            m "You're dismissed [cho_name]."
            call cho_main("Good!", "annoyed", "base", "angry", "mid", cheeks="blush")
            call cho_walk("door", "base")
            call cho_main("{size=-4}Seriously... just ask first...{/size}", "disgust", "base", "angry", "down", cheeks="heavy_blush", flip=True, trans=d3) #Small text #Pout #Blush

            call cho_walk(action="leave")

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E3:
    m "Let's see what that mouth can do."
    call cho_main("You want to...{w=0.4} use my mouth again [cho_genie_name]?", "soft", "narrow", "base", "downR", cheeks="blush")
    call cho_main("I guess I could...", "open", "narrow", "base", "down", cheeks="blush") #Blush #Horny

    if cho_bj_choice == "points":
        m "And this time I won't make the mistake of offering house points..."
        call cho_main("You better not.", "annoyed", "narrow", "base", "downR", cheeks="blush")
        m "But my expectations are still the same..."
        m "For you to push your limits on your own..."
        call cho_main("So you want me to...", "soft", "base", "base", "downR", cheeks="blush")
    elif cho_bj_choice == "taste":
        m "And if you don't want those clothes dirty you better swallow this time..."
        call cho_main("...", "annoyed", "narrow", "base", "downR", cheeks="blush") #blush
    elif cho_bj_choice == "swallow":
        call cho_main("You expect me to swallow again?", "open", "base", "base", "downR", cheeks="blush")
        m "Of course, that's part of the deal..."
    else: # cho_bj_choice == throat - Using `else` as a fallback for degenerates that use cheats
        call cho_main("Will you warn me this time?", "annoyed", "narrow", "base", "downR", cheeks="blush")
        m "Of course..."

    call cho_main("Fine...", "base", "narrow", "base", "R", cheeks="blush")
    m "Good! And one more thing..."
    m "I expect some dirty talk this time."
    call cho_main("Dirty talk, [cho_genie_name]?", "upset", "base", "raised", "mid", cheeks="blush") #pout
    call cho_main("I... If that's what you want...", "soft", "base", "base", "downR", cheeks="blush") #Blush
    m "Good, then get over here..."

    call cho_walk("desk_close", "base")
    pause 1.0

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("mid")
    if game.daytime:
        $ camera.set_overlay("day_overlay")
    else:
        $ camera.set_overlay("night_overlay")
    $ camera.set(zoom=0.5, pos=(100, 100), initialize=True)

    show screen animatedCG
    with fade

    pause 1

    $ camera.set_image("up_neutral")

    cho "Did you want me to take my top off again [cho_genie_name]?"
    gen "Taking initiative, *huh*? I like it."

    $ camera.set_image("up_smile")

    cho "In that case...{w=0.4} Just relax [cho_genie_name] and I'll take care of you..."

    call play_sound("cloth")
    $ camera.set_image("topless_mid_dreamy", trans=Fade(0.5, 2.0, 0.5))

    #Cho moves up closer
    cho "..."
    cho "Your--... your cock is so big [cho_genie_name]!"
    gen "That's it [cho_name], keep talking just like that..."
    gen "Put your hand on it and tell me how it feels..."

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_mid_dreamy")

    #Cho grabs genies dick
    cho "It...{w=0.4} it feels like I'm holding a beater's bat!"
    cho "I can't believe how hard it is..."

    #Cho starts jacking genie off #Looking at dick
    $ camera.set_image("cho_hj topless mid smile")

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Do you like it when I stroke your cock, [cho_genie_name]?" #Looks at genie
    gen "Very much so!"
    cho "*Mhmmm* Good answer. {heart}"

    $ camera.set_image("cho_hj topless mid smile")

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Although this is far too slow, let's pick up the pace a little..."#Looks at genie

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "*Ahh* You make me proud, [cho_name]...{w=0.3} I've taught you well."

    $ camera.set_image("cho_hj topless up blush")

    cho "Thank you, [cho_genie_name]... it's my pleasure. {heart}" #Worried #Looks at dick

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "*Ahh*...{w=0.3} Pleasure's all mine, [cho_name]."

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "You've been such a help to me, [cho_genie_name]."

    $ camera.set_image("cho_hj topless up blush")
    cho "I would never have been able to get this far without you..."

    gen "That's it, [cho_name], keep talking..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "I love how your cock barely fits in my hand..."
    cho "And the feeling as it goes in and out of my mouth..."

    $ camera.set_image("cho_hj topless up blush")

    cho "And when it twitches happily... It makes me glad, knowing I am making you feel good..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "The look of pleasure on your face once you cum in my mouth..."
    if cho_bj_choice in ("swallow", "throat"):
        cho "The sensation of your jizz going down my throat is so..." #Looks at dick

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "addicting! {heart}{heart}"
    elif cho_bj_choice == "points":
        cho "To finally feel your jizz slide down my throat, I..."

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "can't wait! {heart}{heart}"

    else:
        cho "And the taste of your jizz is so..."

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "delicious! {heart}{heart}"

    gen "(If she keeps going like this, I'll blow before an actual blowjob...)"

    $ camera.set_image("topless_up_blush2")

    cho "Will you let me put my lips around it now, [cho_genie_name]?" #Looks at genie
    gen "Perhaps..."

    $ camera.set_image("topless_up_worried")

    cho "... Perhaps?"  #Looks at genie
    gen "Tell me you want it..."

    $ camera.set_image("topless_up_blush2")

    cho "[cho_genie_name]?"
    gen "Tell me how badly you want-- no, how badly you {i}need{/i} cock in your mouth."

    $ camera.set_image("topless_up_cringe")

    cho "How badly I n-need...!?"

    $ camera.set_image("topless_away_pout")

    cho "......"
    cho "(I-I don't need his cock... I think...)"

    $ camera.set_image("topless_away_blush")

    cho "(But...)"

    $ camera.set_image("topless_mid_dreamy")

    cho "(*Ah* {heart}{heart}{heart})"
    gen "Well then?"

    $ camera.set_image("topless_up_wide")

    #Cho stops stroking but still holding genies cock #looking at cock
    cho "I...{w=0.4} I want..."

    $ camera.set_image("topless_away_blush")

    cho "I need..."

    $ camera.set_image("topless_mid_dreamy")

    gen "Go on..."

    $ camera.set_image("topless_up_blush2")

    cho "I need your cock in my mouth...{w=0.2} and I need to feel your cum going down my throat..."
    gen "(She sure is a quick learner...)"
    gen "That's it [cho_name]... Now work that mouth of yours for your reward..."

    $ camera.set_image("topless_mid_dreamy")

    cho "*Ah* Thank you, [cho_genie_name]..." #Blushes

    $ camera.set_image("cho_bj topless suck medium start")
    pause 2
    $ camera.set_image("cho_bj topless suck medium")

    call ctc

    gen "*Mhm*... Suck that cock like it's the only thing between you and winning that cup..."
    #Cho looks up at genie as she's sucking and starts going faster.

    $ camera.set_image("cho_bj topless suck medium up")

    gen "Your [cho_genie_name] will soon reward you for all of your efforts..."

    $ camera.set_image("cho_bj topless suck deep")

    cho "*glick* *glick* *glick*" #Looks back down on cock
    gen "*Argh* You slut, I'm almost there..."

    call ctc

    $ camera.set_image("cho_bj topless suck closed exit")
    gen "What--{w=1.0}{nw}"
    pause 2.0

    #Cho suddenly pulls out
    $ camera.set_image("cho_hj topless up")

    gen "I didn't say you could--"
    cho "Cum for me [cho_genie_name]!"

    $ camera.set_image("cho_hj topless up blush")

    cho "I need to taste your delicious cum down my throat!"
    cho "I need to swallow it all!"

    $ camera.set_image("cho_bj topless suck deep start")
    pause 1
    $ camera.set_image("cho_bj topless suck deep")

    call ctc

    gen "That's it [cho_name], get ready for your reward."

    $ camera.set_image("cho_bj topless suck medium")

    call ctc

    $ camera.set_image("cho_bj topless suck medium up")

    gen "Open up [cho_name], here it comes!" #large text
    gen "*ARGH!*"

    with vpunch
    $ camera.set_image("cho_bj topless cum mouth")
    pause 0.5
    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
    pause 1.5
    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("topless_mid_cum_mouth")

    pause 1

    gen "*Ah*..." #Genie pulls out

    call ctc

    $ camera.set_image("topless_mid_full_worried2")

    gen "Don't swallow yet!"

    cho "*Mfff*..." #Mouth full
    gen "Good... Now play with it with your tongue."

    $ camera.set_image("topless_mid_full_worried")
    cho "....{w}......{w}....."
    gen "Now you can swallow."
    pause 1

    $ camera.set_image("topless_mid_full_angry")

    pause 1
    call play_sound("gulp")
    $ camera.set_image("topless_mid_full_swallowed2", trans=d5)
    pause 1.5
    $ camera.set_image("topless_mid_full_swallowed")

    gen "I hope you liked your reward."
    gen "Now... On your feet, [cho_name]."

    $ camera.set(zoom=1.0, pos=(300, 400), t=5.0, pause=True)

    # Set cum on doll and strip her
    $ cho.set_cum(face="light")
    $ cho.strip("robe", "top", "bra")

    hide screen animatedCG
    with fade

    if cho_bj_choice in ("taste", "points"):
        call cho_main("I...{w=0.4} I did it...{w=0.4} I swallowed your cum [cho_genie_name].", "base", "happyCl", "base", "mid", cheeks="blush", trans=d3)
        m "As expected."
        m "But an improvement from last time nevertheless..."
        call cho_main("Thank you [cho_genie_name]...", "base", "narrow", "base", "down", cheeks="blush")
    elif cho_bj_choice == "swallow":
        call cho_main("I...{w=0.4} I hope you liked it [cho_genie_name].", "base", "narrow", "base", "down", cheeks="blush", trans=d3)
    else: # cho_bj_choice == throat - Using `else` as a fallback for degenerates that use cheats
        call cho_main("I...{w=0.4} I did it...", "base", "narrow", "base", "down", cheeks="blush", trans=d3)
        m "And without my help this time."

    call cho_main("Your...{w=0.4} Your cum...{w=0.4} was delicious [cho_genie_name]...", "soft", "closed", "base", "mid", cheeks="blush")
    g9 "That's right [cho_name]... and if you keep doing such a good job there's even more where that came from..."
    m "You can stop talking dirty now."
    call cho_main("I wasn't--", "open", "narrow", "base", "down", cheeks="heavy_blush") #blush, looking right
    call cho_main("Yes, [cho_genie_name]...", "upset", "narrow", "base", "R", cheeks="heavy_blush")
    call cho_main("So... Is that all?", "soft", "narrow", "base", "R", cheeks="blush")
    m "For now..."
    call cho_main("Okay then...", "soft", "base", "base", "mid", cheeks="blush")

    $ renpy.sound.play("sounds/cloth_sound2.mp3")
    $ cho.wear("all")
    $ cho.set_cum(None)
    with fade

    if game.daytime:
        call cho_main("In that case I'll head back to class.", "open", "base", "base", "R", cheeks="blush")
    else:
        call cho_main("I'll head back to my dorms then...", "base", "base", "base", "mid")
    m "Of course...{w=0.4} you better be ready for next time..."
    call cho_main("Next...{w=0.4} yes [cho_genie_name]...", "horny", "narrow", "base", "down", cheeks="blush")
    call cho_walk("door", "base")
    call cho_main("(He's so commanding...)", "horny", "narrow", "base", "R", cheeks="heavy_blush", flip=True, trans=d3) # horny
    call cho_main("(No wonder Hermione enjoys it so much...)", "horny", "closed", "base", "mid", cheeks="heavy_blush")
    m "[cho_name]."

    call cho_chibi("stand", "door", "base", flip=False)
    call cho_main(flip=False, trans=d5)

    call cho_main("Yes... sorry!", "mad", "base", "base", "L", cheeks="heavy_blush") #Heavy Blush
    call cho_main("Bye then!", "soft", "happyCl", "base", "mid", cheeks="heavy_blush") #Heavy Blush

    call cho_walk(action="leave")

    pause 1

    m "Turns out I'm a better coach than I gave myself credit for."
    g9 "Time for the next step!"

    jump end_cc_pf_blowjob
