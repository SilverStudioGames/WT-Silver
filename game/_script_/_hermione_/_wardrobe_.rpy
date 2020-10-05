###############
## Character ##
###############

default hermione = Doll(name="hermione",
                        clothes={"headgear":   [None, 15, True],
                                 "hair":       [None, 4, True],
                                 "glasses":    [None, 12, True],
                                 "earrings":   [None, 14, True],
                                 "neckwear":   [None, 16, True],
                                 "robe":       [None, 22, True],
                                 "gloves":     [None, 14, True],
                                 "top":        [None, 15, True],
                                 "bra":        [None, 9, True],
                                 "bottom":     [None, 8, True],
                                 "garterbelt": [None, 7, True],
                                 "panties":    [None, 6, True],
                                 "stockings":  [None, 5, True],
                                 "buttplug":   [None, -1, True],
                                 "pubes":      [None, 3, True],
                                 "tattoo0":    [None, 1, True],
                                 "tattoo1":    [None, 1, True],
                                 "tattoo2":    [None, 1, True],
                                 "tattoo3":    [None, 1, True],
                                 "tattoo4":    [None, 1, True],
                                 "piercing0":  [None, 2, True],
                                 "piercing1":  [None, 2, True],
                                 "piercing2":  [None, 2, True],
                                 "piercing3":  [None, 2, True],
                                 "piercing4":  [None, 2, True],
                                 "accessory0": [None, 12, True],
                                 "accessory1": [None, 12, True],
                                 "accessory2": [None, 12, True],
                                 "accessory3": [None, 12, True],
                                 "accessory4": [None, 12, True],
                                 "makeup0":    [None, 3, True],
                                 "makeup1":    [None, 3, True],
                                 "makeup2":    [None, 3, True],
                                 "makeup3":    [None, 3, True],
                                 "makeup4":    [None, 3, True]},
                        face={"tears":    [None, 12, True],
                              "cheeks":   [None, 7, True],
                              "eyebrows": ["base", 11, True],
                              "eyes":     ["base", 8, True],
                              "pupils":   ["mid", 9, True],
                              "mouth":    ["base", 13, True]},
                        body={"armleft": ["down", 3],
                              "armright":["down", 0],
                              "base":    ["front", 1],
                              "breasts": ["normal", 2]})

###############
##   Hair    ##
###############

default her_hair_base = DollCloth("hermione", ("head", "hair"), "hair", "base", [[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]], unlocked=True)

################
## Schoolgirl ##
################

default her_top_school1 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school2 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_2", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school3 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_3", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school4 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_4", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=4)
default her_top_school5 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_5", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
default her_top_school6 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_6", [[109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
default her_top_school7 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_7", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=13)
default her_bottom_school1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True)
default her_bottom_school2 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=4)
default her_bottom_school3 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=10)
default her_bottom_school4 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=19)
default her_stockings_base1 = DollCloth("hermione", ("legwear", "socks"), "stockings", "stockings_1", [[219, 165, 13, 255], [146, 63, 30, 255]], unlocked=True)
default her_panties_base1 = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "basic_panties_1", [[232, 232, 232, 255], [202, 60, 1, 255]], unlocked=True)
default her_bra_base1 = DollCloth("hermione", ("upper undergarment", "bras"), "bra", "basic_bra_1", [[232, 232, 232, 255], [202, 60, 1, 255]], unlocked=True)
default her_robe_school_1 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_1", [[96, 96, 96, 255], [206, 206, 209, 255], [167, 77, 42, 255]], unlocked=True, level=0)
default her_robe_school_2 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_2", [[96, 96, 96, 255], [206, 206, 209, 255], [167, 77, 42, 255]], unlocked=True, level=4)
default her_robe_school_3 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_3", [[96, 96, 96, 255], [206, 206, 209, 255], [167, 77, 42, 255]], unlocked=True, level=10)
default her_robe_school_4 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_4", [[96, 96, 96, 255], [206, 206, 209, 255], [167, 77, 42, 255]], unlocked=True, level=13)

