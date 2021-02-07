
### Let Classmate Molest Her ###

label hg_pr_grope:

    # Setup
    $ current_payout = 25

    if hg_pr_grope.counter == 0:
        m "{size=-4}(Tell her to go get groped by one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")

    #Intro.
    if hg_pr_grope.counter == 0:
        m "You do like boys your age, don't you?"
        call her_main("...?", "normal", "base", "base", "mid")
        m "One of your classmates maybe?"
        call her_main("Well...", "open", "base", "worried", "R")
        her "Must I really discuss things like this with you, [genie_name]?"
        call her_main("It's a bit embarrassing...", "annoyed", "base", "worried", "R")
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, [hermione_name]."
        m "Go confront that boy...{w=0.5} or a girl, you fancy. The one you think is \"just so dreamy\"..."
        call her_main(".......?", "open", "base", "base", "mid")
        m "And let them touch you..."

        if her_reputation < 6:
            jump too_much_public

        call her_main("Let them... touch me, [genie_name]?", "open", "base", "base", "mid")
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, [hermione_name]? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        call her_main("\"The talk\", [genie_name]?", "angry", "happyCl", "worried", "mid", emote="sweat")
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that \"pee-pee\" in their mouths?"
        call her_main("[genie_name]!!!", "normal", "base", "base", "mid")
        call her_main("What kind of demented parent would have such a talk with their child?", "angry", "base", "angry", "mid")
        m "{size=-3}I wish mine did.{/size}"
        call her_main("I beg your pardon, [genie_name]?", "annoyed", "squint", "base", "mid")
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, [hermione_name]."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        call her_main("..........", "annoyed", "narrow", "angry", "R")
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        call her_main("How many points would I receive after completing such a task, [genie_name]?", "disgust", "narrow", "base", "mid_soft")
        m "*Hmm*... {number=current_payout} should do..."
        call her_main("{number=current_payout} house points...", "annoyed", "narrow", "angry", "R")
        her "...."
        call her_main("Well, so be it then...", "disgust", "narrow", "base", "mid_soft")
        m "Great..."
        call her_main("I'd better go now. The classes are about to start...", "angry", "base", "angry", "mid")
    else:
        if her_tier >= 4:
            m "[hermione_name], I need you to go out there..."
            m "Find a handsome guy and force yourself on him!"
            call her_main("You mean like...", "base", "base", "base", "mid")
            call her_main("In a sexual way, [genie_name]?", "angry", "wink", "base", "mid")
            m "What? No, I mean just let him get under your uniform that's all..."
            call her_main("Oh, I see...", "grin", "happyCl", "worried", "mid", emote="sweat")
            call her_main("I wonder who it should be this time...", "grin", "base", "base", "R")
            call her_main("More than one boy, is not a problem, is it, [genie_name]?", "angry", "base", "base", "mid")
            m "A problem? Of course not!"
            m "If anything - it is encouraged."
            call her_main("Great. I will see you after the classes then, [genie_name]. As usual.", "angry", "wink", "base", "mid")
            m "Yes. Good luck."
        elif her_tier >= 3:
            m "[hermione_name], I need you to go out there, and make one of your classmates molest you a little."
            call her_main("I understand, [genie_name]...", "base", "base", "base", "mid")
            m "Off you go then."
            her "..........."
        else:
            m "How about you go let one of your classmates molest you a little again?"
            call her_main("........", "upset", "closed", "base", "mid")
            m "{number=current_payout} house points, [hermione_name]."
            call her_main("[genie_name], it's just...", "annoyed", "narrow", "angry", "R")
            call her_main("I do not understand why I must do things like that...", "annoyed", "narrow", "annoyed", "mid")
            m "To help out your house?"
            call her_main("That's not what I meant...", "disgust", "narrow", "base", "mid_soft")
            call her_main("Oh, never mind...", "annoyed", "narrow", "angry", "R")
            her "The classes are about to start, I'd better go..."
            m "Will you do it?"
            call her_main("I don't know... Maybe...", "disgust", "narrow", "base", "mid_soft")

    call her_walk(action="leave")

    $ hg_pr_grope.inProgress = True

    jump end_hermione_event

