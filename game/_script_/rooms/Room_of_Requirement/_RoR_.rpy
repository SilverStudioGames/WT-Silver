define mirror_bg = [None, "images/rooms/room_of_requirement/agrabah.webp"]
default mirror_image = 0

transform mirrage:
    on show, appear, start:
        alpha 0.0
        linear 0.5 alpha 1.0

screen room_of_requirement():
    zorder 0
    add Transform("images/rooms/room_of_requirement/corridor.webp", xzoom=-1.0)
    if mirror_image != 0:
        add Transform(mirror_bg[mirror_image], xzoom=-1.0) xpos -540 at mirrage

    # Show a copy of chibi screen in the mirror
    $ mirror_chibi = renpy.get_screen("genie_chibi")
    if mirror_chibi:
        add mirror_chibi.copy() xzoom -1 xoffset 450-config.screen_width

    add "images/rooms/room_of_requirement/empty_room.webp"
    add "images/rooms/objects/doors/door_idle_night.webp" xpos 898 ypos 315 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "images/rooms/room_of_requirement/mirror.webp" xpos 100 ypos 180

    add "images/rooms/objects/candles/candleM.webp" xpos 700  ypos 200  xanchor 0.5 yanchor 0.5 zoom 0.5

    use ui_top_bar

screen room_of_requirement_overlay():
    tag foreground
    zorder 5

    add "images/rooms/room_of_requirement/foreground.webp"
    add "candle_fire_01" xpos 592 ypos 85
    add "candle_fire_02" xpos 248 ypos 50

screen room_of_requirement_menu():
    tag room_screen
    zorder 1

    imagebutton: # Mirror
        xpos 100
        ypos 180
        idle "images/rooms/room_of_requirement/mirror.webp"
        hover "images/rooms/room_of_requirement/mirror_hover.webp"
        tooltip "Look into the mirror"

        action [Hide("room_of_requirement_menu"), Jump("mirror_menu")]

    imagebutton: # DOOR
        xpos 758+140
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle door_night_OBJ.get_room_image()
        hover door_night_OBJ.get_hover_image()
        tooltip "Return to office"

        action Jump("return_office")

label hide_room_req:
    hide screen room_of_requirement_menu
    hide screen room_of_requirement
    hide screen room_of_requirement_overlay
    with None
    return

label mirror_menu:
    show screen list_menu("mirror_menu", "Mirror Stories\n{size=9}Short stories written by the Witch Trainer community.{/size}", (), [mr_evs_list])
    with d3

    label .interact:
    $ _choice = ui.interact()

    if isinstance(_choice, MirrorStory):
        hide screen list_menu
        $ renpy.jump(_choice.start_label)

    elif _choice == "Close":
        hide screen list_menu
        call screen room_of_requirement_menu

    jump .interact

screen floor_7th_door():
    add "images/rooms/objects/doors/front_door.webp" xpos 420 ypos 105
    zorder -1

screen floor_7th_screen():
    add "images/rooms/room_of_requirement/corridor_edit.webp"
    add "images/rooms/objects/candles/candle.webp" xpos 0 ypos 95 zoom 0.5
    add "candle_fire_02" xpos 0 ypos 95
    add "images/rooms/objects/candles/candleM.webp" xpos 900 ypos 95 zoom 0.5
    add "candle_fire_01" xpos 900 ypos 95
    add "images/rooms/objects/deco/hogwarts_banner.webp" xpos 800 ypos 105
    add "fireplace_fire" xpos 575 ypos 60
    add "images/rooms/objects/deco/owlbasin.webp" xpos 660 ypos 255 zoom 0.3
    add "fireplace_fire" xpos 265 ypos 60
    add "images/rooms/objects/deco/owlbasin.webp" xpos 350 ypos 255 zoom 0.3
    add "images/rooms/objects/deco/hogwarts_banner.webp" xpos 200 ypos 105
    zorder -1

    use ui_top_bar

#animation of flower for painting maybe?
image flower_animation:
    "images/animation/Bouquet4.webp"
    pause 30
    "images/animation/BouquetPaf.webp"
    pause .2
    "images/animation/Flower1.webp"
    pause .2
    "images/animation/Flower2.webp"
    pause .2
    "images/animation/Flower3.webp"
    pause .2
    "images/animation/Flower4.webp"
    pause 30
    "images/animation/FlowerPaf.webp"
    pause .2
    "images/animation/Bouquet1.webp"
    pause .2
    "images/animation/Bouquet1.webp"
    pause .2
    "images/animation/Bouquet2.webp"
    pause .2
    "images/animation/Bouquet3.webp"
    pause .2
    "images/animation/Bouquet4.webp"
    repeat

screen floor_7th_menu():
    imagebutton:
        xpos 420
        ypos 105
        idle "images/rooms/objects/doors/front_door.webp"
        hover "images/rooms/objects/doors/front_door_hover.webp"
        tooltip "Enter"

        action Jump("enter_room_of_req")
    zorder -1

