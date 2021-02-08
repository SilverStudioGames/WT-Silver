
# Sets up a chibi scene with Tonks and Genie in it
label ton_chibi_scene(action="reset", xpos="mid", ypos="base", trans=None):
    if trans != None:
        call hide_characters

    if trans: # Not sure if this part is needed, depends on context?
        hide screen bld1
        hide screen blkfade

    call ton_chibi("hide")
    call gen_chibi("hide")

    $ menu_y = 0.75

    if action == "reset":
        $ menu_y = 0.5
        call ton_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    # Blowjob
    elif action in ('bj_desk', 'bj_desk_shocked'):
        show screen tonks_chibi_desk(action)

    if trans:
        with trans

    return

screen tonks_chibi_desk(action):
    tag tonks_chibi_scene
    zorder desk_zorder

    # Works with any image that matches the desk area
    add "ch_ton [action]" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5
