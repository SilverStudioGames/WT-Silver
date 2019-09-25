label a_christmas_tale:
    show screen blkfade
    with d5
    pause 2

    call room(hide_screens=True)

    centered "{size=+7}{color=#cbcbcb}A Christmas tale{/color}{/size}"

    pause 2

    $ temp_time = daytime #Switch 'daytime' back to this at the end of the store.
    $ daytime = False #Night
    $ interface_color = "gray"
    $ room_deco = "_deco_1" #Xmas deco
    $ gen_chibi_stand = "characters/misc/santa/santa_chibi.png"

    call room("main_room")
    hide screen genie
    show screen chair_left
    show screen desk
    show screen fireplace_fire
    show screen main_room_overlay

    hide screen blkfade
    with d3

    pause 1

    call play_music("anguish")
    show screen bld1
    with d3
    nar "It was the night before Christmas, with excitement at the school."
    nar "But the headmasters room empty, now where is that fool?"
    nar "The stockings were hung by the chimney with care,"
    nar "But no genie to be found. As if he'd never been there."
    hide screen bld1
    with d3
    pause.8

    call play_sound("door")
    call sna_chibi("stand","door","base")
    with d5
    pause.8

    show screen bld1
    with d3
    nar "Severus then entered, all flustered and spent."

    call sna_walk(xpos="mid", ypos="base", speed=2.5)
    pause.2

    call sna_main("Genie? Where are you... I came here, to vent...",face="snape_03",ypos="head")
    nar "He wondered if the genie had found a way home..."
    call sna_main("Seems like a normal Christmas, spent all alone...",face="snape_06")

    nar "But then a crash and a bang from the chimney was heard."
    call play_sound("bump")

    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_main("What the fuck was that, some kind of bird?",face="snape_14")
    nar "With a snap and a crackle, and a strong blinding light."

    call play_sound("bump")
    hide screen fireplace_fire
    call gen_chibi("stand","620","150")
    call teleport("genie")
    pause.8

    nar "A figure appeared, in the most silent of nights."
    pause.2

    call gen_chibi("stand","620","150",flip=True)
    with d3
    pause.2

    show screen bld1
    with d3
    san_[1] "Oh hello there my friend."
    nar "Said the figure at last."
    san_[1] "I thought you might be here, but where's that genie?"
    call sna_main("...",face="snape_25")
    san_[1] "Blast..."

    call sna_main("Genie...",face="snape_24")
    nar "Said the teacher."
    call sna_main("You're not fooling me.",face="snape_24")
    call sna_main("Have you been drinking again?",face="snape_25")
    call sna_main("And I don't mean drinking tea.",face="snape_29")

    san_[1] "I don't know what you mean."
    nar "Said the large bearded man..."
    san_[2] "I'm santa of course."
    san_[2] "I bring presents...."
    san_[2] "That's the plan!"
    pause.8

    nar "After silence and confusion then Severus said..."
    call sna_main("Well, just get it over with so I can go back to bed.",face="snape_09")
    san_[1] "Now boy where's your spirit, it's Christmas is it not?"
    call sna_main("Now genie, look here...",face="snape_24")
    nar "But then he froze on the spot."

    hide screen bld1
    call gen_chibi("hide")
    call teleport("genie")
    with d3
    pause.5

    show screen bld1
    with d3
    nar "The man had then vanished, without even a trace.."
    hide screen bld1
    with d3

    pause.2
    call sna_chibi("stand","mid","base",flip=False)
    with d3
    pause.5
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.8

    call sna_main("I thought he couldn't use magic...",face="snape_05")
    nar "You should've seen the look on Snape's face."
    hide screen bld1
    with d3

    call sna_chibi("hide")
    with d3
    call sna_chibi("stand","570","190",flip=True)
    with d3
    pause.5

    show screen bld1
    with d3
    nar "With only a gift left where he had stood, should he open or should he wait?"
    call sna_main("My first present since childhood...",face="snape_04")
    nar "As he peeled back the wrapping he just stood there in shock."
    call sna_main("Where on earth did he get this?",face="snape_03")
    nar "Then suddenly..."
    call play_sound("knocking")
    nar "A knock."

    "Snape are you in there, I think I lost my keys."
    call sna_main("The door is open, you fool.",face="snape_08",xpos="base",ypos="base")
    nar "His voice... now just a wheeze."

    call play_sound("knocking")
    nar "The genie knocked again. The mutter, he hadn't heard."
    call sna_main("",face="snape_06")
    nar "Now Snape saying nothing, not even a word."
    show screen snape_picture_frame
    with d5
    nar "A picture we then see as it's our time to depart."
    call sna_main("",face="snape_23")
    nar "As sadness turned to joy in the cold teachers heart."
    call ctc

    hide screen snape_picture_frame
    hide screen snape_main
    with d5
    pause.8

    san_[4] "Happy Holidays."

    if not card_exist(unlocked_cards, card_santa):
        if deck_unlocked:
            call give_reward("You have received a special card as a gift!", "images/cardgame/t1/special/santa_v1.png")
        $ unlocked_cards += [card_santa]

    show screen blkfade
    with d9
    pause 2

    call room(hide_screens=True)

    #Reset
    $ daytime = temp_time
    if daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    call update_gen_chibi

    #Unlock Xmas Deco
    $ unlocked_xmas_deco = True

    jump enter_room_of_req