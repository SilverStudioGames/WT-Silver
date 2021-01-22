### Yule Ball Ending ###

label ball_ending_start:
    m "[hermione_name], that ball you've mentioned..."
    m "When did you say it would start again?"
    call her_main("The autumn ball?!", "grin", "base", "base", "mid")
    call her_main("I'm so excited!!! I can't wait for it!", "grin", "happyCl", "base", "mid")
    call her_main("Just two more days, [genie_name]", "base", "narrow", "base", "mid_soft")
    m "That soon, *huh*?"
    call her_main("Yep! I still have a tonne of preparation to do, though.", "soft", "base", "base", "R")
    m "Well then I better not keep you occupied any longer..."
    m "Unless..."
    g9 "Maybe we could..."
    call her_main("Have some fun?", "soft", "narrow", "base", "mid_soft")
    g9 "You can read my mind, girl."

    $ ball_quest.started = True
    $ ss_event_pause += 2

    jump hermione_favor_menu


screen genie_snape_shake_hands(shake=False):
    if shake:
        add "characters/snape/chibis/handshake/hand_01.webp" pos (220, 205) zoom 0.5
    else:
        add "characters/snape/chibis/handshake/hand_00.webp" pos (220, 205) zoom 0.5

label ball_ending_E1:
    stop music fadeout 1.0

    call sna_walk(action="enter", xpos="desk", ypos="base")
    pause.8

    call play_music("snape")
    call sna_main("Genie...","snape_01", xpos="base", ypos="base")
    m "Severus?"
    call sna_main("I think I may have figured out why your magic does not work the way it should...","snape_05")
    g4 "Seriously?!"
    call sna_main("Yes...","snape_23")
    sna "It's quite obvious actually... I'm surprised that it didn't cross my mind before."
    call sna_main("You see, the thing is that every building in Hogwarts is enchanted with all kinds of protection spells...","snape_24")
    m "Protection spells, *huh*?"
    call sna_main("Yes...","snape_23")
    sna "Very powerful, old and nasty magic..."
    call sna_main("Even the land itself is heavily enchanted for miles in every direction...","snape_24")
    m "*Hmm*..."
    call sna_main("Basically, any number of spells could be interfering with your powers around here...","snape_25")
    m "Wait, then how come you have no problems casting {i}your{/i} spells?"
    call sna_main("Well, you see, my magic is \"Hogwarts magic\"...","snape_05")
    sna "But I suspect your powers are alien enough to be perceived as a threat."
    m "Interesting..."
    call sna_main("I think if you manage to get away far enough from the school grounds--","snape_24")
    m "I will be able to go home!{w=0.5} finally..."
    call sna_main("Yes, and the best time to do that would be tonight.","snape_02")
    call sna_main("While everyone is preoccupied with that bloody Autumn ball, you could sneak out unnoticed...","snape_23")

    ### SHAKE HANDS WITH SNAPE ###
    hide screen snape_main
    call blkfade

    hide screen bld1
    call gen_chibi("hide")
    call sna_chibi("hide")
    show screen genie_snape_shake_hands(False)

    play music "music/machinations-by-kevin-macleod.mp3" fadein 1 fadeout 1
    pause 1
    call hide_blkfade

    m "Right, today is the night of the Autumn ball..."
    m "So it ends tonight then..."
    call sna_main("Seems like it...","snape_09")
    call hide_blkfade
    pause.5

    call sna_main("So... Just in case I will never see you again...","snape_05")
    m "Right..."

    show screen genie_snape_shake_hands(True)
    with d3
    pause 2

    call sna_main("The past several month were the best months of my life, Genie...","snape_26")
    call sna_main("Thank you for that...{w=0.3} you incredible traveller from another world...")
    call sna_main("Thank you, my friend...")
    m "I don't know what to say, Severus..."
    call sna_main("Then don't say anything...","snape_06")
    call sna_main("Just move on to your next adventure...")
    call sna_main("Our world has stalled you long enough...")
    m "Thank you for keeping me company and being my only friend here, Severus."
    call sna_main("Thank you for being mine...","snape_27")
    call sna_main("I'd better go now...","snape_06")

    # Goes to the door, stops and turns around.
    call blkfade

    hide screen snape_main
    hide screen genie_snape_shake_hands
    call gen_chibi("sit_behind_desk")
    call sna_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade
    pause.5

    call sna_walk("door", "base")
    pause.5

    call sna_chibi("stand","door","base", flip=False)
    pause.5

    call sna_main("One more thing though...","snape_01", ypos="head")
    m "Yes?"
    call sna_main("If it all goes well...","snape_24")
    call sna_main("Will I find the real Albus Dumbledore in that chair tomorrow?")
    m "I believe so..."
    call sna_main("*Hmm*...","snape_04")
    call sna_main("Albus can't know that I was aware of his absence...","snape_03")
    call sna_main("Is there a way to tell you guys apart?","snape_01")
    m ".............."
    m "How about a secret password?"
    call sna_main("A password?","snape_05")
    m "Yes... just ask me tomorrow: \"Who rules?\""
    call sna_main("\"Who rules?\"","snape_01")
    g9 "\"Robin Williams!\""
    call sna_main("Robin Wil--... *Err*...{w=0.3} I'm sorry, who?","snape_05")
    m "You didn't see the \"Flubber\"? Great movie. Just came out."
    call sna_main("Can't say that I have...","snape_02")
    call sna_main("Alright then...","snape_06")
    call sna_main("Have a safe trip home...")
    m "Thank you. Have fun hosting the ball..."
    call sna_main("*Sigh*","snape_06")

    call hide_characters

    pause.3

    stop music fadeout 1.0

    call sna_chibi("stand","door","base", flip=True)
    with d3
    pause.3

    call sna_chibi("leave")
    with d3
    pause.8

    m "............................"
    m "So this is it then..."

    call play_music("despair")
    m "Seems like my time in this world has come to an end..."
    m "......................."

    if not public_whore_ending:
        # Personal whore ending
        # Writing a letter
        m "That Means I'll probably never see the girl again..."
        m "..........."
        m "When I first met her she was so annoying..."
        m "to be honest, all the training I put her through changed very little in that regard..."
        m "But we did have a few special moments together..."
        m ".............."
        m "......................"
        m "It doesn't feel right to leave her without saying goodbye properly..."
        m "And yet I don't want to miss my chance to sneak out unnoticed..."
        m "I don't like long goodbyes..."
        m "*Hmm*..."
        m "I suppose I could leave her a note or something..."

        m "Let's see..."

        call gen_chibi("paperwork")
        with d3
        m "\"Dear...\""
        call gen_chibi("paperwork_idle")
        with d3
        m "*Hmm*... How should I address her?"

        menu:
            m "Dear..."
            "\"Miss Granger\"":
                $ word_01 = "Hermione Granger"
            "\"Nasty whore\"":
                $ word_01 = "Nasty whore"
            "\"Slut\"":
                $ word_01 = "Slut"
            "\"Cumbucket\"":
                $ word_01 = "Cumbucket"
            "\"Human female\"":
                $ word_01 = "Human female"
            "\"friend\"":
                $ word_01 = "Friend"

        call gen_chibi("paperwork")
        with d3
        m "Yes, \"Dear [word_01]\" fits perfectly..."
        "*scribble-scribble-scribble*"
        "*scribble-scribble-scribble*"
        m "\"... it is time for me to go back...\""
        call gen_chibi("paperwork_idle")
        with d3
        m "What should I write now?"

        menu:
            m "... time to go back..."
            "\"home\"":
                $ word_02 = "home"
            "\"to the mother-ship\"":
                $ word_02 = "to the mother-ship"
            "\"to Dimension \"X\"":
                $ word_02 = "to Dimension \"X\""
            "\"to my world\"":
                $ word_02 = "to my world"
            "\"To my Home Planet - Krypton\"":
                $ word_02 = "to my Home Planet - Krypton"

        call gen_chibi("paperwork")
        with d3
        m "Yes, \"Time to go back [word_02]\" that will do..."
        "*scribble-scribble-scribble*"
        "*scribble-scribble-scribble*"
        m "\"... farewell my little...\""
        call gen_chibi("paperwork_idle")
        with d3
        m "What should I write now?"

        menu:
            m "... farewell my little... "
            "\"cock-hungry slut\"":
                $ word_03 = "cock-hungry slut"
            "\"cum receptacle\"":
                $ word_03 = "cum receptacle"
            "\"Girl\"":
                $ word_03 = "girl"
            "\"Witch\"":
                $ word_03 = "witch"

        call gen_chibi("paperwork")
        with d3
        m "Yes, \"farewell my little [word_03]\" sounds about right..."
        "*scribble-scribble-scribble*"
        "*scribble-scribble-scribble*"
        call gen_chibi("paperwork_idle")
        with d3
        m "And now to sign it as..."

        label stupid_kent:
            pass

        menu:
            m "..."
            "\"Genie\"":
                $ word_04 = "Genie"
            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                call gen_chibi("paperwork")
                with d3
                m "Yes, \"sincerely yours, [word_04]\"..."
                call gen_chibi("paperwork_idle")
                with d3
                m "..........."
                m "No, that doesn't make any sense..."
                jump stupid_kent
            "\"Lord Voldemort\"":
                $ word_04 = "Lord Voldemort"
            "\"Traveller\"":
                $ word_04 = "Traveller"

        call gen_chibi("paperwork")
        with d3
        m "Yes, \"[word_04]\"..."
        call gen_chibi("sit_behind_desk")
        with d3
        m "........................"
        m "Yes, this should do..."

    m "Well, off I go then..."

    call blkfade

    call gen_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade

    call gen_walk("door", "base")
    pause.5

    m "...................."
    m "Agrabah... here I come..."
    pause .5

    call gen_chibi("leave")
    pause 1
    call blkfade

    stop music fadeout 1.0
    stop bg_sounds
    stop weather

    # Outskirts of Hogwarts
    centered "{size=+7}{color=#cbcbcb}Outskirts of Hogwarts{/color}{/size}"

    call play_music("night_outside")

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")

    pause.3
    call hide_blkfade
    call ctc

    pause.5
    call play_sound("walking_on_grass")

    $ ccg(layer2="172")

    m "Severus was right..."
    m "The farther away I get from the school grounds..."
    m "The more powerful I'm starting to feel..."

    $ ccg(layer3="173")
    pause.5

    m "I think  this is far enough..."
    m "Time to undo the spell and go back home..."
    m ".........."
    m "...................."
    m "Agrabah, here I come..."

    if not persistent.game_complete:
        # First play-through
        # Fake early ending
        call ctc

        show screen blkfade
        with d9
        pause .5

        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.

        centered """{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}This is ending \"00\" out of \"02\".{/color}{/size}"""

        centered "{size=+7}{color=#cbcbcb}Thank you for playing!{/color}{/size}\n\n"

        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Wait, I'm still here!"

        centered "{size=+7}{color=#cbcbcb}WHAT?!{/color}{/size}"

        g4 "I said I am still here, dammit!"

        centered "{size=+7}{color=#cbcbcb}Oh... :({/color}{/size}"

        $ ccg(layer3="blank")
        hide screen blkfade
        with d9

        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.

    m "....................."
    $ ccg(layer3="blank")
    m "No, I can't just leave like this!"
    m "I must see the girl one last time..."

    call play_sound("walking_on_grass")

    $ ccg(layer2="blank")

    call ctc

    hide screen ccg
    call blkfade
    stop music fadeout 1.0

    if not persistent.game_complete:
        # First play-through
        centered "{size=+7}{color=#cbcbcb}Fine whatever...{/color}{/size}"

    jump ball_ending_E2


