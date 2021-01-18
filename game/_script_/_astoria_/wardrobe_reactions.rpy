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
    if category == "upper undergarment":
        call ast_main("Good one sir!", "smile", "narrow", "base", "mid")
        m "I wasn't--"
        m "..."
    elif category == "lower undergarment":
        call ast_main("Why would I do that?", "base", "narrow", "angry", "R")
        m "I don't know, why wouldn't you do it?"
        call ast_main("...", "base", "narrow", "base", "down")
    elif category == "piercings & tattoos":
        call ast_main("Sounds awesome but you'll just make it something stupid.", "angry", "narrow", "base", "R")
        m "I'd never..."
        call ast_main("Lies...", "clench", "base", "base", "mid")
    return

label ast_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call ast_main("Whatever...", "base", "base", "base", "down")
        elif random_number == 2:
            call ast_main("I'm only letting you do this cause you didn't snitch on me...", "open", "closed", "base", "mid")
            m "Sure..."
        elif random_number == 3:
            call ast_main("What's this obsession with petting coming from?", "open", "narrow", "base", "L")
            m "*Err*..."
            call ast_main("When people called you eccentric I didn't think they meant bonkers mad...", "clench", "closed", "base", "down")
    elif what == "breasts":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call ast_main("You're really enjoying that aren't you?", "base", "narrow", "base", "mid")
            call ast_main("Well I guess you're just a man after all...", "open", "closed", "base", "mid")
        elif random_number == 2:
            call ast_main("Hey!", "clench", "base", "base", "mid")
            m "What?"
            call ast_main("...", "grin", "narrow", "base", "L")
        elif random_number == 3:
            call ast_main("Gross...", "annoyed", "narrow", "base", "mid")
    elif what == "vagina":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if random_number == 1:
            call ast_main("What do you think you're doing?", "clench", "base", "base", "mid", cheeks="blush")
            m "Kissing you?"
            call ast_main("Surely that's against some rule...", "annoyed", "base", "base", "R")
            m "Worried about rule breaking all of a sudden are we?"
            call ast_main("No...", "base", "narrow", "base", "mid")
        elif random_number == 2:
            call ast_main("Aren't you a bold one...", "base", "narrow", "base", "mid")
        elif random_number == 3:
            call ast_main("Thought you could slip past my wards did you?", "clench", "base", "base", "mid")
            call ast_main("I'll have you know I felt none of that!", "open", "closed", "base", "mid", cheeks="blush")

    return

