
# Mirror story: Panty raid
label panty_raid:

    $ temp_day = game.daytime
    $ game.daytime = True
    call update_interface_color
    call room("main_room")
    show screen blkfade
    with d5

    call reset_menu_position

    centered "{size=+7}{color=#cbcbcb}Panty Raid{/color}{/size}\n\n{color=#cbcbcb}Based on a story written by {size=+4}WaxerRed{/size}\n{size=-4}Proofreading & Editing by Lineup, Johnny and LoafyLemon\nImplementation by Lineup and LoafyLemon{/size}{/color}"

    label panty_raid_menu:
    show screen blkfade
    with d5

    menu:
        "For the best experience it is recommended to play the story in chronological order."
        "{size=-4}Part one{/size}\n-Defiance-":
            $ pathvalue = 0
        "{size=-4}Part two{/size}\n-Acceptance-":
            $ pathvalue = 1
        "{size=-4}Part three{/size}\n-Realization-":
            $ pathvalue = 2
        "{size=-4}Part four{/size}\n-Obedience-":
            $ pathvalue = 3
        "-Go back-":
            # Return
            $ game.daytime = temp_day
            call update_interface_color
            jump enter_room_of_req

    stop music fadeout 1.0
    pause 1.0

    $ game.daytime = True
    call update_interface_color
    call music_block

    if pathvalue == 0:
        # Part 1
        call her_chibi("stand","mid","base")
        call hide_blkfade

        call her_main("Hello [genie_name].", "open", "base", "base", "mid", flip=False)
        call her_main("", mouth="base")
        m "Good day [hermione_name]."
        m "How would you feel about going out and earning thirty-five points for your house today?"
        call her_main("I would love to...{w=0.3} as long as it doesn't involve me humiliating myself in front of my peers.", "open", "base", "base", "R", cheeks="blush")
        call her_main("", mouth="normal", cheeks="blush")
        g9 "Well then, perhaps today is your lucky day."
        call her_main("Really?", "open", "base", "base", "mid", cheeks="blush")
        call her_main("", mouth="soft", cheeks="blush")
        m "Yes, in fact you may wish to remain as unseen as possible during your activities today."
        call her_main("(That doesn't sound suspicious at all...)", "disgust", "narrow", "worried", "down", cheeks="blush")
        call her_main("", "normal", "base", "base", "mid", cheeks="blush")
        g9 "I would very much like for you to recover one of the most revered and sacred objects in this academy...{w=0.5} No, in the world!"
        call her_main("Oh! You want me to recover a magical artifact?", "open", "base", "base", "mid")
        call her_main("", "normal", "base", "base", "mid")
        m "Something like that..."
        call her_main("", "normal", "base", "base", "mid")
        call her_main("I am glad you're finally asking me to properly utilise my abilities as one of Hogwarts' top students.", "open", "closed", "base", "mid")
        call her_main("{size=-4}I only wish you would have asked this of me sooner...{/size}","open","narrow", "base","R_soft")
        call her_main("You can count on me, [genie_name]! I am happy to perform a task such as this one.", "smile", "base", "base", "mid")
        call her_main("", "base", "base", "base", "mid")
        m "Great! Now all the information I have for this \"artifact\" is an ancient riddle..."
        m "Are you ready?"
        call her_main("Of course, [genie_name].", "open", "base", "base", "mid_soft")
        call her_main("", mouth="base")
        m "Good, here we go..."
        m "\"I am sought by many,{w=0.2} yet the same number already possess me.\""
        call her_main("", "soft", "happy", "base", "mid")
        m "\"The more I am used, the more valuable I become.\""
        call her_main("The sword of Gryffindor...", "open", "closed", "base", "mid")
        call her_main("no, wait...", "angry", "wide", "worried", "shocked")
        call her_main("... the elder wand?", "base", "base", "base", "mid")
        call her_main("", mouth="disgust")
        m "I am not done yet [hermione_name]..."
        call her_main("Sorry...", "soft", "narrow", "worried", "down")
        call her_main("", "normal", "base", "base", "mid")
        m "\"The only thing man covet more than my form is the secret I hid.\""
        call her_main("*Hmm*...", "upset", "base", "base", "R")
        call her_main("", "normal", "base", "base", "mid")
        m "... \"Sometimes I am plain and white, but I look my best when skimpy and black.\""
        call her_main("", "normal", "happy", "base", "mid")
        g4 "No wait! \"skimpy and pink.\""
        call her_main("This is an ancient riddle...?", "open", "squint", "angry", "mid")
        call her_main("", "upset", "base", "base", "R")
        m "Hush girl... "
        m "\"In order to find me you must get close to earth, then look up to the heavens.\""
        call her_main("...", "upset", "base", "base", "mid")
        m "..."
        m "\"No schoolgirl fetish would be complete without me.\""
        call her_main("[genie_name]...?!", "open", "squint", "angry", "mid")
        g9 "\"The answer is on page 74, Spell {i}seitnaP{/i} backwards.\""
        call her_main("PROFESSOR!", "scream", "squint", "angry", "mid")
        call her_main("", "angry", "squint", "angry", "mid")
        m "Yes?{w=0.5} Did you figure it out?"
        call her_main("If you wanted to see my...{w=0.3} *ahem*{w=0.3} {i}undergarments{/i}, you could have just asked...", "disgust", "squint", "base", "mid", cheeks="blush")
        call her_main("{size=-4}You didn't have to make the whole story up to grab my attention...{/size}", "upset", "narrow", "base", "R_soft", cheeks="blush")
        g9 "By Merlin's beard! I think you've got it girl...{w=0.5} {size=-4}for the most part at least.{/size}"
        call her_main("[genie_name], my classes start soon, can we just get it over with so I can get my points and leave?", "open", "closed", "base", "mid", cheeks="blush")
        call her_main("", "upset", "narrow", "base", "mid_soft")
        g9 "Such eagerness...{w=0.3} but where's the challenge in handing me your own?"
        call her_main("Sorry, you wanted me to hand you a pair?", "open", "wide", "base", "mid", cheeks="blush")
        m "Of course, but not yours silly girl..."
        call her_main("", mouth="angry", cheeks="blush")
        g9 "This is meant to be a treasure hunt! Go find someone's panties out in the world and then bring them to me."
        call her_main("But, [genie_name]?!", "shock", "squint", "angry", "mid", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        m "You're a bright young gal, I'm sure you'll think of something... Make haste!"
        call her_main(".......", mouth="disgust", cheeks="blush")
        pause 1.0
        call her_main("", "soft", "narrow", "worried", "down")
        m "What are you standing there for?"
        call her_main("Isn't there any other way I coul--", "soft", "narrow", "base", "mid_soft", cheeks="blush")
        m "No."
        call her_main("{size=-4}... fine.{/size}", "soft", "narrow", "worried", "down")

        call her_walk(action="leave")

        show screen blkfade
        with d3

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Three hours later...{/color}{/size}"

        $ game.daytime = False
        call update_interface_color
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call play_sound("knocking")
        pause 1.0
        m "Enter!"

        call her_walk(action="enter", xpos="mid", ypos="base")

        call her_main("Good evening, [genie_name].", "open", "base", "base", "R")
        call her_main("", "normal", "base", "base", "R")
        m "Hello again, [hermione_name]."
        call her_main("", cheeks="blush")
        m "Did you finish your assignment?"
        call her_main("about that...", "soft", "narrow", "base", "R_soft", cheeks="blush")

        call her_walk("desk", "base")

        "She elegantly drops a pair of frilly pink panties on your desk."
        call her_main("And for extra credit...", "soft", "narrow", "worried", "down", cheeks="blush")
        hide screen bld1
        hide screen hermione_main
        with d3
        "She adds a matching pink lingerie bra to the spoils on your desk."
        show screen bld1 with d3
        g9 "You absolute minx!"
        call her_main("", "normal", "base", "base", "R", cheeks="blush")
        g9 "You've outdone yourself [hermione_name], how did you manage this feat?"
        call her_main("I would prefer not to talk about it...", "disgust", "narrow", "worried", "down", cheeks="blush")
        g9 "Well you can certainly colour me impressed."
        call her_main("Does that mean I've earned some extra house points?", "open", "base", "base", "R")
        m "I think the situation calls for it..."
        call her_main("", "smile", "base", "base", "R")
        g9 "Ninety points to Gryffi--{w=0.5}{nw}"
        g4 "Ninety points to Gryffi--{fast} wait a second..."
        call her_main("", "smile", "base", "base", "mid")
        "> You take another look at the panties and notice something unusual."
        call her_main("", "base", "base", "base", "mid")
        "> Both panties and bra have a small piece of paper tied to them."
        call her_main("", "normal", "base", "base", "mid")
        "> You reach out and grab the closest pair of panties, then study the paper."
        call her_main("", "normal", "base", "base", "R")
        "8.99$\n{size=-3}Thank you for shopping with us and hope to see you back soon!{/size}\nMadam Mafkin"
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "crooked_smile", "closed", "base", "mid")
        m "Why is there a price tag on these?"
        call her_main("...!", "angry", "wide", "base", "stare")
        call her_main("Uh.... Well, the person I bough--{w=0.3} *ahem*{w=0.2} {size=+2}BORROWED{/size} these from must have forgotten to take the price tag off.", "open", "happy", "base", "mid")
        call her_main("", mouth="normal")
        m "I see...{w=0.3} Well whoever you took them from must be a bit slow to forget something like that, don't you agree?"
        call her_main("Uhh...", "normal", "narrow", "worried", "down")
        m "I would even dare to call them...{w=0.2} a moron."
        call her_main("...", mouth="upset")
        call her_main("", "upset", "base", "worried", "R")
        g9 "A bloated...{w=0.2} Scatterbrained,{w=0.2} moron!"
        call her_main("{size=+4}[genie_name]!{/size}", "open", "squint", "angry", "mid")
        call her_main("", mouth="normal")
        m "Yes, [hermione_name]?"
        call her_main("Fine...", "annoyed", "narrow", "annoyed", "mid")
        call her_main("it was me!", "angry", "narrow", "worried", "down")
        call her_main("I couldn't do it, so I bought them at the shop...", mouth="disgust")
        m "So...{w=0.5} You're the bloated, scatterbrained moron then?"
        call her_main("Sir, this has been embarrassing enough...{w=0.5} Can I just go back to my dormitory please?", "disgust", "narrow", "base", "mid_soft")
        m "[hermione_name]..."

        menu:
            "-Cheaters never prosper-":
                m "I must say I am disappointed with your actions, [hermione_name]."
                call her_main("I am so sorry [genie_name]...", "disgust", "narrow", "worried", "down")
                call her_main("", "disgust", "narrow", "base", "mid_soft")
                m "Not only did you disobey me, but you also tried to trick me - your headmaster - into thinking these belonged to some colleague of yours."
                call her_main("it won't happen again...", "disgust", "narrow", "worried", "down")
                call her_main("", "disgust", "narrow", "base", "mid_soft")
                g4 "For your own sake it better doesn't, or I will have to take action."
                call her_main("", "disgust", "narrow", "worried", "down")
                m "Dismissed."
                call her_main("Yes sir.")

            "-Yes, they do-":
                m "I must say...{w=0.3} I am impressed with your courage, [hermione_name]."
                call her_main("I am sorry [genie_name]. I wo--", "disgust", "narrow", "worried", "down")
                call her_main("Wait what?", "shock", "base", "worried", "mid")
                call her_main("", "soft", "base", "worried", "mid")
                m "I never imagined you'd possess such \"out of the box\" problem solving!"
                call her_main("Really?", "open", "base", "worried", "mid")
                call her_main("", "soft", "base", "worried", "mid")
                g9 "You fumbled the landing, but otherwise cheated like a pro!"
                call her_main("Thank you...", "soft", "base", "worried", "mid")
                call her_main("(I guess...?)", "soft", "narrow", "base", "R_soft")
                call her_main("", "soft", "base", "worried", "R")
                m "Now, I won't overburden you with compliments..."
                call her_main("", "soft", "base", "worried", "mid")
                m "Take your house points and go...{w=0.5} Thirty-five points to Gryffindor!"
                call her_main("{size=+4}Really?!{/size}{w=0.2} Thank you so much [genie_name]!", "smile", "base", "base", "mid", cheeks="blush")

                call her_walk("mid", "base")

                m "I hope next time you do better though."
                call her_main("(Next time...?!)", "shock", "wide", "worried", "shocked", cheeks="blush", flip=True)
                call her_main("(Think about the points Hermione, the points......)", "angry", "happyCl", "worried", "mid", cheeks="blush", flip=True)

        call her_walk(action="leave")

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen fireplace_fire
        centered "{size=+7}{color=#cbcbcb}End of part one{/color}{/size}"
        jump panty_raid_menu

    if pathvalue == 1:
        # Part 2
        call hide_blkfade
        pause 1.5
        call play_sound("knocking")
        pause 1.0
        m "Come in!"

        call her_walk(action="enter", xpos="mid", ypos="base")

        call her_main("Hello [genie_name], you called?", "open", "base", "base", "mid", flip=False)
        call her_main("", mouth="base")
        m "Hello to you too, [hermione_name]."
        g9 "Say...{w=0.3} would you like to earn some points today girl?"
        call her_main("Possibly...", mouth="open")
        call her_main("But that depends on the task required of me.", "open", "closed", "base", "mid")
        call her_main("", "soft", "base", "base", "R")
        m "I would like you to try yourself at that \"treasure hunt\" again."
        call her_main("*sigh* I knew that sooner or later you would ask me about it, [genie_name]...", "open", "closed", "base", "mid")
        call her_main("Do I have a choice?", "upset", "base", "worried", "mid")
        g9 "Certainly, if you don't mind those \"Slytherin Harlots\" taking the house cup!"
        call her_main("I Do mind...", "upset", "narrow", "base", "down")
        call her_main("", "upset", "base", "worried", "mid")
        g9 "Then you'd better head on out and steal some girl's panties!"
        call her_main("{size=-4}... one hundred points{/size}", "open", "base", "worried", "R")
        call her_main("", mouth="upset")
        m "Thirty-five."
        call her_main("... seventy-five points", "open", "happyCl", "worried", "mid")
        call her_main("", mouth="upset")
        m "Forty..."
        call her_main("... fifty points", mouth="upset")
        m "Forty-five..."
        call her_main("Fine.", "disgust", "narrow", "base", "R_soft")
        call her_main("", "upset", "base", "base", "R")
        g9 "We got a deal then, splendid!"
        call her_main("", "normal", "base", "base", "mid")
        m "You're free to go now."
        call her_main("Thank you [genie_name].", "open", "base", "base", "mid")

        call her_walk("door", "base")

        call bld
        m "Oh and one more thing..."
        call her_main("Yes?", "soft", "base", "base", "R", flip=True)
        m "Make sure they're not new this time."
        call her_main("... okay.", "disgust", "narrow", "worried", "down", flip=True)
        hide screen hermione_main
        hide screen bld1
        with d3
        pause 0.5

        call play_sound("door")
        call her_chibi("hide")
        with d3
        pause 1.0

        show screen blkfade
        with d3
        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Four hours later...{/color}{/size}"
        $ game.daytime = False
        call update_interface_color
        call music_block
        show screen fireplace_fire
        pause 1.0

        call hide_blkfade
        pause.5

        call her_walk(action="enter", xpos="desk", ypos="base")

        call play_sound("bump")
        "She drops a slightly used pair of plain panties on your desk."
        call her_main("", "soft", "base", "base", "R", cheeks="blush", flip=False)
        m "I don't see any tags, that's good. Did you learn from your previous error?"
        call her_main("Yes sir...", "disgust", "narrow", "worried", "down", cheeks="blush")
        call her_main("", "soft", "narrow", "worried", "down", cheeks="blush")

        menu:
            "-Let her Go-":
                m "Well, quality leaves a bit to be desired, but it's a good step forward."
                call her_main("", "soft", "base", "base", "mid", cheeks="blush")
                m "Forty-five points to Gryffindor!"
                call her_main("Thank you, [genie_name].", "open", "base", "base", "mid", cheeks="blush")
                call her_main("Am I free to go now?", "soft", "base", "base", "mid", cheeks="blush")
                m "Yes, you are free to go."

                call her_walk("mid", "base")

                $ renpy.play('sounds/sniff.mp3')
                g9 "{size=-4}Such nice fragrance, I wonder to whom these belong?{/size}"
                call her_main(".........(I'm sorry Ginny).........", "disgust", "narrow", "worried", "down", cheeks="blush", flip=True)

                call her_walk(action="leave")

            "-Ask for details-":
                m "So, who was the lucky lady?"
                call her_main("No one.", "open", "base", "worried", "R", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "Come on now."
                call her_main("Umm...{w=0.3} Does that really matter?", "open", "base", "base", "mid", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "It does to me."
                call her_main("*sigh*", "soft", "happyCl", "worried", "mid", cheeks="blush")
                call her_main("It was Ginny, sir...", "open", "base", "worried", "mid", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "Interesting...{w=0.5} I don't know who that is."
                call her_main("She's a sister of one of my friends...", "open", "base", "worried", "R", cheeks="blush")
                call her_main("", mouth="normal", cheeks="blush")
                m "Is she hot? Or cute?"
                call her_main("...", "soft", "narrow", "worried", "down")
                m "Well?"
                call her_main("I guess she is kind of both...", mouth="soft", cheeks="blush")
                g9 "(Splendid! Maybe she can introduce her to me sometimes)"
                call her_main("", "soft", "base", "base", "mid", cheeks="blush")
                m "So, how did you do it?"
                call her_main("I offered to do her laundry along with mine this week...", "open", "narrow", "worried", "down", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "And?"
                call her_main("And whilst I was working, I grabbed one of her...{w=0.4} panties...{w=0.3} and shoved them in my pocket.", "soft", "narrow", "base", "R_soft", cheeks="blush")
                m "And?"
                call her_main("If she asks what happened to them... I will just say that they had gotten lost in the wash.", "soft", "narrow", "base", "mid_soft", cheeks="blush")
                call her_main("", mouth="normal", cheeks="blush")
                m "And?"
                call her_main(" And... that's really it.", "open", "base", "base", "mid")
                call her_main("", mouth="normal")
                g4 "How dull.{w=0.5} forty-five stupid house points to Gryffindor."
                call her_main("Do those count the same as regular points?", mouth="annoyed")
                m "I suppose..."
                call her_main("Goodnight then sir.", "open", "base", "base", "mid")

                call her_walk("door", "base")

                m "{size=-4}Ginny...{w=1.0} it's time for you to meet {i}George{/i}.{/size}{w=0.2}{nw}"
                call gen_chibi("jerk_off_behind_desk")
                $ renpy.play('sounds/zipper.mp3')
                g9 "{size=-4}Ginny... It's time for you to meet {i}George{/i}.{/size}{fast}"
                call her_main("", "angry", "wide", "worried", "shocked", cheeks="blush", flip=True)
                pause 0.8
                call her_main("(I'd better leave now...)", "disgust", "base", "base", "R", cheeks="blush", flip=True)
                hide screen hermione_main
                hide screen bld1
                with d3
                pause 0.5

                call her_chibi("leave")

        call blkfade

        stop music fadeout 1.0
        hide screen fireplace_fire
        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}End of part two{/color}{/size}"
        jump panty_raid_menu

    elif pathvalue == 2:
        # Part 3
        call hide_blkfade
        pause 1.0
        call play_sound("knocking")
        pause 0.5
        her "I'm coming in."

        call her_walk(action="enter", xpos="mid", ypos="base")

        g9 "Well, well, well... if it isn't my favourite minx!"
        call her_main("Good morning to you too, [genie_name].", "open", "closed", "base", "mid", flip=False)
        call her_main("", "base", "base", "base", "mid")
        m "What brings you here this time?"
        call her_main("Well... I...", "open", "base", "base", "R", cheeks="blush")
        call her_main("", mouth="upset", cheeks="blush")
        m "Don't you worry, I'm just teasing you."
        call her_main("", "normal", "base", "base", "mid", cheeks="blush")
        m "But we've made it quite a habit by now, didn't we?"
        m "You coming here every morning and asking for points..."
        call her_main("", "normal", "base", "worried", "mid", cheeks="blush")
        m "... for which in return you bring me panties of that colleague of yours..."
        call her_main("", "normal", "narrow", "base", "down", cheeks="blush")
        g9 "... I wonder if she realised by now that a washing machine can only eat so many panties."
        call her_main("", "soft", "narrow", "base", "R_soft", cheeks="blush")
        m "but surely that's something worth risking your reputation over, am I right?"
        call her_main("...", "annoyed", "narrow", "base", "R_soft")
        g9 "I'll take that as a yes."
        m "You know what to do, off you go."
        call her_main("Fine.", "open", "closed", "base", "mid")
        call her_main("", "annoyed", "narrow", "base", "mid_soft")
        g9 "That a girl."

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}A few hours later...{/color}{/size}"
        $ game.daytime = False
        call update_interface_color
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base")

        g9 "Hello [hermione_name], looking good."
        call her_main("Uh-huh... Sir, if I'm not mistaken... {w=0.3}Hogwarts does not have a \"linguistics\" class, do we?", "open", "narrow", "worried", "mid_soft")
        call her_main("", mouth="upset")
        m "(Why is she asking me?{w=0.3} Oh Right, \"headmaster Rumbleboar\")"
        m "Do you really think we have a class you wouldn't know about?"
        call her_main("True... Then, do you know of how many \"Connies\" attend Hogwarts?", "open", "base", "base", "mid")
        call her_main("", mouth="normal")
        call her_main("There aren't any in Gryffindor or Ravenclaw I believe, but I'm not sure for some of the other houses.", "open", "base", "base", "mid_soft")
        call her_main("", mouth="normal")
        m "I feel as though there's some context missing."
        call her_main("*Ehm*... alright, so...{w=0.5} I was in the Gryffindor girl's dorm, working on my \"task.\"", mouth="open")
        call her_main("", mouth="normal")
        m "The perfect hunting grounds."
        call her_main("I am astonished that I'll have to agree with you, but yes... I had the pick of the litter with no absence of choice.{w=0.3} Speaking of...", "open", "closed", "base", "mid")

        call her_walk("desk", "base")

        $ renpy.play('sounds/cloth_sound.mp3')
        "She drops a bunched-up ball of about half a dozen girls' panties on your desk, coming in an array of different sizes, designs and colours."
        call her_main("I usually don't conduct such a shotgun approach to work, although...", "open", "base", "base", "mid", cheeks="blush")
        call her_main("", mouth="soft", cheeks="blush")
        g9 "In this instance it appears to have served you well. Full marks for stealing panties from your schoolmates."
        call her_main("It would have flustered me if I hadn't told my dorm mates time and time again that it is all of our responsibilities to keep our dorm tidy.", "annoyed", "base", "base", "R", cheeks="blush")
        call her_main("Loss of their undergarments is expected when leaving said property strewn around as if a hurricane blew through their drawers.", "open", "base", "base", "mid")
        call her_main("", mouth="soft")
        m "Yes, Yes... But how does this connect back to a Connie?"
        call her_main("Right... Well, I obviously chose a time at which I believed all my dorm mates would be gone.", "open", "happyCl", "worried", "mid")
        call her_main("But just as I was shoving the last pair into my bag, Katie Bell walked in...", "angry", "narrow", "base", "down", cheeks="blush")
        call her_main("She caught me red handed!", "disgust", "narrow", "worried", "down", cheeks="blush")
        call her_main("", "normal", "narrow", "worried", "mid_soft")
        g9 "Or silky handed!{w=1.0}{nw}"
        m "Or silky handed!{fast}... panty handed?"
        call her_main("", "normal", "narrow", "worried", "down")
        m "..."
        m "Sounded better in my head...{w=0.5} give me a minute and I'll come up with something that works..."
        call her_main("I've never been more embarrassed in my entire life!", "normal", "narrow", "worried", "mid_soft", cheeks="blush")
        call her_main("", "annoyed", "narrow", "base", "R_soft")
        m "Pff, as if you've never said {i}that{/i} before."
        call her_main("I mean it! I was mortified standing there clutching her panties while stumbling over my words for an excuse.", "open", "narrow", "worried", "mid_soft", cheeks="blush")
        call her_main("", mouth="upset", cheeks="blush")
        m "And what did she do?"
        call her_main("Well... that's the odd thing, while I was floundering like a fish she was just grinning at me. Then she said, and I quote...", "open", "base", "base", "mid")
        call her_main("\"I always had a feeling about you Granger... But if you want them, you'll need to do me a favour. Meet me tonight and we can help with Connie's Linguistics homework.\"", "open", "base", "base", "R")
        call her_main("", "base", "base", "base", "mid")
        m "Connie's linguist?-{w=1.0}{nw}"
        g9 "Connie's linguist?-{fast} oh I see..."
        call her_main("As embarrassing as the circumstances were, I would never turn down a request to help a student with homework! But I don't think we have a linguistics class or what Connie she was--", "open", "narrow", "worried", "mid_soft")
        call her_main("", "soft", "base", "base", "mid")
        g9 "{i}Cunnilingus{/i} [hermione_name]... She was asking for Cunnilingus."
        call her_main("*huh*? But she said she wanted study help.")
        m "It was a metaphor... She was assuming you were a bit more worldly than you really are."
        call her_main("I am plenty worldly!", "angry", "base", "angry", "mid")
        call her_main("...", "upset", "narrow", "angry", "R")
        call her_main("", "upset", "base", "worried", "mid")
        pause 0.5
        call her_main("... What's Cunnilingus?", "open", "base", "worried", "mid")
        call her_main("", mouth="upset")
        m "*Sigh*, she was asking for Dinner beneath the bridge."
        call her_main("Dinner? But if she wanted to eat with me why didn't she--", "open", "base", "base", "mid")
        call her_main("", mouth="upset")
        m "Metaphor, [hermione_name]... She wanted you to sip from her furry cup."
        call her_main("*huh*?", "open", "narrow", "worried", "mid_soft")
        call her_main("", mouth="upset")
        m "Muff Diving..."
        call her_main("", "upset", "base", "worried", "mid")
        m "Munch her carpet..."
        call her_main("", "clench", "closed", "angry", "mid")
        m "Deluxe wash..."
        call her_main("Stop not making any sense!", "clench", "base", "angry", "mid")
        call her_main("", mouth="annoyed")
        m "Are you really supposed to be this school's top student? She was asking you to eat her out."
        call her_main("Eat her what out?", mouth="open")
        call her_main("", "annoyed", "narrow", "angry", "R")
        m "Alright... work with me. She wanted you...{w=1.0} Still with me here?"
        call her_main("Yes obviously...", "open", "closed", "angry", "mid")
        call her_main("(Does he think I'm an idiot?)", "annoyed", "narrow", "angry", "R")
        m "Okay then repeat after me."
        call her_main("", "annoyed", "base", "base", "mid_soft")
        m "She wanted you..."
        call her_main("She wanted me...", "open", "base", "base", "mid_soft")
        call her_main("", mouth="normal")
        m "To take your tongue..."
        call her_main("Thake myh tonghue?", mouth="open_tongue")
        call her_main("", "open_wide_tongue", "squint", "base", "mid")
        pause 1.0
        g9 "And stick it in her vagina!"
        call her_main("{size=+8}WHAT?!{/size}", "shock", "wide", "base", "stare", cheeks="blush")
        call her_main("Why would she want that?!", "shock", "wide", "base", "mid", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        g9 "Because in my experience it feels awesome...{w=0.5}{nw}"
        m "Because in my experience it feels awesome...{fast} Wait, did that make it sound like I have a vagin--"
        call her_main("You're wrong! She-- She--", "shock", "closed", "angry", "mid", cheeks="blush")
        call her_main("", "angry", "happyCl", "worried", "mid", cheeks="blush")
        m "What? Never done it before?"
        call her_main("{size=+4}OF COURSE NOT!{/size}", "angry", "base", "angry", "mid", cheeks="blush")
        g9 "I mean, I assumed you didn't have any real friends... But to get to your age and never eat another girl out? How shameful."
        call her_main("Not everyone in this school is as gross as you!", "angry", "narrow", "annoyed", "mid", cheeks="blush")
        g9 "well, there's one way to prove me wrong. Go find Katie and ask her yourself."
        call her_main("", "annoyed", "narrow", "annoyed", "mid", cheeks="blush")
        call her_main("Maybe I will...", "open", "closed", "angry", "mid")
        call her_main("", "upset", "narrow", "annoyed", "mid")
        call her_main("She will surely--", "open", "closed", "base", "mid")
        call her_main("{size=+4}HOLD ON!{/size}", "scream", "wide", "base", "stare")
        call her_main("", mouth="shock")
        m "What?"
        call her_main("I-I-I-I-I...", "angry", "wide", "base", "mid", cheeks="blush")
        m "Just spit it out!"
        call her_main("I was so nervous with her that I just said yes! She'll be expecting me soon!", "mad", "narrow", "base", "down", cheeks="blush")
        g9 "You better get to it then, [hermione_name]!"
        call her_main("But I-- But I-- I couldn't--", "shock", "narrow", "worried", "down", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        call her_main("I'll just have to inform her that it was a misunderstanding, yes that will have to do.", "shock", "narrow", "base", "mid_soft", cheeks="blush")
        call her_main("", "angry", "narrow", "base", "mid_soft", cheeks="blush")
        g9 "Sure, and risk her spilling the beans to your entire dorm that the proud Hermione Granger steals girls' panties."
        call her_main("...", "soft", "narrow", "worried", "down")
        call her_main("", "soft", "closed", "angry", "mid", cheeks="blush")
        g9 "Hey, for sixty points would you let me watch--"
        call her_main("Absolutely not!", "scream", "base", "angry", "mid", cheeks="blush")
        call her_main("", "angry", "base", "angry", "mid", cheeks="blush")
        m "That's a bummer..."
        call her_main("", "angry", "narrow", "angry", "R", cheeks="blush")
        m "You can go then."
        call her_main("...", mouth="annoyed", cheeks="blush")
        call her_main("......", "annoyed", "base", "worried", "mid", cheeks="blush")
        call her_main("What about the points sir?", "open", "narrow", "worried", "mid_soft", cheeks="blush")
        call her_main("", "annoyed", "base", "worried", "mid", cheeks="blush")
        m "Oh yes, right..."
        m "Forty-five points to Gryffindor!"
        call her_main("Thank you sir...", "open", "narrow", "worried", "mid_soft")
        call her_main("", "upset", "base", "base", "R")
        pause 0.5

        call her_walk("mid", "base")

        g9 "{i}Bon appetit!{/i}"
        call her_main("", "open", "base", "base", "R", flip=True)
        pause 0.5
        call her_main("...", "angry", "base", "base", "mid", flip=True)
        call her_main("(What did I get myself into this time...?)", "angry", "narrow", "base", "down", cheeks="blush", flip=True)

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0
        hide screen fireplace_fire
        pause 1.0
        call play_sound("knocking")
        pause 1.0
        fem "Who is it?"
        pause 0.5
        her "It's me... Hermione granger."
        call play_sound("door")
        her "Hello Katie I--"
        $ renpy.play('sounds/giggle2.mp3')
        "Katie" "Hey there sweet cheeks. {heart}{w=0.5} I have been waiting for you. {heart}{heart}{heart}"
        her "We need to talk--"
        "Katie" "I know exactly what we need. {heart}"
        $ renpy.play('sounds/slap_03.mp3')
        "> Katie grabs Hermione and pulls her in the room{nw}"
        $ renpy.play('sounds/door2.mp3')
        "> Katie grabs Hermione and pulls her in the room{fast}, then shuts the door."
        pause 1.0
        $ renpy.play('sounds/09_lock.wav')
        pause 0.5
        her "Why did you lock the door...?!"
        $ renpy.play('sounds/cloth_sound.mp3')
        "> Katie starts taking off her clothes."
        her "Wha-wha-what-t-t are you d-doing?!"
        $ renpy.play('sounds/giggle.mp3')
        "Katie" "Aren't you talkative today?{w=0.5} I would save my breath if I were you. {heart}{heart}{heart}"
        "Katie" "I'm quite{w=0.2} {heart}horny{heart}{w=0.2} so you might be stuck here for a while."
        $ renpy.play('sounds/push_on_bed.mp3')
        "> She pushes Hermione onto the bed." with vpunch
        her "{size=+4}W-wait?!{/size}"
        $ renpy.play('sounds/sit_on_bed.mp3')
        "> Then she swiftly straddles her face in cowgirl position." with hpunch
        $ renpy.play('sounds/gltch.mp3')
        her "..........!!!"
        her "*Hmph*"
        $ renpy.play('sounds/gasp2.mp3')
        "Katie" "Ahh!{heart} {w=0.5}So much better... {heart}{heart}{heart}"
        "Katie" "I'll start moving now.{w=0.5} You ready?"
        her "*nwh*!!!"
        $ renpy.play('sounds/giggle3.mp3')
        "Katie" "I'll take that as a yes. {heart}{heart}{heart}"
        $ renpy.play('sounds/jump_on_bed.mp3')
        her "*Hmph{cps=10}hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh{/cps}*{nw}" with vpunch_repeat
        pause 1.0
        centered "{size=+7}{color=#cbcbcb}End of part three{/color}{/size}"
        jump panty_raid_menu

    elif pathvalue == 3:
        # Part 4
        centered "{size=+7}{color=#cbcbcb}A couple of months after the \"linguistics\" incident...{/color}{/size}"
        call hide_blkfade
        pause 1.0

        call her_walk(action="enter", xpos="mid", ypos="base")

        call her_main("Hello, [genie_name].{heart}", "smile", "wink", "base", "mid", flip=False)
        call her_main("", "smile", "base", "base", "mid")
        g9 "[hermione_name]! My favourite slut."
        m "I have another riddle for you."
        call her_main("Oh, this ought to be fun.", mouth="grin")
        call her_main("Could you make it a {i}hard one{/i} [genie_name]?", mouth="open_wide_tongue")
        call her_main("", mouth="smile")
        g9 "You'll enjoy this one for sure...{w=0.5} Ready?"
        call her_main("Ready!", "smile", "happyCl", "base", "mid")
        call her_main("", "base", "base", "base", "mid")
        m "\"I am as soft and pure as a kitten, though far more desirable.\""
        call her_main("*Hmm*...", "base", "base", "base", "R")
        call her_main("Boobs?{w=0.5} Titjob?", "soft", "base", "base", "mid")
        call her_main("", "smile", "base", "base", "mid")
        m "No. In this case, contrary to a titjob, it being both small and tight is usually preferred."
        call her_main("Sex?", "grin", "narrow", "base", "mid_soft")
        call her_main("", "base", "narrow", "base", "mid_soft")
        m "Nope...{w=0.5} \"While boys may want me, they wouldn't be caught dead ever just buying me for themselves.\""
        call her_main("Well that definitely rules out sex.", "open", "base", "base", "R")
        call her_main("", mouth="base")
        m "\"The less of me there is, the more... desirable... I become to behold.\""
        call her_main("Oh! Oh! Panties!", "crooked_smile", "closed", "base", "mid")
        call her_main("", "base", "base", "base", "mid")
        g9 "Spot on."
        call her_main("Mine or someone else's?", "smile", "happy", "base", "mid_soft")
        m "Someone else's if you don't mind, [hermione_name]."
        call her_main("On it! I'll be back soon...", "base", "base", "base", "mid")

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"
        $ game.daytime = False
        call update_interface_color
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base")

        call her_main("Hello [genie_name], I hope I didn't keep you waiting for too long...", "smile", "happy", "base", "mid_soft")

        call her_walk("desk", "base")

        call her_main("I had a little...{w=0.3} \"setback\"{w=0.3} if you know what I mean...", "grin", "narrow", "base", "mid_soft", cheeks="blush")
        call her_main("", mouth="base", cheeks="blush")
        pause 0.5
        hide screen bld1
        hide screen hermione_main
        with d3
        "She drops a pair of laced white panties on your desk."
        show screen bld1 with d3
        m "No trouble at all [hermione_name]...{w=0.5} And you have excellent taste as always."
        $ renpy.play('sounds/sniff.mp3')
        g9 "These smell fantastic!"
        call her_main("You're too kind [genie_name].", "grin", "happy", "base", "mid_soft", cheeks="blush")
        hide screen bld1
        hide screen hermione_main
        with d3
        pause 1.0
        call gen_chibi("jerk_off_behind_desk")
        $ renpy.play('sounds/zipper.mp3')
        ">You take your cock out and start stroking it..."
        call gen_chibi("jerk_off_behind_desk")
        call her_main("Mmmm, [genie_name] need any help with that?", "base", "squint", "base", "mid", cheeks="blush")
        m "These already feel a little damp in the middle. Why don't you tell me why that is?"
        call her_main("Oh you know, girls will be girls and all.", "grin", "narrow", "base", "mid_soft", cheeks="blush")
        g9 "You know, charming the panties off someone is just a figure of speech."
        call her_main("Not anymore... I'd like to think Katie was quite pleased with me.", "smile", "narrow", "base", "mid_soft", cheeks="blush")
        m "Katie? Katie Bell? The same delicious dyke that wanted you to clam joust with her?"
        call her_main("Maybe...", "smile", "narrow", "base", "R_soft", cheeks="blush")
        call her_main("Although, Katie keeps raising the fee every time I ask.", "smile", "happyCl", "base", "mid", cheeks="blush")
        call her_main("", mouth="open", cheeks="blush")
        call her_main("Not that I mind, but my tongue can get quite sore sometimes.", mouth="open_tongue", cheeks="blush")
        call her_main("Especially since we've started the \"linguistics\" thing.", "open_wide_tongue", "squint", "worried", "up", cheeks="blush")
        call her_main("", "open_wide_tongue", "squint", "worried", "up", cheeks="blush")
        g4 "Ugh!"
        call cum_block
        call gen_chibi("cum_behind_desk")
        call her_main("", "open_wide_tongue", "narrow", "base", "mid_soft", cheeks="blush")
        pause 1.5
        call gen_chibi("cum_behind_desk_done")
        call her_main("Oh, poor [genie_name], I had no idea you were so pent up. You can start calling me out more than twice a day if that isn't enough.", "soft", "narrow", "worried", "mid_soft", cheeks="blush")
        m "During the day? But what about your classes?"
        call her_main("*Hmm*? Oh well, missing one or two wouldn't hurt... Especially if the headmaster has an important \"assignment\" for me.", "base", "narrow", "base", "mid_soft", cheeks="blush")
        m "I'll consider it... Now let's circle back to you, Katie and your binge of her minge."
        call her_main("Professor... How dare you... I would never even think to shamelessly do something so heinous with a classmate and give you all the juicy details...", "annoyed", "base", "base", "R")
        call her_main("For less than forty house points.", "grin", "wink", "base", "mid", cheeks="blush")
        call her_main("", "base", "narrow", "base", "mid_soft", cheeks="blush")
        m "Maybe next time [hermione_name]. I'm a little... spent for tonight."
        call her_main("We both know you could go for longer if you wanted to...", "soft", "narrow", "base", "mid_soft", cheeks="blush")
        call her_main("but you're right, we'll leave it for later.", "base", "happy", "base", "mid_soft", cheeks="blush")
        call her_main("See you tomorrow [genie_name].", "smile", "wink", "base", "mid", cheeks="blush")

        call her_walk(action="leave")

        pause 1.0
        m "... *Hmm*...{w=1.0} I don't think I ever gave her points."
        pause 0.5

        show screen blkfade with d9
        stop music fadeout 5.0
        hide screen fireplace_fire
        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}End of part four{/color}{/size}"
        jump panty_raid_menu
