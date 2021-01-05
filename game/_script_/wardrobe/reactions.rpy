init python:
    def wardrobe_check_category(category):
        req = get_character_requirement(active_girl, "category {}".format(category))
        flag = get_character_progression(active_girl)

        return (flag >= req)

    def wardrobe_check_touch(what):
        req = get_character_requirement(active_girl, "touch {}".format(what))
        flag = get_character_progression(active_girl)

        return (flag >= req)

    def wardrobe_check_equip(item):
        req = item.level
        flag = get_character_progression(active_girl)

        return (flag >= req)

    def wardrobe_check_unequip(item):
        req = get_character_requirement(active_girl, "unequip {}".format(item.type))
        flag = get_character_progression(active_girl)

        return (flag >= req)

    def wardrobe_check_equip_outfit(item):
        req = max((i.level for i in item.group))
        flag = get_character_progression(active_girl)

        has_bra = any(i.type == "bra" for i in item.group)
        has_panties = any(i.type == "panties" for i in item.group)

        if not has_bra:
            req = max(req, wardrobe_check_category("upper undergarment"))

        if not has_panties:
            req = max(req, wardrobe_check_category("lower undergarment"))

        return (flag >= req)

    def wardrobe_check_blacklist(item):
        if not item.blacklist:
            return True

        req = max( ( get_character_requirement(active_girl, "unequip {}".format(i)) for i in item.blacklist ) )
        flag = get_character_progression(active_girl)

        return (flag >= req)

    def wardrobe_react(what, arg):
        if wardrobe_chitchats:
            renpy.call(get_character_response(active_girl, what), arg)
        return