label ast_reaction_touch_fail(what):
    if what == "head":
        $ random_number = renpy.random.randint(1, 6)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey!", "annoyed", "base", "angry", "mid")
        elif random_number == 2:
            call ast_main("I'm not your pet, [ast_genie_name]...", "clench", "base", "base", "mid")
        elif random_number == 3:
            call ast_main("Oh sorry, my hand slipped.", "annoyed", "closed", "angry", "mid")
        elif random_number == 4:
            call ast_main("Do that again and you'll regret it...", "base", "base", "base", "mid")
        elif random_number == 5:
            call ast_main("Stop...", "base", "base", "base", "mid")
        elif random_number == 6:
            call ast_main("Don't!", "clench", "base", "base", "mid")
            $ mouse_slap()
            call ast_main("Don't!{fast} Do!", "clench", "narrow", "base", "mid")
            $ mouse_slap()
            call ast_main("Don't! Do!{fast} That!", "scream", "narrow", "angry", "mid")
            $ mouse_slap()
            call ast_main("Don't! Do! That!{fast} Again!", "scream", "closed", "angry", "mid")
            $ mouse_slap()
            call play_sound("kick")
            with hpunch
            pause 1.0
            g4 "(Ouch, that hurt!)"

    elif what == "breasts":
        $ random_number = renpy.random.randint(1, 7)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey, cut that out!", "angry", "narrow", "base", "mid")
        elif random_number == 2:
            call ast_main("Ouch, that hurts...", "base", "base", "angry", "mid")
        elif random_number == 3:
            call ast_main("Hey, no nipple twisters...", "clench", "base", "base", "mid")
        elif random_number == 4:
            call ast_main("Bad Touch!", "upset", "closed", "base", "mid")
        elif random_number == 5:
            call ast_main("*EEEH* Don't you have better things to do?", "scream", "closed", "angry", "mid")
        elif random_number == 6:
            call ast_main("{size=+5}What are you doing?{/size}", "scream", "narrow", "angry", "L")
        elif random_number == 7:
            call ast_main("Stop that!", "upset", "narrow", "base", "mid")

    elif what == "vagina":
        $ random_number = renpy.random.randint(1, 7)
        $ mouse_slap()

        if random_number == 1:
            call ast_main("Hey, that's private property.", "base", "narrow", "angry", "down")
        elif random_number == 2:
            call ast_main("Get your filthy hands off me, [ast_genie_name].", "upset", "narrow", "base", "mid")
        elif random_number == 3:
            call ast_main("Stop it, you creep.", "annoyed", "narrow", "angry", "R")
        elif random_number == 4:
            call ast_main("Why would you do that... nasty old man...", "clench", "narrow", "base", "L")
        elif random_number == 5:
            call ast_main("Don't touch me...", "clench", "base", "base", "mid")
        elif random_number == 6:
            call ast_main("Don't be gross, [ast_genie_name].", "base", "base", "base", "mid")
        elif random_number == 7:
            call ast_main("...", "clench", "closed", "base", "mid")
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
        call ast_main("*Nuh-uh*, I'm not putting that on.", "clench", "closed", "base", "mid")
    elif random_number == 2:
        call ast_main("*Pfff* You want me to wear that? In your dreams old man...", "annoyed", "narrow", "angry", "R")
    else:
        call ast_main("Don't be such a creep, thanks but no thanks.", "upset", "narrow", "base", "mid")

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

        call ast_main("Like hell! Take off your own panties old man...", "clench", "closed", "base", "mid")

        show screen blkfade
        with d5

        $ renpy.sound.play("sounds/zipper.mp3")
        call ast_main("W-What are you doing?!", "scream", "narrow", "angry", "L")
        call play_sound("thump")
        with hpunch
        pause 0.5
        call ast_main("Oh my god-- is that...?!", "upset", "narrow", "base", "mid")
        g9 "..."
        $ mouse_slap()
        with vpunch

        hide screen blkfade
        with d5

        g4 "Did you really have to slap me?"
        call ast_main("You deserved it you perverted... Pervert!", "scream", "closed", "angry", "mid")

    elif item.type == "bra":
        call ast_main("Why would you even suggest that?", "clench", "closed", "base", "mid")

    elif item.type == "top":
        call ast_main("Ha! Keep dreaming old man!", "smile", "narrow", "base", "mid")

    elif item.type == "bottom":
        call ast_main("My bottoms stay where they are and that's final!", "annoyed", "narrow", "angry", "R")
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

    call ast_main("That's way beyond what I would consider dignified.", "annoyed", "narrow", "angry", "R")

    if susan_unlocked:
        call ast_main("Consider asking Susan instead.", "base", "narrow", "base", "mid")
        call ast_main("I'm sure she'd enjoy wearing it for you, that cow.", "smile", "narrow", "base", "R")

    return

label ast_reaction_blacklist(item):
    call ast_main("Aren't you demanding too much, [ast_genie_name]?", "annoyed", "narrow", "base", "R")

    if "top" in item.blacklist and astoria.is_worn("top"):
        call ast_main("My topmost garment won't work with that.", "upset", "base", "base", "mid")

    if "bottom" in item.blacklist and astoria.is_worn("bottom"):
        call ast_main("Wearing bottoms with this would be a fashion-crime.", "clench", "base", "base", "mid")

    if "bra" in item.blacklist and astoria.is_worn("bra"):
        call ast_main("I'd have to take off my bra.", "base", "base", "base", "down")

    if "panties" in item.blacklist and astoria.is_worn("panties"):
        call ast_main("How do I even wear panties with that?", "annoyed", "base", "base", "down")

    call ast_main("This is stupid...", "base", "base", "base", "mid")

    if susan_unlocked:
        m "Perhaps I'll ask Susan instead--"

    call ast_main("J-Just give me that!", "annoyed", "base", "base", "L")

    return
