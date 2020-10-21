
# Mirror story: Whose points is it anyway?
label whose_points:

    $ temp_day = game.daytime
    $ game.daytime = True
    call update_interface_color
    call hide_screens

    show screen blkfade
    with d5

    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_default)

    $ ast_outfit_last.save()
    $ astoria.equip(ast_outfit_default)

    #TODO Equip Luna's default outfit (and store last)

    call ast_chibi("stand", 380, 420)
    call her_chibi("stand", 450, 426)
    call lun_chibi("stand", 530, 430)

    $ luna_zorder = 16
    $ astoria_zorder = 14

    centered "{size=+7}{color=#cbcbcb}Whose points is it anyway?{/color}{/size}"

    show screen whose_points_screen
    hide screen blkfade
    with d5

    stop music
    $ renpy.play("sounds/epic_intro.mp3")
    call bld

    g9 "Hello and welcome to \"whose points is it anyway?\""
    g9 "The show where everything is made up and the points don't matter."
    g9 "Just like at Hogwarts."
    $ renpy.play("sounds/applause01.ogg")
    call her_main("(I hope I win! I need those house points.)", "base", "happy", "base", "R", xpos="base", ypos="head")

    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1

    m "First, let me introduce today's contestants."
    m "The curly haired harlot we all know and love. Give it up for Hermione!"
    $ renpy.play("sounds/applause01.ogg")
    call her_main("...", "grin", "base", "worried", "mid", cheeks="blush", xpos=500, ypos="base")
    $ renpy.sound.play("sounds/wolf_whistle.mp3")
    call her_main("...", "base", "base", "worried", "mid", cheeks="blush")

    m "The ravishing ravenclaw who will rock your socks off. Luna! "
    $ renpy.play("sounds/applause01.ogg")
    call lun_main("...", "base", "wink", "base", "mid", xpos=650, ypos="base")
    $ renpy.play("sounds/giggle2_loud.mp3")
    call lun_main("*heh*... hello.", "base", "base", "base", "mid")

    m "And the small girl with a big personality. Astoria!"
    $ renpy.play("sounds/applause01.ogg")
    g9 "..."
    $ renpy.play("sounds/gasp3.mp3")
    call ast_main("Hey!", "scream", "base", "angry", "mid", xpos=380, ypos="base")

    pause.5
    hide screen hermione_main
    hide screen luna_main
    hide screen astoria_main
    with d5
    pause.5

    m "Today we're playing scenes from a hat."

    with hpunch
    $ renpy.play("sounds/MaleGasp.mp3")
    hat "What!? Stay the fuck away from me!"

    g4 "But the notes are already inside you...{w=0.5} I put them in there last night."

    hat "You put notes inside me without my consent?"
    $ renpy.play("sounds/burp.mp3")
    hat "*Burp*"
    hat "Pardon me."

    m "Looks like we have our first prompt."
    m "\"Things you might say in potions class, but also in your bedroom.\""

    call her_main("This cauldron hasn't been used for years. It's all mouldy and full of muck!", "grin", "base", "worried", "mid", cheeks="blush", xpos="right", ypos="base")

    $ renpy.play("sounds/applause01.ogg")
    hat "Boo! There's no cauldrons in the bedroom!"

    m "Quiet now, it was a good euphemism. Ten points to Gryffindor."
    hide screen hermione_main
    with d3

    call ast_main("Snape! Get your gross hands off my shoulders, you creep!","clench","narrow","angry","mid", xpos="right", ypos="base")

    $ renpy.sound.play("sounds/cough_male.mp3")
    mal "..."
    m "I'm not sure you got the idea of the game there..."
    hide screen astoria_main
    with d3

    call lun_main("Oops... I was supposed to squeeze the mucus out with my hands and not crush it.","silly","closed","raised","mid", xpos="right", ypos="base")

    $ renpy.play("sounds/applause01.ogg")
    m "Sounds painful... Fifteen points to Ravenclaw."
    hide screen luna_main
    with d3

    call her_main("(How's that worth more than mine?)", "annoyed", "base", "worried", "mid")
    hide screen hermione_main
    with d3

    m "Any more?{w=0.5} On to the next prompt then... Hat?"
    hat "Sorry, what did you *cough* call me? That's {i}Sorting Hat{/i} to you..."
    $ renpy.play("sounds/burp.mp3")
    hat "*Burp*"
    hat "That one was spicy..."
    m "Ah, this one..."
    g9 "\"Things you might do in Quidditch, but also with your lover...\""

    call ast_main("I'm going first this time! I have a good one!","smile","base","base","mid")
    m "Go on..."
    call ast_main("Madam Hooch! Get your gross hands off my quidditch robes, you creep!" ,"clench","narrow","angry","mid")
    m "Again, I don't think you understand the game..."
    call ast_main("Give me the points!","scream","narrow","angry","mid", trans=hpunch)
    m "Disqualified!"
    call ast_main("Wait, you can't do that!","clench","base","base","mid")
    g9 "It's my game, I make the rules."
    call ast_main("(We'll see about that...)","annoyed","narrow","angry","R")
    hide screen astoria_main
    with d3

    call her_main("My turn.")
    call her_main("I love the feeling of a hard wooden object between my legs.{w=0.5} I tend to tense up during the climax.","grin", cheeks="blush")

    $ renpy.play("sounds/applause01.ogg")
    m "A bit direct, but I like it.{w=0.5} Fifteen points to Gryffindor."
    hide screen hermione_main
    with d3

    call lun_main("It's quite exciting but also a bit hard. You need to make sure not to end up with one of the balls in your throat.","grin","seductive","raised","mid")

    g9 "(I don't mind having you end up with one of mine in your throat one day, if you know what I mean...)"

    $ renpy.play("sounds/applause01.ogg")
    m "Twenty points to Ravenclaw."
    hide screen luna_main
    with d3

    call her_main("(Seems like pleasing the judge is the way to go. Only one round left...)", "annoyed", "base", "worried", "mid")
    hide screen hermione_main
    with d3

    m "Last round ladies. You better make it a good one. It's still all to play for."
    m "The last note, if you please!"

    hat "..."
    m "If you please..."
    hat "I'm all out, looks like you only wrote two after all."

    g4 "That can't be right..."

    call ast_main("Let me check professor!","smile","base","base","mid")
    $ renpy.play("sounds/cloth_sound.mp3")
    call ast_main("*Hmm*...{w} It has to be here somewhere...","annoyed","base","base","down")
    call ast_main("There it is! It was stuck under one of the folds!","smile","base","base","mid")
    hide screen astoria_main
    with d3

    $ renpy.sound.play("sounds/MaleGasp.mp3")
    hat "Are you calling me fat, young lady?!"

    call ast_main("I'll read it for you, shall I?","smile","closed","base","mid")

    m "Go ahead..."

    call ast_main("\"Things that you would not share with your classmates, but would share with...\" what do you call him again? ah yes, \"[lun_genie_name]\".","open","base","base","down")
    hide screen astoria_main
    with d3

    m "(I don't remember writing that one...)"

    call lun_main("I see invisible creatures... but people don't belie... ","soft","annoyed","sad","down")
    hide screen luna_main
    hide screen bld1
    with d3
    pause.1

    stop music
    call her_chibi("lift_top", 450, 426)
    with d5
    pause.8

    $ hermione.strip("bra", "top")

    $ renpy.sound.play("sounds/crowd_gasp.mp3")
    call her_main("...", "smile", "base", "worried", "mid")

    g9 "Five hundred points to Gryffindor!"
    hide screen hermione_main
    with d3

    call lun_main("That's cheating, I didn't even get to finish! ","scream","mad","angry","mid")
    hide screen luna_main

    m "Well, that's all for this episode of \"whose points is it anyway?\""

    call her_main("I win, all the points for me!", "smile", "base", "worried", "mid")
    hide screen hermione_main
    with d3

    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1
    call lun_main("Don't end now! This game is rigged!","scream","mad","angry","mid")
    hide screen luna_main
    with d3

    m "And remember, the points don't matter!"

    call her_main("Wait, they don't?! I thought they were house points!", "annoyed", "base", "worried", "mid")
    hide screen hermione_main
    with d3

    call ast_main("Harlot! Harlot! Harlot!","grin","closed","base","mid", xpos="400", ypos="base")

    call lun_main("How do those points taste now? ","grin","base","base","mid", xpos="600", ypos="base")
    call lun_main("The whole wizarding world is going see your tits!","silly","base","base","mid")
    hide screen luna_main
    hide screen astoria_main
    with d3

    call her_main("Oh no, I forgot about that!", "shock", "base", "worried", "mid", tears="crying")

    $ renpy.play("sounds/epic_intro.mp3")
    $ renpy.play("sounds/applause01.ogg")
    g9 "Good night!"

    "To be continued?"

    $ luna_zorder = 15
    $ astoria_zorder = 15

    $ hermione.equip(her_outfit_last)
    $ astoria.equip(ast_outfit_last)

    $ game.daytime = temp_day

    call set_her_action("none")
    jump enter_room_of_req
