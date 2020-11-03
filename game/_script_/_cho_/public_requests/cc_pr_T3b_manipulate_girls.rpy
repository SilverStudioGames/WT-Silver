

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_manipulate_girls_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_manipulate_girls.is_event_complete(3, 1): # Completed Alicia Spinnet?
        # Alicia Spinnet

        if not cc_pr_spy_girls.is_event_complete(3, 2):
            # Return if player has not spied on Alicia just yet.
            m "Let’s try and manipulate the girls on the enemy team!"
            call cho_main("You're expecting me to just jump in blind?", "angry", "base", "base", "mid")
            call cho_main("I don't know any of these girls, how do you expect me to manipulate them in any way without knowing what I'm dealing with?", "annoyed", "wide", "base", "mid")
            m "Good point, perhaps we should consider spying on them a bit beforehand."

            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "I think it's time to manipulate the female members of the enemy team a bit and see if we can find some way to distract them during the game."
        call cho_main("And how do you suggest we do that?", "annoyed", "base", "raised", "mid")
        m "Well, the Slytherin \"brutes\" seemed to think they had a pretty good chance to get with you during the last game."
        call cho_main("They're idiots though, I barely had to do anything.", "soft", "base", "base", "R")
        m "Which means it's even more important to try and entice those girls before the match itself..."
        call cho_main("...", "disgust", "base", "raised", "down")
        m "It's all about throwing them off their game, like you said... if the girls won't get thrown off by you wearing some outfit then maybe an emotional... bond... would be more appropriate."
        call cho_main("Don't you think we'd have an easier time focusing on the boys?", "upset", "base", "base", "mid", cheeks="blush")
        m "Sometimes the hard route is the right one to take... you shouldn't dismiss it."
        g9 "(Since those girls sound freaky...)"
        call cho_main("But Harry is the seeker and Ron is the keeper... wouldn't it be more useful if--", "open", "wide", "base", "mid", cheeks="blush")
        m "I'm certain my reasoning is correct here, are you questioning your trainer?"
        call cho_main("...", "upset", "base", "base", "R", cheeks="blush")
        call cho_main("No...", "open", "base", "base", "R")
        g9 "Great, then off you go..."
        g9 "Time to make your team proud!"
        g9 "Pride is important!"
        call cho_main("...{w}I suppose...", "soft", "base", "base", "mid")
        call cho_main("Wish me luck...", "horny", "base", "base", "mid")
        g9 "Good luck..."

    elif not cc_pr_manipulate_girls.is_event_complete(3, 2): # Completed Katie Bell - Part 1?
        # Katie Bell - Part 1

        if not cc_pr_spy_girls.is_event_complete(3, 3):
            # Return if player has not spied on Katie just yet.
            m "Let's try and manipulate--"
            call cho_main("I'm going to stop you right there...", "soft", "base", "angry", "mid")
            m "Yes?"
            call cho_main("There's no way I'll try this again before I know more about the girls.", "annoyed", "base", "angry", "mid")
            m "Why? I thought it went great with the Spinnet girl!"
            call cho_main("She cornered me!", "scream", "wide", "angry", "mid")
            m "And?"
            call cho_main("I'm not going to attempt the other two unless I know a bit more about them...", "upset", "base", "angry", "R")
            m "Fine..."


            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "One down, two to go..."
        m "I think it's time to manipulate one of the other Gryffindor girls."
        call cho_main("Who do you want me to target this time?", "open", "base", "raised", "mid")
        m "Katie Bell!"
        call cho_main("So, we're still set on targeting the girls?", "upset", "base", "raised", "mid")
        g9 "Of course, I'm sure we got but a taste last time...{w=0.4} No pun intended."
        call cho_main("...", "angry", "closed", "base", "mid")
        m "I hope you've  remembered what you learned from her. This girl likes being treated rough so show some assertiveness with her and I'm sure she'll fall for you."
        call cho_main("Okay...", "open", "narrow", "base", "down", cheeks="blush") #looking down a bit worried
        g9 "Assertiveness!"
        call cho_main("...", "clench", "base", "raised", "mid") #Changes from worried looking down to looking at genie
        call cho_main("Yes, I will!", "mad", "base", "raised", "mid")
        g9 "Great, off you go!"

    elif not cc_pr_manipulate_girls.is_event_complete(3, 3): # Completed Katie Bell - Part 2?
        # Katie Bell - Part 2

        # No return here since it's just a continuation of previous Katie event.

        m "Follow that girl again!"
        call cho_main("Sir?", "mad", "base", "raised", "mid")
        m "I mean... Today's mission is to follow that Bell girl again..."
        call cho_main("But... isn't one time enough?", "disgust", "narrow", "base", "mid", cheeks="blush")
        call cho_main("My butt is still sore from last time...", "clench", "narrow", "base", "downR", cheeks="blush")
        m "There can never be too much of a good thing."
        call cho_main("Fine...", "open", "narrow", "base", "down", cheeks="blush")
        m "Excellent, make sure to come back with an extensive report as usual B."
        call cho_main("Got it...", "soft", "base", "base", "mid", cheeks="blush")

    elif not cc_pr_manipulate_girls.is_event_complete(3, 4): # Completed Angelina Johnson?
        # Angelina Johnson

        if not cc_pr_spy_girls.is_event_complete(3, 4):
            # Return if player has not spied on Angelina just yet.
            m "Let's try and manipulate--"
            call cho_main("I'm going to stop you right there...", "soft", "base", "angry", "mid")
            m "Yes?"
            call cho_main("There's no way I’ll try this again before I know more about the girls.", "annoyed", "base", "angry", "mid")
            m "Fine..."

            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "You seem to have gotten to know the Gryffindor girls quite well by now [cho_name]."
        g9 "If you're not careful you might turn into one yourself."
        call cho_main("As if, Ravenclaw always comes first!", "angry", "base", "base", "mid", cheeks="blush")
        g9 "You do? No shame in that!"
        m "So...{w=0.4} Today we're up against their team Captain, Angelina Johnson."
        m "Once you've managed to bond with her you'll have no problem winning the cup."
        call cho_main("Yes!", "grin", "closed", "base", "mid")
        call cho_main("We're so close I could almost taste it!", "horny", "happyCl", "base", "mid")
        g9 "I'm sure you will!"
        g9 "Now go get her..."
        call cho_main("Yes [cho_genie_name]!", "smile", "base", "base", "R")
    else:
        # Repeatable events.

        m "Let's manipulate those girls some more!"
        call cho_main("More? Haven't I done it enough already?", "clench", "base", "raised", "mid")
        m "There's always room for more bonding."
        call cho_main("Okay then...", "open", "base", "raised", "down")
        m "Make sure to bring me your report as usual B."
        call cho_main("Yes [cho_genie_name]!", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_manipulate_girls.inProgress = True

    jump end_cho_event

### Return Events ###

### Tier 3 (pre Gryffindor) ###

label cc_pr_manipulate_girls_T3_alicia:
    # Alicia Spinnet
    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "normal", "narrow", "base", "down", cheeks="blush", xpos="mid", ypos="base", trans=fade)

    m "Back so soon? I wasn't expecting you for another hour."
    call cho_main("...", "normal", "narrow", "base", "down", cheeks="blush") #Blushing
    m "Are you alright? How did it go with the girls?"
    call cho_main("Fine...", "open", "narrow", "base", "down", cheeks="blush") #Blush
    m "So, did you manage to connect with them in an emotional way?"
    call cho_main("...", "annoyed", "closed", "base", "mid", cheeks="blush")
    m "[cho_name]?"
    call cho_main("You could say that.", "upset", "narrow", "base", "mid", cheeks="heavy_blush")
    m "Tell me what happened."
    call cho_main("Well...", "disgust", "base", "base", "R", cheeks="blush")
    call cho_main("My plan was to try and approach Alicia Spinnet without the other two around.", "open", "base", "base", "down", cheeks="blush")
    call cho_main("So, I gestured her to come over to me as the other two entered the changing room...", "open", "base", "raised", "mid", cheeks="blush")
    m "Nicely done. Splitting up the group makes it less likely they'll gang up on you."
    call cho_main("That's what I thought... and I felt pretty confident in my plan as she approached me.", "soft", "closed", "base", "mid", cheeks="blush")
    call cho_main("But before I even got a word out she had come up and kissed me on the lips!", "quiver", "base", "raised", "mid", cheeks="blush")
    g4 "Whoa, wait what?"
    g4 "I thought the plan was for you to make the advances here..."
    call cho_main("You and me both!", "clench", "base", "raised", "mid", cheeks="blush")
    m "Do you know why she just came up and kissed you like that?"
    call cho_main("Well, apparently she saw me when I entered the girls bathroom...", "horny", "base", "base", "R", cheeks="blush")
    call cho_main("And assumed I had followed her in there because I wanted to get in on the action...", "annoyed", "narrow", "base", "mid", cheeks="blush")
    g9 "Smart girl. She figured out you were perving on her!"
    call cho_main("I'm not perving on anybody! I only followed her into that bathroom to gather information!", "horny", "happyCl", "angry", "mid", cheeks="blush")
    g9 "But I'm sure you liked sneaking a peek at her moist muff regardless."
    call cho_main("How was I to know she wasn't wearing any panties...", "clench", "closed", "angry", "mid", cheeks="blush") # annoyed
    m "Be that as it may, this Alicia girl seems to be one step ahead of us..."
    m "So, what happened next B?"
    call cho_main("She started kissing me again, and placed a hand on one of my butt cheeks...", "angry", "narrow", "base", "down", cheeks="blush")
    m "Correction, she's two steps ahead of us..."
    m "Sounds to me like you got a fan on the Gryffindor team..."
    g9 "That girl has the hots for you, that's for sure!"
    call cho_main("*Tzzs!*... Those sluts would probably make out with anybody...", "clench", "closed", "raised", "downR", cheeks="heavy_blush")
    m "Tongue or no tongue?"
    call cho_main("Sorry?", "normal", "base", "raised", "mid", cheeks="blush") #Blush, shocked
    m "Did she slip you any tongue or what?"
    call cho_main("How is that relevant to anything?", "upset", "base", "base", "downR", cheeks="blush")
    m "Did she though?"
    call cho_main("...", "normal", "base", "raised", "down", cheeks="blush") #blush
    g9 "I knew it!"
    g9 "I hope you were at least courteous enough to return the favour..."
    g9 "Tongue kissing and a butt squeeze... Now that's what I'd call a true challenger!"
    call cho_main("...", "base", "narrow", "base", "down", cheeks="blush") #Glaring
    m "What happened next?"
    call cho_main("She broke off the kiss and slapped my butt cheek, before running off to the changing rooms.", "angry", "base", "base", "mid", cheeks="blush")
    m "Sounds to me like a job well done, [cho_name]."
    call cho_main("But I didn't even do anything!", "clench", "wide", "base", "mid", cheeks="blush")
    m "Yet you achieved exactly what I asked of you, you formed an emotional bond with her."
    m "Now we only have to do the same with the other two..."
    call cho_main("So that's what this emotional bonding is all about? Getting them to kiss me?", "mad", "narrow", "raised", "mid", cheeks="blush")
    m "Not kissing specifically..."
    call cho_main("...", "annoyed", "closed", "base", "down", cheeks="blush")
    m "And now I'd like you to entice the other two as well."
    call cho_main("Sure, no problem... I'll just walk up to one of them and they'd throw themselves at me, just like Spinnet did!", "normal", "narrow", "angry", "R", cheeks="blush") #Sarcastic
    m "Great plan!"
    m "But for now you better get some rest and ready yourself to take on the other two."
    call cho_main("...", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Don't look so dejected, [cho_name]. You had a beautiful girl kiss you today... surely you can't be disappointed by that?"
    call cho_main("It's...{w=0.4} it's not that...{w=0.4} I'm just used to it being me who...", "annoyed", "closed", "base", "mid", cheeks="blush")
    call cho_main("...", "upset", "closed", "base", "mid", cheeks="blush") #Blush
    call cho_main("Never mind, good night then.", "normal", "base", "base", "downR", cheeks="heavy_blush")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_part1:
    # Katie Bell - Part 1

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("...", "normal", "narrow", "base", "down", cheeks="blush", xpos="mid", ypos="base", trans=fade)

    m "[cho_name]?"
    call cho_main("...", "normal", "narrow", "base", "down", cheeks="blush")
    m "Hello?"
    call cho_main("Oh... Sorry [cho_genie_name]!", "upset", "closed", "base", "mid", cheeks="blush") #face more focused still blushing
    m "What's the report. Did you manage to bond with the girl?"
    call cho_main("Of course...", "angry", "narrow", "base", "down", cheeks="blush")
    m "Then how did it go? Tell me all the details!"
    call cho_main("All the details...", "upset", "closed", "base", "mid", cheeks="heavy_blush")
    call cho_main("So...{w=0.4} Much like before, my plan was to follow Katie as she wandered off away from the others.", "open", "base", "base", "mid", cheeks="blush")
    call cho_main("And to no surprise... She was once again making her way down towards the lake.", "soft", "narrow", "base", "R", cheeks="blush")
    call cho_main("So I ran up to her and questioned her on where she was headed, and she responded that she was just going for a walk to clear her head.", "open", "narrow", "base", "mid", cheeks="blush")
    m "Yeah right..."
    call cho_main("That's what I said...", "clench", "narrow", "base", "R", cheeks="blush")
    call cho_main("So to try and catch her off guard I bluntly asked her if she wasn't going for another round with those tentacles.", "open", "base", "raised", "mid", cheeks="blush")
    m "Whoa, right to the point!"
    call cho_main("Yes, although she didn't even respond to it and just started walking again...", "angry", "base", "base", "mid", cheeks="blush")
    call cho_main("So I pushed her further and asked what the Gryffindor house would think if they knew...", "soft", "base", "angry", "mid", cheeks="blush")
    call cho_main("But she just kept walking, completely ignoring me.", "upset", "base", "angry", "mid", cheeks="blush")
    call cho_main("I wasn't able to get through to her at all until I said that I would snitch to her captain unless she did something for me.", "clench", "narrow", "base", "mid", cheeks="blush")
    call cho_main("That's when she stopped in her tracks, eyed me up and down and asked what her punishment was going to be.", "disgust", "base", "base", "down", cheeks="blush")
    g9 "Such a naughty girl!"
    call cho_main("I know! That's not at all where I was going with the conversation.", "open", "wide", "angry", "mid", cheeks="blush")
    call cho_main("What I hadn't realized during my failed attempts at confronting her she had been leading me off the path.", "clench", "base", "base", "downR", cheeks="blush")
    call cho_main("Because just as I was about to reply, I felt something tighten around my waist and suddenly I found myself dangling several feet off the ground!", "open", "wide", "base", "mid", cheeks="blush")
    call cho_main("That's when I realized, she had led me all the way to the Whomping Willow!", "clench", "happyCl", "angry", "mid", cheeks="blush")
    m "The whomping what?"
    call cho_main("That darn tree students are told to stay away from...", "upset", "base", "angry", "mid", cheeks="blush")
    call cho_main("It had grabbed both Katie and I, lifting us into the air... I thought we were done for.", "angry", "narrow", "base", "mid", cheeks="blush")
    call cho_main("And for a brief moment we just dangled there until the silence was cut short by a loud snapping sound and a yell.", "clench", "base", "base", "mid", cheeks="blush")
    g4 "Terrifying!"
    call cho_main("It was! Until I realised the tree wasn't even trying to kill us...", "upset", "closed", "angry", "mid", cheeks="blush")
    call cho_main("It had started to vigorously lash its branches about, smacking Katie...{w} and to my horror she was thoroughly enjoying the whole thing.", "disgust", "base", "base", "mid", cheeks="blush")
    g9 "A spanking tree? Seriously?"
    call cho_main("Yes!{w=0.4} And I'm sure this wasn't her first time doing this!", "clench", "base", "raised", "mid", cheeks="blush")
    call cho_main("I couldn't believe what I was seeing, I just stared at her in disbelief...", "disgust", "base", "base", "down", cheeks="blush")
    call cho_main("And at that moment, the tree--", "upset", "happyCl", "angry", "mid", cheeks="blush")
    call cho_main("Smacked one of its branches across my breasts and stomach...", "clench", "base", "angry", "mid", cheeks="blush")
    g9 "Surely a little bit of spanking wouldn't bother a girl as tough as you, would it?"
    call cho_main("Of course it doesn't! I've taken plenty of bruises playing Quidditch, I was just taken by surprise...", "disgust", "base", "base", "mid", cheeks="blush")
    call cho_main("Once I got over that initial shock the tree swiftly moved me right up next to Katie.", "mad", "narrow", "base", "downR", cheeks="blush")
    call cho_main("And I watched as it continuously smacked her with its branches...", "soft", "happyCl", "base", "down", cheeks="blush")
    g9 "I bet she knew you were looking."
    call cho_main("Obliviously, no doubt she was enjoying it even more than the spanking.", "annoyed", "base", "angry", "mid", cheeks="blush")
    call cho_main("And seeing that she was enjoying the attention so much, I decided to revert back to the original plan...", "angry", "base", "base", "R", cheeks="blush")
    call cho_main("Your plan...", "disgust", "base", "base", "down", cheeks="blush")
    m "Yes?"
    call cho_main("To form an emotional bond with her instead...", "disgust", "closed", "base", "mid", cheeks="blush")
    m "Finally took that stick out of your butt, did you?"
    call cho_main("What? There was no stick up my butt!", "mad", "base", "angry", "mid", cheeks="blush")
    m "Figuratively speaking...{w=0.4} All that matters is that you finally accepted that you were enjoying yourself."
    m "Now you can forever cherish this moment with Katie... and that spanking willow."
    call cho_main("Whomping, Sir.", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("And I just took it for what it was... Endurance training! There's nothing wrong with that...", "upset", "base", "base", "mid", cheeks="heavy_blush")
    m "Whatever you want to call it, I do it at least once or twice a day myself."
    call cho_main("Anyhow... After a couple more minutes the tree finally stopped smacking us, and I was able to catch my breath...", "angry", "base", "base", "mid", cheeks="blush")
    m "Sounds like a great workout."
    call cho_main("Yes, it was a workout and a half that's for sure!", "horny", "base", "base", "down", cheeks="blush")
    m "Then maybe we should incorporate it into your training."
    call cho_main("But Sir, the Whomping Willow is still extremely dangerous!", "mad", "wide", "raised", "mid")
    call cho_main("Everybody knows to stay as far away from it as possible!", "open", "wide", "base", "mid")
    m "Because of a little ass spanking? Don't be silly..."
    m "That Katie girl sure took it like a champ... you need to be fearless as well, next time that tree spanks you red!"
    call cho_main("Next time?", "clench", "base", "base", "mid", cheeks="blush")
    m "Just agree on a safe-word, if it gets too much."
    call cho_main("It's a tree! It's not going to agree to anything!", "clench", "wide", "base", "mid", cheeks="blush")
    call cho_main("She tricked me into this!", "scream", "base", "angry", "R", cheeks="blush")
    g4 "..."
    call cho_main("I bet I ruined it anyway...", "annoyed", "base", "angry", "R", cheeks="blush")
    call cho_main("Because as soon as the tree lowered us back to the ground Katie rushed off.", "upset", "base", "base", "downR", cheeks="blush")
    call cho_main("So I couldn't even talk to her...", "clench", "base", "base", "down", cheeks="blush")
    g9 "You kidding me? Talking would've just ruined it at that point!"
    g9 "You just had an amazing experience together, and didn't exchange a word throughout the entire thing. There's no better emotional bonding than that..."
    call cho_main("...", "mad", "happyCl", "base", "down", cheeks="blush") #Blushing
    m "Well, I'd say we're one step closer to taking on the Lions for the finals."
    m "I'm confident you'll be able to tame those lionesses by then."
    call cho_main("I...{w=0.4} of course...", "open", "happyCl", "base", "mid", cheeks="heavy_blush") #Smiles and blushes
    m "You should take some rest now..."
    g9 "You look beat."
    call cho_main("Very well... Good night then.", "annoyed", "narrow", "base", "down", cheeks="blush")
    m "Until next time."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_part2:
    # Katie Bell - Part 2

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="angry", xpos="mid", ypos="base", trans=fade)

    m "Welcome back, any progress?"
    call cho_main("If your goal was to get my ass red raw again then sure, plenty of progress...", "angry", "narrow", "base", "R", cheeks="blush")
    m "Progress is progress... So, what went down today?"
    call cho_main("I followed Katie again... just as you wanted...", "annoyed", "base", "base", "down", cheeks="blush")
    call cho_main("I attempted to strike up another conversation but just like last time, she wasn't really up for chatting...", "open", "base", "base", "mid", cheeks="blush")
    call cho_main("So since she as giving me the silent treatment I asked her if this was another attempt of hers to trick me again.", "open", "closed", "base", "mid", cheeks="blush")
    call cho_main("But she simply shrugged and said that if I was to join her again then I should just be quiet and follow her...", "open", "base", "raised", "mid", cheeks="blush")
    g9 "And, did you?"
    call cho_main("Well, yes...", "disgust", "base", "base", "down", cheeks="blush")
    call cho_main("Since she put it like that, how could I refuse? I'd look like a total wimp!", "upset", "base", "angry", "mid", cheeks="blush")
    call cho_main("I mean... It's only a giant, half-conscious, murderous tree... What's the worst that could happen?", "annoyed", "base", "angry", "mid")
    call cho_main("Having said that...{w=0.4} It ended up being even more intense than last time!", "clench", "base", "base", "R", cheeks="blush")
    call cho_main("Maybe Katie jinxed it this time around... or she forgot to jinx it... who knows.", "soft", "base", "base", "down", cheeks="blush")
    call cho_main("It yanked us into the air with such speed even I wasn't ready for it!", "angry", "base", "raised", "mid", cheeks="blush")
    call cho_main("I had to fight its grip, to at least get some form of control back...", "horny", "base", "base", "downR", cheeks="blush")
    call cho_main("But that was easier said than done as the tree had already snaked some of its branches underneath my clothes... sliding them right off my body.", "soft", "narrow", "base", "down", cheeks="blush")
    g9 "Nice! Just like that?"
    call cho_main("Well I tried to grab them... but it had already moved its branches away from me...", "mad", "base", "base", "mid", cheeks="blush")
    m "What happened to your reflexes... Are you being bested by a tree now?"
    call cho_main("No. I simply let it do its thing to...{w=0.4} impress Katie...", "upset", "narrow", "base", "downR", cheeks="blush")
    call cho_main("I'm sure didn't mind that her clothing got taken off as well... that slut.", "open", "wide", "angry", "mid", cheeks="heavy_blush")
    m "(As well?)"
    call cho_main("Just eyeing me up and down like a piece of meat... right up until...", "clench", "base", "base", "R", cheeks="blush")
    g9 "Yes?"
    call cho_main("The tree threw one of its branches about and swung it at us, smacking our butts...", "soft", "happyCl", "base", "mid", cheeks="blush")
    g9 "Got to bless nature!"
    call cho_main("And It just kept doing it over and over until our cheeks turned all red...", "clench", "base", "base", "downR", cheeks="blush")
    call cho_main("It was as if my body was on fire!", "horny", "narrow", "base", "down", cheeks="blush")
    call cho_main("As it continued, Katie looked up at me and reached out to grab my hand...", "soft", "narrow", "base", "down", cheeks="blush")
    call cho_main("And as I finally managed to grab it, the tree smacked us hard across our cheeks.", "angry", "narrow", "base", "downR", cheeks="blush")
    call cho_main("And with that pain came a sudden rush of relief as Katie tightened her hand around mine.", "smile", "narrow", "base", "down", cheeks="blush")
    g9 "An orgasm, Miss Chang?"
    call cho_main("It...{w=0.4} yes, I think she might've.", "upset", "base", "base", "mid", cheeks="heavy_blush")
    m "Still too early to admit it?"
    call cho_main("Too early to admit what?", "mad", "base", "base", "mid", cheeks="blush")
    m "Never mind... did anything else happen after that?"
    call cho_main("Not much, as far as I recall...", "base", "base", "base", "downR", cheeks="blush")
    call cho_main("All I remember is the tree lowering us to the ground and the sound of Katie's breathing...", "soft", "closed", "base", "mid", cheeks="blush")
    call cho_main("I just laid there for a while catching my breath, until the only thing I could hear was the sound of the forest around me...", "open", "closed", "base", "mid", cheeks="blush")
    call cho_main("Once I recovered, I turned to face Katie but again she was already gone...", "angry", "narrow", "base", "down", cheeks="blush")
    m "Now that's how it's done!"
    call cho_main("Thank you!", "smile", "base", "base", "mid", cheeks="blush")
    m "That shall be all for today..."
    m "You may leave now. Dismissed."
    call cho_main("Good night then.", "base", "base", "base", "mid", cheeks="blush")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_angelina:

    # Angelina Johnson
    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "normal", "narrow", "base", "down", cheeks="blush", xpos="mid", ypos="base", trans=fade)

    if game.weather == "rain":
        g4 "Whoa, you're soaking!"
        call cho_main("Oh, yes... I guess my clothes ended up a little wet...", "base", "narrow", "base", "down", cheeks="blush") #Blushing
    else:
        g9 "Welcome back..."
        call cho_main("...", "normal", "base", "base", "downR", cheeks="blush")
        g4 "You look soaked."
        call cho_main("Oh, yes... I guess my clothes ended up a little wet...", "base", "narrow", "base", "down", cheeks="blush") #Blushing
        m "How? It's not even raining!"
        call cho_main("*Ehm*....", "disgust", "narrow", "base", "mid", cheeks="blush")

    m "So, do you have that report for me?"
    call cho_main("I...{w=0.3} yes...", "horny", "base", "base", "downR", cheeks="blush")
    m "I'm waiting [cho_name]... give me the {i}deets{/i}."
    call cho_main("Of course!", "open", "happyCl", "base", "mid", cheeks="blush")
    call cho_main("Well...{w=0.4} I went to see if I could catch Angelina talking to Madame Hooch again.", "soft", "base", "base", "down", cheeks="blush")
    call cho_main("Determined to get the full context of what was going on this time!", "open", "base", "base", "mid", cheeks="blush")
    call cho_main("I immediately went and hid in the boys changing room as soon as they had gone for lunch to listen in.", "soft", "base", "base", "L", cheeks="blush")
    call cho_main("Although I got there a bit early and they were still in the showers, touching each other and gossiping..", "upset", "base", "base", "mid", cheeks="blush")
    g4 "Hooch and Johnson?!"
    call cho_main("No, the Gryffindor team!", "clench", "narrow", "base", "mid", cheeks="blush")
    m "Right..."
    call cho_main("So, doing my best to eavesdrop on their conversation, I went up to that hole I told you about.", "angry", "closed", "base", "mid", cheeks="blush")
    call cho_main("After a while, as Angelina brought up the subject of spying to the other two Alicia replied that she was already aware.", "open", "base", "base", "mid")
    call cho_main("Katie then chimed in, saying she knew about it as well.", "soft", "base", "base", "mid")
    call cho_main("Which seemed to surprise Angelina at first but she then moved on saying that they need to form some sort of plan.", "open", "base", "base", "mid")
    m "I bet Miss Johnson didn't think they kept anything secret from her..."
    call cho_main("For sure...", "soft", "base", "base", "R")
    m "So, did they come up with a plan?"
    call cho_main("Well, sort of...", "open", "narrow", "base", "down")
    call cho_main("Katie had obviously already thought about it as she immediately responded that she knew exactly how to deal with it...", "soft", "base", "base", "mid")
    call cho_main("But as I waited to find out what it was, they suddenly went quiet, and I couldn't hear any of them.", "angry", "base", "raised", "mid")
    m "Left for the changing room?"
    call cho_main("That's what I thought, until I removed my ear from the hole to have a look...", "disgust", "base", "base", "down", cheeks="blush")
    call cho_main("No, they hadn't left... when I took a peek through the hole I found all three of them staring back at me...", "open", "wide", "base", "mid", cheeks="blush")
    g9 "Busted!"
    g9 "So what did you do, run away?"
    call cho_main("At first I just sort of stood there in shock, not knowing what to do...", "clench", "narrow", "base", "down", cheeks="blush")
    call cho_main("Until Angelina angrily beckoned me to get in there.", "clench", "base", "base", "downR", cheeks="blush")

    g4 "There goes our plan to separate them from each other..."
    call cho_main("Let me finish!", "angry", "happyCl", "base", "mid", cheeks="blush")
    call cho_main("Once I got in there and before Angelina got a chance to do anything, Spinnet came up to me...", "upset", "base", "base", "down", cheeks="blush")
    call cho_main("And just like before, she leaned in and kissed me!", "normal", "wide", "base", "mid", cheeks="blush")
    m "Nice, and you kissed her back?"
    call cho_main("Of course! I wasn't about to blow my cover, was I?", "upset", "base", "angry", "mid", cheeks="blush")
    g9 "Of course..."
    call cho_main("As she kissed me, Angelina shouted at her, asking what the hell she was doing.", "mad", "closed", "base", "mid", cheeks="blush")
    call cho_main("Alicia then broke off the kiss and turned to her, asking what the problem was...", "soft", "narrow", "base", "downR", cheeks="blush")
    call cho_main("Angelina just sort of stared dumbfounded at us until she shouted that I'm the seeker of an enemy team.", "clench", "base", "base", "mid", cheeks="blush")
    g4 "..."
    call cho_main("I honestly thought it was over at that point but that's when Katie joined in...", "soft", "closed", "base", "down", cheeks="blush")
    call cho_main("Telling Angelina off for being mean, saying how it's unfair that I don't have a group of girls to play with after practice like she does.", "base", "narrow", "base", "downR", cheeks="blush")
    g9 "Nice... you got both Spinnet and Bell on your side! Told you that bonding with them would do it!"
    call cho_main("I...{w=0.3} I suppose so.", "base", "happyCl", "base", "mid", cheeks="blush") #Smiles
    call cho_main("Angelina still didn't look convinced though and just stood there with her arms crossed staring at me...", "soft", "base", "base", "downR", cheeks="blush")
    call cho_main("So as an attempt at convincing her... I grabbed Alicia's head and pressed her lips against mine...", "smile", "base", "angry", "mid", cheeks="blush")
    call cho_main("Which was enough to grab Katie's attention, as she then moved up behind me to try and pull my top off.", "soft", "wink", "base", "mid", cheeks="blush")
    g9 "Nicely done!"
    call cho_main("Of course I didn't let her...", "annoyed", "base", "base", "R", cheeks="heavy_blush")
    g4 "Why not? What about your cover?"
    call cho_main("Because...{w=0.3} I...{w=0.4} Well, I didn't blow it okay!", "open", "base", "angry", "downR", cheeks="blush")
    call cho_main("I wasn't going to let her undress me like that... so instead I grabbed her hands and put them under my bra to let her play with my breasts.", "horny", "narrow", "base", "down", cheeks="blush")
    call cho_main("Luckily she didn't seem to think much of it and began massaging them.", "soft", "narrow", "base", "mid", cheeks="blush")
    call cho_main("Angelina on the other hand was not convinced... telling the other girls to step aside...", "angry", "base", "base", "down", cheeks="blush")
    call cho_main("Which they did...{w=0.4} both Alicia and Katie jumped back as Angelina walked up, staring me down.", "disgust", "base", "base", "mid", cheeks="blush")
    m "Scary..."
    call cho_main("I don't think I've ever had a girl scrutinize me like that...", "horny", "base", "base", "down", cheeks="blush")
    m "Especially a naked one..."
    call cho_main("She then smirked at me, saying I must truly be something special if her girls would just throw themselves at me as eagerly as they did.", "soft", "base", "base", "mid", cheeks="heavy_blush")
    call cho_main("I didn't really know how to respond to that so I instinctively took a step back against the wall just as she leaned in and pressed her lips against mine...", "horny", "closed", "base", "mid", cheeks="blush")
    call cho_main("Which took me by such surprise I tripped and slid down onto the wet floor.", "upset", "closed", "base", "mid", cheeks="blush")
    m "Ouch..."
    g4 "(Those Lionesses are animals!)"
    call cho_main("She didn't even apologize and just looked down at me, telling me I kiss like a high-schooler...", "mad", "base", "base", "mid", cheeks="blush")
    call cho_main("That said... didn't stop her from crouching down for another... although this time she put her tongue in there.", "angry", "base", "base", "mid", cheeks="blush")
    g9 "Straight in there!"
    g9 "I hope you returned the favour!"
    call cho_main("I tried to... but as I attempted it, she stopped and stood back up.", "upset", "narrow", "base", "R", cheeks="blush")
    call cho_main("And as I steadied myself to get up as well, she put her foot beneath my skirt and pressed it against my panties which made me slide back down onto the floor.", "open", "wide", "base", "mid", cheeks="blush")
    g9 "..."
    call cho_main("Then, turning back to the others she started chastising them even further, saying she was still mad about what they did...", "open", "base", "base", "mid", cheeks="blush")
    call cho_main("But when doing so, she also started rubbing her foot up and down against my panties.", "disgust", "base", "base", "down", cheeks="blush")
    call cho_main("Both Katie and Alicia didn't seem to notice as they had turned towards Angelina to defend themselves.", "horny", "base", "base", "downR", cheeks="blush")
    call cho_main("I don't remember exactly what they were saying at that point...", "angry", "happyCl", "base", "mid", cheeks="blush")
    m "(not surprising...)"
    call cho_main("She just kept rubbing me more and more as they were arguing and...", "horny", "closed", "base", "mid", cheeks="blush")
    call cho_main("I just...{w} couldn't...{w} hold it in at that point!", "soft", "closed", "base", "mid", cheeks="blush") #ahegao?
    m "She made you--"
    call cho_main("She made me orgasm as I lay there on the ground!", "horny", "base", "base", "up", cheeks="blush")
    call cho_main("Which they all realised as they stopped arguing to look at me...", "clench", "base", "base", "up", cheeks="blush")
    call cho_main("Angelina's expression quickly changed into a smile as she pressed her foot down even harder, telling me I'd been a naughty girl...", "disgust", "wide", "base", "mid", cheeks="heavy_blush")
    call cho_main("And that the other two shouldn't have been so selfish to keep me all for themselves.", "disgust", "narrow", "base", "downR", cheeks="blush")
    call cho_main("She then stepped off me and made her way out of the showers, beckoning the other two to come with her.", "clench", "base", "base", "mid", cheeks="blush")
    call cho_main("And they just looked at me, giggled, then proceeded to follow her.", "mad", "narrow", "base", "mid", cheeks="blush")
    m "Nice..."
    call cho_main("What do you mean nice?", "mad", "base", "angry", "mid", cheeks="blush")  #large text
    call cho_main("She humiliated me!", "open", "base", "angry", "mid", cheeks="blush")  #large text
    m "She was testing you..."
    call cho_main("She was...", "clench", "wide", "base", "down", cheeks="blush")
    g9 "Yes...{w=0.4} Not only that...{w=0.4} I think you passed!"
    m "Maybe I underestimated those girls... they aren't easy to boss around that's for sure..."
    m "But no matter..."
    call cho_main("...", "upset", "happyCl", "base", "mid", cheeks="blush") #pout
    m "We shall see soon enough what comes from this..."
    m "In any case, what has happened has happened."
    call cho_main("You reckon I ruined it?", "upset", "narrow", "base", "mid", cheeks="blush") #worried
    m "Of course not, you did great!"
    m "But you can't let them take charge like that during the game."
    call cho_main("Yes [cho_genie_name].", "open", "narrow", "base", "down", cheeks="blush")
    m "Good!"
    m "One step closer towards sipping at the fizzy cup!"
    call cho_main("You don't drink from--", "clench", "base", "base", "mid")
    m "Better ready yourself [cho_name]. The finals are looming ever so closer."
    m "You got this."
    call cho_main("Thanks...", "soft", "narrow", "base", "downR") #smiles
    m "Now, time for some rest."
    call cho_main("Yes, good night then [cho_genie_name].", "open", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event
