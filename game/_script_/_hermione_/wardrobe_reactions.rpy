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
    ### Examples
    # if category == "upper undergarment":
    #     her "Not in this century."
    # elif category == "lower undergarment":
    #     her "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     her "Not in this... Eternity!"
    return

label her_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     her "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     her "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     her "Grab me by the pussy!"
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
            call her_main("Unhand me..", "mad", "wide", "angry", "mid")
        elif random_number == 4:
            call her_main("Stop it please..", "open", "happyCl", "angry", "mid", cheeks="blush")
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
        call her_main("I'm not wearing that.", "annoyed", "base", "angry", "down")
    elif random_number == 2:
        call her_main("It's too slutty..", "annoyed", "happyCl", "angry", "R")
    elif random_number == 3:
        call her_main("I would look like a tramp, I refuse.", "annoyed", "wide", "angry", "mid")
    elif random_number == 4:
        call her_main("I'm not some Slytherin skank [genie_name], ask them to humiliate themselves for your amusement..", "open", "narrow", "angry", "L")
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
    if item.type == "panties":
        $ random_number = renpy.random.randint(1, 3)

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
        $ random_number = renpy.random.randint(1, 3)

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
        call her_main("I'm not wearing that.", "annoyed", "base", "angry", "down")
    elif random_number == 2:
        call her_main("It's too slutty..", "annoyed", "happyCl", "angry", "R")
    elif random_number == 3:
        call her_main("I would look like a tramp, I refuse.", "annoyed", "wide", "angry", "mid")
    elif random_number == 4:
        call her_main("I'm not some Slytherin skank [genie_name], ask them to humiliate themselves for your amusement..", "open", "narrow", "angry", "L")
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
