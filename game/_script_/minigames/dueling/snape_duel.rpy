define genie_max_hp = 1000
define snape_max_hp = 2000

default genie_hp = genie_max_hp
default snape_hp = snape_max_hp

default blocking = False
default snape_blocking = False

default pentogram = False

default duel_OBJ = silver_duel()

init python:
    class silver_duel(object):
        in_progress = False
        snape = ""
        genie = ""

        def show(self,image=None,x=720,y=250,z=5):
            renpy.show(image,at_list=[Position(xpos=x, ypos=y, xanchor="center", yanchor="center")],layer="screens",zorder=z)
        def hide(self,image=None):
            renpy.hide(image,layer="screens")

label duel:
    ### DUEL ###
    $ d_flag_01 = False #Turns True after conversation triggered when Genie's HP runs low.
    $ d_flag_02 = False #Turns True after conversation triggered when Snape's HP runs low.

    # Hide all the screens.

    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen ui_top_bar
    hide screen ctc
    hide screen snape_defends
    call gen_chibi("hide")
    hide screen blkfade


    ### Set Duel Defaults ###
    $ genie_hp = genie_max_hp
    $ snape_hp = snape_max_hp

    $ blocking = False #True when "block" command is chosen, when Gennie turn into a guard.
    $ snape_blocking = False #True when Snape goes into defensive stance.
    $ pentogram = False #True when pentagram been casted an is displayed on the floor.
    $ used_tease = False
    $ in_action = False

    show screen duel
    show screen hp_bar

    hide screen snape_glass
    hide screen bld1
    with fade

    call bld
    m "This is foolish... You are no match for me..."
    call sna_main("Amusing...","snape_01", ypos="head", wand=True)
    m "{size=-4}(Actually my human body is quite weak...){/size}"
    m "{size=-4}(But I should still be way more powerful than any human wizard...){/size}"
    call sna_main("Let the duel begin!","snape_01", wand=True)
    hide screen bld1

    $ duel_OBJ.in_progress = True
    with d1

    jump duel_main

label duel_main:
    if blocking:
        $ duel_OBJ.show("smoke",x=520, y=318,z=5)
        $ duel_OBJ.genie = ""
        $ blocking = False

    if genie_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        call sna_main("Ready to give up yet?","snape_01", ypos="head", wand=True)
        g4 "*Tsk*..."

    if snape_hp <= 400 and not d_flag_02:
        $ d_flag_02 = True
        g4 "{size=-4}(He is getting weaker, I can feel it!){/size}"
        call sna_main("*Panting*","snape_01", ypos="head", wand=True)

    hide screen bld1
    call screen duel_buttons


screen duel_buttons():
    zorder 3

    imagebutton: # tease
        xpos 726
        yalign 1.0
        focus_mask True
        if not used_tease and not in_action:
            idle "images/dueling/snape/attack_tease.webp"
            hover image_hover("images/dueling/snape/attack_tease.webp")
            action [Jump("main_tease")]
        else:
            idle gray_tint("images/dueling/snape/attack_tease.webp")
            if not in_action:
                hover image_hover(gray_tint("images/dueling/snape/attack_tease.webp"))
                action [Jump("main_tease")]
    imagebutton: # attack
        xpos 802
        yalign 1.0
        focus_mask True
        if not in_action:
            idle "images/dueling/snape/attack_melee.webp"
            hover image_hover("images/dueling/snape/attack_melee.webp")
            action [Jump("main_attack")]
        else:
            idle gray_tint("images/dueling/snape/attack_melee.webp")
            if not in_action:
                hover image_hover(gray_tint("images/dueling/snape/attack_melee.webp"))
                action [Jump("main_attack")]
    imagebutton: # aguard
        xpos 868
        yalign 1.0
        focus_mask True
        if not in_action:
            idle "images/dueling/snape/attack_defend.webp"
            hover image_hover("images/dueling/snape/attack_defend.webp")
            action [Jump("main_defend")]
        else:
            idle gray_tint("images/dueling/snape/attack_defend.webp")
            if not in_action:
                hover image_hover(gray_tint("images/dueling/snape/attack_defend.webp"))
                action [Jump("main_defend")]
    imagebutton: # item
        xpos 954
        yalign 1.0
        focus_mask True
        if potions > 0 and not in_action:
            idle "images/dueling/snape/attack_item.webp"
            hover image_hover("images/dueling/snape/attack_item.webp")
            action [Jump("main_potion")]
        else:
            idle gray_tint("images/dueling/snape/attack_item.webp")
            if not in_action:
                hover image_hover(gray_tint("images/dueling/snape/attack_item.webp"))
                action [Jump("main_potion")]