default her_accessory_house_emblem = DollCloth("hermione", ("misc", "accessory"), "accessory0", "house_emblem", [[167, 77, 42, 255], [237, 179, 14, 255]], zorder=16, unlocked=True)
default her_accessory4_reading_glasses = DollCloth("hermione", ("head", "glasses"), "glasses", "reading_glasses", [[240, 240, 241, 255]], unlocked=True)
default her_accessory4_vintage_glasses = DollCloth("hermione", ("head", "glasses"), "glasses", "vintage_glasses", [[255, 255, 255, 50], [36, 36, 36, 255], [116, 116, 116, 255]], unlocked=True, zorder=3)

default her_outfit_default = DollOutfit([her_hair_base, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True)
default her_outfit_default_no_vest = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1])
default her_outfit_default_no_tie_open_shirt = DollOutfit([her_hair_base, her_top_school5, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1])
default her_outfit_last = DollOutfit([her_hair_base])

###########################
## Leather Bikini Outfit ##
###########################
default her_panties_bikini1 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1", [[138, 0, 0, 255], [252, 135, 0, 255]], level=19)
default her_bra_bikini1 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1", [[138, 0, 0, 255], [252, 135, 0, 255]], level=19)

default her_outfit_bikini1 = DollOutfit([her_hair_base, her_panties_bikini1, her_bra_bikini1], price=350)

########################
## Rave Bikini Outfit ##
########################

default her_panties_bikini2 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_2", [[55, 55, 55, 255], [197, 142, 35, 255]], level=19)
default her_bra_bikini2 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_2", [[55, 55, 55, 255], [197, 142, 35, 255]], level=19)

default her_outfit_bikini2 = DollOutfit([her_hair_base, her_panties_bikini2, her_bra_bikini2], price=350)

#########################
## Sling Bikini Outfit ##
#########################
default her_panties_bikini3 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "sling_panties", [[48, 69, 164, 255], [212, 164, 32, 255]], level=19)
default her_bra_bikini3 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "sling_bra", [[48, 69, 164, 255], [212, 164, 32, 255]], level=19)

default her_outfit_bikini3 = DollOutfit([her_hair_base, her_panties_bikini3, her_bra_bikini3], price=350)

#################
## Maid Outfit ##
#################

default her_top_maid1 = DollCloth("hermione", ("upper body", "dresses"), "top", "maid_dress_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]], level=4)
default her_stockings_maid1 = DollCloth("hermione", ("legwear", "socks"), "stockings", "maid_stockings_1", [[53, 33, 30, 255]], level=4)
default her_hat_maid1 = DollCloth("hermione", ("head", "headgear"), "headgear", "maid_hat_1", [[236, 243, 244, 255]], level=4)
default her_neckwear_maid1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_1", [[40, 51, 61, 255], [236, 243, 244, 255]], level=4)
default her_neckwear_maid2 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_2", [[236, 243, 244, 255]], level=4)
default her_gloves_maid1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "maid_gloves_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]], level=4)

default her_outfit_maid = DollOutfit([her_hair_base, her_top_maid1, her_stockings_maid1, her_hat_maid1, her_neckwear_maid1, her_neckwear_maid2, her_gloves_maid1], price=450)

##################
## Poker Outfit ##
##################

default her_hat_poker1 = DollCloth("hermione", ("head", "headgear"), "headgear", "poker_hat_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]], level=4)
default her_hat_poker2 = DollCloth("hermione", ("head", "headgear"), "headgear", "poker_hat_2", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]], level=4)
default her_neckwear_poker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "poker_bowtie_1", [[232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]], level=4)
default her_stockings_poker1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_1", [[26, 26, 35, 255], [153, 22, 10, 255]], level=13)
default her_stockings_poker2 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_2", [[26, 26, 35, 255], [153, 22, 10, 255]], level=13)
default her_panties_poker1 = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "poker_panties_1", [[26, 26, 35, 255], [153, 22, 10, 255], [255, 179, 3, 255]], level=19)
default her_bra_poker1 = DollCloth("hermione", ("upper undergarment", "other"), "bra", "poker_bra_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]], blacklist=["panties", "top", "bottom"], level=19)
default her_gloves_poker1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "poker_gloves_1", [[232, 232, 232, 255], [255, 179, 3, 255]], level=4)
default her_earring_poker1 = DollCloth("hermione", ("head", "earrings"), "earrings", "poker_earring_1", [[255, 179, 3, 255]], level=4)
default her_piercing2_poker1 = DollCloth("hermione", ("lower undergarment", "piercing"), "piercing2", "poker_belly_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]])

default her_outfit_poker = DollOutfit([her_hair_base, her_hat_poker1, her_hat_poker2, her_neckwear_poker1, her_stockings_poker1, her_stockings_poker2, her_panties_poker1, her_bra_poker1, her_gloves_poker1, her_earring_poker1, her_piercing2_poker1], price=450)

##################
## Bunny Outfit ##
##################

default her_top_bunny1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "bunny_top_1", [[48, 48, 48, 255]], blacklist=["panties", "bra"], zorder=7, level=19)
default her_stockings_bunny1 = DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", [[81, 81, 81, 255]], level=19)
default her_tattoo3_bunny1 = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo3", "bunny_tattoo1", [[0, 0, 1, 255]])
default her_hat_bunny1 = DollCloth("hermione", ("head", "headgear"), "headgear", "bunny_hat_1", [[48, 48, 48, 255], [232, 232, 232, 255]], level=13)
default her_gloves_bunny1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "bunny_gloves_1", [[232, 232, 232, 255]], level=4)
default her_neckwear_bunny1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", [[232, 232, 232, 255], [48, 48, 48, 255]], level=4)

