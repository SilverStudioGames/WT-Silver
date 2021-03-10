
# TODO: Replace values according to Luna's expressions list
define lun_face = {
    "mouth": {
        "neutral":      ["base","open"],
        "happy":        ["base","grin"],
        "naughty":      ["soft","base"],
        "horny":        ["horny","base"],
        "annoyed":      ["upset","annoyed"],
        "disgusted":    ["disgust","upset"],
        "angry":        ["clench","mad","upset"]
    },

    "eyes": {
        "neutral":      ["base"],
        "happy":        ["happyCl"],
        "naughty":      ["narrow"],
        "horny":        ["narrow"],
        "annoyed":      ["narrow","base"],
        "disgusted":    ["base"],
        "angry":        ["base"]
    },

    "eyebrows": {
        "neutral":      ["base"],
        "happy":        ["base","raised"],
        "naughty":      ["base","raised"],
        "horny":        ["base","raised"],
        "annoyed":      ["annoyed"],
        "disgusted":    ["raised","worried"],
        "angry":        ["angry"]
    },

    "pupils": {
        "neutral":      ["mid"],
        "happy":        ["mid"],
        "naughty":      ["mid","up","downR"],
        "horny":        ["mid","stare","down"],
        "annoyed":      ["mid","downR","R"],
        "disgusted":    ["mid","down"],
        "angry":        ["mid"]
    }
}

label lun_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        lun "predict"

    python:

        if flip != None:
            luna_flip = -1 if flip else 1

        if animation != False:
            luna_animation = animation

        if xpos:
            luna_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            use_luna_head = True if ypos == "head" else False

            luna_ypos = int(sprite_pos["y"].get(ypos, ypos))

        luna.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        luna_emote = get_character_emote("luna", emote)

        if face:
            if not mouth:
                luna.set_face(mouth=renpy.random.choice(lun_face["mouth"].get(face, None)))
            if not eyes:
                luna.set_face(eyes=renpy.random.choice(lun_face["eyes"].get(face, None)))
            if not eyebrows:
                luna.set_face(eyebrows=renpy.random.choice(lun_face["eyebrows"].get(face, None)))
            if not pupils:
                luna.set_face(pupils=renpy.random.choice(lun_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe"):
        hide screen luna_main
        show screen luna_main
        show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(lun, text)

    if use_luna_head:
        hide screen luna_main
    return

label end_luna_event:

    call lun_chibi("hide")
    hide screen luna_main
    with d3
    pause.5

    call update_luna

    $ active_girl = None
    $ luna_busy = True
    $ luna.wear("all")

    $ renpy.stop_predict(luna.get_image())
    $ renpy.stop_predict("characters/luna/face/*.webp")

    call music_block
    jump main_room_menu

label update_luna:
    # Chibi Update
    $ luna_chibi.update()
    $ luna_chibi.position(flip=False)
    $ luna_flip = 1
    hide screen luna_cloth_pile

    return

screen luna_main():
    tag luna_main
    zorder luna_zorder
    sensitive False

    # Get image and apply transition and set position
    default luna_img = apply_doll_transition(luna.get_image(), "luna_main", use_luna_head)
    default luna_pos = get_character_pos("luna")
    default properties = {"zoom": 0.5, "xzoom": luna_flip}

    fixed:
        pos luna_pos
        at luna_animation

        add luna_img properties properties
        if luna_emote:
            add luna_emote properties properties