label main_tease:
    $ in_action = True

    if not used_tease:
        $ used_tease = True
        call nar(">You turn around and start shaking your buttocks violently.")
        call sna_main("What the hell are you doing?","snape_05", wand=True)
        m ".......{w=1.0} teasing you?"
        call sna_main(".........","snape_14", wand=True)
        call sna_main("Stop mocking me!","snape_08", wand=True)
        call sna_main("Prepare to die!","snape_15", wand=True)
        g4 "shit!"
        hide screen bld1
        with d3
        pause 1
        #$ in_action = False
        jump snapes_turn
    else:
        m "No way I'm doing THAT again..."
        $ in_action = False
        jump duel_main

label main_attack:
    $ in_action = True

    if snape_blocking:
        $ snape_blocking = False
        pause 1
        jump snape_defends
    else:
        jump genie_attack

label main_defend:
    $ in_action = True
    $ blocking = True
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=520, y=318,z=5)
    $ duel_OBJ.genie = "defend"
    pause 1
    jump snapes_turn

label main_potion:
    $ in_action = True
    if potions > 0:
        jump potion
    else:
        m "Crap! I'm out of healing potions!"
        $ in_action = False
        jump duel_main

### SNAPE DEFENDS ### (Snape -0 HP)
label snape_defends:
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=520, y=318,z=5)
    $ duel_OBJ.show("snape_defend",x=720, y=250,z=4)
    $ duel_OBJ.snape = "block"
    pause 1
    $ renpy.play('sounds/attack_axe.mp3')

    pause 1.3
    hide screen duel_damage
    show screen duel_damage(0)

    $ duel_OBJ.hide("snape_defend")
    $ duel_OBJ.snape = ""
    $ duel_OBJ.genie = "barb"
    pause 1

    $ duel_OBJ.show("smoke",x=520, y=318, z=5)
    $ duel_OBJ.genie = ""
    pause 1

    jump snapes_turn

### GENIE ATTACK ### (Snape -100 HP)
label genie_attack:
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=520, y=318, z=5)
    $ duel_OBJ.show("genie_attack",x=720,y=250,z=4)
    $ duel_OBJ.genie = "attack"
    pause 1
    $ renpy.play('sounds/attack_axe.mp3')
    pause 1.8

    if pentogram:
        hide screen duel_damage
        if game.difficulty <= 1: #Easy
            show screen duel_damage(500)
            $ snape_hp -= 500
        elif game.difficulty == 2: #Normal
            show screen duel_damage(500)
            $ snape_hp -= 500
        else: #Hardcore
            show screen duel_damage(500)
            $ snape_hp -= 500
    else:
        hide screen duel_damage
        if game.difficulty <= 1: #Easy
            show screen duel_damage(300)
            $ snape_hp -= 300
        elif game.difficulty == 2: #Normal
            show screen duel_damage(200)
            $ snape_hp -= 200
        else: #Hardcore
            show screen duel_damage(100)
            $ snape_hp -= 100

    pause 1
    if snape_hp <= 100: #Check for gameover
        jump snape_lost

    $ duel_OBJ.show("smoke",x=520, y=318,z=5)
    $ duel_OBJ.hide("genie_attack")
    $ duel_OBJ.genie = ""
    pause 1

    jump snapes_turn


