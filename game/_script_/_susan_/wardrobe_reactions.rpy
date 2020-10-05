define sus_requirements = {
    "change_underwear": 5,
    "unequip_underwear": 15,
    "unequip_clothes": 3,
    "tattoos": 18,
    "headpat": 4,
    "touch_boobs": 12,
    "touch_pussy": 18
    }

label susan_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if sus_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if sus_whoring < sus_requirements["change_underwear"]:
                                temp_count[1] += 1

        # Outfit outrage score check
        if sus_whoring < temp_count[0]:
            call sus_main("You're joking right? Why would you think I would ever put this on...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and sus_whoring < sus_requirements["unequip_underwear"]:
            if temp_score > 0:
                call sus_main("... There's no underwear on that... What kind of pervert created this?",face="annoyed")
            else:
                call sus_main("No panties? I'd rather keep mine on thank you very much...",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call sus_main("I prefer wearing the underwear I have on already...",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call sus_main("Sorry, [ast_genie_name] but I won't wear that.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], sus_requirements["change_underwear"], sus_requirements["unequip_underwear"]))
            return
    else:
        if section == "tabswitch":
            if sus_whoring < sus_requirements["tattoos"]:
                if wardrobe_chitchats:
                    call sus_main("Cool idea!",face="happy")
                    call sus_main("Maybe for an idiot like you!",face="angry")
                #Hint
                $ wardrobe_fail_hint(sus_requirements["tattoos"])
                return False
            return True
        elif section == "category":
            # TODO: Simplify
            python:
                _value = arg
                _failure = False
                if arg[1] in ("bras", "panties"): # Intentional double check.
                    if sus_whoring < sus_requirements["change_underwear"]:
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
                call sus_main("Forget it old man.", face="annoyed")
                $ wardrobe_fail_hint(sus_requirements["change_underwear"])
            return _value
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 7)
            if arg == "head":
                if sus_whoring < sus_requirements["headpat"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call sus_main("Hey!", face="angry")
                        elif random_number == 2:
                            call sus_main("I'm not your pet, [ast_genie_name]...", face="annoyed")
                        elif random_number == 3:
                            call sus_main("Oh sorry, my hand slipped.", face="happy")
                        elif random_number == 4:
                            call sus_main("Do that again and you'll regret it...", face="angry")
                        elif random_number == 5:
                            call sus_main("Stop...", face="angry")
                        elif random_number == 6:
                            call sus_main("Don't!", face="angry")
                            $ mouse_slap()
                            call sus_main("Don't!{fast} Do!", face="angry")
                            $ mouse_slap()
                            call sus_main("Don't! Do!{fast} That!", face="angry")
                            $ mouse_slap()
                            call sus_main("Don't! Do! That!{fast} Again!", face="angry")
                            $ mouse_slap()
                            call play_sound("kick")
                            with hpunch
                            pause 1.0
                            g4 "(Ouch, that hurt!)"
                        return
                else:
                    $ mouse_headpat()
                    call sus_main("", face="happy")
                    return
            elif arg == "boobs":
                if sus_whoring < sus_requirements["touch_boobs"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call sus_main("Hey, cut that out!",face="annoyed",mouth="clench")
                        elif random_number == 2:
                            call sus_main("Ouch, that hurts...",face="annoyed",mouth="scream")
                        elif random_number == 3:
                            call sus_main("Hey, no nipple twisters...",face="annoyed")
                        elif random_number == 4:
                            call sus_main("Bad Touch!",face="annoyed")
                        elif random_number == 5:
                            call sus_main("*EEEH* Don't you have better things to do?",face="annoyed")
                        elif random_number == 6:
                            call sus_main("{size=+5}What are you doing?{/size}",face="angry",mouth="scream")
                        elif random_number == 7:
                            call sus_main("Stop that!",face="annoyed")
                    return
            elif arg == "pussy":
                if sus_whoring < sus_requirements["touch_pussy"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call sus_main("Hey, that's private property.",face="annoyed")
                        elif random_number == 2:
                            call sus_main("Get your filthy hands off me, [ast_genie_name].",face="annoyed")
                        elif random_number == 3:
                            call sus_main("Stop it, you creep.",face="annoyed")
                        elif random_number == 4:
                            call sus_main("Why would you do that... nasty old man...",face="annoyed")
                        elif random_number == 5:
                            call sus_main("Don't touch me...",face="annoyed")
                        elif random_number == 6:
                            call sus_main("Don't be gross, [ast_genie_name].",face="annoyed")
                        elif random_number == 7:
                            call sus_main("...",face="annoyed")
                    return
            $ mouse_heart()
            call sus_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if sus_whoring < sus_requirements["unequip_underwear"]:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 2)
                        if random_number == 1:
                            call sus_main("*Eeeh* No?",face="angry")
                        elif random_number == 2:
                            call sus_main("I'd rather keep my underwear on...",face="angry")
                    #Hint
                    $ wardrobe_fail_hint(sus_requirements["unequip_underwear"])
                    return
            elif arg in ("top", "bottom"):
                if sus_whoring < sus_requirements["unequip_clothes"]:
                    if wardrobe_chitchats:
                        if arg == "top":
                            call sus_main("You want me to take my clothes off... Oh sure, I'll just go ahead and bare my chest and all as well then shall I?",face="annoyed")
                            g4 "Really?!"
                            call sus_main("{size=+5}NO!{/size}",face="annoyed",mouth="scream")
                            m "......"
                        elif arg == "bottom":
                            call sus_main("{size=+5}No, get away from me!{/size}",face="annoyed",mouth="scream")
                    #Hint
                    $ wardrobe_fail_hint(sus_requirements["unequip_clothes"])
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if sus_whoring < sus_requirements["unequip_underwear"]:
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call sus_main("I'd rather not do that right now, [ast_genie_name].",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(sus_requirements["unequip_underwear"])
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call sus_main("I can't do that...",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(sus_requirements["unequip_underwear"])
                            return
                if sus_whoring < arg.level:
                    call .too_much
                    return
            else:
                if sus_whoring < sus_requirements["unequip_clothes"]:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call sus_main("I guess I could... but I'm not going to.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(sus_requirements["unequip_clothes"])
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call sus_main("Hey, that's a great idea... but not in this universe.",face="angry")
                                #Hint
                                $ wardrobe_fail_hint(sus_requirements["unequip_clothes"])
                                return

                label .too_much:
                if sus_whoring < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call sus_main("Nuh uh, I'm not putting that on.",face="annoyed")
                        elif random_number == 2:
                            call sus_main("*Pfff* You want me to wear that? In your dreams old man...",face="annoyed")
                        else:
                            call sus_main("Don't be such a creep, thanks but no thanks.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

                # Blacklist support
                if arg.blacklist:
                    if sus_whoring < sus_requirements["unequip_underwear"] and any(x in arg.blacklist for x in ("bra", "panties")):
                        call sus_main("How am I supposed to wear my underwear with this?!", face="angry")
                        call sus_main("I guess I could take it off for now...", face="annoyed")
                    elif sus_whoring < sus_requirements["unequip_clothes"] and any(x in arg.blacklist for x in ("top", "bottom")):
                        call sus_main("This looks stupid!", face="angry")
                        call sus_main("...", face="annoyed")
                        call sus_main("J-just give me that!", face="angry")
                        call sus_main("", face="annoyed")

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and current_item.type != "hair" and char_active.is_equipped(current_item.type) and char_active.get_equipped(current_item.type) == current_item:
        $ char_active.unequip(current_item.type)
        $ current_item = None
    else:
        $ char_active.equip(current_item)
    $ char_active.reset_blacklist()

    # Blacklist fallbacks
    if sus_whoring < sus_requirements["unequip_underwear"]:

        $ underwear_pass = True

        if not "bra" in char_active.blacklist and not char_active.is_equipped("bra"):
            $ underwear_pass = False
            $ char_active.equip(sus_bra_base1)

        if not char_active.is_equipped("panties") and not "panties" in char_active.blacklist:
            $ underwear_pass = False
            $ char_active.equip(sus_panties_base1)

        if not underwear_pass:
            call sus_main("I'm glad to have my underwear back.", face="annoyed")

    if sus_whoring < sus_requirements["unequip_clothes"]:
        $ clothes_pass = True

        if not "top" in char_active.blacklist and not char_active.is_equipped("top"):
            $ clothes_pass = False
            $ char_active.equip(sus_top_school1)

        if not char_active.is_equipped("bottom") and not "bottom" in char_active.blacklist:
            $ clothes_pass = False
            $ char_active.equip(sus_bottom_school1)

        if not clothes_pass:
            call sus_main("I missed my old clothes so much, thanks!", face="happy")
    return
