init python:
    from collections import OrderedDict

default wardrobe_background_day = "#e8c97e"
default wardrobe_background_night = "#7d756e"

default wardrobe_toggles = False
default wardrobe_music = False
default wardrobe_chitchats = True

# Used as custom order for the sorting
define wardrobe_subcategories_sorted = {
    "hair": 5, "shirts": 5, "skirts": 5, "pantyhose": 5, "slot1": 5,
    "earrings": 4, "sweaters": 4, "trousers": 4, "stockings": 4, "slot2": 4,
    "neckwear": 3, "dresses": 3, "shorts": 3, "socks": 3, "slot3": 3,
    "other": -1, "slot4": 2, "one-piece suits": 2,
    "slot5": 1, "robes": 1,
    "gloves": 0,
}

label wardrobe(char_label):
    python:
        # TODO: Streamline and unify whoring variables.
        _char_var_list = {
            "hermione": (her_whoring, her_requirements["change_underwear"]),
            "tonks": (ton_friendship, ton_requirements["change_underwear"]),
            "astoria": (ast_whoring, ast_requirements["change_underwear"]),
            "cho": (cho_whoring, cho_requirements["change_underwear"]),
            "luna": (lun_whoring, lun_requirements["change_underwear"]),
            "susan": (sus_whoring, sus_requirements["change_underwear"])
            }

        char_active = getattr(store, active_girl)
        char_nickname = char_active.name
        char_scale = 0.5
        char_level = _char_var_list[active_girl][0]
        char_underwear_allowed = char_level >= _char_var_list[active_girl][1]

        renpy.start_predict("interface/wardrobe/gold/*.webp")
        renpy.start_predict("interface/wardrobe/gray/*.webp")
        renpy.start_predict("interface/wardrobe/icons/*.webp")

        wardrobe_background = wardrobe_background_night if gui.is_dark() else wardrobe_background_day

        current_page = 0
        current_category = ""
        current_subcategory = ""
        current_item = None
        wardrobe_categories = ("head", "makeup", "upper body", "upper undergarment", "lower body", "lower undergarment", "legwear", "misc")
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
        show screen tooltip

    show screen wardrobe_menu(650, 50)
    with d2


    label .after_init:

    show screen wardrobe_menu(650, 50)

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
                $ wardrobe_categories = ("face", "makeup", "torso", "breasts", "hips", "pelvis", "legs", "misc")
                $ char_active.strip("all")
                $ char_active.strip("accessory")

            else:
                $ wardrobe_categories = ("head", "makeup", "tops", "bras", "bottoms", "panties", "legwear", "misc")
                $ char_active.wear("all")
                $ char_active.wear("accessory")
            hide screen wardrobe_menuitem
    elif _return == "studio":
        $ renpy.play('sounds/click3.mp3')
        $ renpy.call_in_new_context("studio", active_girl)
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
                $ last_outfit = char_active.create_outfit()
                $ char_active.equip(_return[1])
                $ item_to_export = _return[1]
                $ renpy.call_in_new_context("studio", active_girl)
                $ char_active.equip(last_outfit)
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
                            if char_active.is_worn(item.type) and char_active.get_equipped(item.type) == item:
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
    style_prefix "wardrobe"

    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/wardrobe.webp")

    add "gui_fade"

    use invisible_button(action=Return("Close"))
    use close_button

    window:
        pos (xx, yy)
        xysize (344, 507)
        background panel

        use invisible_button()

        # Main Categories
        grid 2 4:
            ypos 72
            xoffset -36
            xspacing 200 + 72
            yspacing 18

            for i, category in enumerate(wardrobe_categories):
                $ icon = Fixed(Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                $ icon_zoom = 0.5
                $ icon_offset = -18 if (i % 2) == 0 else 18

                button:
                    xysize (72, 72)
                    background icon
                    tooltip category
                    action Return(["category", category])
                    if current_category == category:
                        xoffset icon_offset

        # Character
        add char_active.get_image():
            yoffset -6
            corner1 (238, 200)
            corner2 (872, 1200)
            zoom 0.45
            anchor (0.5, 1.0)
            align (0.5, 1.0)
            events False

        # Switch to body modifications tab
        add gui.format("interface/frames/{}/circle.webp") pos (373, 62)
        button:
            style "empty"
            pos (373, 62)
            xysize (50, 50)
            background "interface/wardrobe/switch.webp"
            hover_background image_hover("interface/wardrobe/switch.webp")
            tooltip "Switch tabs"
            action Return("tabswitch")

        # Outfits Manager
        add gui.format("interface/frames/{}/circle.webp") pos (373, 117)
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
            add gui.format("interface/frames/{}/circle.webp") pos (373, 172)
            button:
                style "empty"
                pos (373, 172)
                xysize (50, 50)
                background "interface/wardrobe/studio.webp"
                hover_background image_hover("interface/wardrobe/studio.webp")
                tooltip "Open Studio"
                action Return("studio")

        # Easter Egg (Headpats, boobs, pussy)
        button style "empty" xysize (120, 80) xalign 0.525 ypos 60 action Return(["erozone", "head"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 238 action Return(["erozone", "boobs"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 360 action Return(["erozone", "pussy"])

        # Clothing Toggles
        use dropdown_menu(name="Toggles", pos=(116, 29), items_offset=(-5, 2)):
            for item in character_toggles:
                $ _item = item[0]
                $ _is_worn = char_active.is_worn(_item)
                $ _is_equipped = char_active.is_equipped(_item)
                $ _bool = _is_worn if _is_equipped else None
                textbutton "[_item]":
                    style gui.theme("dropdown")
                    tooltip "Show/hide "+str(_item)
                    selected _is_worn
                    sensitive _is_equipped
                    action Return(["toggle", _item])

        # Wardrobe Settings
        use dropdown_menu(name="Options", pos=(350, 29), items_offset=(-59, 2)):
            textbutton "Music":
                style gui.theme("dropdown")
                tooltip "Toggle music"
                selected wardrobe_music
                action Return("music")
            textbutton "Chit-chats":
                style gui.theme("dropdown")
                tooltip "Toggle character chit-chats"
                action ToggleVariable("wardrobe_chitchats", True, False)

screen wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16
    style_prefix "wardrobe"

    default icon_size = (72, 72)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (xx, yy)
        xysize (560, 454)
        background panel

        use invisible_button()

        text "[current_category]" size 22 xalign 0.5 ypos 65

        # Colours
        if current_item:
            hbox:
                spacing 2
                xanchor 1.0
                pos (552, 61)

                for i in xrange(current_item.layers):
                    button:
                        xysize (32, 32)
                        background Fixed(Frame("interface/color_picker/checker.webp", tile=True), Color(tuple(current_item.color[i])))
                        tooltip "Change colour ("+str(i+1)+")"
                        action Return(["item_color", i])
                        add icon_frame
                # Reset Button
                button:
                    xysize (32, 32)
                    background "#d3d3d3"
                    tooltip "Reset all colours"
                    action Return("item_reset")
                    text "R" align (0.5, 0.5)
                    add icon_frame

        # Subcategory icons
        hbox:
            spacing 5
            pos (8, 108)

            for subcategory in category_items.keys():
                $ icon = "interface/wardrobe/icons/{}.webp".format(subcategory)
                $ icon_zoom = get_zoom(icon, icon_size)

                button:
                    xysize icon_size
                    background Transform(icon, zoom=icon_zoom, alpha=0.65)
                    selected_background Transform(icon, zoom=icon_zoom)
                    selected (subcategory == current_subcategory)
                    tooltip subcategory
                    action Return(["subcategory", subcategory])

        # Item icons
        vpgrid:
            cols 7
            spacing 5
            draggable True
            mousewheel True
            scrollbars "vertical"
            pos (8, 192)
            ysize 308

            for item in menu_items:
                $ icon = item.get_icon()
                $ icon_zoom = get_zoom(icon, (icon_size))
                $ is_equipped = bool(char_active.get_equipped(item.type) == item)
                $ is_modded = bool(item.modpath)
                $ is_blacklisted = char_active.is_blacklisted(item.type)
                $ is_allowed = bool(get_progression(active_girl) >= item.level)
                $ has_blacklist = bool(item.blacklist)
                $ is_multislot = any(x in item.type for x in ("makeup", "accessory", "piercing", "tattoo"))

                button:
                    xysize icon_size
                    background Transform(icon, zoom=icon_zoom, anchor=(0.5, 0.5), align=(0.5, 0.5))
                    action Return(["equip", item])
                    if not is_allowed:
                        foreground "#b2000040"
                        tooltip "Character level too low."

                    add icon_frame

                    if is_equipped:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-6, -6) zoom 0.8
                    if is_multislot:
                        $ slot = str(int(item.type[-1])+1)
                        textbutton slot:
                            anchor (0.0, 1.0)
                            align (0.0, 1.0)
                            tooltip "Occupies slot number [slot]."
                            offset (6, -6)

                    hbox:
                        if is_modded:
                            textbutton "{color=#00b200}M{/color}":
                                tooltip "This item belongs to a mod:\n{size=-4}{color=#35aae2}"+ item.get_modname() + "{/color}{/size}"
                                action NullAction()
                        if has_blacklist:
                            textbutton "{color=#b20000}!{/color}":
                                tooltip "Incompatible with:\n{color=#35aae2}" + "\n".join(str(k) for k in item.blacklist) + "{/color}\n{size=-4}{color=#e4cb35}Above items will be unequipped.{/color}{/size}"
                                action NullAction()
                        if is_blacklisted:
                            textbutton "{color=#b20000}X{/color}":
                                tooltip "Incompatible with your current setup."
                                action NullAction()
style wardrobe_window is empty

style wardrobe_button is empty:
    foreground None
    hover_foreground "#ffffff80"

style wardrobe_button_text:
    color "#fff"
    size 20
    outlines [ (1, "#000", 0, 0) ]

screen wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16

    # Navigational Buttons Up/Down
    if menu_items_length > 9:
        if not current_page <= 0:
            imagebutton:
                pos (xx+480, yy+190)
                idle gui.format("interface/general/{}/button_arrow_up.webp")
                hover gui.format("interface/general/{}/button_arrow_up_hover.webp")
                action Return("dec")
        if current_page < math.ceil((menu_items_length)/10):
            imagebutton:
                pos (xx+480, yy+245)
                idle gui.format("interface/general/{}/button_arrow_down.webp")
                hover gui.format("interface/general/{}/button_arrow_down_hover.webp")
                action Return("inc")

    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background

        use invisible_button()

        add gui.format("interface/frames/{}/item_rectangle.webp")

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
                style gui.theme("overlay_button")
                pos (10+90*i, 86)
                xysize (86, 86)
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
                            style gui.theme("overlay_button")
                            tooltip "Equip Outfit"
                            action Return(["equip", menu_items[i]])
                    elif current_subcategory == "Export&Import":
                        button:
                            style gui.theme("overlay_button")
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
                    style gui.theme("overlay_button")
                    xysize (83, 177)
                    pos (12+90*col, 179+184*row)
                    idle_background "#00000033"
                    text_align (0.5, 0.5)
                    action Return("addoutfit")
            elif current_subcategory == "Export&Import":
                textbutton "Import\n{size=-5}Slot [n]{/size}":
                    style gui.theme("overlay_button")
                    xysize (83, 177)
                    pos (12+90*col, 179+184*row)
                    idle_background "#00000033"
                    text_align (0.5, 0.5)
                    action Return("import")
            else:
                button style "empty" xysize (83, 177) pos (12+90*col, 179+184*row) background "#00000033"

        # Schedule Toggle
        if current_subcategory == "Schedule":
            textbutton "Outfit scheduling":
                style gui.theme("dropdown")
                pos (290, 42)
                background gui.format("interface/frames/{}/check_")+str(globals()[active_girl+"_outfits_schedule"])+".webp"
                tooltip "{color=#35aae2}[active_girl]{/color} will automatically wear outfits\nbased on set schedule, time of day and weather."
                action Return("toggle_schedule")

            if not globals()[active_girl+"_outfits_schedule"]:
                textbutton "Disabled":
                    style gui.theme("menu")
                    pos (10, 178)
                    xysize (447, 360)
                    background "#00000080"
                    text_align (0.5, 0.5)
                    text_size 24
                    action NullAction()
