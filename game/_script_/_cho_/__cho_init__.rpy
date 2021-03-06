# Main
default cho_xpos = 300
default cho_ypos = 0
default cho_zorder = 15
default cho_flip = 1
default cho_emote = None
default cho_animation = None
default use_cho_head = False

# Stats
default cho_tier                = 1
default cho_whoring             = 0
default cho_reputation          = 0
default cho_mood                = 0
default cho_jerk_off_counter    = 0

# Flags
default cho_known               = False
default cho_unlocked            = False
default cho_favors_unlocked     = False
default cho_requests_unlocked   = False
default cho_shaming_unlocked    = False
default cho_strip_complete      = False
default cho_wardrobe_unlocked   = False
default cho_busy                = False
default cho_chatted             = False
default has_cho_panties         = False
default cho_panties_soaked      = False
default cho_outfits_schedule    = True
default cho_bj_choice           = None # Dynamic string. Valid choices: failed, swallow, throat, points, taste.
default doppler_done            = False # For Strip event with Tonks.
default succubus_done           = False # For Strip event with Tonks.

# Intro
default jerked_off_during_cho_intro = False

# Quidditch Outfit
default quid_outfit_intro       = []

# Quidditch Matches
default hufflepuff_match      = ""
default slytherin_match       = ""
default gryffindor_match      = ""

default cho_content_complete  = False

# Names
default cho_genie_name = "Professor"
default cho_name = "Cho"
default tonks_cho_name = "Sweetie"

default gave_cho_gift      = False

# Cho Favors
# cc_pf = Cho Chang Personal Favor
default cc_pf_talk = event_class(title = "Talk to me!", start_label = "cc_pf_talk", start_tier = 1,
    events = [
        [
            ["cc_pf_talk_T1_intro_E1"],
            ["cc_pf_talk_T1_intro_E2"],
            ["cc_pf_talk_T1_E3"]
        ],
        [
            ["cc_pf_talk_T2_intro_E1"],
            ["cc_pf_talk_T2_intro_E2"],
            ["cc_pf_talk_T2_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
)
#cc_pf_strip_T3_intro_E3
default cc_pf_strip = event_class(title = "Inspect her body!", start_label = "cc_pf_strip", start_tier = 2,
    events = [
        [
            ["cc_pf_strip_T2_intro_E1"],
            ["cc_pf_strip_T2_intro_E2"],
            ["cc_pf_strip_T2_intro_E3"], ["cc_pf_strip_T2_E3"]
        ],
        [
            ["cc_pf_strip_T3_intro_E1"],
            ["cc_pf_strip_T3_intro_E2"],
            ["cc_pf_strip_T3_intro_E3"], ["cc_pf_strip_T3_repeat"]
        ]
    ],
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
)

default cc_pf_blowjob = event_class(title = "Suck it!", start_label = "cc_pf_blowjob", start_tier = 3,
    events = [
        [
            ["cc_pf_blowjob_T3_intro_E1"],
            ["cc_pf_blowjob_T3_E2"],
            ["cc_pf_blowjob_T3_E3"],
        ]
    ],
    iconset = [["heart_empty", "heart_red"]]
)

default cc_favor_list = [cc_pf_talk, cc_pf_strip, cc_pf_blowjob]

# Public requests
# cc_pr = Cho Chang Public Request

default cc_pr_spy_boys = event_class(title = "Spy on the boys!", start_label = "cc_pr_spy_boys_start", start_tier = 3,
    events = [
        [
            ["cc_pr_spy_boys_T3_twins"],
            ["cc_pr_spy_boys_T3_ron"],
            ["cc_pr_spy_boys_T3_harry"],
        ]
    ],
    icons = ["gryf"],
    iconset = [["star_empty", "star_yellow"]]
)

default cc_pr_manipulate_boys = event_class(title = "Manipulate the boys!", start_label = "cc_pr_manipulate_boys_start",
    events = [
        [
            ["cc_pr_manipulate_boys_T1_intro_E1"], ["cc_pr_manipulate_boys_T1_E1"],
            ["cc_pr_manipulate_boys_T1_E2"],
            ["cc_pr_manipulate_boys_T1_E3"]
        ],
        [
            ["cc_pr_manipulate_boys_T2_intro_E1"], ["cc_pr_manipulate_boys_T2_E1"],
            ["cc_pr_manipulate_boys_T2_intro_E2"],
            ["cc_pr_manipulate_boys_T2_intro_E3"], ["cc_pr_manipulate_boys_T2_E3"]
        ],
        [
            ["cc_pr_manipulate_boys_T3_twins"],
            ["cc_pr_manipulate_boys_T3_ron"],
            ["cc_pr_manipulate_boys_T3_harry"]
        ]
    ],
    icons = ["huff", "slyt", "gryf"], #if a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

default cc_pr_spy_girls = event_class(title = "Spy on the girls!", start_label = "cc_pr_spy_girls_start", start_tier = 3,
    events = [
        [
            ["cc_pr_spy_girls_T3_showers"],
            ["cc_pr_spy_girls_T3_alicia"],
            ["cc_pr_spy_girls_T3_katie"],
            ["cc_pr_spy_girls_T3_angelina"],
        ]
    ],
    icons = ["gryf"],
    iconset = [["star_empty", "star_yellow"]]
)

default cc_pr_manipulate_girls = event_class(title = "Manipulate the girls!", start_label = "cc_pr_manipulate_girls_start", start_tier = 3,
    events = [
        [
            ["cc_pr_manipulate_girls_T3_alicia"],
            ["cc_pr_manipulate_girls_T3_katie_part1"],
            ["cc_pr_manipulate_girls_T3_katie_part2"],
            ["cc_pr_manipulate_girls_T3_angelina"]
        ]
    ],
    icons = ["gryf"],
    iconset = [["star_empty", "star_yellow"]]
)

# TODO: lock favours until you finish `talk to me` part 3 in tier 3

default cc_requests_list = [cc_pr_spy_boys, cc_pr_manipulate_boys, cc_pr_spy_girls, cc_pr_manipulate_girls]

label reset_cho_progress:
    $ reset_variables(
        # Stats
        "cho_tier",
        "cho_whoring",
        "cho_reputation",
        "cho_mood",
        "cho_jerk_off_counter",

        # Flags
        "cho_known",
        "cho_unlocked",
        "cho_favors_unlocked",
        "cho_requests_unlocked",
        "cho_shaming_unlocked",
        "cho_strip_complete",
        "cho_wardrobe_unlocked",
        "cho_busy",
        "cho_chatted",
        "has_cho_panties",
        "cho_panties_soaked",
        "cho_bj_choice",
        "doppler_done",
        "succubus_done",

        # Intro
        "jerked_off_during_cho_intro",

        # Quidditch Outfit
        "quid_outfit_intro",

        # Quidditch Matches
        "hufflepuff_match",
        "slytherin_match",
        "gryffindor_match",
        "cho_content_complete",

        # Event objects
        "cc_pf_talk",
        "cc_pf_strip",
        "cc_pf_blowjob",
        "cc_favor_list",

        "cc_pr_manipulate_boys",
        "cc_pr_spy_girls",
        "cc_pr_manipulate_girls",
        "cc_requests_list",

        # Names
        "cho_genie_name",
        "cho_name",
        "tonks_cho_name",
        "gave_cho_gift"
    )
    return