default her_outfit_bunny = DollOutfit([her_hair_base, her_top_bunny1, her_stockings_bunny1, her_tattoo3_bunny1, her_hat_bunny1, her_gloves_bunny1, her_neckwear_bunny1], price=350)

################
## Ball Dress ##
################

default her_hair_updo = DollCloth("hermione", ("head", "hair"), "hair", "updo", [[152, 89, 48, 255], [195, 137, 89, 255]])
default her_top_ball1 = DollCloth("hermione", ("upper body", "dresses"), "top", "ball_dress_1", [[255, 140, 174, 255], [242, 218, 255, 255]], blacklist=["bottom"])
default her_earring_pearls1 = DollCloth("hermione", ("head", "earrings"), "earrings", "pearl_1", [[233, 166, 253, 255]], level=4)
default her_neckwear_pearls1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "ball_pearls_1", [[233, 166, 253, 255]], level=4)
default her_accessory_ball_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "ball_sash", [[247, 222, 231, 255], [161, 82, 159, 255]], zorder=16, level=4)

default her_outfit_ball = DollOutfit([her_hair_updo, her_neckwear_pearls1, her_top_ball1, her_earring_pearls1, her_accessory_ball_sash1], price=1000)

#####################
## Yennefer Outfit ##
#####################

default her_top_yen1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "yen_top", [[9, 32, 47, 255]], level=10)
default her_bottom_yen_skirt1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "yen_skirt", [[26, 26, 26, 255]], level=4)
default her_stockings_yen1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "yen_stockings", [[76, 76, 76, 255]], level=10)
default her_accessory_yen_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "yen_sash", [[25, 25, 25, 255], [51, 51, 51, 255]], zorder=9, level=13)
default her_accessory_yen_belt1 = DollCloth("hermione", ("misc", "accessory"), "accessory3", "yen_belt", [[52, 37, 31, 255], [146, 142, 137, 255]], zorder=10, level=4)
default her_accessory_yen_feathers1 = DollCloth("hermione", ("misc", "accessory"), "accessory2", "yen_feathers", [[42, 190, 199, 255]], zorder=16, level=4)
default her_accessory_yen_scarf1 = DollCloth("hermione", ("misc", "accessory"), "accessory1", "yen_scarf", [[9, 32, 47, 255]], zorder=17, level=4)
default her_accessory_yen_corset1 = DollCloth("hermione", ("misc", "accessory"), "accessory0", "yen_corset", [[37, 27, 27, 255], [19, 14, 11, 255]], zorder=16, level=10)
default her_neckwear_yen_choker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "yen_choker", [[30, 29, 28, 255]], level=4)
default her_gloves_yen1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "yen_gloves", [[52, 37, 31, 255]], zorder=16, level=4)

