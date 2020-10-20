
init python:
    def shop_sortfilter(item, sortby="Price (Asc)", filtering=None):
        #if filtering == "Locked":
            #item = filter(lambda x: x[1][3] is False, item)

        if sortby == "Price (Asc)":
            item = sorted(item, key=lambda x: x.price, reverse=False)
        elif current_sorting == "Price (Desc)":
            item = sorted(item, key=lambda x: x.price, reverse=True)
        return item

label shop_dress():

    python:
        current_sorting = "Price (Asc)"
        category_items = {"hermione": hermione.outfits, "tonks": tonks.outfits, "cho": cho.outfits, "luna": luna.outfits, "astoria": astoria.outfits, "susan": susan.outfits}
        current_category = "hermione"
        menu_items = shop_sortfilter(filter(lambda x: bool(x.unlocked == False and x.price > 0), category_items.get(current_category, [])), current_sorting)
        current_item = next(iter(menu_items), None)

    if not renpy.android:
        show screen tooltip

    show screen shop_dress_menu()

    label .after_init:

    $ _return = ui.interact()

    python:
        if _return[0] == "category":
            current_category = _return[1]
            menu_items = shop_sortfilter(filter(lambda x: bool(x.unlocked == False and x.price > 0), category_items.get(current_category, [])), current_sorting)
            current_item = next(iter(menu_items), None)
        elif _return[0] == "buy":
            gold -= _return[1].price
            _return[1].unlock()

            menu_items = shop_sortfilter(filter(lambda x: bool(x.unlocked == False and x.price > 0), category_items.get(current_category, [])), current_sorting)
            current_item = next(iter(menu_items), None)
        elif _return == "sort":
            if current_sorting == "Price (Asc)":
                current_sorting = "Price (Desc)"
            elif current_sorting == "Price (Desc)":
                current_sorting = "Price (Asc)"

            menu_items = shop_sortfilter(filter(lambda x: bool(x.unlocked == False and x.price > 0), category_items.get(current_category, [])), current_sorting)
        else:
            renpy.return_statement()

    jump .after_init

screen shop_dress_menu():
    tag shop_menu
    zorder 15
    style_prefix "shop"

    add "gui_fade"

    use invisible_button(action=Return("Close"))
    use close_button

    use shop_dress_menuitem()

    default icon_bg = gui.format("interface/achievements/{}/iconbox.webp")
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel_left.webp")
    default highlight = gui.format("interface/achievements/{}/highlight_left_b.webp")

    window:
        pos (150, 90)
        xysize (207, 454)
        background panel

        use invisible_button()

        vbox:
            pos (6, 6)
            for category in category_items.iterkeys():
                $ icon = Fixed(icon_bg, Frame( Transform("interface/icons/head/{}.webp".format(category), fit="contain"), xysize=(42, 42), offset=(3, 3)), "interface/achievements/glass_iconbox.webp")

                vbox:
                    textbutton category:
                        style "empty"
                        xysize (195, 48)
                        text_align (0.6, 0.5)
                        text_xanchor 0.5
                        text_size 20

                        foreground icon
                        hover_background highlight
                        selected_background highlight
                        selected (current_category == category)
                        action Return(["category", category])

                    add gui.format("interface/frames/{}/spacer_left.webp")

        vbox:
            style_prefix gui.theme('achievements_filters')

            pos (6, 384)
            button action None
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen shop_dress_menuitem():

    tag shop_menuitem
    zorder 16
    style_prefix "shop"

    default icon_size = (72, 144)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (367, 37)
        xysize (560, 501)
        background panel

        use invisible_button()

        if current_item:
            text "[current_item.name]" size 22 xalign 0.5 ypos 65
            frame: # For text wrapping
                pos (10, 110)
                xysize (246+100, 150)
                text "[current_item.desc]" size 12

        vpgrid:
            cols 3
            xspacing 5
            yspacing 10
            draggable True
            mousewheel True
            scrollbars "vertical"
            ysize 308
            pos (8, 192)

            for item in menu_items:
                $ icon = Crop((210, 200, 700, 1000), item.get_image())
                $ is_modded = item.is_modded()
                $ is_affordable = bool(gold >= item.price)

                button:
                    style "shop_outfit_button"
                    xysize icon_size
                    background Transform(icon, xsize=72, ysize=144, fit="contain", anchor=(0.5, 1.0), align=(0.5, 1.0), yoffset=-6)
                    selected (current_item == item)
                    action SetVariable("current_item", item)

                    add icon_frame

                    if is_affordable:
                        text "G [item.price]" xalign 0.5 ypos 10
                    else:
                        text "G {color=#ff0000}[item.price]{/color}" xalign 0.5 ypos 10

                    hbox:
                        offset (5, -5)
                        align (0.0, 1.0)

                        if is_modded:
                            text "M" color "#00b200"

        if current_item:
            add current_item.get_image() zoom 0.4 align (1.0, 1.0) xoffset 25

            textbutton "Buy":
                align (0.5, 0.95)
                sensitive (gold >= current_item.price)
                activate_sound "sounds/money.mp3"
                action Return(["buy", current_item])

style shop_window is empty

style shop_outfit_button is empty:
    foreground None
    hover_foreground "#ffffff80"
    selected_foreground "#ffffff40"
    activate_sound "sounds/click.ogg"

style shop_outfit_button_text is default:
    size 14
