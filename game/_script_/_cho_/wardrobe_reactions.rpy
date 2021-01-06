define cho_requirements = {
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
    ### Examples
    # if category == "upper undergarment":
    #     cho "Not in this century."
    # elif category == "lower undergarment":
    #     cho "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     cho "Not in this... Eternity!"
    return

label cho_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     cho "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     cho "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     cho "Grab me by the pussy!"
    return

label cho_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        cho "Stop that! You will ruin my hairstyle."

    elif what == "breasts":
        $ mouse_slap()

        cho "[cho_genie_name]?! What are you doing!"
        cho "This isn't a part of our training..."

    elif what == "vagina":
        $ mouse_slap()

        cho "Hold your hands where I can see them!"

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

    cho "There's no way I would wear that."
    cho "Not even after a thousand push-ups!"

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
        cho "You want me to take off my underwear?"
        cho "How is that supposed to help with my training exactly?"

    elif item.type == "bra":
        cho "I bet that Gryffindor cow happily shows you her tits but that doesn't mean I will..."

    elif item.type == "top":
        cho "I'm sorry if you don't like my choice of clothes, [cho_genie_name]..." # Sarcastic

    elif item.type == "bottom":
        cho "I'm sorry if you don't like my choice of clothes, [cho_genie_name]..." # Sarcastic
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

    cho "An athlete like myself cannot be seen wearing something like this."

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
