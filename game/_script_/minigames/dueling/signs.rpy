init 1 python:
    _sign_value = 0.0
    _sign_max = 0.0

    s_shape = ((235, 129), (235, 128), (235, 125), (235, 123), (235, 122), (235, 120), (235, 118), (235, 117), (235, 114), (235, 113), (234, 111), (234, 108), (233, 106), (233, 104), (232, 103), (232, 102), (231, 100), (231, 99), (230, 96), (230, 95), (228, 93), (227, 90), (224, 88), (224, 86), (223, 84), (222, 84), (220, 83), (219, 82), (217, 80), (216, 80), (215, 79), (213, 77), (211, 76), (208, 75), (206, 74), (204, 74), (201, 74), (200, 74), (198, 74), (194, 74), (191, 74), (190, 74), (188, 74), (186, 74), (182, 74), (179, 75), (178, 76), (176, 76), (174, 76), (169, 78), (164, 80), (163, 80), (158, 82), (152, 84), (148, 86), (146, 87), (143, 89), (141, 90), (139, 92), (137, 93), (134, 95), (133, 96), (129, 100), (127, 103), (124, 107), (122, 109), (120, 112), (120, 113), (119, 116), (118, 119), (117, 123), (117, 126), (117, 130), (118, 132), (120, 136), (120, 137), (123, 141), (127, 144), (130, 148), (135, 152), (136, 153), (140, 155), (141, 156), (145, 158), (147, 159), (152, 163), (157, 166), (164, 168), (168, 172), (170, 172), (175, 176), (176, 176), (179, 179), (186, 183), (191, 188), (196, 191), (200, 195), (201, 196), (205, 200), (208, 203), (209, 204), (212, 208), (215, 212), (217, 215), (220, 218), (220, 219), (220, 221), (220, 223), (221, 224), (221, 226), (222, 228), (222, 231), (222, 234), (222, 236), (222, 239), (222, 241), (222, 245), (222, 246), (221, 248), (221, 250), (220, 252), (218, 255), (218, 256), (216, 259), (215, 263), (212, 265), (212, 269), (211, 270), (209, 272), (208, 272), (207, 275), (206, 275), (204, 277), (200, 280), (199, 282), (198, 282), (196, 284), (195, 284), (193, 285), (192, 285), (188, 286), (186, 287), (185, 287), (182, 287), (179, 288), (176, 288), (175, 288), (172, 288), (171, 288), (168, 287), (167, 287), (164, 286), (162, 285), (159, 284), (155, 281), (150, 278), (149, 277), (146, 275), (144, 275), (140, 272), (136, 268), (134, 267), (131, 265), (128, 263), (128, 262), (125, 260), (124, 260), (122, 257), (122, 256), (120, 255), (120, 254), (118, 253), (118, 252), (117, 252), (116, 251))

    tutorial_shape = [(228.0, 132.0), (229.0, 132.0), (230.0, 131.0), (232.0, 129.0), (232.0, 128.0), (232.0, 127.0), (233.0, 126.0), (233.0, 122.0), (234.0, 117.0), (234.0, 113.0), (234.0, 109.0), (233.0, 104.0), (230.0, 99.0), (228.0, 96.0), (228.0, 94.0), (226.0, 92.0), (226.0, 92.0), (222.0, 88.0), (221.0, 86.0), (219.0, 84.0), (217.0, 83.0), (216.0, 81.0), (215.0, 81.0), (212.0, 80.0), (212.0, 80.0), (210.0, 79.0), (207.0, 77.0), (204.0, 76.0), (201.0, 75.0), (196.0, 75.0), (196.0, 75.0), (192.0, 75.0), (191.0, 75.0), (186.0, 75.0), (180.0, 75.0), (175.0, 76.0), (169.0, 78.0), (165.0, 80.0), (160.0, 81.0), (154.0, 82.0), (150.0, 83.0), (146.0, 84.0), (145.0, 84.0), (143.0, 85.0), (139.0, 87.0), (138.0, 87.0), (136.0, 88.0), (132.0, 90.0), (130.0, 92.0), (127.0, 93.0), (124.0, 95.0), (122.0, 97.0), (122.0, 98.0), (120.0, 100.0), (120.0, 100.0), (119.0, 103.0), (117.0, 105.0), (116.0, 108.0), (116.0, 109.0), (116.0, 112.0), (116.0, 113.0), (116.0, 116.0), (118.0, 119.0), (118.0, 119.0), (120.0, 122.0), (121.0, 125.0), (124.0, 128.0), (126.0, 131.0), (127.0, 132.0), (130.0, 135.0), (132.0, 137.0), (134.0, 140.0), (136.0, 142.0), (139.0, 144.0), (143.0, 148.0), (145.0, 152.0), (148.0, 155.0), (149.0, 155.0), (152.0, 157.0), (152.0, 158.0), (156.0, 161.0), (156.0, 162.0), (160.0, 164.0), (164.0, 167.0), (168.0, 170.0), (172.0, 173.0), (177.0, 176.0), (178.0, 177.0), (180.0, 179.0), (185.0, 180.0), (189.0, 183.0), (192.0, 186.0), (195.0, 188.0), (198.0, 189.0), (201.0, 192.0), (204.0, 196.0), (206.0, 199.0), (208.0, 200.0), (211.0, 203.0), (212.0, 204.0), (213.0, 205.0), (213.0, 206.0), (215.0, 208.0), (216.0, 208.0), (216.0, 211.0), (217.0, 213.0), (219.0, 215.0), (220.0, 216.0), (221.0, 219.0), (221.0, 221.0), (221.0, 222.0), (222.0, 225.0), (223.0, 228.0), (223.0, 232.0), (223.0, 236.0), (223.0, 236.0), (223.0, 239.0), (223.0, 240.0), (223.0, 243.0), (223.0, 244.0), (223.0, 248.0), (223.0, 252.0), (222.0, 253.0), (222.0, 258.0), (221.0, 261.0), (220.0, 264.0), (219.0, 267.0), (217.0, 269.0), (216.0, 272.0), (216.0, 272.0), (214.0, 274.0), (212.0, 277.0), (209.0, 280.0), (207.0, 282.0), (204.0, 284.0), (204.0, 284.0), (202.0, 285.0), (201.0, 285.0), (198.0, 286.0), (195.0, 287.0), (192.0, 287.0), (189.0, 287.0), (188.0, 287.0), (186.0, 288.0), (183.0, 288.0), (182.0, 288.0), (179.0, 288.0), (176.0, 288.0), (172.0, 288.0), (169.0, 288.0), (168.0, 288.0), (165.0, 288.0), (164.0, 288.0), (162.0, 287.0), (159.0, 287.0), (156.0, 285.0), (153.0, 285.0), (153.0, 284.0), (151.0, 284.0), (150.0, 283.0), (149.0, 281.0), (148.0, 280.0), (146.0, 279.0), (144.0, 276.0), (140.0, 274.0), (138.0, 272.0), (137.0, 272.0), (132.0, 268.0), (132.0, 267.0), (132.0, 266.0), (128.0, 265.0), (127.0, 264.0), (125.0, 264.0), (124.0, 263.0), (123.0, 261.0), (121.0, 260.0), (120.0, 260.0), (120.0, 258.0), (119.0, 256.0), (118.0, 256.0), (117.0, 255.0), (116.0, 255.0), (116.0, 254.0)]

    def lerp_sign_power(st, at):
        """Animate the text string value each fraction of a second"""
        # TODO: Find out if global vars can be replaced with class attributes instead.
        global _sign_value, _sign_max

        if _sign_value < 25.0:
            val = _sign_value/25.0
            col = Color("#FFFFFF").interpolate("#0000FF", val)
        elif 50.0 > _sign_value >= 25.0:
            val = max(_sign_value-25.0, 0.0)/25.0
            col = Color("#0000FF").interpolate("#008000", val)
        elif 75.0 > _sign_value >= 50.0:
            val = max(_sign_value-50.0, 0.0)/25.0
            col = Color("#008000").interpolate("#FFFF00", val)
        else:
            val = max(_sign_value-75.0, 0.0)/25.0
            col = Color("#FFFF00").interpolate("#ff0000", val)

        if _sign_value < _sign_max:
            _sign_value = min(_sign_value+1.11, _sign_max)

            return Text("%.2f%%" % _sign_value, color=col, size=32, outlines=[(2, "#000", 0, 0)]), .01
        else:
            return anim.Blink(Text("%.2f%%" % _sign_value, color=col, size=32, outlines=[(2, "#000", 0, 0)])), None

    test_sign = class_draw_canvas(400, 400, s_shape)

