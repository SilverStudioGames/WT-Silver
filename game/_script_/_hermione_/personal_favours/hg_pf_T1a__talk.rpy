

### Hermione Talks ###

label hg_pf_talk:

    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"

    if hg_pf_talk.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 5
    $ hg_pf_talk.start()

    # End Event
    label end_hg_pf_talk:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    call her_main(xpos="mid", ypos="base", trans=fade)


    # Points
    if her_tier <= 3:
        $ gryffindor += current_payout
        m "{number=current_payout} points to Gryffindor, [hermione_name]. Well done."
    elif her_tier == 4 and hg_pf_talk.points == 1:
        m "{number=current_payout} points to Gryffindor, [hermione_name]. Well done."
        her "Oh, don't worry about the points, [genie_name]. We were just having a nice talk."
        m "Really? What about Gryffindor winning the cup?"
        call her_main("It's only {number=current_payout} points...", "soft", "base", "base", "R")
        m "If you say so."

    if hg_pf_talk.counter == 1: #First time.
        call her_main("Another {number=current_payout} points... The Guys will be so happy!", "base", "happyCl", "base", "mid")

    if her_mood != 0:
        call her_main("Will this be all then?", "annoyed", "base", "angry", "mid")
    else:
        call her_main("Will this be all then?", "soft", "base", "base", "mid")
    m "Yes, you can go now."
    her "Thank you, [genie_name]."

    # Hermione leaves
    call her_walk("door", "base")
    call her_chibi("leave")

    # Increase level
    if her_tier == 1:
        if her_whoring < 3: # Points til 3
            $ her_whoring += 1

    if her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pf_talk_T1_intro_E1:
    call play_music("chipper_doodle")

    m "Alright then..."
    m "Just tell me some news about you."
    call her_main("*Ehm*... Alright...", "open", "squint", "base", "mid")
    call her_main("I just stand here and talk then...? Like this?", "base", "squint", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.8

    m "Well?"
    call her_main("*Ehm*... very well...", "open", "base", "worried", "mid")
    call nar(">Hermione is feeling confused...")
    call her_main("...................", "annoyed", "narrow", "angry", "R")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1_E1:
    call play_music("chipper_doodle")

    m "Alright then..."
    m "Just tell me some news about you."
    call her_main("Here in the middle, right? I remember...", "open", "squint", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.8

    m "Yes?"
    call her_main("*Ehm*... very well...", "open", "base", "worried", "mid")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1: # Call label
    call her_main("My life has been quite uneventful lately, to be honest...", "annoyed", "narrow", "angry", "R")
    call her_main("Apart from the day when I failed that test...", "open", "closed", "base", "mid")
    call her_main("I still can't believe it happened...", "annoyed", "narrow", "angry", "R")

    menu:
        "-Jerk off while she is talking-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8

            call her_main("[genie_name], what are you doing?", "open", "base", "base", "mid", xpos="mid", trans=d3)
            m "What? Oh, it's nothing. Just scratching my leg."
            m "You were saying?"
            call her_main("Yes... Well, that test I failed...", "open", "base", "base", "mid")

        "-Participate in the conversation-":
            $ masturbating = False #NOT JERKING OFF.
            m "Yes, what a tragedy that was..."
            call her_main("Exactly! I'm glad you understand, [genie_name].", "open", "base", "angry", "mid")

    call her_main("Come to think of it, I don't feel like talking about it anymore...", "annoyed", "narrow", "worried", "down")
    m "Alright, what else has happened lately?"
    call her_main("*Ehm*... Well, I'm doing pretty well at Herbology...", "annoyed", "base", "base", "R")
    call her_main("I mean, I always score the top marks, but I have been studying really hard anyway...", "open", "closed", "base", "mid")
    call her_main("And now I sort of feel like sometimes I know more than professor Sprout herself...", "base", "base", "base", "mid")

    if masturbating:
        m "{size=-4}(Yes... *Ah*...){/size}"
    else:
        m "(Professor Sprout... *He-he*, what a ridiculous name...)"

    call her_main("Did you say something, [genie_name]?", "normal", "squint", "angry", "mid")
    m "It's nothing, keep going..."
    call her_main("Well, some students are making fun of professor Quirrell behind his back...", "open", "base", "base", "mid")

    call her_main("I disapprove of such behaviour, of course.", "base", "closed", "base", "mid")
    if masturbating:
        m "{size=-4}(Come on! Say something naughty!){/size}"
    else:
        m ".................."

    call her_main("Oh, and my \"Men's Rights Movement\" group is gaining popularity...", "open", "base", "base", "mid")
    call her_main("I'm very happy about that...", "smile", "base", "base", "R")
    call her_main("I think, given time, we will be able to make a real difference...", "open", "closed", "base", "mid")
    call her_main("It is so invigorating to know that you are doing the right thing!", "base", "base", "base", "mid")
    call her_main("Wouldn't you agree, professor?", "base", "base", "base", "mid")

    if masturbating:
        $ masturbating = False
        m "{size=-4}(Dammit. Now she's killed the mood completely...){/size}"
        call gen_chibi("sit_behind_desk")
        with d3
        pause.8
    else:
        m "*snore*........"

    call her_main("[genie_name]?", "angry", "base", "angry", "mid")
    m "Yes, yes, I'm totally listening..."
    m "This is all very self-righteous, er..."
    m "I mean, very invigorating and stuff..."
    call her_main("..........................", "normal", "squint", "angry", "mid")

    return



### Tier 2 ###

# Hermione realizes you've been jerking off this whole time!
# 'hg_jerkoff.trigger' is required to advance into the next tier.
# Event 1 (i) - Hermione can spot you jerking off.
# Event 2 (r) - Slight dialogue variation if you've been busted jerking off before.

label hg_pf_talk_T2_intro_E1:

    call her_main("Very well, Sir.", "base", "base", "base", "mid")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2_E1:

    if hg_jerkoff.trigger:
        call her_main("Another talk, [hermione_name]?", "soft", "base", "base", "mid")
        call her_main("(I hope he doesn't do \"that\" again...)", "disgust", "narrow", "base", "down")
    else:
        call her_main("Of course, Sir.", "soft", "base", "base", "R")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2:
    call her_main("", "normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    call her_main("My life has been quite uneventful lately, to be honest...", "annoyed", "narrow", "angry", "R")
    call her_main("*Hmm*...", "annoyed", "base", "base", "R")
    call her_main("There is a fierce competition going on between the Slytherin and the Gryffindor house.", "open", "closed", "base", "mid")
    call her_main("To be honest, [genie_name], there should be none...", "open", "narrow", "angry", "R")
    call her_main("Gryffindor would have been in the lead if not for those Slytherin harlots...", "annoyed", "base", "angry", "mid")
    call her_main("The things I hear those girls do - simply to get a few extra points...", "angry", "narrow", "angry", "R")
    call her_main("How despicable!", "open", "closed", "angry", "mid")
    m "What does this make you then, [hermione_name]?"
    call her_main("Exactly!", "normal", "base", "base", "mid")
    m "*huh*?"
    call her_main("I have to work even harder to compensate for the damage those nasty girls are doing...", "open", "closed", "angry", "mid")
    call her_main("Thank you for helping me out, [genie_name].", "normal", "base", "base", "mid")

    menu:
        "-Start jerking off-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8

            call her_main("[genie_name], what are you doing?", "open", "base", "base", "mid")
            call her_main("You are not.....?", "open", "base", "worried", "mid")
            call her_main("Are you...?", "annoyed", "base", "worried", "R")
            m "What? Oh, it's nothing. Keep going."
            call her_main("*Hmm*...", "normal", "squint", "angry", "mid")
            m "{size=-4}(Is she onto me? Nah...){/size}"

        "-Participate in the conversation-":
            $ masturbating = False
            m "Don't mention it."

    call her_main("Well, like I was saying...", "open", "closed", "base", "mid")
    call her_main("I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points...", "open", "narrow", "angry", "R")

    if masturbating:
        m "{size=-4}(What a slut... *Ah*... Yes...){/size}"
    else:
        m "Ten points, *huh*?"

    call her_main("Yes...", "open", "closed", "base", "mid")

    if masturbating:
        call her_main("And these two other girls...", "annoyed", "base", "worried", "R")
        call her_main("There is a rumour that they are actually sleeping with professor Snape...", "annoyed", "base", "worried", "mid")
        m "{size=-4}(Yes... Those nasty Slytherin sluts!){/size}"
        call her_main("Also, there was this one girl who gave a teacher a handjob, right during class...", "base", "base", "base", "mid")
        m "{size=-4}(Yes... This is good stuff, go on!){/size}"
        call her_main("And this other girl, she sucked off a teacher!", "annoyed", "base", "worried", "R")
        m "{size=-4}(Yes! Yes!){/size}"
        call her_main("And another girl let a teacher cum in her mouth...", "smile", "base", "base", "R")
        call her_main("And she swallowed it all and loved it!", "soft", "base", "base", "R")
        m "{size=-4}(Wait... Is she making this up?){/size}"
        call her_main("I'm a nasty girl too, you know...", "smile", "narrow", "base", "mid_soft")
        g4 "What?!"
        call her_main("I just want to suck a cock...", "soft", "narrow", "base", "mid_soft")
        call her_main("I want men to cum on my face like in those magazines I saw!", "open_tongue", "narrow", "base", "mid_soft")
        g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause.8

        call cum_block
        g4 "*Argh*! YES!"

        if hg_jerkoff.trigger:
            call her_main("I can't believe it, [genie_name]!", "soft", "base", "angry", "mid")
            call her_main("You were touching yourself!{w} Again!", "angry", "base", "angry", "mid")
        else:
            call her_main("You were touching yourself, [genie_name]!", "angry", "base", "angry", "mid")

        g4 "What? No, I was just... Ah, shit, this feels good..."

        call hide_characters
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.8

        call her_main("This is disgusting! How could you!?", "scream", "happyCl", "worried", "mid")
        call her_main("[genie_name], you are the headmaster! You are supposed to set a good example!", "scream", "base", "angry", "mid")
        m "Hey, little Missy, are you going to judge me or do you want your points?"
        call her_main("My points please, I believe I earned those.", "angry", "happyCl", "worried", "mid",emote="sweat")
        m "Yes, you did."
        call her_main("*Eww*... I feel so dirty now...", "angry", "base", "angry", "mid")

        $ her_mood = +7

        if hg_jerkoff.trigger == False:
            $ achievement.unlock("busted")
            $ hg_pf_talk.change_icon(a="heart_half", b="heart_red")
        $ hg_jerkoff.triggered() # .trigger = True, .counter += 1

    else:
        call her_main("We need to put an end to this behaviour, [genie_name]!", "open", "closed", "base", "mid")
        m "Yeah, sure..."
        call her_main("So you agree with me then?", "base", "narrow", "base", "mid_soft")
        call her_main("I think we need to implement a new penalty system to punish girls who are known to sell favours...", "open", "base", "base", "R")
        m "(All I heard was \"punish girls\"...)"
        call her_main("This will also help the boys in our school to feel less discriminated against!", "open", "closed", "base", "mid")
        m "The boys?"
        m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
        call her_main("I'm so glad that you understand my concerns, [genie_name].", "base", "base", "base", "mid")
        m "Yes, yes, sure..."

    return



### Tier 3 ###

# Hermione knows by now that you like to jerk off while she talks.
# She tells you true stories that happened at Hogwarts.
# Favours can revolve around Cho, Luna, Tonks

label hg_pf_talk_T3_intro_E1:
    m "Let's have another chat, [hermione_name]."
    call her_main("Okay...", "annoyed", "base", "worried", "mid")
    m "I'd like you to tell me a bit about your day."
    call her_main("Are you going to...{w=0.8} touch yourself again sir?", "open", "squint", "base", "mid")
    m "I can't guarantee I won't..."
    m "You will be awarded with house points - as usual."
    call her_main("...", "mad", "narrow", "worried", "down", cheeks="blush") #mad Blush
    m "You've not walked out the door, so please, tell me about your day."

    call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_intro_E2:
    m "{size=-4}(Should I spice things up a bit?){/size}"
    menu:
        #"-Suggest inviting Snape-":
        #    pass
        #    #To be added
        #    #$ hg_pf_talk_snape.start()
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ hg_pf_talk_tonks.start()
        "-Decide against it-":
            m "Let's have another chat, [hermione_name]."
            call her_main("Okay...", "base", "base", "base", "mid")

            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_repeat:
    menu:
        #"-Suggest inviting Snape-":
        #    pass
        #    #To be added
        #    #$ hg_pf_talk_snape.start()
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ hg_pf_talk_tonks.start()
        "-Decide against it-":
            m "Tell me about your day, [hermione_name]."
            call her_main("Okay...", "base", "base", "base", "mid")
            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.5

    menu:
        "-Start jerking off-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8
            call her_main("[genie_name], I hoped we wouldn't do this again...", "open", "squint", "base", "mid")
            call her_main("Are you actually... Masturbating again?", "disgust", "squint", "base", "mid")
            m "Me? I'd never do such a thing. Ever..."
            m "Anyhow... Don't forget why you're here, [hermione_name]. To earn some points..."

        "-Participate in the conversation-":
            $ masturbating = False
            m "Time to earn those points."

    call her_main("Well...", "open", "closed", "base", "mid")
    her "Today started off fairly normal..."
    call her_main("We had muggle studies.", "base", "base", "base", "mid")
    call her_main("Professor Burbage babbled on about things she doesn't understand as usual.", "open", "base", "base", "R")
    call her_main("As I'm a muggle born I've been considering dropping the subject. It's a waste of time.", "base", "base", "base", "mid")
    call her_main("Although since I failed that test I feel like I need all the extra points I can get...", "open", "narrow", "worried", "down")
    call her_main("Her views on muggle and wizarding relations, and the fact that we're not that different is also quite refreshing...", "base", "happy", "base", "mid_soft")
    call her_main("Not that the Slytherins aren't constantly trying to disrupt her classes...", "annoyed", "happyCl", "base", "mid")
    if masturbating:
        m "*Hmm* I bet they were..."
        call her_main("*UGH* Do you have to keep touching yourself professor?", "disgust", "narrow", "worried", "down", cheeks="blush")
        m "Just keep talking [hermione_name]..."
        call her_main("Fine...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    else:
        m "Is that so?"
        m "So, what were they doing exactly?"

    call her_main("Well, her room is filled with a bunch of muggle toys, instruments and trinkets...", "open", "base", "base", "mid")
    call her_main("Her collection would even bring mister Weasley's to shame.", "base", "base", "base", "mid")

    if masturbating:
        m "(I bet she has a bunch of sex toys in there...)"
    else:
        m "Maybe I should have a look at her collection myself."

    call her_main("There's obviously nothing that stands out as odd to me in any way.", "open", "base", "base", "mid", cheeks="blush")
    call her_main("But since most of the Slytherins are pure-blood they were handling her items with little to no care.", "mad", "base", "base", "R")
    call her_main("So when they weren't silently insulting her about her views, they were constantly making suggestive remarks about the objects, asking where she'd insert them...", "annoyed", "base", "worried", "R")
    call her_main("She's quite oblivious to it most of the time but the constant giggling from the Slytherin girls is very distracting and annoying.", "open", "narrow", "worried", "down", cheeks="blush")
    call her_main("It didn't help when they discovered what professor Burbage actually believed to be a back massager...", "angry", "happyCl", "base", "mid", cheeks="blush")
    m "I mean, that's what it says on the box..."
    g4 "Wait, how do you know what people usually use them for?"
    call her_main("...", "disgust", "wide", "worried", "shocked", cheeks="blush")
    g9 "Well?"
    call her_main("I...", "annoyed", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("Well, it's obvious to anyone with common sense isn't it!", "open", "narrow", "angry", "R", cheeks="blush")
    call her_main("Even those Slytherin girls quickly realised what people use it for... and they're thicker than polyjuice potion!", "mad", "closed", "angry", "mid", cheeks="blush")
    if masturbating:
        m "(I bet you wouldn't mind nicking it for yourself...)"
    else:
        m "(Poly... what?)"
    g9 "Why don't {size=+4}you{/size} tell me since you seem so knowledgeable about the subject..."
    call her_main("Sorry?", "mad", "base", "worried", "mid", cheeks="blush")
    m "What {size=+4}would{/size}{w=0.6} they use those massagers for?"
    call her_main("Well, you know...", "open", "narrow", "worried", "down", cheeks="blush")
    m "Pretend that I don't."
    call her_main("...", "normal", "narrow", "base", "down", cheeks="blush")

    if masturbating:
        call her_main("They'd use it for what you're doing...", "open", "happyCl", "worried", "mid")
        m "Which is..."
        call her_main("Well, you'd insert it...{w=0.5} and use it to...", "normal", "narrow", "worried", "down", cheeks="blush")
        m "To what?"
        her "To pleasure yourself..."
        m "And are you using one of these devices?"
        call her_main("Of...{w=0.5} of course I'm not!{w=0.5} Muggle electronics does not work at Hogwarts!", "base", "happyCl", "base", "mid", cheeks="blush")
        g9 "So you have one at home then?"
        call her_main("I...", "normal", "narrow", "worried", "down", cheeks="blush")
        g9 "(I knew it, you dirty slut!)"
        call her_main("I don't have to talk about my personal health to you!", "open", "narrow", "angry", "R", cheeks="blush")
        g9 "I bet you use it any chance you get when nobody is around!"
        call her_main("I do not!", "angry", "base", "angry", "mid", cheeks="blush")
        g9 "{size=-4}So you do it even when your parents are at home?{/size}"
        g4 "{size=-4}You dirty...{w=0.5}*HNGH*...{w=0.5} whore! *Argh!*{/size}"

        call play_music("stop")
        call hide_characters
        hide screen bld1
        with d3
        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause.8

        call cum_block
        call bld
        g4 "*Argh!* YES!"

        call play_music("playful_tension")
        if her_tier <= 4:
            $ her_mood = +7
            call her_main("[genie_name]...{w} did you just...?", "disgust", "narrow", "base", "down")
        else:
            call her_main("[genie_name]...{w} did you just...?", "soft", "narrow", "worried", "down")

        call hide_characters
        hide screen bld1
        with d3
        pause.1
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.5

        if her_tier <= 4:
            call her_main("*Yuck*!...", "annoyed", "narrow", "base", "mid_soft")
        call bld
        m "That felt amazing..."
        call her_main("...", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")
        g9 "You shouldn't hold it in, [hermione_name]... It could help you relax a bit."
        m "All great wizards do it..."
        call her_main("(.........)", "annoyed", "narrow", "angry", "R")
        m "I could even go fetch that massager for you if you'd like."
        her "No!"
        m "Oh yeah, you said they don't work at the school..."
        call her_main("That's not what I meant...", "annoyed", "happyCl", "worried", "mid")
        m "Loosen up a bit won't you, I'll figure something out don't you worry..."
        call her_main("{size=-4}I am not-{/size}", "annoyed", "happyCl", "worried", "mid")
        call her_main("(...................)", "disgust", "base", "worried", "mid")
        m "You've done well today [hermione_name]..."
        call her_main("You've soiled your entire desk!", "mad", "wide", "base", "stare")
        m "I'm sure it will be cleaned at one point or another..."
        if her_tier <= 4:
            call her_main("Gross...", "normal", "happyCl", "worried", "mid", cheeks="blush")
        else:
            call her_main("(Such a waste...)", "soft", "narrow", "worried", "down", cheeks="blush")
        call her_main("May I have my points now?", "open", "narrow", "worried", "down", cheeks="blush")
        m "Of course..."

    else:
        m "Yes?"
        call her_main("They're...{w=0.5} they're back massagers, it says so on the box... you said so yourself.", "open", "base", "worried", "R", cheeks="blush")
        m "Then what's the problem with the Slytherin girls having a go with it?"
        call her_main("Nothing! I'm sure they found it very educational!", "angry", "happyCl", "worried", "mid", cheeks="blush")
        call her_main("I had never seen them more interested in muggle studies in fact!", "disgust", "narrow", "angry", "R", cheeks="blush")
        m "I bet..."
        m "So, since you're muggle born and all..."
        call her_main("Yes?", "open", "happy", "base", "mid_soft")
        m "I hope you properly demonstrated how to use it to them."
        call her_main("What? Why on earth do you think I would do that?", "shock", "wide", "base", "stare", cheeks="blush")
        call her_main("Do you take me for some sort of exhibitionist?", "mad", "wide", "base", "stare", cheeks="blush")
        m "Sorry?"
        call her_main("Don't you sorry me...{w=0.5} you expect me to get my fanny out and casually just shove it in there for the whole class to see?", "angry", "base", "angry", "mid", cheeks="blush")
        call her_main("I'm sure they would love that and find it more than educational...", "base", "closed", "angry", "mid", cheeks="blush")
        with hpunch
        call her_main("How{w=0.8} {size=+6}dare{/size} you suggest--", "open", "base", "angry", "mid", cheeks="blush")
        m "What are you talking about? Weren't we talking about back massagers?"
        call her_main("-I'd just tear my clothes off and...", "open", "closed", "angry", "mid", cheeks="blush")
        $ renpy.sound.play("sounds/glass_shatter.mp3")
        call her_main("...", "mad", "wide", "base", "stare", cheeks="blush")
        her "I...{w} I'm sorry professor!"
        g9 "I didn't take you for such a naughty girl, [hermione_name]!"
        g9 "Here we were having an innocent conversation about back massagers and you spring all this on me."
        call her_main("Professor... I didn't mean.", "soft", "happyCl", "worried", "mid", cheeks="blush")
        g9 "Don't you 'Professor' me..."
        call her_main("But please, I assure you...", "open", "base", "worried", "mid", cheeks="blush")
        m "That will be all for today Miss Granger."
        m "You've surely opened my eyes..."
        call her_main("...", "annoyed", "base", "base", "mid")
    return



label hg_pf_talk_tonks_T3_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], for today's favour I'd like to bring in a guest to join us."
    call her_main("What? Didn't we decide it was going to be between just you and I?", "open", "squint", "angry", "mid")
    m "Well, why only the two of us when there is the option to bring another person in?"
    call her_main("The option to?", "normal", "squint", "angry", "mid")
    call her_main("Sorry, I'm not following...", "normal", "squint", "base", "mid")
    m "[hermione_name], what is your opinion of Miss Tonks?"
    call her_main("Well, she's a very talented witch... You'd have to be to become an auror.", "open", "closed", "base", "mid")
    m "Wouldn't it be great if we could have another chat with each other?"
    m "I heard you already had a bit of a talk previously."
    call her_main("You knew about that?", "angry", "base", "worried", "mid", cheeks="blush")
    m "I'm the headmaster [hermione_name]...{w} It's my job to know what goes on within the castle."
    m "She was the one that suggested you try selling some favours yourself, was it not?"
    call her_main("Well...", "disgust", "narrow", "base", "down")
    m "I think it could be quite nice to have a little conversation - all of us together."
    call her_main("Just a conversation then?", "open", "base", "base", "R")
    m "Yes, just a conversation..."
    m "And you'd be awarded points of course."
    call her_main("...", "annoyed", "base", "base", "R")
    call her_main("Would I be getting any extra points for this?", "open", "base", "base", "mid")
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    call her_main("Okay... Just let me get more presentable.", "base", "base", "base", "mid")
    m "Great, I'll call for her then..."

    call hg_pf_talk_tonks

    jump end_hg_pf_talk


label hg_pf_talk_tonks_T3_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Let's call Miss Tonks up for this one shall we."
    call her_main("For what?", "open", "happy", "base", "mid")
    m "For today's favour of course!"
    call her_main("...", "annoyed", "narrow", "base", "mid_soft")
    call her_main("Will I get any extra points for this?", "open", "base", "base", "mid")
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    call her_main("Fine.. Just let me get more presentable.", "base", "base", "worried", "R")

    call hg_pf_talk_tonks

    jump end_hg_pf_talk


label hg_pf_talk_tonks:
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    pause 1

    # Setup
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_default)

    $ ton_outfit_last.save()
    $ tonks.equip(ton_outfit_default)

    call play_sound("door")
    call ton_chibi("stand",500,"base")
    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d5
    pause.8

    call ton_main("","base","base","base","mid", hair="basic", xpos="600", ypos="base")
    call her_main("Hello, Professor Tonks.", "open", "closed", "base", "mid", xpos="right", ypos="base")
    call her_main("", "base", "base", "base", "mid")
    if game.daytime:
        m "Good day, Miss Tonks."
        call ton_main("Good day, Professor.","base","happyCl","base","mid")
    else:
        m "Good evening, Miss Tonks."
        call ton_main("Good evening, Professor.","base","happyCl","base","mid")
    call ton_main("Hermione...","horny","base","base","L", hair="horny")
    call ton_main("Is there some sort of special circumstance as to why the two of you summoned me here?","base","base","raised","mid", hair="basic")
    m "More or less."
    m "I think the three of us should have a bit of a chat..."
    call ton_main("Miss Granger, you didn't cause any trouble I hope?","open","base","base","L")
    call her_main("Me? Of course not!", "open", "closed", "base", "mid")
    call her_main("", "base", "base", "base", "mid")
    m "Now, I thought we could have a chat about these favour trading allegations..."
    m "That you most kindly brought to Miss Tonks' attention."
    call her_main("Oh, those...", "open", "narrow", "worried", "down")
    m "Unless you've suddenly changed your mind on that sort of thing?"
    call her_main("...", "normal", "base", "base", "R")
    call her_main("No, I'll talk about it - if you like...", "open", "narrow", "base", "down", cheeks="blush")
    call her_main("", "normal", "base", "base", "mid", cheeks="blush")
    call ton_main("...","horny","base","base","mid", hair="horny")
    m "Why don't we start with..."

    menu:
        "\"Those pesky Slytherin Sluts!\"":
            call ton_main("Yes, I've heard those Slytherin girls are up to no good...","horny","base","angry","mid")
            call her_main("They are! Where do I begin?", "open", "closed", "angry", "mid", cheeks="blush")

            menu:
                "-Start jerking off-":
                    $ her_jerk_off_counter += 1
                    $ masturbating = True
                    call hide_characters
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("jerk_off_behind_desk")
                    with d3
                    pause.8

                    call nar(">You reach under the desk and grab your cock...")

                "-Participate in the conversation-":
                    $ masturbating = False

            call ton_main("","horny","base","base","down")
            call her_main("There's the time Tracey Davis gave Slughorn a lap dance, in the middle of class!", "annoyed", "narrow", "angry", "R", cheeks="blush")
            call ton_main("In the middle of class?", "mad", "wide", "shocked", "stare")
            call her_main("Yes...", "disgust", "narrow", "worried", "down", cheeks="blush")
            call ton_main("Oh my...", "base", "narrow", "raised", "mid", hair="horny")
            call her_main("She was just sitting on his lap while he taught from his desk...", "open", "base", "base", "R", cheeks="blush")
            call her_main("But we could all see her moving her hips!", "annoyed", "base", "base", "R", cheeks="blush")
            call ton_main("Interesting...", "grin", "narrow", "shocked", "down")
            call ton_main("Any other incidents, Miss Granger?", "upset", "wide", "shocked", "L", cheeks="blush")
            call her_main("More than I could count!", "open", "closed", "angry", "mid")
            call ton_main("", "mad", "base", "base", "mid")
            call her_main("I'm almost certain one of the girls wasn't wearing any underwear in class - which is completely unhygienic.", "angry", "narrow", "worried", "mid_soft")
            if not hermione.is_worn("panties"):
                m "(Is she even wearing any herself right now?...)"
            call her_main("It was as if a snail had dragged themselves across one of the seats.", "annoyed", "base", "base", "R", cheeks="blush")
            call her_main("I had to insist on staying after class - and I spent a good ten minutes scourgifying everything.", "disgust", "narrow", "worried", "down", cheeks="blush")
            if masturbating:
                g9 "(I bet you lapped it all up, slut!)"
            call ton_main("Why bother, the elves would've done it anyway.", "mad", "narrow", "raised", "R")
            call her_main("About that--", "open", "squint", "angry", "mid")
            call ton_main("Actually, let's save that topic for another time...", "normal", "narrow", "base", "L")
            if masturbating:
                g4 "(You wanted it all for yourself, that's why!)"
            call ton_main("Is there anything else you could tell us about these... naughty Slytherin girls?","horny","base","angry","mid", hair="horny")
            call her_main("Of course!", "open", "closed", "angry", "mid")
            call her_main("I could go on for hours about the vile things they've been up to...", "annoyed", "narrow", "annoyed", "mid")
            call ton_main("I'm not in a rush.", "base", "narrow", "base", "down", cheeks="blush")
            call ton_main("But even if I was, it can wait until later.", "horny", "base", "raised", "L", cheeks="blush")
            call her_main("Well, that girl...{w=0.3} Pansy Parkinson...", "open", "closed", "angry", "mid")
            call her_main("She just lets Snape grab her ass whenever he wants... and gives her five points each time...", "annoyed", "base", "angry", "mid")
            call ton_main("Only five measly points?", "open", "shocked", "worried", "R")
            call ton_main("(She'd get double from me... easily...)", "upset", "base", "base", "R")
            m "..."
            call ton_main("Now, we can't have that, can we...", "open", "base", "annoyed", "L")
            call her_main("I know... It angers me to the core...", "annoyed", "base", "worried", "mid")
            call ton_main("", "upset", "base", "worried", "L", hair="basic")
            call her_main("Everyone has been working so hard towards winning the cup... I have been working so hard...", "open", "base", "worried", "mid", cheeks="blush")
            if masturbating:
                m "(You have no idea what your hard work does to me...)"
            call her_main("The way it is right now doesn't promote fairness at all.", "annoyed", "narrow", "worried", "down")
            call ton_main("I can see how that could be a problem...","open","closed","base","mid")
            call her_main("It's a huge problem!", "angry", "base", "angry", "mid")
            call ton_main("","base","base","worried","L")

        "\"Yourself, Miss Granger!\"":
            call her_main("What?!", "soft", "base", "worried", "mid")
            call ton_main("Yes, I would love to hear a bit more about what's going on with you Miss Granger...","horny","base","base","L", hair="horny")
            call ton_main("When I took the teaching position, you and I had a bit of a discussion, didn't we?", "base", "base", "raised", "L")
            call ton_main("From what I've been hearing on the Portrait vine, you have been selling a few favours yourself to professor Dumbledore here...", "base", "narrow", "shocked", "down")
            call her_main("I have not!", "shock", "squint", "angry", "mid", cheeks="blush")

            menu:
                "-Start jerking off-":
                    $ her_jerk_off_counter += 1
                    $ masturbating = True
                    call hide_characters
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("jerk_off_behind_desk")
                    with d3
                    pause.8

                    call nar(">You reach under the desk and grab your cock...")

                "-Participate in the conversation-":
                    $ masturbating = False

            call ton_main("","horny","base","base","down")
            call her_main("", "annoyed", "squint", "angry", "mid", cheeks="blush")

            if masturbating:
                g9 "(Oh yes you have, you naughty slut...)"
            else:
                $ tmp_val = her_jerk_off_counter+hg_pf_admire_panties.counter+hg_pf_admire_breasts.counter+hg_pf_grope.counter+hg_pf_strip.counter+hg_pf_handjob.counter+hg_pf_blowjob.counter+hg_pf_titjob.counter+hg_pf_sex.counter
                $ tmp_word = num_to_word(tmp_val) # Sum up all favour counters and turn them into a word.

                m "{size=-4}...[tmp_word]...{/size}"
                call her_main("*huh*?", "open", "squint", "angry", "mid", cheeks="blush")
                m "You sold me exactly [tmp_word] favours."
                call her_main("B-but that's--","angry","happy", cheeks="blush")
                if tmp_val < 10:
                    call ton_main("Disappointing, but it's a start.","open","closed","base","mid", hair="basic")
                    call her_main("...", "annoyed", "narrow", "base", "R_soft", cheeks="blush")
                elif tmp_val >= 10 and tmp_val < 20:
                    call ton_main("Not bad, but I expected better from one of the top students in entire school.","open","base","base","L", hair="basic")
                elif tmp_val >= 20 and tmp_val < 30:
                    call her_main("", "angry", "narrow", "base", "R_soft", cheeks="blush")
                    call ton_main("You go girl! I expected as much from one of my students.","open","base","angry","L", hair="basic")
                    m "..."
                    call ton_main("I meant to say, one of {i}your{/i} students, of course.","upset","base","worried","mid", hair="basic")
                elif tmp_val >= 30 and tmp_val < 40:
                    call ton_main("Aren't you a sneaky one, *huh*? Almost tricked me with those doe-like eyes of yours - that you're an innocent girl.","horny","base","angry","L", hair="horny")
                    call ton_main("But, as it turns out, you're actually quite high on the list.","open","base","raised","L", hair="basic")
                    call her_main("(... there's a list...?)", "open", "happyCl", "worried", "mid", cheeks="blush")
                    call ton_main("At the very top!", "silly", "happyCl", "base", "mid")
                    call her_main("...", "angry", "narrow", "base", "down", cheeks="blush")
                else:
                    call ton_main("Wow! Who would have thought you're the girl from top of the list.", "silly", "happyCl", "base", "mid")
                    call ton_main("Colour me surprised, looks like they were telling the truth after all.","horny","base","angry","L", hair="horny")
                    call her_main("(... a list ... what list...?)", "angry", "wide", "worried", "stare", cheeks="blush")
                    call ton_main("Congratulations for being a \"top\" student.","horny","base","raised","L")
                    call her_main("...", "disgust", "narrow", "base", "R_soft", cheeks="blush")

            call ton_main("Don't be so shy, girl. I'm happy that you took my advice to heart...","open","base","base","L", hair="basic")
            call ton_main("After all, it's thanks to you that the ministry sent me here.","base","base","base","L")
            call her_main("I guess...", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("I assure you that I was actually against the practice - during the time of sending the letter...", "annoyed", "narrow", "worried", "down", cheeks="blush")
            call her_main("At least, until we had our talk about it, Professor.", "soft", "base", "base", "R", cheeks="blush")
            if masturbating:
                m "(And we've only just started...)"
            call her_main("To help my house catch up in points. Doing it to help Gryffindor...", "soft", "narrow", "worried", "down", cheeks="blush")
            if masturbating:
                g9 "(And because you love it...)"
            call ton_main("Well, if you can't beat them...","horny","base","base","R", hair="horny")
            call ton_main("So, how has that been working for you so far, Miss Granger?","open","base","base","L", hair="basic")
            call ton_main("How is morale amongst the Gryffindor students, now?","base","base","raised","L")
            call her_main("It's great! Although... I still believe that it isn't fair...", "soft", "base", "base", "mid", cheeks="blush")
            call her_main("That is why I created the \"M.R.M\"!", "open", "happy", "base", "mid_soft")
            call ton_main("Yes. The \"Men's Reign Movement\"...","open","closed","base","mid")
            call ton_main("","base","base","base","mid")
            call her_main("But...{w=0.5} that's not what \"M.R.M\" stands for!", "angry", "base", "worried", "mid")
            call her_main("It's the \"Men's Rights Movement!\"", "open", "closed", "base", "mid")
            call her_main("I've told you both about it... In detail!", "annoyed", "base", "angry", "mid")
            call ton_main("I see... I probably wrote it down and put it somewhere in my...{w=0.8} extensive notes folder...", "soft", "base", "raised", "R")
            m "{size=-5}(*Heh!* It's like looking at myself in a mirror...){/size}" # Small text
            call her_main("(...)", "annoyed", "narrow", "worried", "down")
            call her_main("The \"M.R.M\" is there to provide male students with the same fairness, righteousness, and just benefits that girls are receiving at the school.", "open", "closed", "base", "mid")
            call her_main("I felt its creation was necessary...", "annoyed", "base", "base", "mid")

    call her_main("All this favour trading has been completely unfair to the boys!", "open", "narrow", "annoyed", "mid")
    call ton_main("Ah, yes... yes.", "open", "closed", "worried", "mid")
    call ton_main("... Wait, what?", "mad", "shocked", "raised", "L")
    g9 "..."
    call her_main("*Ugh!*... I assumed you read through the initial letter more thoroughly...", "open", "narrow", "worried", "mid_soft")
    if masturbating:
        m "(too busy staring her down I bet...)"
    else:
        m "Now-now, Miss Granger... Tonks was very quick to get here when she heard about your accusations."
    call her_main("I suppose...", "annoyed", "narrow", "base", "R_soft")
    call ton_main("So your problem was never that the girls of this school are engaging in illicit, sexual favours with their teachers...", "normal", "wide", "raised", "L")
    call ton_main("It's that the boys aren't able to do the same?", "upset", "base", "raised", "L")
    call her_main("Exactly!", "open", "closed", "angry", "mid")
    call ton_main("Why didn't you say so during our talk earlier, Miss Granger?", "grin", "narrow", "raised", "L")
    call ton_main("I can easily sort out that problem!","horny","base","base","L", hair="horny")
    call her_main("I {i}did{/i} mention it!", "angry", "happyCl", "worried", "mid")
    call ton_main("Oh...", "annoyed", "base", "raised", "downR", hair="basic")
    if not masturbating:
        m "..."
    call ton_main("Hold on...","open","closed","base","mid")
    call ton_main("That doesn't explain as to why {i}you{/i} decided to contribute to this problem, and do favours for your teachers as well.","open","base","raised","L")
    call her_main("Well...", "disgust", "base", "base", "R")
    call ton_main("There is no need for you to keep up an act, if you changed your mind on it.", "soft", "base", "base", "down")
    call ton_main("You can tell us. I most certainly won't judge you...","horny","base","base","L", cheeks="blush", hair="horny")
    call her_main("I just...{w=0.6} Sometimes Gryffindor is just so far behind in points...", "soft", "narrow", "base", "down")
    call ton_main("Oh, I see...", "base", "base", "base", "L", hair="basic")
    call her_main("So I also asked Professor Dumbledore for a favour, but only once or twice...", "soft", "base", "base", "mid", cheeks="blush")

    if not masturbating:
        m "Actually..."
        call her_main("*Hmph*...", "annoyed", "narrow", "angry", "R", cheeks="blush")

    call ton_main("And I suppose you're against the idea of doing favours for another teacher?","horny","base","raised","L", hair="horny")
    call her_main("I...", "angry", "narrow", "worried", "down", cheeks="blush")
    call her_main("*Umm*... maybe I could?", "soft", "base", "base", "R", cheeks="blush")
    call her_main("I haven't actively considered it...", "soft", "narrow", "base", "mid_soft", cheeks="blush")
    if masturbating:
        g4 "(Yes! You want to make out with your slutty teacher, don't you!)"
    call ton_main("Don't think I'm judging you, Miss Granger.", "normal", "base", "base", "L", hair="basic")
    call ton_main("I'm sure your house has been ecstatic about the sudden spike in house points.", "soft", "wide", "raised", "L")
    if masturbating:
        g4 "(And they're not the only ones being ecstatic!)"
        "*fap-fap-fap*"
        m "(I'm getting close. Maybe I should ask her about something else...)"
        $ tmp_name = hermione_name[:3]
        g4 "[tmp_name]-...{w=0.3} *Ugh*... Miss Granger..."
        g4 "Why don't you tell us more about..."
    else:
        m "I think we've been trailing a bit off topic here..."
        call ton_main("Oh yes, perhaps...","base","base","base","L", hair="basic")
        m "Miss Granger, why don't you tell us more about..."

    menu:
        "\"Those pesky Slytherin Sluts!\"":
            call her_main("What else would you like to know?", "open", "base", "base", "mid")
            if masturbating:
                m "What other.. *Ugh.. activities do you have here?"
            else:
                m "What other classes do you have here?"
            call her_main("I'm not sure what you mean, Professor...", "annoyed", "base", "base", "R")
            call ton_main("I think what your headmaster is getting at...","open","closed","base","mid")
            call ton_main("Is there any other... uncouth behaviour going on outside of the dungeons?", "grin", "base", "raised", "L", hair="horny")
            call ton_main("You've only mentioned potions and alchemy class thus far.","base","base","base","L")
            if masturbating:
                g9 "(Where did those bad teachers touch you?)"
            else:
                m "Yes, that!"
            call her_main("Well, of course there is... Even if they might not be as successful...", "annoyed", "base", "angry", "mid_soft")
            call her_main("With all the teachers, there are plenty of filthy tactics being used - all over the school.", "open", "base", "angry", "mid")
            if masturbating:
                g4 "(Filthy, *huh*?)"
                "*fap-fap-fap*"
            else:
                m "Such-{w=0.5}{nw}"
            call ton_main("Such as?","horny","base","raised","L")

            # Random choice of stuff that has happened.
            $ character_choice = []
            $ character_choice.append("slytherins") # 'else' choice. List can't be empty.
            if cho_tier >= 2:
                $ character_choice.append("cho_1")
            if cc_pf_strip.counter >= 2: # Cho stripped and Hermione saw it.
                $ character_choice.append("cho_2")
            if astoria_unlocked:
                $ character_choice.append("astoria_1")

            $ random_choice = renpy.random.choice(character_choice)

            if random_choice == "cho_1": # After winning against Hufflepuff.
                call her_main("It's not even just the Slytherins doing it!", "open", "closed", "angry", "mid")
                call ton_main("Oh really?","base","base","raised","L")
                call her_main("Yes, that girl from Ravenclaw...{w=0.6} Cho Chang...", "open", "base", "angry", "mid")
                call her_main("She was using some pretty dirty tactics - during the first Quidditch match of the season!", "angry", "base", "angry", "mid")
                g9 "(Yes, very dirty indeed...)"
                call her_main("You could clearly see her panties at one point...", "soft", "base", "angry", "mid")
                call her_main("Surely she dressed that way just to distract the other team...", "annoyed", "narrow", "angry", "R")
                if masturbating:
                    m "(I'm sure it distracted the commentator as well...)"
                else:
                    m "Were you looking, Miss Granger?"
                    call her_main("...", "annoyed", "narrow", "base", "R_soft", cheeks="blush")
                call ton_main("*Hmm*... sounds like watching Quidditch has gotten a lot more interesting since I was in school.","horny","base","raised","mid")
                call her_main("I wouldn't use the word interesting to describe it...", "annoyed", "base", "worried", "mid", cheeks="blush")
                call ton_main("I'll make sure to show up to the next match, to see what's going on for myself.","base","base","base","mid")
                call her_main("Thank you professor...", "open", "closed", "base", "mid")

            elif random_choice == "cho_2": # After Cho stripped for you.
                call her_main("You're well aware that it's not just Slytherins that have been doing stuff like this...", "open", "closed", "angry", "mid")
                call ton_main("If you'd like to give an example...","base","base","base","L")
                call her_main("I'm talking about Cho Chang!", "open", "base", "angry", "mid")
                call ton_main("Ah yes, the Ravenclaw seeker...","base","base","raised","mid")
                call ton_main("She's a feisty one, isn't she!","horny","base","angry","mid")
                call her_main("...", "annoyed", "base", "angry", "mid")
                call ton_main("Would you like to tell me what she did?","horny","base","base","L")
                if masturbating:
                    g4 "(Stripped right in front us is what she did!)"
                    "*fap-fap-fap*"
                else:
                    g9 "I can tell you all about Miss Chang's little--"
                call her_main("She was dancing! Right here!", "open", "closed", "base", "mid")
                call ton_main("Oh, did she really?", "base", "base", "raised", "L")
                call ton_main("With or without clothes?","horny","base","angry","mid")
                if masturbating:
                    call her_main("Without...", "soft", "narrow", "base", "R_soft")
                else:
                    g9 "The latter!"
                call ton_main("Oh my... What girl would do such a shameful thing...", "open", "base", "worried", "mid")
                call her_main("...", "disgust", "narrow", "worried", "down", cheeks="blush")
                call ton_main("Are you blushing, Miss Granger?","base","base","angry","L")
                call her_main("...", "disgust", "narrow", "base", "down", cheeks="blush")
                her "N-no...? Anyway..."

            elif random_choice == "astoria_1": # After Astoria got caught.
                call her_main("That Astoria girl, casting imperio on a student - making her lift her top...", "soft", "narrow", "angry", "R")
                call ton_main("Ah, yes that was unfortunate...", "normal", "base", "worried", "R", hair="basic")
                if masturbating:
                    g4 "(And hot...)"
                call her_main("I take it that has been dealt with?", "normal", "base", "base", "R")
                call ton_main("Yes, there's no need for you to worry about her, miss Granger...", "base", "happyCl", "raised", "mid", hair="basic")
                call ton_main("She has been properly reprimanded - and both professor Dumbledore and I have taken it upon ourselves to work on her behaviour.","horny","base","base","mid", hair="horny")
                #if first training done:
                if masturbating:
                    g9 "(If only there was a reason to give you some punishment...)"
                    "*fap-fap-fap*"
                call her_main("I see...", "normal", "narrow", "worried", "down")
                call her_main("Well, that's good to hear...", "open", "closed", "base", "mid")
                call her_main("I would have just handed her over to the authorities, if it was up to me...", "open", "base", "angry", "mid")
                call her_main("Anyway...", "open", "closed", "base", "mid")

            else:
                call her_main("...", "annoyed", "narrow", "worried", "down", cheeks="blush")
                call ton_main("Miss Granger?", "normal", "base", "raised", "L")
                call her_main("*Ehm*...", "annoyed", "base", "base", "R", cheeks="blush")
                call her_main("Well, I could pick any of the girls in Slytherin, really...", "soft", "narrow", "angry", "R")

            call her_main("It is quite astonishing to what level those Slytherins would go - to get the teachers going...", "annoyed", "base", "angry", "mid")
            call her_main("Especially that one time during care for magical creatures...", "open", "base", "base", "mid")
            call ton_main("Oh? You weren't studying centaurs, were you?", "horny", "base", "raised", "mid")
            call her_main("No? Why would you assume that?", "normal", "wink", "base", "mid")
            call ton_main("No reason... please continue...","open","base","raised","R", cheeks="blush", hair="horny")
            call ton_main("","base","base","raised","mid", hair="basic")
            call her_main("Well, I do hope that Hagrid is above this favour trading business. He sure seems like it during my classes with him.", "open", "base", "base", "R")
            call her_main("One of those Slytherin students was being quite rough with a {i}Blast-ended Skrewt{/i}... making it go off on purpose...", "annoyed", "narrow", "worried", "down")

            if masturbating:
                call her_main("She was slowly moving it up and down, only agitating it a bit initially...", "annoyed", "base", "base", "mid")
                g9 "(Yes I bet you'd love to do that with my cock.)"
                call her_main("But once she got going - you could really see how it could just go off any minute...", "open", "base", "base", "mid")
                g4 "(Yes, any minute now...)"
                call her_main("I was just about to call her out on it, as it started shaking violently.", "open", "base", "base", "R")
                g4 "(Yes, any second now...)"
                call ton_main("Then what happened?","open","base","raised","L", cheeks="blush")
                call her_main("I could momentarily see the concerned look on her face, as the {i}Skrewt{/i} exploded right into it...", "open", "narrow", "worried", "down", cheeks="blush")
                call ton_main("","horny","base","angry","mid", cheeks="blush", hair="horny")
                g4 "(Yes, take it right on your face you slut!)"

                call hide_characters
                hide screen bld1
                with d3
                call cum_block
                call gen_chibi("cum_behind_desk")
                with d3
                pause.8

                call cum_block
                call bld
                g4 "{size=-5}*Argh*! YES!{/size}"

                call her_main("", "annoyed", "base", "base", "mid", cheeks="blush")
                call ton_main("Are you okay, professor? You're awfully quiet...","base","base","raised","mid", cheeks="blush")
                call her_main("(.............)", "soft", "base", "base", "mid")
                call gen_chibi("cum_behind_desk_done")
                with d3
                pause.2
                call bld
                m "Oh... yes, I was just so engaged in the conversation."
                call ton_main("Oh really?", "horny", "narrow", "raised", "mid")
                call ton_main("What were we talking about then?","base","base","angry","mid")
                m "Fast...{w=0.4} blended...{w=0.6} fruits?"
                call ton_main("Right...", "open", "closed", "raised", "mid", hair="basic")
                call ton_main("Well, then... I think we're done here...", "base", "narrow", "raised", "R")
                call her_main("...", "normal", "base", "base", "R", cheeks="blush")
                if game.daytime:
                    call ton_main("I'll leave you two to it, have a good day, Miss Granger.","base","base","base","L")
                    call her_main("Good day, professor Tonks.", "soft", "base", "base", "R")
                else:
                    call ton_main("I'll leave you two to it, have a good night, Miss Granger.","base","base","base","L")
                    call her_main("Good night, professor Tonks.", "soft", "base", "base", "R")
                call ton_main("Professor...","horny","base","raised","mid")
                m "Miss Tonks..."

                call ton_walk(action="leave")

            else:
                call ton_main("Oh no, those poor things!", "upset", "base", "worried", "mid", hair="basic")
                call her_main("...", "annoyed", "base", "base", "R")
                call ton_main("That's not how you're supposed to care for a Blast-ended skrewt...","open","closed","angry","mid")
                call ton_main("Wait, what is a {i}Blast-ended Skrewt{/i} actually?", "upset", "base", "worried", "L")
                call her_main("It's some crossbreed that Hagrid has made... I don't know exactly how he managed it...", "annoyed", "narrow", "worried", "down")
                call ton_main("Sounds to me that this Hagrid fellow has been doing some illegal breeding...","upset","base","raised","mid")
                g9 "(He-he-he)"
                m "*Ahem*..."
                call ton_main("Although, all things considered!","open","closed","base","mid")
                call ton_main("It's probably nothing too bad.", "silly", "happyCL", "base", "mid")

                call ton_main("Well then, I think we're done here.", "open", "base", "worried", "mid")
                call ton_main("I'll leave you two to it...","base","base","base","mid")
                if game.daytime:
                    call ton_main("Have a good day, Miss Granger.","base","base","base","L")
                    call her_main("Good day, professor Tonks.", "open", "base", "base", "R")
                else:
                    call ton_main("Have a good night, Miss Granger.","base","base","base","L")
                    call her_main("Good night, professor Tonks.", "open", "base", "base", "R")
                call ton_main("Professor...","horny","base","raised","mid")
                m "Miss Tonks..."

                call ton_walk(action="leave")

        "\"Yourself.\"":
            call her_main("Well...", "angry", "narrow", "worried", "down")
            call ton_main("Yes...","base","base","raised","L")
            call ton_main("What does our Headmaster ask of you to earn those house points?","horny","base","angry","mid", hair="horny")
            g4 "..."
            if masturbating:
                g9 "(Let's take a short break, my hands are getting tired.)"
                call gen_chibi("sit_behind_desk")
            call her_main("I...", "angry", "happyCl", "worried", "mid")
            call ton_main("Go on, I'm sure the Headmaster doesn't mind.", "grin", "narrow", "raised", "L")
            call ton_main("My lips are sealed. {heart}","horny","base","base","mid")
            call her_main("Professor...", "disgust", "narrow", "base", "down")
            m "Miss Granger, your professor asked you a question..."
            call her_main("But, I thought it was supposed to stay between just you and I...", "disgust", "narrow", "base", "mid_soft")

            menu:
                "\"That's true\"":
                    m "Then let's end it here for today..."
                    call ton_main("But sir...", "open", "base", "worried", "mid", hair="sad")
                    m "Tonks..."
                    call ton_main("Fine...", "upset", "base", "worried", "down", hair="basic")
                    call ton_main("I've thoroughly enjoyed it, in any case.", "base", "base", "base", "L")
                    g9 "Good to hear."
                    call ton_main("I'll leave you two to it...","base","base","base","mid")
                    if game.daytime:
                        call ton_main("Have a good day, Miss Granger.","base","base","base","L")
                        call her_main("Good day, professor Tonks.", "open", "base", "base", "R")
                    else:
                        call ton_main("Have a good night, Miss Granger.","base","base","base","L")
                        call her_main("Good night, professor Tonks.", "open", "base", "base", "R")

                    call ton_walk(action="leave")

                    call bld
                    m "(She ignored me...?)"
                    if masturbating:
                        m "(And I just got blue-balled, bollocks...)"
                    $ masturbating = False

                "\"Tonks isn't some kind of snitch\"":
                    m "I'm sure we can take Miss Tonks at her word."
                    call her_main("But...", "disgust", "narrow", "worried", "mid_soft")
                    m "I'm sure Miss Tonks would be happy to provide additional points, as you'd basically be providing a favour for us both."
                    call ton_main("*Hmmm* Oh yes, I'd love to be of help for the Gryffindor house.", "horny", "base", "base", "mid", hair="horny")
                    call her_main("In that case I want another five points.", "annoyed", "base", "base", "mid")
                    m "That can be arrange--"
                    call ton_main("Done!","base","base","angry","mid")
                    $ current_payout = 10
                    if masturbating:
                        call gen_chibi("jerk_off_behind_desk")
                        m "(This should be good...)"
                    call her_main("W-{w=0.3}What would you like to know about then?", "open", "base", "base", "R", cheeks="blush")
                    call ton_main("I'd be happy with anything you'd like to tell me...","base","base","base","L")
                    call her_main("Well... it's quite embarrassing.", "disgust", "narrow", "worried", "down", cheeks="blush")
                    call ton_main("Yes?", "soft", "base", "raised", "L")
                    if hg_pf_strip.counter > 1:
                        call her_main("Well, he asked me to dance for him...", "open", "narrow", "base", "R_soft", cheeks="blush")
                        call ton_main("Yes... dance...","open","base","raised","R")
                        if masturbating:
                            g4 "(And you loved every second of it, that butt bouncing around...)"
                    else:
                        call her_main("Well, he made me show him my panties...", "open", "narrow", "base", "R_soft", cheeks="blush")
                        call ton_main("Panties, you say...", "base", "base", "raised", "L", cheeks="blush")
                        if masturbating:
                            g4 "(And you loved every second of it, I bet you were totally wet under those panties!)"
                            if hermione.is_worn("panties"):
                                g9 "(Not that you wear any anymore, don't you [hermione_name]?)"
                    call ton_main("And how did that make you feel?", "soft", "base", "raised", "L", cheeks="blush")
                    call her_main("Humiliated!", "annoyed", "narrow", "base", "R_soft", cheeks="blush")
                    call ton_main("And your headmaster, did he enjoy it?", "base", "narrow", "raised", "mid")

                    if masturbating:
                        if hg_pf_strip.counter > 1:
                            call her_main("He did seem to enjoy it.", "open", "closed", "base", "mid", cheeks="blush")
                            g4 "(Yes! I thoroughly enjoyed that little show of yours, you slut!)"
                        else:
                            call her_main("He did seem to enjoy... them.", "soft", "narrow", "base", "down", cheeks="blush")
                            g4 "(Yes! Panties!)"

                        call hide_characters
                        hide screen bld1
                        with d3
                        pause.2
                        call cum_block
                        call gen_chibi("cum_behind_desk")
                        with d3
                        pause.8

                        call cum_block
                        call bld
                        g4 "{size=-5}*Argh!* YES!{/size}"

                        call her_main("", "annoyed", "base", "base", "R")
                        call ton_main("Seems like the headmaster enjoyed our little discussion...","horny","base","angry","mid", hair="horny")
                        call her_main("(.............)", "soft", "base", "base", "mid")

                        call gen_chibi("cum_behind_desk_done")
                        with d3
                        pause.2

                        call bld
                        g4 "*Ah-Ah*..."
                        call ton_main("What have you been doing back there?", "soft", "narrow", "raised", "mid", hair="horny")
                        m "I--"
                        call her_main("H-{w=0.3}he isn't doing anything! Isn't that right, Professor?", "angry", "happyCl", "worried", "mid", cheeks="blush")
                        call her_main("Just *Ehm*...{w=0.5} stretching your leg, as always.", "crooked_smile", "base", "worried", "mid", cheeks="blush")
                        call ton_main("Right...", "normal", "base", "shocked", "R")
                        call ton_main("Well then, since my work here is done... I need to go back to my regular duties.","open","closed","base","mid", hair="basic")

                    else:
                        m "I sure what--"
                        call ton_main("I'm asking miss Granger.","upset","base","base","mid")
                        m "Oh, of course!"

                        call her_main("He did seem to enjoy it.", "open", "closed", "base", "mid", cheeks="blush")
                        call her_main("Maybe a bit too much even...", "angry", "narrow", "base", "R_soft", cheeks="blush")
                        call ton_main("That just means you did a great job, Miss Granger.","base","base","base","L")
                        call ton_main("Your house surely benefited even more from it.","horny","base","raised","L")
                        call her_main("True...", "soft", "base", "base", "R", cheeks="blush")
                        call ton_main("Well, I do believe we're done here...","open","closed","base","mid", hair="basic")
                        call ton_main("You've done a great, job Miss Granger.","open","base","base","L")
                        call ton_main("The Gryffindor house should be proud to have you.","base","base","base","mid")
                        m "Yes..."
                        m "That surely was something, Miss Granger..."
                        call ton_main("It was... I'm glad you two called me...", "silly", "happyCl", "base", "mid")
                        call ton_main("This conversation has been very enlightening.","horny","base","base","mid", hair="horny")

                    call ton_main("I'll leave you two to it...","base","base","base","mid", hair="basic")
                    if game.daytime:
                        call ton_main("Have a good day, Miss Granger.","base","base","base","L")
                        call her_main("Good day, professor Tonks.", "open", "base", "base", "R")
                    else:
                        call ton_main("Have a good night, Miss Granger.","base","base","base","L")
                        call her_main("Good night, professor Tonks.", "open", "base", "base", "R")
                    call ton_main("Professor...","horny","base","raised","mid")
                    m "Miss Tonks..."

                    call ton_walk(action="leave")


    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)
    $ tonks_busy = True

    return
