init python:
    def upgrades_sortfilter(item, sortby=False):
        return item

default upgrades_show_locked = False
default upgrades_show_complete = True
default item_bought = False # TEMP var - Used as a return value out of context.

default her_upgrade_school2 = DollOutfit([her_hair_base, her_top_school2, her_bottom_school2, her_panties_base1, her_bra_base1, her_stockings_base1])

default her_upgrade_school3 = DollOutfit([her_hair_base, her_top_school3, her_bottom_school3, her_panties_base1, her_bra_base1, her_stockings_base1])

default her_upgrade_school4 = DollOutfit([her_hair_base, her_top_school4, her_bottom_school4, her_panties_base1, her_bra_base1, her_stockings_base1])

###

default her2_upgrade_school2 = DollOutfit([her_hair_base, her_top_school2, her_bottom_school2, her_panties_base1, her_bra_base1, her_stockings_base1])

default her2_upgrade_school3 = DollOutfit([her_hair_base, her_top_school3, her_bottom_school3, her_panties_base1, her_bra_base1, her_stockings_base1])

default her2_upgrade_school4 = DollOutfit([her_hair_base, her_top_school4, her_bottom_school4, her_panties_base1, her_bra_base1, her_stockings_base1])

###

default her3_upgrade_school2 = DollOutfit([her_hair_base, her_top_school2, her_bottom_school2, her_panties_base1, her_bra_base1, her_stockings_base1])

default her3_upgrade_school3 = DollOutfit([her_hair_base, her_top_school3, her_bottom_school3, her_panties_base1, her_bra_base1, her_stockings_base1])

default her3_upgrade_school4 = DollOutfit([her_hair_base, her_top_school4, her_bottom_school4, her_panties_base1, her_bra_base1, her_stockings_base1])

label upgrades:
    python:
        her_upgrade_school2.price = 50
        her_upgrade_school3.price = 75
        her_upgrade_school4.price = 100
        #
        her2_upgrade_school2.price = 15
        her2_upgrade_school3.price = 30
        her2_upgrade_school4.price = 45
        #
        her3_upgrade_school2.price = 100
        her3_upgrade_school3.price = 100
        her3_upgrade_school4.price = 100

    $ gui.in_context("upgrades_menu")
    return item_bought

