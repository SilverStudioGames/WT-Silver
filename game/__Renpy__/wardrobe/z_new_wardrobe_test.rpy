












label cho_wardrobe_test: # WIP

    # Reset
    $ current_page = 0
    $ current_group = "1"
    $ category_choice = None
    $ char_name = "cho"
    $ char_nickname = cho_name
    $ hide_transitions = True

    label cho_wardrobe_test_menu:

    $ bg_color = cho_bg_color
    $ current_category = category_choice

    call update_cho_wardrobe_items(char_name, current_category, current_group) # Updates 'item_list'
    call cho_main(xpos="wardrobe",ypos="base")

    label wardrobe_test_menu:

    python:

        # Right Wardrobe Panel
        current_category = category_choice
        wardrobe_categories = ["head","tops","bottoms","other","misc","underwear","outfits","gifts"]

        # Left Wardrobe Panel

        # Category Name Update
        if current_category == "head":
            menu_title = "Hair & Head Items"
        elif current_category == "other":
            menu_title = "Other Clothing"
        elif current_category == "misc":
            menu_title = "Miscellaneous"
        else:
            menu_title = current_category

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))

    show screen wardorobe_menu(char_nickname, char_name, current_category, xpos=550, ypos=50)

    if current_category != None:
        show screen wardorobe_item_menu(item_list, char_name, current_category, group_list, menu_title, xpos=20, ypos=50)

    $ _return = ui.interact()

    hide screen wardorobe_menu
    hide screen wardorobe_item_menu

    if isinstance(_return, item_class):
        call equip_cho_item(_return)


    elif _return == "open_category":
        $ renpy.play('sounds/scroll.mp3') #opening wardrobe page
    elif _return == "close_category":
        $ renpy.play('sounds/door2.mp3') #closing wardrobe page

    elif _return == "change_bg_color":
        $ cho_bg_color = color_picker([playercolor_r*255, playercolor_g*255, playercolor_b*255, 255], False, "wardrobe color")

    elif _return == "Close":
        $ renpy.play('sounds/door2.mp3') #closing wardrobe page
        $ current_page = 0
        $ hide_transitions = False
        call cho_main(xpos="base",ypos="base")

        jump cho_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump cho_wardrobe_test_menu


# Right Wardrobe Menu
screen wardorobe_menu(nickname, character, category, xpos, ypos):
    $ ui_xpos = xpos
    $ ui_ypos = ypos
    zorder 4

    # Close Button
    use top_bar_close_button

    # Main Window im.MatrixColor( image, im.matrix.tint(red, green, blue))
    add im.MatrixColor( "interface/panels/bg/wardrobe_panel.png", im.matrix.tint(bg_color[0]/255.0, bg_color[1]/255.0, bg_color[2]/255.0)) xpos ui_xpos+100 ypos ui_ypos
    if category == None:
        add "interface/wardrobe/test/" +str(interface_color)+ "/icons_" +str(character)+ ".png" xpos ui_xpos+13 ypos ui_ypos+80 zoom 0.5
    else:
        add "interface/wardrobe/test/" +str(interface_color)+ "/icons_" +str(character)+ "_" +str(category)+ ".png" xpos ui_xpos+13 ypos ui_ypos+80 zoom 0.5

    imagemap:
        xpos ui_xpos
        ypos ui_ypos
        xsize 540 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/panels/"+interface_color+"/wardrobe_panel.png"
        hover "interface/panels/"+interface_color+"/wardrobe_panel_hover.png"

        for i in range(0,4): # Left side.
            if category == wardrobe_categories[i]:
                hotspot (15 , 82 +(110*i) , 85 , 93) clicked SetVariable("category_choice",None), Return("close_category")
            else:
                hotspot (15+48 , 82 +(110*i) , 37 , 93) clicked SetVariable("category_choice",wardrobe_categories[i]), Return("open_category")

        for i in range(4,8): # Right side.
            if category == wardrobe_categories[i]:
                hotspot (15 +425 , 82 +(110*(i-4)) , 84 , 93) clicked SetVariable("category_choice",None), Return("close_category")
            else:
                hotspot (15 +425 , 82 +(110*(i-4)) , 40 , 93) clicked SetVariable("category_choice",wardrobe_categories[i]), Return("open_category")

        # Character Name
        add "interface/general/"+str(interface_color)+"/button_wide.png" xpos 200 ypos -4
        hbox:
            xpos 200
            ypos -4
            xsize 140
            ysize 34
            text nickname xalign 0.5 yalign 0.5 size 16 bold 0.2

        # BG color
        hotspot (340, 60, 18, 18) clicked Return("change_bg_color")
        add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 340 ypos 60-5
        text "bg color" xpos 340+21 ypos 60+4 size 10

        #Wardrobe music
        #if play_wardrobe_music:
        #    hotspot (900,150+410,18,18) clicked [SetVariable("play_wardrobe_music",False), Jump("wardrobe_update")]
        #    add "interface/wardrobe/"+str(interface_color)+"/check_true.png" xpos 900 ypos 145+410
        #else:
        #    hotspot (900,150+410,18,18) clicked [SetVariable("play_wardrobe_music",True), Jump("wardrobe_update")]
        #    add "interface/wardrobe/"+str(interface_color)+"/check_false.png" xpos 900 ypos 145+410
        #text "Music" xpos 900+21 ypos 154+410 size 10


