transform popup_animation(time=4.0, xx=-200):
    xoffset xx
    linear 0.5 xoffset absolute(0)
    pause time
    linear 0.5 xoffset absolute(xx)

screen popup_window(string="", xpos=0, ypos=60):
    tag popup_window
    zorder 100

    style_prefix gui.theme()

    timer 5.0 action Hide("popup_window")
    frame:
        at popup_animation
        pos (xpos, ypos)

        text string align (0.5, 0.5) size 12

label give_reward(text="You found something!", gift="interface/icons/box_blue_2.webp", sound=True):
    if sound:
        $ renpy.play("sounds/win2.mp3")

    show screen gift(gift)
    show screen blktone
    show screen notes
    with d3

    # It has to be a renpy.say function in order to evaluate text tags i.e "You found [item.name]".
    $ renpy.say(None, text)

    hide screen gift
    hide screen blktone
    hide screen notes
    with d3

    return
