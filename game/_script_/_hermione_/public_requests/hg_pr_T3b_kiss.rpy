
### Make Out With A Girl ###

label hg_pr_kiss:

    # Setup
    $ current_payout = 45

    if hg_pr_kiss.counter == 0:
        m "{size=-4}(Tell her to go make out with one of her female classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)

    #Intro.
    if hg_pr_kiss.counter == 0:
        m "Have You ever kissed another girl, [hermione_name]?"
        call her_main("?!", "normal", "squint", "angry", "mid")

        if her_reputation < 9:
            jump too_much_public

        call her_main("I am not a... lesbian, [genie_name].", "open", "base", "base", "mid")
        m "Silly girl... You don't need to be a lesbian to kiss girls."
        m "I mean, I do it and I am not a lesbian either."
        call her_main("...............", "angry", "base", "angry", "mid")
        her "[genie_name]--"
        m "No, \"[genie_name]s\"! This is your task for today!"
        m "Go find a cute little thing and plant a \"smooch\" on her!"
        call her_main("[genie_name], but I am--", "open", "base", "worried", "mid")
        m "Dismissed, [hermione_name]."
        call her_main("[genie_name]!......", "normal", "squint", "angry", "mid")
        m "I said you're dismissed."
        call her_main("*Humph*!...", "annoyed", "squint", "angry", "mid")
    else:
        if her_tier >= 5:
            m "[hermione_name], {number=current_payout} house points are up for grabs today!"
            m "Are you interested?"
            call her_main("Sure, why not?", "base", "base", "base", "mid")
            m "Great."
            m "I want you to make out with another girl today."
            call her_main("Alright.", "soft", "base", "base", "R")
            call her_main("I know a couple of girls who are hungry for attention and wouldn't mind putting on a little show.", "smile", "narrow", "base", "mid_soft")
            m "Great. See you after your classes then."
        elif her_tier >= 4:
            m "[hermione_name], {number=current_payout} house points are up for grabs today!"
            m "Are you interested?"
            call her_main("I suppose...", "annoyed", "narrow", "annoyed", "up")
            m "Great. All you need to do is make out with another girl."
            call her_main("I see...", "annoyed", "narrow", "worried", "down")
            m "Up for the task, [hermione_name]?"
            call her_main("I guess...", "annoyed", "base", "worried", "R")
            m "Great. See you after your classes then."
        else:
            m "[hermione_name], {number=current_payout} house points are up for grabs today!"
            m "Are you interested?"
            call her_main("It depends...", "normal", "base", "base", "mid")
            her "Will I have to do something depraved again?"
            m "\"Depraved\"??! When did I ever--?"
            call her_main("Really, [genie_name]?", "open", "closed", "angry", "mid")
            m "Fine, fine... But all I want you to do today is to make out with another girl."
            call her_main("Oh, is that all?", "angry", "base", "angry", "mid") # :(
            m "Yes... Pretty basic stuff for you, right?"
            m "And you will be getting {number=current_payout} house points afterwards of course."
            call her_main(".............", "normal", "squint", "angry", "mid")
            m "So... Are you up for it?"
            call her_main("I will see what I can do, [genie_name]...", "annoyed", "narrow", "angry", "R")
            m "Great. See you after your classes then."
            call her_main("................", "annoyed", "narrow", "annoyed", "mid")

    call her_walk(action="leave")

    $ hg_pr_kiss.inProgress = True

    jump end_hermione_event

label end_hg_pr_kiss:
    $ gryffindor += current_payout

    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."
    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_kiss.counter == 1:
        show screen blktone
        with d3

        call her_main("(*Tsk*)", "mad", "base", "angry", "R", ypos="head", flip=False, trans=d3)

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_kiss.inProgress = False

    # Increase Points

    if her_tier == 3:
        if her_reputation < 12:
            $ her_reputation += 1

        if her_whoring < 12:
            $ her_whoring += 1

    elif her_tier == 4:
        if her_reputation < 18:
            $ her_reputation += 1

        if her_whoring < 18:
            $ her_whoring += 1

    elif her_tier == 5:
        if her_reputation < 21:
            $ her_reputation += 1

        if her_whoring < 21:
            $ her_whoring += 1

    jump end_hermione_event

label hg_pr_kiss_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you succeed in completing your task?"
    her "Yes, [genie_name]..."

    if hg_pr_kiss.is_tier_complete():
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_kiss

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_kiss.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("Well... I...", "soft", "base", "base", "R")
        m "Don't be shy, [hermione_name]."

    m "Have you kissed someone?"

    return

