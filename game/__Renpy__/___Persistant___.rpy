

### PERSISTANTS ###

label __init_variables:

    #place save variables here
    if not hasattr(renpy.store,'addicted'): #important!
        $ addicted = False
    if not hasattr(renpy.store,'first_time_7th'): #important!
        $ first_time_7th = True
    if not hasattr(renpy.store,'pitch_open'): #important!
        $ pitch_open = True
    if not hasattr(renpy.store,'inn_intro'): #important!
        $ inn_intro = False
    if not hasattr(renpy.store,'attic_open'): #important!
        $ attic_open = False
    if not hasattr(renpy.store,'tentacle_cosmetic'): #important!
        $ tentacle_cosmetic = False




    if not hasattr(renpy.store,'shaming'): #important!
        $ shaming = 0
    if not hasattr(renpy.store,'shaming_busy'): #important!
        $ shaming_busy = False
    if not hasattr(renpy.store,'shaming_01'): #important!
        $ shaming_01 = False
    if not hasattr(renpy.store,'shaming_02'): #important!
        $ shaming_02 = False
    if not hasattr(renpy.store,'shaming_03'): #important!
        $ shaming_03 = False


    if not hasattr(renpy.store,'heretic'): #important!
        $ heretic = 0
    if not hasattr(renpy.store,'heretic_01'): #important!
        $ heretic_01 = False
    if not hasattr(renpy.store,'heretic_02'): #important!
        $ heretic_02 = False
    if not hasattr(renpy.store,'heretic_03'): #important!
        $ heretic_03 = False
    if not hasattr(renpy.store,'heretic_busy'): #important!
        $ heretic_busy = False


    if not hasattr(renpy.store,'scene_number'): #important!
        $ scene_number = 1
    if not hasattr(renpy.store,'fawkes_intro_done'): #important!
        $ fawkes_intro_done = True


    ### Interface ###
    if not hasattr(renpy.store,'interface_color'):
        $ interface_color = "gold"

    ### Difficulty ###
    if not hasattr(renpy.store,'game_difficulty'):
        $ game_difficulty = 2                      # 2 = normal
        $ hardcore_difficulty_active = False       # for hardcore play-through rewards

    ### Gameplay ###
    if not hasattr(renpy.store,'ignore_warning'):
        $ ignore_warning = False #Warning message that tells you which ending you will get.

    ### Cheats ###
    if not hasattr(renpy.store,'cheats_active'): #important!
        $ cheats_active = False
    if not hasattr(renpy.store,'force_unlock_pub_favors'): #important!
        $ force_unlock_pub_favors = False
    if not hasattr(renpy.store,'skip_duel'): #important!
        $ skip_duel = False
    if not hasattr(renpy.store,'skip_to_hermione'): #important!
        $ skip_to_hermione = False
    if not hasattr(renpy.store,'next_day'): #important!
        $ next_day = False





    if not hasattr(renpy.store,'pub_q_sex_teach'): #important!
        $ pub_q_sex_teach = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_Flag'): #important!
        $ hg_pf_TheGamble_Flag = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagA'): #important!
        $ hg_pf_TheGamble_FlagA = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagB'): #important!
        $ hg_pf_TheGamble_FlagB = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagC'): #important!
        $ hg_pf_TheGamble_FlagC = False



    ###Tutoring fix
    if not hasattr(renpy.store,'table_position_x'): #important!
        $ table_position_x = 20

    ###MISC
    if not hasattr(renpy.store,'unlocked_7th'): #important!
        $ unlocked_7th = False
        $ found_puzzle_1 = False
        $ charName = "genie"

    #Phoenix
    if not hasattr(renpy.store,'phoenix_is_fed'):
        $ fawkes_intro_done = False
        $ phoenix_is_fed = False
        $ phoenix_is_petted = False
        $ phoenix_fed_counter = 0
        $ phoenix_petted_counter = 0




    #HD RESCALE RATION
    if not hasattr(renpy.store,'genie_scaleratio'): #important!
        $ scaleratio = 2 #BECAUSE THE IMAGES ARE 2X LARGER

        $ genie_scaleratio = 2 #Scaleratio of each character can be changed to be used in custom "CG" scenes. Made larger, more zoomed in,...
        $ snape_scaleratio = 2
        $ tonks_scaleratio = 2

        $ hermione_scaleratio = 2
        $ luna_scaleratio = 2
        $ astoria_scaleratio = 2
        $ susan_scaleratio = 2
        $ cho_scaleratio = 2

    ###CGs
    if not hasattr(renpy.store,'ccg_folder'): #important!
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg2 = 1
        $ ccg3 = "gene"

    #SC34 update 2 stuff, thanks akabur.
    if not hasattr(renpy.store,'sc_cg_base'): #important!
        $ sc_cg_base = "images/CG/sc34/1/base_1.png"
        $ sc_cg_image_1 = "images/CG/sc34/1/A_1.png"
        $ sc_cg_image_2 = "images/CG/sc34/2/B_1.png"
        $ sc_cg_image_3 = "images/CG/sc34/2/C_1.png"
        $ sccgxpos = 200
        $ sccgypos = 50

    #Using images instead of chibis.
    if not hasattr(renpy.store,'face_on_cg'): #important!
        $ face_on_cg = False #"call her_main(,ypos="head")" will use screen "her_face". Face gets positioned automatically.
        $ use_cgs = False



    #Reset Persistants
    if not hasattr(renpy.store,'reset_persistants'): #Turns true when creating a new game only.
        $ reset_persistants            = False

    if not hasattr(renpy.store,'reset_cho_content'):
        $ reset_luna_content = False
        $ reset_cho_content = False

    #Genie Init
    call genie_init

    #Snape Init
    call snape_init
    call snape_progress_init

    #Hermione Init
    call her_init #Defines newly added variables. Resets variables after creating a new game.
    call her_clothing_lists_init #Lists update every time!
    call her_progress_init #Defines newly added variables. Resets variables after creating a new game.

    #Luna Init
    call luna_init
    call luna_progress_init

    #Cho Init
    call cho_init
    call cho_progress_init

    #Susan Init
    call susan_init
    call susan_progress_init

    #Astoria Init
    call astoria_init
    call astoria_progress_init

    #Tonks Init
    call tonks_init
    call tonks_progress_init

    call wardrobe_init

    # Store Init
    call store_init
    call store_items_init

    call clothing_init

    call cheats_init

    label update_unlocked_character_list:
    $ unlocked_character_list = ["genie"]
    if snape_unlocked:
        $ unlocked_character_list.append("snape")
    if hermione_unlocked:
        $ unlocked_character_list.append("hermione")
    if luna_unlocked:
        $ unlocked_character_list.append("luna")
    if astoria_unlocked:
        $ unlocked_character_list.append("astoria")
    if susan_unlocked:
        $ unlocked_character_list.append("susan")
    if cho_unlocked:
        $ unlocked_character_list.append("cho")
    if tonks_unlocked:
        $ unlocked_character_list.append("tonks")




    ### Do not add anything after this line !!!


    #Update or Reset Persistants
    call update_persistants # Reset/update old vars for a specific update here! To make it compatible with older saves/prevent crashes!

    return
