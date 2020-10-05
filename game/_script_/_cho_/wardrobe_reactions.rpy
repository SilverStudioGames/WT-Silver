define cho_requirements = {
    "change_underwear": 5,
    "unequip_underwear": 15,
    "unequip_clothes": 3,
    "tattoos": 18,
    "headpat": 4,
    "touch_boobs": 12,
    "touch_pussy": 18
    }

label cho_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if cho_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if cho_whoring < cho_requirements["change_underwear"]:
                                temp_count[1] += 1

        # Outfit outrage score check
        if cho_whoring < temp_count[0]:
            call cho_main("It's too "+random.choice(("slutty", "revealing", "much", "breezy", "Granger like"))+"...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and cho_whoring < cho_requirements["unequip_underwear"]:
            if temp_score > 0:
                call cho_main("... not to mention missing underwear!",face="annoyed")
            else:
                call cho_main("It's missing underwear!",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call cho_main("I have told you before, I'm not letting you pick any underwear for me!",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call cho_main("I'm sorry [cho_genie_name] but that's too much.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], cho_requirements["change_underwear"], cho_requirements["unequip_underwear"]))
            return
    else:
        if section == "tabswitch":
            if cho_whoring < cho_requirements["tattoos"]:
                if wardrobe_chitchats:
                    call cho_main("Piercing and tattoos?", face="angry")
                    call cho_main("Why would I want that...",face="annoyed")
                #Hint
                $ wardrobe_fail_hint(cho_requirements["tattoos"])
                return False
            return True
        elif section == "category":
            # TODO: Simplify
            python:
                _value = arg
                _failure = False
                if arg[1] in ("bras", "panties"): # Intentional double check.
                    if cho_whoring < cho_requirements["change_underwear"]:
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
                call cho_main("I don't think so, [cho_genie_name].", face="annoyed")
                $ wardrobe_fail_hint(cho_requirements["change_underwear"])
            return _value
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 5)
            if arg == "head":
                if cho_whoring < cho_requirements["headpat"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call cho_main("No touching!",face="annoyed")
                        elif random_number == 2:
                            call cho_main("Bad [cho_genie_name]!",face="annoyed")
                        elif random_number == 3:
                            call cho_main("Hands to yourself.",face="annoyed")
                        elif random_number == 4:
                            call cho_main("Cut it out..",face="annoyed")
                        elif random_number == 5:
                            call cho_main("Hands off me.",face="annoyed")
                        return
                else:
                    $ mouse_headpat()
                    call cho_main("", face="happy")
                    return
            elif arg == "boobs":
                if cho_whoring < cho_requirements["touch_boobs"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call cho_main("No touching!",face="annoyed")
                        elif random_number == 2:
                            call cho_main("Bad [cho_genie_name]!",face="annoyed")
                        elif random_number == 3:
                            call cho_main("Hands to yourself.",face="annoyed")
                        elif random_number == 4:
                            call cho_main("Cut it out..",face="annoyed")
                        elif random_number == 5:
                            call cho_main("Hands off me.",face="annoyed")
                    return
            elif arg == "pussy":
                if cho_whoring < cho_requirements["touch_pussy"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call cho_main("Stop that!",face="annoyed")
                        elif random_number == 2:
                            call cho_main("[cho_genie_name]!",face="annoyed")
                        elif random_number == 3:
                            call cho_main("Unhand me..",face="annoyed")
                        elif random_number == 4:
                            call cho_main("Stop it please..",face="annoyed")
                        elif random_number == 5:
                            call cho_main("Hands off me.",face="annoyed")
                    return
            $ mouse_heart()
            call cho_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if cho_whoring < cho_requirements["unequip_underwear"]:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call cho_main("I'm not gonna flash you anything!",face="angry")
                            call cho_main("{size=-4}Pervert..{/size}",face="annoyed")
                        elif random_number == 2:
                            call cho_main("Take off my [arg]?! No way!",face="angry")
                            call cho_main("", face="annoyed")
                        else:
                            call cho_main("I am not taking off my [arg]!",face="angry")
                            call cho_main("", face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(cho_requirements["unequip_underwear"])
                    return
            elif arg in ("top", "bottom"):
                if cho_whoring < cho_requirements["unequip_clothes"]:
                    if wardrobe_chitchats:
                        if arg == "top":
                            call cho_main("Take my top off? Are you crazy?",face="annoyed")
                        elif arg == "bottom":
                            call cho_main("Take my bottoms off so you can ogle my ass? No thank you.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(cho_requirements["unequip_clothes"])
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if cho_whoring < cho_requirements["unequip_underwear"]:
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call cho_main("No, I'm not taking off my bra!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(cho_requirements["unequip_underwear"])
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call cho_main("No, I'm not taking off my panties!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(cho_requirements["unequip_underwear"])
                            return
                if cho_whoring < arg.level:
                    call .too_much
                    return
            else:
                if cho_whoring < cho_requirements["unequip_clothes"]:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call cho_main("I am not taking off my top, forget it!",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(cho_requirements["unequip_clothes"])
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call cho_main("I can't be walking bottomless on the quidditch grounds..",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(cho_requirements["unequip_clothes"])
                                return

                label .too_much:
                if cho_whoring < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 5)
                        if random_number == 1:
                            call cho_main("I'm not wearing that.",face="annoyed")
                        elif random_number == 2:
                            call cho_main("It's too slutty..",face="annoyed")
                        elif random_number == 3:
                            call cho_main("I would look like a tramp, I refuse.",face="annoyed")
                        elif random_number == 4:
                            call cho_main("I'm not Granger, [cho_genie_name]... Ask her to humiliate herself for your amusement..",face="angry")
                        elif random_number == 5:
                            call cho_main("You're asking too much.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

                # Blacklist support
                if arg.blacklist:
                    if cho_whoring < cho_requirements["unequip_underwear"] and any(x in arg.blacklist for x in ("bra", "panties")):
                        call cho_main("But my undies won't fit in it!", face="angry")
                        call cho_main("*sigh* fine...", face="annoyed")
                    elif cho_whoring < cho_requirements["unequip_clothes"] and any(x in arg.blacklist for x in ("top", "bottom")):
                        call cho_main("Do I have to wear this?", face="annoyed")
                        call cho_main("Alright, alright... But I'm putting my old clothes back on once you change your mind.", face="annoyed")

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and current_item.type != "hair" and char_active.is_equipped(current_item.type) and char_active.get_equipped(current_item.type) == current_item:
        $ char_active.unequip(current_item.type)
        $ current_item = None
    else:
        $ char_active.equip(current_item)
    $ char_active.reset_blacklist()

    # Blacklist fallbacks
    if cho_whoring < cho_requirements["unequip_underwear"]:

        $ underwear_pass = True

        if not "bra" in char_active.blacklist and not char_active.is_equipped("bra"):
            $ underwear_pass = False
            $ char_active.equip(cho_bra_basic1)

        if not char_active.is_equipped("panties") and not "panties" in char_active.blacklist:
            $ underwear_pass = False
            $ char_active.equip(cho_panties_basic1)

        if not underwear_pass:
            call cho_main("Finally I can put my underwear back on..", face="annoyed")

    if cho_whoring < cho_requirements["unequip_clothes"]:
        $ clothes_pass = True

        if not "top" in char_active.blacklist and not char_active.is_equipped("top"):
            $ clothes_pass = False
            $ char_active.equip(cho_top_school1)

        if not char_active.is_equipped("bottom") and not "bottom" in char_active.blacklist:
            $ clothes_pass = False
            $ char_active.equip(cho_bottom_school1)

        if not clothes_pass:
            call cho_main("Finally I can put my old clothes back on..", face="annoyed")
    return
