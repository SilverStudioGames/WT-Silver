
# Mirror story: Sucn and Run
label suck_and_run:

    $ temp_day = game.daytime
    $ game.daytime = False
    call update_interface_color
    call room("main_room")
    show screen blkfade
    with d5

    call reset_menu_position

    centered "{size=+7}{color=#cbcbcb}Suck & Run{/color}{/size}"

    label .choices:
    show screen blkfade
    with d5

    menu:
        "For the best experience it is recommended to play the story in chronological order."
        "-Part one-":
            $ pathvalue = 0
        "-Part two-":
            $ pathvalue = 1
        "-Part three-":
            $ pathvalue = 2
        "-Go back-":
            # Return
            $ game.daytime = temp_day
            call update_interface_color
            jump enter_room_of_req

    stop music fadeout 1.0
    pause 1.0

    if pathvalue == 0:
        $ game.daytime = False
        call update_interface_color
        call music_block

        call setup_fireplace_hangout(char="snape")

        call sna_main("*Ah*... Been looking forward to this...","snape_23", ypos="head")
        m "Rough day I take it?"
        call sna_main("Bloody slackers all of them!","snape_17")
        g4 "..."
        call sna_main("What's the point of me teaching them anything if they can't even bother staying awake?","snape_32")
        m "Are we talking about your Slytherin sluts again?"
        m "Surely that's on you if anything."
        m "Maybe you need to spice things up a bit."
        call sna_main("What? No! I'm perfectly capable in that capacity!","snape_04")
        call sna_main("... Unless you've heard something?","snape_03")
        call sna_main("No, these students in particular are some Hufflepuff boys.","snape_16")
        call sna_main("Now they're lazy at the best of times, but catching someone sleeping in my class... That's a first.","snape_07")
        call sna_main("I wish I could hang them up by their ankles, like in the old days! That would show them!","snape_08")
        m "Come on man, it's Halloween!"
        m "Cheer up a little will you."
        call sna_main("*Mmm*... The time of year when girls will put on any type of outfit with the word \"slutty\" written in front of it.","snape_23")
        g9 "Exactly!"
        call sna_main("Wait a minute...","snape_01")
        call sna_main("Do genies even celebrate Holidays?","snape_04")
        call sna_main("I'd think the novelty of it would wear off rather quickly.","snape_01")
        m "You kidding me?"
        m "The time these Holiday celebrations have been around has been but a blip of my entire existence."
        m "I was around when they burnt your kind at the stake... And that wasn't even that long ago to me."
        call sna_main("Right...","snape_31")
        m "Besides... Nightmare before Christmas is like my favourite Halloween movie..."
        call sna_main("Halloween... what?","snape_05") # Snape doesn't know what a movie is
        m "Christmas movie... Whatever."
        call sna_main("You're such a mystery to me sometimes Genie...","snape_06")
        g4 "Come on, you must have seen it! At least heard of it."
        call sna_main("I'm afraid I have not seen this Nightmare {i}moo-wee{/i} thing.","snape_09")
        m "Okay so there's this guy... Jack Skellington, and he's the \"Pumpkin King\" of Halloween Town."
        m "Which kind of makes him the boss of the place. Only there's a mayor. Look, I don't know enough about the politics."
        m "Anyway... He decides he wants to be Santa Claus, so he kidnaps him in order to take over his position."
        m "Only then the Americans shoot him down and Jack has to release Santa in order to save Christmas."
        call sna_main("...","snape_03")
        m "Actually, maybe it is a Christmas movie after all..."
        call sna_main("...","snape_04")
        m "Yeah, you're right... In that case Die Hard would easily take the top spot."
        m "Now that I think of it, the villain kind of looks like--"
        call sna_main("Die... Hard?","snape_05")
        m "Don't you dare tell me it's not A Christmas movie!"
        call sna_main("Whatever it is you're on about sounds dreadfully boring.","snape_03")

        call nar("You and Snape continue drinking long into the night. You exchange tales of the skimpiest outfits you've seen girls wearing, and the issues with sticking your dick in crazy.")

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen with_snape
        $ game.daytime = temp_day
        centered "{size=+7}{color=#cbcbcb}End of part one{/color}{/size}"

        jump suck_and_run.choices

    elif pathvalue == 1:
        $ game.daytime = False
        call update_interface_color
        call play_music("tonks")

        call setup_fireplace_hangout(char="tonks")

        m "Getting into the Halloween spirit?"
        call ton_main("Of course!", "grin", "wide", "base", "mid", ypos="head")
        call ton_main("I've been looking forward to the Halloween feast ever since I got here.", "crooked_smile", "closed", "base", "mid")
        call ton_main("Brings back memories.", "base", "base", "base", "downR")
        m "*Ha-hah*, yeah... That food thing that I do all the time. Love it!"
        call ton_main("It also gives me a great excuse to dress down!", "horny", "closed", "base", "mid")
        m "Don't you mean dress up?"
        call ton_main("Same thing...", "horny", "narrow", "base", "mid")
        m "So, what will it be this year then?"
        call ton_main("*Hmm*... Why don't you have a guess...", "soft", "base", "raised", "down")

        menu:
            "\"A Slutty Nurse?\"":
                call ton_main("Ohhh... that'd be fun. Do you have a fever?", "horny", "wink", "base", "mid")
                call ton_main("I could take your temperature.", "grin", "narrow", "raised", "mid")
                call ton_main("Orally, of course.", "horny", "closed", "base", "mid") #lewd wink
                g9 "You naughty--"
                g4 "Wait, what do you mean about that exactly?"
                call ton_main("Wouldn't you like to know...", "base", "base", "raised", "R")
                call ton_main("But no, that's not it...", "soft", "narrow", "base", "R")
            "\"A Slutty School girl?\"":
                call ton_main("Someone's getting greedy.", "base", "narrow", "base", "mid")
                call ton_main("Don't you have enough of those already?", "horny", "base", "raised", "mid")
                m "Never."
            "\"A Slutty Witch?\"":
                call ton_main("Isn't that just my normal clothing?", "soft", "base", "base", "down")
                m "That's true..."

        m "So... What is it then?"
        call ton_main("*Hmm*... Not sure I should ruin the surprise.", "horny", "wink", "base", "mid")
        call ton_main("I'm sure you'll find out soon enough...", "base", "narrow", "base", "R", hair="horny") #Glance #hornyhair
        g9 "Looking forward to it."
        call ton_main("Anyway...", "base", "base", "shocked", "mid")
        call ton_main("Anything else going on that I should know of?", "soft", "base", "base", "down")
        m "*Err*... I had a little chat with Severus the other night."
        call ton_main("*Hmm*... Not really the kind of thing I was talking about...", "annoyed", "base", "base", "mid")
        call ton_main("Although I'm always up for gossip.", "base", "base", "shocked", "R")
        call ton_main("I assume you weren't talking about Halloween... Since I doubt Snape would care about it in the slightest.", "crooked_smile", "base", "base", "R")
        m "Oh no, he absolutely loves it."
        call ton_main("Really?", "disgust", "wide", "shocked", "mid")
        call ton_main("Well... Colour me surprised...", "open", "closed", "base", "mid")
        m "Yes... He seemed quite eager to find out what the girls will be wearing this year in fact."
        call ton_main("Oh, so it's like that is it?", "base", "base", "raised", "down")
        m "He also mentioned that some Hufflepuff boys have been falling asleep during his lessons lately... What do you think--"
        call ton_main("What?! Why do you think I'd know anything about Hufflepuff boys falling asleep in class!?", "mad", "wide", "base", "mid")
        call ton_main("Are you implying that I'm sneaking into their room to fuck them? That I'm draining their cocks dry every night!?", "clench", "closed", "shocked", "mid")
        m "What? I was just going to ask if you thought they'd been staying up late partying or something."
        call ton_main("Oh.... No, I don't think they're doing anything like that.", "soft", "base", "base", "R", cheeks="blush")
        m "What was that about sucking them dry at night?"
        call ton_main("Did I say that? Are you sure you didn't just hear what you wanted to hear Genie?", "disgust", "base", "base", "downR")
        m "I'm pretty sure I heard you ask if I thought you were fucking your students at night."
        call ton_main("Then you must've misheard me..", "normal", "closed", "base", "mid", hair="horny")
        m "... Are you drooling?"
        call ton_main("*Mhmm*?", "normal", "wide", "base", "down")
        call ton_main("Oh, this?", "mad", "base", "raised", "mid")
        call ton_main("I was just thinking about what I'll be having for dinner tonight...", "soft", "closed", "base", "R")
        call ton_main("Creamy mushroom soup... Delicious!", "horny", "base", "base", "down", hair="horny")
        m "I see...{w=0.3} Very well."
        m "Please keep an eye on those Hufflepuff boys, alright?"
        call ton_main("Of course.... I'll make sure to inspect their dorms thoroughly.", "open", "closed", "base", "mid")
        call ton_main("I'll even give them a little pat down. Make sure they're not smuggling alcohol up there.", "grin", "closed", "base", "mid")
        call ton_main("Maybe a strip search or two.", "soft", "narrow", "base", "mid") #drooling ahegao face
        m "I don't think that will be necessary."
        m "Just make sure they're not staying up all night, alright?"
        call ton_main("*Aww*, You're no fun at all.", "annoyed", "narrow", "base", "mid") #pout
        m "*glares*"
        call ton_main("*Sigh* Fiiiiiine... Goodnight [ton_genie_name].","base","base","base","mid")
        m "Goodnight [tonks_name]."

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen with_tonks_animated
        $ game.daytime = temp_day
        centered "{size=+7}{color=#cbcbcb}End of part two{/color}{/size}"

        jump suck_and_run.choices

    elif pathvalue == 2:

        $ game.daytime = False
        $ fire_in_fireplace = False
        hide screen fireplace_fire
        hide screen bld1

        $ ton_outfit_last.save()
        call update_interface_color
        call gen_chibi("sit_behind_desk")
        call play_music("night_outside")

        show screen add_overlay
        hide screen blkfade
        with d5

        $ renpy.sound.play("sounds/snore1.mp3")
        m "*Snore*...{w=0.4}"

        call ton_walk(action="enter")
        call chibi_emote("exclaim", "tonks")
        pause 1.0
        call ton_walk("desk", "base")
        call chibi_emote("hearts", "tonks")
        pause 0.5

        #Black screen
        show screen blkfade
        with d3

        pause 1.5
        $ renpy.sound.play("sounds/zipper.mp3")
        pause 0.5
        call play_sound("giggle")
        pause 1.0

        call ton_chibi("hide")
        hide screen blkfade
        with d9

        pause 1.0
        play bg_sounds "sounds/slickloop.mp3" fadein 2
        "*Slurp* *Slurp* *Slurp*"
        m "*Mmm*...{w=0.3} Yes...{w=0.3} That's it, princess...{w=0.4} *Snore*..."
        "*Slurp* *Slurp* *Gulp*"
        m "*Nghh*...{w=0.3} I'm almost...{w=0.3} There...{w=0.4} Princess."
        "*Slurp* *Slurp* *Gulp*"
        m "*Snore*... *Sn--*"
        m "Princess--"
        g16 "Tonks?!"

        call play_music("tonks")
        call ton_main("*Slurp* *Slurp* *Gulp*!", face="horny", mouth="open_wide_tongue", xpos="far_right", ypos=200, trans=d3) # Explicit positions to avoid hiding the doll

        g4 "am I still dreaming?"
        call ton_main("*Slurp* *Slurp* *slurp*!", "open_wide_tongue", "narrow", "shocked", "stare")
        g4 "*Ngh*... But it feels so real!"
        stop bg_sounds
        call ton_main("...", "base", "closed", "annoyed", "up", hair="angry") #Hair turns red
        m "*Ah*... T-Tonks?!"

        $ renpy.sound.play("sounds/magic3.mp3")
        stop music fadeout 0.5
        $ tonks.equip(ton_outfit_succubus)
        call ton_main("", face="horny", pupils="mid", mouth="horny", trans=flash)

        pause 0.5
        call play_sound("giggle")
        call ton_main("*giggles*")

        $ renpy.music.play("music/determined_pursuit_loop.mp3")

        g4 "ARGH!"
        g4 "Unhand me foul demon!"
        call ton_main("Of course sir...", "grin", "base", "base", "L", hair="angry")
        call play_sound("giggle")
        pause .8
        call ton_main("Right away sir...", "crooked_smile", "base", "angry", "mid", hair="angry")
        call ton_main("Once I've gotten what I want...", "normal", "base", "angry", "stare", hair="angry")

        g4 "You may not have my life essence foul--"


        stop music fadeout 1.0
        call ton_main("", "horny", "base", "angry", "mid", hair="angry")
        $ renpy.sound.play("sounds/spit.mp3")
        pause 1
        g4 "Temptress?"
        call play_sound("giggle")
        call ton_main("", "grin", "base", "angry", "up", hair="angry")
        pause 2

        call ton_main("Just close your eyes and relax...", "normal", "narrow", "angry", "stare", hair="angry")
        m "*Ehm*..."
        m "So you don't want my soul?"
        call ton_main("Me? Want a soul as tainted and corrupt as yours?", "base", "base", "angry", "stare", hair="angry")
        call ton_main("Don't make me laugh...", "base", "base", "angry", "R", hair="angry")
        m "Then what do you--"
        call ton_main("", "grin", "base", "angry", "up", hair="angry")
        pause 2
        m "I see..."
        m "Well I guess that could be arranged..."
        call play_sound("giggle")
        pause 1
        call ton_main("Excellent... Now just relax and enjoy it...", "crooked_smile", "base", "base", "up", hair="angry")
        play bg_sounds "sounds/slickloopfast.mp3" fadein 2
        call ton_main("*Slurp* *Slurp* *slurp*!", face="horny", mouth="open_wide_tongue", ypos="head", hair="angry")
        g4 "*Argh*!"
        g4 "So...{w=0.4} *Ah*... What is it then?"
        call ton_main("*Slurp*?", "open_wide_tongue", "base", "base", "L", hair="angry")
        m "What kind of foul creature am I dealing with?"
        call ton_main("*Slurp* *Slurp* *slurp*", "open_wide_tongue", "closed", "base", "mid", cheeks="blush")
        m "Oh! Let me guess!"
        m "Are you a--"

        call play_music("tonks")

        stop bg_sounds
        call ton_main("A succubus?", "crooked_smile", "base", "angry", "up", hair="angry")
        m "*Argh*... You're no fun, I was just about to--"
        play bg_sounds "sounds/slickloopveryfast.mp3" fadein 2
        call ton_main("*Slurp* *Slurp* *Slurp*", "open_wide_tongue2", "narrow", "base", "up", hair="horny", cheeks="blush")
        m "*Nghh*...{w=0.4} To..."
        call ton_main("*Slurp*! *Slurp*! *Slurp*!", "open_wide_tongue2", "closed", "base", "up", cheeks="blush")
        m "Cum down your throat!"
        call ton_main("*Slurp* *Slurp* *Slurp*", "open_wide_tongue", "happyCl", "shocked", "mid", cheeks="blush")
        g4 "You asked for it!"
        g4 "Take this, foul demon!" #large text?
        stop bg_sounds
        $ renpy.sound.play("sounds/slick_02.mp3")
        call ton_main("*mmhf*!", "open_wide_tongue", "wide", "shocked", "up", cheeks="blush")

        with hpunch

        g4 "May the seed of an immortal--" #large text?
        $ renpy.sound.play("sounds/slick_02.mp3")
        call ton_main("*Mmm*! *Gulp* *Gulp*", "open_wide_tongue", "shocked", "shocked", "stare")

        with hpunch

        m "Quench your lust filled desires!"
        $ renpy.sound.play("sounds/slick_02.mp3")
        call ton_main("*Gulp*...{w=0.4} *Gulp*...{w=0.6} *Gulp*", "open_wide_tongue", "happyCl", "shocked", "mid", cheeks="blush")
        call ton_main("*Ah*...", "open_wide_tongue_cum", "base", "base", "down", cheeks="blush")
        $ renpy.sound.play("sounds/gulp.mp3")
        call ton_main("*Gulp*...", "normal", "closed", "base", "mid", cheeks="blush")
        call ton_main("Now that hit the--", "grin", "base", "base", "mid", cheeks="blush")

        $ renpy.sound.play("sounds/magic3.mp3")
        $ tonks.equip(ton_outfit_last)
        with flash

        call ton_main("Spot...", "open", "closed", "base", "mid")
        g9 "..."
        call ton_main("Hey!", "clench", "wide", "base", "down")
        call ton_main("How did you do that?", "clench", "wide", "base", "mid")
        m "Do what?"
        call ton_main("My form changed...", "disgust", "narrow", "base", "down")
        g9 "Nice, It worked!"
        g9 "My seed actually did quench your--"
        call ton_main("You idiot!", "open", "wide", "angry", "mid")
        g4 "What?!"
        call ton_main("Halloween is the only time I can get away with this...", "clench", "base", "annoyed", "down")
        call ton_main("And now you've ruined it!", "annoyed", "closed", "worried", "mid", hair="sad")
        m "Surely it is not my fault that my semen contains such immeasurable--"
        call ton_main("...", "annoyed", "narrow", "base", "down", hair="sad") #sad
        m "*Ahem*"
        m "So... A Succubus... *eh*?"
        call ton_main("Obviously...", "open", "narrow", "shocked", "downR", hair="sad")
        m "A sexual deviant that can't hold in their own desires..."
        g9 "Not sure why I didn't figure it out sooner..."
        call ton_main("Don't you dare tell anybody...", "annoyed", "base", "annoyed", "mid")
        m "Tell anybody that there's a lust filled creature hiding in plain sight?"
        g9 "Who are we talking about again?"
        call play_sound("giggle")
        call ton_main("*giggles*", "base", "happyCl", "base", "mid")

        show screen blkfade with d3

        call unlock_clothing(text=">New clothing items for Tonks have been unlocked!", item=ton_outfit_succubus)

        stop music fadeout 1.0
        hide screen add_overlay
        $ game.daytime = temp_day
        centered "{size=+7}{color=#cbcbcb}End of part three{/color}{/size}"

        jump suck_and_run.choices
