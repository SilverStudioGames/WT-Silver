
# Todo : Change all ".purchase" from the outfit_OBJ to ".unlocked"
label update_wr_lists:
    call update_wr_color_list
    call update_wr_head_list
    call update_wr_tops_list
    call update_wr_bottoms_list
    call update_wr_other_clothings_list
    call update_wr_miscellaneous_list
    call update_wr_underwear_list
    call update_wr_outfits_list
    return


### Color List ###
label update_wr_color_list:

    #Hair Color
    $ wr_haircolor = []

    #House Color
    $ wr_housecolor = []


    #Cloth Color
    $ wr_clothcolor = []

    if active_girl in ["luna"]:
        $ wr_clothcolor.append("dark_blue")
        $ wr_clothcolor.append("dark_green")
        $ wr_clothcolor.append("crimson")
        $ wr_clothcolor.append("orange")
        $ wr_clothcolor.append("purple")
        $ wr_clothcolor.append("brown")
        $ wr_clothcolor.append("black")

        $ wr_clothcolor.append("blue")
        $ wr_clothcolor.append("green")
        $ wr_clothcolor.append("red")
        $ wr_clothcolor.append("yellow")
        $ wr_clothcolor.append("pink")
        $ wr_clothcolor.append("gray")
        $ wr_clothcolor.append("white")

    return


### Hair & Head Accessories List ###
label update_wr_head_list:

    $ wr_hair = []
    $ wr_makeup = []
    $ wr_glasses = []
    $ wr_ears = []
    $ wr_hats = []

    if active_girl == "luna":

        #Hair
        $ wr_hair.append("curly")
        $ wr_hair.append("playful")
        $ wr_hair.append("short")

        if luna_reverted:
            $ wr_glasses.append("spectrespecs")

        #Hats
        if ll_stewardess_ITEM.unlocked or ll_stewardess_short_ITEM.unlocked:
            $ wr_hats.append("hat_stewardess")

    if active_girl == "susan":

        $ wr_hair.append("braided")

    return


### Tops List ###
label update_wr_tops_list:

    $ wr_tops_uniform = [] #ADD school clothing and cheerleader tops...
    $ wr_tops_cheerleader = []  #Cheerleader Tops
    $ wr_tops_normal = []  #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    $ wr_tops_wicked = []  #ADD kinky clothing items like leather, fishnet
    $ wr_tops_misc = []    #ADD Misc top items

    if active_girl == "luna":

        #Uniform
        $ wr_tops_uniform.append("top_1_r")
        $ wr_tops_uniform.append("top_2_r")
        $ wr_tops_uniform.append("top_3_r")

        if not luna_reverted:
            $ wr_tops_uniform.append("top_1_s")
            $ wr_tops_uniform.append("top_2_s")

        #Cheerleader
        if ll_cheer_r_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_r")

        #Muggle
        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_tops_normal.append("top_muggle_1")
            $ wr_tops_normal.append("top_muggle_2")
            $ wr_tops_normal.append("top_muggle_3")

    if active_girl == "susan":

        #Uniform
        $ wr_tops_uniform.append("top_1")
        $ wr_tops_uniform.append("top_2")
        $ wr_tops_uniform.append("top_3")
        $ wr_tops_uniform.append("top_4")
        $ wr_tops_uniform.append("top_5")

    return


### Bottoms List ###
label update_wr_bottoms_list:

    $ wr_bottoms_uniform = []
    $ wr_bottoms_cheerleader = []  #Add low hanging school skirts
    $ wr_bottoms_skirts = []       #Add skirts
    $ wr_bottoms_pants = []        #Add
    $ wr_bottoms_misc = []         #ADD Misc bottom items

    if active_girl == "luna":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")
        $ wr_bottoms_uniform.append("skirt_3")
        $ wr_bottoms_uniform.append("skirt_4")
        $ wr_bottoms_uniform.append("skirt_5")

        $ wr_bottoms_uniform.append("skirt_1_low")
        $ wr_bottoms_uniform.append("skirt_2_low")
        $ wr_bottoms_uniform.append("skirt_3_low")
        $ wr_bottoms_uniform.append("skirt_4_low")

        #Cheerleader
        if ll_cheer_r_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_r")

        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_bottoms_skirts.append("skirt_muggle_1")

    if active_girl == "susan":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")

    return


