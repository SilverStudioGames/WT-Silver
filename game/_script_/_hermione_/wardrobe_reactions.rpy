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
        call her_main("Thanks but no thanks...", "annoyed", "happyCl", "angry", "R")
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
    # if item == <DollOutfit Object>:
    #     her "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label her_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     her "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 5)

    if random_number == 1:
        call her_main("I am not wearing that...", "annoyed", "base", "angry", "down")
    elif random_number == 2:
        call her_main("Thanks but no thanks...", "annoyed", "happyCl", "angry", "R")
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
