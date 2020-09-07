
default DRgame = DarkRoomGame()

default DRplayer   = DarkRoomCharacter(name="You",          hp=8, skills=["strength"],              unskilled=["cooking","hunting","sewing"], inventory=["axe"])
default DRstranger = DarkRoomCharacter(name="The Stranger", hp=7, skills=["hunting"],               unskilled=["sewing"],                     inventory=["knife"])
default DRmaid     = DarkRoomCharacter(name="The Maiden",   hp=3, skills=["sewing"],                unskilled=["hunting","strength"])
# default DRmaid     = DarkRoomCharacter(name="The Maiden",   hp=3, skills=["cooking"],               unskilled=["hunting"],                    inventory=[])
default DRhunter   = DarkRoomCharacter(name="The Hunter",   hp=7, skills=["hunting","sewing"],      unskilled=["cooking"],                    inventory=["knife","rifle"])

label reset_dark_room_init:
    $ reset_variables(
        "DRgame",
        "DRplayer",
        "DRstranger",
        "DRmaid",
        "DRhunter"
    )
    return

### A Dark Room ###

label start_dark_room_game:
    call play_music("stop")
    show screen blkfade
    with d9

    $ temp_time = daytime

    $ daytime = False
    call update_interface_color

    call hide_screens
    pause 2

    centered "{size=+7}{color=#cbcbcb}A Dark Room{/color}{/size}"

    pause 2

    label dark_room_game_start_menu:
    menu:
        "-Start a new Game-":
            call reset_dark_room_init
            jump dark_room_main
        "-Continue-" if DRgame.day > 1 and not DRgame.game_over:
            jump dark_room_load_save
        "-Get coin rewards-" if DRgame.day > 1 and not DRgame.game_over:
            ">You'll get gold for each day you have survived in the game.\n>This will delete your current Save!"
            menu:
                "Would you like to delete your save and get gold coins for it?"
                "-Yes-":
                    $ current_payout = DRgame.day*2
                    $ gold += current_payout
                    ">You have received {number=current_payout} gold.\n>Thank you for playing \"A Dark Room\"."
                    call reset_dark_room_init
                    jump dark_room_game_start_menu
                "-No-":
                    jump dark_room_game_start_menu
            jump dark_room_load_save
        "-Never mind-":
            jump enter_room_of_req

label dark_room_main:
    show screen blkfade
    with d9

    #Reset
    hide screen fireplace_fire
    $ DRgame.time = "morning"
    $ DRgame.fire = 0
    $ read_book = False
    call update_DRgame_random_number
    call update_DRgame_meat_spoiling
    call update_DRgame_needs

    label dark_room_load_save:

    call play_music("stop")

    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    if DRgame.day in [1,2,3,6,7]:
        $ set_weather("storm")
    elif DRgame.day in [4,5]:
        $ set_weather("clear")
    else:
        $ set_weather()
    call weather_sound

    pause 2
    centered "{size=+7}{color=#cbcbcb}Day [DRgame.day]{/color}{/size}"
    pause 1

    label DRgame_resume:
    if DRgame.game_over:
        show screen blkfade
        with d5
        pause 1
        centered "{size=+7}{color=#cbcbcb}Game Over...{/color}{/size}"
        pause 1
        centered "{size=+7}{color=#cbcbcb}You made it to day [DRgame.day]!{/color}{/size}"
        pause 1
        jump enter_room_of_req

    show screen weather
    show screen dark_room
    if DRgame.fire >= 1:
        show screen fireplace_fire
    else:
        hide screen fireplace_fire
    hide screen DRgame_blktone
    show screen DRgame_blktone
    call DRgame_chibis #Sets up character chibis & positions.
    hide screen blkfade
    with d9

    if DRgame.time == "morning":
        call DRgame_random_event
        call screen DRgame_menu #Do something.

    if DRgame.time == "noon":
        call DRgame_leave_for_task #Characters Leave
        call DRgame_random_event
        call screen DRgame_menu #Do another thing.

    if DRgame.time == "afternoon":
        call DRgame_return_from_task #Characters Return
        call update_DRgame_hunger #Eating
        call DRgame_random_event

    if DRgame.time == "night":
        call update_DRgame_sickness
        call DRgame_random_event

    if DRgame.game_over:
        show screen blkfade
        with d5
        pause 1
        centered "{size=+7}{color=#cbcbcb}Game Over...{/color}{/size}"
        pause 1
        centered "{size=+7}{color=#cbcbcb}You made it to day [DRgame.day]!{/color}{/size}"
        pause 1
        jump enter_room_of_req

    #Jump next day
    call nar(">Night gathers...\nAnd a new day begins.")
    $ DRgame.day += 1
    jump dark_room_main



