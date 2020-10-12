
label hg_ps_buttplug:
    # Public shaming: Wear a butt plug
    hide screen hermione_main
    with d3

    if anal_plugs_ITEM.number == 0:
        m "{size=-4}(I should get some anal plugs first, then I could make her wear them...){/size}"
        jump hermione_favor_menu

    if hg_ps_buttplug.points == 0:
        m "{size=-4}(I could ask her to wear a butt plug around the school today.){/size}"

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu
    else:
        m "{size=-4}(I feel like making her walk around with a butt plug again!){/size}"



    m "{size=-4}(But which one?){/size}"
    label .plug_choice:
    menu:
        "-Small, regular-":
            $ buttplug_size = 1

        "-Medium, magical-":
            if hg_ps_buttplug.points >= 1:
                $ buttplug_size = 2
            else:
                m "(I don't think she's ready for that yet.)"
                jump .plug_choice

        "-Large, magical-":
            if buttplug_2_worn and her_whoring > 23:
                $ buttplug_size = 3
            else:
                m "(I don't think she's ready for that yet.)"
                jump .plug_choice

    $ current_payout = 55 # Default payout

    if not buttplug_1_worn and buttplug_size == 1:
        # First time with small butt plug
        m "[hermione_name], I want you to do something different today..."
        call her_main("...........", "soft", "base", "base", "mid",xpos="right",ypos="base")
        call nar(">You pull a large size butt plug out from under your desk and place it in front of her.")

        if her_whoring < 11:
            m "I want you to wear a butt plug around the school."
            jump too_much

        call her_main("and what is that supposed to be? Some sort of animals tail?", "open", "squint", "base", "mid")
        m "Not exactly, it's a butt plug. I want you to wear it while you attend class today."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}", "shock", "wide", "base", "stare")
        call play_music("chipper_doodle")
        call her_main("You expect me to put that massive thing in my...", "angry", "base", "angry", "mid")
        her "and then parade myself around the school!?"
        m "It just looks like a fake tail, No one will be able to tell what it really is."
        call her_main("{size=+5}That's not the point!{/size}", "scream", "closed", "angry", "mid")
        her "I'm not going to put that ridiculous thing anywhere near my butt!"
        call her_main("We are done here, [genie_name]!", "angry", "base", "angry", "mid",emote="angry")
        m "Alright, alright, calm down..."
        call her_main("I most certainly will not, [genie_name]! That thing is beyond absurd!", "scream", "closed", "angry", "mid")
        m "Alright, fine, maybe I underestimated how large it is..."
        call her_main("You think [genie_name]?! I'd like to see you try and fit it up your--", "angry", "base", "angry", "mid")
        m "alright, alright..."
        call her_main(".........", "annoyed", "narrow", "annoyed", "mid")
        m "How about we try one a little less... ambitious?"
        call her_main("............", "upset", "closed", "base", "mid")
        m "I'm willing to give Gryffindor fifty-five points."
        m "and All I ask for..."
        call her_main("..........?", "annoyed", "squint", "base", "mid")
        call nar(">You pull out a small butt plug from your desk.")
        m "is that you wear this to class..."
        call her_main("!!!", "angry", "base", "angry", "mid")
        m "Oh, come on... Just a harmless little baby one."
        call her_main("...", "disgust", "narrow", "base", "mid_soft")
        m "Fifty-five house points..."
        call her_main("..............", "annoyed", "narrow", "angry", "R")
        call her_main("Fine.", "annoyed", "narrow", "annoyed", "mid")
        m "Fantastic."
        m "Will you be putting it in now then?"
        call her_main("........", "annoyed", "narrow", "angry", "R")
        call her_main("I'll do it in the girls' bathroom, [genie_name]", "annoyed", "narrow", "angry", "R")
        m "*Hmm*... alright, I'll see you tonight then."

        $ buttplug_1_worn = True

    elif not buttplug_2_worn and buttplug_size == 2:
        # First time with medium butt plug
        m "[hermione_name], I want you to try something different today..."
        call her_main("...........", "soft", "base", "base", "mid",xpos="right",ypos="base")
        call nar(">You pull the medium size butt plug out from under your desk and place it in front of her.")

        if her_whoring <=15:
            m "I want you to wear this butt plug around the school."
            jump too_much

        call her_main("and what is this supposed to be?", "open", "squint", "base", "mid")
        m "Can't you tell it's a butt plug? They shouldn't be new to you at this point."
        call her_main("...", "annoyed", "narrow", "annoyed", "mid")
        call play_music("chipper_doodle")
        call her_main("Why does it have a such a large tail attached to it...", "annoyed", "base", "angry", "mid")
        her "you can't expect me to wear that around the school!"
        m "I can and do, unless you want our little trading game to come to a halt..."
        call her_main("but it's so long! everyone will be able to see it!", "normal", "happyCl", "worried", "mid")
        m "That's the point, [hermione_name]..."
        call her_main("...........", "angry", "happyCl", "worried", "mid",emote="sweat")
        call her_main("I want a hundred points.", "annoyed", "base", "angry", "mid")

        menu:
            "\"Fine, but I expect you to put it in now.\"":
                $ current_payout = 100
                call her_main("What? Right now!?.", "angry", "happyCl", "worried", "mid")
                call her_main("In front of you?", "angry", "wink", "base", "mid")
                m "One hundred points [hermione_name]..."
                call her_main("*Ugh*... Fine...", "angry", "narrow", "base", "down")
                call her_main("But I'm not turning around!", "annoyed", "narrow", "annoyed", "mid")
                m "Whatever suits you best..."
                ">You hand her the butt plug"
                call her_main("{size=-7}It's so big...{/size}", "clench", "narrow", "base", "down")
                ">Hermione lifts her skirt and presses the butt plug against her asshole."
                call her_main("*Ughh*... it's too big...", "shock", "happyCl", "worried", "mid")
                call her_main("It won't fit!", "open", "happyCl", "worried", "mid")
                m "Try spitting on it."
                call her_main(".........", "angry", "narrow", "base", "down")
                ">She spits on the end of the butt plug and tries to put it in again."
                call her_main("it doesn't work, It's just too bi--", "angry", "base", "base", "mid")
                stop music

                call set_hermione_plug("medium")

                with hpunch
                call her_main("{size=+5}!!!!{/size}", "shock", "wide", "base", "stare")
                call play_music("chipper_doodle")
                call her_main(".............", "angry", "base", "base", "mid")
                call her_main("...", "angry", "narrow", "base", "down")
                call her_main("well.... ah, I... better get to.... class... then...", "angry", "wink", "base", "mid")
                m "See you tonight [hermione_name]."

            "\"You'll get seventy points.\"":
                $ current_payout = 70
                call her_main("*Hmph*...", "annoyed", "narrow", "angry", "R")
                call her_main("Alright then, just don't expect me to show it to you!", "angry", "base", "angry", "mid")
                m "So long as you wear it to class then you'll get your seventy points."
                ">You hand her the butt plug."
                call her_main("Will that be all [genie_name]?.", "annoyed", "narrow", "annoyed", "mid")
                m "Yes [hermione_name], see you tonight."
                call her_main("{size=-5}(cheap bastard...){/size}", "annoyed", "narrow", "angry", "R")

        $ buttplug_2_worn = True

    else:
        # Third event
        if her_whoring <= 15 and buttplug_size == 1:
            # Small butt plug (first part)
            m "Today's favour shall be..."
            call her_main(".........", "angry", "base", "base", "mid",xpos="right",ypos="base")
            m "Wearing your favourite little butt plug to class!"
            call her_main("... again?", "angry", "narrow", "base", "down")
            m "Sure, why not?"
            m "And another fifty-five house points for the Gryffindor house of course."
            call her_main("..........", "annoyed", "base", "worried", "R")
            m "So... Are you okay with that, [hermione_name]?"
            call her_main("I suppose so...", "annoyed", "narrow", "angry", "R")
            ">You hand her the butt plug."
            m "Fantastic! See you after class."

        elif her_whoring <= 20 and buttplug_size == 1:
            # Small butt plug (second part)
            ">You pull out the large butt plug."
            m "Ready to try out the dragon yet?"
            stop music fadeout 1.0
            call her_main("What?", "scream", "wide", "base", "mid",xpos="right",ypos="base")
            call her_main("Of course not! That thing would tear me--", "scream", "closed", "angry", "mid")
            ">you pull out the small butt plug"
            m "How about this one then?"
            call her_main("Oh, okay then!", "smile", "happyCl", "base", "mid",emote="happy")
            m "You'll do it that easily?"
            call her_main("Well for fifty-five house points I'd be crazy not to.", "base", "closed", "base", "mid")
            call her_main("Plus I don't hate the way it feels", "open", "base", "base", "R")
            ">You hand her the butt plug."
            m "why don't you put it in now."
            call her_main("you want me to put it in now? in front of you!", "scream", "wide", "base", "mid")
            m "I don't see the harm in it."
            call her_main("well... it does save me having to visit the girls' bathroom before class...", "annoyed", "narrow", "worried", "down")
            call her_main("alright then, I'll do it... but I want an extra five points!", "smile", "base", "base", "R")
            m "Done."
            $ current_payout += 5
            call her_main("well... here goes.", "smile", "base", "base", "R")
            ">Hermione lifts her skirt and sticks it in rather slowly."

            call set_hermione_plug("small")

            call her_main("{heart}*ah*{heart}...", "grin", "narrow", "annoyed", "up")
            call her_main("i better head to class...", "soft", "happy", "base", "R")
            m "See you tonight [hermione_name]."
            call her_main("{size=-5}({heart}it feels so good{heart}){/size}", "grin", "narrow", "annoyed", "up")

        elif her_whoring >= 21 and buttplug_size == 1:
            # Small butt plug (final part)
            call play_music("chipper_doodle")
            m "[hermione_name]..."
            m "What do you think about wearing a butt pl--?"
            call her_main("I'll do it.", "grin", "base", "base", "R",xpos="right",ypos="base")
            m "You're eager."
            call her_main("well... I mean it is a lot of points and... I've sort of grown fond of how it feels...", "open", "narrow", "worried", "down")
            m "Great. Go have fun then!"
            ">You hand her the butt plug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."

            call set_hermione_plug("small")

            call her_main("{heart}ah{heart}...", "grin", "narrow", "annoyed", "up")
            call her_main("I will, [genie_name]. Thank you.", "base", "happyCl", "base", "mid")

        elif her_whoring <= 19 and buttplug_size == 2:
            # Medium butt plug (first part)
            m "Today my gracious request will be..."
            call her_main(".........", "angry", "base", "base", "mid",xpos="right",ypos="base")
            m "That you wear everyone's favourite magical butt plug to class!"
            call her_main("... again?", "angry", "narrow", "base", "down")
            m "why not? This will be the easiest fifty-five points you'll ever earn!"
            call her_main("..........", "annoyed", "base", "worried", "R")
            m "Do you have a problem with it, [hermione_name]?"
            call her_main("I suppose not...", "annoyed", "narrow", "angry", "R")
            ">You hand her the butt plug."
            m "Fantastic! See you after class."

        elif her_whoring <= 23 and buttplug_size == 2:
            # Medium butt plug (second part)
            ">You pull out the butt plug."
            m "Ready to try out the phoenix again?"

            if buttplug_2_question == False:
                $ buttplug_2_question = True

                call her_main("Oh, I suppose so...", "soft", "happy", "base", "R",xpos="right",ypos="base")
                call her_main("But is it alright if I ask you something first?", "open", "narrow", "worried", "down")
                m "What's that [hermione_name]"
                call her_main("Don't you worry about us getting caught?", "annoyed", "base", "base", "mid")
                m "Why would I?"
                call her_main("Well it's just that making me wear something like this is drawing a lot of attention...", "open", "base", "worried", "R")
                call her_main("and what if someone realises that it's you who's making me do all this...", "open", "base", "worried", "mid")
                m "And who is going to suspect the great {i}Albis Dumbledorf{/i}?"
                call her_main("... I suppose no one...", "annoyed", "base", "worried", "R")
                m "Then don't worry about it. If anyone asks just tell them you're going through an exhibitionist stage."
                m "Speaking of which..."
                ">You hand her the butt plug."
                call her_main("Oh... right...", "base", "narrow", "worried", "down")
                ">Hermione lifts her skirt and pushes it in gently, taking her time."

            else:
                call her_main("Oh, alright then...", "open", "narrow", "worried", "down",xpos="right",ypos="base")
                call her_main("but if you pay me and additional five points I'll turn around as I put it in...", "soft", "happy", "base", "R")
                menu:
                    "\"Done\"":
                        $ current_payout += 5
                        call her_main("thank you [genie_name], you won't regret it...", "open", "base", "base", "R")

                    "\"Fifty-five is all I can do.\"":
                        m "Any more and people might get suspicious."
                        call her_main("*Hmm*... I suppose you're right.", "annoyed", "narrow", "angry", "R")
                        call her_main("but as a present I'll show you anyway...", "base", "narrow", "worried", "down")
                        call her_main("although you better appreciate it...", "base", "squint", "base", "mid")
                        m "I'm sure I will."

                ">You hand her the butt plug."
                call her_main("well... here goes...", "base", "narrow", "worried", "down")
                ">Hermione turns around, lifts her skirt and pushes it in gently, taking her time."

            call set_hermione_plug("medium")

            call her_main("{heart}{heart}{heart}ah{heart}{heart}{heart}...", "grin", "narrow", "annoyed", "up")
            call her_main("i better... head to class... now...", "soft", "happy", "base", "R")
            m "See you tonight [hermione_name]."
            call her_main("{size=-5}({heart}it's... so... good...{heart}){/size}", "grin", "narrow", "annoyed", "up")

        elif her_whoring >= 24 and buttplug_size == 2:
            # Medium butt plug (final part)
            call play_music("chipper_doodle")
            m "[hermione_name]..."
            m "What do you think about wearing a butt pl--?"
            call her_main("I'll do it.", "grin", "base", "base", "R",xpos="right",ypos="base")
            m "You're eager. I haven't even said what one yet..."
            call her_main("oh... can it be the big one... with the long tail...", "open", "narrow", "worried", "down")
            call her_main("please...", "soft", "happy", "base", "R")
            m "well seeing as how you asked so nicely..."
            ">You hand her the butt plug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."

            call set_hermione_plug("medium")

            call her_main("{heart}ah{heart}...", "grin", "narrow", "annoyed", "up")
            call her_main("Thank you [genie_name]!", "open", "base", "base", "R")
            call her_main("{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}", "grin", "narrow", "annoyed", "up")

        elif not buttplug_3_worn and buttplug_size == 3:
            # Large buttplug first time
            call play_music("chipper_doodle")
            m "[hermione_name]..."
            m "What do you think about wearing a butt pl--?"
            call her_main("I'll do it.", "grin", "base", "base", "R",xpos="right",ypos="base")
            m "You're eager. I haven't even said which one yet..."
            call her_main("oh... can it be the big one... with the long tail...", "open", "narrow", "worried", "down")
            call her_main("please...", "soft", "happy", "base", "R")
            m "well seeing as how you did ask for the big one..."
            call nar(">You hand her the butt plug.")
            call her_main("!!!", "angry", "narrow", "base", "down")
            call her_main("This isn't the one I meant [genie_name]...", "angry", "narrow", "base", "down")
            m "Didn't you ask for the big one?"
            call her_main("I did--", "grin", "narrow", "annoyed", "up")
            m "Well here's the {b}big{/b} one."
            call her_main("I didn't know you had one this big!", "disgust", "narrow", "worried", "down")
            call her_main("I don't even think this will fit...", "disgust", "base", "base", "mid",cheeks="blush")
            m "Never say never!"
            call her_main("You can't be serious!", "scream", "narrow", "worried", "down")
            call her_main("This thing is ridiculous!", "open", "closed", "base", "mid")
            m "You said the same thing about the smaller one."
            call her_main("That was different...", "disgust", "narrow", "base", "down")
            m "I have confidence in you!"

            if hg_anal.trigger:
                g9 "Besides, you were pretty great when you were taking my cock up your ass!"

            call her_main("[genie_name]!", "shock", "wide", "base", "mid",cheeks="blush")
            m "Come on..."
            call her_main("This is too much sir! even your cock isn't this {b}thick{/b}...", "open", "narrow", "angry", "R")
            m "Nothing a little spit won't solve!"
            call her_main("Don't be ridiculous! This is beyond spit!", "open", "closed", "base", "mid")
            call her_main("Unless you have some sort of actual {i}lubricant{/i} in your possession, I don't think I'll be letting this thing anywhere near me...", "open", "base", "angry", "mid")

            menu:
                "-Use anal lube-" if anal_lube_ITEM.number > 0:
                    $ buttplug_3_worn = True
                    call play_music("playful_tension")
                    m "well it just so happens that I recently came across the solution to your problem."
                    call her_main("Which is?", "disgust", "wink", "base", "mid")
                    m "Here."

                    call give_gift(">You hand hermione the jar of anal lubricant.",anal_lube_ITEM)

                    call her_main("!!!", "clench", "wide", "base", "stare")
                    call her_main("I wasn't serious, [genie_name]!", "scream", "base", "angry", "mid")
                    m "Now, now. No one likes a liar."
                    call her_main("I didn't promise anything! Besides, I didn't actually expect you to have a jar of lube in your desk.", "open", "narrow", "angry", "R")
                    m "I bought it for just such an occasion..."
                    call her_main("...", "annoyed", "base", "angry", "mid")
                    call her_main("*Ugh*... fine. I'll {b}try{/b} to fit it in.", "disgust", "narrow", "worried", "down")
                    call her_main("but I'm not promising anything!", "open", "closed", "base", "mid")
                    m "That's all I ask."
                    call nar(">You hand hermione the large butt plug.")
                    call her_main("I still don't think this is going to work...", "open", "base", "base", "mid")
                    call nar(">Hermione slowly coats the massive butt plug with lube.")
                    call her_main("There's barely even enough here to cover it...", "open", "narrow", "worried", "down")
                    call her_main("(There's no way this thing will fit.)", "disgust", "narrow", "base", "down")
                    call nar(">Hermione slowly places the lubed up butt plug to her anus.")
                    call her_main("I'm telling you, [genie_name], this isn't going to--", "open", "closed", "base", "mid")
                    call her_main("{size=+10}!!!{/size}", "soft", "wide", "base", "stare",cheeks="blush",trans=hpunch)
                    call her_main("{size=+10}It's moving!{/size}", "disgust", "happyCl", "worried", "mid")
                    m "Really?"
                    call her_main("{size=+5}*Ugh*...{/size}", "disgust", "happyCl", "worried", "mid")
                    call her_main("{size=+5}it's forcing its way inside me....{/size}", "open", "wide", "worried", "shocked")
                    call her_main("ah...", "shock", "happyCl", "worried", "mid")
                    call her_main("it's...{w=0.3} it's...", "open", "wide", "base", "stare")

                    call play_sound("pop")

                    call set_hermione_plug("large")

                    call her_main("", "soft", "narrow", "annoyed", "up",cheeks="blush")
                    call ctc

                    call her_main("{size=+5}incredible!{/size}", "soft", "narrow", "annoyed", "up",cheeks="blush")

                    call her_main(".............", "disgust", "narrow", "annoyed", "up")
                    m "Are you alright, [hermione_name]?"
                    call her_main("..........................", "soft", "narrow", "base", "up")
                    call her_main("ah... y-yes...", "open", "narrow", "base", "mid_soft")
                    m "Fantastic! I'll see you after class then."
                    call her_main(".............", "disgust", "narrow", "worried", "down",cheeks="blush")
                    call nar(">Hermione slowly leaves your office, barely able to walk in a straight line.")

                "{color=[menu_disabled]}-Use anal lube-{/color}" if anal_lube_ITEM.number == 0:
                    m "I'm afraid I do not have that..."
                    call her_main("well then i think I better be off to class then.", "open", "closed", "base", "mid")
                    call her_main("{size=-2}unless {size=-2}you {size=-2}have {size=-2}the {size=-2}smaller {size=-2}one?{/size}{heart}", "soft", "narrow", "base", "R_soft",cheeks="blush")
                    g9 "It just so happens that I do!"
                    call nar(">You hand her a small butt plug.")

                    $ buttplug_size = 1
                    call set_hermione_plug("small")

                    call her_main("{heart}ah{heart}...", "silly", "narrow", "annoyed", "up")
                    call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")
                    call her_main("{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}", "soft", "narrow", "annoyed", "up")
                    hide screen hermione_main
                    with d3
                    pause.2
                    m "(Maybe those Weasley boys have anything that could help me with my.. *ahem* {i}her{/i} friction problem...)"

        elif buttplug_size == 3:
            # Large buttplug repeat
            call play_music("chipper_doodle")
            m "[hermione_name]..."
            m "how do you feel about wearing another butt plug to class today?"
            call her_main("...", "base", "base", "base", "R",xpos="right",ypos="base")
            call her_main("which one?", "grin", "base", "base", "mid")
            m "how about the big one again?"
            call her_main("really?", "open", "narrow", "worried", "down")
            call her_main("do i have to?", "soft", "happy", "base", "R")
            m "you didn't seem to hate wearing it last time..."
            call her_main("...", "open", "narrow", "worried", "down")
            call her_main("{size=-5}alright then...{/size}", "open", "narrow", "worried", "down")
            call nar(">You hand her the butt plug.","start")
            call nar(">You watch it magically worm it's way inside her eager butthole.","end")

            call set_hermione_plug("large")

            call her_main("{heart}ah{heart}ah...", "grin", "narrow", "annoyed", "up")
            call her_main("Thank you, [genie_name]!", "base", "narrow", "base", "mid_soft")
            call her_main("{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}", "soft", "narrow", "annoyed", "up")

    call her_walk(action="leave")

    $ hg_ps_buttplug.inProgress = True

    # Set the butt plug in case she didn't insert it during the event
    if buttplug_size == 1:
        call set_hermione_plug("small")
    elif buttplug_size == 2:
        call set_hermione_plug("medium")
    if buttplug_size == 3:
        call set_hermione_plug("large")

    jump end_hermione_event


