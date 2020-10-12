label eating_for_pleasure:
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Eating for Pleasure{/color}{/size}"

    pause 2

    narrator "This story is best played when drunk...{w=0.4} or not at all...{w=0.4} it's the worst...{w=0.4} enjoy!"

    # Setup
    $ temp_time = daytime
    $ daytime = False
    $ her_outfit_last.save()
    call update_interface_color
    call music_block
    call room("main_room")
    with d5

    $ renpy.music.play("music/fluffing-a-duck-by-kevin-macleod.mp3")
    m "Gah... this place is so dull..."
    m "Not a single gambling den or a whore house..."
    m "And even if I don't need to eat I'd do anything for a pizza right about now..."
    hat "Just call a pizza place then..."
    if not hat_known:
        $ renpy.play("sounds/MaleGasp.mp3")
        g4 "Did that hat just speak?!" with vpunch
        hat "Of course I speak!"
        hat "Not only that... I know who you are..."
        g5 "You do?"
        g4 "Then why haven't you said anything until now!"
        g4 "I've been sitting here alone for months!"
        hat "A wise man told me not to speak unless you have something to say."
        m "Wait..."
        g9 "The real Dumbledore told you to shut the fuck up?"
        hat "..."
        m "Anyway, what did you mean by \"call\"?"
    else:
        m "What do you mean, call?"
    m "I haven't seen a single phone in this place!"
    hat "Just use the floo-network."
    m "The floo... is that like a sewer network or something?"
    m "You guys got magic turtle pizza deliverers?"
    hat "No, I'm talking about the fireplace."
    hat "Wizards use it as a form of communication and travel."
    m "Wait, so like a portal?"
    g4 "I've been able to just travel to any ole fireplace this whole time?!"
    hat "Hogwarts fireplaces are limited to voice communication or we'd have all sorts of dark wizards roaming this place..."
    m "(Sounds like discrimination to me...)"
    m "How does it work then?"
    hat "There should be some powder in one of the drawers, take it and throw some in the fire and say out loud who you want to call."
    m "Gimme a sec."
    pause 0.5
    call gen_chibi("jerk_off_behind_desk")
    with d5
    $ renpy.sound.play("sounds/drawer_open.mp3")
    pause 0.75
    call gen_chibi("sit_behind_desk")
    with d5
    m "Oh, that powder!"
    m "I was wondering what it was for..."
    m "Okay, let's do this!"
    show screen blkfade
    with d5
    $ renpy.play('sounds/08_hop_on_desk.mp3')
    show screen desk
    show screen chair_left
    pause 1.4
    call gen_chibi("stand", "desk", "base", flip=True)
    hide screen blkfade
    with d5
    pause 0.3
    call gen_walk(560, "base")
    pause 2.0
    m "..."
    call gen_chibi("stand", flip=False)
    with d3
    m "So I just throw it in and say who I'm calling?"
    hat "Yes... make sure you get right up next to it..."
    m "Okay then..."
    call gen_chibi("stand_alt", flip=True)
    with d3
    pause 1.0
    call gen_chibi("grab_low")
    pause 0.5
    $ renpy.sound.play("sounds/fire_woosh.mp3")
    $ fire_in_fireplace = True
    show screen gfx_effect(780, 280, img="smoke", zoom=0.5)
    pause 0.1
    show screen fireplace_greenfire
    with d5
    pause 1.0
    $ renpy.sound.play("sounds/cough_male.mp3")
    m "*Cough* *Cough*"
    hat "Say the name!"
    $ renpy.play('sounds/sniff.mp3')
    m "*ah* Piz-- *ah-a*"
    $ renpy.play('sounds/sniff.mp3')
    pause 0.5
    $ renpy.play('sounds/sniff.mp3')
    pause 0.5
    call gen_chibi("sneeze")
    with d2
    $ renpy.play('sounds/glass_break.mp3')
    pause 0.4
    call gen_chibi("stand_alt")
    with d2
    "Pizza Hu--*shoo*lut!!!{fast}" with hpunch
    pause 1.0
    hat "Did you say Pizza--?"
    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    "*static*... Welcome to Pizza slut, may I take your order?"
    hat "Well I'll be damned..."
    m "{size=+8}Yes! Hello, is this thing on?{/size}"
    "Sir, I can hear you... No need to shout."
    $ flag = None
    menu:
        "What will be your order, sir?"

        "-Meat Eater-":
            $ flag = 0
            g16 "{size=+16}I'll have the pepperoni!{/size}" with vpunch
            "*Sigh* One pepperoni... anything else?"
            $ her_outfit_pizza.group[2].set_color([[180, 50, 10, 255]])
            $ her_outfit_pizza.group[3].set_color([[180, 50, 10, 255]])
        "-Vegan Delight-":
            $ flag = 1
            g16 "{size=+16}I'll have the vegetariana!{/size}" with vpunch
            "*Sigh* One vegetariana... anything else?"
            $ her_outfit_pizza.group[2].set_color([[73, 226, 53, 255]])
            $ her_outfit_pizza.group[3].set_color([[73, 226, 53, 255]])
    $ hermione.equip(her_outfit_pizza)
    m "{size=+8}Hold on...{/size}"
    call gen_chibi("stand", flip=False)
    with d3
    m "Did you want anything?"
    hat "...{w=0.4}I'm a hat."
    m "Oh... right."
    call gen_chibi("stand_alt", flip=True)
    with d3
    g16 "{size=+16}That's all, thanks!{/size}" with hpunch
    "And your address?"
    m "{size=+8}Headmaster's office, Hogwash!{/size}"
    "Hogwarts sir?"
    if flag == 0:
        g16 "{size=+8}No, just pepperoni thanks!{/size}" with vpunch
    else:
        g16 "{size=+8}No meat please, just olives!{/size}" with vpunch
    "..."
    "Okay then..."
    m "{size=+8}Ten minutes or pizza's free?{/size}"
    "Of course, sir... we've never been late using the floo..."
    "hold on a second..."
    "It seems like your floo-network fireplace has blocked incoming travel."
    g9 "{size=+8}What a shame... I guess you'll have to make your way here the old fashioned way.{/size}"
    g9 "{size=+8}Headmaster's office is on the seventh floor, enjoy the moving staircases!{/size}"
    "But sir..."
    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    g16 "{size=+16}Clock's ticking...{/size}" with hpunch
    "Okay then, your delivery will be as soon as... humanly possible..."
    pause 1.0
    call gen_chibi("stand", flip=False)
    with d3
    pause 0.5
    m "Hat, how do I hang up?"
    hat "Just extinguish the fire."
    call gen_chibi("stand", flip=True)
    with d3
    m "(A phone would have been so much easier...)"
    $ renpy.sound.play("sounds/spit.mp3")
    m "..."
    hat "No just use the..."
    m "Don't worry, I got this..."

    call gen_chibi("stand_alt")
    with d3
    pause 0.3
    show screen blkfade
    with d5
    m "..."
    $ renpy.sound.play("sounds/zipper.mp3")
    hat "Wait... what are you..."
    $ renpy.sound.play("sounds/fuse.mp3")
    g9 "Ah...{w=0.4} Must've been at least a hundred years..."
    pause 1.0
    hide screen blkfade
    pause 1.0
    $ renpy.sound.play("sounds/fire_woosh.mp3")
    hide screen fireplace_greenfire
    with d5
    $ fire_in_fireplace = False
    pause 1.0

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    call gen_chibi("sit_behind_desk")
    hide screen desk
    hide screen chair_left

    hide screen blkfade
    with d5

    g4 "They sure are taking their goddamn time!"
    m "..."
    m "Maybe I could jerk off a little..."
    call gen_chibi("jerk_off_behind_desk")
    with d5
    pause 1.2
    hat "Eww!"
    call gen_chibi("sit_behind_desk")
    with d5
    $ renpy.play('sounds/MaleGasp.mp3')
    g4 "Ah fuck!"
    m "You're still here..."
    g4 "How am I supposed to jerk off in peace... It will never be the same with a pervert hat ogling me!"
    hat "{size=-4}..... It never seemed to bother you before......{/size}"
    if not hat_known:
        g4 "Because I wasn't aware of your existence!"
    pause 1.0

    call play_sound("knocking")
    "*knock-knock*"
    pause 1.0
    g16 "{size=+4}Who's there?{/size}"
    "{size=+5}Pizza!{/size}"
    m "{size=+4}Pizza who?{/size}"
    "{cps=8}..........{/cps}"
    "{size=+5}Pizza slut,{w=0.5} sir........{/size}"
    g9 "*he-he-heh*"
    m "Finally..."
    g16 "{size=+4}Come in!{/size}"
    pause 0.5
    call her_walk(action="enter", xpos="desk", ypos="base")
    call her_main("Your order, sir!", "smile", "happyCl", "base", "mid", trans=d3)
    g5 "What...{w=0.3} the hell...{w=0.3} is this!"
    call her_main("What do you mean... Did we get the wrong toppings?", "annoyed", "base", "worried", "mid")
    g4 "Toppings?!"
    g4 "There's only two slices! And they're on your body!"
    call her_main("A-Actually,{w=0.5} sir,{w=0.5} there are three slices...", "open", "base", "base", "R", cheeks="blush")
    g4 "Don't lie to me, I can clearly see just tw--"
    pause 0.5
    $ hermione.strip("bottom")
    call her_main("", "grin", "base", "base", "mid", cheeks="blush")
    pause 1.0
    g5 "{cps=3}..............{/cps}"
    g4 "You expect me to eat this?"
    call her_main("Sir, you ordered from pizza slut. A slut and a pizza!", "annoyed", "base", "worried", "mid")
    call her_main("Our slogan is \"Enjoy a nice pizza ass with every slice!\"", "open", "closed", "base", "mid")
    call her_main("", "base", "wink", "base", "mid")
    m "..."
    m "But there's only three..."
    m ".........."
    m "Give me the pizza..."
    her "Of course!"
    $ hermione.strip("all")
    pause 1.0
    call her_main("Now, what else would you like to--", "smile", "wink", "base", "mid")
    m "Get out..."
    call her_main("Sir, the payme--", "open", "base", "worried", "mid")
    g4 "I said, get out!"
    call her_main("Okay...", "disgust", "base", "worried", "down")
    call her_walk(action="leave")
    m "..."
    m "These wizard customs... ruining something as holy as pizza..."
    g9 "Mmm... Come to genie you beautiful temptress..."

    show screen blkfade
    with d5

    "{cps=5}.........{/cps}{nw}"
    pause 1.0
    $ renpy.play('sounds/gltch.mp3')
    "Genie" "Yes.... *Mhmmmmmmm*... Just like that."
    hat "By Merlins beard, that's disgusting!"
    "Genie" "Shut up hat! Don't judge me!"

    call unlock_clothing(text=">New clothing items for Hermione have been unlocked!", item=her_outfit_pizza)

    centered "{size=+7}{color=#cbcbcb}{cps=1}...{/cps}End?{/color}{/size}"

    #Reset
    $ daytime = temp_time
    $ hermione.equip(her_outfit_last)
    call hide_screens
    call update_interface_color
    jump enter_room_of_req

screen fireplace_greenfire():
    tag fireplace_fire
    zorder 2
    add "fireplace_greenfire" xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos+25 xanchor 0.5 yanchor 0.5

### Fireplace ###
image fireplace_greenfire: #Fireplace fire.
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_01.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_02.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_03.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_04.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_05.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_06.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_07.webp", im.matrix.hue(100))
    pause.1
    im.MatrixColor("images/rooms/_objects_/fireplace/fireplace_fire_08.webp", im.matrix.hue(100))
    pause.1
    repeat
