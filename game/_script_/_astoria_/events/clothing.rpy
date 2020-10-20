

#Door Events (Astoria wears random clothing.)

label astoria_summon_setup:

    # Reset doll state
    $ astoria.wear("all")
    $ astoria.set_cum(None)
    $ astoria_animation = None

    if astoria_outfits_schedule:
        $ astoria.equip_random_outfit()

    call play_sound("door")
    call ast_chibi("stand","mid","base")
    with d3

    #Astoria greeting.
    call play_music("astoria")

    if ast_mood > 0:
        if 5 > ast_mood >= 1:
            call ast_main("[ast_genie_name]?", "annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > ast_mood >= 5:
            call ast_main("What now?", "annoyed", "base", "worried", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > ast_mood >= 10:
            call ast_main("What is it, Dumby?", "annoyed", "base", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 30 > ast_mood >= 20:
            call ast_main("What do you want, \"Dumby\"?", "angry", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 40 > ast_mood >= 30:
            call ast_main("*Hmph*...", "annoyed", "narrow", "worried", "L", xpos="base", ypos="base", trans=d3)
        elif 50 > ast_mood >= 40:
            call ast_main("*Tsk*", "angry", "narrow", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif ast_mood >= 50:
            call ast_main("What?!", "scream", "narrow", "angry", "mid", xpos="base", ypos="base", trans=d3)
            call ast_main("", "angry", "narrow", "angry", "mid")

        call describe_mood("Astoria", ast_mood)
        call tutorial("moodngifts")
    else:
        if game.daytime:
            call ast_main("Mornin', [ast_genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
             call ast_main("Evenin', [ast_genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
