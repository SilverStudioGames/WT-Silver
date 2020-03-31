init python:
    ChibiRoom("main_room",  1.0, {
        "base": (None, 250+180), # sna: y 190 (240/245?) gen: y 190
        "mid": (540, None), # cho: x 560 lun: x 580 sna: x 500 gen: x 500
        "desk": (440, None),
        "right": (620, None),
        "on_desk": (350, 180+180+5),
        "behind_desk": (210, 190+250), # def: x 210, y 260
        "door": (750, None),

        # for genie
        "left": (100, None),
        "fireplace": (550, 160+250),
        "cupboard": (260, None),

        # for snape
        "desk_close": (425, 245+250),
    })

    ChibiRoom("quidditch_pitch", 1.4, {
        "base": (None, 500),
        "left": (300, None),
        "mid": (450, None),
        "right": (600, None),
        "stairs_base": (800, 500),
        "stairs_up": (1000, 370),
    })

    ChibiRoom("quidditch_stands", 1.0, {})

    ChibiRoom("room_of_requirement", 1.0, {
        "door": (750, None),
        "left": (200, None),
        "base": (None, 430),
    })

    ChibiRoom("weasley_store", 1.0, {
        "left": (100, None),
        "base": (None, 430),
    })

    ChibiRoom("clothing_store", 1.0, {
        "left": (100, None),
        "base": (None, 430),
    })

    ChibiRoom("potions_room", 1.0, {
        "left": (100, None),
        "base": (None, 430),
    })

    ChibiRoom("floor_seven", 1.0, {
        "base": (None, 430),
        "right": (750, None),
        "left_mid": (200, None),
        "left": (120, None),
    })
