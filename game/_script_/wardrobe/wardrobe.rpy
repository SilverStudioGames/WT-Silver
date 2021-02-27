
default wardrobe_music = False
default wardrobe_chitchats = True
default wardrobe_autosave = False

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

label wardrobe:
    $ gui.in_context("wardrobe_menu")
    return

screen wardrobe(xx, yy):
    tag wardrobe
    zorder 30
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button

    fixed:
        # TODO: Wardrobe doesn't work well with the gui animation
        # if settings.get("animations"):
        #     at gui_animation

        use wardrobe_menu(xx, yy)
        if current_category == "outfits":
            use wardrobe_outfit_menuitem(20, 50)
        elif current_subcategory != None:
            use wardrobe_menuitem(20, 50)

label wardrobe_menu():
    python:
        char_active = get_character_object(active_girl)
        char_outfit = get_character_outfit(active_girl, type="last")
        char_outfit.save()

        wardrobe_subcategories = char_active.wardrobe

        if renpy.android:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule"} } } )
        else:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule", "import", "export"} } } )

        # Defaults
        current_category = "head"
        category_items = OrderedDict(sorted(wardrobe_subcategories.get(current_category, {}).iteritems(), key=lambda x: wardrobe_subcategories_sorted.get(x[0], 0), reverse=True))
        current_subcategory = category_items.keys()[0] if category_items else ""
        menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory, []))
        current_item = char_active.get_equipped_item(menu_items)

    if wardrobe_music:
        call play_music("wardrobe")

    if not renpy.android:
        show screen tooltip

    show screen wardrobe(662, 50)

    label .after_init:

    $ _choice = ui.interact()

    if _choice[0] == "category":

        if wardrobe_check_category(_choice[1]):
            $ current_category = _choice[1]

            $ category_items = OrderedDict(sorted(wardrobe_subcategories.get(current_category, {}).iteritems(), key=lambda x: wardrobe_subcategories_sorted.get(x[0], 0), reverse=True))
            $ current_subcategory = category_items.keys()[0] if category_items else ""
            $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory, []))

            if current_category == "outfits":
                $ _outfit = char_active.create_outfit(temp=True)
                $ current_item = next( (x for x in char_active.outfits if _outfit == x), None)
            else:
                $ current_item = char_active.get_equipped_item(menu_items)

            $ char_active.wear("all")
            if current_category in ("lower undergarment", "upper undergarment"):
                $ char_active.strip("top", "bottom", "robe", "accessory")
            elif current_category == "piercings & tattoos":
                $ char_active.strip("top", "bottom", "robe", "accessory", "bra", "panties", "stockings", "gloves")
        else:
            $ wardrobe_react("category_fail", _choice[1])

    elif _choice[0] == "subcategory":
        $ current_subcategory = _choice[1]

        if current_subcategory == "import":
            $ menu_items = list_outfit_files()
        else:
            $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))

        if current_category == "outfits":
            $ _outfit = char_active.create_outfit(temp=True)
            $ current_item = next( (x for x in char_active.outfits if _outfit == x), None)
        else:
            $ current_item = char_active.get_equipped_item(menu_items)

    elif _choice[0] == "equip":
        ### CLOTHING ###
        if isinstance(_choice[1], DollCloth):
            if _choice[1].type == "hair" and char_active.is_equipped_item(_choice[1]):
                $ renpy.play("sounds/fail.mp3")
                $ renpy.notify("Hair cannot be removed.")
            else:
                if char_active.is_equipped_item(_choice[1]):
                    # UNEQUIP
                    if wardrobe_check_unequip(_choice[1]):
                        $ wardrobe_react("unequip", _choice[1])
                        $ char_active.unequip(_choice[1].type)
                        $ current_item = None
                    else:
                        $ wardrobe_react("unequip_fail", _choice[1])
                else:
                    # EQUIP
                    if wardrobe_check_equip(_choice[1]):
                        $ wardrobe_react("equip", _choice[1])

                        # Blacklist handling
                        if not wardrobe_check_blacklist(_choice[1]):
                            $ wardrobe_react("blacklist", _choice[1])

                        $ char_active.equip(_choice[1])
                        $ current_item = _choice[1]

                        # Lipstick Fix - Synchronize image with the current mouth after equipping.
                        if isinstance(_choice[1], DollLipstick):
                            $ _choice[1].rebuild_image()
                    else:
                        $ wardrobe_react("equip_fail", _choice[1])

        ### OUTFIT ###
        elif isinstance(_choice[1], DollOutfit):
            $ _outfit = char_active.create_outfit(temp=True)

            if _outfit == _choice[1]:
                $ renpy.notify("Load failed: Outfit already equipped.")
            else:
                if wardrobe_check_equip_outfit(_choice[1]):

                    if not _outfit.exists():
                        $ _confirmed = renpy.call_screen("confirm", "Discard unsaved changes and load this outfit?")

                        if _confirmed:
                            $ wardrobe_react("equip_outfit", _choice[1])
                            $ char_active.equip(_choice[1])
                            $ current_item = _choice[1]
                        else:
                            $ renpy.notify("Load failed: Cancelled by user.")
                    else:
                        $ wardrobe_react("equip_outfit", _choice[1])
                        $ char_active.equip(_choice[1])
                        $ current_item = _choice[1]
                else:
                    $ wardrobe_react("equip_outfit_fail", _choice[1])

    elif _choice[0] == "setcolor":
        $ current_item.set_color(_choice[1])

    elif _choice[0] == "touch":
        if wardrobe_check_touch(_choice[1]):
            $ wardrobe_react("touch", _choice[1])
        else:
            $ wardrobe_react("touch_fail", _choice[1])

    elif _choice[0] == "addoutfit":
        $ _outfit = char_active.create_outfit(temp=True)

        if _outfit.exists():
            $ renpy.notify("Save failed: Outfit already exists.")
        else:
            if _choice[1]:
                $ _index = char_active.outfits.index(_choice[1])
                $ _confirmed = renpy.call_screen("confirm", "Discard unsaved changes and load this outfit?")

                if _confirmed:
                    $ _outfit = char_active.create_outfit()
                    $ _outfit.delete() # Removes it from list only
                    $ char_active.outfits[_index] = _outfit
                    $ renpy.notify("Overwritten.")
                else:
                    $ renpy.notify("Save failed: Cancelled by user.")

            else:
                $ char_active.create_outfit()
                $ renpy.notify("Outfit Saved.")

        $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
        $ current_item = next( (x for x in char_active.outfits if _outfit == x), None)

    elif _choice[0] == "deloutfit":
        $ _confirmed = renpy.call_screen("confirm", "Delete this outfit?")

        if _confirmed:
            $ _choice[1].delete()
            $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
            $ renpy.notify("Outfit Deleted.")

    elif _choice[0] == "export":
        $ _choice[1].export_data(datetime.datetime.now().strftime("%d %b %Y-%H%M%S"))
        $ achievement.unlock("export")

    elif _choice[0] == "import":
        $ _outfit = char_active.import_outfit(_choice[1])

    elif _choice[0] == "schedule":
        $ renpy.call_screen("wardrobe_schedule_menuitem", _choice[1])

    elif _choice == "music":
        if wardrobe_music:
            $ wardrobe_music = False
            $ renpy.call("play_music", active_girl)
            $ renpy.call(get_character_label(active_girl), face="annoyed")
        else:
            $ wardrobe_music = True
            $ renpy.call("play_music", "wardrobe")
            $ renpy.call(get_character_label(active_girl), face="happy")

    else: #_choice == "Close":
        $ _confirmed = False

        if wardrobe_autosave:
            $ _outfit = char_active.create_outfit()
        else:
            $ _outfit = char_active.create_outfit(temp=True)

            if not _outfit.exists():
                $ renpy.notify("Advice: If you want to keep an outfit, save it.")
                $ _confirmed = renpy.call_screen("confirm", "Exit without saving?\n{size=-6}Unsaved changes will be lost.{/size}")

                if not _confirmed:
                    jump .after_init
                $ char_active.equip(char_outfit)

        hide screen wardrobe
        $ char_active.wear("all")
        $ renpy.play('sounds/door2.mp3')
        if wardrobe_music:
            $ renpy.call("play_music", active_girl)
        $ enable_game_menu()
        return

    jump .after_init

