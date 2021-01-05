define ast_requirements = {
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

define ast_responses = {
    "category_fail": "ast_reaction_category_fail",
    "equip": "ast_reaction_equip",
    "equip_fail": "ast_reaction_equip_fail",
    "unequip": "ast_reaction_unequip",
    "unequip_fail": "ast_reaction_unequip_fail",
    "touch": "ast_reaction_touch",
    "touch_fail": "ast_reaction_touch_fail",
    "equip_outfit": "ast_reaction_equip_outfit",
    "equip_outfit_fail": "ast_reaction_equip_outfit_fail",
    "blacklist": "ast_reaction_blacklist",
}

label ast_reaction_category_fail(category):
    ### Examples
    # if category == "upper undergarment":
    #     ast "Not in this century."
    # elif category == "lower undergarment":
    #     ast "Not in this millennium!"
    # elif category == "piercings & tattoos":
    #     ast "Not in this... Eternity!"
    return

label ast_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    ### Examples
    # if what == "head":
    #     ast "Rawrrrr, pet me master. :3"
    # elif what == "breasts":
    #     ast "Yes, squeeze my slutty tits, [genie_name]!"
    # elif what == "vagina":
    #     ast "Grab me by the pussy!"
    return

label ast_reaction_touch_fail(what):
    if what == "head":
        $ random_number = renpy.random.randint(1, 6)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey!", face="angry")
        elif random_number == 2:
            call ast_main("I'm not your pet, [ast_genie_name]...", face="annoyed")
        elif random_number == 3:
            call ast_main("Oh sorry, my hand slipped.", face="happy")
        elif random_number == 4:
            call ast_main("Do that again and you'll regret it...", face="angry")
        elif random_number == 5:
            call ast_main("Stop...", face="angry")
        elif random_number == 6:
            call ast_main("Don't!", face="angry")
            $ mouse_slap()
            call ast_main("Don't!{fast} Do!", face="angry")
            $ mouse_slap()
            call ast_main("Don't! Do!{fast} That!", face="angry")
            $ mouse_slap()
            call ast_main("Don't! Do! That!{fast} Again!", face="angry")
            $ mouse_slap()
            call play_sound("kick")
            with hpunch
            pause 1.0
            g4 "(Ouch, that hurt!)"

    elif what == "breasts":
        $ random_number = renpy.random.randint(1, 7)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey, cut that out!",face="annoyed",mouth="clench")
        elif random_number == 2:
            call ast_main("Ouch, that hurts...",face="annoyed",mouth="scream")
        elif random_number == 3:
            call ast_main("Hey, no nipple twisters...",face="annoyed")
        elif random_number == 4:
            call ast_main("Bad Touch!",face="annoyed")
        elif random_number == 5:
            call ast_main("*EEEH* Don't you have better things to do?",face="annoyed")
        elif random_number == 6:
            call ast_main("{size=+5}What are you doing?{/size}",face="angry",mouth="scream")
        elif random_number == 7:
            call ast_main("Stop that!",face="annoyed")

    elif what == "vagina":
        $ random_number = renpy.random.randint(1, 7)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey, that's private property.",face="annoyed")
        elif random_number == 2:
            call ast_main("Get your filthy hands off me, [ast_genie_name].",face="annoyed")
        elif random_number == 3:
            call ast_main("Stop it, you creep.",face="annoyed")
        elif random_number == 4:
            call ast_main("Why would you do that... nasty old man...",face="annoyed")
        elif random_number == 5:
            call ast_main("Don't touch me...",face="annoyed")
        elif random_number == 6:
            call ast_main("Don't be gross, [ast_genie_name].",face="annoyed")
        elif random_number == 7:
            call ast_main("...",face="annoyed")
    return

label ast_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ast "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label ast_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ast "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    $ random_number = renpy.random.randint(1, 3)

    if random_number == 1:
        call ast_main("*Nuh-uh*, I'm not putting that on.",face="annoyed")
    elif random_number == 2:
        call ast_main("*Pfff* You want me to wear that? In your dreams old man...",face="annoyed")
    else:
        call ast_main("Don't be such a creep, thanks but no thanks.",face="annoyed")

    return

label ast_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if ast_whoring > 15:
    #        ast "You want to see my snatch?"
    #        ast "You got it [genie_name]!"
    #
    return

label ast_reaction_unequip_fail(item):
    if item.type == "panties":
        $ random_number = renpy.random.randint(1, 3)

        ast "Like hell! Take off your own panties old man..."

        show screen blkfade
        with d5

        $ renpy.sound.play("sounds/zipper.mp3")
        ast "W-What are you doing?!"
        call play_sound("thump")
        with hpunch
        pause 0.5
        ast "Oh my god-- is that...?!"
        g9 "..."
        $ mouse_slap()
        with vpunch

        hide screen blkfade
        with d5

        g4 "Did you really have to slap me?"
        ast "You deserved it you perverted pervert!"

    elif item.type == "bra":
        ast "Why would you even suggest that?"

    elif item.type == "top":
        ast "Ha! Keep dreaming old man!"

    elif item.type == "bottom":
        ast "My bottoms stay where they are and that's final!"
    return

label ast_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ast "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label ast_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ast "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    ast "That's way beyond what I would consider dignified."

    if susan_unlocked:
        ast "Consider asking Susan instead."
        ast "I'm sure she'd enjoy wearing it for you, that cow."

    return

label ast_reaction_blacklist(item):
    ast "Aren't you demanding too much, [ast_genie_name]?"

    if "top" in item.blacklist and astoria.is_worn("top"):
        ast "My topmost garment won't work with that."

    if "bottom" in item.blacklist and astoria.is_worn("bottom"):
        ast "Wearing bottoms with this would be a fashion-crime."

    if "bra" in item.blacklist and astoria.is_worn("bra"):
        ast "I'd have to take off my bra."

    if "panties" in item.blacklist and astoria.is_worn("panties"):
        ast "How do I even wear panties with that?"

    ast "This is stupid..."

    if susan_unlocked:
        m "Perhaps I'll ask Susan instead--"

    ast "J-Just give me that!"

    return
