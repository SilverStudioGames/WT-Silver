define lun_requirements = {
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

define lun_responses = {
    "category_fail": "lun_reaction_category_fail",
    "equip": "lun_reaction_equip",
    "equip_fail": "lun_reaction_equip_fail",
    "unequip": "lun_reaction_unequip",
    "unequip_fail": "lun_reaction_unequip_fail",
    "touch": "lun_reaction_touch",
    "touch_fail": "lun_reaction_touch_fail",
    "equip_outfit": "lun_reaction_equip_outfit",
    "equip_outfit_fail": "lun_reaction_equip_outfit_fail",
    "blacklist": "lun_reaction_blacklist",
}

label lun_reaction_category_fail(category):
    ### Examples
    # if category == "upper undergarment":
    #     lun "Not in this century."
    # elif category == "lower undergarment":
    #     lun "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     lun "Not in this... Eternity!"
    return

label lun_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     lun "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     lun "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     lun "Grab me by the pussy!"
    return

label lun_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        g4 "Ouch! Why would you do that?!"
        lun "Oh! I'm terribly sorry, [lun_genie_name], I used to play this game with my father and..."
        m "I don't need to hear it..."
        lun "...as you wish sir."

    elif what == "breasts":
        $ mouse_slap()

        lun "*giggles* [lun_genie_name] stop that! It tickles."

    elif what == "vagina":
        $ mouse_slap()

        lun "*Ah* Sir, please don't tease me, wrackspurts have been terribly active today and I'm barely able to withhold as it is."

    return

label lun_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label lun_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    lun "*Hmm*"
    m "What?"
    lun "There's a weird aura surrounding this piece of garment."
    lun "It seems to be affecting the wrackspurts, as if they're multiplying!"
    lun "I'm sorry sir but I can't wear, not until I know how to fight them at least."
    m "(I guess that means she's not yet ready.)"

    return

label lun_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if lun_whoring > 15:
    #        lun "You want to see my snatch?"
    #        lun "You got it [genie_name]!"
    #
    return

label lun_reaction_unequip_fail(item):
    if item.type == "panties":
        lun "I'm sorry [lun_genie_name] but my panties are my one and only defence against wrackspurts."

    elif item.type == "bra":
        lun "*giggles*"
        m "What's so funny?"
        lun "You remind me of my daddy."
        m "(What the hell.....?)"

    elif item.type == "top":
        lun "I'm not sure how it would help me with my problem, sir."

    elif item.type == "bottom":
        lun "Wouldn't that make my wrackspurts problem worse, [lun_genie_name]?"
    return

label lun_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     lun "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label lun_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     lun "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    lun "This outfit seems to have wrackspurts all over it!"
    m "(I don't remember cumming on this piece of garment...)"
    g4 "(!!!)"
    g4 "(Could it be--...)"
    lun "Are you okay sir? You look pale."
    m "Yes, I'm fine. I guess you can stay in your clothes... for now."

    return

label lun_reaction_blacklist(item):
    lun "Will that really help? With the wrackspurts I mean."

    if "top" in item.blacklist and luna.is_worn("top"):
        lun "I would need to lose my top."

    if "bottom" in item.blacklist and luna.is_worn("bottom"):
        lun "The bottoms I'm wearing wound need to go."

    if "bra" in item.blacklist and luna.is_worn("bra"):
        lun "It seems no bra can fit in this garment."

    if "panties" in item.blacklist and luna.is_worn("panties"):
        lun "Wrackspurts would have a feast as I would not be able to wear panties with this."

    m "Trust me, I know what I'm doing."
    lun "If you say so sir."

    return
