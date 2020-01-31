label setup_fireplace_hangout(char=None):

    if not daytime: # Night time
        show screen blkfade

        $ fire_in_fireplace = True

        call hide_characters
        call gen_chibi("hide")
        call sna_chibi("hide")
        call ton_chibi("hide")
        hide screen chair_right
        show screen desk

        show screen fireplace_fire
    else: # Daytime
        stop bg_sounds
        show screen blkfade

        $ fire_in_fireplace = False

        call hide_characters
        call gen_chibi("hide")
        call sna_chibi("hide")
        call ton_chibi("hide")
        hide screen chair_right
        show screen desk

    # Proceed as usual
    if char == "snape":
        show screen with_snape(ani=True)
    elif char == "tonks":
        show screen with_tonks_animated

    hide screen bld1
    hide screen blkfade
    with fade

    return
    
label slap_her:
    call play_sound("slap") #SLAP!
    show screen white
    with hpunch
    pause.08
    hide screen white

    return

label kiss_her:
    call play_sound("kiss") #Kiss!
    with hpunch
    pause.08

    return

label spit_on_her:
    call play_sound("spit") #Kiss!
    show screen white
    pause.2
    hide screen white
    with hpunch
    pause.08

    return

label cast_spell(spell=""):
    if spell in ["revelio","imperio"]:

        stop music fadeout 2.0
        call play_sound("spell")
        show screen white
        pause.1
        hide screen white
        with hpunch

    return
    
label cum_block:
    show screen white
    pause.1
    hide screen white
    pause.2
    show screen white
    pause.1
    hide screen white
    with hpunch

    return
    
label vague_idea:
    call nar(">You lack imagination for an idea of this caliber.")
    return

label increase_house_points(house, points):
    call bld
    $ renpy.play('sounds/win_04.mp3')
    show screen notes
    if house.startswith("g"):
        $ gryffindor += points
        ">Gryffindor has received [points] house points today!"
    elif house.startswith("h"):
        $ hufflepuff += points
        ">Hufflepuff has received [points] house points today!"
    elif house.startswith("r"):
        $ ravenclaw += points
        ">Ravenclaw has received [points] house points today!"
    else:
        $ slytherin += points
        ">Slytherin has received [points] house points today!"
    hide screen notes
    return

#TODO Check and fix teleport/heal effect position (chibis are now anchored bottom-left)
label teleport(position=None,effect=True,poof_label=None):
    if position == "genie":
        $ teleport_xpos = genie_chibi.pos[0]+75
        $ teleport_ypos = genie_chibi.pos[1]
        $ teleport_zorder = 3
    elif position == "hermione":
        $ teleport_xpos = hermione_chibi.pos[0]+45
        $ teleport_ypos = hermione_chibi.pos[1]
        $ teleport_zorder = 3
    elif position == "cho":
        $ teleport_xpos = cho_chibi.pos[0]+45
        $ teleport_ypos = cho_chibi.pos[1]
        $ teleport_zorder = 3
    elif position == "astoria":
        $ teleport_xpos = astoria_chibi.pos[0]+45
        $ teleport_ypos = astoria_chibi.pos[1]
        $ teleport_zorder = 3
    elif position == "desk":
        $ teleport_xpos = 320
        $ teleport_ypos = 160
        $ teleport_zorder = 1
        show screen desk
    else:
        $ teleport_xpos = position[0]
        $ teleport_ypos = position[1]
        $ teleport_zorder = 2

    if effect == True:
        $ renpy.play('sounds/magic4.ogg')
        show screen whitefade
        with d1

        hide screen whitefade
        with d1

        show screen blkfade
        with d1

        hide screen blkfade
        show screen heal_animation
        with d3

    #stop music fadeout 1

    hide screen heal_animation
    if poof_label != None:
        $ renpy.call(poof_label)
    show screen teleport_animation
    with d5

    hide screen teleport_animation
    with d5

    if effect == True:
        pause 1

    return

screen teleport_animation():
    add "teleport_ani" anchor (0.5, 0.7) xpos teleport_xpos ypos teleport_ypos zoom 0.5
    zorder teleport_zorder

screen heal_animation():
    add "heal_ani" anchor (0.5, 1.0) xpos teleport_xpos ypos teleport_ypos zoom 0.5
    zorder teleport_zorder

# Dummy labels. To prevent crashes. # TODO: Remove later.
label update_her_uniform:
    $ hermione_wear_top=False
    $ hermione_wear_bottom=False
    $ hermione_wear_bra=False
    $ hermione_wear_panties=False
    return
label reset_hermione:
    return
label h_equip_temp_outfit(outfit=None):
    return
label h_unequip_temp_outfit(outfit=None):
    return
default hermione_action = None
label set_her_action(action=None, update=None):
    $ hermione_action = action
    return