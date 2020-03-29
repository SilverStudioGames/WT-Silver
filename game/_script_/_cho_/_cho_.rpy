define cho_face = {
    "mouth": {
        "neutral":      ["base","normal","annoyed"],
        "happy":        ["base", "smile"],
        "naughty":      ["base","quiver","horny","soft"],
        "horny":        ["horny","soft"],
        "annoyed":      ["annoyed"],
        "disgusted":    ["disgust","upset"],
        "angry":        ["angry","clench","mad","upset"]
    },

    "eyes": {
        "neutral":      ["base","base","closed"],
        "happy":        ["base","base","happyCl"],
        "naughty":      ["narrow"],
        "horny":        ["narrow"],
        "annoyed":      ["narrow","narrow","closed"],
        "disgusted":    ["base","narrow"],
        "angry":        ["narrow"]
    },

    "eyebrows": {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["base","raised","worried"],
        "horny":        ["base","raised"],
        "annoyed":      ["angry"],
        "disgusted":    ["base","raised","worried"],
        "angry":        ["angry"]
    },

    "pupils": {
        "neutral":      ["mid","L","R"],
        "happy":        ["mid","L","R"],
        "naughty":      ["mid","L","R","down","up"],
        "horny":        ["mid","L","R","down","up"],
        "annoyed":      ["mid","L","R","downR"],
        "disgusted":    ["mid","down"],
        "angry":        ["mid"]
    }
}

label cho_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        cho "predict"

    python:

        if flip != None:
            cho_flip = -1 if flip else 1

        if animation != False:
            cho_animation = animation

        if xpos:
            cho_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            if ypos == "head":
                use_cho_head = True
            elif ypos in ("base", "default"):
                use_cho_head = False

            cho_ypos = int(sprite_pos["y"].get(ypos, ypos))

        cho.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)

        if face:
            if not mouth:
                cho.set_face(mouth=renpy.random.choice(cho_face["mouth"].get(face, None)))
            if not eyes:
                cho.set_face(eyes=renpy.random.choice(cho_face["eyes"].get(face, None)))
            if not eyebrows:
                cho.set_face(eyebrows=renpy.random.choice(cho_face["eyebrows"].get(face, None)))
            if not pupils:
                cho.set_face(pupils=renpy.random.choice(cho_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        show screen cho_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(character.cho, text)

    if use_cho_head:
        hide screen cho_main
    return

label update_cho:

    # Chibi Update
    $ cho_chibi.update()
    $ cho_chibi.position(flip=False)
    $ cho_flip = 1
    hide screen cho_cloth_pile

    return

label end_cho_event:
    call cho_chibi("hide")
    hide screen cho_main
    with d3
    pause.5

    call update_cho

    $ active_girl = None
    $ cho_busy = True
    $ cho.wear("all")

    $ renpy.stop_predict(cho.get_image())
    $ renpy.stop_predict("characters/cho/face/*.png")

    call music_block
    jump main_room

screen cho_main():
    pass
