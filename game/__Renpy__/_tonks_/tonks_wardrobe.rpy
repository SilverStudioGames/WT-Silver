label tonks_wardrobe_check(section, arg=None):
    if isinstance(arg, outfit_class):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if ton_friendship < item.whoring*2 and temp_count[0]*2 < item.whoring*2:
                    temp_count[0] = item.whoring
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_cloth(item.type) != None:
                        if not char_active.get_cloth(item.type).id == item.id:
                            if ton_friendship < 15:
                                temp_count[1] += 1

        # Outfit outrage score check
        if ton_friendship < temp_count[0]*2:
            call ton_main("It looks lovely, but you'd have to prove yourself a bit more before I put that on...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and ton_friendship < 20:
            if temp_score > 0:
                call ton_main("...especially something without underwear",face="annoyed")
            else:
                call ton_main("No panties? I like that, but no thanks, I'm at work.",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ton_main("I feel perfectly fine wearing my current set of underwear for the time being.",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call ton_main("Sorry, [ton_genie_name] but I can't wear that.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0]*2, 15, 20))
            return
    else:
        if section == "tabswitch":
            # Need more art
            $ TBA_message()
            return False

            # if ton_friendship < 24:
                # call ton_main("As much as I'd like to get a new piercing or a tattoo I can't simply let you modify my body like that.",face="angry")
                # #Hint
                # $ wardrobe_fail_hint(24)
                # return False
            # return True
        elif section == "category":
            #haircolour fix
            if arg[1] == "head":
                call ton_main("",face="neutral")
                $ tonks_class.get_cloth("hair").color = tonks_haircolor
            return arg #IMPORTANT
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 10)
            if arg == "boobs":
                if ton_friendship < 20:
                    $ slap_mouse_away()

                    if random_number == 1:
                        call ton_main("That's not how a headmaster should treat their subordinates.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("Its inappropriate, lets keep it civil okay?",face="annoyed")
                    elif random_number == 3:
                        call ton_main("Someone fancy themselves a bit of a bad boy?",face="annoyed")
                    elif random_number == 4:
                        call ton_main("Hey, those are my funbags... Don't be naughty.",face="annoyed")
                    elif random_number == 5:
                        call ton_main("Hey now, someone's getting a bit ahead of themselves.",face="annoyed")
                    elif random_number == 6:
                        call ton_main("Those aren't for you to play with...",face="annoyed")
                    return
            if arg == "pussy":
                if ton_friendship < 30:
                    $ slap_mouse_away()

                    if random_number == 1:
                        call ton_main("You have to to earn it first.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("If you'd like to keep these hands intact I suggest you stop it right now, [ton_genie_name].",face="annoyed")
                    elif random_number == 3:
                        call ton_main("Hey, who said you had permission to approach the chamber of secrets?",face="annoyed")
                    elif random_number == 4:
                        call ton_main("That place is reserved for good boys and girls...",face="annoyed")
                    elif random_number == 5:
                        call ton_main("That forest is forbidden entry for first years... let's get to know each other a bit better first...",face="annoyed")
                    return
            $ love_mouse_away()
            call ton_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if ton_friendship < 15:
                    $ random_number = renpy.random.randint(1, 2)
                    if random_number == 1:
                        call ton_main("Maybe another time...",face="angry")
                    elif random_number == 2:
                        call ton_main("I like my underwear in its proper place.",face="angry")
                    #Hint
                    $ wardrobe_fail_hint(15)
                    return
            elif arg in ("top", "bottom"):
                if ton_friendship < 10:
                    if arg == "top":
                        call ton_main("Someone's being naughty... I might have to give you a spanking for that.",face="annoyed")
                        call ton_main("Just kidding, sure have a quick look, [ton_genie_name].",face="annoyed")
                        $ char_active.toggle_wear(arg)
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        $ char_active.toggle_wear(arg)
                        g4 "What gives?!"
                        call ton_main("Time's up.",face="annoyed")
                        m "......"
                    elif arg == "bottom":
                        call ton_main("Maybe later.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if ton_friendship < 20:
                    if char_active.get_cloth("bra"):
                        if arg.id == char_active.get_cloth("bra").id:
                            call ton_main("If you behave maybe I'll let you take a peek later, [ton_genie_name].",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                    if char_active.get_cloth("panties"):
                        if arg.id == char_active.get_cloth("panties").id:
                            call ton_main("",face="happy")
                            nar "> Tonks clicks her tongue, staring at you in a disapproving manner."
                            call ton_main("Getting ahead of ourselves are we? You're bold, I'll give you that much.",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                else:
                    if ton_friendship < arg.whoring:
                        call tonks_wardrobe_too_much
                        return
            else:
                if ton_friendship < 30:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_cloth("top"):
                            if arg.id == char_active.get_cloth("top").id:
                                call ton_main("Mmm... I like where your head is at, but I have to refuse.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                        if char_active.get_cloth("bottom"):
                            if arg.id == char_active.get_cloth("bottom").id:
                                call ton_main("Really... doing that would be quite uncouth don't you think?",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                label tonks_wardrobe_too_much:
                if ton_friendship < arg.whoring*2:
                    $ random_number = renpy.random.randint(1, 3)
                    if random_number == 1:
                        call ton_main("Not yet big boy, perhaps once this scheme of ours comes more into fruition...",face="annoyed")
                    elif random_number == 2:
                        call ton_main("It does look nice but you need to deserve it...",face="annoyed")
                    else:
                        call ton_main("Hmm, what'd you think of me if I wore this... Later perhaps.",face="annoyed")

                    #Hint
                    $ wardrobe_fail_hint(arg.whoring*2)
                    return

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    $ char_active.equip(current_item)
    return