transform sepia():
    matrixcolor SepiaMatrix()

transform uvlight():
    matrixcolor SepiaMatrix("#590098", desat=(1.0, 1.5, 1.0))

transform move_in(x, t):
    xpos x
    linear t xpos 0
    pause t

transform move_fade:
    on show, appear, start:
        alpha 0.0
        xoffset 200
        easein_back 1.0 alpha 1.0 xoffset absolute(0)

    on hide:
        alpha 1.0
        xoffset 0
        easeout_back 1.0 alpha 0.0 xoffset absolute(200)

transform fade_show(t):
    alpha 0
    on show:
        linear t alpha 1

transform fade_show_hide(t):
    alpha 0
    linear t alpha 1
    on hide:
        linear t alpha 0

transform fade_hide(t):
    on hide:
        linear t alpha 0.0

transform blink:
    on show:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat

transform bob(t=1):
    on show, appear, start:
        yoffset absolute(0)
        ease t yoffset absolute(10)
        ease t yoffset absolute(0)
        repeat

transform sprite_blink(img):
    events False
    choice:
        pause 4
    choice:
        pause 3
    choice:
        pause 2
    img
    linear 0.13 alpha 1.0
    pause.05
    linear 0.13 alpha 0.0
    repeat

transform pulse:
    on show:
        xzoom 1.0
        yzoom 1.0
        linear 0.8 xzoom 1.2 yzoom 1.2
        linear 0.8 xzoom 1.0 yzoom 1.0
        repeat

transform move_to(start_x=0, start_y=0, target_x, target_y, duration=1.0):
    on show:
        xpos start_x
        ypos start_y
        linear duration xpos target_x ypos target_y

transform main_sprite_position(x, y, flip, scale):
    xpos x
    ypos y
    xzoom flip
    zoom (1.0/scale)

transform random_rotation(a=-45, b=45):
    rotate random.randint(a, b)
