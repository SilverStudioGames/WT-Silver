define cho_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4, #TODO set to fail until start of Slytherin match tier (after Hufflepuff match)
    "touch breasts": 12, #TODO set to fail until start of Gryffindor match tier (after Slytherin match)
    "touch vagina": 18, #TODO set to fail until highest level of Gryffindor match tier (after Slytherin match)
    "unequip panties": 15,
    "unequip bra": 15,
    "unequip top": 3,
    "unequip bottom": 3,
    }

define cho_responses = {
    "category_fail": "cho_reaction_category_fail",
    "equip": "cho_reaction_equip",
    "equip_fail": "cho_reaction_equip_fail",
    "unequip": "cho_reaction_unequip",
    "unequip_fail": "cho_reaction_unequip_fail",
    "touch": "cho_reaction_touch",
    "touch_fail": "cho_reaction_touch_fail",
    "equip_outfit": "cho_reaction_equip_outfit",
    "equip_outfit_fail": "cho_reaction_equip_outfit_fail",
    "blacklist": "cho_reaction_blacklist",
}

label cho_reaction_category_fail(category):

    if category == "upper undergarment":
        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call cho_main("You want to pick my underwear?", "disgust", "narrow", "angry", "mid")
            call cho_main("I don't think so.", "open", "narrow", "angry", "R")
        elif random_number == 2:
            call cho_main("Unless we're doing exercises I don't see why you want me to change my underwear...", "disgust", "base", "angry", "R")
        elif random_number == 3:
            call cho_main("I'm perfectly fine with the underwear I'm already wearing thank you...", "base", "base", "base", "mid")
    elif category == "lower undergarment":
        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call cho_main("My underwear?", "disgust", "base", "raised", "mid")
            call cho_main("Why do you want me to change them exactly?", "angry", "narrow", "angry", "mid")
        elif random_number == 2:
            call cho_main("*Err*... You want me to do what?", "disgust", "base", "angry", "mid", cheeks="blush")
        elif random_number == 3:
            call cho_main("Are we doing something that requires me to change my underwear?", "annoyed", "narrow", "raised", "mid")
            m "I just thought I could pick some for you to wear."
            call cho_main("Well... You thought wrong.", "upset", "narrow", "angry", "mid")
    elif category == "piercings & tattoos": #TODO set appropriate levels
        if cho_whoring >= 12:
            call cho_main("My body is already perfect without such things...", "smile", "closed", "base", "mid")
        elif cho_whoring >= 6: #After she has stripped
            call cho_main("Isn't seeing me naked good enough for you?", "annoyed", "narrow", "base", "mid")
        else: #Under naked level
            call cho_main("Yeah, that's not happening...", "annoyed", "narrow", "angry", "R")

    return

