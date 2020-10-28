transform crop_meter(fill, opacity):
    transform_anchor True
    on show, appear, start:
        alpha opacity
        yanchor 1.0
        yzoom -1.0
        easein_back 1.0 crop (0, 0, 60, int((float(fill)/100)*500))
        repeat

label exp_o_meter(fill=50, opacity=1.0, alt=False, alt_text=None):
    show screen exp_o_meter(fill=fill, opacity=opacity, alt=alt, alt_text=alt_text)
    #with d3
    return

screen exp_o_meter(fill, opacity, alt, alt_text):
    tag exp_o_meter
    zorder 30

    frame:
        style "empty"
        xpos 50
        ypos 570

        add gui.format("interface/meter/{}/meter.webp") yanchor 1.0 alpha opacity
        add "interface/meter/fill.webp" at crop_meter(fill, opacity)
        add "interface/meter/glass.webp" yanchor 1.0 alpha opacity

    if not alt:
        frame:
            style "empty"
            xpos 150
            ypos 70
            add gui.format("interface/meter/{}/circle.webp") alpha opacity
            if fill >= 90:
                add "interface/meter/100.webp" alpha opacity
            elif fill >= 50:
                add "interface/meter/50.webp" alpha opacity
            else:
                add "interface/meter/0.webp" alpha opacity

    if alt_text:
        text alt_text size 22 vertical True color "#FFF" outlines [ (2, "#000", 0, 0) ] xpos 70 ypos 340 yalign 0.5

screen swear_bubble(type):
    tag bubble
    zorder 30

    add "interface/meter/bubble/"+str(type)+".webp" ypos 100 xpos 100
    timer 1.0 action Hide("swear_bubble")



### Quidditch Quiz ###