label ball_ending_E2:
    # Main part of the ball event
    # Event replay starts here

    call blkfade
    play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1

    centered "{size=+7}{color=#cbcbcb}The Annual Hogwarts Autumn Ball{/color}{/size}"

    # Scene Setup
    $ game.daytime = True
    call update_interface_color

    hide screen bld1
    hide screen blktone
    call her_chibi("hide")

    $ dynamic_cg("ball", "background")

    #Setting up Hermione's outfit.
    $ hermione.equip(her_outfit_ball)

    hide screen hermione_main
    hide screen room # MAIN BG (DAY).

    hide screen notes
    with fade
    pause.1

    hide screen bld1
    hide screen blktone
    call hide_blkfade
    call ctc


    m "I better make sure to avoid being noticed..."
    m "......................"
    m "That's a whole lot of people out there..."
    m "How big is this school?!"
    m ".................."
    m ".................................."
    m "I don't see the girl anywhere..."
    m ".............."
    m "......................"
    m "She has got to be here somewhere..."
    m "................"
    m "................................."

    call blktone_top

    if public_whore_ending:
        # Public whore ending
        # Students talking
        mal "Have you heard that rumour about Hermione Granger?"
        mal2 "That she is a major slut?"
        mal "*huh*? No, that's not a rumour, that's a fact."
        mal "The rumour was that she is being paid in house points to whore herself out."
        mal2 "*Hmm*... I don't believe that. I think she is just a slut."
        fem "Who's a slut?"
        mal "Oh, hey you..."
        fem "So, who's a slut?"
        mal2 "Hermione Granger..."
        fem "*Tsk*! You, guys are talking about that whore again?"
        fem "That girl jerks off a couple of dicks, gives a few blowjobs and suddenly she is the school's new sensation."
        fem "Pathetic little muggle-born..."
        mal "You should not be jealous of--"
        fem "Jealous? Of her? Puh-lease!"
        fem "I have no use for popularity that comes from putting cocks in my mouth!"
        mal "Well, if you ever change your mind..."
        fem "*huh*?"
        mal "Feel free to use me as a stepping stone on your road to fame!"
        fem "You wish!"
        mal2 "Hey, guys, I think that's Hermione over there!"
        mal "You're right!"
        mal2 "Do you think if I ask her to the dance, I might get lucky later?"
        mal "Not if I ask her first!"
        call play_sound("walking")
        pause 2
        mal2 "Hey, wait up! That was my idea!"
        call play_sound("running")
        pause 2
        fem "Guys...?"
        fem "........................."
        fem "*Tsk*... Men......"

    else:
        # Personal whore ending
        # Students talking
        mal "{size=-4}Have you heard the rumours?{/size}"
        mal2 "{size=-4}Yeah, they say Hermione took one for the team.{/size}"
        fem "{size=-4}Whoring herself out for house points!{/size}"
        fem "{size=-4}How disgraceful!{/size}"
        mal "{size=-4}Those are just rumours!{/size}"
        fem "{size=-4}I think it's more than just that...{/size}"
        mal "{size=-4}Oh, shut up! You are just jealous.{/size}"
        mal2 "{size=-4}Yeah, you wish you had Hermione's courage!{/size}"
        mal "{size=-4}Exactly! No one is more loyal to Gryffindor than she is!{/size}"
        mal "{size=-4}Even if the rumours are true, what does it matter?{/size}"
        mal "{size=-4}Thanks to her sacrifice our house will be getting the cup this year!{/size}"
        mal2 "{size=-4}Yeah, and what did you ever do for our house?{/size}"
        fem "{size=-4}I..... But....{/size}"
        mal "{size=-4}Exactly! So don't you bad-mouth Hermione!{/size}"
        mal2 "{size=-4}You said it, man.{/size}"
        fem "{size=-4}*Pouting*{/size}"

    hide screen bld1
    call hide_blktone_top
    call ctc

    $ dynamic_cg("ball/intro", "background", "bloom", "foreground", "overlay")
    pause 1.0
    m "(*Hmm*... I don't see her...)"
    pause 1.0
    $ dynamic_cg("ball/intro", "background", "bloom", "hermione", "foreground", "overlay")
    pause 0.5
    g9 "(There she is!)"

    mal "Hermione, hey..."
    call her_main("Oh, hello.", "base", "base", "base", "mid", xpos="base", ypos="head")
    mal "You look... so beautiful tonight, Hermione."
    call her_main("Thank you, you are too sweet.", "base", "closed", "base", "mid")
    mal2 "Can I have the next dance?"
    mal "What? Back off buddy, I was here first!"
    mal2 "Like hell you were!"
    mal "Alright, pal! That does it!"
    mal2 "I'm not your \"pal\", buddy!"
    call her_main("..............", "open", "wide", "worried", "stare")

    call blktone_top
    stop music fadeout 3.0
    m "(Here is my chance!)"
    m "Psst! Girl!"
    call her_main("???", "upset", "base", "base", "mid")
    m "Girl, it's me! Over here!"
    call her_main("[genie_name]?", "open", "base", "base", "mid")
    m "Shush! Keep your voice down and follow me."
    call her_main("Oh?", "open", "base", "base", "mid")

    $ dynamic_cg("ball/bj", "background")
    call hide_blktone_top
    call ctc

    call her_main("Sir, what is going on? Why are you... lurking in the shadows?", "upset", "base", "base", "mid")
    m "Just be quiet and listen for a second! Can you do that for me?"
    call play_music("playful_tension") # SEX THEME.
    call her_main("Yes, sir...", "upset", "base", "base", "mid")
    m "Well, here is the thing..."
    m "There is something you need to kn--"
    call her_main("Of course sir!", "grin", "happy", "base", "mid",cheeks="blush")
    m "What?"
    call her_main("Let's just make this quick, alright?", "soft", "narrow", "base", "R_soft",cheeks="blush")
    g4 "Let's make what quick?"
    call her_main("You want me to thank you for the dress, don't you, sir?", "base", "narrow", "base", "mid_soft",cheeks="blush")
    m "The dress? No, no that's not why I am here."
    call her_main("It is fine, sir. I do not mind.", "soft", "narrow", "base", "R_soft",cheeks="blush")
    m "Listen to me, girl! I am not who you think--"
    call her_main("Please, sir, let me suck on your cock a little.", "open_tongue", "narrow", "worried", "mid_soft",cheeks="blush")
    g4 "*Gh*--!!!"
    call her_main("Just a little will do. Please? I'm begging you...", "open_tongue", "narrow", "worried", "mid_soft",cheeks="blush")
    g4 "Damn you, you damn witch!"
    g4 "Stop this! I really need to talk to you!"
    call her_main("Well of course, sir.", "base", "narrow", "base", "mid_soft",cheeks="blush")
    call her_main("Put your dick in my mouth and talk to me.", "open_tongue", "narrow", "worried", "mid_soft",cheeks="blush")
    call her_main("Talk dirty to me...")
    g4 "*growl*!"
    m "*Sigh*...."
    m "Fine, have it your way..."
    m "But you are abusing your power, girl!"
    call her_main("*Giggle*!", "crooked_smile", "happyCl", "worried", "mid",cheeks="blush")
    m "And after we're done, we'll have that talk!"

    show screen blkfade
    with d7

    her "*Slurp*! *Slurp*! *Slurp*!"
    m "................."

    hide screen bld1
    hide screen blkfade
    $ dynamic_cg("ball/bj", "background", "base", "sweat")
    call ctc

    her "*Slurp*! *Gulp*! *Slurp*!"
    her "*Slurp*--"
    $ dynamic_cg("ball/bj", "background", "base2", "sweat2")
    her "*huh*.........."
    her "...................."
    $ dynamic_cg("ball/bj", "background", "base", "sweat")
    her "*Slurp*! *Gulp*! *Slurp*!"
    m "Yes... Like that.... oh... yes..."
    her "*Gulp*! *Slurp*! *Slurp*!"
    her "*Gulp*--"
    $ dynamic_cg("ball/bj", "background", "base2", "sweat2")
    her "...................." #LOOKING BACK
    m "Just keep going girl."
    m "I will let you know if I see someone coming..."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_open2", "sweat2")
    her "Oh... I'm not worried about that, sir..."
    m "*Hmm*?"
    her "They are supposed to make the announcement soon..."
    $ dynamic_cg("ball/bj", "background", "base", "sweat")
    her "*Slurp*! *Gulp*! *Slurp*!"
    m "The announcement?"
    her "*Slurp*! *Slurp*! *Slurp*!"
    her "*Slurp*--"
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_open2", "sweat2")
    her "Yes. About the coronation..."
    $ dynamic_cg("ball/bj", "background", "base", "sweat")
    her "*Gulp*! *Slurp*! *Gulp*!"
    m "What...?"
    her "*Slurp*--"
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "mouth_open2", "sweat2")
    her "The Hogwarts autumn ball queen coronation, sir."
    m "Oh... Is that a thing?"
    m "Any chance you might be chosen?"
    her "A chance?"
    her "It's already been decided, sir."
    m "What?"
    her "Oh, I mean I hope I will win..."
    her "But since I am the one who organised the whole thing, it is only fair..."
    her "Wouldn't you agree, sir?"
    m "Well... Sounds like cheat--"
    $ dynamic_cg("ball/bj", "background", "base", "eyes_up", "sweat")
    her "*Slurp*! *Slurp*! *Slurp*!"
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_smile2", "sweat2")
    her "Wouldn't you agree, sir?"
    m "*Err*..."
    her "Wouldn't you?"
    with hpunch
    $ dynamic_cg("ball/bj", "background", "base3", "blush3")
    her "{size=+7}*gobble*!{/size}" #DEEPTHROATING
    g4 "{size=+7}Oh, yes!!!{/size}"
    her "*gobble-gobble-gobble*!"
    her "*gobble*"
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_smile2", "sweat2")
    her "Good. I knew you would approve."
    $ dynamic_cg("ball/bj", "background", "base", "eyes_up", "sweat")
    her "*Slurp*! *Slurp*! *Gulp*!"
    m "Oh... This is amazing..."
    her "*Slurp*! *Slurp*! *Gulp*!"

    sna "*Khem*!"
    sna "Attention, maggots!"
    m "(Snape?)"
    sna "Quiet down everyone!"
    sna "It is time to announce who will be this year's queen of the annual Hogwarts autumn ball."

    her "*Slurp*--"
    $ dynamic_cg("ball/bj", "background", "base2", "sweat2")
    her "Oh no! I think they are about to start..."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_open2", "sweat2")
    her "But I can't just leave you in this...{w=0.5} condition, sir."

    $ dynamic_cg("ball/bj", "background", "base2", "eyes_down2", "sweat2")
    her "What should I do?"
    m "Just go, girl. We can finish this up later."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_open2", "sweat2")
    her "But... But you got me this dress, sir, and..."
    her ".........."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "mouth_open2", "sweat2")
    her "No, I can't just leave you like this, sir."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "mouth_smile2", "sweat2")
    m "Fine! Finish the job then."
    m "If you put some effort into this we'll be done in no time."
    m "I believe in you, girl."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "sweat2")
    her "*Hmm*..."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_open2", "sweat2")
    her "Then you must promise me something, sir."
    m "Yes, what is it?"
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_up2", "mouth_happy2", "sweat2")
    her "Please, do not restrain yourself."
    g9 "Heh... I rarely do, girl."

    $ dynamic_cg("ball/bj", "background", "base2", "sweat2")
    sna "This year's Hogwarts Autumn Ball queen is..."
    sna "Let's see... Can't open the damn envelope..."
    $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "sweat2")
    her "Alright, sounds like we have no time to lose."

    if public_whore_ending:
        # Public whore ending
        $ dynamic_cg("ball/bj", "background", "base", "sweat")
        her "*Slurp*! *Gulp*! *Slurp*!"
        m "Yes! That's the spirit!"
        $ dynamic_cg("ball/bj", "background", "base", "lashes", "sweat", "sperm")
        her "*Gulp*! *Slurp*! *Gulp*!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_open2", "eyes_up2", "blush2", "sweat2")
        her "Sir, is this really the proper way to treat one of your students?"
        m "*huh*?"
        $ dynamic_cg("ball/bj", "background", "base", "lashes", "sweat", "sperm")
        her "*Slurp*! *Gulp*! *Gulp*!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "blush2", "sweat2")
        her "I am like a fragile and impressionable little dove..."
        her "Entrusted to your care by my parents..."
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_grimmace2", "eyes_up2", "brows2", "blush2", "sweat2")
        her "You were supposed to treat me {i}right{/i}, sir..."
        her "And what did you do instead?"
        m "*Ahem*! Let me repeat my previous statement..."
        m "{size=+7}\"*huh*?\"{/size}"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_happy2", "eyes_down2", "brows2", "blush2", "sweat2")
        her "You put your penis in my innocent mouth, sir!"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "blush", "sweat")
        her "*Slurp*! *Slurp*! *Slurp*!"
        g9 "Oh, I see! Yes, I like this innocent girl act!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_open2", "eyes_up2", "blush2", "sweat2")
        her "You pretended to be kind to me..."
        her "You bought me this dress..."
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "blush2", "sweat2")
        her "And then........."
        $ dynamic_cg("ball/bj", "background", "base", "eyes_up", "sweat")
        her "*Slurp*! *Gulp*! *Gulp*!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "blush2", "sweat2")
        her "You took advantage of me, sir!"
        her "Tricked me into sucking your big cock!"
        g4 "Oh... Yes! You're good!"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_grimmace2", "lashes2", "blush2")
        her "I'm supposed to be enjoying the ball with my classmates right now..."
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_grimmace2", "brows2", "blush2")
        her "But what am I doing instead?"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_up")
        her "*Slurp*! *Slurp*! *Slurp*!"
        m "Oh..."
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "brows", "blush")
        her "*Slurp*! *Gulp*! *Slurp*! *Slurp*! *Slurp*!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "mouth_open2", "brows2", "blush2")
        her "I'm on my knees, sucking off my headmaster!"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "brows", "blush")
        her "*Slurp*! *Slurp*! *Gulp*!"
        m "Oh, yes you are, you little slut!"
        her "*Slurp*! *Slurp*! *Slurp*!"
        her "*Slurp*! *Slurp*! *Gulp*!"
        g4 "You are really good at this dirty talk stuff..."
        g9 "You should try writing a fairy tale, or something..."
        $ dynamic_cg("ball/bj", "background", "base", "eyes_up", "blush")
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_open2", "eyes_up2", "blush2")
        her "Oh, but I wouldn't know how, sir..."
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "blush2")
        g4 "You nasty little thing!"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "brows", "blush")
        her "*Slurp*! *Slurp*! *Gulp*! *Slurp*! *Slurp*!"

        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur starts running through the crowd of students."

        her "*Slurp*! *Slurp*! *Gulp*!"
        her "*Gulp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_open2", "eyes_up2", "blush2")
        her "Sir, am I being an obedient little slut?"
        g4 "Yes you are, girl!"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_grimmace2", "brows2", "blush2")
        her "Would you say that I am a good student?"
        g9 "I would say that you are an excellent student, girl!"
        $ dynamic_cg("ball/bj", "background", "base2", "eyes_closed2", "blush2")
        her "Good..."
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_smile2", "eyes_down2", "brows2", "blush2")
        her "I'm making my mommy and my daddy proud!"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "blush")
        her "*Slurp*! *Slurp*! *Gulp*!"
        g4 "Oh, girl, you are killing me!"
        her "*Slurp-slurp-slurp-slurp*!!!"
        g4 "Oh, yes! Like that!"
        her "*Slurp*--"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_grimmace2", "brows2", "blush2")
        her "Do I deserve a reward, sir?"
        $ dynamic_cg("ball/bj", "background", "base2", "mouth_happy2", "eyes_up2", "blush2")
        her "I would like you to reward me with your cum, please."
        g4 "*Grh*!"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_closed", "brows", "blush")
        her "*Slurp*! *Slurp*! *Slurp*!"
        g4 "*Geh*! Almost...!"
        her "{size=+5}*Slurp-gulp-slurp-slurp*!!!{/size}"
        g4 "{size=+5}Here it com--{/size}"
        $ dynamic_cg("ball/bj", "background", "base", "eyes_down", "brows", "blush")
        her "*Slurp*.........................."
        her "!!!"
        call ctc

        call blkfade
        $ dynamic_cg("ball/bj", "background", "base4", "lashes4", "brows4", "blush4")
        g4 "{size=+5}What the...!? Why did you stop?!{/size}"
        g4 "{size=+5}What the hell are you doing--{/size}"
        call hide_blkfade
        call ctc

        her "{size=+5}Cum for me, sir! Cum for me!{/size}"
        with hpunch
        g4 "{size=+5}What the hell is this?!{/size}"
        $ dynamic_cg("ball/bj", "background", "base4", "eyes_up4", "mouth_smile4", "brows4", "blush4")
        her "{size=+5}Cum for me, sir! I want your hot cum on me!{/size}"
        g4 "*Argh*! You whore!"
        $ dynamic_cg("ball/bj", "background", "base4", "eyes_up4", "lashes4", "brows4", "blush4")
        her "{size=+5}Yes I am!{/size}"
        her "{size=+5}Nothing but a cum hungry whore, sir!{/size}"
        with hpunch
        g4 "{size=+7}*Argh*!!!{/size}"
        g4 "{size=+7}Take this, then!!!{/size}"

        show screen white
        pause .1
        hide screen white
        with hpunch

        g4 "{size=+7}*ARGH*!{/size}"
        $ dynamic_cg("ball/bj", "background", "base4", "eyes_up4", "lashes4", "blush4")
        her "{size=+5}*Ah*! Yes, sir! Yes! cum for me!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch

        g4 "{size=+7}*ARGH*!{/size}"
        g4 "{size=+7}*Argh*!!! YES!!!{/size}"
        $ dynamic_cg("ball/bj", "background", "base4", "lashes4", "blush4")
        her "*Ah*... yes... *ah*..."
        g4 "Oh... *ght*... *panting*"
        $ dynamic_cg("ball/bj", "background", "base4", "eyes_up4", "lashes4", "blush4")
        her "Thank you sir..."
        $ dynamic_cg("ball/bj", "background", "base4", "mouth_smile4", "sperm4", "lashes4", "blush4")
        her "..........................................."
        call ctc

        call blkfade
        pause.5

        m "What on earth just happened, girl?!"
        call her_main("What do you mean, sir?", "soft", "narrow", "base", "R_soft",cheeks="blush", ypos="head")
        $ dynamic_cg("ball/bj", "background")
        call hide_blkfade

        m "Do I really need to point this out to you?"
        g4 "{size=+5}Do I really?{/size}"
        call her_main("Oh... You mean the hair thing...?", "soft", "narrow", "base", "R_soft",cheeks="blush")
        m "Yes... \"the hair thing\"..."
        call her_main("Well, what did you expect me to do, sir?", "crooked_smile", "happyCl", "worried", "mid",cheeks="blush")
        m "Literally anything..."
        g4 "... but {size=+7}THAT!{/size}"
        call her_main("But... I need to look my best for the coronation...", "open", "base", "base", "mid")
        m "And a hairdo full of cum is supposed to ensure that?"
        call her_main("Well... yes...", "soft", "narrow", "base", "R_soft",cheeks="blush")
        call her_main("You see, cum is a great hair fixative and--", "open", "base", "base", "mid")

        stop music fadeout 1.0
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        sna "{size=-4}Not that I care...{/size}"

        call her_main("The coronation! I must go now!", "open", "wide", "worried", "stare")
        call play_sound("running")
        pause 3

        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}WHAT THE HELL...?!!{/size}"
        call ctc

        call blkfade

    else:
        $ dynamic_cg("ball/bj", "background", "base3", "blush3")
        with hpunch
        her "{size=+5}*GOBBLE*!{/size}"
        g4 "{size=+5}Yeeeeeeeeeees!{/size}"

        sna "There! *Hmm*...?"
        sna "(Well of course... Why am I not surprised?)"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "eyes_stare3")
        sna "Miss Hermione Granger of the Gryffindor house..."
        ">Loud applause and cheering erupts from the crowd."
        $ dynamic_cg("ball/bj", "background", "base3", "blush3")
        sna "Miss Granger, if you would be so kind to grace us with your presence..."

        her "*gobble-gobble-gobble*!"
        m "Yes! That's a good slut!"
        her "{size=+5}*gobble-gobble-gobble*!!!{/size}"
        m "Yes. Now, move your tongue..."
        m "Lick my balls, girl. Come on!"
        $ dynamic_cg("ball/bj", "background", "base3", "eyes_closed3", "blush3")
        her "*gobble*! *Lick*! *Lick*! *gobble*!"
        m "Yes... Like that."
        m "What a good whore you are..."
        her "*Lick*! *Lick*! *gobble*! *Lick*!"
        m "Now look up at me whore."
        $ dynamic_cg("ball/bj", "background", "base3", "eyes_up3", "blush3")
        her "???................"

        call play_sound("spitting")
        show screen white
        pause.3
        hide screen white
        with vpunch
        $ dynamic_cg("ball/bj", "background", "base3", "eyes_stare3", "blush3", "spit_base3")
        call ctc

        her "*gobble*??!"
        m "No, don't you stop now!"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "brows_angry3", "spit_base3")
        her "*gobble-gobble-gobble*!"
        m "Yes, whore! Yes!"

        sna "Miss Granger?"
        sna "If you would, please..."
        sna "Miss Granger?"

        call play_sound("spitting")
        show screen white
        pause.3
        hide screen white
        with vpunch
        $ dynamic_cg("ball/bj", "background", "base3", "eyes_stare3", "blush3", "spit_base3", "spit_forehead3")
        call ctc

        her "!!!!!!!!!!!"
        her "......................................?"
        m "What's the matter, my little spit bucket?"
        m "Keep sucking my cock!"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3")
        her "*gobble-gobble-gobble*!"
        m "Yes. Good whore."
        her "*gobble-gobble-gobble*!"
        m "Keep deep throating me like that, yes!"
        her "*gobble*! *gobble*! *gobble*!"
        m "The balls, girl! Don't forget to work your tongue!"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "tears_base3", "spit_base3", "spit_forehead3")
        her "*gobble*! *Lick*! *Lick*!"
        m "Yes! Keep at it and we will be done here in no time!"
        m "Oh, I almost forgot..."
        call play_sound("spitting")
        pause.3
        with vpunch
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "eyes_stare3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3", "spit_nose3")
        call ctc

        her "..........................."
        her ".................."
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "eyes_happycl3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "*gobble*! *gobble*! *Lick*... *gobble*!"
        m "you just look so pretty with your face all covered in my spit!"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "*gobble*! *gobble*! *Lick*... *gobble*!"
        m "*Hmm*..."
        her "*gobble*! *gobble*! *Lick*... *gobble*!"
        m "Maybe we should show your pretty face to everyone?"
        m "Should I call some of your classmates over?"
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "eyes_stare3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "!!!!!!!!!!!!!!!"
        m "Relax..."
        m "I want to get caught as much as you do."
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "tears_base3", "brows_angry3", "spit_base3", "spit_forehead3", "spit_nose3")

        sna "Miss Granger?"
        sna "{size=-4}Where is that girl?{/size}"
        ">A murmur starts running through the crowd of students."

        m "Alright, listen up, whore."
        $ dynamic_cg("ball/bj", "background", "base3", "blush3", "eyes_squintup3", "tears_base3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "*gobble*?"
        m "I need you to stay still now."
        her "???"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_up3", "tears_base3", "spit_base3", "spit_forehead3", "spit_nose3")
        m "Yes, just like that."
        her "................"

        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_dead3", "tears_base3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "....................................."
        m "I plan to choke you a little bit with my cock..."
        m "It'll be fun... just relax..."
        her "......................................"
        m "Your throat is the best, girl."
        her "..........."
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_squintdead3", "tears_base3", "spit_base3", "spit_forehead3", "spit_nose3")
        m "So warm and tight..."
        her "............................................."
        her "...................."
        her "......."
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_up3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3")
        with hpunch
        her "!!!"
        m "I know, I know, you can't really breathe..."
        g9 "But that's what makes this so much fun!"

        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Stop struggling, slut. You are not going anywhere!"
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"

        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"

        g9 "Heh..."
        g9 "Your queen is right here..."
        g4 "Choking on my engorged cock!"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_happycl3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Oh. You are turning blue, love."
        m "Will you be alright?"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        m "Look up whore!"
        her "{size=+3}........................{/size}"
        g4 "I said, look at me!"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_up3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3")
        her "{size=+9}??!.....................{/size}"

        call play_sound("spitting")
        pause.5

        with vpunch
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_up3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_on_eye3")
        her "{size=+9}!!!!!!!!!!!!!!!!!!{/size}"

        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_closed3", "tears_base3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3")
        her "...................................................................................."
        g4 "There you go! You wear it well!"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_closed3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3")
        her "...........................................................*SOB!*"
        with hpunch
        g4 "*Gght*!"
        g4 "Here it comes!"
        g4 "I know you are fighting for air down there..."
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_dead3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3")
        g4 "But all you will get from me is a load of hot cum!"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "cheeks3", "blush3", "eyes_stare3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3")
        with hpunch
        her "{size=+9}*GHT*!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        g4 "{size=+9}*ARGH*!{/size}"
        with hpunch
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "eyes_dead3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3", "sperm3")
        her "{size=+9}*GULP-GULP-GULP-GULP-GULP*!!!{/size}"
        g4 "{size=+5}Yes, whore! Drink my cum!{/size}"
        her "*GULP-GULP-GULP-GULP*......"
        with hpunch
        g4 "Not done yet!{w=0.3} Not... done... *Argh!*"
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3", "sperm3")
        her "{size=-4}*Gulp*! *Gulp*! *Gulp...*{/size}"
        m "Oh, yes..."
        $ dynamic_cg("ball/bj", "background", "base3_alt", "blush3", "mascara3", "tears_crying3", "brows3", "spit_base3", "spit_forehead3", "spit_nose3", "spit_eye3")
        her "...................................................."
        m "Well, I think that was the last of it--"
        with hpunch
        g4 "{size=+5}*huh*?!{/size}"
        call blkfade

        stop music fadeout 1.0
        g4 "Hey, what are you--"
        ">Hermione gets up abruptly and runs off without saying a word..."
        call play_sound("running")
        pause 3
        m "*Hmm*...?"
        m "Oh, that's right... The coronation thing..."
        m "............."

    pause 1.5

    if public_whore_ending:
        # Public whore ending
        call sna_main("Miss Granger...?","snape_03", xpos="base", ypos="head")
        call sna_main("So you decided to show up after all","snape_04")
        call sna_main("What an unpleasant surprise...","snape_03")

        call her_main("Professor...", "upset", "base", "base", "mid", xpos="base", ypos="head")
        call sna_main("Well, go ahead then...","snape_10")
        call sna_main("Here is the tiara...")

        call her_main("Professor...", "upset", "base", "base", "mid", xpos="base", ypos="head")

        call sna_main("And the stage is yours...")
        call her_main("Thank you, professor.", "base", "closed", "base", "mid")
        pause.7

        hide screen blkfade
        $ dynamic_cg("ball/speech", "background", "base", "overlay")

        call play_sound("applause")
        call ctc

        her "..............."
        her ".................................."
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_closed", "overlay")

        play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
        her "Hello, everyone!"
        her "Thank you for making me your ball queen for two years in a row!"

        show screen blktone
        m "!!!"
        m "Her hairdo looks perfect!"
        m "I suppose I was wrong and--"
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_closed", "cum0", "overlay")
        g4 "Nope, there it is!"
        g4 "Dripping down behind her ear!"
        hide screen blktone

        her "I would like to dedicate my speech to every girl in this room..."

        show screen blktone
        g4 "What was she thinking pulling a stunt like that?"
        hide screen blktone

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_squint", "cum1", "overlay")
        her "I shall not go as far as to say that I do not deserve this honour..."
        her "Because I think I do..."
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "cum2", "overlay")
        her "But I am still very grateful to stand here before all of you tonight..."

        show screen blktone
        mal "{size=-4}*huh*?{/size}"
        mal "{size=-4}What's that stuff on her forehead you wager?{/size}"
        mal2 "{size=-4}Sweat...?{/size}"
        mal "{size=-4}*Hmm*... Probably...{/size}"
        hide screen blktone

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_squint", "cum3", "overlay")
        her "I would especially like to thank our esteemed teachers for their hard work."

        show screen blktone
        g4 "Doesn't she feel it by now?!"
        g4 "She'd better cut her speech short!"
        hide screen blktone

        her "Hogwarts truly did become a second home for all of us..."
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_squint", "cum4", "overlay")
        her "I know that I speak for every student in this building when I say this."
        show screen blktone

        mal "{size=-4}That doesn't look like sweat though...{/size}"
        mal2 "{size=-4}Yeah...{/size}"
        mal2 "{size=-4}Some weird goo seeping out of her hair...{/size}"
        fem "{size=-4}Are you guys really {i}that{/i} dim?{/size}"
        mal "{size=-4}What?{/size}"
        fem "{size=-4}That's cum... obviously.{/size}"
        mal2 "{size=-4}What? Bullshit, girl!{/size}"
        fem "{size=-4}I think I know cum when I see it.{/size}"
        mal "{size=-4}I bet you do. *Chuckle*{/size}"
        fem "{size=-4}Whatever. Just take a better look...{/size}"
        fem "{size=-4}She must've let some guy bury his cock in her hair and pump it full of semen.{/size}"
        mal "{size=-4}*Hmm*... Hair fucking then? Is that a thing now?{/size}"
        mal2 "{size=-4}You girls do the craziest things.{/size}"
        fem "{size=-4}*Humph*! Not all of us are sluts, you know.{/size}"
        mal "{size=-4}Unfortunately not...{/size}"
        fem "{size=-4}\"Unfortunately\"?!{/size}"
        fem "{size=-4}*Tsk*! You, men are so clueless about everything!{/size}"
        fem "{size=-4}You could never build a meaningful relationship with a slut!{/size}"
        mal "{size=-4}What's a \"meaningful relationship\"?{/size}"
        fem "{size=-4}It's when your girl is also your best friend.{/size}"
        mal "{size=-4}Oh, I don't need {i}that{/i}!{/size}"
        mal "{size=-4}I already have a best friend, this ugly bugger right here.{/size}"
        mal2 "{size=-4}Right back at you, mate!{/size}"
        mal "{size=-4}But I sure could use a slut in my life!{/size}"
        mal2 "{size=-4}What he said!{/size}"
        fem "{size=-4}you guys are...{/size}"
        fem "Such Idiots!!!"
        hide screen blktone

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_closed", "cum4", "overlay")
        her "I remember when I was just a little girl..."

        show screen blktone
        m "*Huh*?"
        hide screen blktone

        her "Frightened of my power... confused..."

        show screen blktone
        m "*Hmm*..."
        m "There... She did it again..."
        hide screen blktone

        her "Who knows what would have become of me if not for Hogwarts!"

        show screen blktone
        m "And again..."
        m "Why does she keep on jerking her shoulder in that awkward manner...?"
        hide screen blktone

        her "I am so lucky to be a student here..."
        call ctc

        # Reveal titty
        stop music
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_closed", "cum4", "overlay")
        $ renpy.sound.play("sounds/boing02.mp3")
        call ctc

        show screen blktone
        with hpunch
        g4 "!!!"
        call sna_main("!!!","snape_11")
        hide screen blktone

        play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
        her "Thank you, everyone..."
        her "Let me say this again..."
        her "Thank you for making me your ball queen this year..."
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_closed", "cum5", "overlay")
        call ctc

        call blktone_top
        mal "{size=-4}Am I hallucinating?{/size}"
        mal2 "{size=-4}No, it's really happening... I see it too...{/size}"
        mal "{size=-4}Hermione... Granger's... tit...{/size}"
        mal "{size=-4}Major wardrobe malfunction, mate!{/size}"
        fem "{size=-4}Oh no! Poor thing! We must let her know!{/size}"
        mal "{size=-4}Don't you dare to take this away from us, girl!{/size}"
        fem "{size=-4}But...!!{/size}"
        call hide_blktone_top
        call ctc

        her "And most of all I am thankful to my parents..."
        her "The people who raised me..."
        her "Mommy... Daddy..."
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_squint", "brows", "cum6", "overlay")
        her "I wish you could see how much Hogwarts changed me..."
        her "I wish you could see what has happened to that little girl you raised..."
        her "{size=-5}*Ah*...{/size}{heart}"
        call ctc

        call blktone_top
        g4 "The whore is blushing! She is well aware of what's going on!"
        g4 "Nasty slut!"
        g4 "(She planned the whole thing??!)"
        m "(By the great desert sands... What have I unleashed!?)"
        call hide_blktone_top

        $ dynamic_cg("ball/speech", "background", "base2", "eyes_squint", "brows", "cum6", "overlay")
        her "..............................."
        her ".................."
        call ctc

        call blktone_top
        mal "{size=-4}Now she just sort of stands there...{/size}"
        mal2 "{size=-4}Giving us a better look...?{/size}"
        mal "{size=-4}Do You think she is aware of her tit being visible at all?{/size}"
        fem "{size=-4}What a shameless display...{/size}"
        fem "{size=-4}And to think that I almost felt sorry for that slut...{/size}"
        fem "........................"
        with hpunch
        fem "{size=+5}Cover up, you shameless slut!!!{/size}"
        mal "{size=-4}!!!{/size}"
        mal2 "{size=-4}Have you lost your mind, yelling like that?!{/size}"
        with hpunch
        fem "{size=+5}Gryffindor whore!!!{/size}"
        call hide_blktone_top

        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_closed", "brows", "cum6", "overlay")
        her "{size=-3}*Ah*...{/size}{heart}"
        her "...............................*a-ha*...{heart}{heart}{heart}"
        call ctc

        "Somebody from the crowd" "Show us both of them, Hermione!"
        "Another voice from the crowd" "Look! Her face is all covered in cum!"
        "Somebody from the crowd" "Have you no shame anymore, Hermione?!"
        "Another voice from the crowd" "Cover up, you slut!"

        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "cum6", "overlay")
        her "Oh... That's right..."
        her "I almost forgot..."
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_closed", "cum6", "overlay")
        her "{size=+5}Go Gryffindor!{/size}"
        call play_sound("applause")
        ">The crowd starts whistling and cheering wildly."
        $ dynamic_cg("ball/speech", "background", "base2", "eyes_squint", "brows", "cum6", "overlay")
        her "......................................"
        her ".........................................................."
        call ctc

        call sna_main("Quiet down everyone!","snape_12", ypos="head")
        call sna_main("As for you, miss Granger...","snape_12")
        call sna_main("I think that's enough.","snape_12")
        call sna_main("Cover up and get off the stage... Go...","snape_12")
        pause.1

        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "cum6", "overlay")
        her "\"Cover up\", sir?"
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_squint", "brows", "cum6", "overlay")
        her "Oh? What is this? One of my breasts is completely exposed..."
        $ dynamic_cg("ball/speech", "background", "base2", "eyes_squint", "brows", "cum6", "overlay")
        her "How embarrassing..."
        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "eyes_closed", "brows", "cum6", "overlay")
        her "*Ah*...{heart}{heart}{heart}"
        call ctc

        "Somebody from the crowd" "Whore!"
        "Another voice from the crowd" "Gryffindor slut!"
        "Somebody from the crowd" "I love you, Hermione!"
        "Another voice from the crowd" "Gryffindor rules!!!"

        call sna_main("Miss Granger, I said that's enough!","snape_18", ypos="head")
        pause.1

        her "As you say, professor..."
        call sna_main("And wipe your face, girl. You look repulsive.","snape_12", ypos="head")
        pause.1

        $ dynamic_cg("ball/speech", "background", "base2", "mouth_open", "cum6", "overlay")
        her "Oh, this? This is just my--"
        call sna_main("Don't care! Get off the stage already!","snape_18", ypos="head")
        call sna_main("Now!","snape_18")
        pause.1

        $ dynamic_cg("ball/speech", "background", "base2", "eyes_squint", "brows", "cum6", "overlay")
        call ctc

        call blkfade
        call play_sound("applause")
        ">Wild whistling and cheering continues as Hermione descends from the stage."
        pause 1
        stop music fadeout 3.0

        # Back in the alcove
        $ dynamic_cg("ball", "background")
        call hide_blkfade
        call ctc

        call her_main("[genie_name]...", "soft", "narrow", "base", "R_soft",cheeks="blush",ypos="head")
        call her_main("There was something you wanted to discuss with me?")
        g4 "Not right now, whore!"
        call blkfade

        call her_main("Sir?!", "base", "narrow", "base", "mid_soft",cheeks="blush")
        g4 "I want to fuck you so badly! Come over here!"
        call play_music("playful_tension")
        call her_main("Of course, sir...", "silly", "squint", "worried", "up",cheeks="blush")

        # Insertion
        call play_sound("insert")
        with hpunch
        with kissiris
        pause.5
        g4 "{size=+7}OH YEEEES!{/size}"

        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush")
        show screen bld1
        call hide_blkfade
        call ctc

        her "*Aaah*!!!"
        g4 "Your acceptance speech was a disgrace, girl!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_smile", "eyes_closed", "brows", "blush")
        her "I thought it went rather well..."
        g4 "Showing off your tits like that?!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_smile", "eyes_closed", "blush")
        her "Only one... *ah*..."
        g4 "What?"
        her "Only one tit, sir..."
        g4 "Whatever happened to that idealistic and self-righteous girl you once were?!"
        $ dynamic_cg("ball/sex", "background", "base", "lashes", "blush")
        her "You fucked her out of me, sir!"
        g4 "You're damn right I did!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "brows", "blush")
        her "You fucked her out of me with your enormous cock, sir!"
        g4 "Argh! You whore!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        $ dynamic_cg("ball/sex", "background", "base", "eyes_wide", "blush")
        her "Ah!!!"
        g4 "Quiet, whore! Someone will hear you!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        her "Ah! [genie_name]!"
        g4 "I said be quiet!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush")
        her "Ah! [genie_name]!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "brows", "blush")
        her "Yes! Fuck me harder!"
        m "Are you raising your voice on purpose, whore?"
        g4 "Do you want to get caught like this?"
        g4 "On your professor's cock?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_r", "mouth_open_tongue", "blush")
        her "Ah! Maybe..."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "brows", "blush")

        her "Call me a mudblood, sir!"
        m "What?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush")
        her "Call me a mudblood, please!"
        m "A \"mudblood\"?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_wide", "blush")
        her "Ah! Yes! Yes! I am a mudblood whore!"
        g4 "Whatever!"

        call play_sound("slap")
        show screen white
        pause.5
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.4
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        $ dynamic_cg("ball/sex", "background", "base", "spank", "eyes_stare", "tears", "blush")

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.2
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "tears2", "blush")
        her "*AAAAAAAhH*!"
        her "Yes!!! Yeeees! Ah!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open_tongue", "eyes_stare", "tears2", "brows", "blush")
        her "Fuck me [genie_name]! Fuck me harder!!!"
        g4 "*Grh*! Harder than this, whore?!"
        g4 "!!!"
        g4 "Crap!  Someone's coming!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "tears2", "blush")
        her "No, sir, not yet. But if you keep spanking me--"
        g4 "No, whore! I mean a bunch of students are coming this way!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_smile", "tears2", "blush")
        her "What?!"

        # Students join
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "mouth_open", "tears", "blush", "dudes")
        sly1 "Well, well, well... What do we have here?"
        her "!!!"
        sly1 "I thought it could be you, Gryffindor filth..."
        sly1 "Moaning like a whore..."
        sly1 "Getting fucked by... Oh..."
        with hpunch
        sly1 "Professor Dumbledore!?"
        m "Hello, boys..."
        her ".........................."
        sly1 "Oh... *Ehm*... We didn't know..."
        sly1 "We'll be leaving now..."
        m "What? Don't be silly, boys."
        m "You are more than welcome to stay."
        sly1 "We are?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_wide", "mouth_open", "blush", "dudes")
        her "What?!"
        m "Of course."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "dudes")

        her "Professor!!!?"
        m "The girl's front side is completely at your disposal."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "brows", "dudes")
        her "Professor! No!"
        m "What's wrong, slut?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "dudes")
        her "Sir, don't call me that in front of them, please..."
        m "What's the matter? Why are you Acting shy all of a sudden?"
        her "Can't you see that they are from Slytherin?!"
        m "So what?"
        her "Our two houses... we have a history."
        m "Oh..."
        m "Well, then you shall become the bridge between Slytherin and Gryffindor."
        m "Hermione Granger, the ambassador of peace!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "mouth_open", "blush", "brows", "dudes")
        her "No, sir! I refuse!"
        her "And stop moving your hips while we're talking, sir!"
        m "Boys, what is taking you so long?"
        m "I said, the whore is yours!"
        her "Professor Dumbled--"
        sly1 "Shut up, filth!"

        # Spit on face
        call play_sound("spit")
        show screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open", "blush", "dudes", "dudes_spit")
        pause.2
        hide screen white
        with hpunch
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open", "blush", "spit_on_face", "dudes")
        her "!!!"
        m "There you go!"
        sly2 "*Ha-ha-ha*! Nice one! Look at her stupid face!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "mouth_open", "blush", "spit_on_face", "brows", "dudes")
        her "You... You...!"
        sly1 "We really enjoyed your speech, Gryffindor slut."
        sly2 "Yeah... Sure did..."
        her "That wasn't meant for you, you Slytherin scum!"
        sly1 "Wasn't meant for us? What are you, stupid?"
        sly1 "You bared your filthy, muggle-born flesh on stage! In front of the entire school!"
        sly1 "{size=+7}Of course it was for everyone, you dumb cunt!{/size}"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_down", "mouth_open", "blush", "spit_on_face", "brows", "dudes")
        her "Sir! Stop fucking me!"
        m "*huh*? You mean, like this?"
        with hpunch
        pause.3

        her "*Ah-aha*! No, professor, stop it!"
        m "Stop? I think I will fuck you harder instead!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open", "blush", "spit_on_face", "dudes")
        her "*Ah-ah*!!!"
        sly1 "Yes... You are ours now, slut!"
        call ctc

        # Dicks out
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush", "spit_on_face", "dudes2")
        her "What?! What are you doing?!"
        her "Put your filthy dicks away immediately!"
        with hpunch
        pause.3
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "spit_on_face", "dudes2")
        her "*Ah*... *Ah-a*..."
        sly1 "Yes... I wanted to do this for quite some time now..."
        her "Professor!"
        m "*huh*? Oh, don't you mind me girl."
        m "Imagine that I'm not even here..."

        call play_sound("spit")
        show screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open", "blush", "spit_on_face", "dudes2", "dudes_spit")
        pause.2
        hide screen white
        with hpunch
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "mouth_open", "blush", "brows", "spit_on_face", "dudes2")
        her "Stop it! Stop spitting in my face, you bastards!"
        sly1 "Make us, whore!"
        her "I am warning--"

        call play_sound("spit")
        show screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open_tongue", "blush", "brows", "spit_on_face", "dudes2", "dudes_spit_mouth")
        pause.2
        hide screen white
        with hpunch
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_smile", "blush", "brows", "spit_on_face", "dudes2")
        call play_sound("gulp")
        her "{size=+5}*Gulp*!{/size}"
        sly2 "*Ha-ha-ha*! Right in the mouth! Good one, mate!"
        sly1 "And she swallowed it too!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "mouth_open", "blush", "brows", "spit_on_face", "dudes2")
        her "That's was an accident!"
        sly1 "Was it? Let's see."
        her "*huh*?"

        call play_sound("spit")
        show screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open_tongue", "blush", "brows", "spit_on_face", "dudes2", "dudes_spit_mouth")
        pause.2
        hide screen white
        with hpunch
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_smile", "blush", "brows", "spit_on_face", "dudes2")
        call play_sound("gulp")
        her "{size=+5}*Gulp*!{/size}"

        sly2 "She did it again!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "mouth_open", "blush", "brows", "spit_on_face", "dudes2")
        her "That's because I didn't expect it... It's just a reflex!"
        sly1 "That's one hot reflex!"
        g4 "Oh... yes..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Ah*... *Ah-aha*..."
        her "You will pay for this, you spineless slytheri--"
        sly1 "Shut it, mudblood!"
        with vpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "spit_on_face", "dudes2", "dude_bj")
        call ctc

        # Dick in mouth
        her "!!!........................................................."
        sly2 "Cool! I'm next!"
        her "*Gulp*!"
        sly1 "Suck my cock, bitch! Suck it!"
        m "Do what the boy tells you, girl."
        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        m "Come on!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "blush", "spit_on_face", "dudes2", "dude_bj")
        her "*Slurp*..."
        sly1 "She's doing it! Hermione Granger sucking me off, lads!"
        sly2 "Awesome! Can't wait to give it a go myself!"
        sly1 "Oh... wow... she's good..."
        her "*Slurp*! *Slurp*! *Gulp*!"
        sly1 "Oh yes... Yes..."
        sly1 "Oh... You are so good at this, whore!"
        sly1 "It's... I..."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "spit_on_face", "dudes2", "dude_bj", "cheeks")
        her "{size=+7}*gobble*?!?{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"

        # Swallowing cum
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "blush", "brows", "spit_on_face", "dudes2", "dude_bj")
        call play_sound("gulp")
        her "{size=+5}*Gulp-gulp-gulp-gulp*!{/size}"
        call play_sound("gulp")
        her "*{size=+3}Gulp-gulp-gulp*...{/size}"
        call play_sound("gulp")
        her "*Gulp-gulp-gulp*..."
        call play_sound("gulp")
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "blush", "brows", "spit_on_face", "dudes2")
        her "*Gu-aha*..."
        her "Is this all you got? Pathetic!"
        sly2 "Oh... Shut up whore... You sucked me dry..."
        $ dynamic_cg("ball/sex", "background", "base", "blush", "brows", "spit_on_face", "dudes2")
        her "Come on! Who's next?!"
        sly2 "Me! I'm next!"
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "blush", "brows", "spit_on_face", "dudes2", "dude_bj")
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "blush", "brows", "spit_on_face", "dudes2", "dude_bj")
        her "*Slurp*! *Slurp*! *Slurp*!"
        g4 "Oh... Yes... Yes!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly2 "Oh! Her mouth is so slippery and warm!"
        her "*Slurp*! *Slurp*! *Slurp*!"
        g4 "Yes! Suck that cock, you whore!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Gulp*! Gulp!* *Slurp*!"
        sly2 "I don't know... *gh*... How much longer..."
        sly2 "... I could keep up like that."
        her "*Slurp-Slurp-Slurp-slurp*!"
        her "*Slurp-Gulp-Slurp-Slurp-gulp*!!!"
        sly2 "Oh, man... Oh man..."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp*!!"
        sly2 "I... I..."
        sly2 "..................."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp*!!"
        with hpunch
        sly2 "{size=+7}I'm cummiiiiiiiiing!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "brows", "spit_on_face", "dudes2", "dude_bj")
        her "{size=+7}*gobble*?!?{/size}"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "blush", "brows", "spit_on_face", "dudes2", "dude_bj")
        call play_sound("gulp")
        her "{size=+5}*Gulp-gulp-gulp-gulp*!{/size}"
        call play_sound("gulp")
        her "{size=+3}*Gulp-gulp*...{/size}"
        call play_sound("gulp")
        her "*Gulp..."
        sly2 "*Argh*... my cock..."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "blush", "brows", "spit", "spit_on_face", "dudes2")
        her "*Gu-aha*..."
        $ dynamic_cg("ball/sex", "background", "base", "blush", "brows", "spit", "spit_on_face", "dudes2")
        her "Next! Come on! Is this all you got?"
        sly1 "I'm next, mudblood!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush", "lashes", "brows", "spit", "spit_on_face", "dudes2")
        her "{size=-5}*Ah*... Don't call me that, you bastard...{/size}{heart}"
        sly1 "Gonna fuck your face real good, whore!"
        sly1 "And after I fill your mouth with my cum, you're gonna thank me!"
        sly1 "Aren't you, mudblood whore?"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush", "brows", "spit", "spit_on_face", "dudes2")
        her "Fuck you!"

        call play_sound("spit")
        show screen white
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open_tongue", "blush", "brows", "spit_on_face", "dudes2", "dudes_spit_mouth")
        pause.2
        hide screen white
        with hpunch
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_smile", "blush", "brows", "spit_on_face", "dudes2")
        call play_sound("gulp")
        her "{size=+5}*Gulp*!{/size}"

        sly1 "That's what I thought!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush", "lashes", "brows", "spit", "spit_on_face", "dudes2")
        her "You worthless... slythe--"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_down", "blush", "lashes", "brows", "spit_on_face", "dudes2", "dude_bj3")
        her "!!?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "blush", "lashes", "brows", "spit_on_face", "dudes2", "dude_bj3")
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly1 "Yes! Yes, you mudblood filth! Suck my cock! Suck it!"
        m "This is quite extraordinary..."
        sly1 "Sir?"
        m "It's just..."
        m "Her pussy..."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_down", "blush", "lashes", "brows", "spit_on_face", "dudes2", "dude_bj3")
        her "*Slurp*?"
        m "It tightens every time you call the girl a \"mudblood\"..."
        m "Try calling her that again, boy."
        sly1 "Gladly, sir."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "blush", "lashes", "brows", "spit_on_face", "dudes2", "dude_bj3")
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly1 "Yes, whore! I love fucking your {i}mudblood{/i} face!"
        sly1 "And you're loving every moment of this, aren't you?"
        sly1 "Aren't you, {i}mudblood{/i}?"
        her "*Slurp*! *Slurp*! *Gulp*!"
        m "Yup... Every time you say that..."
        m "*huh*?"
        m "What is this? Her legs are shaking!"
        m "Are you cumming, girl?"
        $ dynamic_cg("ball/sex", "background", "base", "lashes", "blush", "lashes", "spit_on_face", "dudes2", "dude_bj3")
        her "..............................................."
        m "I think you are!"
        m "Come on, boy, let's speed this thing up a little!"
        m "Let's fuck her from both ends while she is cumming like a dirty slut!"
        sly1 "Of course, sir."

        sly1 "Take this, you mudblood whore!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3

        g4 "And this!!!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        her "{size=+7}!!!!!!!!{/size}"
        g4 "Yes! Her pussy is flooded with juice!"
        sly1 "*Agh*! Her mouth as well, sir."
        sly1 "I don't know how much longer I... oh..."
        sly1 "*Argh*!"
        sly1 "{size=+3}Take this, whore!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause.1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "lashes", "dudes2", "dude_bj3", "cum_nose")
        her "{size=+7}*gobble*?!?{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"

        # Swallowing cum
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "lashes", "tears", "blush", "lashes", "dudes2", "dude_bj3", "dude_bj_cum", "spit_on_face")
        call play_sound("gulp")
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        call play_sound("gulp")
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        call play_sound("gulp")
        her "*Gulp-gulp-gulp*..."
        call play_sound("gulp")
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        her "....................."
        $ dynamic_cg("ball/sex", "background", "base", "mouth_open", "blush", "lashes", "brows", "spit", "spit_on_face", "dudes2")
        her "*Gu-aha*..."
        sly2 "You drained my balls, bitch..."
        m "Alright, boys! Let's bring this little party to a worthy conclusion."
        her "{size=+7}I'm cumming!{/size}"
        m "Yeah, whatever, whore."
        m "So, rest of you boys, you can just jerk off on her face now, alright?"
        sly1 "Of course, sir."
        sly2 "Yes, sir!"
        m "Yes, just plaster her face with cum. She loves that shit!"
        $ dynamic_cg("ball/sex", "background", "base", "mouth_smile", "eyes_dead", "tears2", "blush", "lashes", "spit", "spit_on_face", "dudes2")
        her "{size=+3}No! I am already cumming... Stop!{/size}"
        sly1 "Heh... Hermione Granger... What a whore!"
        sly2 "Yeah! Nothing but a mudblood cunt!"
        her "{size=+9}AAAAAH!!!!!{/size}"
        her "{size=+3}Yes! I'm a whore! I'm a whore!{/size}"
        sly1 "She even admits it!"
        sly2 "I don't think I can last much longer!"
        sly1 "Me neither!"
        sly2 "ARGH!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum")
        call ctc

        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        her "{size=+3}My face!!{/size}"
        sly1 "Take this, whore!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum2")
        call ctc

        her "{size=+5}*AAAAAAAAAAAAH*!{/size}"
        sly2 "*Argh*! Here! Me too!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum3")
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum3", "bukkake")
        call ctc

        her "{size=+4}I'm cumming!{/size}"
        m "Well, don't mind if I do!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum3", "bukkake")
        her "{size=+3}No professor, I............!{/size}"
        g4 "*Argh*!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "dudes_cum3", "bukkake", "cum_anal", "cum_pussy")
        call ctc

        her "{size=+8}*AAAAAAAAAAAAH*!{/size}"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "cum_after", "bukkake", "cum_anal", "cum_pussy")
        her "{size=+5}No! My face! My pussy! Ah! I can't stop cumming!!!{/size}"
        sly1 "What a slut!"
        sly2 "Whore!"
        sly1 "Mudblood!"
        her "{size=+8}*AAAAAAAAAAAAH*!{/size}"

        call play_sound("spit")
        show screen white
        pause.3
        hide screen white
        with vpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "cum_after", "bukkake", "cum_anal", "cum_pussy", "dudes_spit_mouth")
        call ctc

        $ dynamic_cg("ball/sex", "background", "base", "mouth_smile", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "cum_after", "bukkake", "cum_anal", "cum_pussy", )
        call play_sound("gulp")
        her "{size=+8}*Gulp*!{/size}"

        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "tears2", "blush", "spit", "spit_on_face", "dudes2", "cum_after", "bukkake", "cum_anal", "cum_pussy")
        her "{size=+8}I'll go insane!{/size}"
        call ctc

        show screen white
        with d9
        pause 1
        hide screen white
        show screen blkfade
        with d9

        call ctc

        m "Well, thank you for your cooperation, boys."
        sly1 "Of course, professor Dumbledore."
        sly2 "Glad to be of help, sir."
        sly1 "Thank you, professor."
        sly2 "Alright, let's go back to the ball."
        sly1 "Yeah, let's go!"
        sly2 "Bye, mudblood whore!"
        sly1 "Yeah, thank you for being such a slut!"
        call her_main("..........................", "soft", "narrow", "annoyed", "up", cheeks="blush", tears="mascara_soft", ypos="head")

        call play_sound("footsteps")
        $ dynamic_cg("ball/sex", "background")
        pause 2

        hide screen blkfade
        with d9

        sly1 "{size=-4}Man, professor Dumbledore sure is one cool dude.{/size}"
        sly2 "{size=-4}Yeah... Who would have thought...{/size}"
        sly1 "{size=-4}True. I can't help but respect the man...{/size}"
        m "(*Aww*... Such nice boys...)"
        sly2 "{size=-4}Yeah... I hope I will be as agile as he is when I am that ancient.{/size}"
        g4 "(I'm not ancient, you punks!)"
        m "(Although I suppose in some way I am...)"

        #TODO Cum layer on Hermione doll (and ball ending CG?)

        call her_main("..........................", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Whore! Why are you so quiet?"
        call her_main("I...", "silly", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        call her_main("I am... not sure...",cheeks="blush",tears="mascara_soft")
        call her_main("What...? What is...", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Come on, girl. Pull yourself together!"
        call her_main("I... I... What?", "open", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara_soft")
        call her_main("I don't understand... I...",cheeks="blush",tears="mascara_soft")
        m "*Hmm*..."
        m "I will be leaving now."
        call her_main("Leaving...?", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Yes. Maybe you should too..."
        m "Go clean yourself up and rest or something."
        call her_main("But I can't leave... No... I must...", "open", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara_soft")
        call her_main("The formal dance... I must...",cheeks="blush",tears="mascara_soft")
        m "A dance? You can't dance in this condition."
        call her_main("No! I am the ball queen! I must...", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Well, suit yourself."
        m "I'm leaving..."
        call her_main("Goodbye... sir...", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "............."
        m "Farewell, girl."
        call ctc

        call blkfade
        $ dynamic_cg("ball/intro", "background", "bloom", "hermione2", "foreground", "overlay")
        pause.5
        call hide_blkfade

        play music "music/Brandenburg No4-1 BWV1049 Kevin-McKleod.mp3" fadein 1 fadeout 1
        call ctc

        m "*Hmm*..."
        m "Maybe I should stay and watch Hermione's post-multiple-orgasm dancing?"
        m "No... This ball is almost over. This is my only chance to sneak out unnoticed."
        call ctc

        call blkfade
        pause.5

    else:
        # Personal whore ending
        call sna_main("Miss Granger...?","snape_03", ypos="head")
        call sna_main("You decided to show up after all? What an unpleasant surprise...","snape_04")
        call her_main("...............................", "full", "narrow", "annoyed", "up",cheeks="blush",tears="mascara", ypos="head")
        call sna_main("What happened to your face, girl?","snape_13")
        call her_main(".......................................", "full", "narrow", "worried", "down",cheeks="blush",tears="mascara")
        call sna_main("*Hmm*... Well, go ahead then...","snape_13")
        call sna_main("Here is the tiara...","snape_13")
        call her_main(".......................................", "full", "narrow", "worried", "down",cheeks="blush",tears="mascara")

        call sna_main("And the stage is yours...","snape_13")
        pause.7

        $ dynamic_cg("ball/speech", "background", "base", "cheeks", "blush", "cum_nose", "brows", "mascara", "sweat", "overlay")
        hide screen bld1
        call hide_blkfade

        call play_sound("applause")
        call ctc

        her "..............."
        her ".................................."
        her ".........................................................................."

        play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_mouth", "eyes_squint", "brows", "mascara", "sweat", "overlay")
        her "Ah-a........."

        m "Is that...?"
        m "are Leftovers of my cum still in her mouth?"
        g4 "What the hell is she doing?"

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_mouth", "eyes_closed", "brows", "mascara", "sweat", "overlay")
        her "...................................."
        her "*{i}Helwo eweruone{/i}*..." #Misspelled on purpose.

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_mouth", "eyes_closed", "brows", "mascara", "sweat", "overlay")
        her "{i}Fenk you for being heah today{/i}..." #Misspelled on purpose.
        m "I can barely understand a word she is saying..."
        her "{i}Fifst of all I would like foo fenk Profeffor Dumblefore...{/i}" #Misspelled on purpose.
        m "Me?"
        her "................"

        $ dynamic_cg("ball/speech", "background", "base", "cheeks", "blush", "cum_nose", "brows", "mascara", "sweat", "overlay")
        stop music fadeout 1.0
        her ".................................................."
        call ctc

        $ dynamic_cg("ball/speech", "background", "base", "blush", "cum_nose2", "eyes_closed", "mascara", "sweat", "overlay")
        call play_sound("gulp")
        her "{size=+5}*GULP*!!!{/size}"
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_nose2", "eyes_squint", "mascara", "brows", "sweat", "overlay")
        her "*Gua-ha*..."
        her "Thank you, professor."
        with hpunch
        g4 "YOU WHORE!!!"
        g4 "When did you get this nasty!?"

        play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_nose2", "mascara", "brows", "sweat", "overlay")
        her "I would also like to thank my parents..."
        her "And I would like to thank my fellow students!"

        call play_sound("applause")
        ">Loud cheering and whistling erupts from the crowd."

        her "As well as the teachers, of course..."
        $ dynamic_cg("ball/speech", "background", "base", "blush", "cum_nose2", "mascara", "brows", "sweat", "overlay")
        ">A few people can be heard clapping their hands."
        call ctc

        call blktone_top
        mal "{size=-4}So it's Hermione Granger again this year...{/size}"
        fem "{size=-4}*Tsk*... Why am I not surprised?{/size}"
        mal2 "{size=-4}Maybe because she deserves it?{/size}"
        mal "{size=-4}Yeah! Stop hating on Hermione!{/size}"
        fem "{size=-4}*Tch*... Whatever.{/size}"
        mal "{size=-4}By the way, when Hermione went on stage-{/size}"
        mal2 "{size=-4}Yeah, there was something in her mouth. I noticed it too.{/size}"
        fem "{size=-4}I bet it was someone's cum!{/size}"
        mal "{size=-4}WHAT?!!{/size}"
        mal2 "{size=-4}Get your head out of the gutter, girl!{/size}"
        fem "{size=-4}Why not?{/size}"
        fem "{size=-4}Everyone knows she is sleeping with Professor Dumbledore!{/size}"
        mal "{size=-4}No, not your gossips again.{/size}"
        mal2 "{size=-4}Wait, I want to hear this one. Tell us more.{/size}"
        fem "{size=-4}What is there to tell?{/size}"
        fem "{size=-4}Hermione Granger is a whore. She enjoys sucking cocks....{/size}"
        fem "{size=-4}Yes, she loves to suck cocks but she loves sperm even more!{/size}"
        mal "{size=-4}....{/size}"
        fem "{size=-4}She is a sperm addict! She must swallow half a cup of sperm every day...{/size}"
        fem "{size=-4}Because if she doesn't she goes into a sex-craze...{/size}"
        mal2 "{size=-4}.....{/size}"
        fem "{size=-4}And when that happens she cannot control herself and will gladly sleep with the first man she sees.{/size}"
        mal "{size=-4}.............{/size}"
        mal2 "{size=-4}.....................{/size}"
        fem "{size=-4}*Hmm*? Why are you staring at me like that?{/size}"
        mal "{size=-4}What? We're not staring.{/size}"
        mal2 "{size=-4}Yes, keep talking. You are good at this!{/size}"
        fem "{size=-4}Good at what?!{/size}"
        fem "{size=-4}Wait a second, are you guys getting off on this?{/size}"
        mal "{size=-4}Heh... Look at the crow calling the raven black!{/size}"
        fem "{size=-4}What do you mean?{/size}"
        mal2 "{size=-4}You are blushing like crazy, girl! And your eyes are all misty!{/size}"
        mal "{size=-4}Yeah! You enjoy this as much as we do!{/size}"
        fem "{size=-4}!!!?{/size}"
        fem "{size=-4}You guys are idiots!{/size}"

        call play_sound("running")
        pause 3
        mal "{size=-4}What? What did I say?{/size}"
        mal2 "{size=-4}Who knows, bro? Witches be crazy...{/size}"
        mal "{size=-4}They do be crazy...{/size}"
        call hide_blktone_top

        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_nose2", "mascara", "brows", "sweat", "overlay")
        her "Thank you, everyone, for being such a big help in organising tonight's event."
        her "And thank you for choosing me as your queen again this year..."
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "eyes_closed", "blush", "cum_nose2", "mascara", "brows", "sweat", "overlay")
        her "What a pleasant and completely unexpected surprise...!"
        her "And one more thing..."
        $ dynamic_cg("ball/speech", "background", "base", "mouth_open", "blush", "cum_nose2", "mascara", "brows", "sweat", "overlay")
        her "{size=+5}Go Gryffindor!{/size}"

        call play_sound("applause")
        ">The crowd explodes with loud cheers and whistles, interspersed by occasional booing..."

        call ctc

        call blkfade
        pause.7

        stop music fadeout 1.0
        m "Great speech..."
        m "Very arousing... *Ehm*... I mean inspiring."
        call her_main("Thank you, sir.", "soft", "narrow", "base", "R_soft",cheeks="blush",ypos="head")
        m "Swallowing my load in front of the entire school?"
        g9 "A very nice touch."
        call her_main("........................................................", "crooked_smile", "happyCl", "worried", "mid", cheeks="blush")

        call play_music("playful_tension") # SEX THEME.

        $ dynamic_cg("ball/sex", "background")
        show screen bld1
        call hide_blkfade

        m "Alright, girl. Let's have that talk now..."
        call her_main("....................", "upset", "base", "base", "mid")
        m "There is something I need to tell you..."
        m "Not sure where to start though..."
        m "........................................"
        m "Well, first of all I am--"
        call her_main("Sir, I think I know exactly what you are about to say.", "open", "base", "base", "mid")
        m "You do?"
        call her_main("Of course.", "open", "base", "base", "mid")
        call her_main("One hasty blowjob is not nearly enough to repay my debt to you, am I right?", "base", "narrow", "base", "mid_soft",cheeks="blush")
        m "What? No, that's not what I--"
        call her_main("It's fine, sir. Really.", "base", "narrow", "base", "mid_soft",cheeks="blush")
        call her_main("Let me just pull my panties down a little...", "soft", "narrow", "base", "R_soft",cheeks="blush")
        g4 "Damn you girl! Will you let me finish!?"
        call her_main("Of course sir...", "base", "narrow", "base", "mid_soft",cheeks="blush")
        m "*huh*?"
        call her_main("Just make sure you don't hit my dress, alright?", "open_tongue", "narrow", "worried", "mid_soft",cheeks="blush")
        g4 "*growl*!"
        g4 "Come here, whore!"
        g4 "Suppose I might as well fuck you one last time!"
        call her_main("(One last time?)", "upset", "base", "base", "mid")
        call ctc

        call blkfade
        call play_sound("insert")
        with hpunch
        with kissiris

        call her_main("{size=+5}Ahh!!!{/size}", "open", "wide", "worried", "stare",cheeks="blush",tears="soft")
        g4 "Oh, yes!"

        $ dynamic_cg("ball/sex", "background", "base", "blush")
        hide screen bld1
        call hide_blkfade
        call ctc

        her "*Ah-ah*..."
        m "*Hmm*? Your pussy..."
        m "It's dripping wet, girl."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_down", "mouth_smile", "blush")
        her "*Ah*...{heart} It is, sir?"
        her "That's probably from before..."
        m "From before?"
        m "You mean when you were choking on my cock?"
        her "*Ah*...{heart} Yes, sir..."
        m "Did it make you cum?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "mouth_open", "blush")
        her "A little..."
        m "Well, you're just precious then, aren't you?"
        her "*ah*......"
        m "Aren't you, whore?!"
        her "*Ah*... Whatever you say, sir."
        m "Yes, you are precious, you slut!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_closed", "mouth_smile", "blush")
        her "............."
        m "Squeezing my cock with your little pussy!"
        her "......................"
        m "*Hmm*...?"
        m "Why are you being so quiet?"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush")
        her "Oh... I'm just afraid that someone would--"
        m "I think that's because you want to get spanked!"
        her "What!?"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "mouth_open", "brows", "blush", "tears")

        her "*EEeeeeeeeegh*!"
        m "Quiet, whore! Someone could hear you!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "brows", "blush", "tears")
        her "Sir, I--"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "mouth_smile", "brows", "blush", "tears")

        her "{size=+7}*EEghh*!!!{/size}"
        m "Be quiet, I said!"
        m "Or do you want to get caught like this, on your headmaster's cock?"
        m "Do you, Miss queen of the autumn ball?"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears")

        her "*Ah*..."
        m "Yes, you're liking this aren't you?!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_happycl", "mouth_smile", "blush")
        her ".............."
        g4 "Answer me, slut!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears")

        her "Yes, sir! I love it!!!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "brows", "blush", "tears")
        her "Spank me harder, sir! I deserve it!"
        m "That's the spirit!"
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears", "spank")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "blush", "tears", "spank")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open_tongue2", "lashes", "blush", "tears", "spank")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background", "base", "eyes_dead", "mouth_open_tongue2", "lashes", "blush", "tears", "spank")
        call ctc

        her "{size=+7}*Aaaaaah*............................{/size}"

        call blktone_top
        sna "Attention, maggots!"
        sna "The formal dance of the Hogwarts Autumn Ball is about to begin..."
        call hide_blktone_top

        $ dynamic_cg("ball/sex", "background", "base", "eyes_wide", "mouth_open", "blush", "tears", "spank")
        her "!!!"
        her "The dance! I completely forgot!!!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "tears", "spank")
        her "Sir, excuse me, but you have to let me go..."
        g4 "*Ah*... Your pussy is something else!"
        her "Sir... *Ah*... I am serious."
        her "As the queen I am expected to lead the dance."
        g4 "Yes... Like that, just like that... *Oh*, yes."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "brows", "blush", "tears", "spank")
        her "Sir, are you even listening?"
        m "Oh, I hear you alright... But let me make you a counteroffer."
        $ dynamic_cg("ball/sex", "background", "base", "eyes_up", "mouth_open", "blush", "tears", "spank")
        her "Sir?"
        m "Instead of letting you go..."
        m "I will stick my cock up your ass."
        m "How about that?"
        her "What? B-but..."
        m "I think that is a great plan!"
        her "Sir, no! I--"
        m "One sec, one sec..."
        call blkfade

        m "Let me take my dick out of your pussy first..."

        call play_sound("boing")
        with hpunch
        pause.3

        # Insertion
        call her_main("*Ah*...", "open", "wide", "worried", "stare",cheeks="blush",tears="soft", ypos="head")
        call her_main("Sir, no. You must listen to me--", "open_tongue", "narrow", "worried", "mid_soft",cheeks="blush")
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris

        call her_main("{size=+7}!!!!!!!!!!!!!!!!!{/size}", "scream", "wide", "worried", "stare",cheeks="blush",tears="soft")
        call her_main("My...{w} My...{w} My...")
        m "Shut it, girl! You are being loud."
        with hpunch
        call her_main("{size=+7}My anus!!!!!!!!!!!!!{/size}", "scream", "wide", "worried", "stare",cheeks="blush",tears="soft")
        g4 "Dammit, girl. I said be quiet."

        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "mouth_open_tongue", "brows", "blush", "tears2")
        call hide_blkfade

        her "{size=+7}I can't! I don't care! It hurts!!!{/size}"
        g4 "Maybe you don't care, but I do, you whore!"
        $ dynamic_cg("ball/sex", "background", "base", "eyes_stare", "blush", "tears2")
        her "{size=+5}Your cock is so huge!{/size}"
        g4 "We'll get caught because of you, you stupid slut!"
        m "Maybe this will help you shut up..."

        # Fishhooking
        $ dynamic_cg("ball/sex", "background", "base2", "blush2")
        her "!!!............"
        g4 "That's right, you slut. Keep quiet!"
        $ dynamic_cg("ball/sex", "background", "base2", "open_tongue2", "blush2")
        her "*Ah*... *Blah*..."
        g4 "Your butthole... It's so damn tight..."
        $ dynamic_cg("ball/sex", "background", "base2", "open_tongue2", "blush2", "spit")
        her "*Ah*... *blah*... *ah*..."
        g4 "You are drooling all over my hand, you nasty slut!"
        her "*Ah*... *Blah-blhah*... *ah*... *bla-ah*..."

        call blktone_top
        stop music fadeout 1.0
        sna "Well, we are about to start..."
        sna "Get into pairs now..."
        sna "No! Male-female pairs, you dull creatures. What do you think this is? A laboratory assignment?"

        call hide_blktone_top
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open_tongue2", "eyes_r", "lashes", "blush", "spit")

        play music "music/Brandenburg No4-1 BWV1049 Kevin-McKleod.mp3" fadein 1 fadeout 1
        m "Don't you worry about missing out on your dance, whore."
        m "We will do a little bit of dancing of our own..."
        her "*Ah*..."
        m "Yes, this year's ball queen is performing a complicated pirouette with a dick buried deep in her tiny asshole!"
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open_tongue2", "eyes_stare", "lashes", "blush", "spit")
        her "*Ah*... I am *ahh*..."
        m "Did you say something, your majesty?"
        her "*Ah*... I am the autumn ball queen... *ah*..."
        m "Well of course you are!"
        m "But you're also a whore!"
        her "I'm a whore..."
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open_tongue2", "eyes_stare", "lashes", "brows", "blush", "spit")
        her "{size=+7}I'm a whore!!!{/size}"
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open_tongue2", "eyes_stare", "blush", "spit")
        her "{size=+10}I'm a whoooooooore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open_tongue2", "eyes_wide", "brows", "blush", "spit")

        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        $ dynamic_cg("ball/sex", "background2", "base", "eyes_dead", "blush", "spit")
        her "{size=+5} I'm cumming!!!{/size}"

        with hpunch
        g4 "*Argh*! My cock!"
        $ dynamic_cg("ball/sex", "background2", "base", "eyes_dead", "brows", "blush", "spit")
        her "{size=+10}I'M CUMMING! I'm a whore!{/size}"
        g4 "I can't fucking move it anymore!"
        her "{size=+10}I'm CUMMING!{/size}"

        g4 "My cock is stuck in your asshole, slut!"
        her "{size=+10}I'm a whooore!!!{/size}"
        g4 "Relax your muscles a little, dammit!"
        $ dynamic_cg("ball/sex", "background2", "base", "eyes_dead", "blush", "spit")
        her "{size=+7}I can't! I'm cumming!!!{/size}"
        g4 "Fine! Have it your way. I am switching back to your pussy..."
        $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "blush", "spit")
        her "*Huh*?"
        call blkfade

        g4 "Can't pull out!"
        g4 "Relax your damn anus, girl! ..."

        call play_sound("boing")
        with hpunch
        pause.3

        call her_main("...........", "angry", "narrow", "annoyed", "up",cheeks="blush",tears="messy", ypos="head")
        m "There..."


        ### INSERTING ###

        call play_sound("insert")
        with hpunch
        with kissiris
        pause.5

        hide screen bld1
        hide screen blkfade
        $ dynamic_cg("ball/sex", "background2", "base", "blush", "mascara", "spit")
        her "{size=+10}*AAAAAAAAAAAH*!!{/size}"
        her "It's in my pussy again..."
        g4 "Yes it is, slut!"
        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open", "eyes_up", "lashes", "blush", "mascara", "spit")
        her "But I'm still cumming!"
        her "What is happening to me, sir!?"
        m "Relax girl, I know what I'm doing!"
        m "This is normal for a slut."
        $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "lashes", "blush", "mascara", "spit")
        her "{size=+5}No! I will go insane!!!{/size}"
        g4 "You will not. Just ride the wave."
        g4 "Enjoy the sensation while I keep on pounding your pussy!"
        her "{size=+5}*Ah*!!!{/size}"

        $ dynamic_cg("ball/sex", "background2", "base", "mouth_open", "eyes_down", "lashes", "brows", "blush", "mascara", "spit")
        her "{size=+5}*Oh*!!!{/size}"
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"
        her "{size=+5}I'm a slut!!!{/size}"
        g4 "Yes you are!"
        g4 "*Oh*... I think I am getting close myself..."
        g4 "*Argh*!"

        $ menu_x = 0.5 #Menu is moved to the left side.

        menu:
            "-Cum inside Hermione's pussy-":
                $ d_flag_01 = True # Came into pussy

                g4 "You think your pussy is ready for this, whore?"
                her "Sir?!"
                g4 "Then take this!"

                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_wide", "blush", "mascara", "spit", "cum_pussy")

                her "{size=+5}*Ah*! *AAaaah*!!{/size}"
                g4 "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

                her "{size=+5}*Ah*! I can feel it! It's so hot!{/size}"
                g4 "*Argh*! Yes!"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "lashes", "blush", "mascara", "spit", "cum_pussy", "cum_extra")

                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump your witch cunt full of my cum!"

                $ dynamic_cg("ball/sex", "background2", "base", "eyes_down", "mouth_open_tongue2", "blush", "mascara", "spit", "cum_pussy", "cum_extra")
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the moment!"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "lashes", "blush", "mascara", "spit", "cum_pussy", "cum_extra")
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"
                g4 "*Oh*......."

            "-Cum inside Hermione's butt-":
                $ d_flag_01 = False # Came into asshole

                g4 "Your butthole better be ready for this, whore!"
                her "What?!"

                call play_sound("insert")
                pause.5
                her "*Ah*..."

                call play_sound("boing")
                with hpunch
                with kissiris
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_stare", "mouth_open", "blush", "brows", "mascara", "spit")
                her "{size=+10}*AAaaaahhhhh*!!!{/size}"
                her "{size=+5}It's in my butthole again!{/size}"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "mouth_open", "blush", "brows", "mascara", "spit")
                her "{size=+5}No, sir, please! Don't cum in my butt!{/size}"
                her "{size=+5}No, I will die!!!{/size}"
                g4 "You will not die, you silly girl."
                g4 "You will orgasm like crazy, maybe even pass out for a while, but that's all..."
                her "No, sir, please... I'm scared..."
                g4 "Take this, whore!"
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch

                g4 "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_stare", "mouth_open", "blush", "brows", "mascara", "spit")
                her "{size=+5}*Ah*! I can feel it!!!{/size}"
                g4 "*Argh*! Yes!"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_stare", "blush", "brows", "mascara", "spit", "cum_anal")
                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump you full of my cum!"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_down", "blush", "mascara", "spit", "cum_anal")
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the moment!"
                $ dynamic_cg("ball/sex", "background2", "base", "eyes_up", "blush", "lashes", "mascara", "spit", "cum_anal")
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"

        call ctc

        show screen blkfade
        with d9

        stop music fadeout 1.0
        call her_main("*Ah*...", "silly", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft", ypos="head")
        call her_main("I can... barely... stand...")
        g4 "I know what you mean, girl."
        g4 "This was our most intense fucking session yet!"
        call her_main("Yes... I never knew I could...", "silly", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        call her_main("orgasm so hard...")
        call her_main("Sir... That thing you wanted to discuss with me...", "soft", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Yeah... You know what? I actually wrote you a little letter on the matter..."
        call her_main("A letter?", "open", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara_soft")
        m "Yeah... It should explain a couple of things..."
        call her_main("Oh... Alright...", "silly", "narrow", "annoyed", "up",cheeks="blush",tears="mascara_soft")
        m "Just come and pick it up from my office tomorrow morning..."
        m "Or whenever..."
        m "Or don't pick it up, I don't care..."
        g4 "............."
        call her_main("Sir...?", "base", "base", "worried", "mid", cheeks="blush",tears="mascara")
        m "Stop it with the eyes! You're making me feel uncomfortable..."
        m "I wrote you a letter, so what?"
        call her_main("I think it's sweet.........", "base", "base", "worried", "mid", cheeks="blush",tears="mascara")
        g4 "I said stop gawking at me girl. I thought you were late for your dance or something!"
        call her_main("{size=+5}THE DANCE!{/size}", "open", "wide", "base", "stare",cheeks="blush",tears="mascara")
        call her_main("I'm sorry, I have to go!")
        call her_main("I will see you later, sir!")

        call play_sound("running")
        pause 3
        m "......................"
        m "No you won't..."
        m "Farewell...{w=0.3} Hermione..."

        pause 2

        play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1

        $ dynamic_cg("ball/intro", "background", "bloom", "hermione2", "foreground", "overlay")

        ">You linger in the alcove for a short while longer..."
        ">And watch Hermione participate in the formal dance."
        hide screen bld1
        call hide_blkfade
        call ctc

        ">There is no doubt that she is tired and exhausted, but she hides it well..."

        m "(*Hmm*... The girl really is strong...)"
        m "(In all sorts of ways...)"


        if d_flag_01: # Came into pussy
            ">You see a tiny stream of glistening liquid dripping down her inner thighs, going unnoticed by the crowd."
        else: # Came into asshole
            ">You notice that she sort of clenches her buttocks together every now and then..."
            ">Probably doing her best to keep in the enormous load you deposited up her butthole just a moment ago..."


        m "................................................."
        m "..............."
        m "(I'd better go now...)"

        call ctc

    $ renpy.end_replay()

    label test_final_scene:

    # Genie is leaving
    call blkfade
    pause 1
    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    $ game.daytime = False
    call update_interface_color

    hide screen cg

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")
    pause.3
    call hide_blkfade

    call play_music("night_outside")
    call ctc

    call play_sound("walking_on_grass")
    pause 2

    $ ccg(layer2="172")
    pause 1
    m "Well, now it is really time for me to go..."

    $ ccg(layer3="173")
    pause.5

    m "Goodbye, world of bizarre magic..."
    m "Goodbye, my whores..."
    m "Goodbye, smart cumslut Hermione..."
    if cho_unlocked:
        m "and my token asian Cho..."
    if astoria_unlocked:
        m "and my sassy blonde Astoria..."
    if luna_unlocked:
        m "and my {i}wackspit-sucking{/i} queen Luna..."
    if susan_unlocked:
        m "and my big-titted redhead Susan..."
    m "and of course, goodbye to my favourite nympho, Tonks..."
    m "....................."
    m "..........."
    "......"

    call play_sound("magic")
    with hpunch

    $ ccg(layer2="174", layer3="blank")
    pause.2

    $ ccg(layer2="175")
    pause.2

    $ ccg(layer3="blank")
    pause.2

    $ ccg(layer2="blank")
    call ctc

    show screen blktone
    with d7

    $ achievement.unlock("ending")
    stop music fadeout 1.0

    if public_whore_ending:
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n{color=#cbcbcb}This is one of two possible endings (public whore){/color}"
    else:
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n{color=#cbcbcb}This is one of two possible endings (personal whore){/color}"

    show screen blkfade
    with d7

    if not persistent.game_complete:
        call original_credits

    pause.5

    # Dumbledore is back at Hogwarts
    centered "{size=+7}{color=#cbcbcb}The next morning...{/color}{/size}"

    $ game.daytime = True
    call update_interface_color

    $ hermione.equip(her_outfit_default)

    hide screen ccg
    hide screen blktone
    stop bg_sounds
    stop weather
    hide screen notes
    hide screen bld1

    $ game.weather = "random"
    call weather_sound
    show screen weather

    show screen main_room
    show screen chair_right

    call gen_chibi("hide")
    $ owl_OBJ.hidden = True
    hide screen with_snape

    show screen chair_right
    show screen dumbledore

    hide screen blkfade
    with d9

    if public_whore_ending:
        call play_sound("door")
        call sna_chibi("stand","door","base", flip=False)
        with d3
        pause.8
        call sna_walk("mid", "base")
        pause.8

        call play_music("snape")
        dum1 "Good morning, Severus."
        call sna_main(".......................................","snape_09", xpos="base", ypos="base")
        dum1 "I have the most extraordinary tale to share with you, old friend."
        sna "......................................"
        dum1 "But before I do..."
        sna "........................................"
        dum2 "*Ehm*... Severus?"
        sna "........................................."
        call sna_main("Who rules?","snape_06")
        dum2 "I beg your pardon?"
        call sna_main("Who rules?","snape_26")
        dum2 "... who rules what?"
        sna "R...?"
        dum2 "R?"
        call sna_main("Robin....?","snape_27")
        dum2 "You don't make any sense, Severus."
        call sna_main("Ah, bloody hell.........","snape_29")
        pause.5
        call ctc

        stop music fadeout 1.0

        hide screen snape_main
        hide screen bld1
        show screen blkfade
        with d7
        pause.1

    else:
        # Personal whore ending
        call play_sound("door")
        call her_chibi("stand","door","base", flip=False)
        pause.8

        call her_walk("mid", "base")
        pause.8

        call play_music("hermione")
        call her_main("Sir, if this is about yesterday...", "upset", "closed", "base", "mid", xpos="right", ypos="base")
        dum1 "Good morning, Miss Granger."
        call her_main("It's not like I actually enjoyed it or anything, you know...", "annoyed", "narrow", "annoyed", "mid")
        dum1 "Miss Granger, I found this letter on my desk..."
        dum1 "It's addressed to you..."
        call her_main("A letter, sir?", "soft", "base", "base", "mid")
        call her_main("Oh, of course! The one you wrote for me, sir.", "grin", "happyCl", "worried", "mid",emote="sweat")
        dum1 "This letter is not from me, miss Granger."
        call her_main("It is not?", "annoyed", "squint", "base", "mid")
        call her_main("Oh, I see...", "grin", "happyCl", "worried", "mid",emote="sweat")
        call her_main("There is no need to be so shy about this, sir. It's alright.")
        dum1 "*ahem*... here it is."
        call her_main("Thank you, sir.", "base", "base", "base", "mid")
        call her_main("Let's see...", "annoyed", "narrow", "worried", "down")
        hide screen hermione_main
        with d3
        stop music fadeout 7.0
        pause.1

        # Read letter from Genie
        $ letter = Letter(text="""{size=-5}To: Hermione Granger{/size}

{size=-4}Dear [word_01],

I am not who you think I am... I'm not even human, so to speak. For months I have been posing as a person known to you as Professor Dumbledore. But now it is time for me to go back [word_02], where I belong.
By the time you will read this letter I shall be long gone. We shall never cross paths again, but I promise you that I will cherish the memories of my brief time in your strange world.

Farewell, my little [word_03].{/size}

{size=-5}-Yours truly, [word_04]-{/size}"""
        )

        $ menu_x = 0.5
        $ menu_y = 0.9

        show screen letter
        with d5

        menu:
            "-Done reading-":
                pass

        call reset_menu_position

        hide screen letter

        call her_main( "...........................................................................................................","disgust","wide","worried","shocked",cheeks="blush")
        dum1 "I assume you were expecting to meet with that \"[word_04]\" fellow?"
        dum1 "The one who has been impersonating me for the past several months?"
        call her_main( "...........................................................................................................","disgust","wide","worried","shocked",cheeks="blush")
        dum1 "Well, now that I am back..."
        dum1 "I will be putting an end to all that \"favour selling business\", of course."
        call her_main("", "scream", "base", "angry", "mid",emote="angry")
        pause.1
        with hpunch
        call play_music("hermione")
        her "{size=+7}What?!!{/size}"
        call her_main("How am I supposed to win any points then?", "disgust", "narrow", "base", "mid_soft")
        dum1 "The same way you always did, miss Granger."
        call her_main("Huh...?","open","narrow","annoyed","mid",cheeks="blush")
        dum1 "With hard work."
        call her_main("That's just stupid!", "angry", "base", "angry", "mid",cheeks="blush")
        dum2 "Miss Granger, would you mind to guard your tongue when--"

        ### TITS ###
        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top", "bra")
        call her_main("", "annoyed", "narrow", "annoyed", "mid")
        stop music
        call ctc

        dum3 "{size=+4}!!!{/size}"
        call her_main("Or would you rather see my pussy, sir?", "scream", "base", "angry", "mid",emote="angry")
        call her_main("", "annoyed", "base", "angry", "mid")

        $ hermione.strip("bottom", "panties")
        call ctc

        with hpunch
        dum5 "{size=+7}*GHT*!!!{/size}"
        her "I am willing to do anything to get those points, sir!"

        call her_main("And I mean {size=+9}ANYTHING!!!{/size}", "scream", "base", "angry", "mid",emote="angry", trans=hpunch)
        call her_walk("desk", "base", reduce=0.8)
        call blkfade

        call play_sound("climb_desk")
        pause.7

        dum4 "Oh, dear... {heart} "
        pause 1


    $ renpy.play('sounds/win2.mp3')

    centered "{color=#cbcbcb}This concludes the original Witch Trainer ending{fast}\n\n{size=+7}-\{Thank you for playing!\}-{/size}{/color}"

    pause 2

    $ ball_quest.completed = True
    $ persistent.game_complete = True
    $ persistent.gold = game.gold

    if public_whore_ending:
        $ persistent.ending_02 = True
    else:
        $ persistent.ending_01 = True

    # But wait, there's even more
    jump ending_after

label original_credits:
    play music "music/Only 115 (Electro Loop)_125 BPM.mp3" fadein 1 fadeout 1

    centered """{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}The following credits are the creators of the original game, Witch Trainer,\nand did not take part in creating, or are affiliated in any way with the Silver mod.{/color}{/size}\n\n
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"""

    centered """{cps=40}
    {size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Dahr{/color}{/size}\n
    {color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n
    {size=+5}{color=#cbcbcb}Xaljio{/color}{/size}\n
    {color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n{/color}
    {size=+5}{color=#cbcbcb}Lyk.D9 (a.k.a. Silentchill){/color}{/size}\n
    {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar.{/color}\n\n
    {size=+5}{color=#cbcbcb}Bookfisher{/color}{/size}\n
    {color=#e5e297}For everything.\n\n{/color}
    {size=+5}{color=#cbcbcb}The fate (universe or higher power){/color}{/size}\n
    {color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.{/color}\n\n\n
    {size=-1}{color=#cbcbcb}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.{/color}{/size}{/cps}"""

    centered """{cps=70}
    {color=#cbcbcb}This is not a commercial video game. The entire project was independently founded solely through\nhttp://www.patreon.com/ and\nby \"Hentai United\" subscribers.{/color}\n\n\n
    {color=#e5e297}{size=-1}-People who supported development of this game with extraordinary amount of money-{/size}{/color}\n
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/cps}"""

    centered """{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}"""

    centered """{cps=70}
    {size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}"""

    pause 1
    call ctc
    stop music fadeout 3.0
    return
