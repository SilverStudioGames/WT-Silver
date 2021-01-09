init python:
    ChibiRoom("main_room",  1.0, {
        "base": (None, 430),
        "back": (None, 400),
        "mid": (540, None),
        "desk": (440, None),
        "right": (620, None),
        "by_desk": (335, None),
        "on_desk": (350, 365),
        "behind_desk": (210, 440),
        "door": (750, None),

        # for genie
        "left": (100, None),
        "fireplace": (550, 410),
        "cupboard": (260, None),

        # for snape
        "desk_close": (425, 435),
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

    ChibiRoom("floor_seven", 1.0, {
        "base": (None, 430),
        "right": (750, None),
        "left_mid": (200, None),
        "left": (120, None),
    })
