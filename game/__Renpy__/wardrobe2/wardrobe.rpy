default wardrobe_event = False
label t_wardrobe(return_label, char_label):
    $ char_active = get_character_object(active_girl)
    $ char_nickname = char_active.char
    $ hide_transitions = True
    
    # Styling
    if daytime:
        $ btn_hover = "#e3ba7140"
    else:
        $ btn_hover = "#7d75aa40"
        
    default bg_color_wardrobe = "#7d756e"
    
    $ items_shown = 20
    $ current_page = 0
    $ current_category = ""
    $ current_subcategory = ""
    $ current_item = None
    $ wardrobe_categories_sorted = ["head", "tops", "bottoms", "misc", "event", "underwear", "outfits", "studio"]
    $ wardrobe_categories = char_active.clothing_dictlist
    
    python:
        character_clothing = []
        for key, value in char_active.clothing.iteritems():
            if key != 'hair':
                character_clothing.append([key, value])
        character_clothing.sort(key=lambda x: x[1][1], reverse=True)
    
    if wardrobe_music_active and not wardrobe_event:
        call play_music("my_immortal")
    
    label t_wardrobe_after_init:
    
    show screen t_wardrobe_menu(550, 50)
    
    if current_category:
        if current_category == "outfits":
            show screen t_wardrobe_outfit_menuitem(20, 50)
        else:
            show screen t_wardrobe_menuitem(20, 50)
    
    $ _return = ui.interact()
    
    hide screen t_wardrobe_menu
    hide screen t_wardrobe_menuitem
    hide screen t_wardrobe_outfit_menuitem
    
    $ ui_hint = ""
    
    if _return[0] == "equip":
        $ renpy.play('sounds/equip.ogg')
        $ current_item = _return[1]
        $ char_active.equip(current_item)
    elif _return == "addoutfit":
        $ cho_outfit_custom.clone()
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "deloutfit":
        $ char_active.outfits.pop(_return[1])
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "export":
        menu:
            "Export to TXT file":
                $ txt_filename = "exported"
                $ txt_filename = renpy.input("Filename", txt_filename, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#& ", length=64)
                $ _return[1].outfit_export(True, txt_filename)
            "Export to clipboard":
                $ _return[1].outfit_export(False)
            "Back":
                pass
        $ achievement.unlock("export")
    elif _return == "import":
        menu:
            "Import from TXT file":
                $ txt_filename = "exported"
                $ txt_filename = renpy.input("Filename", txt_filename, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#& ", length=64)
                $ cho_outfit_custom.outfit_import(True, txt_filename)
            "Import from clipboard":
                $ cho_outfit_custom.outfit_import(False)
            "Back":
                pass
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        show screen t_wardrobe_menu(550, 50)
        $ char_active.cache_override = True
        $ current_item.set_color(active_layer)
        $ char_active.cache_override = False
        $ active_layer = None
        $ char_active.cached = False
    elif _return == "item_reset":
        $ current_item.reset_color()
        $ char_active.cached = False
    elif _return == "bg_color":
        show screen t_wardrobe_menu(550, 50)
        $ bg_color_wardrobe = color_picker(get_rgb_tuple(bg_color_wardrobe), False, "Wardrobe Background Color", pos_xy=[20, 130])
        $ bg_color_wardrobe = get_hex_string(bg_color_wardrobe[0]/255.0, bg_color_wardrobe[1]/255.0, bg_color_wardrobe[2]/255.0, bg_color_wardrobe[3]/255.0)
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return[0] == "category":
        # check if its event time
        if wardrobe_event:
            if not _return[1] == "event":
                $ renpy.play('sounds/locked.ogg')
                show screen popup_window("Not available.")
                jump t_wardrobe_after_init
        else:
            if _return[1] == "event":
                $ renpy.play('sounds/locked.ogg')
                show screen popup_window("Not available.")
                jump t_wardrobe_after_init
        #
        $ current_page = 0
        if current_category == _return[1]:
            $ renpy.play('sounds/door2.mp3')
            $ current_category = ""
            $ current_subcategory = ""
            $ char_active.wear("all")
        else:
            $ renpy.play('sounds/scroll.mp3')
            $ current_category = _return[1]
            # Outfits
            if current_category == "outfits":
                $ category_items = ["Load", "Save", "Delete", "Export&Import"]
                $ current_subcategory = category_items[0]
                $ current_item = None
                $ char_active.wear("all")
                $ menu_items = char_active.outfits
                $ menu_items_length = len(menu_items)
            elif current_category == "studio":
                call expression 'studio' pass (studio_return=return_label, studio_char=char_label)
            else:
                if current_category == "underwear":
                    $ char_active.strip("top")
                    $ char_active.strip("bottom")
                    $ char_active.strip("robe")
                else:
                    $ char_active.wear("top")
                    $ char_active.wear("bottom")
                    $ char_active.wear("robe")
                $ category_items = wardrobe_categories.get(current_category)
                # Default subcategory
                if category_items:
                    $ current_subcategory = category_items.keys()[0]
                    $ menu_items = category_items.get(current_subcategory)
                else:
                    $ category_items = []
                    $ current_subcategory = "No items available"
                    $ menu_items = []
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if item.id == char_active.get_equipped(current_category, current_subcategory):
                            current_item = item
                            break
    elif _return[0] == "subcategory":
        if current_subcategory != _return[1]:
            $ renpy.play('sounds/scroll.mp3')
            $ current_subcategory = _return[1]
            if current_category != "outfits":
                $ current_page = 0
                $ menu_items = category_items.get(current_subcategory)
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if item.id == char_active.get_equipped(current_category, current_subcategory):
                            current_item = item
                            break
    elif _return == "erozone":
        call expression char_label pass (text="", face="horny")
    elif _return == "music":
        if wardrobe_music_active:
            $ wardrobe_music_active = False
            call music_block
            call expression char_label pass (text="", face="annoyed")
        else:
            $ wardrobe_music_active = True
            call play_music("my_immortal")
            call expression char_label pass (text="", face="happy")
    else: #_return == "Close":
        $ renpy.play('sounds/door2.mp3')
        $ hide_transitions = False
        $ char_active.wear("all")
        if wardrobe_music_active and not wardrobe_event:
            call music_block
        python:
            renpy.jump(return_label)
    jump t_wardrobe_after_init
        
screen t_wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 4

    python:
        if current_item and color_preview and not active_layer == None:
            current_item.color[active_layer] = color_preview
    
    use top_bar_close_button
    
    frame:
        xpos xx
        ypos yy
        xsize 540
        ysize 548
        style "empty"
        
        for i, category in enumerate(wardrobe_categories_sorted):
            $ cat_row = (i // 4) % 2
            $ cat_col = i % 4
            if current_category == category:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/test/"+char_active.char+"_"+category+".png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                button xpos 14+411*cat_row ypos 80+110*cat_col xsize 90 ysize 96 style "empty" hover_background btn_hover action Return(["category", category])
            else:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                if not wardrobe_event and category == "event":
                    add grayTint("interface/wardrobe/test/"+char_active.char+"_"+category+".png") xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                elif wardrobe_event and category != "event":
                    add grayTint("interface/wardrobe/test/"+char_active.char+"_"+category+".png") xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                else:
                    add "interface/wardrobe/test/"+char_active.char+"_"+category+".png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                button xpos 61+377*cat_row ypos 80+110*cat_col xsize 44 ysize 96 style "empty" hover_background btn_hover action Return(["category", wardrobe_categories_sorted[i]]) hovered SetVariable("ui_hint", category) unhovered SetVariable("ui_hint", "")
        
        frame xsize 340 ysize 548 xpos 100 style "empty" background bg_color_wardrobe
        
        #add "interface/wardrobe/test/"+str(interface_color)+"/icons_"+char_active.char+"_"+current_category+".png" xpos 13 ypos 80 zoom 0.5

        add "interface/panels/"+interface_color+"/wardrobe_panel.png"

        if not wardrobe_event:
            hbox:
                xpos 120
                ypos 60
                spacing 158
                vbox:
                    spacing 2
                    for item in character_clothing:
                        $ curr_item = item[0]
                        textbutton "{size=12}[curr_item]{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(char_active.get_worn(curr_item))+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Function(char_active.toggle_wear, curr_item)
                vbox:
                    ypos 416
                    textbutton "{size=12}Music{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(wardrobe_music_active)+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("music")
                    textbutton "{size=12}BG Color{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_true.png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("bg_color")
                
        # Tooltip
        if persistent.ui_hint:
            text "[ui_hint]" xalign 0.5 ypos 33
            
        #Erogenous zones
        vbox:
            xalign 0.5
            ypos 260
            spacing 72
            button xsize 120 ysize 60 style "empty" action Return("erozone")
            button xsize 120 ysize 50 style "empty" action Return("erozone")
                
        add "interface/general/"+str(interface_color)+"/button_wide.png" xpos 200 ypos -4
        text char_nickname xalign 0.5 ypos 4 size 16
        
screen t_wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Buttons
    if menu_items_length > items_shown:
        # Up Button
        imagebutton:
            xpos xx+480
            ypos yy+190
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            if not current_page <= 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")

        # Down Button
        imagebutton:
            xpos xx+480
            ypos yy+245
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            if current_page < math.ceil((menu_items_length-1)/items_shown):
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        xpos xx
        ypos yy
        xsize 467
        ysize 548
        style "empty"
        background bg_color_wardrobe
   
        add "interface/panels/"+interface_color+"/icon_panel_1.png"
        
        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                xpos 270
                spacing 5
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown)+1)) ypos 44 size 16
        
        if current_item and not wardrobe_event:
            hbox:
                xpos 300
                ypos 40
                spacing 4
                
                for i in xrange(current_item.layers):
                    button xsize 24 ysize 24 background current_item.get_color_hex(i) action Return(["item_color", i])
                textbutton "R" xsize 24 ysize 24 background "#d3d3d3" action Return("item_reset")
            
        # Add subcategory list
        if len(category_items) > 0:
            for i, subcategory in enumerate(category_items.keys()):
                add "interface/wardrobe/test/icons/"+char_active.char+"/"+current_category+"_"+subcategory+".png" ypos 88 xpos 10+(90*i) zoom 0.2
                button xsize 86 ysize 86 ypos 88 xpos 10+(90*i) style "empty" hover_background btn_hover action Return(["subcategory", subcategory])
            
        text "[current_category]: [current_subcategory]" xpos 24 ypos 44 size 16
        
        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 5) % 4
                $ col = i % 5
                $ image_zoom = get_zoom(menu_items[i].get_icon(), 80, 80)
                add menu_items[i].get_icon() xpos 58+90*col ypos 225+90*row xanchor 0.5 yanchor 0.5 zoom image_zoom
                button xsize 90 ysize 90 style "empty" hover_background btn_hover xpos 10+90*(col) ypos 176+90*(row) action Return(["equip", menu_items[i]])
                if menu_items[i].id == char_active.get_equipped(current_category, current_subcategory, i):
                    #$ current_item = menu_items[i]
                    text "{color=#FFFFFF}Worn{/color}"xpos 26+90*col ypos 240+90*row
                    
        # Add empty items
        for i in xrange(menu_items_length, items_shown):
            $ row = (i // 5) % 4
            $ col = i % 5
            button xsize 88 ysize 88 style "empty" background "#00000033" xpos 10+90*(col) ypos 180+90*(row)
                    
screen t_wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    if menu_items_length > 9:
        # Up Button
        if not current_page <= 0:
            imagebutton:
                xpos xx+480
                ypos yy+190
                idle "interface/general/"+interface_color+"/button_arrow_up.png"
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")
        if current_page < math.ceil((menu_items_length)/10):
            # Down Button
            imagebutton:
                xpos xx+480
                ypos yy+245
                idle "interface/general/"+interface_color+"/button_arrow_down.png"
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        xpos xx
        ypos yy
        xsize 467
        ysize 548
        style "empty"
        background bg_color_wardrobe
   
        add "interface/panels/"+interface_color+"/icon_panel_2.png"
            
        text "[current_category]: [current_subcategory]" xpos 24 ypos 44 size 16
        
        # Page counter
        if menu_items_length > 9:
            hbox:
                xanchor 1.0
                xpos 270
                spacing 5
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/10))+1) ypos 44 size 16
        
        # Add subcategory list
        for i, subcategory in enumerate(category_items):
            add "interface/wardrobe/test/icons/"+current_category+"_"+subcategory+".png" ypos 88 xpos 10+(90*i) zoom 0.2
            button xsize 86 ysize 86 ypos 88 xpos 10+(90*i) style "empty" hover_background btn_hover action Return(["subcategory", subcategory])
        
        # Add items
        for i in xrange(current_page*10, (current_page*10)+10):
            if i < menu_items_length:
                $ row = (i // 5) % 2
                $ col = i % 5
                add menu_items[i].get_image() xpos 40+90*col ypos 117+180*row xalign 0.5 zoom 0.2
                if current_subcategory == "Delete":
                    button xsize 90 ysize 180 style "empty" hover_background "#cc330040" xpos 10+90*col ypos 176+180*row action Return(["deloutfit", i])
                    #textbutton "{color=#B33A3A}{size=50}-{/size}{/color}" style "empty" hover_background "#cc330040" xsize 90 ysize 180 xpos 10+90*col ypos 176+180*row text_xalign 0.5 text_yalign 0.5 action Return(["deloutfit", i]) text_outlines [ (4, "#000", 0, 0) ]
                elif current_subcategory == "Load":
                    button xsize 90 ysize 180 style "empty" hover_background btn_hover xpos 10+90*col ypos 176+180*row action Return(["equip", menu_items[i]])
                elif current_subcategory == "Export&Import":
                    textbutton "Export" xsize 90 ysize 180 style "empty" hover_background btn_hover text_color "#FFF" text_outlines [(4, "#000", 0, 0)] xpos 10+90*col ypos 176+180*row text_xalign 0.5 text_yalign 0.95 action Return(["export", menu_items[i]])
                    
        # Add empty items
        for i in xrange(menu_items_length, (current_page*10)+10):
            $ row = (i // 5) % 2
            $ col = i % 5
            if current_subcategory == "Save":
                textbutton "{size=50}+{/size}" style "empty" background "#00000033" hover_background btn_hover text_color "#FFF" xsize 88 ysize 178 xpos 10+90*col ypos 180+180*row text_xalign 0.5 text_yalign 0.5 action Return("addoutfit")
            elif current_subcategory == "Export&Import":
                textbutton "Import" style "empty" background "#00000033" hover_background btn_hover text_color "#FFF" text_outlines [(4, "#000", 0, 0)] xsize 88 ysize 178 xpos 10+90*col ypos 180+180*row text_xalign 0.5 text_yalign 0.5 action Return("import")
            else:
                button style "empty" background "#00000033" xsize 88 ysize 178 xpos 10+90*col ypos 180+180*row