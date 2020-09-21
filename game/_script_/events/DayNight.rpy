# Common logic for day/night cycle

default defer_daytime_change = False

label defer_daytime_change(set_daytime):
    $ daytime = set_daytime
    $ defer_daytime_change = True
    call update_interface_color
    call music_block
    return

label common_start(set_daytime):
    show screen blkfade
    with dissolve

    $ daytime = set_daytime
    $ defer_daytime_change = False

    call update_interface_color

    # Update various time-based values
    if daytime:
        call update_day_values
    call update_day_and_night_values

    call points_changes # Calculates points
    call house_points   # Updates points

    # Set save filename
    $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name

    # Reset character appearances (chibis, clothing, etc.)
    call update_luna
    call update_astoria
    call update_hermione
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    #call stop_sound_effects

    # Play owl arrival sound once per day/night start
    if mailbox.get_letters() and not owl_away:
        call play_sound("owl")

    call room("main_room", stop_sound=False, hide_screens=True)

    hide screen blkfade
    with dissolve
    return

label update_day_values:
    $ fire_in_fireplace = False
    $ phoenix_is_fed = False
    $ phoenix_is_petted = False
    $ owl_away = False

    # Snape
    if ss_event_pause > 0:
        $ ss_event_pause -= 1
    if ss_summon_pause > 0:
        $ ss_summon_pause -= 1

    # Tonks
    if nt_event_pause > 0:
        $ nt_event_pause -= 1
    if nt_summon_pause > 0:
        $ nt_summon_pause -= 1
    $ gave_tonks_gift    = False

    # Hermione
    if hg_event_pause > 0:
        $ hg_event_pause -= 1
    if hg_summon_pause > 0:
        $ hg_summon_pause -= 1
    $ gave_hermione_gift = False

    # Luna
    if ll_event_pause > 0:
        $ ll_event_pause -= 1
    if ll_summon_pause > 0:
        $ ll_summon_pause -= 1
    $ gave_luna_gift     = False

    # Cho
    if cc_event_pause > 0:
        $ cc_event_pause -= 1
    if cc_summon_pause > 0:
        $ cc_summon_pause -= 1
    $ gave_cho_gift      = False

    # Astoria
    if ag_event_pause > 0:
        $ ag_event_pause -= 1
    if ag_summon_pause > 0:
        $ ag_summon_pause -= 1
    $ gave_astoria_gift  = False

    # Susan
    if sb_event_pause > 0:
        $ sb_event_pause -= 1
    if sb_summon_pause > 0:
        $ sb_summon_pause -= 1
    $ gave_susan_gift    = False

    # Nicknames
    call set_random_nicknames

    # Mood
    if game_difficulty < 3:
        if game_difficulty == 1:   # Easy difficulty
            $ val = 3
        elif game_difficulty == 2: # Normal difficulty
            $ val = 2

        $ ton_mood = max(ton_mood-val, 0)
        $ her_mood = max(her_mood-val, 0)
        $ lun_mood = max(lun_mood-val, 0)
        $ cho_mood = max(cho_mood-val, 0)
        $ ast_mood = max(ast_mood-val, 0)
        $ sus_mood = max(sus_mood-val, 0)

    # Set randomly awarded house points
    $ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
    $ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
    $ generating_points_gryffindor = renpy.random.randint(1, 10)
    $ generating_points_hufflepuff = renpy.random.randint(1, 10)
    $ generating_points_ravenclaw = renpy.random.randint(1, 10)

    # Set random variables
    $ one_out_of_three = renpy.random.randint(1, 3)
    $ one_of_five = renpy.random.randint(1, 5)
    $ one_of_ten = renpy.random.randint(1, 10)

    $ day_random = renpy.random.randint(0, 10)

    # Count days of the week. Every day +1. When day_of_week = 7, reset to zero.
    if day_of_week == 7:
        $ day_of_week = 0
        if reports_finished >= 1:
            $ letter_work_report.send()
        if not first_random_twins:
            $ twins_interest = True

    $ day_of_week += 1
    $ day += 1

    # Change the weather
    if day <= 1:
        $ set_weather("cloudy")
    else:
        $ set_weather()

    # Weather for Quidditch Matches
    if cc_event_pause == 0 and hufflepuff_match == "start":
        $ set_weather("clear")
    if cc_event_pause == 0 and slytherin_match == "start":
        $ set_weather("clear")

    # Change whether today is a full moon day
    $ set_moon()

    # Package delivery
    $ mailbox.tick()

    return


label update_day_and_night_values:

    # Snape
    if ss_summon_pause == 0:
        $ snape_busy = False
    $ chitchated_with_snape = False

    # Tonks
    if nt_summon_pause == 0:
        $ tonks_busy = False
    $ chitchated_with_tonks = False

    # Hermione
    if hg_summon_pause == 0:
        $ hermione_busy = False
    $ chitchated_with_her = False
    $ her_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_her_map_location()

    # Luna
    if ll_summon_pause == 0:
        $ luna_busy = False
    $ chitchated_with_luna = False
    $ lun_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_lun_map_location()

    # Cho
    if cc_summon_pause == 0:
        $ cho_busy = False
    $ chitchated_with_cho = False
    $ cho_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_cho_map_location()

    # Astoria
    if ag_summon_pause == 0:
        $ astoria_busy = False
    $ chitchated_with_astoria = False
    $ ast_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_ast_map_location()

    # Susan
    if sb_summon_pause == 0:
        $ susan_busy = False
    $ chitchated_with_susan = False
    $ sus_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_sus_map_location()

    $ searched  = False # Cupboard.

    $ random_gold = renpy.random.randint(8, 40) # Money you find in the cupboard.

    return
