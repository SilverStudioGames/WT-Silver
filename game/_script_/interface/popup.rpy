transform popup_animation(time=4.0, xx=-200):
    on show, appear, start:
        xoffset xx
        linear 0.5 xoffset absolute(0)
        pause time
        linear 0.5 xoffset absolute(xx)

screen popup_window(string="", xpos=0, ypos=60):
    tag popup_window
    zorder 100

    frame:
        at popup_animation
        style "say_who_window"
        pos (xpos, ypos)

        text string align (0.5, 0.5) size 12
    timer 4.0 action Hide("popup_window")

label give_reward(text=None, gift=None, sound=True):
    if gift:
        $ the_gift = gift
    else:
        $ the_gift = "interface/icons/box_blue_2.webp"

    show screen gift(sound)
    show screen blktone
    with d3

    if text:
        $ renpy.say(None, text)
    else:
        call ctc

    hide screen gift
    hide screen blktone
    with d3

    return
