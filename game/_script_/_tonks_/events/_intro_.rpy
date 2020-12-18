

### Tonks Intro ###

label tonks_intro_E1:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "(...)"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "(Can't I even have one quiet day here?...)"
    m "Who is it?"
    ton "It's Tonks--"
    ton "*Ugh*..."
    m "..................."
    ton "I meant, Nymphadora Tonks, Sir."
    m "(Nympho...{w=0.6} what?)"
    ton "Ministry of Magic, Auror division.{w=0.8} May I come in, Sir?"

    if letter_favors.read:
        g4 "(Oh shit, the fuzz!!!)"
        m "(I thought they would have forgotten about those damn letters by now...)"
        ton "Sir, I'm here to discuss an important matter with you regarding your students."
        m "(Governments are all the same with their bloody rules.)"
        ton "Sir?"
        m "(...)"
    else:
        m "(Another female?)"
        m "(She sounds a bit too old to be a student...)"
        m "(...)"

    menu:
        m "(Should I let her in?)"
        "\"Please, come on in.\"":
            call bld
            g9 "(Better to just let my charm play...)"
        "\"Not right now.\"":
            call bld
            ton "But, Sir..."
            ton "I've travelled across half the country just to get here."
            m "........................."
            ton "Via apparition, of course. It only took me a couple of seconds..."
            ton "But still, it's quite a long walk up here from Hogsmeade..."
            ton "I'd just like to get this over with. May I come in, Sir?"
            m "(I wouldn't mind having a look at her...)"
            m "(There is something special about women in uniform...)"
            ton "Sir?"
            m "*Uhm* Yes, you may enter..."

    #Tonks walks in
    call bld("hide")
    pause.2

    call play_sound("door")
    call ton_chibi("stand","door","base")
    call chibi_emote("hearts", "tonks")
    with d3
    pause.5

    call chibi_emote("hide", "tonks")
    with d3
    pause.1

    call bld
    m "*Hmm*?"

    call ton_walk("mid", "base")
    pause.5

    call play_music("tonks")
    call ton_main("Thank you, Professor.","base","base","base","mid", xpos="right", ypos="base", trans=d3)
    m "(Oh shit,{w=0.1}{nw})"
    g9 "(Oh shit,{fast} she's hot...)"
    call ton_main("I apologise for arriving unannounced...{w=0.8} And a couple of days late...","open","base","base","R")
    g9 "Please, I'm glad you could make it."
    call ton_main("I was occupied with some unfinished ministry business. Took me a lot longer to solve than I had anticipated...", "normal", "narrow", "base", "mid")

    call ton_main("I had quite the \"pleasant\" encounter with a group of centaurs.", "soft", "wide", "raised", "R")
    m "Centaurs?!"
    call ton_main("*Mhmm*...","base","base","base","mid", hair="horny")
    call ton_main("As usual, they ignored the boundaries of their allocated territory.", "open", "closed", "base", "mid")
    call ton_main("I had to get them to comply with our rules, to the best of my abilities...", "soft", "base", "base", "mid")
    m "Is that so?..."

    menu:
        "-Start jerking off!-":
            $ masturbating = True
            $ jerked_off_during_tonks_intro = True
            g9 "Tell me more!"

        "-Pay attention-":
            $ masturbating = False
            $ jerked_off_during_tonks_intro = False
            m "Tell me about it..."

    if masturbating:
        call ton_main("Oh... about the centaurs?", "annoyed", "base", "raised", "mid")
        m "Yes, centaurs!"
        g4 "Half of a man, and the other half that of a horse?"
        call ton_main("Yes?", "normal", "narrow", "raised", "mid")
        m "With the bottom half being that of a{w=0.2}.{w=0.2}.{w=0.2}.{w=0.6} horse?!"
        call ton_main("Of course, Sir.", "base", "base", "shocked", "mid")
        g9 "(Sweet!)"
        m "Just wanted to check if I still knew my mythology..."
        g4 "(And it wasn't just dudes with horse heads...)"
        m "(That would have been weird...)"

        call hide_characters
        hide screen bld1
        with d3
        pause.2

        call gen_chibi("jerk_off_behind_desk")
        with d3
        pause.8

        call nar(">You take out your cock and start jerking off.")

        call ton_main("They are fascinating creatures, aren't they, Professor?", "soft", "base", "base", "R", trans=dissolve)
        m "What?{w} Oh yes, very fascinating..."

        call nar("*Fap-Fap-Fap*!")
        m "Don't mind me... Please continue..."
        g9 "I'd like to hear more about the things you did with those centaurs!"
        call ton_main("I'm sorry Professor, but that's classified information.", "open", "closed", "shocked", "mid")
        call ton_main("The Ministry would be furious if they knew that I'd told you!", "upset", "wide", "raised", "mid")
        call ton_main("(Not that I'd mention any of it... They'd probably have me sacked on the spot if they knew...)", "mad", "base", "worried", "R", cheeks="blush")
        call ton_main("(I did the job. That's all that should matter to them...)","upset","base","base","down")
        g4 "Come on! ..."
        call ton_main("I'm sorry, Professor, but I really shouldn't!", "open", "base", "base", "mid")
        call ton_main("Anyway, sharing stories is not why I came here.", "normal", "base", "base", "R")
        m "(Balls...)"

        # Stop Masturbating
        $ masturbating = False
        call hide_characters
        hide screen bld1
        with d3
        pause.2

        call gen_chibi("sit_behind_desk")
        with d3
        pause.8

    else:
        call ton_main("Of course, Sir.","base","base","base","mid")
        call ton_main("I had to make a compelling offer so they'd peacefully return to their assigned territory, which isn't easy...","open","base","base","mid")
        m "(...)"
        call ton_main("You'd never be able to guess how I did it, it's quite the story.","horny","base","base","R", hair="horny")
        call ton_main("Unfortunately, I cannot tell you...{w} Strictly confidential Ministry information...", "soft", "base", "raised", "mid")
        m "(Why? Did she suck them off?)"
        call ton_main("Okay then, let's get this over with.", "open", "narrow", "base", "R")

    call ton_main("Professor Dumbledore, are you aware of why the Ministry has sent me here?", "open", "wide", "raised", "mid", trans=dissolve)

    if letter_favors.read:
        m "More or less..."
        call ton_main("We have received a letter from a Miss named \"Hermione Granger\", about the trading of... \"favours\" between staff and students at this school.", "open", "base", "base", "mid") #not sure if it's better to put miss in quotations or not. My logic is that the fact that she is a "miss" is a given, the name however is something the ministry may not know hence the quotations
        m "Yes she very much enjoys doing that..."
        call ton_main("Trading favours?", "soft", "base", "raised", "mid")
        m "(I wish...)"
        m "No. She enjoys writing letters...{w} lots of 'em..."
    else:
        m "I can't say that I am."
        call ton_main("So you haven't had any complaints from students in regards to \"favour trading\"?","open","base","raised","mid")
        g4 "(Oh, fuck...)"
        g9 "That depends...{w=0.3} What sort of favours are you referring to?"
        call ton_main("...","base","base","angry","mid")
        call ton_main("Well, we've received a letter from a Miss \"Hermione Granger.\"","open","base","base","L") #same here as line 159
        m "Oh, good..."
        g4 "..."

    call ton_main("I take it that you're acquainted with Miss Granger?","open","base","base","mid")
    m "You could say that..."
    call ton_main("Fantastic! Let's get right to it then!", "grin", "base", "base", "mid") #the second line was superfluous. You already established the point of the meeting earlier, so the reader knows what "let's get right to it" means
    m "..."
    show screen blktone
    with d5
    m "(I need to be smart about this...)"
    hide screen blktone
    with d5

    menu:
        m "..."
        "\"I never even touched her!\"":
            call ton_main("Sir?", "upset", "wide", "shocked", "stare")
            call ton_main("I'm sorry Professor, I wasn't accusing you of--", "soft", "base", "worried", "downR")
            m "I did not have sexual relations with that woman."
            call ton_main("Professor! I wasn't implying that--...", "mad", "base", "raised", "mid")
            call ton_main("In the letter she wrote, Miss Granger never accused you of selling favours to your students...", "mad", "base", "raised", "L")
            call ton_main("Nonetheless, she was very persistent that certain other teachers weren't behaving as adequately...", "soft", "base", "base", "mid")

        "\"What did she want?\"":
            call ton_main("Miss Granger wrote about several students, most commonly girls of the Slytherin House, that were inclined to do favours for their male teachers.","open","base","base","R") #Tonks is a hogwarts graduate. Slytherin doesn't need to be in quotations, she knows what it is.
            m "So what?"
            call ton_main("According to her letter, those favours tend to be very...{w=0.1} \"sexual\" in nature...", "soft", "base", "raised", "mid", hair="horny")

    m "(Shit...)"
    call ton_main("Professor, this is a very serious allegation, don't you agree that the ministry is under an obligation to investigate?", "open", "wide", "raised", "mid")
    m "..........................................{w} No?"
    call ton_main("I'm sorry?","upset","base","raised","mid")
    g4 "Well, I can't say I'm very well versed in these...{w=0.8} very,{w=0.6} very rare occurrences."
    m "I was actually just about to begin my own investigation in the matter."
    call ton_main("The Ministry has sent me specifically to determine if there is any truth to Miss Granger's concerns...","open","base","base","L")
    call ton_main("I'll be happy to look into this for you.", "soft", "base", "base", "mid")
    m "Now, now. I wouldn't want you to waste your time with this."
    call ton_main("Don't worry, Professor. {i}Investigation{/i} is in my job description.","base","base","angry","mid")
    call ton_main("I'll just stay for a little while, just to examine these claims and question the students.","open","base","base","R")
    m "That won't be necessary."
    call ton_main("Do have some confidence in me, Professor. This is what I was trained for...","horny","base","base","mid")
    m "................................."
    call ton_main("I've already gotten a room down in Hogsmeade.","open","base","base","R")
    call ton_main("I'll be staying there, so no need to worry about accommodation.","base","base","base","mid")
    m "Great..."
    call ton_main("I shall start right away!","base","happyCl","base","mid")
    call ton_main("Good day, Sir.","base","base","base","mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    m "This can't be good..."

    $ snape_busy = True

    $ tonks_intro.E1_complete = True
    # Don't add event pause here!

    jump main_room


label tonks_intro_E2:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    ton "Professor, it's Tonks."
    ton "May I come in?"
    m "(Her again...)"

    menu:
        m "(...)"
        "\"Come in...\"":
            pass

        "\"Not now, I'm busy!\"":
            call bld
            m "That will have to wait, I'm afraid..."
            ton "But Sir, I need to update you on the investigation!"
            ton "Please, hear me out, Professor!"
            ton "The students have been reluctant to even speak about the \"favour trading\" in my presence, which raises red flags." #idk I like this phrase more but that's subjective
            ton "You'd think that if those girls were innocent, they'd be telling me about it."
            m "....................."
            ton "Be that as it may, I will keep pushing them till they open up to me..."
            m "Good for you..."
            ton "And they will, as soon as I can get my hands on some Veritaserum!"
            ton "But Professor Snape has been very reluctant to provide me with a vial of his..."
            ton "{size=-4}Very suspicious if you ask me... Very suspicious indeed...{/size}"
            ton "Either way, it's only a matter of time until this will all be cleared up!"
            m "Great! I can't wait to hear about it..."
            ton "Of course, Sir."
            ton "I'll gladly spare some of my time and tell you right now, if you don't mind."
            m "Wait, what?"
            ton "I'm coming in..."
            g4 "(Shit!)"

    call ton_walk(action="enter", xpos="mid", ypos="base")

    call play_music("tonks")
    call ton_main("Professor.", "soft", "base", "base", "mid", xpos="right", ypos="base", trans=dissolve)
    m "Hey! If it isn't..."

    menu:
        m "(What was her name again?...)"
        "\"Tonks!\"":
            pass
        "\"Nymphadora!\"":
            call ton_main("Sir?", "annoyed", "base", "base", "R")
            m "What? Isn't that your name, or did I get it wrong again?"
            call ton_main("I'm sorry, Sir.{w=0.3} I thought that, when I was a student here, I made it very clear that I wouldn't want to be called Nymphadora--", "normal", "closed", "annoyed", "down")
            call ton_main("Please, just call me Tonks, Professor.", "annoyed", "wide", "base", "mid")
            m "Fine..."
        "\"Nympho-whora!\"":
            call ton_main("What?!", "clench", "wide", "shocked", "stare")
            call ton_main("I'm sorry, Professor. I clearly must have misheard you...", "disgust", "narrow", "annoyed", "down")
            call ton_main("What did you just call me?", "mad", "base", "angry", "mid")
            m "*Uhm*...{w=0.5} isn't that your name?"
            call ton_main("My name is \"Tonks\", Professor!","upset","base","angry","mid")
            call ton_main("You of all people should know this...", "annoyed", "base", "angry", "R")
            m ".............."
            m "(Tonks...)"
            m "(Still a weird fucking name...)"

    menu:
        m "..."
        "\"Found any evidence yet?\"":
            call ton_main("Sadly no, Professor.","open","base","base","mid")
            m "(Sadly...?)"
        "\"How's the investigation going?\"":
            pass
    call ton_main("I haven't gotten a chance to do my job properly so far.", "upset", "base", "base", "R")
    call ton_main("I've been rather preoccupied listening to Miss Granger's own {i}investigations{/i}...", "open", "narrow", "base", "R")
    call ton_main("That girl sure is something, isn't she?", "open", "base", "raised", "mid")
    call ton_main("Not that I mind listening to her.", "soft", "base", "shocked", "R", hair="horny")
    call ton_main("She gave me a very long report that went well into the evening, whilst I enjoyed a glass of firewhisky...","open","base","base","mid")
    call ton_main("She has been very thorough in documenting all the happenings she's witnessed...","base","base","base","mid")
    m "I can imagine that..."
    call ton_main("Anyhow... She had no proof of any illicit activities.{w} It's all just hearsay.", "open", "closed", "base", "R")
    call ton_main("As much as I wish it were true...", "horny", "closed", "base", "R", hair="horny")
    m "*huh*?"
    call ton_main("So I could conclude this whole business sooner, of course...", "base", "narrow", "base", "downR")
    call ton_main("And bring this favour trading business to an end, once and for all.", "open", "base", "base", "mid")
    m "Best of luck with that..."
    call ton_main("Thank you, Professor.", "base", "wide", "shocked", "mid")
    call ton_main("I really should get going.{w} Lots that needs to be taken care of.","open","base","base","R")
    m "Don't overwork yourself..."
    call ton_main("I won't Professor.{w} Have a good night.", "base", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    m "Shit..."
    m "I better talk to Snape about this..."

    $ tonks_intro.E2_complete = True
    $ nt_event_pause += 1

    jump main_room


### Snape Hangout Event 1 ###
# You discuss Tonks and the Ministry with Snape.

label ss_he_tonks_E1:
    call sna_main(".........................","snape_31", ypos="head")
    call sna_main("That bloody wench has outdone herself, once again!","snape_35")
    m "Granger?"
    call sna_main("Yes! She and her cursed letters!","snape_08")
    call sna_main("I'm certain she was the one who informed the Ministry about our little escapades...","snape_16")
    call sna_main("And now we have an Auror breathing down our necks... All thanks to that mischievous little whore!","snape_15")
    m "................."
    call sna_main("....................","snape_31")
    m "On the subject of that Auror..."
    call sna_main("Nymphadora?","snape_39")
    m "Yes, the Nympho."
    m "She came by the other day..."
    call sna_main("What?!","snape_36")
    m "Twice, actually..."
    call sna_main("And you're telling me about this... now?","snape_32")
    call sna_main("I'm surprised you didn't blow our cover right there and then...","snape_16")
    g9 "What can I say. I'm very good with the ladies!"
    call sna_main("Or you are just too lucky for your own good, more likely...","snape_43")
    m "That too, to a lesser extent..."

    if jerked_off_during_hermione_intro:

        call sna_main("Please tell me you didn't jerk off in front of her as well...","snape_03")
        m "Well..."
        call sna_main("Did you?","snape_01")

        if jerked_off_during_tonks_intro:
            m "No..."
            call sna_main("*glares*","snape_04")
            m "Yes...? But I didn't finish this time..."
            call sna_main("What you mean by \"I didn't fin--","snape_08")
        else:
            m "Not this time."

    call sna_main("Listen, we have to be even more cautious, now that there's an Auror making her rounds...","snape_10")
    call sna_main("They are the ministry's private investigators.","snape_35")
    call sna_main("One slip-up and they will have us locked up in no time!","snape_24")
    m "\"Us?\"..."
    m "What wrong did I do?"
    call sna_main("You snapped the most talented, clever, and most beloved wizard that's ever lived out of existence!","snape_10")
    m "Oh right...{w=0.3} Who was it again?"
    call sna_main("Albus{w=0.2} Percival{w=0.2} Wulfric{w=0.2} Brian{w=0.2} Dumbledore!","snape_34")
    m "..........................."
    m "I thought I traded places with just one person..."
    call sna_main("That {b}is{/b} one person!","snape_30", trans=hpunch)
    call sna_main("It's our headmaster's full name. And it's your name now!{w} You best make sure to remember it.","snape_34")
    m "Yeah...{w=0.5} I'm not even going to try..."
    call sna_main("Let's just hope this whole Ministry situation will solve itself...","snape_31")

    call sna_main("Thankfully, out of all the people the ministry could have sent...","snape_06")
    call sna_main("They brought that clumsy, good-for-nothing hufflepuff...","snape_35")
    call sna_main("As long as we keep our heads down and act as if we've nothing to hide...","snape_03")
    call sna_main("There will be nothing to worry about.","snape_09")
    m "I have my doubts about that."
    call sna_main("Let her continue her little investigation. And you can be as unhelpfully helpful as usual...","snape_04")

    menu:
        m "................."
        "{size=-2}\"That's a bit uncalled for, don't you think?\"{/size}":
            call sna_main("Maybe you're right.","snape_06")
            call sna_main("My apologies.","snape_09")
            m "Apologies accepted."

        "-Let it slide-":
            pass

    m "So..."
    m "What if she's not going to leave that easily?"
    m "Can you think of any spell, or potion to help us with that?"
    call sna_main("And what would this potion or spell achieve exactly?","snape_05")
    m "I don't know... Send her to the shadow realm or something?"
    call sna_main("What on earth...","snape_03")
    call sna_main("Actually, I'd rather not know...","snape_06")
    call sna_main("No, and even if there was one... we're still dealing with a trained Auror here.","snape_01")
    call sna_main("We should keep everything running as normal.","snape_35")
    call sna_main("Or as normal as can be, without the real Albus...","snape_09")
    m ".................."
    call sna_main("Even if she finds any concrete proof of something going on, any involvement on our part should be kept quiet at all cost.","snape_01")
    call sna_main("And as soon as she is out of here, I'll go back to drinking wine, whilst enjoying my students' company...","snape_40")
    m "And Granger? What do you suggest we do with her?"
    call sna_main("*Tzzzgh*-{w=0.6} Like that annoying brat can do any harm to us...","snape_25")
    call sna_main("A girl her age would do anything for attention, is what I'd say...","snape_09")
    call sna_main("Do you think some student's word would be as good as the headmaster's?","snape_02")
    call sna_main("The Headmaster of the most respected educational institution in the country, no less...","snape_37")
    g4 "I'm the headmaster of the most respected institution in the country!?!"
    call sna_main("It is also the only magical institution...","snape_09")
    m "...................................."

    "You spend the remaining day with Snape, drenching your worries in plenty of wine..."

    #m "So, what are your thoughts on this whole ministry situation?"
    #sna "I can't say I have a very high opinion on how those fools run the place."
    #sna "The Department of Magical Law Enforcement are a joke."
    #sna "The only decent auror they have is Alistair Moody and he's more concerned dealing with dark magic than petty rumours to get involved with this investigation."
    #sna "The minister for magic himself is a fool."
    #sna "He might bring a good smile and spirits to the people during times of rebuilding after great loss."
    #sna "But when it comes to making any worthwhile decisions or recognizing potential threats or misconduct..."
    #m "I was talking mostly about our current predicament rather thant he ministry at large..."
    #sna "I know..."
    #m "..."
    #m "Surely you must be slightly worried."
    #sna "I have committed many crimes much worse than chatting up some students, all of which I should've been incarcerated for."
    #sna "As I said, the current ministry is a shamble of what it once was... no change will come from this."
    #sna "Cornelius fudge is more interested in how the ministry looks from the outside rather than expose existing issues and dealing with them."
    #m "Such as?"
    #sna "Well, apart from leaving Hogwarts completely in the hands of the headmaster..."
    #sna "Corruption, illegal trades of magical artefacts and creatures. The list goes on..."
    #sna "The only one showing any interest in the schools business is the Head of the Department of Magical law Enforcement herself."
    #m "And that's not a problem because?"
    #sna "Because in the end you'd see a dementor getting frisky with a human before any of these things aren't getting swept under the carpet."
    #sna "You could put the tooth fairy in front of the minister and he'd still deny her existence if he were to have held that stance."
    #sna "And the other fools at the ministry would do so as well even if they witnessed it themselves."

    $ ss_he.tonks_E1 = True
    $ ss_event_pause += 1

    jump day_start


label tonks_intro_E3:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"

    call play_sound("knocking")
    "*Knock-knock-knock*"

    m "............"

    ton "Professor Dumbledore, may I come in?"
    m "(It's that hot Ministry chick again...)"

    menu:
        "\"Yes, please come on in.\"":
            pass
        "\"Not right now.\"":
            ton "But it's urgent, Sir. I need to talk to you about Miss Granger's favour trading accusations..."
            g4 "(Shit. That can't be good.)"
            m "Do you mind coming another time, I'm very busy...{w} watering the bird."
            ton "Watering what?"
            ton "Sir, I'm coming in."
        "\"Who is it?\"":
            ton "It's Tonks."
            m "Who?"
            ton "..."
            ton "Nymphadora Tonks..."
            m "(That {i}Nympho{/i} again...)"
            ton "Sir, I'm coming in."

    #Tonks enters the office
    call ton_walk(action="enter", xpos="desk", ypos="base")

    call play_music("tonks")
    call ton_main("Professor...", "soft", "base", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    m "How's the investigation going? Nothing to report I gather?"
    call ton_main("On the contrary...", "open", "wide", "shocked", "stare")
    call ton_main("It's worse than I could have ever imagined!", "open", "wide", "angry", "mid", hair="angry")
    g4 "(........)"
    call ton_main("This school truly has changed since I was a student here.", "mad", "base", "base", "mid")
    call ton_main("I never thought I would see Hogwarts in a state such as this...", "open", "base", "annoyed", "down")
    call ton_main("Corrupted! Right down to the core!", "mad", "base", "angry", "mid", hair="angry")
    g4 "(What's the matter with her hair?!)"
    call ton_main("You don't have to search for too long to uncover the vile debaucheries that are happening at this school...", "open", "base", "annoyed", "mid", hair="angry")
    g4 "(Snape you fucking idiot! You blew it!!!)"
    call ton_main("Teachers taking advantage of their students, promising house points in return for sexual acts...","open","base","angry","R", hair="angry") #in a sexual favour, the sex act is the favour
    call ton_main("While they abuse their authority and power to do the most despicable things to them...", "open", "base", "annoyed", "R", hair="horny")
    call ton_main("But the Dumbledore I know would never allow such disgracefulness at his school...", "mad", "base", "angry", "mid", hair="angry")
    m "(...)"

    stop music fadeout 1.0
    call ton_main("I had this suspicion... Since the very day I got here...", "open", "wide", "angry", "mid", hair="angry")
    # Tonks threatens Genie.
    # Maybe have her chibi point her wand at him?
    call play_music("hitman")
    call ton_main("Now tell me, who are you?{w} And you better tell the truth!", "mad", "base", "angry", "mid", hair="angry")
    g4 "(Shit, how often is this going to happen to me?)"

    menu:
        g4 "I am..."
        "\"Albus Dumbledore!\"":
            call ton_main("You are most certainly {b}not{/b} Albus Dumbledore!","upset","base","angry","mid")
            g4 "No wait, it was {i}Albertus Dumblerdore{/i}! That's it!"
            m "(Yes, that was probably it...)"
        "\"You know who!\"":
            call ton_main("What?", "open", "wide", "angry", "mid")
            m "You...{w=0.8} know...{w=0.8} who..."
            call ton_main("That can't be true!", "open", "base", "annoyed", "mid")
            m "You know who I am. You said it yourself earlier."
            m "(If only I could remember what she called me...)"
        #"The danger!":
        #    call ton_main("What?", "base", "wide", "shocked", "stare")
        #    g4 "I am the one who knocks..."

    call ton_main("I've had enough of this!", "mad", "base", "angry", "mid")
    call ton_main("Reveal your true identity, dark wizard!","open","base","angry","mid")
    g4 "I'm not a dark wizard, you racist twat!"
    call ton_main("How dare you call me a racist!", "mad", "shocked", "angry", "mid", hair="angry")
    g4 "Bring it! Do your worst, witch!"
    call hide_characters
    hide screen bld1
    with d3

    # Glass break animation.
    # Duel won't happen and Tonks just casts a spell.

    play music "music/boss_battle_#2_metal_loop.mp3" fadein 1 fadeout 1
    call play_sound("glass_break")
    pause.1

    show screen snape_glass
    pause 2.3

    hide screen snape_glass
    with irisout
    pause.1

    call gen_chibi("hide")
    show screen dumbledore
    call cast_spell("revelio")
    call ton_main("Revelio!", "open_wide", "shocked", "annoyed", "mid", hair="angry", ypos="head")
    call bld("hide")
    pause.6

    call gen_chibi("sit_behind_desk")
    hide screen dumbledore
    with d9
    pause.6

    call ton_main("", "disgust", "shocked", "shocked", "stare", xpos="right", ypos="base")
    m "(...)"
    $ renpy.music.play("music/Under-the-Radar by PhobyAk.mp3")
    call ton_main("No way!", "soft", "shocked", "base", "mid")
    m "What just happened?"
    call ton_main("What... are you...?", "mad", "shocked", "raised", "mid")
    m "(Can she see through the illusion?)"
    call ton_main("Wait a minute... Are you...{w=0.5} {size=+4}a Genie?{/size}", "open", "shocked", "raised", "mid")
    g4 "(This witch knows her shit!)"
    m "..."

    g9 "Some people would say I'm {b}the{/b} Genie, actually!"
    m "The most powerful being in the entire universe... Multiple universes even..."
    m "Glad my reputation precedes me..."
    call ton_main("How curious. I've never had a Genie before...", "horny", "wide", "base", "down", hair="horny") # Tonks looks horny.
    m "I'm sorry-- what?"
    call ton_main("I meant, I've never had the pleasure of meeting a Genie before. This is brilliant!", "grin", "shocked", "shocked", "mid")
    m "(Is she hitting on me?!)"
    m "I'm flattered... But how were you able to tell?"
    call ton_main("I'm an Auror. It's my job to identify and catch magical beings...", "soft", "wide", "shocked", "mid")
    call ton_main("But, if you are here, what happened to Professor Dumbledore?{w} Did he use one of your wishes and wish himself away?", "mad", "wide", "shocked", "R")
    m "No... I don't do that anymore."
    m "I'm what you would call a \"free\" Genie..."
    call ton_main("So? What happened to him?","upset","base","raised","mid")
    m "I believe we traded places when one of my magical inventions went wrong..."
    call ton_main("Really?! Is he okay?", "mad", "wide", "base", "mid")
    m "I think so.{w} He travelled to my universe, and I'm stuck in this dull place..."
    m "Believe me, there are a lot more brothels in Agrabah.{w} I bet he's having the time of his life..."
    call ton_main("So, you just {i}*poofed*{/i} in here and decided to turn this school into your own private brothel...", "open", "narrow", "angry", "mid")
    call ton_main("Because you were bored?!","upset","base","angry","mid")
    m "Hey! I'm an immortal being... boredom is my worst enemy."
    m "And I didn't do much, just a nudge in the right direction..."
    call ton_main("You need to bring him back, the real Dumbledore, immediately!", "mad", "base", "angry", "mid", hair="angry")
    m "I don't know how, ... yet.{w} We're still working on it..."
    call ton_main("We? Who else knows about this?", "open", "narrow", "annoyed", "mid")

    menu:
        m "(Crap...)"
        "\"You know who...\"":
            call ton_main("{size=+4}What?!{/size}", "open", "wide", "worried", "mid", hair="scared")
            m "(Why do they keep freaking out whenever I say this...)"
            m "That Snape guy."

        "\"Nobody...":
            call ton_main("You mean Professor Snape is in on this?!", "open", "wide", "shocked", "mid")
            m "What? But I didn't--"

    call ton_main("But of course!{w} After all he was mentioned in Miss Granger's letter as one of the main offenders.", "disgust", "wide", "shocked", "stare")
    call ton_main("That sleazy, vile snake...{w} Naturally he'd be all over an opportunity such as this.", "mad", "base", "angry", "R", hair="angry")
    m "(Snake? Have I been saying his name wrong this entire time?...)"
    m "(I hate when that happens...)"
    call ton_main("And to think I believed that creep when I questioned him about it.", "mad", "closed", "angry", "mid")
    m "(...)"
    call ton_main("He's a very skilled liar, I'll give him that.", "upset", "narrow", "angry", "down")
    m "Are you going to lock us up now?"
    call ton_main("I very well should! It would be the moral thing to do.","open","base","angry","mid")
    m "(Shit...)"
    call ton_main("You and Professor Snape should be locked in Azkaban for what you've done...", "mad", "base", "angry", "mid")
    call ton_main("And stay there for the rest of your lives...","open","base","angry","mid")
    g4 "You can't do that to me, I'm immortal! I'd go insane!"
    call ton_main("You should have thought about that before deciding to fuck your own students!", "mad", "base", "angry", "mid")
    g4 "But I haven't even gotten to that part yet!"
    call ton_main("And you never will!", "open", "wide", "angry", "mid")
    call ton_main("I'm going to put you in the smallest cell Azkaban has to offer...","open","base","angry","mid")
    g4 "No, please! I hate confined spaces!"
    # fake game over
    $ renpy.music.stop(fadeout=4)
    $ renpy.music.stop(channel="weather", fadeout=4)
    $ renpy.play('sounds/level_failed.mp3')
    show screen cartoon_zoom
    g4 "...{w=6.0}{nw}"
    call gameover()
    # back from game over

    call weather_sound
    stop music fadeout 1.5

    $ renpy.play('sounds/scratch.wav')
    call ton_main("Unless...", "upset", "narrow", "annoyed", "downR", trans=hpunch)

    g4 "Unless?"
    call play_music("tonks")
    call ton_main("You let me join in on the fun!", "grin", "base", "raised", "mid", hair="horny")
    m "..."
    g4 "What?" #screenshake
    call ton_main("The ministry sent me to investigate what they assumed to be a silly rumour a student made up...", "base", "base", "angry", "R")
    call ton_main("And whilst I could just squash the rumour and go back to a dull, quiet desk job.", "disgust", "base", "raised", "mid") #rule of 3
    call ton_main("I simply couldn't pass up an opportunity like this...", "horny", "narrow", "base", "mid", hair="horny") #now that she's not being official and talking ministry business, she should slip back into more casual language
    call ton_main("Keeping quiet would be far more... \"exciting\".", "soft", "base", "base", "stare", hair="horny")
    m "How so?"
    call ton_main("I know for a fact that the Ministry has been trying to plant an inside man here at Hogwarts.", "normal", "base", "base", "R")
    m "Then what are you suggesting?"
    call ton_main("Hire me as a teacher.","base","base","base","mid")
    call ton_main("I could teach the students a thing or two about the \"Defence against the Dark Arts\"...","open","base","base","mid")
    m "(...)"
    call ton_main("And if you and Snape want this favour trading to continue, you'll need somebody who can keep things quiet with the ministry.", "base", "closed", "base", "mid")
    m "Do I even have a choice?"
    call ton_main("The alternative would be me informing the ministry, and locking you both up.", "soft", "base", "base", "mid") #formal language here for the 'official procedure'
    g9 "Then welcome aboard!"
    call ton_main("Don't worry. I'm not here to spoil your little act.", "base", "base", "raised", "mid")
    m "That's a relief..."
    call ton_main("I'll inform the other teachers about my stay.","open","base","base","R")
    call ton_main("And the Ministry too of course. I'll be their inside man at Hogwarts, here at the request of Professor Dumbledore himself, no less.","base","base","base","mid")
    call ton_main("If only they knew...", "horny", "narrow", "base", "mid", hair="horny")
    call ton_main("In any case, Profess--","open","base","base","R")
    call ton_main("I'm sorry, what would you like me to call you?", "mad", "base", "raised", "mid")

    menu:
        m "You can call me..."
        "\"Professor is fine.\"":
            $ ton_genie_name = "Professor"
            call ton_main("Very well.","base","base","base","mid")
        "\"You can call me Genie.\"":
            $ ton_genie_name = "Genie"
            call ton_main("Very well, Genie.","base","base","base","mid")
        "\"Call me Daddy...\"":
            $ ton_genie_name = "Daddy"
            call ton_main("What? Are you serious?!", "open", "wide", "shocked", "stare")
            call ton_main("*Ha-Ha-Ha!*...{w=0.3} you're too funny!", "silly", "happyCl", "raised", "mid", hair="happy")
            g4 "(What?-- Now it's yellow!)"
            call ton_main("Are all Genies this desperate?", "crooked_smile", "base", "raised", "mid", hair="happy")
            m "Desperate? Why Desperate? ..."
            call ton_main("Nothing...", "base", "base", "base", "down", hair="happy")
            call ton_main("Very well... \"Daddy\"! {heart}{heart}{heart}", "horny", "narrow", "base", "mid", hair="horny")
            g9 "*He*-*He*-*He*-He*..."

    call ton_main("Call me to your office whenever you require my help, [ton_genie_name].","base","base","base","mid") #would it be better to have her call him by the requested name here, since later on we have the bit where Tonks submits to genie and calls him sir
    m "I most certainly will..."

    #Tonks leaves
    call ton_walk(action="leave")

    call bld
    m "What an interesting turn of events..."
    g9 "Who would've guessed that she's such a pervert?!"

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton", True)
    call popup("{size=-4}You can now summon Tonks into your office.{/size}", "Character unlocked!", "interface/icons/head/tonks.webp")

    $ tonks_busy = True

    $ tonks_intro.E3_complete = True
    $ nt_event_pause += 1

    jump main_room


### Snape Hangout Event 2 ###
# You inform Snape that Tonks is now an ally and has been made a teacher.

label ss_he_tonks_E2:
    call sna_main(".........................","snape_31", ypos="head")
    call sna_main("So, here is the plan...","snape_03")
    call sna_main("You get a shovel and a body-bag ready, and I'll do the \"Avada Kedavra\"!","snape_01")
    m "\"Avra-ka--\"{w} What the fuck are you talking about?"
    call sna_main("Tonks! We need to get rid of her! Immediately!","snape_10")
    call sna_main("Otherwise things will never go back to how they were!","snape_03")
    m "Have you lost your mind again?"
    call sna_main("No, but I'm about to!","snape_01")
    #call sna_main("I haven't had a mouth on my cock in so long...","snape_29")
    #call sna_main("Please, Genie. I need a fix!","snape_19") # Weird look
    #m "..................."
    #call sna_main("...................","snape_19") # Weird look
    #g4 "Would you stop looking at me like that!!!"
    #call sna_main("What? Don't be ridiculous...","snape_14")
    m "..................."
    call sna_main("What a fool I was to believe that she'd be gone by now...","snape_31")
    call sna_main("But of course not! ","snape_32")
    call sna_main("{size=+5}Instead they made that mischievous {b}cunt{/b} a teacher!{/size}","snape_33", trans=hpunch) # Screaming
    m "Actually, that was--"
    call sna_main("The whole universe has turned against me!","snape_43")
    call sna_main("That bloody Ministry! Curse them!","snape_35")
    call sna_main("Of course it was only a matter of time until they got themselves involved...","snape_06")
    call sna_main("We had something good, Genie. And now it's over...","snape_26")

    m "Well, lucky for us, it isn't over just yet..."
    call sna_main("What's that supposed to mean? Are you concocting something?!","snape_25")
    m "It's like you've said..."
    g9 "The situation solved itself!"
    m "She's going to join us."

    call sna_main("Join us? Doing what?","snape_05")
    g9 "Corrupting those precious students of ours, of course!"
    call sna_main("And according to you, Tonks wants to help us break that Gryffindor bitch as well?","snape_34")
    m "Yep."
    call sna_main("*Ha-ha-ha*!{w} That's just fucking silly!","snape_28")
    m "................"
    call sna_main("Good one...","snape_45")
    call sna_main("No seriously. What's going on?","snape_03")
    m "She asked me if she could join us..."
    call sna_main("*A-ha-ha-ha-ha*...","snape_28")
    m "Who do you think made her a teacher in the first place?"
    call sna_main("Stop it, please!!!","snape_42")
    m "You don't believe me..."
    call sna_main("Not a single word! *A-Ha-ha-ha*...","snape_28")
    m "Fair enough..."
    call sna_main("*Ha-ha-ha*--","snape_42")
    call sna_main("*cough* {w=0.4}*cough* {w=0.4}*cough*...","snape_17", trans=hpunch)
    m "..............."
    call sna_main("...................","snape_31")

    call sna_main("But none of this makes any sense!","snape_03")
    m "Well, as it turns out..."
    call sna_main("She's a pervert!","snape_36") # Revelation
    m "She's a-- wait, how did you know?"
    call sna_main("How could I've been so ignorant!","snape_08")
    m "Am I missing something here, you're not a mind reader, are you?"
    call sna_main("I'm a very skilled Occlumens, but no...","snape_31")
    m "(Occlu-what?)"
    m "Could you stop making up words..."
    call sna_main("It's quite obvious in hindsight...","snape_35")
    m "It...{w=0.4} is?"
    call sna_main("Why would the Ministry have sent a full-fledged Auror, to deal with some eccentric insinuations made by some petty student...","snape_16")
    m "Shouldn't they?"
    call sna_main("Just because of some silly rumour about teachers having sexual intercourse with their students?","snape_34")
    m "And that's not a reasonable enough concern to send somebody to look into?"
    call sna_main("It's the Ministry we're talking about...{w=0.8} They don't give a shit...","snape_30")
    call sna_main("They wouldn't even believe it if \"you-know-who\" were to make a return...","snape_31")
    m "Who?"
    call sna_main("That Tonks had to be the only Ministry personnel that saw some truth in Granger's letters...","snape_35")
    call sna_main("What if she specifically requested to be sent here to investigate?","snape_03")
    m "She might have..."
    call sna_main("So...{w=0.4} what does she want?","snape_04")
    call sna_main("Surely she's taking the position for a reason...","snape_01")
    m "It appears that she'd like to be part of this whole favour trading business, which is also why she asked to be made a teacher..."
    m "And in return she'll keep things quiet with the ministry."

    call sna_main("*Hmm*... Not having to worry about the Ministry anymore, you say...","snape_38")
    call sna_main("And I'm supposed to believe that she'd be willing to do that for us?","snape_25")
    call sna_main("How exactly did you end up in this situation with her?","snape_04")
    m "I don't know... It just... happened."
    m "She pretty much figured everything out by herself."
    m "Straight away even guessed that I'm a Genie..."
    call sna_main("So she knows everything? How did she--","snape_03")
    m "It appears the \"illusion charm\" wasn't perfect. She momentarily got a glimpse through it..."
    call sna_main("That's impressive... perhaps I didn't give her enough credit...","snape_01")

    call sna_main("If what you're telling me about her intentions are true...","snape_03")
    call sna_main("Maybe she could even be persuaded to help with the Granger situation...","snape_05")

    if nt_he.hermione_E1:
        g9 "Way ahead of you!"
        m "She's already offered to help with Granger."
    else:
        m "Oh, I'm sure there's little to no persuasion needed."
        m "I have no doubt that she'd be well into the idea of convincing Granger to sell favours herself..."

    call sna_main("What a wicked bitch!","snape_13")
    call sna_main("If only we were selling favours back then...","snape_46")
    call sna_main("You know what they say about students from Hufflepuff...","snape_20")
    call sna_main("They are quite the \"hard-working\" bunch!","snape_21")
    m "(...)"
    m "I'm calling dibs on her!"
    call sna_main("You do what?","snape_14")
    m "Dibs, she's mine. I said it first..."
    call sna_main("Are you twelve or something?","snape_04")
    m "Over twelve thousand, actually."

    pause.1
    call blktone

    ">You and professor Snape keep discussing various staff members of Hogwarts."
    ">The bond between you two grows stronger."

    call sly_plus
    call hide_blktone

    $ ss_he.tonks_E2 = True
    $ ss_event_pause += 1

    jump end_snape_hangout_points


### Snape Hangout Event 3 ###
# You tell Snape that you made Tonks the teacher for 'DAtDA'

label ss_he_tonks_E3:
    call bld
    m "Our new partner in crime, is she getting on well?"
    call sna_main("Tonks? I haven't seen her since last time we talked...","snape_09", ypos="head")
    call sna_main("Shouldn't you know what that witch is up to? You made her a teacher, after all...","snape_01")
    m "I'm sure she's still just settling down..."
    call sna_main("Probably drinking booze down at Hogsmeade, more likely...","snape_35")
    call sna_main("What subject is she even supposed to teach? What did you give her?","snape_03")
    m "I have not the slightest clue..."
    call sna_main("................","snape_38")
    call sna_main("You know, I've been teaching \"Potions\" at this school for as long as I can remember...","snape_06")
    call sna_main("Of course I'm the best they have.{w=0.8} And they don't call me \"Master of Potions\" for nothing!","snape_17")
    call sna_main("But if we're honest, even a \"dim-witted Demiguise\" could teach potions to those simpletons...","snape_35")

    menu:
        m "..............."
        "\"Are the students really that bad?\"":
            call sna_main("*sigh* You have no idea, even an ape would show more learning abilities.","snape_06")
            m "*Hmm*..."
        "\"... Demiguise?\"":
            m "What the fuck is that?"
            call sna_main("*sigh* I keep forgetting you're not from around here...","snape_06")
            call sna_main("It's a magical beast that can make itself invisible and has precognitive sight.","snape_24")
            m "... Sounds boring, forget I asked."
            call sna_main("...........","snape_05")
            call sna_main("Anyway, back to the topic at hand--","snape_04")

    call sna_main("When it comes to \"Defence against the dark arts\"...","snape_03")
    call sna_main("That's a subject that requires skill and cunning!","snape_02")
    call sna_main("And a very competent and skilled teacher, to guide those hopeless souls through their lessons...","snape_40")
    call sna_main("Now, If you were to assign me for that, and give Tonks my old subject to teach...","snape_20")
    m "Yeah, about that...{w=0.4} I think I might have given that role to her..."
    call sna_main("{size=+5}You did what?!{/size}","snape_33", trans=hpunch)
    m "\"Defence against... something-something\"..."
    call sna_main("You should have given me the \"defence against the dark arts\" position!","snape_34")
    call sna_main("And she could've had something else... like \"muggle studies\", or something.","snape_16")
    m "First come, first served, I suppose..."
    m "And I am not making her teach any \"smuggle studies\", who do you take me for?"
    call sna_main("Curse you...","snape_08")
    m "There wasn't really any room for me to argue with her..."
    m "It was either that, or prison."
    call sna_main("..................","snape_31")

    call sna_main("I can't say that I trust her just yet...","snape_35")
    call sna_main("Not before I get to slip in a couple drops of \"Veritaserum\" into her drink...","snape_03")
    m "\"Veritaserum?\""
    call sna_main("Truth potion!{w=0.4} I oftentimes use some on my \"very attractive Slytherins\"...","snape_02")
    call sna_main("Only a single drop, and they'll tell me everything I want to know.","snape_41")
    call sna_main("Very handy should you need information to blackmail someone...","snape_46")
    call sna_main("Or learn everything about their secret fetishes...","snape_20")
    g9 "Neat!"

    pause.1
    call blktone

    "You take some time to muse about the fetishes Tonks might have..."
    "For blackmailing... or to have some fun..."

    $ ss_he.tonks_E3 = True
    $ ss_event_pause += 1

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points