### SNAPE'S TURN ###
label snapes_turn:
    if pentogram:
        $ pentogram = False
        $ duel_OBJ.snape = "hand"
        $ duel_OBJ.show("hand",x=720, y=250,z=4)
        $ renpy.play('sounds/attack_snape3.ogg')
        pause 1.5
        $ renpy.play('sounds/attack_snape4.ogg')

        if blocking: # GENIE BLOCKS AGAINST THE HAND.(Genie -50 HP)
            $ duel_OBJ.hide("hand")
            $ duel_OBJ.genie = "hand"
            $ duel_OBJ.show("hand_guard",x=720, y=250,z=4)
            pause 1.8
            $ duel_OBJ.hide("hand_guard")
            $ duel_OBJ.snape = ""

            hide screen duel_damage
            if game.difficulty <= 1: #Easy
                show screen duel_damage(0, False)
            elif game.difficulty == 2: #Normal
                show screen duel_damage(100, False)
                $ genie_hp -= 100
            else: #Hardcore #Shouldn't increase the penalty if you blocked correctly...
                show screen duel_damage(100, False)
                $ genie_hp -= 100

            if genie_hp < 50: #Check for gameover
                jump genie_lost

            $ duel_OBJ.show("smoke",x=520, y=318,z=5)
            $ duel_OBJ.genie = ""
            $ in_action = False
            jump duel_main


        else: # GENIE DOESN'T BLOCK AGAINST THE HAND. (Genie -400 HP)
            $ duel_OBJ.hide("hand")
            $ duel_OBJ.genie = "hand"
            $ duel_OBJ.show("hand_genie")
            pause 1.3
            $ duel_OBJ.hide("hand_genie")
            $ duel_OBJ.snape = ""

            hide screen duel_damage
            if game.difficulty <= 1: #Easy
                show screen duel_damage(300, False)
                $ genie_hp -= 300
            elif game.difficulty == 2: #Normal
                show screen duel_damage(400, False)
                $ genie_hp -= 400
            else: #Hardcore
                show screen duel_damage(500, False)
                $ genie_hp -= 500

            if genie_hp < 50: #Check for gameover
                jump genie_lost

            $ duel_OBJ.genie = ""
            $ in_action = False
            jump duel_main


    else:
        if snape_blocking:
            $ snape_blocking = False
            if blocking:
                jump snape_attack_guard
            else:
                jump snape_attack

        $ snape_decides = renpy.random.randint(1, 2)

        if snape_decides in [1]: #BLOCK
            $ snape_blocking = True
            $ duel_OBJ.snape = "defend"
            pause 1
            $ in_action = False
            jump duel_main

        elif snape_decides in [2]:  #MAGIC. CASTS THE PICTOGRAM.
            $ duel_OBJ.snape = "hand"
            $ duel_OBJ.show("snape_summon",720,250,4)
            $ renpy.play('sounds/attack_snape2.ogg')
            pause.8
            $ pentogram = True
            pause 1
            $ duel_OBJ.hide("snape_summon")
            $ duel_OBJ.snape = ""
            $ in_action = False
            jump duel_main


### GENIE DRINKS POTION ### (-300 HP)
label potion:
    pause.5
    $ duel_OBJ.show("heal_02",500,330,4)
    $ renpy.play('sounds/attack_heal.ogg')
    pause 1

    hide screen duel_heal
    show screen duel_heal(300)
    pause 1
    $ potions -= 1
    $ genie_hp += 300
    pause.5

    $ duel_OBJ.hide("heal_02")

    jump snapes_turn



### SNAPE ATTACK ### (Genie -100 HP)
label snape_attack:
    hide screen duel_damage
    $ duel_OBJ.show("snape_attack",x=720, y=250,z=5)
    $ duel_OBJ.snape = "attack"
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.45
    $ duel_OBJ.hide("snape_attack")
    $ duel_OBJ.snape = ""

    hide screen duel_damage
    if game.difficulty <= 1: #Easy
        show screen duel_damage(100, False)
        $ genie_hp -= 100
    elif game.difficulty == 2: #Normal
        show screen duel_damage(100, False)
        $ genie_hp -= 100
    else: #Hardcore
        show screen duel_damage(300, False)
        $ genie_hp -= 300

    if genie_hp < 50: #Check for gameover
        jump genie_lost
    $ in_action = False
    jump duel_main