label update_DRgame_random_number:
    python:
        for i in DRgame.characters:
            i.random_number = renpy.random.randint(1, 4) #1 is lucky, 4 is not
    return


label DRgame_chibis:

    call gen_chibi("hide")
    call sna_chibi("hide")

    #Player
    $ genie_chibi.zorder = 1
    if DRplayer in DRgame.characters:
        call gen_chibi("stand",710,165+250,flip=False)

    #Stranger
    $ snape_chibi.zorder = 1
    if DRstranger in DRgame.characters:
        if DRstranger.location != "outside":
            call sna_chibi("stand",450,180+250,flip=True)

    return


label update_DRgame_needs:
    python:
        for i in DRgame.characters:
            i.hunger -= 1
            if i.task == "" and i.hp < 10 and i != DRplayer:
                i.hp += 1

        for i in DRgame.characters:
            if i.sick == False:
                if (i.hunger < 5 and i.hp < 6 and i.random_number in [4]) or i.hp < 2:
                    i.sick = True
                    if i.name == "You":
                        renpy.say(None,"You have gotten ill.")
                    else:
                        renpy.say(None,"[i.name] has gotten ill.")
            if i.sick:
                i.force_task = False
                i.task = ""

    return


label update_DRgame_sickness:
    python:
        for i in DRgame.characters:
            if i.sick:
                if i.hp >= 6 and i.hunger >= 3 and DRgame.fire >= 1:
                    i.sick = False
                    renpy.say(None,"[i.namse] looks to be a lot healthier. Their sickness seems to be gone.")

    return


label update_DRgame_meat_spoiling:
    $ random_number = renpy.random.randint(1, 5)
    if random_number in [1]:
        $ DRgame.meat -= 5
    if random_number in [2]:
        $ DRgame.meat -= 3
    if DRgame.meat < 0:
        $ DRgame.meat = 0
    return


label update_DRgame_hunger:
    if DRgame.meals <= 0:
        "There was no food left to eat."
        "If this continues, you will starve..."
        return
    if DRgame.fire <= 0 and DRgame.wood >= 1:
        "There was no fire to heat up the meal..."
        menu:
            "-Stoke the fire-":
                $ DRgame.fire = 1
                $ DRgame.wood -= 1
                show screen fireplace_fire
                with d5
    if DRgame.fire <= 0 and DRgame.wood <= 0:
        "You had no more wood to heat up the fire..."
        "You turn back to your tasks hungry..."
        return

    python:
        for i in DRgame.characters:
            if DRgame.meals >= 1:
                if i.sick: #Priority
                    if i.hunger < 7:
                        i.hunger += 1
                        DRgame.meals -= 1
                else:
                    if i.hunger < 7:
                        i.hunger += 1
                        DRgame.meals -= 1
        for i in DRgame.characters:
            if DRgame.meals >= 1:
                if i.sick: #Priority
                    if i.hunger < 10:
                        i.hunger += 1
                        DRgame.meals -= 1
                else:
                    if i.hunger < 10:
                        i.hunger += 1
                        DRgame.meals -= 1

    if DRgame.time in ["afternoon"]:
        "A long day of work... it was time to eat..."
    if DRgame.meals <= 0:
        "All food that was left got eaten..."

    return


label DRgame_leave_for_task:
    python:
        for i in DRgame.characters:
            if i.task in ["wood_cutting","hunting"]:
                if weather in ("clear", "cloudy", "overcast"):
                    i.location = "outside"
                elif i.force_task == True:
                    i.location = "outside"
                else:
                    i.location = "room"

    call DRgame_chibis
    with d5

    return

