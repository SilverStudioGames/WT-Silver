init python:
    def shop_item_sortfilter(item, sortby="Price (Asc)", filtering=None):
        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: x.name)

        if sortby == "Price (Asc)":
            item = sorted(item, key=lambda x: x.price, reverse=False)
        elif current_sorting == "Price (Desc)":
            item = sorted(item, key=lambda x: x.price, reverse=True)
        return item

label shop_item:
    $ gui.in_context("shop_item_menu")
    return

label shop_item_menu(xx=150, yy=90):
    $ inventory_dict = {
        "Gifts": inventory.get_instances_of_type("gift"),
        "Books": inventory.get_instances_of_type("book"),
        "Scrolls": inventory.get_instances_of_type("scroll"),
        "Ingredients": inventory.get_instances_of_type("ingredient"),
        "Decorations": inventory.get_instances_of_type("decoration"),
        "Quest Items": inventory.get_instances_of_type("quest"),
    }

    $ items_shown = 36
    $ current_page = 0
    $ current_item = None
    $ current_category = next(iter(inventory_dict.iterkeys()))
    $ current_sorting = "Price (Asc)"

    if current_category in {"Gifts", "Ingredients"}:
        $ category_items = filter(lambda x: bool(x.price > 0), inventory_dict[current_category])
    elif current_category in {"Books", "Scrolls", "Decorations", "Quest Items"}:
        $ category_items = filter(lambda x: bool(x.price > 0 and x.owned < 1), inventory_dict[current_category])

    $ menu_items = shop_item_sortfilter(category_items, current_sorting)
    $ menu_items_length = len(menu_items)

    if not renpy.android:
        show screen tooltip

    show screen shop_item(xx, yy)
    with d3

    label .after_init:
    $ _return = ui.interact()

    if _return[0] == "select":
        if current_item == _return[1]:
            $ current_item = None
        else:
            $ current_item = _return[1]
    elif _return[0] == "category":
        $ current_category = _return[1]
        if current_category in {"Gifts", "Ingredients"}:
            $ category_items = filter(lambda x: bool(x.price > 0), inventory_dict[current_category])
        elif current_category in {"Books", "Scrolls", "Decorations", "Quest Items"}:
            $ category_items = filter(lambda x: bool(x.price > 0 and x.owned < 1), inventory_dict[current_category])
        $ menu_items = shop_item_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
        pass
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return == "sort":
        if current_sorting == "Price (Asc)":
            $ current_sorting = "Price (Desc)"
        elif current_sorting == "Price (Desc)":
            $ current_sorting = "Price (Asc)"

        $ menu_items = shop_item_sortfilter(category_items, current_sorting)
    elif _return == "buy":
        if current_category == "Decorations":
            $ tokens -= current_item.price
        else:
            $ game.gold -= current_item.price

        $ current_item.owned += 1
        $ renpy.play("sounds/money.mp3")

        if current_category in {"Gifts", "Ingredients"}:
            $ category_items = filter(lambda x: bool(x.price > 0), inventory_dict[current_category])
        elif current_category in {"Books", "Scrolls", "Decorations", "Quest Items"}:
            $ category_items = filter(lambda x: bool(x.price > 0 and x.owned < 1), inventory_dict[current_category])
        $ menu_items = shop_item_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
    else:
        hide screen inventory
        return

    jump .after_init

screen shop_item(xx, yy):
    tag shop_item
    zorder 30
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button

    use shop_item_menu(xx, yy)
    use shop_item_menuitem(xx, yy)

screen shop_item_menu(xx, yy):
    frame:
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
        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen shop_item_menuitem(xx, yy):
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

        text "Store" size 22 xalign 0.5 ypos 65

        if current_category == "Decorations":
            text "{color=#2055da}T{/color} {outlinecolor=#ffffff00}[tokens]{/outlinecolor}" size 16 pos (24, 70) outlines [ (2, "#000", 0, 0) ]
        else:
            text "{color=#daa520}G{/color} {outlinecolor=#ffffff00}[game.gold]{/outlinecolor}" size 16 pos (24, 70) outlines [ (2, "#000", 0, 0) ]

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
                $ price = menu_items[i].price

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

                    if ((current_category == "Decorations" and tokens >= menu_items[i].price) or (menu_items[i].owned < 99 and game.gold >= menu_items[i].price)):
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

                    if menu_items[i].owned > 0:
                        text str(menu_items[i].owned) size 10 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

                    if current_category == "Decorations":
                        if tokens >= menu_items[i].price:
                            text "{color=#2055da}T{/color} [price]" size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        else:
                            text "{color=#2055da}T{/color} {color=#ff0000}[price]{/color}" size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                    else:
                        if game.gold >= menu_items[i].price:
                            text "{color=#daa520}G{/color} [price]" size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        else:
                            text "{color=#daa520}G{/color} {color=#ff0000}[price]{/color}" size 10 align (0.95, 0.95) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

        if menu_items_length <= 0:
            text "Nothing here yet" align (0.5, 0.5) anchor (0.5, 0.5) size 24

        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add gui.format("interface/achievements/{}/icon_selected.webp")

                if (current_category == "Decorations" and tokens >= current_item.price) or (current_item.owned < 99 and game.gold >= current_item.price):
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84, True)

                add image_zoom align (0.5, 0.5)
                add "interface/achievements/glass_selected.webp" pos (6, 6)

                if current_item.owned > 0:
                    text "[current_item.owned]" size 14 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

                if current_category == "Decorations":
                    if tokens >= current_item.price:
                        text "{color=#2055da}T{/color} [current_item.price]" size 14 align (0.9, 0.9) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                    else:
                        text "{color=#2055da}T{/color} {color=#ff0000}[current_item.price]{/color}" size 14 align (0.90, 0.90) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                else:
                    if game.gold >= current_item.price:
                        text "{color=#daa520}G{/color} [current_item.price]" size 14 align (0.9, 0.9) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                    else:
                        text "{color=#daa520}G{/color} {color=#ff0000}[current_item.price]{/color}" size 14 align (0.90, 0.90) anchor (1.0, 1.0) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]

            add gui.format("interface/achievements/{}/highlight.webp") pos (112, 375)
            add gui.format("interface/achievements/{}/spacer.webp") pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item.name ypos 380 size 16 xoffset 45

            textbutton "Buy":
                xysize (90, 26)
                xalign 0.89
                xoffset 45
                ypos 374
                text_size 16
                sensitive ((current_category == "Decorations" and tokens >= current_item.price) or (current_item.owned < 99 and game.gold >= current_item.price))
                action Return("buy")

            hbox:
                pos (132, 407)
                xsize 410
                text current_item.desc size 12
