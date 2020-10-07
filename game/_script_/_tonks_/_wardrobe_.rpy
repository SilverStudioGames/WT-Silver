###############
## Character ##
###############

default tonks = Doll(name="tonks",
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
                        body={"armleft": ["on_hips", 3],
                              "armright":["on_hips", 1],
                              "base":    ["front", 0],
                              "breasts": ["normal", 2]})

##################
## Auror Outfit ##
##################

default ton_hair_base = DollCloth("tonks", ("head", "hair"), "hair", "base", [[255, 146, 185, 255], [254, 218, 238, 255]], unlocked=True)
default ton_hair_base_new = DollCloth("tonks", ("head", "hair"), "hair", "new", [[255, 146, 185, 255], [254, 218, 238, 255]], unlocked=True)
default ton_neckwear_beads = DollCloth("tonks", ("head", "neckwear"), "neckwear", "choker_beads",[[45, 45, 48, 255], [177, 168, 172, 255]], unlocked=True)
default ton_gloves_auror = DollCloth("tonks", ("upper body", "gloves"), "gloves", "auror_gloves",[[45, 45, 48, 255]], armfix=True, unlocked=True)
default ton_top_auror  = DollCloth("tonks", ("upper body", "shirts"), "top", "auror",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True, unlocked=True)
default ton_top_auror2 = DollCloth("tonks", ("upper body", "shirts"), "top", "auror2",[[124, 42, 50, 255]], armfix=True, unlocked=True)
default ton_robe_auror = DollCloth("tonks", ("upper body", "robes"), "robe", "auror_coat",[[40, 40, 41, 255], [174, 165, 169, 255]], armfix=True, unlocked=True)
default ton_bottoms_leggings = DollCloth("tonks", ("lower body", "leggings"), "bottom", "leggings",[[45, 45, 48, 255]], armfix=True, unlocked=True)
default ton_bottoms_leggings_hole = DollCloth("tonks", ("lower body", "leggings"), "bottom", "leggings_hole",[[45, 45, 48, 255]], level=60, armfix=True, unlocked=True)
default ton_stockings_auror = DollCloth("tonks", ("legwear", "stockings"), "stockings", "auror",[[45, 45, 48, 255], [177, 168, 172, 255]], armfix=True, unlocked=True)

default ton_outfit_default = DollOutfit([ton_hair_base_new, ton_neckwear_beads, ton_gloves_auror, ton_top_auror, ton_robe_auror, ton_bottoms_leggings, ton_stockings_auror], True)
default ton_outfit_last = DollOutfit([ton_hair_base_new])

###################
## School Outfit ##
###################

#default ton_bottom_school1 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True) # Not implemented
default ton_top_tied = DollCloth("tonks", ("upper body", "other"), "top", "tied_top",[[183, 183, 184, 255]], blacklist=["bra"])
default ton_bottom_school2 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=20)
default ton_bottom_school3 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=40)
default ton_bottom_school4 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=60)

default ton_outfit_school = DollOutfit([ton_hair_base_new, ton_top_tied, ton_bottom_school2], price=350)

##################
## Flag Bikinis ##
##################

default ton_bra_bikini_1 = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1", [[255, 255, 255, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_striped = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_striped", [[255, 255, 255, 255], [139, 0, 0, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_UK = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_UK", [[255, 255, 255, 255], [200, 16, 46, 255], [1, 33, 105, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_USA = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_USA", [[255, 255, 255, 255], [139, 0, 0, 255], [12, 99, 216, 255], [255, 255, 255, 255]])

default ton_panties_bikini_1 = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1", [[255, 255, 255, 255], [255, 255, 255, 255]])
default ton_panties_bikini_1_jock = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_jock", [[255, 255, 255, 255]])
default ton_panties_bikini_1_striped = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_striped", [[255, 255, 255, 255], [139, 0, 0, 255]])
default ton_panties_bikini_1_UK = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_UK", [[255, 255, 255, 255], [200, 16, 46, 255], [1, 33, 105, 255]])

default ton_outfit_bikini_1 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1, ton_panties_bikini_1], price=250)
default ton_outfit_bikini_2 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_striped, ton_panties_bikini_1_striped], price=250)
default ton_outfit_bikini_3 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_UK, ton_panties_bikini_1_UK], price=250)
default ton_outfit_bikini_4 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_USA, ton_panties_bikini_1_jock], price=250)

###################
## Casual Outfit ##
###################

default ton_top_crop_casual = DollCloth("tonks", ("upper body", "shirts"), "top", "crop_top",[[200, 8, 45, 255]])
default ton_bottoms_leggings_casual = DollCloth("tonks", ("lower body", "leggings"), "bottom", "latex_leggings",[[32, 32, 32, 255], [25, 24, 24, 255]], armfix=True)

default ton_outfit_casual = DollOutfit([ton_hair_base_new, ton_top_crop_casual, ton_bottoms_leggings_casual], price=350)

#############
## Nightie ##
#############

default ton_top_nightie_1 = DollCloth("tonks", ("upper body", "shirts"), "top", "nightie_1", [[153, 38, 96, 255]], armfix=True)

default ton_outfit_nightie = DollOutfit([ton_hair_base_new, ton_top_nightie_1], price=350)

##################
## Bunny outfit ##
##################