default her_outfit_yennefer = DollOutfit([her_hair_base, her_top_yen1, her_bottom_yen_skirt1, her_accessory_yen_sash1, her_stockings_yen1, her_accessory_yen_feathers1, her_accessory_yen_scarf1, her_neckwear_yen_choker1, her_gloves_yen1, her_accessory_yen_corset1, her_accessory_yen_belt1], price=400)

#######################
## Pizza Slut Outfit ##
#######################

default her_bottom_pizza = DollCloth("hermione", ("lower body", "skirts"), "bottom", "pizza_skirt", [[180, 50, 10, 255], [235, 199, 44, 255]], level=4)
default her_top_pizza = DollCloth("hermione", ("upper body", "other"), "top", "pizza_top", [[180, 50, 10, 255]], level=19)
default her_panties_pizza = DollCloth("hermione", ("lower undergarment", "other"), "panties", "pizza_panties", [[180, 50, 10, 255]], level=19)

default her_outfit_pizza = DollOutfit([her_hair_base, her_bottom_pizza, her_top_pizza, her_panties_pizza])

#####################
## Bioshock Outfit ##
#####################

default her_hair_bioshock = DollCloth("hermione", ("head", "hair"), "hair", "bio_hair", [[31, 29, 27, 255], [54, 50, 48, 255]], level=4)
default her_bottom_bioshock = DollCloth("hermione", ("lower body", "skirts"), "bottom", "bioshock_skirt", [[12, 1, 72, 255]], level=4)
default her_top_bioshock = DollCloth("hermione", ("upper body", "other"), "top", "bioshock_corset", [[225, 224, 232, 255], [46, 46, 48, 255], [232, 232, 232, 255]], level=4)
default her_neckwear_bioshock = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bioshock_choker", [[12, 1, 72, 255]], level=4)
default her_robe_bioshock = DollCloth("hermione", ("upper body", "robes"), "robe", "bioshock_robe", [[12, 1, 72, 255], [232, 232, 232, 255]], level=4)

default her_outfit_bioshock = DollOutfit([her_hair_bioshock, her_robe_bioshock, her_bottom_bioshock, her_top_bioshock, her_neckwear_bioshock], price=400)

##############
## Swimsuit ##
##############

default her_top_swimsuit_1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "swimsuit_top_1", [[22, 27, 48, 255], [224, 198, 16, 255]], blacklist=["panties", "bra"], zorder=7, level=13)

default her_outfit_swimsuit = DollOutfit([her_hair_base, her_top_swimsuit_1], price=350)

#####################
## Egyptian Outfit ##
#####################

default her_top_egypt = DollCloth("hermione", ("upper body", "other"), "top", "egypt_top", [[240, 237, 250, 255]], blacklist=["bra"], level=19)
default her_bottom_egypt = DollCloth("hermione", ("lower body", "other"), "bottom", "egypt_loincloth", [[240, 237, 250, 255], [227, 182, 101, 255], [47, 151, 255, 255]], blacklist=["panties"], level=13)
default her_gloves_egypt = DollCloth("hermione", ("upper body", "gloves"), "gloves", "egypt_armband", [[227, 182, 101, 255]], level=4)
default her_neckwear_egypt = DollCloth("hermione", ("head", "neckwear"), "neckwear", "egypt_neck", [[227, 182, 101, 255], [94, 209, 236, 255], [47, 151, 255, 255]], level=4)

default her_outfit_egypt = DollOutfit([her_hair_base, her_neckwear_egypt, her_top_egypt, her_bottom_egypt, her_gloves_egypt], price=400)

