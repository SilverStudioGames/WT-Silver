label ton_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ tonks_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ tonks_chibi.hide()
        return
    elif action == "leave":
        hide screen tonks_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ tonks_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ tonks_chibi.do(None)
        return

    $ tonks_chibi.do(action)

    return

label ton_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call ton_chibi(None, "door", "base", False)
        with d3
        if xpos or ypos:
            $ tonks_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ tonks_chibi.show()
        $ tonks_chibi.move(("door", "base"), speed, reduce)
        call play_sound("door")
        $ tonks_chibi.hide()
        with d3
        pause .5
    elif path:
        $ tonks_chibi.show()
        $ tonks_chibi.move(path, speed, reduce)
    else:
        $ tonks_chibi.show()
        $ tonks_chibi.move((xpos, ypos), speed, reduce)

    return

# Screens
screen ton_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag ton_cloth_pile
    zorder tonks_chibi.zorder
    add "characters/chibis/cloth_pile_r.webp" pos position zoom 0.5

label ton_sit(xpos=nxpos, ypos=nypos, flip=None, chair=True): # TODO: replace this with the regular chibi call and add a sitting pose/action -- call ton_chibi("sit", chair=False)

    # call ton_sit(chair=False, xpos=0, ypos=0)
    # Quidditch stands position: xpos=-140, ypos=125

    python:

        xpos = nxpos
        ypos = nypos

        if flip != None:
            tonks_flip = -1 if flip else 1

    show screen tonks_sit_ani(nxpos, nypos, chair)

    return

screen tonks_sit_ani(xpos=nxpos, ypos=nypos, chair=True): # TODO: use Tonks' regular chibi position for this -- tonks_chibi.pos
    tag ton_chibi
    zorder tonks_chibi.zorder

    if chair == True:
        add "ch_ton sit_chair" xpos nxpos ypos nypos xzoom tonks_flip

    add "ch_ton sit" xpos nxpos ypos nypos xzoom tonks_flip

    if tonks.is_worn("bottom"):
        add "ch_ton sit_trousers" xpos nxpos ypos nypos xzoom tonks_flip
    if tonks.is_any_worn("bottom", "stockings"):
        add "ch_ton sit_shoes" xpos nxpos ypos nypos xzoom tonks_flip
    if tonks.is_worn("top"):
        add "ch_ton sit_top" xpos nxpos ypos nypos xzoom tonks_flip

screen with_tonks_animated():
    tag ton_chibi
    zorder tonks_chibi.zorder

    if game.daytime:
        add "ch_gen toast_goblet_daytime" xpos 435 ypos 200
    else:
        add "ch_gen toast_goblet" xpos 435 ypos 200

    add "ch_ton sit_chair" xpos 610 ypos 175
    add "ch_ton sit" xpos 610 ypos 175

    if tonks.is_worn("bottom"):
        add "ch_ton sit_trousers" xpos 610 ypos 175
    if tonks.is_any_worn("bottom", "stockings"):
        add "ch_ton sit_shoes" xpos 610 ypos 175
    if tonks.is_worn("top"):
        add "ch_ton sit_top" xpos 610 ypos 175
    if tonks.is_worn("neckwear"):
        add "ch_ton sit_choker" xpos 610 ypos 175


# Chibi definition
default tonks_chibi = Chibi("tonks", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves", "neck"], update_tonks_chibi)

init python:
    def update_tonks_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_ton {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Determine clothing state

        if tonks.is_worn("top"):
            chibi["top"] = "nt_top.webp"

        if tonks.is_worn("bottom"):
            if chibi.action == "walk":
                chibi["bottom"] = "ch_ton walk trousers"
            else:
                chibi["bottom"] = "nt_trousers.webp"

        if tonks.is_worn("gloves"):
            chibi["gloves"] = "nt_gloves.webp"

        if tonks.is_worn("robe"):
            chibi["robe"] = "nt_robe.webp"

        if tonks.is_worn("bottom") or tonks.is_worn("stockings"):
            if chibi.action == "walk":
                chibi["shoes"] = "ch_ton walk shoes"
            else:
                chibi["shoes"] = "nt_shoes.webp"

        if tonks.is_worn("neckwear"):
            chibi["neck"] = "nt_choker.webp"
