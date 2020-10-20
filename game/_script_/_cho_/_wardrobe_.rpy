###############
## Character ##
###############

default cho = Doll(name="cho",
                        clothes={"headgear":   [None, 15, True],
                                 "hair":       [None, 4, True],
                                 "glasses":    [None, 12, True],
                                 "earrings":   [None, 14, True],
                                 "neckwear":   [None, 11, True],
                                 "robe":       [None, 28, True],
                                 "gloves":     [None, 21, True],
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
                              "armright":["down", 1],
                              "base":    ["front", 0],
                              "breasts": ["normal", 2]})

################
## Schoolgirl ##
################

default cho_hair_ponytail1 = DollCloth("cho", ("head", "hair"), "hair", "ponytail", [[52, 59, 80, 255], [70, 90, 147, 255]], unlocked=True)
default cho_top_school1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]], unlocked=True)
default cho_top_school2 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_2", [[183, 183, 184, 255], [109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]], level=4, unlocked=True)
default cho_top_school3 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_3", [[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]], level=8, unlocked=True)
default cho_top_school4 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_4", [[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]], level=8, unlocked=True)
default cho_top_school5 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_5", [[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]], level=12, unlocked=True)
default cho_top_school6 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_6", [[109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]], level=12, unlocked=True)
default cho_bottom_school1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, unlocked=True)
default cho_bottom_school2 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], level=4, armfix=True, unlocked=True)
default cho_bottom_school3 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], level=8, armfix=True, unlocked=True)
default cho_bottom_school4 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], level=12, armfix=True, unlocked=True)
default cho_bra_basic1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "basic_bra_1", [[230, 230, 231, 255], [89, 116, 194, 255]], unlocked=True)
default cho_panties_basic1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "basic_panties_1", [[230, 230, 231, 255], [89, 116, 194, 255]], unlocked=True)
default cho_stockings_house = DollCloth("cho", ("legwear", "socks"), "stockings", "house", [[216, 163, 10, 255], [89, 116, 194, 255]], unlocked=True)
default cho_robe_school_1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_1", color=[[96, 96, 96, 255], [206, 206, 209, 255], [89, 116, 194, 255]], level=0, unlocked=True)
default cho_robe_school_2 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_2", color=[[96, 96, 96, 255], [206, 206, 209, 255], [89, 116, 194, 255]], level=4, unlocked=True)
default cho_robe_school_3 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_3", color=[[96, 96, 96, 255], [206, 206, 209, 255], [89, 116, 194, 255]], level=8, unlocked=True)
#default cho_neckwear_tie1  = DollCloth("cho", ("head", "neckwear"), "neckwear", "tie_1", [[216, 163, 10, 255], [89, 116, 194, 255]])

default cho_outfit_last = DollOutfit([cho_hair_ponytail1])
default cho_outfit_default = DollOutfit([cho_hair_ponytail1, cho_top_school1, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_house], True)

##################
## Misty Outfit ##
##################

default cho_top_shirt1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_shirt_1", [[255, 229, 126, 255]])
default cho_bottom_shorts3 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_3", [[47, 150, 136, 255], [175, 220, 191, 255], [247, 152, 38, 255]], level=10, armfix=True)
default cho_accessory3_suspenders = DollCloth("cho", ("misc", "accessory"), "accessory3", "suspenders", [[137, 22, 17, 255], [229, 140, 33, 255]])

default cho_outfit_misty = DollOutfit([cho_hair_ponytail1, cho_accessory3_suspenders, cho_top_shirt1, cho_bottom_shorts3], price=500, name="Misty Costume", desc="For trainers that want to be the very best! To train them is your cause!")

##################
## Party Outfit ##
##################

default cho_bottom_skirt2 = DollCloth("cho", ("lower body", "skirts"), "bottom", "skirt_short_2", [[93, 119, 173, 255]], level=16, armfix=True)
default cho_bra_bikini1 = DollCloth("cho", ("upper undergarment", "bikini bras"), "bra", "bikini_top_1", [[3, 237, 234, 255]], level=10)

default cho_outfit_party = DollOutfit([cho_hair_ponytail1, cho_bottom_skirt2, cho_bra_bikini1], price=500, name="Clubslut", desc="Release your inner slut with this unique club outfit!")

###################
## Sailor Outfit ##
###################

default cho_bottom_skirt1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "skirt_short_1", [[89, 116, 194, 255]], level=18, armfix=True)
default cho_top_sailor1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_sailor_1", [[252, 252, 253, 255], [89, 116, 194, 255]], level=14)
default cho_stockings_sailor1 = DollCloth("cho", ("legwear", "stockings"), "stockings", "sailor", [[232, 232, 233, 255]])
default cho_panties_bikini2 = DollCloth("cho", ("lower undergarment", "bikini panties"), "panties", "bikini_bottom_2", [[213, 161, 13, 255]], level=18, armfix=True)