#######################
## Latex dress Outfit ##
#######################

default her_top_latex_dress_1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "latex_dress_1", [[250, 139, 241, 255], [255, 173, 22, 255]], blacklist=["bra"], level=19)

default her_outfit_latex_dress = DollOutfit([her_hair_base, her_top_latex_dress_1], price=350)

####################
## Nightie Outfit ##
####################

default her_top_nightie = DollCloth("hermione", ("upper body", "shirts"), "top", "nightie", [[255, 172, 184, 215]], level=13)

default her_outfit_nightie = DollOutfit([her_hair_base, her_top_nightie], price=350)

##################
## Teddy Outfit ##
##################

default her_top_teddy = DollCloth("hermione", ("upper body", "shirts"), "top", "teddy_top", [[20, 20, 20, 215], [148, 144, 163, 215], [148, 144, 163, 215]], level=16)

default her_outfit_teddy = DollOutfit([her_hair_base, her_top_teddy], price=350)

#################
## Tifa Outfit ##
#################

default her_top_tifa = DollCloth("hermione", ("upper body", "shirts"), "top", "tifa_top", [[232, 232, 232, 255]], level=10)
default her_accessory_tifa_belt = DollCloth("hermione", ("misc", "accessory"), "accessory3", "tifa_belt", [[50, 50, 50, 255], [154, 154, 154, 255]], level=4)
default her_accessory_tifa_suspenders = DollCloth("hermione", ("misc", "accessory"), "accessory4", "tifa_suspenders", [[86, 61, 67, 255], [154, 154, 154, 255]], zorder=16, level=4)
default her_gloves_tifa = DollCloth("hermione", ("upper body", "gloves"), "gloves", "tifa_gloves", [[72, 63, 70, 255], [228, 107, 98, 255], [125, 120, 127, 255], [189, 167, 158, 255]], level=4)
default her_bottom_tifa = DollCloth("hermione", ("lower body", "skirts"), "bottom", "tifa_skirt", [[72, 63, 70, 255]], level=10)

default her_outfit_tifa = DollOutfit([her_hair_base, her_top_tifa, her_accessory_tifa_belt, her_accessory_tifa_suspenders, her_gloves_tifa, her_bottom_tifa], price=400)

#######################
## Ms. Marvel Outfit ##
#######################

default her_top_msmarv = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "msmarv_suit", [[64, 70, 99, 255], [123, 136, 181, 255], [255, 236, 134, 255]], zorder=7, blacklist=["panties", "bra"], level=10)
default her_accessory_msmarv_ribbon = DollCloth("hermione", ("misc", "accessory"), "accessory3", "msmarv_ribbon", [[206, 41, 22, 255]], level=4)
default her_gloves_msmarv = DollCloth("hermione", ("upper body", "gloves"), "gloves", "msmarv_gloves", [[64, 70, 99, 255], [123, 136, 181, 255]], level=4)
default her_stockings_msmarv = DollCloth("hermione", ("legwear", "stockings"), "stockings", "msmarv_stockings", [[64, 70, 99, 255], [123, 136, 181, 255]], level=10)

default her_outfit_msmarv = DollOutfit([her_hair_base, her_top_msmarv, her_accessory_msmarv_ribbon, her_gloves_msmarv, her_stockings_msmarv], price=400)

#######################
## Heart Slut Outfit ##
#######################

