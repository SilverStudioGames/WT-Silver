init python:
    from collections import OrderedDict

default wardrobe_background_day = "#e8c97e"
default wardrobe_background_night = "#7d756e"

default wardrobe_toggles = False
default wardrobe_music = False
default wardrobe_chitchats = True
default wardrobe_requirements = False

# Used as custom order for the sorting
define wardrobe_subcategories_sorted = {
    "hair": 5, "shirts": 5, "skirts": 5, "pantyhose": 5, "robes": 5, "slot1": 5,
    "earrings": 4, "sweaters": 4, "trousers": 4, "stockings": 4, "slot2": 4,
    "neckwear": 3, "dresses": 3, "shorts": 3, "socks": 3, "slot3": 3,
    "other": -1, "slot4": 2,
    "slot5": 1,
}

label wardrobe(char_label):
    python:
        # TODO: Streamline and unify whoring variables.
        _char_var_list = {
            "hermione": (her_whoring, her_requirements["change_underwear"]),
            "tonks": (ton_friendship, ton_requirements["change_underwear"]),
            "astoria": (ast_whoring, ast_requirements["change_underwear"]),
            "cho": (cho_whoring, cho_requirements["change_underwear"])
            }

        char_active = getattr(store, active_girl)
        char_nickname = char_active.name
        char_scale = 0.5
        char_level = _char_var_list[active_girl][0]
        char_underwear_allowed = char_level >= _char_var_list[active_girl][1]

        renpy.start_predict("interface/wardrobe/gold/*.webp")
        renpy.start_predict("interface/wardrobe/gray/*.webp")
        renpy.start_predict("interface/wardrobe/icons/*.webp")

        wardrobe_background = wardrobe_background_day if interface_color == "gold" else wardrobe_background_night

        items_shown = 20
        current_page = 0
        current_category = ""
        current_subcategory = ""
        current_item = None
        wardrobe_categories = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
        wardrobe_subcategories = char_active.wardrobe
        export_in_progress = False
        item_to_export = None
        wardrobe_outfit_schedule = ("Day", "Night", "Cloudy", "Rainy", "Snowy")

        character_toggles = [(k, v[1]) for k, v in char_active.clothes.iteritems() if k != "hair" and not any(i.isdigit() for i in k)]
        character_toggles.extend([("tattoo", 30), ("piercing", 31), ("makeup", 32), ("accessory", 33)])
        character_toggles.sort(key=lambda x: x[1], reverse=True)

        renpy.hide_screen(active_girl+"_main")

    if wardrobe_music:
        call play_music("wardrobe")

    if not renpy.android:
        show screen mouse_tooltip

    show screen wardrobe_menu(550, 50)
    with d2


    label .after_init:

    show screen wardrobe_menu(550, 50)

    if current_category:
        if current_category == "outfits":
            show screen wardrobe_outfit_menuitem(20, 50)
        else:
            show screen wardrobe_menuitem(20, 50)

    $ _return = ui.interact()

    if _return == "tabswitch":
        $ renpy.call(active_girl+"_wardrobe_check", _return)
        if _return in (None, True):
            $ current_page = 0
            $ current_category = ""
            $ current_subcategory = ""
            $ current_item = None
            $ renpy.play('sounds/click3.mp3')
            if "head" in wardrobe_categories:
                $ wardrobe_categories = ("face", "torso", "hips", "legs", "makeup", "breasts", "pelvis", "misc")
                $ char_active.strip("all")
                $ char_active.strip("accessory")

            else:
                $ wardrobe_categories = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
                $ char_active.wear("all")
                $ char_active.wear("accessory")
            hide screen wardrobe_menuitem
    elif _return == "studio":
        $ renpy.play('sounds/click3.mp3')
        $ renpy.call_in_new_context("studio", char_label)
    elif _return[0] == "equip":
        # Lipstick Fix - Synchronize image with current mouth after equipping.
        if isinstance(_return[1], DollLipstick):
            $ _return[1].rebuild_image()

        if isinstance(_return[1], DollCloth) and char_active.is_blacklisted(_return[1].type):
            $ renpy.play('sounds/fail.mp3')
        else:
            $ renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])
    elif _return == "addoutfit":
        $ _outfit = char_active.create_outfit()
        if not _outfit.validate():
            $ _outfit.delete()
            $ renpy.notify("This outfit has already been saved!")

        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
        $ menu_items_length = len(menu_items)
    elif _return[0] == "deloutfit":
        $ _return[1].delete()
        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
        $ menu_items_length = len(menu_items)
    elif _return[0] == "tagoutfit":
        $ _return[1].schedule[_return[2]] = not _return[1].schedule[_return[2]]
    elif _return[0] == "export":
        menu:
            "-Export to PNG file-" if not renpy.android:
                $ export_in_progress = True
                $ getattr(renpy.store, active_girl[:3]+"_outfit_last").save()
                $ char_active.equip(_return[1])
                $ item_to_export = _return[1]
                $ renpy.call_in_new_context("studio", char_label)
            "-Export to clipboard-":
                $ _return[1].export_data(False)
            "-Back-":
                pass
        $ achievement.unlock("export")
    elif _return == "import":
        menu:
            "-Import from PNG file-" if not renpy.android:
                #call file_explorer # Unfinished

                $ txt_filename = "exported"
                $ txt_filename = renpy.input("Filename", txt_filename, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#&_- ", length=64)
                $ getattr(renpy.store, active_girl[:3]+"_outfit_last").import_data(True, txt_filename)
            "-Import from clipboard-":
                $ getattr(renpy.store, active_girl[:3]+"_outfit_last").import_data(False)
            "-Back-":
                pass
        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
        $ menu_items_length = len(menu_items)
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        hide screen wardrobe_menuitem
        $ current_item.set_color(active_layer)
        $ active_layer = None
    elif _return == "item_reset":
        $ current_item.reset_color()
    elif _return == "bg_color":
        $ active_layer = None
        hide screen wardrobe_menuitem
        $ wardrobe_background = color_picker(get_rgb_list(wardrobe_background), False, "Wardrobe Background Color", pos_xy=[40, 85])
        $ wardrobe_background = get_hex_string(wardrobe_background[0]/255.0, wardrobe_background[1]/255.0, wardrobe_background[2]/255.0, wardrobe_background[3]/255.0)
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return[0] == "category":
        $ current_page = 0
        if current_category == _return[1]:
            $ renpy.play('sounds/door2.mp3')
            $ current_category = ""
            $ current_subcategory = ""
            if "head" in wardrobe_categories:
                $ char_active.wear("all")
            hide screen wardrobe_menuitem
            hide screen wardrobe_outfit_menuitem
        else:
            $ renpy.call(active_girl+"_wardrobe_check", "category", _return)

            if _return[1] != None:
                $ renpy.play('sounds/scroll.mp3')
                $ current_category = _return[1]
                # Outfits
                if current_category == "outfits":
                    $ category_items = ["Load", "Save", "Delete", "Export&Import", "Schedule"]
                    $ current_subcategory = category_items[0]
                    $ current_item = None
                    $ char_active.wear("all")
                    $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
                    $ menu_items_length = len(menu_items)
                else:
                    if current_category in ("bras", "panties"):
                        $ char_active.strip("top", "bottom", "robe", "accessory")
                    else:
                        if 'head' in wardrobe_categories:
                            $ char_active.wear("top", "bottom", "robe", "accessory")

                    $ category_items = OrderedDict(sorted(wardrobe_subcategories.get(current_category, {}).iteritems(), key=lambda x: wardrobe_subcategories_sorted.get(x[0], 0), reverse=True))

                    # Default subcategory
                    if category_items:
                        $ current_subcategory = category_items.keys()[0]
                        $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
                    else:
                        $ category_items = []
                        $ current_subcategory = "No items available"
                        $ menu_items = []
                    $ menu_items_length = len(menu_items)
                    # Default selected item
                    $ current_item = None
                    python:
                        for item in menu_items:
                            if char_active.clothes[item.type][0] and item.id == char_active.clothes[item.type][0].id:
                                current_item = item
                                break
    elif _return[0] == "subcategory":
        if current_subcategory != _return[1]:
            $ renpy.play('sounds/scroll.mp3')
            $ current_subcategory = _return[1]
            if current_category != "outfits":
                $ current_page = 0
                $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if char_active.clothes[item.type][0] and item.id == char_active.clothes[item.type][0].id:
                            current_item = item
                            break
    elif _return[0] == "erozone":
        $ renpy.call(active_girl+"_wardrobe_check", "touching", _return[1])
    elif _return[0] == "toggle":
        $ renpy.call(active_girl+"_wardrobe_check", "toggle", _return[1])
    elif _return == "toggle_schedule":
        $ globals()[active_girl+"_outfits_schedule"] = not globals()[active_girl+"_outfits_schedule"]
    elif _return == "music":
        if wardrobe_music:
            $ wardrobe_music = False
            call play_music(active_girl)
            call expression char_label pass (text="", face="annoyed")
        else:
            $ wardrobe_music = True
            call play_music("wardrobe")
            call expression char_label pass (text="", face="happy")
    else: #_return == "Close":
        $ renpy.play('sounds/door2.mp3')
        $ char_active.wear("all")
        #$ char_active.clothes_compatible()
        if wardrobe_music:
            call play_music(active_girl)
        $ renpy.stop_predict("interface/wardrobe/gold/*.webp")
        $ renpy.stop_predict("interface/wardrobe/gray/*.webp")
        $ renpy.stop_predict("interface/wardrobe/icons/*.webp")
        return
    jump .after_init

screen wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 15

    add im.Blur(screenshot_image, 2)

    use invisible_button(action=Return("Close"))
    use close_button

    frame:
        style "empty"
        pos (xx, yy)
        xysize (540, 548)

        use invisible_button()

        # Main Categories
        for i, category in enumerate(wardrobe_categories):
            $ cat_row = (i // 4) % 2
            $ cat_col = i % 4
            if current_category == category:
                add "interface/wardrobe/{}/frame.webp".format(interface_color) xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category) xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                button:
                    style "empty"
                    pos (14+411*cat_row, 80+110*cat_col)
                    xysize (90, 96)
                    hover_background btn_hover
                    action Return(["category", category])
            else:
                add "interface/wardrobe/{}/frame.webp".format(interface_color) xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                # Underwear disabled check
                if category in ("bras", "panties") and not char_underwear_allowed:
                    add gray_tint("interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category)) xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                else:
                    add "interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category) xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                button:
                    style "empty"
                    pos (61+377*cat_row, 80+110*cat_col)
                    xysize (44, 96)
                    hover_background btn_hover
                    tooltip category
                    action Return(["category", wardrobe_categories[i]])

        # Background
        frame xysize (340, 548) xpos 100 style "empty" background wardrobe_background

        # Character
        add char_active.get_image() yoffset -12 corner1 (238, 200) corner2 (872, 1200) zoom 0.5 align (0.5, 1.0) events False

        # Switch to body modifications tab
        add "interface/frames/{}/circle.webp".format(interface_color) pos (373, 62)
        button:
            style "empty"
            pos (373, 62)
            xysize (50, 50)
            background "interface/wardrobe/switch.webp"
            hover_background image_hover("interface/wardrobe/switch.webp")
            tooltip "Switch tabs"
            action Return("tabswitch")

        # Outfits Manager
        add "interface/frames/{}/circle.webp".format(interface_color) pos (373, 117)
        button:
            style "empty"
            pos (373, 117)
            xysize (50, 50)
            background "interface/wardrobe/outfits.webp"
            hover_background image_hover("interface/wardrobe/outfits.webp")
            tooltip "Outfits Manager"
            action Return(["category", "outfits"])

        # Studio
        if not renpy.android:
            add "interface/frames/{}/circle.webp".format(interface_color) pos (373, 172)
            button:
                style "empty"
                pos (373, 172)
                xysize (50, 50)
                background "interface/wardrobe/studio.webp"
                hover_background image_hover("interface/wardrobe/studio.webp")
                tooltip "Open Studio"
                action Return("studio")

        add "interface/panels/{}/wardrobe_panel.webp".format(interface_color)

        #Easter Egg (Headpats, boobs, pussy)
        button style "empty" xysize (120, 80) xalign 0.525 ypos 60 action Return(["erozone", "head"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 238 action Return(["erozone", "boobs"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 360 action Return(["erozone", "pussy"])

        # Toggles and User Settings
        use dropdown_menu(name="Toggles", pos=(116, 29), items_offset=(-5, 2)):
            for item in character_toggles:
                $ _item = item[0]
                $ _is_worn = char_active.is_worn(_item)
                $ _is_equipped = char_active.is_equipped(_item)
                $ _bool = _is_worn if _is_equipped else None
                textbutton "[_item]":
                    style interface_style+"_dropdown"
                    background "interface/frames/{}/check_{}.webp".format(interface_color, _bool)
                    tooltip "Show/hide "+str(_item)
                    action [SensitiveIf(_is_equipped), Return(["toggle", _item])]
        use dropdown_menu(name="Options", pos=(350, 29), items_offset=(-59, 2)):
            textbutton "Music":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.webp".format(interface_color, wardrobe_music)
                tooltip "Toggle music"
                action Return("music")
            textbutton "Background":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_true.webp".format(interface_color)
                tooltip "Change background colour"
                action Return("bg_color")
            textbutton "Chit-chats":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.webp".format(interface_color, wardrobe_chitchats)
                tooltip "Toggle character chit-chats"
                action ToggleVariable("wardrobe_chitchats", True, False)
            textbutton "Requirements":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.webp".format(interface_color, wardrobe_requirements)
                tooltip "Toggle level requirements display"
                action ToggleVariable("wardrobe_requirements", True, False)

        # Zoom slider
        # bar:
            # area (25, 290, 255, 30)
            # value VariableValue("char_scale", range=1.0, step=0.01, style=u'bar')
            # top_gutter 0
            # bottom_gutter 0

        add "interface/general/{}/button_wide.webp".format(interface_color) pos (200, -4)
        text char_nickname xalign 0.5 ypos 4 size 16

screen wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16

    # Navigational Buttons Up/Down
    if menu_items_length > items_shown:
        imagebutton:
            pos (xx+480, yy+190)
            idle "interface/general/{}/button_arrow_up.webp".format(interface_color)
            if not current_page <= 0:
                hover "interface/general/{}/button_arrow_up_hover.webp".format(interface_color)
                action Return("dec")

        imagebutton:
            pos (xx+480, yy+245)
            idle "interface/general/{}/button_arrow_down.webp".format(interface_color)
            if current_page < math.ceil((menu_items_length-1)/items_shown):
                hover "interface/general/{}/button_arrow_down_hover.webp".format(interface_color)
                action Return("inc")

    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background

        use invisible_button()

        add "interface/panels/{}/icon_panel.webp".format(interface_color)

        hbox:
            pos (24, 44)
            spacing 3
            text "[current_category]:" size 18
            text "[current_subcategory]" size 12 yalign 0.5

        # Page Counter
        if menu_items_length > items_shown:
            textbutton str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown)+1)):
                style "empty"
                ysize 32
                pos (270, 37)
                xanchor 1.0
                background "interface/page.webp"
                text_yalign 0.5
                text_first_indent 26
                action NullAction()

        # Colours
        if current_item:
            hbox:
                pos (283, 31)
                spacing 2

                for i in xrange(current_item.layers):
                    button:
                        xysize (32, 44)
                        background Color(tuple(current_item.color[i]))
                        tooltip "Change colour ("+str(i+1)+")"
                        action Return(["item_color", i])
            # Reset Button
            textbutton "R":
                pos (422, 31)
                xysize (32, 44)
                background "#d3d3d3"
                tooltip "Reset all colours"
                action Return("item_reset")

        # Add subcategory list and sort them based on custom order
        if len(category_items) > 0:
            for i, subcategory in enumerate(category_items.keys()):
                if current_subcategory == subcategory:
                    add "interface/wardrobe/icons/{}.webp".format(subcategory) ypos 95 xpos 19+(90*i) zoom 0.8
                else:
                    add image_alpha("interface/wardrobe/icons/{}.webp".format(subcategory), 0.65) ypos 95 xpos 19+(90*i) zoom 0.8
                button:
                    style "empty"
                    pos (10+90*i, 86)
                    xysize (86, 86)
                    hover_background btn_hover
                    tooltip subcategory
                    action Return(["subcategory", subcategory])

        # Add Clothing Items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 5) % 4
                $ col = i % 5
                $ image_zoom = get_zoom(menu_items[i].get_icon(), 83, 85)
                frame:
                    style "empty"
                    pos (12+90*col, 180+92*row)
                    xysize (83, 85)

                    add menu_items[i].get_icon() zoom image_zoom xalign 0.5 yalign 0.5 events False
                if char_active.clothes[menu_items[i].type][0] and menu_items[i].id == char_active.clothes[menu_items[i].type][0].id:
                    button:
                        style "empty"
                        pos (12+90*col, 180+92*row)
                        xysize (83, 85)
                        hover_background btn_hover
                        tooltip "Take off"
                        action Return(["equip", menu_items[i]])

                    add "interface/topbar/icon_check.webp" pos (60+90*col, 225+90*row)
                else:
                    button:
                        style "empty"
                        pos (12+90*col, 180+92*row)
                        xysize (83, 85)
                        hover_background btn_hover
                        # tooltip "Put on"
                        action Return(["equip", menu_items[i]])

                # Whoring req
                if wardrobe_requirements:
                    if menu_items[i].level > get_progression(active_girl):
                        textbutton str(menu_items[i].level):
                            style "empty"
                            pos (15+90*col, 180+92*row)
                            text_size 20
                            text_outlines [ (1, "#000", 0, 0) ]
                            text_color "#b20000"
                            tooltip ("{color=#35aae2}[active_girl]'s{/color} level is too low to wear that." if not active_girl.endswith("s") else "{color=#35aae2}[active_girl]'{/color} level is too low to wear that.")
                            action NullAction()
                # Check current item compatibility, if fails forbid equipping
                if char_active.is_blacklisted(menu_items[i].type):
                    textbutton "{color=#b20000}X{/color}":
                        pos (64+90*col, 180+92*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with your current setup."
                        action NullAction()
                elif menu_items[i].blacklist != None:
                    textbutton "{color=#b20000}!{/color}":
                        pos (64+90*col, 180+92*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with:\n{color=#35aae2}"+"\n".join(str(k) for k in menu_items[i].blacklist)+"{/color}\n{size=-4}{color=#e4cb35}Above items will be unequipped.{/color}{/size}"
                        action NullAction()
                if menu_items[i].modpath:
                    textbutton "{color=#00b200}M{/color}":
                        style "empty"
                        pos (15+90*col, 240+92*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "This item belongs to a mod:\n{size=-4}{color=#35aae2}"+menu_items[i].get_modname()+"{/color}{/size}"
                        action NullAction()

        # Add empty items
        for i in xrange(menu_items_length-(items_shown*current_page), items_shown):
            $ row = (i // 5) % 4
            $ col = i % 5
            button style "empty" pos (12+90*col, 179+92*row) xysize (83, 85) background "#00000033"

screen wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16

    # Navigational Buttons Up/Down
    if menu_items_length > 9:
        if not current_page <= 0:
            imagebutton:
                pos (xx+480, yy+190)
                idle "interface/general/"+interface_color+"/button_arrow_up.webp"
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.webp"
                action Return("dec")
        if current_page < math.ceil((menu_items_length)/10):
            imagebutton:
                pos (xx+480, yy+245)
                idle "interface/general/"+interface_color+"/button_arrow_down.webp"
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.webp"
                action Return("inc")

    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background

        use invisible_button()

        add "interface/panels/"+interface_color+"/icon_panel2.webp"

        hbox:
            pos (24, 44)
            spacing 3
            text "[current_category]:" size 18
            text "[current_subcategory]" size 12 yalign 0.5

        # Page Counter
        if menu_items_length > 9:
            textbutton str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/10))+1):
                style "empty"
                ysize 32
                pos (270, 37)
                xanchor 1.0
                background "interface/page.webp"
                text_yalign 0.5
                text_first_indent 26
                action NullAction()

        # Add subcategory list
        for i, subcategory in enumerate(category_items):
            if current_subcategory == subcategory:
                add "interface/wardrobe/icons/outfits/"+subcategory+".webp" ypos 95 xpos 19+(90*i) zoom 0.8
            else:
                add image_alpha("interface/wardrobe/icons/outfits/"+subcategory+".webp") ypos 95 xpos 19+(90*i) zoom 0.8
            button:
                style "empty"
                pos (10+90*i, 86)
                xysize (86, 86)
                hover_background btn_hover
                tooltip subcategory
                action Return(["subcategory", subcategory])

        # Add Outfit Items
        for i in xrange(current_page*10, (current_page*10)+10):
            if i < menu_items_length:
                $ row = (i // 5) % 2
                $ col = i % 5

                # Preview Icon
                frame:
                    style "empty"
                    xysize (83, 177)
                    pos (12+90*col, 179+184*row)
                    add menu_items[i].get_image() corner1 (270, 0) corner2 (840, 1200) maxsize (83, 177) yalign 1.0 events False

                # Button Icons
                    if current_subcategory == "Delete":
                        button:
                            style "empty"
                            hover_background "#cc330040"
                            tooltip "Delete Outfit"
                            action Return(["deloutfit", menu_items[i]])
                    elif current_subcategory == "Load":
                        button:
                            style "empty"
                            hover_background btn_hover
                            tooltip "Equip Outfit"
                            action Return(["equip", menu_items[i]])
                    elif current_subcategory == "Export&Import":
                        button:
                            style "empty"
                            hover_background btn_hover
                            tooltip "Export Outfit"
                            action Return(["export", menu_items[i]])
                    elif current_subcategory == "Schedule":
                        frame:
                            style "empty"
                            background "#000000B3"
                            padding (5, 5)
                            vbox:
                                spacing 5
                                for x in wardrobe_outfit_schedule:
                                    $ _ico = "interface/wardrobe/icons/outfits/"+x.lower()+".webp"
                                    $ _on = menu_items[i].schedule[x.lower()]
                                    $ _yesno = "yes" if _on else "no"

                                    if x in ("Day", "Night"):
                                        $ _tooltip = "Worn during the "+x+":\n{size=-4}"+_yesno+"{/size}"
                                    elif x in ("Rainy", "Cloudy", "Snowy"):
                                        $ _tooltip = "Worn during "+x+" weather:\n{size=-4}"+_yesno+"{/size}"

                                    button:
                                        style "empty"
                                        xysize (25, 25)
                                        background image_alpha(gray_tint(_ico))
                                        hover_background white_tint(_ico)
                                        selected_background _ico
                                        tooltip _tooltip
                                        action [SelectedIf(_on), Return(["tagoutfit", menu_items[i], x.lower()])]

                    if menu_items[i].is_modded():
                        textbutton "{color=#00b200}M{/color}":
                            style "empty"
                            pos (3, 155)
                            background None
                            text_size 20
                            text_outlines [ (1, "#000", 0, 0) ]
                            tooltip "This outfit contains modded items:\n{size=-4}{color=#35aae2}"+"\n".join(menu_items[i].get_modname())+"{/color}{/size}"
                            action NullAction()

        # Add empty items
        for i in xrange(menu_items_length, (current_page*10)+10):
            $ row = (i // 5) % 2
            $ col = i % 5
            $ n = i+1
            if current_subcategory == "Save":
                textbutton "Save\n{size=-5}Slot [n]{/size}":
                    style interface_style+"_menu"
                    xysize (83, 177)
                    pos (12+90*col, 179+184*row)
                    background "#00000033"
                    hover_background btn_hover
                    text_align (0.5, 0.5)
                    action Return("addoutfit")
            elif current_subcategory == "Export&Import":
                textbutton "Import\n{size=-5}Slot [n]{/size}":
                    style interface_style+"_menu"
                    xysize (83, 177)
                    pos (12+90*col, 179+184*row)
                    background "#00000033"
                    hover_background btn_hover
                    text_align (0.5, 0.5)
                    action Return("import")
            else:
                button style "empty" xysize (83, 177) pos (12+90*col, 179+184*row) background "#00000033"

        # Schedule Toggle
        if current_subcategory == "Schedule":
            textbutton "Outfit scheduling":
                style interface_style+"_dropdown"
                pos (290, 42)
                background "interface/frames/"+str(interface_color)+"/check_"+str(globals()[active_girl+"_outfits_schedule"])+".webp"
                tooltip "{color=#35aae2}[active_girl]{/color} will automatically wear outfits\nbased on set schedule, time of day and weather."
                action Return("toggle_schedule")

            if not globals()[active_girl+"_outfits_schedule"]:
                textbutton "Disabled":
                    style interface_style+"_menu"
                    pos (10, 178)
                    xysize (447, 360)
                    background "#00000080"
                    text_align (0.5, 0.5)
                    text_size 24
                    action NullAction()
