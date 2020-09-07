

### Kissing ###

# ([tonks_name] makes out with her students...)

#TODO Add Tonks chibi to all her public request nightly reports

label nt_pr_kiss_start:
    call ton_main("","base","base","base","mid", xpos="right", ypos="base", trans=fade)

    if ton_tier == 2:

        if nt_pr_kiss.points == 0:
            m "Ready to try something a little different?"
            call ton_main("*Mmmm*... Absolutely! This is the most fun I've had in years!","horny","base","base","mid")
            call ton_main("What did you have in mind?", "base", "base", "shocked", "mid")
            m "What do you think?"
            if nt_pr_grope.points == 0:
                call ton_main("I think making out with them would be really fucking hot...","horny","base","base","R")
                m "Just kissing?"
                call ton_main("You don't understand...{w} The way I make out...", "soft", "base", "base", "mid")
                call ton_main("It's way more intense than anything these students will have ever experienced...", "base", "base", "annoyed", "stare")
            else:
                call ton_main("I know you shot it down earlier... but I think a little making out would be really fucking hot...","horny","base","angry","mid")
                m "*Pfft*... you're such a bad girl..."
                m "You've already gotten to second base! Let's not jump back to first!"
                call ton_main("You don't get it...{w} The way I make out...","horny","base","base","R")
                call ton_main("It's way more intense than anything these students will have ever experienced...","base","base","angry","mid")
            m "*Hmmm*..."
            g9 "So you're not just going to give them a peck on the cheek, are you?"
            call ton_main("Oh no...", "crooked_smile", "narrow", "base", "mid")
            call ton_main("They'll be lucky if they can talk straight after I'm done with them...", "crooked_smile", "closed", "base", "mid")
            m "You've set my expectations in you quite high, you know that right?"
            call ton_main("I'll make sure you get your money's worth, don't worry...", "soft", "wink", "base", "mid")
            m "Just see me after class."
            call ton_main("Yes, sir!", "grin", "base", "base", "R")

        else:

            m "Fancy another student-snog-session?"
            call ton_main("*Mmmm*... You bet... Teaching is my job...","horny","base","base","R", hair="horny")
            call ton_main("Even if that lesson is \"French Kissing\"...", "soft", "wink", "shocked", "mid")
            m "Well, don't let me stop you."
            call ton_main("Thank you, sir...", "grin", "base", "base", "mid")

    elif ton_tier >= 3: # Not in 1.37

        if nt_pr_kiss.points == 0: # Tell her to be even lewder for the next level of favors.

            m "Would you like to help your students with their oral skills again?"
            call ton_main("*Mmmm*, yes... Some of them are in dire need of some practice...","horny","base","raised","mid")
            g9 "Then go give them some practice!"
            call ton_main("I will, [ton_genie_name]...","base","base","base","mid")

        else: # Repeat

            m "How would you feel about French kissing your students again?"
            call ton_main("*Mmmm*... Pretty good if the last few times are anything to go by...","horny","base","base","R", hair="horny")
            call ton_main("I'll see you after class...","base","base","angry","mid")

    # Tonks leaves

    $ nt_pr_kiss.inProgress = True

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 1 ###

