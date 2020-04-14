# Sprite blinking
image spr_astoria blink:
    sprite_blink("characters/astoria/face/eyes/closed.png")

# Astoria chibi

image ch_ast stand:
    random_blink("characters/astoria/chibis/ag_stand_blink.png", "characters/astoria/chibis/ag_walk_01.png")

image ch_ast walk:
    "characters/astoria/chibis/ag_walk_01.png"
    pause.08
    "characters/astoria/chibis/ag_walk_02.png"
    pause.08
    "characters/astoria/chibis/ag_walk_03.png"
    pause.08
    "characters/astoria/chibis/ag_walk_02.png"
    pause.08
    "characters/astoria/chibis/ag_walk_01.png"
    pause.08
    "characters/astoria/chibis/ag_walk_04.png"
    pause.08
    "characters/astoria/chibis/ag_walk_05.png"
    pause.08
    "characters/astoria/chibis/ag_walk_04.png"
    pause.08

    repeat

image ch_ast walk_shoes: # Walk shoes layer
    "characters/astoria/chibis/ag_walk_01_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_02_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_03_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_02_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_01_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_04_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_05_shoes.png"
    pause.08
    "characters/astoria/chibis/ag_walk_04_shoes.png"
    pause.08

    repeat

image ch_ast wand:
    size (350, 360) # Set size when using `contains`, so additional transforms work as expected
    contains:
        "characters/astoria/chibis/wand/ag_stand_01.png"

    contains:
        random_blink("characters/astoria/chibis/wand/ag_head_02.png", "characters/astoria/chibis/wand/ag_head_01.png")

image ch_ast wand_casting:
    size (350, 360) # Set size when using `contains`, so additional transforms work as expected
    contains:
        "characters/astoria/chibis/wand_casting/ag_stand_01.png"
        pause.22
        "characters/astoria/chibis/wand_casting/ag_stand_02.png"
        pause.26
        "characters/astoria/chibis/wand_casting/ag_stand_03.png"
        pause.22
        repeat

    contains:
        random_blink("characters/astoria/chibis/wand_casting/ag_head_02.png", "characters/astoria/chibis/wand_casting/ag_head_01.png")

    contains:
        xpos 78
        ypos 78
        "characters/astoria/chibis/wand_casting/sparkles.png"
        linear .48 xoffset -10 yoffset 10
        linear .22 xoffset 10 yoffset -10
        repeat

image ch_ast wand_imperio:
    size (350, 360) # Set size when using `contains`, so additional transforms work as expected
    contains:
        "characters/astoria/chibis/wand_imperio/ag_stand_03.png"
        pause.12
        "characters/astoria/chibis/wand_imperio/ag_stand_01.png"
        pause.12
        "characters/astoria/chibis/wand_imperio/ag_stand_02.png"
        pause 1
        "characters/astoria/chibis/wand_imperio/ag_stand_04.png"

    contains:
        random_blink("characters/astoria/chibis/wand_imperio/ag_head_02.png", "characters/astoria/chibis/wand_imperio/ag_head_01.png")

    contains:
        "blank"
        pause.12
        "characters/astoria/chibis/wand_imperio/ag_head_03.png"
        pause 1
        "blank"

    contains:
        xpos 78
        ypos 78
        alpha 1.0
        "characters/astoria/chibis/wand_imperio/sparkles.png"
        linear .22 xoffset -10 yoffset 10
        linear 1.0 alpha 0.0 xoffset -80 yoffset -4

    contains:
        xpos -28
        ypos 31
        rotate -70
        alpha 0.0
        xzoom 0

        pause.24
        alpha 1.0
        "characters/astoria/chibis/wand_imperio/smoke.png"
        linear 1.0 xzoom 1.0 xpos -34 ypos 37
        "blank"

    contains:
        xpos -34
        ypos -37

        pause 1.24
        "ch_ast imperio_smoke"

image ch_ast imperio_smoke: # Imperio smoke layer
    xoffset 0
    yoffset 72
    rotate -70
    alpha 1.0
    "characters/astoria/chibis/wand_imperio/smoke.png"
    linear 1.0 alpha 0.7 yzoom 0.85 xoffset 16 yoffset 86
    linear 1.0 alpha 1.0 yzoom 1.0 xoffset 0 yoffset 72
    repeat

image ch_ast imperio_shoes: # Imperio shoes layer
    "characters/astoria/chibis/wand_imperio/ag_shoes.png"
    pause 1.24
    "characters/astoria/chibis/wand_imperio/ag_shoes_04.png"