default her_top_hslut = DollCloth("hermione", ("upper body", "other"), "top", "hslut_top", [[226, 95, 95, 255], [242, 242, 242, 255]], level=19)
default her_gloves_hslut = DollCloth("hermione", ("upper body", "gloves"), "gloves", "hslut_gloves", [[242, 242, 242, 255]], level=10)
default her_stockings_hslut = DollCloth("hermione", ("legwear", "stockings"), "stockings", "hslut_socks", [[242, 242, 242, 255]], level=10)
default her_panties_hslut = DollCloth("hermione", ("lower undergarment", "other"), "panties", "hslut_panties", [[226, 95, 95, 255]], level=19)
default her_bra_hslut = DollCloth("hermione", ("upper undergarment", "other"), "bra", "hslut_pasties", [[226, 95, 95, 255], [226, 95, 95, 255]], level=19)
default her_earring_hslut = DollCloth("hermione", ("head", "earrings"), "earrings", "hslut_earring", [[226, 95, 95, 255]], level=4)
default her_neckwear_hslut = DollCloth("hermione", ("head", "neckwear"), "neckwear", "hslut_choker", [[242, 242, 242, 255], [226, 95, 95, 255]], level=10)
default her_garterbelt_hslut = DollCloth("hermione", ("legwear", "garterbelts"), "garterbelt", "hslut_garter", [[226, 95, 95, 255], [249, 148, 148, 255]], level=10)

default her_outfit_hslut = DollOutfit([her_hair_base, her_top_hslut, her_gloves_hslut, her_stockings_hslut, her_panties_hslut, her_bra_hslut, her_earring_hslut, her_neckwear_hslut, her_garterbelt_hslut], price=450)

#######################
## Lara Croft Outfit ##
#######################

default her_top_croft = DollCloth("hermione", ("upper body", "shirts"), "top", "croft_top", [[163, 201, 152, 255]], level=10)
default her_bottom_croft = DollCloth("hermione", ("lower body", "shorts"), "bottom", "croft_shorts", [[147, 114, 61, 255], [137, 136, 120, 255], [252, 192, 4, 255]],level=10)
default her_accessory_croft_belt = DollCloth("hermione", ("misc", "accessory"), "accessory3", "croft_belt", [[111, 86, 66, 255], [116, 123, 114, 255], [252, 192, 4, 255]], level=4)
default her_accessory_croft_suspenders = DollCloth("hermione", ("misc", "accessory"), "accessory4", "croft_suspenders", [[111, 86, 66, 255], [116, 123, 114, 255]], zorder=16, level=4)

default her_outfit_croft = DollOutfit([her_hair_base, her_top_croft, her_bottom_croft, her_accessory_croft_belt, her_accessory_croft_suspenders], price=400)

##################
## Witch Outfit ##
##################

default her_top_witch = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "witch_top", [[71, 51, 102, 255], [252, 180, 112, 255]], blacklist=["panties"], level=10)
default her_stockings_witch = DollCloth("hermione", ("legwear", "stockings"), "stockings", "witch_stockings", [[71, 51, 102, 255], [252, 180, 112, 255]], level=4)
default her_robe_witch = DollCloth("hermione", ("upper body", "robes"), "robe", "witch_cape", [[71, 51, 102, 255], [252, 180, 112, 255], [36, 112, 58, 255]], level=4)

default her_outfit_witch = DollOutfit([her_hair_base, her_top_witch, her_stockings_witch, her_robe_witch], price=400)

#######################
## Slutty Schoolgirl ##
#######################

default her_top_slutty1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "open_top_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], level=19)
default her_bottom_slutty1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "open_skirt_1", [[103, 90, 108, 255]], level=19)
default her_stockings_slutty = DollCloth("hermione", ("legwear", "stockings"), "stockings", "stockings_2", [[170, 170, 170, 255]], level=4)

default her_outfit_slutty_schoolgirl = DollOutfit([her_hair_base, her_top_slutty1, her_bottom_slutty1, her_stockings_slutty], price=500)

##################
## Latex Outfit ##
##################

default her_top_latex = DollCloth("hermione", ("upper body", "shirts"), "top", "latex_top", [[55, 55, 55, 255]], level=19)
default her_gloves_latex = DollCloth("hermione", ("upper body", "gloves"), "gloves", "latex_gloves", [[55, 55, 55, 255]], level=10)
default her_stockings_latex = DollCloth("hermione", ("legwear", "stockings"), "stockings", "latex_stockings", [[55, 55, 55, 255]], level=10)
default her_panties_latex = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "latex_panties", [[55, 55, 55, 255]], level=13)
default her_neckwear_latex = DollCloth("hermione", ("head", "neckwear"), "neckwear", "latex_choker", [[55, 55, 55, 255]], level=13)