label DRgame_return_from_task: #renpy.say(None,"[i.name] has gotten ill.")
    python:
        for i in DRgame.characters:
            if i.location == "outside":
                i.location = "room"

    call DRgame_chibis
    with d5

    python:
        for i in DRgame.characters:

            #Hunting
            if i.task == "hunting" and weather in ("clear", "cloudy", "overcast") or i.force_task == True: #They were hunting.
                temp_item = 2
                if weather in ("blizzard", "snow", "storm", "rain"):
                    temp_item -= 1
                    if i.hp > 1:
                        i.hp -= 1
                if "hunting" in i.unskilled:
                    temp_item -= 1
                if "hunting" in i.skills:
                    temp_item += 1
                if temp_item == 3 or (temp_item == 2 and "knife" in i.inventory):
                    temp_item += 1

                #Deer
                if "bow" in i.inventory and "arrows" in i.inventory and "hunting" not in i.unskilled:
                    if i.random_number in [1,2]:
                        temp_item = 5 #Deer
                    else:
                        temp_item = 4 #Fox

                DRgame.meat += temp_item
                renpy.say(None,"[i.name] came back from the hunt, hungry and freezing.")
                if weather in ("blizzard", "snow", "storm", "rain"):
                    renpy.say(None,"The cold rains have shown its mark on them...")
                if temp_item >= 5:
                    renpy.say(None,"A large deer on their back. This will last a couple of days.")
                    renpy.say(None,"Its leather seems almost untouched.")
                    DRgame.leather += renpy.random.randint(2, 3)
                elif temp_item in [3,4]:
                    renpy.say(None,"They found a small fox. Should be good enough to eat...")
                    renpy.say(None,"Its fur will help with the cold.")
                    DRgame.fur += renpy.random.randint(1, 2)
                elif temp_item == 2:
                    renpy.say(None,"They found a wild chicken.")
                    renpy.say(None,"The feathers will make good arrows")
                    DRgame.feathers += renpy.random.randint(4, 8)
                elif temp_item == 1:
                    renpy.say(None,"They only caught a small rabbit. There won't be much to eat it seems...")
                else:
                    renpy.say(None,"They were unsuccessful and couldn't find any wild animals in the thick snow.")

            #Wood Chopping/Gathering
            if i.task == "chopping_wood" and weather in ("clear", "cloudy", "overcast") or i.force_task == True: #They were gathering wood/chopping wood.
                temp_item = 3
                if weather in ("blizzard", "snow", "storm", "rain"):
                    temp_item -= 1
                    if i.hp > 1:
                        i.hp -= 1
                if "strength" in i.unskilled:
                    temp_item -= 1
                if "strength" in i.skills:
                    temp_item += 1
                if "axe" in i.inventory:
                    temp_item += 1

                DRgame.wood += temp_item
                if "axe" in i.inventory:
                    renpy.say(None,"[i.name] came back from chopping wood.")
                    renpy.say(None,"They chopped [temp_item] piles with their axe.")
                else:
                    renpy.say(None,"[i.name] came back from gathering wood.")
                    if temp_item == 1:
                        renpy.say(None,"They gathered [temp_item] pile of wood out in the forest.")
                    else:
                        renpy.say(None,"They gathered [temp_item] piles of wood out in the forest.")

    return

