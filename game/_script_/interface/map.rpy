default UI_xpos_offset = 230
default UI_ypos_offset = 150

default map_unlocked = False

default her_map_location = "library"
default lun_map_location = "room_r"
default ast_map_location = "room_s"
default sus_map_location = "room_h"
default cho_map_location = "training_grounds"

default sna_map_location = "room_potions"
default ton_map_location = "room_defense"

default first_time_7th = True
default pitch_open = True

default map_animated = "once"

define map_scale = 0.35
define map_ani_time = 1.5

transform map_fadein:
    alpha 0
    pause (map_ani_time)
    linear 1 alpha 1

image map_unfold:
    "interface/map/anim/map_03.webp"
    pause map_ani_time/3
    "interface/map/anim/map_02.webp" with Dissolve(map_ani_time/3)
    pause map_ani_time/3
    "interface/map/anim/map_01.webp" with Dissolve(map_ani_time/3)
    pause map_ani_time/3
    "interface/map/map.webp" with Dissolve(1)
    pause 1
    "interface/map/map.webp"

screen map_screen():
    tag map
    zorder 4

    # Default avoids changing the screen if the animation is toggled quickly
    default unfold = map_animated

    # Disable animation after first time (can still be toggled)
    if map_animated == "once":
        timer map_ani_time+1 action SetVariable("map_animated", False)

    if unfold:
        add "map_unfold" xpos UI_xpos_offset ypos UI_ypos_offset zoom map_scale # 588x420
    else:
        add "interface/map/map.webp" xpos UI_xpos_offset ypos UI_ypos_offset zoom map_scale # 588x420

    fixed:
        if unfold:
            at map_fadein
        use map_buttons
        use map_screen_characters

