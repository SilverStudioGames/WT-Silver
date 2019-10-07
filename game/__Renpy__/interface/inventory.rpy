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

transform rotate_circular():
    subpixel True

    on show, appear, start:
        rotate 0
        linear 7.0 rotate 360
        repeat

####################################
############# Menu #################
####################################

label inventory_menu(xx=150, yy=90):

    $ hide_transitions = True
    # Styling
    if daytime:
        $ btn_hover = "#edc48240"
    else:
        $ btn_hover = "#7d75aa40"
        
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

    label inventory_menu_after_init:
    $ renpy.block_rollback()

    show screen bld1
    show screen inventory_menu(xx, yy)
    show screen inventory_menuitem(xx, yy)

    $ _return = ui.interact()

    hide screen bld1
    hide screen inventory_menu
    hide screen inventory_menuitem

    if _return[0] == "select":
        if current_item == _return[1]:
            $ current_item = None
        else:
            $ current_item = _return[1]
    elif _return[0] == "use":
        if current_item.number > 0:
            $ renpy.call(_return[1])
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
        $ hide_transitions = False
        jump main_room_menu

    jump inventory_menu_after_init

screen inventory_menu(xx, yy):
    tag inventory_menu
    zorder 4
    modal True

    use top_bar_close_button

    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"

        vbox:
            pos (6, 41)
            for category in inventory_categories_sorted:
                vbox:
                    textbutton category:
                        style "empty"
                        xsize 195 ysize 16
                        text_xalign 0.5
                        if current_category == category:
                            background "interface/achievements/"+interface_color+"/highlight_left.png"
                        else:
                            hover_background "interface/achievements/"+interface_color+"/highlight_left.png"
                            action Return(["category", category])
                    add "interface/achievements/"+interface_color+"/spacer_left.png"
        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            textbutton "Sort by: [current_sorting]":
                style "empty"
                xsize 195 ysize 32
                text_align (0.5, 0.5)
                text_size 12
                hover_background btn_hover
                action Return("sort")

screen inventory_menuitem(xx, yy):
    tag inventory_menuitem
    zorder 4

    frame:
        style "empty"
        pos (xx+217, yy-53)
        xsize 560
        ysize 507
        
        add "interface/achievements/inventory.png"
        add "interface/achievements/"+interface_color+"/panel.png"
        
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
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown))+1) ypos 44 size 16
            vbox:
                pos (570, 186)
                spacing 10

                imagebutton:
                    idle "interface/frames/"+interface_color+"/arrow_up.png"
                    if not current_page <= 0:
                        hover image_hover("interface/frames/"+interface_color+"/arrow_up.png")
                        action Return("dec")

                imagebutton:
                    idle im.Flip("interface/frames/"+interface_color+"/arrow_up.png", vertical=True)
                    if current_page < math.ceil((menu_items_length-1)/items_shown):
                        hover im.Flip(image_hover("interface/frames/"+interface_color+"/arrow_up.png"), vertical=True)
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
                    add "interface/achievements/"+interface_color+"/iconbox.png"
                    if not current_item == None and current_item.id == menu_items[i].id:
                        add "interface/achievements/glow.png" align (0.5, 0.5) zoom 0.105 alpha 0.7 at rotate_circular
                    if menu_items[i].number > 0:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42)
                    else:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42, True)
                    add image_zoom[0] zoom image_zoom[1] align (0.5, 0.5)
                    add "interface/achievements/glass_iconbox.png" pos (3, 2)
                    if current_category == "Gifts":
                        if menu_items[i].number > 0:
                            text str(menu_items[i].number) size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        #else:
                            #text str(menu_items[i].number) size 10 align (0.9, 0.9) color "#FFFFFF80" outlines [ (1, "#00000080", 0, 0) ]
                    button:
                        style "empty"
                        xsize 46 ysize 46
                        hover_background btn_hover
                        action Return(["select", menu_items[i]])
                        tooltip menu_items[i].name
                    
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
                add "interface/achievements/"+interface_color+"/icon_selected.png"
                if current_item.number > 0:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84, True)
                add image_zoom[0] zoom image_zoom[1] align (0.5, 0.5)
                add "interface/achievements/glass_selected.png" pos (6, 6)
                text str(current_item.number) size 14 align (0.90, 0.90) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

            add "interface/achievements/"+interface_color+"/highlight.png" pos (112, 375)
            add "interface/achievements/"+interface_color+"/spacer.png" pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item.name ypos 380 size 16 xoffset 45
                
            if current_category == "Quest Items":
                textbutton "Use" action Return(["use", current_item.event]) xsize 90 ysize 26 xalign 0.89 ypos 374 text_size 16 xoffset 45 style btn_style text_style txt_style
            hbox:
                pos (132, 407)
                xsize 410
                text current_item.description size 12
