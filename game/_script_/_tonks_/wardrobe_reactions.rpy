define ton_requirements = {
    "category upper undergarment": 10,
    "category lower undergarment": 10,
    "category piercings & tattoos": 60,
    "touch head": 50,
    "touch breasts": 20,
    "touch vagina": 40,
    #"unequip panties": 6, # Tonks does not use panties unequip limits.
    #"unequip bra": 6, # Tonks does not use bra unequip limits.
    "unequip top": 20,
    "unequip bottom": 20,
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

    $ random_number = renpy.random.randint(1, 4)
    if category == "upper undergarment":
        if random_number == 1:
            call ton_main("*Hmm*... You'd like that wouldn't you?", "horny", "narrow", "base", "mid")
        elif random_number == 2:
            call ton_main("If you behave maybe I'll let you take a peek later, [ton_genie_name]...", "soft", "narrow", "base", "mid")
        elif random_number == 3:
            call ton_main("Patience dear...", "grin", "wink", "raised", "mid")
        elif random_number == 4:
            call ton_main("These crystal orbs are yet to predict that I would ever allow you to ask such a thing...", "open", "closed", "shocked", "mid")
            m "They might just need a good dusting..."
            call ton_main("Perhaps... But not right now...", "soft", "narrow", "base", "mid")
    elif category == "lower undergarment":
        if random_number == 1:
            call ton_main("You want me to put on underwear? Now that's asking a bit much don't you think?", "crooked_smile", "narrow", "base", "mid")
        elif random_number == 2:
            call ton_main("Like the Scottish say, I'd rather let it feel the breeze.", "grin", "narrow", "base", "mid")
        elif random_number == 3:
            call ton_main("Underwear? Don't make me laugh...", "base", "base", "base", "down")
        elif random_number == 4:
            call ton_main("You'd have to do better than that if you want this kitty to come out and play...", "base", "narrow", "base", "mid")
    elif category == "piercings & tattoos":
        if random_number == 1:
            call ton_main("I decide where such things go...", "open", "base", "base", "mid")
        elif random_number == 2:
            call ton_main("You'd like that wouldn't you? I think I'd keep such decisions for myself thank you.", "soft", "base", "base", "R")
        elif random_number == 3:
            call ton_main("*Hmm*... I'd be such a bad girl if I let you do that...", "annoyed", "closed", "base", "mid")
        elif random_number == 4:
            call ton_main("What would you think of me if I let you do that?", "horny", "narrow", "base", "down")
    return

label ton_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
        $ random_number = renpy.random.randint(1, 5)

        if random_number == 1:
            call ton_main("Is this what you do to our students? A bit tame don't you think?", "soft", "narrow", "base", "mid")
        elif random_number == 2:
            call ton_main("Surely this is not an appropriate method of rewarding your subordinate...", "horny", "narrow", "base", "R")
        elif random_number == 3:
            call ton_main("Does this mean I'm your favourite student?", "grin", "base", "raised", "mid")
            call ton_main("Teacher, I mean...", "base", "narrow", "base", "downR")
        elif random_number == 4:
            call ton_main("How naughty... How could I ever have allowed such indecent behaviour...", "disgust", "narrow", "base", "mid")
            call ton_main("Don't you dare touch my elbows next...", "soft", "narrow", "base", "mid")
        elif random_number == 5:
            call ton_main("Such a weird custom but I'll allow it...", "horny", "closed", "base", "mid")
    elif what == "breasts":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 4)

        if random_number == 1:
            call ton_main("*Mmm*...", "base", "narrow", "base", "up")
        elif random_number == 2:
            call ton_main("Trying to get put in detention are we?", "grin", "narrow", "base", "mid")
        elif random_number == 3:
            call ton_main("*Tsk*... How naughty... And with an employee no less.", "horny", "narrow", "base", "mid")
        elif random_number == 4:
            call ton_main("I don't remember this being part of the job description...", "horny", "narrow", "shocked", "down")
            call ton_main("But I'll look the other way for now...", "grin", "closed", "base", "mid")
    elif what == "vagina":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 4)

        if random_number == 1:
            call ton_main("A gentleman usually doesn't kiss on the lips but I'll allow it...", "soft", "closed", "base", "mid")
        elif random_number == 2:
            call ton_main("*Hmm*...{w=0.3} Did I feel some tongue? Must've been my imagination...", "horny", "narrow", "base", "down")
        elif random_number == 3:
            call ton_main("Is this one part of the extra curricular activities in my work contract?", "grin", "narrow", "raised", "mid")
        elif random_number == 4:
            call ton_main("I didn't expect to receive a bonus today... What a nice surprise...", "grin", "narrow", "raised", "mid")
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
            call ton_main("You have to earn it first.",face="annoyed")
        elif random_number == 2:
            call ton_main("If you'd like to keep these hands intact I suggest you stop it right now, [ton_genie_name].",face="annoyed")
        elif random_number == 3:
            call ton_main("Hey, who said you had permission to approach the chamber of secrets?",face="annoyed",eyebrows="angry",mouth="grin")
        elif random_number == 4:
            call ton_main("That place is reserved for good boys and girls...",face="annoyed",eyebrows="angry",mouth="grin")
        elif random_number == 5:
            call ton_main("That forest is forbidden entry for first years... Let's get to know each other a bit better first...",face="annoyed",eyebrows="angry",mouth="grin")

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
        $ random_number = renpy.random.randint(1, 4)
        if random_number == 1:
            call ton_main("I thought patience came with old age...", "base", "base", "raised", "R")
        elif random_number == 2:
            call ton_main("What's the point in that? You already know what's under there don't you?", "soft", "narrow", "base", "mid")
        elif random_number == 3:
            call ton_main("You could do with learning some restraint... Perhaps I need to teach you a thing or two...", "grin", "narrow", "base", "mid")
        elif random_number == 4:
            call ton_main("Eager are we? Well I can't say I blame you...", "open", "closed", "base", "mid")
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
