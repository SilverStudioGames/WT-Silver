label sus_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ susan_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ susan_chibi.hide()
        return
    elif action == "leave":
        hide screen susan_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ susan_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ susan_chibi.do(None)
        return

    $ susan_chibi.do(action)

    return

label sus_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call sus_chibi(None, "door", "base", False)
        with d3
        if xpos or ypos:
            $ susan_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ susan_chibi.show()
        $ susan_chibi.move(("door", "base"), speed, reduce)
        call play_sound("door")
        $ susan_chibi.hide()
        with d3
        pause .5
    elif path:
        $ susan_chibi.show()
        $ susan_chibi.move(path, speed, reduce)
    else:
        $ susan_chibi.show()
        $ susan_chibi.move((xpos, ypos), speed, reduce)
    return

# Chibi definition
default susan_chibi = Chibi("susan", ["base", "shoes", "top", "bottom", "robe"], update_susan_chibi)

init python:
    def update_susan_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_sus {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Determine clothing state

        if susan.is_any_worn("bottom", "stockings"):
            if chibi.action == "walk":
                chibi["shoes"] = "ch_sus walk_shoes"
            else:
                chibi["shoes"] = "sb_walk_01_shoes.webp"

        if susan.is_worn("top"):
            chibi["top"] = "sb_cloth_shirt_h.webp"

        if susan.is_worn("bottom"):
            chibi["bottom"] = "sb_cloth_skirt.webp"

        if susan.is_worn("robe"):
            chibi["robe"] = "sb_cloth_robe_h.webp"
