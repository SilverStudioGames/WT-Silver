###############
## Character ##
###############

default susan = Doll(name="susan",
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
                        body={"armleft": ["behind", -1],
                              "armright":["behind", -1],
                              "base":    ["front", 0],
                              "breasts": ["normal", 2]})

#######################
## Schoolgirl Outfit ##
#######################

default sus_hair_base = DollCloth("susan", ("head", "hair"), "hair", "base", [[213, 90, 42, 255]], unlocked=True)

default sus_top_school1 = DollCloth("susan", ("upper body", "shirts"), "top", "school_top_1", [[0, 0, 0, 0]], unlocked=True)
default sus_top_school2 = DollCloth("susan", ("upper body", "shirts"), "top", "school_top_2", [[0, 0, 0, 0]], unlocked=True)
default sus_top_school3 = DollCloth("susan", ("upper body", "shirts"), "top", "school_top_3", [[0, 0, 0, 0]], unlocked=True)
default sus_top_school4 = DollCloth("susan", ("upper body", "shirts"), "top", "school_top_4", [[0, 0, 0, 0]], unlocked=True)
default sus_top_school5 = DollCloth("susan", ("upper body", "shirts"), "top", "school_top_5", [[0, 0, 0, 0]], unlocked=True)
default sus_top_ball = DollCloth("susan", ("upper body", "dresses"), "top", "ball", [[0, 0, 0, 0]], blacklist=["bottom"], unlocked=True)
default sus_top_heart = DollCloth("susan", ("upper body", "dresses"), "top", "heart", [[0, 0, 0, 0]], blacklist=["bottom", "bra", "neckwear"], unlocked=True)
default sus_top_sling1 = DollCloth("susan", ("upper body", "one-piece suits"), "top", "sling", [[0, 0, 0, 0]], unlocked=True)
default sus_top_sling2 = DollCloth("susan", ("upper body", "one-piece suits"), "top", "sling2", [[0, 0, 0, 0]], unlocked=True)

default sus_bottom_school1 = DollCloth("susan", ("lower body", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True)

default sus_stockings_base1 = DollCloth("susan", ("legwear", "stockings"), "stockings", "base", [[0, 0, 0, 0]], unlocked=True)
default sus_stockings_lace1 = DollCloth("susan", ("legwear", "stockings"), "stockings", "lace", [[0, 0, 0, 0]], unlocked=True)
default sus_stockings_lace2 = DollCloth("susan", ("legwear", "stockings"), "stockings", "lace2", [[0, 0, 0, 0]], unlocked=True)

default sus_bra_base1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "base", [[0, 0, 0, 0]], unlocked=True)
default sus_bra_chain = DollCloth("susan", ("upper undergarment", "bras"), "bra", "chain", [[0, 0, 0, 0]], unlocked=True)
default sus_bra_lace = DollCloth("susan", ("upper undergarment", "bras"), "bra", "lace", [[0, 0, 0, 0]], unlocked=True)

default sus_panties_base1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "base", [[0, 0, 0, 0]], unlocked=True)
default sus_panties_lace1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "lace", [[0, 0, 0, 0]], unlocked=True)

default sus_neckwear_choker = DollCloth("susan", ("head", "neckwear"), "neckwear", "choker", [[0, 0, 0, 0]], unlocked=True)

default sus_outfit_default = DollOutfit([sus_hair_base, sus_top_school1, sus_bottom_school1, sus_bra_base1, sus_panties_base1, sus_stockings_base1], True)
default sus_outfit_last = DollOutfit([sus_hair_base])