default her_outfit_latex = DollOutfit([her_hair_base, her_top_latex, her_gloves_latex, her_stockings_latex, her_panties_latex, her_neckwear_latex], price=350)

#################
## Fishnet Outfit
#################

default her_top_fishnet = DollCloth("hermione", ("upper body", "other"), "top", "fishnet_top", [[24, 24, 24, 255]], blacklist=["bra"], level=19)
default her_panties_fishnet = DollCloth("hermione", ("lower undergarment", "other"), "panties", "fishnet_panties", [[24, 24, 24, 255]], level=19)

default her_outfit_fishnet = DollOutfit([her_hair_base, her_top_fishnet, her_panties_fishnet], price=350)

###################
## Winter Outfit ## (Unfinished) # TODO: Add to clothing event once it's been finished.
###################

default her_top_pullover_1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_1", [[255, 123, 207, 255]], unlocked=True)
default her_top_pullover_2 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_2", [[255, 123, 207, 255]], unlocked=True, level=8)
default her_top_pullover_3 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_3", [[255, 123, 207, 255]], unlocked=True, level=16)
default her_bottom_winter_1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "winter_skirt_1", [[192, 31, 30, 255]])
default her_stockings_pantyhose_1= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_1", [[177, 144, 131, 255]], unlocked=True, level=4)
default her_stockings_pantyhose_2= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_2", [[177, 144, 131, 255]], unlocked=True, level=10)
default her_stockings_pantyhose_3= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_3", [[177, 144, 131, 255]], unlocked=True, level=19)

default her_outfit_winter = DollOutfit([her_hair_base, her_top_pullover_1, her_bottom_winter_1, her_stockings_pantyhose_1])

###################
## Spring Outfit ##
###################

default her_top_ruffled = DollCloth("hermione", ("upper body", "shirts"), "top", "ruffled_top", [[235, 223, 163, 255]], unlocked=True, level=4)
default her_bottom_jeans = DollCloth("hermione", ("lower body", "trousers"), "bottom", "jeans_1", [[64, 87, 88, 255], [174, 93, 11, 255], [155, 142, 130, 255]], unlocked=True)

default her_outfit_spring = DollOutfit([her_hair_base, her_top_ruffled, her_bottom_jeans])

###################
## Casual Outfit ## TODO: Turn into clothing event once it's been finished.
###################

default her_top_casual1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "casual_top_1", [[116, 18, 48, 255], [60, 111, 66, 255]], unlocked=True)
default her_top_casual2 = DollCloth("hermione", ("upper body", "sweaters"), "top", "casual_top_2", [[116, 18, 48, 255]], unlocked=True, level=6)

default her_outfit_casual = DollOutfit([her_hair_base, her_top_casual1])

########################
## Cheerleader Outfit ##
########################

default her_top_cheerleader1 = DollCloth("hermione", ("upper body", "shirts"), "top", "cheerleader_top_1", [[251, 251, 251, 255], [167, 77, 42, 255], [237, 179, 14, 255]], level=10)
default her_top_cheerleader2 = DollCloth("hermione", ("upper body", "other"), "top", "cheerleader_top_2", [[167, 77, 42, 255], [237, 179, 14, 255]], level=16)

default her_bottom_cheerleader1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "cheerleader_skirt_1", [[251, 251, 251, 255], [167, 77, 42, 255], [237, 179, 14, 255]], level=10)
default her_bottom_cheerleader2 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "cheerleader_skirt_2", [[232, 232, 232, 255], [167, 77, 42, 255], [237, 179, 14, 255]], level=14)

default her_gloves_cheerleader = DollCloth("hermione", ("upper body", "gloves"), "gloves", "cheerleader_armband", [[167, 77, 42, 255], [237, 179, 14, 255]])