label end_hg_pr_grope:
    $ gryffindor += current_payout

    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."

    label .no_pay:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if hg_pr_grope.counter == 1:
        show screen blktone
        with d3

        call her_main("(Why did I agree to this...)", "disgust", "base", "worried", "down", ypos="head", flip=False, trans=d3)

        hide screen blktone
        with d3

    call her_chibi("leave")

    $ hg_pr_grope.inProgress = False

    # Increase Points

    if her_tier == 2:
        if her_reputation < 9:
            $ her_reputation += 1

        if her_whoring < 9:
            $ her_whoring += 1
    elif her_tier == 3:
        if her_reputation < 12:
            $ her_reputation += 1

        if her_whoring < 12:
            $ her_whoring += 1

    elif her_tier == 4:
        if her_reputation < 18:
            $ her_reputation += 1

        if her_whoring < 18:
            $ her_whoring += 1

    jump end_hermione_event

label hg_pr_grope_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Did you finish your task?"
    her "I did, just as you asked [genie_name]..."

    if hg_pr_grope.is_tier_complete():
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_grope

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0
    show screen blktone
    with d3

    if hg_pr_grope.counter == 1:
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("I... *Uhh*...", "soft", "base", "base", "R")

    m "Did you let some lucky guy feel you up or what?"

    return

### Tier 2 ###

