### House-Points ###

label points_changes: # Gets called every day/night.


    ####################
    ### Daily Points ###
    ####################

    ### House-Points Generator ###
    if gryffindor > slytherin:  # G is in the lead. How unfair!
        $ generating_points = 2 # 2 = Slytherin is guaranteed to get bonus points.
    else:
        $ generating_points = renpy.random.randint(1, 2) # 1 = No bonus points today.

    $ generating_points_gryffindor = renpy.random.randint(1, 10)
    $ generating_points_hufflepuff = renpy.random.randint(1, 10)
    $ generating_points_ravenclaw = renpy.random.randint(1, 10)

    ### Gryffindor ###
    if 3 <= generating_points_gryffindor <= 4:
        $ gryffindor += 1
    elif 5 <= generating_points_gryffindor <= 6:
        $ gryffindor += 2
    elif 7 <= generating_points_gryffindor <= 8:
        $ gryffindor += 3
    elif generating_points_gryffindor == 9:
        $ gryffindor += 5
    elif generating_points_gryffindor == 10:
        $ gryffindor += 11

    ###  Hufflepuff ###
    if 3 <= generating_points_hufflepuff <= 4:
        $ hufflepuff += 1
    elif 5 <= generating_points_hufflepuff <= 6:
        $ hufflepuff += 2
    elif 7 <= generating_points_hufflepuff <= 8:
        $ hufflepuff += 4
    elif generating_points_hufflepuff == 9:
        $ hufflepuff += 7
    elif generating_points_hufflepuff == 10:
        $ hufflepuff += 14

    ### Ravenclaw ###
    if 3 <= generating_points_ravenclaw <= 4:
        $ ravenclaw += 1
    elif 5 <= generating_points_ravenclaw <= 6:
        $ ravenclaw += 3
    elif 7 <= generating_points_ravenclaw <= 8:
        $ ravenclaw += 6
    elif generating_points_ravenclaw == 9:
        $ ravenclaw += 10
    elif generating_points_ravenclaw == 10:
        $ ravenclaw += 15

    ### Slytherin ###
    $ slytherin += renpy.random.randint(0, 2) # They get some points but not much.


    ########################
    ### Teacher's Favour ###
    ########################

    ### Gryffindor ###

    ### Hufflepuff ###
    if (gryffindor > hufflepuff) or (slytherin > hufflepuff) or (ravenclaw > hufflepuff):
        if generating_points == 1 and ton_support > 0: # Bonus points from Tonks.
            $ hufflepuff += ton_support

    ### Ravenclaw ###

    ### Slytherin ###
    if generating_points == 1 and game.difficulty >= 2: # Failed, no bonus points for S today.
        pass

    else: # Success, award bonus points to S today.
        # sna_support = number between 0 and 15
        # ton_support = number between 0 and 12
        # Tonks' is lower since you can do events with her to directly increase points.
        $ slytherin += (sna_support * renpy.random.randint(1, 3))
        $ slytherin += (ton_support * renpy.random.randint(1, 2))

    return