label nt_pr_kiss_T1_intro_E1: # Tier 1 - Event 1 - Slytherin boy
    #Gentle kissing
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 7 and nt_pr_kiss.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I made out with my favourite Slytherin boy again...","open","base","base","R")
                call ton_main("He's getting quite good at it...","horny","base","base","up")
                m "Well done, [tonks_name]... We'll talk next time."
                call ton_main("Have a good night, [ton_genie_name].","base","happyCl","base","mid")
                call increase_house_points("s", 40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "Fun day?"
    call ton_main("It was!", "crooked_smile", "happyCl", "base", "mid")
    call ton_main("I got to show some students a Boggart for the first time...{w} That was pretty entertaining!", "smile", "base", "base", "mid")
    m ".................."
    call ton_main("Not to mention that I got to take a boy's first kiss...", "soft", "narrow", "annoyed", "mid")
    g9 "A first for everybody!"
    call ton_main("*Mmmm*... I know which one I preferred...", "crooked_smile", "base", "base", "up")
    m "Care to fill me in?"
    call ton_main("I'd love to!", "base", "base", "shocked", "stare")
    call ton_main("So, today I had class with my favourite little \"Slythinerin boy\"...","open","closed","base","mid")
    call ton_main("I didn't really have much to do after classes, so I figured I may as well hold him back...", "grin", "base", "base", "R")
    call ton_main("He was expecting me to buy a favour straight away...", "soft", "closed", "base", "mid")
    call ton_main("However, I was in the mood for a little conversation today...", "base", "narrow", "base", "mid")
    call ton_main("Some rather unimportant banter... Such as his performance in class...", "open", "base", "base", "down")
    call ton_main("Then I asked if he had a girlfriend, to maybe help with him at school...","base","happyCl","base","mid")
    call ton_main("He answered {b}no{/b}, of course... so I showed him some sympathy...", "soft", "narrow", "base", "R")
    call ton_main("Saying how {b}hard{/b} it must be - trying your best to concentrate on school with so many pretty girls running around...", "soft", "narrow", "shocked", "mid")
    m "(I should go for a walk as well some day...)"
    call ton_main("Then I asked if he'd ever made out with any of the girls...", "base", "base", "raised", "mid")
    call ton_main("And of course he hadn't...", "soft", "base", "shocked", "up")
    call ton_main("So, obviously, I just had to buy this little favour from him...", "open", "closed", "shocked", "mid")
    call ton_main("It's my duty as a teacher of this school - to see to my students education!", "soft", "wink", "shocked", "mid")
    m "How noble..."
    call ton_main("He was so excited by the whole thing.", "crooked_smile", "base", "base", "down")
    call ton_main("You should have seen his face... It was precious.","base","happyCl","base","mid")
    m "Was it as intense as you promised?"
    call ton_main("Not that intense, per say... I wanted to take it slow for his first time...", "soft", "narrow", "base", "downR")
    call ton_main("I just sat next to him, and slowly peppered a few kisses on his lips...", "soft", "narrow", "base", "mid")
    call ton_main("After the initial excitement died down, we eventually got into a nice rhythm of kissing... and some light tongue-play...", "horny", "base", "base", "stare")
    call ton_main("He was very inexperienced, but definitely eager to learn.", "horny", "wink", "annoyed", "mid")
    call ton_main("Then, after five minutes or so, I awarded him some house points... and sent him on his way...", "base", "narrow", "base", "R")
    m "And that was all?"
    call ton_main("I don't think it's the last I'll see of him... Besides, I don't want to push him too far.", "soft", "closed", "base", "mid")
    call ton_main("This favour trading might actually be a good way to address student behaviour!", "crooked_smile", "base", "raised", "mid")
    m "Oh... How so?"
    call ton_main("His behaviour has really started to improve after I began buying favours from him!", "base", "narrow", "base", "mid")
    m "Maybe you should consider dealing with all your troublemakers this way?"
    call ton_main("*Hmmm*... Don't tempt me...","horny","base","base","R")
    m "That'll be all then."
    call ton_main("Right, see you, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves.

    call increase_house_points("s", 40)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 7 and nt_pr_kiss.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("Sorry I'm a bit late today...","open","base","base","R")
                call ton_main("I was \"occupied\" kissing that little Ravenclaw boy again...","horny","base","angry","mid")
                m "Very good, [tonks_name]."
                call ton_main("Thank you, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points("r", 20)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "You're a bit late..."
    g9 "Got caught up having too much fun with your students?"
    call ton_main("*Mmmm*... and then some...","horny","base","base","R")
    g9 "I like the sound of that!"
    m "Now, care to elaborate?"
    call ton_main("Alright then, you old perv...", "soft", "wink", "annoyed", "mid")
    call ton_main("Today's event was with my favourite little Ravenclaw boy...", "open", "closed", "base", "down")
    m "That shy one?"
    call ton_main("Yes, the cute one!{w} He made a classic mistake today...", "crooked_smile", "wide", "base", "mid")
    m "Which is?"
    call ton_main("Calling your teacher \"Mommy\".", "open", "base", "shocked", "down")
    g9 "*ha-ha-ha*!... Really?"
    m "I bet the students had a field day with that one!"
    call ton_main("Surprisingly not... Everyone just sort of went quiet.", "annoyed", "narrow", "base", "R")
    m "I know that {b}I{/b} would have given him hell for that..."
    call ton_main("I might have blushed as much as him - after he said it...", "upset", "base", "base", "down")
    call ton_main("Anyhow... I decided that it was reason enough to hold him back...","open","closed","base","mid")
    call ton_main("Not that I needed to... He seemed almost paralysed for the rest of the lesson...", "crooked_smile", "base", "raised", "R")
    call ton_main("He just sat there with his head down... waiting for everyone to leave the classroom...", "soft", "closed", "base", "mid")
    call ton_main("So, I figured I'd indulge him...", "soft", "narrow", "base", "mid")
    call ton_main("I walked over - and plonked myself onto his lap, facing him...", "grin", "base", "base", "mid")
    g9 "Bet that woke him up!"
    call ton_main("Yes... However I wouldn't say it bothered him too much...", "open", "base", "base", "R")
    call ton_main("He just looked up at me with those big puppy eyes...", "soft", "base", "base", "mid")
    call ton_main("And then I broke our gaze and kissed him...", "horny", "wink", "base", "mid")
    m "How did he take it?"
    call ton_main("Great! That kiss must have awoken something in him...", "crooked_smile", "base", "shocked", "mid")
    call ton_main("He really got into it after a while...", "base", "happyCl", "base", "mid")
    call ton_main("*Ugh*!... I've never had someone attack me with their tongue like that...", "horny", "base", "base", "up")
    call ton_main("It was intense! And neither of us wanted it to end...", "soft", "base", "shocked", "ahegao", hair="horny")
    g9 "Is that why you were late today?"
    call ton_main("*Hmmm*... Can you blame me?", "crooked_smile", "base", "base", "up")
    g9 "So you spent all afternoon French kissing one of your students?"
    call ton_main("Yes, [ton_genie_name]...", "soft", "closed", "base", "mid")
    call ton_main("I guess I fucking did!", "crooked_smile", "base", "shocked", "mid", hair="neutral")
    g9 "I'm very proud!"
    m "Great work, [tonks_name]."
    call ton_main("...", "crooked_smile", "base", "base", "up", hair="horny")
    call ton_main("Thank you, [ton_genie_name]. Have a good night.", "base", "wink", "base", "mid")

    # Tonks leaves.

    call increase_house_points("r", 20)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T1_E3: # Tier 1 - Event 3 - Slytherin girls
    #Tonks pays two best friends to make out
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 7 and nt_pr_kiss.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I gave those two Slytherin sluts detention again...","open","base","base","R")
                call ton_main("Fuck, I came so hard watching them kiss!","base","base","base","mid")
                m "You wouldn't believe how jealous I am!"
                call ton_main("You have no idea, [ton_genie_name]!","base","base","angry","mid")
                call ton_main("I better get going. Until next time!","base","happyCl","base","mid")
                call increase_house_points("s", 40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How was your day?"
    call ton_main("Better than most... You'll love this one!", "base", "wink", "base", "mid")
    g9 "Don't let me stop you then..."
    call ton_main("As always, there were a few Slytherins messing around in class...", "base", "base", "base", "mid")
    call ton_main("With an especially annoying pair of girls that wouldn't shut up!", "open", "closed", "raised", "mid")
    call ton_main("So... I gave them detention... which thankfully got them to quiet down a little.", "soft", "base", "base", "L")
    m "So far so good..."
    call ton_main("Normally, I only try and buy favours from one person at a time...", "normal", "closed", "base", "mid")
    call ton_main("But then I figured, why not give both those Slytherin sluts a shot.", "crooked_smile", "base", "base", "mid")
    g9 "So you took turns kissing the girls?"
    call ton_main("No, but I could have...", "soft", "base", "base", "R")
    call ton_main("I gave them the option of staying behind - for a full hour of detention...","open","closed","base","mid")
    call ton_main("Or... have them do their teacher a little favour...","base","base","base","mid")
    g9 "Which was?"
    call ton_main("*Mmmm*... They had to make out with each other!", "horny", "base", "shocked", "down")
    call ton_main("And they had to do it properly. For at least ten minutes.", "soft", "closed", "base", "mid")
    call ton_main("*Ugh*... It was the hottest thing to witness, I tell you...", "horny", "base", "base", "stare")
    g9 "Don't spare any details!"
    call ton_main("Well, they were a bit hesitant at first... which I can't even blame them for...", "soft", "base", "base", "mid")
    call ton_main("It doesn't happen often that you have a teacher watch you make out... and savouring every second of it!", "horny", "narrow", "base", "mid")
    call ton_main("But, I have a feeling that wasn't their first time kissing another girl...", "crooked_smile", "closed", "base", "mid")
    call ton_main("Maybe not even each other...", "base", "narrow", "annoyed", "mid")
    m "Ought to be young again..."
    call ton_main("I couldn't help myself, [ton_genie_name]!", "crooked_smile", "base", "base", "stare")
    call ton_main("I simply {b}had{/b} to play around while they did it...", "horny", "happyCl", "shocked", "mid", hair="horny")
    m "Did they care?"
    call ton_main("Not one bit!", "horny", "base", "base", "down", hair="horny")
    call ton_main("They'd just take it in waves...", "soft", "base", "base", "L")
    call ton_main("Making out... Calling me a pervert...", "horny", "base", "base", "up", cheeks="blush")
    call ton_main("Locking their mouths together, only to break apart again to tease me  more...", "base", "base", "base", "ahegao", cheeks="blush")
    call ton_main("*Ugh*... It was so {b}bloody hot!{/b}...", "open_wide_tongue", "base", "base", "ahegao", cheeks="blush")
    m "I take your word for it..."
    call ton_main("This really is the best job ever!", "grin", "wide", "shocked", "mid")
    m "Very good! That shall be all for now, [tonks_name]."
    call ton_main("Have a good night, [ton_genie_name].","base","happyCl","base","mid")

    # Tonks leaves.

    call increase_house_points("s", 40)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T1_E4: #Level 1 Event 4
    #Tender make-out session with a Slytherin lesbian
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 7 and nt_pr_kiss.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I kissed that cute little Slytherin girl...","open","base","base","mid")
                call ton_main("She getting there!","base","happyCl","base","mid")
                m "Very good, [tonks_name]."
                call ton_main("Thank you, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points("s", 40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    call ton_main("I have a story for you!", "grin", "base", "shocked", "mid")
    g9 "Let's hear it!"
    call ton_main("This is so good, I feel I should write it down and turn it into a novel...","base","happyCl","base","mid")
    g9 "About a boy snogging his teacher?"
    call ton_main("No.{w} About a tender and confused girl...", "crooked_smile", "closed", "base", "mid")
    call ton_main("Who's coming to terms with her sexuality, thanks to her stunningly intelligent teacher.", "soft", "wink", "annoyed", "mid")

    call ton_main("That little Slytherin girl is starting to come around to me more often - as of late...", "crooked_smile", "narrow", "base", "mid")
    call ton_main("So, I figured now might be a good time to take it to the next level...", "base", "base", "base", "R")
    call ton_main("Getting her to stay after class is easy enough now...","open","closed","base","mid")
    call ton_main("I just brush her hand as I walk past her... and throw her a subtle wink.", "horny", "narrow", "base", "mid")
    g9 "You're getting brazen!"
    call ton_main("Wasn't that the plan?", "upset", "base", "shocked", "R")
    m "I never said it was a bad thing..."
    call ton_main("Good!{w} Because I don't intend on slowing down...", "crooked_smile", "closed", "annoyed", "mid")
    call ton_main("Not after what happened today!","horny","base","angry","mid")
    call ton_main("She was so cute!...", "open", "happyCl", "worried", "mid")
    call ton_main("Still nervous, but not nearly as cocky...", "soft", "base", "shocked", "R")
    call ton_main("Today, she simply let her reddened cheeks do most of the talking... Until the end of my lessons...", "grin", "narrow", "base", "mid")
    call ton_main("And, once the classroom had emptied out, I offered to purchase another favour from her.", "base", "closed", "base", "mid")
    call ton_main("It's not as if she'd say no at this stage.", "soft", "wink", "base", "mid")
    call ton_main("I believe she wasn't expecting me to ask for a kiss though... It really threw her for a loop...", "crooked_smile", "narrow", "base", "mid")
    m "....................."
    call ton_main("She couldn't quite work out whether it was too extreme of a favour... or too mild...", "annoyed", "base", "shocked", "R")
    m "Well, it all depends on how you kiss..."
    call ton_main("*Hmmm*... Yes!","horny","base","base","ahegao")
    call ton_main("For an emotionally charged schoolgirl, she really didn't let me down one bit...", "horny", "base", "annoyed", "up")
    call ton_main("Her lips kept quivering...{w} And I'm not sure if it was because of fear... or anticipation...", "soft", "narrow", "base", "R")
    call ton_main("And she gazed at me like a stunned deer... Waiting for me to make the first move...", "soft", "narrow", "base", "mid")
    call ton_main("*Mmmm*... Her lips were so soft!", "soft", "base", "base", "up")
    g9 "This is good!"
    g9 "Did you slip in some tongue?"
    call ton_main("*Mhmm*... More than some...", "horny", "base", "base", "stare")
    call ton_main("I was surprised just how easily she opened her mouth for me...", "grin", "base", "shocked", "mid")
    call ton_main("Once my tongue was in there - it was game-over for her!", "soft", "closed", "base", "mid")
    call ton_main("I just softly cradled her head - and spent the next five minutes teaching her how to \"french\"...", "soft", "base", "shocked", "up")
    call ton_main("They can't offer you an experience like that at the Ministry!", "grin", "wink", "base", "mid")
    g9 "Consider yourself lucky then."
    call ton_main("Oh, I do!{w} Believe me!", "crooked_smile", "closed", "shocked", "mid", hair="horny")
    m "That shall be all for now..."
    call ton_main("Thank you, [ton_genie_name].", "soft", "narrow", "base", "mid")

    # Tonks leaves.

    call increase_house_points("s", 40)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 2 ###

label nt_pr_kiss_T2_E1: # Tier 2 Event 1 # Not in use.
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)
    m "How did your extracurricular activities pan out today?"
    call ton_main("Honestly? I don't think I've ever been as turned on in my life...","base","base","base","mid")
    call ton_main("Fuck... It was incredible... the power I felt over him... it was intoxicating...","base","base","base","mid")
    m "Care to elaborate?"
    call ton_main("Well, you know that stuck up little Slytherin I've been fooling around with?","base","base","base","mid")
    m "The guy or the girl?"
    call ton_main("The boy.","base","base","base","mid")
    m "Yep, I think I remember them..."
    call ton_main("I asked them to stay back after classes again... Even if it was by staring at them during class...","base","base","base","mid")
    call ton_main("Either way... He knew he had to stay behind to play with \"auntie\" Tonks...","base","base","base","mid")
    m "Kinky..."
    call ton_main("Mmmm, I walked over to him slowly... Making sure I savoured that frightened look on his face...","base","base","base","mid")
    call ton_main("Then, I got to his desk... I was half expecting him to blabber on about not deserving to be there...","base","base","base","mid")
    call ton_main("But today he just looked up at me with a delectable mix of fear and anticipation...","base","base","base","mid")

    # Genie starts jerking off

    #">Unable to help yourself any longer, you start to inconspicuously stroke your cock under your desk."
    #call ton_main("*tsk* *tsk* *tsk*...{w} Couldn't help yourself, could you?"
    #m "Can you blame me?"
    #call ton_main("I suppose not..."
    #call ton_main("Anyway, back to that cute little thing..."

    call ton_main("Eventually I'd had enough of his eager expression...","base","base","base","mid")
    call ton_main("I pounced upon him... Sitting down on his lap, pinning him to his chair and forcing my chest into his...","base","base","base","mid")
    call ton_main("I could feel his heartbeat... It was so fast... Like a mouse...","base","base","base","mid")
    call ton_main("Whispering in his ear I asked if he wanted a little kiss...","base","base","base","mid")
    call ton_main("Making sure to let him know that I'd pay him plenty of points...","base","base","base","mid")
    call ton_main("Just for a kiss...","base","base","base","mid")
    m "*Mmmmm*..."
    call ton_main("Of course he said yes... Even if it was so faint I could barely hear it...","base","base","base","mid")
    call ton_main("But once he said it... I was on him...","base","base","base","mid")
    call ton_main("I pinned him down as I held his head in place...","base","base","base","mid")
    call ton_main("Ugh... My tongue was going crazy...","base","base","base","mid")
    call ton_main("I'm not sure if you remember this from school, sir, but I'm an Metamorphmagus...","base","base","base","mid") # Note: I'd wait with adding Tonks' abilities and reserve them for the 2nd level of favors (longer tongue, bigger breasts...)
    call ton_main("Normally I just use that to blend in or for jokes...","base","base","base","mid")
    call ton_main("But sometimes I use it to... Play around...","base","base","base","mid")
    call ton_main("And all the excitement today may have caused me to lose control of my tongue...","base","base","base","mid")
    m "Lose control of your tongue?"
    call ton_main("Ugh... it was so long...","base","base","base","mid")
    call ton_main("It was like I was fucking that poor boys mouth with it...","base","base","base","mid") # Note: This section is a bit too extreme for the first level.
    call ton_main("I wrapped his tongue in mine... stuck it down his throat...","base","base","base","mid")
    call ton_main("Ugh... I even licked his face clean...","base","base","base","mid")
    call ton_main("By the time I was done there wasn't a dry spot on his face...","base","base","base","mid")
    m "*Argh*..."
    call ton_main("Poor thing... I think I broke him if I'm being honest...","base","base","base","mid")
    m "That's it..."
    call ton_main("I thought he'd like it... but there were so many tears--","base","base","base","mid")

    #g9 "UGH... THERE IT IS!!!"
    # Genie cums
    #">You begin firing a load of under your desk, making a dull thud with each blast hitting against the backboard..."

    call ton_main("*Mmmm*, looks like you enjoyed our little lesson as well...","base","base","base","mid")
    m "Ugh... can you blame me? That was... Ugh..."
    call ton_main("I told you I knew how to kiss...","base","base","base","mid")
    m "I believe you... that'll be all for now..."
    m "I need to clean up..."
    call ton_main("Very well... Thank you, sir.","base","base","base","mid")

    call ton_walk(action="leave")
    jump end_tonks_event

label tonks_teacher_event_3_6: #Level 2 Event 2
    #Spends afternoon making out with ravenclaw, topless

    return

label tonks_teacher_event_3_7: #Level 2 Event 3
    #Tonks has two best friends make out while she plays with herself

    return

label tonks_teacher_event_3_8: #Level 2 Event 4
    #Another make out sesh with slytherin involving tonks fingering the student

    call ton_walk(action="leave")
    jump end_tonks_event
