#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\"

### Equip Neckwear ### MISSING TEXTS
### Equip Body Accessories ###
### Equip Gloves ### MISSING TEXTS
### Equip Stockings ### MISSING TEXTS
### Equip Robe ### MISSING TEXTS



### Neckwear Equip ###
label equip_neckwear:
    #Susan
    if active_girl == "susan":
        jump equip_sus_neckwear

### Equip Susan's Neckwear ###
label equip_sus_neckwear:
    call set_sus_neckwear(neckwear_choice)

    jump return_to_wardrobe

### Gloves Equip ###
label equip_gloves:
    #Susan
    if active_girl == "susan":
        jump equip_sus_gloves

### Equip Susan's Gloves ###
label equip_sus_gloves:
    #call set_sus_gloves(gloves_choice)

    jump return_to_wardrobe

### Body Accs Equip ###
label equip_body_accessory:
    pass

    #Susan
    #if active_girl == "susan":
        #jump equip_sus_body_accessory

### Equip Hermione's Body Accessory ###
# label equip_her_body_accessory:

    # if her_mood >= 1:
        # jump equipping_failed

    # if body_accessory_choice not in hermione_body_accs_list:
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hermione_xpos = 665
            # $ hide_transitions = False #activates dissolve in her_main

            # m "[hermione_name]..."

            # #S.P.E.W Badge
            # if body_accessory_choice == "badge_spew":
                # m "Would you wear this badge for me?"
                # if her_whoring >= 0:
                    # call her_main("A S.P.E.W. badge?", "base", "base", "base", "mid")
                    # call her_main("I'll wear this with pride [genie_name].", "open", "closed", "base", "mid")

            # #I <3 Cum Badge
            # if body_accessory_choice == "badge_cum":
                # m "Would you wear this badge for me?"

                # if her_whoring >= 20:
                    # if her_whoring < 24:
                        # call her_main("Hm...?", "soft", "base", "base", "mid")
                        # call her_main("An \"I love cum\" badge?", "annoyed", "squint", "base", "mid")
                        # call her_main("{size=-5}(I suppose that it's not a complete lie...){/size}", "base", "narrow", "worried", "down")
                        # call her_main("Alright, I'll wear it.", "base", "narrow", "base", "mid_soft")
                    # else: #24
                        # call her_main("An \"I love cum\" badge?", "annoyed", "squint", "base", "mid")
                        # call her_main("Sure, [genie_name]!", "soft", "base", "base", "mid")
                        # call her_main("Let me put it on for you.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 8:
                        # jump too_much
                    # else: #8-19
                        # call her_main("An I love cum badge...?", "open", "base", "worried", "mid")
                        # call her_main("You cannot be serious, [genie_name]!", "open", "base", "base", "mid")
                        # m "What's wrong?"
                        # call her_main("I am not going to wear a badge that says that{w=0.5} {b}I{/b}{w=0.5} {b}love{/b}{w=0.5} {b}cum!{/b}", "normal", "squint", "angry", "mid")
                        # call her_main("I absolutely refuse!", "annoyed", "squint", "angry", "mid")
                    # ">She won't cover herself in cum just yet."
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 20."
                    # jump return_to_wardrobe

            # hide screen hermione_main
            # with d3

            # pause.5

            # call set_her_body_accessory(body_accessory_choice)

            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else:

            # $ hide_transitions = True
            # call set_her_body_accessory(body_accessory_choice)
            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old


    # else:

        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hide_transitions = False #activates dissolve in her_main
            # $ hermione_xpos = 665

            # m "[hermione_name]..."

            # #S.P.E.W Basge
            # if body_accessory_choice == "badge_spew":
                # m "Could you remove that Spew badge again?"
                # call her_main("Alright. Let me take it off.", "annoyed", "narrow", "worried", "down")

            # #I <3 Cum Badge
            # if body_accessory_choice == "badge_cum":
                # m "Could you remove that Cum badge again?"
                # call her_main("Alright. Let me take it off.", "annoyed", "narrow", "worried", "down")

            # hide screen hermione_main
            # with d3

            # pause.5

            # call set_her_body_accessory(body_accessory_choice) #Removes Item

            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else:

            # $ hide_transitions = True
            # call set_her_body_accessory(body_accessory_choice) #Removes Item
            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old

### Stockings Equip ###
label equip_stockings:
    #Susan
    if active_girl == "susan":
        jump equip_sus_stockings

### Equip Susan's Stockings ###
label equip_sus_stockings:
    call set_sus_stockings(stockings_choice)

    jump return_to_wardrobe


### Robe Equip ###
label equip_robe:
    #Susan
    if active_girl == "susan":
        jump equip_sus_robe

### Equip Susan's Robe ###
label equip_sus_robe:
    call set_sus_robe(robe_choice)

    jump return_to_wardrobe