label cho_reaction_touch(what): #TODO set proper whoring levels , Check comments on each for info
    if what == "head":
        $ mouse_headpat()

        #if cho_whoring >= 16: #TODO change to Post Gryffindor match (end of tier)
            #$ random_number = renpy.random.randint(1, 3)
            #if random_number == 1:
                #call cho_main("Thank you [cho_genie_name]...", "open", "narrow", "base", "down", cheeks="blush")
            #elif random_number == 2:
                #call cho_main("I'm glad you're so proud of me [cho_genie_name]...", "base", "narrow", "base", "mid", cheeks="blush")
            #elif random_number == 3:
                #call cho_main("*Mmm*...", "horny", "closed", "base", "mid", cheeks="blush")
        #elif cho_whoring >= 12: #TODO change to Post Gryffindor match (start of tier)
            #$ random_number = renpy.random.randint(1, 3)
            #if random_number == 1:
                #call cho_main("I could get used to this...", "base", "narrow", "base", "R", cheeks="blush")
            #elif random_number == 2:
                #call cho_main("Are you sure there isn't anywhere else you could distribute that praise?", "smile", "narrow", "base", "mid", cheeks="blush")
            #elif random_number == 3:
                #call cho_main("Is this supposed to be my reward, [cho_genie_name]?", "soft", "narrow", "base", "mid", cheeks="blush")
                #call cho_main("I was expecting more coming from you...", "open", "narrow", "base", "downR", cheeks="blush")
        if cho_whoring >= 8: #TODO change to Pre Gryffindor match (after Slytherin match)
            $ random_number = renpy.random.randint(1, 3)
            if random_number == 1:
                call cho_main("*Hmm*... Well I suppose this is fine... You did help me beat those Slytherins after all.", "soft", "closed", "base", "mid", cheeks="blush")
            elif random_number == 2:
                call cho_main("Thank you, but don't we have other things to focus on?", "open", "narrow", "base", "R", cheeks="blush")
            elif random_number == 3:
                call cho_main("Yes, I do believe I've deserved some praise...", "base", "base", "base", "mid", cheeks="blush")
                call cho_main("Although petting is a bit out there as a reward...", "soft", "base", "base", "R", cheeks="blush")
        else: #TODO Pre Slytherin match (after hufflepuff match)
            #Confusing / joking manner
            $ random_number = renpy.random.randint(1, 4)
            if random_number == 1:
                call cho_main("Are you measuring my height or something?", "annoyed", "narrow", "base", "mid")
            elif random_number == 2:
                call cho_main("Is this supposed to encourage me?", "disgust", "closed", "base", "mid")
            elif random_number == 3:
                call cho_main("You'd usually only pet a dog when they do well with their training you know that right?", "open", "narrow", "raised", "mid")
            elif random_number == 4:
                call cho_main("What next? A treat?", "soft", "narrow", "base", "R")

    elif what == "breasts":
        $ mouse_heart()
        # Post Gryffindor match
            #if random_number == 1:
                #call cho_main("*Mmm*...", "horny", "closed", "base", "mid")
            #elif random_number == 2:
                #call cho_main("Thank you [cho_genie_name]...", "soft", "narrow", "base", "mid", cheeks="blush")
            #elif random_number == 3:
                #call cho_main("Glad you appreaciate them as much as I do...", "smile", "wink", "base", "mid", cheeks="blush")

        #else: Start of Gryffindor match tier

        $ random_number = renpy.random.randint(1, 4)
        if random_number == 1:
            call cho_main("Kissing them for good luck are we?", "smile", "narrow", "base", "mid", cheeks="blush")
        elif random_number == 2:
            call cho_main("*Mmm*...", "horny", "closed", "base", "mid")
            call cho_main("...", "disgust", "narrow", "base", "mid", cheeks="blush")
        elif random_number == 3:
            call cho_main("My Quaffles are quite perfect aren't they?", "grin", "narrow", "base", "mid", cheeks="blush")
            call cho_main("*Ugh*... Why did I just call them that...", "disgust", "narrow", "base", "downR", cheeks="heavy_blush")
        elif random_number == 4:
            call cho_main("*Mmm*... Feel how firm those bad girls are?", "base", "narrow", "base", "mid", cheeks="blush")
            call cho_main("That's the reward from years of hard training...", "grin", "closed", "base", "mid", cheeks="blush")
    elif what == "vagina":
        $ mouse_heart()
        # Post Gryffindor match
            #if random_number == 1:
                #call cho_main("Found one of the goal posts did you?", "base", "narrow", "base", "mid", cheeks="blush")
                #call cho_main("There's two more you know...", "smile", "wink", "base", "mid", cheeks="blush")
            #elif random_number == 2:
                #call cho_main("Careful or I might lock my thighs around your neck and keep you there...", "soft", "narrow", "base", "mid", cheeks="blush")
            #else: #highest level of Gryffindor tier (after Slytherin match) (will put below writing here once match implemented)

        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call cho_main("*Hmm*... I can appreciate a man who goes for what he wants no matter what...", "base", "narrow", "base", "mid", cheeks="blush")
        elif random_number == 2:
            call cho_main("Such speed... Fancy yourself a seeker do you?", "smile", "narrow", "base", "mid", cheeks="blush")
        elif random_number == 3:
            call cho_main("*Hmm*... Surely such a move must count as a foul...", "smile", "wink", "base", "mid", cheeks="blush")

    return

label cho_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        $ random_number = renpy.random.randint(1, 4)
        if random_number == 1:
            call cho_main("Don't touch my hair...", "clench", "base", "base", "mid")
        elif random_number == 2:
            call cho_main("Bad [cho_genie_name]...", "annoyed", "base", "angry", "mid")
        elif random_number == 3:
            call cho_main("No touch!", "open", "closed", "angry", "mid")
        elif random_number == 4:
            call cho_main("Don't...{w=0.4} Pet...{w=0.4} me...", "soft", "narrow", "angry", "mid")

    elif what == "breasts":
        $ mouse_slap()

        $ random_number = renpy.random.randint(1, 4)
        if random_number == 1:
            call cho_main("[cho_genie_name]?!", "mad", "base", "angry", "mid")
            call cho_main("This isn't a part of our training...", "clench", "base", "angry", "mid")
        elif random_number == 2:
            call cho_main("Nice try...", "smile", "narrow", "angry", "mid")
        elif random_number == 3:
            call cho_main("What are you doing?!", "disgust", "wide", "base", "mid")
        elif random_number == 4:
            call cho_main("Too slow...", "crooked_smile", "narrow", "angry", "mid")

    elif what == "vagina":
        $ mouse_slap()

        $ random_number = renpy.random.randint(1, 4)
        if random_number == 1:
            call cho_main("Hands where I can see them!", "angry", "base", "angry", "mid")
        elif random_number == 2:
            call cho_main("You'd have to be a lot faster to get even close to getting away with that...", "crooked_smile", "narrow", "angry", "mid")
        elif random_number ==3:
            call cho_main("Nice try...", "soft", "narrow", "angry", "mid")
        elif random_number ==4:
            call cho_main("No foul plays, [cho_genie_name]...", "angry", "narrow", "angry", "mid")

    return

