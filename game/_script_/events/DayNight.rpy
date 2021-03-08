
label day_start:
    show screen blkfade
    with dissolve

    # Reset room objects
    $ fire_in_fireplace = False
    $ phoenix_is_fed = False
    $ phoenix_is_petted = False
    $ phoenix_OBJ.foreground = None # Removes seeds image
    $ owl_away = False
    $ cupboard_searched = False

    # Reset gift flags
    $ gave_tonks_gift = False
    $ gave_hermione_gift = False
    $ gave_luna_gift = False
    $ gave_cho_gift = False
    $ gave_astoria_gift = False
    $ gave_susan_gift = False

    # Reset chit-chat flags
    $ chitchated_with_snape = False
    $ chitchated_with_tonks = False
    $ chitchated_with_hermione = False
    $ chitchated_with_luna = False
    $ chitchated_with_cho = False
    $ chitchated_with_astoria = False
    $ chitchated_with_susan = False

    # Tick Event timers
    $ ss_event_pause = max(ss_event_pause-1, 0)
    $ ss_summon_pause = max(ss_summon_pause-1, 0)
    $ nt_event_pause = max(nt_event_pause-1, 0)
    $ nt_summon_pause = max(nt_summon_pause-1, 0)
    $ hg_event_pause = max(hg_event_pause-1, 0)
    $ hg_summon_pause = max(hg_summon_pause-1, 0)
    $ ll_event_pause = max(ll_event_pause-1, 0)
    $ ll_summon_pause = max(ll_summon_pause-1, 0)
    $ cc_event_pause = max(cc_event_pause-1, 0)
    $ cc_summon_pause = max(cc_summon_pause-1, 0)
    $ ag_event_pause = max(ag_event_pause-1, 0)
    $ ag_summon_pause = max(ag_summon_pause-1, 0)
    $ sb_event_pause = max(sb_event_pause-1, 0)
    $ sb_summon_pause = max(sb_summon_pause-1, 0)

    # Reset busy flags (Based on current tick)
    $ snape_busy = bool(ss_summon_pause)
    $ tonks_busy = bool(nt_summon_pause)
    $ hermione_busy = bool(hg_summon_pause)
    $ luna_busy = bool(ll_summon_pause)
    $ cho_busy = bool(cc_summon_pause)
    $ astoria_busy = bool(ag_summon_pause)
    $ susan_busy = bool(sb_summon_pause)

    # Improve Mood
    if game.difficulty == 1:   # Easy difficulty
        $ val = 3
    elif game.difficulty == 2: # Normal difficulty
        $ val = 2
    elif game.difficulty == 3: # Hardcore difficulty
        $ val = 1

    $ ton_mood = max(ton_mood-val, 0)
    $ her_mood = max(her_mood-val, 0)
    $ lun_mood = max(lun_mood-val, 0)
    $ cho_mood = max(cho_mood-val, 0)
    $ ast_mood = max(ast_mood-val, 0)
    $ sus_mood = max(sus_mood-val, 0)

    # Game flags
    $ game.day += 1
    $ game.weather = "random"
    $ game.daytime = True

    # Randomisers
    $ random_gold = renpy.random.randint(8, 40)
    $ random_map_loc = renpy.random.randint(1, 5)

    # Send salary every 7th day
    if game.day % 7 == 0:
        if reports_finished >= 1:
            $ letter_work_report.send()
        if not first_random_twins:
            $ twins_interest = True

    # Deliver mail
    $ mailbox.tick()

    # Update map locations
    call set_her_map_location()
    call set_lun_map_location()
    call set_cho_map_location()
    call set_ast_map_location()
    call set_sus_map_location()
    #TODO: Add Tonks map location
    #TODO: Add Snape map location

    # Reset appearances and sprites
    call update_luna
    call update_astoria
    call update_hermione
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    # Reset and update interface
    call update_interface_color

    # Points gains
    call points_changes
    call update_ui_points

    call room(current_room, stop_sound=False, hide_screens=True)

    # Equip scheduled outfits
    if luna_outfits_schedule:
        $ luna.equip_random_outfit()
    if astoria_outfits_schedule:
        $ astoria.equip_random_outfit()
    if hermione_outfits_schedule:
        $ hermione.equip_random_outfit()
    if susan_outfits_schedule:
        $ susan.equip_random_outfit()
    if cho_outfits_schedule:
        $ cho.equip_random_outfit()
    if tonks_outfits_schedule:
        $ tonks.equip_random_outfit()

    hide screen blkfade
    with dissolve

    $ renpy.force_autosave(True)

    # Start Quests
    jump quests

    label day_resume:

    $ renpy.choice_for_skipping()

    call screen main_room_menu

label night_start:

    show screen blkfade
    with dissolve

    # Reset room objects
    $ cupboard_searched = False

    # Reset chit-chat flags
    $ chitchated_with_snape = False
    $ chitchated_with_tonks = False
    $ chitchated_with_hermione = False
    $ chitchated_with_luna = False
    $ chitchated_with_cho = False
    $ chitchated_with_astoria = False
    $ chitchated_with_susan = False

    # Reset busy flags (Based on current tick)
    $ snape_busy = bool(ss_summon_pause)
    $ tonks_busy = bool(nt_summon_pause)
    $ hermione_busy = bool(hg_summon_pause)
    $ luna_busy = bool(ll_summon_pause)
    $ cho_busy = bool(cc_summon_pause)
    $ astoria_busy = bool(ag_summon_pause)
    $ susan_busy = bool(sb_summon_pause)

    # Game flags
    $ game.weather = "random"
    $ game.daytime = False

    # Randomisers
    $ random_gold = renpy.random.randint(8, 40)
    $ random_map_loc = renpy.random.randint(1, 5)

    # Update map locations
    call set_her_map_location()
    call set_lun_map_location()
    call set_cho_map_location()
    call set_ast_map_location()
    call set_sus_map_location()
    #TODO: Add Tonks map location
    #TODO: Add Snape map location

    # Reset appearances and sprites
    call update_luna
    call update_astoria
    call update_hermione
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    # Reset and update interface
    call update_interface_color

    call room(current_room, stop_sound=False, hide_screens=True)

    # Equip scheduled outfits
    if luna_outfits_schedule:
        $ luna.equip_random_outfit()
    if astoria_outfits_schedule:
        $ astoria.equip_random_outfit()
    if hermione_outfits_schedule:
        $ hermione.equip_random_outfit()
    if susan_outfits_schedule:
        $ susan.equip_random_outfit()
    if cho_outfits_schedule:
        $ cho.equip_random_outfit()
    if tonks_outfits_schedule:
        $ tonks.equip_random_outfit()

    hide screen blkfade
    with dissolve

    $ renpy.force_autosave(True)

    # Start Quests
    jump quests

    label night_resume:

    $ renpy.choice_for_skipping()

    call screen main_room_menu
