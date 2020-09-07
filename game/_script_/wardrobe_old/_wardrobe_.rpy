

screen wardrobe_old():
    tag wardrobe_menu_old
    zorder 11

    if active_girl in ["luna","susan"]:
        $ icon_ypos_offset = 0
        $ wardrobe_toggle_page = 4 #Force disables toggle pages.

    imagemap:
        cache False


        ## Ground & Hovers ##
        if wardrobe_page == 0: #default
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+".webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_right_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_right_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 1: #hair
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_hair.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 2: #tops
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_tops.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 3: #bottoms
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_bottoms.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 4: #other clothings
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_stockings.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 5: #accessories
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_accessories.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 6: #underwear
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_underwear.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 7: #outfits
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_outfits.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_outfits_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_outfits_"+str(wardrobe_color)+".webp"
        elif wardrobe_page == 8: #gifts
            add "interface/wardrobe/old/"+str(interface_color)+"/icons_"+str(active_girl)+"_gifts.webp" zoom 0.5
            ground "interface/wardrobe/old/"+str(interface_color)+"/ground_full_"+str(wardrobe_color)+".webp"
            hover "interface/wardrobe/old/"+str(interface_color)+"/hover_full_"+str(wardrobe_color)+".webp"


        ## Always Active ##
        use close_button(close_action=[SetVariable("wardrobe_page",0), Jump("close_wardrobe")])

        if active_girl == "luna":
            text ""+lun_name xalign 0.5 xpos 820 ypos 57 size 20
        if active_girl == "susan":
            text ""+susan_name xalign 0.5 xpos 820 ypos 57 size 20
        text "Wardrobe" xpos 668 ypos 154+360 size 12

        #Wardrobe background color
        for i in range(0,len(wr_background_color)):
            $ col = i % 5

            hotspot (667+(20*col), 559, 20, 20) clicked [SetVariable("wardrobe_color",wr_background_color[i]), Jump("update_wardrobe_color")]
            add "interface/wardrobe/old/icons/colors/"+wr_background_color[i]+".webp" xpos 668+(20*col) ypos 560

        #Wardrobe music
        if play_wardrobe_music:
            hotspot (900,150+410,18,18) clicked [SetVariable("play_wardrobe_music",False), Jump("wardrobe_update")]
            add "interface/wardrobe/old/"+str(interface_color)+"/check_true.webp" xpos 900 ypos 145+410
        else:
            hotspot (900,150+410,18,18) clicked [SetVariable("play_wardrobe_music",True), Jump("wardrobe_update")]
            add "interface/wardrobe/old/"+str(interface_color)+"/check_false.webp" xpos 900 ypos 145+410
        text "Music" xpos 900+21 ypos 154+410 size 10

        ## Page Specific Hotspots ##
        if wardrobe_page == 0: #default #Not used yet.
            pass
        else:
            pass

        #Hair
        if wardrobe_page == 1:
            hotspot (561, 122, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Hair-Style & Head Accs." xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 122, 38, 93) clicked [SetVariable("wardrobe_page_choice",1),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Tops
        if wardrobe_page == 2:
            hotspot (561, 232, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Top Clothings" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 232, 38, 93) clicked [SetVariable("wardrobe_page_choice",2),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Bottoms
        if wardrobe_page == 3:
            hotspot (561, 342, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]
            text "Bottom Clothings" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 342, 38, 93) clicked [SetVariable("wardrobe_page_choice",3),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]

        #Other Clothings
        if wardrobe_page == 4:
            hotspot (561, 452, 86, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Other Clothings" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (609, 452, 38, 93) clicked [SetVariable("wardrobe_page_choice",4),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Miscellaneous Accessories
        if wardrobe_page == 5:
            hotspot (987, 122, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Miscellaneous" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 122, 40, 93) clicked [SetVariable("wardrobe_page_choice",5),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Underwear
        if wardrobe_page == 6:
            hotspot (987, 232, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Underwear" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 232, 40, 93) clicked [SetVariable("wardrobe_page_choice",6),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")]

        #Outfits
        if wardrobe_page == 7:
            hotspot (987, 342, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Costumes & Outfits" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 342, 40, 93) clicked [SetVariable("wardrobe_page_choice",7),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Gifts
        if wardrobe_page == 8:
            hotspot (987, 452, 84, 93) clicked [SetVariable("wardrobe_page_choice",0),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #return to default
            text "Gifts" xalign 0.5 xpos 208 ypos 96 size 18
        else:
            hotspot (987, 452, 40, 93) clicked [SetVariable("wardrobe_page_choice",8),SetVariable("add_wardrobe_sound",True), Jump("wardrobe_update")] #default

        #Temporary. Disables toggles for Luna Susan
        if wardrobe_toggle_page == 4:
            pass

        ## Wardrobe ChitChat Toggle
        hotspot (667,150+385,18,18) clicked Jump("wardrobe_chitchat_toggle")
        if wardrobe_chitchat_active:
            add "interface/wardrobe/old/"+str(interface_color)+"/check_true.webp" xpos 667 ypos 145+385 #ypos-5 of hotspot ypos
        else:
            add "interface/wardrobe/old/"+str(interface_color)+"/check_false.webp" xpos 667 ypos 145+385
        text "Chit-Chat" xpos 688 ypos 154+385 size 10


### Wardrobe Hair & Head Accessories ###

        if wardrobe_page == 1:

            #Hair-Style and Hair-Color
            hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
            add "characters/"+str(active_girl)+"/body/head/"+str(wr_base_hair_style)+"_"+str(wr_base_hair_color)+".webp" xpos 10 ypos 102+icon_ypos_offset zoom 0.175
            #text "Hair" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Makeup
            if active_girl in ["hermione"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",1),Show("wardrobe_old")]
                add "interface/icons/lipstick_red.webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Makeup" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Glasses
            if active_girl in ["hermione","luna"]:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",2),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/glasses.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Glasses" xalign 0.5 xpos 115+180 ypos 140+75 size 10
            #Ears
            if active_girl in ["hermione"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",3),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/ears.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Ears" xalign 0.5 xpos 115+270 ypos 140+75 size 10
            #Hats
            if active_girl in ["hermione","luna","astoria","cho","tonks"]:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",4),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/hats.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Hats" xalign 0.5 xpos 115+360 ypos 140+75 size 10

            #Hair Color Palette
            if wardrobe_head_category == 0 and active_girl in ["hermione","tonks"]: #Hair Color
                for i in range(0,len(wr_haircolor)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((370+(20*col)), (84+(20*row)), 20, 20) clicked [SetVariable("wr_base_hair_color",wr_haircolor[i]), Jump("wardrobe_update")]
                    add "interface/wardrobe/old/icons/colors/"+wr_haircolor[i]+".webp" xpos 371+(20*col) ypos (85+(20*row))

            #Hair-Style and Hair-Color
            if wardrobe_head_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
                add "characters/"+str(active_girl)+"/body/head/"+str(wr_base_hair_style)+"_"+str(wr_base_hair_color)+".webp" xpos 10 ypos 102+icon_ypos_offset zoom 0.175
                #text "Hair" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_hair)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("hair_style_choice",(wr_hair[i])),SetVariable("hair_color_choice",wr_base_hair_color), Jump("change_hair")]
                    add "characters/"+str(active_girl)+"/body/head/"+wr_hair[i]+"_"+str(wr_base_hair_color)+".webp" xpos 10+(90*col) ypos (102+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Makeup
            if wardrobe_head_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
                add "interface/icons/lipstick_red.webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Makeup" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_makeup)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("makeup_choice",(wr_makeup[i])), Jump("equip_makeup")]
                    add "interface/wardrobe/old/icons/items/"+wr_makeup[i]+".webp" xpos 0+(90*col) ypos (90+92+(92*row)) zoom 0.3

            #Glasses
            if wardrobe_head_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/glasses.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Glasses" xalign 0.5 xpos 115+180 ypos 140+75 size 10
                for i in range(0,len(wr_glasses)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("head_accessory_choice",wr_glasses[i]), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/clothes/glasses/"+wr_glasses[i]+".webp" xpos -165+(90*col) ypos (-10+icon_ypos_offset+92+(92*row)) zoom 0.5

            #Ears
            if wardrobe_head_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/ears.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Ears" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_ears)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("head_accessory_choice",(wr_ears[i])), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/clothes/ears/"+wr_ears[i]+".webp" xpos -30+(90*col) ypos (100+icon_ypos_offset+92+(92*row)) zoom 0.25

            #Hats
            if wardrobe_head_category == 4:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_head_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/hats.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Hats" xalign 0.5 xpos 115+360 ypos 140+75 size 10
                for i in range(0,len(wr_hats)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("head_accessory_choice",(wr_hats[i])), Jump("equip_head_accessory")]
                    add "characters/"+str(active_girl)+"/clothes/hats/hair_"+str(wr_base_hair_style)+"/"+wr_hats[i]+".webp" xpos -65+(90*col) ypos (70+icon_ypos_offset+92+(92*row)) zoom 0.3


### Wardrope Tops ###

        if wardrobe_page == 2:

            #Uniform
            hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe_old")]
            add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_1.webp" xpos 75 ypos 139 zoom 0.2
            #text "Uniform" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Cheerleader
            if active_girl in ["hermione","luna"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",1),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Cheerleader" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Muggle
            if active_girl in ["hermione","luna","cho"]:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",2),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Muggle" xalign 0.5 xpos 115+180 ypos 140+75 size 10
            #Wicked
            if active_girl in ["hermione","tonks"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",3),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Wicked" xalign 0.5 xpos 115+270 ypos 140+75 size 10


            #Uniforms
            if wardrobe_tops_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_1.webp" xpos 75 ypos 139 zoom 0.2
                #text "Uniform" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_tops_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice","base"),SetVariable("top_choice",wr_tops_uniform[i]), Jump("equip_top")]
                    add "characters/"+str(active_girl)+"/clothes/tops/"+wr_tops_uniform[i]+".webp" xpos 15+(90*col) ypos (60+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Cheerleader
            if wardrobe_tops_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Cheerleader" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_tops_cheerleader)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice","base"),SetVariable("top_choice",wr_tops_cheerleader[i]), Jump("equip_top")]
                    add "characters/"+str(active_girl)+"/clothes/tops/"+wr_tops_cheerleader[i]+".webp" xpos 15+(90*col) ypos (60+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Muggle
            if wardrobe_tops_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Muggle" xalign 0.5 xpos 115+180 ypos 140+75 size 10
                for i in range(0,len(wr_tops_normal)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice",wardrobe_tops_color),SetVariable("top_choice",wr_tops_normal[i]), Jump("equip_top")]
                    add "characters/"+str(active_girl)+"/clothes/tops/"+wr_tops_normal[i]+".webp" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.175

            #Wicked
            if wardrobe_tops_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/tops_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Wicked" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_tops_wicked)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_color_choice","base"),SetVariable("top_choice",wr_tops_wicked[i]), Jump("equip_top")] #Wicked tops have NO recolor!
                    add "characters/"+str(active_girl)+"/clothes/tops/"+wr_tops_wicked[i]+".webp" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.175


### Wardrobe Bottoms ###

        if wardrobe_page == 3:

            #Uniform
            hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe_old")]
            add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_1.webp" xpos 75 ypos 139 zoom 0.2
            #text "Uniform" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Cheerleader
            if active_girl in ["hermione","luna"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",1),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Cheerleader" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Pants
            if active_girl in ["hermione","cho","tonks"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",3),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Pants" xalign 0.5 xpos 115+270 ypos 140+75 size 10

            #Uniforms
            if wardrobe_bottoms_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_1.webp" xpos 75 ypos 139 zoom 0.2
                #text "Uniform" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice",wardrobe_bottoms_color),SetVariable("skirt_choice",wr_bottoms_uniform[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+wr_bottoms_uniform[i]+".webp" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Cheerleader
            if wardrobe_bottoms_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Cheerleader" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_cheerleader)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice","base"),SetVariable("skirt_choice",wr_bottoms_cheerleader[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+wr_bottoms_cheerleader[i]+".webp" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Pants
            if wardrobe_bottoms_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/bottoms_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Pants" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_bottoms_pants)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("bottom_color_choice","base"),SetVariable("skirt_choice",wr_bottoms_pants[i]), Jump("equip_bottom")]
                    add "characters/"+str(active_girl)+"/clothes/bottoms/"+wr_bottoms_pants[i]+".webp" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.175



## Wardrobe Other Clothings ##

        if wardrobe_page == 4:

            #Neckwear
            if active_girl in ["hermione","luna","astoria","susan","cho","tonks"]:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/neck.webp" xpos 75 ypos 139 zoom 0.2
                #text "Neckwear" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Body Accessories
            if active_girl in ["hermione","cho"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",1),Show("wardrobe_old")]
                add "interface/icons/badge_spew.webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Body Accs." xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Gloves
            if active_girl in ["hermione","cho","tonks"]:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",2),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/gloves.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Gloves" xalign 0.5 xpos 115+180 ypos 140+75 size 10
            #Stockings
            if active_girl in ["hermione","luna","astoria","susan","cho","tonks"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",3),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/stockings.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Stockings" xalign 0.5 xpos 115+270 ypos 140+75 size 10
            #Robes
            if active_girl in ["hermione","astoria","tonks"]:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",4),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/robes.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Robes" xalign 0.5 xpos 115+360 ypos 140+75 size 10


            #Neckwear
            if wardrobe_stockings_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/neck.webp" xpos 75 ypos 139 zoom 0.2
                #text "Neckwear" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_neckwears)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("neckwear_choice",wr_neckwears[i]), Jump("equip_neckwear")]
                    add "characters/"+str(active_girl)+"/clothes/neckwear/"+str(wr_neckwears[i])+".webp" xpos 15+(90*col) ypos 60+icon_ypos_offset+92+(92*row) zoom 0.175

            #Body Accessories
            if wardrobe_stockings_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/icons/badge_spew.webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Body Accs." xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_body_accs)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("body_accessory_choice",(wr_body_accs[i])), Jump("equip_body_accessory")]
                    add "characters/"+str(active_girl)+"/clothes/accs/"+wr_body_accs[i]+".webp" xpos 15+(90*col) ypos (60+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Gloves
            if wardrobe_stockings_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/gloves.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Gloves" xalign 0.5 xpos 115+180 ypos 140+75 size 10
                for i in range(0,len(wr_gloves)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("gloves_choice",wr_gloves[i]), Jump("equip_gloves")]
                    add "characters/"+str(active_girl)+"/clothes/gloves/"+str(wr_gloves[i])+".webp" xpos 15+(90*col) ypos 30+icon_ypos_offset+92+(92*row) zoom 0.175

            #Stockings
            if wardrobe_stockings_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/stockings.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Stockings" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_stockings)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("stockings_choice",wr_stockings[i]), Jump("equip_stockings")]
                    add "characters/"+str(active_girl)+"/clothes/stockings/"+str(wr_stockings[i])+".webp" xpos -25+(90*col) ypos -75+92+(92*row) zoom 0.25

            #Robes
            if wardrobe_stockings_category == 4:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/robes.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Robes" xalign 0.5 xpos 115+360 ypos 140+75 size 10
                for i in range(0,len(wr_robes)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("robe_choice",wr_robes[i]),Jump("equip_robe")]
                    add "characters/"+str(active_girl)+"/clothes/robe/"+str(wr_robes[i])+".webp" xpos 45+(90*col) ypos 77+92+(92*row) zoom 0.125


## Wardrobe Miscellaneous Accessories ##

        if wardrobe_page == 5:

            #Potions
            if active_girl in ["hermione","cho","tonks"]:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe_old")]
                add "interface/icons/item_potion.webp" xpos 72 ypos 128 zoom 0.30
                #text "Potions" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Items and Toys
            if active_girl in ["hermione","tonks"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",1),Show("wardrobe_old")]
                add "interface/icons/item_anal_plugs.webp" xpos 72+90 ypos 128 zoom 0.30
                text "Toys" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Piercings
            if active_girl in ["hermione","cho","tonks"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",3),Show("wardrobe_old")]
                add "interface/icons/icon_piercing_fancy.webp" xpos 72+270 ypos 128 zoom 0.30
                #text "Piercings" xalign 0.5 xpos 115+270 ypos 140+75 size 10
            #Tattoos
            if active_girl in ["hermione"]:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",4),Show("wardrobe_old")]
                add "interface/icons/icon_tattoo.webp" xpos 72+360 ypos 128 zoom 0.30
                #text "Tattoos" xalign 0.5 xpos 115+360 ypos 140+75 size 10


            ## Potions Category ##
            if wardrobe_accessories_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe_old")]
                add "interface/icons/item_potion.webp" xpos 72 ypos 128 zoom 0.30
                #text "Potions" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_potions_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("potion_choice",(wr_potions_list[i])), Jump("use_potion")]
                    add "interface/wardrobe/old/icons/potions/"+wr_potions_list[i]+".webp" xpos 65+(90*col) ypos (138+92+(92*row)) zoom 0.8

            ## Items and Toys Category ##
            if wardrobe_accessories_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe_old")]
                add "interface/icons/item_anal_plugs.webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Toys" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_items_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("misc_item_choice",(wr_items_list[i])), Jump("equip_misc_item")]
                    add "interface/icons/"+wr_items_list[i]+".webp" xpos 72+(90*col) ypos (128+92+(92*row)) zoom 0.30

            ##  Piercings ##
            if wardrobe_accessories_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe_old")]
                add "interface/icons/icon_piercing_fancy.webp" xpos 72+270 ypos 128 zoom 0.30
                #text "Piercings" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_piercings_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("piercing_choice",(wr_piercings_list[i])), Jump("equip_piercing")]
                    add "characters/"+str(active_girl)+"/clothes/piercings/"+wr_piercings_list[i]+".webp" xpos 15+(90*col) ypos (70+92+(92*row)) zoom 0.175

            ##  Tattoos ##
            if wardrobe_accessories_category == 4:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe_old")]
                add "interface/icons/icon_tattoo.webp" xpos 72+360 ypos 128 zoom 0.30
                #text "Tattoos" xalign 0.5 xpos 115+360 ypos 140+75 size 10
                for i in range(0,len(wr_tattoos_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("tattoo_choice",(wr_tattoos_list[i])), Jump("equip_tattoo")]
                    add "characters/"+str(active_girl)+"/body/tattoos/"+wr_tattoos_list[i]+".webp" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.175



## Wardrobe Underwear ##

        if wardrobe_page == 6:

            #Bras
            hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
            add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_1.webp" xpos 75 ypos 139 zoom 0.2
            #text "Bras" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Panties
            hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",1),Show("wardrobe_old")]
            add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_2.webp" xpos 75+90 ypos 139 zoom 0.2
            #text "Panties" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #One-Pieces
            if active_girl in ["hermione","luna","astoria","susan","tonks"]:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",2),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "One-Pieces" xalign 0.5 xpos 115+180 ypos 140+75 size 10
            #Garterbelts
            if active_girl in ["hermione","cho"]:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",3),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Garterbelts" xalign 0.5 xpos 115+270 ypos 140+75 size 10
            #Stockings
            if active_girl in ["hermione","luna","astoria","susan","cho","tonks"]:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",4),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/stockings.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Stockings" xalign 0.5 xpos 115+360 ypos 140+75 size 10


            #Bras
            if wardrobe_underwear_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_1.webp" xpos 75 ypos 139 zoom 0.2
                #text "Bras" xalign 0.5 xpos 115 ypos 140+75 size 10
                for i in range(0,len(wr_bras)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",wr_bras[i]), Jump("equip_bra")]
                    add "characters/"+str(active_girl)+"/clothes/bras/"+wr_bras[i]+".webp" xpos 15+(90*col) ypos (55+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Panties
            if wardrobe_underwear_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Panties" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                for i in range(0,len(wr_panties)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",wr_panties[i]), Jump("equip_panties")]
                    add "characters/"+str(active_girl)+"/clothes/panties/"+wr_panties[i]+".webp" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Nighties & Onepieces #Needs art edits for large breasts, poses...
            if wardrobe_underwear_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "One-Pieces" xalign 0.5 xpos 115+180 ypos 140+75 size 10
                for i in range(0,len(wr_onepieces)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_onepieces[i])), Jump("equip_onepiece")]
                    add "characters/"+str(active_girl)+"/clothes/onepieces/"+wr_onepieces[i]+".webp" xpos 15+(90*col) ypos (47+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Garterbelts
            if wardrobe_underwear_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/underwear_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "Garterbelts" xalign 0.5 xpos 115+270 ypos 140+75 size 10
                for i in range(0,len(wr_garterbelts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_garterbelts[i])), Jump("equip_garterbelt")]
                    add "characters/"+str(active_girl)+"/clothes/garterbelts/"+wr_garterbelts[i]+".webp" xpos 15+(90*col) ypos (17+icon_ypos_offset+92+(92*row)) zoom 0.175

            #Stockings
            if wardrobe_underwear_category == 4:
                hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/stockings.webp" xpos 75+360 ypos 139 zoom 0.2
                #text "Stockings" xalign 0.5 xpos 115+360 ypos 140+75 size 10
                for i in range(0,len(wr_stockings)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("stockings_choice",wr_stockings[i]), Jump("equip_stockings")]
                    add "characters/"+str(active_girl)+"/clothes/stockings/"+str(wr_stockings[i])+".webp" xpos -25+(90*col) ypos -75+92+(92*row) zoom 0.25


## Wardrobe Outfits ##

        if wardrobe_page == 7:

            #Outfits
            if active_girl in ["hermione","luna","astoria","susan","cho"]:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_1.webp" xpos 75 ypos 139 zoom 0.2
                #text "Outfits" xalign 0.5 xpos 115 ypos 140+75 size 10
            #Costumes
            if active_girl in ["hermione","luna","astoria","susan","cho"]:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",1),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Costumes" xalign 0.5 xpos 115+90 ypos 140+75 size 10
            #Dresses
            if active_girl in ["hermione","luna","astoria","susan","cho"]:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",2),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Dresses" xalign 0.5 xpos 115+180 ypos 140+75 size 10

            #
            #if active_girl in [""]:
                #hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",3),Show("wardrobe_old")]
                #add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_4.webp" xpos 75+270 ypos 139 zoom 0.2
                #text "" xalign 0.5 xpos 115+270 ypos 140+75 size 10

            #Save/Load Custom Outfit
            #if active_girl in ["hermione"]:
            #    hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",4),Show("wardrobe_old")]
            #    add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_5.webp" xpos 75+360 ypos 139 zoom 0.2
            #    text "Custom" xalign 0.5 xpos 115+360 ypos 140+75 size 10


            #Outfits
            if wardrobe_outfits_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_1.webp" xpos 75 ypos 139 zoom 0.2
                #text "Outfits" xalign 0.5 xpos 115 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_outfits)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(184*row)), 83, 175) clicked [SetVariable("outfit_choice",wr_outfits[i]), Jump("equip_outfit")]
                    add wr_outfits[i].get_image() xpos 31+(90*col) ypos 131+92+(179*row) zoom 0.155

            #Costumes
            if wardrobe_outfits_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_2.webp" xpos 75+90 ypos 139 zoom 0.2
                #text "Costumes" xalign 0.5 xpos 115+90 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_costumes)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(184*row)), 83, 175) clicked [SetVariable("outfit_choice",wr_costumes[i]), Jump("equip_outfit")]
                    add wr_costumes[i].get_image() xpos 31+(90*col) ypos 131+92+(179*row) zoom 0.155

            #Dresses
            if wardrobe_outfits_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
                add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_3.webp" xpos 75+180 ypos 139 zoom 0.2
                #text "Dresses" xalign 0.5 xpos 115+180 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_dresses)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(184*row)), 83, 175) clicked [SetVariable("outfit_choice",wr_dresses[i]), Jump("equip_outfit")]
                    add wr_dresses[i].get_image() xpos 31+(90*col) ypos 131+92+(179*row) zoom 0.155

            #
            #if wardrobe_outfits_category == 3:
            #    hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
            #    add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_4.webp" xpos 75+270 ypos 139 zoom 0.2
            #    text "" xalign 0.5 xpos 115+270 ypos 140+75 size 10
            #    $ index = 0
            #    for i in range(0,len(wr_swimsuits)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        if index < len(hg_purchased_swimsuits):

            #            hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("outfit_choice",hg_purchased_swimsuits[index]), Jump("equip_outfit")]
            #            add "images/panels/cs_gui/"+wr_swimsuits[i]+".webp" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
            #            $ index = index+1

            #Custom Saves
            #if wardrobe_outfits_category == 4:
            #    hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe_old")]
            #    add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits_5.webp" xpos 75+360 ypos 139 zoom 0.2
            #    text "Custom" xalign 0.5 xpos 115+360 ypos 140+75 size 10

                #Load Custom Outfit #Default
            #    if wardrobe_load_custom_outfit:
            #        hotspot (347, 95, 20, 20) clicked [SetVariable("wardrobe_load_custom_outfit",False), Jump("wardrobe_update")]
            #        hotspot (370, 84, 30, 30) clicked [SetVariable("wardrobe_load_custom_outfit",True), Jump("wardrobe_update")]
            #        add "interface/wardrobe/old/icons/colors/base.webp" xpos 371 ypos 85 zoom 1.5
            #        add "interface/wardrobe/old/icons/colors/blue.webp" xpos 348 ypos 96

                #Save Custom Outfit
            #    else:
            #        hotspot (347, 95, 30, 30) clicked [SetVariable("wardrobe_load_custom_outfit",False), Jump("wardrobe_update")]
            #        hotspot (370, 84, 20, 20) clicked [SetVariable("wardrobe_load_custom_outfit",True), Jump("wardrobe_update")]
            #        add "interface/wardrobe/old/icons/colors/base.webp" xpos 371 ypos 85
            #        add "interface/wardrobe/old/icons/colors/blue.webp" xpos 348 ypos 96 zoom 1.5



            #    $ index = 0
            #    for i in range(0,len(saved_custom_outfits)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        if index < len(saved_custom_outfits):

            #            hotspot ((75+(90*col)), (230+(184*row)), 83, 175) clicked [SetVariable("outfit_choice",saved_custom_outfits[index]), Jump("equip_custom_outfit")]
            #            #use image_layer_A xpos 77+(90*col) ypos 139+92+(92*row) zoom 0.18/scaleratio
            #            add "interface/wardrobe/old/icons/"+str(active_girl)+"/outfits/mannequin.webp" xpos 31+(90*col) ypos 131+92+(179*row) zoom 0.155
            #            #use image_layer_B xpos 77+(90*col) ypos 139+92+(92*row) zoom 0.18/scaleratio
            #            $ index = index+1


## Wardrobe Gifts ##

        if wardrobe_page == 8:
            hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
            add "interface/icons/"+str(chocolate_ITEM.image)+".webp" xpos 72 ypos 128 zoom 0.30
            #text "Candy" xalign 0.5 xpos 115 ypos 140+75 size 10

            hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",1),Show("wardrobe_old")]
            add "interface/icons/"+str(adult_mag_ITEM.image)+".webp" xpos 72+90 ypos 128 zoom 0.30
            #text "Magazines" xalign 0.5 xpos 115+90 ypos 140+75 size 10

            hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",2),Show("wardrobe_old")]
            add "interface/icons/"+str(butterbeer_ITEM.image)+".webp" xpos 72+180 ypos 128 zoom 0.30
            #text "Beverages" xalign 0.5 xpos 115+180 ypos 140+75 size 10

            hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",3),Show("wardrobe_old")]
            add "interface/icons/"+str(plush_owl_ITEM.image)+".webp" xpos 72+270 ypos 128 zoom 0.30
            #text "Toys" xalign 0.5 xpos 115+270 ypos 140+75 size 10

            #hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",4),Show("wardrobe_old")]
            #add "interface/icons/box_red_2.webp" xpos 72+360 ypos 128 zoom 0.30
            #text "Quest Items" xalign 0.5 xpos 115+360 ypos 140+75 size 10

            #Sweets
            if wardrobe_gifts_category == 0:
                hotspot (75, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
                add "interface/icons/"+str(chocolate_ITEM.image)+".webp" xpos 72 ypos 128 zoom 0.30
                #text "Candy" xalign 0.5 xpos 115 ypos 140+75 size 10

                if active_girl == "hermione":
                    for i in range(0,len(candy_gift_list)):
                        $ row = i // 5    #6
                        $ col = i % 5     #6
                        if candy_gift_list[i].number > 0:
                            hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",candy_gift_list[i]),Jump("wardrobe_give_gift")]
                            add "interface/icons/"+str(candy_gift_list[i].image)+".webp" xalign 0.5 yalign 0.5 xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        else:
                            add gray_tint("interface/icons/"+str(candy_gift_list[i].image)+".webp") xalign 0.5 yalign 0.5 xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        text str(candy_gift_list[i].number) xpos 75+(90*col) ypos (210+92+(92*row))

            #Magazines
            if wardrobe_gifts_category == 1:
                hotspot (75+90, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
                add "interface/icons/"+str(adult_mag_ITEM.image)+".webp" xpos 72+90 ypos 128 zoom 0.30
                #text "Magazines" xalign 0.5 xpos 115+90 ypos 140+75 size 10

                if active_girl == "hermione":
                    for i in range(0,len(mag_gift_list)):
                        $ row = i // 5    #6
                        $ col = i % 5     #6
                        if mag_gift_list[i].number > 0:
                            hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",mag_gift_list[i]),Jump("wardrobe_give_gift")]
                            add "interface/icons/"+str(mag_gift_list[i].image)+".webp" xalign 0.5 yalign 0.5  xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        else:
                            add gray_tint("interface/icons/"+str(mag_gift_list[i].image)+".webp") xalign 0.5 yalign 0.5 xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        text str(mag_gift_list[i].number) xpos 75+(90*col) ypos (210+92+(92*row))

            #Beverages
            if wardrobe_gifts_category == 2:
                hotspot (75+180, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
                add "interface/icons/"+str(butterbeer_ITEM.image)+".webp" xpos 72+180 ypos 128 zoom 0.30
                #text "Beverages" xalign 0.5 xpos 115+180 ypos 140+75 size 10

                if active_girl == "hermione":
                    for i in range(0,len(drink_gift_list)):
                        $ row = i // 5    #6
                        $ col = i % 5     #6
                        if drink_gift_list[i].number > 0:
                            hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",drink_gift_list[i]),Jump("wardrobe_give_gift")]
                            add "interface/icons/"+str(drink_gift_list[i].image)+".webp" xalign 0.5 yalign 0.5  xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        else:
                            add gray_tint("interface/icons/"+str(drink_gift_list[i].image)+".webp") xalign 0.5 yalign 0.5 xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        text str(drink_gift_list[i].number) xpos 75+(90*col) ypos (210+92+(92*row))

            #Toys
            if wardrobe_gifts_category == 3:
                hotspot (75+270, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
                add "interface/icons/"+str(plush_owl_ITEM.image)+".webp" xpos 72+270 ypos 128 zoom 0.30
                #text "Toys" xalign 0.5 xpos 115+270 ypos 140+75 size 10

                if active_girl == "hermione":
                    for i in range(0,len(toy_gift_list)):
                        $ row = i // 5    #6
                        $ col = i % 5     #6
                        if toy_gift_list[i].number > 0:
                            hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",toy_gift_list[i]),Jump("wardrobe_give_gift")]
                            add "interface/icons/"+str(toy_gift_list[i].image)+".webp" xalign 0.5 yalign 0.5  xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        else:
                            add gray_tint("interface/icons/"+str(toy_gift_list[i].image)+".webp") xalign 0.5 yalign 0.5 xpos 120+(90*col) ypos 180+92+(92*row) zoom 0.30
                        text str(toy_gift_list[i].number) xpos 75+(90*col) ypos (210+92+(92*row))

            #Quest Items
            #if wardrobe_gifts_category == 4:
            #    hotspot (75+360, 139, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe_old")]
            #    add "interface/icons/box_red_2.webp" xpos 72+360 ypos 128 zoom 0.30
            #    #text "Quest Items" xalign 0.5 xpos 115+360 ypos 140+75 size 10


            #    if active_girl == "hermione":

            #        #Collar Event
            #        if collar == 0 and her_whoring >= 24:
            #            hotspot (75, 140+92, 83, 85) clicked [Jump("start_collar_event")]
            #            add "interface/icons/icon_collar.webp" xpos 72 ypos 128+92 zoom 0.30
            #            text "Collar Event" xalign 0.5 xpos 115 ypos 140+75+92 size 10
            #        else:
            #            add add gray_tint("interface/icons/icon_collar.webp") xpos 72 ypos 128+92 zoom 0.30


# ADD wardrobe page for stats here!
