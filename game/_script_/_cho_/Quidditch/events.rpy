
# Training Intro 1. (Hufflepuff)

label cho_quid_E1:
    # Genie should get into a drill sergeant mood here, but fails at the end.

    call cho_main(xpos="mid", ypos="base", trans=fade)

    m "Are you ready for your first training session?"
    call cho_main("Of course, Professor!", "smile", "base", "base", "mid")
    g4 "Professor? Who are you calling Professor, girl?"
    call cho_main("I'm... sorry?", "soft", "base", "worried", "mid")
    m "From now on you will address me only as \"Sir\"!{w} Or..."

    menu:
        "\"Coach\"":
            $ cho_genie_name = "Coach"
        "\"Sergeant\"":
            $ cho_genie_name = "Sergeant"
        "\"Captain\"":
            $ cho_genie_name = "Captain"
        "\"Professor\"":
            $ cho_genie_name = "Professor"
            m "You know what, keep calling me Professor..."

    call cho_main("Yes, [cho_genie_name].", "base", "base", "angry", "mid")
    m "And you I will call..."

    menu:
        "\"Cadet\"":
            $ cho_name = "Cadet"
        "\"Pilot\"":
            $ cho_name = "Pilot"
        "\"Maggot\"":
            $ cho_name = "Maggot"
            call cho_main("(...)", "quiver", "base", "worried", "R")
        "\"Eagle #1\"":
            $ cho_name = "Eagle #1"
        "\"Eagle #2\"":
            $ cho_name = "Eagle #2"
        "\"Cho\"":
            $ cho_name = "Cho"

    call cho_main("Yes, Sir!", "soft", "closed", "angry", "mid")
    g4 "Let's start with your {i}Quiddesh{/i} training!"
    call cho_main("\"Quidditch\", Sir.", "annoyed", "narrow", "angry", "mid")
    g4 "Let's start with your \"Quidditch\" training, [cho_name]."
    call cho_main("!!!", "smile", "happyCl", "base", "mid", cheeks="blush")
    call cho_main("Shall I call the rest of my team up here?", "open", "base", "base", "mid")
    m "What? Why?"
    call cho_main("So they can hear your expertise as well, of course.", "soft", "narrow", "base", "mid")
    m "I don't think that will be necessary."
    m "Let's focus on you, for the moment..."
    call cho_main("Very well, [cho_genie_name].", "soft", "base", "worried", "R")
    m "Tell me, how did you usually play?{w} Why were you always losing?"
    call cho_main("Well, Hufflepuff has a really good seeker!", "open", "base", "base", "mid")
    call cho_main("He's always catching the snitch before me.", "quiver", "narrow", "worried", "down")
    call cho_main("I don't know how he does it, to be honest. It always happens so quick...", "open", "narrow", "worried", "mid")
    m "And you are \"both\" looking for that thing? At the same time?"
    call cho_main("Yes, [cho_genie_name].", "soft", "base", "base", "mid")
    call cho_main("I do my best flying around the pitch searching for it. But it's just so small and really tricky to see...", "angry", "base", "worried", "down")
    m "Why don't you look for it together? After all there is only one."
    call cho_main("*Hmmm*?", "annoyed", "base", "base", "mid")
    g9 "You just need to grab that Snatch before he does."
    call cho_main("???", "annoyed", "wide", "raised", "mid")
    call cho_main("[cho_genie_name]! It's \"Snitch\"!", "angry", "closed", "angry", "mid")
    m "Potato {i}potato{/i}..."
    call cho_main("You just said the same thing twice...", "open", "base", "raised", "R")
    m "Exactly..."
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("But what am I supposed to do once he catches sight of it?", "open", "narrow", "base", "mid")
    m "Catches the sight of what?"
    call cho_main("The snitch!", "annoyed", "narrow", "base", "mid")
    m "Oh, I see..."
    call cho_main("There wouldn't be a way for me to stop him. With how determined he is... and how fast he can be...", "open", "base", "base", "R")
    g9 "Well, lucky for you, you have me!"
    call cho_main("", "annoyed", "base", "raised", "mid")
    g9 "I'm also very fast and determined!"
    m "And you just gave me a great idea."
    m "We'll need to distract him!"
    g4 "So you can get a hold of that Snatch before he does!"
    call cho_main("Please stop saying that, [cho_genie_name]!", "angry", "closed", "angry", "mid")
    m "Saying what?"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("{size=-4}\"Snatch.\"{/size}", "soft", "narrow", "angry", "mid")
    g9 "*Hehehehe*{w} Now you've said it!"
    call cho_main("Could we please just talk about your plan, [cho_genie_name]?", "open", "narrow", "angry", "R")
    m "Patience, Miss Chang."
    call cho_main("Tell me!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("", "annoyed", "narrow", "angry", "mid")

    m "We'll hit him where he least expects it!"
    call cho_main("And that would be?", "soft", "base", "angry", "mid")
    m "The balls!"
    call cho_main("What?!?", "mad", "wide", "raised", "mid")
    call cho_main("Sir, surely you can't be--", "clench", "base", "angry", "mid")
    m "If we entice him during the game he'll lose focus..."
    call cho_main("Entice...{w=0.4} what are you...", "clench", "base", "base", "mid")

    call cho_main("Sir, this is just ridiculous!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("I thought a highly regarded wizard of your stature would know at least something that could help us at Quidditch.", "open", "narrow", "angry", "mid")
    call cho_main("I didn't hold it against you that you seemingly know very little about the sport.", "open", "base", "angry", "R")
    m "Which I proved you wrong, but who cares..."
    call cho_main("Even with my limited time I thought it was at least worth a try.{w} But hearing your suggestions now...", "angry", "narrow", "angry", "mid")
    m "You will learn soon enough, girl."
    m "It's very clear that to win we'll have to go beyond normal conventional methods."
    g4 "The only way you can keep a man from fulfilling his sought-out purpose, is by confronting him with his most primal instinct!"
    call cho_main("Which would be?", "annoyed", "narrow", "angry", "mid")
    g9 "The act of procreation!"
    call cho_main("Sir, are you suggesting I should have \"sex\" with him?!", "soft", "wide", "base", "mid") # Shocked
    m "What? I never said that..."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    g9 "You have a really dirty mind, girl!"
    call cho_main("But you just said--", "angry", "closed", "angry", "mid")
    m "I merely want you to distract him with your body, during the match."
    g9 "And then, when he can't keep his eyes off you..."
    g9 "You grab that Snatch!"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("I'm sorry Sir, but I feel methods like those would get us nowhere!", "open", "closed", "raised", "mid")
    call cho_main("And it's very improper for a teacher to suggest such things! Not to mention right out vulgar!", "open", "base", "angry", "R")
    call cho_main("I'll be leaving now.{w=0.8} Please only call me should you decide to finally take things seriously...", "soft", "narrow", "angry", "mid")
    g9 "And you, think about using that petite body of yours to get closer to your dreams!"
    call cho_main("*Tzzzz*", "angry", "closed", "angry", "mid")

    if game.daytime:
        call cho_main("Good day, Sir...", "soft", "narrow", "angry", "mid")
    else:
        call cho_main("Good night, Sir...", "soft", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call popup("You've lost the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/cho.webp")

    call bld
    m "She'll get over it..."

    # Flags
    $ cho_mood += 9
    $ cho_quid.E1_complete = True

    jump end_cho_event

label cho_quid_E2:
    # Genie regains ability to train Cho

    call cho_main(xpos="mid",ypos="base", trans=fade)
    m "So, have you consider going with my training methods?"
    call cho_main("I... Yes...", "soft", "closed", "angry", "mid")
    call cho_main("I've simply run out of options.{w=0.8} If we want to win the cup this year, you're the only hope we have left...", "open", "narrow", "angry", "mid")
    call cho_main("I have no choice but to try your methods, Sir.", "annoyed", "narrow", "angry", "mid")
    g9 "I'm glad you've come to your senses."
    call cho_main("(...)", "annoyed", "narrow", "angry", "R")
    g9 "Let's get this ball rolling... flying then shall we!"
    call cho_main("(...)", "annoyed", "base", "base", "mid")

    m "I will show you."
    call cho_main("", "base", "base", "base", "mid")

    m "First, get your flying thing ready!"
    call cho_main("My broom?", "soft", "base", "raised", "mid")
    m "Broom... flying carpet... Whichever you prefer."
    call cho_main("Only brooms are allowed in Quidditch, Sir.", "annoyed", "base", "base", "mid")
    m "Good for you."
    m "And put on your Quidditch outfit while you're at it..."
    call cho_main("Yes, Sir.{w} Let me just go and get all of my equipment.", "smile", "base", "base", "mid")
    call cho_main("I'll be right back.", "base", "narrow", "base", "mid")

    call cho_walk(action="leave", speed=1.5) # Cho moves, excitedly.

    call blkfade
    pause .8

    # Scene Setup
    show screen chair_left
    show screen desk
    call gen_chibi("stand", "desk", "base")
    call cho_chibi("stand", "right", "base")

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    call hide_blkfade
    pause .8

    call cho_main("Ready when you are, [cho_genie_name]!", "smile", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    hide screen cho_main
    with d3

    # Tutorial menu
    $ _selected = [False, False, False]
    $ menu_y = 0.8

    label .choices:

    if not all(x == True for x in _selected): # Has selected every position once? Loop if the answer is no.
        call bld
        menu:
            m "Now..."
            "\"Fly in front of me.\"" if not _selected[0]:
                $ _selected[0] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                call cho_walk("mid", "base")
                if cho_chibi.flip == False:
                    m "Looking good, now turn away from me..."
                    call cho_chibi("fly", "mid", "base", flip=True)
                    with d5
                call cho_main("Like this?", "soft", "base", "base", "R", xpos="base", ypos="head")
                m "A bit higher maybe..."
                call cho_walk(550, 200+180)

                m "Excellent!"

                jump cho_quid_E2.choices

            "\"Fly above me.\"" if not _selected[1]:
                $ _selected[1] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                m "Move a bit higher."
                call cho_walk(600, 150+180)
                call cho_main("Like this?", "soft", "base", "base", "downR", xpos="base", ypos="head")
                m "Great, you've got some excellent control over that stick."

                jump cho_quid_E2.choices

            "\"Fly close to me.\"" if not _selected[2]:
                $ _selected[2] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                cho "How close?"
                m "As close as you can get..."
                call cho_walk(450, 240+180)
                m "Nice, and you could hold this position during movement?"
                cho "Of course..."
                m "Great!"

                jump cho_quid_E2.choices
    else:
        pass

    m "That should be enough..."
    m "You can come down now."
    cho "Okay."

    #Cho flies down
    call cho_walk("mid", "base")
    call cho_chibi("stand", "right", "base")
    with fade


    m "Great job, we should definitely use positioning to our advantage!"
    call cho_main("Well, that much is true for any quidditch game...", "open", "base", "raised", "mid")
    call cho_main("I don't really see what we've achieved here.", "soft", "base", "raised", "R")
    m "All in due time, [cho_name]..."
    m "With my training methods you'll have the upper hand over those other teams, I'm sure of it."
    call cho_main("I'll have to take you for your word then...", "base", "base", "raised", "mid") #cautious smile
    m "That's all for today."
    call cho_main("Already? I usually train for a couple of hours!", "angry", "base", "raised", "mid")
    m "Yes, I need to come up with a pl...{w=0.3} prepare for our next session!"
    call cho_main("Oh... okay.", "soft", "base", "base", "down")
    call cho_main("Bye then.", "base", "base", "base", "mid")
    m "Bye, Miss Chang."

    call cho_walk(action="leave")

    m "(Now to find out what the boy's into and make sure she's prepared to do what it takes...)"
    call popup("You've unlocked Cho private favours!", "Congratulations!", "interface/icons/head/cho.webp")

    # Flags
    $ cho.equip(cho_outfit_last)
    $ cho_quid.E2_complete = True
    $ cho_favors_unlocked = True
    $ cho_quid.lock_training = False

    jump end_cho_event

label cho_quid_E3:
    # Commentator disaster, Lee Jordan is unable to commentate.

    call cho_walk(action="enter", "desk", "base", speed=1.5)

    call play_music("stop")

    call cho_main("[cho_genie_name], there's been a disaster!", "scream", "closed", "angry", "mid", xpos="mid", ypos="base", trans=hpunch)

    call play_music("cho")

    m "Off to a good start..."
    call cho_main("[cho_genie_name], something terrible happened to Lee Jordan!", "soft", "narrow", "worried", "mid")
    m "Lee Jordan?{w=0.5} Is that a famous basketball player I'm not aware of?"
    call cho_main("What?{w=0.5} No Sir, Lee is our quidditch commentator!", "soft", "narrow", "base", "mid")
    call cho_main("He got hit in the throat by a bludger!", "disgust", "base", "raised", "down")
    call cho_main("Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season.", "soft", "closed", "worried", "mid")
    call cho_main("What are we going to do! We can't have a Quidditch Cup without a commentator!", "soft", "base", "worried", "mid")
    m "Can't you play without one?"
    call cho_main("No. Someone has to announce the points after all.", "annoyed", "narrow", "base", "mid")
    m "I see..."

    $ _selected = [False, False]

    label .choices:
    menu:
        m "How about we ask..."
        "\"Hermione\"":
            pass

        "\"Astoria\"" if astoria_unlocked and not _selected[0]:
            $ _selected[0] = True

            call cho_main("That mischievous little...", "clench", "wide", "raised", "mid")
            call cho_main("Not a chance!", "open", "closed", "angry", "mid")
            call cho_main("Besides, [cho_genie_name]. Did you forget that she's a Slytherin?", "open", "narrow", "angry", "mid")
            m "Right. No Slytherins. Got it."
            m "How about..."

            jump cho_quid_E3.choices

        "\"Luna\"" if luna_unlocked and not _selected[1]:
            $ _selected[1] = True

            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?", "open", "narrow", "raised", "mid")
            m "Yes?"
            call cho_main("Surely{w=0.3}, nobody in their right mind would let Luna Lovegood commentate.", "grin", "happyCl", "base", "mid") # Book quote.
            #m "I am of right mind, Miss Chang...{w} and don't call me Shirley..."
            m "(...)"
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...", "open", "base", "base", "R")
            call cho_main("Trust me, [cho_genie_name]. Luna would be a terrible choice!", "soft", "narrow", "base", "mid")
            m "Fine. How about..."

            jump cho_quid_E3.choices

    call cho_main("Hermione Granger?", "scream", "wide", "raised", "mid")
    call cho_main("She wouldn't know the first thing about quidditch!", "clench", "narrow", "angry", "mid")
    call cho_main("You can't pick her!", "annoyed", "narrow", "angry", "mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    call cho_main("Absolutely not! I won't talk to that Gryffindor skunk ever again!", "scream", "closed", "angry", "mid")
    call cho_main("Didn't I make it clear that I don't want her to {b}ever{/b} be involved in Quidditch again?", "annoyed", "narrow", "angry", "mid")
    m "Alright... are there any other students who know Quidditch rules well enough to take this... Jordan boy's place?"
    call cho_main("...", "annoyed", "base", "base", "down")
    m "Well?"
    call cho_main("Well, most of them would be on one of the Quidditch teams...", "soft", "base", "raised", "R")
    call cho_main("But Granger wouldn't know anything about Quidditch either!", "annoyed", "narrow", "angry", "mid")
    m "Do you know anybody else suited for the job?"
    call cho_main("{size=-4}Probably anyone at this point...{/size}", "annoyed", "base", "raised", "R")
    call play_music("stop")
    call cho_main("(Wait a minute...)", "annoyed", "wide", "raised", "mid")
    play music "music/marty-gots-a-plan-by-kevin-macleod.mp3" fadein 1.0
    call cho_main("No...", "smile", "base", "base", "mid") #Mischievous smile
    g9 "I'll ask her... What's the worst that could happen..."
    call cho_main("Yeah, actually you're probably right...", "grin", "narrow", "angry", "mid")
    m "Don't worry she'll do a--"
    g4 "Wait... what did you say?"
    call cho_main("I'm sure she'll do a heckin' good job!", "smile", "narrow", "angry", "mid")
    call cho_main("(She'll flub the whole thing and everyone will laugh at her.)", "smile", "narrow", "angry", "R") #Mischievous smile
    g9 "Well, great then. I'll ask her in that case!"
    call cho_main("(She'll be so humiliated! And no one will ever see her as anything but a show-off that knows nothing!)", "grin", "narrow", "angry", "down")
    call cho_main("(I can already picture it...{w=0.8} the whole school laughing...)", "silly", "base", "raised", "up")
    m "Miss Chang?"
    call cho_main("Oh, thank you for handling it professor!", "open", "base", "base", "mid")
    call cho_main("Boy, you took a load off my mind...", "silly", "happyCl", "base", "mid", trans=hpunch)
    m "(...)"
    call cho_main("I'll be heading back to class, if you don't mind.", "soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(...)"

    # Reset
    $ cho.equip(cho_outfit_last) # Equip last worn clothes
    $ cho_quid.E3_complete = True
    $ cho_quid.lock_practice = True

    jump end_cho_event

label cho_quid_E4:
    # Genie asks Hermione if she would agree to commentate the game.

    call her_main(xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I mean, I've taken flying lessons... they're mandatory.", "open", "base", "base", "R")
    m "Ah, okay... and here I was hoping that you'd be able to commentate this years quidditch games..."
    call her_main("Me, wasting time on something as stupid as--", "base", "closed", "base", "mid")
    call her_main("Wait...{w=0.3} What did you say?", "open", "squint", "base", "mid")
    m "I was going to ask you if you'd commentate this year's quidditch games..."
    call her_main("You want me... to commentate this year's Quidditch cup?", "open", "wide", "base", "mid")
    call her_main("I'd be honoured, sir!", "scream", "closed", "base", "mid", trans=hpunch)
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...", "open", "base", "angry", "mid")
    call her_main("Not to mention getting to make all the announcements...", "smile", "base", "base", "R")
    call her_main("The speeches...", "grin", "happy", "base", "mid")

    if her_whoring < 18:
        call her_main("The paper...", "soft", "narrow", "annoyed", "up")
        call her_main("The {heart}{b}preparation{/b}{heart}...", "open_tongue", "narrow", "base", "up")
    else:
        call her_main("Everybody will be focused on me...", "soft", "narrow", "annoyed", "up")

    call her_main("I accept!", "scream", "closed", "angry", "mid", trans=hpunch)
    g4 "I thought you just said you didn't--"
    call her_main("Cho will be so mad!", "crooked_smile", "happy", "base", "mid")
    m "I see..."
    g9 "Congratulations then, [hermione_name]! You got the job."
    call her_main("Ah!!! I better start learning--{w=0.4} I mean, preparing my opening speech!", "open", "wide", "base", "mid", trans=hpunch)

    call her_walk(action="leave", speed=1.5)

    call bld
    m "Aaaa-nd, she's gone..."
    m "I better tell Cho about the...{w=0.8} news."

    $ cho_quid.E4_complete = True

    jump end_hermione_event # This is correct, it's Hermione talking!

label cho_quid_E5:
    # Slytherin Quidditch intro. Triggers after you summon Cho.

    stop music fadeout 6.0

    call cho_walk(action="enter")
    call cho_walk("mid", "base")

    if game.daytime:
        call cho_main("Good morning, [cho_genie_name]...", "annoyed", "narrow", "worried", "downR", xpos="right", ypos="base", trans=d3)
        m "Mornin'."
    else:
        call cho_main("Good evening, [cho_genie_name]...", "annoyed", "narrow", "worried", "downR", xpos="right", ypos="base", trans=d3)
        m "Evenin'."
    m "[cho_name], before we get back to our usual diversions, why don't we have a little chat about the recent happenings?"
    call cho_main("Very well, [cho_genie_name]...", "open", "narrow", "worried", "mid")
    m "Cheer up, will you..."
    m "Where did that high-spirit from your \"big win\" fly off to?"
    call cho_main("Nowhere, [cho_genie_name]...{w=0.6} I'm still very happy we won the game, it's just...", "open", "narrow", "worried", "down") # worried/sad
    call cho_main("I'm a bit worried about the future.", "soft", "narrow", "worried", "mid") # sad/relieved
    m "The future?"
    m "You didn't get pregnant during your little celebration event, did you?"

    call play_music("cho")
    call cho_main("WHAT?!", "clench", "wide", "base", "mid", cheeks="heavy_blush")  # Upset/whatthefuck face
    call cho_main("Sir, why would you even suggest that?!", "angry", "narrow", "angry", "mid", cheeks="blush") # upset
    m "Then what is it?"
    call cho_main("It's about the upcoming quidditch match.", "annoyed", "narrow", "angry", "R") # annoyed - eyes R, mouth annoyed
    m "Oh...{w=0.4} Of course..."
    m "{size=-6}Always some stupid quest...{/size}"
    call cho_main("Pardon?", "annoyed", "narrow", "raised", "mid")
    m "It's nothing,{w=0.5} please continue."
    call cho_main("[cho_genie_name], I worry that we won't be able to beat Slytherin in the next match.", "annoyed", "narrow", "worried", "mid") # eyebrows sad, eyes mid, mouth pout
    g9 "Slytherin is next?{w=0.6} Sweet!"
    call cho_main("They're an entirely different ballpark compared to Hufflepuff.", "open", "base", "worried", "mid")
    m "Really? Why's that?"
    call cho_main("They're brutal and ruthless!{w} And they think they can get away with anything...", "open", "narrow", "angry", "mid") # eyebrows sad, eyes mid, mouth pout
    m "Then we should do the same, shouldn't we?"
    call cho_main("", "annoyed", "narrow", "base", "mid")
    m "We'll show those Slytherins what {b}we{/b} got -- no problem!"
    call cho_main("...", "base", "base", "base", "mid") # slight smile
    g9 "(And show Snape who's boss.)"
    m "Trust me, our tactics have worked perfectly thus far, haven't they?"
    call cho_main("I--{w=0.3} yes...", "soft", "base", "raised", "downR")
    call cho_main("You're right! Thank you, [cho_genie_name].", "base", "base", "base", "mid") # happy

    $ cho_quid.E5_complete = True
    $ cho_favors_unlocked = True

    jump cho_requests

label cho_quid_E6:
    # Hermione refuses to commentate Slytherin match.
    stop music fadeout 3.0

    pause 1.0

    call her_walk(action="enter")
    call chibi_emote("thought", "hermione")
    pause 2.0
    call chibi_emote("hide", "hermione")

    call bld
    m "..."

    call her_walk("desk", "base")
    call her_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base") # annoyed
    pause .5
    call her_main("I can't believe her...", "clench", "closed", "angry", "mid", trans=hpunch) # angry
    m "Good day to you too..."

    call play_music("hermione")

    call her_main("That bitch has been walking around saying that I quit the commentator job.", "open", "base", "angry", "mid")
    m "Who did?"
    call her_main("Cho Chang.", "soft", "base", "angry", "mid")
    g4 "..."
    m "Wait, so you didn't quit?"
    call her_main("No! Why would I be here telling you this if I did?", "angry", "base", "angry", "mid")
    m "I guess you would've had to give me a two weeks notice..."
    call her_main("You tell me, you're the one that appointed me.", "annoyed", "narrow", "annoyed", "mid")
    m "Oh, right."
    call her_main("And since I didn't sign anything...", "soft", "closed", "base", "mid")
    call her_main("I quit!", "soft", "narrow", "base", "mid")
    g4 "What?{w=0.5} You can't do that!"
    call her_main("Why not? After all, I'm terrible at it, aren't I?", "clench", "base", "angry", "mid")
    call her_main("I made such a fool out of myself during the Hufflepuff game...", "upset", "base", "worried", "R", tears="soft") # Sad, tears
    call her_main("And now with the Slytherin team being next...", "open", "happyCl", "worried", "mid", tears="soft_blink")
    call her_main("I won't just stand there and have them laugh at me...", "open", "base", "worried", "mid", tears="soft")
    call her_main("I'm not giving those Slytherins that satisfaction!", "annoyed", "base", "worried", "R", tears="soft")

    menu:
        m "(...)"
        "\"Tough luck, Miss Granger!\"":
            $ her_mood += 16

            call her_main("Tough luck?!", "clench", "wide", "base", "stare")
            m "You agreed to do this, remember..."
            g4 "May I remind you how many house points I gave you?"
            call her_main("No amount of house points was worth the humiliation I got!", "angry", "base", "angry", "mid")
            m "Well, *boo* --{w=0.3} bloody --{w=0.3} *hoo*..."
            call her_main("*Tzzzs*!...", "clench", "closed", "angry", "mid", emote="angry")
            call her_main("Good luck finding somebody that is more willing to be the school's laughing stock!", "open", "base", "angry", "mid")


        "\"We'll look for somebody more competent, then.\"":
            $ her_mood += 10

            call her_main("More competent?!", "clench", "base", "angry", "mid")
            m "Surely we can find a replacement for you in no time."
            call her_main("Well if that's the case, it seems like I'm no longer needed...", "open", "base", "angry", "mid")

        "\"All you need is a bit of practice...\"":
            if hg_pf_sex.counter == 0:
                g9 "(And a good fucking, but we'll get to that...)"
            else:
                g9 "(And a good fucking...)"
            m "You're a natural at this!"
            call her_main("...", "annoyed", "base", "worried", "mid", tears="soft")
            call her_main("It doesn't matter...", "soft", "base", "worried", "R", tears="soft")
            call her_main("Thanks to Cho, everybody now thinks I'm a fraud...", "open", "happyCl", "worried", "mid", tears="soft_blink")
            call her_main("I don't understand why she feels the need to constantly spread rumours about me.", "annoyed", "base", "annoyed", "R", tears="soft")
            m "(Look who's talking...)"

    call her_main("You can tell that bitch to look for somebody else to commentate!", "open", "base", "angry", "mid")
    call her_main("Because I will not!", "clench", "base", "angry", "mid")
    m "..."
    call her_main("Good day, Sir.", "annoyed", "base", "annoyed", "R")

    #Hermione walks out
    call her_walk(action="leave")
    call bld

    g4 "(What in the great desert sands do these women want from me...)"
    m "(Can't they get along like me and my ol' pal Snape?)"

    $ cho_quid.E6_complete = True

    jump end_hermione_event

label cho_quid_E7:
    # Genie blackmails Hermione

    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    m "[hermione_name], could I change your mind about your role in the Slytherin match?"
    call her_main("My answer is still no, [genie_name].", "open", "closed", "base", "mid")
    g4 "Come on!"
    call her_main("That's my final answer.", "annoyed", "narrow", "angry", "mid")
    m "(This girl...)"
    m "What if..."

    menu:
        "\"I'll give you house points.\"":
            call her_main("Not...{w=0.3} interested.", "annoyed", "narrow", "angry", "R")
            g4 "But you're always eager for those points!"
            call her_main("No amount of points would be worth it.", "open", "base", "angry", "mid")
            m "So, you don't even want to hear my offer?"
            call her_main("I guess I don't...", "open", "closed", "base", "mid") # upset
            m "Your loss..."

        "\"You could make fun of those Slytherins.\"":
            if her_tier >= 5:
                call her_main("I'm not that childish, [genie_name].", "annoyed", "base", "base", "mid")
                m "You're not?"
                m "So what they're doing doesn't bother you? Calling you all sorts of names?"
                call her_main("Not in the slightest...", "soft", "narrow", "base", "mid")
                call her_main("They can act like the usual dorks if they want to, that's no concern to me.", "soft", "base", "base", "R", cheeks="blush")
                call her_main("But I have no reason to stoop down to their level.", "open", "closed", "base", "mid")
            else:
                call her_main("And why would I want to do that? I'm not that foolish!", "open", "base", "annoyed", "mid")
                call her_main("Bad-mouthing their entire team would make me an even bigger target than I already am.", "annoyed", "base", "base", "R")
                call her_main("Besides, I wouldn't really be able to mock them with a teacher present.", "open", "closed", "base", "mid")
                call her_main("Madam Hooch would be unquestionably against that.", "open", "narrow", "base", "mid")

    m "..."
    call her_main("I wont step a foot on that podium, [genie_name].", "base", "base", "base", "mid")
    call her_main("There's nothing you could tempt me with that would change my mind.", "base", "base", "base", "mid")
    m "Well then..."
    g4 "(No more mister nice guy...)"
    call her_main("[genie_name]?", "soft", "wink", "base", "mid")
    m "[hermione_name], you're going to commentate that match. Whether you like it or not."
    call her_main("No! You can't change my mind on this!", "annoyed", "base", "angry", "mid")
    g9 "Are you sure about that?"
    call her_main("Why?", "annoyed", "narrow", "angry", "mid") # suspicious

    menu:
        g9 "[hermione_name]..."
        "\"I heard Cho has a crush on you!\"":
            $ d_flag_01 = True
            call her_main("She has a--{w=0.5} What?", "open", "wide", "base", "stare")

        "\"I heard you have a crush on Cho!\"":
            $ d_flag_01 = False
            call her_main("But--{w=0.3} That's not true!", "open", "wide", "base", "mid")

    call her_main("That's a lie!", "clench", "base", "angry", "mid") # angry
    call her_main("Not even Cho would agree to this!", "open", "base", "angry", "mid")
    g9 "Why don't we ask her?"
    call her_main("What?", "angry", "base", "base", "mid")
    call her_main("[genie_name], you can't do this!", "open", "base", "angry", "mid")
    g9 "Sure I can."

    call hide_characters
    call nar(">You telepathically call Cho into your office.")

    hide screen bld1
    with d3
    pause .2

    if her_tier < 4: # Hermione changes into her school outfit
        # TODO Does this even make sense? She's supposed to be comfortable enough to wear her clothes around the school anyway
        call nar(">While Hermione hastily puts on some less revealing clothes.")
        $ her_outfit_last.save()
        $ hermione.equip(her_outfit_default)
    else:
        $ hermione.wear("all")

    call her_walk("mid", "base")
    call chibi_emote("thought", "hermione")
    with d3
    pause .1

    # Summon Cho.
    call cho_walk(action="enter")
    pause 1

    call cho_walk(680, "base")
    pause .2

    call chibi_emote("hide", "hermione")
    with d3

    call her_main("", "annoyed", "base", "angry", "R", xpos="270", ypos="base", flip=True)
    call cho_main("Hello, Sir.", "base", "base", "base", "mid", xpos="close", ypos="base")
    call cho_main("Granger.", "soft", "narrow", "base", "L")
    call her_main("...", "annoyed", "base", "angry", "mid", cheeks="blush")
    call cho_main("How can I be of help?", "base", "base", "base", "mid")
    m "I have very good news for you, Miss Chang."
    m "Miss Granger and I were just discussing who should commentate the next Squidditch game."
    call cho_main("Oh, am I sensing a blackmail situation?", "crooked_smile", "base", "base", "mid")
    call her_main("Blackmailing?!{w=0.5} Me?", "open", "wide", "base", "stare") # shocked
    call cho_main("", "annoyed", "narrow", "base", "L")
    m "What other choice do we have? You're acting stubborn, Miss Granger."
    call her_main("So that's what's going on here. You two are scheming against me!", "angry", "base", "angry", "mid") # angry
    call cho_main("Come on, Hermione. You can't be {b}that{/b} scared of those Slytherins...", "open", "narrow", "raised", "L")
    call cho_main("Don't be such a coward...", "annoyed", "narrow", "angry", "L")
    call her_main("I am not!", "annoyed", "base", "angry", "R", cheeks="blush")
    call cho_main("Please! We need somebody to commentate.", "open", "narrow", "base", "L")
    call her_main("I won't do it! And neither of you can change my mind on this!", "angry", "base", "angry", "mid")
    g9 "I bet she can!"
    call cho_main("Me? How so?", "annoyed", "base", "raised", "mid")

    if d_flag_01: # Cho has crush
        m "Miss Chang, I've heard rumours that you have a huge crush on Hermione..."
        call cho_main("What? That's rubbish!", "open", "narrow", "angry", "mid")
        call her_main("...", "annoyed", "base", "angry", "mid")

    else: # Hermione has crush
        m "Miss Chang, I've heard rumours that Hermione secretly has a crush on you..."
        call cho_main("She does?", "soft", "base", "raised", "mid") # Surprised
        call her_main("No, I don't!", "clench", "happyCl", "angry", "mid")
        call her_main("It's just made up rubbish...", "open", "base", "angry", "mid")

    g9 "Rubbish or not, I'm sure Miss Granger wouldn't want such rumours to make their rounds now, would she?"
    call cho_main("", "annoyed", "base", "raised", "L")
    call her_main("*Pfff*...{w=0.3} As if anybody would believe that...", "annoyed", "base", "angry", "R")
    call cho_main("Oh, I get it now!", "base", "base", "base", "mid")
    call her_main("", "annoyed", "narrow", "angry", "L")
    call cho_main("You can count on me, Sir!", "crooked_smile", "base", "base", "mid")
    call cho_main("I don't mind if my reputation gets a bit tarnished, from being associated with her.", "open", "narrow", "angry", "L")
    call cho_main("For as long as it gets me closer to that cup...", "base", "narrow", "base", "mid")
    call her_main("You're such an idiot...", "clench", "happyCl", "angry", "mid")
    call her_main("I can't believe you'd stoop as low as blackmail for some stupid Quidditch Cup!", "open", "narrow", "angry", "L")

    if d_flag_01: # Cho has crush
        call cho_main("Don't be mean to me, Hermione.", "soft", "base", "base", "L")
        call cho_main("After all, I really, really like you!", "base", "narrow", "base", "L")
        call her_main("...", "annoyed", "narrow", "angry", "R") # looks away
        call cho_main("I love your bushy hair, your cute little nose, your gorgeous eyes...", "soft", "narrow", "raised", "L")
        call cho_main("Your enormous rack!", "grin", "narrow", "angry", "L")
        call her_main("*Tzzzs*!", "clench", "closed", "angry", "mid", cheeks="blush") # Starts to blush
        call her_main("Stop lying!", "open", "base", "angry", "L", cheeks="blush")
        call cho_main("", "horny", "narrow", "angry", "L", cheeks="blush")
        m "She sounds pretty convincing to me..."
        call cho_main("Everybody will know that I have a thing for you, Granger!", "open", "narrow", "angry", "L")
        call cho_main("And, sooner or later, I might even mix in some love potion into your pumpkin juice...", "soft", "narrow", "raised", "L")
        call her_main("You'd...{w=0.5} do what?", "clench", "wide", "worried", "stare", cheeks="blush")
        m "(Pumpkin juice? Sounds disgusting.)"
        call cho_main("You wouldn't want all of your friends to see us finally make out, would you?", "horny", "narrow", "raised", "L", cheeks="blush")

    else: # Hermione has crush
        call cho_main("Tell me, Granger...", "soft", "narrow", "raised", "L")
        call cho_main("What exactly do you like about me?", "base", "narrow", "angry", "L")
        call her_main("", "annoyed", "narrow", "angry", "L")
        call cho_main("Is it my hair? Or my strong legs? Or my abs?", "open", "narrow", "base", "down")
        call cho_main("Would you like me to show you my body again, right now?", "grin", "narrow", "base", "L")
        call her_main("No thanks.", "normal", "closed", "base", "mid")
        call cho_main("I should mix in some drops of Veritaserum into your pumpkin juice, and ask you again...", "annoyed", "narrow", "base", "L")
        call cho_main("Maybe then you'll speak the truth... How you really think of me.", "annoyed", "narrow", "raised", "mid")
        call her_main("You wouldn't!", "clench", "base", "angry", "L", cheeks="blush")
        call cho_main("Yes I would!", "base", "narrow", "base", "L")
        #g9 "(I need to get some of that stuff...)"
        #m "(The truth potion, not the pumpkin juice...)" #I feel like this give false expectations.
        m "(Pumpkin juice? Sounds disgusting...)"
        call cho_main("And I'll make sure that all your friends hear about it. Maybe I'll even let them watch!", "open", "narrow", "angry", "L")

    call her_main("Professor! You can't have her do that. That's insane!", "clench", "happyCl", "worried", "mid", cheeks="blush")
    call cho_main("", "annoyed", "narrow", "base", "up")
    m "That's all up to you, Miss Granger."
    g9 "All you have to do is agree to commentate again."
    call her_main("All the matches!", "clench", "base", "angry", "mid")
    call cho_main("", "annoyed", "narrow", "base", "L")
    m "What?"
    call her_main("I will commentate all the matches, the Gryffindor match as well! The one after this one, should Ravenclaw even get that far...", "open", "base", "angry", "mid")
    call cho_main("Oh no you won't! You'd be all in favour of Gryffindor!", "clench", "base", "angry", "L")
    call her_main("Yes I would. And I'll make sure that you lose.", "base", "narrow", "base", "L")
    m "Great. Finally we can get on with this..."
    call cho_main("Wait!--", "clench", "happyCl", "worried", "mid", cheeks="blush")
    m "Miss Granger, you better keep to this promise..."
    call her_main("", "base", "base", "base", "mid")
    call cho_main("(...)", "annoyed", "narrow", "angry", "L", cheeks="blush")
    g9 "If you don't show up I'll take a hundred points away from Gryffindor!"
    call her_main("That's just typical of you!", "annoyed", "narrow", "base", "mid")
    m "Make sure to be present..."
    call her_main("I will.", "annoyed", "narrow", "base", "L")
    m "You are both dismissed..."
    call her_main("...", "base", "base", "base", "mid")

    call her_walk(action="leave")
    pause .2

    show screen blkfade
    with d3

    call cho_chibi("stand","mid","base")
    hide screen blkfade
    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    m "I'd say that was a success."
    call cho_main("(...)", "annoyed", "narrow", "angry", "R")

    if game.daytime:
        call cho_main("Good day, Sir.", "open", "narrow", "angry", "mid")
    else:
        call cho_main("Good night, Sir.", "open", "narrow", "angry", "mid")

    call cho_walk(action="leave")

    pause 1.0
    call bld
    g9 "Quest complete!"

    $ cho_mood = 0

    $ hermione_busy = True
    $ cho_busy = True

    $ cho_quid.E7_complete = True

    if cho_quid.slytherin_training: # Finished practice match?
        $ cho_quid.lock_training = True

    # Reset
    if her_tier < 4:
        $ hermione.equip(her_outfit_last) # Equip player outfit.

    jump main_room

label cho_quid_E8:
    # Genie hangouts with Tonks, asks her for help with the Slytherins.

    m "I wanted to ask you for a favour..."
    call ton_main("Me? Selling a favour to you?", "grin", "closed", "base", "mid", ypos="head")
    call ton_main("You sure you can afford me?","base","base","raised","mid") #Horny
    m "Not that kind of favour."
    call ton_main("*Aww*...", "annoyed", "base", "raised", "down")

    # Tell Tonks about Cho.
    m "You know this {i}Quiddish{/i} sport the students play here?"
    call ton_main("Quidditch?","upset","base","raised","mid")
    m "Close enough."
    m "The next match is coming up, and I require your help with something."
    call ton_main("Of course. What is it?","base","base","base","mid")
    m "There's this asian girl..."
    call ton_main("Cho Chang?","open","base","raised","mid")
    m "How did you--"
    m "(Is she the {i}token asian{/i} girl in this school?)"
    m "Yes, the little Ravenclaw minx, correct."
    call ton_main("Well, I figured you'd be talking about her - if it has to do with Quidditch.","open","base","base","R")
    m "She's one of the girls I buy favours from."
    call ton_main("No way!", "open_wide", "shocked", "shocked", "mid", hair="horny")
    call ton_main("You got that little hotty--", "horny", "base", "raised", "R", hair="horny")
    call ton_main("*Uhm*... hot-head to sell you favours?", "mad", "base", "raised", "R")
    m "Once or twice..."
    call ton_main("Impressive.","horny","base","raised","mid")
    call ton_main("Tell me everything!","horny","base","angry","mid")

    menu:
        m "..."
        "-Tell her everything-":
            m "She's been stripping for me."
            call ton_main("Cho?! And I'm supposed to believe that?","upset","wide","raised","mid")
            g9 "Oh, you better believe it!"
            call ton_main("Holy shit!", "upset", "wide", "shocked", "stare", hair="horny")
            call ton_main("I'd pay so many galleons to watch that girl take her clothes off...", "base", "base", "raised", "R")
            call ton_main("You need to invite me next time!", "annoyed", "base", "angry", "mid", hair="angry") # angry
            m "And how would I get her to agree to that?"
            call ton_main("Well... *Uhm*...", "upset", "base", "worried", "down", hair="horny")
            m "It was difficult enough to get her to strip just for me..."
            m "She only did it because I helped her win against Hufflepuff."
            call ton_main("So that was your idea with the skirt? Very clever.", "horny", "base", "annoyed", "mid")
            m "Maybe I could arrange something once we've beaten those Slytherins..."
            m "For the two of you."
            call ton_main("Or all three of us!", "soft", "base", "raised", "mid")
            g9 "Yes!"
            g9 "I'm sure that minx would love that!"
            call ton_main("I can't wait!","base","happyCl","base","mid")

        "-Don't tell her-":
            m "I don't think I should..."
            call ton_main("What? Why not?", "open", "base", "worried", "mid")
            m "Miss Chang wouldn't like anybody to know."
            call ton_main("I can keep a secret!","upset","base","worried","R")
            m "I really shouldn't..."
            call ton_main("Tell me, or I'll jinx your balls off!","upset","base","angry","mid", hair="angry")
            g4 "*Ghzzz!* Alright! Alright!"
            m "You sure know how to get me to talk..."

    # Talk about Slytherin.
    m "..."
    m "But to get any further with her, I'll have to help her beat the opposing team in the next match."
    call ton_main("Slytherin? That shouldn't be too difficult.","open","base","raised","mid")
    m "Really? How so?"
    call ton_main("Their tactics revolve around strength, brute force, and manifesting their dominance on the field!","open","closed","angry","mid")
    call ton_main("A good strategy for when you're in bed with your partner, but not in Quidditch.","base","base","angry","mid")
    m "You don't say..."
    g4 "Wait, what?"
    call ton_main("I've seen them play a couple of times. They clearly aren't the brightest bunch...", "upset", "base", "annoyed", "R")
    call ton_main("What tactics are you gonna use against them?","base","base","raised","mid")
    g9 "I shouldn't ruin the surprise."
    call ton_main("Can't wait... If it's anything like the first game.","base","base","raised","R")
    m "The main hurdle right now is that I have no way to try out our tactics on the Slytherins..."
    m "They refuse to practice against Ravenclaw."
    call ton_main("Well that's unfortunate...", "upset", "base", "shocked", "L")
    call ton_main("Perhaps you could ask Snape. He should be able to get those lazy gits back on the pitch...","open","base","base","mid")

    if cho_quid.E9_complete:
        m "I already did. He isn't going to help me out..."
        call ton_main("Well that's just like him.","open","base","angry","R")
    else:
        m "I guess I could..."
        call ton_main("Yeah, maybe not...","open","closed","base","mid")

    call ton_main("Just leave it to me, Genie.","base","base","angry","mid")
    call ton_main("I'll get those shits back on the grass...", "mad", "base", "angry", "mid")
    m "And how will you accomplish that?"
    call ton_main("Oh, don't worry...", "silly", "happyCl", "base", "mid")
    call ton_main("Perhaps I'll tell you my techniques some other time.", "base", "narrow", "angry", "mid")

    m "..."
    if not cho_quid.E7_complete:
        # Has NOT blackmailed Hermione

        m "That's not all, though. There's something else I need your help with."
        call ton_main("You can't expect me to fix all of your problems, Genie.", "annoyed", "base", "base", "mid")
        m "It's about Hermione's role as a commentator..."
        call ton_main("Really? What happened to Miss Granger?","upset","base","worried","mid")
        m "She quit..."
        call ton_main("Hmm... that's too bad...", "open", "base", "worried", "R")
        call ton_main("But it's understandable... after all that mocking she had to go through last game.", "open", "base", "worried", "mid")
        call ton_main("Poor thing...", "mad", "base", "worried", "L")
        call ton_main("Have you tried talking to her?", "open", "base", "raised", "mid")
        m "Not yet..."
        call ton_main("Well, if anyone could convince her surely you'd be the one to be able to.", "base", "base", "base", "R")
        m "..."
        call ton_main("Why don't you tell her that a very special someone will be really disappointed if she doesn't show up.", "horny", "base", "base", "stare")
        g9 "(So it's not just me who thinks she's into Cho!)"
        call ton_main("(She was so cute fumbling over her words...)", "base", "happyCl", "base", "mid")
        call ton_main("I'm sure you'll be able to change her mind.", "base", "base", "base", "mid")
    else:
        m "Did you know Hermione wanted to quit her task as a commentator?"
        call ton_main("Did she now? I thought she did well in the Hufflepuff game.","upset","base","raised","mid")
        call ton_main("A bit wooden, but not bad for her first try.","open","base","base","R")
        call ton_main("Speaking in front of such a large crowd and all.","open","base","raised","mid")
        call ton_main("I thought it was rather cute listening to her fumble her words...","base","happyCl","base","mid")
        call ton_main("What changed her mind?","base","base","base","mid")
        m "Cho helped me convince her to do it."
        call ton_main("Really? How?","open","base","raised","mid")
        call ton_main("I'd love to hear it.","horny","base","angry","mid")
        m "*Hmm*... Maybe next time."
        call ton_main("Very well...", "upset", "base", "worried", "R")

    call ton_main("In any case, I could join you in the commentator booth during the next game to help encourage Miss Granger.", "open", "base", "base", "mid")
    call ton_main("If anything I'll get a nice view from up there.", "grin", "happyCl", "base", "mid")
    call ton_main("Since you already made sure Hufflepuff is out of the competition...", "upset", "base", "raised", "R")
    call ton_main("The best we can hope for now is to not get last...","open","closed","base","mid")
    call ton_main("It's always third or nothing with us Puffs.", "open", "base", "worried", "R")
    m "(Puffs?)"

    g9 "Well, I'd be happy to have you."
    call ton_main("*N'Aww*, you're so sweet!", "base", "base", "worried", "mid")
    with hpunch
    $ renpy.play("sounds/hiccup_fem.mp3")
    call ton_main("*Hick*!... whoopsie...", "upset", "wide", "base", "mid")
    call ton_main("Now, I better get going convincing those boys to play again...", "open", "base", "raised", "R", hair="horny")

    if game.daytime:
        ">You finish your drinks before calling it a day."
    else:
        ">You finish your drinks before calling it a night."

    $ tonks_busy = True
    $ cho_quid.E8_complete = True
    $ cho_quid.lock_practice = False
    $ cho_quid.slytherin_prepared = True # Unlocks practice match

    if game.daytime:
        jump night_start
    else:
        jump day_start

label cho_quid_E9:
    # Ask Snape for help, but it backfires (optional)

    call sna_main("Your precious Ravenclaw bird, made any breakthroughs with her yet?","snape_37", ypos="head")
    m "The little asian?"
    call sna_main("Yes, Miss Chang.","snape_40")
    m "..."
    call sna_main("I wish her best of luck against my team of Slytherins.","snape_02")
    call sna_main("She'll need it.","snape_45")
    g4 "What kind of game are you playing?"
    call sna_main("I'm sorry?","snape_38")
    m "Your team didn't show up for practice against Ravenclaw!"
    call sna_main("Well, there's no specific rule that forces the teams to practise against each other...","snape_05")
    m "There's not?"
    m "(Actually that does make sense...)"
    call sna_main("Of course not, but it is heavily encouraged for students that are looking to make it professionally.","snape_09")
    m "Do you have something to do with this?"
    call sna_main("I don't know what you're talking about...","snape_47") #Smirk
    g4 "You little weasel..."
    call sna_main("Ha! Do you have another trick up your sleeve?","snape_20")
    call sna_main("What's it gonna be? An even shorter skirt? Prohibit her from wearing panties?","snape_13")
    call sna_main("Well, we'll see during the game if it has any effect...","snape_46")
    g4 "*Grrrrr*!..."
    g4 "Get your team back on that pitch, you coward!"
    call sna_main("No... I don't think I will...","snape_41")
    g4 "Give me that wine!"
    call sna_main("You want some?","snape_20")
    call play_sound("spit") # Spits in the cup
    m "I'm gonna win that bet. Then I'll have the last laugh!"
    call sna_main("I wish you good fortune.","snape_22")
    m "..."
    g4 "Get your wine from some place else, you slacker."
    call sna_main("You won't win by making friends, isn't that right?","snape_18")
    m "..."
    call sna_main("*Hrhm*... Good riddance, then...","snape_12")
    $ renpy.sound.play(["sounds/gulp.mp3"]*3)
    call nar(">Snape empties the last drop of wine, before leaving.","start")
    ">You feel a sense of remorse shortly after he's gone, realizing that you're both just parts of the same coin."
    call nar(">Your friendship level with him has not changed...{w=0.5} Probably...","end")

    $ snape_busy = True
    $ ss_summon_pause = 5 # Snape can't be summoned for a couple of days. Can be set to 0 once you talked to Tonks.

    $ cho_quid.E9_complete = True

    if game.daytime:
        jump night_start
    else:
        jump day_start
