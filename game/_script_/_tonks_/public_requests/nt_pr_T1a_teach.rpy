

### Tonks Teaching ###

# Detention with Tonks
# (Tonks gives students detention or lets them stay after class)
# (Gets to see the boy's dicks, the girl's panties, punishs them...)
# (Gives hours points to each of the students)

#TODO Add Tonks chibi to all her public request nightly reports

label nt_pr_teach_start:
    call ton_main("","base","base","base","mid", xpos="right", ypos="base", trans=fade)

    if ton_tier == 1:

        if nt_pr_teach.points == 0:
            call ton_main("So, what's the plan?", "open", "base", "base", "mid")
            m "The plan?"
            call ton_main("You know, how does this go down?", "soft", "base", "base", "mid")
            call ton_main("I'm hardly a regular when it comes to this stuff.", "open", "base", "base", "R")
            m "It would be best if we start small, don't you think?"
            m "You should build up a bit of a reputation for yourself, before we start trying anything crazy."
            call ton_main("A reputation?", "normal", "base", "raised", "mid")
            call ton_main("Think I'll get a nickname?{w} Maybe they'll call me touchy tonks?", "soft", "narrow", "shocked", "mid")
            m "Maybe..."
            call ton_main("What did you do with Hermione on her first favour?", "open", "narrow", "shocked", "down")
            m "*Ugh*... I think I got her to make \"a silly face\", or something..."
            call ton_main("You paid her for that? I expected something a little more...{w=0.4} Perverse.", "crooked_smile", "base", "base", "R")
            if hg_pf_admire_panties.counter != 0:
                m "In that case, the first \"real\" favour I bought was getting her to lift her skirt for me."
                call ton_main("That's more like it!","horny","base","base","mid")
                call ton_main("But, even though we're in Scotland, none of the boys are wearing skirts...","open","base","base","L")
            elif hg_pf_admire_breasts.counter != 0:
                m "In that case, the first \"real\" favour I bought was getting her to show me her bra."
                call ton_main("That's more like it!","horny","base","base","mid")
                call ton_main("Although it's not a big deal for boys to show you their chests...","open","base","base","L")
            else:
                m "Yes, Granger is greedy when it comes to points..."
                call ton_main("I'm not interested in just chatting with my Students! I get to do that all day...", "annoyed", "base", "raised", "downR")
            m "Just get them to show you their dicks then."
            call ton_main("Oh, wow! Are you serious?", "crooked_smile", "wide", "shocked", "stare")
            m "I don't see why not."
            m "It isn't such a big deal for a boy to show a girl his wiener..."
            call ton_main("Seeing their dicks... That does sound good...", "soft", "happyCl", "base", "mid", cheeks="blush")
            call ton_main("Can I touch them?", "horny", "narrow", "raised", "mid")
            m "Let's stick with looking for now..."
            call ton_main("Fine... So how many am I allowed to look at?", "annoyed", "base", "base", "down")
            m "As many as you like..."
            call ton_main("And how many points am I allowed to give out?", "soft", "base", "base", "L")
            m "Look, I'm not really convinced these points are real..."
            m "I just say \"Ten points to Gryffindor!\" And these girls do whatever I want for some reason..."
            $ gryffindor += 10
            m "So as far as I'm concerned, hand out as many as you want."
            call ton_main("All right... Well, I better get to class.","base","base","base","R")
            call ton_main("I've got some boys to \"teach\"...", "horny", "narrow", "raised", "mid", hair="neutral")
            m "Don't forget to come back here after classes to fill me in."
            call ton_main("Will do...","base","happyCl","base","mid")

        else: # Repeat
            m "Ready to help the boys earn some points?"
            call ton_main("And reward them for showing me their dicks?", face="horny")
            m "Yes. Return to me after class..."
            call ton_main("*Mhmm*... Don't worry if I'm a little late though...", face="horny")

    elif ton_tier >= 2:

        if nt_pr_teach.points == 0: # Tell her to be even lewder for the next level of favors.
            m "Would you like to give some boys detention again?"
            call ton_main("And what would you suggest I do with them?", face="horny")
            call ton_main("Make them show me their dicks?", face="horny")
            call ton_main("Or can we move on to something a little more... progressive?", face="horny")
            m "If that's what you want..."
            call ton_main("*Hmm*...{w=0.4} Yes...{w=0.3} I wouldn't mind seeing the {b}hard cocks{/b} of some of my favourites.", face="horny")
            call ton_main("Might even have them jerk off for me... I would love to see that!","horny","base","base","ahegao")
            m "And make sure they remember it."
            call ton_main("Yes, [ton_genie_name]. Don't wait for me...","base","base","base","mid")

        else: # Repeat
            m "Ready to give some boys detention again?"
            call ton_main("Yes. I'm very much in the mood for some {b}hard cocks{/b}!", face="horny")
            g9 "Go on then... Teach them a lesson..."
            call ton_main("I shall see you later, [ton_genie_name]...","base","base","base","mid")

    # Tonks leaves

    $ nt_pr_teach.inProgress = True

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 1 ###