screen map_buttons():
    tag map
    zorder 4
    #Office
    imagebutton:
        xpos UI_xpos_offset +112
        ypos UI_ypos_offset +234
        idle "interface/map/room_office_idle.webp"
        hover "interface/map/room_office_hover.webp"
        hovered SetVariable("ball_hint", "office")
        unhovered SetVariable("ball_hint", None)
        action Return("main_room")

    #Gryffindor
    imagebutton:
        xpos UI_xpos_offset +148
        ypos UI_ypos_offset +214
        idle "interface/map/room_gryffindor_idle.webp"
        hover "interface/map/room_gryffindor_hover.webp"
        hovered SetVariable("ball_hint", "dorm_gryffindor")
        unhovered SetVariable("ball_hint", None)
        action Return("gryffindor_dormitories")

    #Ravenclaw
    imagebutton:
        xpos UI_xpos_offset +286
        ypos UI_ypos_offset +256
        idle "interface/map/room_ravenclaw_idle.webp"
        hover "interface/map/room_ravenclaw_hover.webp"
        hovered SetVariable("ball_hint", "dorm_ravenclaw")
        unhovered SetVariable("ball_hint", None)
        action Return("ravenclaw_dormitories")

    #Hufflepuff
    imagebutton:
        xpos UI_xpos_offset +76
        ypos UI_ypos_offset +295
        idle "interface/map/room_hufflepuff_idle.webp"
        #hovered SetVariable("ball_hint", "dorm_hufflepuff")
        #unhovered SetVariable("ball_hint", None)
        #hover "interface/map/room_hufflepuff_hover.webp"
        #action Return("hufflepuff_dormitories")

    #Slytherin
    imagebutton:
        xpos UI_xpos_offset +214
        ypos UI_ypos_offset +136
        idle "interface/map/room_slytherin_idle.webp"
        #hovered SetVariable("ball_hint", "dorm_slytherin")
        #unhovered SetVariable("ball_hint", None)
        #hover "interface/map/room_slytherin_hover.webp"
        #action Return("slytherin_dormitories")

    #Weasley Store 15 x 15
    if not item_store_intro_done:
        add "interface/achievements/glow.webp" pos (UI_xpos_offset+246, UI_ypos_offset+231) align (0.5, 0.5) offset (15, 15) zoom 0.15 alpha 0.5 at rotate_circular
    imagebutton:
        xpos UI_xpos_offset +246
        ypos UI_ypos_offset +231
        idle "interface/map/room_weasley_store_idle.webp"
        hover "interface/map/room_weasley_store_hover.webp"
        hovered SetVariable("ball_hint", "weasley_store")
        unhovered SetVariable("ball_hint", None)
        action Return("item_store")

    #Clothing Store
    if not clothing_store_intro_done:
        add "interface/achievements/glow.webp" pos (UI_xpos_offset+462, UI_ypos_offset+231) align (0.5, 0.5) offset (15, 15) zoom 0.15 alpha 0.5 at rotate_circular
    imagebutton:
        xpos UI_xpos_offset +462
        ypos UI_ypos_offset +231
        idle "interface/map/room_clothing_store_idle.webp"
        hover "interface/map/room_clothing_store_hover.webp"
        hovered SetVariable("ball_hint", "clothing_store")
        unhovered SetVariable("ball_hint", None)
        action Return("clothing_store")

    # TODO: Uncomment after Snape's office has been implemented.
    #Potions
    # imagebutton:
        # xpos UI_xpos_offset +314
        # ypos UI_ypos_offset +331
        # idle "interface/map/room_potions_idle.webp"
        # unhovered SetVariable("ball_hint", None)
        # if item_store_intro_done:
            # hover "interface/map/room_potions_hover.webp"
            # hovered SetVariable("ball_hint", "potions")
            # action Return("potions_room")

    #Room of Requirement
    if unlocked_7th:
        if not mirror_intro_done:
            add "interface/achievements/glow.webp" pos (UI_xpos_offset+116, UI_ypos_offset+160) align (0.5, 0.5) offset (15, 15) zoom 0.15 alpha 0.5 at rotate_circular
        imagebutton:
            xpos UI_xpos_offset +116
            ypos UI_ypos_offset +160
            unhovered SetVariable("ball_hint", None)
            if first_time_7th == True:
                idle "interface/map/room_ror_empty_idle.webp"
                hover "interface/map/room_ror_empty_hover.webp"
                hovered SetVariable("ball_hint", "room_of_req")
                action Return("floor_7th")
            else:
                idle "interface/map/room_ror_idle.webp"
                hover "interface/map/room_ror_hover.webp"
                hovered SetVariable("ball_hint", "room_of_req")
                action Return("floor_7th")

    #Lake
    imagebutton:
        xpos UI_xpos_offset +131
        ypos UI_ypos_offset +367
        idle "interface/map/room_boat_house_idle.webp"
        hover "interface/map/room_boat_house_hover.webp"
        hovered SetVariable("ball_hint", "lake")
        unhovered SetVariable("ball_hint", None)
        action Return("map_lake")

    #Forest
    imagebutton:
        xpos UI_xpos_offset +103
        ypos UI_ypos_offset +12
        idle "interface/map/room_north_courtyard_idle.webp"
        hover "interface/map/room_north_courtyard_hover.webp"
        hovered SetVariable("ball_hint", "forest")
        unhovered SetVariable("ball_hint", None)
        action Return("map_forest")

    #Attic
    if tentacle_scroll_examined:
        if not tentacle_sample:
            add "interface/achievements/glow.webp" pos (UI_xpos_offset+340, UI_ypos_offset+226) align (0.5, 0.5) offset (15, 15) zoom 0.15 alpha 0.5 at rotate_circular
            imagebutton:
                xpos UI_xpos_offset +340
                ypos UI_ypos_offset +226
                idle "interface/map/room_attic_closed_idle.webp"
                hover "interface/map/room_attic_closed_hover.webp"
                hovered SetVariable("ball_hint", "attic")
                unhovered SetVariable("ball_hint", None)
                action Return("map_attic")
        else:
            imagebutton:
                xpos UI_xpos_offset +340
                ypos UI_ypos_offset +226
                idle "interface/map/room_attic_open_idle.webp"
                hover "interface/map/room_attic_open_hover.webp"
                hovered SetVariable("ball_hint", "attic")
                unhovered SetVariable("ball_hint", None)
                action Return("map_attic")

    # Map animation toggle
    text "Animation" xpos 700+21 ypos 530+10 size 10
    imagebutton:
        xpos 700
        ypos 530
        idle gui.format("interface/general/{}/check_false_hidden.webp")
        hover gui.format("interface/general/{}/check_true.webp")
        selected_idle gui.format("interface/general/{}/check_true_hidden.webp")
        selected_hover gui.format("interface/general/{}/check_false.webp")
        tooltip "Toggles map folding animation"
        action ToggleVariable("map_animated", True, False)