label cho_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     cho "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label cho_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     cho "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 4)
    if random_number == 1:
        call cho_main("There's no way I would wear that.", "upset", "narrow", "angry", "mid")
    elif random_number == 2:
        call cho_main("Put it on yourself...", "open", "base", "angry", "mid")
        m "I don't think it would fit."
        call cho_main("Well, tough luck...", "annoyed", "narrow", "angry", "R")
    elif random_number == 3:
        call cho_main("I am not wearing that...", "upset", "closed", "base", "mid")
    elif random_number == 4:
        call cho_main("Ask Granger to wear it why don't you...", "open", "closed", "angry", "mid")
        m "It's made for your size."
        call cho_main("What is that supposed to mean?", "soft", "base", "angry", "mid")
        g4 "..."

    return

label cho_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if cho_whoring > 15:
    #        cho "You want to see my snatch?"
    #        cho "You got it [genie_name]!"
    #
    return

label cho_reaction_unequip_fail(item):
    if item.type == "panties":

        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call cho_main("You want me to take off my underwear?", "upset", "narrow", "angry", "mid")
            call cho_main("How is that supposed to help with my training?", "open", "closed", "angry", "mid", cheeks="blush")
        elif random_number == 2:
            call cho_main("You want me to stand here without underwear?", "disgust", "narrow", "base", "mid")
            call cho_main("Yeah, in your dreams [cho_genie_name]...", "annoyed", "narrow", "angry", "R")
        elif random_number == 3:
            call cho_main("Take your own underwear off why don't you...", "disgust", "narrow", "angry", "mid")
            m "What's to say I'm wearing any?"
            call cho_main("...", "angry", "closed", "angry", "mid")

    elif item.type == "bra":
        $ random_number = renpy.random.randint(1, 2)
        if random_number == 1:
            call cho_main("I bet that Gryffindor cow happily shows you her tits but that doesn't mean I will...", "disgust", "base", "angry", "R", cheeks="blush")
        elif random_number == 2:
            call cho_main("You want me to flash you my tits?", "angry", "wide", "base", "mid", cheeks="blush")
            m "I want you to take it off and keep it off..."
            call cho_main("No way!", "clench", "narrow", "angry", "mid")

    elif item.type == "top":
        call cho_main("I'm sorry if you don't like my choice of clothes, [cho_genie_name]...", "annoyed", "narrow", "angry", "R")

    elif item.type == "bottom":
        call cho_main("I'm sorry if you don't like my choice of clothes, [cho_genie_name]...", "open", "narrow", "angry", "downR")
    return

label cho_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     cho "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label cho_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     cho "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 5)
    if random_number == 1:
        call cho_main("I am not wearing that...", "clench", "closed", "base", "mid")
    elif random_number == 2:
        call cho_main("Thanks but no thanks...", "base", "base", "base", "mid")
    elif random_number == 3:
        call cho_main("You actually think I'd put on something like that?", "angry", "base", "base", "mid")
    elif random_number == 4:
        call cho_main("Do I look like Granger [cho_genie_name]? I am not wearing something like that...", "disgust", "narrow", "base", "mid")
    elif random_number == 5:
        call cho_main("This is too much.", "mad", "closed", "base", "mid")

    return

label cho_reaction_blacklist(item):
    cho "Is that really necessary, [cho_genie_name]?"

    if "top" in item.blacklist and cho.is_worn("top"):
        cho "My upper garment won't fit with this."

    if "bottom" in item.blacklist and cho.is_worn("bottom"):
        cho "Forget about my bottoms, no way they'd fit."

    if "bra" in item.blacklist and cho.is_worn("bra"):
        cho "I don't know if I can wear a bra with it."

    if "panties" in item.blacklist and cho.is_worn("panties"):
        cho "Seems as if I would need to take off my panties first to wear this."

    cho "You're asking a lot, [cho_genie_name], you know that?"
    m "Come on Cho, you're my favourite {size=-6}snatch grabber{/size} in training!"
    cho "What was that?"
    m "I said. You're my favourite snitch catcher in training."
    cho "*sigh* Alright, if it means this much to you [cho_genie_name]..."
    g9 "Hell yes!"

    return
