init python:
    def inventory_sortfilter(item, sortby="A-z"):
        if sortby == "z-A":
            item = sorted(item, key=lambda x: x.name, reverse=True)
        elif current_sorting == "Available":
            item = sorted(item, key=lambda x: x.number, reverse=True)
        elif current_sorting == "Unavailable":
            item = sorted(item, key=lambda x: x.number)
        else:
            item = sorted(item, key=lambda x: x.name)
        return item

####################################
############# Menu #################
####################################

label inventory:
    $ gui.in_context("inventory_menu")
    jump main_room_menu

label inventory_menu(xx=150, yy=90):
    # Inventory dictionary
    $ inventory_dict = {
                        "Gifts": candy_gift_list+mag_gift_list+drink_gift_list+toy_gift_list,
                        "Quest Items": gen_quest_items_list
                        }

    $ inventory_categories_sorted = ["Gifts", "Quest Items"]
    $ inventory_categories_sorted_length = len(inventory_categories_sorted)

    $ items_shown = 36
    $ current_page = 0
    $ current_item = None
    $ current_category = inventory_categories_sorted[0]
    $ current_sorting = "Available"

    $ category_items = inventory_dict[current_category]
    $ menu_items = inventory_sortfilter(category_items, current_sorting)
    $ menu_items_length = len(menu_items)

    if not renpy.android:
        show screen tooltip

    show screen inventory(xx, yy)
    with d3

    label .after_init:
    $ _return = ui.interact()

    if _return[0] == "select":
        if current_item == _return[1]:
            $ current_item = None
        else:
            $ current_item = _return[1]
    elif _return[0] == "use":
        if current_item.number > 0:
            $ renpy.jump_out_of_context(_return[1])
    elif _return[0] == "category":
        $ current_category = _return[1]
        $ category_items = inventory_dict[current_category]
        $ menu_items = inventory_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
        pass
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        elif current_sorting == "z-A":
            $ current_sorting = "Available"
        elif current_sorting == "Available":
            $ current_sorting = "Unavailable"
        else:
            $ current_sorting = "A-z"
        $ menu_items = inventory_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
    else:
        hide screen inventory
        return

    jump .after_init

screen inventory(xx, yy):
    tag inventory
    zorder 30
    modal True

    add "gui_fade"

    use invisible_button(action=Return("Close"))
    use close_button

    use inventory_menu(xx, yy)
    use inventory_menuitem(xx, yy)

screen inventory_menu(xx, yy):
    frame:
        style "empty"
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 41)
            for category in inventory_categories_sorted:
                vbox:
                    textbutton category:
                        style "empty"
                        xsize 195 ysize 16
                        text_xalign 0.5
                        if current_category == category:
                            background gui.format("interface/achievements/{}/highlight_left.webp")
                        else:
                            hover_background gui.format("interface/achievements/{}/highlight_left.webp")
                            action Return(["category", category])
                    add gui.format("interface/achievements/{}/spacer_left.webp")
        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            textbutton "Sort by: [current_sorting]":
                style gui.theme("overlay_button")
                xsize 195 ysize 32
                text_align (0.5, 0.5)
                text_size 12
                action Return("sort")

screen inventory_menuitem(xx, yy):
    frame:
        style "empty"
        style_prefix gui.theme()
        pos (xx+217, yy-53)
        xysize (560, 507)

        use invisible_button()

        add "interface/achievements/inventory.webp"
        add gui.format("interface/achievements/{}/panel.webp")

        #Western Egg
        button xsize 90 ysize 60 action Function(renpy.play, "sounds/plushie.mp3") xalign 0.5 style "empty"

        text "Inventory" size 22 xalign 0.5 ypos 65

        #text "Unlocked: "+str(len(filter(lambda x: x[1][3] is True, menu_items)))+"/[menu_items_length]" size 12 pos (24, 70)

        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                pos (540, 24)
                spacing 5
                add "interface/page.webp" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown))+1) ypos 44 size 16
            vbox:
                pos (570, 186)
                spacing 10

                imagebutton:
                    idle gui.format("interface/frames/{}/arrow_up.webp")
                    if not current_page <= 0:
                        hover image_hover(gui.format("interface/frames/{}/arrow_up.webp"))
                        action Return("dec")

                imagebutton:
                    idle im.Flip(gui.format("interface/frames/{}/arrow_up.webp"), vertical=True)
                    if current_page < math.ceil((menu_items_length-1)/items_shown):
                        hover im.Flip(image_hover(gui.format("interface/frames/{}/arrow_up.webp")), vertical=True)
                        action Return("inc")

        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 9) % 4
                $ col = i % 9
                frame:
                    style "empty"
                    xsize 48
                    ysize 48
                    pos (24+58*(col), 113+58*(row))
                    add gui.format("interface/achievements/{}/iconbox.webp")

                    if not current_item == None and current_item.id == menu_items[i].id:
                        add "interface/achievements/glow.webp" align (0.5, 0.5) zoom 0.105 alpha 0.7 at rotate_circular

                    if menu_items[i].number > 0:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42)
                    else:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42, True)

                    add image_zoom align (0.5, 0.5)
                    button:
                        style gui.theme("overlay_button")
                        background "interface/achievements/glass_iconbox.webp"
                        xsize 46 ysize 46
                        action Return(["select", menu_items[i]])
                        tooltip menu_items[i].name

                    if current_category == "Gifts":
                        if menu_items[i].number > 0:
                            text str(menu_items[i].number) size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        #else:
                            #text str(menu_items[i].number) size 10 align (0.9, 0.9) color "#FFFFFF80" outlines [ (1, "#00000080", 0, 0) ]

        if menu_items_length <= 0:
            text "Nothing here yet" align (0.5, 0.5) anchor (0.5, 0.5) size 24

        # Add empty items
        #for i in xrange(menu_items_length, items_shown):
            #$ row = (i // 9) % 4
            #$ col = i % 9
            #button xsize 48 ysize 48 style "empty" background "#00000033" xpos 24+58*(col) ypos 113+58*(row)

        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add gui.format("interface/achievements/{}/icon_selected.webp")
                if current_item.number > 0:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84, True)
                add image_zoom align (0.5, 0.5)
                add "interface/achievements/glass_selected.webp" pos (6, 6)
                text str(current_item.number) size 14 align (0.90, 0.90) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

            add gui.format("interface/achievements/{}/highlight.webp") pos (112, 375)
            add gui.format("interface/achievements/{}/spacer.webp") pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item.name ypos 380 size 16 xoffset 45

            if current_category == "Quest Items" and hasattr(current_item, "event"):
                textbutton "Use":
                    xysize (90, 26)
                    xalign 0.89
                    xoffset 45
                    ypos 374
                    text_size 16
                    action Return(["use", current_item.event])
            hbox:
                pos (132, 407)
                xsize 410
                text current_item.description size 12
