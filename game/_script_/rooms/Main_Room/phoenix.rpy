label phoenix:

    if not bird_examined:
        $ bird_examined = True
        call gen_chibi("stand","mid","base",flip=False)
        show screen chair_left
        show screen desk
        with d5
        m "*Hmm*..."
        m "Even this weird-looking bird radiates magic..."
        call gen_chibi("sit_behind_desk")
        with d5
        jump main_room_menu

    if not phoenix_is_fed:
        $ phoenix_is_fed = True
        $ phoenix_fed_counter += 1
        jump feeding
    if phoenix_is_fed and not phoenix_is_petted:
        $ phoenix_is_petted = True
        $ phoenix_petted_counter += 1
        jump petting

    jump main_room_menu

label feeding:
    show screen chair_left
    show screen desk
    call gen_chibi("grab_high", phoenix_OBJ.xpos, phoenix_OBJ.ypos+365, flip=False) # Note: Flip is inconsistent
    with d3
    pause .5

    show screen phoenix_food
    with d3

    $ random_number = renpy.random.randint(1, 3)
    if random_number == 1:
        m "There you go..."
    elif random_number == 2:
        m "Eat up, buddy."
    else:
        pause .8

    jump main_room_menu

label petting:
    show screen chair_left
    show screen desk
    call gen_chibi("petting", phoenix_OBJ.xpos, phoenix_OBJ.ypos+270, flip=False) # Note: Flip is inconsistent
    with d3
    pause .5

    $ random_number = renpy.random.randint(1, 5)
    if random_number == 1:
        m "Who's a good bird?"
    elif random_number == 2:
        "*Pat *Pat *Pat..."
    elif random_number == 3:
        "Glad you aren't as noisy as Iago..."
    else:
        pause 2.4

    jump main_room_menu
