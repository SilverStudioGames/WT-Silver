
# Luna (converted) strip for me
label luna_favour_3:

    # Setup
    if lun_whoring < 9:
        $ lun_whoring += 1

    if lun_whoring > 14:
        # Jump to blowjob with Hermione
        # Note: Prevents player from replaying the strip event, also dialogue doesn't flow well
        m "how do you feel about stripping?"
        call lun_main("really?","normal","angry","angry","mid")
        call lun_main("Aren't we a little past that?","normal","mad","raised","mid")
        m "What would you rather do then?"
        call lun_main("...","normal","seductive","angry","R")
        call lun_main("how about another blowjob?","base","seductive","angry","mid")
        m "Well then..."
        jump luna_favour_6

    call play_music("chipper_doodle")

    if lun_whoring < 8:
        if lun_sub > lun_dom:
            if lun_whoring == 6: # First time
                m "Have you ever been naked in front of another person [lun_name]?"
                call lun_main("What?","normal","base","sad","down")
                call lun_main("Well... um... not really, I suppose.","normal","base","sad","R")
                m "Well then there's a first time for everything!"
            else:
                m "How would you like to step out of those restrictive clothes, [lun_name]?"
                call lun_main("...","normal","base","sad","down")
                call lun_main("Well... {size=-3}they're{/size} {size=-4}not{/size} {size=-5}really{/size} {size=-6}that{/size} {size=-7}restrictive.{/size}","normal","base","sad","R")
                m "..."
                call lun_main("Alright then, [lun_genie_name]...","upset","base","sad","down")
            hide screen luna_main
            with d3
            call lun_walk("desk")
            call lun_main("...","upset","base","sad","R", xpos=270)
        else:
            m "You don't mind taking some of your clothes off, do you [lun_name]?"
            call lun_main("I suppose not...","normal","base","angry","R")
            call lun_main("So long as you're prepared to show some {i}appreciation...{/i}","normal","angry","angry","mid")
            m "Yes, [lun_name]..."
            call lun_main("... pervert...","normal","angry","angry","R")
            hide screen luna_main
            with d3
            $ luna_xpos = 270
            call lun_walk("desk")
            call lun_main("...","normal","angry","angry","R")

        menu:
            "\"Take off your skirt.\"" if lun_sub >= 5:
                $ luna_choice = 1
                call lun_main("you want me to take off my skirt!?","pout","wide","sad","mid")
                m "Yes... You think you could manage that?"
                call lun_main("of course I can manage--","normal","angry","sad","R")
                m "Fantastic! Why don't you pop it off then so we can take a look..."
                call lun_main("...","normal","closed","sad","down")
                call lun_main("Fine... (I hope he doesn't expect me to take off my panties as well)","pout","angry","sad","down")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_bottom = False
                call update_lun_uniform
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on your desk."
                show screen luna_main
                hide screen blkfade
                with d3

                call lun_main("There... are you happy now [lun_genie_name]?","upset","mad","sad","down")
                m "Almost... take off your shirt next."
                call lun_main("... alright...","clench","suspicious","sad","R")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_top = False
                call update_lun_uniform
                ">Luna starts to unbutton her shirt..."
                ">She fumbles with the buttons until finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of her skirt."
                show screen luna_main
                hide screen blkfade
                with d3

            "\"Take off your shirt.\"" if lun_sub > lun_dom:
                $ luna_choice = 2
                call lun_main("my shirt?","normal","angry","sad","mid")
                m "Did I stutter, [lun_name]?"
                call lun_main("no...","normal","mad","sad","R")
                m "Well, why don't you take it off then so we can take a look..."
                call lun_main("...","upset","suspicious","sad","down")
                call lun_main("Fine... (I hope he doesn't expect me to take off my bra as well)","normal","angry","sad","R")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_top = False
                call update_lun_uniform
                ">Luna starts to unbutton her shirt..."
                ">She fumbles with the buttons until finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of your desk."
                show screen luna_main
                hide screen blkfade
                with d3
                call ctc

                call lun_main("There... are you happy now, [lun_genie_name]?","normal","suspicious","sad","mid")
                m "Almost... take off your skirt next."
                call lun_main("... fine...","normal","angry","sad","R")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_bottom = False
                call update_lun_uniform
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on top of her shirt."
                show screen luna_main
                hide screen blkfade
                with d3

            "\"Please take off your shirt.\"" if lun_dom >= lun_sub:
                $ luna_choice = 3
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("well, seeing as how you said the magic word, I suppose it's only fair...","base","suspicious","base","R")
                m "thank you, [lun_name]."
                call lun_main("(Who'd have thought it'd be this easy...)","base","angry","base","R")
                call lun_main("close your eyes...","normal","mad","angry","mid")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_top = False
                call update_lun_uniform
                ">you can hear the soft ruffle of clothes being removed..."
                ">You hear her softly place her shirt and vest on the table..."
                m "..."
                m "Can I open my eyes yet, [lun_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna_main
                hide screen blkfade
                with d3
                call ctc

            "\"Please take off your skirt [lun_name]...\"" if lun_dom >= 5:
                $ luna_choice = 4
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("well seeing as how you said the magic word I suppose it's only fair...","base","suspicious","base","R")
                m "thank you, [lun_name]."
                call lun_main("(Who'd have thought it'd be the easy...)","base","angry","base","R")
                call lun_main("well... close your eyes...","normal","angry","angry","mid")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_bottom = False
                call update_lun_uniform
                ">you can hear the soft ruffle of clothes and zips..."
                ">You hear her softly place her skirt on the table..."
                m "..."
                m "Can I open my eyes yet, [lun_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna_main
                hide screen blkfade
                with d3
                call ctc

        if luna_choice <= 2: #luna sub choices
            if lun_sub <= 5:
                $ lun_sub += 1
            m "Good... now your underwear..."
            call lun_main("!!!","normal","wide","sad","mid")
            call lun_main("You're not serious are you?","normal","angry","sad","R")
            m "I am. And I expect you to do it now, [lun_name]."
            call lun_main("[lun_genie_name]!","upset","mad","mad","mid")
            m "don't you raise your voice at me, [lun_name]!"
            call lun_main(".....!!?","normal","angry","sad","R")
            m "Nobody is forcing you to do this."
            call lun_main("but--","normal","seductive","sad","R")
            m "I am doing you and your family a favour!"
            m "so If you don't think your father needs help with his failing magazine, please feel free to leave."
            call lun_main(".....................","upset","suspicious","sad","R")
            call lun_main(".....................","normal","angry","sad","down")
            call lun_main("please [lun_genie_name]...","normal","mad","sad","mid",tears="soft")
            call lun_main("isn't there anything else I can do?","normal","suspicious","sad","R",tears="soft")

            menu:
                "-Make her strip-" if luna_choice == 1:
                    $ current_payout = 40
                    m "Take off your underwear now, [lun_name]..."
                    call lun_main("{size=-5}(Should I really do this?){/size}","normal","suspicious","sad","down",tears="soft")
                    call lun_main("[lun_genie_name] I don't know about this... ","normal","mad","sad","mid",tears="soft")
                    if daytime:
                        m "Come on, [lun_name], just a little peek and then you'll be off to class."
                    else:
                        m "Come on, [lun_name], just a little peek and then you'll be off to bed."
                    call lun_main("Alright, [lun_genie_name]... ","normal","suspicious","sad","down",tears="soft")
                    call lun_main("(Stripping for the headmaster...)","normal","suspicious","sad","R",tears="soft")
                    call lun_main("(imagine if daddy found out...)","normal","suspicious","sad","down",tears="soft")
                    call lun_main("......","normal","suspicious","sad","mid",tears="soft")
                    hide screen luna_main
                    show screen blkfade
                    with d3

                    $ luna_wear_bra = False
                    call update_lun_uniform
                    ">Luna slowly unlatches her bra and places it on your desk."
                    show screen luna_main
                    hide screen blkfade
                    with d3

                    m "*Mmmm*, very nice, [lun_name]."
                    m "Now for your panties..."
                    call lun_main("yes, [lun_genie_name]... ","upset","mad","sad","R",tears="crying")
                    hide screen luna_main
                    show screen blkfade
                    with d3

                    $ luna_wear_panties = False
                    call update_lun_uniform
                    ">Luna slightly turns to the side so you can't quite make out her crotch..."
                    ">She's very hesitant and takes her time pulling down her panties..."
                    ">Luna slowly steps out of her panties and places them on top of the pile of clothes on your desk."
                    show screen luna_main
                    hide screen blkfade
                    with d3
                    call ctc

                    call lun_main("...","upset","suspicious","sad","down",tears="crying")
                    m "Very nice..."
                    call lun_main("c-can I get dressed now... it's a bit cold in here.","normal","suspicious","sad","R",tears="crying")
                    m "*mmmm*... so I can see."
                    call lun_main("!!!","upset","wide","angry","mid",tears="crying")
                    call lun_main("That's enough! I refuse to stand here any longer!","normal","suspicious","mad","mid",tears="crying")

                "-Start jerking off-":
                    $ current_payout = 65
                    m "anything?"
                    hide screen blktone
                    with d3

                    ">You reach under the desk and grab your cock..."
                    hide screen blktone
                    with d3
                    call gen_chibi("jerk_off_behind_desk")
                    with d3
                    call ctc

                    m "Is this better, [lun_name]?"
                    call lun_main("{size=-3}I suppose so...{/size}","upset","suspicious","sad","down",tears="soft")
                    m "Well, if it makes you happy..."
                    ">You start stroking faster."
                    call lun_main("...","upset","suspicious","sad","down",tears="soft")
                    m "Yes... Ah, yes, this is good..."
                    call lun_main("Fine! Have it your way, [lun_genie_name]!","upset","suspicious","sad","down",tears="mascara")
                    call lun_main("enjoy stroking your filthy old cock while you force me to stand here...","upset","suspicious","mad","mid",tears="mascara")
                    m "{size=-4}(*mmmm*... yes...){/size}"
                    m "well, seeing as how you are standing there... why don't you give those nice little tits of yours a good shake?"
                    call lun_main("*Hmph*...","normal","angry","angry","mid",tears="mascara")
                    ">Luna sways her chest side to side ever so slightly."
                    call lun_main("well...","normal","angry","mad","down",tears="mascara")
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "just a little bit faster..."
                    call lun_main("*Hmph*... just hurry up and get it over with, [lun_genie_name]...","upset","suspicious","sad","down",tears="mascara")
                    ">Luna starts shaking her chest a little faster"
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep going..."
                    call lun_main("........","normal","mad","mad","mid",tears="mascara")
                    m "{size=-4}(*argh*... yes...){/size}"
                    call lun_main("(he's going to shoot it all out in front of me...)","normal","angry","sad","down",tears="mascara")
                    m "{size=-4}yes...{/size}"
                    call lun_main("(Should I stop?)","upset","suspicious","sad","R",tears="mascara")
                    g4 "{size=+2}*mmmm*... that's it, keep shaking those milky tits...{/size}"
                    call lun_main(".........","base","seductive","sad","mid", tears="mascara")
                    g4 "{size=+4}(*agh*... almost there...){/size}"
                    call lun_main("(too late...)","base","suspicious","sad","down",tears="mascara")
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    hide screen luna_main
                    with d3
                    call cum_block

                    g4 "*Argh*! YES!"
                    hide screen luna_main
                    hide screen bld1
                    call gen_chibi("cum_behind_desk")
                    show screen bld1
                    with d3

                    call lun_main("*ugh*... there's so much...","normal","mad","sad","down",tears="mascara")
                    call lun_main("{size=-5}(As usual...){/size}","base","mad","sad","R",tears="mascara")
                    call gen_chibi("cum_behind_desk_done")
                    with d3

                    g4 "good work, slut... ah, shit, this feels so good..."
                    hide screen bld1
                    with d3

                    call lun_main("......","normal","angry","sad","mid",tears="mascara")
                    m "*Ah*... you did good, [lun_name]..."

            hide screen luna_main
            show screen blkfade
            with d3

            call load_luna_clothing_saves
            call update_lun_uniform
            ">Luna quickly picks her clothes up off your desk and gets dressed."
            hide screen blkfade

            call lun_main("I think I'd like to leave now, [lun_genie_name]...","normal","angry","sad","down",xpos="base",ypos="base",trans=fade)
            m "You're free to leave whenever you like, [lun_name]."
            call lun_main("Well I'm certainly not leaving until you pay me!","upset","suspicious","angry","mid")

        else:
            $ current_payout = 300
            call lun_main("There... is this what you wanted to see, [lun_genie_name]?","normal","angry","angry","mid")
            g4 "gods yes!"
            if lun_dom <= 5:
                $ lun_dom += 1
            call lun_main("well... seeing as how you seem to be enjoying yourself so much...","base","seductive","angry","mid")
            m "what?"
            call lun_main("why don't you start... touching yourself, [lun_genie_name]...","base","seductive","angry","down")
            m "I'm not sure if--"
            call lun_main("that wasn't a question, [lun_genie_name]...","normal","mad","angry","mid")

            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            call ctc

            call lun_main("there we are...","base","mad","sad","mid")
            call lun_main("don't you feel better now?","base","mad","sad","R")
            m "*mmmm*... yes..."
            call lun_main("*Hmm*... I'm not sure if I believe you.","upset","suspicious","sad","mid")
            call lun_main("maybe you need a little encouragement...","base","suspicious","sad","R")
            m "encouragement?"
            call lun_main("close your eyes, [lun_genie_name]...","base","suspicious","sad","mid")
            hide screen luna_main
            show screen blkfade
            with d3

            if luna_wear_top:
                $ luna_wear_panties = False
            else:
                $ luna_wear_bra = False

            call update_lun_uniform
            call lun_chibi("stand","desk","base")

            ">you can hear the soft ruffle of clothes being taken off..."
            ">You feel something light get thrown against your chest..."
            m "???"
            m "Can I open my eyes yet, [lun_name]?"
            lun "Go ahead, [lun_genie_name]..."
            hide screen blkfade
            call lun_main("","base","suspicious","sad","R")
            call ctc

            call lun_main("like what you see?","soft","suspicious","sad","R")
            g9 "!!!"
            call nar(">You start stroking your cock with renewed vigour.")
            call lun_main("I'll take that as a yes...","base","mad","angry","mid")
            g9 "*Ah-a*... Yeah... This feels great..."
            call lun_main("good... just work up a nice big load for me...","base","suspicious","angry","mid")
            if luna_wear_panties:
                call lun_main("if you're a good boy, I might even let you shoot it all over my bra...","base","mad","angry","R")
            else:
                call lun_main("if you're a good boy, I might even let you shoot it all over my panties...","base","mad","angry","R")
            g9 "Yes, [lun_name]!"
            call lun_main("I bet you'd love that wouldn't you?","base","angry","angry","mid")
            m "yes..."
            call lun_main("Shooting your filthy old cum all over my underwear...","base","mad","sad","down")
            m "..."
            call lun_main("come on then, [lun_genie_name]...","base","suspicious","sad","mid")
            call lun_main("keep stroking that disgusting cock of yours...","base","suspicious","angry","mid")
            m "{size=-4}(*argh*... yes...){/size}"
            call lun_main("do you need a little more encouragement, [lun_genie_name]?","base","mad","mad","mid")
            m "{size=-4}yes...{/size}"
            call lun_main("say it louder...","base","mad","mad","mid")
            g9 "{size=+4}yes{/size}"
            call lun_main("well, close your eyes...","base","suspicious","mad","mid")
            hide screen luna_main
            show screen blkfade
            with d3

            if luna_wear_panties:
                $ luna_wear_bottom = False
            else:
                $ luna_wear_top = False

            call update_lun_uniform
            call lun_chibi("stand","desk","base")

            ">you can once more hear the soft ruffle of clothes..."
            m "{size=-2}(*mmmm*...){/size}"
            lun "open wide, [lun_genie_name]..."
            hide screen blkfade

            call lun_main("","base","suspicious","angry","mid")
            call ctc

            call lun_main("you love this, don't you?","soft","suspicious","angry","mid")
            g4 "{size=+4}(*agh*...){/size}"
            call nar(">you start stroking your cock even faster!")
            g4 "{size=+4}yes...{/size}"
            call lun_main("that's it, [lun_genie_name], cum for your princess...","base","suspicious","sad","mid")
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            g4 "{size=+4}(*agh*... almost there...){/size}"
            call lun_main("cum...","soft","angry","mad","mid")

            if luna_wear_panties:
                call lun_main("{size=+4}cum all over my bra!{/size}","soft","angry","mad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"
                call nar(">You grab Luna's bra and start stroking your cock into it.")
            else:
                call lun_main("{size=+4}cum all over my panties!{/size}","soft","angry","mad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"
                call nar(">You grab Luna's panties and start stroking your cock into them.")

            hide screen luna_main
            with d3
            call cum_block

            g4 "*Argh*! YES!"
            hide screen luna_main
            hide screen bld1
            call gen_chibi("cum_behind_desk")
            show screen bld1
            with d3

            call lun_main("That's it, [lun_genie_name], make sure you cover them...","base","suspicious","mad","mid")
            call gen_chibi("cum_behind_desk_done")
            with d3
            g4 "ah, shit they're so soft, why does this feels so good..."

            call gen_chibi("sit_behind_desk")
            with d3

            call lun_main("*mmm*...","base","mad","mad","mid")
            m "ah..."
            call lun_main("keep going... make sure you get every last drop out.","base","mad","sad","down")
            m "ah... Thank you..."
            call lun_main("Thank you...?","upset","suspicious","raised","mid")
            m "Thank you princess..."
            $ lun_name = "Princess"
            call lun_main("*Hmph*","normal","suspicious","angry","R")
            call lun_main("Well seeing as how you've... finished... I suppose I better get dressed.","normal","angry","angry","R")

            hide screen luna_main
            show screen blkfade
            with d3

            call load_luna_clothing_saves

            if luna_wear_panties:
                ">Luna quickly picks her clothes up off your desk and gets dressed, except for her cum covered bra."
                $ luna_wear_bra = False
            else:
                ">Luna quickly picks her clothes up off your desk and gets dressed, except for her cum covered panties."
                $ luna_wear_panties = False

            call update_lun_uniform
            hide screen blkfade

            call lun_main("","base","closed","raised","mid",xpos="base",ypos="base")
            m "aren't you going to put those on as well?"
            call lun_main("What? and risk contaminating the evidence?","upset","suspicious","raised","mid")
            g4 "Evidence?"
            call lun_main("Oh don't worry, I just needed some... insurance...","base","angry","sad","R")
            m "insurance? Against what?"
            call lun_main("well if I tried to tell the ministry of magic what was going on here, I'd get laughed out of the room.","base","mad","raised","mid")
            call lun_main("but this?","base","angry","angry","mid")
            ">She dangles the cum soaked underwear in front of you."
            call lun_main("This says otherwise.","base","angry","angry","down")
            m "How will they know it's mine? That could be anyone's cum!"
            call lun_main("Please... we're taught identification spells in second year. Even Neville Longbottom would know it's yours.","base","suspicious","mad","mid")
            m "(Shit, if she actually tries that she might work out I'm not really {i}Dumblefore{/i} or whatever his name is...)"
            m "So you're going to tell them everything?"
            call lun_main("What? of course not.","base","suspicious","base","R")
            call lun_main("As long as you behave yourself...","base","suspicious","base","mid")
            m "And what does that entail?"
            call lun_main("Well, first things first, we're going to talk about how much I'm going to be paid.","base","suspicious","base","R")
            call lun_main("Three hundred gold sounds fair to me... {w=0.5}how about you?","base","suspicious","angry","mid")
            m "It sounds... fair..."
            call lun_main("I'm glad we could come to an agreement.","base","mad","sad","R")
            m "yes, [lun_name]..."
            call lun_main("Good boy... now, speaking of payment...","normal","suspicious","angry","mid")

    else: ###THIRD TIME EVENT IS RUN
        if lun_sub > lun_dom :
            m "You don't mind taking your clothes off again, do you, [lun_name]?"
            call lun_main("...","normal","base","sad","R")
            call lun_main("Well... {size=-3}I {size=-4}mean {size=-2}I {size=-2}do {size=-2}mind.","normal","base","sad","down")
            m "..."
            call lun_main("...","normal","base","sad","mid")
            call lun_main("alright then, [lun_genie_name]...","base","base","sad","R")
            hide screen luna_main
            with d3
            call lun_walk("desk")
            call lun_main("(Why can't I stand up for myself?)","upset","base","sad","R", xpos=270)
            call lun_main("...","pout","base","sad","down")
        else:
            m "If it's not too much trouble--"
            call lun_main("...","normal","base","angry","R")
            m "--Could you please take your clothes off?"
            call lun_main("*Hmph* {w=0.5}Well, seeing as how you seemed to have learned some manners.","normal","angry","angry","mid")
            m "yes, [lun_name]..."
            call lun_main("I suppose there's no harm in it...","base","seductive","angry","R")
            hide screen luna_main
            with d3
            call lun_walk("desk")
            call lun_main("...","base","suspicious","angry","mid", xpos=270)

        menu:
            "\"Take off your skirt.\"" if lun_sub >= 5:
                $ luna_choice = 1
                call lun_main("My skirt?","pout","wide","sad","mid")
                m "Yes..."
                call lun_main("...","normal","angry","sad","R")
                call lun_main(".......","normal","angry","sad","R")
                call lun_main("{size=-7}Alright...{/size}","base","angry","sad","R")
                m "*Mmmm*, someone's eager today."
                call lun_main("[lun_genie_name]...","normal","closed","sad","down")
                call lun_main("...","base","base","sad","R")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_bottom = False
                call update_lun_uniform
                ">Luna slowly starts to unzip her skirt..."
                ">However, she doesn't hesitate, quickly placing the skirt on your desk..."
                show screen luna_main
                hide screen blkfade
                with d3

                call lun_main("There... Is that all [lun_genie_name]?","upset","mad","sad","R")
                m "Not quite..."
                call lun_main("(Surely he doesn't want me to take off my panties?)","upset","suspicious","angry","R")
                call lun_main("[lun_genie_name] please...","normal","angry","sad","mid")
                m "Now now, [lun_name], a deal's a deal..."
                call lun_main("...","upset","suspicious","sad","R")
                call lun_main("At least close your eyes...","normal","angry","sad","mid",tears="soft")
                m "As you wi-- command..."
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_panties = False
                call update_lun_uniform
                ">You hear the soft rustle of clothes..."
                ">Suddenly something is gently placed on your desk"
                hide screen blkfade

                call lun_main("There... are you happy now!?","normal","seductive","angry","R",tears="soft")
                g9 "Of course!"
                g9 "I only expected you to take your shirt off!"
                call lun_main("What!","open","wide","angry","mid",tears="soft")
                call lun_main("Please! let me put them back on!","normal","wide","sad","mid",tears="soft")
                ">Luna scrambles to pick her panties back up off your desk, but you're too fast for her, quickly snatching them up."
                m "Ah ah ah, Miss Lovegood."
                call lun_main("You're so... You're so mean!","normal","mad","sad","R",tears="soft")
                m "Don't complain too much, I was hoping you'd take those off anyway."
                call lun_main("*hmph*","upset","suspicious","base","mid",tears="soft")
                m "Well, seeing as how we've already crossed this line, how about you take off your top?"
                call lun_main("You can't be serious!? I think you've seen enough, [lun_genie_name]!","upset","angry","angry","mid",tears="soft")

            "\"Take off your shirt.\"" if lun_sub > lun_dom:
                $ luna_choice = 2
                call lun_main("my shirt?","normal","angry","sad","mid")
                m "That's not too much is it, [lun_name]?"
                call lun_main("no...","normal","mad","sad","R")
                m "..."
                call lun_main("...","upset","suspicious","sad","down")
                call lun_main("*ugh*, Fine... (I hope he doesn't expect me to take off my bra as well)","normal","angry","sad","R")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_top = False
                call update_lun_uniform
                ">Luna starts to unbutton her shirt..."
                ">She gently undoes the buttons, letting it slide off her shoulders before placing it on your desk."
                show screen luna_main
                hide screen blkfade
                with d3
                call ctc

                call lun_main("There... is that all, [lun_genie_name]?","normal","suspicious","sad","mid")
                m "Almost... take off your bra next."
                call lun_main("[lun_genie_name], I really don't--","normal","angry","sad","R")
                m "[lun_name]..."
                call lun_main("...{w=0.5} fine...","base","angry","sad","R")
                call lun_main("But you have to close your eyes.","normal","angry","sad","mid")
                m "done."
                call lun_main("...","base","suspicious","sad","down")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_bra = False
                call update_lun_uniform
                ">You hear the soft rustle of clothes..."
                ">You can hear something being placed softly onto your desk"
                show screen luna_main
                hide screen blkfade
                with d3

                m "Very nice..."
                m "Now your skirt."
                call lun_main("You can't be serious! I think you've seen enough, [lun_genie_name]!","upset","angry","angry","mid")


            "\"Please take off your shirt.\"" if lun_dom >= lun_sub:
                $ luna_choice = 3
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("well seeing as how you asked so {i}nicely{/i}...","base","suspicious","base","mid")
                m "thank you, [lun_name]."
                call lun_main("(I can't believe people think that this is the greatest wizard ever...)","base","angry","base","R")
                call lun_main("close your eyes...","base","mad","angry","mid")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_bottom = False
                $ luna_wear_top = False
                call update_lun_uniform
                ">you can hear the soft ruffle of clothes being removed..."
                m "..."
                m "Can I open my eyes yet, [lun_name]?"
                lun "you can open then when I tell you..."
                ">You hear her softly place something on the table..."
                lun "..."
                m "..."
                lun "Alright, go ahead."
                show screen luna_main
                hide screen blkfade
                with d3

            "\"Please take off your skirt, [lun_name]...\"" if lun_dom >= 5:
                $ luna_choice = 4
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("well seeing as how you said the magic word I suppose it's only fair...","base","suspicious","base","mid")
                m "thank you, [lun_name]."
                call lun_main("(I've got him wrapped around my finger...)","base","angry","base","R")
                call lun_main("well... close your eyes...","normal","angry","angry","mid")
                hide screen luna_main
                show screen blkfade
                with d3

                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_bottom = False
                $ luna_wear_top = False
                call update_lun_uniform
                ">you can hear the soft ruffle of clothes and zips..."
                m "..."
                m "Can I open my eyes yet, [lun_name]?"
                lun "wait..."
                m "..."
                ">You hear her softly place something on the table..."
                lun "Alright, you can open them now..."
                show screen luna_main
                hide screen blkfade
                with d3

        if luna_choice <= 2: #luna sub choices
            if lun_sub <= 6:
                $ lun_sub += 1

            m "I am, and I expect you to do it now, [lun_name]."
            call lun_main("[lun_genie_name]... please...","normal","seductive","sad","mid",tears="soft")
            m "*Hmm*... Well... Seeing as how I'm in a generous mood, how about we make another deal?"
            call lun_main("...","normal","angry","sad","R",tears="soft")
            call lun_main("Really? What sort?","normal","angry","sad","R")
            m "what's the closest school to {i}Howgsmorts{/i}?"
            call lun_main("?... {w=0.5}Um, probably Beauxbatons Academy of Magic, [lun_genie_name]...","normal","seductive","sad","R")
            m "Well, how about I send a glowing letter of recommendation to them concerning your father's magazine?"
            m "I'm sure it would boost sales.{w=0.4} {size=-4}Probably...{/size}"
            call lun_main("Really sir? You'd do that?","base","wide","base","mid")
            call lun_main("And all I have to do is stand here and...","normal","seductive","sad","R")
            if luna_wear_bottom == False:
                call lun_main("take off my top...","normal","angry","sad","down")
                m "and your bra."
            else:
                call lun_main("take off my skirt...","normal","angry","sad","down")
                m "and your panties."
            call lun_main("......","normal","mad","sad","mid")
            call lun_main("..........","normal","suspicious","sad","R")
            call lun_main("Alright... but you have to close your eyes...","normal","suspicious","sad","mid")
            m "Of course."

            hide screen luna_main
            show screen blkfade
            with d3

            $ luna_wear_panties = False
            $ luna_wear_bra = False
            $ luna_wear_bottom = False
            $ luna_wear_top = False
            call update_lun_uniform
            ">You hear the soft rustle of clothes..."
            ">Suddenly something is gently placed on your desk"

            call lun_chibi("stand","desk","base")

            hide screen blkfade
            with d3

            call lun_main("......","normal","mad","sad","down",xpos="mid",ypos="base")
            g9 "looking good, [lun_name]!"
            g9 "So good, in fact, that I think I need a closer look!"
            hide screen luna_main
            show screen blkfade
            with d3

            $ luna_chibi.zorder = 2
            call gen_chibi("stand_alt",440,"base")
            call lun_chibi("stand",535,"base")
            show screen chair_left
            show screen desk

            hide screen blkfade
            with fade
            call ctc

            m "*mmmm*..."
            call lun_main("......","normal","mad","sad","R", xpos=500)

            menu:
                "-Grab her tits-":
                    $ current_payout = 40
                    m "Come closer, [lun_name]."
                    call lun_main("Okay...","normal","mad","sad","R")

                    show screen blkfade
                    with d3

                    call lun_chibi("stand",510,"base")

                    ">You reach out swiftly and grab both of her creamy tits..."
                    hide screen blkfade

                    call lun_main("!!!","upset","wide","mad","mid")
                    ">YOu start gently kneading her breasts."
                    m "*Mmmm*... that's it, [lun_name]..."
                    call lun_main("{size=-5}(What is he doing?){/size}","normal","suspicious","sad","R")
                    call lun_main("[lun_genie_name], you really have to stop... ","upset","mad","sad","mid")
                    if daytime:
                        m "Come on, [lun_name], just a little more, then you'll be off to class."
                    else:
                        m "Come on, [lun_name], just a little more, then you'll be off to bed."
                    call lun_main("[lun_genie_name]... no...","normal","suspicious","sad","down",tears="crying")
                    call lun_main("(I should stop him...)","normal","suspicious","sad","R",tears="crying")
                    call lun_main("(before he gets too excited...)","normal","suspicious","sad","down",tears="crying")
                    ">Luna pushes you back."
                    call lun_main("......","normal","suspicious","sad","mid",tears="crying")
                    ">You let her go and take a step back."

                    call gen_chibi("stand_alt",420,"base")
                    with d3

                    call lun_main("...","upset","suspicious","sad","down",tears="crying")
                    m "Sorry..."
                    call lun_main("It-it's alright, [lun_genie_name]...","normal","suspicious","sad","R",tears="crying")
                    call lun_main("You just got a little over-excited...","normal","suspicious","sad","down",tears="crying")
                    call lun_main("Just, please, try and control yourself next time...","base","suspicious","sad","R",tears="crying")
                    g9 "With tits like that, I'm not so sure!"
                    call lun_main("...","normal","suspicious","sad","R",tears="crying")


                "-start jerking off-" if luna_choice == 1:
                    $ current_payout = 100
                    m "*mmmm*..."
                    call lun_main("......","normal","mad","sad","mid")
                    hide screen blktone
                    show screen blkfade
                    with d3

                    ">You reach into your robe and pull out your cock..."
                    ">You spit on your hand to lube it before you start stroking..."

                    call gen_chibi("jerk_off")
                    hide screen blkfade
                    with fade

                    call lun_main("!!!","upset","wide","mad","mid")
                    call lun_main("(Am I just going to let him do this?)","upset","suspicious","angry","R")
                    call lun_main("Sir I really think--","upset","mad","angry","mid")
                    m "*Shhhh*..."
                    ">You start stroking faster."
                    call lun_main("...","upset","seductive","sad","R")
                    call lun_main("(I can't just let him...)","upset","suspicious","sad","down")
                    m "Yes... Ah, yes, this is good..."
                    call lun_main("sir... please... don't...","upset","suspicious","sad","down",tears="crying")
                    m "I said \"*shhhh*\", [lun_name]..."
                    call lun_main("Sir... I-I'll leave if y-you don't stop...","upset","suspicious","sad","R",tears="crying")
                    m "If you leave, you can say goodbye to the {i}Squibbler{/i}, or whatever it's called."
                    call lun_main("(I can't do that to daddy...)","upset","angry","sad","down",tears="crying")
                    call lun_main("Fine! I hope you're happy!","upset","angry","sad","mid",tears="crying")
                    call lun_main("enjoy stroking that filthy old cock while you force me to stand here...","upset","angry","sad","down",tears="crying")
                    g9 "{size=-4}(*mmmm*... yes...){/size}"
                    g9 "Oh I am!"
                    call lun_main("*Hmph*...","normal","angry","angry","mid",tears="crying")
                    ">Luna tosses her hair over her shoulder in frustration."
                    call lun_main("You're disgusting...","normal","angry","mad","down",tears="crying")
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "*mmmm*... that's it, [lun_name]..."
                    call lun_main("*Hmph*... just hurry up and get it over with, [lun_genie_name]...","upset","suspicious","sad","down",tears="mascara")
                    call lun_main("I'm sick of looking at that... thing...","normal","angry","sad","R",tears="mascara")
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep looking..."
                    call lun_main("Professor!","normal","mad","angry","down",tears="mascara")
                    m "{size=-4}(*argh*... yes...){/size}"
                    call lun_main("I really don't--","normal","seductive","sad","down",tears="mascara")
                    m "{size=-4}yes...{/size}"
                    call lun_main("--think that--","upset","suspicious","sad","down",tears="mascara")
                    g4 "{size=+2}*mmmm*... that's it keep going...{/size}"
                    call lun_main("--we should be--","base","seductive","sad","down",tears="mascara")
                    g4 "{size=+4}(*agh*... almost there...){/size}"
                    call lun_main("--doing this--","base","suspicious","sad","down",tears="mascara")
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"

                    call gen_chibi("cum_close")
                    $ luna_wear_cum = True
                    $ luna_cum = 5
                    call update_lun_uniform
                    hide screen luna_main
                    with d3
                    call cum_block

                    g4 "*Argh*! YES!"
                    hide screen luna_main
                    hide screen bld1
                    with d3

                    call gen_chibi("cum_close_done")
                    call lun_main("*ugh*... there's so much...","normal","mad","sad","down",tears="mascara")
                    call lun_main("{size=-5}(I can't believe this...){/size}","normal","mad","sad","R",tears="mascara")
                    call lun_main("*ugh*... {size=-5}(it stinks as well...){/size}","normal","mad","angry","down",tears="mascara")
                    g4 "*argh*... good work, slut... ah, shit, this feels so good..."
                    hide screen bld1
                    with d3

                    call lun_main("......","normal","angry","sad","mid",tears="mascara")
                    m "*Ah*... you did good, [lun_name]..."

            hide screen luna_main
            show screen blkfade
            with d3

            call gen_chibi("sit_behind_desk")

            call load_luna_clothing_saves

            $ luna_cum = 2
            call update_lun_uniform
            if luna_wear_cum:
                ">Luna quickly picks her clothes up off your desk and gets dressed, putting on her shirt over the cum."
            else:
                ">Luna quickly picks her clothes up off your desk and gets dressed."
            hide screen blkfade

            call lun_main("I think I'd like to leave now, [lun_genie_name]...","normal","angry","sad","down")
            m "You're free to leave whenever you like, [lun_name]."
            call lun_main("Well I'm certainly not leaving until you pay me!","upset","suspicious","angry","mid")


        else: # Dom choice ?
            $ current_payout = 100
            call lun_main("...","base","angry","base","mid",xpos="mid",ypos="base")
            call lun_chibi("stand","desk","base")
            call ctc

            g9 "*mmmm*"
            if lun_dom <= 5:
                $ lun_dom += 1
            call lun_main("Like what you see [lun_genie_name]?","base","seductive","base","R")
            g9 "Yes... Yes..."
            call lun_main("well... why don't you come take a closer look?...","base","seductive","angry","mid")
            m "what?"
            call lun_main("why don't you stand up and take a good look, [lun_genie_name]...","base","mad","mad","mid")
            m "I don't think that--"
            call lun_main("*shhh*...","soft","angry","angry","mid")
            call lun_main("just stand up sir...","base","angry","angry","mid")
            m "..."
            show screen blkfade
            with d3

            ">You stand up and walk in front of luna, feeling the pressure of her gaze."

            hide screen bld1
            show screen chair_left
            show screen desk
            hide screen luna_main
            call gen_chibi("stand_alt",400,"base")
            call lun_chibi("stand",535,"base")

            hide screen blktone
            hide screen blkfade
            with d5
            call ctc

            call lun_main("there we are...","base","mad","sad","mid", xpos=500)
            call lun_main("Isn't that better?","base","mad","sad","R")
            m "*mmmm*... yes..."
            call lun_main("*Hmm*... that's it, just keep looking...","base","mad","mad","R")
            ">Luna gives her tits a little shake."
            g9 "!!!"
            call lun_main("See something you like?...","base","suspicious","sad","R")
            m "ah, gods yes..."
            call lun_main("*mmmmm*... why don't you take it out [lun_genie_name]...","base","suspicious","sad","mid")
            m "..."
            call lun_main("be a good boy...","base","seductive","sad","mid")
            show screen blkfade
            with d5
            ">You take your cock out and start stroking it..."
            call gen_chibi("jerk_off")
            hide screen blkfade
            with d5

            call lun_main("that's it, [lun_genie_name]...","base","suspicious","sad","mid")
            ">you stare at her soft milky tits..."
            m "*Mmmm*..."
            call lun_main("*Mmmm*, isn't that better?","base","suspicious","sad","R")
            g9 "yes..."
            ">You start stroking your cock with renewed vigour."
            call lun_main("Aren't you keen today?","base","mad","angry","mid")
            g9 "Aha... Yeah... This really great..."
            call lun_main("good... make sure you work up a nice big load for me...","base","suspicious","angry","mid")
            call lun_main("if you're a really good boy I might even let you shoot it... on me...","base","seductive","sad","R")
            g9 "Yes!"
            call lun_main("I bet you'd love that wouldn't you?","base","angry","angry","mid")
            g9 "gods yes..."
            call lun_main("Shooting your filthy old cum all over me...","base","suspicious","angry","down")
            g9 "!!!"
            call lun_main("come on then [lun_genie_name]...","base","suspicious","angry","mid")
            call lun_main("stroke it faster...","base","seductive","sad","mid")
            m "{size=-4}(*argh*... yes...){/size}"
            call lun_main("get that nasty cum ready for me...","base","mad","mad","mid")
            m "{size=-4}yes...{/size}"
            call lun_main("*mmm*...","base","mad","mad","mid")
            m "{size=+2}yes...{/size}"
            call lun_main("you really love this don't you...","base","suspicious","angry","mid")
            g4 "{size=+4}(*agh*...){/size}"
            ">you start stroking your cock even faster!"
            g4 "{size=+4}yes...{/size}"
            call lun_main("Is this why you became a teacher...","base","suspicious","sad","mid")
            call lun_main("Just to cover students in your filthy cum...","base","seductive","angry","mid")
            g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"
            call lun_main("well?","base","suspicious","sad","mid")
            g4 "{size=+4}(*agh*... almost there...){/size}"
            call lun_main("do it...","base","angry","angry","mid")
            call lun_main("{size=+4}cum all over me!{/size}","smile","suspicious","angry","mid")
            g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"

            call gen_chibi("cum")
            $ luna_wear_cum = True
            if luna_addicted:
                $ luna_cum = 11
            else:
                $ luna_cum = 5
            call update_lun_uniform
            hide screen luna_main
            with d3
            call cum_block

            call lun_main("...","base","seductive","base","down")
            g4 "*Argh*! YES!"
            hide screen luna_main
            with d3

            call ctc

            call gen_chibi("jerk_off")
            hide screen bld1
            with d3

            if luna_addicted:
                call lun_main("That's it, [lun_genie_name], make sure you cover me...","base","suspicious","mad","mid")

                call gen_chibi("cum")
                with d3
                g4 "ah shit... *ah*... this is too good..."
                call lun_main("*mmm*...","base","mad","mad","mid")
                m "*ah*..."
                call lun_main("keep going... make sure you get every last drop of that delicious cum out...","base","mad","sad","down")
                m "*ah*... Thank you..."
                call lun_main("Good boy...","base","seductive","angry","R")

                call gen_chibi("hold_dick")
                call lun_main("Well seeing as how you've... finished... I suppose I better clean up.","normal","angry","angry","R")
                $ luna_cum = 12
                ">Luna collects a strand of cum on the end of her finger, staring at it intently before putting it into her mouth."
                call lun_main("{heart}{heart}{heart}","base","seductive","sad","empty")
                call lun_main("*mmmm*{heart}{heart}","base","seductive","sad","mid")
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{heart}{heart}{heart}","base","seductive","sad","mid")
                call ctc

                $ luna_cum = 14
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{heart}{heart}{heart}","base","seductive","sad","mid")
                $ luna_cum = 15
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{heart}{heart}{heart}","base","seductive","sad","mid")
                $ luna_wear_cum = False
                call update_lun_uniform
                call lun_main("ah...","base","seductive","sad","mid")
                call lun_main("amazing...","base","seductive","sad","L")
                hide screen luna_main
                with d3

                show screen blkfade
                with d5

                ">Luna quickly picks her clothes up off your desk and gets dressed."

                call load_luna_clothing_saves

                $ luna_wear_cum = False
                call update_lun_uniform
                call gen_chibi("sit_behind_desk")
                show screen luna_main
                hide screen blkfade
                with d3

                g4 "That was... incredible!"
                call lun_main("I'm glad you enjoyed yourself...","base","base","base","mid")
                m "we need to do this again!"
                call lun_main("*mmmm*... but before that, I think we need to discuss payment for this time...","base","seductive","angry","R")

            else:
                call lun_main("That's it, [lun_genie_name], make sure you cover me...","base","suspicious","mad","mid")

                call gen_chibi("cum")
                with d3
                g4 "ah, shit... ah... this is too good..."
                call lun_main("*mmm*...","base","mad","mad","mid")
                m "ah..."
                call lun_main("keep going... make sure you get every last drop out.","base","mad","sad","down")
                m "ah... Thank you..."
                call lun_main("Good boy...","base","seductive","angry","R")

                call gen_chibi("hold_dick")
                call lun_main("Well seeing as how you've... finished... I suppose I better get dressed.","normal","angry","angry","R")

                show screen blkfade
                with d5
                ">Luna quickly picks her clothes up off your desk and gets dressed, putting her shirt on over her cum covered chest."
                hide screen luna_main

                call load_luna_clothing_saves

                $ luna_cum = 2
                call update_lun_uniform
                call gen_chibi("sit_behind_desk")
                show screen luna_main
                hide screen blkfade
                with d3

                m "That was... amazing"
                call lun_main("I'm glad you enjoyed yourself...","base","base","base","mid")
                m "I have to ask though. why did you--"
                call lun_main("Do this?","normal","seductive","angry","R")
                m "yes."
                call lun_main("Don't worry about that...","base","mad","angry","mid")
                call lun_main("THe only thing you have to worry about...","base","angry","angry","mid")
                $ luna_l_arm = 2
                ">She runs her finger across the edge of her mouth."
                call lun_main("Is keeping that cock of yours in check...","base","angry","angry","down")
                m "What?"
                call lun_main("I know you're probably leering after some other students sir...","base","suspicious","mad","mid")
                call lun_main("But if I find out that you've buying favours from other students.","base","suspicious","base","R")
                call lun_main("well...","base","suspicious","base","mid")
                m "..."
                call lun_main("let's just say I wouldn't let that happen if I were you...","base","suspicious","base","R")
                call lun_main("Now forget about that, let's discuss payment. A hundred gold sounds fair to me... {w=0.5}how about you?","base","suspicious","angry","mid")
                m "It sounds fair..."
                call lun_main("I'm glad we could have a happy ending.","base","mad","sad","R")
                m "yes, [lun_name]..."
                call lun_main("Good boy... now, speaking of payment...","normal","suspicious","angry","mid")

    hide screen bld1
    if lun_dom >= lun_sub:
        m "Alright, alright. Here's your gold."
    else:
        m "well then, Here's your payment, [lun_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    $ renpy.play("sounds/coins.mp3")
    ">You hand Luna {number=current_payout} gold."
    if current_payout <= 40:
        call lun_main("(only {number=current_payout}?) *Hmph*...","upset","mad","angry","R")
        call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
    else:
        call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
    $ luna_wear_cum = False
    call update_lun_uniform

    jump luna_away