screen draw_magic():
    tag draw
    zorder 4

    use bld1

    frame:
        #background "#FFF"
        style "empty"
        padding (0, 0)
        xsize 400
        ysize 400
        xanchor 0.5
        yanchor 0.5
        align (0.5, 0.5)

        add test_sign

    add DynamicDisplayable(lerp_sign_power) xalign 0.5 yalign 0.9

label magic_tutorial:
    "Magician" "Welcome to the very first prototype version of magic dueling!"
    menu:
        "Magician" "Would you like to read the rules and play the tutorial?"
        "Yes please!":
            pass
        "No, fuck off..":
            "Magician" "Rude.. but whatever."
            jump draw_magic

    "Magician" "Draw shapes with mouse to get high score, high score lets you win, the point of the game is to win. Now go get them tiger!"
    m "..............."
    "Magician" "Fine. I'll try to be more descriptive."
    $ test_sign.interactive = False
    show screen draw_magic
    "Magician" "The black shape you see on the screen is called a guideline shape."
    "Magician" "Your goal is to map the shape with your mouse pointer while holding left mouse button. You can start either from top or the bottom."
    $ _trash = class_draw_shape((51, 153, 0), 400, 400, 1)
    $ _trash.shape = tutorial_shape
    $ test_sign.children.append(_trash)
    $ test_sign.force_redraw()
    "Magician" "The closer you get to the original shape the more points you gain which translates to higher spell damage your pokem-- subordinate student will deal to their opponent."
    "Magician" "Now try drawing a shape with your mouse and score at least 50%%, unless you want to be stuck in this tutorial forever."

    label .in_tutorial:

    $ _sign_value = 0.0
    $ _sign_max = 0.0
    $ test_sign.clear()

    $ test_sign.interactive = True

    $ _choice = ui.interact()

    if _choice[0] == "result":
        $ test_sign.interactive = False
        pause 3.0
        if _choice[1] >= 50.0:
            "Magician" "Congratulations, you have passed the test with the score of [_sign_max]%%, I am proud of you!"
            menu:
                "Magician" "Would you like to keep playing?"
                "Yes":
                    pass
                "No":
                    hide screen draw_magic
                    with d3
                    jump cheats.devroom
        else:
            "Magician" "You scored [_sign_max]%% Better luck next time."
            jump magic_tutorial.in_tutorial

    jump draw_magic

label draw_magic:
    $ _sign_value = 0.0
    $ _sign_max = 0.0
    $ test_sign.clear()

    label .after_init:
    $ test_sign.interactive = True

    show screen draw_magic

    $ _choice = ui.interact()

    if _choice[0] == "result":
        $ test_sign.interactive = False
        pause 3.0

        if _choice[1] == 0.0:
            "Magician" "You suck."
        elif 25.0 > _choice[1] > 0.0:
            "Magician" "You still suck."
        elif 50.0 > _choice[1] > 25.0:
            "Magician" "You're average."
        elif 75.0 > _choice[1] > 50.0:
            "Magician" "You're above average."
        elif 100.0 > _choice[1] > 75.0:
            "Magician" "You're good."
        else:
            "Magician" "Holy shit! CRITICAL HIT!"

        menu:
            "Magician" "Try again?"
            "Yes":
                $ _sign_value = 0.0
                $ _sign_max = 0.0
                $ test_sign.clear()
                jump draw_magic.after_init
            "No, I'm done playing your stupid games!":
                "{size=-5}Magician{/size}" ":("
                pass

    hide screen draw_magic
    with d3
    jump cheats.devroom