### SNAPE ATTACKS GUARD ### (-0 HP)
label snape_attack_guard:
    $ duel_OBJ.show("snape_attack_guard",x=720, y=250,z=5)
    $ duel_OBJ.snape = "attack"
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.5
    hide screen duel_damage
    show screen duel_damage(0, False)
    $ duel_OBJ.hide("snape_attack_guard")
    $ duel_OBJ.snape = ""
    pause 1
    $ in_action = False
    jump duel_main

### DUEL ###
screen duel():
    zorder 2

    if pentogram:
        add "pentogram" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")

    if duel_OBJ.genie in ["attack"] or duel_OBJ.snape in ["attack","block"]:
        pass
    else:
        if duel_OBJ.genie == "hand":
            pass
        elif duel_OBJ.genie == "no_magic":
            add "genie_no_magic" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.genie == "defend":
            add "ch_gen guard" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.genie == "barb":
            add "ch_gen barb" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")
        else:
            add "ch_gen duel_01" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")

        if duel_OBJ.snape == "hand":
            pass
        elif duel_OBJ.snape == "lost":
            add "snape_lost" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.snape == "defend":
            add "ch_sna defend" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")
        else:
            add "ch_sna duel_01" at Position(xpos=720, ypos=250, xanchor="center", yanchor="center")


screen hp_bar():
    zorder 3

    ### health bar is 271 px wide ###
    add "images/dueling/snape/hp_bar_02.webp" xpos int((genie_hp-genie_max_hp)/(genie_max_hp/271.0)) ypos 0
    add "images/dueling/snape/hp_bar.webp" #Genie avatr pic.

    ### health bar is 727 px wide ###
    add "images/dueling/snape/hp_bar_11.webp" #Black background for HP bar.
    add "images/dueling/snape/hp_bar_12.webp" xpos int((snape_max_hp-snape_hp)/(snape_max_hp/727.0)) ypos 0
    add "images/dueling/snape/hp_bar_10.webp" #Snape avatr pic.

    use duel_buttons

screen snape_defends(xx=0):
    add "ch_sna defend" at Position(xpos=-90+140+xx, ypos=-5)
    zorder 2

transform damage_transform:
    alpha 1.0
    linear 1.5 yoffset -100 alpha 0.0

screen duel_damage(value=0, attacking=True):
    tag damage
    frame:
        style "empty"
        at damage_transform
        if attacking:
            xpos 780
            ypos 120
        else:
            xpos 450
            ypos 120
        add "images/dueling/damage/"+str(value)+".webp"

screen duel_heal(value=300, player=True):
    tag damage
    frame:
        style "empty"
        at damage_transform
        if not player:
            xpos 780
            ypos 120
        else:
            xpos 450
            ypos 120
        add "images/dueling/damage/plus_"+str(value)+".webp"

### SNAPE LOSES ###
label snape_lost:
    $ pentogram = False
    $ duel_OBJ.show("smoke",x=520, y=318,z=5)
    $ duel_OBJ.hide("genie_attack")
    $ duel_OBJ.genie = ""
    $ duel_OBJ.snape = "lost"
    $ duel_OBJ.in_progress = False
    hide screen hp_bar
    hide screen duel_damage
    show screen ui_top_bar
    with flashbulb
    pause 1
    $ snape_intro.duel_complete = True
    jump snape_intro_E4

### GENIE LOSES ###
label genie_lost:
    $ renpy.music.stop(fadeout=4)
    $ renpy.music.stop(channel="weather", fadeout=4)
    $ renpy.play('sounds/level_failed.mp3')

    call gameover(autohide=False)
    hide screen duel
    hide screen hp_bar
    hide screen duel_damage

    pause 3

    menu:
        "-Try again-":
            $ renpy.play('sounds/glass_break.mp3')
            play music "music/boss_battle_#2_metal_loop.mp3" fadein 1 fadeout 1
            show screen snape_glass
            pause 2.3
            hide screen gameover
            $ potions = 3 # Give healing potions to make the fight less frustrating
            $ duel_OBJ.genie = ""
            jump duel

        "-Give up-":
            hide screen gameover
            jump credits

screen snape_glass():
    add "glass"
    zorder 21