default cho_outfit_sailor = DollOutfit([cho_hair_ponytail1, cho_top_sailor1, cho_bottom_skirt1, cho_stockings_sailor1, cho_panties_bikini2], price=500, name="Sailor Outfit", desc="A slutty sailor outfit, perfect for the average cannon swabber.")

############################
## Japanese School Outfit ##
############################

default cho_top_j_school1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_j_school_1", [[255, 248, 223, 255], [95, 110, 142, 255], [161, 161, 164, 255], [253, 254, 250, 255]], level=4, armfix=True)
default cho_bottom_j_skirt1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "j_school_skirt_1", [[161, 161, 164, 255]], level=4, armfix=True)
default cho_stockings_j_kneehigh1 = DollCloth("cho", ("legwear", "socks"), "stockings", "kneehigh", [[253, 254, 250, 255]], level=0)

default cho_outfit_j_school = DollOutfit([cho_hair_ponytail1, cho_top_j_school1, cho_bottom_j_skirt1, cho_stockings_j_kneehigh1], price=300, name="Japanese School Uniform", desc="A school girl uniform inspired by the land of culture.")

###################
## Bikini Outfit ##
###################

default cho_bra_bikini2 = DollCloth("cho", ("upper undergarment", "bikini bras"), "bra", "bikini_top_2", [[89, 116, 194, 255]], level=14) #Red: [138, 22, 17, 255]
default cho_panties_bikini1 = DollCloth("cho", ("lower undergarment", "bikini panties"), "panties", "bikini_bottom_1", [[213, 161, 13, 255]], level=14, armfix=True)

default cho_outfit_bikini = DollOutfit([cho_hair_ponytail1, cho_bra_bikini2, cho_panties_bikini1], price=500, name="Micro Bikini", desc="The regular size bikinis are out of stock...")

##########################
## Lace Lingerie Outfit ##
##########################

default cho_neckwear_lace1 = DollCloth("cho", ("head", "neckwear"), "neckwear", "choker_lace_1", [[100, 100, 255, 255], [220, 220, 221, 255]])
default cho_garterbelt_lace1 = DollCloth("cho", ("legwear", "garterbelts"), "garterbelt", "lace_garter_1", [[220, 220, 221, 255], [100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]])
default cho_stockings_lace1 = DollCloth("cho", ("legwear", "stockings"), "stockings", "lace_stockings_1", [[100, 100, 255, 255], [220, 220, 221, 255]], level=12)
default cho_bra_lace1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "lace_bra_1", [[100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]], level=14)
default cho_panties_lace1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "lace_panties_1", [[100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]], level=12)
default cho_earring_feather = DollCloth("cho", ("head", "earrings"), "earrings", "feather", [[232, 232, 232, 255], [70, 90, 147, 255], [136, 91, 34, 255]])

default cho_outfit_lacelingerie = DollOutfit([cho_hair_ponytail1, cho_neckwear_lace1, cho_garterbelt_lace1, cho_panties_lace1, cho_bra_lace1, cho_stockings_lace1, cho_earring_feather], price=500, name="Lace Lingerie Set", desc="This lingerie set turns even the toughest tomboy into a cute and sexy princess!")

##################
## Dress Outfit ##
##################

default cho_top_dress1 = DollCloth("cho", ("upper body", "dresses"), "top", "dress_1", [[231, 29, 41, 255], [242, 162, 73, 255]], armfix=True, level=12, blacklist=["bottom"])

default cho_outfit_dress1 = DollOutfit([cho_hair_ponytail1, cho_top_dress1, cho_panties_basic1, cho_bra_basic1], price=500, name="Traditional Chinese Dress", desc="A traditional dress inspired by Chinese culture.")

########################
## Cheerleader Outfit ##
########################

#default cho_hair_pigtails = DollCloth("cho", ("head", "hair"), "hair", "pigtails", [[52, 59, 80, 255], [70, 90, 147, 255], [242, 162, 73, 255]], level=8)
default cho_earring_snitch = DollCloth("cho", ("head", "earrings"), "earrings", "snitch", [[220, 220, 221, 255], [213, 161, 13, 255]])
default cho_stockings_quid1 = DollCloth("cho", ("legwear", "socks"), "stockings", "quid1", [[64, 84, 141, 255], [213, 161, 13, 255]], level=10)
default cho_panties_sport2 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_2", [[156, 204, 249, 255]], level=4)
default cho_bra_sports1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "sport_bra_1", [[156, 204, 249, 255]], unlocked=True)
default cho_top_quid1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_quid_1", [[64, 84, 141, 255], [213, 161, 13, 255]], level=10)
default cho_bottom_quid1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "quid_skirt_1", [[64, 84, 141, 255], [213, 161, 13, 255]], level=10, armfix=True)
default cho_makeup0_blush = DollCloth("cho", ("makeup", "blush"), "makeup0", "blush", [[238, 113, 196, 255]], level=2)