label nt_pr_teach_T1_E1: #Tier 1 - Event 1 - Slytherin boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hello, [ton_genie_name].","base","base","base","mid", xpos="mid", ypos="base", trans=fade)
    call ton_main("I'm back with my report...", "horny", "narrow", "base", "mid")

    if ton_reputation <= 3: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I had some fun with that Slytherin boy again...","horny","base","angry","mid")
                call ton_main("Gave him a couple of points for his house.","open","base","base","R")
                m "Well done, [tonks_name]... We'll talk next time."
                call ton_main("Yes, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points("s", 20)
                if ton_reputation < 4: # Points til 4.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How were your... \"extra curricular activities\" today?"
    call ton_main("It's such a rush!", "grin", "happyCl", "base", "mid")
    call ton_main("I can't believe how naughty I feel!", "soft", "base", "base", "ahegao")
    m "So I take it you managed to sneak a peek?"
    call ton_main("Sort of... I didn't really see it.", "mad", "base", "base", "R")
    call ton_main("But it was still incredible...", "base", "happyCl", "base", "mid")
    call ton_main("*Ugh*... that look on his face...", "mad", "base", "base", "ahegao")
    m "What did you see then?"
    call ton_main("Well, this sweet little Slytherin student had been staring at my breasts all lesson...","base","base","base","down")
    call ton_main("So, naturally, I get him to stay behind after class.","open","closed","base","mid")
    call ton_main("I couldn't tell if he was angry about it, or just scared...", "soft", "base", "base", "R")
    call ton_main("But, as his teacher, I insisted that he should write out some lines to correct his behaviour...", "open", "closed", "base", "mid")
    m "Do I need to ask what he had to write?"
    call ton_main("\"I shall not stare at my teacher's big, beautiful breasts\"...", "soft", "base", "base", "ahegao")
    m "Was the \"big\" and \"beautiful\" part really necessary?"
    call ton_main("Oh, that's not the best bit...", "horny", "wide", "base", "mid")
    call ton_main("I went on to lecture him just how \"naughty\" and \"wrong\" it is for a student to peek at his teacher's tits......", "soft", "wink", "annoyed", "mid")
    call ton_main("Oh, and I made him pull down his trousers while he wrote his lines!", "silly", "narrow", "base", "mid")
    m "So you did see it!"
    call ton_main("He still had his underwear on...","open","base","base","R")
    call ton_main("If I had pushed him any further... he probably would've snapped!", "soft", "base", "base", "downR")
    call ton_main("Besides, I could still see how {b}hard{/b} he was...", "base", "closed", "annoyed", "mid")
    call ton_main("It was crazy...", "silly", "base", "base", "stare")
    call ton_main("I started to really tease him at the end... while he wrote out the last of his lines...", "grin", "narrow", "shocked", "mid")
    m "That poor boy..."
    call ton_main("Don't worry, I just whispered in his ear a little...", "horny", "narrow", "base", "R")
    call ton_main("Told him what a naughty boy he'd been...", "horny", "base", "shocked", "mid")
    call ton_main("While my boobs dug into him... and my nipples poked into his back...", "soft", "narrow", "base", "stare")
    call ton_main("His underwear was practically {b}soaked{/b} in pre-cum.", "horny", "narrow", "shocked", "stare")
    m "And do you think he'll spread the word about you?"
    call ton_main("I sure hope so...","base","base","base","down")
    call ton_main("He earned twenty whole points from me today!","base","happyCl","base","down")
    call ton_main("Certainly he won't be able to keep his eyes off me anymore...", "soft", "narrow", "shocked", "mid")
    m "Very good."
    m "And try to reward those \"evil Slytherins\" with at least double the amount of points."
    call ton_main("If you say so, [ton_genie_name]...", "soft", "narrow", "base", "R")
    call ton_main("It's so... iniquitous... what we are doing.{w} I fucking love it!", "base", "base", "shocked", "stare")
    m "That'll be all now..."
    call ton_main("Thank you, [ton_genie_name].", "horny", "wink", "base", "mid")
    call ton_main("Sweet dreams.", "grin", "narrow", "base", "mid")

    # Tonks leaves

    call increase_house_points("s", 20)

    if ton_reputation < 4: # Points til 4.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T1_E2: # Tier 1 - Event 2 - Racenclaw boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 3: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I was fooling around with my favourite Ravenclaw boy again...","horny","base","angry","mid")
                call ton_main("And he earned a bunch of points from me.","base","happyCl","base","mid")
                m "Well done, [tonks_name]... We'll talk next time."
                call ton_main("Yes, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points("r", 10)
                if ton_reputation < 4: # Points til 4.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How were your classes today?"
    call ton_main("*Mmmm*... Long and hard...", "soft", "base", "base", "stare")
    call ton_main("Just how I like them...", "grin", "base", "shocked", "mid")
    m "I take it you were able to steal a few glances?"
    call ton_main("It was even better than I thought it'd be!", "grin", "closed", "base", "mid")
    call ton_main("Who knew they'd be so nervous!", "base", "wide", "base", "mid")
    m "What happened?"
    call ton_main("Well, I figured I'd have to be alone with a student, to convince them to whip it out for me...", "base", "base", "base", "R")
    call ton_main("So I gave the cutest little thing I could find detention...", "grin", "base", "shocked", "mid")
    call ton_main("Poor boy... I'm not sure he'd ever even been in trouble before.", "grin", "base", "raised", "R")
    call ton_main("So, when the bell rang, he immediately began babbling about how sorry he was for speaking in class, and that he'd never do it again...", "base", "closed", "shocked", "mid")
    call ton_main("*Ugh*... I had to hold myself back from jumping on him right then and there...", "horny", "closed", "angry", "stare")
    call ton_main("Anyway, I eventually managed to calm him down and tell him it'll be okay.", "soft", "base", "base", "stare")
    call ton_main("I even let him know that, if he was a good boy, he could earn some points for his house.", "base", "narrow", "base", "mid")
    m "Did he like the sound of that?"
    call ton_main("You should have seen his eyes light up! Like a kid on Christmas!", "grin", "base", "base", "R")
    m "You fooled around with a kid?"
    call ton_main("What? No of course not.{w} Every student is of age here...", "open", "shocked", "angry", "mid")
    call ton_main("And he didn't look like a kid at all down there...", "grin", "base", "base", "stare")
    call ton_main("(He was so fucking hung!)", "horny", "base", "shocked", "ahegao")
    call ton_main("It was child's play... Getting what I wanted from him.", "soft", "base", "angry", "R")
    m "..................."
    call ton_main("*Mmmm*, I even had him play with himself for a little bit...", "horny", "base", "base", "stare")
    call ton_main("Fuck, he looked tasty...", "open_wide_tongue", "narrow", "base", "ahegao")
    m "*Ahem*... So did you award him his points or just tease him?"
    call ton_main("Don't worry, I made sure Ravenclaw was paid handsomely.","base","happyCl","base","mid")
    m "And did he look like the kind to talk?"
    call ton_main("Probably not...","upset","base","base","R")
    m "Well, try and get a talker next time..."
    m "We're trying to build your reputation, remember?"
    call ton_main("I'll try...", "annoyed", "happyCl", "base", "mid")
    call ton_main("(Although, I'll have to play with this one a few more times...)", "horny", "narrow", "base", "stare")
    m "That will be all for now, [tonks_name]."
    call ton_main("Thanks, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    call increase_house_points("r", 10)

    if ton_reputation < 4: # Points til 4.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys. Guess who...
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 3: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I had some fun with those two Gryffindor boys again...","horny","base","base","R")
                call ton_main("Of course I didn't give them any points...","open","closed","base","mid")
                call ton_main("I wouldn't want Gryffindor to have an unfair advantage.","horny","base","angry","mid")
                call ton_main("They practically begged me if they could do it for free anyway...","open","base","base","R")
                m "Well done, [tonks_name]... Until next time."
                call ton_main("Have a good night, [ton_genie_name].","base","happyCl","base","mid")
                if ton_reputation < 4: # Points til 4.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How'd it go?"
    call ton_main("Great! I even managed to convince two boys to show me their dicks...", "grin", "base", "base", "mid")
    call ton_main("At the same time!", "horny", "wink", "base", "mid")
    g9 "Two at once? Congratulations!"
    call ton_main("Yep... To be honest, they probably would have done it for free.", "crooked_smile", "happyCl", "base", "mid")
    call ton_main("Not that they turned down the offer of points, though...", "base", "base", "base", "mid")
    m "Care to elaborate?"
    call ton_main("Alright then... you old perv...", "base", "base", "shocked", "R")
    call ton_main("Normally I'd just have the cutest thing that takes my eye stay behind after class...","open","base","base","R")
    call ton_main("For a little one-on-one time...", "horny", "base", "base", "stare")
    call ton_main("But I actually had to punish these two idiots for real.", "upset", "closed", "annoyed", "mid")
    m "What did they do?"
    call ton_main("*Ugh*... They just wouldn't shut up during the whole lesson!", "upset", "base", "base", "mid")
    call ton_main("And then they tried to lift a girl's skirt with \"wingardium leviosa\"...", "mad", "base", "base", "R")
    g9 "A classic."
    call ton_main("They reminded me of my younger self...", "horny", "narrow", "base", "R")
    call ton_main("Which probably meant that they were going too far...", "upset", "base", "base", "mid")
    call ton_main("So... I kept them after class... Gave them the whole lecture about \"responsibility\" and \"respect\"...","open","closed","base","mid")
    m "................"
    call ton_main("Then I told them that I'd pay them both ten points, to show me their cocks... {heart}", "grin", "closed", "base", "mid", cheeks="blush")
    m "Just like that?"
    call ton_main("Well, there's a lot more subtlety to it in practice...", "soft", "base", "base", "stare")
    call ton_main("Not that I think I needed subtlety, given how horny they were...", "crooked_smile", "base", "shocked", "mid")
    call ton_main("I think those poor buggers actually thought I was going to jerk them both off...", "horny", "narrow", "base", "stare")
    call ton_main("Still, I think they had a fun time.", "soft", "wink", "base", "mid")
    m "Any chance they'll tell their friends about it?"
    call ton_main("Oh yes! The Gryffindor common room is probably a buzz already!", "grin", "closed", "shocked", "mid")
    call ton_main("It wouldn't surprise me if I start getting asked to give more boys detention...", "horny", "base", "shocked", "mid")
    m "Fooling around with Gryffindors and rewarding them isn't too helpful for our situation..."
    m "But great work nonetheless..."
    call ton_main("Thank you, [ton_genie_name]. That means a lot coming from you.","base","happyCl","base","mid")
    m "Even if it is encouragement for seducing your students?"
    call ton_main("Even then.", "base", "narrow", "base", "mid")
    call ton_main("Well, I better get back to work, these halls aren't safe unless there's a teacher on patrol.", "horny", "base", "base", "R")
    m "(I'm not sure they're safe with her on patrol...)"

    # Tonks leaves

    call increase_house_points("g", 20)
    if ton_reputation < 4: # Points til 4.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if ton_reputation <= 3: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I confronted that little Slytherin girl again...","horny","base","base","mid")
                call ton_main("Although, I kept myself in check with her... didn't want to scare her away again...","open","base","base","R")
                call ton_main("But she was very happy about the points.","base","base","angry","mid")
                m "Well done, [tonks_name]..."
                call ton_main("Yes, [ton_genie_name]. Good night.", "silly", "happyCl", "base", "mid")
                call increase_house_points("s", 20)
                if ton_reputation < 4: # Points til 4.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "Did you manage to sneak a peek today?"
    call ton_main("*Umm*... I'm afraid not...", "open", "narrow", "base", "R")
    m "Oh..."
    call ton_main("But I do have a story for you!","base","happyCl","base","mid")
    m "Why didn't you just start with that? You had me worried for a moment!"
    call ton_main("Are you that desperate to hear about me \"fooling around\" with my students?", "horny", "narrow", "annoyed", "mid")
    m "I'm desperate to hear {b}anything{/b}..."
    m "This office isn't exactly riveting to listen to..."
    call ton_main("In that case, I'll try and add some flair to it.", "base", "closed", "base", "mid")
    call ton_main("Once upon a time--", "open", "wide", "base", "R")
    m "*Ahem*..."
    call ton_main("Too much?", "crooked_smile", "happyCl", "base", "mid")
    m "Just a tad."
    call ton_main("So, I know my job is to try and balance out the favour trading a little...", "soft", "narrow", "base", "R")
    call ton_main("But I just couldn't help myself today...", "normal", "base", "worried", "R")
    m "Help yourself? You mean..."
    call ton_main("*Ugh*... I don't normally mess around with girls...", "open", "base", "base", "down", cheeks="blush")
    call ton_main("(Not since I left here anyway...)", "mad", "base", "raised", "R")
    call ton_main("But today there was {b}the tastiest morsel{/b} I have ever seen in my class!", "horny", "wide", "base", "stare")
    m "...................."
    call ton_main("Now, I know when I'm being checked out, I can feel anyone's eyes on me...", "open", "closed", "shocked", "mid")
    m "...................."
    call nar(">You nod, unconsciously... Gazing directly at her tits...")
    call ton_main("And most of the time I don't mind... I might even encourage it from time to time...", "base", "narrow", "shocked", "mid")
    with hpunch
    pause.8
    call nar(">Tonks gives her boobs a subtle little shake.")
    g9 ".................."
    call ton_main("So, when I felt a pair of cute little eyes struggling their hardest not to stare at me...", "horny", "base", "annoyed", "down")
    call ton_main("I just {b}had{/b} to play with her!","horny","base","base","ahegao")
    m "*Mmmm*... what happened?"
    call ton_main("Nothing much... I'm pretty sure she would have freaked if I tried anything...", "soft", "base", "base", "stare")
    call ton_main("So I just asked her to stay after class for a little... \"chat.\"", "base", "base", "shocked", "mid")
    m "What did that chat involve?"
    call ton_main("Well, what do you think?", "horny", "base", "shocked", "mid")
    call ton_main("I just sat directly in front of her desk...","open","base","base","mid")
    call ton_main("Asked her if she was doing well in class...", "normal", "base", "base", "R")
    call ton_main("If anything was making her feel... distracted...", "base", "closed", "annoyed", "mid")
    call ton_main("All the while I was playing with the buttons on my shirt...", "soft", "base", "shocked", "down")
    call ton_main("*Ugh*... I've never seen someone so flustered...", "horny", "base", "base", "stare")
    call ton_main("Eventually, it got too much for her, so she just yelled that I was wasting her time and ran off in typical Slytherin fashion.","open","closed","base","mid")
    m "Do you really think she was looking at you?"
    call ton_main("After that? There's no doubt... She's hooked.", "base", "narrow", "annoyed", "mid")
    call ton_main("Now I've just got to reel her in.", "grin", "base", "base", "R")
    call ton_main("If that's all right with you, sir!", "soft", "base", "base", "mid")
    m "You're asking for my permission?"
    call ton_main("Well, I was only supposed to buy favours from the boys...","open","closed","base","mid")
    g9 "Eat your heart out!"
    m "Just make sure you keep me in the loop..."
    call ton_main("Thanks, [ton_genie_name].","base","base","base","mid")
    m "Did she receive any points for it?"
    call ton_main("Well, not this time...", "open", "base", "shocked", "R")
    m "I think you should give her some anyway."
    g9 "For being a tease!"
    call ton_main("Very well...", "grin", "base", "base", "mid")
    call ton_main("Twenty points for Slytherin!","open","closed","base","mid")
    call ton_main("Now, if you don't mind... It's getting a bit late...","open","base","base","R")
    m "Yes. You may leave..."
    call ton_main("Good night, [ton_genie_name].","base","happyCl","base","mid")
    m "Good night, [tonks_name]."

    # Tonks leaves

    call increase_house_points("s", 20)

    if ton_reputation < 4: # Points til 4.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 2 ###

label nt_pr_teach_T2_E1: # Tier 2 - Event 1 - Hufflepuff girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Guess what happened, [ton_genie_name]!","base","happyCl","base","mid", xpos="mid", ypos="base", trans=fade)

    if nt_pr_teach.points <= 4 and ton_reputation <= 8: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"................\"":
                pass
            "\"You made that Hufflepuff girl squirt again?\"":
                call ton_main("Yes! Right on point! I'm impressed...","open","base","raised","mid")
                call ton_main("I just got done cleaning my desk...","horny","base","base","down")
                call ton_main("And I didn't use my wand to clean it...","horny","base","angry","mid")
                m "Very good, [tonks_name]..."
                call ton_main("Thank you, [ton_genie_name]. Until next time...","base","base","base","mid")
                call increase_house_points("h", 40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "*Umm*... You found the golden ticket?"
    call ton_main("Better! I had a student come to me to sell a favour!", "grin", "base", "base", "mid")
    m "And you haven't bought a favour from them before?"
    call ton_main("Not one! They're not even in any of my classes!", "grin", "base", "base", "R")
    m "Very good! Word must be getting around that you're... \"purchasing.\""
    m "So what house is he in?"
    call ton_main("Oh... *Umm*... it wasn't a he...","base","base","base","down")
    call ton_main("I hope that's fine... I know I'm supposed to be balancing out the favours for the boys...", "mad", "base", "shocked", "mid")
    m "Right..."
    m "(I'd forgotten about Miss Granger's dumb \"M.R.M.\" thing...)"
    m "(Does she even still run that?)"
    m "I wouldn't worry about that too much... As long as you're also buying from the boys, I don't think it should matter."
    call ton_main("Good... Because there was no way I could turn down this cute little Hufflepuff...", "grin", "closed", "base", "mid")
    call ton_main("Poor thing must have spent hours building up the courage...", "base", "wink", "base", "mid")
    m "So what did you buy from her?"
    call ton_main("Well... I asked her what sort of favour she wanted to sell me...", "soft", "narrow", "base", "R")
    call ton_main("She was so flustered... And probably didn't plan this far ahead at all...", "grin", "happyCl", "base", "mid")
    call ton_main("She started babbling on and on, so I calmed her down by letting her know what favour I wanted...", "soft", "narrow", "base", "L")
    g9 "Was it something naughty?"
    call ton_main("Naturally...", "horny", "closed", "base", "mid")
    call ton_main("She just sort of stood there after I told her, stunned for a little bit...", "soft", "closed", "base", "mid")
    call ton_main("I rushed to the door and made sure it was locked.", "soft", "base", "base", "R")
    call ton_main("After that, I sat down in the front row of the class, and told her to sit on my desk...", "grin", "base", "shocked", "mid")
    m "*Mmm*, now that's a front row seat to die for."
    call ton_main("All that was missing was a bucket of popcorn...", "horny", "wide", "annoyed", "mid")
    call ton_main("Eventually, she was able to muster up enough courage to pull up her skirt...","base","base","angry","mid")
    call ton_main("Poor thing only thought to ask how many points she'd be paid after she lifted her skirt though.", "silly", "happyCl", "base", "mid")
    call ton_main("I told her five for showing me her panties...", "soft", "base", "base", "R")
    m "Only five?"
    call ton_main("She said the same. I explained that showing her plain white panties only gets five points.", "base", "closed", "annoyed", "mid")
    call ton_main("If she were to take those panties off though... Then that might get Hufflepuff an extra twenty...","horny","base","angry","mid")
    m "Did she say yes?"
    call ton_main("She didn't say anything... but she pulled them down all the same...", "soft", "closed", "base", "mid")
    call ton_main("","base","base","angry","mid")
    g9 "Nice! Getting a student to strip on the first favour is hard work!"
    call ton_main("Oh, we're not done yet...","open","closed","base","mid")
    call ton_main("After soaking in the view for a while, I started to notice she was soaking as well...","horny","base","angry","mid")
    call ton_main("So... I offered her forty points to play with herself... for me...","open","closed","base","mid")
    m "*Mmmm*... Go on..."
    call ton_main("*Ugh*... It was amazing!{w} She was so nervous... the expression on her face looked incredible...","horny","base","base","ahegao")
    call ton_main("That, and the soft mewling while she did it...","horny","base","angry","mid")
    call ton_main("It was that perfect combination of \"slutty need\" and \"statuesque beauty\"...","base","base","base","ahegao")
    call ton_main("I wanted to taste her so badly...","open_wide_tongue","wide","base","ahegao")
    g9 "..................."
    call ton_main("It was a struggle to hold myself back... I don't think she would've been ready for that just yet...","open","closed","worried","mid")
    m "...................."
    call ton_main("But she was more than ready to squirt all over my table...", "silly", "happyCl", "base", "mid")
    g4 "She did what?!"
    call ton_main("*Ugh*... I had to spend ten whole minutes scourgifying the desk afterwards...", "mad", "base", "shocked", "down")
    m "*Ah*... Very good..."
    call ton_main("","base","base","base","mid")
    m "I think that should be all for now..."
    g4 "Much more of this, and I'll need to \"scour-ify\" my own desk as well..."
    call ton_main("I can help you with that.","horny","base","angry","mid")
    m "Maybe some other time..."
    call ton_main("*Mmmm*... okay then, [ton_genie_name].", "base", "base", "annoyed", "mid")
    call ton_main("I better be on my way as well now...","open","base","base","R")
    call ton_main("(Fuck knows, I could use a bit of \"alone time\" myself...)", "base", "base", "base", "stare")

    # Tonks leaves

    call increase_house_points("h", 40)

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy
    #TODO Have a few drops of cum on her clothes when she comes in
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hello, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if nt_pr_teach.points <= 4 and ton_reputation <= 8: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("Remember that cute boy?","open","base","base","mid")
                call ton_main("Every time he shot out some cum for me I gave him five points...","horny","base","angry","mid")
                m "I bet he earned quite a lot today. Well done, [tonks_name]..."
                call ton_main("That he did, [ton_genie_name]... See you next time...","base","base","base","mid")
                call increase_house_points("r", 20)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How did your day go?"
    call ton_main("The teaching was a little dull...", "upset", "base", "base", "stare")
    call ton_main("Simple wards, hex-detection, basic stuff...", "soft", "base", "base", "stare")
    call ton_main("Not that anyone else would think so, with how much they all struggled with it...", "upset", "base", "annoyed", "R")
    m "I was more interested in hearing about your... \"extracurricular\" activities..."
    call ton_main("I know, I just wanted to get that off my chest.", "upset", "closed", "base", "mid")
    call ton_main("I'd complain to someone else, but I'm not that fond of the other teachers...", "annoyed", "base", "base", "down")
    m "Like who?"
    call ton_main("Well, McGonagall is as stuck-up as ever and Slughorn is a gross weirdo...", "open", "closed", "shocked", "R")
    call ton_main("Anyway, let's get on with the story, shall we?", "grin", "wink", "base", "mid")

    menu:
        "-Let her know about the cum-":
            $ choice_flag=True
            m "You do know that you've got some cum on you?"
            call ton_main("*Hmm?*...","base","base","base","down")
            call ton_main("Oh...", "mad", "base", "shocked", "down")
            call ton_main("That cheeky bugger! I can't believe he actually shot it that far...","open","base","base","down")
            m ".................."
            call ton_main("Best to start from the beginning...", "soft", "closed", "base", "mid")
        "-Ignore it-":
            $ choice_flag=False
            pass

    call ton_main("So, I spent a little time with my favourite Ravenclaw student today...", "soft", "narrow", "base", "down")
    m "Another detention session after class?"
    call ton_main("I don't need to resort to detention anymore... He's learned what a wink in class means.", "grin", "wink", "base", "mid")
    call ton_main("Plus, I think a few of the other students have worked out what it means as well.", "base", "narrow", "base", "R")
    call ton_main("There were a few whispers today... Hopefully that helps get the word out...", "soft", "base", "base", "mid")
    m "I bet."
    call ton_main("So, after class, I locked the door like normal and went over to him...","open","base","base","R")
    call ton_main("Let him know that I wanted another favour...","open","closed","base","mid")
    call ton_main("He wanted to sell me a kiss today... I almost took him up on it...", "horny", "base", "base", "stare")
    call ton_main("I think he was a little disappointed when I told him I wanted another look...", "grin", "base", "shocked", "R")
    call ton_main("So I told him I didn't {b}just{/b} want to look at it...", "soft", "narrow", "shocked", "mid")
    call ton_main("But watch him play with it...", "horny", "narrow", "annoyed", "mid")
    m "Make him an offer he can't refuse..."
    call ton_main("His eyes truly lit up after that...", "base", "happyCl", "base", "mid", hair="horny")
    call ton_main("He just kept on staring at me, while he started stroking it...", "horny", "narrow", "base", "mid")
    call ton_main("Getting it hard for his teacher...","horny","base","base","ahegao")
    call ton_main("*Mmmm*... The way he was staring at my tits... with such hunger...", "soft", "closed", "shocked", "mid")
    call ton_main("I just {b}had{/b} to get them out for him...", "silly", "base", "shocked", "mid")
    g9 "Nice!"
    call ton_main("They got him even more excited...", "horny", "base", "base", "ahegao", cheeks="blush")
    call ton_main("He even started to speak after that...", "base", "closed", "base", "mid", cheeks="blush")
    m "What did he say?"
    call ton_main("The usual stuff...", "soft", "base", "base", "R")
    call ton_main("How pretty I was, how nice my tits looked...", "crooked_smile", "base", "base", "down")
    call ton_main("You know how guys are...", "base", "base", "annoyed", "mid")
    call ton_main("What was weird was... when he started to call me mommy again...", "upset", "closed", "base", "mid")
    m "What a wimp."
    call ton_main("Don't be cruel, [ton_genie_name]! It's just a little dirty talk...", "soft", "base", "raised", "R")
    call ton_main("And you have to admit, it's kinda hot... I even joined in on it.", "base", "narrow", "base", "mid")
    m "Really?"
    call ton_main("What do you think made him fire his load across the room?", "horny", "narrow", "base", "mid")
    call ton_main("All it took was me saying \"cum for Mommy\"... and he had shot the biggest load towards me.", "horny", "closed", "base", "mid")
    call ton_main("","base","base","angry","mid")
    m "Fuck... That {b}is{/b} pretty hot..."
    call ton_main("I know...", "crooked_smile", "narrow", "base", "mid")
    call ton_main("*Ugh*... I definitely have to go rub one out after this...", "mad", "base", "base", "ahegao")
    call ton_main("See you, [ton_genie_name].", "base", "narrow", "base", "L")

    if choice_flag:
        m "Are you going to do anything about the cum?"
        call ton_main("*Hmm?*... The cum?","upset","base","worried","down")
        call ton_main("Oh... Why bother...", "soft", "base", "base", "down")
        call ton_main("It was already there on my way over here.", "soft", "closed", "shocked", "mid")
        call ton_main("Besides, it'll be good for spreading the word, don't you think?", "horny", "narrow", "base", "mid")
        m "Whatever you say..."

    m "Goodbye, [tonks_name]."

    # Tonks leaves

    call increase_house_points("r", 20)

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T2_E3: # Tier 2 - Event 3 - Slytherin boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("[ton_genie_name]...", face="horny", xpos="mid", ypos="base", trans=fade)

    if nt_pr_teach.points <= 4 and ton_reputation <= 8: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("This Slytherin dickhead was asking for trouble again!", "mad", "base", "angry", "R")
                call ton_main("I did my best to punish him... thoroughly...","horny","base","angry","mid")
                m "Very good, [tonks_name]..."
                call ton_main("*Mhmm*... Until next time, [ton_genie_name]...","base","happyCl","base","mid")
                call increase_house_points("s", 20)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "How'd your favour go today?"
    call ton_main("It was all right...","open","base","base","R")
    call ton_main("I was able to kill two birds with one stone, though.", "base", "closed", "annoyed", "mid")
    m "I'm intrigued."
    call ton_main("So, I had some cocky little brat from Slytherin cause all sorts of trouble in class.", "open", "narrow", "annoyed", "downR")
    call ton_main("Talking... letting a chocolate frog loose... forgetting to lock his \"Monster Book of Monsters\"...","open","closed","base","mid")
    m "(His what?)"
    call ton_main("Just being a general pain in the ass.","open","base","angry","R")
    m "Sounds like a hassle."
    call ton_main("Slytherins always are.", "upset", "base", "base", "stare")
    call ton_main("Anyway, I let him know he'd earned himself detention after class.","open","closed","base","mid")
    call ton_main("Little bastard cursed me out for that... Disrespected me in front of the entire class...", "upset", "base", "angry", "mid")
    call ton_main("Once the class had emptied out, I proceeded to lock the door... to scare him a little...", "soft", "base", "annoyed", "R")
    call ton_main("After that I let him know that his \"Punishment\" was going to be selling me a favour.", "soft", "closed", "base", "mid")

    call ton_main("I made him pull down his pants and whip his cock out...", "open", "base", "shocked", "mid")
    call ton_main("At first the idiot thought I was going to jerk him off...", "disgust", "base", "shocked", "R")
    call ton_main("I might have, if he'd played his cards right...", "open", "narrow", "base", "mid")
    call ton_main("Instead, his favour wouldn't be nearly as fun.", "soft", "narrow", "shocked", "R")
    call ton_main("I demanded of him to start jacking it...", "soft", "base", "annoyed", "mid")
    call ton_main("It was actually pretty cute at first...", "open", "closed", "base", "mid")
    call ton_main("Then just as he was about to blow his load...", "soft", "closed", "base", "mid")
    call ton_main("Boom! Petrficus Totalus!", "scream", "shocked", "angry", "mid", trans=vpunch_repeat)
    m "{i}Petrifi{/i}-{w} {i}Petrifico{/i}?-{w} {i}Petrificato{/i}--"
    call ton_main("I petrified him!", "open", "wide", "angry", "mid")
    m "*Ahh*..."
    call ton_main("*Ha-ha-ha*... You should have seen his look on his face!", "silly", "happyCl", "base", "mid")
    call ton_main("That's what he gets, the little shit!", "mad", "base", "angry", "down")
    call ton_main("Not only did I leave him blue balled... I also left him pants down in the class.","base","base","angry","mid")
    m "Forever?"
    call ton_main("No, just until the spell wears off...","open","closed","base","mid")
    call ton_main("In an hour or so...","upset","base","angry","R")
    call ton_main("That, or someone else finds him...","upset","base","base","up")
    call ton_main("Either way, he learned his lesson about not screwing around in my class.","open","closed","base","mid")
    m "Very good..."
    call ton_main("Thank you, Sir...","base","base","base","mid")
    call ton_main("See you...","base","happyCl","base","mid")

    # Tonks leaves

    call bld
    m "(This bitch might be crazier than I thought...)"

    call increase_house_points("s", 20)

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T2_E4: # Tier 2 - Event 4 - Slytherin girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans=fade)

    if nt_pr_teach.points <= 4 and ton_reputation <= 8: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                call ton_main("This cute Slytherin girl earned herself a couple of points from me today...","open","base","base","R")
                call ton_main("She's really starting to get into it!","base","base","angry","mid")
                m "Good work, [tonks_name]..."
                call ton_main("Thank you... Have a good night, [ton_genie_name]...","base","base","base","mid")
                call increase_house_points("s", 20)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                call ton_walk(action="leave")
                jump end_tonks_event

    m "Anything interesting happen today, [tonks_name]?"
    call ton_main("Oh yes!... I broke new ground today...", "silly", "base", "shocked", "mid")
    m "That's very promising... So what happened?"
    call ton_main("Remember that cute little Slytherin?","horny","base","base","mid")
    call ton_main("The one that's still coming to grips with her budding sexuality?","base","base","angry","mid")
    m "The girl that you're turning into a lesbian?"
    call ton_main("Well, I had her stay back after class today...", "horny", "closed", "base", "mid")
    call ton_main("For someone who supposedly hates selling favours... she was surprisingly keen today...", "base", "base", "shocked", "mid")
    m "Maybe she's finally coming around..."
    call ton_main("I got her to give me a little peek under her skirt, for twenty house points...", "base", "narrow", "base", "down")
    call ton_main("And, after she'd pulled up her skirt, I did the old... \"offer more points for something else\" trick...", "grin", "base", "base", "mid")
    call ton_main("Had her drop her panties as well.", "base", "narrow", "base", "down")
    call ton_main("I was expecting her to at least argue at least a bit about the amount of points she would receive for it...","open","base","base","R")
    call ton_main("But she dropped them in an instant, without even hearing my offer.", "horny", "base", "annoyed", "mid")
    call ton_main("Next, she just looked at me as if to ask, \"what next?\"","open","base","base","mid")
    call ton_main("*Ugh*... It was so fucking hot...", "soft", "base", "base", "stare", hair="horny")
    g9 "And?... What did happen \"next?\""
    call ton_main("I had her play with herself...", "grin", "closed", "shocked", "mid")
    call ton_main("But... that cute face of hers... and all the teasing...", "open", "closed", "shocked", "R", cheeks="blush")
    call ton_main("I decided to take matters into my own hands...", "grin", "base", "base", "stare", cheeks="blush")
    call ton_main("Specifically her matter...","horny","base","base","mid")
    m "You couldn't help yourself, could you?"
    call ton_main("Can you blame me for wanting to \"finger\" that cute little slut?", "soft", "base", "annoyed", "mid", cheeks="blush")
    g9 "You're a bad teacher, you know that?"
    call ton_main("Tell me about it...", "horny", "narrow", "base", "up")
    m "What did she have to say about the whole thing?"
    call ton_main("Not much...", "soft", "narrow", "base", "R")
    call ton_main("She just looked up at me, with those puppy-dog eyes... whispering \"wow\" and \"don't stop\" to me...", "base", "narrow", "shocked", "up")
    call ton_main("To think only a couple of days ago she tried pretending not to be into me...","open","closed","base","mid")
    m "Think she'll start talking now?"
    call ton_main("Not unless she's ready to out herself as bi...", "annoyed", "base", "base", "R")
    call ton_main("But there are already some whispers going around school...", "base", "base", "annoyed", "down")
    call ton_main("And I may or may not have contributed to that...", "grin", "base", "base", "R")
    m "Very good work."
    m "That'll be all then..."
    call ton_main("Thank you, [ton_genie_name]...","base","happyCl","base","mid")
    call ton_main("See you next time...","base","base","base","mid")

    # Tonks leaves

    call increase_house_points("s", 20)

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    call ton_walk(action="leave")
    jump end_tonks_event
