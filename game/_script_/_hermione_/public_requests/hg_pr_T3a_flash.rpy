
### Flash A Classmate ###

label hg_pr_flash:

    # Setup
    $ current_payout = 35

    if hg_pr_flash.counter == 0:
        m "{size=-4}(Tell her to flash her tits to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)

    #Intro.
    if hg_pr_flash.counter == 0:
        m "[hermione_name]..."
        m "I would like to award Gryffindor with twenty-five house points today."
        call her_main("Really?", "base", "base", "base", "mid")
        her "Thank you, [genie_name]!"
        m "Yes, but first I will require your help with something..."
        her "Of course, [genie_name]! Anything!"
        m "I need you to go out there and show off your tits to people..."

        stop music fadeout 1.0

        call her_main("...?", "open", "base", "base", "mid")
        m "You know, flash your breasts to some boys..."
        call her_main("?!!", "shock", "wide", "base", "stare")

        if her_reputation < 9:
            jump too_much_public

        call play_music("hermione")

        her "[genie_name]!"
        call her_main("This is a completely new level of inappropriate, even for you, [genie_name]!", "angry", "base", "angry", "mid")
        her "How can you ask one of your pupils to perform such a task?"
        m "So that's how you feel then? I see..."
        m "I suppose I will be awarding those points to some other house instead ..."
        m "Slytherin perhaps?"
        call her_main("................", "disgust", "narrow", "base", "mid_soft")
        m "But, you know, no pressure..."
        call her_main("[genie_name]...", "annoyed", "narrow", "angry", "R")
        her "The fate of my house is very important to me, but..."
        m "Is it really?"
        m "Why don't you show it to me then?"
        m "Yes. Show me how important it is to you exactly, [hermione_name]."
        call her_main("But this is inappropriate...", "angry", "base", "angry", "mid")
        m "Are we really in any position to discuss what is appropriate and what is not at this point?"
        call her_main("..................", "annoyed", "narrow", "angry", "R")
        m "I would say that ship has sailed a long time ago..."
        call her_main("..............", "disgust", "narrow", "base", "mid_soft")
        m "All I ask you to do is to give some lucky boy a quick peek..."
        call her_main("But why? Why must I do things like this, [genie_name]?", "annoyed", "narrow", "angry", "R")
        m "A minute of your time for twenty-five house points..."
        m "A pretty nifty deal, wouldn't you agree?"
        her "I suppose..."
        her "Well alright, I'll see what I can do..."
    else:
        if her_tier >= 5:
            m "[hermione_name] I need you to go out there and flash your tits to one of your classmates."
            call her_main("I will do my best [genie_name].", "open", "closed", "base", "mid")
            m "Really? Just like that? No complaints or anything?"
            call her_main("I am getting paid for this, am I not?", "base", "narrow", "base", "mid_soft")
            m "Of course."
            call her_main("Why would I complain about a simple task like this then?", "open", "closed", "base", "mid")
            her "{number=current_payout} house points is a fair prices for a few seconds of excitement... err..."
            call her_main("... I mean, embarrassment.", "base", "happyCl", "base", "mid")
            m "{size=-3}(She changed this much already?){/size}"
            g9 "{size=-3}(I'm so good at this training thing that it's starting to get creepy!){/size}"
            call her_main("Classes are about to start... I'd better leave now.", "base", "base", "base", "mid")
            her "I will see you later tonight, [genie_name]."
        elif her_tier >= 4:
            m "I think you need to show off your tits some more, [hermione_name]."
            call her_main("You mean to you, [genie_name]?", "upset", "wink", "base", "mid")
            m "No, to your classmates..."
            call her_main("Oh...", "angry", "base", "base", "mid")
            m "Yes, go do that and then report back to me..."
            call her_main("Will I get paid for this?", "annoyed", "narrow", "angry", "R")
            m "Of course you will get paid for this, [hermione_name]. Don't be silly."
            m "{number=current_payout} house points. The usual rate..."
            call her_main(".................", "annoyed", "narrow", "angry", "R")
            call her_main("Well alright... I will see what I can do, [genie_name]...", "disgust", "narrow", "base", "mid_soft")
        else:
            m "I think you need to show off your tits some more, [hermione_name]."
            call her_main("You mean to you, [genie_name]?", "upset", "wink", "base", "mid")
            m "No, to your classmates..."
            call her_main("Oh...", "angry", "base", "base", "mid")
            m "Yes, go do that and then report back to me..."
            call her_main("Will I get paid for this?", "annoyed", "narrow", "angry", "R")
            m "Of course you will get paid for this, [hermione_name]. Don't be silly."
            m "{number=current_payout} house points. The usual rate..."
            call her_main(".................", "annoyed", "narrow", "angry", "R")
            call her_main("Well alright... I will see what I can do, [genie_name]...", "disgust", "narrow", "base", "mid_soft")

    call her_walk(action="leave")

    $ hg_pr_flash.inProgress = True

    jump end_hermione_event

