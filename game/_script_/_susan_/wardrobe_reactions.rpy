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
    ### Examples
    # if category == "upper undergarment":
    #     sus "Not in this century."
    # elif category == "lower undergarment":
    #     sus "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     sus "Not in this... Eternity!"
    return

label sus_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     sus "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     sus "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     sus "Grab me by the pussy!"
    return

label sus_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        sus "*Eeek!*"
        sus "I'm sorry sir, you scared me..."
        m "(Poor thing isn't used to human touch...)"

    elif what == "breasts":
        $ mouse_slap()

        sus "Please don't bully me sir..."

    elif what == "vagina":
        $ mouse_slap()

        sus "No! Please don't make me do this in front of everyone again..."
        m "Do what?"
        sus "N-nothing, sir, forgive me."
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

    sus "I-I..."
    m "You don't like it?"
    sus "It's not like t-that, I just..."
    m "Not comfortable wearing it?"
    sus "*Uh-huh*"
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
        sus "I'm n-not comfortable with that, sir..."

    elif item.type == "bra":
        sus "P-please I don't want to.."

    elif item.type == "top":
        sus "I don't know if this is a good idea..."
        m "You have nothing to be ashamed of."
        sus "S-Sorry but no..."

    elif item.type == "bottom":
        sus "I don't want to..."
        m "It's okay, we'll work on your confidence first."
        sus "Thank you..."
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

    sus "Oh wow it's..."
    m "You like it? How about you wear it?"
    sus "I couldn't, I..."
    m "(Perhaps it was a little too soon for that.)"

    return

label sus_reaction_blacklist(item):
    sus "B-but..."
    m "But what?"

    if "top" in item.blacklist and susan.is_worn("top"):
        sus "I would feel cold without my top..."

    if "bottom" in item.blacklist and susan.is_worn("bottom"):
        sus "I can't t-take off my skirt."
        m "Can't or won't?"
        sus "Won't..."

    if "bra" in item.blacklist and susan.is_worn("bra"):
        m "Let me guess, you aren't comfortable without a bra?"
        sus "*uh-huh*"

    if "panties" in item.blacklist and susan.is_worn("panties"):
        sus "The panties are e-essential for me..."

    m "How about just giving it a try?"
    m "If you don't like it you can always change back, that okay?"
    sus "Alright..."

    return
