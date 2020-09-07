
label lun_main(text="", mouth=None, eye=None, brows=None, pupils=None, cheeks=None, tears=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):

    #Flip
    if flip == False:
        $ luna_flip = 1 #Default
    if flip == True:
        $ luna_flip = -1

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if emote == None:
        $ emote = "blank"

    if xpos:
        $ luna_xpos = int(sprite_pos["x"].get(xpos, xpos))

    if ypos:
        $ use_luna_head = True if ypos == "head" else False

        $ luna_ypos = int(sprite_pos["y"].get(ypos, ypos))

    if face != None:
        if mouth == None:
            call set_lun_face(mouth = face)
        if eye == None:
            call set_lun_face(eyes = face)
        if brows == None:
            call set_lun_face(brows = face)
        if pupils == None:
            call set_lun_face(pupils = face)

    $ changeLuna(mouth, eye, brows, pupils, cheeks, tears, emote)

    show screen luna_main
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(lun, text)

    if use_luna_head:
        hide screen luna_main

    return


label luna_away:
    call reset_luna
    call reset_genie
    call gen_chibi("sit_behind_desk")

    #TODO Check if Luna stands in the right place at the end of her events (when jumping to luna_away)
    # call lun_chibi("stand", ypos="base")

    hide screen blkfade
    with d3

    call lun_walk(action="leave")

    $ luna_busy = True

    jump main_room


label end_luna_event:

    call hide_characters
    call lun_chibi("hide")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    with d3

    call reset_luna

    $ luna_busy = True

    jump main_room


label reset_luna:

    call load_luna_clothing_saves

    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    $ luna_chibi.zorder = 3
    $ luna_zorder = 15

    call update_luna

    return


label update_luna:
    $ luna_flip = 1
    $ use_luna_head = False
    $ luna_l_arm = 1
    $ luna_r_arm = 1

    call update_lun_uniform

    return


label luna_no_money:
    call lun_main("You expect me to do it for free?", "angry", "mad", "mad", "R")
    call lun_main("Hmph!", "angry", "mad", "mad", "R")
    jump luna_away


init python:
    def changeLuna(
        mouth=None,
        eye=None,
        brows=None,
        pupils=None,
        cheeks=None,
        tears=None,
        emote=None):

        global luna_mouth
        global luna_eye
        global luna_eyebrow
        global luna_pupil
        global luna_cheeks
        global luna_tears
        global luna_emote

        if mouth is not None:
            luna_mouth       = "characters/luna/face/mouth/"+str(mouth)+".webp"
        if eye is not None:
            luna_eye         = "characters/luna/face/eyes/"+str(eye)+".webp"
        if brows is not None:
            luna_eyebrow     = "characters/luna/face/brow/"+str(brows)+".webp"
        if pupils is not None:
            luna_pupil       = "characters/luna/face/pupil/"+str(luna_pupil_color)+"/"+str(pupils)+".webp"
        if cheeks is not None:
            luna_cheeks      = "characters/luna/face/extras/cheeks_"+str(cheeks)+".webp"
        if tears is not None:
            luna_tears       = "characters/luna/face/extras/tears_"+str(tears)+".webp"
        if emote is not None:
            luna_emote       = "characters/luna/emotes/"+str(emote)+".webp"