screen wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 15
    style_prefix "wardrobe"

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
                if wardrobe_check_category(category):
                    $ icon = Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                else:
                    $ icon = Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5), matrixcolor=SaturationMatrix(0.0)), icon_frame)
                $ icon_xoffset = -18 if (i % 2) == 0 else 18

                button:
                    xysize (72, 72)
                    background icon
                    activate_sound "sounds/scroll.mp3"
                    tooltip category
                    action Return(["category", category])
                    if current_category == category:
                        xoffset icon_xoffset

        # Outfits and Studio
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

        # Character image cut to the size of the wardrobe
        add char_active.get_image():
            yoffset -6
            corner1 (184, 218)
            corner2 (924, 1200)
            zoom 0.45
            anchor (0.5, 1.0)
            align (0.5, 1.0)
            events False

        # Easter Egg (Headpats, boobs, pussy)
        button style "empty" xysize (120, 80) xalign 0.525 ypos 60 action Return(["touch", "head"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 238 action Return(["touch", "breasts"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 360 action Return(["touch", "vagina"])

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
            textbutton "Autosave Outfits":
                style gui.theme("dropdown")
                tooltip "Toggle auto-saving feature for Outfits"
                action ToggleVariable("wardrobe_autosave", True, False)

screen wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 16
    style_prefix "wardrobe"

    default icon_size = (72, 72)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default icon_transparent = Frame("interface/color_picker/checker.webp", tile=True)
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
                        background Fixed(icon_transparent, Color(tuple(current_item.color[i])))
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
                $ is_inadequate = bool(get_character_progression(active_girl) < item.level)
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

                        if config.developer:
                            text "\nReq. {}".format(item.level) size 10 color "#00ffff" outlines [(1, "#000000", 1, 1)]

                    # Bottom-Right
                    if is_equipped:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5) zoom 0.5

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

            # Add empty slot
            if current_subcategory == "save":
                textbutton "Save":
                    xysize icon_size
                    idle_background "#00000033"
                    text_align (0.5, 0.5)
                    action Return(["addoutfit", None])

            for item in reversed(menu_items):
                if current_subcategory == "import":
                    $ icon = "/outfits/{}".format(item)
                    $ is_modded = False
                    $ is_equipped = False
                else:
                    $ icon = Crop((210, 200, 700, 1000), item.get_image())
                    $ is_modded = item.is_modded()
                    $ is_equipped = bool(current_item == item)
                $ is_inadequate = (current_subcategory in {"save", "load"} and not wardrobe_check_equip_outfit(item))

                $ warnings = []

                if is_modded:
                    $ warnings.append("Outfit contains items from these mods:\n{size=-4}{color=#35aae2}"+ "\n".join(item.get_modname()) + "{/color}{/size}")

                $ alternate = None
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
                    $ action = Return(["schedule", item])
                    $ alternate = Return(["schedule", item])

                button:
                    xysize icon_size
                    background Transform(icon, xsize=72, ysize=144, fit="contain", anchor=(0.5, 1.0), align=(0.5, 1.0), yoffset=-6)
                    tooltip ("\n".join(warnings))
                    action action
                    alternate alternate
                    if is_inadequate:
                        foreground "#b2000040"
                        hover_foreground "#CD5C5C40"
                        selected_foreground "#CD5C5C40"

                    add icon_frame

                    hbox:
                        offset (5, 5)

                        if is_modded:
                            text "M" color "#00b200"

                    if not current_subcategory in {"import", "export"} and getattr(renpy.store, active_girl+"_outfits_schedule"):
                        vbox:
                            pos (6, 6)
                            spacing 1
                            for i in wardrobe_outfit_schedule:
                                if item.schedule[i]:
                                    add Transform("interface/wardrobe/icons/outfits/{}.webp".format(i), size=(16, 16))

                    if is_equipped:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5) zoom 0.5

screen wardrobe_schedule_menuitem(item):
    tag dropdown
    zorder 31
    modal True

    default mpos = renpy.get_mouse_pos()

    use invisible_button(action=Return(), alternate=Show("wardrobe_schedule_menuitem", item=item))

    window:
        style "empty"
        pos mpos
        use invisible_button(action=NullAction(), alternate=Return())

        frame:
            style "empty"
            background "#00000080"
            padding (5, 5, 5, 5)

            vbox:
                spacing 0
                for i in wardrobe_outfit_schedule:
                    $ boolean = "" if item.schedule[i] else "Not "
                    $ caption = "{}worn during the {}".format(boolean, i) if i in ("day", "night") else "{}worn in {} weather".format(boolean, i)
                    textbutton i:
                        style gui.theme("dropdown")
                        tooltip caption
                        action ToggleDict(item.schedule, i, True, False)

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