label enter_room_of_req:
    show screen blkfade
    with d3

    call music_block

    call room("room_of_requirement")
    show screen room_of_requirement_overlay

    python:
        for i in mr_evs_list:
            i.check_lock()

    if not mirror_intro_done:
        $ mirror_intro_done = True
        $ achievement.unlock("mirror")
        call gen_chibi("stand","door","base",flip=False)
        call hide_blkfade

        stop music fadeout 1.0
        $ renpy.music.stop("weather")
        $ renpy.sound.play( "sounds/door.mp3")
        m "..."
        $ renpy.music.play("music/RoomOfReqIntro.mp3")
        call gen_chibi("stand","door","base")
        g4 "It's just a room filled with a bunch of crap..."
        call gen_chibi("stand","door","base",flip=False)
        m "And a mirror?"

        call gen_walk("left", "base")

        call bld
        m "..."
        m "Odd, it appears the source of the magic is emanating from this mirror..."

        # Single line, doesn't deserve a defined character speaker.
        "Male Voice" "So you've found the mirror of Erised..."

        $ renpy.sound.play( "sounds/MaleGasp.mp3")
        stop music fadeout 1.0
        g4 "Dumbledore!"
        $ renpy.sound.play( "sounds/soft_wind.mp3")
        call sna_chibi("stand","door","base")
        call gen_chibi("stand", flip=True)
        g9 "*Cough* I mean... Yes Severus, it is I...{w} \"Dumbledore\"."
        m "I'm so glad to be back..."
        call sna_main(".....","snape_05")
        m "Worth a shot..."
        play music "music/song18.mp3" fadein 4 fadeout 1
        call sna_main("I'm quite certain I told you to stay in your office... For how long have you been roaming the school grounds?","snape_06")
        m "This is the first time... hence why I was so lost."
        call sna_main(".....","snape_05")
        m "Only for the past week or so..."
        call sna_main(".....","snape_07")
        m "Yeah pretty much since the moment I got here."
        call sna_main("*Sigh* Well, at least it doesn't appear you've been caught...{w} yet.","snape_06")
        call sna_main("So I wont stop you as long as you refrain from any of your...{w=0.6} weird requests or comments to other staff members.","snape_05")
        m "...."
        if clothing_store_intro_done:
            call sna_main(".....","snape_03")
            m "I might have ordered a few oddities from Madam Mafkin..."
            call sna_main("Hahahah... That old hag?","snape_28")
            call sna_main("She's nuts, she can sew that's for damn sure but she'd never know nor care... do whatever you want with her. ", "snape_01")
            m "(I'd rather not...)"
            call sna_main("Continuing where I left off.", "snape_09")
        call sna_main("Now, this mirror that you've found...", "snape_01")
        call sna_main("I thought Albus would've moved it out of the school after the last incident...", "snape_22")
        call gen_chibi("stand", flip=False)
        with d3
        show screen bld1
        m "What kind of incident? It's just some dusty old mirror... why would Dumbledore care about it? And what's going on with this room?"
        call sna_main("I don't know about the room, I'm more concerned by this mirror. Why don't you have a look in it and tell me what you see?", "snape_01")
        m "*Squints* Just seems like an old mirror to me, a bit dusty and cloudy thou... hold on a minute."
        $ mirror_image = 1
        call sna_main(".....", "snape_23")
        g4 "... I see myself... I've won the house cup!"
        call sna_main("Really?", "snape_05")
        m "No, I can see myself in Agrabah. I'm surrounded by a harem of women all dedicated to pleasing me."
        call sna_main("You really are nothing more than a sexual deviant are you?", "snape_02")
        m "Pretty much."
        call sna_main("The mirror is known as the mirror of Erised, or Desire backwards...", "snape_09")
        g9 "Very clever..."
        call sna_main("Quite... in short, it's designed to show you your deepest desire... but by your comment I'm sure you already got that.", "snape_05")
        m "Your magic might be foreign to me but this seems like nothing more than a party trick, I already know what I desire. "
        call sna_main("Well, it would be quite dull... if you didn't include the changes I made that had it locked up in the first place.", "snape_20")
        m "I could probably make a good guess already but please, do tell..."
        call sna_main("The intended purpose was far too boring, so I modified the enchantment. This would be incredibly difficult for a lesser wizard, but genius like I am...", "snape_23")
        m "Booooring."
        call sna_main("It's a porn creator...", "snape_03")
        $ mirror_image = 0
        call gen_chibi("stand", flip=True)
        g5 "A what?!"
        call sna_main("A porn creator. Well, technically it's used to let you live out your fantasies, be they impure or not. So not necessarily porn.", "snape_01")
        g5 "And you didn't tell me a thing like this existed?"
        call sna_main("Well, it didn't exist until I made it... and I thought it was moved or destroyed.", "snape_26")
        g4 "Get out."
        call sna_main("What?", "snape_05")
        g9 "I said get out, I found it so I get to keep it."
        call sna_main("But, I thought maybe I could move...", "snape_06")
        g4 "It's staying right where it is, I've been getting incredibly bored lately and might consider roaming the school a bit more... actually, I feel the urge to take a trip to the girls dormitory right now."
        call sna_main("Fine, it stays. Please don't... just remember that it will take time for it to reshape and create imagery so check back every now and then.", "snape_06")
        m "Noted... Out. Now."

        hide screen snape_main
        hide screen bld1
        call give_reward("You've unlocked the room of requirement","images/rooms/room_of_requirement/mirror_hover.webp")
        call sna_chibi("hide")
        call gen_chibi("hide")
    else:
        $ mirror_image = 0
        play music "music/song18.mp3" fadein 4 fadeout 1
        call gen_chibi("stand", "door", "base", flip=False)
        call hide_blkfade

        call gen_walk(200, "base")
        #TODO Dont have Genie walk to the mirror when returning from a mirror story

    $ mirror_image = 1
    call gen_chibi("stand", "left", "base", flip=False)
    call hide_blkfade
    call screen room_of_requirement_menu