### Tier 3 ###

label hg_pr_kiss_T3_E1:

    call hg_pr_kiss_intro

    call her_main("I...", "open", "base", "worried", "mid")
    m "I told you to make out with another girl..."
    m "Did you do it or not?"
    call her_main("I...", "open", "base", "worried", "R")
    her "I tried, [genie_name]. I really did."
    m "And?"
    call her_main("Well...", "annoyed", "base", "worried", "R")
    call play_music("hermione") # Music
    her "It was awkward and embarrassing..."
    m "did you do it or not?"
    call her_main("... no I did not, [genie_name]...", "annoyed", "narrow", "angry", "R")
    her "All I achieved was making a complete fool out of myself..."
    call her_main("In front of the entire class...", "angry", "base", "angry", "mid")
    m "Tell me what happened, [hermione_name]."
    call her_main("No, I will not, [genie_name].", "annoyed", "narrow", "angry", "R")
    her "Not in a million years!"
    call her_main("Why do I have to perform such ridiculous tasks anyway?!", "shock", "happyCl", "worried", "mid")
    her "What is the point of all this?"
    call her_main("I hate this!", "scream", "closed", "angry", "mid")
    call her_main("...............", "annoyed", "narrow", "angry", "R")
    her "................."
    m ".............."
    m "You are not getting paid, you know that, right?"
    call her_main("I don't care...", "scream", "closed", "angry", "mid")

    call her_walk(action="leave")

    $ her_mood += 12

    $ hg_pr_kiss.inProgress = False

    jump end_hermione_event