label end_hg_pr_flash:
    $ gryffindor += current_payout

    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_flash.counter == 1:
        show screen blktone
        with d3

        call her_main("(Stupid Slytherin...)", "angry", "narrow", "angry", "mid", ypos="head", flip=False, trans=d3)
        call her_main("(I {b}HATE{/b} them!)", "angry", "closed", "worried", "mid")

        hide screen blktone
        with d3

    elif not hg_pr_flash.monologue_glass and hg_pr_flash.is_event_complete(5, 3): # Event specific
        $ hg_pr_flash.monologue_glass = True

        show screen blktone
        with d3

        call her_main("(I can't believe I did that today...)", "upset", "closed", "base", "mid", ypos="head", flip=False, trans=d3)
        call her_main("(What if Harry or Ron saw me like that?)", "angry", "wide", "base", "stare")
        call her_main("(Standing there...)")
        call her_main("(Pressing my breasts against that window glass...)")
        call her_main("(I would probably just die of embarrassment right there on the spot...)", "angry", "narrow", "base", "down")
        call her_main("(No. Protecting the honour of the Gryffindor house is my number one priority.)", "upset", "closed", "base", "mid")
        call her_main("(We must get the cup this year, no matter the cost...)")
        call her_main("(........)", "angry", "narrow", "base", "down")

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_flash.inProgress = False

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

label hg_pr_flash_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    if hg_pr_flash.is_tier_complete():
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_flash

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_flash.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("Well... *Ehm*...", "soft", "base", "base", "R")
        m "Speak up, [hermione_name]."

    m "Did you flash some lucky guy? How did it go?"

    return

### Tier 3 ###

label hg_pr_flash_T3_E1:

    call hg_pr_flash_intro

    call play_music("playful_tension") # Music
    call her_main("*Ehm*... Not too well, actually...", "angry", "happyCl", "worried", "mid",emote="sweat")
    her "................................"
    m "Just tell me what happened, [hermione_name]."
    call her_main("That is the thing, [genie_name]...", "open", "base", "base", "mid")
    her "Nothing happened..."
    call her_main("I just couldn't bring myself to do it...", "open", "narrow", "worried", "down")
    m "I see..."
    m "Well, I can't just give you the points for nothing, [hermione_name]."
    call her_main("Of course, [genie_name]... I understand...", "open", "closed", "base", "mid")
    call her_main("I shall try harder next time... I promise...", "annoyed", "base", "worried", "R")
    m "Then I will just put these {number=current_payout} points aside for now..."
    call her_main("Thank you, [genie_name]...", "annoyed", "base", "worried", "R")
    her "..."
    her "I'd better go now."

    call her_walk(action="leave")

    $ hg_pr_flash.inProgress = False

    jump end_hermione_event

label hg_pr_flash_T3_E2:

    call hg_pr_flash_intro

    call play_music("hermione") # Music
    call her_main("*Ehm*... Sort of...", "annoyed", "base", "worried", "R")
    m "Sort of?"
    call her_main("Yes... *Ehm*...", "open", "base", "base", "mid")
    her "Well, I decided to try and flash them to this Hufflepuff boy..."
    call her_main("I've been waiting for the right moment...", "open", "narrow", "worried", "down")
    her "I was worried that something would go wrong..."
    call her_main("And, of course, everything that could - did...", "annoyed", "narrow", "angry", "R")
    call her_main("When I tried to expose myself to the boy...", "open", "base", "base", "mid")
    her "At first I only pulled up my vest..."
    her "Then I tried to pull my shirt up as well..."
    her "And one of my breasts got entangled in the fabric and was pulled up along with the shirt..."
    call her_main("So only one of my breasts was naked and I was desperately trying to free the other one.", "scream", "happyCl", "worried", "mid")
    her "Other students started to pay attention to me..."
    her "So I had to fix my clothes back into place quickly..."
    her "And then the moment was gone..."
    call her_main("............", "normal", "happyCl", "worried", "mid")
    m "*Hmm*..."
    m "What about the boy? Did he see your tits or not?"
    call her_main("Well, I think he may have seen one of them...", "open", "base", "base", "mid")
    her "But from the way he was looking at me..."
    her "I doubt that he understood that the whole commotion was for his benefit."
    call her_main("......................", "annoyed", "base", "worried", "R")
    call her_main("I'm sorry, [genie_name]...", "open", "base", "base", "mid")
    m "That's alright..."
    m "I wouldn't expect you to perform perfectly this early in your training..."
    call her_main("(My training?)", "angry", "base", "base", "mid")

    jump end_hg_pr_flash