default cho_outfit_cheerleader = DollOutfit([cho_hair_ponytail1, cho_earring_snitch, cho_stockings_quid1, cho_panties_sport2, cho_bra_sports1, cho_bottom_quid1, cho_top_quid1, cho_makeup0_blush], price=500, name="Ravenclaw Cheerleader Outfit", desc="Ravenclaw! Ravenclaw!")

####################
## Trainee Outfit ##
####################

default cho_top_tank2 = DollCloth("cho", ("upper body", "shirts"), "top", "top_tanktop_2", [[252, 192, 213, 255], [253, 221, 232, 255]], level=16)
default cho_bottom_shorts1 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_1", [[230, 230, 231, 255]], level=8, armfix=True)
default cho_stockings_pantyhose = DollCloth("cho", ("legwear", "pantyhose"), "stockings", "pantyhose", [[190, 146, 129, 255]])
default cho_earring_basic = DollCloth("cho", ("head", "earrings"), "earrings", "basic", [[220, 220, 221, 255]])

default cho_outfit_trainee = DollOutfit([cho_hair_ponytail1, cho_bra_basic1, cho_panties_basic1, cho_bottom_shorts1, cho_top_tank2, cho_stockings_pantyhose, cho_earring_basic], price=500, name="Sporty Outfit", desc="Great for reducing fat.")

###########
## Other ##
###########

default cho_panties_sport1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_1", [[156, 204, 249, 255]], unlocked=True, armfix=True)
default cho_pubes_thick = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "thick", [[52, 59, 80, 255], [70, 90, 147, 255]], unlocked=True)
default cho_pubes_heart = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "heart", [[52, 59, 80, 255], [70, 90, 147, 255]], unlocked=True)
default cho_tattoo0_free = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo0", "pelv_free", [[0, 0, 1, 255]], unlocked=True)
default cho_piercing0_stud = DollCloth("cho", ("piercings & tattoos", "piercings"), "piercing0", "stud", [[220, 220, 221, 255]], unlocked=True)
default cho_tattoo1_slut = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo1", "breasts_slut", [[0, 0, 1, 255]], unlocked=True)
default cho_piercing1_barbell = DollCloth("cho", ("piercings & tattoos", "piercings"), "piercing1", "breast_barbell", [[220, 220, 221, 255]], unlocked=True)
default cho_hat_catears = DollCloth("cho", ("head", "headgear"), "headgear", "catears", [[70, 90, 147, 255]], unlocked=True)
default cho_hat_witch = DollCloth("cho", ("head", "headgear"), "headgear", "witch", [[71, 51, 102, 255], [215, 170, 98, 255]], unlocked=True)
default cho_accessory4_glasses1 = DollCloth("cho", ("head", "glasses"), "glasses", "glasses1", [[240, 240, 241, 255]], unlocked=True)
default cho_hat_goggles = DollCloth("cho", ("head", "headgear"), "headgear", "goggles", [[137, 150, 193, 255], [165, 165, 166, 255]], unlocked=True)
default cho_neckwear_medallion = DollCloth("cho", ("head", "neckwear"), "neckwear", "choker_medallion", [[25, 25, 26, 255]], unlocked=True)
default cho_neckwear_leather1 = DollCloth("cho", ("head", "neckwear"), "neckwear", "collar_leather_1", [[56, 56, 57, 255]], unlocked=True)
default cho_stockings_fishnet = DollCloth("cho", ("legwear", "stockings"), "stockings", "fishnet", [[100, 100, 101, 255], [50, 50, 51, 255]], level=14, unlocked=True)
default cho_top_sweater1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_1", [[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True, unlocked=True)
default cho_top_sweater2 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_2", [[89, 116, 194, 255]], level=6, unlocked=True)
default cho_top_tanktop1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_tanktop_1", [[230, 230, 231, 255]], level=14, unlocked=True)
default cho_robe_quidditch1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_quidditch_1", [[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True, unlocked=True)
default cho_bottom_pants1 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_1", [[230, 230, 231, 255]], armfix=True, unlocked=True)
default cho_bottom_shorts2 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_2", [[114, 168, 210, 255], [232, 177, 13, 255]], level=10, armfix=True, unlocked=True)
default cho_bottom_pants2 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_2", [[109, 105, 121, 255], [213, 161, 13, 255]], armfix=True, unlocked=True)
default cho_bottom_shorts4 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_4", [[109, 105, 121, 255], [213, 161, 13, 255]], level=8, armfix=True, unlocked=True)

