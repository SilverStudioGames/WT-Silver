define ast_face = {
    "mouth": {
        "neutral":      ["annoyed", "base"],
        "happy":        ["smile", "grin"],
        "naughty":      ["grin", "horny"],
        "horny":        ["grin", "horny"],
        "annoyed":      ["annoyed"],
        "disgusted":    ["clench", "annoyed"],
        "angry":        ["clench","angry"]
    },

    "eyes": {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["narrow", "base"],
        "horny":        ["narrow", "base"],
        "annoyed":      ["narrow"],
        "disgusted":    ["narrow"],
        "angry":        ["narrow", "base"]
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
        "happy":        ["mid","L","R"],
        "naughty":      ["mid","L","R","down"],
        "horny":        ["mid","L","R","down"],
        "annoyed":      ["mid","R"],
        "disgusted":    ["down"],
        "angry":        ["L"]
    }
}

label ast_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        ast "predict"

    python:

        if flip != None:
            astoria_flip = -1 if flip else 1

        if animation != False:
            astoria_animation = animation

        if xpos:
            astoria_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            use_astoria_head = True if ypos == "head" else False

            astoria_ypos = int(sprite_pos["y"].get(ypos, ypos))

        astoria.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        astoria_emote = get_character_emote("astoria", emote)

        if face:
            if not mouth:
                astoria.set_face(mouth=renpy.random.choice(ast_face["mouth"].get(face, None)))
            if not eyes:
                astoria.set_face(eyes=renpy.random.choice(ast_face["eyes"].get(face, None)))
            if not eyebrows:
                astoria.set_face(eyebrows=renpy.random.choice(ast_face["eyebrows"].get(face, None)))
            if not pupils:
                astoria.set_face(pupils=renpy.random.choice(ast_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        hide screen astoria_main
        show screen astoria_main()
        show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(ast, text)

    if use_astoria_head:
        hide screen astoria_main
    return

label update_astoria:

    $ random_number = renpy.random.randint(0, 5)
    if random_number in [1,5]:
        $ ast_susan_name = renpy.random.choice(["Suzy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    if random_number in [2,5]:
        $ ast_tonks_name = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    if random_number in [3,5]:
        $ ton_astoria_name = renpy.random.choice(["Cutie","Kitty","Princess","Cupcake","Honey"])

    # Chibi Update
    $ astoria_chibi.update()
    $ astoria_chibi.position(flip=False)
    $ astoria_flip = 1
    hide screen astoria_cloth_pile

    return

label end_astoria_event:
    call ast_chibi("hide")
    hide screen astoria_main
    with d3
    pause.5

    call update_astoria

    $ active_girl = None
    $ astoria_busy = True
    $ astoria.wear("all")

    $ renpy.stop_predict(astoria.get_image())
    $ renpy.stop_predict("characters/astoria/face/*.webp")

    call music_block
    jump main_room

screen astoria_main():
    tag astoria_main
    zorder astoria_zorder
    sensitive False

    # Get image and apply transition and set position
    default astoria_img = apply_doll_transition(astoria.get_image(), "astoria_main", use_astoria_head)
    default astoria_pos = get_character_pos("astoria")
    default properties = {"zoom": 0.5, "xzoom": astoria_flip}

    fixed:
        pos astoria_pos
        at astoria_animation

        add astoria_img properties properties
        if astoria_emote:
            add astoria_emote properties properties
