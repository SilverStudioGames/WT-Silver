
# Mirror story: Sucn and Run
label suck_and_run:

    $ temp_day = game.daytime
    $ game.daytime = False
    call update_interface_color
    call room("main_room")
    hide screen owl
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

        sna "*Ah*... Been looking forward to this..."
        m "Rough day I take it?"
        sna "Bloody slackers all of them..."
        sna "What's the point of me teaching them anything if they can't even bother staying awake?"
        m "Are we talking about your Slytherin sluts again?"
        m "Surely that's on you if anything."
        m "Maybe you need to spice things up a bit."
        sna "What? No! I'm perfectly capable in that capacity!"
        sna "... Unless you've heard something?"
        sna "No, these students in particular are some Hufflepuff boys."
        sna "Now they're lazy at the best of times, but catching someone sleeping in my class... That's a first."
        sna "I wish I could hang them up by their ankles, like in the old days! That would show them!"
        m "Come on man, it's Halloween!"
        m "Cheer up a little will you."
        sna "*Mmm*... The time of year when girls will put on any type of outfit with the word \"slutty\" written in front of it."
        m "Exactly!"
        sna "Wait a minute..."
        sna "Do genies even celebrate Holidays?"
        sna "I'd think the novelty of it would wear off rather quickly."
        m "You kidding me?"
        m "The time these Holiday celebrations have been around has been but a blip of my entire existence."
        m "I was around when they burnt your kind at the stake... And that wasn't even that long ago to me."
        sna "Right..."
        m "Besides... Nightmare before Christmas is like my favourite Halloween movie..."
        sna "Halloween... what?" # Snape doesn't know what a movie is
        m "Christmas movie... Whatever."
        sna "You're such a mystery to me sometimes Genie..."
        m "Come on, you must have seen it! At least heard of it."
        sna "I'm afraid I have not seen this {i}moo-wee{/i} thing."
        m "Okay so there's this guy, Jack Skellington, and he's the \"Pumpkin King\" of Halloween Town."
        m "Which kind of makes him the boss of the place. Only there's a mayor. Look, I don't know enough about the politics."
        m "Anyway... He decides he wants to be Santa Claus, so he kidnaps him in order to take over his position."
        m "Only then the Americans shoot him down and Jack has to release Santa in order to save Christmas."
        m "You really haven't ever heard of this?"
        sna "Whatever it is you're on about sounds dreadfully boring."

        nar "You and Snape continue drinking long into the night. You exchange tales of the skimpiest outfits you've seen girls wearing, and the issues with sticking your dick in crazy."

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
        ton "Of course!"
        ton "I've been looking forward to the Halloween feast ever since I got here."
        ton "Brings back memories."
        m "*Ha-hah*, yeah... That food thing that I do all the time. Love it!"
        ton "It also gives me a great excuse to dress down!"
        m "Don't you mean dress up?"
        ton "Same thing..."
        m "So, what will it be this year then?"
        ton "Hmm... Why don't you have a guess..."

        menu:
            "\"A Slutty Nurse?\"":
                ton "Ohhh... that'd be fun. Do you have a fever?"
                ton "I could take your temperature."
                ton "Orally, of course." #lewd wink
                g9 "You naughty--"
                g4 "Wait, what do you mean about that exactly?"
                ton "Wouldn't you like to know..."
                ton "But no, that's not it.:.."
            "\"A Slutty School girl?\"":
                ton "Someone's getting greedy."
                ton "Don't you have enough of those already?"
                m "Never."
            "\"A Slutty Witch?\"":
                ton "Isn't that just my normal clothing?"
                m "That's true..."

        m "So... What is it then?"
        ton "Hmm... Not sure I should ruin the surprise."
        ton "I'm sure you'll find out soon enough..." #Glance #hornyhair
        g9 "Looking forward to it."
        ton "Anyway..."
        ton "Anything else going on that I should know of?"
        m "*Err*... I had a little chat with Severus the other night."
        ton "Hmm... Not really the kind of thing I was talking about..."
        ton "Although I'm always up for gossip."
        ton "I assume you weren't talking about Halloween... Since I doubt Snape would care about it in the slightest."
        m "Oh no, he absolutely loves it."
        ton "Really?"
        ton "Well... Colour me surprised..."
        m "Yes... In fact he seemed quite eager to find out what will the girls wear this year."
        ton "Oh, so it's like that is it?"
        m "He also mentioned that some Hufflepuff boys have been falling asleep during his lessons lately... What do you think--"
        ton "What?! Why do you think I'd know anything about Hufflepuff boys falling asleep in class!?"
        ton "Are you implying that I'm sneaking into their room to fuck them? That I'm draining their cocks dry every night!?"
        m "What? I was just going to ask if you thought they'd been staying up late partying or something."
        ton "Oh.... No, I don't think they're doing anything like that."
        m "What was that about sucking them dry at night?"
        ton "Did I say that? Are you sure you didn't just hear what you wanted to hear Genie?"
        m "I'm pretty sure I heard you ask if I thought you were fucking your students at night."
        ton "Then you must've misheard me.."
        m "...Are you drooling?"
        ton "*Mhmm*?"
        ton "Oh, this?"
        ton "I was just thinking about what I'll be having for dinner tonight..."
        ton "Creamy mushroom soup... Delicious!"
        m "I see...{w=0.3} Very well."
        m "Please keep an eye on those Hufflepuff boys, alright?"
        ton "Of course.... I'll make sure to inspect their dorms thoroughly."
        ton "I'll even give them a little pat down. Make sure they're not smuggling alcohol up there."
        ton "Maybe a strip search or two…" #drooling ahegao face
        m "I don't think that will be necessary."
        m "Just make sure they're not staying up all night, alright?"
        ton "*Aww*, You're no fun at all." #pout
        m "*glares*"
        ton "*Sigh* Fiiiiiine... Goodnight [tonks_genie_name]."
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
        ton "*Slurp* *Slurp* *slurp*!"
        g4 "*Ngh*... But it feels so real!"
        ton "..." #Hair turns red
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
        ton "Not before I get what I want..."
        m "You may not have my life essence foul--"

        stop music fadeout 1.0

        call ton_main("*Slurp* *Slurp* *slurp*!", face="horny", mouth="open_wide_tongue", ypos="head")
        m "*Ah*...{w=0.4} Temptress."
        m "So...{w=0.4} *Ah*... What is it then?"
        ton "*Slurp*?"
        m "What kind of foul creature am I dealing with?"
        ton "*Slurp* *Slurp* *slurp*"
        m "Oh! Let me guess!"
        m "Are you a--"

        call play_music("tonks")

        ton "A succubus?"
        m "*Argh*... You're no fun, I was just about to--"
        ton "*Slurp* *Slurp* *Slurp*"
        m "*Nghh*...{w=0.4} To..."
        ton "*Slurp*! *Slurp*! *Slurp*!"
        m "Cum down your throat!"
        ton "*Slurp* *Slurp* *Slurp*"
        g4 "You asked for it!"
        g4 "Take this, foul demon!" #large text?
        ton "*mmhf*!"

        with hpunch

        g4 "May the seed of an immortal--" #large text?
        ton "*Mmm*! *Gulp* *Gulp*"

        with hpunch

        m "Quench your lust filled desires!"
        ton "*Gulp*...{w=0.4} *Gulp*...{w=0.6} *Gulp*"
        ton "*Ah*..."
        ton "Now that hit the--"

        $ renpy.sound.play("sounds/magic3.mp3")
        $ tonks.equip(ton_outfit_last)
        with flash

        ton "Spot..."
        g9 "..."
        ton "Hey!"
        ton "How did you do that?"
        m "Do what?"
        ton "My form changed..."
        g9 "Nice, It worked!"
        g9 "My seed actually did quench your--"
        ton "You idiot!"
        g4 "What?!"
        ton "Halloween is the only time I can get away with this..."
        ton "And now you've ruined it!"
        m "Surely it is not my fault that my semen contains such immeasurable--"
        ton "..." #sad
        m "*Ahem*"
        m "So... A Succubus... ey?"
        ton "Obviously..."
        m "A sexual deviant that can't hold in their own desires..."
        g9 "Not sure why I didn't figure it out sooner..."
        ton "Don't you dare tell anybody..."
        m "Tell anybody that there's a lust filled creature hiding in plain sight?"
        g9 "Who are we talking about again?"
        call play_sound("giggle")
        ton "*giggles*"

        show screen blkfade with d3

        call unlock_clothing(text=">New clothing items for Tonks have been unlocked!", item=ton_outfit_succubus)

        stop music fadeout 1.0
        hide screen add_overlay
        $ game.daytime = temp_day
        centered "{size=+7}{color=#cbcbcb}End of part three{/color}{/size}"

        jump suck_and_run.choices