label hg_pr_flash_T3_E3:

    call hg_pr_flash_intro

    call play_music("hermione") # Music
    call her_main("I think it went well, [genie_name].", "annoyed", "base", "worried", "R")
    m "Good. Tell me more."
    call her_main("*Ehm*... There is not much to tell, really...", "open", "base", "base", "mid")
    call her_main("I spent the first half of the day with studying in the library...")
    call her_main("It is usually quite deserted during that time...")
    call her_main("Apart from me there was only one student...")
    call her_main("Some boy from Ravenclaw...", "upset", "closed", "base", "mid")
    call her_main("So I waved to him and when he looked up at me...")
    call her_main("I quickly pulled my shirt up...", "angry", "base", "base", "mid")
    m "Good job."
    m "How did he react to the sight of your naked tits?"
    call her_main("I'm not sure...", "angry", "narrow", "base", "down")
    call her_main("He looked rather shocked I suppose...", "angry", "base", "base", "mid")
    call her_main("After I showed him my breasts it got too embarrassing for me to stay there any longer...", "angry", "narrow", "base", "down")
    call her_main("So I just gathered all my books and left...", "angry", "base", "base", "mid")
    m "I see..."

    jump end_hg_pr_flash

### Tier 4 ###

label hg_pr_flash_T4_E1:

    call hg_pr_flash_intro

    call her_main("...........", "upset", "base", "worried", "R")
    m "[hermione_name], did you complete your task or not?"
    call her_main("Yes I did, [genie_name].", "upset", "wink", "base", "mid")
    call her_main(".............", "angry", "narrow", "base", "down")
    m "Well?"
    call her_main("................", "angry", "narrow", "base", "down")
    call play_music("hermione") # Music
    call her_main("Just for the record, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "*Hmm*?"
    call her_main("I think that forcing your pupils to do things like this...", "scream", "closed", "angry", "mid")
    call her_main("Is beneath an esteemed wizard such as yourself...", "upset", "closed", "base", "mid")
    m "\"Forcing\"? Nobody is forcing you to do anything, [hermione_name]."
    m "You came to me, remember?"
    call her_main("..........", "open", "base", "base", "mid")
    m "You begged me to buy a sexual favour from you."
    call her_main("... I...", "annoyed", "base", "worried", "R")
    call her_main("I never said \"sexual\"...", "open", "base", "base", "mid")
    m "Nevertheless, you can stop selling me these favours at any moment, [hermione_name]."
    call her_main("I suppose...", "annoyed", "narrow", "angry", "R")
    m "And yet you keep on coming back..."
    call her_main("............................", "angry", "narrow", "base", "down")
    m "I think you may actually be taking some twisted form of pleasure from this."
    call her_main("What?", "angry", "base", "angry", "mid")
    m "Shame on you, [hermione_name]. Shame on you."
    call her_main("[genie_name], I never...!", "angry", "base", "angry", "mid")
    m "Enough of this. Did you complete your task or not?"
    call her_main("Yes I did...", "upset", "closed", "base", "mid")
    m "And?"
    call her_main("And that is all I am going to say...", "open", "narrow", "worried", "down")
    call her_main("........", "upset", "closed", "base", "mid")
    m ".........."
    her "........"
    m "Oh, whatever. Just take your points and go."
    call her_main("", "annoyed", "closed", "base", "mid")

    jump end_hg_pr_flash

label hg_pr_flash_T4_E2:

    call hg_pr_flash_intro

    call play_music("hermione") # Music
    call her_main("..........", "normal", "happyCl", "worried", "mid")
    m "................"
    her "..............."
    m "Well?"
    call her_main("Can I get paid first?", "open", "base", "base", "mid")
    m "Not before you tell me what exactly you did today."
    call her_main("....................", "normal", "happyCl", "worried", "mid")
    call her_main("Do I really have to, [genie_name]?", "open", "base", "base", "mid")
    m "When you are being coy like this..."
    m "It only makes me more curious. You know that, right?"
    call her_main("*Aww*...", "angry", "base", "base", "mid")
    call her_main("Well... *Ehm*...", "angry", "narrow", "base", "down")
    her "Well, alright, here it goes..."
    call her_main("I flashed my tits to that Slytherin underclassman in a corridor...", "scream", "happyCl", "worried", "mid")
    her "But I was standing too close to him..."
    call her_main("....", "normal", "happyCl", "worried", "mid")
    her "...."
    call her_main("Well, he sort of grabbed one of my breasts, [genie_name]...", "open", "base", "base", "mid")
    her "he squeezed it hard and just wouldn't let go..."
    call her_main("He made me promise to meet him after my classes...", "angry", "base", "base", "mid")
    her "And let him..."
    call her_main("\"Play with my tits\" some more...", "open", "happyCl", "worried", "mid")
    call her_main("You see, that is why I hate Slytherin boys, [genie_name]...", "angry", "narrow", "base", "down")
    her "They don't have a shred of honour.."
    her "..."
    m "Did you keep your promise?"
    call her_main("No, not yet...", "angry", "base", "base", "mid")
    her "I'm planning to meet that awful boy after we are done here, [genie_name]."
    m "I see..."
    m "Well, I shouldn't keep you waiting then, should I?"

    jump end_hg_pr_flash

label hg_pr_flash_T4_E3:

    call hg_pr_flash_intro

    call her_main("It went well.", "open", "base", "base", "mid")
    m "I'm listening..."
    call her_main("Well...", "open", "base", "base", "mid")
    her "I had to spend a big portion of the day at the school library..."
    her "So I didn't really have the time to perform your task properly, [genie_name]..."
    m "*Hmm*...?"
    call play_music("playful_tension") # Music
    her "Instead I just went to the library window and..."
    call her_main("... I just pulled my shirt up and pressed my bare breasts against the glass...", "angry", "narrow", "base", "down")
    her "I stood there like that for several seconds..."
    her "To make sure that at least someone sees me from the outside..."
    call her_main("I hope this still counts, [genie_name]...", "angry", "base", "base", "mid")
    m "*Hmm*..."
    m "How many students would you say saw you standing behind that window?"
    call her_main("I am not sure, [genie_name]... A couple maybe...?", "angry", "narrow", "base", "down")
    m "\"Maybe\"?"
    call her_main("I don't know, [genie_name]...", "open", "happyCl", "worried", "mid",cheeks="blush")
    her "To be honest I kept my eyes closed..."
    m "How do you know that anyone saw you at all then, [hermione_name]?"
    call her_main("I heard someone shout: \"Look! At that window over there!\".", "angry", "squint", "base", "mid",cheeks="blush")
    her "When I heard that I covered up and quickly left..."
    call her_main("....", "angry", "base", "base", "mid")
    m "*Hmm*..."
    m "Well, alright... I think this counts..."

    jump end_hg_pr_flash

### Tier 5 ###

label hg_pr_flash_T5_E1:

    call hg_pr_flash_intro

    call her_main("As usual, [genie_name]...", "base", "base", "base", "mid")
    m "I'm listening..."
    call her_main("Well... I had to spend a big portion of the day in the school library...", "upset", "wink", "base", "mid")
    call her_main("So I didn't really have the time to perform your task properly, [genie_name]...")
    m "*Hmm*...?"
    call her_main("Instead I just made sure there were no teachers around...", "angry", "base", "base", "mid")
    call play_music("playful_tension") # Music
    call her_main("Pulled my shirt up...")
    call her_main("And then I just sat there like that for a while...", "open", "base", "base", "mid")
    call her_main("trying to get some studying done...", "open", "narrow", "worried", "down")
    her "I don't think there were many people around..."
    call her_main("Or at least I hope so...", "angry", "narrow", "base", "down")
    call her_main("But they definitely saw my breasts, [genie_name]...", "angry", "base", "base", "mid")
    call her_main("eventually A few first years seemed to notice...", "angry", "narrow", "base", "down")
    call her_main("I had to leave pretty quickly after that...", "angry", "base", "base", "mid")
    m "*Hmm*..."
    m "How many people would you say saw your tits today, [hermione_name]?"
    call her_main("Hard to say, [genie_name]...", "open", "base", "base", "mid")
    call her_main("Two dozen boys or so I suppose...")
    call her_main("A few girls as well...", "annoyed", "base", "worried", "R")
    call her_main("I think the school librarian may have seen me too...")
    m "*Hmm*... Well, I'd say that's a job well done."

    jump end_hg_pr_flash

label hg_pr_flash_T5_E2:

    call hg_pr_flash_intro

    call her_main("It went alright, I suppose.", "base", "base", "base", "mid")
    m "Well, tell me all about it, then."
    call her_main("*Ehm*... Okay...", "open", "base", "base", "mid")
    her "I was flashing my tits to this boy in the Gryffindor common room..."
    call her_main("When my friend, Ginny walked in on us...", "open", "base", "base", "mid")
    m "Another boy?"
    call her_main("A boy? No, Ginny is a girl's name, [genie_name].", "soft", "base", "base", "R")
    m "....."
    call her_main("Ginny Weasley, [genie_name].", "open", "base", "base", "mid")
    m "Alright, fine, continue..."
    call her_main("*Ehm*...", "soft", "base", "base", "R")
    her "......."
    call play_music("hermione") # Music
    call her_main("*Giggle*", "grin", "happyCl", "worried", "mid",emote="sweat")
    m "*Hmm*...?"
    call her_main("Then Ginny grabbed my breasts...", "smile", "base", "base", "R")
    her "And started to squeeze them..."
    her "then she started to kiss my breasts passionately..."
    m "............"
    call her_main("to kiss and suck on my nipples...", "smile", "base", "angry", "mid")
    call her_main("And I couldn't help myself - I started to moan...", "base", "narrow", "base", "mid_soft")
    m ".............."
    call her_main("And then the boy took out his throbbing cock...", "base", "squint", "base", "mid")
    her "And sprayed his hot spunk all over me and Ginny!"
    call her_main("And then me and Ginny, we licked his hot sperm off of our bodies...", "smile", "base", "angry", "mid")
    m ".............."
    m "Are you making this up, [hermione_name]?"
    call her_main("... maybe.", "grin", "happyCl", "worried", "mid",emote="sweat")
    call her_main("I just thought that you would like to hear something like that, [genie_name]...", "base", "narrow", "base", "mid_soft")
    m "What I would like to hear, [hermione_name], is the truth."
    call her_main("Even if it's incredibly dull, [genie_name]?", "open", "closed", "base", "mid")
    m "Dull or not..."
    m "I only want to know what actually happened..."
    m "Keep your fantasies to yourself, [hermione_name]."
    call her_main("As you wish, [genie_name].", "annoyed", "narrow", "annoyed", "up")
    her "My friend Ginny walked in on me while I was flashing my tits to that guy."
    her "But she promised to not tell anyone."
    call her_main("And that's all that happened, [genie_name]...", "soft", "base", "base", "mid")
    m "I see..."
    m "I still prefer this to some made up stories..."

    jump end_hg_pr_flash

label hg_pr_flash_T5_E3:

    call hg_pr_flash_intro

    call play_music("hermione") # Music
    call her_main("Yes I did, [genie_name]...", "base", "base", "base", "mid")
    m "Alright, tell me how did it go."
    call her_main("Well, let's see...", "annoyed", "base", "worried", "R")
    her "First I flashed them to that one boy from Ravenclaw..."
    call her_main("Then to that upperclassman from Hufflepuff...", "open", "base", "base", "mid")
    call her_main("Then there was this other boy from Ravenclaw.", "base", "base", "base", "mid")
    m "???"
    call her_main("After that I flashed my tits to some Gryffindor underclassman by mistake...", "angry", "happyCl", "worried", "mid",emote="sweat")
    call her_main("No, wait... the boy from Gryffindor was after that other boy...", "annoyed", "base", "worried", "R")
    m "How many boys did you flash your tits to today, [hermione_name]?"
    call her_main("Half a dozen or so?", "angry", "base", "base", "mid")
    call her_main("I had an opening in my schedule...", "angry", "wink", "base", "mid")
    her "So I decided to go for some extra credit with your assignment, [genie_name]."
    m "This is not an assignment, [hermione_name]..."
    m "And there are no extra credits..."
    call her_main("Oh...?", "open", "base", "base", "mid")
    m "You are still getting your usual payment, [hermione_name], and that's it."
    call her_main("Oh... I see...", "annoyed", "base", "worried", "R")
    m "But, [hermione_name]..."
    call her_main("Yes, [genie_name]?", "open", "base", "base", "mid")
    g9 "That was very well done."
    call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")

    jump end_hg_pr_flash
