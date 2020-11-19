image spectrevision:
    contains:
        zoom 0.5
        "images/spectrevision/bg_room.webp"

    contains:
        "images/spectrevision/bg1.webp"
        align (0.5, 0.5)
        zoom 0.55
        subpixel True

        parallel:
            linear 2.5 yoffset -10
            linear 2.5 yoffset 10
            repeat

        parallel:
            linear 5.0 xoffset 20
            linear 5.0 xoffset -20
            repeat

    contains:
        "images/spectrevision/bg2.webp"
        align (0.5, 0.5)
        zoom 0.52
        subpixel True

        parallel:
            linear 2.0 yoffset -10
            linear 2.0 yoffset 10
            repeat

        parallel:
            linear 2.0 xoffset 20
            linear 2.0 xoffset -20
            repeat

        parallel:
            easein 1.0 alpha 0.2
            easein 1.0 alpha 1.0
            repeat

image wrackspurt:
    "images/spectrevision/wrackspurt_0000.webp"
    pause 0.12
    "images/spectrevision/wrackspurt_0001.webp"
    pause 0.12
    "images/spectrevision/wrackspurt_0002.webp"
    pause 0.12
    "images/spectrevision/wrackspurt_0003.webp"
    pause 0.12
    "images/spectrevision/wrackspurt_0004.webp"
    pause 0.12
    "images/spectrevision/wrackspurt_0005.webp"
    pause 0.12
    repeat

screen spectrevision():
    zorder 16
    tag spectrevision

    default count = 25 if renpy.mobile else 50

    for i in xrange(count):
        add "object" at OBJwrackspurt

    add "spectrevision"

screen spectrevision_cursor():
    zorder 100
    tag cursor

    $ mpos = renpy.get_mouse_pos()
    add "OBJwrackspurtplayer":
        at transform:
            pos mpos

init python:
    config.per_frame_screens.append("spectrevision_cursor")
