# Sprite blinking
image spr_tonks blink = sprite_blink("characters/tonks/face/eyes/closed.webp")

# Tonks chibi

image ch_ton stand:
    random_blink("characters/tonks/chibis/nt_stand_blink.webp", "characters/tonks/chibis/nt_walk_01.webp")

image ch_ton stand_shocked:
    size (200,360)
    contains:
        "ch_ton stand"
    contains:
        "characters/tonks/chibis/nt_shocked.webp"

image ch_ton walk:
    "characters/tonks/chibis/nt_walk_01.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_03.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_01.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_05.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04.webp"
    pause.08

    repeat

image ch_ton walk shoes: # Walk shoes layer
    "characters/tonks/chibis/nt_walk_01_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_03_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_01_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_05_shoes.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04_shoes.webp"
    pause.08

    repeat

image ch_ton walk trousers: # Walk trousers layer
    "characters/tonks/chibis/nt_walk_01_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_03_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_02_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_01_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_05_trousers.webp"
    pause.08
    "characters/tonks/chibis/nt_walk_04_trousers.webp"
    pause.08

    repeat

#Drinking chibi
image ch_ton sit_chair:
    zoom 0.5

    # Chair
    contains:
        "characters/tonks/chibis/drinking/chair.webp"

image ch_ton sit:
    zoom 0.5

    # Blinking
    contains:
        "characters/tonks/chibis/drinking/nt_head_01.webp"
        pause 2
        "characters/tonks/chibis/drinking/nt_head_02.webp"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.webp"
        pause 5
        "characters/tonks/chibis/drinking/nt_head_02.webp"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.webp"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_02.webp"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.webp"
        pause 3
        repeat

    # Leg sway
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01.webp"
        pause 2.5
        repeat

image ch_ton sit_trousers:
    zoom 0.5

    # Trousers
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_trousers.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01_trousers.webp"
        pause 2.5
        repeat

image ch_ton sit_shoes:
    zoom 0.5

    # Shoes
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_shoes.webp"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01_shoes.webp"
        pause 2.5
        repeat

image ch_ton sit_top:
    zoom 0.5
    "characters/tonks/chibis/drinking/nt_top.webp"

image ch_ton sit_choker:
    zoom 0.5
    "characters/tonks/chibis/drinking/nt_choker.webp"

image ch_ton bj_desk:
    zoom 0.5
    "characters/tonks/chibis/bj_desk/01.webp"
    pause .3
    "characters/tonks/chibis/bj_desk/02.webp"
    pause .3
    repeat

image ch_ton bj_desk_shocked:
    zoom 0.5
    "characters/tonks/chibis/bj_desk/shocked_01.webp"
    pause .3
    "characters/tonks/chibis/bj_desk/shocked_02.webp"
    pause .3
    repeat

image ch_ton elf:
    zoom 0.5
    anchor (0.5, 1.0)

    "characters/tonks/chibis/elf/default.webp"
    pause 2
    "characters/tonks/chibis/elf/blink.webp"
    pause.08
    "characters/tonks/chibis/elf/default.webp"
    pause 5
    "characters/tonks/chibis/elf/blink.webp"
    pause.08
    "characters/tonks/chibis/elf/default.webp"
    pause.08
    "characters/tonks/chibis/elf/blink.webp"
    pause.08
    "characters/tonks/chibis/elf/default.webp"
    pause 3
    repeat