label hg_ps_buttplug_complete:

    call her_walk(action="enter", xpos="mid", ypos="base")

    call bld
    if her_whoring <= 15 and buttplug_size == 1:
        if one_out_of_three == 1:
            # Got distracted
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle")
            show screen blktone
            $ sc34CG(1, 8)
            call her_main("It was awful... of course...", "annoyed", "squint", "angry", "mid",xpos="base",ypos="base")
            m "Just tell me what happened, [hermione_name]..."
            call her_main("I've never been so uncomfortable in my life [genie_name]!", "disgust", "narrow", "base", "mid_soft")
            call her_main("I wasn't able to focus on anything all day!", "annoyed", "narrow", "annoyed", "mid")
            m "Why's that?"
            call her_main("Whenever I was sitting down in class it just kept prodding me...", "annoyed", "narrow", "angry", "R")
            her "So naturally I had to adjust the way I was sitting, [genie_name]..."
            $ sc34CG(1, 9)
            call her_main("but that just made it worse...", "annoyed", "narrow", "angry", "R")
            m "Do you think anyone else noticed you?"
            call her_main("I've got no idea...", "annoyed", "narrow", "annoyed", "mid")
            $ sc34CG(1, 10)
            call her_main("I could hardly think straight... Let alone notice other people.", "annoyed", "narrow", "annoyed", "mid")
            m "So it felt good then?"
            call her_main("Good?", "open", "base", "base", "mid")
            $ sc34CG(1, 12)
            call her_main("If you call getting your... butt teased all day good...", "annoyed", "narrow", "worried", "down")
            call her_main("Then yes, I suppose it did...", "annoyed", "narrow", "annoyed", "up")
            $ sc34CG(1, 13)
            call her_main("Still... being this distracted during class could really damage my grades...", "angry", "base", "base", "mid")
            m "I wouldn't worry about that. Just think of Gryffindor!"
            hide screen sccg
            call her_main("Speaking of that...", "annoyed", "narrow", "annoyed", "mid", xpos="right",ypos="base",trans=fade)
            m "Oh yes, quite right."

        elif one_out_of_three == 2:
            # Flashed a few Ravenclaw girls by accident
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...", "open", "base", "base", "mid",xpos="right",ypos="base")
            call play_music("playful_tension")
            her "Barely anybody noticed that I was wearing it..."
            call her_main("... Except for a few girls from Ravenclaw...", "open", "base", "base", "mid",cheeks="blush")
            m "What happened?"
            call her_main("I was walking down the hall, on my way to potions class...", "open", "closed", "base", "mid")
            call her_main("And suddenly a gust of wind came and blew my skirt up...", "upset", "wink", "base", "mid")
            m "A gust of wind? inside?"
            call her_main("It must have been from a window...", "soft", "base", "base", "R")
            call her_main("Anyway the three girls walking behind me may have... seen it.", "open", "narrow", "worried", "down")
            m "Did they say anything to you?"
            call her_main("No... But I did hear them giggling afterwards...", "clench", "narrow", "base", "down")
            m "Well, it sounds like a job well done..."

        elif one_out_of_three == 3:
            # Caught by Moaning Myrtle
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle")
            show screen blktone
            call her_main("Awful, [genie_name]. Simply awful...", "scream", "happyCl", "worried", "mid",xpos="right",ypos="base")
            m "What happened?"
            call her_main("Moaning Myrtle happened!", "normal", "happyCl", "worried", "mid")
            m "{i}Moaning Mittle{/i}?"
            call her_main("That pesky little ghost!", "annoyed", "narrow", "angry", "R")
            call her_main("This thing left me so frustrated that in my free period I went to the girls toilets to...", "annoyed", "narrow", "angry", "R")
            call her_main("Relieve myself...", "annoyed", "base", "worried", "R")
            call her_main("When all of a sudden that annoying ghost poked her head through the door!", "scream", "closed", "angry", "mid")
            call her_main("As it if wasn't bad enough that she saw me...", "open", "narrow", "worried", "down")
            call her_main("She then started yelling \"Hermione has a butt plug\" to everyone in the toilets!", "scream", "base", "angry", "mid",emote="angry")
            call her_main("Luckily the stalls where empty! Imagine if they weren't!", "annoyed", "narrow", "annoyed", "mid")
            m "Well, it certainly sounds like you've earned your points."

    elif her_whoring <= 20 and buttplug_size == 1:
        if one_out_of_three == 1:
            # Flashed Luna in the library
            call play_music("chipper_doodle")
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Of course.", "open", "base", "base", "mid",xpos="right",ypos="base")
            m "Did anyone notice?"
            call her_main("Yes... well I might have...", "base", "narrow", "worried", "down")
            call her_main("shown someone...", "base", "narrow", "base", "mid_soft")
            her "I was in the library fetching some books when I saw Luna..."
            her "She was reading at a desk..."
            call her_main("So I decided to walk over to her and have a chat...", "grin", "base", "base", "R")
            call her_main("She was talking about something nonsensical...", "base", "base", "base", "R")
            her "And I figured that if she saw it..."
            her "no one would believe her..."
            m "alright..."
            call her_main("So I feigned dropping my quill...", "grin", "base", "base", "R")
            m "Go on..."
            call her_main("then I turned around in front of her...", "base", "narrow", "worried", "down")
            her "and bent over..."
            her "... keeping my knees straight..."
            call her_main("... giving her a full view...", "base", "narrow", "base", "up")
            m "I see..."
            m "Did she say anything?"
            call her_main("No, [genie_name]...", "soft", "happy", "base", "R")
            her "But when I turned back around she didn't make eye contact..."
            m "*Hmm*..."
            call her_main("I don't think I've seen anyone blush so hard...", "base", "narrow", "base", "mid_soft")
            m "Well it sounds like you've earned your points and then some."

        elif one_out_of_three == 2:
            # Couldn't focus and touched herself during class
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 9, 1)
            call her_main("I did, [genie_name]...", "open", "closed", "base", "mid",xpos="base",ypos="base")
            call her_main("Although I am still not sure how I feel about all of this...", "annoyed", "base", "worried", "R")
            $ sc34CG(1, 11, 1)
            call her_main("It's starting to really affect my grades...", "annoyed", "base", "worried", "R")
            call her_main("I couldn't even tell you what potions we were taught today...", "open", "base", "base", "mid")
            call play_music("playful_tension")
            call her_main("Me, Hermione Granger...", "open", "narrow", "worried", "down")
            $ sc34CG(1, 12, 1)
            call her_main("Not learning in class...", "angry", "narrow", "base", "down")
            m "Well you could try relieving yourself in between lessons."
            $ sc34CG(1, 13, 1)
            call her_main("Oh, I've tried that... but it doesn't work...", "angry", "base", "base", "mid")
            her "It just makes the next class harder..."
            $ sc34CG(1, 12, 1)
            call her_main("today, After potions I went to my room to... calm myself...", "open", "base", "base", "R")
            call her_main("But it just made Herbology worse...", "open", "narrow", "worried", "down")
            $ sc34CG(1, 11, 1)
            call her_main("I was forced into touching myself in the middle of class...", "clench", "narrow", "base", "down")
            call her_main("Do you think anyone noticed, [genie_name]?", "open", "happy", "base", "mid",cheeks="blush")
            $ sc34CG(1, 9, 1)

            menu:
                "\"What? Of course not, [hermione_name]!\"":
                    $ sc34CG(1, 8, 2)
                    call her_main("..............", "base", "base", "base", "R",cheeks="blush")
                    call her_main("You are right, [genie_name]...", "base", "narrow", "worried", "down")
                    her "I was very discreet..."
                    $ sc34CG(1, 12, 3)
                    call her_main("very quiet...", "soft", "narrow", "annoyed", "up")
                    call her_main("barely making a sound...", "grin", "base", "base", "R")
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?", "base", "narrow", "base", "mid_soft",xpos="right",ypos="base",trans=fade)
                    her "......"

                "\"Of course they did!\"":
                    $ sc34CG(1, 13, 2)
                    m "Do you honestly believe that no one noticed you touching yourself?"
                    call her_main("I was afraid that you would say that, [genie_name]...", "mad", "happyCl", "worried", "mid",tears="soft_blink")
                    m "You were surrounded by people!"
                    call her_main("........", "mad", "happyCl", "worried", "mid",tears="soft_blink")
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?", "angry", "base", "base", "mid",tears="soft",xpos="right",ypos="base",trans=fade)

            m "Certainly."

        elif one_out_of_three == 3:
            # Nothing happened
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 11)
            call her_main("Yes, [genie_name]. I did.", "open", "closed", "base", "mid",xpos="base",ypos="base")
            m "Great. Tell me more."
            call play_music("playful_tension")
            call her_main("Well, there's not much to tell...", "open", "base", "base", "mid")
            $ sc34CG(1, 12)
            her "I attended classes..."
            her "tried to take notes."
            her "all in all it was a fairly regular day..."
            $ sc34CG(1, 13)
            call her_main("Well as regular as it could have been with a plug up my butt.", "annoyed", "narrow", "angry", "R")
            m "and Nobody noticed?"
            call her_main("I don't think so, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
            $ sc34CG(1, 11)
            m "Well I suppose something interesting can't happen everyday."
            hide screen sccg
            call her_main("...", "annoyed", "base", "base", "R",xpos="right",ypos="base",trans=fade)


    elif her_whoring >= 21 and buttplug_size == 1:
        if one_out_of_three == 1:
            # Pleasured herself in class
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].", "base", "base", "base", "mid",xpos="right",ypos="base")
            m "Well? How was your day?"
            call her_main("great, [genie_name]...", "base", "narrow", "base", "up")
            m "go on..."
            call play_music("playful_tension")
            $ sc34CG(1, 14, 1)
            call her_main("Well I've worked out how to deal with this thing being in me all day...", "soft", "happy", "base", "R",xpos="base",ypos="base")
            m "Really? And how is that?"
            call her_main("before now I've been going around it the wrong way...", "open", "base", "base", "R")
            call her_main("I just tried to ignore it...", "open", "closed", "base", "mid")
            her "and pay attention in class..."
            call her_main("But that didn't work at all...", "upset", "wink", "base", "mid")
            call her_main("I was just too... distracted...", "base", "narrow", "worried", "down")
            $ sc34CG(1, 15, 2)
            call her_main("So I thought to myself that I've just got to focus on it...", "base", "narrow", "base", "up")
            $ sc34CG(1, 16, 3)
            call her_main("block out everything else...", "base", "narrow", "worried", "down")
            $ sc34CG(1, 17, 2)
            call her_main("... embrace it...", "grin", "narrow", "base", "dead")
            m "and how did you do that?"
            call her_main("well if I rock my hips while I'm sitting in class it's almost enough...", "base", "narrow", "base", "mid_soft")
            $ sc34CG(1, 16, 3)
            call her_main("but if I sit of the edge of my chair while I rock my hips...", "base", "squint", "base", "mid")
            $ sc34CG(1, 17, 2)
            call her_main("{heart}{heart}{heart}", "soft", "narrow", "annoyed", "up")
            m "So you worked out how to pleasure yourself in class."
            call her_main("I did [genie_name].", "base", "narrow", "worried", "down")
            her "Although I worry that it will really start to affect my grades..."
            m "Well I'm sure that missing one class a day is something you can catch up on."
            $ sc34CG(1, 15, 2)
            call her_main("only One?", "angry", "wink", "base", "mid")
            m "You mean to say that you spent all your class time pleasuring yourself?"
            $ sc34CG(1, 17, 2)
            call her_main("..........", "soft", "narrow", "annoyed", "up")
            hide screen sccg
            call her_main(xpos="right",ypos="base",trans=fade)
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2:
            # Colin Creevey took an upskirt photo
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].", "base", "base", "base", "mid", xpos="right", ypos="base")
            call her_main("But, *umm*...", "open", "base", "worried", "mid")
            m "...?"
            call her_main("Well, I may have gotten a bit more attention than I had hoped for...", "disgust", "narrow", "base", "down")
            call her_main("...............", "clench", "narrow", "base", "down")
            m "Tell me what happened, [hermione_name]."
            call play_music("playful_tension")
            call her_main("I might have had a few photos taken...", "open", "narrow", "worried", "down")
            m "Photos..."
            call her_main("Well I was in the library minding my own business...", "annoyed", "closed", "base", "mid")
            her "When I went to get a copy of Zygmunt Budge's book of potions."
            call her_main("as it was on the bottom shelf I had to kneel down to reach it...", "annoyed", "base", "base", "mid")
            call her_main("When all of a sudden I heard the flash of a camera!", "annoyed", "narrow", "angry", "R")
            her "I turned around and there was Colin Creevey..."
            her "with the biggest grin on his face!"
            m "You let your photo be taken?!"
            call her_main("I didn't let anything of the sort happen! It was without my consent!", "scream", "base", "angry", "mid", emote="angry")
            call her_main("I even made him promise not to show anyone the photo...", "open", "narrow", "worried", "down")
            her "... in exchange I did have to let him take a few more..."
            her "but he insisted that he wouldn't show anyone else..."
            m "And you believe him?"
            call her_main("Of course [genie_name], he's a Gryffindor.", "annoyed", "closed", "base", "mid")
            call her_main("Although the thought did cross my mind.", "open", "narrow", "worried", "down")
            call her_main("What if he were to distribute the photos around the school.", "clench", "narrow", "base", "down")
            call her_main("Imagine everyone looking at photos of me...", "open", "base", "base", "R")
            her "Everyone would know what I was wearing..."
            call her_main("Any time someone saw me they'd think about whether or not it was in...", "base", "narrow", "worried", "down")
            m "That's quite the thought process."
            call her_main("Yes, well I certainly don't want that to happen...", "base", "squint", "base", "mid")
            m "I'm sure..."
            call her_main("", "base", "narrow", "base", "mid_soft")
            m "It sounds like a job well done [hermione_name]."

        elif one_out_of_three == 3:
            # Flashed students on her way to class
            call play_music("chipper_doodle")
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...", "base", "squint", "base", "mid", xpos="right", ypos="base")
            m "Did anyone notice?"
            her "maybe a few third years..."
            m "well go on."
            call her_main("It was the stairs...", "base", "narrow", "base", "mid_soft")
            her "I may have gotten a little carried away with myself..."
            m "What happened, [hermione_name]?"
            call her_main("Well as I was walking to divination class I ended up in front of a group of third year students...", "base", "squint", "base", "mid")
            call her_main("And seeing as how they were behind me on the stairs they may have been able to... see it.", "base", "narrow", "base", "mid_soft")
            m "So you intentionally showed it to a group of boys? You don't expect me to grant you extra points for showing them, do you?"
            call her_main("Of course not, [genie_name].", "base", "base", "base", "R", cheeks="blush")
            m "Then why do it?"
            call her_main("Well, it just sort of just happened...", "open", "happy", "base", "mid", cheeks="blush")
            call her_main("plus the look on their faces when they noticed it...", "grin", "narrow", "base", "dead")
            call her_main("they could barely hide their...", "soft", "narrow", "annoyed", "up")
            m "So you like being seen then?"
            call her_main("well...", "open", "base", "base", "R")
            m "Well done, [hermione_name]."
            call her_main("", "base", "narrow", "worried", "down")

    elif her_whoring <= 19 and buttplug_size == 2:
        if one_out_of_three == 1:
            # Stood in front during potions class
            m "[hermione_name], how was it?"
            call play_music("chipper_doodle")
            show screen blktone
            call her_main("It was awful... simply awful...", "annoyed", "squint", "angry", "mid",xpos="right",ypos="base")
            m "what happened, [hermione_name]..."
            call her_main("It was that nasty professor Snape, [genie_name]!", "annoyed", "narrow", "angry", "R")
            call her_main("I've never been so embarrassed in my life!", "annoyed", "narrow", "annoyed", "mid")
            m "What did he do?"
            call her_main("Well in potions class I may have corrected him about the proper way to crush a Sopophorous bean...", "annoyed", "narrow", "angry", "R")
            her "so he made me stand out the front and show him the \"correct\" way..."
            call her_main("and what's worse is that he made me do it facing away from the class...", "annoyed", "narrow", "annoyed", "mid")
            m "Do you think anyone saw it?"
            call her_main("Everyone saw it!", "disgust", "narrow", "base", "down")
            call her_main("I could barely even crush the bean my legs were shaking that hard...", "clench", "narrow", "base", "down")
            m "Well it sounds like you earned your points."
            call her_main(".......", "annoyed", "narrow", "worried", "down")

        elif one_out_of_three == 2:
            # Flashed some Hufflepuffs
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...", "open", "base", "base", "mid",xpos="right",ypos="base")
            call play_music("playful_tension")
            her "A group of second years from Hufflepuff even complimented me on it..."
            call her_main("... they said that it looked cute...", "grin", "base", "base", "R")
            m "did anything else happen?"
            call her_main("well seeing as how they were so nice...", "base", "narrow", "worried", "down")
            call her_main("I might have flicked my skirt up for them...", "soft", "happy", "base", "R")
            m "you showed it to them?"
            call her_main("well they were so kind...", "open", "base", "base", "R")
            call her_main("and they could already see most of it...", "base", "narrow", "worried", "down")
            m "Did they say anything to you?"
            call her_main("No... But the looks on their faces...", "base", "narrow", "base", "mid_soft")
            m "Well, it sounds like a job well done..."

        elif one_out_of_three == 3:
            # Cat swatting it
            label buttplug_magic_show:
            $ buttplug_magic_known = True
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle")
            show screen blktone
            call her_main("what on earth did you do to this thing?!", "scream", "happyCl", "worried", "mid",xpos="right",ypos="base")
            m "What happened?"
            call her_main("Why did you not tell me this \'thing\' was cursed!", "normal", "happyCl", "worried", "mid")
            m "Cursed?"
            call her_main("It vibrates!", "annoyed", "narrow", "angry", "R")
            m "Really? When?"
            call her_main("when something else touches it...", "annoyed", "narrow", "angry", "R")
            m "Wouldn't your skirt set it off then?"
            call her_main("I think it has to be alive...", "annoyed", "base", "worried", "R")
            call her_main("All I know is that when my cat Crookshanks swatted at it went off!", "scream", "closed", "angry", "mid")
            m "How bad was it?"
            call her_main("It was ridiculous! I was barely able to stand...", "open", "happyCl", "worried", "mid")
            call her_main("but then Crookshanks thought it was some sort of game... he wouldn't leave it alone...", "shock", "happyCl", "worried", "mid")
            call her_main("the vibrations were so intense that my knees gave out and I collapsed onto my bed!", "angry", "narrow", "base", "down")
            call her_main("then he just played with it for hours...", "angry", "wink", "base", "mid")
            m "are you still up for wearing it in the future?"
            call her_main("I suppose... So long as I know how it works now.", "upset", "closed", "base", "mid")
            call her_main("I'll just have to keep it away from Crookshanks...", "angry", "narrow", "base", "down")
            call her_main("{size=-6}or not...{/size}", "soft", "narrow", "annoyed", "up")
            m "Well good work then [hermione_name]"

    elif her_whoring <= 23 and buttplug_size == 2:
        if one_out_of_three == 1:
            # Luna played with it in the library
            if not buttplug_magic_known:
                jump buttplug_magic_show
            call play_music("chipper_doodle")
            m "[hermione_name], did you have fun?"
            show screen blktone
            call her_main("I suppose you could say that.", "base", "narrow", "worried", "down",xpos="right",ypos="base")
            m "Anything interesting happen?"
            call her_main("Yes... well I might have...", "base", "narrow", "worried", "down")
            call her_main("had someone...", "base", "happyCl", "worried", "mid")
            call her_main("touch it...", "base", "narrow", "base", "mid_soft")
            m "*Hmm*..."
            call her_main("It was Luna Lovegood again.", "grin", "base", "base", "R")
            call her_main("We ended up sitting next to each other in class.", "soft", "base", "base", "R")
            her "we were talking about school, clothes..."
            m "Yes, yes, spit it out..."
            call her_main("well she said that she thought my tail was cute...", "grin", "base", "base", "R")
            m "Go on..."
            call her_main("then she asked so politely if she could touch it...", "base", "narrow", "worried", "down")
            call her_main("I could hardly say no...", "open", "base", "base", "R")
            call her_main("so I... let her spend the rest of the lesson... playing with it...", "soft", "happy", "base", "R")
            m "I see..."
            m "Did she realise what was happening?"
            call her_main("maybe... it felt so good that it was hard to keep it hidden.", "soft", "narrow", "annoyed", "up")
            her "But I think that just made her want to touch it more..."
            m "*Hmm*..."
            call her_main("I don't think I've ever had a better lesson...", "grin", "narrow", "base", "dead")
            m "Well it sounds like you've earned your points and then some."

        elif one_out_of_three == 2:
            # Ginny played with it
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name].", "open", "closed", "base", "mid",xpos="right",ypos="base")
            call her_main("Only... *Ehm*...", "grin", "base", "base", "R")
            m "What is it this time [hermione_name]?"
            call her_main("Well... you know my friend...", "base", "base", "base", "mid")
            her "Ginny Weasley..."
            call her_main("well I told her about the tail...", "base", "base", "base", "R",cheeks="blush")
            her "and how it worked and well..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip Herbology class together...", "open", "base", "base", "R")
            call play_music("playful_tension")
            call her_main("And then she sort of grabbed it...", "grin", "narrow", "annoyed", "up")
            call her_main("And she just played with it so aggressively...", "grin", "narrow", "base", "dead")
            her "I was a mess afterwards..."
            g9 "And did you return the favour?"

            if hg_pr_kiss.counter >= 1:
                call her_main("Err... maybe...", "open", "happy", "base", "mid",cheeks="blush")
                m "What did you do?"
                call her_main("well I don't want to say too much [genie_name].", "base", "base", "base", "R",cheeks="blush")
                her "but after she saw what it was doing to me..."
                her "she insisted that I let her have a go..."
                call her_main("and that's all I'll say...", "base", "narrow", "worried", "down")
                m "*Hmm*... I suppose you've earned your points [hermione_name], even if you are secretive about it..."
            else:
                call her_main("... No.", "open", "narrow", "worried", "down")
                m "Why not?"
                call her_main("well I don't mind letting her touch the tail [genie_name].", "annoyed", "base", "base", "mid")
                her "but anything else..."
                m "Very good [hermione_name]..."

        elif one_out_of_three == 3:
            # Called a slut by Slytherin girls
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, [genie_name]. I did.", "annoyed", "narrow", "angry", "R",xpos="right",ypos="base")
            m "Great. Tell me more."
            call play_music("playful_tension")
            call her_main("Well, there's not much to tell...", "open", "narrow", "worried", "down")
            her "I attended classes..."
            her "studied for the upcoming potions exam..."
            call her_main("it was a normal day except for a group of those nasty slytherin tramps...", "annoyed", "narrow", "angry", "R")
            call her_main("I was minding my business on the way to class when they called me a \"butt slut\".", "angry", "narrow", "base", "down")
            m "did you say anything back to them?"
            call her_main("and sink to their level...", "annoyed", "narrow", "angry", "R")
            m "Well I suppose it's for the best."


    elif her_whoring >= 24 and buttplug_size == 2:
        if one_out_of_three == 1:
            # Groped by first years
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].", "scream", "closed", "angry", "mid",xpos="right",ypos="base")
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...", "annoyed", "base", "angry", "mid")
            m "you were attacked by first years?"
            call play_music("playful_tension")
            call her_main("I may have been exaggerating slightly...", "open", "base", "worried", "R")
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...", "annoyed", "narrow", "angry", "R")
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...", "angry", "happyCl", "worried", "mid")
            call her_main("\"is it fluffy\"...", "annoyed", "narrow", "angry", "R")
            call her_main("\"why are you wearing it\"...", "angry", "narrow", "base", "down")
            call her_main("\"does it feel nice\"...", "base", "narrow", "worried", "down")
            call her_main("\"can we touch it\"...", "base", "narrow", "worried", "down")
            call her_main("\"can you make it wag\"...", "angry", "wink", "base", "mid")
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...", "upset", "closed", "base", "mid")
            call her_main("but in exchange I may have had to let them touch it...", "open", "narrow", "worried", "down")
            call her_main("{heart}{heart}{heart}", "soft", "narrow", "annoyed", "up")
            m "So you let a group of innocent first years touch your butt plug..."
            call her_main("It sounds sinister when you put it like that.", "annoyed", "narrow", "angry", "R")
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......", "base", "narrow", "worried", "down")
            m "So did you enjoy it?"
            call her_main("..........", "angry", "base", "base", "mid")
            call her_main("Truthfully [genie_name].... It was one of the most pleasurable experiences of my life...", "grin", "narrow", "base", "dead")
            call her_main("all their hands touching it...", "soft", "narrow", "annoyed", "up")
            call her_main("taking turns...", "grin", "narrow", "annoyed", "up")
            call her_main("all the while it was vibrating away...", "base", "narrow", "worried", "down")
            call her_main("I nearly passed out.", "silly", "narrow", "base", "dead")
            call her_main("I even tried to make them stop...", "silly", "narrow", "annoyed", "up")
            call her_main("but they just kept going...", "grin", "narrow", "annoyed", "up")
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2:
            # Glory hole with Astoria
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...", "base", "base", "base", "mid",xpos="right",ypos="base")
            call her_main("Did you know there are holes between the stalls in the girls' bathroom?", "soft", "base", "base", "mid")
            m "i did not, but What does that have to do with your butt plug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...", "grin", "base", "base", "R")
            call her_main("...............", "grin", "happyCl", "worried", "mid")
            m "go on, [hermione_name]."
            call play_music("playful_tension")
            call her_main("I might have put it through...", "base", "narrow", "worried", "down")
            m "what?"
            call her_main("Well I was in the stall finishing up...", "base", "base", "base", "R")
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a slytherin...", "upset", "wink", "base", "mid")
            call her_main("So I decided to press my cheeks to the wall and stick my tail through!", "smile", "base", "base", "R")
            m "did they touch it?"
            call her_main("not immediately...", "base", "base", "base", "R")
            call her_main("but after I gave it a little wiggle she eventually came around...", "grin", "base", "base", "R")
            call her_main("she was curious at first but eventually she started to really play with it...", "open", "base", "base", "R")
            call her_main("stroking it... flicking it... I even think she may have licked it...", "soft", "narrow", "annoyed", "up")
            her "... imagine that... a Slytherin, licking something that was inside my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].", "open", "base", "worried", "mid")
            call her_main("It was at lunch, in the great hall.", "open", "closed", "base", "mid")
            call her_main("I was walking past the Slytherin table on my way to sit down...", "open", "closed", "base", "mid")
            call her_main("when I saw that little... vixen, Astoria Greengrass.", "base", "squint", "base", "mid")
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... Astoria Greengrass... pure-blood, licking my...", "grin", "narrow", "annoyed", "up")
            call her_main("{heart}........{heart}", "soft", "narrow", "annoyed", "up")
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}", "base", "narrow", "worried", "down")

        elif one_out_of_three == 3:
            call play_music("chipper_doodle")
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...", "base", "squint", "base", "mid",xpos="right",ypos="base")
            m "Anything interesting happen?"
            her "Do you know the Patil twins [genie_name]?"
            m "*Err*..."
            call her_main("well they were walking down the hall behind me...", "base", "narrow", "base", "mid_soft")
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...", "base", "squint", "base", "mid")
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...", "base", "narrow", "base", "mid_soft")
            m "You exposed yourself just like that?"
            call her_main(".......", "base", "base", "base", "R",cheeks="blush")
            m "Very good, [hermione_name]!"

    elif buttplug_size == 3:
        if one_out_of_three == 1:
            # Groped by first years again...
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].", "scream", "closed", "angry", "mid",xpos="right",ypos="base")
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...", "annoyed", "base", "angry", "mid")
            m "you were attacked by first years?"
            call play_music("playful_tension")
            call her_main("I may have been exaggerating slightly...", "open", "base", "worried", "R")
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...", "annoyed", "narrow", "angry", "R")
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...", "angry", "happyCl", "worried", "mid")
            call her_main("\"is it fluffy\"...", "annoyed", "narrow", "angry", "R")
            call her_main("\"why are you wearing it\"...", "angry", "narrow", "base", "down")
            call her_main("\"does it feel nice\"...", "base", "narrow", "worried", "down")
            call her_main("\"can we touch it\"...", "base", "narrow", "worried", "down")
            call her_main("\"can you make it wag\"...", "angry", "wink", "base", "mid")
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...", "upset", "closed", "base", "mid")
            call her_main("but in exchange I may have had to let them touch it...", "open", "narrow", "worried", "down")
            call her_main("{heart}{heart}{heart}", "soft", "narrow", "annoyed", "up")
            m "So you let a group of innocent first years touch your butt plug..."
            call her_main("It sounds sinister when you put it like that.", "annoyed", "narrow", "angry", "R")
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......", "base", "narrow", "worried", "down")
            m "So did you enjoy it?"
            call her_main("..........", "angry", "base", "base", "mid")
            call her_main("Truthfully [genie_name].... It was one of the most pleasurable experiences of my life...", "grin", "narrow", "base", "dead")
            call her_main("all their hands touching it...", "soft", "narrow", "annoyed", "up")
            call her_main("taking turns...", "grin", "narrow", "annoyed", "up")
            call her_main("all the while it was vibrating away...", "base", "narrow", "worried", "down")
            call her_main("I nearly passed out.", "silly", "narrow", "base", "dead")
            call her_main("I even tried to make them stop...", "silly", "narrow", "annoyed", "up")
            call her_main("but they just kept going...", "grin", "narrow", "annoyed", "up")
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2:
            # Speech in McGonagall's class
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...", "base", "base", "base", "mid", xpos="right", ypos="base")
            call her_main("Did you know there are holes between the stalls in the girls' bathroom?", "soft", "base", "base", "mid")
            m "i did not, but What does that have to do with your butt plug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...", "grin", "base", "base", "R")
            call her_main("...............", "grin", "happyCl", "worried", "mid")
            m "go on, [hermione_name]."
            call play_music("playful_tension")
            call her_main("I might have put it through...", "base", "narrow", "worried", "down")
            m "what?"
            call her_main("Well I was in the stall finishing up...", "base", "base", "base", "R")
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a slytherin...", "upset", "wink", "base", "mid")
            call her_main("So I decided to stick my tail through!", "smile", "base", "base", "R")
            m "did they touch it?"
            call her_main("not immediately...", "base", "base", "base", "R")
            call her_main("but after I gave it a little wiggle she eventually came around...", "grin", "base", "base", "R")
            call her_main("she was curious at first but eventually she started to really play with it...", "open", "base", "base", "R")
            call her_main("stroking it... flicking it... I even think she may have licked it...", "soft", "narrow", "annoyed", "up")
            her "... imagine that... a Slytherin, licking something that was in my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].", "open", "base", "worried", "mid")
            call her_main("It was at lunch, in the great hall.", "open", "closed", "base", "mid")
            call her_main("I was walking past the Slytherin table on my way to sit down...", "open", "closed", "base", "mid")
            call her_main("when I saw that little... vixen, Astoria Greengrass.", "base", "squint", "base", "mid")
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... Astoria Greengrass... pure-blood, licking my...", "grin", "narrow", "annoyed", "up")
            call her_main("{heart}........{heart}", "soft", "narrow", "annoyed", "up")
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}", "base", "narrow", "worried", "down")

        elif one_out_of_three == 3:
            # Sits down in hall with it showing
            call play_music("chipper_doodle")
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...", "base", "squint", "base", "mid",xpos="right",ypos="base")
            m "Anything interesting happen?"
            her "Do you know the Patil twins [genie_name]?"
            m "*Err*..."
            call her_main("well they were walking down the hall behind me...", "base", "narrow", "base", "mid_soft")
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...", "base", "squint", "base", "mid")
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...", "base", "narrow", "base", "mid_soft")
            m "You exposed yourself just like that?"
            call her_main(".......", "base", "base", "base", "R",cheeks="blush")
            m "Very good, [hermione_name]!"

    $ gryffindor += current_payout
    m "The Gryffindor house gets {number=current_payout} points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave")

    $ hg_ps_buttplug.counter += 1
    $ hg_ps_buttplug.points += 1
    $ hg_ps_buttplug.inProgress = False

    call set_hermione_plug(None)

    jump end_hermione_event


default hermione_plug_img = "blank"

label set_hermione_plug(size):
    if size in ("small", "medium", "large"):
        $ hermione_plug_img = "characters/hermione/clothes/plugs/{}.webp".format(size)
    else:
        $ hermione_plug_img = "blank"
