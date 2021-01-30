###############
## Character ##
###############

default luna = Doll(name="luna",
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
                        body={"armleft": ["up", 3],
                              "armright":["up", 1],
                              "base":    ["front", 0],
                              "breasts": ["normal", 2]})

#######################
## Schoolgirl Outfit ##
#######################

default lun_hair_base = DollCloth("luna", ("head", "hair"), "hair", "base", [[255, 228, 168, 255], [48, 144, 135, 255]], unlocked=True)

################
## Schoolgirl ##
################

default lun_top_school1 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_1", [[109, 105, 121, 255], [183, 183, 184, 255], [89, 116, 194, 255], [216, 163, 10, 255]], unlocked=True)
default lun_top_school2 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_2", [[109, 105, 121, 255], [183, 183, 184, 255], [89, 116, 194, 255], [216, 163, 10, 255]], unlocked=True)
default lun_top_school3 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_3", [[109, 105, 121, 255], [183, 183, 184, 255], [89, 116, 194, 255], [216, 163, 10, 255]], unlocked=True)
#default lun_top_school4 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_4", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
#default lun_top_school5 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_5", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=4)
#default lun_top_school6 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_6", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
#default lun_top_crop = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_crop", [[109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
default lun_top_vest = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_vest", [[109, 105, 121, 255], [89, 116, 194, 255], [216, 163, 10, 255]], unlocked=True, level=13)

default lun_outfit_default = DollOutfit([lun_hair_base], True)
default lun_outfit_last = DollOutfit([lun_hair_base])

# default ll_stewardess_ITEM = CostumeItem(
#     id="ll_stewardess", name="Stewardess Outfit", type="outfit", items=["onepiece-top","hat","necklace","thong"],
#     cost=80, wait_time=2, image="outfits/ll_stewardess", description="> An outfit giving you immediate access to the mile-high club!",
#     # Layers
#     outfit_layers = ["panties/panties_thong_1","onepieces/onepiece_stewardess_1","neckwear/cloth_tie"],
#     top_layers    = "hat_stewardess"
# )
# default ll_stewardess_short_ITEM = CostumeItem(
#     id="ll_stewardess_short", name="Short Stewardess Outfit", type="outfit", items=["onepiece-top","hat","necklace","thong"], image="outfits/ll_stewardess_short", unlockable=True,
#     # Layers
#     outfit_layers = ["panties/panties_thong_2","onepieces/onepiece_stewardess_2","neckwear/cloth_tie"],
#     top_layers    = "hat_stewardess"
# )
# default ll_dress_orange_ITEM = CostumeItem(
#     id="ll_dress_orange", name="Ball Dress", type="outfit", items=["earrings","onepiece-top","stockings"],
#     cost=200, wait_time=3, image="outfits/ll_dress_orange", description=">A cute dress in a questionable colour.",
#     # Layers
#     outfit_layers = ["stockings/leggings_1","onepieces/onepiece_ball_dress","piercings/ears_starts_1"]
# )
