
default wardrobe_music = False
default wardrobe_chitchats = True

# Used as custom order for the sorting
define wardrobe_subcategories_sorted = {
    "hair": 5, "shirts": 5, "skirts": 5, "pantyhose": 5, "slot1": 5, "panties": 5, "save": 5,
    "earrings": 4, "sweaters": 4, "trousers": 4, "stockings": 4, "bikini panties": 4, "load": 4,
    "neckwear": 3, "dresses": 3, "shorts": 3, "socks": 3, "schedule": 3,
    "one-piece suits": 2, "import": 2,
    "robes": 1, "export": 1,
    "gloves": 0, "pubes": 0, "delete": 0,
    "other": -1,
}

define wardrobe_categories = ("head", "piercings & tattoos", "upper body", "upper undergarment", "lower body", "lower undergarment", "legwear", "misc")
define wardrobe_outfit_schedule = ("day", "night", "cloudy", "rainy", "snowy")

label wardrobe():
    python:
        char_active = getattr(store, active_girl)
        char_outfit = getattr(renpy.store, active_girl[:3] + "_outfit_last")
        char_outfit.save()

        wardrobe_subcategories = char_active.wardrobe

        if renpy.android:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule"} } } )
        else:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule", "import", "export"} } } )

        current_category = None
        current_subcategory = None
        current_item = None

    if wardrobe_music:
        call play_music("wardrobe")

    if not renpy.android:
        show screen tooltip

    show screen wardrobe_menu(662, 50)

    label .after_init:

    $ _return = ui.interact()

    python:
        if _return[0] == "category":
            current_category = _return[1]

            category_items = OrderedDict(sorted(wardrobe_subcategories.get(current_category, {}).iteritems(), key=lambda x: wardrobe_subcategories_sorted.get(x[0], 0), reverse=True))
            current_subcategory = category_items.keys()[0] if category_items else ""
            menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory, []))

            if current_category == "outfits":
                _outfit = char_active.create_outfit()
                current_item = next( (x for x in char_active.outfits if _outfit.hash == x.hash), None)
                _outfit.delete()
            else:
                current_item = char_active.get_equipped_item(menu_items)

            char_active.wear("all")
            if current_category in ("lower undergarment", "upper undergarment"):
                char_active.strip("top", "bottom", "robe", "accessory")
            elif current_category == "piercings & tattoos":
                char_active.strip("top", "bottom", "robe", "accessory", "bra", "panties", "stockings", "gloves")
        elif _return[0] == "subcategory":
            current_subcategory = _return[1]

            if current_subcategory == "import":
                menu_items = list_outfit_files()
            else:
                menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))

            if current_category == "outfits":
                _outfit = char_active.create_outfit()
                current_item = next( (x for x in char_active.outfits if _outfit.hash == x.hash), None)
                _outfit.delete()
            else:
                current_item = char_active.get_equipped_item(menu_items)
        elif _return[0] == "equip":
            if isinstance(_return[1], DollCloth):
                if _return[1].type == "hair" and char_active.is_equipped_item(_return[1]):
                    renpy.play("sounds/fail.mp3")
                    renpy.notify("Hair cannot be removed.")
                else:
                    renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])

                # Lipstick Fix - Synchronize image with current mouth after equipping.
                if isinstance(_return[1], DollLipstick):
                    _return[1].rebuild_image()
            elif isinstance(_return[1], DollOutfit):
                _outfit = char_active.create_outfit()

                if _outfit.hash == _return[1].hash:
                    renpy.notify("Load failed: Outfit arleady equipped.")
                    _outfit.delete()
                    renpy.jump("wardrobe.after_init")

                if not _outfit.exists():
                    _confirmed = False
                    renpy.call_screen("confirm", "Discard unsaved changes and load this outfit?", [SetVariable("_confirmed", True), Return()], Return())

                    _outfit.delete()

                    if _confirmed:
                        renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])
                    else:
                        renpy.notify("Load failed: Cancelled by user.")
                else:
                    _outfit.delete()
                    renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])
        elif _return[0] == "setcolor":
            current_item.set_color(_return[1])
        elif _return[0] == "touching":
            renpy.call(active_girl+"_wardrobe_check", "touching", _return[1])
        elif _return[0] == "addoutfit":
            _outfit = char_active.create_outfit()

            if _outfit.exists():
                _outfit.delete()
                renpy.notify("Save failed: Outfit already exists.")
            else:
                if _return[1]:
                    _indx = char_active.outfits.index(_return[1])
                    char_active.outfits.remove(_outfit)
                    renpy.call_screen("confirm", "Overwrite outfit?", [SetDict(char_active.outfits, _indx, _outfit), Return()], [Function(_outfit.delete), Return()])

                menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
                renpy.notify("Saved.")

        elif _return[0] == "deloutfit":
            _return[1].delete()
            menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
            renpy.notify("Deleted.")
        elif _return[0] == "export":
            _return[1].export_data(datetime.datetime.now().strftime("%d %b %Y-%H%M%S"))
            achievement.unlock("export")
        elif _return[0] == "import":
            _outfit = char_active.import_outfit(_return[1])

            if _outfit and _outfit.exists():
                _outfit.delete()
                renpy.notify("Import failed: Outfit already exists.")
        elif _return == "music":
            if wardrobe_music:
                wardrobe_music = False
                renpy.call("play_music", active_girl)
                #renpy.call(char_label, face="annoyed")
            else:
                wardrobe_music = True
                renpy.call("play_music", "wardrobe")
                #renpy.call(char_label, face="happy")
        else: #_return == "Close":
            _confirmed = False
            _outfit = char_active.create_outfit()

            if not _outfit.exists():
                _outfit.delete()
                renpy.notify("Advice: If you want to keep an outfit, save it.")
                renpy.call_screen("confirm", "Exit without saving?\n{size=-6}Unsaved changed will be lost.{/size}", [SetVariable("_confirmed", True), Return()], Return())

                if not _confirmed:
                    renpy.jump("wardrobe.after_init")
                char_active.equip(char_outfit)

            _outfit.delete()
            char_active.wear("all")
            renpy.play('sounds/door2.mp3')
            if wardrobe_music:
                renpy.call("play_music", active_girl)

            renpy.return_statement()

    jump .after_init