label DRgame_random_event:
    if DRgame.day == 1:
        if DRgame.time in ["morning"]:
            if "intro" not in DRgame.events:
                $ DRgame.events.append("intro")
                call play_music("night_outside")
                pause 2
                "Wind howls throughout the night."
                "A merciless cold, creeps into every part of your bones..."
                "You've been walking through a raging blizzard for what felt like hours, the cold biting deep into your skin..."
                pause 2
                "And then you finally found it..."
                "An empty wood cabin. No lights. No sound. Not a soul."
                pause 1
                "Shelter, at last..."
                pause 2
                call play_music("stop")
                call play_sound("door")
                pause.5
                call gen_chibi("stand","door","base",flip=False)
                with d5
                pause.8
                "The cabin, its walls strong against the harsh winds... but still as cold as the outside..."
                "You need to take action... Fast..."
                $ DRgame.characters.append(DRplayer)

    if DRgame.day in [3,5]:
        if DRgame.time in ["noon"]:
            if "stranger_intro" not in DRgame.events:
                if DRgame.day == 3:
                    call play_sound("knocking")
                    pause.2
                    call gen_chibi("hide")
                    with d3
                    call gen_chibi("stand","mid","base")
                    with d5
                    pause.5
                    "A strong knocking halls through the nearly empty cabin."
                    "It's a man. Stranger, he calls himself..."
                    "The cold has been taking its toll on him."
                    "He promises you help, for shelter..."
                    pause.8
                    "Will you let him in?"
                    menu:
                        "-Let him in-":
                            $ DRgame.events.append("stranger_intro")
                            $ DRgame.characters.append(DRstranger)
                            $ DRstranger.location = "room"
                            pause.5
                            call play_sound("door")
                            call sna_chibi("stand","door","base")
                            with d5
                            pause.8
                            "The stranger is more than thankful to you."
                            "He'd be happy to help gather wood or hunt meat."
                        "-Tell him to leave-":
                            "The stranger reluctantly leaves."
                            $ DRgame.time = "afternoon"
                            return
                elif DRgame.day == 5:
                    call play_sound("knocking")
                    pause.2
                    call gen_chibi("hide")
                    with d3
                    call gen_chibi("stand","mid","base")
                    with d5
                    pause.5
                    "Another loud knocks at the sturdy cabin door."
                    "Once again, it's the stranger..."
                    "He has no more food, no more water, so he says..."
                    "He is making a threat. You will regret this, he tells you..."
                    pause.8
                    menu:
                        "-Let him in-":
                            $ DRgame.events.append("stranger_intro")
                            $ DRgame.characters.append(DRstranger)
                            $ DRstranger.location = "room"
                            pause.5
                            call play_sound("door")
                            call sna_chibi("stand","door","base")
                            with d5
                            pause.8
                            "The stranger is more than thankful to you."
                            "He'd be happy to help gather wood or hunt for meat."
                        "-Let him starve-":
                            "He quietly leaves."
                            $ DRgame.time = "afternoon"
                            return
    #Afternoon
    if DRgame.time in ["afternoon"]:

        #Fire goes out.
        $ random_number = renpy.random.randint(1, 5)
        if random_number in [1,2] and DRgame.fire in [1]:
            $ DRgame.fire = 0
            stop bg_sounds
            hide screen DRgame_blktone
            show screen DRgame_blktone
            hide screen fireplace_fire
            with d9
            pause.8
            call nar(">The fire wasn't strong enough.\nIt failed fighting the bitter cold, and went out...")
            pause.8

        $ DRgame.time = "night"

    #Night
    if DRgame.time in ["night"]:

        if DRgame.day == 6 and "stranger_intro" not in DRgame.events:
            call play_music("night_outside")
            show screen blkfade
            with d5
            pause .8
            "In the night, you quietly woke up."
            "You thought someone was moving outside of the cabin."
            "You heard a clashing sound of metal hitting stone..."
            "Followed closely by a sound that was only too familiar..."
            call play_music("stop")
            play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
            pause.8
            "The sound that had been the only comfort in the last few days in this cold winter, now made you feel dread..."
            "It was fire! The cabin was slowly burning from every side, more and more."
            call play_music("hitman")
            "You hurried across the empty room towards the only way that went outside"
            "You unhinged the metal locks on the heavy door."
            call play_sound("bump")
            "But the large door wouldn't move... It was barricaded from the outside..."
            call play_sound("bump")
            pause.8
            call play_sound("bump")
            pause.6
            call play_sound("bump")
            "With no way out, you grabbed your axe and started tearing down the wooden door..."
            pause.5
            call play_sound("bump")
            pause.6
            call play_sound("bump")
            pause.8
            call play_sound("bump")
            call play_music("stop")
            "The heat grew unbearable. At last, you dropped your axe and sank to the floor."
            "The cabin burned down over the night, into a pile of ash and snow..."
            "You didn't make it out..."
            $ DRgame.game_over = True

        if not DRgame.game_over:
            $ temp_name = ""
            python:
                for i in DRgame.characters:
                    if i.sick:
                        if i.random_number in [4] and DRgame.fire == 0:
                            DRgame.characters.remove(i)
                            temp_name = i.name
            if temp_name != "":
                show screen blkfade
                with d9
                "A long-fought battle against illness has been lost..."
                pause 2
                if DRplayer not in DRgame.characters:
                    "You died in the night..."
                    $ DRgame.game_over = True
                else:
                    "[temp_name], has died in the night."

        $ DRgame.time = "morning"

    return


