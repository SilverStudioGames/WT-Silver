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
    else: # stand
        $ susan_chibi.do(None)

    return

label sus_walk(xpos=None, ypos=None, speed=1.0, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call sus_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ susan_chibi.move(xpos, ypos, speed)
    elif action == "leave":
        $ susan_chibi.show()
        $ susan_chibi.move("door", "base", speed)
        call play_sound("door")
        $ susan_chibi.hide()
        with d3
        pause .5
    else:
        $ susan_chibi.show()
        $ susan_chibi.move(xpos, ypos, speed)
    return

# Chibi definition
default susan_chibi = chibi("susan", ["base", "shoes", "top", "bottom", "robe"], update_susan_chibi)

init python:
    def update_susan_chibi(chibi):
        if chibi.action == "walk":
            chibi["base"] = "ch_sus walk"
        else:
            chibi["base"] = "ch_sus blink"
        
        if susan_wear_bottom or susan_wear_stockings:
            if chibi.action == "walk":
                chibi["shoes"] = "ch_sus walk_shoes"
            else:
                chibi["shoes"] = "sb_walk_01_shoes.png"
        
        if susan_wear_top:
            chibi["top"] = "sb_cloth_shirt_h.png"

        if susan_wear_bottom:
            chibi["bottom"] = "sb_cloth_skirt.png"

        if susan_wear_robe:
            chibi["robe"] = "sb_cloth_robe_h.png"
