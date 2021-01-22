
label floor_7th:
    if not unlocked_7th:
        m"\"I don't have any reason to go there...\""
        jump desk
    else:
        call blkfade
        call hide_screens
        call update_interface_color("gray")
        call room("floor_seven")

        if first_time_7th:
            $ first_time_7th = False
            call gen_chibi("stand", "right", "base", flip=False)
            call hide_blkfade

            m "So... The diary mentioned he was walking around here."

            call gen_walk("left_mid", speed=1.5)
            call bld

            m "I can definitely sense a strong magical energy in this place..."

            call gen_walk("right", speed=1.5)
            call bld

            m "Maybe if I... or I could..."

            call gen_walk("left", speed=1.5)
            call bld

            g4 "I could be in my office jacking off right now!!"
            hide screen bld1
            show screen floor_7th_door
            with d9
            pause .5
            call gen_chibi(flip=True)
            pause.8
            call bld

            g9 "Well... will you look at that!"

            hide screen bld1
            with d3
            call screen floor_7th_menu
        else:
            call gen_chibi("stand", "left", "base")
            show screen floor_7th_door
            call hide_blkfade
            call screen floor_7th_menu


label map_attic:
    with d5 # Transition from desk

    if tentacle_sample:
        m "(I have no reason to go there anymore.)"

        jump desk
    else:
        $ tentacle_sample = True

        m "(The attic huh...)"
        m "(I guess I could check it out.)"

        call blkfade
        call gen_chibi("stand","desk","base")
        call hide_blkfade

        call gen_walk(action="leave")
        call blkfade

        stop music fadeout 3.0
        stop weather fadeout 3.0

        pause 1.0
        call play_sound("walking")
        play weather "sounds/wind_long_loop.mp3" fadein 2 fadeout 2

        ">You find your way through the winding staircases to the attic door."
        m "Hmm, hopefully this is the right place to use that key..."
        play bg_sounds "sounds/pulse.mp3"
        ">As you approach the door the lock begins to glow..."
        ">Looking down at the key in your hand you notice the same glow around the key..."
        m "Well, this has to be it then..."
        stop bg_sounds fadeout 2.0
        call play_sound("lock")
        pause 2.0
        call play_sound("door")
        ">After unlocking the door you're presented to a dusty room filled with random junk and knick-knacks."
        $ renpy.sound.play("sounds/cough_male.mp3")
        g16 "...*cough* *cough*..."
        g4 "This room is just filled with random junk and knick-knacks!"
        m "(So now what... I'm supposed to take a piece of something and use with this scroll?)"
        m "(I don't even know what the scroll is supposed to do, how am I going to find what it wants me to use!)"
        m "..."
        m "(Screw it... I'm just going to cheat and check the item description in my inventory.)"
        m "(Let's see what it says...)"
        m "(Turns the user into a magical tentacle plant with the usage of living plant material.)"
        m "Well, well... that could be useful..."
        m "So I guess this tentacle plant should be here somewhe--"
        ">As you scan the room you notice a slender piece of vine poking out from behind some crates, as if to avoid the light."
        m "This must be it."
        $ renpy.sound.play("sounds/slash.wav")
        ">You make a clean cut just when..{nw}"
        $ renpy.play("sounds/mondead.wav")
        ">You make a clean cut just when..{fast}"
        g4 "I better get the fuck out of here."
        $ renpy.play("sounds/mon.wav")
        ">As you shut the door you hear the room erupt in a series of loud crashes and growling."

        call play_sound("walking")
        "> You hastily make your way towards your office."

        call gen_walk(action="enter")
        call hide_blkfade

        stop weather
        call music_block

        m "(A tentacle plant and a body-bending magical scroll huh...)"
        g9 "(Maybe I could use it to have some fun with Granger...)"

        menu:
            m "(Question is... Should I use it now or save it for later?)"
            "-Use it now-":
                if game.daytime:
                    if not hermione_busy:
                        g9 "Yes, there's no time like the present..."
                        m "I'll just grab a seat first."

                        call blkfade
                        call gen_chibi("sit_behind_desk")
                        call hide_blkfade

                        jump tentacle_scene_intro
                    else:
                        m "(On second thought... she's probably busy right now.)"
                else:
                    m "(It's a bit late... Miss granger wont be having any classes right now...)"
            "-Save for later-":
                pass

        m "(I'll just store this in my inventory for now...)"

        call blkfade
        call gen_chibi("sit_behind_desk")
        call hide_blkfade

        jump main_room

