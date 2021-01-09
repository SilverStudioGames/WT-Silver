label day_start:
    call common_start(True)

    # Start Quests
    jump quests

    label day_resume:

    $ renpy.choice_for_skipping()

    # Favors
    if hg_pr_sex_skip: # Hermione does not show up. This sends to label where she shows up next morning.
        $ hg_pr_sex.start() # hg_pr_sex_T1_intro_E2

    label day_main_menu: # Use `jump main_room_menu` instead of jumping directly to this label

    $ renpy.choice_for_skipping()

    # Special first day event (examine objects in the room)
    if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined and not genie_intro.E2_complete:
        jump genie_intro_E2

    call screen main_room_menu
