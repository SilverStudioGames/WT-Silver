

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_spy_girls_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_spy_girls.is_event_complete(3, 1): # Completed shower event?
        # Shower event - looking through the glory hole

        if cc_pr_spy_boys.is_event_complete(3, 1):
            # Player has not spied on boys just yet.

            m "Time for some good old espionage!"
            m "For this mission -- I'd like you to spy on the girls of the Gryffindor team."
            m "When they're alone..."
            call cho_main("When they're alone, [cho_genie_name]?", "open", "narrow", "raised", "mid")
            call cho_main("I can't get into their common room... you should know that.", "soft", "narrow", "base", "R")
            m "There are plenty of other places where girls hang out and gossip..."
            g9 "Want to know the place I'm thinking of?"
            call cho_main("...", "disgust", "narrow", "base", "mid", cheeks="blush") #Blushes
            g9 "That's right, the women's changing room!"
            call cho_main("Fine... I'll see what I can do.", "open", "closed", "base", "mid")
            g9 "Excellent!"
            call cho_main("", "annoyed", "base", "base", "mid")
            m "Report back to me as usual, C."
            call cho_main("\"C\", [cho_genie_name]?", "soft", "base", "raised", "mid")
            g9 "It's your spy name!"
            call cho_main("My spy name, [cho_genie_name]?", "soft", "narrow", "base", "mid")
            call cho_main("The C stands for my Cho, I presume?", "smile", "narrow", "base", "mid")
            m "What?"
            m "No, not your name... I'm not that unimaginative..."
            call cho_main("", "annoyed", "narrow", "base", "mid")
            m "C is your cup-size, is it not?"
            call cho_main("My cup-size?!", "angry", "wide", "base", "mid", cheeks="blush")
            call cho_main("But that's not even correct! Mine is--", "disgust", "happyCl", "base", "mid", cheeks="heavy_blush")
            call cho_main("I mean... where do you get all these ideas from... seriously!?", "upset", "narrow", "angry", "R", cheeks="blush")
            m "So what's your actual size then?{w} B?"
            call cho_main("...", "annoyed", "narrow", "worried", "down", cheeks="blush") #Blushes
            call cho_main("Yes it's B...", "soft", "narrow", "angry", "downR", cheeks="heavy_blush") #Blushes and glances to the side
            g9 "Noted..."
            call cho_main("You're such an old pervert, you know that right?", "annoyed", "narrow", "angry", "mid", cheeks="blush")

        else:
            # Player has spied on the boys

            m "Time for some more espionage..."
            g9 "This time we'll be targeting the girls!"
            call cho_main("The girls? Anyone in particular you want me to spy on, [cho_genie_name]?", "soft", "narrow", "raised", "mid")
            g9 "Why one of them when you could do all at once?"
            call cho_main("All at once?", "clench", "base", "base", "mid")
            m "That's what I said..."
            m "Their changing room should be a good place to start."
            call cho_main("You can't be serious!", "mad", "happyCl", "worried", "mid", cheeks="blush")
            g9 "I know! I surprise myself with how good my plans are sometimes..."
            call cho_main("I'm gonna get caught for sure...", "disgust", "base", "worried", "down", cheeks="blush") # small text
            call cho_main("...", "annoyed", "base", "angry", "down")
            call cho_main("I'll see what I can do...", "annoyed", "narrow", "angry", "mid")
            g9 "Excellent."

        m "Now, to the gadgets..."
        g9 "I've got this great new invention... It's a vibrating magical rod that--"
        call cho_main("A vibrating what?", "open", "base", "raised", "mid")
        m "You could have let me finish, and I would have told you..."
        call cho_main("Wouldn't something like an extendable ear make more sense for eavesdropping?", "open", "narrow", "base", "mid")
        m "Not unless it vibrates..."
        call cho_main("...", "annoyed", "narrow", "angry", "mid")
        m "You don't want it?"
        call cho_main("I'll manage without, [cho_genie_name].", "annoyed", "narrow", "base", "mid")
        m "Suit yourself..."
        m "Anyway, you'd better get a move on..."
        m "I expect your report this evening, B!"
        m "Good luck!"
        call cho_main("Thanks...", "open", "narrow", "angry", "R")

    elif not cc_pr_spy_girls.is_event_complete(3, 2): # Completed Alicia Spinnet?
        # Spy on Alicia Spinnet

        m "Ready for some more espionage, B?"
        call cho_main("I suppose...", "soft", "narrow", "base", "mid")
        call cho_main("Who's the target?", "open", "narrow", "raised", "mid")
        m "Let's do the spinner girl--"
        m "I mean... Let's do Miss Spinnet next."
        call cho_main("Alicia?", "soft", "base", "raised", "mid")
        m "I suggest you try and spy on her when she's not with the other two."
        call cho_main("Why just her?", "soft", "narrow", "base", "mid")
        m "It's the best way to get to know a person, wouldn't you agree."
        m "Maybe she's putting up a front with her friends."
        call cho_main("If you say so...", "annoyed", "base", "base", "R")
        m "Off you go, and good luck!"
        call cho_main("Thanks, [cho_genie_name].", "base", "base", "base", "mid")

    elif not cc_pr_spy_girls.is_event_complete(3, 3): # Completed Katie Bell?
        # Spy on Katie Bell

        m "Ready for some more espionage, B?"
        call cho_main("Of course!", "base", "base", "base", "mid")
        m "Which one of the girls from the Gryffindor team have we yet to spy on?"
        call cho_main("Well, I could spy on Katie...", "open", "base", "raised", "R")
        m "Katie... who again?{w=0.5} That name doesn't ring a bell..."
        call cho_main("Katie Bell, [cho_genie_name].", "soft", "narrow", "base", "mid")
        m "(...)"
        m "Well, now it does..."
        m "Just keep it quiet when you go after her... We're on a spy mission, after all."
        g9 "I don't want you to ring Katie's bell just yet. Well do that later..."
        call cho_main("You want me to do what?", "open", "narrow", "raised", "mid")
        m "Never mind... Off you go."
        call cho_main("Very well... Until later then...", "base", "base", "base", "mid")

        call cho_walk("door", "base")

        call bld
        g4 "Oh, wait... I forgot about the gadgets!"

        call cho_walk(action="leave")

        call bld
        m "(Damn, she must've not heard me...)"

        # End early, cho already left!
        $ cc_pr_spy_girls.inProgress = True

        jump end_cho_event

    elif not cc_pr_spy_girls.is_event_complete(3, 4): # Completed Angelina Johnson?
        # Spy on Angelina Johnson

        m "Ready for some more espionage, B?"
        call cho_main("I suppose... I assume you want me to go after the girls again?", "soft", "base", "base", "mid")
        m "You'd be correct with that assumption..."
        call cho_main("Well, there's only one member I haven't spied on yet, which would be A--", "open", "base", "base", "R")
        with hpunch
        g4 "{b}Johnson!{/b}" # large text
        call cho_main("...", "disgust", "narrow", "base", "mid")
        m "Sorry. Couldn't help myself..."
        call cho_main("I meant to say Angelina, but yes... her.", "annoyed", "narrow", "base", "mid")
        m "She's their team captain, isn't she?"
        m "I can't stress enough that today's performance is of the utmost importance."
        call cho_main("...", "soft", "base", "base", "mid")
        g4 "You can't get caught when you spy on her Johnson--"
        g4 "I mean-- when you spy on Johnson..."
        call cho_main("Of course... So what--", "open", "base", "base", "mid")
        g4 "Utmost!"
        call cho_main("", "upset", "base", "base", "mid")
        g4 "Importance!"
        call cho_main("...", "annoyed", "narrow", "base", "mid")
        m "So are you ready, B?"
        call cho_main("Yes I'm ready...", "soft", "narrow", "angry", "R")
        m "Don't get spotted!"
        call cho_main("Until later then...", "open", "closed", "base", "mid")

    else:
        m "Let's spy on those girls some more!"
        call cho_main("Again? I've already spied on them all...", "soft", "base", "raised", "mid")
        m "You can never get enough intel."
        m "Make sure to bring me your report as usual B."
        call cho_main("Of course.", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_spy_girls.inProgress = True

    jump end_cho_event



### Return Events ###


### Tier 3 (pre Gryffindor) ###

label cc_pr_spy_girls_T3_showers:
    # Showers - looking through the glory hole

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    m "Welcome back!{w=0.3} What's the report, B?"
    call cho_main("...", "annoyed", "narrow", "angry", "downR", cheeks="blush") #Blushing looking away
    m "Did you get any juicy info that we could use against the Gryffindor girls?"
    call cho_main("No juicy info per se...", "open", "closed", "base", "mid")
    m "Then how'd it go, anything you could tell me?"
    call cho_main("Well... I went to spy on them in the showers, just as you asked me...", "soft", "narrow", "worried", "R", cheeks="blush")
    call cho_main("I found a hole in one of the walls, actually...", "annoyed", "narrow", "raised", "mid")
    m "That's unfortunate, I'll have to look into filling that hole at some point..."
    m "So what were they talking about if it wasn't Quidditch?"
    call cho_main("*Ehm*... There wasn't much talking at all...", "disgust", "narrow", "base", "downR", cheeks="blush")
    call cho_main("They were too preoccupied with kissing, and touching each other.", "open", "happyCl", "base", "mid", cheeks="blush")
    g9 "I knew it!"
    call cho_main("*Hmph*...", "annoyed", "narrow", "angry", "mid", cheeks="blush") #annoyed
    g9 "Makes you wish you had those girls on your own team, doesn't it?"
    call cho_main("Yeah right...", "annoyed", "narrow", "angry", "downR", cheeks="heavy_blush") #annoyed glancing to the right #blush
    m "What else did they do?"
    call cho_main("Not a lot to be honest...", "open", "closed", "base", "mid")
    call cho_main("I wasn't going to stay until they were done...", "annoyed", "narrow", "angry", "mid")
    m "Why not? What's the worst that could happen?"
    g9 "They'd catch you -- and ask for you to join in?"
    call cho_main("*Pfff*...{w=0.3} As if...{w=0.3} They'd never let one of their opponents in -- on anything they were doing.", "soft", "narrow", "angry", "downR", cheeks="blush")
    m "At least you considered it."
    call cho_main("I didn't say that.", "mad", "narrow", "angry", "mid", cheeks="heavy_blush")
    call cho_main("I had no idea they were so lewd...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call cho_main("I'm worried that there's little I could do in terms of clothing that would distract them...", "open", "closed", "worried", "mid")
    call cho_main("Seeing how they were crawling over each other's naked bodies...", "annoyed", "narrow", "angry", "mid")
    m "..."
    m "You should've stayed for longer... Perhaps you could've learned a thing or two."
    call cho_main("...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Anyway... I'll think of something..."
    call cho_main("Okay...", "soft", "closed", "base", "mid")
    g4 "Mission accomplished, B!"
    m "You may go now..."
    call cho_main("Good night, [cho_genie_name].", "annoyed", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event


## Alicia Spinnet ##
label cc_pr_spy_girls_T3_alicia:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Cho returns blushing with a vacant expression on her face
    m "Ready for you report, B..."
    m "What's the {i}sitch{/i}?"
    call cho_main("The \"sitch\", [cho_genie_name]?", "soft", "narrow", "raised", "mid")
    m "What's the situation?"
    m "Did you manage to spy on Miss Spinnet?"
    call cho_main("I did...", "open", "closed", "raised", "mid")
    m "Great, tell me what happened."
    call cho_main("She's been assisting the Weasley twins -- by drawing in more customers to their shop.", "open", "narrow", "base", "mid")
    m "How kind."
    call cho_main("I wouldn't call it that...", "soft", "narrow", "base", "R")
    call cho_main("The only reason she's assisting them is because they promised they'd behave during Quidditch.", "open", "narrow", "raised", "mid")

    # Has player sent Hermione to work with the Twins, promoting the cardgame?
    if not first_time_cardgame_work:
        m "(I thought Hermione was helping them with that already...)"

    call cho_main("And she sure doesn't seem to have any problems enticing people.", "soft", "narrow", "base", "mid")
    m "So, how does she do it?"
    call cho_main("Well... If I didn't know better, I'd say she must be using some kind of hypnosis.", "annoyed", "narrow", "angry", "R")
    m "Hypnosis? Now that sounds completely absurd."

    # Has player started imperius curse training?
    if ag_st_imperio.points > 0:
        m  "She's not using that im-perv-ius curse, is she?"
        call cho_main("The Imperius curse?", "open", "narrow", "raised", "mid")
        m "That's what I said..."
        call cho_main("Of course not. That spell is illegal!{w=0.8} She'd be thrown into Azkaban for it...", "soft", "narrow", "angry", "mid")
        m "That's-- *Ehm*...{w=0.3} correct.{w=0.5} Straight into prison..."
        call cho_main("But No... I haven't seen her with a wand in hand...", "open", "closed", "base", "mid")
    else:
        call cho_main("That's why I said, \"if I didn't know any better\"...", "open", "closed", "base", "mid")

    call cho_main("I saw her whisper something into another student's ear...", "soft", "closed", "base", "mid")
    call cho_main("And as if on command -- they immediately followed her into the girls toilets.", "soft", "narrow", "angry", "mid")
    g9 "A girl that takes what she wants... I respect that."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "So, what was she doing with them?"
    call cho_main("Do you really have to ask, [cho_genie_name]?", "open", "narrow", "raised", "mid")
    call cho_main("Surely you're able to guess what they did in there...", "soft", "closed", "base", "mid")
    g9 "No, I have no idea!"
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    g9 "Isn't that why you're here?{w=0.4} to tell me..."
    call cho_main("She was doing lewd stuff with the student, obviously...", "soft", "narrow", "angry", "R", cheeks="blush")
    g9 "Such as?"
    call cho_main("So predictable...", "disgust", "closed", "angry", "mid")
    call cho_main("Well, since I knew you'd ask... I did sneak in after her, and got a glimpse of her kneeling inside one of the stalls...", "soft", "narrow", "angry", "mid")
    call cho_main("And whoever was in there with her wasn't being quiet... that's for sure.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "I should get her number."
    call cho_main("Her what?", "annoyed", "narrow", "angry", "mid")
    m "Never mind... {w=0.4} So is that all you saw?"
    call cho_main("*Ehm*... Yes...{w=0.5} That was it...", "quiver", "narrow", "base", "down", cheeks="blush") #Blushing
    call cho_main("As I said, I could only see her bottom, from underneath that stall...", "open", "narrow", "base", "downR", cheeks="blush") #Blushing
    m "Your face says otherwise... Is that really everything you saw?"
    call cho_main("When I say bottom... She wasn't wearing any panties, [cho_genie_name]...", "disgust", "happyCl", "worried", "mid", cheeks="blush") #Blushing
    call cho_main("She was also...", "soft", "narrow", "worried", "mid", cheeks="blush") #Blushing
    call cho_main("She was also really wet down there...", "horny", "narrow", "worried", "downR", cheeks="blush") #Blushing
    g9 "There it is..."
    call cho_main("I just thought I'd tell you, since she was making a huge mess on the floor!", "soft", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("That's all...", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    m "Of course, thanks for letting me know."
    m "You've done a great job today, B!"
    g9 "Although, I still think my gadgets -- especially the magic rod -- would've been a great help for this mission."
    call cho_main("...", "annoyed", "narrow", "angry", "R", cheeks="blush") #Blushing
    m "I could let you borrow it, to figure out how it works."
    g9 "It's very useful, you know."
    call cho_main("I'm good, thanks...", "soft", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("I think I'll just head straight to bed, if you don't mind.", "soft", "narrow", "base", "downR", cheeks="blush")

    call cho_walk(xpos="door", ypos="base")

    pause .8
    call bld
    m "Changed your mind?"
    call cho_main("N-- no, Good night!", "open", "happyCl", "base", "mid", cheeks="blush") # head

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event


## Katie Bell ##
label cc_pr_spy_girls_T3_katie:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)

    m "Mission successful?"
    m "What did you learn about Katie Bell?"
    call cho_main("She's a freak!", "soft", "narrow", "angry", "mid") # angry
    m "Whoa, that's a bit uncalled for, don't you think?"
    m "I'm sure she looks perfectly fine."
    call cho_main("No, not her looks... what she's been doing.", "open", "closed", "angry", "mid") # blush
    call cho_main("I followed her all the way down to the lake today. And then hid behind a tree to observe her.", "open", "narrow", "angry", "mid")
    m "Something wrong with a little swim?"
    call cho_main("No, but...{w=0.5} she went in there butt-naked!", "disgust", "narrow", "base", "mid", cheeks="blush")
    g9 "Butt-naked? Did they open up a nude-beach without telling me?"
    call cho_main("Of course they haven't!", "angry", "base", "base", "mid", cheeks="blush")
    m "Shame..."
    call cho_main("Once she had taken her clothes off -- she slowly walked into the water -- and then just vanished beneath the surface.", "open", "narrow", "base", "mid")
    m "That's...{w=0.4} odd..."
    g9 "Perhaps she's a mermaid?"
    call cho_main("I highly doubt that, seeing that she has legs...", "open", "closed", "base", "mid")
    call cho_main("Although, for a moment I did consider that the mermaids living there -- might have used their songs to charm her...", "soft", "base", "raised", "up")
    m "Well that's not concerning at all..."
    call cho_main("She did resurface a couple of moments later though... just as I began to worry...", "annoyed", "base", "base", "mid")
    call cho_main("But she emerged with a huge splash -- as she had been lifted into the air by some giant tentacles!", "soft", "base", "angry", "mid")
    g4 "Whoa, tentacles!"
    m "Wait, you're seriously not making this up? Since when do Mermaids have tentacles?"
    call cho_main("I highly doubt it was them...", "open", "closed", "base", "mid")
    call cho_main("I've told you, she's a freak!", "soft", "narrow", "angry", "mid")
    m "So she's into tentacles, *huh*?"
    call cho_main("Yes... Gross, slimy, green tentacles...", "disgust", "narrow", "angry", "down", cheeks="blush")
    call cho_main("She must've used some charm... It was as if the lake had come to life!", "clench", "narrow", "angry", "R")
    g4 "Shiver me timbers!"
    g4 "What a fearless woman, to meddle with such magic?!"
    m "What was it doing to her?"
    call cho_main("*Ugh* Do I really have to tell you...", "disgust", "narrow", "angry", "R", cheeks="blush")
    g9 "With as much detail as possible, thank you."
    call cho_main("Fine...", "annoyed", "narrow", "angry", "down", cheeks="blush")
    call cho_main("They were holding her body stationary in the air -- whilst more of its tentacles were working their way around -- squeezing her breasts.", "soft", "closed", "base", "mid")
    g4 "Classic tentacle move!"
    call cho_main("As it... {w=0.5} continued...{w=0.8} the tentacles grabbed her around the waist and began moving her body up and down -- with another one wrapping itself around her legs.", "clench", "narrow", "worried", "mid", cheeks="heavy_blush")
    call cho_main("She almost looked like a doll being puppeteered by those giant arms...", "soft", "narrow", "angry", "mid", cheeks="blush")
    m "And she was letting it do this willingly?"
    call cho_main("Yes, she seemed to thoroughly enjoy being its...{w=0.8} toy to play with.", "clench", "narrow", "base", "downR", cheeks="blush")
    call cho_main("She looked as if possessed! Being held up in the air like that, with her eyes rolled back into her head.", "soft", "narrow", "angry", "mid")
    call cho_main("Then I watched another tentacle slip through her legs -- which was enough to bring her over the edge, I think.", "mad", "narrow", "raised", "down", cheeks="blush")
    m "Impressive..."
    g9 "Sounds to me like a mission accomplished!"
    call cho_main("Mission... what?", "soft", "narrow", "raised", "mid")
    m "I'm sure you've just learned more about her than even her closest friends."
    call cho_main("", "annoyed", "narrow", "base", "mid", cheeks="blush")
    g4 "She's a girl who likes it dirty, and takes it rougher than even the toughest sea dog can muster!"
    call cho_main("If you say so, [cho_genie_name]...", "soft", "narrow", "base", "R", cheeks="blush")
    g9 "A pervert who doesn't give a hoot about foreplay."
    call cho_main("...", "annoyed", "narrow", "angry", "mid", cheeks="blush")
    g9 "And you definitely know not to entice her with any sort of seaweed."
    call cho_main("Can I go now?", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Yes, you may leave..."
    g9 "Good job today, [cho_name]."
    call cho_main("Thanks...", "soft", "closed", "base", "mid")
    call cho_main("Good Night.", "normal", "narrow", "base", "mid")
    m "Until next time."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event


## Angelina Johnson ##
label cc_pr_spy_girls_T3_angelina:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "normal", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    g9 "Ready for your report, B... lay on me!"
    call cho_main("Don't you mean lay \"it\" on me, [cho_genie_name]?", "soft", "narrow", "raised", "mid")
    m "I'm pretty sure I'm right..."
    m "But before that, tell me how everything went with Miss Johnson!"
    call cho_main("Well enough, I'd say...", "open", "narrow", "raised", "down")
    call cho_main("I stayed behind after practice, to see if I could follow her once they were done changing their clothes.", "smile", "narrow", "angry", "mid")
    call cho_main("To my surprise, she didn't head back to the castle like the others, but went to the referee's office instead...", "base", "narrow", "angry", "mid")
    m "The Referee?"
    call cho_main("Madam Hooch's office, [cho_genie_name].", "soft", "base", "raised", "mid")
    call cho_main("I managed to eavesdrop on their conversation, although I only caught the tail end of it...", "open", "base", "base", "L")
    call cho_main("I suspect Madame Hooch might know what they've been doing in the showers after the game...", "base", "narrow", "angry", "mid", cheeks="blush")
    call cho_main("Angelina was talking about how she couldn't believe that she and her friends were being spied on like that.", "open", "base", "base", "up")
    call cho_main("Madam Hooch just laughed it off and told her she should take it as a compliment.", "grin", "happyCl", "base", "mid", cheeks="blush")
    m "Good to know my staff knows how to diffuse a situation..."
    call cho_main("Angelina sure didn't see it that way -- and stormed right out her office...", "base", "narrow", "angry", "mid")
    m "You sure she wasn't talking about--"
    call cho_main("[cho_genie_name]... If Madame Hooch is spying on them, then Angelina might get the idea to entice her into helping them during the finals!", "annoyed", "narrow", "base", "mid")
    m "*Hmm*... Not a bad idea, now that I think about it..."
    g9 "We should try that as well."
    call cho_main("No! I don't want to win by cheating!", "clench", "narrow", "angry", "mid")
    m "Yes, cause distracting hardly counts as cheating..."
    call cho_main("Well of course it doesn't! It's within the rules!", "open", "closed", "base", "mid")
    m "..."
    call cho_main("We need to do something about it, before Angelina tries to take advantage of the situation...", "soft", "narrow", "angry", "mid")
    m "I'll... figure something out..."
    call cho_main("You'd better!", "annoyed", "narrow", "angry", "mid") #Angry
    call cho_main("So... are we done here?", "base", "narrow", "raised", "mid") #smiles and focuses on genie
    g9 "Yes, mission successful, [cho_name]!"
    m "We'll have that girl wrapped around our--"
    g9 "I mean... around your finger soon enough..."
    call cho_main("Counting on it!", "soft", "narrow", "raised", "mid")
    call cho_main("Good night, [cho_genie_name].", "base", "narrow", "base", "mid")

    #cho leaves
    call cho_walk(action="leave")

    call bld
    g9 "(Wrapped around your finger...{w} good one...)"

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event
