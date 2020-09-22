# Main
default luna_xpos = 600
default luna_ypos = 0
default luna_zorder = 15
default luna_flip = 1
default luna_emote = None
default luna_animation = None
default use_luna_head = False

# Stats
default lun_tier = 1
default lun_whoring = 0
default lun_mood = 0
default luna_gold = 0
default lun_skirt_level = 1
default lun_top_level = 1
default lun_dom = 0
default lun_sub = 0

# Flags
default hat_known = False
default luna_known = False
default luna_busy = False
default luna_unlocked = False
default luna_wardrobe_unlocked = False

default luna_herm_talk = False
default luna_reverted = False # True if Luna is on normal path
default luna_reverted_intro = False # True if Luna was just reverted
default luna_addicted = False

# Names
default lun_genie_name = "Professor"
default luna_name = "Miss Lovegood"

default gave_luna_gift = False

# TODO: Yeet it
default hermione_kneel_leg     = False
default hermione_kneel_cock    = False

default lun_cg_path       = "images/CG/luna_desk2/"
default lun_cg_overlay    = lun_cg_path+"blank.webp"
default lun_cg_base       = lun_cg_path+"base.webp"
default lun_cg_border     = lun_cg_path+"border.webp"
default lun_cg_body       = lun_cg_path+"luna_base.webp"
default lun_cg_hair       = lun_cg_path+"playful_hair.webp"
default lun_cg_cheeks     = lun_cg_path+"c_base.webp"
default lun_cg_mouth      = lun_cg_path+"m_base.webp"
default lun_cg_eyewhite   = lun_cg_path+"eye_white.webp"
default lun_cg_pupil      = lun_cg_path+"pup_base.webp"
default lun_cg_eye        = lun_cg_path+"eye_base.webp"
default lun_cg_eyebrow    = lun_cg_path+"eb_base.webp"
default lun_cg_eyewear    = lun_cg_path+"glasses.webp"
default lun_cg_tears      = lun_cg_path+"blank.webp"
default lun_cg_hairtop    = lun_cg_path+"playful_hair_top.webp"
default lun_cg_extra_1    = lun_cg_path+"blank.webp"
default lun_cg_extra_2    = lun_cg_path+"blank.webp"
default lun_cg_extra_3    = lun_cg_path+"blank.webp"
default lun_cg_dick       = lun_cg_path+"dick_1.webp"
default lun_cg_genie      = lun_cg_path+"genie.webp"
default lun_cg_xpos       = 0
default lun_cg_ypos       = 0
default lun_cg_xpos_abs   = 0
default lun_cg_ypos_abs   = 0
default lun_loop_xpos     = [-150, 0, 55, 66, 74, 80, 88, 99, 103, 114, 121, 129, 134, 141, 148, 152, 155]
default lun_loop_ypos     = [0, 0, 12, 20, 31, 40, 48, 59, 71, 76, 83, 90, 97, 103, 107, 111, 112]
default lun_cg_zoom       = 1

default seen_luna_sex_list = []

# Events
default ll_pf_masturbate = event_class(title = "Masturbate for me!", start_label = "ll_pf_masturbate", start_tier = 2,
    events = [
        [
            ["ll_pf_masturbate_T1_intro"],
            ["ll_pf_masturbate_T1_E1"],
            ["ll_pf_masturbate_T1_E2"],
            ["ll_pf_masturbate_T1_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_red"]]
)

default ll_pf_blowjob = event_class(title = "Suck it!", start_label = "ll_pf_blowjob", start_tier = 3,
    events = [
        [
            ["ll_pf_blowjob_T1_intro"],
            ["ll_pf_blowjob_T1_E1"],
            ["ll_pf_blowjob_T1_E2"],
            ["ll_pf_blowjob_T1_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_red"]]
)

default ll_pf_sex = event_class(title = "Let's have sex!", start_label = "ll_pf_sex", start_tier = 4,
    events = [
        [
            ["ll_pf_sex_T1_intro"],
            ["ll_pf_sex_T1_E1"],
            ["ll_pf_sex_T1_E2"],
            ["ll_pf_sex_T1_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_red"]]
)

# Favors get added to the list after their intro events.
# Do not add them manually to this list!
default ll_favor_list = []

label reset_luna_progress:
    $ reset_variables(
        "lun_whoring",
        "lun_tier",
        "lun_mood",
        "luna_gold",
        "lun_skirt_level",
        "lun_top_level",
        "lun_dom",
        "lun_sub",

        "hat_known",
        "luna_known",
        "luna_busy",
        "luna_unlocked",
        "luna_wardrobe_unlocked",
        "luna_herm_talk",
        "luna_reverted",
        "luna_addicted",

        "lun_genie_name",
        "luna_name",
        "gave_luna_gift",

        # Event objects
        "ll_pf_masturbate",
        "ll_pf_blowjob",
        "ll_pf_sex",
        "ll_favor_list"
    )
    return
