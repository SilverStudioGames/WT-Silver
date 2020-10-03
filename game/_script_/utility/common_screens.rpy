screen blkfade():
    tag blkfade
    zorder 20
    add Color("#000")

screen whitefade():
    tag whitefade
    zorder 20
    add Color("#fff")

screen blktone(alpha=0.5):
    tag blktone
    zorder 10
    add Color("#000", alpha=alpha)

screen blktone(): #For narrator. (label nar) #Don't add tag blktone!
    zorder 20
    add Color("#000", alpha=0.5)

screen white():
    zorder 20
    add Color("#fff")

screen bld1():
    zorder 10
    if not current_room == "quidditch_stands":
        add "interface/bld.webp"

screen bld2():
    zorder 10
    add im.Flip("interface/bld.webp", vertical=True)

screen notes():
    add "notes" xpos 320+140 ypos 330
    zorder 1

screen gift(win=False):
    zorder 30
    if win:
        use notes
        on "show" action Play("sound", "sounds/win2.mp3")
    add the_gift align (0.5, 0.4) zoom get_zoom(the_gift, 320,320)

screen clothing_unlock(item):
    zorder 30
    modal True

    use notes
    on "show" action Play("sound", "sounds/win2.mp3")

    frame:
        style "empty"
        xalign 0.5
        ypos 100
        xysize (197, 325)

        add "interface/frames/"+str(interface_color)+"/outfit.webp"

        if isinstance(item, DollCloth):
            add item.get_icon() align (0.5, 0.5) zoom 0.5
        elif isinstance(item, (DollOutfit, Item)):
            add item.get_image() align (0.5, 1.0) offset (-13, -13) zoom 0.3
        else:
            add item align (0.5, 0.5)

screen invisible_button(action=NullAction(), keysym=None):
    # Actions cannot be passed as transclude, separate parameter is required.
    button style "empty":
        action action
        keysym keysym
        transclude
