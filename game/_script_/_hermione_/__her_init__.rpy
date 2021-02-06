# Main
default hermione_xpos = 300
default hermione_ypos = 0
default hermione_zorder = 15
default hermione_flip = 1
default hermione_emote = None
default hermione_animation = None
default use_hermione_head = False

# Stats
default her_tier       = 1
default her_whoring    = 0
default her_reputation = 0
default her_mood       = 0
default her_tutoring   = 1

default forest_BJ_progress = 1

# Flags
default hermione_busy      = False
default hermione_unlocked  = False
default hermione_favors    = False
default hermione_tutoring  = False
default her_panties_soaked = False

default hermione_favors_convinced = 0

default her_level_up = None

# Names
default genie_name = "Sir"
default dumbledore_name = "Albus Dumbledore"
default hermione_name = "Miss Granger"

# Clothing Flags
default hermione_dribble = False
default dribble_equippable = False
default hermione_wetpanties = False
default wetpanties_equippable = False
default hermione_outfits_schedule = True

# Stat Screen
default her_jerk_off_counter = 0

# Personal Requests
default hg_hidden_bj_seen_list = []

# Public Request Vars
default hg_pr_sex_skip = False

# Public Shaming Flags
default current_job = 0
default transparent_quest = False

# Event Vars
default jerked_off_during_hermione_intro = False # Turns True when you choose to jerk off while Hermione talks (Event_08)

default tutoring_offer_made = False # If you offered her to tutor her (In hermione_intro_E4). Affects conversation in the next event.

default hermione_is_waiting_01 = False # Turns True at the end of first special event with Snape. Triggers next visit from Hermione (hermione_intro_E2)
default hermione_is_waiting_02 = False # Turns True at the end of second special event with Snape. Triggers next visit from Hermione

# Potions
default her_potions_drunk = set() # Can contain
    # "polyjuice", "cat_polyjuice", "luna_polyjuice",
    # "expansion", "ass_expansion", "breast_expansion",
    # "addiction", "cum_addiction",
    # "hypno", "milk", "transparency"

default her_cum_potion_fail = 0
default her_cum_potion_return = False
default her_cat_polyjuice_return = False
default her_milk_potion_return = False
default potion_scene_11_progress = 0
default potion_version = 0

# Buttplug Events
default buttplug_magic_known = False
default buttplug_1_worn      = False
default buttplug_2_worn      = False
default buttplug_3_worn      = False
default buttplug_1_question  = False
default buttplug_2_question  = False
default buttplug_3_question  = False

# Cardgame promotion job
default her_shop_help       = False
default her_shop_help_first = True

# Rewards
default autograph                  = False # Professor Lockhart's tattoo.
default gave_hermione_gift         = False
default hermione_wardrobe_unlocked = False

# Tentacle event
default tentacle_sample = False # Quest "item" flag.
default tentacle_scroll_examined = False

default hg_ps_get_panties = shaming_class(
    tier = 2,
    title = "Panty Thief",
    start_label = "hg_ps_get_panties",
    complete_label = "hg_ps_get_panties_complete"
)

default hg_ps_buttplug = shaming_class(
    tier = 3,
    title = "Wear A Buttplug",
    start_label = "hg_ps_buttplug",
    complete_label = "hg_ps_buttplug_complete"
)

default hg_ps_cumslut = shaming_class(
    tier = 4,
    title = "Wear My Cum",
    start_label = "hg_ps_cumslut",
    complete_label = "hg_ps_cumslut_complete"
)

# Not used
default hg_ps_walk = shaming_class(
    tier = 2,
    title = "Walk Of Shame",
    start_label = "hg_ps_walk",
    complete_label = "hg_ps_walk_complete"
)

default hg_ps_list = [
    hg_ps_get_panties,
    hg_ps_buttplug,
    hg_ps_cumslut
]

