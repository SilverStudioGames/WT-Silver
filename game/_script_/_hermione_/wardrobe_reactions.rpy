define her_requirements = {
    "change_underwear": 5,
    "unequip_underwear": 15,
    "unequip_clothes": 3,
    "tattoos": 18,
    "headpat": 4,
    "touch_boobs": 12,
    "touch_pussy": 18
    }

label hermione_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if her_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if her_whoring < her_requirements["change_underwear"]:
                                temp_count[1] += 1

        # Outfit outrage score check
        if her_whoring < temp_count[0]:
            call her_main("It's too "+random.choice(("slutty", "revealing", "much", "breezy"))+"...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and her_whoring < her_requirements["unequip_underwear"]:
            if temp_score > 0:
                call her_main("... not to mention missing underwear!",face="annoyed")
            else:
                call her_main("It's missing underwear!",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call her_main("I have told you before, I'm not letting you pick any underwear for me!",face="angry")
            $ temp_score += 1

        if temp_score > 0:
            call her_main("I am NOT wearing it!",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], her_requirements["change_underwear"], her_requirements["unequip_underwear"]))
            return
    else:
        if section == "category":
            # TODO: Simplify
            python:
                _value = arg
                _failure = False
                if arg[1] in ("bras", "panties"): # Intentional double check.
                    if her_whoring < her_requirements["change_underwear"]:
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
                call her_main("I won't let you pick underwear for me!", face="angry")
                $ wardrobe_fail_hint(her_requirements["change_underwear"])
            return _value
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 5)
            if arg == "head":
                if her_whoring < her_requirements["headpat"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call her_main("Hey!", "open", "narrow", "angry", "L")
                        elif random_number == 2:
                            call her_main("Bad [genie_name]!", "annoyed", "happyCl", "angry", "L", cheeks="blush")
                        elif random_number == 3:
                            call her_main("*Grrr*...", "clench", "base", "angry", "R")
                        elif random_number == 4:
                            call her_main("Cut it out..", "open", "narrow", "angry", "mid")
                        elif random_number == 5:
                            call her_main("Hands off me.", "mad", "wide", "angry", "mid")
                        return
                else:
                    $ mouse_headpat()
                    call her_main("", face="happy")
                    return
            elif arg == "boobs":
                if her_whoring < her_requirements["touch_boobs"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
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
                    return
            elif arg == "pussy":
                if her_whoring < her_requirements["touch_pussy"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
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
            $ mouse_heart()
            call her_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if her_whoring < her_requirements["unequip_underwear"]:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call her_main("I'm not gonna flash you anything!", "clench", "narrow", "angry", "mid")
                            call her_main("{size=-4}Pervert..{/size}", "annoyed", "narrow", "angry", "R")
                        elif random_number == 2:
                            call her_main("Take off my [arg]?! No way!", "clench", "narrow", "angry", "mid")
                            call her_main("", "annoyed", "narrow", "angry", "down")
                        else:
                            call her_main("I am not taking off my [arg]!", "clench", "narrow", "angry", "mid")
                            call her_main("", "annoyed", "narrow", "angry", "mid")
                    #Hint
                    $ wardrobe_fail_hint(her_requirements["unequip_underwear"])
                    return
            elif arg in ("top", "bottom"):
                if her_whoring < her_requirements["unequip_clothes"]:
                    if wardrobe_chitchats:
                        if arg == "top":
                            call her_main("Take my top off? Are you crazy?", "annoyed", "narrow", "angry", "L")
                        elif arg == "bottom":
                            call her_main("Take my bottoms off so you can ogle my ass? No thank you.", "open", "narrow", "angry", "mid")
                    #Hint
                    $ wardrobe_fail_hint(her_requirements["unequip_clothes"])
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if her_whoring < her_requirements["unequip_underwear"]:
                    if char_active.is_item_equipped(arg):
                        if wardrobe_chitchats:
                            call her_main("No, I'm not taking off my [arg.type]!", "clench", "wide", "angry", "mid")
                        #Hint
                        $ wardrobe_fail_hint(her_requirements["unequip_underwear"])
                        return

                if her_whoring < arg.level:
                    call .too_much
                    return
            elif arg.type in ("top", "bottom"):
                if her_whoring < her_requirements["unequip_clothes"]:
                    if char_active.is_item_equipped(arg):
                        if wardrobe_chitchats:
                            call her_main("I am not taking off my clothes, forget it!", "annoyed", "narrow", "angry", "L", cheeks="blush")
                        #Hint
                        $ wardrobe_fail_hint(her_requirements["unequip_clothes"])
                        return
            else:

                label .too_much:
                if her_whoring < arg.level:
                    if wardrobe_chitchats:
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
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

                # Blacklist support
                if arg.blacklist:
                    if her_whoring < her_requirements["unequip_underwear"] and any(x in arg.blacklist for x in ("bra", "panties")):
                        call her_main("I can't wear underwear with this!", "annoyed", "narrow", "angry", "L", cheeks="blush")
                        call her_main("Fine! I'll wear this stupid thing.", "disgust", "narrow", "angry", "down", cheeks="blush")
                    elif her_whoring < her_requirements["unequip_clothes"] and any(x in arg.blacklist for x in ("top", "bottom")):
                        call her_main("Do I have to wear this?", "open", "narrow", "angry", "mid")
                        call her_main("Fine, I'll wear it... but I'm putting my old clothes back on once you change your mind.", "annoyed", "narrow", "angry", "R", cheeks="blush")

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and char_active.is_item_equipped(current_item):
        $ char_active.unequip(current_item.type)
        $ current_item = None
    else:
        $ char_active.equip(current_item)

    # Blacklist fallbacks
    if her_whoring < her_requirements["unequip_underwear"]:
        $ underwear_pass = True

        if not "bra" in char_active.blacklist and not char_active.is_equipped("bra"):
            $ underwear_pass = False
            $ char_active.equip(her_bra_base1)

        if not char_active.is_equipped("panties") and not "panties" in char_active.blacklist:
            $ underwear_pass = False
            $ char_active.equip(her_panties_base1)

        if not underwear_pass:
            call her_main("I'm putting my underwear back on then!", "open", "closed", "angry", "mid", cheeks="blush")
            call her_main("", "normal", "base", "worried", "mid", cheeks="blush")

    if her_whoring < her_requirements["unequip_clothes"]:
        $ clothes_pass = True

        if not "top" in char_active.blacklist and not char_active.is_equipped("top"):
            $ clothes_pass = False
            $ char_active.equip(her_top_school1)

        if not char_active.is_equipped("bottom") and not "bottom" in char_active.blacklist:
            $ clothes_pass = False
            $ char_active.equip(her_bottom_school1)

        if not clothes_pass:
            call her_main("In that case I'm putting my old clothes back on!", "open", "closed", "angry", "mid", cheeks="blush")
            call her_main("", "normal", "base", "worried", "mid", cheeks="blush")
    return
