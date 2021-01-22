
# Genie chibi actions:
# stand, stand_alt, stand_shocked
# rummage, petting, grab_mid, grab_high
# sit_behind_desk
# jerk_off_behind_desk, cum_behind_desk, cum_behind_desk_done
# dick_out
# hold_dick, jerk_off, cum, cum_done, cum_close, cum_close_done
# read, read_done, read_near_fire, read_near_fire_done

# Note: The flip parameter defaults to True, because Genie is most often facing right
label gen_chibi(action=None, xpos=None, ypos=None, flip=True, pic=None):

    $ genie_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ desk_OBJ.hidden = False
        $ desk_OBJ.idle = "desk_empty"
        $ genie_chibi.hide()
        return

    elif action == "leave":
        hide screen genie_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")

        $ desk_OBJ.hidden = False
        $ desk_OBJ.idle = "desk_empty"
        $ genie_chibi.hide()
        with d3
        pause .5
        return

    elif action == "sit_behind_desk":
        $ desk_OBJ.hidden = False
        $ desk_OBJ.idle = "ch_gen sit_behind_desk"
        $ genie_chibi.hide()
        return

    elif action in ("jerk_off_behind_desk", "cum_behind_desk", "cum_behind_desk_done"):
        $ desk_OBJ.hidden = True
        $ genie_chibi.position(218, 205+262, False)
        $ genie_chibi.do(action)
        return

    elif action in ("paperwork", "paperwork_idle"):
        $ desk_OBJ.hidden = True
        $ genie_chibi.position(224, 205+262, False)
        $ genie_chibi.do(action)
        return

    elif action in ("read", "read_done", "read_near_fire", "read_near_fire_done"):
        $ genie_chibi.position(430, 205+340, False)

    $ desk_OBJ.hidden = False
    $ desk_OBJ.idle = "desk_empty"
    $ genie_chibi.do(action)

    return

label gen_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call gen_chibi(None, "door", "base", False)
        with d3
        if xpos or ypos:
            $ genie_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ genie_chibi.show()
        $ genie_chibi.move(("door", "base"), speed, reduce)
        call play_sound("door")
        $ genie_chibi.hide()
        with d3
        pause .5
    elif path:
        $ genie_chibi.show()
        $ genie_chibi.move(path, speed, reduce)
    else:
        $ genie_chibi.show()
        $ genie_chibi.move((xpos, ypos), speed, reduce)
        $ genie_chibi.do()

    return

# Chibi definition
default genie_chibi = Chibi("genie", ["base"], update_genie_chibi)

init python:
    def update_genie_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_gen {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image
