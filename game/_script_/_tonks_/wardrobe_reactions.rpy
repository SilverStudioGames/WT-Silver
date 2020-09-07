define ton_requirements = {
    "change_underwear": 10,
    "unequip_underwear": 0,
    "unequip_clothes": 20,
    "tattoos": 60,
    "headpat": 50,
    "touch_boobs": 20,
    "touch_pussy": 40
    }

label tonks_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if ton_friendship < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if ton_friendship < ton_requirements["change_underwear"]:
                                temp_count[1] += 1

        # Outfit outrage score check
        if ton_friendship < temp_count[0]:
            call ton_main("It looks lovely, but you'd have to prove yourself a bit more before I put that on...",face="annoyed",eyebrows="angry",mouth="grin")
            $ temp_score += 1
        if temp_count[2] < 2 and ton_friendship < ton_requirements["unequip_underwear"]:
            if temp_score > 0:
                call ton_main("... especially something without underwear",face="annoyed",eyebrows="angry",mouth="horny")
            else:
                call ton_main("No panties? I like that, but no thanks, I'm at work.",face="annoyed",eyebrows="angry",mouth="base")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ton_main("I feel perfectly fine NOT having to wear underwear.",face="neutral")
            $ temp_score += 1

        if temp_score > 0:
            call ton_main("Sorry, [ton_genie_name] but I can't wear that.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], ton_requirements["change_underwear"], ton_requirements["unequip_underwear"]))
            return
    else:
        if section == "tabswitch":
            if ton_friendship < ton_requirements["tattoos"]:
                if wardrobe_chitchats:
                    call ton_main("As much as I'd like to get a new piercing or a tattoo I can't simply let you modify my body like that.",face="annoyed")
                #Hint
                $ wardrobe_fail_hint(ton_requirements["tattoos"])
                return False
            return True
        elif section == "category":

            # Haircolour Fix
            if arg[1] == "head":
                $ tonks.get_equipped("hair").set_color(tonks_haircolor)
            else:
                if tonks_haircolor != tonks.get_equipped("hair").color:
                    $ tonks_haircolor = tonks.get_equipped("hair").color

            # TODO: Simplify
            python:
                _value = arg
                _failure = False
                if arg[1] in ("bras", "panties"): # Intentional double check.
                    if ton_friendship < ton_requirements["change_underwear"]:
                        _value = ("category", None)
                        _failure = True

                    for i in char_active.clothes.itervalues():
                        if i[0]:
                            if i[0].blacklist and "bra" in i[0].blacklist and arg[1] == "bras":
                                _value = ("category", None)
                                break
                            if i[0].blacklist and "panties" in i[0].blacklist and arg[1] == "panties":
                                _value = ("category", None)
                                break
            if _failure:
                $ renpy.play('sounds/fail.mp3')
                call ton_main("Underwear? Puh-lease, only a prude would wear something silly like that.", face="neutral")
                $ wardrobe_fail_hint(ton_requirements["change_underwear"])
            return _value
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 6)
            if arg == "head":
                if ton_friendship < ton_requirements["headpat"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
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
                        return
                else:
                    $ mouse_headpat()
                    call ton_main("", face="happy")
                    return
            elif arg == "boobs":
                if ton_friendship < ton_requirements["touch_boobs"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
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
                    return
            elif arg == "pussy":
                if ton_friendship < ton_requirements["touch_pussy"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
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
            $ mouse_heart()
            call ton_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if ton_friendship < ton_requirements["unequip_underwear"]:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 2)
                        if random_number == 1:
                            call ton_main("Maybe another time...",face="annoyed",eyebrows="raised")
                        elif random_number == 2:
                            call ton_main("I like my underwear in its proper place.",face="annoyed",eyebrows="base",mouth="angry")
                    #Hint
                    $ wardrobe_fail_hint(ton_requirements["unequip_underwear"])
                    return
            elif arg in ("top", "bottom"):
                if ton_friendship < ton_requirements["unequip_clothes"]:
                    if wardrobe_chitchats:
                        call ton_main("Someone's being naughty... I might have to give you a spanking for that.",face="annoyed",eyebrows="angry",mouth="grin")
                        call ton_main("Just kidding! Sure, have a quick look, [ton_genie_name].",face="annoyed",eyebrows="raised",mouth="horny")
                        $ char_active.toggle_wear(arg)
                        $ char_active.strip("robe")
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        $ char_active.toggle_wear(arg)
                        $ char_active.wear("robe")
                        g4 "What gives?!"
                        call ton_main("Time's up.",face="annoyed",eyebrows="angry",mouth="grin")
                        m "......"
                    #Hint
                    $ wardrobe_fail_hint(ton_requirements["unequip_clothes"])
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if ton_friendship < ton_requirements["unequip_underwear"]:
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call ton_main("If you behave maybe I'll let you take a peek later, [ton_genie_name].",face="annoyed",eyebrows="angry",mouth="grin")
                            #Hint
                            $ wardrobe_fail_hint(ton_requirements["unequip_underwear"])
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call ton_main("",face="happy")
                                nar "> Tonks clicks her tongue, staring at you in a disapproving manner."
                                call ton_main("Getting ahead of ourselves are we? You're bold, I'll give you that much.",face="annoyed",eyebrows="angry",mouth="grin")
                            #Hint
                            $ wardrobe_fail_hint(ton_requirements["unequip_underwear"])
                            return
                if ton_friendship < arg.level:
                    call .too_much
                    return
            else:
                if ton_friendship < ton_requirements["unequip_clothes"]:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call ton_main("*Mmm*... I like where your head is at, but I have to refuse.",face="annoyed",eyebrows="angry",mouth="grin")
                                #Hint
                                $ wardrobe_fail_hint(ton_requirements["unequip_clothes"])
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call ton_main("Really... doing that would be quite uncouth don't you think?",face="annoyed",eyebrows="angry",mouth="horny")
                                #Hint
                                $ wardrobe_fail_hint(ton_requirements["unequip_clothes"])
                                return

                label .too_much:
                if ton_friendship < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call ton_main("Not yet big boy, perhaps once this scheme of ours comes more into fruition...",face="annoyed",eyebrows="angry",mouth="grin")
                        elif random_number == 2:
                            call ton_main("It does look nice but you need to deserve it...",face="annoyed",eyebrows="angry",mouth="grin")
                        else:
                            call ton_main("Hmm, what would you think of me if I wore this...? Later perhaps.",face="annoyed",eyebrows="raised",mouth="horny")
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

                # Blacklist support
                if arg.blacklist:
                    if ton_friendship < ton_requirements["unequip_underwear"] and any(x in arg.blacklist for x in ("bra", "panties")):
                        call ton_main("I like how it accents my figure and forbids me from wearing underwear.", face="horny")
                    elif ton_friendship < ton_requirements["unequip_clothes"] and any(x in arg.blacklist for x in ("top", "bottom")):
                        call ton_main("You really want me to whore myself up *huh*? Fine, but I'm putting my old clothes back on once you change your mind.", face="happy")

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and current_item.type != "hair" and char_active.is_equipped(current_item.type) and char_active.clothes[current_item.type][0].id == current_item.id:
        $ char_active.unequip(current_item.type)
    else:
        $ char_active.equip(current_item)
    $ char_active.reset_blacklist()

    # NOTE: Tonks does not utilize underwear checks, she's supposed to not wear them and will refuse to wear any underwear until higher friendship level.
    # Blacklist fallbacks
    # if ton_friendship < ton_requirements["unequip_underwear"]:

        # $ underwear_pass = True

        # if not "bra" in char_active.blacklist and not char_active.is_equipped("bra"):
            # $ underwear_pass = False
            # $ char_active.equip(ton_bra_base)

        # if not char_active.is_equipped("panties") and not "panties" in char_active.blacklist:
            # $ underwear_pass = False
            # $ char_active.equip(ton_panties_base)

        # if not underwear_pass:
            # call ton_main("Time to put back on my undies.", face="neutral")

    if ton_friendship < ton_requirements["unequip_clothes"]:
        $ clothes_pass = True

        if not "top" in char_active.blacklist and not char_active.is_equipped("top"):
            $ clothes_pass = False
            $ char_active.equip(ton_top_auror)

        if not char_active.is_equipped("bottom") and not "bottom" in char_active.blacklist:
            $ clothes_pass = False
            $ char_active.equip(ton_bottoms_leggings)

        if not clothes_pass:
            call ton_main("Time to put back on my clothes.", face="neutral")
    return
