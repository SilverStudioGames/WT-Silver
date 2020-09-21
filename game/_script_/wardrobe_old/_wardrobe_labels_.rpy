### CALL WARDROBE LABELS ###

label reset_wardrobe_vars:
    $ wardrobe_page = 0
    $ wardrobe_page_choice = 0
    $ hide_transitions = True
    $ wardrobe_toggle_page = 0            #default page
    $ wardrobe_head_category = 0          #default page
    $ wardrobe_tops_category = 0          #default page
    $ wardrobe_bottoms_category = 0       #default page
    $ wardrobe_stockings_category = 0     #default page
    $ wardrobe_accessories_category = 0   #default page
    $ wardrobe_underwear_category = 0     #default page
    $ wardrobe_outfits_category = 0       #default page
    $ wardrobe_gifts_category = 0         #default page
    $ wardrobe_load_custom_outfit = True  #False = save custom outfit.

    $ wr_action_list = []

    if active_girl == "susan":
        $ wr_base_hair_style = "braided"
        $ wr_base_hair_color = "red"

    $ wardrobe_head_color             = "base"
    $ wardrobe_uniform_color          = "base"
    $ wardrobe_tops_color             = "base"
    $ wardrobe_bottoms_color          = "base"
    $ wardrobe_stockings_color        = "base"
    $ wardrobe_other_clothings_color  = "base"
    $ wardrobe_accessories_color      = "base"
    $ wardrobe_underwear_color        = "base"
    $ wardrobe_outfits_color          = "base"

    #Music
    if play_wardrobe_music:
        if not wardrobe_music:
            $ wardrobe_music = True
            call play_music("wardrobe")

    return

label return_to_wardrobe:
    if not hide_transitions:
        if active_girl == "susan":
            call sus_main(face="happy",xpos="wardrobe",ypos="base",trans=fade)

        $ hide_transitions = True
        call screen wardrobe_old

    else:
        $ hide_transitions = True

        if active_girl == "susan":
            call sus_main(face="happy",xpos="wardrobe",ypos="base")

        call screen wardrobe_old


### UPDATE WARDROBE COLOR PALETTE ###

label update_wardrobe_color:

    if active_girl == "susan":
        call sus_main(xpos="wardrobe",ypos="base")

    call screen wardrobe_old

label wardrobe_update:

    if wardrobe_page_choice == 0: #Default
        call update_wr_color_list
        $ wardrobe_page = 0
    if wardrobe_page != 1 and wardrobe_page_choice == 1:
        call update_wr_head_list
        $ wardrobe_page = 1
    if wardrobe_page != 2 and wardrobe_page_choice == 2:
        call update_wr_tops_list
        $ wardrobe_page = 2
    if wardrobe_page != 3 and wardrobe_page_choice == 3:
        call update_wr_bottoms_list
        $ wardrobe_page = 3
    if wardrobe_page != 4 and wardrobe_page_choice == 4:
        call update_wr_other_clothings_list
        $ wardrobe_page = 4
    if wardrobe_page != 5 and wardrobe_page_choice == 5:
        call update_wr_miscellaneous_list
        $ wardrobe_page = 5
    if wardrobe_page != 6 and wardrobe_page_choice == 6:
        call update_wr_underwear_list
        call update_wr_other_clothings_list #For stockings
        $ wardrobe_page = 6
    if wardrobe_page != 7 and wardrobe_page_choice == 7:
        call update_wr_outfits_list
        $ wardrobe_page = 7
    if wardrobe_page != 8 and wardrobe_page_choice == 8: #gifts
        $ wardrobe_page = 8

    #Music
    if play_wardrobe_music:
        if not wardrobe_music:
            $ wardrobe_music = True
            call play_music("wardrobe")
    else:
        if wardrobe_music:
            $ wardrobe_music = False
            call play_music(active_girl)

    #Sound Effects
    if add_wardrobe_sound: #False by default. Only happens on a "wardrobe_page" change.
        if wardrobe_page == 0:
            $ renpy.play('sounds/door2.mp3') #closing wardrobe page
        else:
            $ renpy.play('sounds/scroll.mp3') #opening wardrobe page
    $ add_wardrobe_sound = False

    if active_girl == "susan":
        call wr_sus_clothing_reset
        call sus_main(xpos="wardrobe",ypos="base")

    call screen wardrobe_old

label wr_sus_clothing_reset:
    #Reload Clothing
    call load_susan_clothing_saves

    #Qol stuff
    if wardrobe_page != 6:
        pass
    #    if susan_action != "none":
    #        $ susan_use_action = True
    else: #Underwear page Qol
        $ susan_wear_robe = False
        $ susan_wear_top = False
        $ susan_wear_bottom = False

    call update_sus_uniform

    return

### CLOSE WARDROBE LABELS ###

label hide_wardrobe:
    call ctc
    call screen wardrobe_old

label close_wardrobe:
    $ renpy.play('sounds/door2.mp3') #closing wardrobe page
    #Music
    if wardrobe_music:
        $ wardrobe_music = False
        call music_block

    if active_girl == "susan":
        call sus_main(xpos="base",ypos="base")
        jump susan_requests

### TOGGLE LABELS ###

label wardrobe_chitchat_toggle:

    if wardrobe_chitchat_active:
        $ wardrobe_chitchat_active = False
    else:
        $ wardrobe_chitchat_active = True

    call screen wardrobe_old
### MISCELLANEOUS SECTION ###

## Piercings ##
label equip_piercing:
    jump return_to_wardrobe

## Tattoos ##
label equip_tattoo:
    jump return_to_wardrobe


### GIFTS SECTION ###

## Gifts ##
label wardrobe_give_gift:
    jump return_to_wardrobe

## Potions ## Not in use ## Move to Accessories
label wardrobe_give_potion:
    hide screen wardrobe_gifts
    $ renpy.jump("potion_scene_"+str(wardrobe_potion))