label cho_quiz:
    call cho_main(xpos="mid",ypos="base", trans=fade)

    $ cho_quiz.correct_answers = 0
    if cho_quiz.checkpoint:
        m "I'm ready to show you what I know about Quidditch..."
        call cho_main("Great!", "base", "base", "base", "L")
        call cho_main("Let's begin...", "open", "wide", "raised", "mid")
        jump cho_quiz_checkpoint

    $ confidence_meter = 50
    call exp_o_meter(fill=confidence_meter, opacity=0.0)

    # Intro
    if not cho_quiz.E1_complete:
        $ cho_quiz.E1_complete = True
        m "It's time to start our first lesson, Miss Chang."
        call cho_main("Great, where do we begin?", "smile", "base", "base", "mid")
        m "Well, first we're going to have to discuss what you'll do for me in this arrangement of ours..."
        call cho_main("Oh, well... as I said, I'll do anything to win the cup!", "soft", "base", "base", "R")
        g9 "That's what I want to hear!"
        m "In that case, I'd like you to start selling favours to me for my service..."
        call cho_main("Favours? What kind of favours?", "annoyed", "narrow", "raised", "mid")
        m "Nothing that Miss Granger hasn't had any issues with."

        if her_reputation < 16:
            call cho_main("(So nothing sexual, at the very least...)", "grin", "base", "base", "R")
        else:
            call cho_main("(I hope it's nothing sexual. I've heard some rumours about Granger...)", "quiver", "base", "worried", "R")

        call cho_main("Well... if Granger could do it, so can I!", "open", "closed", "base", "mid")
        call cho_main("And better!", "soft", "narrow", "base", "mid")
        m "Great!"
        call cho_main("And longer!", "smile", "narrow", "base", "mid")
        m "Longer?"
        call cho_main("And harder!", "angry", "narrow", "angry", "mid", trans=hpunch)
        m "(Oh my...)"
        call cho_main("But...", "soft", "closed", "base", "mid")
        m "Yes?"
        call cho_main("I'll only do it if we actually win!", "soft", "narrow", "raised", "mid")
        m "..."
        g4 "(Damn it! Always a catch...)"
        m "Fine..."
        m "Okay, so...{w} I'll help you win quidditch matches, and in return, you'll sell me favours..."
        m "Sounds good?"
        call cho_main("Yes, that's the deal.", "smile", "base", "base", "mid")
        call cho_main("Although...", "annoyed", "base", "worried", "down")
        m "Although?"
        call cho_main("Well, how do I know that you actually know anything about the game?", "open", "base", "base", "mid")
        call cho_main("I mean...{w} I never really saw you showing too much interest before...", "soft", "narrow", "base", "mid")
        m "About what?"
        call cho_main("Quidditch!", "angry", "closed", "angry", "mid", trans=hpunch)
        g9 "Ah, yes... Quidditch.{w} It's like the Wizards version of Basketball, right?"
        call cho_main("Basketball?!", "clench", "base", "raised", "mid")
        call cho_main("Is that the muggle sport nobody cares about?", "soft", "narrow", "raised", "L")
        g4 "Nobody cares?{w} What are you...{w} Haven't you seen \"Space Jam\"?"
        call cho_main("...", "annoyed", "base", "raised", "mid")
        g4 "Come on."
        m "Well..."

    # Repeat
    else:
        m "I'm ready to make my case on how Quidditch is a knock-off of basketball..."
        call cho_main("Really sir... again?", "open", "narrow", "angry", "L")
        m "Of course, it's an important subject for your education..."
        call cho_main("I can't really see how, but I'm sure you know what you're talking about...", "open", "base", "base", "mid")
        m "Alright, so..."

    $ renpy.music.play("music/ominous_music.mp3")
    $ renpy.music.stop("weather")

    call exp_o_meter(fill=confidence_meter)

    # Question 1
    menu:
        "-There's five players on each team...-":
            m "There's two teams with each one having five players on the court at one time..."
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            call cho_main("Whilst Quidditch does have two teams...{w=0.5} there's 7 players on each...", "annoyed", "narrow", "raised", "mid")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(1.0)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Ah,{w=0.4} well..."

        "-[cho_quiz.hint]At the start of the game the ball gets thrown in the air...-":
            $ cho_quiz.correct_answers += 1

            m "You start the game by the referee throwing the ball into the air..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.sound.play( "sounds/hmm1.mp3")
            $ renpy.block_rollback()
            call cho_main("I guess that's kind of similar...", "smile", "base", "raised", "mid")
            $ renpy.music.set_volume(1.0)
            g9 "It is? I mean, yes... and also..."


    # Question 2
    menu:
        "-It's played on a rectangular court...-":
            m "The game is played on a rectangular court..."
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            call cho_main("Well, that's not similar at all then. The Quidditch pitch is oval shaped...", "annoyed", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(1.0)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Of course!{w=0.4}... and in basketball..."

        "-[cho_quiz.hint]You may not go out of bounds with the ball...-":
            $ cho_quiz.correct_answers += 1

            m "You're not allowed outside the bounds whilst holding the ball or you'll have to hand it over to the opponent team..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            $ renpy.sound.play("sounds/hmm1.mp3")
            call cho_main("I guess that's pretty much the same as in Quidditch...", "base", "base", "raised", "L")
            $ renpy.music.set_volume(1.0)
            m "Great! I mean, obviously! And..."


    # Question 3
    menu:
        "-[cho_quiz.hint]Each player takes a certain position...-":
            $ cho_quiz.correct_answers += 1

            m "Each player takes a certain position."
            m "There are defensive positions..."
            m "And offensive positions..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            $ renpy.sound.play( "sounds/hmm2.mp3")
            call cho_main("I guess Quidditch has something like that...", "base", "narrow", "base", "R")
            $ renpy.music.set_volume(1.0)
            g9 "Exactly, which is obviously why I brought it up, and lastly..."

        "-You can't run with the ball unless you dribble or pass...-":
            m "You can't run whilst holding the ball,{w=0.4} you need to pass it or dribble..."
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            call cho_main("Well, you can move with the ball freely without passing in Quidditch, that's why we have the beaters...", "annoyed", "narrow", "raised", "mid")
            call cho_main("To make the opponents drop the ball.", "open", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(1.0)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Ah!{w=0.4} Well, I guess that is different... Lastly though..."


    # Question 4
    menu:
        "-You can't touch your opponent...-":
            m "You're not allowed to touch your opponent or it would be counted as a foul..."
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            call cho_main("Well, that's definitely not the case in Quidditch...", "open", "closed", "raised", "mid")
            call cho_main("Except for excessive use of elbows...", "annoyed", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Well...{w=0.4}"
            m "Fine..."

        "-[cho_quiz.hint]You score by getting the ball through a hoop...-":
            $ cho_quiz.correct_answers += 1

            m "The way you score is by getting the ball through a hoop."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            $ renpy.sound.play( "sounds/hmm3.mp3")
            call cho_main("*Hmm*... Well that's the same as in Quidditch I suppose.", "smile", "base", "base", "mid")
            g9 "Naturally..."


    pause 1.0
    hide screen exp_o_meter
    with d3

    $ renpy.music.set_volume(1.0)

    call play_music("cho")

    call weather_sound

    $ renpy.block_rollback()

    # Failed
    if cho_quiz.correct_answers <= 1: # 0-1 answers correct?
        m "Well, I'm sure that the winning conditions are pretty similar at least..."
        call cho_main("And what are the winning conditions?", "base", "base", "base", "mid")
        m "You win by having the most amount of points when the time is over."
        call cho_main("Well, in Quidditch the game doesn't end until the snitch is caught, so it could technically go on forever.", "open", "narrow", "raised", "mid")
        call cho_main("So in short... nothing like basketball.", "annoyed", "closed", "base")
        m "The game doesn't end until the snitch is caught?"
        call cho_main("Yes...", "base", "base", "base", "mid")
        m "Well, that is stupid..."
        call cho_main("Yes, that bit is kind of stupid...", "annoyed", "base", "worried", "down")
        call cho_main("Anyway...", "base", "closed", "base")
        call cho_main("I didn't come here to listen to you talk about about basketball...", "annoyed", "base", "base", "downR")
        m "Right..."
        call cho_main("I came for you to tutor me...", "annoyed", "narrow", "angry", "L")
        m "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)"
        g9 "Oh, well... look at the time!"
        call cho_main("What?", "open", "wide", "raised", "mid")
        g9 "You've made me go on about basketball for such a long time so we're already at the end of today's session."
        call cho_main("But we didn't even get to any tutoring...", "annoyed", "narrow", "base", "mid")
        m "We'll get there, don't you worry... next time..."
        call cho_main("...{w=0.4}Fine.", "annoyed", "base", "base", "mid")
        call cho_main("Bye then professor...", "annoyed", "base", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        g4 "(What am I supposed to do now... I clearly know fuck-all about Quidditch...)"
        m "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)"

        $ cho_quiz.lost = True

        if quidditchguide_ITEM.used:
            m "(Why didn't I just follow the book? Serves me right...)"
        elif quidditchguide_ITEM.owned > 0:
            m "(Maybe I should read that book they gave me...)"
        elif store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"


    # Success! Or did you?
    elif cho_quiz.correct_answers == 4:
        call exp_o_meter(fill=confidence_meter, opacity=0.0)
        m "So as you can see, Basketball and Quidditch are pretty much the same game..."
        call cho_main("I'm sure that can't be right...", "annoyed", "base", "base", "mid")
        call cho_main("I'll have to look up this \"Space Jamming\"...{w=1.0} thing.", "open", "narrow", "base", "mid")
        g9 "You should! It has Bugs Bunny in it!"
        call cho_main("And now you stopped making sense again...", "annoyed", "base", "raised", "L")
        call cho_main("Also I'm still quite unsure if you actually know Quidditch or are just trying to confuse me with Basketball terms...", "annoyed", "narrow", "raised", "mid")
        call exp_o_meter(fill=75)
        pause .3
        call bld
        g4 "(Fuck, she's onto me!)"
        g9 "Of course I'm not... I'll prove it to you!"
        call exp_o_meter(fill=50)
        pause .5
        call bld
        g4 "(Wait, why did I say that?)"
        call cho_main("...", "smile", "base", "raised", "mid")
        call cho_main("Okay then, show me what you know...", "smile", "base", "raised", "mid")

        jump cho_quiz_checkpoint

    # Failed
    else: # 2-3 answers correct.
        call cho_main("I guess it has some similarities...", "annoyed", "narrow", "worried", "mid")
        m "Pretty much the same game I'd say..."
        call cho_main("I wouldn't say that... You fly for one in quidditch...", "open", "base", "base", "mid")
        g4 "You do?!?"
        call cho_main("Very funny professor, of course you do...", "annoyed", "base", "raised", "down")
        call cho_main("Anyway, weren't you supposed to tutor me?...", "annoyed", "narrow", "base", "L")
        m "Oh, right..."
        m "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)"
        g9 "Oh, well... look at the time!"
        call cho_main("What?", "upset", "closed", "worried")
        g9 "You've made me go about basketball for such a long time so we're already at the end of today's session."
        call cho_main("But we didn't even get to any tutoring...", "annoyed", "narrow", "angry", "mid")
        m "We'll get there, don't you worry... next time..."
        call cho_main("...{w=0.4}Fine.", "annoyed", "narrow", "base", "mid")
        call cho_main("Bye then professor...", "annoyed", "base", "base", "R")

        # Cho leaves.
        call cho_walk(action="leave")

        g4 "(The fuck am I supposed to do now... I feel like that must've been a fluke, I know nothing about Quidditch..)."
        m "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)"

        $ cho_quiz.lost = True

        # Read the book.
        if quidditchguide_ITEM.used:
            m "(Why didn't I just follow the book?{w} Serves me right...)"

        # Got the book but not read.
        elif quidditchguide_ITEM.owned > 0:
            m "(Maybe I should read that book they gave me...)"

        # Visited their shop before.
        elif store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"

    $ cho_busy = True

    jump main_room



### Quiz - Part 2 ###

label cho_quiz_checkpoint:
    $ confidence_meter = 50
    call exp_o_meter(fill=confidence_meter, opacity=0.0)

    $ renpy.music.play("music/determined_pursuit_loop.mp3")
    $ renpy.music.stop("weather")

    # Intro
    if not cho_quiz.E2_complete:
        $ cho_quiz.E2_complete = True
        call cho_main("You do seem to know some basic things, but do you know anything about the balls?", "open", "narrow", "base", "mid")
        m "I could probably teach you quite a lot..."
        g9 "You should never neglect the balls."
        call cho_main("In that case...", "base", "base", "base", "mid")

    call cho_main("My position on the team is seeker, it is my job to catch the \"Blank\" to end the game and score our team 150 points.", "open", "base", "base", "L")
    call exp_o_meter(fill=confidence_meter)

    # Question 1
    menu:
        "-Stitch-":
            m "Stitch?"
            $ renpy.block_rollback()
            call cho_main("No...", "open", "narrow", "angry", "mid")
            g4 "Oh wait, that's that blue alien thing, isn't it?"
            call cho_main("I don't know what a stitch is, sorry sir...", "soft", "narrow", "worried", "R")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down")

        "-Lich-":
            m "Lich?"
            $ renpy.block_rollback()
            call cho_main("A Lich? Like those undead skeletal creatures?", "open", "narrow", "raised", "mid")
            g4 "Oh, that's what I said?"
            m "I must've had a PTSD flashback from my tomb raiding days..."
            call cho_main("You've been tomb raiding?", "soft", "base", "raised", "mid")
            m "..."
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            m "Of course not..."
            call cho_main("Next question...", "open", "base", "raised", "down")

        "-[cho_quiz.hint]Snitch-":
            m "Snitch?"
            $ renpy.block_rollback()
            $ renpy.sound.play( "sounds/gasp.mp3")
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            call cho_main("Yes!", "smile", "wide", "base", "mid")
            g9 "Well then, surely that should show you how superi--"
            call cho_main("Next question...", "open", "closed", "base", "down")
            $ cho_quiz.correct_answers += 1

    call cho_main("Apart from the Snitch there are two other types of balls on the pitch, what are they called?", "open", "base", "angry", "mid")

    # Question 2
    menu:
        "-Butter and Waffles-":
            m "Butter and Waffles?"
            $ renpy.block_rollback()
            call cho_main("Sir?", "annoyed", "narrow", "raised", "mid")
            m "Sorry, I didn't have any lunch..."
            g4 "Actually, I can't even remember the last time I ate..."
            call cho_main("Well, you're obviously wrong...", "soft", "narrow", "raised", "R")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down")

        "-[cho_quiz.hint]Bludger and Quaffle-":
            m "Bludger and Quaffle?"
            $ renpy.block_rollback()
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("Yes!", "smile", "wide", "base", "mid")
            g9 "Great! Then let's get started with the--"
            call cho_main("Next question...", "open", "base", "raised", "down")
            $ cho_quiz.correct_answers += 1

        "-Quabble and Bluffer-":
            m "Quabble and bluffer?"
            $ renpy.block_rollback()
            call cho_main("I think you got some letters mixed up there...", "soft", "narrow", "raised", "R")
            m "Quibble and Blodger?"
            call cho_main("No, that's also not--", "annoyed", "base", "base", "up")
            m "Qacker and Blugger?"
            call cho_main("Professor...", "annoyed", "narrow", "angry", "mid")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down")

    call cho_main("Let's do some history...", "base", "base", "base", "mid")
    g9 "I am made out of history, this should be a breeze..."
    call cho_main("Okay then...", "smile", "base", "raised", "mid")
    call cho_main("A game of Quidditch doesn't finish until the Snitch is caught, therefore it could go on forever...", "open", "base", "base", "down")
    call cho_main("In the longest ever match played, they had to constantly bring on substitutes to let the players get some sleep...", "open", "base", "base", "mid")
    call cho_main("For how long did the game go on for?", "base", "narrow", "raised", "mid")

    # Question 3
    menu:
        "-[cho_quiz.hint]Three Months-":
            m "Three months?"
            $ renpy.block_rollback()
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("Yes!", "smile", "wide", "base", "mid")
            call cho_main("That's impressive, how did you know that one?", "grin", "happyCl", "base", "mid")
            m "I feel like there weren't that many realistic options available this time..."
            call cho_main("Okay... I'm not sure what that means...", "soft", "narrow", "worried", "mid")
            call cho_main("Anyway, final question...", "open", "base", "raised", "down")
            $ cho_quiz.correct_answers += 1

        "-Seven Years-":
            m "Seven years?"
            $ renpy.block_rollback()
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("How long?! That's the same amount of time a student stays at Hogwarts!", "clench", "wide", "base", "mid")
            m "Oh right, I don't know what I was thinking..."
            m "Seven just seems like the magical right answer most of the time..."
            call cho_main("Not in this case...", "annoyed", "narrow", "angry", "mid")
            call cho_main("Anyway, final question...", "open", "base", "raised", "down")

        "-Two Minutes-":
            m "Two minutes?"
            $ renpy.block_rollback()
            call cho_main("What?", "angry", "base", "raised", "mid")
            g4 "What?"
            call cho_main("Sir, what sport lasts only two minutes?", "soft", "narrow", "angry", "mid")
            m "A Splurge race?"
            call cho_main("Never heard of it, is it anything like that basketball thing?", "annoyed", "narrow", "base", "mid")
            g9 "Well, balls have a big role in it..."
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("I'll have to take your word on that one...", "soft", "narrow", "angry", "R")
            call cho_main("Anyway... final question...", "open", "base", "raised", "down")

    call cho_main("As you know, you may not go outside of the bounds with the ball during the game, or you'd have to hand it over to the opposition...", "open", "base", "base", "down")
    call cho_main("But what is the penalty if the defensive goes out of bounds?", "smile", "narrow", "angry", "mid")

    # Question 4
    menu:
        "-Three Months-":
            m "Three months?"
            $ renpy.block_rollback()
            call cho_main("Three months, what?", "annoyed", "narrow", "angry", "mid")
            m "Three months...{w=0.5} in prison?"
            call cho_main("Professor, you're not going to get a prison sentence unless you do something that's actually illegal...", "open", "narrow", "angry", "L")
            m "What if the Quidditch pitch was in prison?"
            m "And you flew outside the prison boundaries..."
            g9 "Did you consider that?"
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("I think you're going off track a bit...", "annoyed", "narrow", "raised", "mid")
            g9 "Or off the pitch..."

        "-A free shot at the goal-":
            m "Free goal shot?"
            $ renpy.block_rollback()
            call cho_main("No that's not right...", "soft", "narrow", "raised", "L")
            m "Then what is it?"
            call cho_main("Well, I don't know...", "angry", "narrow", "worried", "down")
            g4 "How am I supposed to then?"
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("I'm not sure what else to tell you...", "open", "closed", "base", "mid")

        "-[cho_quiz.hint]I don't know...-":
            m "Uh... I don't know..."
            $ renpy.block_rollback()
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("That's right!", "smile", "wide", "base", "mid")
            g4 "What?"
            call cho_main("Nobody knows what happens! There isn't any rule for it...", "open", "wide", "raised", "L")
            g4 "Why wouldn't there be a rule for it?"
            call cho_main("Why would the defensive leave the pitch... they'd just leave the goal open...", "soft", "base", "worried", "mid")
            m "..."
            $ cho_quiz.correct_answers += 1

    pause 1.0
    hide screen exp_o_meter
    with d3

    $ renpy.music.set_volume(1.0)

    call music_block

    call weather_sound

    $ renpy.block_rollback()

    # Success
    if cho_quiz.correct_answers >= 4:
        call cho_main("Well Sir, I thought for a minute that you only cared about basketball, but it looks like I was wrong...", "smile", "base", "base", "mid")
        m "Of course, I am well versed in all sports. I just thought I'd teach you a thing or two."
        m "So, will you let me train you then?"
        call cho_main("I suppose...", "soft", "base", "raised", "R")
        g9 "{size=-4}(Fuck yeah, here we go!){/size}"
        call cho_main("And I will stay true to my word... I'll sell you favours...{w} For wins...", "soft", "closed", "base", "mid")
        g4 "(Hell yes!)"
        call cho_main("But keep it civil. I won't do anything those Slytherin skanks do!", "angry", "narrow", "worried", "R")
        call cho_main("And should you not be able to help me and my team beat Hufflepuff, this will be over before you can even say Snitch!", "scream", "closed", "base", "mid")
        g4 "..."

        if game.daytime:
            call cho_main("Anyway, got to go now, or I'll be too late for classes.", "smile", "base", "base", "mid")
        else:
            call cho_main("Anyway, it's getting late. I should better head to my dorms.", "soft", "base", "base", "R")

        call cho_main("I'll be ready for training by tomorrow morning.", "soft", "base", "base", "down")
        m "{size=-4}Oh, I'm not so sure you'll be that prepared...{/size}"
        call cho_main("Until then, Sir.", "smile", "base", "base", "mid")
        m "Looking forward to it."

        # Cho leaves.
        call cho_walk(action="leave")

        $ cho_quiz.complete = True

        call popup("You've unlocked the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/cho.webp")

    # Failed
    else:
        call cho_main("You seem to care a lot about basketball Sir, but I'm not sure if you know that much about Quidditch...", "open", "narrow", "worried", "mid")
        m "Or were you asking the wrong questions?"
        call cho_main("Sorry?", "soft", "narrow", "raised", "mid")
        g9 "Time is just relative... what is the difference between a month or a few minutes, really..."
        call cho_main("Sir, you got bunch of the questions wrong...", "annoyed", "narrow", "angry", "mid")
        m "The truth lies in the eyes of the beholder, Miss Chang..."
        call cho_main("I don't...{nw=1.0}", "annoyed", "base", "worried", "mid")
        m "You'll see... I'll show you the real truth..."
        m "The true truth!"
        m "(Once I can figure out what the fuck I'm doing...)"
        call cho_main("...", "annoyed", "base", "raised", "mid")
        g9 "Next time..."
        call cho_main("Oh...", "soft", "narrow", "base", "down")
        call cho_main("Well, goodbye then, Sir...", "soft", "base", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        g4 "(What am I supposed to do now... I clearly don't know enough about Quidditch...)"
        m "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)"

        $ cho_quiz.lost = True

        # Read the book.
        if quidditchguide_ITEM.used:
            m "(Why didn't I just follow the book?{w} Serves me right...)"

        # Got the book but not read.
        elif quidditchguide_ITEM.owned > 0:
            m "(Maybe I should read that book they gave me...)"

        # Visited their shop before.
        elif store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"

    jump main_room



# Ask Snape for Quidditch help.
label ss_he_cho_E2:

    call bld
    m "So It looks like I might need some information about Quidditch..."
    call sna_main("I see, I guess it was only a matter of time before you got yourself involved...", "snape_01", ypos="head")
    m "Oh, I don't care much about the sport..."
    call sna_main("Worried you will lose the bet?", "snape_03")
    m "No?{w} Let's say it's more of a plot device to push the narrative forward..."
    call sna_main("Of course you can't teach the girl Quidditch if you know nothing about it...", "snape_09")
    call sna_main("Did she call your bluff?", "snape_13")
    m "Of course not..."
    call sna_main("Well, whilst I could drone on for hours about Quidditch rules...", "snape_06")
    call sna_main("I'd rather not spend my time on such a topic.", "snape_03")
    m "Where am I supposed to learn the basics then?"
    call sna_main("Why do you think I care where you'd learn it from?", "snape_09")
    m "Because keeping me occupied is within your best interests?"
    call sna_main("...", "snape_04")
    call sna_main("Good point...", "snape_06")
    call sna_main("Well, I guess it wouldn't be too harmful if you made yourself to the Weasley Twins...", "snape_05")

    if store_intro_done:
        m "And how would they be able to help me?"
        call sna_main("Well, they're both on the Gryffindor team...", "snape_03")
        call sna_main("And as much as it pains me to say this...", "snape_06")
        call sna_main("They're very discrete business minded individuals...", "snape_02")
        m "I've take it you've had a fair deal of business with them yourself?"
        call sna_main("No comment...", "snape_03")

    else:
        m "The Twins? Have you been keeping twins from me now as well?"
        call sna_main("I mean, if two very irritating ginger boys is your type I'm not going to judge...", "snape_03")
        m "..."
        call sna_main("Fred and George Weasley runs a secret shop in the school...", "snape_01")
        m "Doesn't sound very secret if you know about it..."
        call sna_main("Their rates are good, plus it means I don't have to leave the castle unless absolutely necessary...", "snape_09")
        m "Ah, a basement dweller... charmed."
        call sna_main("In any case, about your inquiry...", "snape_03")
        call sna_main("The boys are sure to have the means of providing what you need.", "snape_01")
        m "Sweet, looking forward to meeting them..."
        call sna_main("Aren't you going to ask for directions?", "snape_05")
        m "I'm sure I'll manage..."
        call sna_main("Try not to wander too far from your office...", "snape_09")
        m "Yes... dad..."
        call sna_main("...", "snape_08") #[angry]

    # Ending
    show screen bld1
    call notes

    ">You spend the rest of the evening in Snape's company once again talking about Cho's remarkable legs."

    hide screen bld1
    with d3

    $ ss_he.cho_E2 = True

    jump day_start
