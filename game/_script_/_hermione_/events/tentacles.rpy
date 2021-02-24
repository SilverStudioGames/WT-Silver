#Public tentacle scene
label tentacle_scene_intro:
    with d3
    show screen bld1

    if not tentacle_scroll_examined:
        $ tentacle_scroll_examined = True
        m "(*Hmm*... let's see if we can get this writing to show...)"
        m "(It should be something simple like a command word...)"

        $ d_flag_01 = False
        $ d_flag_02 = False
        $ d_flag_03 = False
        label .spell:
        if d_flag_01 and d_flag_02 and d_flag_03:
          jump .after_spell
        menu:
          "\"Open Sesame!\"" if not d_flag_01:
            $ d_flag_01 = True
            m "...{w=0.8} Guess not..."
            jump .spell
          "\"Hocus Pocus!\"" if not d_flag_02:
            $ d_flag_02 = True
            m "...{w=0.8} Damn..."
            jump .spell
          "\"Abracadabra!\"" if not d_flag_03:
            $ d_flag_03 = True
            m "...{w=0.8} ..."
            jump .spell

        label .after_spell:
        m "Work you stupid scroll or I'll throw you in the fire!"
        $ renpy.play('sounds/scribble.mp3')
        m "That's what I thought..."

        m "Now then... Let's find out what this scroll says..."
        m "At the highest point is where I'm hidden..."
        g4 "(fuck, it's a riddle...{w=0.4} Guess I deserved that...)"

        m "At the highest point is where I'm hidden--"
        m "A place where you will need this key--"
        m "To use this scroll that is forbidden--"
        m "You'll need to take a piece of me..."

        m "Key... what k--"
        $ renpy.play('sounds/magic1.ogg')
        show screen white
        with d9
        pause 0.9
        hide screen white
        with d5
        g4 "ARGH!"
        g4 "(Bloody magic...)"
        m "(Oh look, a rusty key just popped out from that scroll...)"
        m "(Convenient...)"
        m "(Now I'll just have to find where it fits...)"
        jump main_room_menu

    m "(Okay... so...{w=0.3} What was this scroll supposed to do again?)"
    m "(Let's see...)"
    if not tentacle_sample:
        m "Right, the riddle..."

        label .riddle:
        m "\"At the highest point is where I'm hidden-\""
        m "\"A place where you will need this key-\""
        m "\"To use this scroll that is forbidden-\""
        m "\"You'll need to take a piece of me...\""

        menu:
            m "..."
            "-Continue-":
                pass
            "-Repeat the riddle-":
                jump tentacle_scene_intro.riddle

        m "(Well... I have the key, now to figure out the rest...)"
        m "(The highest point... *Hmm* I wonder where that could be.)"
        jump main_room_menu
    else:
        m "(Ah, that's it... it's supposed to turn me into some sort of magical tentacle plant...)"
        m "(I have everything I need to perform the ritual and have some fun with Hermione.)"

        if not game.daytime:
            m "(*hmm* But it's too late for me to use it now. I should do it at dawn, before class has started.)"
            jump main_room_menu
        elif hermione_busy:
            m "(*Hmm* But Hermione is busy at the moment, I should postpone my plans until tomorrow.)"
            jump main_room_menu

    m "(I better write her a note first so she can carry me with her to class...)"
    call gen_chibi("paperwork")
    with d3
    pause 1.0

    # Setup
    $ hermione_busy = True
    $ d_flag_01 = []
    $ d_flag_02 = False

    menu:
        m "(*Hmm*... how should I start?)"
        "\"Dear Hermione, ...\"":
            $ d_flag_01.append("Dear Hermione,\n\n")
        "\"Dear [hermione_name], ...\"":
            $ d_flag_01.append("Dear [hermione_name],\n\n")
        "\"You, the bimbo, ...\"":
            $ d_flag_01.append("You, the bimbo,\n\n")

    "*Scribble* *Scribble*"

    menu:
        m "....*Mhmm*...."
        "\"... I had very important business matter to attend to...\"":
            $ d_flag_01.append("I had very important business matter to attend to,")
        "\"... I went out to visit a brothel...\"":
            $ d_flag_01.append("I went out to visit a brothel,")
        "\"... I have turned myself into a plant...\"":
            $ d_flag_01.append("I have turned myself into a plant,")
            $ d_flag_02 = True

    "*Scribble* *Scribble*"

    menu:
        m "..."
        "\"... I ask you kindly...\"":
            $ d_flag_01.append("I ask you kindly,")
        "\"... Just listen for once...\"":
            $ d_flag_01.append("just listen for once and")

    "*Scribble* *Scribble*"

    menu:
        m "... and now..."
        "\"... take this plant with you to your class...\"" if not d_flag_02:
            $ d_flag_01.append("take this plant with you to your class.\n\n")
        "\"... take this plant then shove it up your ass...\"" if not d_flag_02:
            $ d_flag_01.append("take this plant then {b}{s}shove it up yo{/s}{/b} bring it to class.\n\n")
            g9 "Shove it up yo--..."
            call gen_chibi("sit_behind_desk")
            with d3
            g4 "I can't write that!"
            m "What if she does it and I get shat on... No, no, no, let me change that."
            call gen_chibi("paperwork")
            with d3
        "\"... take me to class...\"" if d_flag_02:
            $ d_flag_01.append("take me to class.\n\n")

        "\"... shove me up your ass...\"" if d_flag_02:
            $ d_flag_01.append("{b}{s}shove me up yo{/s}{/b} take me to class.\n\n")
            g9 "Shove me up yo--..."
            call gen_chibi("sit_behind_desk")
            with d3
            g4 "I can't write that!"
            m "What if she does it and I get shat on... No, no, no, let me change that."
            call gen_chibi("paperwork")
            with d3

    "*Scribble* *Scribble*"

    menu:
        m "..."
        "\"... Sincerely, Dombledure.\"":
            $ d_flag_01.append("Sincerely,\nDombledure.")
        "\"... Yours truly, [genie_name].\"":
            $ d_flag_01.append("Yours truly,\n[genie_name].")

    $ d_flag_01 = " ".join(d_flag_01)

    call gen_chibi("sit_behind_desk")
    with d3
    pause 1.0
    m "Yes...{w=0.5} that should do it... now to call her up here and use that scroll..."
    stop music fadeout 3.0
    show screen blkfade
    with d5
    centered "{size=+7}{color=#cbcbcb}A few moments later...{/color}{/size}"
    call gen_chibi("hide")
    $ desk_OBJ.foreground = "letter_and_plant_on_desk"
    hide screen blkfade
    with d5

    pause 3.0
    call her_walk(action="enter")
    with d3
    pause 1
    call her_main("[genie_name], my class is about to--", "open", "base", "worried", "L", trans=d3)
    call her_main("[genie_name]?", "open", "squint", "base", "L")
    call her_walk(xpos="mid", ypos="base")
    pause 1.0
    call chibi_emote("thought","hermione")
    pause 2.0
    call chibi_emote("hide", "hermione")
    call her_main("Are we playing hide and seek??", "annoyed", "base", "angry", "R", trans=d3)
    call her_main("[genie_name], I really don't have the time--", "annoyed", "narrow", "angry", "stare")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause 1.0
    call chibi_emote("exclaim","hermione")
    pause 1.0
    call chibi_emote("hide", "hermione")
    her "..."
    call her_walk(xpos="desk", ypos="base")
    m "(Yes... she's seen me...)"
    m "(Take the note!)"
    call her_main("What's with this ugly plant?", "disgust", "narrow", "angry", "stare", trans=d3)
    with vpunch
    g4 "(I'm not ugly!)"
    m "(... Just haven't blossomed yet...)"
    pause 1.0
    call her_chibi("stand", flip=True)
    with d3
    call her_main("Professo--...?", "open", "base", "worried", "L", flip=True, trans=d3)
    call her_main("I thought I heard him for a second...", "annoyed", "narrow", "worried", "R")
    m "(Read the note already, would you..)"
    pause 1.0
    call her_chibi("stand", flip=False)
    with d3
    call her_main("Oh, there's also a note, I better read it...", "open", "base", "base", "down", flip=False, trans=d3)

    m "(Can't help herself but snoop in other peoples business can she...)"
    $ desk_OBJ.foreground = "plant_on_desk"
    with d3
    $ renpy.play("sounds/pageflip.mp3")
    call her_main("Oh... It's actually addressed to me...", "soft", "base", "base", "stare")

    # Read letter from Genie
    $ letter = Letter(text=d_flag_01)

    $ menu_x = 0.5
    $ menu_y = 0.9

    show screen letter
    hide screen hermione_main
    with d5

    menu:
        "-Done reading-":
            pass

    call reset_menu_position

    hide screen letter
    call her_main("....................................", "disgust", "narrow", "angry", "mid", trans=d3)
    call her_main("So I'm a delivery girl as well now?", "annoyed", "narrow", "angry", "stare")
    call her_main("Well... I suppose I'm already headed there anyway...", "annoyed", "closed", "angry", "stare")
    call her_main("Guess he must've checked my schedule for once...", "annoyed", "narrow", "worried", "R")
    g9 "(Herbology class, here I come!)"

    hide screen hermione_main
    hide screen plant_on_desk
    call her_chibi("hide")
    show screen blkfade
    with d9

    pause 1.5
    call play_sound("door")
    pause 1
    centered "{size=+7}{color=#cbcbcb}Herbology{/color}{/size}"
    pause 1

    call play_music("agenda")
    play bg_sounds "sounds/murmur.mp3" fadein 2 fadeout 2

    spo "In today's class, we will be learning about a plant called Devil's Snare."
    spo "Hermione Granger was kind enough to bring us a pot with an underdeveloped Devil's Snare."
    spo "It's kind of wilted and looks weak but..."
    g4 "(Oh fuck you, bitch!)"
    her "Actually, professor that wa--"
    spo "Miss Granger, please don't interrupt me."
    her "Sorry..."
    spo "Now then..."
    spo "This is an incredibly dangerous plant, known to constrict and kill its prey with its fast and powerful tendrils."
    spo "They are found naturally in caves and swamps as they like dark and damp places and hate sunlight."
    her "Isn't Devil's Snare extremely dangerous?"
    spo "Yes, Miss Granger. At least you're paying attention to what I was saying. Now please sit down."
    $ renpy.sound.play("sounds/giggle2_loud.mp3")
    pause 1.5
    $ renpy.sound.play("sounds/shush.mp3")
    her "..........."
    spo "These aren't even a week old, so they would barely be able to stroke you with their tendrils, let alone constrict you."
    spo "Now everyone, pass the samples around so that you all can get a good look."
    her "Professor Sprout, are they supposed to have mouths?"
    spo "Yes Miss Granger, it's how they consume their prey once they have asphyxiated them."
    her "Okay, well what are the eyes for? I thought they sensed their prey by touch?"
    spo "What are you on about Miss Granger? Devil's Snare don't have eyes."
    her "This one d--"
    $ renpy.sound.play("sounds/crowd_gasp.mp3")
    $ renpy.sound.play("sounds/plant_burst.mp3")
    stop bg_sounds
    with vpunch
    pause 2.0
    ">All of a sudden, you explode outwards in a flash of thick green tentacles."
    her "What's happening?!?"
    $ renpy.sound.play("sounds/plant_grab.mp3")
    ">You quickly bind her wrists and waist..."
    $ renpy.sound.play("sounds/gasp.mp3")
    her "I can't move!"
    $ renpy.sound.play("sounds/creaking.mp3")
    ">then lift her into the air with your powerful appendages..."
    spo "Stay calm Miss Granger, Devil's Snare will let you go if you don't move!"
    ">Slinking your slimy tentacles under her top and skirt."
    if not hermione.is_worn("panties"):
        mal "Hey, look, look! She doesn't have panties on!"
        fem "Oh my gosh, so the rumours about her were true?!"
        mal2 "And she brought her own plant sample, I bet she planned this out, what a total slut!"
    her "Oh no..."
    $ renpy.sound.play("sounds/cloth_rip.mp3")
    ">You rip her top off in a flurry of buttons and cotton..."
    her "*Ahhhh*!"
    $ renpy.sound.play("sounds/plant_slithering.mp3")
    ">Sliding your tentacles up her legs and slowly pulling them apart."
    ">Hermione struggles against you but her effort is in vain."
    her "Please no... Not here."
    if hermione.is_worn("panties"):
        ">The tentacles slowly remove her panties, revealing her pussy to the entire class."
    mal "Wow..."
    fem "This is horrible, someone should do something!"
    mal2 "Professor Sprout says as long as she doesn't move she'll be released."
    $ renpy.sound.play("sounds/plant_slithering.mp3")
    ">You position a large, flowered tentacle above Hermione's head."
    her "What is that!?"
    $ renpy.sound.play("sounds/creaking.mp3")
    ">It suddenly opens to reveal a long slender appendage with an engorged base."
    her "What the hell is that? It looks like a..."
    ">While she is focused on the dangling limb above her you move six of your smaller tentacles towards her waist."
    her "Oh god no, someone please help me! Professor Sprout do something!"
    spo "Students, stand back!"
    ">Professor Sprout casts an impressive-looking spell at the mass of writhing tentacles."
    $ renpy.sound.play("sounds/magic3.mp3")
    spo "Confringo!"
    $ renpy.sound.play("sounds/boing.mp3")
    ">It strikes the plant forcefully but does nothing."
    spo "What? That should have killed it. It must be magically protected."
    ">You move three tentacles to Hermione's vagina and start teasing the opening."
    her "Please Professor Sprout, do something! Anything!"
    spo "I'm not sure I can, it has a powerful magical aura protecting it."
    spo "If I try anything more advanced than the spell I just cast, I might hurt you."
    ">You move two smaller tentacles to her asshole and start teasing the entrance, slowly prying it open."
    her "Then what am I supposed to do?!"
    spo "Just stay as still as possible and it should eventually let you go..."
    ">You move a tentacle with a mouth on the end of it to her right breast and latch onto it."
    her "Please, I'm not going to be able to stay still if this keeps going!"
    ">The three tentacles at the entrance of her vagina suddenly thrust into her."

    $ renpy.sound.play("sounds/slick_02.mp3")

    if her_reputation > 15:
        call tentacle_1
    else:
        call tentacle_2

    stop bg_sounds fadeout 3.0

    "> After everyone leaves the room your body starts to turn back to normal..."
    gen "That was hot!"
    "> You notice that something is amiss..."
    gen "What happened to my clothes?!"
    gen "... I was expecting this other-wordly magic to cover the basics of transmutations at the very least."
    gen "Guess I was wrong..."
    gen "I must get out of here before anyone spots me."

    call play_sound("running")

    "> You dash through the castle in a flash and get back to your office where, fortunately, you find your clothes lying in a pile behind the desk."

    hide screen blkfade
    with d5

    jump main_room

