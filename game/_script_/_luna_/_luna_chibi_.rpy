label lun_chibi(action=None, xpos=None, ypos=None, flip=False):
    hide screen luna_chibi_scene # screen tag

    $ luna_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ luna_chibi.hide()
        return
    elif action == "leave":
        hide screen luna_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ luna_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ luna_chibi.do(None)
        return

    $ luna_chibi.do(action)

    return

label lun_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call lun_chibi(None, "door", "base", False)
        with d3
        if xpos or ypos:
            $ luna_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ luna_chibi.show()
        $ luna_chibi.move(("door", "base"), speed, reduce)
        call play_sound("door")
        $ luna_chibi.hide()
        with d3
        pause .5
    elif path:
        $ luna_chibi.show()
        $ luna_chibi.move(path, speed, reduce)
    else:
        $ luna_chibi.show()
        $ luna_chibi.move((xpos, ypos), speed, reduce)

    return

# Chibi definition
default luna_chibi = Chibi("luna", ["base"], update_luna_chibi, actions=luna_chibi_actions)

define luna_chibi_actions = {
    "lie": (False, "chibi_lie", "float_move"),
    "float_move": (False, "chibi_float_move", 0)
}

init python:
    def update_luna_chibi(chibi):
        if chibi.action == "walk":
            if luna.is_worn("robe"):
                chibi["base"] = "ch_lun walk_robe"
            elif luna.is_worn("top") and luna.is_worn("bottom"):
                chibi["base"] = "ch_lun walk_a"
            elif luna.is_worn("bottom"):
                chibi["base"] = "ch_lun walk_topless"
            else:
                chibi["base"] = "ch_lun walk_n"

        elif not chibi.action or chibi.action in ("stand", "lie", "float_move"):
            if luna.is_worn("robe"):
                chibi["base"] = "ch_lun blink_robe"
            elif luna.is_worn("top") and luna.is_worn("bottom"):
                chibi["base"] = "ch_lun blink_a"
            elif luna.is_worn("bottom"):
                chibi["base"] = "ch_lun blink_topless"
            else:
                chibi["base"] = "ch_lun blink_n"

        else:
            # Assume chibi action has a matching image definition
            chibi_image = "ch_lun {}".format(chibi.action or "stand")
            chibi["base"] = chibi_image