screen dark_room():
    add "images/rooms/_bg_/main_room_night.webp"

    add "images/rooms/_objects_/doors/door_idle_night.webp" at Position(xpos=898, ypos=315, xanchor="center", yanchor="center")
    add "images/rooms/_objects_/fireplace/fireplace_w_shadow.webp" at Position(xpos=693, ypos=277, xanchor="center", yanchor="center")
    if read_book:
        if DRgame.fire == 0:
            add "ch_gen read" xpos 350 ypos 205
        else:
            add "ch_gen read_near_fire" xpos 350 ypos 205
    else:
        use chair_left
    add "images/rooms/main_room/desk_with_shadow.webp" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5

    zorder 0

screen DRgame_blktone(): #Use this instead of "blktone", or it will cause issues with chibis.
    tag DRgame_blktone
    if DRgame.fire <= 0:
        add Color("#000", alpha=0.7)
    elif DRgame.fire == 1:
        add Color("#000", alpha=0.3)
    zorder 4

screen DRgame_menu():
    tag DRgame_menu

    #Door
    imagebutton:
        xpos 898
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/_objects_/doors/door_idle.webp"
        hover "images/rooms/_objects_/doors/door_hover.webp"
        action [Hide("DRgame_menu"), Jump("DRgame_door")]

    #Fireplace
    imagebutton:
        xpos 693
        ypos 277
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/_objects_/fireplace/fireplace_idle.webp"
        hover "images/rooms/_objects_/fireplace/fireplace_hover.webp"
        action [Hide("DRgame_menu"), Jump("DRgame_fireplace")]

    #Chair left chair_left
    imagebutton:
        xpos 332
        ypos 300
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/main_room/chair_left_no_shadow.webp"
        hover yellow_tint("images/rooms/main_room/chair_left_no_shadow.webp")
        action [Hide("DRgame_menu"), Jump("dark_room_chair_left")]

    #Desk
    imagebutton:
        xpos 360
        ypos 330
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/main_room/desk_no_shadow.webp"
        hover yellow_tint("images/rooms/main_room/desk_no_shadow.webp")
        action [Hide("DRgame_menu"), Jump("dark_room_desk")]

    #Player
    imagebutton:
        xpos genie_chibi.pos[0]
        ypos genie_chibi.pos[1]
        focus_mask True
        #xanchor "center"
        #yanchor "center"
        if not genie_chibi.flip:
            idle "ch_gen stand"
            hover yellow_tint("ch_gen stand")
        else:
            idle im.Flip("ch_gen stand", horizontal=True)
            hover yellow_tint( im.Flip("ch_gen stand", horizontal=True) )
        action [Hide("DRgame_menu"), Jump("dark_room_player")]

    #Stranger
    if DRstranger in DRgame.characters and DRstranger.location not in ["outside"]:
        imagebutton:
            pos sna_chibi.pos
            focus_mask True
            #xanchor "center"
            #yanchor "center"
            if not snape_chibi.flip:
                idle "ch_sna stand"
                hover yellow_tint("ch_sna stand")
            else:
                idle im.Flip("ch_sna stand", horizontal=True)
                hover yellow_tint( im.Flip("ch_sna stand", horizontal=True) )
            action [Hide("DRgame_menu"), Jump("dark_room_stranger")]

    if DRmaid in DRgame.characters and DRmaid.location in ["room","desk","fireplace"]:
        imagebutton:
            pos hermione_chibi.pos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle hermione_chibi_blink
            hover yellow_tint(hermione_chibi_blink)
            action [Hide("DRgame_menu"), Jump("dark_room_maid")]

    zorder 1