label tentacle_1: #Public path
    call cg_scene(folder="", layer="p1")
    hide screen blkfade
    with d9
    call ctc

    her "!!!"
    her "What on earth is going on?"
    play bg_sounds "sounds/slickloop.mp3" fadein 2 fadeout 2
    ">You slowly begin to move the tentacles in her vagina."
    call cg_scene("p2")
    her "Oh..."
    ">You move a small, mouthed tentacle to her ear so that only she can hear you."
    gen "Enjoying yourself slut?"
    her "Professor!"
    gen "That's right, just do as I say and relax."
    her "How am I supposed to relax?!"
    gen "Well if you're not going to relax, at least try to enjoy it..."
    ">You start rotating the tentacles in her vagina."
    $ renpy.sound.play("sounds/slick_02.mp3")
    call cg_scene("p3")
    her "..."
    spo "If you keep thrashing about so much it won't let you go, stay still girl!"
    her "I-I'm trying!"
    gen "Are you sure you're trying enough? Judging by how much you're moving I'd say that's quite the opposite."
    gen "Someone might even think that you are enjoying this."
    her "They wouldn't..."
    mal "Who's she talking to?"
    mal2 "I've got no idea, this bitch is crazy."
    gen "Are you sure? Do you think you'll be able to stifle every moan?"
    $ renpy.sound.play("sounds/slick_02.mp3")
    ">You push deeply into her with the three tentacles."
    her "!!!"
    call cg_scene("p4")
    gen "Do you think you'll be able to stop your hips from bucking?"
    ">You give her another powerful thrust."
    $ renpy.sound.play("sounds/slick_02.mp3")
    her "{size=-6}{heart}*Ah*{/size}"
    gen "Do you really think that you'll be able to stop yourself from begging me for more?"
    ">You increase the speed of the tentacles."
    play bg_sounds "sounds/slickloopfast.mp3" fadein 2 fadeout 2
    her "{size=-3}*mmmmmmm*{/size}"
    gen "I don't think you will. In fact I know that you won't."
    gen "Because I know what you are. A slut."
    gen "A slut who can only think about getting off when she's being fucked by a plant in front of her classmates."
    stop bg_sounds fadeout 2
    ">You stop moving the tentacles."
    gen "Now tell them what you are."
    her "W-w-what? No please, just don't stop."
    $ renpy.sound.play("sounds/creaking.mp3")
    gen "Tell them what you are and I'll keep going."
    her "I can't... Just keep going..."
    gen "Say it."
    her "{size=-3}I'm a slut.{/size}"
    play bg_sounds "sounds/slickloop.mp3" fadein 2 fadeout 2
    ">You start rotating the tentacles in her vagina ever so slowly."
    gen "What was that? I don't think that they heard you. Why don't you say it once more, with feeling."
    her "I'm a slut!"
    play bg_sounds "sounds/slickloopveryfast.mp3" fadein 2 fadeout 2
    ">You begin fiercely fucking her vagina."
    her "Yes, yes, I'm a fucking slut. Fuck me harder."
    gen "See that wasn't so hard now was it. How about I give you a little reward."
    her "Wha--"
    call cg_scene("p5")
    ">You thrust a ribbed tentacle deeply into her asshole in one motion."
    $ renpy.sound.play("sounds/slick_02.mp3")
    her "!!!"
    her "It's in my ass... I-I'm...{w=0.4} I-I'm cumming."
    ">You take alternating turns pumping into her ass and pussy."
    her "I'm cumming! It's too much..."
    call cg_scene("p6")
    $ renpy.sound.play("sounds/slick_01.mp3")
    ">You feel her body shudder as the orgasm rocks her."
    ">This only spurs you on to fuck her harder."
    her "Please... no more... I'll faint..."
    ">You start to feel a strange energy flowing through the vines, moving towards the tips."
    gen "This is it girl, get ready."
    her "... ready?..."
    call cg_scene("p7")
    stop bg_sounds fadeout 2
    $ renpy.sound.play("sounds/slick_01.mp3")
    ">With one final surge you release the pent up energy in a surge of white sap all over her."
    $ renpy.sound.play("sounds/slick_02.mp3")
    gen "By the gods, it's as if each vine is cumming. This is amazing..."
    $ renpy.sound.play("sounds/slick_02.mp3")
    ">The sensations proved to much for Hermione and she faints, going limp in your tentacles."
    mal "What a slut..."
    fem "That's what I've been telling you!"
    mal2 "Man, I'm going to have to join Gryffindor."
    hide screen cg
    show screen blkfade
    with d9
    pause.8
    ">You place Hermione back onto the desk as the plant that you are occupying slowly wilts and dies."
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay?"
    her "..."
    spo "Quickly, someone take her to the hospital wing."
    mal "Should we cover her up?"

    # This is the public route, don't change writing please!

    if hermione.is_worn("panties"):
        spo "Oh yes, I suppose you should."
        mal "{size=-4}Damn dude, have you seen her tits?!{/size}"
        ">*Squeeze* *Squeeze*"
        mal2 "{size=-4}Holy shit, they're soft.{/size}"
        spo "If you two don't stop that at once you'll get expelled."
        mal "S-sorry..."
        mal2 "Sorry professor!"
        spo "Just take her out."
    else:
        spo "No need, if she feels comfortable parading without panties in MY class, then she should be fine being taken naked to the infirmary."
        mal "Are you su--"
        spo "I said take her out!"
        mal "Y-yes ma'am..."

    call play_sound("walking")

    ">You hear the boys snickering to each other whilst they carry Hermione out in some unknown direction..."

    spo "Class dismissed!"

    hide screen cg
    show screen blkfade
    with d9
    pause.8

    return

