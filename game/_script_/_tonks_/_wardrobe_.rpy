###############
## Character ##
###############

default tonks = Doll(name="tonks",
                        clothes={"hat":        [None, 15, True],
                                 "hair":       [None, 4, True],
                                 "earring":    [None, 14, True],
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
default ton_gloves_auror = DollCloth("tonks", ("misc", "gloves"), "gloves", "auror_gloves",[[45, 45, 48, 255]], armfix=True, unlocked=True)
default ton_top_auror  = DollCloth("tonks", ("tops", "shirts"), "top", "auror",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True, unlocked=True)
default ton_top_auror2 = DollCloth("tonks", ("tops", "shirts"), "top", "auror2",[[124, 42, 50, 255]], armfix=True, unlocked=True)
default ton_robe_auror = DollCloth("tonks", ("misc", "robes"), "robe", "auror_coat",[[40, 40, 41, 255], [174, 165, 169, 255]], armfix=True, unlocked=True)
default ton_bottoms_leggings = DollCloth("tonks", ("bottoms", "leggings"), "bottom", "leggings",[[45, 45, 48, 255]], armfix=True, unlocked=True)
default ton_bottoms_leggings_hole = DollCloth("tonks", ("bottoms", "leggings"), "bottom", "leggings_hole",[[45, 45, 48, 255]], level=60, armfix=True, unlocked=True)
default ton_stockings_auror = DollCloth("tonks", ("legwear", "stockings"), "stockings", "auror",[[45, 45, 48, 255], [177, 168, 172, 255]], armfix=True, unlocked=True)

default ton_outfit_default = DollOutfit([ton_hair_base_new, ton_neckwear_beads, ton_gloves_auror, ton_top_auror, ton_robe_auror, ton_bottoms_leggings, ton_stockings_auror], True)
default ton_outfit_last = DollOutfit([ton_hair_base_new])

###################
## School Outfit ##
###################

#default ton_bottom_school1 = DollCloth("tonks", ("bottoms", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True) # Not implemented
default ton_top_tied = DollCloth("tonks", ("tops", "other"), "top", "tied_top",[[183, 183, 184, 255]], blacklist=["bra"])
default ton_bottom_school2 = DollCloth("tonks", ("bottoms", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=20)
default ton_bottom_school3 = DollCloth("tonks", ("bottoms", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=40)
default ton_bottom_school4 = DollCloth("tonks", ("bottoms", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, level=60)

default ton_outfit_school = DollOutfit([ton_hair_base_new, ton_top_tied, ton_bottom_school2], price=350)

##################
## Flag Bikinis ##
##################

default ton_bra_bikini_1 = DollCloth("tonks", ("bras", "bikini bras"), "bra", "bikini_bra_1", [[255, 255, 255, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_striped = DollCloth("tonks", ("bras", "bikini bras"), "bra", "bikini_bra_1_striped", [[255, 255, 255, 255], [139, 0, 0, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_UK = DollCloth("tonks", ("bras", "bikini bras"), "bra", "bikini_bra_1_UK", [[255, 255, 255, 255], [200, 16, 46, 255], [1, 33, 105, 255], [255, 255, 255, 255]])
default ton_bra_bikini_1_USA = DollCloth("tonks", ("bras", "bikini bras"), "bra", "bikini_bra_1_USA", [[255, 255, 255, 255], [139, 0, 0, 255], [12, 99, 216, 255], [255, 255, 255, 255]])

default ton_panties_bikini_1 = DollCloth("tonks", ("panties", "bikini panties"), "panties", "bikini_panties_1", [[255, 255, 255, 255], [255, 255, 255, 255]])
default ton_panties_bikini_1_jock = DollCloth("tonks", ("panties", "bikini panties"), "panties", "bikini_panties_1_jock", [[255, 255, 255, 255]])
default ton_panties_bikini_1_striped = DollCloth("tonks", ("panties", "bikini panties"), "panties", "bikini_panties_1_striped", [[255, 255, 255, 255], [139, 0, 0, 255]])
default ton_panties_bikini_1_UK = DollCloth("tonks", ("panties", "bikini panties"), "panties", "bikini_panties_1_UK", [[255, 255, 255, 255], [200, 16, 46, 255], [1, 33, 105, 255]])

default ton_outfit_bikini_1 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1, ton_panties_bikini_1], price=250)
default ton_outfit_bikini_2 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_striped, ton_panties_bikini_1_striped], price=250)
default ton_outfit_bikini_3 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_UK, ton_panties_bikini_1_UK], price=250)
default ton_outfit_bikini_4 = DollOutfit([ton_hair_base_new, ton_bra_bikini_1_USA, ton_panties_bikini_1_jock], price=250)

###################
## Casual Outfit ##
###################

default ton_top_crop_casual = DollCloth("tonks", ("tops", "shirts"), "top", "crop_top",[[200, 8, 45, 255]])
default ton_bottoms_leggings_casual = DollCloth("tonks", ("bottoms", "leggings"), "bottom", "latex_leggings",[[32, 32, 32, 255], [25, 24, 24, 255]], armfix=True)

default ton_outfit_casual = DollOutfit([ton_hair_base_new, ton_top_crop_casual, ton_bottoms_leggings_casual], price=350)

#############
## Nightie ##
#############

default ton_top_nightie_1 = DollCloth("tonks", ("tops", "shirts"), "top", "nightie_1", [[153, 38, 96, 255]], armfix=True)

default ton_outfit_nightie = DollOutfit([ton_hair_base_new, ton_top_nightie_1], price=350)

##################
## Bunny outfit ##
##################

default ton_top_bunny1 = DollCloth("tonks", ("tops", "one-piece suits"), "top", "bunnysuit", [[48, 48, 48, 255]], blacklist=["panties", "bra"], zorder=7, level=40)
default ton_stockings_bunny1 = DollCloth("tonks", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", [[81, 81, 81, 255]], armfix=True, level=40)
default ton_hat_bunny1 = DollCloth("tonks", ("head", "headgear"), "hat", "bunny", [[48, 48, 48, 255], [232, 232, 232, 255]], level=20)
default ton_neckwear_bunny1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", [[232, 232, 232, 255], [48, 48, 48, 255]], level=10)

default ton_outfit_bunny = DollOutfit([ton_hair_base_new, ton_top_bunny1, ton_stockings_bunny1, ton_hat_bunny1, ton_neckwear_bunny1], price=350)

#############
## Dresses ##
#############

default ton_top_silk_dress = DollCloth("tonks", ("tops", "dresses"), "top", "silk_dress", [[240, 237, 250, 255], [234, 234, 234, 255]], blacklist=["bra", "bottom"], armfix=True)
default ton_robe_silk = DollCloth("tonks", ("misc", "robes"), "robe", "silk_robe", [[240, 237, 250, 255]], armfix=True)

default ton_top_skimpy_dress = DollCloth("tonks", ("tops", "dresses"), "top", "skimpy_dress", [[147, 1, 1, 255]], blacklist=["bottom"], armfix=True, level=40)
default ton_top_skimpy_dress2 = DollCloth("tonks", ("tops", "dresses"), "top", "skimpy_dress_2", [[108, 0, 105, 255]], blacklist=["bottom"], armfix=True, level=20)

#####################
## Succubus Outfit ##
#####################

default ton_hat_succubus = DollCloth("tonks", ("head", "headgear"), "hat", "horns", [[62, 51, 57, 255], [106, 63, 67, 255]])
default ton_neckwear_succubus = DollCloth("tonks", ("head", "neckwear"), "neckwear", "succubus_colar", [[62, 51, 57, 255]])
default ton_gloves_succubus = DollCloth("tonks", ("misc", "gloves"), "gloves", "succubus_gloves", [[62, 51, 57, 255]])
default ton_top_succubus = DollCloth("tonks", ("tops", "other"), "top", "succubus_corset",[[62, 51, 57, 255], [181, 86, 84, 255], [136, 134, 134, 255]], blacklist=["bra"])
default ton_top_succubus2 = DollCloth("tonks", ("tops", "other"), "top", "succubus_corset_2",[[62, 51, 57, 255], [181, 86, 84, 255], [136, 134, 134, 255]])
default ton_panties_succubus = DollCloth("tonks", ("panties", "bikini panties"), "panties", "succubus_panties", [[62, 51, 57, 255], [136, 134, 134, 255]])
default ton_accessory0_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory0", "succubus_wings", [[62, 51, 57, 255], [181, 86, 84, 255], [136, 134, 134, 255]], zorder=-160, blacklist=["robe"])
default ton_accessory1_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory1", "succubus_tail", [[62, 51, 57, 255], [181, 86, 84, 255]])

default ton_outfit_succubus = DollOutfit([ton_hair_base_new, ton_hat_succubus, ton_neckwear_succubus, ton_gloves_succubus, ton_top_succubus, ton_panties_succubus, ton_accessory0_succubus, ton_accessory1_succubus], price=666)

#####################
## Cavegirl Outfit ##
#####################

default ton_earring_pearls = DollCloth("tonks", ("head", "earrings"), "earring", "pearls", [[223, 240, 255, 255]])
default ton_neckwear_pearls = DollCloth("tonks", ("head", "neckwear"), "neckwear", "pearls_1", [[223, 240, 255, 255]], zorder=16)
default ton_top_cavegirl = DollCloth("tonks", ("tops", "dresses"), "top", "cavegirl_dress", [[223, 240, 255, 255]], armfix=True)

################# ~*~Ä~*~*~*~*~ #################
## Xmas Stuff ###   /%\  ___$__ ### Elf Outfit ##
#################  /% \ |=I~I=| #################

# Accessories
default ton_makeup3_elf_ears = DollCloth("tonks", ("makeup", "slot4"), "makeup3", "elf_ears", [[255, 255, 255, 255]], zorder=5)
default ton_hat_antlers = DollCloth("tonks", ("head", "headgear"), "hat", "antlers", [[234, 187, 170, 255]])
default ton_hat_elf = DollCloth("tonks", ("head", "headgear"), "hat", "elf", [[2, 116, 71, 255], [255, 239, 248, 255]])
default ton_neckwear_choker1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "choker_1", [[255, 43, 149, 255]], unlocked=True)
default ton_neckwear_bell1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "bell_1", [[2, 116, 71, 255], [244, 181, 82, 255]], zorder=16)
default ton_accessory4_bells = DollCloth("tonks", ("misc", "accessory"), "accessory4", "bells_1", [[244, 181, 82, 255]], zorder=16)
default ton_accessory3_belt1 = DollCloth("tonks", ("misc", "accessory"), "accessory3", "belt_1", [[42, 42, 42, 255], [185, 135, 73, 255]], zorder=16)
default ton_earring_bells = DollCloth("tonks", ("head", "earrings"), "earring", "bells", [[244, 181, 82, 255]])
default ton_piercing1_nipple_bells = DollCloth("tonks", ("breasts", "piercing"), "piercing1", "nipple_bells", [[244, 181, 82, 255]])
# Main Clothing
default ton_top_elf = DollCloth("tonks", ("tops", "dresses"), "top", "elf_dress",[[2, 116, 71, 255]], armfix=True)
default ton_bra_ribbon = DollCloth("tonks", ("bras", "other"), "bra", "ribbon", [[255, 43, 149, 255]], blacklist=["top", "piercing1"])
default ton_panties_ribbon = DollCloth("tonks", ("panties", "other"), "panties", "ribbon", [[255, 43, 149, 255]], blacklist=["bottom"], armfix=True)
default ton_bra_pasties = DollCloth("tonks", ("bras", "other"), "bra", "pasties_1",[[255, 43, 149, 255]], unlocked=True)
default ton_bra_pasties2 = DollCloth("tonks", ("bras", "other"), "bra", "pasties_2",[[2, 116, 71, 255], [244, 181, 82, 255]])
default ton_bottom_xmas = DollCloth("tonks", ("bottoms", "other"), "bottom", "xmas",[[2, 116, 71, 255], [255, 239, 248, 255]], armfix=True)
default ton_gloves_xmas = DollCloth("tonks", ("misc", "gloves"), "gloves", "xmas", [[255, 239, 248, 255]])
default ton_stockings_xmas = DollCloth("tonks", ("legwear", "stockings"), "stockings", "xmas",[[255, 255, 255, 255], [255, 255, 255, 255]], armfix=True)

#############################
## Stockings & Garterbelts ##
#############################

# Short

# Medium

# Long
default ton_stockings_long = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_basic_1",[[255, 255, 255, 255]], unlocked=True)
default ton_stockings_long2 = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_basic_2",[[0, 0, 0, 255], [16, 16, 16, 255]]) # Skimpy Outfit
default ton_stockings_long_meshed = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_meshed",[[0, 0, 0, 255], [0, 0, 0, 255]]) # Referee Outfit - SOON
default ton_stockings_long_sports = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_sports",[[255, 255, 255, 255], [23, 23, 23, 255]], unlocked=True)
default ton_stockings_long_striped = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_striped",[[255, 233, 246, 255], [180, 18, 36, 255]]) # Elf Outfit
default ton_garterbelt_long_basic = DollCloth("tonks", ("legwear", "garterbelts"), "garterbelt", "long_basic_1", [[255, 255, 255, 255]], armfix=True)

##########
## Misc ##
##########

default ton_top_corset = DollCloth("tonks", ("tops", "other"), "top", "corset",[[247, 206, 146, 255]], blacklist=["bra"], armfix=True, unlocked=True)
default ton_bottoms_jeans = DollCloth("tonks", ("bottoms", "trousers"), "bottom", "jeans",[[51, 104, 105, 255]], armfix=True, unlocked=True)
default ton_panties_base = DollCloth("tonks", ("panties", "bikini panties"), "panties", "base",[[94, 67, 67, 255], [251, 247, 246, 255]], armfix=True, unlocked=True)
default ton_bra_base = DollCloth("tonks", ("bras", "bikini bras"), "bra", "bikini",[[124, 42, 50, 255], [177, 168, 172, 255]], unlocked=True)
default ton_ruffled_top = DollCloth("tonks", ("tops", "shirts"), "top", "ruffled_top",[[213, 173, 219, 255]], level=25, unlocked=True)

default ton_earring_cartilege = DollCloth("tonks", ("head", "earrings"), "earring", "cartilege", [[161, 159, 159, 255]], unlocked=True)
default ton_earring_hoops = DollCloth("tonks", ("head", "earrings"), "earring", "hoops", [[161, 159, 159, 255]], unlocked=True)
default ton_earring_industrial = DollCloth("tonks", ("head", "earrings"), "earring", "industrial", [[161, 159, 159, 255]], unlocked=True)

default ton_piercing0_clit_stud = DollCloth("tonks", ("pelvis", "piercing"), "piercing0", "clit_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_stud = DollCloth("tonks", ("breasts", "piercing"), "piercing1", "nipple_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_rings = DollCloth("tonks", ("breasts", "piercing"), "piercing1", "nipple_rings", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_rings2 = DollCloth("tonks", ("breasts", "piercing"), "piercing1", "nipple_rings2", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing1_nipple_rings3 = DollCloth("tonks", ("breasts", "piercing"), "piercing1", "nipple_rings3", [[161, 159, 159, 255]], unlocked=True)

default ton_piercing2_belly_stud = DollCloth("tonks", ("torso", "piercing"), "piercing2", "belly_stud", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing2_belly_heart = DollCloth("tonks", ("torso", "piercing"), "piercing2", "belly_heart", [[161, 159, 159, 255]], unlocked=True)
default ton_piercing2_belly_dick = DollCloth("tonks", ("torso", "piercing"), "piercing2", "belly_dick", [[161, 159, 159, 255]], unlocked=True)

################
## Pubic Hair ##
################

default ton_pubes_arrow = DollCloth("tonks", ("pelvis", "pubes"), "pubes", "arrow", [[255, 146, 185, 255]], unlocked=True)
default ton_pubes_beaver = DollCloth("tonks", ("pelvis", "pubes"), "pubes", "beaver", [[255, 146, 185, 255]], unlocked=True)
default ton_pubes_stuble = DollCloth("tonks", ("pelvis", "pubes"), "pubes", "stuble", [[132, 64, 89, 255]], unlocked=True)
default ton_pubes_unshaved = DollCloth("tonks", ("pelvis", "pubes"), "pubes", "unshaved", [[132, 64, 89, 255]], unlocked=True)

# Lipstick (DollLipstick)
default ton_makeup4_lipstick = DollLipstick("tonks", ("makeup", "slot5"), "makeup4", "lipstick", [[255, 70, 70, 255]], unlocked=True)



#############
## Outfits ##
#############

# Dresses
default ton_outfit_silky        = DollOutfit([ton_hair_base_new, ton_top_silk_dress, ton_robe_silk], price=100)
default ton_outfit_club_dress   = DollOutfit([ton_hair_base_new, ton_top_skimpy_dress2, ton_stockings_long_meshed], price=300)
default ton_outfit_skimpy_dress = DollOutfit([ton_hair_base_new, ton_top_skimpy_dress, ton_stockings_long2], price=300)
default ton_outfit_cavegirl     = DollOutfit([ton_hair_base_new, ton_top_cavegirl, ton_earring_pearls, ton_neckwear_pearls], price=200)

# Xmas
default ton_outfit_elf    = DollOutfit([ton_hair_base_new, ton_makeup3_elf_ears, ton_earring_bells, ton_hat_elf, ton_neckwear_bell1, ton_top_elf, ton_accessory3_belt1, ton_accessory4_bells, ton_garterbelt_long_basic, ton_stockings_long_striped])
default ton_outfit_ribbon = DollOutfit([ton_hair_base_new, ton_neckwear_choker1, ton_bra_ribbon, ton_panties_ribbon])
default ton_outfit_xmas   = DollOutfit([ton_hair_base_new, ton_hat_antlers, ton_earring_bells, ton_neckwear_bell1, ton_bra_pasties2, ton_bottom_xmas, ton_gloves_xmas, ton_stockings_xmas])
