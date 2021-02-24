define her_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 12,
    "touch vagina": 18,
    "unequip panties": 6,
    "unequip bra": 6,
    "unequip top": 3,
    "unequip bottom": 3,
    }

define her_responses = {
    "category_fail": "her_reaction_category_fail",
    "equip": "her_reaction_equip",
    "equip_fail": "her_reaction_equip_fail",
    "unequip": "her_reaction_unequip",
    "unequip_fail": "her_reaction_unequip_fail",
    "touch": "her_reaction_touch",
    "touch_fail": "her_reaction_touch_fail",
    "equip_outfit": "her_reaction_equip_outfit",
    "equip_outfit_fail": "her_reaction_equip_outfit_fail",
    "blacklist": "her_reaction_blacklist",
}

label her_reaction_category_fail(category):

    if category == "upper undergarment":
        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call her_main("I'd rather keep the underwear I have on already thank you very much...", "annoyed", "closed", "angry", "mid")
        elif random_number == 2:
            call her_main("You want me to change my underwear?", "angry", "wide", "base", "mid")
            call her_main("Why on earth would I do that?", "open", "base", "angry", "R")
        elif random_number == 3:
            call her_main("Change my--", "soft", "wide", "base", "mid")
            call her_main("I'm not changing my underwear for you...", "clench", "closed", "angry", "mid")
    elif category == "lower undergarment":
        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call her_main("I'm not going to let you ogle at my underwear...", "angry", "happy", "angry", "mid")
        elif random_number == 2:
            call her_main("I don't believe there's anything wrong with my current underwear...", "open", "base", "annoyed", "mid")
        elif random_number == 3:
            call her_main("[genie_name], I don't think this is part of our arrangement...", "soft", "base", "annoyed", "mid")
    elif category == "piercings & tattoos":
        if her_whoring >= 12:
            call her_main("*Ehm*... Do I have to?", "annoyed", "squint", "base", "mid")
            call her_main("Isn't it supposed to hurt?", "upset", "base", "base", "R")
        elif her_whoring >= 6:
            call her_main("You can look all you want but I will not have such things done to my body...", "normal", "base", "annoyed", "mid")
        else:
            #under naked level
            call her_main("You want me to what?", "open", "wide", "base", "mid")
            call her_main("I will not put such things on my body...", "clench", "base", "base", "mid")

    return