### Other Clothings List ###
label update_wr_other_clothings_list:

    $ wr_neckwears = []
    $ wr_body_accs = []
    $ wr_gloves = []
    $ wr_stockings = []
    $ wr_robes = []

    if active_girl == "luna":

        #Neck
        if ll_stewardess_ITEM.unlocked or ll_stewardess_short_ITEM.unlocked:
            $ wr_neckwears.append("cloth_tie")

        #Stockings
        if ll_cheer_r_ITEM.unlocked:
            $ wr_stockings.append("stockings_cheer_r")
        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_stockings.append("stockings_muggle_1")
        if ll_dress_orange_ITEM.unlocked:
            $ wr_stockings.append("leggings_1")

    if active_girl == "susan":

        $ wr_neckwears.append("choker_base")

        $ wr_stockings.append("stockings_base")
        $ wr_stockings.append("stockings_lace")
        $ wr_stockings.append("stockings_rose")

    return


### Underwear List ###
label update_wr_underwear_list:

    $ wr_bras = []
    $ wr_panties = []
    $ wr_onepieces = []
    $ wr_garterbelts = []

    if active_girl == "luna":

        #Bras
        $ wr_bras.append("bra_basic")
        if ll_lingerie_silk_ITEM.unlocked:
            $ wr_bras.append("bra_silk")

        #Panties
        $ wr_panties.append("panties_basic")
        if ll_lingerie_silk_ITEM.unlocked:
            $ wr_panties.append("panties_silk")
        if ll_stewardess_ITEM.unlocked:
            $ wr_panties.append("panties_thong_1")
        if ll_stewardess_short_ITEM.unlocked:
            $ wr_panties.append("panties_thong_2")

        #One-Pieces
        $ wr_onepieces.append("nighty_long")
        $ wr_onepieces.append("nighty_long_translucent")

    if active_girl == "susan":

        #Bras
        $ wr_bras.append("bra_base")
        $ wr_bras.append("bra_lace")
        $ wr_bras.append("bra_chain")

        #Panties
        $ wr_panties.append("panties_base")
        $ wr_panties.append("panties_lace")

        #One-Pieces
        $ wr_onepieces.append("sling_1")
        $ wr_onepieces.append("sling_2")

    return


### Outfits List ###
label update_wr_outfits_list:

    $ wr_outfits = []
    $ wr_costumes = []
    $ wr_dresses = []
    $ wr_custom_outfits = []

    if active_girl == "luna":
        python:

            #Outfits
            for i in luna_outfits_list:
                if i.unlocked:
                    wr_outfits.append(i)
            #Costumes
            for i in luna_costumes_list:
                if i.unlocked:
                    wr_costumes.append(i)
            #Dresses
            for i in luna_dresses_list:
                if i.unlocked:
                    wr_dresses.append(i)

    if active_girl == "susan":
        python:

            #Outfits
            for i in susan_outfits_list:
                if i.unlocked:
                    wr_outfits.append(i)
            #Costumes
            for i in susan_costumes_list:
                if i.unlocked:
                    wr_costumes.append(i)
            #Dresses
            for i in susan_dresses_list:
                if i.unlocked:
                    wr_dresses.append(i)

    return

### Miscellaneous List ###
label update_wr_miscellaneous_list:

    $ wr_potions_list = []
    $ wr_items_list = []
    $ wr_piercings_list = []
    $ wr_tattoos_list = []

    if active_girl == "luna":
        if potion_inv.has("p_transparency"):
            $ wr_potions_list.append("clothes_potion")

    return
