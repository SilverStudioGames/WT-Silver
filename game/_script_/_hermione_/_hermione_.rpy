define her_face = {
    "mouth": {
        "neutral":      ["annoyed","base"],
        "happy":        ["smile","grin"],
        "naughty":      ["base","soft"],
        "horny":        ["base","grin","soft"],
        "annoyed":      ["annoyed"],
        "disgusted":    ["disgust","clench","annoyed"],
        "angry":        ["angry","clench","mad"]
    },

    "eyes": {
        "neutral":      ["base"],
        "happy":        ["base","base","happyCl"],
        "naughty":      ["narrow","base"],
        "horny":        ["narrow"],
        "annoyed":      ["narrow"],
        "disgusted":    ["narrow"],
        "angry":        ["narrow","base"]
    },

    "eyebrows": {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["base"],
        "horny":        ["base"],
        "annoyed":      ["worried"],
        "disgusted":    ["base", "angry"],
        "angry":        ["angry"]
    },

    "pupils": {
        "neutral":      ["mid","L","R"],
        "happy":        ["mid_soft","L_soft","R_soft"],
        "naughty":      ["mid_soft"],
        "horny":        ["mid","L","R","down","up"],
        "annoyed":      ["mid","R"],
        "disgusted":    ["down"],
        "angry":        ["mid"]
    }
}

label her_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        her "predict"

    python:

        if flip != None:
            hermione_flip = -1 if flip else 1

        if animation != False:
            hermione_animation = animation

        if xpos:
            hermione_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            if ypos == "head":
                use_hermione_head = True
            elif ypos in ("base", "default"):
                use_hermione_head = False

            hermione_ypos = int(sprite_pos["y"].get(ypos, ypos))

        hermione.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)

        if face:
            if not mouth:
                hermione.set_face(mouth=renpy.random.choice(her_face["mouth"].get(face, None)))
            if not eyes:
                hermione.set_face(eyes=renpy.random.choice(her_face["eyes"].get(face, None)))
            if not eyebrows:
                hermione.set_face(eyebrows=renpy.random.choice(her_face["eyebrows"].get(face, None)))
            if not pupils:
                hermione.set_face(pupils=renpy.random.choice(her_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        hide screen hermione_main
        show screen hermione_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(her, text)

    if use_hermione_head:
        hide screen hermione_main
    return

label update_hermione:

    $ hermione_chibi.update()
    $ hermione_flip = 1
    $ use_hermione_head = False

    return

label end_hermione_event:
    call her_chibi("hide")
    hide screen hermione_main
    with d3
    pause.5

    call update_hermione

    $ active_girl = None
    $ hermione_busy = True
    $ hermione.wear("all")
    $ hermione.set_cum(None)

    $ renpy.stop_predict(hermione.get_image())
    $ renpy.stop_predict("characters/hermione/face/*.png")

    call music_block
    jump main_room

screen hermione_main():
    tag hermione_main
    zorder hermione_zorder
    sensitive False
    default hermione_img = apply_doll_transition(hermione.get_image(), "hermione_main", use_hermione_head)
    if hermione_animation != None:
        #TODO Remove temporary plug image solution once the butt plug events have some kind of CG
        add hermione_plug_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom 0.5 at hermione_animation
        add hermione_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom 0.5 at hermione_animation
    else:
        add hermione_plug_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom 0.5
        add hermione_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom 0.5