label tentacle_2: # Personal path
    call cg_scene(folder="", layer="p1")
    hide screen blkfade
    with d9
    call ctc

    her "What kind of sick plant is this?!"
    play bg_sounds "sounds/slickloop.mp3" fadein 2 fadeout 2
    ">You start pumping the tentacles in her vagina slowly..."
    her "Oh..."
    ">You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    gen "Enjoying yourself, [hermione_name]?"
    her "Profes--"

    call cg_scene("e2")
    call ctc

    $ renpy.sound.play("sounds/slick_02.mp3")
    ">You quickly force another flowered tentacle into her mouth."
    gen "Now, now [hermione_name], you don't want anyone to find out how much you actually are enjoying yourself now, do you?"
    her "*Hmmmhhhhhhhhh* !"
    gen "Well, then just do what Miss Sprout says and stay still."
    gen "Just act like this is some horrible accident, that you are just a victim."
    gen "Instead of the slut that you really are..."
    $ renpy.sound.play("sounds/slick_02.mp3")
    ">You start to rotate the tentacles in her vagina."
    gen "!!! *HMMMMM*"
    mal "Wow, I think she's starting to enjoy it."
    fem "Hermione? No way, she's too stuck-up to let boys kiss her, not to mention enjoying sex. {size=-6}With a plant but still..{/size}"
    mal2 "I don't know man, she doesn't look like she hates it."
    play bg_sounds "sounds/slickloopfast.mp3" fadein 2 fadeout 2
    ">You increase the speed of the tentacles in her vagina."
    gen "Hear that, [hermione_name]? Your classmates are starting to realize how much you like getting your pussy stuffed."
    her "*NNNNNNNNNm*"
    gen "What was that? Faster you say?"
    gen "You got it, [hermione_name]!"
    call cg_scene("e3")
    play bg_sounds "sounds/slickloopveryfast.mp3" fadein 2 fadeout 2
    ">You begin fucking Hermione in earnest."
    her "*HMMMMMMm...!!!*"
    ">The sensation of fucking Hermione in two different holes is almost overwhelming."
    gen "I know you are loving every second of this..."
    gen "... Being fucked in front of your classmates."
    gen "Having your tits and pussy on display..."

    ">You move a ridged tentacle towards her ass."
    her "*mm eehh oorr mmmnooo*!"
    $ renpy.sound.play("sounds/slick_02.mp3")
    call cg_scene("e4")
    ">You enter her tight ass. The feeling of being in every hole at once is incredible."
    her "*mmmmmmmm*"
    ">Hermione barely manages a groan, overwhelmed by the shear amount of pleasure she is currently bombarded with."
    play bg_sounds "sounds/slickloop.mp3" fadein 2 fadeout 2
    gen "Admit it! You're loving this aren't you."
    gen "Having your holes filled in front of your classmates like the whore you are."
    gen "Go on say it! Tell me what you are!"
    her "*Hmmm aaaaa hhhhhhuuuttt*"
    gen "What was that, I couldn't quite make it out over the sound of you sucking dick."
    her "*Hmmm aaaaa hhhhhhuuuttt*!"
    gen "One last time. Say it like you mean it."
    call cg_scene("e5")
    ">As she exhales, you quickly remove the tentacle from her mouth."
    her "{size=+5}I'm a slut!{/size}"
    ">The realisation of what has just occurred hits her like a ton of bricks."
    her "I-I'm cumming... Professor--"
    call cg_scene("e6")
    $ renpy.sound.play("sounds/slick_02.mp3")
    ">You quickly reinsert the tentacle into her mouth, silencing her."
    gen "Good girl. Time for your reward."
    play bg_sounds "sounds/slickloopveryfast.mp3" fadein 2 fadeout 2
    ">You quicken the pace as she convulses beneath you."
    call cg_scene("e7")
    $ renpy.sound.play("sounds/slick_01.mp3")
    ">You explode inside of her from every tentacle-like heads, filling her up to the brim."
    stop bg_sounds fadeout 2
    $ renpy.sound.play("sounds/slick_02.mp3")
    mal "Told you she was a slut."
    $ renpy.sound.play("sounds/slick_02.mp3")
    fem "I guess you were right..."
    hide screen cg
    show screen blkfade
    with d9
    pause.8
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay? Miss Granger!"
    her "..................*Ah*"
    spo ".... She's breathing, thank be Merlin."
    spo "You! Yes, you girls! Take her to the hospital wing at once!"
    fem "W-wha-- But..."
    spo "What are you waiting for!"
    fem "{size=-4}Fine...{/size}"

    call play_sound("running")
    pause 3.0

    spo "Class dismissed!"

    return