label her_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
        $ random_number = renpy.random.randint(1, 3)

        if her_whoring >= 20:
            #craving it
            if random_number == 1:
                call her_main("*Mmm*...", "base", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("Does this mean I've been a good girl, [genie_name]?", "crooked_smile", "narrow", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("Thank you [genie_name]...", "base", "happy", "base", "mid", cheeks="blush")
        elif her_whoring >= 16:
            #enjoying it
            if random_number == 1:
                call her_main("I guess I could get used to this...", "soft", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("*Hmm*... This does feel kind of nice...", "open", "closed", "worried", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("...", "base", "closed", "base", "mid", cheeks="blush")
        elif her_whoring >= 12:
            #enjoying it a bit
            if random_number == 1:
                call her_main("...", "normal", "happyCl", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("I'm only letting you do this because I have to...", "open", "squint", "annoyed", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("*Ehm*... Do you do this to every student?", "base", "closed", "base", "mid", cheeks="blush")
        elif her_whoring >= 8:
            #confused
            if random_number == 1:
                call her_main("*Ehm*... Isn't petting your student a bit weird?", "upset", "happyCl", "base", "mid")
            elif random_number == 2:
                call her_main("Okay then... I guess this is what we're doing now...", "disgust", "squint", "base", "mid")
            elif random_number == 3:
                call her_main("Is there something in my hair?", "soft", "base", "base", "mid")
        else: # >= 4
            #annoyed but letting you
            if random_number == 1:
                call her_main("Are you petting me?", "disgust", "base", "base", "mid")
            elif random_number == 2:
                call her_main("Did you just...{w=0.4} Whatever...", "annoyed", "narrow", "base", "R")
            elif random_number == 3:
                call her_main("Why are you doing that?", "clench", "base", "base", "R")

    elif what == "breasts":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 4)

        if her_whoring >= 20:
            if random_number == 1:
                call her_main("*Mmm*...{w=0.4} Lower...", "base", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("I'm glad you're enjoying them so much, [genie_name].", "base", "narrow", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("*Ah*...", "open", "closed", "base", "mid", cheeks="blush")
            elif random_number == 4:
                call her_main("Please be gentle...", "soft", "closed", "base", "mid", cheeks="blush")
        elif her_whoring >= 16:
            if random_number == 1:
                call her_main("So, I guess this is part of our arrangement now...", "base", "narrow", "base", "down", cheeks="blush")
            elif random_number == 2:
                call her_main("Oh! Hey, at least give me a warning first.", "soft", "squint", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("Your hands not good enough anymore?", "base", "squint", "base", "R", cheeks="blush")
            elif random_number == 4:
                call her_main("Hey... These things are sensitive you know...", "grin", "narrow", "base", "down", cheeks="blush")
        else: # >= 12
            if random_number == 1:
                call her_main("Why are you kissing my...", "angry", "base", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("I didn't say you could...{w=0.4} Never mind...", "clench", "closed", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("I thought I was supposed to get points for this...", "annoyed", "base", "base", "mid", cheeks="blush")
                call her_main("I guess a small kiss is fine...", "annoyed", "base", "base", "R", cheeks="blush")
            elif random_number == 4:
                call her_main("That's not my cheek...", "disgust", "narrow", "base", "mid", cheeks="blush")
    elif what == "vagina":
        $ mouse_heart()

        if hermione.is_worn("bottom"):
            # Bottoms only OR Bottoms AND panties
            $ random_number = renpy.random.randint(1, 3)
            if random_number == 1:
                call her_main("Naughty...", "grin", "narrow", "base", "mid")
            elif random_number == 2:
                call her_main("*Mmm*... Want to see what's underneath do you?", "base", "narrow", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("Got your eye on something?", "base", "narrow", "base", "mid")
        elif hermione.is_worn("panties"):
            # Panties only
            $ random_number = renpy.random.randint(1, 2)
            if random_number == 1:
                call her_main("*Mmm*... Shall I take off my panties?", "open", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("You're going to make my panties wet if you keep doing that...", "soft", "narrow", "base", "mid", cheeks="blush")
        else:
            # NO bottoms AND NO panties
            $ random_number = renpy.random.randint(1, 4)
            if random_number == 1:
                call her_main("*Ah*...", "open_tongue", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call her_main("*Mmm*...", "soft", "closed", "base", "mid", cheeks="blush")
            elif random_number == 3:
                call her_main("More...", "open", "closed", "base", "mid", cheeks="blush")
            elif random_number == 4:
                call her_main("Keep going [genie_name]...", "smile", "closed", "base", "mid", cheeks="blush")
            ##This could play after touching her enough times this wardrobe session##
            #call her_main("*Nnngh*...", "base", "base", "base", "mid")
            #with kissiris

    return

label her_reaction_touch_fail(what):
    $ random_number = renpy.random.randint(1, 5)

    if what == "head":
        $ mouse_slap()
        if random_number == 1:
            call her_main("Stop that!", "angry", "wide", "angry", "mid")
        elif random_number == 2:
            call her_main("[genie_name]!", "open", "narrow", "angry", "L")
        elif random_number == 3:
            call her_main("Unhand me...", "mad", "wide", "angry", "mid")
        elif random_number == 4:
            call her_main("Stop it please...", "open", "happyCl", "angry", "mid", cheeks="blush")
        elif random_number == 5:
            call her_main("Hands off me.", "clench", "narrow", "angry", "mid")
    elif what == "breasts":
        $ mouse_slap()
        if random_number == 1:
            call her_main("No touching!", "open", "narrow", "angry", "L")
        elif random_number == 2:
            call her_main("Bad [genie_name]!", "annoyed", "happyCl", "angry", "L", cheeks="blush")
        elif random_number == 3:
            call her_main("Hands to yourself.", "clench", "base", "angry", "R")
        elif random_number == 4:
            call her_main("Cut it out..", "open", "narrow", "angry", "mid")
        elif random_number == 5:
            call her_main("Hands off me.", "mad", "wide", "angry", "mid")
    elif what == "vagina":
        $ mouse_slap()
        if random_number == 1:
            call her_main("Stop that!", "angry", "wide", "angry", "mid")
        elif random_number == 2:
            call her_main("[genie_name]!", "open", "narrow", "angry", "L")
        elif random_number == 3:
            call her_main("Unhand me..", "mad", "wide", "angry", "mid")
        elif random_number == 4:
            call her_main("Stop it please..", "open", "happyCl", "angry", "mid", cheeks="blush")
        elif random_number == 5:
            call her_main("Hands off me.", "clench", "narrow", "angry", "mid")
    return

label her_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     her "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label her_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     her "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 5)

    if random_number == 1:
        call her_main("I am not wearing that...", "annoyed", "base", "angry", "down")
    elif random_number == 2:
        call her_main("Thanks. but no thanks...", "annoyed", "happyCl", "angry", "R")
    elif random_number == 3:
        call her_main("You actually think I'd put on something like that?", "annoyed", "wide", "angry", "mid")
    elif random_number == 4:
        call her_main("I'm not some Slytherin skank [genie_name], ask them to humiliate themselves for your amusement...", "open", "narrow", "angry", "L")
    elif random_number == 5:
        call her_main("This is too much.", "annoyed", "narrow", "angry", "R")

    return

label her_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if her_whoring > 15:
    #        her "You want to see my snatch?"
    #        her "You got it [genie_name]!"
    #
    return

label her_reaction_unequip_fail(item):
    $ random_number = renpy.random.randint(1, 3)

    if item.type == "panties":
        if random_number == 1:
            call her_main("I'm not gonna flash you anything!", "clench", "narrow", "angry", "mid")
            call her_main("{size=-4}Pervert..{/size}", "annoyed", "narrow", "angry", "R")
        elif random_number == 2:
            call her_main("Take off my panties?! No way!", "clench", "narrow", "angry", "mid")
            call her_main("", "annoyed", "narrow", "angry", "down")
        elif random_number == 3:
            call her_main("I am not taking off my panties!", "clench", "narrow", "angry", "mid")
            call her_main("", "annoyed", "narrow", "angry", "mid")

    elif item.type == "bra":
        if random_number == 1:
            call her_main("I'm not gonna flash you anything!", "clench", "narrow", "angry", "mid")
            call her_main("{size=-4}Pervert..{/size}", "annoyed", "narrow", "angry", "R")
        elif random_number == 2:
            call her_main("Take off my bra?! No way!", "clench", "narrow", "angry", "mid")
            call her_main("", "annoyed", "narrow", "angry", "down")
        elif random_number == 3:
            call her_main("I am not taking off my bra!", "clench", "narrow", "angry", "mid")
            call her_main("", "annoyed", "narrow", "angry", "mid")

    elif item.type == "top":
        call her_main("Take my top off? Are you crazy?", "annoyed", "narrow", "angry", "L")

    elif item.type == "bottom":
        call her_main("Take my bottoms off so you can ogle my ass? No thank you.", "open", "narrow", "angry", "mid")
    return

label her_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Default Schoolgirl ##
    ########################
    if item == her_outfit_default:
        m "Could you put on your regular school uniform?"
        if her_whoring < 10:
            call her_main("Of course, [genie_name].", "open", "base", "base", "mid")
            call her_main("Let me go and change real quick...", "soft", "base", "base", "R")
        elif her_whoring < 19:
            call her_main("Alright, [genie_name].", "base", "base", "base", "mid")
            call her_main("Let me go and change real quick...", "open", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("Are you sure, [genie_name]?", "open", "base", "base", "mid")
            call her_main("My regular school uniform...", "soft", "base", "base", "R")
            call her_main("You don't even want me to remove my tie or show off any cleavage?", "open", "squint", "worried", "mid")
            m "No, [hermione_name]... No cleavage today."
            call her_main("(Is he up to something?).", "normal", "narrow", "base", "R")
            call her_main("(Maybe this is a test of some sort...)", "clench", "squint", "base", "stare")
            call her_main("Okay then, let me change it real quick", "clench", "squint", "base", "R")
        else: #22+

            call her_main("That old thing?", "clench", "base", "base", "mid")
            call her_main("Is this some silly joke, [genie_name]?", "annoyed", "narrow", "base", "mid")
            m "..."
            m "(I don't know...{w=0.3} Is it?)"
            call her_main("This is unacceptable!", "open", "closed", "annoyed", "mid")
            call her_main("It doesn't even show any skin!", "clench", "closed", "annoyed", "mid")
            m "(...)"
            call her_main("It's an insult to my breast, [genie_name]!!!", "open", "squint", "annoyed", "mid")
            g4 "*Gasps* {w=0.9}I would never... [hermione_name]!"

            $ temp_word = renpy.random.choice(["marvellous", "magnificient", "breath-taking", "wonderful", "spectacular", "sensational", "glorious", "beautiful", "lovely", "bananas"])

            g4 "Your tits are [temp_word]!"

            call her_main("And yet you want me to wear those... rags!", "annoyed", "base", "annoyed", "mid")
            m "You going to wear it or not?"
            call her_main("*Ugh*, fine! Let me change it real quick.", "upset", "closed", "annoyed", "mid")

    ###############################
    ## Clear Day (School no vest)##
    ###############################
    elif item == her_outfit_s_clearday:
        m "Could you wear your school uniform for me? But leave the vest off."
        if her_whoring < 4:
            call her_main("Certainly, [genie_name].", "open", "squint", "base", "mid")
            call her_main("I'd usually only take it off if it's hot outside... When it isn't, I always make a point to wear the vest.", "normal", "closed", "base", "mid")
            call her_main("But you are the headmaster, after all, so I'll wear it without the vest if I must.", "open", "closed", "base", "mid")
            call her_main("Let me just go and change, [genie_name].", "open", "base", "base", "R")
        elif her_whoring < 13:
            call her_main("Alright, [genie_name].", "open", "squint", "base", "mid")
            call her_main("Let me go and change it real quick.", "soft", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("Of course, [genie_name].", "base", "squint", "base", "mid")
            call her_main("I will just change it right here if you don't mind...", "open", "closed", "base", "mid")
        else: #22+
            call her_main("Just my school shirt and tie?", "open", "base", "base", "mid")
            m "Yes, [hermione_name]."
            call her_main("Do you want me to tie the shirt around my breasts?", "base", "narrow", "base", "mid")
            m "No, put it on properly."
            call her_main("Properly, [genie_name]?", "annoyed", "squint", "worried", "mid")
            m "You know, buttons and everything."
            call her_main("Can I leave some buttons open, [genie_name]?", "open", "squint", "worried", "mid")
            m "I'm afraid not, [hermione_name]."
            call her_main("Okay then... Let me just change it real quick.", "annoyed", "narrow", "base", "R")

    ########################################################
    ## Clear Night (Jeans and muggle top with undershirt) ##
    ########################################################
    elif item == her_outfit_s_clearnight:
        m "Could you wear your normal clothing, the one with jeans and the top with the undershirt?"
        if her_whoring < 4:
            call her_main("Of course!", "base", "happy", "base", "mid")
            call her_main("You should've seen the look on Malfoy's face when he saw me buy it in a muggle shop.", "smile", "closed", "base", "mid")
            call her_main("It was right outside the leaky cauldron you see.", "crooked_smile", "squint", "base", "R")
            call her_main("He looked as if he had bit into a--", "smile", "happyCl", "base", "mid")
            m "I don't need your life story, just put it on..."
            call her_main("*Hmph*... Fine.", "upset", "squint", "base", "mid")
        elif her_whoring < 13:
            call her_main("OK, [genie_name].", "base", "base", "base", "mid")
            call her_main("Let me put it on.", "open", "happy", "base", "mid")
        elif her_whoring < 22:
            call her_main("Just my regular muggle clothing, [genie_name]?", "soft", "squint", "base", "mid")
            m "Indeed."
            call her_main("If you say so...", "open", "base", "base", "R")
        else: #22+
            call her_main("My muggle clothing, [genie_name]?", "open", "squint", "base", "L")
            m "Yeah, that one!"
            call her_main("It's a bit... Too normal don't you think?", "soft", "squint", "base", "mid")
            m "I don't see how that's a bad thing..."
            call her_main("Alright then... Let me put it on real quick.", "open", "narrow", "base", "down")

    ################################
    ## Snowy (Jeans and pullover) ##
    ################################
    elif item == her_outfit_s_snow:
        m "Could you put on your regular clothing, the one with jeans and pullover?"
        if her_whoring < 4:
            call her_main("As you wish, [genie_name].", "base", "squint", "base", "mid")
            call her_main("I do love wearing it.", "base", "happyCl", "base", "mid")
            m "Why's that?"
            call her_main("My mother made it for me.", "base", "happy", "base", "R")
            m "I see...{w} Is she as hot--"
            call her_main("Let me go and change real quick.", "soft", "happy", "base", "R")
        elif her_whoring < 13:
            call her_main("Glad you're caring about my health [genie_name]... This office does get a little bit cold sometimes.", "base", "closed", "base", "mid")
            m "Ah yes... Your health is important... I wouldn't be able to summon you if you caught a cold, would I?"
            call her_main("...", "normal", "squint", "base", "mid")
            call her_main("I'll just go and change it then... [genie_name].", "open", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("My mother made that jumper for me you know...", "open", "closed", "base", "mid")
            call her_main("I wonder what she'd say if she knew I rarely wear it anymore...", "soft", "closed", "base", "mid")
            m "She'd probably be proud that you're not relying on her giving you clothes anymore."
            call her_main("*Hmm*... Somehow I doubt that...", "normal", "squint", "base", "R")
        else: #22+
            call her_main("That old thing?", "annoyed", "base", "base", "mid")
            call her_main("It's a bit boring don't you think?", "open", "squint", "base", "R")
            m "I think you look great in it!"
            call her_main("*Hmm*... Alright then.", "soft", "narrow", "base", "mid")

    ##########################################
    ## Overcast (School skirt and pullover) ##
    ##########################################
    elif item == her_outfit_s_overcast:
        m "Could you put on your regular clothing, the one with the school skirt and pullover?"
        if her_whoring < 4:
            call her_main("The pullover does go well with the school skirt don't you think?", "base", "squint", "base", "mid")
            m "It would look good even without the skirt on in my opinion."
            call her_main("How nice, I'll let my mother know you said--", "base", "closed", "base", "mid", cheeks="blush")
            call her_main("Wait, what did you say?", "soft", "wide", "base", "mid", cheeks="blush")
            m "I said it looks good."
            call her_main("Oh... Okay then...", "open", "happy", "base", "mid")
            call her_main("Give me a moment to let me change.", "open", "base", "base", "R")
        elif her_whoring < 13:
            call her_main("The skirt and pullover?", "open", "squint", "base", "mid")
            m "That's what I just said..."
            call her_main("Okay, just making sure.", "soft", "squint", "base", "mid")
            call her_main("One moment please...", "base", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("Is it cold in here?", "open", "squint", "base", "L")
            call her_main("I guess I didn't notice...", "normal", "base", "base", "down")
            call her_main("One moment...", "open", "base", "base", "mid")
        else: #22+
            call her_main("Skirt and pullover...", "normal", "squint", "base", "stare")
            call her_main("A little bit of home...", "normal", "squint", "base", "stare")
            m "[hermione_name]?"
            call her_main("Oh... Sorry!", "base", "base", "base", "mid")
            call her_main("One moment...", "open", "squint", "base", "mid")

    #####################################
    ## Rainy (School outfit with cloak)##
    #####################################
    elif item == her_outfit_s_rain:
        m "Could you put on your regular school outfit, and your cloak as well."
        if her_whoring < 4:
            call her_main("I wanted to talk to you about this actually...", "open", "closed", "base", "mid")
            m "(Oh, here we go...)"
            call her_main("The cloak doesn't cover the head so when it rains it just ends up in your hair.", "annoyed", "squint", "base", "mid")
            call her_main("I always end up having to dry it using magic, making it go all frizzy.", "upset", "narrow", "base", "R")
            m "Isn't your hair already--"
            call her_main("...", "normal", "narrow", "base", "mid")
            m "I mean... great point [hermione_name]."
            call her_main("Thank you...", "base", "closed", "base", "mid")
            m "Now. can you put it on?"
            call her_main("...{w=0.4} Fine...", "normal", "base", "base", "R")
        elif her_whoring < 13:
            call her_main("Certainly, [genie_name]...", "base", "base", "base", "mid")
            call her_main("Just let me go change real quick.", "open", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("You suddenly want me to cover up now?", "angry", "narrow", "base", "R")
            menu:
                "\"Yes, your body disgusts me and I'm doing everyone a favour...\"":
                    call her_main("What!?", "clench", "wide", "base", "mid")
                "\"Of course not...\"":
                    m "I'd just like you to wear it... Is that so much to ask?"
                    call her_main("I guess not...", "upset", "base", "base", "R")
            m "Don't be silly... Just put it on..."
            call her_main("...", "normal", "narrow", "base", "mid")
            call her_main("Alright...", "open", "narrow", "base", "mid")
        else: #22+
            call her_main("*Hmm*... I don't really like wearing the cloak...", "upset", "base", "base", "down")
            m "Why's that?"
            m "(As if I don't know the answer...)"
            call her_main("It covers all the good bits!", "soft", "closed", "annoyed", "mid")
            m "Really? It doesn't look like it does..."
            call her_main("What do you mean? You can barely see any--", "annoyed", "narrow", "annoyed", "mid")
            m "Your face is perfectly visible..."
            call her_main("Oh... Such a charmer...", "base", "squint", "annoyed", "R")
            call her_main("Well... Since you're putting it that way...", "smile", "wink", "base", "mid")
            call her_main("", "smile", "base", "base", "mid")
    ########################
    ## Cheerleader Normal ##
    ########################
    elif item == her_outfit_cheerleader_1: #Req 10 whoring
        m "Could you wear the cheerleader outfit for me?"
        if her_whoring < 19:
            call her_main("Gryffindor colours I presume?", "open", "closed", "base", "mid")
            m "We'll see..."
            call her_main("...{w=0.4} Fine.", "annoyed", "closed", "base", "mid")
        elif her_whoring < 22:
            call her_main("*Hmm*... Alright then...", "base", "happy", "worried", "R")
            call her_main("I'll just change it here shall I?", "base", "narrow", "base", "mid")
            m "That's the spirit."
        else: #22+
            $ random_number = renpy.random.randint(1, 3)
            call her_main("That thing is so silly...", "base", "squint", "base", "R")
            call her_main("You sure you don't want to get a giant lion's head to go with it?", "crooked_smile", "narrow", "base", "mid")
            if random_number == 1:
                call her_main("Or perhaps some Raven's feathers?!", "smile", "narrow", "base", "R")
            elif random_number == 2:
                call her_main("Or some Snake fangs?!", "smile", "narrow", "base", "R")
            elif random_number == 3:
                call her_main("Or face paint, so I could look like a badger?!", "smile", "narrow", "base", "R")
            m "I mean, if I could find something like that, sure!"
            call her_main("You can't be serious, [genie_name]!", "open", "wide", "worried", "stare")
            m "Wear it, or I will have you go naked!"
            call her_main("...", "normal", "closed", "base", "mid")
            call her_main("{size=-5}(How exciting!){/size}", "base", "closed", "base", "mid", cheeks="blush")
            call her_main("I will wear it if I absolutely have to,...", "open", "squint", "base", "mid", cheeks="blush")
            call her_main("{size=-5}Do I?{/size}", "grin", "base", "base", "L", cheeks="blush")
            m "Yes."
            call her_main("*Tzzz--* Your loss...", "annoyed", "base", "base", "R")

    ######################
    ## Cheerleader Lewd ##
    ######################
    elif item == her_outfit_cheerleader_2: #Req 16 whoring (top)
        m "Could you put on the cheerleader outfit for me?"
        if her_whoring < 22:
            call her_main("Of course!", "smile", "base", "base", "mid")
            m "Great, here you go!"
            call her_main("[genie_name], did you hand me the wrong outfit?", "open", "squint", "base", "mid", cheeks="blush")
            m "Let me see..."
            m "Looks correct to me..."
            call her_main("[genie_name]... This is not the official cheerleader outfit...", "soft", "narrow", "base", "mid")
            m "Oh, I see why you were confused then... Yes. this one has indeed had some improvements."
            call her_main("...", "angry", "squint", "base", "R")
            m "So, will you put it on?"
            call her_main("Alright, fine...", "angry", "squint", "base", "mid")
        else: #22+
            call her_main("Of course!", "smile", "happy", "base", "mid")
            m "Excellent, here you are..."
            call her_main("How naughty... Although I doubt you'd be able to focus on the match if the cheerleaders wore these...", "soft", "narrow", "base", "down", cheeks="blush")
            m "Good point..."
            m "I'm sure people would get excited..."
            call her_main("I'm sure they would...", "base", "squint", "base", "R")
            call her_main("Go-Go Gryffindor!", "smile", "squint", "base", "mid")

    #################
    ## Fishnet Outfit
    #################
    elif item == her_outfit_fishnet: #Req 19 (panties, top)
        m "Could you please wear--"
        if her_whoring < 22:
            call her_main("A fishnet outfit?", "angry", "squint", "base", "down")
            call her_main("[genie_name]... Isn't this a bit...", "annoyed", "squint", "base", "mid")
            m "A bit what?"
            call her_main("Well, it's fetish gear, isn't it?", "open", "base", "base", "R", cheeks="blush")
            m "I'd say it's closer to lingerie than fetish gear."
            call her_main("*Hmm*... Alright fine I'll wear it then...", "annoyed", "closed", "base", "mid")
        else: #22+
            call her_main("A fishnet outfit?", "soft", "squint", "base", "down")
            call her_main("*Hmm*... My nipples would stick right through this...", "base", "narrow", "base", "down", cheeks="blush")
            m "I think that's the point."
            call her_main("Alright, just give me a moment and I'll put it on for you...", "soft", "base", "base", "mid", cheeks="blush")

    ##################
    ## Latex Outfit ##
    ##################
    elif item == her_outfit_latex: #Req 19 (top)
        m "Could you put on this latex outfit for me?"
        if her_whoring < 22:
            call her_main("Latex outfit?", "open", "squint", "base", "mid")
            call her_main("*Whoa*... This is skin tight!", "clench", "narrow", "base", "down", cheeks="blush")
            m "I know! Glad you're as excited as I am!"
            call her_main("I... How do you put this on?", "disgust", "base", "base", "mid", cheeks="blush")
            m "Using lots of patience I reckon..."
            call her_main("As if you have any of that...", "open", "base", "annoyed", "R")
            call her_main("Well... Here it goes.", "open", "base", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("*Hmm*... Well I can't say something as skin tight as this doesn't excite me a little bit...", "base", "narrow", "base", "mid", cheeks="blush")
            call her_main("I might as well not be wearing anything with how little this leaves to the imagination.", "smile", "narrow", "base", "mid", cheeks="blush")
            m "Like that's a bad thing..."
            call her_main("I knew you'd say that... Alright then, give me a moment...", "angry", "base", "base", "R", cheeks="blush")

    #######################
    ## Slutty Schoolgirl ##
    #######################
    elif item == her_outfit_slutty_schoolgirl: #Req 19 (top, Bottom)
        m "Could you put on this school uniform for me?"
        if her_whoring < 22:
            call her_main("My school uniform?", "angry", "base", "worried", "mid")
            call her_main("Is this some sort of test?", "clench", "squint", "base", "mid")
            m "No, not a test. I'd just like you to put it on..."
            call her_main("(*Hmm*... I feel like he's trying to trick me...)", "normal", "base", "base", "R")
            m "Just put it on..."
            call her_main("Alright then...", "open", "squint", "base", "mid")
            call her_main("Oh... I see... That makes more sense.)", "open", "base", "base", "down", cheeks="blush")
            m "Is there something wrong?"
            call her_main("No, it's all good... Just give me a moment...", "open", "base", "base", "mid", cheeks="blush")
            call her_main("", "base", "base", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("My school uniform?", "open", "squint", "worried", "mid")
            call her_main("But that thing is so boring...", "clench", "closed", "worried", "mid")
            m "Not this one..."
            call her_main("Oh... That one...", "open", "base", "base", "down", cheeks="blush")
            call her_main("Well I suppose I could put that one on...", "base", "base", "base", "R", cheeks="blush")
            call her_main("One moment...", "base", "base", "base", "mid")

    ##################
    ## Witch Outfit ##
    ##################
    elif item == her_outfit_witch: #Req 10 (top)
        m "Put on this witch outfit for me will you?"
        if her_whoring < 13:
            call her_main("Witch outfit?", "open", "squint", "base", "mid")
            m "The one I have right here."
            call her_main("Sir, this is not a witch outfit...", "disgust", "narrow", "base", "mid")
            m "Of course it is... I see this kind of outfit all the time in the shops."
            call her_main("In the... What shops exactly?", "angry", "narrow", "base", "mid")
            m "Next to the nurse outfits."
            call her_main("Sir... Are you talking about the Cosplay section?", "clench", "squint", "base", "mid")
            m "That's the one!"
            call her_main("Figures...", "disgust", "closed", "base", "mid")
            call her_main("I would've thought an actual wizard would get mad about the muggle interpretation of a witch...", "open", "narrow", "base", "R")
            m "I think it's flattering."
            call her_main("...", "angry", "closed", "base", "mid")
            m "So..."
            call her_main("So?", "upset", "base", "base", "mid")
            m "You putting it on or what?"
            call her_main("If I have to...", "normal", "squint", "base", "R", cheeks="blush")
            m "You do."
            call her_main("Fine...", "open", "base", "base", "down", cheeks="blush")
            call her_main("Give me a moment to let me change.", "open", "base", "base", "R")
        elif her_whoring < 22:
            call her_main("Witch outfit?", "soft", "squint", "base", "mid")
            m "The one I have right here."
            call her_main("Oh, I see...", "angry", "narrow", "base", "down", cheeks="blush")
            call her_main("Of course you'd want me to wear something like that...", "clench", "closed", "base", "mid", cheeks="blush")
            call her_main("To think it'd be a regular witches outfit...", "open", "narrow", "base", "R", cheeks="blush")
            call her_main("Well... I suppose I could put it on.", "normal", "base", "base", "down", cheeks="blush")
            call her_main("One moment please...", "normal", "squint", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("Witch outfit?", "open", "squint", "base", "mid")
            m "The one I have right here."
            call her_main("Right...", "grin", "base", "base", "down", cheeks="blush")
            call her_main("Well... While real witches' outfits don't look like this I do like this muggle interpretation...", "crooked_smile", "narrow", "base", "mid", cheeks="blush")
            m "Actually I had this custom made..."
            call her_main("*Hmm*... You did, did you?", "grin", "narrow", "base", "mid", cheeks="blush")
            call her_main("Looks like someone's gotten their hands on a particular kind of muggle magazine...", "crooked_smile", "wink", "base", "mid")
            m "No idea what you're talking about..."
            m "Just put it on will you?"
            call her_main("Of course [genie_name], as you wish...", "base", "narrow", "base", "mid", cheeks="blush")

    #######################
    ## Lara Croft Outfit ##
    #######################
    elif item == her_outfit_croft: #Req 10 (top, bottom)
        m "Could you put on this archaeologist outfit for me?"
        call her_main("A what?", "open", "squint", "base", "mid")
        m "This one..."
        if her_whoring < 13:
            m "Worn by the great Lara Croft!"
            call her_main("Someone you know?", "soft", "base", "base", "mid")
            m "Indeed... I'm a massive fan."
            m "(Especially of the fan service...)"
            call her_main("Must be a great woman then, seeing your reaction.", "base", "closed", "base", "mid")
            g9 "A great woman indeed! Went cave exploring with her a couple times..."
            m "Good times..."
            call her_main("I wonder why I haven't heard of her...", "angry", "base", "base", "R")
            call her_main("Well... I suppose I could wear it since you speak so highly of her.", "open", "closed", "base", "mid")
            call her_main("Give me a moment to let me change.", "open", "base", "base", "R")
        elif her_whoring < 22:
            m "Lara Croft looks stunning in it so I think you'd probably fill it just as well."
            call her_main("Fill it?", "angry", "squint", "base", "mid")
            m "Fit it..."
            call her_main("I guess I'll have to look up this Archaeologist...", "open", "happy", "base", "R")
            m "Please do, she's got a lot of material out there for you to enjoy."
            m "\"Goons raid her\" is one of my favourites."
            call her_main("Sounds fascinating.", "open", "squint", "base", "mid")
            call her_main("Well, hopefully I'll do her clothing justice.", "open", "base", "base", "down")
            call her_main("Just give me a minute to put it on...", "base", "base", "base", "mid")
        else: #22+
            m "I'm sure Lara Croft would love to see someone wear her famous outfit."
            m "Although last time I saw her, she couldn't wait to take it off..."
            call her_main("Take it off?", "open", "squint", "base", "R", cheeks="blush")
            m "Indeed... She's quite famous in certain circles you know."
            m "Let's just say if you're anyone in the world of archaeology you've heard about Lara Croft..."
            call her_main("Right...", "base", "narrow", "base", "down", cheeks="blush")
            m "I'd delve her cavern any--"
            call her_main("Okay, okay... Just don't call me Lara once I put it on...", "clench", "narrow", "base", "mid", cheeks="blush")

    #######################
    ## Heart Slut Outfit ##
    #######################
    elif item == her_outfit_hslut: #Req 19 (top, panties, bra)
        m "Put on this burlesque outfit for me will you?"
        if her_whoring < 22:
            call her_main("A burlesque outfit?", "open", "base", "base", "mid", cheeks="blush")
            m "Yes, this one to be exact..."
            call her_main("*Hmm*... {w=0.4} Well, I must say it's quite creative...", "angry", "narrow", "base", "down", cheeks="blush")
            m "You should see those pasties spin..."
            call her_main("...", "clench", "squint", "base", "mid", cheeks="blush")
            m "How 'bout it?"
            call her_main("Alright fine... Just give me a moment.", "angry", "squint", "base", "R", cheeks="blush")
            call her_main("", "angry", "squint", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("A burlesque outfit?", "angry", "narrow", "base", "down", cheeks="blush")
            call her_main("Strippers wear these, right?", "open", "closed", "base", "mid", cheeks="blush")
            m "Sometimes..."
            call her_main("What do you mean sometimes?", "soft", "narrow", "base", "mid", cheeks="blush")
            m "Put in on and I'll change that answer to a yes..."
            call her_main("How cheeky...{w=0.4} Alright then...", "base", "narrow", "base", "R", cheeks="blush")

    #######################
    ## Ms. Marvel Outfit ##
    #######################
    elif item == her_outfit_msmarv: #Req 10 (top, stockings)
        m "I've got this Cosplay outfit I'd like you to wear."
        if her_whoring < 13:
            call her_main("Cosplay, [genie_name]?", "open", "squint", "base", "mid")
            m "Miss Marvel... One of my favourites!"
            call her_main("*Hmm*... Well I can certainly see why...", "disgust", "narrow", "base", "down", cheeks="blush")
            call her_main("Alright fine...", "open", "closed", "worried", "mid", cheeks="blush")
            call her_main("Just give me a moment to change.", "normal", "base", "base", "R", cheeks="blush")
        elif her_whoring < 22:
            call her_main("Cosplay, [genie_name]?", "angry", "squint", "base", "mid", cheeks="blush")
            m "Yes... A miss Marvel cosplay to be precise."
            call her_main("I see...", "soft", "narrow", "base", "down", cheeks="blush")
            call her_main("And why do you want me to wear this cosplay exactly?", "open", "squint", "base", "R", cheeks="blush")
            m "I believe it would enhance your physical traits."
            call her_main("Sorry?", "annoyed", "squint", "base", "mid")
            m "You heard me..."
            call her_main("*Hmm*... Well, I suppose I could put it on...", "soft", "squint", "base", "R")
            call her_main("One moment please...", "open", "squint", "base", "mid")
            call her_main("", "normal", "squint", "base", "mid")
        else: #22+
            call her_main("Cosplay, [genie_name]?", "base", "squint", "base", "mid")
            m "Yes, this Miss Marvel cosplay..."
            call her_main("*Hmm*... My nipples are sure to poke through in this...", "soft", "narrow", "base", "down", cheeks="blush")
            m "That's the idea..."
            call her_main("Well... I guess it can't be helped...", "open", "closed", "annoyed", "mid", cheeks="blush")
            call her_main("I suppose I'll just... *Ehm*... Suit up...", "open", "squint", "base", "mid", cheeks="blush")
            call her_main("", "base", "squint", "base", "mid", cheeks="blush")

    #################
    ## Tifa Outfit ##
    #################
    elif item == her_outfit_tifa: #Req 10 (top, bottom)
        m "Could you put on this Tifa Cosplay outfit?"
        if her_whoring < 19:
            call her_main("Cosplay, [genie_name]?", "open", "squint", "base", "mid")
            m "Indeed, a Tifa Lockheart cosplay!"
            call her_main("*Hmm*... Can't say I know who that is...", "normal", "squint", "base", "R")
            m "..."
            m "She's from Final Fantasy..."
            call her_main("*Huh*?", "upset", "happy", "base", "mid")
            m "Sorry... I should've been more specific shouldn't I..."
            m "Final Fantasy Seven is the one you'd probably know her from."
            call her_main("*Ehm*...", "clench", "squint", "base", "mid")
            m "Oh... Come on... it was so good it even got a remake!"
            m "And let me tell you... They really did a great job on those assets..."
            call her_main("I don't--", "annoyed", "squint", "base", "mid")
            m "...{w=0.4} Just put it on will you."
            call her_main("Oh-- Okay...", "mad", "squint", "base", "mid")
            call her_main("One moment...", "soft", "squint", "base", "mid")
        else: #19+
            call her_main("A Cosplay outfit...", "base", "squint", "base", "mid")
            m "Indeed, none other than the hottest game babe of 1997!"
            call her_main("I see...", "base", "narrow", "base", "R")
            call her_main("Alright then... Just give me a moment to put it on.", "open", "happy", "base", "mid")

    ##################################
    ## Teddy Outfit (short nightie) ##
    ##################################
    elif item == her_outfit_teddy: #Req 16 (top)
        m "Could you put on this nightgown?"
        if her_whoring < 22:
            call her_main("This is lingerie...", "angry", "base", "base", "down", cheeks="blush")
            m "Indeed it is..."
            call her_main("Isn't this what couples put on to look sexy for their partner?", "mad", "narrow", "base", "mid", cheeks="blush")
            m "I mean..."
            call her_main("Sir... I'm doing this to help--", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "Putting this on will help your house."
            call her_main("How? You're not exactly giving me any points...", "annoyed", "narrow", "base", "mid", cheeks="blush")
            m "No... But it surely aids with the tasks that do..."
            call her_main("...", "disgust", "base", "base", "mid", cheeks="blush")
            call her_main("Alright, fine...", "open", "narrow", "base", "R", cheeks="blush")
            call her_main("Just give me a moment to put it on.", "soft", "narrow", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("Lingerie...", "soft", "narrow", "base", "down", cheeks="blush")
            m "Quite observant of you, [hermione_name]..."
            call her_main("Well I suppose if wearing this helps you build up... *Ehm*...", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "No, do finish that sentence please."
            call her_main("What I meant is... If it means I'll be able to finish my tasks faster...", "annoyed", "squint", "base", "R", cheeks="blush")
            call her_main("Just... I'll just put it on...", "disgust", "squint", "base", "mid", cheeks="blush")
            m "Good plan..."
            call her_main("", "normal", "squint", "base", "mid", cheeks="blush")

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == her_outfit_nightie: #Req 13 (top)
        m "Can you put on this nightie for me?"
        if her_whoring < 19:
            call her_main("This is a nightie is it?", "clench", "narrow", "base", "down", cheeks="blush")
            m "Yep... Completely ordinary nightgown."
            call her_main("Nice try... I can see it's see-through.", "angry", "narrow", "base", "mid", cheeks="blush")
            m "Oh... Isn't that what they're like normally?"
            call her_main("*Sigh*... Whatever... Let's just get this over with...", "normal", "closed", "annoyed", "mid", cheeks="blush")
            call her_main("", "normal", "base", "annoyed", "mid", cheeks="blush")
        elif her_whoring < 22:
            call her_main("A nightie you say?", "open", "squint", "worried", "mid")
            m "Indeed."
            call her_main("*Hmm*... Well I suppose I could wear it...", "normal", "base", "base", "down", cheeks="blush")
            call her_main("Just give me a moment to put it on.", "soft", "base", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("Not much left for the imagination with this one...", "soft", "narrow", "base", "down", cheeks="blush")
            m "I mean... We need you to stay modest, don't we?"
            m "Can't be having you stand around naked, that'd be shameful!"
            call her_main("Right...", "normal", "closed", "worried", "mid", cheeks="blush")
            call her_main("Well I better put it on then...", "open", "closed", "base", "mid", cheeks="blush")
            call her_main("", "base", "base", "base", "mid", cheeks="blush")

    #######################
    ## Latex dress Outfit ##
    #######################
    elif item == her_outfit_latex_dress: #Req 19 (top)
        m "Put on this latex dress for me."
        if her_whoring < 22:
            call her_main("A latex dress?", "open", "squint", "base", "mid", cheeks="blush")
            call her_main("I can't believe you actually want me to wear this...", "soft", "narrow", "base", "R", cheeks="blush")
            call her_main("Fine...{w=0.4} Here it goes...", "open", "closed", "annoyed", "mid", cheeks="blush")
        else: #22+
            call her_main("*Hmm*...", "base", "narrow", "base", "down", cheeks="blush")
            call her_main("And I thought latex gloves were hard to put on...", "open", "closed", "base", "mid", cheeks="blush")
            m "It's worth it if you don't want to get splashed."
            m "Although maybe you don't mind getting splashed by--"
            call her_main("Well...{w=0.4} I suppose I could put it on if you really want me to.", "normal", "squint", "annoyed", "mid", cheeks="blush")
            call her_main("One moment...{w=0.4} *Ehm*...{w=0.4} One minute please.", "open", "narrow", "base", "down", cheeks="blush")

        show screen blkfade
        with d5
        pause .8

        her "Alright... Let's see..."
        her "It's... Quite tight..."
        $ renpy.sound.play("sounds/creaking02.mp3")
        pause 1
        her "How am I even supposed to--"
        $ renpy.sound.play("sounds/creaking02.mp3")
        pause 1
        her "Alright, I think I got it..."
        $ renpy.sound.play("sounds/creaking01.mp3")
        pause 2
        $ renpy.sound.play("sounds/slap_04.mp3")
        her "Ouch!"

        hide screen blkfade
        call her_main("", "angry", "squint", "base", "mid", cheeks="blush")

    #####################
    ## Egyptian Outfit ##
    #####################
    elif item == her_outfit_egypt: #Req 19 (top)
        m "Put on this Egyptian-themed outfit for me will you?"
        if her_whoring < 22:
            call her_main("Why am I suspecting this is not your ordinary--", "open", "closed", "worried", "mid")
            m "Here you go..."
            call her_main("...", "normal", "squint", "base", "down", cheeks="blush")
            call her_main("Why am I not surprised...", "open", "narrow", "base", "mid", cheeks="blush")
            call her_main("Sir, do you actually believe they wear this in Egypt?", "angry", "narrow", "base", "R")
            m "Of course I do... Quite fashionable when I was there."
            m "I even had a pair of those wristbands myself..."
            m "Couldn't force myself to take them off!"
            call her_main("Alright... I guess I'll wear it...", "open", "closed", "worried", "mid")
            call her_main("One moment...", "soft", "squint", "base", "mid")
        else: #22+
            call her_main("Egyptian-themed you say?", "soft", "happy", "base", "mid")
            m "Yeah, this one right here..."
            call her_main("I see...", "normal", "happy", "base", "down", cheeks="blush")
            m "Cleopatra wore this quite proudly I'll have you know..."
            call her_main("Right...", "soft", "closed", "worried", "mid", cheeks="blush")
            call her_main("Well I wouldn't want to displease the great Cleopatra...", "normal", "base", "base", "R")
            call her_main("Hopefully I'll do it justice...", "open", "squint", "base", "mid", cheeks="blush")
            call her_main("One moment please...", "base", "base", "base", "mid", cheeks="blush")

    ##############
    ## Swimsuit ##
    ##############
    elif item == her_outfit_swimsuit: #Req 13 (top)
        m "I've got this swimsuit I'd like you to wear."
        if her_whoring < 22:
            call her_main("A swimsuit...", "open", "squint", "base", "mid")
            call her_main("I guess I could put it on.", "soft", "narrow", "base", "R")
            call her_main("Although, it's a bit weird as I assume I'm not going swimming...", "disgust", "closed", "worried", "mid")
            m "I'm sure we can find a way to get it wet no problem..."
            call her_main("...", "angry", "wide", "base", "mid")
            call her_main("Why I'm not quite sure what you mean by that...", "open", "closed", "base", "mid", cheeks="blush")
            call her_main("But if I'm expected to put it on for the sake of--", "soft", "closed", "base", "mid", cheeks="blush")
            m "Just put it on will you?"
            call her_main("*Ahem*...{w=0.4} Okay then.", "clench", "narrow", "base", "R", cheeks="blush")
            call her_main("Just give me a moment...", "open", "squint", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("A swimsuit...", "open", "base", "base", "R", cheeks="blush")
            call her_main("Are you expecting me to get wet today?", "open", "closed", "base", "mid", cheeks="blush")
            m "Can never be too careful..."
            call her_main("Well... If that's the case then I better put it on...", "open", "narrow", "base", "R", cheeks="blush")

    #####################
    ## Bioshock Outfit ##
    #####################
    elif item == her_outfit_bioshock: #Req 5 (no bra)
        m "Can you put on this Elisabeth Cosplay outfit?"
        if her_whoring < 13:
            call her_main("A cosplay outfit?", "open", "base", "base", "mid")
            m "Yep... Ever heard of her?"
            call her_main("*Hmm*... Can't say that I have.", "upset", "squint", "base", "mid")
            m "She's from a video--"
            call her_main("...", "normal", "narrow", "base", "mid")
            m "I mean... She's a famous, *ugh*... Witch?"
            call her_main("...", "base", "base", "base", "mid")
            m "(Phew, that was close...)"
            call her_main("A corset!", "clench", "wide", "worried", "down")
            m "*Uh-oh*..."
            call her_main("Aren't these supposed to make it really hard to breathe?", "angry", "closed", "base", "mid")
            m "..."
            m "Have you seen your waste-line?"
            m "A corset is hardly going to hinder you from breathing..."
            call her_main("...", "normal", "closed", "base", "mid", cheeks="blush")
            call her_main("I guess that's true.", "open", "happy", "base", "R", cheeks="blush")
            m "Great... So no complaints then?"
            call her_main("*Hmm*... I suppose not...", "angry", "closed", "base", "mid")
            call her_main("...", "normal", "base", "base", "R")
            m "So... Are you putting it on?"
            call her_main("Oh...{w=0.4} Alright...", "angry", "squint", "base", "mid")
            call her_main("", "base", "squint", "base", "mid")
        elif her_whoring < 22:
            call her_main("A cosplay...", "open", "squint", "base", "mid")
            call her_main("*Hmm*... I like the necklace.", "soft", "squint", "base", "L")
            m "I like the corset!"
            call her_main("Of course you do...", "normal", "closed", "base", "mid")
            call her_main("Alright, I suppose I can put it on...", "soft", "base", "base", "R")
            m "Wait a second, they forgot the coin purse!"
            call her_main("*Huh*?", "upset", "squint", "base", "mid")
            m "There's supposed to be a coin purse for you to store silver coins in..."
            call her_main("Oh... So you don't want me to wear it then?", "angry", "squint", "base", "mid")
            m "Of course I do... You'll just have to store the coins in a pocket or something..."
            call her_main("*Hmm*... There doesn't seem to be any pockets...", "upset", "narrow", "base", "down")
            m "Well... I'm sure you'll find somewhere to put them."
            call her_main("Right...", "disgust", "narrow", "base", "down")
            call her_main("Well... Let's see if I can get into this corset to start with...", "angry", "squint", "base", "R", cheeks="blush")
            call her_main("", "base", "squint", "base", "mid")
        else: #22+
            call her_main("A cosplay...", "open", "squint", "base", "mid")
            m "Indeed... And she's quite the popular one as well..."
            m "You should see what zone did with her..."
            call her_main("Who?", "soft", "squint", "base", "mid")
            m "*Err*... I meant, you should see the zone she's--"
            m "What I meant to say was..."
            m "Just... Put it on will you?"
            call her_main("Alright.", "grin", "narrow", "base", "R")
            call her_main("", "base", "squint", "base", "mid")

    #####################
    ## Yennefer Outfit ##
    #####################
    elif item == her_outfit_yennefer: #Req 10
        m "I got this Yennefer Cosplay that I'd like you to put on."
        if her_whoring < 22:
            call her_main("Who?", "normal", "squint", "base", "mid")
            m "*Sigh*...{w=0.4}  Yennefer... {w=0.4} From the witcher."
            call her_main("Oh...{w=0.4}  Her...", "open", "squint", "base", "R")
            call her_main("(No clue who that is but I better not offend him...)", "normal", "narrow", "base", "down")
            m "(I guess she picked Triss.)"
            call her_main("You... Like this Yennefer character then?", "clench", "squint", "base", "mid")
            m "(She did pick Triss!)"
            m "I mean... Shouldn't I?"
            m "(I only did the one playthrough... Maybe Triss was the right choice... Should I have save scummed--)"
            call her_main("*Err*... No you definitely should...", "open", "squint", "base", "R")
            m "..."
            call her_main("...", "clench", "narrow", "base", "L")
            call her_main("I'll just put it on shall I?", "angry", "closed", "base", "mid")
            m "*Err*... Yes... You do that..."
            call her_main("Okay then.", "base", "closed", "base", "down")
            call her_main("", "base", "open", "base", "down")
        else: #22+
            call her_main("This is quite the intricate outfit...", "angry", "narrow", "base", "down")
            m "A Classy outfit for a classy lady."
            call her_main("Oh... Well, thank you...", "base", "closed", "base", "mid", cheeks="blush")
            m "*Huh*?"
            m "Oh... Yes, put it on for me will you?"
            call her_main("As you wish.", "open", "squint", "base", "R", cheeks="blush")
            call her_main("One moment...", "base", "squint", "base", "mid", cheeks="blush")

    ################
    ## Ball Dress ##
    ################
    elif item == her_outfit_ball: #Req 5 (no bra)
        if not ball_quest.E4_complete:
            m "Could you put on this dress?"
            call her_main("*Hmm*... This looks expensive...", "soft", "squint", "base", "down")
            m "I had it custom made!"
            m "(As if my other purchases haven't been...)"
            call her_main("I do like a pearl necklace...", "soft", "narrow", "base", "down")
            m "I knew it... Well, I'm always happy to give you one as long as you don't tell anyone about it."
            m "We wouldn't want anyone to know the headmaster gave a student a pearl necklace, do we?"
            call her_main("Of course.", "open", "closed", "base", "mid")
            call her_main("Well, let's put it on then...", "soft", "happy", "base", "mid")
            call her_main("", "base", "happy", "base", "mid", cheeks="blush")
        else:
            m "What did Hermione Granger say when she got to the ball?"
            call her_main("{size=-4}This dress...{/size}", "soft", "narrow", "base", "down", cheeks="blush")
            m "*Gag* *Cough* *Cough*"
            call her_main("...", "base", "narrow", "base", "down", cheeks="blush")
            m "..."
            m "Well, I thought it was funny..."
            call her_main("...", "base", "narrow", "base", "down", cheeks="blush")
            m "Miss Granger?"
            m "(Looks like she's zoned out...)"
            m "[hermione_name]?"
            call her_main("*Huh*?", "angry", "squint", "base", "mid", cheeks="blush")
            call her_main("Oh... Sorry sir, let me just put it on...", "open", "base", "base", "R", cheeks="blush")
            m "Never mind the dress, what about my joke?"
            call her_main("Sorry?", "soft", "base", "base", "mid", cheeks="blush")
            m "...{w=0.4} Whatever... Just put it on..."
            call her_main("Alright.", "base", "base", "base", "mid", cheeks="blush")

    ##################
    ## Bunny Outfit ##
    ##################
    elif item == her_outfit_bunny: #Req 19 (top, stockings)
        m "I've got this bunny costume I'd like you to wear."
        if her_whoring < 22:
            call her_main("A bunny costume?", "soft", "squint", "base", "mid")
            call her_main("Where do you even get these ideas from?", "angry", "narrow", "base", "stare")
            m "In some junk mail, showing a mansion full of attractive and scantily clad women."
            call her_main("I see...", "soft", "closed", "base", "mid", cheeks="blush")
            call her_main("It does look a little bit tight, but I suppose I'll wear it for you...", "open", "narrow", "base", "down", cheeks="blush")
            g9 "(Hugh success!)" #Like Hugh Hefner
        else: # 22+
            call her_main("A bunny costume?", "open", "base", "base", "mid", cheeks="blush")
            m "I thought we could get it on like rabbits."
            call her_main("*Huh*? Get what on?", "annoyed", "squint", "base", "mid")
            g9 "*Heh-heh*... You know..."
            call her_main("...", "annoyed", "base", "base", "mid")
            call her_main("...", "annoyed", "squint", "base", "stare", cheeks="blush")
            g9 "(She knows...)"
            call her_main("Sir, I'm--", "open", "closed", "base", "mid", cheeks="blush")
            m "Just put the thing on."
            call her_main("Alright...", "open", "narrow", "base", "down", cheeks="blush")

    ###############################
    ## Poker Outfit (token shop) ##
    ###############################
    elif item == her_outfit_poker: #Req 19 (panties, bra)
        m "I spent some tokens getting this outfit for you..."
        if her_whoring < 22:
            call her_main("*Whoa*...", "soft", "narrow", "base", "down", cheeks="blush")
            m "I know... Quite intricate is it not?"
            call her_main("You... you want me to wear this?", "normal", "closed", "base", "mid", cheeks="blush")
            m "I mean, I am a winner after all..."
            call her_main("*Hmm*... I'm not so sure about that...", "soft", "narrow", "base", "R", cheeks="blush")
            m "Sounds like jealousy to--"
            call her_main("...", "normal", "narrow", "base", "mid")
            m "*Ahem*... Just put it on will you?"
            call her_main("...{w=0.4} Fine.", "base", "narrow", "base", "R", cheeks="blush")
        else: #22+
            call her_main("You won this did you?", "open", "narrow", "base", "down")
            m "Indeed."
            call her_main("How do I know you didn't just have it made for me?", "open", "narrow", "base", "mid", cheeks="blush")
            m "You think I'd be able to come up with something like this?"
            call her_main("...", "normal", "narrow", "base", "R", cheeks="blush")
            m "Okay... I probably would..."
            m "You're just going to have to trust me on this one..."
            call her_main("*Hmm*... Well then, it'd be a shame if the prize went to waste...", "base", "narrow", "base", "mid", cheeks="blush")
            call her_main("Just give me a moment to put it on...", "open", "base", "base", "mid", cheeks="blush")

    #################
    ## Maid Outfit ##
    #################
    elif item == her_outfit_maid: #Req 4
        m "Could you put on this maid's outfit?"
        if her_whoring < 13:
            call her_main("You want me to clean your office now too?", "clench", "narrow", "base", "mid")
            m "Well... Let's just have you wear the outfit for now..."
            call her_main("*Ugh*... Maid's outfits are so silly...", "disgust", "narrow", "base", "mid")
            call her_main("Well... Here it goes I guess...", "disgust", "narrow", "base", "R")
        elif her_whoring < 22:
            call her_main("*Hmm*...", "upset", "narrow", "base", "down")
            call her_main("I presume your reason for wanting me to put it on isn't related to cleaning...", "open", "narrow", "base", "mid", cheeks="blush")
            m "I mean..."
            call her_main("Figured...", "open", "closed", "worried", "mid", cheeks="blush")
            call her_main("Oh... Well I guess it can't be helped...", "soft", "narrow", "base", "down", cheeks="blush")
            call her_main("One moment please...", "open", "narrow", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("*Hmm*... Is it one of those \"Sexy\" maid's outfits?", "soft", "narrow", "base", "down", cheeks="blush")
            m "It depends..."
            call her_main("What is that supposed to mean?", "clench", "squint", "base", "mid", cheeks="blush")
            m "It depends on who wears it... I think I'd be able to make a judgement whilst seeing you with it on."
            call her_main("Charmed...{w} Alright, just let me get changed so we can find out...", "base", "narrow", "base", "R", cheeks="blush")
            call her_main("", "base", "squint", "base", "mid", cheeks="blush")

    #########################
    ## Sling Bikini Outfit ##
    #########################
    elif item == her_outfit_bikini3: #Req 17 (panties, bra)
        m "Put on this bikini for me will you."
        call her_main("*Hmm*... A bikini you say?", "normal", "narrow", "base", "R")
        m "Yep, this one right here..."
        call her_main("Right...{w} Why would I even expect something normal...", "angry", "narrow", "base", "down", cheeks="blush")
        m "Looks normal to me..."
        call her_main("It's held up by chains, How is that normal to you?", "disgust", "narrow", "base", "mid", cheeks="blush")
        m "I mean, perhaps you wouldn't see it at the beach exactly..."
        call her_main("Then where would you?", "normal", "narrow", "base", "R", cheeks="blush")
        m "A strip--{w=0.3} I mean... The Vegas strip!"
        call her_main("They wear these on the Vegas strip do they?", "open", "narrow", "annoyed", "mid")
        m "Of course, it's pretty hot there so why wouldn't--"
        call her_main("You're lying...", "open", "closed", "annoyed", "mid")
        g4 "What?!"
        g4 "(She's seen through my clever ruse... Impossible!)"
        call her_main("Give me the real reason why you want me to wear this.", "upset", "base", "annoyed", "mid", cheeks="blush")
        m "*Huh*?"
        call her_main("The \"real\" reason... Or I'm not putting it on...", "angry", "narrow", "base", "mid", cheeks="blush")
        m "The--"
        m "(Hold on... This isn't in the script...)"
        call her_main("I'm waiting...", "annoyed", "closed", "annoyed", "mid", cheeks="blush")
        m "One moment..."
        $ renpy.play("sounds/pageflip.mp3")
        m "(Alright, let's see what's going on here...)"
        $ renpy.play("sounds/pageflip.mp3")
        m "(\"Genie fights Snape using magic... #TODO add explanation to this later...\")"
        m "(That's the tutorial so it must be further in...)"
        $ renpy.play("sounds/pageflipback.mp3")
        pause .4
        m "(Genie fucks Hermione in the Ass...)"
        #TODO Add check if you've not done anal favour
            # m "(Whops... Spoilers..)"
        #else:
            # m "(*Heh-heh*... Why am I not doing this right now exactly?)"
        m "(*Hmm*... I've gone too far... Well... In the script at least.)"
        $ renpy.play("sounds/pageflip.mp3")
        pause .3
        $ renpy.play("sounds/pageflip.mp3")
        pause .3
        $ renpy.play("sounds/pageflip.mp3")
        pause .3
        m "(There we go... The wardrobe section...)"
        call her_main("Still waiting... I'm going to need a real reason soon or I'm not putting it on...", "angry", "closed", "annoyed", "mid", cheeks="blush")
        g9 "(*Aha*! I knew it!)"
        g9 "(Genie comes up with another bullshit reason... Hermione thinks for a moment and then accepts it as the truth!)"
        call her_main("Three...{w=1} Two--", "open", "closed", "annoyed", "mid", cheeks="blush")
        g4 "Wait a minute, the script says--"
        call her_main("One...", "open", "narrow", "annoyed", "mid")
        g4 "*Err*... Your tits would look great in it!"
        call her_main("...{w} Well then...", "base", "narrow", "annoyed", "mid")
        m "(Ah fuck... I can't believe she's done this...)"
        call her_main("In that case--", "open", "closed", "annoyed", "mid")
        $ renpy.play("sounds/magic4.ogg")
        with kissiris
        call her_main("...", "normal", "base", "base", "stare")
        m "What the..."
        call her_main("They wear these on the Vegas strip do they?", "open", "base", "base", "mid", cheeks="blush")
        m "*Huh*?"
        call her_main("*Hmm*... Well I suppose I'll put it on then...", "grin", "closed", "base", "mid", cheeks="blush")
        m "(What just...)"
        m "(*Hmm*... The developers must've patched it...{w=0.4} There's my immersion ruined...)"
        call her_main("Just give me a moment...", "open", "base", "base", "mid", cheeks="blush")
        call her_main("", "base", "base", "base", "mid", cheeks="blush")

    ###########################
    ## Leather Bikini Outfit ##
    ###########################
    elif item == her_outfit_bikini2: #Req 16 (panties, bra)
        m "Put on this bikini for me."
        if her_whoring < 22:
            call her_main("What kind of bikini are we talking about?", "open", "narrow", "base", "mid")
            m "This leather one here."
            call her_main("Right...", "open", "narrow", "base", "down", cheeks="blush")
            call her_main("Well I guess it has some coverage...", "normal", "narrow", "base", "down", cheeks="blush")
            m "I'm sure I could adjust it to be smaller if you'd like."
            call her_main("*Err*... No, it's fine... I'll just put it on as is...", "angry", "closed", "base", "mid", cheeks="blush")
            m "You sure? Just say the word and I'll have it--"
            call her_main("No, we're good. Just give me a moment to put it on.", "open", "squint", "worried", "R", cheeks="blush")
        else: # 22+
            call her_main("A bikini?", "open", "squint", "base", "R", cheeks="blush")
            m "Yep, I've got this leather one for you to wear today."
            call her_main("A leather bikini in the headmasters office...", "base", "narrow", "base", "down", cheeks="blush")
            m "That's right..."
            call her_main("*Hmm*... One moment please...", "open", "squint", "base", "mid", cheeks="blush")


    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == her_outfit_bikini1: #Req 18 (panties, bra)
        m "I've got this bikini for you to wear today."
        call her_main("A bikini?", "open", "base", "base", "mid")
        m "Yep... This one right here."
        call her_main("This is supposed to be a bikini is it?", "open", "narrow", "base", "down", cheeks="blush")
        m "Should fall within that definition, yes."
        call her_main("And here I thought bikini's were supposed to protect your modesty...", "open", "closed", "base", "mid", cheeks="blush")
        m "(Your modesty went out the window a long time ago.)"
        call her_main("Well... I suppose it does cover the important bits...", "soft", "narrow", "base", "down", cheeks="blush")
        m "(Is she trying to convince herself out of it or the other way around?)"
        call her_main("Just give me a moment to put it on, [genie_name]...", "normal", "narrow", "base", "R", cheeks="blush")

    ################################
    ## Pizza Slut Outfit (mirror) ##
    ################################
    elif item == her_outfit_pizza: #Req 19 (top, panties)
        m "Put this pizza on."
        call her_main("Put it--", "annoyed", "squint", "base", "mid")
        call her_main("...", "angry", "squint", "base", "mid")
        call her_main("Where did you even get something like this?", "disgust", "narrow", "base", "mid")
        call her_main("It's not real pizza, right?", "angry", "narrow", "base", "mid")
        m "It materialized from a dream."
        call her_main("It did what from where?", "mad", "happy", "base", "mid")
        m "Yeah, better not question it..."
        call her_main("But sir, conjuring food breaks the laws of transfiguration!", "open", "squint", "base", "mid")
        m "What counts as food, really?"
        call her_main("What?", "disgust", "base", "base", "mid")
        m "If you put it on your body then it's not food... it's clothes."
        m "It's the intention of use that matters..."
        call her_main("I'm not sure that's how it works...", "open", "narrow", "base", "R")
        m "..."
        call her_main("...", "annoyed", "squint", "base", "mid")
        call her_main("Don't question it?", "open", "narrow", "base", "mid")
        m "Don't question it."
        m "Now, are you putting on these clothes for me or what?"
        call her_main("*Hmm*...", "annoyed", "narrow", "base", "down")
        call her_main("I guess I could do it, using a sticking charm...", "angry", "narrow", "base", "R")
        m "What's a stick going to--"
        call her_main("Exposimise!", "scream", "happy", "base", "mid") #TODO add flash effect (needs to go away instantly as well so clothes are changed when it does)
        call her_main("", "normal", "happy", "base", "mid")

    ###################
    ## Ribbon Outfit ##
    ###################
    elif item == her_outfit_ribbon: #Req 18 (bra, panties)
        m "I've got this thing that I'd like you to wrap for me."
        if her_whoring < 22:
            call her_main("Is it me?", "open", "narrow", "base", "mid")
            g4 "When did you become so good at guessing?"
            call her_main("It wasn't exactly hard...", "annoyed", "narrow", "base", "mid")
            g9 "It could be if you put these ribbons on."
            call her_main("*Ugh*...", "disgust", "narrow", "base", "mid")
            call her_main("Alright, fine... Just don't tug at the ends.", "open", "narrow", "base", "R", cheeks="blush")
            g9 "Of course..."
            call her_main("One moment...", "open", "narrow", "base", "mid", cheeks="blush")
        else: # 22+
            call her_main("Alright, let me just take my clothes off...", "angry", "narrow", "base", "R", cheeks="blush")
            g4 "I didn't say it was you!"
            call her_main("It's not?", "clench", "squint", "base", "mid", cheeks="blush")
            m "...{w=0.4} Alright, it is..."
            call her_main("Okay then, just give me a--", "open", "closed", "base", "mid", cheeks="blush")
            m "Wrap it tight!"
            call her_main("Very well...", "open", "squint", "base", "R", cheeks="blush")
    ######################
    ## Christmas Outfit ##
    ######################
    elif item == her_outfit_xmas: #Req 13 (top, bottom)
        m "I'm feeling festive today so could you put on the Christmas outfit?"
        if her_whoring < 22:
            call her_main("A Christmas--", "open", "squint", "base", "mid")
            call her_main("Right...", "soft", "narrow", "base", "down", cheeks="blush")
            m "Specifically designed to jingle some balls."
            call her_main("Charming...", "open", "narrow", "base", "R", cheeks="blush")
            call her_main("Is this really what you imagine a proper Christmas-themed outfit is?", "angry", "narrow", "base", "down", cheeks="blush")
            m "I mean... Mrs Claus probably doesn't wear it... Although she probably should."
            call her_main("Why would I even ask...", "disgust", "closed", "base", "mid", cheeks="blush")
            g9 "Because if she did then Santa would probably come more than once a--"
            call her_main("Fine!", "clench", "narrow", "base", "mid", cheeks="blush")
            g4 "I wasn't finished..."
            call her_main("I'll put it on...", "open", "narrow", "base", "R", cheeks="blush")
            m "But... My joke..."
            call her_main("", "base", "narrow", "base", "mid", cheeks="blush")
        else: #22+
            call her_main("Looks a bit naughty--", "soft", "narrow", "base", "down", cheeks="blush")
            m "Yet I'm sure Santa would put you on the good list if you wore it..."
            call her_main("*Hmm*... I doubt that...", "base", "narrow", "base", "R", cheeks="blush")
            call her_main("Well... I'm doing this to make my house happy so surely it'd even out.", "open", "closed", "base", "mid", cheeks="blush")
            m "I'm sure it will."
            call her_main("Just give me a moment to put it on...", "base", "narrow", "base", "mid", cheeks="blush")

    # TODO: Blacklist fallbacks have to be added.
    return

label her_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Cheerleader Normal ##
    ########################
    if item == her_outfit_cheerleader_1: #Req 10 whoring
        m "Could you wear the cheerleader outfit for me?"

        call her_main("Cheerleader outfit?", "upset", "base", "base", "mid")
        call her_main("Sir, I am not some floosy cheerleader...", "open", "closed", "base", "mid")
        call her_main("Their attire shows way to much skin for my liking...", "open", "squint", "base", "R")
        m "Come on, it's just your stomach..."
        call her_main("Sorry [genie_name] but I'll have to decline...", "normal", "squint", "base", "mid")

    ######################
    ## Cheerleader Lewd ##
    ######################
    elif item == her_outfit_cheerleader_2: #Req 16 whoring (top)
        m "Could you put on the cheerleader outfit for me?"
        if her_whoring < 10:
            call her_main("Cheerleader outfit?", "upset", "base", "base", "mid")
            call her_main("Sir, I am not some floosy cheerleader...", "open", "closed", "base", "mid")
            call her_main("Their attire shows way to much skin for my liking...", "open", "squint", "base", "R")
            m "Come on, surely it's not that bad."
            call her_main("Sorry [genie_name] but I'll have to decline...", "normal", "squint", "base", "mid")
        else: # < 16
            call her_main("Of course!", "smile", "happyCl", "base", "mid")
            call her_main("Go-Go Gryffindor!", "grin", "squint", "base", "mid")
            m "Here you go!"
            call her_main("What on earth...", "clench", "squint", "base", "down")
            call her_main("Sir, this is not the official cheerleading attire!", "angry", "closed", "base", "mid")
            m "Oh... I could've sworn it was..."
            call her_main("I am not wearing this...", "disgust", "base", "base", "R")

    #################
    ## Fishnet Outfit
    #################
    elif item == her_outfit_fishnet: #Req 19 (panties, top)
        m "Could you please wear--"
        if her_whoring < 4:
            call her_main("What? Oh, what's this?", "soft", "squint", "base", "L")
            m "It's a fishnet--"
            call her_main("Oh, I get it!", "open", "wide", "base", "mid")
            call her_main("This isn't really a hobby I considered pursuing, [genie_name]...", "open", "closed", "base", "mid")
            call her_main("But if you say it will help me with my grades then I'll try my best.", "smile", "squint", "base", "mid")
            m "Wait what?"
            call her_main("I will go down to the lake later and try it out, if that's okay with you, [genie_name].", "open", "base", "base", "R")
            m "(...)"
            m "(Wait, does she want to go fishing with it...?)"
        elif her_whoring < 10:
            call her_main("What on earth... This top is so revealing!", "angry", "wide", "angry", "mid")
            g9 "Yes, glad you noticed! Now if you don't mind just--"
            call her_main("I'm not going to wear it! You can see everything in this! My nipples would poke right through it!!!", "scream", "base", "angry", "mid")
            m "I wouldn't mind if they did..."
            call her_main("That's just... typical!", "clench", "base", "angry", "R")
            call her_main("You disgust me, [genie_name]!", "disgust", "base", "angry", "mid")
            m "Alright-- Yeesh... Forget I said anything."
        else: # < 19
            call her_main("A fishnet outfit?", "angry", "happy", "base", "mid")
            m "Indeed!"
            call her_main("I didn't know they made bottoms like this!", "disgust", "base", "base", "down")
            m "They don't usually... I had it made custom just for you!"
            call her_main("You did, did you?", "open", "narrow", "base", "mid")
            m "Yes, so if you could just--"
            if her_whoring < 13:
                call her_main("Well, that's too bad because I won't be wearing it...", "disgust", "base", "base", "R")
            else:
                call her_main("This is practically fetish gear, [genie_name]...", "soft", "happy", "base", "mid")
                m "I mean..."
                call her_main("I am not wearing something like this...", "open", "base", "base", "R", cheeks="blush")

    ##################
    ## Latex Outfit ##
    ##################
    elif item == her_outfit_latex: #Req 19 (top)
        m "Could you put on this latex outfit for me?"
        if her_whoring < 10:
            call her_main("Latex--", "soft", "happy", "base", "mid")
            call her_main("Sir, you can't be serious!", "angry", "wide", "annoyed", "mid")
            m "I'm not hearing a no."
            call her_main("I can't believe I'd even have to--", "clench", "squint", "angry", "mid")
            call her_main("No! I am not putting on this disgusting--", "scream", "closed", "angry", "mid")
            m "Alright, Alright... A simple no would've sufficed..."
            call her_main("...", "disgust", "base", "angry", "mid")
        elif her_whoring < 13:
            call her_main("Latex?", "open", "wide", "base", "mid")
            call her_main("You actually expect me to wear something like this?", "clench", "base", "annoyed", "mid")
            m "I don't see why not. You're perfectly fine being naked."
            call her_main("But this...", "disgust", "narrow", "base", "down")
            call her_main("This would make me look like some cheap--", "disgust", "narrow", "annoyed", "down")
            m "Alright, fine... Don't wear it then..."
        else: # < 19
            call her_main("Latex?", "angry", "squint", "base", "mid")
            call her_main("How do you even put this on?", "disgust", "narrow", "annoyed", "down")
            m "No clue, although I'd assume it's no different to a condom..."
            call her_main("...", "normal", "wide", "base", "mid", cheeks="blush")
            call her_main("Yeah I'm not putting this on...", "open", "closed", "annoyed", "mid", cheeks="blush")
            g4 "Did I say condom? I meant... *Err*..."
            call her_main("...", "upset", "base", "base", "R", cheeks="blush")
            m "Fine... Never mind then..."

    #######################
    ## Slutty Schoolgirl ##
    #######################
    elif item == her_outfit_slutty_schoolgirl: #Req 19 (top, Bottom)
        m "Could you put on this school uniform for me?"
        if her_whoring < 4:
            call her_main("Most certainly... The school uniform is a staple within this institution and I'll wear it with--", "open", "closed", "base", "mid")
            m "Here you go."
            call her_main("Pride...", "normal", "squint", "base", "down")
            call her_main("What have you done?!", "shock", "wide", "base", "mid")
            m "What?"
            call her_main("It's cut all weird... Wait, what's wrong with this skirt?", "clench", "base", "base", "down", cheeks="blush")
            m "You like it?"
            call her_main("What do you mean do I like it?", "scream", "happy", "angry", "mid")
            m "I knew you would--"
            call her_main("You've desecrated our school uniform!", "mad", "base", "angry", "mid")
            g4 "..."
            call her_main("I shall not put on this... this--", "angry", "base", "angry", "down")
            m "Alright fine..."
        elif her_whoring < 13:
            call her_main("Why would you...", "clench", "squint", "base", "down")
            m "What?"
            call her_main("This is...{w=0.4} You've completely ruined our school uniform!", "angry", "happyCl", "angry", "mid")
            g4 "I have?"
            m "Looks like an improvement to me..."
            call her_main("I am not putting this on... It's an insult to our school!", "clench", "base", "angry", "R")
            m "(Looks like I crossed some arbitrary line with this one...)"
        else: # < 19
            call her_main("This...", "angry", "base", "base", "down")
            m "I know it's great isn't it?"
            call her_main("This...", "mad", "narrow", "base", "down")
            call her_main("Why would you do this to our school uniform?", "soft", "closed", "base", "mid")
            call her_main("The students wear this with pride... It's a staple of our great institution.", "normal", "squint", "base", "mid", cheeks="blush")
            call her_main("And you've turned it into--", "upset", "narrow", "base", "down", cheeks="blush")
            g9 "I know... Quite an improvement, isn't it?"
            call her_main("I'm sorry but I am not putting this on, [genie_name]...", "open", "closed", "base", "mid")
            m "Suit yourself..."

    ##################
    ## Witch Outfit ##
    ##################
    elif item == her_outfit_witch: #Req 10 (top)
        m "Put on this witch outfit for me will you?"
        call her_main("A witch outfit?", "soft", "base", "base", "mid")
        call her_main("Sir, I'm not sure...", "open", "squint", "base", "R")
        call her_main("As a muggle born, I usually only wear casual muggle wear when the school uniform doesn't suffice.", "normal", "squint", "base", "mid")
        m "Perhaps it's time to widen your wardrobe selection then."
        if her_whoring < 4:
            call her_main("I refuse!", "open", "closed", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")
        else: # < 10
            call her_main("*Hmm*... If you say so...", "normal", "squint", "base", "mid")
            m "Excellent, here you go..."
            call her_main("What on earth is this!?", "clench", "squint", "worried", "down")
            m "A witch outfit?"
            call her_main("This looks like what some muggle bimbo would put on at Halloween...", "angry", "narrow", "base", "mid")
            m "Excellent! So, since it's muggle wear I assume you'd feel more comfortable putting it--"
            call her_main("...", "disgust", "narrow", "base", "mid")
            call her_main("Did you not hear what I just said?", "open", "happyCl", "annoyed", "mid")
            m "You usually only wear casual muggle wear when the school uniform--"
            call her_main("Yes, but I said this looks like some slutified Halloween outfit!", "angry", "squint", "angry", "mid")
            m "*He-heh*... Slutified..."
            call her_main("I am not wearing it...", "upset", "base", "annoyed", "mid")

    #######################
    ## Lara Croft Outfit ##
    #######################
    elif item == her_outfit_croft: #Req 10 (top, bottom)
        m "Could you put on this archaeologist outfit for me?"
        call her_main("A what?", "soft", "squint", "base", "mid")
        m "This one..."
        if her_whoring < 4:
            call her_main("What is this?!", "open", "wide", "base", "down")
            m "An archaeologist outfit?"
            m "Well at least it's an artist representation of what one might look like."
            call her_main("What kind of archaeologist would be wearing something like this?", "clench", "squint", "annoyed", "mid")
            m "Why none other than the great Lara Croft!"
            call her_main("Who?", "disgust", "squint", "base", "mid")
            m "Lara Croft! The worlds most famous Archaeologist!"
            call her_main("What kind of archaeologist is she to be wearing this?", "normal", "slit", "base", "mid")
            m "The kind that delves into ancient temples looking for rare artefacts!"
            call her_main("Well I must say that attire such as this is hardly necessary to--", "open", "closed", "annoyed", "mid")
            m "I'll have you know that she's an expert in her field!"
            m "I've experienced her... *Err*... expertise in taking care of delicate and ancient artefacts first hand!"
            call her_main("Oh, sorry [genie_name]!", "mad", "squint", "base", "mid")
            call her_main("I meant no disrespect, I'd just rather wear something a bit more...", "upset", "squint", "base", "R")
            call her_main("*Ehm*...", "clench", "base", "base", "mid", cheeks="blush")
            m "Whatever you say, [hermione_name]."
        else: # < 10
            call her_main("Hmm... When I think of an archaeologist outfit I don't think of something so...", "soft", "base", "worried", "down")
            m "Triangular?"
            call her_main("No, I was going to say revealing...", "disgust", "squint", "base", "mid")
            m "It's not \"that\" revealing..."
            m "It had to look that way, because... *Err*... She explores volcanoes and stuff..."
            call her_main("...", "disgust", "narrow", "base", "mid")
            m "Limitations of the engine..."
            call her_main("The what?", "upset", "base", "worried", "mid")
            m "Never mind... Forget it..."

    #######################
    ## Heart Slut Outfit ##
    #######################
    elif item == her_outfit_hslut: #Req 19 (top, panties, bra)
        m "Put on this burlesque outfit for me will you?"
        if her_whoring < 4:
            call her_main("A what?", "clench", "wide", "worried", "mid")
            m "Burlesque outfit, it's--"
            call her_main("What the hell is wrong with you?", "mad", "base", "angry", "mid")
            m "What do you mean?"
            call her_main("Just look at it!", "scream", "base", "angry", "mid", cheeks="blush")
            call her_main("What are these heart things even supposed to be?", "clench", "base", "annoyed", "down", cheeks="blush")
            m "Oh, they're called pasties. They go on the top of your nipples."
            call her_main("...", "disgust", "squint", "worried", "stare", cheeks="blush")
            m "You see, if you move your breasts in a circulation motion these little things spin around."
            with hpunch
            call her_main("What?!", "shock", "wide", "angry", "mid", cheeks="blush")
            g9 "I know!"
            g9 "Pretty clever, right?"
            call her_main("Sir, how could you ask me to wear something like this?!", "angry", "happy", "angry", "R", cheeks="blush")
            call her_main("I am not putting this on...", "clench", "narrow", "annoyed", "mid", cheeks="blush")
        elif her_whoring < 13:
            call her_main("Burlesque--", "clench", "base", "base", "mid", cheeks="blush")
            call her_main("My word!", "soft", "base", "annoyed", "down", cheeks="blush")
            m "A piece of art is it not?"
            call her_main("You're expecting me to wear this?", "clench", "wide", "base", "mid", cheeks="blush")
            m "Heck yes!"
            call her_main("Well you can take that expectation and.... and...", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "And what?"
            call her_main("I am not wearing this for you...", "clench", "closed", "base", "mid", cheeks="blush")
            call her_main("", "normal", "base", "base", "mid", cheeks="blush")
        else: # < 19
            call her_main("A Burlesque outfit?", "normal", "squint", "base", "mid", cheeks="blush")
            m "Indeed... And it's got heart shaped pasties and everything!"
            call her_main("...", "normal", "base", "base", "down", cheeks="blush")
            call her_main("You actually want me to put this on?", "open", "squint", "base", "mid", cheeks="blush")
            m "..."
            call her_main("Of course you do... Why'd I even ask...", "normal", "narrow", "base", "R", cheeks="blush")
            call her_main("But... Isn't this what strippers wear, [genie_name]?", "open", "closed", "worried", "mid", cheeks="blush")
            m "Well, some do... on occasion. I guess it depends..."
            call her_main("... [genie_name], I'm not a stripper...", "disgust", "squint", "base", "mid", cheeks="blush")
            m "Sure could've fooled me..."
            call her_main("I only did that because you paid...", "open", "closed", "base", "mid", cheeks="blush")
            m "Go on..."
            call her_main("I'm sorry sir but it's too much...", "angry", "squint", "base", "mid", cheeks="blush")
            m "(You're in denial [hermione_name]... Well, I'm sure she'll come around soon enough.)"

    #######################
    ## Ms. Marvel Outfit ##
    #######################
    elif item == her_outfit_msmarv: #Req 10 (top, stockings)
        m "I've got this Cosplay outfit I'd like you to wear."
        if her_whoring < 4:
            call her_main("Cosplay, [genie_name]?", "clench", "base", "worried", "mid")
            m "Indeed... It's a Miss--"
            call her_main("I am not wearing it...", "open", "closed", "annoyed", "mid")
            m "What? Why not?"
            call her_main("Are you actually expecting me to put on a cosplay outfit for you?", "angry", "base", "annoyed", "mid")
            m "I mean..."
            call her_main("I'll stick to normal clothing thank you very much...", "open", "base", "annoyed", "R")
        else: # < 10
            call her_main("Cosplay outfit, [genie_name]?", "normal", "base", "worried", "mid")
            m "Indeed... It's a Ms Marvel cosplay."
            call her_main("*Hmm*... Can't say that I know it...", "upset", "squint", "base", "R")
            m "Here you go..."
            call her_main("Oh My... This thing is skin tight...", "open", "wide", "worried", "down")
            m "Not too unusual for cosplay..."
            call her_main("I can't put this thing on...", "clench", "squint", "worried", "mid")
            m "Oh come on... Just use some powder and I'm sure it'll slip right--"
            call her_main("I \"won't\" put this thing on...", "angry", "base", "annoyed", "mid")
            m "... Just say so then..."
            call her_main("...", "angry", "base", "base", "R")

    #################
    ## Tifa Outfit ##
    #################
    elif item == her_outfit_tifa: #Req 10 (top, bottom)
        m "Could you put on this Tifa Cosplay outfit?"
        if her_whoring < 4:
            call her_main("Cosplay, [genie_name]?", "clench", "base", "worried", "mid")
            m "Indeed!"
            call her_main("I am not wearing it...", "open", "closed", "annoyed", "mid")
            m "What? Why not?"
            call her_main("Are you actually expecting me to put on a cosplay outfit for you?", "angry", "base", "annoyed", "mid")
            m "I mean..."
            call her_main("I'll stick to normal clothing thank you very much...", "open", "base", "annoyed", "R")
        else: # < 10
            call her_main("What's a Tifa, [genie_name]?", "soft", "base", "base", "mid")
            m "What's a-- Who doesn't know--"
            m "Tifa Lockheart!"
            call her_main("Who?", "upset", "squint", "worried", "mid")
            m "*sigh*... I can't believe it..."
            call her_main("Is that a relative of Gilderoy Lockhart?", "open", "squint", "base", "mid")
            m "*Huh*?"
            call her_main("Gilderoy... One of the teachers...", "angry", "squint", "base", "mid")
            m "No idea who you're talking about..."
            call her_main("...", "disgust", "closed", "worried", "mid")
            m "Are you putting it on or what?"
            call her_main("*Err*... It's a bit revealing...", "disgust", "narrow", "worried", "down")
            m "Come on, it's only your stomach..."
            call her_main("That's not what I'm referring to...", "angry", "narrow", "base", "R")
            m "Alright fine... Don't wear it then..."

    ##################################
    ## Teddy Outfit (short nightie) ##
    ##################################
    elif item == her_outfit_teddy: #Req 16 (top)
        m "Could you put on this nightgown?"
        if her_whoring < 4:
            call her_main("This... This is completely transparent!", "clench", "squint", "annoyed", "down")
            m "Oh come on, it's hardly even translucent."
            call her_main("I can see the wrinkles on your hand through it...", "disgust", "squint", "angry", "mid")
            m "That's just the folds of the fabric."
            call her_main("I am not wearing this...", "angry", "base", "angry", "mid")
        elif her_whoring < 13:
            call her_main("*Ehm*... Isn't a nightgown supposed to...", "disgust", "narrow", "base", "down")
            m "Supposed to what, [hermione_name]?"
            call her_main("You know...", "clench", "narrow", "base", "down")
            call her_main("Cover your body.", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "Isn't it?"
            call her_main("It barely covers anything...", "upset", "narrow", "base", "mid")
            call her_main("And what it does cover is almost completely see-through.", "open", "squint", "annoyed", "mid")
            m "I mean, it's lingerie, that's what--"
            call her_main("I am not wearing it...", "mad", "squint", "base", "mid")
            m "..."
        else: # < 16
            call her_main("*Err*... You want me to wear lingerie?", "open", "base", "base", "R", cheeks="blush")
            m "Yes."
            call her_main("Can I ask you why?", "normal", "squint", "base", "mid", cheeks="blush")
            m "Don't you want to look sexy for me?"
            call her_main("For you-- Sir, that is not why I'm doing this...", "clench", "closed", "base", "mid", cheeks="blush")
            m "Did I say for me? I meant--"
            call her_main("Too late...", "angry", "base", "annoyed", "R", cheeks="blush")
            m "(Damn...)"

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == her_outfit_nightie: #Req 13 (top)
        m "Can you put on this nightie for me?"
        if her_whoring < 4:
            call her_main("What is this?!", "angry", "base", "annoyed", "down")
            m "A nightie?"
            call her_main("It's see-through!", "scream", "squint", "base", "mid")
            m "Oh... Is it? I didn't \"see\" that."
            call her_main("I am not putting that on...", "mad", "narrow", "angry", "mid")
        else: # < 13
            call her_main("What's supposed to make this piece of garment a nightie exactly?", "angry", "narrow", "base", "down")
            m "Well... It's a thin soft material that you put on at night."
            call her_main("Isn't a nightie meant to cover you?", "normal", "narrow", "annoyed", "mid")
            m "I mean it sort of does..."
            call her_main("...", "disgust", "closed", "annoyed", "mid")
            call her_main("Yeah, I'm going to have to decline on this one...", "clench", "closed", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

    #######################
    ## Latex dress Outfit ##
    #######################
    elif item == her_outfit_latex_dress: #Req 19 (top)
        m "Put on this latex dress for me."
        if her_whoring < 4:
            call her_main("Latex dress?", "angry", "squint", "base", "stare")
            call her_main("I didn't know you could make a dress out of--", "open", "squint", "worried", "mid")
            m "Here you go."
            call her_main("Are you crazy?!", "clench", "wide", "base", "down")
            call her_main("What's wrong with you, [genie_name]?!", "scream", "squint", "annoyed", "mid")
            m "What do you--"
            call her_main("I am not putting that thing on...", "disgust", "happyCl", "base", "mid", cheeks="blush")
        elif her_whoring < 13:
            call her_main("Latex dress?", "angry", "narrow", "base", "stare")
            m "This one."
            call her_main("This...", "clench", "squint", "base", "down")
            m "Pretty unique isn't it?"
            call her_main("This looks like someone ripped an oversized balloon.", "disgust", "squint", "annoyed", "mid")
            m "Baloon? I was going to say it looks more like a--"
            call her_main("... {w} Like a what?", "angry", "squint", "annoyed", "mid")
            m "Never mind..."
            m "So will you wear--"
            call her_main("No!", "scream", "closed", "annoyed", "mid")
            call her_main("", "normal", "squint", "annoyed", "mid")
        else: # < 19
            call her_main("[genie_name], this is fetish gear isn't it?", "annoyed", "base", "base", "R", cheeks="blush")
            m "I mean..."
            m "I wouldn't exactly call it..."
            m "..."
            m "From a certain point of view, maybe..."
            m "..."
            m "Yeah okay, I got nothing..."
            call her_main("I am not putting this on...", "open", "closed", "base", "mid", cheeks="blush")
            call her_main("", "normal", "base", "base", "mid", cheeks="blush")

    #####################
    ## Egyptian Outfit ##
    #####################
    elif item == her_outfit_egypt: #Req 19 (top)
        m "Put on this Egyptian-themed outfit for me will you?"
        if her_whoring < 13:
            call her_main("Egyptian-themed? What's that supposed to mean?", "upset", "squint", "worried", "mid")
            m "You know... The type of clothing that they'd wear in Egypt."
            m "Well at least back when I was there."
            call her_main("You've been to Egypt, [genie_name]?", "soft", "squint", "base", "mid")
            m "Of course!"
            m "And let me tell you... Cleopatra was quite the sight to behold!"
            call her_main("Did you see a bust of her there?", "base", "base", "worried", "mid")
            m "Quite a bit more than just her bust."
            call her_main("A statue?", "open", "base", "base", "mid")
            m "A what? No, I've met-- I mean... Yes, I saw a statue of her!"
            call her_main("I see... Well, let me have a look...", "base", "squint", "base", "mid")
            m "Here you go."
            call her_main("What the--", "normal", "wide", "base", "down")
            call her_main("Surely this can't be what they wore, [genie_name]!", "clench", "base", "base", "down")
            m "Oh, I'm quite certain they did..."
            call her_main("There's barely any material to cover... *Ehm*...", "disgust", "squint", "base", "mid", cheeks="blush")
            m "I mean, it's quite hot there..."
            call her_main("Sorry sir, but this-- I can't-- No offence but--", "disgust", "squint", "base", "R", cheeks="blush")
            m "Alright... fine."
        else: # < 19
            call her_main("Egyptian-themed?", "soft", "squint", "worried", "mid")
            m "Yeah, this one."
            call her_main("Sir... I thought Egyptians covered their skin from the sun...", "upset", "narrow", "base", "mid")
            m "Poppycock."
            m "If you did then you wouldn't be able to get an even tan."
            call her_main("...", "disgust", "narrow", "base", "mid")
            call her_main("Sorry [genie_name] but this is too much...", "open", "closed", "annoyed", "mid")
            call her_main("", "normal", "base", "annoyed", "mid")

    ##############
    ## Swimsuit ##
    ##############
    elif item == her_outfit_swimsuit: #Req 13 (top)
        m "I've got this swimsuit I'd like you to wear."
        if her_whoring < 4:
            call her_main("A swimsuit?", "angry", "happy", "base", "mid")
            call her_main("Am I expected to go swimming with you?", "clench", "squint", "base", "mid")
            m "I just thought you'd look good in one."
            call her_main("What?!", "clench", "squint", "worried", "mid")
            call her_main("You want me to wear it in here?", "disgust", "squint", "base", "mid")
            m "Yes, I'd like you to put it on for when you're--"
            call her_main("Why would I stand around in a swimsuit in your office?", "angry", "happy", "annoyed", "mid")
            m "As I said, I think you'd look good in it..."
            call her_main("Well, your opinion on how I'd look isn't going to convince me to put on a swimsuit in here...", "angry", "squint", "base", "R")
        else: # < 13
            call her_main("*Err*... You want me to put on a swimsuit in your office?", "angry", "squint", "base", "mid")
            m "Yes."
            call her_main("Wouldn't that be kind of weird?", "clench", "narrow", "base", "mid")
            m "I don't see why it would..."
            call her_main("I mean... There's not really a pool or anything in here...", "disgust", "base", "worried", "L")
            m "Yeah... No complimentary chocolate either."
            call her_main("*Huh*?", "upset", "squint", "base", "mid")
            m "Never mind..."
            m "Would you put it on if there was a pool in here?"
            call her_main("*Ehm*... Maybe?", "angry", "squint", "base", "mid")
            m "(*Hmm*... Now where would I fit a pool?)"
            m "(Perhaps it'd be easier just to try and convince her some other time...)"

    #####################
    ## Bioshock Outfit ##
    #####################
    elif item == her_outfit_bioshock: #Req 5 (no bra)
        m "Can you put on this Elisabeth Cosplay outfit?"
        call her_main("Cosplay, [genie_name]?", "clench", "base", "worried", "mid")
        m "Indeed!"
        call her_main("I am not wearing it...", "open", "closed", "annoyed", "mid")
        g4 "What? Why not?"
        call her_main("Firstly... Why would I put on a cosplay outfit in your office?", "angry", "base", "annoyed", "mid")
        m "I mean..."
        call her_main("Secondly... There's not even a bra for this... Cosplay.", "open", "closed", "annoyed", "mid")
        m "There's a corset though... Surely--"
        call her_main("I'll stick to normal clothing thank you very much...", "open", "base", "annoyed", "R")

    #####################
    ## Yennefer Outfit ##
    #####################
    elif item == her_outfit_yennefer: #Req 10
        m "I got this Yennefer Cosplay that I'd like you to put on."
        if her_whoring < 4:
            call her_main("Cosplay, [genie_name]?", "clench", "base", "worried", "mid")
            m "Yep, she's from the--"
            call her_main("I am not wearing it...", "open", "closed", "annoyed", "mid")
            g4 "You didn't even let me finish!"
            call her_main("I am not putting on some random cosplay for you...", "open", "narrow", "annoyed", "mid")
            m "Whatever... I picked Triss anyway."
            call her_main("What?", "soft", "squint", "base", "mid")
            m "Alright, I didn't..."
        else: # < 10
            call her_main("A Cosplay?", "normal", "base", "base", "mid")
            m "Yep, Yennefer from the Witcher."
            call her_main("A witch?", "soft", "squint", "base", "mid")
            call her_main("Well, I suppose I could--", "open", "closed", "base", "mid")
            m "That's kind of offensive actually."
            call her_main("*Huh*?", "clench", "squint", "base", "mid")
            m "She's a sorceress, not a witch."
            call her_main("I see...", "angry", "narrow", "base", "R")
            call her_main("(What is he even talking about...)", "angry", "narrow", "base", "down")
            m "You better make up for what you just said by wearing this for me..."
            call her_main("What?", "angry", "squint", "base", "mid")
            m "Calling her a witch... Witches are usually old women or hags you know."
            call her_main("Sir...", "disgust", "base", "worried", "mid")
            m "Yes?"
            call her_main("I'm a witch!", "angry", "base", "annoyed", "mid")
            g4 "But the video ga-- I mean books... Yes, I've read them you know!"
            call her_main("...", "annoyed", "base", "annoyed", "mid")
            m "Okay I didn't..."
            call her_main("Sir, do I have to wear this?", "open", "closed", "annoyed", "mid")
            m "No... I don't deserve it..."
            call her_main("...", "normal", "narrow", "base", "mid")
            m "Don't look at me!"

    ################
    ## Ball Dress ##
    ################
    elif item == her_outfit_ball: #Req 5 (no bra)
        m "Could you put on this dress?"
        call her_main("Sir, this dress has no...{w=0.4} *Ehm*...{w=0.4} Support.", "disgust", "narrow", "base", "down")
        m "Sorry?"
        call her_main("You know...", "clench", "narrow", "worried", "R")
        m "Oh... I see..."
        m "Well your breasts should do shouldn't they?"
        call her_main("What?!", "angry", "wide", "base", "mid")
        call her_main("Sir, I'm not putting on some dress without my bra...", "angry", "squint", "annoyed", "mid")
        m "Why not?"
        m "It's all covered, isn't it?"
        call her_main("Yes, but--", "mad", "closed", "base", "mid")
        call her_main("Why am I explaining myself to you?", "soft", "happyCl", "annoyed", "mid")
        call her_main("I am not wearing it...", "normal", "squint", "annoyed", "mid")

    ##################
    ## Bunny Outfit ##
    ##################
    elif item == her_outfit_bunny: #Req 19 (top, stockings)
        m "I've got this bunny costume I'd like you to wear."
        if her_whoring < 4:
            call her_main("A what?!", "disgust", "wide", "base", "mid")
            m "A Bunny costume."
            call her_main("Why would you even own such a thing?", "open", "squint", "annoyed", "mid")
            m "Own? I bought it for you, of course!"
            call her_main("You bought me a bunny costume?", "angry", "narrow", "annoyed", "mid")
            m "...{w=0.4} No?"
            m "It's just a prank, bro! {w=0.3} *Err*....{w=0.3} No!{w=0.3} Snape dared me to try and make you wear it!"
            call her_main("Professor Snape did?", "upset", "squint", "annoyed", "mid")
            m "...{w=0.4} Yes?"
            call her_main("Well, that kind of humour is very much like him...", "soft", "squint", "annoyed", "R")
            m "(When in doubt, blame Snape!)"
        elif her_whoring < 13:
            call her_main("*Err*... You're joking right?", "clench", "narrow", "base", "mid")
            call her_main("Surely you don't expect me to put on something so--", "open", "closed", "annoyed", "mid")
            m "*Hah-Ha*... Yeah, I'm a bit of a hop-timist sometimes!"
            call her_main("What?", "clench", "squint", "base", "mid")
            m "*Heh*...{w=0.3} Never mind."
        else: # < 19
            call her_main("*Ehm*...", "annoyed", "squint", "base", "R", cheeks="blush")
            call her_main("It's a bit much, don't you think?", "disgust", "narrow", "base", "down", cheeks="blush")
            m "Don't be silly... Just hop right into it."
            call her_main("*Hmm*... I think I'll pass.", "angry", "closed", "base", "mid", cheeks="blush")
            call her_main("", "normal", "squint", "base", "R", cheeks="blush")

    ###############################
    ## Poker Outfit (token shop) ##
    ###############################
    elif item == her_outfit_poker: #Req 19 (panties, bra)
        m "I spent some tokens getting this outfit for you..."
        if her_whoring < 4:
            call her_main("And you're expecting me to just wear this thing because you've won it?", "open", "narrow", "annoyed", "mid")
            call her_main("(Does he think he can play me like he plays games?)", "clench", "narrow", "base", "R")
            g4 "But, I won... fair and square..."
            call her_main("Well, I'm not some prize for you to win in a game...", "open", "narrow", "annoyed", "mid")
            m "Actually--"
            call her_main("...", "normal", "base", "annoyed", "mid")
            m "Alright... Never mind then..."
        elif her_whoring < 13:
            call her_main("And you winning it means that I'm supposed to wear it?", "angry", "narrow", "annoyed", "mid")
            m "Pretty sure that's how it works."
            call her_main("*Hmm*... I don't think so...", "disgust", "narrow", "annoyed", "R")
            call her_main("You may be a winner [genie_name] but that sure doesn't give you some privilege to make me wear--", "open", "closed", "annoyed", "mid")
            call her_main("Whatever this...{w=0.4} Thing... Is supposed to be.", "angry", "narrow", "annoyed", "mid")
            m "(Damn it...)"
        else: # < 19
            call her_main("*Err*... Am I supposed to be some kind of prize for you winning games?", "clench", "narrow", "base", "R")
            m "I mean, this outfit was practically made for you..."
            call her_main("...", "normal", "narrow", "base", "mid", cheeks="blush")
            m "Come on... Surely you can't resist basking in my glory."
            call her_main("...", "normal", "narrow", "base", "mid")
            call her_main("Well, I'm sorry but looks to me as if you spent your hard earned tokens on a piece of fabric.", "open", "narrow", "base", "R")
            m "..."
            m "(Guess even a smidge of my fame is too much for her...)"

    #################
    ## Maid Outfit ##
    #################
    elif item == her_outfit_maid: #Req 4
        m "Could you put on this maid's outfit?"
        call her_main("A maid's outfit?", "upset", "squint", "base", "mid")
        call her_main("Isn't cleaning part of the house elves job?", "open", "closed", "annoyed", "mid")
        call her_main("(Not that I approve of this horrible house elf enslavement...)", "annoyed", "closed", "annoyed", "mid")
        m "I mean, I'd be fine if you just--"
        call her_main("I have no time to clean up your mess, you'll have to do that yourself...", "open", "happy", "annoyed", "mid")
        m "(I don't think there's enough tissues in this world for that.)"
        m "Very well, Miss Granger..."

    #########################
    ## Sling Bikini Outfit ##
    #########################
    elif item == her_outfit_bikini3: #Req 17 (panties, bra)
        m "Put on this bikini for me will you."
        if her_whoring < 4:
            call her_main("A bikini?!", "shock", "wide", "base", "mid")
            g9 "Wow, excited much?"
            g9 "Well then, here you go!"
            call her_main("Sir!", "clench", "wide", "base", "down")
            call her_main("What are these chains?!", "angry", "wide", "base", "down")
            m "Oh, those!"
            m "They are the straps I believe."
            m "Pretty cool, right?"
            call her_main("Cool?!", "angry", "wide", "angry", "mid")
            m "Is that not how you say it anymore?"
            m "I'm not really up to date with the \"lingo\" these days."
            call her_main("Are you crazy?!", "scream", "squint", "annoyed", "mid")
            m "I mean... at least I didn't say \"Tubular\"."
            call her_main("Asking me to wear a normal bikini is bad enough, but this...", "disgust", "closed", "angry", "mid")
            m "*Huh*? Looks pretty normal to me... From where I'm from--"
            g4 "I mean--"
            call her_main("Then you probably need to get your eyes checked...", "angry", "base", "angry", "mid")
            call her_main("Because this bikini you got me would surely never be an appropriate--", "angry", "base", "angry", "R")
            m "Fine... Whatever..."
        elif her_whoring < 13:
            call her_main("A bikini?", "disgust", "squint", "base", "mid")
            m "Indeed... This one right here..."
            call her_main("...", "normal", "wide", "base", "down")
            call her_main("[genie_name], You can't be serious!", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "About what? It's a bikini is it not?"
            call her_main("These straps are made of chains! Surely that wouldn't even help to keep them on...", "angry", "narrow", "annoyed", "down", cheeks="blush")
            m "I'm sure you'll find a way..."
            call her_main("I won't!", "scream", "closed", "annoyed", "mid")
            m "Don't put yourself down like that... I'm sure some spell would--"
            call her_main("I won't, because I'm not putting it on...", "angry", "narrow", "angry", "mid")
            m "Oh...{w=0.4} Right..."
        else: # < 17
            call her_main("A bikini?", "base", "base", "base", "mid")
            call her_main("Well, I suppose that wouldn't be too--", "base", "base", "base", "mid")
            m "This one..."
            call her_main("That one?", "base", "base", "base", "mid")
            call her_main("Sir, are you sure this is...", "base", "base", "base", "mid")
            m "Yes?"
            call her_main("*Ehm*... I mean it looks a bit...", "base", "base", "base", "mid")
            m "A bit what?"
            call her_main("*Ehm*...", "base", "base", "base", "mid")
            m "Come on, it's not that bad... Just put it on."
            call her_main("I...{w} No, I'm sorry... It's too much...", "base", "base", "base", "mid")

    ###########################
    ## Leather Bikini Outfit ##
    ###########################
    elif item == her_outfit_bikini2: #Req 16 (panties, bra)
        m "Put on this bikini for me."
        if her_whoring < 4:
            call her_main("For you?!", "disgust", "base", "annoyed", "mid")
            m "Yes?"
            call her_main("Sir, I'm not some doll for you to dress up!", "scream", "closed", "annoyed", "mid")
            call her_main("Especially not in something like a bikini!", "angry", "narrow", "angry", "mid")
            m "(She's not? Then what the fuck is this wardrobe UI for?)"
            m "My mistake I guess..."
        else: # < 16
            call her_main("You want me to put on a bikini?", "upset", "squint", "base", "mid", cheeks="blush")
            m "Yeah, this leather one."
            call her_main("A leather bikini?!?", "clench", "narrow", "base", "down", cheeks="blush")
            m "I'm sure it's not real leather..."
            call her_main("That... That's not the point!", "open", "closed", "worried", "mid", cheeks="blush")
            m "Oh... I'm sorry, it usually is with this type of thing..."
            call her_main("You actually expect me to--", "angry", "squint", "base", "mid", cheeks="blush")
            m "I didn't ship it from anywhere, it's made locally."
            call her_main("[genie_name], I don't care about where you got it from... It's the fact that--", "angry", "narrow", "worried", "mid", cheeks="blush")
            m "Jeez, perhaps you need to take a good look at yourself then."
            call her_main("What?", "clench", "squint", "base", "mid", cheeks="blush")
            m "Spending a bit more is worth it if it supports your local community."
            call her_main("...", "disgust", "squint", "base", "mid")
            m "Stimulating the economy and all that stuff..."
            if her_whoring < 13:
                call her_main("I'm not wearing it for the fact that it's a bikini... It's weird...", "annoyed", "squint", "base", "R", cheeks="blush")
                g9 "(*Heh-heh*... Stimulating...)"
                m "Anyway, so you're putting it on or what?"
                call her_main("I am not...", "normal", "narrow", "base", "mid", cheeks="blush")
            else: # < 16:
                call her_main("I don't want to put on a bikini in your office.", "open", "closed", "base", "mid", cheeks="blush")
                call her_main("Standing in my underwear is weird enough...", "annoyed", "squint", "base", "R", cheeks="blush")
                m "Whatever you say [hermione_name]..."

    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == her_outfit_bikini1: #Req 18 (panties, bra)
        m "I've got this bikini for you to wear today."
        if her_whoring < 4:
            call her_main("A bikini?!", "clench", "wide", "worried", "mid")
            m "Yep, this one right here."
            call her_main("...", "angry", "squint", "base", "down")
            m "Pretty neat, isn't it?"
            call her_main("Where's the rest of it?!", "disgust", "wide", "base", "mid", cheeks="blush")
            m "What do you mean the rest? Isn't a bikini supposed to only come in two pieces?"
            call her_main("Isn't a bikini supposed to-- Oh... I don't know...", "angry", "squint", "annoyed", "mid", cheeks="blush")
            with hpunch
            call her_main("Cover your privates?!", "scream", "closed", "annoyed", "mid", cheeks="blush")
            m "Doesn't it do that?"
            call her_main("There's barely any fabric to cover anything!", "disgust", "base", "annoyed", "mid", cheeks="blush")
            m "Very environmentally friendly isn't it?"
            call her_main("I am not wearing this...", "mad", "base", "annoyed", "mid", cheeks="blush")
        elif her_whoring < 13:
            call her_main("A bikini?", "clench", "squint", "worried", "mid", cheeks="blush")
            m "This one..."
            call her_main("That... That one?!", "angry", "squint", "base", "down", cheeks="blush")
            m "Yep... Now, if you could just--"
            call her_main("I am not wearing this...", "disgust", "narrow", "base", "mid", cheeks="blush")
            g4 "Why not?!"
            call her_main("What do you think?", "angry", "base", "annoyed", "mid", cheeks="blush")
            m "Oh... I see..."
            call her_main("Finally, you get it...", "open", "closed", "annoyed", "mid", cheeks="blush")
            g9 "I'd gladly help you tie it around your back if you can't reach."
            call her_main("That's not why!", "annoyed", "base", "annoyed", "mid", cheeks="blush")
            call her_main("*Grr*... I can't believe you...", "clench", "narrow", "base", "R", cheeks="blush")
            call her_main("I am not wearing this... This excuse of a bikini...", "annoyed", "closed", "base", "mid", cheeks="blush")
            m "Well excuuuuuse me, princess..."
        else: # < 18
            call her_main("A bikini?", "open", "squint", "base", "mid", cheeks="blush")
            m "This one."
            call her_main("That one?", "angry", "narrow", "base", "down", cheeks="blush")
            m "Yes, that one."
            call her_main("Really?", "angry", "squint", "base", "mid", cheeks="blush")
            m "Really..."
            call her_main("Are you sure--", "angry", "squint", "base", "mid", cheeks="blush")
            m "I am--...{w=0.4} How long are you going to keep this up?"
            call her_main("...", "annoyed", "squint", "base", "R", cheeks="blush")
            call her_main("Sir, surely this kind of bikini...", "normal", "closed", "base", "mid", cheeks="blush")
            call her_main("Why it looks like something you might wear at...", "angry", "narrow", "base", "down", cheeks="blush")
            m "At what, [hermione_name]?"
            call her_main("*Ehm*...", "upset", "narrow", "base", "mid", cheeks="blush")
            m "A porn shoot?"
            call her_main("I...{w=0.4} Yes.", "angry", "narrow", "base", "mid", cheeks="blush")
            m "You've watched porn [hermione_name]?"
            call her_main("What?!", "clench", "squint", "base", "mid", cheeks="blush")
            m "You just agreed with what I said... Which means you've watched porn before."
            call her_main("I...{w=0.4} I have not!", "annoyed", "closed", "annoyed", "mid", cheeks="blush")
            call her_main("I swear, I've never--", "open", "closed", "annoyed", "mid", cheeks="blush")
            m "Look, I'm not judging."
            call her_main("But...", "clench", "squint", "worried", "mid", cheeks="blush")
            call her_main("You...{w=0.4} Sorry [genie_name], but this outfit is too much...", "open", "narrow", "worried", "R", cheeks="blush")

    ################################
    ## Pizza Slut Outfit (mirror) ##
    ################################
    elif item == her_outfit_pizza: #Req 19 (top, panties)
        m "Put this pizza on."
        if her_whoring < 13:
            call her_main("Put it on, [genie_name]?", "normal", "squint", "base", "mid")
            m "Yes, put it on."
            call her_main("Do you want me to heat it up?", "open", "squint", "worried", "mid")
            m "No, I want you to put it on."
            call her_main("*Huh*?", "annoyed", "squint", "base", "mid")
            m "Put... it--"
            m "You know what... Forget it."
        else: # < 19
            call her_main("Put it on, [genie_name]?", "normal", "squint", "base", "mid")
            m "Yes..."
            call her_main("...", "normal", "squint", "base", "mid")
            call her_main("...", "normal", "squint", "base", "stare")
            call her_main("Surely you can't be serious...", "disgust", "squint", "base", "mid")
            call her_main("You want me to wear...{w=0.4} Pizza?", "angry", "narrow", "base", "down")
            call her_main("Where on earth did you get an idea like this?", "open", "closed", "worried", "mid")
            m "In a dream."
            call her_main("...{w} Then it will stay that way...", "normal", "narrow", "base", "R")
            m "(Such a pizzawork that one...)"

    ###################
    ## Ribbon Outfit ##
    ###################
    elif item == her_outfit_ribbon: #Req 18 (bra, panties)
        m "I've got this thing that I'd like you to wrap for me."
        if her_whoring < 4:
            call her_main("You want me to wrap a gift for you?", "annoyed", "squint", "base", "mid")
            m "Yes..."
            call her_main("I guess I could do that...", "open", "closed", "base", "mid")
            m "Here's the ribbons..."
            call her_main("Thank you.", "base", "base", "base", "mid")
            m "Go on..."
            call her_main("[genie_name], you've not provided me any wrapping paper...", "open", "squint", "base", "mid")
            call her_main("Or whatever it is you wanted me to wrap.", "open", "base", "base", "mid")
            m "My mistake... I should've been more clear."
            m "You won't need any paper, the ribbons should do."
            call her_main("Right... but what about--", "angry", "base", "base", "mid")
            m "Now take your clothes off and tie those ribbons around yourself."
            call her_main("...", "clench", "wide", "base", "mid")
            call her_main("You want me to what?!", "disgust", "base", "annoyed", "mid")
            m "Take your clothes--"
            call her_main("[genie_name], are you crazy?!", "scream", "happyCl", "annoyed", "mid")
            m "You've learnt how to tie a knot have you not?"
            m "If it's an issue I suppose I could--"
            call her_main("You want me to take my clothes off and only wear a ribbon?!", "clench", "base", "annoyed", "mid")
            m "Ribbons actually... There's two of them."
            call her_main("Oh... Then I suppose it's fine then!", "disgust", "narrow", "annoyed", "R")
            m "I knew you'd come around sooner rather than--"
            call her_main("...", "annoyed", "base", "angry", "mid")
            m "Ah... Sarcasm... My most loyal friend yet also my greatest enemy..."
        elif her_whoring < 13:
            call her_main("And that gift is?", "open", "narrow", "base", "mid")
            m "It's you!"
            call her_main("*Ugh*...", "disgust", "narrow", "base", "R")
            call her_main("You really expect me to gift wrap myself?", "annoyed", "closed", "annoyed", "mid")
            m "Yep."
            m "But don't worry. I'll unwrap my present myself."
            call her_main("Gross...", "annoyed", "narrow", "base", "R")
            m "Don't put yourself down like that."
            call her_main("I am not putting this on...", "open", "narrow", "annoyed", "mid")
            g4 "Why not?"
            call her_main("I am not some gift for you to unwrap, [genie_name]...", "disgust", "narrow", "base", "mid")
            m "Worst birthday ever..."
        else: # < 18
            call her_main("It's me isn't it?", "disgust", "narrow", "base", "mid")
            g9 "It's--"
            m "How did you know?"
            call her_main("...", "normal", "narrow", "base", "mid")
            m "Am I really that predicable?"
            call her_main("Yes...", "normal", "narrow", "base", "mid")
            m "Well... take this for predictable..."
            m "I want you to tie it around your naked body!"
            call her_main("...", "annoyed", "narrow", "base", "mid")
            m "Don't tell me you knew that too?"
            call her_main("I mean...", "open", "closed", "base", "mid")
            m "*Hmm*... In that case I want you to..."
            g9 "Tie it around your tits so hard it squeezes them together!"
            call her_main("...", "clench", "wide", "base", "mid")
            g9 "Didn't expect that one did you?"
            call her_main("I am not doing that!", "open", "base", "annoyed", "mid")
            m "(Aw, shit...)"
            m "What about doing it loosely?"
            call her_main("...", "upset", "base", "annoyed", "mid")
            m "Yeah, yeah... Fine... Not like it's my birthday or anything..."

    ######################
    ## Christmas Outfit ##
    ######################
    elif item == her_outfit_xmas: #Req 13 (top, bottom)
        m "I'm feeling festive today so could you put on the Christmas outfit?"
        if her_whoring < 4:
            call her_main("What is wrong with this outfit?!", "clench", "squint", "worried", "down", cheeks="blush")
            call her_main("Surely this isn't appropriate holiday attire!", "angry", "narrow", "annoyed", "mid", cheeks="blush")
            m "I don't know... Might jingle a couple of balls..."
            call her_main("What did you just say?!", "clench", "squint", "base", "mid", cheeks="blush")
            m "Bells... I said bells..."
            m "Come on, just put the thing on. I'm sure Santa would give us a white Christmas if you did."
            call her_main("I think I'll pass...", "open", "base", "annoyed", "R", cheeks="blush")
            m "(Balls...)"
        else: # < 13
            call her_main("Are those horns?", "disgust", "narrow", "base", "down", cheeks="blush")
            m "Antlers actually..."
            call her_main("Antlers...", "upset", "narrow", "base", "down", cheeks="blush")
            call her_main("And a bell...", "annoyed", "narrow", "base", "down", cheeks="blush")
            call her_main("You trying to make me to look like some sort of reindeer?", "angry", "closed", "annoyed", "mid", cheeks="blush")
            g9 "Cute, aren't they?"
            call her_main("...", "disgust", "narrow", "annoyed", "mid", cheeks="blush")
            g9 "You'd be like a sexy reindeer!"
            m "Actually, that does sound a bit--"
            call her_main("I'm not putting this on...", "angry", "closed", "annoyed", "mid", cheeks="blush")


    else:
        $ random_number = renpy.random.randint(1, 5)

        if random_number == 1:
            call her_main("I am not wearing that...", "annoyed", "base", "angry", "down")
        elif random_number == 2:
            call her_main("Thanks, but no thanks...", "annoyed", "happyCl", "angry", "R")
        elif random_number == 3:
            call her_main("You actually think I'd put on something like that?", "annoyed", "wide", "angry", "mid")
        elif random_number == 4:
            call her_main("I'm not some Slytherin skank [genie_name], ask them to humiliate themselves for your amusement...", "open", "narrow", "angry", "L")
        elif random_number == 5:
            call her_main("This is too much.", "annoyed", "narrow", "angry", "R")

    return

label her_reaction_blacklist(item):
    call her_main("I would have to take off some my clothes to fit into this...", "disgust", "base", "base", "down")

    if "top" in item.blacklist and hermione.is_worn("top"):
        call her_main("My top won't fit at all.", "open", "narrow", "angry", "mid")

    if "bottom" in item.blacklist and hermione.is_worn("bottom"):
        call her_main("The skirt I'm wearing won't be of much use.", "open", "narrow", "angry", "mid")

    if "bra" in item.blacklist and hermione.is_worn("bra"):
        call her_main("Wearing a bra with this would be impossible.", "annoyed", "narrow", "angry", "L", cheeks="blush")

    if "panties" in item.blacklist and hermione.is_worn("panties"):
        call her_main("And how in the world am I supposed to wear panties with this?", "angry", "narrow", "angry", "mid", cheeks="blush")

    m "Pretty please?"
    call her_main("Fine, I'll wear it... but I'm putting my old clothes back on once you change your mind.", "annoyed", "narrow", "angry", "R", cheeks="blush")

    return
