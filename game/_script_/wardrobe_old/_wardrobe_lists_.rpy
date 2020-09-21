
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

    return


### Hair & Head Accessories List ###
label update_wr_head_list:

    $ wr_hair = []
    $ wr_makeup = []
    $ wr_glasses = []
    $ wr_ears = []
    $ wr_hats = []

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

    return