screen wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 15
    style_prefix "wardrobe"

    add "gui_fade"

    use invisible_button(action=Return("Close"))
    use close_button

    if current_category == "outfits":
        use wardrobe_outfit_menuitem(20, 50)
    elif current_subcategory != None:
        use wardrobe_menuitem(20, 50)

    default icon_bg = Frame(gui.format("interface/frames/{}/iconmed.webp"), 6, 6)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/wardrobe.webp")

    window:
        pos (xx, yy)
        xysize (344, 507)
        #background panel

        use invisible_button()

        # Main Categories
        grid 2 4:
            ypos 108
            xoffset -36
            xspacing 200 + 72
            yspacing 18

            for i, category in enumerate(wardrobe_categories):
                $ icon = Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                $ icon_xoffset = -18 if (i % 2) == 0 else 18

                button:
                    xysize (72, 72)
                    background icon
                    activate_sound "sounds/scroll.mp3"
                    tooltip category
                    action Return(["category", category])
                    if current_category == category:
                        xoffset icon_xoffset

        hbox:
            $ icon_yoffset = -18

            pos (92, 18)
            spacing 18
            # Outfits Manager
            button:
                xysize (72, 72)
                background Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/outfits.webp", zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                tooltip "Outfits Manager"
                action Return(["category", "outfits"])
                if current_category == "outfits":
                    yoffset icon_yoffset

            # Studio
            if not renpy.android:
                button:
                    xysize (72, 72)
                    background Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/studio.webp", zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                    tooltip "Photo Studio"
                    action Function(renpy.call_in_new_context, "studio", active_girl)

        add panel

        # Character
        add char_active.get_image():
            yoffset -6
            corner1 (184, 218)
            corner2 (924, 1200)
            zoom 0.45
            anchor (0.5, 1.0)
            align (0.5, 1.0)
            events False

        # Easter Egg (Headpats, boobs, pussy)
        button style "empty" xysize (120, 80) xalign 0.525 ypos 60 action Return(["touching", "head"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 238 action Return(["touching", "boobs"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 360 action Return(["touching", "pussy"])

        #use dropdown_menu(name="Toggles", pos=(12, 56)):
            #for item in character_toggles:
                #$ item = item[0]
                #$ is_worn = char_active.is_worn(item)
                #$ is_equipped = char_active.is_equipped(item)
                #textbutton "[item]":
                    #style gui.theme("dropdown")
                    #tooltip "Show/hide "+str(item)
                    #selected is_worn
                    #sensitive is_equipped
                    #action Call(active_girl+"_wardrobe_check", "toggle", item)

        use dropdown_menu(name="Options", pos=(12, 56)):
            textbutton "Music":
                style gui.theme("dropdown")
                tooltip "Toggle music"
                selected wardrobe_music
                action Return("music")
            textbutton "Chit-chats":
                style gui.theme("dropdown")
                tooltip "Toggle character chit-chats"
                action ToggleVariable("wardrobe_chitchats", True, False)
            textbutton "Outfit scheduling":
                style gui.theme("dropdown")
                tooltip "{color=#35aae2}[active_girl]{/color} will automatically wear outfits\nbased on set schedule, time of day and weather."
                action ToggleVariable(active_girl+"_outfits_schedule", True, False)

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
                        action Return(["setcolor", i])
                        add icon_frame
                # Reset Button
                button:
                    xysize (32, 32)
                    background "#d3d3d3"
                    tooltip "Reset all colours"
                    action Function(current_item.reset_color)
                    text "R" align (0.5, 0.5)
                    add icon_frame

        # Subcategory icons
        hbox:
            spacing 5
            pos (8, 108)

            for subcategory in category_items.keys():
                $ icon = "interface/wardrobe/icons/{}.webp".format(subcategory)

                button:
                    xysize icon_size
                    background Transform(icon, xsize=icon_size[0], fit="contain", alpha=0.65)
                    selected_background Transform(icon, xsize=icon_size[0], fit="contain", )
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
                $ is_seen = item.seen
                $ is_equipped = char_active.is_equipped_item(item)
                $ is_inadequate = bool(get_progression(active_girl) < item.level)
                $ is_blacklisted = char_active.is_blacklisted(item.type)
                $ is_blacklister = any(char_active.is_equipped(x) for x in item.blacklist)
                $ is_modded = bool(item.modpath)
                $ is_multislot = item.is_multislot()
                $ warnings = []

                if is_blacklisted or is_blacklister:
                    $ blacklisted = [x for x in item.blacklist if char_active.is_equipped(x)] # Offender (List currently blacklisted clothing types by this item)
                    $ blacklister = char_active.get_blacklister(item.type) # Victim (List clothing types blacklisting this item )
                    $ warnings.append("Incompatible with:{size=-4}\n" + "\n".join(set(blacklisted + blacklister)) + "{/size}")

                if is_inadequate:
                    $ warnings.append("Character level too low")

                if is_modded:
                    $ warnings.append("Item belongs to a mod:\n{size=-4}{color=#35aae2}" + item.get_modname() + "{/color}{/size}")

                if is_multislot:
                    $ slot = str(int(item.type[-1])+1)
                    $ warnings.append("Occupies " + item.type[:-1] + " slot number " + slot)

                button:
                    xysize icon_size
                    background Transform(icon, xsize=icon_size[0], fit="contain", anchor=(0.5, 0.5), align=(0.5, 0.5))
                    action Return(["equip", item])
                    tooltip ("\n".join(warnings))
                    if is_inadequate:
                        foreground "#b2000040"
                        hover_foreground "#CD5C5C40"
                    if not is_seen:
                        unhovered Function(item.mark_as_seen)

                    add icon_frame

                    hbox:
                        offset (5, 5)

                        if is_modded:
                            text "M" color "#00b200"

                        if is_blacklisted or is_blacklister:
                            text "!" color "#b20000"

                    # Bottom-Right
                    if is_equipped:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5) zoom 0.8

                    # Bottom-Right
                    if not is_seen:
                        text "NEW" style "wardrobe_item_caption" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5)

                    # Bottom-Left
                    if is_multislot:
                        text "[slot]" style "wardrobe_item_caption" anchor (0.0, 1.0) align (0.0, 1.0) offset (5, -5)

screen wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16
    style_prefix "wardrobe"

    default icon_size = (72, 144)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (xx, yy)
        xysize (560, 454)
        background panel

        use invisible_button()

        text "[current_category]" size 22 xalign 0.5 ypos 65

        # Subcategory icons
        hbox:
            spacing 5
            pos (8, 108)

            for subcategory in category_items.keys():
                $ icon = "interface/wardrobe/icons/{}.webp".format(subcategory)

                button:
                    xysize (72, 72)
                    background Transform(icon, alpha=0.65, xsize=72, fit="contain")
                    selected_background Transform(icon, xsize=72, fit="contain")
                    selected (subcategory == current_subcategory)
                    tooltip subcategory
                    action Return(["subcategory", subcategory])

        # Item icons
        vpgrid:
            cols 7
            xspacing 5
            yspacing 10
            draggable True
            mousewheel True
            scrollbars "vertical"
            pos (8, 192)
            ysize 308

            for item in menu_items:
                if current_subcategory == "import":
                    $ icon = "/outfits/{}".format(item)
                    $ is_modded = False
                    $ is_equipped = False
                else:
                    $ icon = Crop((210, 200, 700, 1000), item.get_image())
                    $ is_modded = item.is_modded()
                    $ is_equipped = bool(current_item == item)

                $ warnings = []

                if is_modded:
                    $ warnings.append("Item belongs to a mod:\n{size=-4}{color=#35aae2}"+ item.get_modname() + "{/color}{/size}")

                if current_subcategory == "delete":
                    $ action = Return(["deloutfit", item])
                elif current_subcategory == "load":
                    $ action = Return(["equip", item])
                elif current_subcategory == "save":
                    $ action = Return(["addoutfit", item])
                elif current_subcategory == "import":
                    $ action = Return(["import", item])
                elif current_subcategory == "export":
                    $ action = Return(["export", item])
                elif current_subcategory == "schedule":
                    $ action = None

                button:
                    xysize icon_size
                    background Transform(icon, xsize=72, ysize=144, fit="contain", anchor=(0.5, 1.0), align=(0.5, 1.0), yoffset=-6)
                    tooltip ("\n".join(warnings))
                    action action

                    add icon_frame

                    hbox:
                        offset (5, 5)

                        if is_modded:
                            text "M" color "#00b200"

                    if current_subcategory == "schedule" and getattr(renpy.store, active_girl+"_outfits_schedule"):
                        vbox:
                            spacing 5
                            for x in wardrobe_outfit_schedule:
                                $ _ico = "interface/wardrobe/icons/outfits/{}.webp".format(x)
                                $ _on = item.schedule[x]
                                $ _yesno = "yes" if _on else "no"

                                if x in ("Day", "Night"):
                                    $ _tooltip = "Worn during the "+x+":\n{size=-4}"+_yesno+"{/size}"
                                else:
                                    $ _tooltip = "Worn during "+x+" weather:\n{size=-4}"+_yesno+"{/size}"

                                button:
                                    xysize (25, 25)
                                    background image_alpha(gray_tint(_ico))
                                    hover_background white_tint(_ico)
                                    selected_background _ico
                                    tooltip _tooltip
                                    action ToggleDict(item.schedule, x, True, False)

                    if is_equipped:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5) zoom 0.8

            # Add empty slot
            $ slot = len(menu_items)+1
            if current_subcategory == "save":
                textbutton "Save\n{size=-5}Slot [slot]{/size}":
                    xysize icon_size
                    idle_background "#00000033"
                    text_align (0.5, 0.5)
                    action Return(["addoutfit", None])

style wardrobe_window is empty

style wardrobe_button is empty:
    foreground None
    hover_foreground "#ffffff80"
    activate_sound "sounds/click.ogg"

style wardrobe_button_text:
    color "#fff"
    size 20
    outlines [ (1, "#000", 0, 0) ]

style wardrobe_item_caption:
    color "#fff"
    size 14
    outlines [ (1, "#000", 0, 0) ]
