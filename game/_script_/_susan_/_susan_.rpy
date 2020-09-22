
define sus_face = {
    "mouth": {
        "neutral":      ["base"],
        "happy":        ["base","grin"],
        "naughty":      ["base"],
        "horny":        ["base"],
        "annoyed":      ["upset"],
        "disgusted":    ["open"],
        "angry":        ["upset"]
    },

    "eyes": {
        "neutral":      ["base", "closed"],
        "happy":        ["base", "eager"],
        "naughty":      ["base", "suspicious"],
        "horny":        ["suspicious"],
        "annoyed":      ["narrow","base", "suspicious"],
        "disgusted":    ["wide"],
        "angry":        ["suspicious"]
    },

    "eyebrows": {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["base","worried"],
        "horny":        ["base","worried"],
        "annoyed":      ["angry"],
        "disgusted":    ["worried"],
        "angry":        ["angry"]
    },

    "pupils": {
        "neutral":      ["mid"],
        "happy":        ["mid","L","R"],
        "naughty":      ["L","R","down"],
        "horny":        ["L","R","down"],
        "annoyed":      ["R","down"],
        "disgusted":    ["R","wide"],
        "angry":        ["mid"]
    }
}

label sus_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        sus "predict"

    python:

        if flip != None:
            susan_flip = -1 if flip else 1

        if animation != False:
            susan_animation = animation

        if xpos:
            susan_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            use_susan_head = True if ypos == "head" else False

            susan_ypos = int(sprite_pos["y"].get(ypos, ypos))

        susan.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        susan_emote = get_character_emote("susan", emote)

        if face:
            if not mouth:
                susan.set_face(mouth=renpy.random.choice(sus_face["mouth"].get(face, None)))
            if not eyes:
                susan.set_face(eyes=renpy.random.choice(sus_face["eyes"].get(face, None)))
            if not eyebrows:
                susan.set_face(eyebrows=renpy.random.choice(sus_face["eyebrows"].get(face, None)))
            if not pupils:
                susan.set_face(pupils=renpy.random.choice(sus_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        hide screen susan_main
        show screen susan_main
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(sus, text)

    if use_susan_head:
        hide screen susan_main
    return

label end_susan_event:

    call sus_chibi("hide")
    hide screen susan_main
    with d3
    pause.5

    call update_susan

    $ active_girl = None
    $ susan_busy = True
    $ susan.wear("all")

    $ renpy.stop_predict(susan.get_image())
    $ renpy.stop_predict("characters/susan/face/*.webp")

    call music_block
    jump main_room

label update_susan:
    # Chibi Update
    $ susan_chibi.update()
    $ susan_chibi.position(flip=False)
    $ susan_flip = 1
    hide screen susan_cloth_pile

    return

screen susan_main():
    tag susan_main
    zorder susan_zorder
    sensitive False

    # Get image and apply transition and set position
    default susan_img = apply_doll_transition(susan.get_image(), "susan_main", use_susan_head)
    default susan_pos = get_character_pos("susan")
    default properties = {"zoom": 0.5, "xzoom": susan_flip}

    fixed:
        pos susan_pos
        at susan_animation

        add susan_img properties properties
        if susan_emote:
            add susan_emote properties properties
