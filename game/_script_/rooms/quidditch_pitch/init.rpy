
screen quid_pitch_back():
    sensitive False
    zorder 0
    add "images/rooms/quidditch_pitch/back.webp" zoom 0.5
    if game.weather == "cloudy":
        for i in xrange(random.randint(2, 5)):
            add "object" at OBJcloud
    add "images/rooms/quidditch_pitch/back_overlay.webp" zoom 0.5

screen quid_pitch_mid():
    sensitive False
    zorder 2
    add "images/rooms/quidditch_pitch/mid.webp" zoom 0.5

screen quid_pitch_front():
    sensitive False
    zorder 5
    add "images/rooms/quidditch_pitch/front.webp" zoom 0.5
    for i in xrange(random.randint(1, 3)):
        add "object" at OBJbutterfly