# Left Wardrobe Menu # Not working yet
screen wardorobe_item_menu(menu_items, character, category, groups, title, xpos, ypos):
    $ items_shown = 20
    $ ui_xpos = xpos
    $ ui_ypos = ypos
    zorder 4

    # Close Button
    use top_bar_close_button

    # Buttons
    if len(menu_items) > 20:
        # Up Button
        imagebutton:
            xpos ui_xpos +480
            ypos ui_ypos +190
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            if not current_page <= 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")

        # Down Button
        imagebutton:
            xpos ui_xpos +480
            ypos ui_ypos +190 +55
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            if current_page < math.ceil((len(menu_items)-1)/items_shown):
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")


    # Main Window
    add im.MatrixColor( "interface/panels/bg/icon_panel.png", im.matrix.tint(bg_color[0]/255.0, bg_color[1]/255.0, bg_color[2]/255.0)) xpos ui_xpos ypos ui_ypos
    imagemap:
        xpos ui_xpos
        ypos ui_ypos
        xsize 467 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/panels/"+interface_color+"/icon_panel.png"
        hover "interface/panels/"+interface_color+"/icon_panel_hover.png"

        # Header
        hbox:
            xpos 11
            ypos 30
            xsize 265
            ysize 45
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        # Groups
        for i in range(0,len(groups)): #Max 5 items!
            hotspot (12+(90*i), 87, 83, 85) clicked SetVariable("group_choice",groups[i]), Return()
            add "interface/icons/wardrobe/" +str(character)+ "/" +str(category)+ "_" +str(groups[i])+ ".png" xalign 0.5 xpos 50+(90*i) yalign 0.5 ypos 129 zoom 0.2

        # Items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                $ row = (i // 4) % 4
                $ col = i % 5
                hotspot ( (12+(90*col)), (87+92+(92*row)-(current_page*items_shown)), 83, 85) clicked Return(menu_items[i])
                add wr_items_path +str(menu_items[i])+ ".png" xalign 0.5 xpos item_xpos +90*(col-(current_page*items_shown)) ypos item_ypos +90*(row-(current_page*items_shown)) zoom item_scaling




label update_cho_wardrobe_items(character, category, group):
python:

    item_list = []
    group_list = ["1"]
    toggle_list = []
    use_wr_color = False

    item_xpos = 40
    item_scaling = 0.2

    if category == "head":
        group_list = ["1","2","3"]
        if group == "1":
            item_xpos = 40
            item_ypos = 130
            item_list.append("ponytail_blue")
            wr_items_path = "characters/" +str(character)+ "/body/head/"

    if category == "tops":
        group_list = ["1","3"]
        item_xpos = 40
        item_ypos = 75
        item_scaling = 0.2

        item_list = []
        if group == "1":
            item_list.append("top_1")
            item_list.append("top_2")
            item_list.append("top_3")
            item_list.append("top_4")
            item_list.append("top_5")
            item_list.append("sweater_1")
            item_list.append("sweater_2")
            item_list.append("top_1")
            item_list.append("top_2")
            item_list.append("top_3")
            item_list.append("top_4")
            item_list.append("top_5")
            item_list.append("top_1")
            item_list.append("top_2")
            item_list.append("top_3")
            item_list.append("top_4")
            item_list.append("top_5")
            item_list.append("top_1")
            item_list.append("top_2")
            item_list.append("sweater_1")
            item_list.append("sweater_2")
            item_list.append("top_5")
            item_list.append("top_1")
            item_list.append("top_2")
        if group == "3":
            use_wr_color = True
            item_list.append("top_tanktop_1")
            item_list.append("top_tanktop_2")
            item_list.append("top_shirt_1")
        wr_items_path = "characters/" +str(character)+ "/clothes/tops/base/"

    if category == "bottoms":
        group_list = ["1","4"]
        item_xpos = 40
        item_ypos = 25
        item_scaling = 0.2

        item_list = []
        if group == "1":
            use_wr_color = True
            item_list.append("skirt_2")
            item_list.append("skirt_2_low")
            item_list.append("skirt_3")
            item_list.append("skirt_3_low")
            item_list.append("skirt_3_belted")
            item_list.append("skirt_4")
            item_list.append("skirt_4_low")
        if group == "4":
            item_list.append("pants_sport_long")
            item_list.append("pants_yoga_long")
            item_list.append("pants_yoga_short")
            item_list.append("pants_jeans_short")
            item_list.append("pants_short_1")
        wr_items_path = "characters/" +str(character)+ "/clothes/bottoms/base/"


return
