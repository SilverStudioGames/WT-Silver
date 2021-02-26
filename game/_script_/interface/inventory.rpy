init python:
    def inventory_sortfilter(item, sortby="A-z", filtering=None):
        if filtering == "Owned":
            item = filter(lambda x: x.owned > 0, item)

        if sortby == "z-A":
            item = sorted(item, key=lambda x: x.name, reverse=True)
        elif current_sorting == "Available":
            item = sorted(item, key=lambda x: x.owned, reverse=True)
        elif current_sorting == "Unavailable":
            item = sorted(item, key=lambda x: x.owned)
        else:
            item = sorted(item, key=lambda x: x.name)
        return item

default inventory_mode = 0 # 0 - Inventory, 1 - gifts

####################################
############# Menu #################
####################################

label inventory:
    $ gui.in_context("inventory_menu")
    jump main_room_menu

label inventory_menu(xx=150, yy=90):
    # Inventory dictionary
    $ inventory_dict = {
        "Gifts": inventory.get_instances_of_type("gift"),
        "Books": inventory.get_instances_of_type("book"),
        "Scrolls": inventory.get_instances_of_type("scroll"),
        "Ingredients": inventory.get_instances_of_type("ingredient"),
        "Potions": inventory.get_instances_of_type("potion"),
        "Decorations": inventory.get_instances_of_type("decoration"),
        "Quest Items": inventory.get_instances_of_type("quest"),
    }

    $ items_shown = 36
    $ current_page = 0
    $ current_item = None
    $ current_category = next(iter(inventory_dict.iterkeys()))
    $ current_filter = "Owned"
    $ current_sorting = "Available"

    $ category_items = inventory_dict[current_category]
    $ menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
    $ menu_items_length = len(menu_items)

    if not renpy.android:
        show screen tooltip

    show screen inventory(xx, yy)

    label .after_init:
    $ _choice = ui.interact()

    if _choice[0] == "select":
        if current_item == _choice[1]:
            $ current_item = None
        else:
            $ current_item = _choice[1]
    elif _choice[0] == "category":
        $ current_category = _choice[1]
        $ category_items = inventory_dict[current_category]
        $ menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
        pass
    elif _choice == "inc":
        $ current_page += 1
    elif _choice == "dec":
        $ current_page += -1
    elif _choice == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        elif current_sorting == "z-A":
            $ current_sorting = "Available"
        elif current_sorting == "Available":
            $ current_sorting = "Unavailable"
        else:
            $ current_sorting = "A-z"
        $ menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
    elif _choice == "filter":
        if current_filter == None:
            $ current_filter = "Owned"
        else:
            $ current_filter = None
        $ menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
    elif _choice == "use":
        $ current_item.use()
    elif _choice == "give":
        hide screen inventory
        $ renpy.call(get_character_gift_label(active_girl), current_item)
        $ enable_game_menu()
        $ renpy.jump_out_of_context("{}_requests".format(active_girl))
    else:
        hide screen inventory
        return

    jump .after_init

screen inventory(xx, yy):
    tag inventory
    zorder 30
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button

    fixed:
        if settings.get("animations"):
            at gui_animation
        use inventory_menu(xx, yy)
        use inventory_menuitem(xx, yy)

screen inventory_menu(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme('achievements')
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 41)
            for category in inventory_dict.iterkeys():
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

            # Gold & Tokens
            null height 16
            text "{color=#daa520}Gold{/color} {outlinecolor=#ffffff00}[game.gold]{/outlinecolor}" size 12 outlines [ (2, "#000", 0, 0) ] xalign 0.1 xanchor 0
            add gui.format("interface/achievements/{}/spacer_left.webp")
            text "{color=#2055da}Tokens{/color} {outlinecolor=#ffffff00}[tokens]{/outlinecolor}" size 12 outlines [ (2, "#000", 0, 0) ] xalign 0.1 xanchor 0
            add gui.format("interface/achievements/{}/spacer_left.webp")

        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)
            if current_filter == None:
                textbutton "Show: All" action Return("filter")
            else:
                textbutton "Show: [current_filter]" action Return("filter")
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen inventory_menuitem(xx, yy):
    window:
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
                    idle Transform(gui.format("interface/frames/{}/arrow_up.webp"), xzoom=-1)
                    if current_page < math.ceil((menu_items_length-1)/items_shown):
                        hover Transform(image_hover(gui.format("interface/frames/{}/arrow_up.webp")), xzoom=-1)
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

                    if menu_items[i].owned > 0:
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

                    if current_category in {"Gifts", "Ingredients", "Potions"}:
                        if menu_items[i].owned > 0:
                            text str(menu_items[i].owned) size 10 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                    elif current_category == "Decorations":
                        if menu_items[i].in_use:
                            add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) zoom 0.5

        if menu_items_length <= 0:
            text "Nothing here yet" align (0.5, 0.5) anchor (0.5, 0.5) size 24

        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add gui.format("interface/achievements/{}/icon_selected.webp")
                if current_item.owned > 0:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84, True)
                add image_zoom align (0.5, 0.5)
                add "interface/achievements/glass_selected.webp" pos (6, 6)
                text str(current_item.owned) size 14 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

            add gui.format("interface/achievements/{}/highlight.webp") pos (112, 375)
            add gui.format("interface/achievements/{}/spacer.webp") pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item.name ypos 380 size 16 xoffset 45

            if inventory_mode == 0 and current_item.usable:
                textbutton "Use":
                    xysize (90, 26)
                    xalign 0.89
                    xoffset 45
                    ypos 374
                    text_size 16
                    sensitive (current_item.owned > 0)
                    action Return("use")
            elif inventory_mode == 1 and current_item.givable:
                textbutton "Give":
                    xysize (90, 26)
                    xalign 0.89
                    xoffset 45
                    ypos 374
                    text_size 16
                    sensitive (current_item.owned > 0)
                    action Return("give")

            hbox:
                pos (132, 407)
                xsize 410
                text current_item.desc size 12