#Fireplace
label DRgame_fireplace:
    if DRgame.wood >= 1 and DRgame.fire <= 0:
        $ DRgame.fire += 1
        $ DRgame.wood -= 1
        show screen fireplace_fire
        with d9
        pause 1
        "The fire is burning..."
        jump DRgame_fireplace
    elif DRgame.wood <= 0 and DRgame.fire <= 0:
        call nar(">You don't have any more wood to burn.\nSoon you will all freeze to death.")
        jump DRgame_resume

    menu:
        "-Stoke the fire-" if DRgame.wood >= 1 and DRgame.fire < 2:
            $ DRgame.fire += 1
            $ DRgame.wood -= 1
            show screen fireplace_fire
            with d9
            pause 1
            if DRgame.fire == 1:
                "The fire is burning..."
            if DRgame.fire == 2:
                "The fire is roaring..."
                "It will burn until night falls."
        "{color=[menu_disabled]}-Stoke the fire-{/color}" if DRgame.wood < 1 or DRgame.fire >= 2:
            if DRgame.fire >= 2:
                call nar(">The fire burns more than enough.")
            else:
                call nar(">You don't have any more wood to burn.\nSoon you will all freeze to death.")
        "-Cook some meat-" if DRgame.fire >= 1 and DRgame.meat >= 1:
            jump DRgame_cook_meat
        "{color=[menu_disabled]}-Cook some meat-{/color}" if DRgame.fire >= 1 and DRgame.meat < 1:
            call nar(">You don't have any meat to cook.")
        "-Leave the fireplace-":
            jump DRgame_resume
    jump DRgame_fireplace

label DRgame_cook_meat:
    call DRgame_advance_time

    $ temp_number = 1
    if DRgame.meat == 1:
        $ temp_number = 1
    elif DRgame.meat == 2:
        $ temp_number = 2
    elif DRgame.meat >= 3:
        $ temp_number = 3

    $ DRgame.meat -= temp_number
    $ DRgame.meals += temp_number

    if temp_number in [1]:
        "With barely any meat left, you were able to cook a small stew..."
    if temp_number in [2]:
        "There was enough meat to cook a decent stew..."
    if temp_number in [3]:
        "You were able to cook a rather large stew with meat."
    jump DRgame_resume


#Door
label DRgame_door:
    menu:
        "-Chop Wood-":
            jump DRgame_chop_wood
        "-Hunt for Animals-":
            jump DRgame_hunt_animals
        "-Leave the door-":
            jump DRgame_resume


label DRgame_chop_wood:
    call DRgame_advance_time

    call play_sound("door")
    call gen_chibi("hide")
    with d5
    pause.2
    call play_music("night")
    pause.8


    $ temp_number = 1
    if DRplayer.random_number in [1]:
        $ temp_number += 2
    if DRplayer.random_number in [2]:
        $ temp_number += 1
    if DRplayer.random_number in [4]:
        $ temp_number -= 1
    if "strength" in DRplayer.skills:
        $ temp_number += 1

    $ DRgame.wood += temp_number

    call gen_chibi("stand","door","base",flip=False)
    with d5

    "Exhausted you return to the cabin..."
    "You were able to gather and chop [temp_number] pieces of wood."

    if weather in ("blizzard", "snow", "storm", "rain"):
        $ DRplayer.hp -= 1
        "The ruthless weather has shown its mark on you. You shouldn't have gone out there."
        "But there was no other choice..."

    jump DRgame_resume


label DRgame_hunt_animals:
    call DRgame_advance_time

    call play_sound("door")
    call gen_chibi("hide")
    with d5
    pause.2
    call play_music("night")
    pause.8

    $ temp_number = 1
    if DRplayer.random_number in [1]:
        $ temp_number += 2
    if DRplayer.random_number in [2]:
        $ temp_number += 1
    if DRplayer.random_number in [4]:
        $ temp_number -= 1
    if weather in ("blizzard", "snow", "storm", "rain"):
        $ temp_number -= 1

    $ DRgame.meat += temp_number

    call gen_chibi("stand","door","base",flip=False)
    with d5

    "You returned from the hunt..."
    if temp_number <= 0:
        "You were unsuccessful, and couldn't find any wild animals in the thick snow."
    elif temp_number == 1:
        "You only caught a small rabbit."
    elif temp_number == 2:
        "You found a wild chicken."
    else:
        "You found a small fox. Should be good enough to eat..."

    if weather in ("blizzard", "snow", "storm", "rain"):
        $ DRplayer.hp -= 1
        "The ruthless weather has shown its mark on you. You shouldn't have gone out there."
        "But there was no other choice..."

    jump DRgame_resume

