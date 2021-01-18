define sus_requirements = {
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

define sus_responses = {
    "category_fail": "sus_reaction_category_fail",
    "equip": "sus_reaction_equip",
    "equip_fail": "sus_reaction_equip_fail",
    "unequip": "sus_reaction_unequip",
    "unequip_fail": "sus_reaction_unequip_fail",
    "touch": "sus_reaction_touch",
    "touch_fail": "sus_reaction_touch_fail",
    "equip_outfit": "sus_reaction_equip_outfit",
    "equip_outfit_fail": "sus_reaction_equip_outfit_fail",
    "blacklist": "sus_reaction_blacklist",
}

label sus_reaction_category_fail(category):

    if category == "upper undergarment":
        call sus_main("M-my my underwear? W-Why do you require me to-- *Ehm*...", "open", "eager", "worried", "R")
    elif category == "lower undergarment":
        call sus_main("M-my my underwear? W-Why do you require me to-- *Ehm*...", "upset", "closed", "worried", "mid")
    elif category == "piercings & tattoos":
        call sus_main("W-what would people... Sir, I don't want to be made f-fun of...", "upset", "wide", "worried", "mid")
    return

label sus_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    if what == "head":
        $ mouse_headpat()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call sus_main("S-Sir...", "base", "eager", "base", "up")
        elif random_number == 2:
            call sus_main("A-Are you s-sure this is appropriate?", "grin", "narrow", "base", "down")
        elif random_number == 3:
            call sus_main("Professor, p-please...", "base", "closed", "base", "mid")

    elif what == "breasts":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call sus_main("W-Why are you...", "upset", "happyCl", "base", "mid")
        elif random_number == 2:
            call sus_main("P-please, it's embarrassing...", "scream", "closed", "worried", "mid")
        elif random_number == 3:
            call sus_main("D-don't... Don't look at me sir...", "base", "closed", "worried", "mid")
    elif what == "vagina":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call sus_main("M-My...", "open", "wide", "worried", "down")
        elif random_number == 2:
            call sus_main("S-Sir...", "upset", "happyCl", "base", "mid")
        elif random_number == 3:
            call sus_main("P-please sir, it's embarrassing...", "base", "closed", "worried", "mid")

    return

label sus_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        call sus_main("*Eeek!*", "scream", "wide", "base", "wide")
        call sus_main("I'm sorry sir, you scared me...", "open", "eager", "worried", "mid")
        m "(Poor thing isn't used to human touch...)"

    elif what == "breasts":
        $ mouse_slap()

        call sus_main("Please don't bully me sir...", "open", "happyCl", "worried", "mid")

    elif what == "vagina":
        $ mouse_slap()

        call sus_main("No! Please don't make me do this in front of everyone again...", "scream", "happyCl", "base", "mid")
        m "Do what?"
        call sus_main("N-nothing, sir, forgive me.", "open", "narrow", "base", "wide")
        m "(...)"

    return

label sus_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     sus "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label sus_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     sus "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    call sus_main("I-I...", "open", "narrow", "worried", "mid")
    m "You don't like it?"
    call sus_main("It's not like t-that, I just...", "open", "happyCl", "base", "mid")
    m "Not comfortable wearing it?"
    call sus_main("*Uh-huh*", "base", "eager", "worried", "mid")
    m "Okay, maybe later then."

    return

label sus_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if sus_whoring > 15:
    #        sus "You want to see my snatch?"
    #        sus "You got it [genie_name]!"
    #
    return

label sus_reaction_unequip_fail(item):
    if item.type == "panties":
        call sus_main("I'm n-not comfortable with that, sir...", "open", "happyCl", "base", "mid")

    elif item.type == "bra":
        call sus_main("P-please, I can't be w-wearing this sir..", "open", "closed", "worried", "mid")

    elif item.type == "top":
        call sus_main("I don't know if this is a good idea...", "open", "narrow", "worried", "mid")
        m "You have nothing to be ashamed of."
        call sus_main("S-Sorry, I can't...", "open", "closed", "worried", "mid")

    elif item.type == "bottom":
        call sus_main("I can't...", "open", "happyCl", "base", "mid")
        m "It's okay, we'll work on your confidence first."
        call sus_main("Thank you...", "base", "eager", "worried", "mid")
    return

label sus_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     sus "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label sus_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     sus "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    call sus_main("Oh wow... It's... *Ehm*...", "open", "narrow", "worried", "mid")
    m "You like it? How about you wear it?"
    call sus_main("I couldn't, I...", "open", "happyCl", "base", "mid")
    m "(Perhaps I'm being a little too forward for something that.)"

    return

label sus_reaction_blacklist(item):
    call sus_main("B-but...", "base", "base", "base", "mid")
    m "But what?"

    if "top" in item.blacklist and susan.is_worn("top"):
        call sus_main("I would feel cold without my top...", "open", "happyCl", "base", "mid")

    if "bottom" in item.blacklist and susan.is_worn("bottom"):
        call sus_main("I can't t-take off my skirt.", "open", "narrow", "worried", "mid")
        m "Can't or won't?"
        call sus_main("Won't...", "open", "happyCl", "base", "mid")

    if "bra" in item.blacklist and susan.is_worn("bra"):
        m "Let me guess, you aren't comfortable without a bra?"
        call sus_main("*uh-huh*", "base", "eager", "worried", "mid")

    if "panties" in item.blacklist and susan.is_worn("panties"):
        call sus_main("The panties are e-essential for me...", "open", "happyCl", "base", "mid")

    m "How about just giving it a try?"
    m "If you don't like it you can always change back, that okay?"
    call sus_main("Alright...", "base", "eager", "worried", "mid")

    return
