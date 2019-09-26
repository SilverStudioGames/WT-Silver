#TODO Move variable defaults to appropriate files, leave common ones here (and rename this file to _Variables_.rpy or something)

default addicted          = False
default tentacle_cosmetic = False

default interface_color = "gold"

default gallery_active = False
default ball_ending_2  = False

default game_difficulty = 2

default day = 0

default daytime        = False
default gold           = 0
default rum_times      = 0 # Counts how many times have you rummaged the cupboard.
default current_payout = 0
default tooltip        = None

# Hermione main screen flags
default no_blinking   = False # When True - blinking animation is not displayed.
default sperm_on_tits = False # Sperm on tits when Hermione pulls her shirt up.
default aftersperm    = False # Shows cum stains on Hermione's uniform.
default uni_sperm     = False # Triggers universal sperm to show on hermione_main screen.

default public_whore_ending = False # If TRUE the game will end with "Public Whore Ending".

# House points
default slytherin  = 180
default gryffindor = 53
default hufflepuff = 25
default ravenclaw  = 31

# Duel
default potions = 0 # Amount of healing potions Genie has in stock.

# Cupboard
default searched = False # Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

# Books
default found_voucher = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.

# Clothing
default gave_miniskirt = False # Turns True when Hermione has the miniskirt.

# Used to pause events/summons for a number of days
default ss_event_pause  = 0
default ss_summon_pause = 0
default nt_event_pause  = 0
default nt_summon_pause = 0
default hg_event_pause  = 0
default hg_summon_pause = 0
default cc_event_pause  = 0
default cc_summon_pause = 0
default ll_event_pause  = 0
default ll_summon_pause = 0
default ag_event_pause  = 0
default ag_summon_pause = 0
default sb_event_pause  = 0
default sb_summon_pause = 0

default always_read_letter = False
default owl_away           = False
default owl_away_counter   = 0

# Sprite positioning
default nxpos        = 0
default nypos        = 0
default nscale       = 0.5
default walk_xpos    = 750
default walk_ypos    = 250
default chibi_xpos   = 0
default chibi_ypos   = 0
default chibi_zorder = 1
default desk_zorder  = 2

default unlocked_7th       = False
default charName           = "genie"
default unlocked_xmas_deco = False

# Phoenix
default phoenix_is_fed         = False
default phoenix_is_petted      = False
default phoenix_fed_counter    = 0
default phoenix_petted_counter = 0

# Paperwork related flags
default day_of_week          = 0 # Counts days of the week. Everyday +1. When day_of_week = = 7 resets to zero.
default report_chapters      = 0 # Number of chapters of current report completed so far. Resets to zero when report is finished.
default finished_report      = 0 # Number of completed reports.
default stat_reports_counter = 0

# Fireplace
default fire_in_fireplace = False
default stat_fireplace_counter = 0

# Examine room flags
default desk_examined = False
default cupboard_examined = False
default bird_examined = False
default door_examined = False
default fireplace_examined = False

# Room decoration
default current_room  = "main_room"
default room_deco     = ""
default cupboard_deco = ""

# Scale factors (because most images are 2x larger)
# Scale-ratio of each character can be changed to be used in custom "CG" scenes. Made larger, more zoomed in,...
default scaleratio          = 2
default genie_scaleratio    = 2
default snape_scaleratio    = 2
default tonks_scaleratio    = 2
default hermione_scaleratio = 2
default luna_scaleratio     = 2
default astoria_scaleratio  = 2
default susan_scaleratio    = 2
default cho_scaleratio      = 2

# CGs
default ccg_folder = "luna_bj"
default ccg1       = "herm"
default ccg2       = 1
default ccg3       = "gene"
default loopimage  = None
default cg_image   = "e2"
default cg_path    = "images/CG/"+cg_image+".png"

default sc_cg_base    = "images/CG/sc34/1/base_1.png"
default sc_cg_image_1 = "images/CG/sc34/1/A_1.png"
default sc_cg_image_2 = "images/CG/sc34/2/B_1.png"
default sc_cg_image_3 = "images/CG/sc34/2/C_1.png"

default sccgxpos = 200
default sccgypos = 50

# CG or chibis
default face_on_cg = False # `call her_main(,ypos="head")` will use screen "her_face". Face gets positioned automatically.
default use_cgs = False
