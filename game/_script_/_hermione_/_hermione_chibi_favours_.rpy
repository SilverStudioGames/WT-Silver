
# Sets up a chibi scene with Hermione and Genie in it
label her_chibi_scene(action="reset", xpos="mid", ypos="base", trans=None):
    if trans != None:
        call hide_characters

    hide screen bld1
    hide screen blkfade

    call her_chibi("hide")
    call gen_chibi("hide")

    $ menu_y = 0.75 # Menu moved down.

    if action == "reset":
        $ menu_y = 0.5
        call her_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    # Stand behind desk
    elif action == "behind_desk_back":
        show screen behind_desk("back")

    elif action == "behind_desk_front":
        show screen behind_desk("front")

    elif action == "behind_desk_show_tits":
        show screen behind_desk("show_tits")

    # Grope ass
    elif action == "grope_ass_back":
        show screen grope_ass_back

    elif action == "grope_ass_back_fast":
        show screen grope_ass_back(True)

    elif action == "grope_ass_front":
        show screen grope_ass_front

    elif action == "grope_ass_front_fast":
        show screen grope_ass_front(True)

    # Grope tits
    elif action in ("grope_tits", "grope_tits_jerk_off", "grope_tits_cum", "grope_tits_cum_done"):
        show screen chair_left
        show screen grope_tits(action)

    # Grope on podium (Quidditch pitch)
    elif action in ("grope_on_podium", "grope_on_podium_idle", "grope_on_podium_horny", "grope_on_podium_close", "grope_on_podium_cum"):
        show screen grope_on_podium(action)

    # Lie on desk (admire ass)
    elif action == "lie_on_desk":
        show screen lie_on_desk

    elif action == "lie_on_desk_fingering":
        show screen lie_on_desk("fingering")
    elif action == "lie_on_desk_fingering_slow":
        show screen lie_on_desk("fingering_slow")
    elif action == "lie_on_desk_fingering_pause":
        show screen lie_on_desk("fingering_pause")

    elif action == "lie_on_desk_jerk_off":
        show screen chair_left
        $ masturbating = True
        show screen lie_on_desk("jerk_off")

    elif action == "lie_on_desk_cum":
        show screen chair_left
        $ masturbating = True
        show screen lie_on_desk("cum")

    # Handjob
    elif action in ("hj", "hj_pause", "hj_cum_in", "hj_cum_in_done", "hj_cum_on", "hj_cum_on_done", "hj_kiss", "hj_kiss_cum"):
        show screen chair_left
        show screen desk
        show screen hermione_chibi_hj(action, xpos=230, ypos=0)

    # Titjob
    elif action in ("tj", "tj_pause", "tj_idle", "tj_cum_on", "tj_cum_on_done", "tj_mouth", "tj_cum_in", "tj_cum_in_done"):
        show screen chair_left
        show screen desk
        show screen hermione_chibi_tj(action, xpos=450, ypos=200)

    # Blowjob
    elif action in ("bj", "bj_pause", "bj_cum_in", "bj_cum_out", "bj_cum_out_done"):
        show screen chair_left
        show screen hermione_chibi_bj(action)

    # Sex
    elif action in (
        "sex_hotdog", "sex", "sex_pause", "sex_slow", "sex_fast",
        "sex_cum_out", "sex_cum_out_done", "sex_cum_in", "sex_cum_in_done",
        "sex_naked", "sex_naked_pause", "sex_naked_slow", "sex_naked_fast",
        "sex_naked_cum_out", "sex_naked_cum_out_done", "sex_naked_cum_in", "sex_naked_cum_in_done"
    ):
        show screen chair_left
        show screen hermione_chibi_sex(action)

    if trans:
        with trans

    return

define desk_scene_position = (-77, 10)

screen behind_desk(alt=None):
    tag favor
    zorder desk_zorder
    fixed:
        pos desk_scene_position
        if alt == "back":
            if not hermione.is_worn("top"):
                add "behind_desk_back_topless"
            else:
                add "behind_desk_back"
        elif alt == "front":
            if not hermione.is_worn("top"):
                add "behind_desk_front_topless"
            else:
                add "behind_desk_front"
        elif alt == "show_tits":
            add "behind_desk_show_tits"

screen lie_on_desk(alt=None):
    tag favor
    zorder desk_zorder
    fixed:
        pos desk_scene_position
        if alt == "jerk_off":
            if hermione.is_worn("bottom"):
                add "lie_on_desk_jerk_off"
            else:
                add "lie_on_desk_naked_jerk_off"
        elif alt == "cum":
            if hermione.is_worn("bottom"):
                add "lie_on_desk_cum"
            else:
                add "lie_on_desk_naked_cum"
        elif alt == "fingering":
            if hermione.is_worn("bottom"):
                add "finger_naked"
            else:
                add "finger_naked"
        elif alt == "fingering_slow":
            if hermione.is_worn("bottom"):
                add "finger_naked_slow"
            else:
                add "finger_naked_slow"
        elif alt == "fingering_pause":
            if hermione.is_worn("bottom"):
                add "finger_naked_pause"
            else:
                add "finger_naked_pause"
        else:
            if hermione.is_worn("bottom"):
                add "lie_on_desk"
            else:
                add "lie_on_desk_naked"

screen finger(img):
    tag favor
    zorder desk_zorder
    add img pos desk_scene_position

screen grope_ass_back(fast=False):
    tag favor
    zorder desk_zorder
    fixed:
        pos desk_scene_position
        if not hermione.is_worn("top"):
            if fast:
                add "grope_ass_back_topless_fast"
            else:
                add "grope_ass_back_topless"
        else:
            add "grope_ass_back"
        add "desk_back_blink" zoom 0.5

screen grope_ass_front(fast=False):
    tag favor
    zorder desk_zorder
    fixed:
        pos desk_scene_position
        if not hermione.is_worn("top"):
            if fast:
                add "grope_ass_front_topless_fast"
            else:
                add "grope_ass_front_topless"
        else:
            add "grope_ass_front"
        add "desk_front_blink" zoom 0.5

screen grope_on_podium(img):
    tag favor
    zorder 9 # In front of screen quidditch_stands_mid (which contains podium)
    add img pos (255, 211)

screen grope_tits(img):
    tag favor
    zorder desk_zorder
    if img == "grope_tits":
        if not hermione.is_worn("top"):
            $ img = "grope_tits_topless"
        elif hermione_action == "lift_top": #TODO Replace with proper char_class method
            $ img = "grope_tits_lift_top"
    add img pos desk_scene_position
    add "desk_front_blink" pos desk_scene_position zoom 0.5

screen hermione_chibi_bj(img):
    tag favor
    zorder desk_zorder
    add img pos desk_scene_position xoffset 68 yoffset 4

screen hermione_chibi_sex(img):
    tag favor
    zorder desk_zorder
    add img pos desk_scene_position

#TODO Implement positioning for hj and tj chibis (the ones without desk, basically)

screen hermione_chibi_hj(img, xpos=230, ypos=0):
    tag favor
    zorder desk_zorder

    add img xpos xpos ypos ypos

screen hermione_chibi_tj(img, xpos=450, ypos=200):
    tag favor
    zorder desk_zorder

    add img xpos xpos ypos ypos
