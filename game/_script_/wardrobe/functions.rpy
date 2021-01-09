init python:
    def get_character_progression(key):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        if key == "tonks":
            return ton_friendship
        return getattr(store, "{}_whoring".format(key[:3]))

    def get_character_requirement(key, type):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(renpy.store, key[:3]+"_requirements").get(type, 0)

    def get_character_response(key, type):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(renpy.store, key[:3]+"_responses").get(type)

    def get_character_object(key):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, key)

    def get_character_outfit(key, type="default"):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, "{}_outfit_{}".format(key[:3], type))

    def get_character_outfit_req(key, item):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))

        if not isinstance(item, DollOutfit):
            raise TypeError("'{}' is not a DollOutfit instance.".format(item))

        req = ["{}: {}".format(i.type, i.level) for i in item.group]
        has_bra = any(i.type == "bra" for i in item.group)
        has_panties = any(i.type == "panties" for i in item.group)

        if not has_bra:
            req += ["NO BRA: {}".format(get_character_requirement(key, "category upper undergarment"))]

        if not has_panties:
            req += ["NO PANTIES: {}".format(get_character_requirement(key, "category lower undergarment"))]
        print "\n".join(req)

    def get_character_outfit_hash(key):
        ### Untested ###
        char = get_character_object(key)
        clothes = [x[0] for x in char.clothes.itervalues() if x[0]]
        salt = str( sorted([ sorted([x.name, x.type, x.id, x.color]) for x in clothes ]) )
        return hash(salt)

    def get_character_screen(key):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key))
        return "{}_main".format(key)

    def get_character_label(key):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key[:3]))
        return "{}_main".format(key[:3])

    def get_character_gift_label(key):
        if not key in CHARACTERS:
            raise KeyError("'{}' character is undefined.".format(key[:3]))
        return "give_{}_gift".format(key[:3])

    ### Outdated, kept for reference.
    # def get_character_score(key):
    #     """Returns character outfit outrage score number"""
    #     score = 0
    #     char = get_character_object(key)
    #     for k, i in char.clothing.iteritems():
    #         if i[0] != None:
    #             if not i[0].type in ("tattoo0", "tattoo1", "piercing0", "piercing1", "buttplug"):
    #                 score += i[0].whoring
    #         else:
    #             if k == "top":
    #                 score += 30
    #                 if not char.get_worn("bra"):
    #                     score += 25
    #                     if char.get_worn("piercing1"):
    #                         score += 10
    #                     if char.get_worn("tattoo1"):
    #                         score += char.get_cloth("tattoo1").whoring
    #             elif k == "bra" and char.get_worn("top"):
    #                 score += 10
    #             elif k == "bottom":
    #                 score += 30
    #                 if char.get_worn("buttplug"):
    #                     score += 10
    #                 if not char.get_worn("panties"):
    #                     score += 25
    #                     if char.get_worn("buttplug"):
    #                         score += 25
    #                     if char.get_worn("piercing0"):
    #                         score += 10
    #                     if char.get_worn("tattoo0"):
    #                         score += char.get_cloth("tattoo0").whoring
    #             elif k == "panties" and char.get_worn("bottom"):
    #                 score += 15
    #     return score

    def mouse_slap():
        """Causes the mouse to be moved away from current position and displays a smoke effect"""
        renpy.play('sounds/slap.mp3')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        xx = x+random.randint(-100, 100)
        yy = y+random.randint(-100, 100)
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=xx, target_y=yy, img="smoke", xanchor=0.1, yanchor=0.7, zoom=0.2, duration=0.15)
        renpy.set_mouse_pos(xx, yy, duration=0.1)

    def mouse_headpat():
        """Causes the mouse to be moved away from current position and displays a heart effect"""
        renpy.play('sounds/slap_03.mp3')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        xx, yy = x, y-15
        img = At(Text("*pat*", size=16, color="#000000CC", outlines=[(1, "#FFFFFFCC", 0, 0)]), random_rotation)
        renpy.hide_screen("gfx_effect")
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=xx, target_y=yy, img=img, xanchor=0.5, yanchor=0.65, zoom=1.0, timer=0.35)

    def mouse_heart():
        """Causes the mouse to be moved away from current position and displays a heart effect"""
        renpy.play('sounds/kiss.mp3')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=x, target_y=y, img="love_heart", xanchor=0.45, yanchor=0.65, zoom=0.2, timer=0.45)

    def wardrobe_fail_hint(value):
        """Displays required whoring/friendship/affection level."""
        word_list = {"tonks": "friendship", "astoria": "affection", "susan": "confidence", "luna": "corruption", "cho": "recklessness", "hermione": "whoring"}
        word = word_list.get(active_girl, "whoring")

        if game.cheats or game.difficulty <= 2:
            renpy.show_screen("blktone")
            renpy.with_statement(d3)
            renpy.say(None, "{size=+6}> Try again at "+word+" level {color=#7a0000}"+str(value)+"{/color}.{/size}")
            renpy.hide_screen("blktone")
            renpy.with_statement(d3)
        return

    def list_outfit_files():
        path = "{}/outfits/".format(config.gamedir)

        if not os.path.exists(path):
            os.makedirs(path)

        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith(".png")]