label hg_pr_grope_T2_E1:

    call hg_pr_grope_intro

    her "Well, there is not much to tell..."
    call her_main("I told that one guy I know that he could touch me a little if he wants...", "open", "base", "base", "mid")
    call her_main("He thought I was joking at first...", "annoyed", "base", "worried", "R")
    call her_main("So embarrassing...", "normal", "happyCl", "worried", "mid")
    m "So, did he cop a feel or not?"
    call play_music("playful_tension") # Music
    call her_main("He did...", "normal", "happyCl", "worried", "mid")
    m "Well, where did he touch you, [hermione_name]?"
    call her_main("*Ehm*... My legs...", "annoyed", "base", "worried", "R")
    her "And my breasts a little I suppose..."
    m "That's all?"
    call her_main("Yes, [genie_name]...", "open", "base", "base", "mid")
    call her_main("It's getting late... I think I'd better leave now...", "normal", "happyCl", "worried", "mid")
    call her_main("I'm sorry, [genie_name]...", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "Nothing to be sorry about, [hermione_name]."
    m "You did good. This will do for now."

    jump end_hg_pr_grope

label hg_pr_grope_T2_E2:

    call hg_pr_grope_intro

    call her_main("I did, but it was all very awkward and embarrassing...", "annoyed", "narrow", "angry", "R")
    m "That's the whole point of it, [hermione_name]."
    m "Tell me where you were touched today..."
    call play_music("playful_tension") # Music
    her "*Ehm*..."
    call her_main("Well, he touched me under my skirt a little...", "angry", "base", "base", "mid")
    her "Then I let him rub my..."
    call her_main("... my c-crotch through my panties, [genie_name].", "angry", "narrow", "base", "down")
    m "Very good... And what happened next?"
    call her_main("He just sort of started... Touching himself [genie_name].", "open", "happyCl", "worried", "mid")
    her "So, I decided to leave..."
    m "I see..."
    call her_main(".............", "normal", "happyCl", "worried", "mid")

    jump end_hg_pr_grope

label hg_pr_grope_T2_E3:

    call hg_pr_grope_intro

    call play_music("playful_tension") # Music
    call her_main("I led this one guy from Hufflepuff to an empty classroom and I told him that he can touch me if he wants.", "open", "base", "base", "mid")
    her "That I don't mind..."
    call her_main("...........", "annoyed", "base", "worried", "R")
    m "And?"
    call her_main("Well, he did touch me a little at first...", "open", "base", "base", "mid")
    call her_main("......", "normal", "happyCl", "worried", "mid")
    m "Don't make me pull every word out of you, [hermione_name]!"
    m "What happened?"
    call her_main("Well...", "open", "narrow", "worried", "down")

    stop music fadeout 1.0

    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
    call her_main("He asked me to call him a \"sissy boy\"...", "upset", "wink", "base", "mid")
    call play_music("despair") # Music
    call her_main("And he kept on reassuring me that he has a very small penis...", "open", "base", "worried", "down")
    call her_main("He just kept repeating that *sob*!...", "angry", "base", "base", "mid", tears="soft")
    call her_main("Why would anyone be like this?", "angry", "base", "base", "mid", tears="soft")
    her "*Sob*! I Could not stay in his company a moment longer, so I just ran."
    m "I'm sorry to hear this..."
    call her_main("It was truly awful, [genie_name]...", "angry", "base", "base", "mid", tears="soft")
    m "There, there..."
    call her_main("*Sob*!", "normal", "base", "base", "R", tears="soft")
    m "Will ten extra points make you feel better?"
    call her_main("*huh*? That would be very sweet of you [genie_name].", "soft", "base", "base", "mid", tears="soft")
    m "Of course... Don't mention it."
    call her_main("Thank you [genie_name]...", "base", "base", "worried", "mid", cheeks="blush", tears="soft")

    $ current_payout += 10

    jump end_hg_pr_grope

### Tier 3 ###

label hg_pr_grope_T3_E1:

    call hg_pr_grope_intro

    call play_music("playful_tension") # Music
    call her_main("Well... There is not much to tell...", "open", "closed", "base", "mid")
    her "I found this one boy from Ravenclaw..."
    her "Led him to one of the empty classrooms in the eastern wing..."
    her "He thought I wanted to make out with him..."
    her "But I told him that I just want him to touch me..."
    call her_main("... so he did.", "normal", "happyCl", "worried", "mid")
    m "I see..."
    m "Well done, [hermione_name]."
    call her_main("Will I be getting my points now?", "upset", "wink", "base", "mid")
    m "In a minute, [hermione_name]. I have a question I would like to ask you before that."
    call her_main("Yes?", "open", "base", "base", "mid")
    m "Did you enjoy it?"
    m "Did it feel good to be touched by that boy?"
    call her_main("Oh...", "open", "closed", "base", "mid")
    her "Well, he was rather handsome I suppose..."
    call her_main("I didn't hate it, if that's what you mean, [genie_name]...", "upset", "closed", "base", "mid")
    m "I see..."

    jump end_hg_pr_grope

label hg_pr_grope_T3_E2:

    call hg_pr_grope_intro

    call her_main("Well...", "open", "closed", "base", "mid")
    her "I'm not sure whether or not this counts, but..."
    her "During Herbology class today..."
    call play_music("hermione") # Music
    call her_main("I let this one boy slide his hand under my skirt...", "upset", "wink", "base", "mid")
    her "So while Professor Sprout explained the differences between {i}mandrake{/i} and {i}mandragore{/i}..."
    call her_main("--Something I already knew of course--...", "open", "squint", "base", "mid")
    call her_main("I let my lab partner grab my buttocks once...", "upset", "wink", "base", "mid")
    her "And that is all..."

    menu:
        m "*Hmm*..."
        "\"You can do better than that, [hermione_name].\"":
            m "I'm afraid I cannot pay you."
            call her_main("Yes, I know, [genie_name]. I am sorry.", "open", "base", "base", "mid")
            m "Just make sure you try harder next time."
            her "I will, [genie_name]."

            jump end_hg_pr_grope.no_pay

        "\"Kudos to you for doing this during class.\"":
            call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
            m "I say you deserve to get paid."

    jump end_hg_pr_grope

label hg_pr_grope_T3_E3:

    call hg_pr_grope_intro

    call her_main(".................", "annoyed", "narrow", "angry", "R")
    m "???"
    call play_music("playful_tension") # Music
    call her_main("I don't want to talk about it, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "What happened, [hermione_name]. Spit it out."
    call her_main(".................", "annoyed", "narrow", "annoyed", "mid")
    call her_main("But... it's so embarrassing...", "open", "base", "worried", "mid")
    call her_main("Do I really have to, [genie_name]?", "normal", "happyCl", "worried", "mid")
    g9 "Yes, I happen to love embarrassing things!"
    call her_main(".................", "annoyed", "narrow", "angry", "R")
    her "Well, alright..."
    her "I approached this one guy that I always found attractive..."
    her "Managed to muster up enough courage to ask him to follow me..."
    call her_main("Normally I wouldn't dare...", "open", "base", "base", "mid")
    her "But the fact that I was doing this as a task entrusted to me by someone else..."
    her "It made it easier somehow..."
    m "Happy to help, [hermione_name]."
    call her_main("I led him to the library...", "open", "narrow", "worried", "down")
    her "We found a secluded spot behind one of the book shelves..."
    her "And I told him that he can touch me wherever he wants..."
    her "And..."
    call her_main("..........", "clench", "narrow", "base", "down")
    m "What?"
    call her_main(".....................", "normal", "happyCl", "worried", "mid")
    call play_music("despair") # Music
    call her_main("He started to touch my... feet, [genie_name].", "scream", "happyCl", "worried", "mid")
    m "*huh*?"
    m "Your \"Feet\"? Is that what zoomers call tits these days?"
    call her_main("I wish, [genie_name]...", "disgust", "narrow", "base", "mid_soft")
    her "He asked me to take off my shoes..."
    her "Then he..."
    call her_main("He started to smell my toes, [genie_name]!", "angry", "base", "base", "mid", tears="soft")
    call her_main("I felt so... violated!", "angry", "base", "base", "mid", tears="soft")
    m "So he didn't touch your tits, or your butt?"
    g4 "Or even in-between your thighs?!"
    call her_main("No, [genie_name]... *sob*!", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    m "Alright, then what happened?"
    call her_main("Nothing! I couldn't bear the humiliation... I just ran...", "angry", "narrow", "base", "mid", cheeks="blush", tears="crying")
    her "I even left my shoes behind and had to come back later to pick them up..."
    call her_main("*Sob*!............", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    m "*Hmm*..."
    m "Well, you did get molested..."
    m "Although in a rather unconventional manner..."
    call her_main("*Sob*! I wish he would have just touched my breasts like any normal boy would, [genie_name]... *Sob!*", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
    m "There, there..."
    m "You earned your points today..."

    jump end_hg_pr_grope

### Tier 4 - ###

label hg_pr_grope_T4_E1:

    call hg_pr_grope_intro

    call her_main("......", "annoyed", "base", "worried", "R")
    call her_main("Well...", "open", "base", "base", "mid")
    her "During the potions class today..."
    her "I wrote a note on a piece of paper..."
    her "I was about to slide it to my lab partner's coat when..."
    call play_music("hermione") # Music
    call her_main("Professor Snape snatched it right out of my hand...", "annoyed", "narrow", "angry", "R")
    call her_main("He then read it out aloud for the entire class...", "annoyed", "narrow", "annoyed", "mid", cheeks="blush")
    call her_main("I thought I was going to die from embarrassment...", "disgust", "narrow", "annoyed", "down", cheeks="blush")
    m "What did the note say?"
    call her_main("Well...", "open", "narrow", "worried", "down", cheeks="blush")
    call her_main("It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\"", "open", "narrow", "worried", "R", cheeks="blush")
    call her_main("Everyone was laughing...", "angry", "narrow", "base", "down", cheeks="blush")
    her "It was so embarrassing..."
    call her_main("I really hate professor Snape, [genie_name]...", "angry", "base", "angry", "mid", cheeks="blush")
    m "What happened then?"
    call her_main("Nothing...", "open", "narrow", "worried", "down")
    call play_music("playful_tension") # Music
    her "But when the class was over..."
    her "These two nasty-looking boys from Slytherin cornered me..."
    her "Actually they weren't mean to me or anything..."
    her "So we just waited for everyone to leave the classroom..."
    call her_main("And then I let them touch me...", "angry", "base", "base", "mid")
    call her_main("They touched me everywhere, [genie_name]...")
    m "\"Everywhere\", *huh*?"
    call her_main("Yes...{w=0.5} Everywhere,{w=0.5} [genie_name]...", "soft", "narrow", "annoyed", "up")
    call her_main("There were hands under my skirt, under my shirt...", "base", "narrow", "base", "mid_soft")
    her "And then I started to breathe heavily..."
    call her_main("So one of them just put his hand over my mouth...", "soft", "narrow", "annoyed", "up")
    her "And their hands were so... thorough..."
    her "My head started to spin..."
    call her_main("It was most exhilarating, [genie_name].", "base", "narrow", "base", "mid_soft")
    m "Very good, [hermione_name]. Very good indeed."

    jump end_hg_pr_grope

label hg_pr_grope_T4_E2:

    call hg_pr_grope_intro

    call her_main("Actually something quite unexpected happened to me today, [genie_name]...", "base", "base", "base", "mid")
    her "Right after the D.A.D.A class..."
    m "D.A.D.A?"
    call her_main("Defence Against Dark Arts, [genie_name].", "open", "closed", "base", "mid")
    her "Anyway..."
    call her_main("This stocky Hufflepuff boy came up to me...", "open", "base", "base", "R")
    call play_music("playful_tension") # Music
    call her_main("He said someone told him that I let boys touch me...", "angry", "wink", "base", "mid")
    call her_main("Normally I would deny everything...", "base", "narrow", "base", "mid_soft")
    her "But I decided not to waste the opportunity..."
    call her_main("I took the boy to a quiet spot and let him touch me...", "base", "narrow", "base", "up")
    her "I let him run his hands up and down my thighs..."
    her "I let him fondle my breasts..."
    call her_main("All the usual things...", "base", "narrow", "base", "mid_soft")
    m "Well done, [hermione_name]."

    jump end_hg_pr_grope

label hg_pr_grope_T4_E3:

    call hg_pr_grope_intro

    call her_main("Well...", "upset", "wink", "base", "mid")
    her "I did what you told me to do, [genie_name]..."
    her "But... it sort of... *Ehm*..."
    call her_main("Well, it sort of escalated into something else...", "base", "narrow", "base", "up")
    call play_music("playful_tension") # Music
    m "*Hmm*?"
    call her_main("*Ehm*...", "upset", "wink", "base", "mid")
    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
    m "You got caught? By one of the teachers?"
    call her_main("No, [genie_name]...", "base", "base", "base", "mid")
    call her_main("By the boy's girlfriend...", "smile", "base", "base", "R")
    m "Interesting..."
    call her_main("She was furious with him at first...", "angry", "base", "base", "mid")
    call her_main("But then...", "angry", "wink", "base", "mid")
    call her_main("*Ehm*... She started to touch my breasts as well...", "base", "narrow", "worried", "down")
    call her_main("Almost the same way her boyfriend did just a moment ago...", "smile", "base", "angry", "mid")
    her "Then she turned to him and she said..."
    call her_main("\"I love you baby, and I want to share everything with you...\"", "open", "closed", "base", "mid")
    her "\"... And that includes your whores.\""
    call her_main("I did not appreciate being called a whore of course...", "angry", "base", "base", "mid")
    call her_main("But that was such a sweet and romantic gesture...", "base", "base", "base", "mid")
    her "Wouldn't you agree, [genie_name]?"
    m "Totally..."
    m "Seems that true love {size=+5}does{/size} exist after all."
    m "Then what happened?"
    call her_main("*Ehm*... Well...", "grin", "happyCl", "worried", "mid", emote="sweat")
    call her_main("They both started touching me a little again...", "upset", "wink", "base", "mid")
    call her_main("And then they started kissing in front of me...", "annoyed", "base", "worried", "R")
    her "A moment later their hands were all over each other."
    her "I felt like the third wheel in that situation, so I just slipped away quietly..."
    m "*Emm*..."
    m "Perhaps if you've stayed a little longer... or perhaps taken the initiative..."
    m "No matter."

    jump end_hg_pr_grope
