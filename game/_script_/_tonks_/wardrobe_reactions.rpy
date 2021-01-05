define ton_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 12,
    "touch vagina": 18,
    #"unequip panties": 6, # Tonks does not use panties unequip limits.
    #"unequip bra": 6, # Tonks does not use bra unequip limits.
    "unequip top": 3,
    "unequip bottom": 3,
    }

define ton_responses = {
    "category_fail": "ton_reaction_category_fail",
    "equip": "ton_reaction_equip",
    "equip_fail": "ton_reaction_equip_fail",
    "unequip": "ton_reaction_unequip",
    "unequip_fail": "ton_reaction_unequip_fail",
    "touch": "ton_reaction_touch",
    "touch_fail": "ton_reaction_touch_fail",
    "equip_outfit": "ton_reaction_equip_outfit",
    "equip_outfit_fail": "ton_reaction_equip_outfit_fail",
    "blacklist": "ton_reaction_blacklist",
}

label ton_reaction_category_fail(category):
    ### Examples
    # if category == "upper undergarment":
    #     ton "Not in this century."
    # elif category == "lower undergarment":
    #     ton "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     ton "Not in this... Eternity!"
    return

label ton_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     ton "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     ton "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     ton "Grab me by the pussy!"
    return

label ton_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()
        $ random_number = renpy.random.randint(1, 5)

        if random_number == 1:
            call ton_main("Stop that.", face="annoyed")
        elif random_number == 2:
            call ton_main("Do you know how long it takes to model my hair like that?", face="neutral")
        elif random_number == 3:
            call ton_main("There's two things a man shouldn't touch, her wallet and her hair.", face="angry")
        elif random_number == 4:
            call ton_main("Don't get any funny ideas.", face="horny")
        elif random_number == 5:
            call ton_main("Hey, don't do that!", face="annoyed")
            call ton_main("Let me pet you instead.", face="neutral")
            $ mouse_headpat()
            pause 0.35
            $ mouse_headpat()
            pause 0.35
            $ mouse_headpat()
            call ton_main("Good boy!", face="happy")

    elif what == "breasts":
        $ mouse_slap()
        $ random_number = renpy.random.randint(1, 6)

        if random_number == 1:
            call ton_main("That's not how a headmaster should treat their subordinates.",face="annoyed")
        elif random_number == 2:
            call ton_main("It's inappropriate, let's keep it civil okay?",face="annoyed")
        elif random_number == 3:
            call ton_main("Someone fancy themselves a bit of a bad boy?",face="annoyed",mouth="base")
        elif random_number == 4:
            call ton_main("Hey, those are my fun bags... Don't be naughty.",face="annoyed",mouth="horny")
        elif random_number == 5:
            call ton_main("Hey now, someone's getting a bit ahead of themselves.",face="annoyed")
        elif random_number == 6:
            call ton_main("Those aren't for you to play with...",face="annoyed")

    elif what == "vagina":
        $ mouse_slap()
        $ random_number = renpy.random.randint(1, 5)

        if random_number == 1:
            call ton_main("You have to to earn it first.",face="annoyed")
        elif random_number == 2:
            call ton_main("If you'd like to keep these hands intact I suggest you stop it right now, [ton_genie_name].",face="annoyed")
        elif random_number == 3:
            call ton_main("Hey, who said you had permission to approach the chamber of secrets?",face="annoyed",eyebrows="angry",mouth="grin")
        elif random_number == 4:
            call ton_main("That place is reserved for good boys and girls...",face="annoyed",eyebrows="angry",mouth="grin")
        elif random_number == 5:
            call ton_main("That forest is forbidden entry for first years... let's get to know each other a bit better first...",face="annoyed",eyebrows="angry",mouth="grin")

    return

label ton_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ton "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label ton_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ton "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 3)
    if random_number == 1:
        call ton_main("Not yet big boy, perhaps once this scheme of ours comes more into fruition...",face="annoyed",eyebrows="angry",mouth="grin")
    elif random_number == 2:
        call ton_main("It does look nice but you need to deserve it...",face="annoyed",eyebrows="angry",mouth="grin")
    else:
        call ton_main("*Hmm*... What would you think of me if I wore this?... Later perhaps.",face="annoyed",eyebrows="raised",mouth="horny")


    return

label ton_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if ton_whoring > 15:
    #        ton "You want to see my snatch?"
    #        ton "You got it [genie_name]!"
    #
    return

label ton_reaction_unequip_fail(item):

    ### Bra and panties checks are not in use as Tonks doesn't mind NOT wearing underwear.
    # if item.type == "panties":
    #     ton "I'm n-not comfortable with that, sir..."

    # elif item.type == "bra":
    #     ton "P-please I don't want to.."

    if item.type == "top":
        call ton_main("Someone's being naughty... I might have to give you a spanking for that.",face="annoyed",eyebrows="angry",mouth="grin")
        call ton_main("Just kidding! Sure, have a quick look, [ton_genie_name].",face="annoyed",eyebrows="raised",mouth="horny")
        $ char_active.strip("top", "robe")
        call ton_main("",face="happy")
        pause 1.0
        call ton_main("",face="happy")
        pause 1.0
        call ton_main("",face="happy")
        $ char_active.wear("top", "robe")
        g4 "What gives?!"
        call ton_main("Time's up.",face="annoyed",eyebrows="angry",mouth="grin")
        m "......"

    elif item.type == "bottom":
        call ton_main("*Mmm*... I like where your head is at, but I have to refuse.",face="annoyed",eyebrows="angry",mouth="grin")
    return

label ton_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ton "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label ton_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ton "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    call ton_main("It looks lovely, but you'd have to prove yourself a bit more before I put that on...", face="annoyed",eyebrows="angry",mouth="grin")

    return

label ton_reaction_blacklist(item):
    ton "*oooh* that's racy!"

    if "top" in item.blacklist and tonks.is_worn("top"):
        ton "I'd need to take off my top."

    if "bottom" in item.blacklist and tonks.is_worn("bottom"):
        ton "It would be very unfashionable wearing bottom garment with that."

    if "bra" in item.blacklist and tonks.is_worn("bra"):
        ton "My girls would definitely appreciate me letting them breathe."
        g9 "Your tits you mean."
        ton "Now, now, don't get needy my dear headmaster."

    if "panties" in item.blacklist and tonks.is_worn("panties"):
        ton "There's not a single pair of panties in the world that would fit this."

    m "Well, what's the verdict?"
    ton "Simply put-- I love it."
    g9 "Jackpot!"

    return
