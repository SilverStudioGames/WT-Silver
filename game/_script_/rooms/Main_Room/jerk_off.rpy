
default jerk_off_choice = None # Last jerk-off fantasy

label jerk_off:
    hide screen bld1
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause 1

    call bld
    m "How should I finish this thing?"

    label how_to_finish:
    menu:
        "-Hermione's panties-" if hg_ps_get_panties.inProgress:
            $ jerk_off_choice = "hermione"
            $ her_panties_soaked = True

        "-LOCKED-" (style="disabled") if not hg_ps_get_panties.inProgress:
            ">You lack the item required for this option."
            jump how_to_finish

        "-Cho's panties-" if has_cho_panties:
            $ jerk_off_choice = "cho"
            $ cho_panties_soaked = True

        "-LOCKED-" (style="disabled") if not has_cho_panties:
            ">You lack the item required for this option."
            jump how_to_finish

        "-On the floor!-":
            $ jerk_off_choice = renpy.random.choice(["jasmine", "lara"])

    hide screen bld1
    show screen blktone
    call nar(">You decide to spend some time by jerking off...")
    pause.5

    if jerk_off_choice == "hermione":
        call nar(">You fantasise about Hermione...")
    elif jerk_off_choice == "cho":
        call nar(">You fantasise about Cho...")
    elif jerk_off_choice == "jasmine":
        call nar(">You fantasise about Princess Jasmine...")
    elif jerk_off_choice == "lara":
        call nar(">You fantasise about Lara Croft...")

    g4 "Yes... that's a good slut!"
    pause.5

    call nar(">You are ready to cum...")
    pause.2

    if jerk_off_choice == "hermione":
        g4 "Suck my almighty cock, you little whore!!!"
    elif jerk_off_choice == "cho":
        g4 "Suck my almighty cock, you exotic goddess!!!"
    elif jerk_off_choice == "jasmine":
        g4 "Suck my almighty cock, you princess-whore!!!"
    elif jerk_off_choice == "lara":
        g4 "Suck my almighty cock, you whore!!!"

    hide screen blktone
    call gen_chibi("cum_behind_desk")
    with hpunch
    pause 1

    if jerk_off_choice == "hermione":
        call nar(">You cum all over Hermione's panties, and then use them to wipe the cum off the floor...")
        call gen_chibi("cum_behind_desk_done")
    elif jerk_off_choice == "cho":
        call nar(">You cum all over Cho's panties, and then use them to wipe the cum off the floor...")
        call gen_chibi("cum_behind_desk_done")
    else:
        call nar(">You cum on the floor.")

    call gen_chibi("cum_behind_desk_done")
    pause.2

    call bld
    m "..."
    m "This was a pretty sweet jerk-off session..."
    m "Back to being productive!"

    call gen_chibi("sit_behind_desk")
    hide screen bld1

    if daytime:
        jump night_start
    else:
        jump day_start
