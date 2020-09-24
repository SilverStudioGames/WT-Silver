###############
## Character ##
###############

default astoria = Doll(name="astoria",
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

#######################
## Schoolgirl Outfit ##
#######################

default ast_hair_base = DollCloth("astoria", ("head", "hair"), "hair", "base", [[229, 198, 129, 255], [163, 125, 80, 255]], unlocked=True)
default ast_hair_short = DollCloth("astoria", ("head", "hair"), "hair", "short", [[229, 198, 129, 255], [163, 125, 80, 255]], unlocked=True)

default ast_top_school1 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default ast_top_school2 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_2", [[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], level=4, armfix=True, unlocked=True)
default ast_top_school3 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_3", [[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], level=8, armfix=True, unlocked=True)
default ast_top_school4 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_4", [[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], level=8, armfix=True, unlocked=True)
default ast_top_school5 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_5", [[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], level=12, armfix=True, unlocked=True)
default ast_top_school6 = DollCloth("astoria", ("tops", "shirts"), "top", "top_school_6", [[109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], level=12, armfix=True, unlocked=True)

default ast_bottom_skirt1 = DollCloth("astoria", ("bottoms", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], armfix=True, unlocked=True)
default ast_bottom_skirt2 = DollCloth("astoria", ("bottoms", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], level=4, armfix=True, unlocked=True)
default ast_bottom_skirt3 = DollCloth("astoria", ("bottoms", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], level=8, armfix=True, unlocked=True)
default ast_bottom_skirt4 = DollCloth("astoria", ("bottoms", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], level=12, armfix=True, unlocked=True)

default ast_bra_basic1 = DollCloth("astoria", ("bras", "bras"), "bra", "basic_bra_1", [[213, 62, 65, 255], [234, 236, 234, 255]], unlocked=True)
default ast_bra_basic2 = DollCloth("astoria", ("bras", "bras"), "bra", "basic_bra_2", [[213, 62, 65, 255]], unlocked=True)
default ast_panties_basic1 = DollCloth("astoria", ("panties", "panties"), "panties", "basic_panties_1", [[213, 62, 65, 255], [234, 236, 234, 255]], armfix=True, unlocked=True)
default ast_panties_basic2 = DollCloth("astoria", ("panties", "panties"), "panties", "basic_panties_2", [[213, 62, 65, 255]], armfix=True, unlocked=True)

default ast_outfit_default = DollOutfit([ast_hair_base, ast_top_school1, ast_bottom_skirt1, ast_bra_basic1, ast_panties_basic1], True)
default ast_outfit_last = DollOutfit([ast_hair_base])

################
## Ann Outfit ##
################

default ast_hair_ann = DollCloth("astoria", ("head", "hair"), "hair", "ann_takamaki", [[229, 198, 129, 255], [163, 125, 80, 255], [255, 209, 105, 255]])
default ast_hat_ann = DollCloth("astoria", ("head", "headgear"), "hat", "ann_takamaki", [[173, 18, 18, 255], [238, 188, 187, 255]], level=14)
default ast_top_ann = DollCloth("astoria", ("tops", "other"), "top", "ann_takamaki", [[173, 18, 18, 255], [232, 232, 232, 255], [238, 188, 187, 255]], level=14, blacklist=("bottom", "bra", "garterbelt"), armfix=True)
default ast_stockings_ann = DollCloth("astoria", ("legwear", "stockings"), "stockings", "ann_takamaki", [[99, 42, 42, 255], [181, 135, 135, 255]], level=14, blacklist=["bottom"], armfix=True)
default ast_gloves_ann = DollCloth("astoria", ("misc", "gloves"), "gloves", "ann_takamaki", [[249, 139, 225, 255]])
default ast_buttplug_ann = DollCloth("astoria", ("misc", "accessory"), "buttplug", "ann_takamaki", [[99, 42, 42, 255], [181, 135, 135, 255]], level=14)

default ast_outfit_ann = DollOutfit([ast_hair_ann, ast_hat_ann, ast_top_ann, ast_stockings_ann, ast_gloves_ann, ast_buttplug_ann], price=500)

##########
## Misc ##
##########

default ast_cloth_pants1 = DollCloth("astoria", ("bottoms", "trousers"), "bottom", "pants_1", [[180, 180, 180, 255], [213, 161, 13, 255]], armfix=True, unlocked=True)
default ast_cloth_shorts1 = DollCloth("astoria", ("bottoms", "shorts"), "bottom", "pants_1_short", [[180, 180, 180, 255], [213, 161, 13, 255]], level=8, armfix=True, unlocked=True)
default ast_cloth_pantyhose1 = DollCloth("astoria", ("legwear", "pantyhose"), "stockings", "pantyhose", [[190, 146, 129, 255]], armfix=True, unlocked=True)

################
## Pubic Hair ##
################

default ast_pubes_arrow = DollCloth("astoria", ("pelvis", "pubes"), "pubes", "arrow", [[229, 198, 129, 255]], unlocked=True)
default ast_pubes_beaver = DollCloth("astoria", ("pelvis", "pubes"), "pubes", "beaver", [[229, 198, 129, 255]], unlocked=True)
default ast_pubes_stuble = DollCloth("astoria", ("pelvis", "pubes"), "pubes", "stuble", [[139, 107, 69, 255]], unlocked=True)
default ast_pubes_unshaved = DollCloth("astoria", ("pelvis", "pubes"), "pubes", "unshaved", [[139, 107, 69, 255]], unlocked=True)

# Lipstick (DollLipstick)
default ast_makeup4_lipstick = DollLipstick("astoria", ("makeup", "slot5"), "makeup4", "lipstick", [[255, 70, 70, 255]], unlocked=True)