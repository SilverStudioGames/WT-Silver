define ton_face = {
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

label ton_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, hair=None, cheeks=None, tears=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        ton "predict"

    python:

        if flip != None:
            tonks_flip = -1 if flip else 1

        if animation != False:
            tonks_animation = animation

        if xpos:
            tonks_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            use_tonks_head = True if ypos == "head" else False

            tonks_ypos = int(sprite_pos["y"].get(ypos, ypos))


        if hair:
            if isinstance(hair, list):
                target_color = hair
            elif hair in ("neutral", "basic", "reset"):
                target_color = tonks_haircolor
            elif hair in ("red", "angry", "furious"):
                target_color = [[164, 34, 34, 255], [219, 83, 83, 255]]
            elif hair in ("orange", "upset", "annoyed"):
                target_color = [[228, 93, 34, 255], [246, 193, 170, 255]]
            elif hair in ("yellow", "happy", "cheerful"):
                target_color = [[255, 213, 23, 255], [255, 239, 167, 255]]
            elif hair in ("green", "disgusted"):
                target_color = [[111, 205, 75, 255], [200, 237, 186, 255]]
            elif hair in ("blue", "sad"):
                target_color = [[64, 75, 205, 255], [182, 186, 237, 255]]
            elif hair in ("purple"):
                target_color = [[205, 75, 205, 255], [237, 186, 237, 255]]
            elif hair in ("white", "scared"):
                target_color = [[238, 238, 241, 255], [249, 249, 250, 255]]
            elif hair in ("pink", "horny"):
                target_color = [[255, 105, 180, 255], [251, 205, 222, 255]]
        else:
            target_color = tonks_haircolor

        if target_color != tonks.get_equipped("hair").color:
            tonks.get_equipped("hair").set_color(target_color)

        tonks.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        tonks_emote = get_character_emote("tonks", emote)

        if face:
            if not mouth:
                tonks.set_face(mouth=renpy.random.choice(ton_face["mouth"].get(face, None)))
            if not eyes:
                tonks.set_face(eyes=renpy.random.choice(ton_face["eyes"].get(face, None)))
            if not eyebrows:
                tonks.set_face(eyebrows=renpy.random.choice(ton_face["eyebrows"].get(face, None)))
            if not pupils:
                tonks.set_face(pupils=renpy.random.choice(ton_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        hide screen tonks_main
        show screen tonks_main()
        show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(ton, text)

    if use_tonks_head:
        hide screen tonks_main
    return

label update_tonks:

    # Chibi Update
    $ tonks_chibi.update()
    $ tonks_chibi.position(flip=False)
    $ tonks_flip = 1
    hide screen ton_cloth_pile

    $ tonks.get_equipped("hair").set_color(tonks_haircolor)
    return

label end_tonks_event:
    call ton_chibi("hide")
    hide screen tonks_main
    with d3
    pause.5

    call update_tonks

    $ active_girl = None
    $ tonks_busy = True
    $ tonks.wear("all")

    $ renpy.stop_predict(tonks.get_image())
    $ renpy.stop_predict("characters/tonks/face/*.webp")

    call music_block
    jump main_room_menu

screen tonks_main():
    tag tonks_main
    zorder tonks_zorder
    sensitive False

    # Get image and apply transition and set position
    default tonks_img = apply_doll_transition(tonks.get_image(), "tonks_main", use_tonks_head)
    default tonks_pos = get_character_pos("tonks")
    default properties = {"zoom": 0.5, "xzoom": tonks_flip}

    fixed:
        pos tonks_pos
        at tonks_animation

        add tonks_img properties properties
        if tonks_emote:
            add tonks_emote properties properties
