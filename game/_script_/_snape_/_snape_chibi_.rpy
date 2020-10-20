label sna_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ snape_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ snape_chibi.hide()
        return
    elif action == "leave":
        hide screen snape_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ snape_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ snape_chibi.do(None)
        return

    $ snape_chibi.do(action)

    return

label sna_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call sna_chibi(None, "door", "base", False)
        with d3
        if xpos or ypos:
            $ snape_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ snape_chibi.show()
        $ snape_chibi.move(("door", "base"), speed, reduce)
        call play_sound("door")
        $ snape_chibi.hide()
        with d3
        pause .5
    elif path:
        $ snape_chibi.show()
        $ snape_chibi.move(path, speed, reduce)
    else:
        $ snape_chibi.show()
        $ snape_chibi.move((xpos, ypos), speed, reduce)

    return

# Screens
screen with_snape(ani=False):
    tag hanging_with_snape
    zorder 3
    if ani:
        if game.daytime:
            add "ch_gen toast_goblet_daytime" xpos 435 ypos 200 # Different shadow.
        else:
            add "ch_gen toast_goblet" xpos 435 ypos 200
        add "snape_toast_goblet" xpos 618 ypos 200 zoom 0.5

    else:
        if game.daytime:
            add "characters/genie/chibis/drinking/01_day.webp" xpos 435 ypos 200 zoom 0.5 # Different shadow.
        else:
            add "characters/genie/chibis/drinking/01.webp" xpos 435 ypos 200 zoom 0.5
        add "characters/snape/chibis/drinking/01.webp" xpos 618 ypos 200 zoom 0.5

# Chibi definition
default snape_chibi = Chibi("snape", ["base"], update_snape_chibi)

init python:
    def update_snape_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_sna {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image
