label night_start:
    call common_start(False)

    # Start Quests
    jump quests

    label night_resume:

    # Favors
    python:
        for i in nt_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()

        for i in cc_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()

        for i in hg_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()
        for i in hg_ps_list: #Call any public shaming event if it's in progress
            if i.inProgress:
                renpy.jump(i.complete_label)

        for i in ag_spell_list: # Spell Training
            if i.inProgress:
                i.inProgress = False
                i.start()

    # Hermione Events.
    if current_job == 1:
        jump maid_responses
    if current_job == 2:
        jump barmaid_responses
    if current_job == 3:
        jump gryffindor_cheer_responses
    if current_job == 4:
        jump slytherin_cheer_responses
    if current_job == 5:
        jump hermione_helping_selling_cards

    #Hermione Potions return.
    # if cat_ears_potion_return:
        # jump potion_scene_1_1_2  <--- Missing label
    if transparent_quest:
        $ transparent_quest = False
        jump potion_scene_4_2
    # if addicted == True:
        # jump potion_scene_3_1_2  <--- Missing label

    if milking == -1:
        call potion_scene_11_1_2 #Returns
    #if milking == -3:
        #call potion_scene_11_3_2 <- label does not exist

    #Atoria / Tonks event return.
    #if astoria_tonks_event_in_progress:
        #jump astoria_tonks_event <- label does not exist #These do not return to 'night_resume'!

    label night_main_menu: # Use `jump main_room_menu` instead of jumping directly to this label

    call screen main_room_menu