label hg_pr_kiss_T3_E2:

    call hg_pr_kiss_intro

    call play_music("hermione") # Music
    call her_main("I did, [genie_name]...", "open", "closed", "base", "mid")
    m "Good. Give me the details."
    call her_main("Well, I kissed a girl. Just like you told me to, [genie_name].", "annoyed", "squint", "base", "mid")
    m "I guess it was embarrassing for you, girl?"
    call her_main("Very much so, [genie_name].", "annoyed", "narrow", "angry", "R")
    m "Did you enjoy it though?"
    call her_main("*Humph*!...", "annoyed", "narrow", "annoyed", "mid")
    m "So you kissed a girl and you liked it?"
    call her_main("Yes...", "disgust", "narrow", "base", "mid_soft")
    m "Did your tongues touch?"
    call her_main("Yes...", "disgust", "narrow", "base", "mid_soft")
    her "It was a proper deep kiss, if that's what you want to know."
    her "Can I just get my payment now?"
    call her_main("Please, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "Well, alright..."

    jump end_hg_pr_kiss

label hg_pr_kiss_T3_E3:

    call hg_pr_kiss_intro

    call play_music("hermione") # Music
    call her_main("Yes, I did, [genie_name].", "open", "closed", "base", "mid")
    m "Good. Tell me how it went."
    call her_main("It went well, [genie_name].", "open", "closed", "base", "mid")
    m "Great. Give me the details."
    call her_main("What would you like to know, [genie_name]?", "open", "closed", "angry", "mid")
    m "Tell me everything! Was the girl pretty?"
    m "Did she return your kiss?"
    call her_main("She was relatively pretty, [genie_name].", "open", "squint", "base", "mid")
    her "And she did return my kiss..."
    call her_main("...........", "annoyed", "closed", "base", "mid")
    call her_main("Anything else, [genie_name]?", "open", "squint", "base", "mid")
    m "...."
    m "Why are you being difficult, [hermione_name]?"
    call her_main("With all due respect, [genie_name]...", "open", "closed", "angry", "mid")
    her "You told me to make out with another girl, and I did..."
    call her_main("Now, I would like to get paid if you would be so kind.", "normal", "base", "base", "mid")
    m "......................"

    menu:
        "\"Fine. Here is your payment, girl.\"":
            jump end_hg_pr_kiss

        "\"I don't appreciate your attitude, [hermione_name].\"":
            call her_main("Well, that is unfortunate, [genie_name].", "open", "closed", "angry", "mid")
            m "Sure is..."
            m "Because you are not getting paid you insolent, little witch."

            stop music fadeout 1.0

            call her_main("What?", "normal", "base", "base", "mid")
            call her_main("[genie_name], you can't do that!", "open", "base", "worried", "mid")
            m "Dismissed."
            call her_main("B-but--", "open", "base", "worried", "R")
            call her_main("[genie_name], please!", "open", "base", "worried", "mid")
            her "The girl was from Hufflepuff and--"
            m "Too late for that, [hermione_name]."
            m "You are dismissed."
            call her_main("......", "angry", "base", "base", "mid", tears="soft")
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            $ her_mood +=25
            $ hg_pr_kiss.inProgress = False

            pause 1.0
            m "*Tsk*"

            jump end_hermione_event

### Tier 4 ###

label hg_pr_kiss_T4_E1:

    call hg_pr_kiss_intro

    call her_main("I did, [genie_name]...", "open", "closed", "base", "mid")
    m "Well, don't just stand there. Give me the details."
    call her_main("*Ehm*, alright...", "open", "base", "base", "mid")
    her "The girl was from Ravenclaw..."
    call her_main("I think she may have been an underclassman, but I did not ask...", "soft", "base", "base", "R")
    her "We got to talking about boys..."
    call her_main("And she told me that she never kissed one...", "open", "closed", "base", "mid")
    her "And that she is worried that she might be very bad at it..."
    call her_main("So I just offered my help...", "base", "base", "base", "mid")
    call play_music("playful_tension") # Music
    her "And then we spent some time in one of the bathroom stalls..."
    call her_main("Making out...", "base", "base", "base", "mid")
    call her_main("She caught on real quick... I think she could be really good at it with some practice...", "open", "base", "base", "mid")
    call her_main("Also she was quite adorable...", "base", "base", "base", "mid")
    call her_main("She kept calling me \"Miss Hermione\"...", "smile", "base", "base", "R")
    m "*Hmm*..."
    m "I Don't recall sending you out with a task to confuse some poor girl, [hermione_name]."
    call her_main("\"Confuse\"? [genie_name], please...", "smile", "narrow", "base", "mid_soft")
    her "You should have seen that {i}poor girl{/i}..."
    call her_main("I assure you that she was anything but confused.", "smile", "base", "angry", "mid")
    her "In fact, at the end of our \"Study session\" she got rather obnoxious..."
    call her_main("And it sort of felt as if she was taking advantage of me...", "open", "base", "base", "mid")
    m "Oh... Well, in that case..."
    call her_main("", "base", "base", "base", "mid")

    jump end_hg_pr_kiss

label hg_pr_kiss_T4_E2:

    call hg_pr_kiss_intro

    call play_music("hermione") # Music
    call her_main("I did, [genie_name].", "open", "closed", "base", "mid")
    m "Tell me how it went."
    call her_main("Well... *Ehm*...", "open", "base", "base", "mid")
    her "There is this one girl who is into girls..."
    her "I thought she would be the ideal candidate for my task..."
    her "so I told her that I am curious and that I would like to kiss her..."
    call her_main("She said that we should go to the girls' restroom for that...", "open", "narrow", "worried", "down")
    her "But I just kissed her right there in the corridor..."
    call her_main("And she kissed me back but...", "open", "base", "base", "mid")
    call her_main("It got weird really fast...", "angry", "narrow", "base", "down")
    her "The way she kissed me..."
    call her_main("She did it like a boy would, [genie_name]...", "angry", "base", "base", "mid")
    call her_main("Aggressive but confident...", "angry", "narrow", "base", "down")
    call her_main("Naturally a small group of spectators gathered up around us right away...", "upset", "closed", "base", "mid")
    call her_main("Mostly boys of course...", "open", "base", "base", "mid", cheeks="blush")
    call her_main("Some of them even cheered us on...", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main(".....", "base", "squint", "base", "mid")
    her "By the way, the girl I kissed, [genie_name]..."
    m "*Hmm*...?"
    call her_main("She is one of those unpopular girls...", "open", "closed", "base", "mid")
    her "I know that other students make fun of her sometimes..."
    call her_main("But today changed everything...", "base", "squint", "base", "mid")
    her "I Single-handedly turned that girl from a social outcast..."
    call her_main("Into \"that lesbian girl who made out with Hermione Granger\"!", "smile", "base", "angry", "mid")
    m "Wow... You are just like some kind of hero or something..."
    call her_main("I suppose I am, [genie_name]...", "base", "narrow", "base", "mid_soft")
    her "I changed that poor girl's life..."
    m "Now you are just pulling on my heartstrings..."

    jump end_hg_pr_kiss

label hg_pr_kiss_T4_E3:

    call hg_pr_kiss_intro

    her "I did."
    call her_main("..........", "annoyed", "base", "base", "R")
    call her_main("[genie_name]?", "open", "closed", "base", "mid")
    m "Yes, [hermione_name]?"
    call her_main("May I ask you a question?", "open", "base", "base", "mid")
    m "By all means."
    call her_main("*Ehm*...", "annoyed", "narrow", "angry", "R")
    call play_music("hermione") # Music
    call her_main("Why are boys so into watching girls make out with each other, [genie_name]?", "disgust", "narrow", "base", "mid_soft")

    menu:
        m "..."
        "\"Who knows? Boys are weird.\"":
            call her_main("Yes, they are, aren't they...?", "angry", "narrow", "base", "down")
            m "Yes, yes..."
            m "And that is why young girls such as yourself..."
            m "Are often interested in a much older gentleman..."
            call her_main("??!", "angry", "base", "base", "mid")
            call her_main("That is not what I meant, [genie_name]...", "annoyed", "narrow", "annoyed", "mid")

        "\"You wouldn't understand, girl.\"":
            call her_main("*Hmm*...", "upset", "closed", "base", "mid")
            call her_main("What about you, [genie_name]?", "angry", "base", "base", "mid")
            her "Were you like that when you were younger?"
            m "You mean if I enjoyed watching two girls going at it?"
            m "Well of course."
            m "I still do..."
            call her_main("Oh...", "upset", "closed", "base", "mid")

        "\"Kissing girls? Where?!!\"":
            call her_main("*Tsk*!......................", "angry", "base", "angry", "mid", emote="angry")

    call her_main("Well, I am only asking you this, [genie_name], because...", "open", "narrow", "worried", "down")
    call her_main("... it is sort of becoming a new trend in our school...", "angry", "base", "base", "mid")
    her "Some girls are willing to do this simply to catch the attention of the boy they fancy..."
    m "Are you one of those girls, [hermione_name]?"
    call her_main("I suppose...", "angry", "narrow", "base", "down")
    call her_main("I mean, only because of the favours you buy from me, [genie_name]...", "upset", "closed", "base", "mid")
    m "Good... Tell me more."
    call her_main("Well, as you know, I am quite popular...", "smile", "happyCl", "base", "mid", emote="happy")
    call her_main("So all I had to do is just mention that I would not mind doing it today...", "base", "happyCl", "base", "mid")
    her "And I had half a dozen girls lined up instantly..."
    call her_main("I chose a girl from Gryffindor of course...", "base", "base", "base", "mid")
    call her_main("And we put on a little show right in the middle of the classroom...", "open", "base", "base", "mid")
    m "Good... Tongue and everything?"
    call her_main("Tongue and everything, [genie_name].", "annoyed", "base", "worried", "R")
    m "Nicely done."
    call her_main("", "base", "base", "base", "mid")

    jump end_hg_pr_kiss

### Tier 5 ###

label hg_pr_kiss_T5_E1:

    call hg_pr_kiss_intro

    call play_music("hermione") # Music
    call her_main("I did, [genie_name].", "soft", "base", "base", "mid")
    m "I'm all ears..."
    call her_main("Well, I kissed that annoying blond girl from Slytherin...", "annoyed", "squint", "base", "mid")
    m "*Hmm*... \"annoying\", *huh*?"
    m "Because she happens to be from Slytherin."
    call her_main("Precisely so, [genie_name].", "open", "closed", "base", "mid")
    m "*Hmm*..."
    m "Don't you think that that's a little bit of prejudice on your part?"
    m "Or shall I say that you are being a \"housist\"?"
    call her_main("... a \"housist\", [genie_name]?", "annoyed", "narrow", "annoyed", "mid")
    m "Well, you know... It's like \"sexist\" or \"ageist\"..."
    m "You just put an \"ist\" after something and it automatically becomes a bad thing..."
    call her_main("\"housist\" is not an actual word, [genie_name]...", "soft", "base", "base", "R")
    m "It's not? Well, give it time..."
    call her_main(".............?", "annoyed", "narrow", "annoyed", "mid")
    m "\"Housophobic\"...?"
    m "No, wait, I got it!"
    m "\"Housophobe\"!"
    call her_main("Stop it, [genie_name]. I am not any of those weird words...", "normal", "squint", "angry", "mid")
    her "Slytherins are evil and annoying. Nobody likes them, and that is a fact!"
    m "Fine, whatever. Back to the \"girl-kissing\" then."
    call her_main("...............", "annoyed", "base", "worried", "R")
    her "Like I was saying..."
    call her_main("I kissed that girl from Slytherin...", "open", "base", "base", "mid")
    call her_main("Normally I would never do it, of course...", "annoyed", "narrow", "angry", "R")
    her "Not with someone from that wretched house any way..."
    call her_main("But she approached me first and practically begged me to do it with her...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("And today of all days...", "annoyed", "narrow", "angry", "R")
    her "to be honest..."
    call her_main("She was quite attractive...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("For someone from Slytherin that is...", "upset", "closed", "base", "mid")
    call her_main("I did not ask her why she needed this so desperately...", "open", "closed", "base", "mid")
    her "She was probably just trying to boost her own popularity at my expense..."
    her "Or it could also be that someone from the school staff bought this favour from her..."
    call her_main("The same way you buy favours from me, [genie_name]...", "open", "narrow", "annoyed", "mid", cheeks="blush")
    m "(Snape?)"
    call her_main("If that is the case I am sure that it was professor Snape...", "angry", "base", "angry", "mid")
    m "What? He would never..."
    call her_main("You should really investigate Professor Snape's activities, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "Of course..."
    m "Putting him on my \"naughty boys list\" as we speak..."
    call her_main("..........", "disgust", "narrow", "base", "mid_soft")
    m "What happened next, [hermione_name]?"
    call her_main("Oh, right...", "open", "narrow", "worried", "down")
    her "Well, we made out for a while..."
    her "She was very... passionate."
    call her_main("So I imagine it was quite a spectacle...", "angry", "wink", "base", "mid")
    her "The boys were cheering and whistling..."
    call her_main("So we decided to \"snowball\" a little...", "base", "narrow", "worried", "down")
    m "I'm sorry, you decided to do what?"
    call her_main("To \"snowball\", [genie_name].", "angry", "wink", "base", "mid")
    call her_main("It is when one girl spits into another girl's mouth...", "base", "narrow", "base", "mid_soft")
    her "We call it \"snowballing\"..."
    her "The boys really go crazy from that for some reason..."
    m "I imagine they do..."
    call her_main("So she spat into my mouth...", "open", "closed", "base", "mid")
    her "And then I spat into hers..."
    call her_main("Although I would much rather spit in her face!", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("Then she returned my spit...", "annoyed", "narrow", "angry", "R")
    call her_main("And I had to fight the urge to slap her smug face for doing that...", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("But I don't think the boys would appreciate that...", "upset", "closed", "base", "mid")
    m "Well... You would be surprised..."
    call her_main("In any case, After that we kissed some more...", "base", "narrow", "worried", "down")
    her "And then the break was over..."
    call her_main("And we had to run to class...", "angry", "wink", "base", "mid")
    m "*Sigh*... Nonchalant and innocent schooldays..."
    m "Home assignments... Classes..."
    m "Schoolgirls \"snowballing\" in the courtyard..."
    m "Well done, [hermione_name]."
    call her_main("", "grin", "base", "base", "R")

    jump end_hg_pr_kiss

label hg_pr_kiss_T5_E2:

    call hg_pr_kiss_intro

    call her_main("I did, [genie_name].", "open", "closed", "base", "mid")
    call her_main("Only... *Ehm*...", "grin", "base", "base", "R")
    m "What is it?"
    call her_main("Well... I have this friend...", "base", "base", "base", "mid")
    her "Her name is Ginny Weasley..."
    call her_main("And... *Ehm*...", "base", "base", "base", "R", cheeks="blush")
    her "I'm Not sure how to say this..."
    m "Just say it, [hermione_name]."
    call her_main("Well, we decided to skip the potions class together...", "open", "base", "base", "mid")
    her "And study for the upcoming Herbology test instead..."
    her "So me and Ginny, we were studying..."
    her "And we got to talking about boys..."
    m "Naturally..."
    call play_music("playful_tension") # Music
    call her_main("And then I sort of kissed her...", "open", "base", "base", "R", cheeks="blush")
    call her_main("And Ginny returned my kiss with such passion...", "base", "narrow", "base", "mid_soft")
    her "that we sort of ended up doing more than just kissing..."
    g9 "And afterwards you had a pillow fight in lingerie?"
    call her_main("Err... No...", "open", "happy", "base", "mid", cheeks="blush")
    m "What did you do then?"
    call her_main("I am not telling you, [genie_name].", "base", "base", "base", "R", cheeks="blush") # :)
    her "You sent me out to kiss a girl..."
    her "And I did just that."
    call her_main("The rest shall remain private.", "angry", "wink", "base", "mid")
    m "Now you are just being cruel, you little witch."
    call her_main("My points please.", "smile", "narrow", "base", "mid_soft")
    m "Fine..."

    jump end_hg_pr_kiss