default panty_jerkoff  = counter_class()
default hg_talk        = counter_class()
default hg_kiss        = counter_class()
default hg_jerkoff     = counter_class()
default hg_strip       = counter_class()
default hg_fingered    = counter_class()
default hg_masturbated = counter_class()
default hg_handjob     = counter_class()
default hg_titjob      = counter_class()
default hg_blowjob     = counter_class()
default hg_sex         = counter_class()
default hg_anal        = counter_class()

# Personal favours
default hg_pf_talk = event_class(title = "Talk to me!", start_label = "hg_pf_talk", start_tier = 1, events = [
    [
    ["hg_pf_talk_T1_intro_E1"],
    ["hg_pf_talk_T1_E1"]
    ],

    [
    ["hg_pf_talk_T2_intro_E1"],
    ["hg_pf_talk_T2_E1"]
    ],

    [
    ["hg_pf_talk_T3_intro_E1"],
    ["hg_pf_talk_T3_intro_E2"],
    ["hg_pf_talk_T3_repeat"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_half"], ["heart_empty", "heart_red"]]
    )

# Alternate talk event with TONKS
default hg_pf_talk_tonks = event_class(title = "", start_label = "", start_tier = 3, events = [
    [
    ["hg_pf_talk_tonks_T3_intro_E1"],
    ["hg_pf_talk_tonks_T3_E1"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_half"], ["heart_empty", "heart_red"]]
    )


default hg_pf_admire_panties = event_class(title = "Show me your Panties!", start_label = "hg_pf_admire_panties", start_tier = 1, events = [
    [
    ["hg_pf_admire_panties_T1_intro_E1"],
    ["hg_pf_admire_panties_T1_E1"]
    ],

    [
    ["hg_pf_admire_panties_T2_intro_E1"],
    ["hg_pf_admire_panties_T2_E1"]
    ],

    [
    ["hg_pf_admire_panties_T3_intro_E1"],
    ["hg_pf_admire_panties_T3_E1"],
    ["hg_pf_admire_panties_T3_E2"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
    )


default hg_pf_admire_breasts = event_class(title = "Show me your tits!", start_label = "hg_pf_admire_breasts", start_tier = 1, events = [
    [
    ["hg_pf_admire_breasts_T1_intro_E1"],
    ["hg_pf_admire_breasts_T1_intro_E2"],
    ["hg_pf_admire_breasts_T1_E2"]
    ],

    [
    ["hg_pf_admire_breasts_T2_intro_E1"],
    ["hg_pf_admire_breasts_T2_intro_E2"],
    ["hg_pf_admire_breasts_T2_E2"]
    ],

    [
    ["hg_pf_admire_breasts_T3_intro_E1"],
    ["hg_pf_admire_breasts_T3_E1"]
    ],

    [
    ["hg_pf_admire_breasts_T4_intro_E1"],
    ["hg_pf_admire_breasts_T4_E1"],
    ["hg_pf_admire_breasts_T4_E2"]
    ]

    ],
    icons = [None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_red"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
    )


default hg_pf_grope = event_class(title = "Grope her!", start_label = "hg_pf_grope", start_tier = 1, events = [
    [
    ["hg_pf_grope_T1_fail_intro"],
    ["hg_pf_grope_T1_fail_repeat"],
    ],

    [
    ["hg_pf_grope_T2_intro_E1"],
    ["hg_pf_grope_T2_E1"]
    ],

    [
    ["hg_pf_grope_T3_intro_E1"],
    ["hg_pf_grope_T3_E1"]
    ],

    [
    ["hg_pf_grope_T4_intro_E1"],
    ["hg_pf_grope_T4_intro_E2"],
    ["hg_pf_grope_T4_E2"]
    ]

    ],
    icons = [None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
    )


default hg_pf_strip = event_class(title = "Dance for Me!", start_label = "hg_pf_strip", start_tier = 1, events = [
    [["hg_pf_strip_fail"]], # Tier 1

    [
    ["hg_pf_strip_T2_fail_intro"],
    ["hg_pf_strip_T2_fail_repeat"],
    ],

    [
    ["hg_pf_strip_T3_intro_E1"], # First Strip event.
    ["hg_pf_strip_T3_intro_E2"], # Strip event where Snape enters.
    ["hg_pf_strip_T3_E2"]        # Clumsy Strip. Has branches.
    ],

    [
    ["hg_pf_strip_T4_intro_E1"], # Hermione has improved.
    ["hg_pf_strip_T4_intro_E2"], # Hermione doesn't mind stripping.
    ["hg_pf_strip_T4_E2"]        # She's happy to strip.
    ]

    ],
    icons = [None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_half"], ["heart_empty", "heart_red"]]
    )


default hg_pf_handjob = event_class(title = "Touch me!", start_label = "hg_pf_handjob", start_tier = 1, events = [
    [["hg_pf_handjob_fail"]], # Tier 1
    [["hg_pf_handjob_fail"]], # Tier 2
    [["hg_pf_handjob_fail"]], # Tier 3

    [
    ["hg_pf_handjob_T4_intro_E1"], # First time handjob
    ["hg_pf_handjob_T4_intro_E2"], # Second time handjob
    ["hg_pf_handjob_T4_repeat"]   # Repeated handjob
    ],

    [
    ["hg_pf_handjob_T5_intro_E1"], # New interaction
    ["hg_pf_handjob_T5_intro_E2"], # More reply options
    ["hg_pf_handjob_T5_repeat"]    # Repeated handjob
    ]

    ],
    icons = [None, None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_half"], ["heart_empty", "heart_red"]]
    )


default hg_pf_titjob = event_class(title = "Let me fuck them!", start_label = "hg_pf_titjob", start_tier = 1, events = [
    [["hg_pf_titjob_fail"]], # Tier 1
    [["hg_pf_titjob_fail"]], # Tier 2
    [["hg_pf_titjob_fail"]], # Tier 3
    [["hg_pf_titjob_fail"]], # Tier 4

    [
    ["hg_pf_titjob_T5_intro_E1"], # First time titjob
    ["hg_pf_titjob_T5_repeat"]   # Repeated titjob
    ],

    [
    ["hg_pf_titjob_T6_intro_E1"], # Couple of choices
    ["hg_pf_titjob_T6_intro_E2"], # New interactions
    ["hg_pf_titjob_T6_repeat"]    # Repeated titjob
    ]

    ],
    icons = [None, None, None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
    )


default hg_pf_blowjob = event_class(title = "Suck it!", start_label = "hg_pf_blowjob", start_tier = 1, events = [
    [["hg_pf_blowjob_fail"]], # Tier 1
    [["hg_pf_blowjob_fail"]], # Tier 2
    [["hg_pf_blowjob_fail"]], # Tier 3

    [
    ["hg_pf_blowjob_T4_fail_intro"], # Hermione refuses
    ["hg_pf_blowjob_T4_fail_repeat"] # Repeat fail
    ],

    [
    ["hg_pf_blowjob_T5_intro_E1"], # First time blowjob
    ["hg_pf_blowjob_T5_intro_E2"], # Snape visit
    ["hg_pf_blowjob_T5_repeat"]   # Repeated blowjob
    ],

    [
    ["hg_pf_blowjob_T6_intro_E1"], # Couple of choices
    ["hg_pf_blowjob_T6_hidden_repeat"], # Repeat: Random visit
    ["hg_pf_blowjob_T6_repeat"]    # Repeat: Regular + Facefuck
    ]

    ],
    icons = [None, None, None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_red"], ["heart_empty", "heart_red"]]
    )


default hg_pf_sex = event_class(title = "Let's have sex!", start_label = "hg_pf_sex", start_tier = 1, events = [
    [["hg_pf_sex_fail"]], # Tier 1
    [["hg_pf_sex_fail"]], # Tier 2
    [["hg_pf_sex_fail"]], # Tier 3
    [["hg_pf_sex_fail"]], # Tier 4
    [["hg_pf_sex_fail"]], # Tier 5 (Add tier 0 events that fail.)

    [
    ["hg_pf_sex_T6_intro_E1"], # First time sex
    ["hg_pf_sex_T6_intro_E2"], # Second time sex
    ["hg_pf_sex_T6_intro_E3"], # Choice to do anal
    ["hg_pf_sex_T6_E3"]        # Regular or anal sex
    ]

    ],
    icons = [None, None, None, None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_black"], ["heart_empty", "heart_half"]]
    )


default hg_favor_list = [
    hg_pf_talk,
    hg_pf_admire_breasts,
    hg_pf_admire_panties,
    hg_pf_grope,
    hg_pf_strip,
    hg_pf_handjob,
    hg_pf_titjob,
    hg_pf_blowjob,
    hg_pf_sex,
    ]


# Public requests

default hg_pr_flirt = event_class(title = "She's a flirt", start_label = "hg_pr_flirt", start_tier = 1, events = [
    [
    ["hg_pr_flirt_T1_E1"],
    ["hg_pr_flirt_T1_E2"],
    ["hg_pr_flirt_T1_E3"]
    ],

    [
    ["hg_pr_flirt_T2_E1"],
    ["hg_pr_flirt_T2_E2"],
    ["hg_pr_flirt_T2_E3"]
    ],

    [
    ["hg_pr_flirt_T3_E1"],
    ["hg_pr_flirt_T3_E2"],
    ["hg_pr_flirt_T3_E3"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )

default hg_pr_flirt_teacher = event_class(title = "She's bait", start_label = "hg_pr_flirt_teacher", start_tier = 1, events = [
    [
    ["hg_pr_flirt_teacher_T1_E1"],
    ["hg_pr_flirt_teacher_T1_E2"],
    ["hg_pr_flirt_teacher_T1_E3"]
    ],

    [
    ["hg_pr_flirt_teacher_T2_E1"],
    ["hg_pr_flirt_teacher_T2_E2"],
    ["hg_pr_flirt_teacher_T2_E3"]
    ],

    [
    ["hg_pr_flirt_teacher_T3_E1"],
    ["hg_pr_flirt_teacher_T3_E2"],
    ["hg_pr_flirt_teacher_T3_E3"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )

default hg_pr_grope = event_class(title = "Let a classmate molest you", start_label = "hg_pr_grope", start_tier = 2, events = [
    [
    ["hg_pr_grope_T2_E1"],
    ["hg_pr_grope_T2_E2"],
    ["hg_pr_grope_T2_E3"]
    ],

    [
    ["hg_pr_grope_T3_E1"],
    ["hg_pr_grope_T3_E2"],
    ["hg_pr_grope_T3_E3"]
    ],

    [
    ["hg_pr_grope_T4_E1"],
    ["hg_pr_grope_T4_E2"],
    ["hg_pr_grope_T4_E3"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )

default hg_pr_flash = event_class(title = "Flash your tits to a classmate", start_label = "hg_pr_flash", start_tier = 3, events = [
    [
    ["hg_pr_flash_T3_E1"],
    ["hg_pr_flash_T3_E2"],
    ["hg_pr_flash_T3_E3"]
    ],

    [
    ["hg_pr_flash_T4_E1"],
    ["hg_pr_flash_T4_E2"],
    ["hg_pr_flash_T4_E3"]
    ],

    [
    ["hg_pr_flash_T5_E1"],
    ["hg_pr_flash_T5_E2"],
    ["hg_pr_flash_T5_E3"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]],
    monologue_glass = False # Event specific
    )

default hg_pr_kiss = event_class(title = "Kiss a girl", start_label = "hg_pr_kiss", start_tier = 3, events = [
    [
    ["hg_pr_kiss_T3_E1"],
    ["hg_pr_kiss_T3_E2"],
    ["hg_pr_kiss_T3_E3"]
    ],

    [
    ["hg_pr_kiss_T4_E1"],
    ["hg_pr_kiss_T4_E2"],
    ["hg_pr_kiss_T4_E3"]
    ],

    [
    ["hg_pr_kiss_T5_E1"],
    ["hg_pr_kiss_T5_E2"]
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )

default hg_pr_handjob = event_class(title = "Give a handjob to a classmate", start_label = "hg_pr_handjob", start_tier = 4, events = [
    [
    ["hg_pr_handjob_T4_E1"],
    ["hg_pr_handjob_T4_E2"],
    ["hg_pr_handjob_T4_E3"]
    ],

    [
    ["hg_pr_handjob_T5_E1"],
    ["hg_pr_handjob_T5_E2"],
    ["hg_pr_handjob_T5_E3"]
    ],

    [
    ["hg_pr_handjob_T6_intro_E1"], # Ron
    ["hg_pr_handjob_T6_E2"],
    ["hg_pr_handjob_T6_E3"] # Ron & Harry
    ]

    ],
    icons = [None, None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )

default hg_pr_blowjob = event_class(title = "Give a blowjob to a classmate", start_label = "hg_pr_blowjob", start_tier = 5, events = [
    [
    ["hg_pr_blowjob_T5_E1"],
    ["hg_pr_blowjob_T5_E2"],
    ["hg_pr_blowjob_T5_E3"]
    ],

    [
    ["hg_pr_blowjob_T6_intro_E1"], # Ron & Harry
    ["hg_pr_blowjob_T6_E2"], # Slytherin
    ["hg_pr_blowjob_T6_E3"] # Restroom bukkake :O
    ]

    ],
    icons = [None, None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"], ["star_empty", "star_yellow"]]
    )


default hg_pr_sex = event_class(title = "Have sex with a classmate", start_label = "hg_pr_sex", start_tier = 6, events = [
    [
    ["hg_pr_sex_T6_intro_E1"],
    ["hg_pr_sex_T6_intro_E2"],
    ["hg_pr_sex_T6_E3"],
    ["hg_pr_sex_T6_E4"]
    ]

    ],
    icons = [None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"]]
    )

default hg_requests_list = [
    hg_pr_flirt,
    hg_pr_flirt_teacher,
    hg_pr_grope,
    hg_pr_flash,
    hg_pr_kiss,
    hg_pr_handjob,
    hg_pr_blowjob,
    hg_pr_sex
    ]

default her_cg_path     = "images/CG/herm_deep/"
default her_cg_overlay  = her_cg_path+"blank.webp"
default her_cg_base     = her_cg_path+"base.webp"
default her_cg_body     = her_cg_path+"luna_base.webp"
default her_cg_cheeks   = her_cg_path+"c_base.webp"
default her_cg_mouth    = her_cg_path+"m_base.webp"
default her_cg_eyewhite = her_cg_path+"eye_white.webp"
default her_cg_pupil    = her_cg_path+"pup_base.webp"
default her_cg_eye      = her_cg_path+"eye_base.webp"
default her_cg_eyebrow  = her_cg_path+"eb_base.webp"
default her_cg_eyewear  = her_cg_path+"glasses.webp"
default her_cg_tears    = her_cg_path+"blank.webp"
default her_cg_extra_1  = her_cg_path+"blank.webp"
default her_cg_extra_2  = her_cg_path+"blank.webp"
default her_cg_extra_3  = her_cg_path+"blank.webp"
default her_cg_genie    = her_cg_path+"genie.webp"
default her_cg_xpos     = 0
default her_cg_ypos     = 0
default her_cg_xpos_abs = 0
default her_cg_ypos_abs = 0
default her_cg_zoom     = 1