label map_locations:


label set_her_map_location(location=""):

    if location != "":
        if location == "library":
            $ her_map_location = "library"
        elif location in ["gryffindor_room","gryff_room","room_g"]:
            $ her_map_location = "room_g"
        elif location in ["slytherin_room","slyth_room","room_s"]:
            $ her_map_location = "room_s"
        elif location == "great_hall":
            $ her_map_location = "great_hall"
        elif location == "courtyard":
            $ her_map_location = "courtyard"

    else: #Random
        if her_whoring < 11:
            if random_map_loc in [1,2]: #Library
                $ her_map_location = "library"
            elif random_map_loc in [3]: #Great Hall
                $ her_map_location = "great_hall"
            else: #Gryff Room
                $ her_map_location = "room_g"
        else:
            if her_reputation < 12:
                if random_map_loc == 1: #Great Hall
                    $ her_map_location = "great_hall"
                elif random_map_loc == 2: #Courtyard
                    $ her_map_location = "courtyard"
                else: #Gryff Room
                    $ her_map_location = "room_g"
            else:
                if random_map_loc == 1: #Slytherin Room
                    $ her_map_location = "room_s"
                elif random_map_loc == 2: #Courtyard
                    $ her_map_location = "courtyard"
                else: #Gryff Room
                    $ her_map_location = "room_g"

            if hg_blowjob.trigger == True and game.weather in ("clear", "cloudy") and not game.daytime and not hermione_busy:
                $ her_map_location = "forest"

    call update_character_map_locations

    return

label set_lun_map_location(location = ""):

    if location != "":
        if location == "greenhouse":
            $ lun_map_location = "greenhouse"
        elif location == "forest":
            $ lun_map_location = "forest"
        elif location in ["ravenclaw_room","raven_room","room_r"]:
            $ lun_map_location = "room_r"

    else: #Random
        if random_map_loc in [1]:
            $ lun_map_location = "greenhouse"
        elif random_map_loc in [2,3]:
            $ lun_map_location = "forest"
        else: #Ravenclaw Room
            $ lun_map_location = "room_r"

    call update_character_map_locations

    return

label set_ast_map_location(location = ""):
    if location != "":
        if location == "courtyard":
            $ ast_map_location = "courtyard"
        elif location in ["slytherin_room","slyth_room","room_s"]:
            $ ast_map_location = "room_s"
        elif location in ["defense_classroom"]:
            $ ast_map_location = "defense"

    else: #Random
        if random_map_loc in [1,2]:
            $ ast_map_location = "courtyard"
        else: #Slytherin Room
            $ ast_map_location = "room_s"

    call update_character_map_locations

    return

label set_sus_map_location(location = ""):
    if location != "":
        if location == "great_hall":
            $ sus_map_location = "great_hall"
        elif location in ["hufflepuff_room","huffl_room","room_h"]:
            $ sus_map_location = "room_r"

    else: #Random
        if random_map_loc in [1,2]:
            $ sus_map_location = "great_hall"
        else: #Hufflepuff Room
            $ sus_map_location = "room_h"

    call update_character_map_locations

    return

label set_cho_map_location(location = ""):
    if location != "":
        if location == "training_grounds":
            $ cho_map_location = "training_grounds"
        elif location in ["ravenclaw_room","raven_room","room_r"]:
            $ cho_map_location = "room_r"

    else: #Random
        if random_map_loc in [1,2]:
            $ cho_map_location = "training_grounds"
        else: #Ravenclaw Room
            $ cho_map_location = "room_r"

    call update_character_map_locations

    return

