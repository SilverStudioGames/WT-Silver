image object:
    Null()

transform OBJbutterfly(hue=random.randint(0, 359)):
    zoom random.uniform(0.4, 0.85)

    choice:
        pause random.randint(1, 7)
        parallel:
            xzoom -1
            pos (-100, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (1200, random.randint(0, 500))
            repeat
        parallel:
            ease_bounce 3 yoffset absolute(-20)
            ease_bounce 3 yoffset absolute(20)
            ease_bounce 3 yoffset absolute(0)
            repeat
        parallel:
            rotate 15
            ease_circ 1.0 rotate 30
            ease_circ 1.0 rotate 15
            repeat
        parallel:
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/0.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/2.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.webp", im.matrix.hue(hue)) with d3
            pause .3
            repeat
    choice:
        pause random.randint(1, 7)
        parallel:
            xzoom 1
            pos (1200, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (-100, random.randint(0, 500))
            repeat
        parallel:
            ease_bounce 3 yoffset absolute(-20)
            ease_bounce 3 yoffset absolute(20)
            ease_bounce 3 yoffset absolute(0)
            repeat
        parallel:
            rotate -15
            ease_circ 1.0 rotate -30
            ease_circ 1.0 rotate -15
            repeat
        parallel:
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/0.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/2.webp", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.webp", im.matrix.hue(hue)) with d3
            pause .3
            repeat
    repeat

transform OBJcloud(start=(random.randint(270, 800), random.randint(60, 130)), speed=random.randint(60, 180)):
    parallel:
        zoom random.uniform(0.6, 1.0)
        pos start
        "images/rooms/_weather_/cloud_small.webp"
        linear speed xpos 800
        xpos 270
        linear speed xpos start[0]
        repeat

transform OBJwrackspurt():
    zoom random.uniform(0.2, 1.0)
    events False

    choice:
        pause random.randint(0, 7)
        "wrackspurt"

        parallel:
            xzoom -1
            pos (-100, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (1200, random.randint(0, 500))
            repeat
        parallel:
            ease_bounce 3 yoffset absolute(-20)
            ease_bounce 3 yoffset absolute(20)
            ease_bounce 3 yoffset absolute(0)
            repeat
        parallel:
            rotate 15
            ease_circ 1.0 rotate 30
            ease_circ 1.0 rotate 15
            repeat
    choice:
        pause random.randint(0, 7)
        "wrackspurt"
        parallel:
            xzoom 1
            pos (1200, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (-100, random.randint(0, 500))
            repeat
        parallel:
            easein 3 yoffset absolute(-20)
            easein 3 yoffset absolute(20)
            easein 3 yoffset absolute(0)
            repeat
        parallel:
            rotate -15
            ease_circ 1.0 rotate -30
            ease_circ 1.0 rotate -15
            repeat
    repeat

image OBJwrackspurtplayer:
    anchor (0.0, 0.0)
    transform_anchor True
    zoom 0.7
    offset (-21, -13)
    events False

    "wrackspurt"

    parallel:
        rotate -10
        ease_circ 1.0 rotate -20
        ease_circ 1.0 rotate -10
        repeat