label map_forest:
    if game.daytime:
        m "I shouldn't be leaving the castle during the day. It's too risky..."
        jump desk

    call outskirts_of_hogwarts

    m "Let's see what I can find out here..."

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the forest and manage to find an odd-looking herb."
                m "This must be wormwood."
                menu:
                    "-Take the wormwood-":
                        ">You gain 1 wormwood."
                        $ potion_inv.add("ing_wormwood")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the forest and manage to find an odd-looking herb."
                m "This must be Knotgrass."
                menu:
                    "-Take the Knotgrass-":
                        ">You gain 1 Knotgrass."
                        $ potion_inv.add("ing_knotgrass")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the forest but find nothing of interest."
                jump return_office


label map_lake:
    if game.daytime:
        m "I shouldn't be leaving the castle during the day. It's too risky..."
        jump desk

    call outskirts_of_hogwarts

    m "Let's see what I can find out here..."

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the lake and manage to find an slender, green vine."
                m "This must be Niffler's fancy."
                menu:
                    "-Take the Niffler's fancy-":
                        ">You gain 1 Niffler's fancy."
                        $ potion_inv.add("ing_niffler_fancy")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the lake and manage to find an exposed root that looks similar to ginger."
                m "This must be Root of Aconite."
                menu:
                    "-Take the Root of Aconite-":
                        ">You gain 1 Root of Aconite."
                        $ potion_inv.add("ing_aconite_root")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the lake but find nothing of interest."
                jump return_office


label gryffindor_dormitories:
    call dormitories

    centered "{size=+7}{color=#cbcbcb}Gryffindor's Dormitory{/color}{/size}"

    menu:
        "-Search the area-":#Cat Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the dorms and manage to find a clump of bright orange fur."
                m "This must belong to some sort of animal."
                menu:
                    "-Take the Fur-":
                        ">You gain 1 Cat Fur."
                        $ potion_inv.add("ing_cat_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office


label ravenclaw_dormitories:
    call dormitories

    centered "{size=+7}{color=#cbcbcb}Ravenclaw's Dormitory{/color}{/size}"

    menu:
        "-Search the area-":#Luna's Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the dorms and manage to find an comb with some hair in it."
                m "This must be someone's hair."
                menu:
                    "-Take the hair-":
                        ">You gain 1 Luna's Hair."
                        $ potion_inv.add("ing_luna_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office

label map_pitch:
    if pitch_open:
        hoo "Hello Professor Dumbledore, nice to see you out of your office today."
        hoo "What brings you down to the Quidditch pitch today?"
        m "Quidditch, what sort of name is that?" #put in low talking tone
        hoo "What was that?"
        m "Nothing, just commenting about the weather." #Maybe change this
        hoo "Well I'm glad that you're here. I wanted to have words with you about a problem that I'm having at the moment."
        m "What's wrong?"
        hoo "Attendance at quidditch matches has slowly been declining over the last couple of months."
        hoo "Students just don't seem to want to turn up to watch their teams play. It's affecting team morale."
        m "And how would you like to fix this?"
        hoo "Perhaps we could make attendance to the match mandatory."
        m "I don't think that that would work. If I did that you would just end up with a lot of disgruntled students booing your own team."
        m "If poor attendance is affecting morale I would hate to think what that would do to the players."
        hoo "Well then what do you suggest?"
        m "You need a way to attract and excite the crowd. To get the students here and to get them cheering."
        m "What you need is a cheerleading team."
        hoo "A what?"
        m "A team of girls to dance and cheer for their team. To get their fellow students brimming with enthusiasm."
        hoo "I'm not sure Sir, Hogwarts has always been a traditional school."
        hoo "Something like this goes in the face of that legacy."
        m "Well if you feel that way then I think you might just have to accept the declining number of students watching the game."
        hoo "Fine, but I'm not comfortable with a team of these \"\Cheerleaders\"\. At most I'd be comfortable with one girl dancing." #Maybe adjust this so that there is a team
        m "Well I think I have the perfect candidate. I'll send her over next practice session to try out."
        hoo "Okay, just make sure she's wearing something appropriate."
        $ pitch_first = False
        jump return_office
    else:
        ">You look around the open field but can't see any students or teachers"
        m "Mustn't be a practice day."
        jump return_office

label outskirts_of_hogwarts:
    call blkfade
    call gen_chibi("stand","desk","base")
    call hide_blkfade

    call gen_walk(action="leave")
    call blkfade

    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of Hogwarts{/color}{/size}"

    call hide_screens

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")
    pause.3
    call hide_blkfade
    pause.8
    call play_sound("walking_on_grass")
    $ ccg(layer2="172")

    return

label dormitories:
    call blkfade
    call gen_chibi("stand","desk","base")
    call hide_blkfade

    call gen_walk(action="leave")
    call blkfade

    stop music fadeout 1.0
    return


label return_office:
    call hide_characters
    show screen blkfade
    with d3

    call update_interface_color
    pause.8

    jump main_room