label update_character_map_locations:
    if her_map_location == "library":
        $ her_map_xpos = 685
        $ her_map_ypos = 94
    if her_map_location == "room_g":
        $ her_map_xpos = 340
        $ her_map_ypos = 212
    if her_map_location == "room_s":
        $ her_map_xpos = 440
        $ her_map_ypos = 184
    if her_map_location == "great_hall":
        $ her_map_xpos = 300
        $ her_map_ypos = 240
    if her_map_location == "courtyard":
        $ her_map_xpos = 674
        $ her_map_ypos = 216
    if her_map_location == "forest":
        $ her_map_xpos = 290
        $ her_map_ypos = 40

    #Luna
    if lun_map_location == "room_r":
        $ lun_map_xpos = 536
        $ lun_map_ypos = 242
    if lun_map_location == "forest":
        $ lun_map_xpos = 430
        $ lun_map_ypos = 50
    if lun_map_location == "greenhouse":
        $ lun_map_xpos = 680
        $ lun_map_ypos = 320

    #Astoria
    if ast_map_location == "room_s":
        $ ast_map_xpos = 476
        $ ast_map_ypos = 118
    if ast_map_location == "courtyard":
        $ ast_map_xpos = 634
        $ ast_map_ypos = 254
    if ast_map_location == "defense": #Event
        $ ast_map_xpos = 530
        $ ast_map_ypos = 190

    #Susan
    if sus_map_location == "room_h":
        $ sus_map_xpos = 360
        $ sus_map_ypos = 320
    if sus_map_location == "great_hall":
        $ sus_map_xpos = 300
        $ sus_map_ypos = 280

    #Cho
    if cho_map_location == "room_r":
        $ cho_map_xpos = 494
        $ cho_map_ypos = 276
    if cho_map_location == "training_grounds":
        $ cho_map_xpos = 750
        $ cho_map_ypos = 50

    #Tonks
    $ ton_map_xpos = 548
    $ ton_map_ypos = 156

    #Snape
    $ sna_map_xpos = 598
    $ sna_map_ypos = 348

    return

screen map_screen_characters():
    tag map
    zorder 5

    $ UI_xpos_offset = 0

    #Hermione
    if hermione_unlocked:
        if her_map_location == "forest": # Mark forest event.
            add "interface/achievements/glow.webp" pos (UI_xpos_offset+her_map_xpos, UI_ypos_offset+her_map_ypos) align (0.5, 0.5) zoom 0.15 alpha 0.5 at rotate_circular
        imagebutton:
            xpos +UI_xpos_offset +her_map_xpos
            ypos +UI_ypos_offset +her_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_hermione.webp"
            hover "interface/map/name_hermione_hover.webp"
            hovered SetVariable("ball_hint", "summon_hermione")
            unhovered SetVariable("ball_hint", None)
            action Return("hermione")

    #Luna
    if luna_unlocked:
        imagebutton:
            xpos UI_xpos_offset+ lun_map_xpos
            ypos UI_ypos_offset+ lun_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_luna.webp"
            hover "interface/map/name_luna_hover.webp"
            hovered SetVariable("ball_hint", "summon_luna")
            unhovered SetVariable("ball_hint", None)
            action Return("luna")

    #Astoria
    if astoria_unlocked:
        imagebutton:
            xpos UI_xpos_offset +ast_map_xpos
            ypos UI_ypos_offset +ast_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_astoria.webp"
            hover "interface/map/name_astoria_hover.webp"
            hovered SetVariable("ball_hint", "summon_astoria")
            unhovered SetVariable("ball_hint", None)
            action Return("astoria")

    #Susan
    if susan_unlocked:
        imagebutton:
            xpos UI_xpos_offset +sus_map_xpos
            ypos UI_ypos_offset +sus_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_susan.webp"
            hover "interface/map/name_susan_hover.webp"
            hovered SetVariable("ball_hint", "summon_susan")
            unhovered SetVariable("ball_hint", None)
            action Return("susan")

    #Cho
    if cho_unlocked:
        imagebutton:
            xpos UI_xpos_offset +cho_map_xpos
            ypos UI_ypos_offset +cho_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_cho.webp"
            hover "interface/map/name_cho_hover.webp"
            hovered SetVariable("ball_hint", "summon_cho")
            unhovered SetVariable("ball_hint", None)
            action Return("cho")

    #Snape
    if snape_unlocked:
        imagebutton:
            xpos UI_xpos_offset +sna_map_xpos
            ypos UI_ypos_offset +sna_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_snape.webp"
            hover "interface/map/name_snape_hover.webp"
            hovered SetVariable("ball_hint", "summon_snape")
            unhovered SetVariable("ball_hint", None)
            action Return("snape")

    #Tonks
    if tonks_unlocked:
        imagebutton:
            xpos UI_xpos_offset +ton_map_xpos
            ypos UI_ypos_offset +ton_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_tonks.webp"
            hover "interface/map/name_tonks_hover.webp"
            hovered SetVariable("ball_hint", "summon_tonks")
            unhovered SetVariable("ball_hint", None)
            action Return("tonks")
