# Main
default susan_xpos = 600
default susan_ypos = 0
default susan_zorder = 15
default susan_flip = 1
default susan_emote = None
default susan_animation = None
default use_susan_head = False

# Stats
default sus_tier = 1
default sus_whoring = 0
default sus_mood    = 0

# Flags
default susan_busy              = False
default susan_unlocked          = False
default susan_wardrobe_unlocked = False
default chitchated_with_susan   = False
default susan_outfits_schedule = True

# Favour stuff
default susan_imperio_influence = False
default susan_imperio_counter   = 0 # Maybe the higher Astoria's spell level gets, the longer this lasts?

# Names
default susan_name     = "Miss Bones"
default sus_genie_name = "Sir"

# Stats Screen
default sus_curse_counter = 2 # She got cursed twice beforeyou unlock her. Poor girl...

default gave_susan_gift = False

label reset_susan_progress:
    $ reset_variables(
        # Stats
        "sus_tier",
        "sus_whoring",
        "sus_mood",

        # Flags
        "susan_busy",
        "susan_unlocked",
        "susan_wardrobe_unlocked",
        "chitchated_with_susan",

        # Favour stuff
        "susan_imperio_influence",
        "susan_imperio_counter",

        # Names
        "susan_name",
        "sus_genie_name",

        # Stats Screen
        "sus_curse_counter"
    )
    return