default ton_top_bunny1 = DollCloth("tonks", ("upper body", "one-piece suits"), "top", "bunnysuit", [[48, 48, 48, 255]], blacklist=["panties", "bra"], zorder=7, level=40)
default ton_stockings_bunny1 = DollCloth("tonks", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", [[81, 81, 81, 255]], armfix=True, level=40)
default ton_hat_bunny1 = DollCloth("tonks", ("head", "headgear"), "headgear", "bunny", [[48, 48, 48, 255], [232, 232, 232, 255]], level=20)
default ton_neckwear_bunny1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", [[232, 232, 232, 255], [48, 48, 48, 255]], level=10)

default ton_outfit_bunny = DollOutfit([ton_hair_base_new, ton_top_bunny1, ton_stockings_bunny1, ton_hat_bunny1, ton_neckwear_bunny1], price=350)

#################
## Silky Dress ##
#################

default ton_top_silk_dress = DollCloth("tonks", ("upper body", "dresses"), "top", "silk_dress", [[240, 237, 250, 255], [234, 234, 234, 255]], blacklist=["bra", "bottom"], armfix=True)
default ton_robe_silk = DollCloth("tonks", ("upper body", "robes"), "robe", "silk_robe", [[240, 237, 250, 255]], armfix=True)

default ton_outfit_silky = DollOutfit([ton_hair_base_new, ton_top_silk_dress, ton_robe_silk], price=350)

#####################
## Succubus Outfit ##
#####################

default ton_hat_succubus = DollCloth("tonks", ("head", "headgear"), "headgear", "horns", [[62, 51, 57, 255], [106, 63, 67, 255]])
default ton_neckwear_succubus = DollCloth("tonks", ("head", "neckwear"), "neckwear", "succubus_colar", [[62, 51, 57, 255]])
default ton_gloves_succubus = DollCloth("tonks", ("upper body", "gloves"), "gloves", "succubus_gloves", [[62, 51, 57, 255]])
default ton_top_succubus = DollCloth("tonks", ("upper body", "other"), "top", "succubus_corset",[[62, 51, 57, 255], [181, 86, 84, 255], [136, 134, 134, 255]], blacklist=["bra"])
default ton_panties_succubus = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "succubus_panties", [[62, 51, 57, 255], [136, 134, 134, 255]])
default ton_accessory0_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory0", "succubus_wings", [[62, 51, 57, 255], [181, 86, 84, 255], [136, 134, 134, 255]], zorder=-160, blacklist=["robe"])
default ton_accessory1_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory1", "succubus_tail", [[62, 51, 57, 255], [181, 86, 84, 255]])

default ton_outfit_succubus = DollOutfit([ton_hair_base_new, ton_hat_succubus, ton_neckwear_succubus, ton_gloves_succubus, ton_top_succubus, ton_panties_succubus, ton_accessory0_succubus, ton_accessory1_succubus], price=666)

##########
## Misc ##
##########

default ton_top_corset = DollCloth("tonks", ("upper body", "other"), "top", "corset",[[247, 206, 146, 255]], blacklist=["bra"], armfix=True, unlocked=True)
default ton_bottoms_jeans = DollCloth("tonks", ("lower body", "trousers"), "bottom", "jeans",[[51, 104, 105, 255]], armfix=True, unlocked=True)
default ton_panties_base = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "base",[[94, 67, 67, 255], [251, 247, 246, 255]], unlocked=True)
default ton_bra_base = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini",[[124, 42, 50, 255], [177, 168, 172, 255]], unlocked=True)
default ton_ruffled_top = DollCloth("tonks", ("upper body", "shirts"), "top", "ruffled_top",[[213, 173, 219, 255]], level=25, unlocked=True)

default ton_earring_cartilege = DollCloth("tonks", ("head", "earrings"), "earrings", "cartilege", [[161, 159, 159, 255]], unlocked=True)
default ton_earring_hoops = DollCloth("tonks", ("head", "earrings"), "earrings", "hoops", [[161, 159, 159, 255]], unlocked=True)
default ton_earring_industrial = DollCloth("tonks", ("head", "earrings"), "earrings", "industrial", [[161, 159, 159, 255]], unlocked=True)

default ton_piercing0_clit_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing0", "clit_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing1", "nipple_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_rings = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing1", "nipple_rings", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_rings2 = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing1", "nipple_rings2", [[161, 159, 159, 255]], unlocked=True)

default ton_piercing2_belly_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing2", "belly_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing2_belly_heart = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing2", "belly_heart", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing2_belly_dick = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing2", "belly_dick", [[161, 159, 159, 255]], unlocked=True)

################
## Pubic Hair ##
################

default ton_pubes_arrow = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "arrow", [[255, 146, 185, 255]], unlocked=True)
default ton_pubes_beaver = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "beaver", [[255, 146, 185, 255]], unlocked=True)
default ton_pubes_stuble = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "stuble", [[132, 64, 89, 255]], unlocked=True)
default ton_pubes_unshaved = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "unshaved", [[132, 64, 89, 255]], unlocked=True)

# Lipstick (DollLipstick)
default ton_makeup4_lipstick = DollLipstick("tonks", ("head", "makeup"), "makeup4", "lipstick", [[255, 70, 70, 255]], unlocked=True)