label upgrades_menu(xx=150, yy=90):

    $ upgrades_dict = {
                    "Tonks": {"ico": "tonks", "flag": tonks_unlocked, "outfits": {"school": []}},
                    "Hermione": {"ico": "hermione", "flag": hermione_unlocked, "outfits": {"school": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other": [her_outfit_default, her2_upgrade_school2, her2_upgrade_school3, her2_upgrade_school4], "other2": [her_outfit_default, her3_upgrade_school2, her3_upgrade_school3, her3_upgrade_school4], "other3": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4]}},
                    "Cho": {"ico": "cho", "flag": cho_unlocked, "outfits": {"school": []}},
                    "Luna": {"ico": "luna", "flag": luna_unlocked, "outfits": {"school": []}},
                    "Astoria": {"ico": "astoria", "flag": astoria_unlocked, "outfits": {"school": []}},
                    "Susan": {"ico": "susan", "flag": susan_unlocked, "outfits": {"school": []}}
                    }

    $ upgrades_categories_sorted = ["Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"]
    $ upgrades_categories_sorted_length = len(upgrades_categories_sorted)

    $ current_category = last_character.capitalize() if last_character else upgrades_categories_sorted[0]
    $ current_item = 0
    $ current_subcategory = "overview"
    $ current_sorting = upgrades_show_locked

    $ category_items = []
    $ menu_items = category_items
    $ menu_items_length = len(menu_items)

    $ item_bought = False

    if not renpy.android:
        show screen mouse_tooltip

    show screen upgrades_menu(xx, yy)
    show screen upgrades_menuitem(xx, yy)
    with d3

    label .after_init:
    $ _return = ui.interact()

    if _return[0] == "category":
        $ current_category = _return[1]
        $ category_items = 0
        $ menu_items = upgrades_sortfilter([], current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_item = 0
    elif _return[0] == "subcat":
        if _return[1] != current_subcategory:
            $ current_subcategory = _return[1]
    elif _return[0] == "buy":
        if gold >= _return[1] and ton_friendship >= _return[3]*25:
            python:
                renpy.play('sounds/money.mp3')

                gold -= _return[1]
                _list = _return[2]
                _iter = _return[3]

                item_bought = True

                for i in xrange(1, min(_iter+1, len(_list))):
                    if not _list[i].unlocked:
                        _list[i].unlock()
                        ton_clothing_upgrades += 1
        elif ton_friendship < _return[4]:
            $ renpy.play('sounds/fail.mp3')
            "> Tonks doesn't like you enough."
        else:
            $ renpy.play('sounds/fail.mp3')
            "> You don't have enough gold."
    else:
        hide screen upgrades_menu
        hide screen upgrades_menuitem
        return

    jump .after_init

screen upgrades_menu(xx, yy):
    tag upgrades_menu
    zorder 30
    modal True

    default bg = At(screenshot_image, gaussianblur(15.0))
    add bg

    use close_button
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "Show locked:":
                    style gui.theme("overlay_button")
                    xsize 195 ysize 32
                    text_align (0.4, 0.5)
                    text_size 12
                    action ToggleVariable("upgrades_show_locked", True, False)
                add gui.format("interface/frames/{}/check_")+str(upgrades_show_locked).lower()+".webp" xalign 0.8 ypos 4
        vbox:
            pos (6, 6)
            for category in upgrades_categories_sorted:
                if upgrades_dict[category]["flag"]:
                    frame:
                        style "empty"
                        xysize (195, 50)
                        vbox:
                            textbutton category:
                                style "empty"
                                xysize (195, 48)
                                text_align (0.6, 0.5)
                                text_xanchor 0.5
                                text_size 20
                                if current_category == category:
                                    background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                else:
                                    hover_background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                    action Return(["category", category])

                            add gui.format("interface/achievements/{}/spacer_left.webp")
                        add gui.format("interface/achievements/{}/iconbox.webp") yoffset 1
                        $ image_zoom = crop_image_zoom("interface/icons/head/"+upgrades_dict.get(category).get("ico")+".webp", 42, 42)

                        frame:
                            style "empty"
                            xsize 42
                            ysize 42
                            add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                        add "interface/achievements/glass_iconbox.webp" pos (3, 3)

screen upgrades_menuitem(xx, yy):
    tag upgrades_menuitem
    zorder 30

    frame:
        style "empty"
        style_prefix gui.theme()
        pos (xx+217, yy-53)
        xysize (560, 507)

        add gui.format("interface/achievements/{}/panel.webp")

        text "Outfit Upgrades" size 22 xalign 0.5 ypos 65

        hbox:
            spacing 5
            pos (18, 70)
            add "interface/icons/small/gold.webp"
            text str(gold) size 15 ypos 4
            add "interface/icons/small/tonks.webp"
            text str(ton_friendship) size 15 ypos 4


        vpgrid:
            cols 1
            xysize (548, 400)
            pos (6, 101)
            draggable True
            mousewheel "change"
            scrollbars "vertical"
            xfill True
            yfill True

            # TODO: Reduce the clutter and optimize the code.
            for i in upgrades_dict[current_category]["outfits"].itervalues():
                $ linear_price = 0

                if len(i) > 0 and (i[0].unlocked or upgrades_show_locked):
                    vbox:
                        hbox:
                            spacing 0
                            for x in xrange(len(i)):
                                if x < len(i)-1:
                                    if not i[x+1].unlocked:
                                        $ linear_price += i[x+1].price
                                    $ actual_price = linear_price-i[x+1].price
                                    $ favor_req = (x)*25
                                elif x == len(i)-1:
                                    $ actual_price = linear_price
                                    $ favor_req = 75
                                frame:
                                    style "empty"
                                    xysize (95, 130)
                                    xpos 10
                                    if x < len(i):
                                        add Flatten(i[x].get_image()) align (1.0, 1.0) zoom 0.125 alpha (1.0 if ((gold >= actual_price and ton_friendship >= favor_req) or i[x].unlocked) else 0.5)
                                        if i[x].unlocked:
                                            add "interface/topbar/icon_check.webp" zoom 0.75 align (0.85, 1.0)
                                        else:
                                            button:
                                                style gui.theme("overlay_button")
                                                xysize (76, 130)
                                                action Return(["buy", actual_price, i, x, favor_req])
                                if x < len(i)-1:
                                    frame:
                                        style "empty"
                                        xysize (50, 50)
                                        yalign 0.5
                                        text ("" if (linear_price <= 0) else str(favor_req+25)+"{unicode}\u2764{/unicode}") color ("#b20000" if (ton_friendship < favor_req+25) else "#402313") size 14 align (0.5, 0.25)
                                        text (str(linear_price)+"g" if linear_price > 0 else "Sold!") color ("#b20000" if (0 < linear_price > gold) else "#402313") size 14 align (0.5, 0.7)
                                        text "{unicode}\u0362{/unicode}" size 65 align (1.0, 0.5) xoffset 5
                        add gui.format("interface/achievements/{}/spacer.webp") yalign 1.0 xpos 274 xanchor 0.5
