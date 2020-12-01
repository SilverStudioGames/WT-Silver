
label decorate_room_menu:

    $ item_list = [wall_deco_list, fireplace_deco_list, cupboard_deco_list+misc_deco_list+misc_hat_list]

    show screen bottom_menu("decorate_room_menu", (
        ("Posters", "deco_wall"), ("Trophies", "ui_quest_items"), ("Miscellaneous", "deco_cupboard")
    ), item_list, "ui_delete")
    with d3

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, tuple):
        if _return[1].owned > 0 or _return[1].unlocked:
            call use_deco_item(_return[1])
            $ achievement.unlock("decorator")
        else:
            ">You haven't unlocked this decoration yet."

    elif _return == "func":
        hide screen bottom_menu
        with d3
        menu:
            ">Remove all decorations?"
            "-Yes-":
                # Loop through all decorations and deactivate them
                python:
                    for i in xrange(len(wall_deco_list)):
                        wall_deco_list[i].active = False
                    for i in xrange(len(fireplace_deco_list)):
                        fireplace_deco_list[i].active = False
                    for i in xrange(len(cupboard_deco_list)):
                        cupboard_deco_list[i].active = False
                    for i in xrange(len(misc_deco_list)):
                        misc_deco_list[i].active = False
                    for i in xrange(len(misc_hat_list)):
                        misc_hat_list[i].active = False

                    poster_OBJ.room_image = ""
                    trophy_OBJ.room_image = ""
                    cupboard_deco = ""
                    cupboard_deco_OBJ.room_image = ""
                    phoenix_deco_OBJ.room_image = ""
                    fireplace_deco_OBJ.room_image = ""
                    owl_deco_OBJ.room_image = ""
                    owl_OBJ.room_image = "owl_idle"
                    owl_OBJ.idle_image = "owl_letter"
                    owl_OBJ.hover_image = "owl_hover"
            "-No-":
                pass
        jump decorate_room_menu

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3
        jump main_room_menu

    jump .interact

label use_deco_item(item=None): # Add the 'item' decoration to the room. Remove it when 'item' is currently displayed as a deco.
    if item.type == "poster":
        # Loop through all posters and deactivate them
        python:
            for i in xrange(len(wall_deco_list)):
                wall_deco_list[i].active = False

        if poster_OBJ.room_image == item.id:
            $ poster_OBJ.room_image = ""
        else:
            $ poster_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "trophy":
        python:
            for i in xrange(len(fireplace_deco_list)):
                fireplace_deco_list[i].active = False

        if trophy_OBJ.room_image == item.id:
            $ trophy_OBJ.room_image = ""
        else:
            $ trophy_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "cupboard":
        if cupboard_deco_OBJ.room_image == item.id:
            $ cupboard_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ cupboard_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "pinup":
        if cupboard_deco == item.id:
            $ cupboard_deco = ""
            $ item.active = False
        else:
            $ cupboard_deco = item.id
            $ item.active = True
    elif item.type == "phoenix":
        if phoenix_deco_OBJ.room_image == item.id:
            $ phoenix_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ phoenix_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "fireplace":
        if fireplace_deco_OBJ.room_image == item.id:
            $ fireplace_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ fireplace_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "owl":
        if owl_deco_OBJ.room_image == item.id:
            $ owl_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ owl_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "mail":
        if owl_OBJ.room_image == item.id:
            $ owl_OBJ.room_image = "owl_idle"
            $ owl_OBJ.idle_image = "owl_letter"
            $ owl_OBJ.hover_image = "owl_letter_hover"
            $ item.active = False
        else:
            $ owl_OBJ.room_image = item.id
            $ owl_OBJ.idle_image = "owl_letter_black"
            $ owl_OBJ.hover_image = "owl_letter_hover_black"
            $ item.active = True
    return