#Chair Left
label dark_room_chair_left:
    call gen_chibi("hide")
    hide screen dark_room
    $ read_book = True
    show screen dark_room
    with d5
    pause.8
    "In a drawer, you found a dusty old book...\nYou decide to read it..."
    if DRgame.fire <= 0:
        "The words written on the pages, merge with the long darkness of the night."
        "For a minute, you stare into the dark, cold, and empty room, wondering if you will ever leave this place alive..."
        "You place the book back to where it was..."
    else:
        "You read through the pages, glued to every word."
        if DRgame.characters == [DRplayer]:
            "It helps you cope with your new found loneliness..."
        if DRplayer.hp < 10:
            $ DRplayer.hp += 1
            "You feel a bit better..."

    hide screen dark_room
    $ read_book = False
    show screen dark_room

    call DRgame_advance_time
    jump DRgame_resume


#Player
label dark_room_player:
    menu:
        "You":
            pass
        "-Hunger-":
            if DRplayer.hunger in [7,8,9,10]:
                "You aren't hungry."
            elif DRplayer.hunger in [6,5,4]:
                "You could do with another meal."
            else:
                "You feel hungry."
        "-Health-":
            if DRplayer.sick == True:
                "You are sick. Eat enough, leave work to others, and make sure that the fire is always warm..."
                "You will die if you don't."
            else:
                if DRplayer.hp in [6,7,8,9,10]:
                    "You feel healthy enough."
                else:
                    "You health is fading. You might become sick."
    jump DRgame_resume

#Stranger
label dark_room_stranger:
    menu:
        "Stranger":
            pass
        "-Hunger-":
            if DRstranger.hunger in [7,8,9,10]:
                "They aren't hungry."
            elif DRstranger.hunger in [6,5,4]:
                "They could do with another meal."
            else:
                "They feel hungry."
        "-Health-":
            if DRstranger.sick == True:
                "They are sick. They will need food and a warm bed..."
                "They will die if they don't get help."
            else:
                if DRstranger.hp in [6,7,8,9,10]:
                    "They are healthy."
                else:
                    "Their health is fading. They might become sick."
        "-Task-":
            menu:
                "Give them a task."
                "-Chopping Wood-":
                    $ DRstranger.task = "chopping_wood"
                "-Hunting-":
                    $ DRstranger.task = "hunting"
                "-Force to do task-" if DRstranger.task in ["chopping_wood","hunting"]:
                    $ DRstranger.force_task = True
                    "The stranger reluctantly agreed do their tasks even in bad weather..."
                    jump DRgame_resume
                "-Get better-" if DRstranger.hp < 6:
                    $ DRstranger.task = ""
                    $ DRstranger.force_task = False
            "You give them their task..."
            "They nod."

    jump DRgame_resume

#Desk
label dark_room_desk:
    menu:
        "Resources"
        "Day [DRgame.day]":
            pass
        "-[DRgame.wood] pieces of firewood-":
            "Gather some more when the weather allows it."
        "-[DRgame.meat] pieces of raw meat-":
            "Cook them or they will spoil."
        "-[DRgame.meals] cooked meals-":
            "Meals don't spoil, but they take time to cook."
        "-[DRgame.leather] pieces of leather-":
            "Leather from hunting deer."
            "Craft a bow and some arrows to hunt them."
        "-[DRgame.fur] pieces of fur-":
            "Leather from hunting small animals like foxes."
            "They can be caught easier with a knife, or by laying out traps."
        "-[DRgame.feathers] feathers-":
            "Feathers are required to craft arrows."
        "-Return to the mirror-":
            jump enter_room_of_req
    jump DRgame_resume


label DRgame_advance_time:
    if DRgame.time == "morning":
        $ DRgame.time = "noon"
    elif DRgame.time == "noon":
        $ DRgame.time = "afternoon"
    elif DRgame.time == "afternoon":
        $ DRgame.time = "night"
    return


init -1 python:

    class DarkRoomGame(object):
        day = 1
        time = ""
        characters = []
        events = []
        fire = 0
        wood = 23
        meat = 5
        meals = 0
        leather = 0
        fur = 0
        feathers = 0
        water = 20
        gold = 0
        game_over = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getChar(self):
            return self.characters

    class DarkRoomCharacter(object):
        name = ""
        hp = 10
        hunger = 5
        sick = False
        random_number = 1
        days_here = 0
        friendship = 0
        task = "" #chopping_wood, hunting, sewing, cooking, woodworking,
        force_task = False #You can tell them to go out in bad weather.
        location = ""
        skills = []
        unskilled = []
        inventory = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
