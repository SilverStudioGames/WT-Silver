
# After the ending when Dumbledore has returned and the original credits have played
# the player gets a choice to either end the game or return to before the ending happened

# Genie gets stuck in the cosmos not being able to go anywhere
label ending_after:
    $ game.daytime = False
    call update_interface_color

    call blkfade
    call hide_screens
    centered "{size=+7}{color=#cbcbcb}Somewhere outside of time and space...{/color}{/size}\n\n"
    play music "music/epic-unease-by-kevin-macleod.mp3" fadein 1 fadeout 1 # noloop
    pause 3
    g2 "Where... where am I...?" with d5
    g2 "Am I dead... is this the end...?"
    g2 "Genies aren't supposed to die are they?"
    g12 "No wait... this is different...{w=0.4} what is this feeling?"
    g12 "I feel..."
    show screen white
    pause .1
    hide screen white
    g14 "Everything!" with hpunch
    g14 "The...{w=0.4} The cosmic power is running through me!"
    g14 "I can see it, the universe... No...{w=0.4} Multiple universes... all around me."
    g14 "But... Why?"
    g14 "Why am I not back yet!?"
    show screen white
    pause .1
    hide screen white
    $ renpy.sound.play("sounds/thunder_2.mp3")
    play bg_sounds "sounds/pulse.mp3"
    g15 "ARGH!" with hpunch
    g15 "My form is being pulled in multiple directions!"
    g15 "If I don't get out of here I'll be torn apart!"
    stop bg_sounds fadeout 4
    show screen white
    pause .1
    hide screen white
    g14 "Wait...{w=0.8} I know..." with d3
    g14 "This... it must be my magic!"
    g14 "I need to focus where I want to be... Or I'll be stuck... stuck here forever!"
    g14 "Stupid... life choices!"
    play bg_sounds "sounds/pulse.mp3"
    g14 "Focus..."
    g14 "I just left a bunch of Sluts at that school!"
    g14 "But... I need to get home!"

    # Choose to end the game or continue playing
    menu:
        g14 "What should I do?"
        "-Go home, to Agrabah!\n{size=-4}(exit to main menu){/size}-":
            g14 "Yes, that is probably for the best..."
            show screen white
            pause .1
            hide screen white
            $ renpy.sound.play("sounds/thunder_2.mp3")
            g15 "Agrabah... here I come! You better prepare yourself..." with hpunch

            stop bg_sounds fadeout 4
            stop music fadeout 10
            call big_bang

            $ renpy.full_restart()

        "-Cause a time paradox at Hogwarts-":
            g14 "On the other hand..."
            g14 "Who doesn't love..."
            show screen white
            pause .1
            hide screen white
            $ renpy.sound.play("sounds/thunder_2.mp3")
            g15 "Who doesn't love...{fast} a good old time paradox!" with hpunch
            g15 "It better be worth it...{w=0.4} Here I go!"

            stop bg_sounds fadeout 4
            stop music fadeout 10
            call big_bang

            # Genie stands in the forest before he's about to leave
            $ ccg_folder = "ball"
            $ ccg(layer1="171", layer2="172", layer3="173")
            call play_music("night_outside")
            pause.5
            call hide_blkfade

            m "Goodbye, world of bizarre magic..."
            m "Goodbye, my whor--"
            m "Wait..."

            # Record scratch, music stops
            $ ccg(layer3="blank")
            stop music fadeout 1.5
            $ renpy.play('sounds/scratch.wav')
            with hpunch

            g4 "What the fuck am I doing..."
            g4 "Why leave now when I'm the king of a castle filled with women ready to serve!?"

            # Heading back to the castle
            call play_music("night_outside")
            call blkfade
            hide screen ccg
            call hide_screens
            call play_sound("walking_on_grass")
            pause .5

            ">You hastily make your way back to the castle, wondering what kind of impulse made you want to leave in the first place..."
            stop music fadeout 3

            if public_whore_ending:
                play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
                ">Arriving at the great hall you glance through the doors and spot Hermione who's currently enjoying the attention she's receiving from some of the other students."
                ">You decide it's probably best to head back to your office. But before you get the chance to slip into the shadows Hermione has already begun making her way in your direction."
                ">As she steps through the door you notice some Slytherin students looking in your direction, smirks spreading across their faces."

                $ hermione.equip(her_outfit_ball)
                call her_main("Back so soon?", "base", "happy", "base", "L", cheeks="blush", xpos="base", ypos="head")
                m "I um...{w=0.4} had a change of heart."
                call her_main("Cold outside?", "base", "base", "base", "mid")
                m "Yes...{w=0.5} that's it."

                ">Standing there in silence, looking at Hermione, you can't help but struggle with what to say."
                ">Hermione looks at you expectantly and breaks the silence by extending one of her arms to you."

                call her_main("Care for a dance?", "open", "squint", "base", "mid", cheeks="blush", xpos="base", ypos="head")
                g9 "I...{w=0.5} of course!"
                call her_main("...", "base", "base", "base", "mid", cheeks="blush")
                ">With your arms wrapped around Hermione's waist the two of you begin moving along with the music."
                ">As some time passes it's very clear that the Slytherin students are looking at you both through the doorway."
                m "Miss Granger..."
                call her_main("Yes?", "base", "narrow", "base", "stare_soft", cheeks="blush")
                call play_sound("slap_3")
                call her_main("...", "soft", "happyCl", "base", "up", cheeks="blush")
                call her_main("Hey! At least warn me!", "clench", "narrow", "annoyed", "L", cheeks="blush")
                ">Swiftly taking your hand away from Hermione's butt, you give a quick smirk towards your audience."
                call her_main("I didn't say stop...", "soft", "narrow", "base", "L", cheeks="blush")
                g9 "Of course..."
                ">Without a moments hesitation you lift her skirt up, holding it against her back and leaving her panties exposed."
                call her_main("Sir...", "crooked_smile", "base", "base", "down", cheeks="blush") #could change the sirs here to the name that the player has set for hermione to call you
                ">Now firmly gripping her butt with your other hand, you begin to massage her cheeks whilst moving along with the music."
                call her_main("...", "grin", "narrow", "worried", "up", cheeks="blush") #Look of pleasure
                ">Your hand finds its way back down, pulling Hermione's panties down with it."
                call her_main("Sir...{w=0.4} what are you doing?", "open", "happyCl", "base", "stare", cheeks="blush")
                m "You seem a little bit tense... just giving you a hand..."
                call her_main("But... What if someone notices...", "annoyed", "base", "base", "R", cheeks="blush")
                ">Ignoring her pleas you begin rubbing your fingers between her thighs, not bothering to be discreet."
                call her_main("*Ah*...{w} Sir...", "open", "happyCl", "base", "mid", cheeks="blush")
                ">As you move your hand higher up her thighs, Hermione's breathing quickens and a wetness begins to spread across the side of your hand, her legs shaking slightly as she tries to keep it together."
                call her_main("Sir...{w=0.4} I...", "open", "happyCl", "base", "down", cheeks="blush")
                ">With the music soon coming to a close you shift your hand and begin stroking against her vagina with even more vigour than before."
                call her_main("Sir...{w=0.3} *Ah*...{w=0.5} they'll...{w=0.2} they'll hear me...", "mad", "happyCl", "base", "L", cheeks="blush")
                m "You better \"come\" quietly then..."
                call her_main("Sir... this isn't the time for...", "open", "happyCl", "base", "mid", cheeks="blush")
                ">As the music reaches it's peak, Hermione moves one of her hands off your back and puts it against her mouth to quickly try and stifle herself."
                her "*Mmmmf*..."
                with hpunch
                with kissiris
                stop music fadeout 6 #It's a bit sudden and quiet but not sure what to do instead
                ">Hermione shudders in your arms and then quickly lets go as the music comes to an end."
                call her_main("*Ah*...{w=0.8}*Ah*...{w=0.8}*Ah*...", "soft", "happyCl", "base", "mid", cheeks="blush")
                ">With a quick glance towards the doorway you notice some Slytherin students have blocked it with their backs towards you."
                m "You look tired girl, you'd better pull yourself together..."
                call her_main("Yes...{w=0.3} *Ah*...{w=0.6} I just need to...{w=0.3} catch my breath...", "open", "squint", "worried", "L", cheeks="blush")
                m "Perhaps sooner rather than later, the music has stopped..."
                call her_main("Oh...{w=0.3} *Ah*...{w=0.3} I didn't even notice...", "open", "happy", "worried", "mid", cheeks="blush")
                ">Hermione moves to stand up but stumbles as she tries to compose herself..."
                ">As she gets on her feet she looks up and notices the backs of the Slytherins in the doorway. She spins around to look at you, a red colour quickly spreading across her cheeks."
                call her_main("I...{w=0.3} I think I'd better head off to bed then...", "mad", "squint", "base", "stare_soft", cheeks="blush") #Worried #Sheepish looking
                m "Sounds like a good idea..."
                call her_main("Okay then...", "soft", "squint", "worried", "R", cheeks="blush") # smiles
                call her_main("Good night...", "base", "squint", "worried", "mid", cheeks="blush")
                m "Good night Miss Granger."


                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                call hide_blkfade
                pause 1.0
                call play_sound("door")
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                m "Good night princess..."

                call blkfade

                # Next day
                call defer_daytime_change(True)
                centered "{size=+7}{color=#cbcbcb}The next morning...{/color}{/size}"
                call hide_blkfade

                # Snape enters and walks up to desk
                call sna_walk(action="enter", xpos="desk")
                g4 "What did I tell you about knocking!"
                call sna_main("Who rule...","snape_03",ypos="head")
                call sna_main("You mother fucker...","snape_01",ypos="head")
                call sna_main("I knew it!","snape_02",ypos="head")
                call sna_main("I knew you couldn't make yourself leave yet.","snape_02",ypos="head")
                g9 "Hey, it's not my fault this place has so many..."
                g4 "I have urges okay!"
                call sna_main("How very uncharacteristic of you...","snape_01",ypos="head")
                call sna_main("But good news nonetheless...","snape_02",ypos="head")
                call sna_main("So I take it you have... unfinished business before you depart?","snape_37",ypos="head")
                m "A headmaster can't just up and leave before the school year is over can he?"
                m "Also I'm getting quite fond of the place... Not that I want to pick out curtains or anything."
                call sna_main("...","snape_45",ypos="head")
                call sna_main("Very well... our little scheme continues.","snape_02",ypos="head")
                call sna_main("Although at the moment I've got a class to attend to.","snape_01",ypos="head")
                call sna_walk("door")
                m "Yes... I also have very important business to get on with..."
                call sna_main("Sure you do...","snape_01",ypos="head")
                call sna_walk(action="leave")

                jump main_room
            else:
                play music "music/court-of-the-queen-by-kevin-macleod.mp3" fadein 1 fadeout 1
                ">Arriving at the great hall you decide to take a quick glance through the doors before heading back to your office."
                ">Hermione is currently occupied looking out one of the windows and doesn't notice your presence."
                ">You glance over at the teachers table and lock eyes with Snape who hastily stands up and quickly slides towards you."
                call sna_main("Good evening sir...{w=0.5} I...{w=0.8} I didn't expect you so soon.","snape_29",ypos="head")
                m "Hello again Severus."
                m "I have returned..."
                call sna_main ("*Ahem...*{w=0.4} I see...","snape_06",ypos="head")
                call sna_main ("Well...{w=0.5} Here it goes...","snape_04",ypos="head")
                call sna_main ("Who...{w=0.5} who rules?","snape_09",ypos="head")
                m "..."
                call sna_main (".............","snape_25",ypos="head")
                call sna_main ("...","snape_26",ypos="head")
                g9 "Robin Williams."
                call sna_main("You mother fucker!","snape_20",ypos="head") #Epic handshake meme (jk)
                g9 "..."
                call sna_main("...","snape_12",ypos="head")
                call sna_main("About the thing I said earlier.","snape_12",ypos="head")
                m "yes?"
                call sna_main("The whole friend thing...","snape_14",ypos="head")
                m "*Ah*... yes..."
                m "I mean, I was leaving and all that--"
                call sna_main("No...{w=0.4} Even that being the case... I did mean it...{w=0.4} good ones are hard to come by.","snape_24",ypos="head")
                g9 "Well... even if you didn't mean it, I bet you ain't never had a friend like me."
                call sna_main ("Ain't that true...{w=0.3}","snape_45",ypos="head")
                call sna_main ("So...{w=0.4} You're staying then?","snape_46",ypos="head")
                g9 "Can't just leave in the middle of the school year can I? What kind of headmaster would do that?"
                call sna_main ("Is that so...","snape_47",ypos="head")
                g9 "There are still plenty of girls that haven't seen me at my best!"
                call sna_main("There it is...","snape_02",ypos="head")
                call sna_main("Well then...{w=0.4} Business as usual tomorrow?","snape_05",ypos="head")
                m "Business as usual..."
                call sna_main ("{size=-4}Fuck yes!{/size}","snape_47",ypos="head")
                m "What did you say?"
                call sna_main ("Nothing...","snape_38",ypos="head")
                m "Okay then..."
                m "In that case I'll head back to my office."

                $ hermione.equip(her_outfit_ball)
                ">As Snape slides back towards the teachers table, Hermione notices your presence and quickly starts walking towards you."
                ">Before you can even attempt to slip into the shadows again, she's already come through the doorway with one of her arms held out in front of her."
                call her_main("Care for a dance?", "base", "happy", "base", "L", cheeks="blush", xpos="base", ypos="head") # smiles
                m "I...{w=0.4} Oh, what the hell... why not."
                call her_main("...", "base", "narrow", "base", "down", cheeks="blush", xpos="base", ypos="head") # smiles
                ">With your arms wrapped around Hermione's waist, the two of you begin moving along with the music."
                ">After some time passes you can't help but look down on Hermione's butt sticking out below your hands."
                m "Miss Granger..."
                call her_main("Yes?", "open", "base", "base", "L", cheeks="blush", xpos="base", ypos="head")
                ">Hands now wandering down towards Hermione's butt she smiles and tightens her grip around you."
                ">Gently resting your hands against her cheeks you return to slowly moving along with the music."
                call her_main("Sir...", "base", "base", "base", "mid", cheeks="blush")
                m "Yes Miss Granger?"
                call her_main("Could...", "normal", "closed", "base", "mid", cheeks="blush")
                call her_main("Why can't this moment go on forever?", "soft", "base", "worried", "mid", cheeks="blush")
                m "We both know that everything has to come to an end..."
                m "But hopefully I've been able to teach you how to cherish every moment."
                ">Hermione tightens her arms even more as you continue the dance in silence."
                ">After a while, her grip loosens slightly as she shifts her head to look up at you."
                call her_main("I...", "open", "squint", "base", "mid", cheeks="blush")
                call her_main("I just wanted to say that...{w=0.5} I'm glad I have you.", "open", "happyCl", "worried", "mid", cheeks="blush")
                m "Where's this suddenly coming from Miss Granger?"
                call her_main("I don't know... it's just...", "upset", "happy", "base", "L", cheeks="blush")
                call her_main("I couldn't help having this bad feeling in my stomach the entire day.", "soft", "closed", "base", "stare", cheeks="blush")
                call her_main("It's stayed there up until now...{w} But now it's finally feeling as if the pain has started to go away...", "upset", "happy", "base", "R", cheeks="blush")
                ">Not knowing how to respond, you stand there in silence for a moment until Hermione pulls you towards her and you both begin moving along with the music once more."
                ">After what only feels like seconds the music comes to a close and Hermione takes a step back to look up at you."
                m "You look tired girl, you'd better head off to bed...{w=0.4} there's always tomorrow."
                call her_main("Oh, yes... I suppose so...", "soft", "base", "base", "mid", cheeks="blush")
                call her_main("Good night then...", "base", "happy", "base", "R", cheeks="blush")
                m "Good night."
                call her_main("Oh... wait,{w=0.3} before you go...", "open", "happyCl", "base", "mid", cheeks="blush")
                m "Yes?"
                call play_sound("kiss")
                with kissiris
                #Heart animation on screen?
                call her_main("...", "base", "narrow", "worried", "mid", cheeks="blush")
                g9 "What was that for?"
                call her_main("Nothing, I just felt like you earned it.", "base", "base", "base", "R", cheeks="blush")
                call her_main("See you tomorrow...", "base", "base", "worried", "mid", cheeks="blush")
                m "Good night Miss Granger."

                stop music fadeout 1
                call blkfade
                pause 3.0
                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                call hide_blkfade
                pause 1.0
                call play_sound("door")
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                m "Good night princess..."

                call blkfade

                jump day_start

label big_bang:
    show screen big_bang
    with Fade(0.7, 0.5, 0.7, color='#fff')
    play bg_sounds "sounds/rumble.mp3" fadein 2
    pause 3
    show screen big_bang(True)
    $ renpy.sound.play("sounds/bang.mp3")
    pause 1.5
    #with Move((0, 25), (0, -25), 0.2, bounce=True, repeat=True, delay=1.0)
    pause 12
    stop bg_sounds fadeout 2
    hide screen big_bang
    with d5
    return

screen big_bang(bang=False):
    zorder 10

    add Solid("#000")

    showif bang:
        add "images/misc/bang.webp":
            at transform:
                zoom 0.0
                anchor (0.5, 0.5)
                pos (540, 300)
                on show:
                    easeout 15.0 zoom 3
    else:
        add "glow_effect" zoom 0.2 anchor (0.5, 0.5) align (0.5, 0.5)