# Quidditch seperate category
default choq_cloth_robequidditch1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_quidditch_1", [[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
default choq_cloth_topsweater1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_1", [[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
default choq_cloth_pantslong2 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_2", [[109, 105, 121, 255], [213, 161, 13, 255]], armfix=True)
default choq_cloth_pantsshort4 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_4", [[109, 105, 121, 255], [213, 161, 13, 255]], armfix=True)
default choq_cloth_glovesquidditch1 = DollCloth("cho", ("upper body", "gloves"), "gloves", "quidditch", [[213, 161, 13, 255]], armfix=True)
default choq_goggles = DollCloth("cho", ("head", "glasses"), "glasses", "goggles", [[137, 150, 193, 255], [165, 165, 166, 255]])
#default choq_goggles_face = DollCloth("cho", ("head", "headgear"), "headgear", "goggles_face", [[137, 150, 193, 255], [165, 165, 166, 255]], unlocked=False) # Not in use
default choq_cloth_schoolskirt3 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=False, armfix=True)

default cho_outfit_quidditch = DollOutfit([choq_cloth_topsweater1, choq_cloth_pantslong2, choq_cloth_robequidditch1, choq_cloth_glovesquidditch1, cho_bra_basic1, cho_panties_basic1])

default cho_outfit_quidditch_hufflepuff = DollOutfit([choq_cloth_topsweater1, choq_cloth_schoolskirt3, choq_cloth_robequidditch1, choq_cloth_glovesquidditch1, cho_bra_basic1, cho_panties_basic1])
default cho_outfit_quidditch_slytherin = DollOutfit([choq_cloth_topsweater1, choq_cloth_pantslong2, choq_cloth_glovesquidditch1, cho_bra_basic1, cho_panties_basic1])
default cho_outfit_quidditch_gryffindor = DollOutfit([choq_cloth_topsweater1, choq_cloth_schoolskirt3, choq_cloth_glovesquidditch1, cho_bra_basic1, cho_panties_basic1])

################
## Pubic Hair ##
################

default cho_pubes_arrow = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "arrow", [[70, 90, 147, 255]], unlocked=True)
default cho_pubes_beaver = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "beaver", [[70, 90, 147, 255]], unlocked=True)
default cho_pubes_stuble = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "stuble", [[52, 59, 80, 255]], unlocked=True)
default cho_pubes_unshaved = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "unshaved", [[52, 59, 80, 255]], unlocked=True)

default cho_makeup4_lipstick = DollLipstick("cho", ("head", "makeup"), "makeup4", "lipstick", [[255, 70, 70, 255]], unlocked=True)

### Event Specific ###

default cho_top_school1_slyt = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
default cho_top_school1_gryf = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default cho_top_school1_huff = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [251, 198, 10, 255], [51, 43, 54, 255]])
default cho_stockings_slyt = DollCloth("cho", ("legwear", "socks"), "stockings", "house", [[58, 115, 75, 255], [205, 205, 206, 255]])
default cho_stockings_gryf = DollCloth("cho", ("legwear", "socks"), "stockings", "house", [[219, 165, 13, 255], [146, 63, 30, 255]])
default cho_stockings_huff = DollCloth("cho", ("legwear", "socks"), "stockings", "house", [[251, 198, 10, 255], [51, 43, 54, 255]])

default cho_outfit_slyt = DollOutfit([cho_hair_ponytail1, cho_top_school1_slyt, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_slyt])
default cho_outfit_gryf = DollOutfit([cho_hair_ponytail1, cho_top_school1_gryf, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_gryf])
default cho_outfit_huff = DollOutfit([cho_hair_ponytail1, cho_top_school1_huff, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_huff])

default smurfette_hair = DollCloth("cho", ("head", "hair"), "hair", "smurfette", [[255, 221, 71, 255],[255, 237, 158, 255]])
default smurfette_hat = DollCloth("cho", ("head", "headgear"), "headgear", "smurfette", [[251, 251, 251, 255]])
default smurfette_top = DollCloth("cho", ("upper body", "dresses"), "top", "smurfette", [[251, 251, 251, 255],[251, 251, 251, 255]], blacklist=["bottom"], armfix=True)

default cho_outfit_smurfette = DollOutfit([smurfette_hair, smurfette_hat, smurfette_top], price=0, name="Smurfette Costume", desc="I'm coming for you, Gargamel.{heart}")