default her_outfit_cheerleader_1 = DollOutfit([her_hair_base, her_top_cheerleader1, her_bottom_cheerleader1, her_gloves_cheerleader], price=450)
default her_outfit_cheerleader_2 = DollOutfit([her_hair_base, her_top_cheerleader2, her_bottom_cheerleader2], price=650)

##########
## MISC ##
##########

default her_accessory_gift_wrap = DollCloth("hermione", ("misc", "accessory"), "accessory3", "leg_wrap", [[167, 77, 42, 255], [237, 179, 14, 255]], zorder=7, unlocked=True, level=4)
default her_bra_bandaids = DollCloth("hermione", ("upper undergarment", "other"), "bra", "bandaids", [[233, 187, 149, 255]], unlocked=True, level=19)

#############
## Tattoos ##
#############

# Pelvis/crotch (Slot 0)
default her_tattoo0_10g = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "10g_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_cockhole = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "cockhole_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_cumhere = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "cumhere_tattoo2", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_cumslut = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "cumslut_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_cunt = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "cunt_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_deatheater = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "deatheater_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_deposit = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "deposit_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_fuckme = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "fuckme_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_mudblood = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "mudblood_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_nocondom = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "nocondom_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_punkblood = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "punkblood_tattoo", [[192, 84, 58, 255], [68, 188, 64, 255]], unlocked=True)
default her_tattoo0_whore = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "whore_tattoo", [[0, 0, 0, 255]], unlocked=True)
default her_tattoo0_womb = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo0", "womb_tattoo", [[0, 0, 0, 255]], unlocked=True)

# Breasts/Nipples (Slot 1)
default her_tattoo1_twist = DollCloth("hermione", ("upper undergarment", "tattoos"), "tattoo1", "twist_tattoo", [[0, 0, 0, 255]], unlocked=True)

# Torso/chest (Slot 2)
default her_tattoo2_cumhere = DollCloth("hermione", ("upper undergarment", "tattoos"), "tattoo2", "cumhere_tattoo1", [[0, 0, 0, 255]], unlocked=True)

# Legs/Thighs (Slot 3)
default her_tattoo3_lockhart = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo3", "lockhart_tattoo", [[70, 70, 70, 255]])
default her_tattoo3_free = DollCloth("hermione", ("lower undergarment", "tattoos"), "tattoo3", "free_tattoo", [[0, 0, 0, 255]], unlocked=True)

############
## Makeup ##
############

# Face (Slot 0)
default her_makeup0_freckles = DollCloth("hermione", ("head", "makeup"), "makeup0", "freckles1", [[185, 124, 81, 255]], unlocked=True)
default her_makeup0_freckles_nonose = DollCloth("hermione", ("head", "makeup"), "makeup0", "freckles1_nonose", [[185, 124, 81, 255]], unlocked=True)

# Breasts
default her_makeup1_freckles = DollCloth("hermione", ("head", "makeup"), "makeup1", "freckles2", [[185, 124, 81, 255]], unlocked=True)

# Torso
default her_makeup2_freckles = DollCloth("hermione", ("head", "makeup"), "makeup2", "freckles3", [[185, 124, 81, 255]], unlocked=True)

# Lipstick (DollLipstick)
default her_makeup4_lipstick = DollLipstick("hermione", ("head", "makeup"), "makeup4", "lipstick", [[255, 70, 70, 255]], unlocked=True)

################
## Pubic Hair ##
################

default her_pubes_arrow = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "arrow", [[152, 89, 48, 255]], unlocked=True)
default her_pubes_beaver = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "beaver", [[152, 89, 48, 255]], unlocked=True)
default her_pubes_stuble = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "stuble", [[92, 54, 29, 255]], unlocked=True)
default her_pubes_unshaved = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "unshaved", [[92, 54, 29, 255]], unlocked=True)


default her_top_school11 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school12 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school13 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school14 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school15 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school16 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school17 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school18 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school19 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school20 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school21 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school22 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school23 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school24 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school25 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school26 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school27 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school28 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school29 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school30 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school31 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school32 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school33 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school34 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school35 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school36 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school37 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school38 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school39 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school40 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
