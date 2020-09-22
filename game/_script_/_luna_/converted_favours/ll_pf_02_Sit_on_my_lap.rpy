
# Luna (converted) sit on my lap
label luna_favour_2:

    m "{size=-4}(I'll just ask her to sit on my lap...){/size}"
    if lun_whoring < 4:
        # First time
        if lun_whoring < 4:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Before we get started, Would you like a seat, [luna_name]?"
        call lun_main("I would, but there's no chair [lun_genie_name]...","normal","angry","raised","mid")
        m "How about you come sit on my lap then?"
        call lun_main("...","upset","suspicious","angry","mid")
        m "Come on, it'll be just like Santa Claus."
        call lun_main("...","upset","suspicious","angry","R")
        call lun_main("You better make this worth it [lun_genie_name]...","upset","mad","angry","R")
        m "Don't worry, I'm sure you'll be very happy with your \"reward\"."
        call lun_main("...","upset","suspicious","angry","mid")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."

        $ luna_chibi.zorder = desk_zorder - 1
        call lun_chibi("stand", "by_desk", "back")
        call lun_main(xpos="left")
        hide screen blkfade
        with d3

        menu:
            "-Pull her onto your lap-" if lun_sub >= 2:
                if lun_sub < 4:
                    $ lun_sub += 1
                $ luna_grope = True

                call lun_main("...","upset","suspicious","angry","R")
                call lun_main("Actually, I'm not sure if...","normal","mad","base","R")
                ">You grab Luna around the waist and pull her onto your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(ypos="low", flip=True)
                with d3

                call lun_main("[lun_genie_name]! What are you doing?","upset","wide","raised","R")
                m "just giving you a helping hand..."
                ">you start rubbing your crotch slowly against her soft ass."
                m "*mmm* that's it..."
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("(this is so humiliating...)","upset","suspicious","sad","down")

                jump .lap_dance

            "-Tell her to sit down-":
                $ luna_grope = False

                m "go on [luna_name]..."
                call lun_main("...","upset","mad","angry","R")
                call lun_main("Do I really have to do this?","upset","mad","angry","R")
                m "Just sit down [luna_name]..."
                call lun_main("...","upset","mad","angry","R")
                ">Luna softly takes a seat on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(ypos="low", flip=True)
                with d3

                m "*mmmmm*..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(ugh, he's so hard...)","clench","suspicious","sad","down")

                label .lap_dance:
                m "That's it, now just start moving your waist."
                ">Luna gradually starts grinding her ass against you."
                m "*ughh*, that's it."
                call lun_main("...","upset","mad","angry","down")
                call lun_main("are you happy now?","upset","mad","mad","R")
                m "Very..."
                call lun_main("Can I leave yet?","upset","mad","angry","mid")
                m "What? We just started!"
                call lun_main("Well, I don't have all day.","upset","mad","angry","R")
                m "*Hmmm*, I'll see what I can do to speed this up..."

                menu:
                    "-Grab her waist-":
                        $ current_payout = 75
                        ">You take a hold of her waist."
                        call lun_main("!!!","clench","wide","base","mid")
                        call lun_main("I don't think touching was part of the arrangement [lun_genie_name]...","upset","angry","mad","R")
                        m "Don't worry [luna_name], you'll be compensated fairly."

                        call lun_chibi_scene("sit_on_lap_grope")
                        with d3

                        ">You pull her firmly against your crotch, rubbing your cock between her cheeks."
                        call lun_main("...","grin","suspicious","sad","down")
                        m "That's it [luna_name], not much longer now."
                        call lun_main(".......","upset","mad","angry","R")
                        m "*mmmm*, almost there..."
                        call lun_main("What?!!!","upset","wide","mad","R")

                        show screen blkfade
                        with d3

                        "Luna quickly pulls away from you and stands up."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("[lun_genie_name]!","soft","angry","mad","mid")
                        m "What on earth did you stop for?"
                        call lun_main("Sitting on your lap is one thing.","upset","mad","angry","R")
                        call lun_main("But letting you do {i}that{/i}...","normal","suspicious","mad","mid")
                        call lun_main("I simply refuse!","clench","mad","mad","R")
                        m "fine fine."
                        call lun_main("Honestly, [lun_genie_name], who do you think I am?","normal","angry","angry","mid")
                        call lun_main("I think I'd like to be paid now...","normal","angry","angry","R")

                    "-Grope her-" if luna_grope:
                        $ current_payout = 40

                        call lun_chibi_scene("sit_on_lap_grope")
                        with d3

                        ">You start running your hands along the outside of her thighs, up to her waist and then over her belly."
                        call lun_main("!!!","clench","wide","base","mid")
                        m "*mmmm*, lovely."
                        ">You keep grinding your cock against her butt cheeks."
                        m "yes, just like that [luna_name]."
                        call lun_main("......","clench","suspicious","sad","down")
                        m "gods you've got such a nice ass."
                        ">You Start moving your hands slowly up towards her breasts"
                        call lun_main(".........","upset","suspicious","sad","R")
                        m "That's it [luna_name], just enjoy it."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">Your hands are now about an inch below her breasts."
                        m "*mmmm*, almost there..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">You're about to reach her ample tits."
                        call lun_main("!!!!","clench","wide","mad","mid")

                        show screen blkfade
                        with d3

                        "Luna quickly pulls away from you and stands up."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("[lun_genie_name]!","upset","wide","mad","mid")
                        m "What on earth did you stop for?"
                        call lun_main("Sitting on your lap is one thing!","upset","suspicious","angry","mid")
                        call lun_main("But letting you touch me there...","normal","mad","mad","R")
                        call lun_main("I won't do it!","upset","mad","angry","R")
                        m "alright fine."
                        call lun_main("Honestly, [lun_genie_name], you really need to learn some self control.","disgust","mad","mad","mid")
                        call lun_main("I think I'd like to be paid now...","upset","mad","angry","R")

            "-Do nothing-" if lun_dom < 2:
                $ current_payout = 120
                call lun_main("...","normal","angry","angry","R")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I guess I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly sits on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(ypos="low", flip=True)
                with d3

                m "*mmmm*"
                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main(".........","upset","mad","mad","R")
                call lun_main("Alright, time's up!","normal","base","base","R")
                ">Luna stands up from your lap."

                call lun_chibi_scene("reset", "by_desk", "back")
                call lun_main(xpos="mid", ypos="base", flip=False)
                with d3

                m "What, you barely even sat down!"
                call lun_main("*hmph* You should consider yourself lucky you got what you did [lun_genie_name]!","upset","mad","angry","R")
                m "You could have at least moved around a little."
                call lun_main("What? Who do you think I am? Some sort of harlot who'll let you grind yourself against them for as long as you want?","clench","suspicious","angry","R")
                m "Well... I expected at least a few minutes."
                call lun_main("Alright, if your that desperate...","base","seductive","base","R")
                ">Luna slams her ass into your crotch"

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "ah..."
                call lun_main("pathetic...","upset","seductive","angry","R")
                ">She starts rocking back and forth on your lap"
                call lun_main("You really are disgusting [lun_genie_name]...","soft","seductive","base","R")
                m "*mmmm*"
                call lun_main("begging your students for a lap dance...","upset","mad","mad","R")
                m "yes, yes..."
                call lun_main("you better pay extra for this...","normal","angry","base","R")
                m "of course..."
                call lun_main("...","normal","seductive","base","down")
                ">Luna starts rolling her hips a little faster."
                call lun_main("a lot extra...","upset","suspicious","mad","R")
                m "of course [luna_name]..."
                call lun_main("that's it [lun_genie_name]... just enjoy it...","base","seductive","base","R")
                m "*mmm*, just a little more..."
                call lun_main("...","upset","mad","raised","down")
                m "yes... almost..."

                show screen blkfade
                with d3

                ">Luna quickly stands up and walks round your desk."

                call lun_chibi_scene("reset", "desk", "base")
                call lun_main(xpos="mid", ypos="base", flip=False)
                hide screen blkfade
                with d3

                call lun_main("Time's up!","base","seductive","angry","R")
                m "What!?"
                call lun_main("Time's{w=0.5} up...","normal","mad","angry","mid")
                m "Ugh, fine."
                call lun_main("Glad you understand...{w=0.5} Now, about my payment...","upset","mad","angry","R")

            "-Do nothing-" if lun_dom >= 2:
                if lun_dom < 4:
                    $ lun_dom += 1

                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I guess I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly sits on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(ypos="low", flip=True)
                with d3

                m "*mmmm*"
                ">You start to feel yourself get hard against her ass."
                call lun_main("...","base","seductive","base","R")
                call lun_main("You're pathetic...","upset","seductive","angry","R")
                call lun_main("The world's greatest wizard...","base","seductive","base","R")
                call lun_main("More like the world's greatest pervert.","upset","suspicious","angry","R")

                ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crotch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed, are you?","soft","seductive","base","R")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","upset","mad","angry","R")
                m "I don't recall begging."
                call lun_main("*Hmmm*...","normal","angry","base","R")
                ">Luna stands up slowly."

                call lun_chibi_scene("reset", "by_desk", "back")
                call lun_main(xpos="mid", ypos="base", flip=False)
                with d3

                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")

                menu:
                    "-Beg-":
                        $ current_payout = 200
                        m "Please..."
                        call lun_main("Please what?","normal","seductive","base","R")
                        m "Please keep going [luna_name]..."
                        ">Luna slowly places herself back on your lap."

                        call lun_chibi_scene("sit_on_lap")
                        call lun_main(xpos="left", ypos="low", flip=True)
                        with d3

                        call lun_main("That's better isn't it?","base","angry","angry","R")
                        ">She starts rocking back and forth on your lap"
                        call lun_main("You're so hard...","normal","seductive","base","down")
                        m "*mmmm*"
                        call lun_main("I bet you'd cum if I kept going wouldn't you...","normal","seductive","raised","R")
                        m "yes..."
                        call lun_main("you better be prepared to pay extra for the privilege...","normal","angry","angry","R")
                        m "of course..."
                        call lun_main("...","upset","mad","angry","R")
                        ">Luna starts rolling her hips, your cock pressed between her cheeks."
                        m "ah..."
                        call lun_main("a {size=+5}lot{/size} extra...","upset","seductive","mad","R")
                        m "of course [luna_name]..."
                        call lun_main("Good. just enjoy yourself then...","base","happyCl","base","R")
                        m "*mmm*, just a little more..."
                        call lun_main("pervert...","normal","seductive","angry","R")
                        ">Luna starts rubbing hard against your lap."
                        m "{size=-2}*mmmm*...{/size}"
                        call lun_main("come on...","base","suspicious","angry","mid")
                        g4 "{size=+4}(*agh*... almost there...){/size}"
                        call lun_main("Come for me...","base","suspicious","sad","mid")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        call cum_block

                        g4 "*Argh*! YES!"
                        call lun_main("ugh... pathetic...","base","seductive","mad","R")
                        call lun_main("...","upset","mad","angry","R")
                        call lun_main("......","normal","mad","raised","down")
                        call lun_main(".........","upset","mad","mad","down")
                        call lun_main("Alright, time's up!","base","seductive","angry","R")

                        show screen blkfade
                        with d3

                        ">Luna stands up from your lap."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("*hmph* You pervert!","normal","suspicious","angry","mid")
                        m "You can hardly blame me for this."
                        call lun_main("What? You're the one who begged for it, of course it's your fault.","upset","angry","mad","R")
                        m "well you didn't have to be so good at it."
                        call lun_main("I was just making sure that I earned my reward.","upset","mad","angry","mid")
                        call lun_main("Speaking of which...","base","seductive","base","R")

                    "-Refuse-":
                        $ current_payout = 100
                        m "I don't think so, [luna_name]."
                        call lun_main("*hmph* Fine...","pout","suspicious","angry","R")

                        show screen blkfade
                        with d3

                        ">Luna stands up and walks to the other side of your desk."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("I'd like to be paid now [lun_genie_name]...","upset","mad","mad","mid")

        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna {number=current_payout} gold."
        if current_payout <= 50:
            call lun_main("(only {number=current_payout}?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    elif lun_whoring < 5:
        # Second time
        if lun_whoring < 5:
            $ lun_whoring += 1

        call play_music("chipper_doodle")
        m "Can I offer you another seat, [luna_name]?"
        if lun_sub > lun_dom:
            call lun_main("...","normal","base","sad","down")
            call lun_main("Alright [lun_genie_name]...","normal","base","sad","R")
            m "Good girl."
            call lun_main("...","upset","base","sad","down")
        else:
            call lun_main("Fine...","normal","base","angry","R")
            call lun_main("But I expect to be fairly compensated, [lun_genie_name]...","normal","angry","angry","mid")
            m "yes, yes..."
            call lun_main("...","normal","angry","angry","R")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."

        $ luna_chibi.zorder = desk_zorder - 1
        call lun_chibi("stand", "by_desk", "back")
        call lun_main(xpos="left")
        hide screen blkfade
        with d3

        menu:
            "-Ask her to remove her skirt first-" if lun_sub >= 2:
                if lun_sub < 4:
                    $ lun_sub += 1
                $ luna_grope = True

                m "How about you take off your skirt before we start?"
                call lun_main("!!!","normal","wide","sad","R")
                call lun_main("You're not serious, are you?","normal","suspicious","sad","R")
                m "I am, [luna_name], or do you not want Hogwarts to keep purchasing new copies of \"the Quibbler\"?"
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("......","normal","suspicious","sad","R")
                m "I'm waiting."
                call lun_main("Fine...","clench","suspicious","sad","down")

                show screen blkfade
                with d3
                ##$ luna_wear_bottom = False
                #call update_lun_uniform

                ">Luna slowly removes her skirt, revealing her black silk panties."

                hide screen blkfade
                with d3

                m "I like your panties..."
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("(this is so degrading)","clench","suspicious","sad","down")
                m "Now take a seat..."
                call lun_main("yes [lun_genie_name]...","normal","suspicious","sad","R")
                ">Luna softly takes a seat on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("...","upset","suspicious","sad","down")
                jump .lap_dance_2

            "-Tell her to sit down-" if lun_sub >= lun_dom:
                $ luna_grope = False

                m "come on now..."
                call lun_main("...","upset","mad","sad","R")
                call lun_main("......","upset","mad","sad","R")
                m "Sit down [luna_name]."
                call lun_main("...","upset","mad","sad","R")
                ">Luna softly takes a seat on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "*mmmmm*..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(ugh, he's so hard...)","clench","suspicious","sad","down")

                label .lap_dance_2:
                m "That's it, now just start moving your ass."
                ">Luna gradually starts grinding her waist against you."
                m "*ughh*, that's it."
                call lun_main("...","upset","mad","sad","down")
                call lun_main("is this alright?","normal","seductive","sad","R")
                m "yes, just keep going..."
                call lun_main("For how long?","upset","mad","sad","mid")
                m "As long as it takes [luna_name]."
                call lun_main("fine...","upset","mad","sad","R")
                call lun_main("...","upset","mad","sad","down")
                call lun_main("..........","upset","suspicious","sad","down")
                call lun_main("Is there anything I can do to speed this up?","normal","suspicious","sad","R")

                menu:
                    "-Do nothing-":
                        $ current_payout = 65
                        m "Just keep doing what you're doing..."
                        call lun_main("...","clench","suspicious","sad","down")
                        call lun_main("How about this?","normal","seductive","sad","R")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "*Mmmm*, yes!"
                        ">You start thrusting into her ever so slightly."
                        call lun_main("...","grin","suspicious","sad","down")
                        m "That's it [luna_name], not much longer now."
                        call lun_main(".......","normal","seductive","sad","R")
                        m "*mmmm*, almost there..."
                        call lun_main("Already?","upset","wide","sad","R")
                        m "Almost... this is really good..."
                        call lun_main("it is?","base","seductive","sad","R")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call lun_main("...","base","seductive","sad","R")
                        call lun_main("How's this?","grin","seductive","sad","down")
                        ">She starts rocking back and forth on your lap"
                        m "*mmmmm*"
                        call lun_main("You're so hard [lun_genie_name]...","base","seductive","sad","down")
                        m "*mmmm*"
                        call lun_main("are you almost there?","normal","seductive","sad","R")
                        m "yes..."
                        call lun_main("well, I expect to be--","upset","seductive","angry","R")
                        m "*shhh*, don't ruin it."
                        call lun_main("...","upset","mad","sad","R")
                        ">Luna starts rolling her hips, your cock pressed between her cheeks."
                        m "ah..."
                        call lun_main("...","upset","seductive","sad","R")
                        m "keep going [luna_name]..."
                        call lun_main("........","base","closed","sad","R")
                        m "*mmm*, just a little more..."
                        call lun_main("...[lun_genie_name]...","normal","angry","sad","down")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}*mmmm*...{/size}"
                        call lun_main("......","base","suspicious","sad","mid")
                        g4 "{size=+4}(*agh*... almost there...){/size}"
                        call lun_main("............","base","suspicious","sad","mid",tears="soft")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        call cum_block

                        g4 "*Argh*! YES!"
                        call lun_main("ugh...","base","seductive","sad","R")
                        call lun_main("...","upset","mad","sad","R")
                        call lun_main("......","normal","mad","sad","down")
                        call lun_main(".........","upset","seductive","sad","down")
                        call lun_main("Are you finished now [lun_genie_name]?","base","seductive","sad","R")
                        m "Almost... just stay there for a little longer..."
                        call lun_main("......","base","seductive","sad","R")

                        show screen blkfade
                        with d3

                        ">Luna waits a few seconds before standing up."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        #call load_luna_clothing_saves
                        hide screen blkfade
                        with d3

                        call lun_main("will that be all, [lun_genie_name]?","normal","suspicious","sad","mid")
                        m "Yes, thank you, [luna_name]."
                        call lun_main("You're welcome, [lun_genie_name].","upset","angry","sad","R")
                        if daytime:
                            call lun_main("Well, I better be off to class then.","upset","mad","sad","mid")
                        else:
                            call lun_main("Well, I better be off to bed then.","upset","mad","sad","mid")
                        m "Don't you want your payment first?"
                        call lun_main("Oh right...","base","seductive","sad","R")

                    "-Grope her-" if luna_grope:
                        $ current_payout = 35

                        call lun_chibi_scene("sit_on_lap_grope")
                        with d3

                        ">You start running your hands along the outside of her thighs."
                        call lun_main("...","clench","wide","sad","mid")
                        m "*mmmm*, lovely."
                        ">You keep grinding your cock against her butt cheeks."
                        call lun_main("....","clench","seductive","sad","R")
                        m "yes, just like that [luna_name]."
                        "You move your hands up to her waist"
                        call lun_main("......","clench","suspicious","sad","down")
                        m "gods you've got such a nice ass."
                        call lun_main("t-thank you [lun_genie_name]...","upset","happyCl","sad","R",tears="crying")
                        ">You Start moving your hands slowly up over her smooth stomach."
                        call lun_main(".........","upset","suspicious","sad","R",tears="crying")
                        m "That's it [luna_name], just enjoy yourself..."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">your hands are about an inch below her breasts."
                        m "*mmmm*, almost there..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">You quickly move your hands up and grab a hold of her supple breasts over her vest."
                        call lun_main("!!!!","clench","wide","mad","mid")
                        "Luna tries to pull away from you."

                        menu:
                            "-Let her go-":
                                $ current_payout = 55

                                show screen blkfade
                                with d3

                                ">Luna quickly stands up and walks to the other side of your desk."

                                call lun_chibi_scene("reset", "desk", "base")
                                call lun_main(xpos="mid", ypos="base", flip=False)
                                #call load_luna_clothing_saves
                                hide screen blkfade
                                with d3

                                call lun_main("[lun_genie_name]!","upset","wide","mad","mid")
                                call lun_main("Grabbing me there wasn't part of the deal!","normal","mad","mad","R")
                                m "I just couldn't resist..."
                                call lun_main("*hmph*","upset","mad","angry","R")
                                m "My apologies, [luna_name]."
                                call lun_main("It's alright... just don't let it happen again!","disgust","mad","mad","mid")
                                call lun_main("I think I'd like to be paid now...","upset","mad","angry","R")

                            "-Hold her down-":
                                if lun_sub < 5:
                                    $ lun_sub += 1

                                call lun_main("[lun_genie_name]!","upset","wide","mad","mid")
                                call lun_main("I'd like to leave now!","normal","mad","mad","R")
                                m "just a bit longer [luna_name]..."
                                ">You start grinding your hard cock between her ample cheeks."
                                call lun_main("!!!","upset","wide","sad","down")
                                call lun_main("I insist you let me go!","pout","wide","mad","R")
                                m "If you leave now you can forget about Hogwarts purchasing any more of your father's newspaper, [luna_name]."
                                call lun_main("...","upset","suspicious","sad","down")
                                call lun_main("you're despicable, [lun_genie_name]...","upset","mad","angry","R",tears="soft")
                                ">You give her tits a couple of firm squeezes."
                                call lun_main("ah... {heart}","upset","angry","sad","down",tears="soft")
                                call lun_main("this isn't right...","upset","angry","sad","R",tears="soft")
                                m "I know, I know... But it's hard to resist..."
                                call lun_main(".................","normal","seductive","sad","down",tears="soft")
                                call lun_main("................. ah... {heart}","soft","seductive","sad","down",tears="soft")
                                call lun_main("[lun_genie_name], you need to stop now...","upset","angry","sad","R",tears="soft")
                                m "Just a bit longer..."
                                call lun_main("please...","upset","angry","sad","down",tears="crying")
                                m "*mmmm*, I suppose this will have to do..."
                                ">You give her tits a final pinch."
                                call lun_main("ah...","upset","angry","sad","down",tears="crying")

                                show screen blkfade
                                with d3

                                ">Luna quickly stands up and moves around to the other side of your desk."

                                call lun_chibi_scene("reset", "desk", "base")
                                call lun_main(xpos="mid", ypos="base", flip=False)
                                #call load_luna_clothing_saves
                                hide screen blkfade
                                with d3

                                call lun_main("[lun_genie_name]!","upset","wide","mad","mid")
                                call lun_main("Grabbing me there wasn't part of the deal!","normal","mad","mad","R")
                                m "Sorry, [luna_name], I just couldn't help myself..."
                                call lun_main("...{w=0.5} just please try to control yourself next time...","disgust","mad","mad","mid")
                                m "So you want there to be a next time?"
                                call lun_main("as long as I'm getting paid.","upset","mad","angry","R")
                                call lun_main("speaking of which...","upset","mad","angry","mid")
                                call lun_main("can I please be paid now?","upset","mad","sad","down")

            "-Do nothing-" if lun_sub <= lun_dom:
                $ current_payout = 200
                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I suppose I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly places herself on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "*mmmm*"
                ">You start to feel yourself get hard against her ass."
                call lun_main("...","base","seductive","base","R")
                call lun_main("You're so pathetic...","upset","seductive","angry","R")
                call lun_main("The world's greatest wizard...","base","seductive","base","R")
                call lun_main("More like the world's greatest pervert.","upset","suspicious","angry","R")
                ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crotch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed, are you?","soft","seductive","mad","R")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","upset","mad","angry","R")
                m "I don't recall begging."
                call lun_main("*Hmmm*...","normal","angry","base","R")
                ">Luna stands up slowly."

                call lun_chibi_scene("reset", "by_desk", "back")
                call lun_main(xpos="mid", ypos="base", flip=False)
                with d3

                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","normal","seductive","base","R")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forth on your lap"
                call lun_main("ugh, You're so hard...","upset","suspicious","mad","down")
                m "*mmmm*"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","base","seductive","angry","R")
                m "yes..."
                call lun_main("you better be prepared to pay extra for the privilege...","normal","angry","angry","R")
                m "of course..."
                call lun_main("...","upset","mad","angry","R")
                ">Luna starts rolling her hips, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","R")
                m "of course [luna_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","base","R")
                m "*mmm*, just a little more..."
                call lun_main("pervert...","base","seductive","angry","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}*mmmm*...{/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(*agh*... almost there...){/size}"
                call lun_main("come for your queen...","base","suspicious","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."

                call cum_block

                g4 "*Argh*! YES!"
                call lun_main("*mmmm*... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","normal","mad","mad","down")
                call lun_main(".........","upset","suspicious","mad","down")
                call lun_main("Alright, time's up!","base","seductive","angry","R")

                show screen blkfade
                with d3

                ">Luna stands up from your lap."

                call lun_chibi_scene("reset", "desk", "base")
                call lun_main(xpos="mid", ypos="base", flip=False)
                hide screen blkfade
                with d3

                call lun_main("*hmph* You naughty pervert!","normal","suspicious","angry","mid")
                m "You can hardly blame me for this."
                call lun_main("What? You're the one who begged for it, of course it's your fault.","upset","angry","mad","R")
                m "well, you didn't have to be so good at it."
                call lun_main("I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")

            "-Ask Nicely-" if lun_dom >= 2:
                if lun_dom < 4:
                    $ lun_dom += 1

                $ current_payout = 250
                m "can you please sit on my lap [luna_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("Alright, because you asked so nicely...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "*mmmm*"
                ">You start to feel yourself get hard against her ass."
                call lun_main("...","base","seductive","angry","down")
                call lun_main("You're pathetic...","base","seductive","angry","R")
                call lun_main("The world's greatest wizard...","base","seductive","base","R")
                call lun_main("More like the world's greatest pervert.","base","suspicious","angry","down")
                ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crotch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed, are you?","soft","seductive","angry","down")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","base","mad","angry","R")
                m "I don't recall begging."
                call lun_main("*Hmmm*...","base","seductive","angry","R")
                ">Luna stands up slowly."

                call lun_chibi_scene("reset", "by_desk", "back")
                call lun_main(xpos="mid", ypos="base", flip=False)
                with d3

                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","base","seductive","raised","mid")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forth on your lap"
                call lun_main("You're so hard...","base","seductive","mad","down")
                m "*mmmm*"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","base","seductive","raised","R")
                m "yes..."
                call lun_main("you better be prepared to pay extra for the privilege...","base","angry","angry","R")
                m "of course..."
                call lun_main("...","base","mad","angry","R")
                ">Luna starts rolling her hips, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","down")
                m "of course [luna_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","angry","R")
                m "*mmm*, just a little more..."
                call lun_main("pervert...","base","seductive","base","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}*mmmm*...{/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(*agh*... almost there...){/size}"
                call lun_main("Come for me...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."

                call cum_block

                g4 "*Argh*! YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [luna_name]."
                call lun_main("Who says you get to decide when this ends?","upset","suspicious","angry","R")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call lun_main("really?","base","mad","raised","R")
                call lun_main("But you sounded so sincere earlier when you were begging for this.","soft","seductive","sad","R")
                call lun_main("Surely you don't want it to end already?","base","seductive","angry","R")
                ">she pushes hard against your cock."
                g11 "ah..."
                call lun_main("That's it pervert, just keep enjoying yourself.","base","mad","angry","down")
                g11 "I can't, it's too sensitive..."
                call lun_main("I don't see how that's my problem.","base","mad","sad","R")
                ">She starts moving as fast as she can."
                g11 "{size=-2}*ahhh*...{/size}"
                call lun_main("come on pervert...","base","suspicious","angry","R")
                g11 "{size=+4}*aghhh*!{/size}"
                call lun_main("shoot another filthy load...","base","suspicious","mad","R")
                g4 "{size=+4}*Argh*! It's too much!{/size}"
                call lun_main("{heart}{heart}{heart}","base","suspicious","mad","down")
                ">You start shooting another load against the inside of your sodden cloak."

                call cum_block

                g4 "*Argh*!"
                call lun_main("good boy...","base","seductive","mad","R")

                show screen blkfade
                with d3

                ">Luna stands up from your lap."

                call lun_chibi_scene("reset", "desk", "base")
                call lun_main(xpos="mid", ypos="base", flip=False)
                hide screen blkfade
                with d3

                call lun_main("*hmph* You nasty old pervert!","base","suspicious","angry","mid")
                m "ah..."
                call lun_main("Enjoy yourself a little too much did we?","base","angry","mad","R")
                m "That was too much, [luna_name]..."
                call lun_main("Stop complaining. I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")

        if lun_dom >= lun_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."

        $ gold -= current_payout
        $ luna_gold += current_payout

        ">You hand Luna {number=current_payout} gold."

        if current_payout <= 50:
            call lun_main("(only {number=current_payout}?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")

        ">Luna leaves your office."

    elif lun_whoring >= 5 and lun_whoring < 13:
        # Third time
        if lun_whoring < 6:
            $ lun_whoring += 1

        call play_music("chipper_doodle")
        m "Can I offer you another seat, [luna_name]?"

        if lun_sub > lun_dom:
            call lun_main("...","normal","base","sad","down")
            call lun_main("Alright [lun_genie_name]...","normal","base","sad","R")
            m "Good girl."
            call lun_main("...","upset","base","sad","down")
        else:
            call lun_main("Fine...","normal","base","angry","R")
            call lun_main("But I expect to be fairly compensated, [lun_genie_name]...","normal","angry","angry","mid")
            m "yes, yes..."
            call lun_main("...","normal","angry","angry","R")

        show screen blkfade
        with d3

        ">Luna walks around the desk and stands in front of you."

        $ luna_chibi.zorder = desk_zorder - 1
        call lun_chibi("stand", "by_desk", "back")
        call lun_main(xpos="left")
        hide screen blkfade
        with d3

        menu:
            "-Pull her onto your lap-" if lun_sub >= 3:
                if lun_sub < 5:
                    $ lun_sub += 1
                $ luna_grope = True

                ">You grab Luna by the waist and pull her hard onto your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("!!!","normal","wide","sad","R")
                call lun_main("There's no need to be so forceful [lun_genie_name]!","pout","angry","sad","R")
                m "Sorry, I just can't help myself when I've got such an eager slut in front of me. You don't mind, do you?"
                call lun_main("...","base","suspicious","sad","down")
                call lun_main("......","normal","seductive","sad","R")
                m "Do you?..."
                call lun_main("{size=-5}No...{/size}","normal","suspicious","sad","down")
                call lun_main("...","normal","suspicious","sad","R")
                m "No what?"
                call lun_main("{size=-5}No... [lun_genie_name]...{/size}","clench","suspicious","sad","down")
                m "Good girl..."
                ">You push your cock hard against her ass."
                call lun_main("ah... thank you [lun_genie_name]...","base","suspicious","sad","down")
                call lun_main("...","upset","suspicious","sad","down")
                jump .lap_dance_3

            "-Tell her to sit down-" if lun_sub >= lun_dom:
                if lun_sub < 4:
                    $ lun_sub += 1
                $ luna_grope = False

                m "why don't you--"
                ">Luna quickly sits down on your lap, wriggling around slightly until your cock rests between her cheeks."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("(ah... {heart})","base","mad","sad","down")
                call lun_main("......","upset","wide","sad","R")
                m "Someone's eager today..."
                call lun_main("...","upset","mad","sad","down")
                ">Luna softly starts rocking her hips back and forth."
                m "*mmmmm*..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(he's so hard... {heart})","base","suspicious","sad","down")

                label .lap_dance_3:
                m "That's it, now just start moving your ass a little more."
                ">Luna starts forcefully grinding her supple ass against you."
                m "*mmmm*, that's it."
                call lun_main("...","upset","mad","sad","down")
                call lun_main("is this good?","normal","seductive","sad","R")
                m "yes, just keep going..."
                call lun_main("For how long?","upset","mad","sad","mid")
                m "As long as it takes, [luna_name]."
                call lun_main("fine...","upset","mad","sad","R")
                call lun_main("...","upset","mad","sad","down")
                call lun_main("..........","upset","suspicious","sad","down")
                call lun_main("Is there anything I can do to speed this up?","base","suspicious","sad","R")
                call lun_main("Not that I want it to end...","base","suspicious","sad","down")
                call lun_main("It's just that people will start to ask questions if--","normal","seductive","sad","R")

                menu:
                    "-Do nothing-":
                        $ current_payout = 75
                        m "*shhh*... Just keep doing what you're doing..."
                        call lun_main("...","clench","suspicious","sad","down")
                        call lun_main("How about this?","normal","seductive","sad","down")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "*Mmmm*, yes!"
                        ">You start thrusting into her ever so slightly."
                        call lun_main("...","pout","suspicious","sad","down")
                        m "That's it [luna_name], not much longer now."
                        call lun_main(".......","normal","seductive","sad","R")
                        m "*mmmm*, almost there..."
                        call lun_main("Already?","upset","wide","sad","R")
                        m "Almost... this is really good..."
                        call lun_main("it is?","base","seductive","sad","R")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call lun_main("...","base","seductive","sad","R")
                        call lun_main("How's this?","grin","seductive","sad","down")
                        ">Luna starts rubbing hard against your lap."
                        m "*mmmmm*"
                        call lun_main("You're so hard [lun_genie_name]...","base","seductive","sad","down")
                        m "*mmmm*"
                        call lun_main("are you almost there?","base","seductive","sad","R")
                        m "yes..."
                        call lun_main("well I expect to be--","upset","seductive","angry","R")
                        m "*shhh*, don't ruin it."
                        call lun_main("...","upset","mad","sad","R")
                        ">Luna starts rolling her hips, your cock pressed between her cheeks."
                        m "ah..."
                        call lun_main("...","upset","seductive","sad","R")
                        m "keep going [luna_name]..."
                        call lun_main("........","base","closed","sad","R")
                        m "*mmm*, just a little more..."
                        call lun_main("... [lun_genie_name]...","base","angry","sad","down")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}*mmmm*...{/size}"
                        call lun_main("......","base","suspicious","sad","mid")
                        g4 "{size=+4}(*agh*... almost there...){/size}"
                        call lun_main("............","base","suspicious","sad","mid",tears="soft")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."

                        call cum_block

                        g4 "*Argh*! YES!"
                        call lun_main("ugh...","base","seductive","sad","R")
                        call lun_main("...","upset","mad","sad","R")
                        call lun_main("......","normal","mad","sad","down")
                        call lun_main(".........","upset","seductive","sad","down")
                        call lun_main("Are you finished now, [lun_genie_name]?","base","seductive","sad","R")
                        m "Almost... just stay there for a little longer..."
                        call lun_main("Okay......","base","seductive","sad","down")

                        show screen blkfade
                        with d3

                        ">Luna waits for a few seconds before standing up."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("will that be all, [lun_genie_name]?","base","suspicious","sad","mid")
                        m "Yes, thank you, [luna_name]."
                        call lun_main("You're welcome, [lun_genie_name].","upset","angry","sad","R")
                        if daytime:
                            call lun_main("Well, I better be off to class then.","upset","mad","sad","mid")
                        else:
                            call lun_main("Well, I better be off to bed then.","upset","mad","sad","mid")
                        m "Don't you want your payment first?"
                        call lun_main("Oh right...","base","seductive","sad","R")

                    "-Grope her-" if luna_grope:
                        if lun_sub < 5:
                            $ lun_sub += 1

                        $ current_payout = 35

                        call lun_chibi_scene("sit_on_lap_grope")
                        with d3

                        ">You start running your hands along the outside of her thighs."
                        call lun_main("ah... {heart}","base","wide","sad","mid")
                        m "*mmmm*, lovely."
                        ">You keep grinding your cock against her butt cheeks."
                        call lun_main("....","clench","seductive","sad","down")
                        m "yes, just like that [luna_name]..."
                        "You move your hands to her knees, just at the edge of her skirt."
                        call lun_main("......","base","suspicious","sad","down")
                        m "gods you've got such nice legs."
                        call lun_main("t-thank you [lun_genie_name]...","normal","happyCl","sad","R",tears="soft")
                        ">You start slowly moving your hands towards her waist, pulling up her skirt slightly as you go."
                        call lun_main(".........","upset","suspicious","sad","R",tears="soft")
                        m "That's it [luna_name], just enjoy yourself..."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">You move your hands to the inside of her thighs."
                        m "*mmmm*, that's it..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">You start stroking the insides of her thighs, moving closer towards her pussy each time."
                        call lun_main("!!!!","clench","wide","mad","mid")
                        call lun_main("[lun_genie_name]...","upset","wide","mad","mid",tears="soft")
                        call lun_main("please...","normal","mad","mad","R",tears="soft")
                        m "just a bit longer [luna_name]..."
                        ">You start grinding your hard cock between her ample cheeks."
                        call lun_main("...","upset","wide","sad","down",tears="soft")
                        call lun_main("[lun_genie_name]...","upset","mad","angry","R",tears="soft")
                        ">You start lightly running your the tips of your fingers up and down her thighs."
                        call lun_main("ah... {heart}","upset","angry","sad","down",tears="soft")
                        call lun_main("[lun_genie_name]... this isn't right...","upset","angry","sad","R",tears="crying")
                        m "you don't seem to mind..."
                        call lun_main("(I'll let him keep going for a little bit more...)","normal","seductive","sad","down",tears="crying")
                        call lun_main("(Then I'll make him stop)....... ah... {heart}","soft","seductive","sad","down",tears="crying")
                        call lun_main("[lun_genie_name], how much longer do you need?...","upset","angry","sad","R",tears="crying")
                        m "Just a bit longer..."
                        ">Luna keeps rubbing her ass against your sensitive cock."
                        m "ugh, that's it [luna_name]."
                        call lun_main("p-please hurry, [lun_genie_name]...","upset","suspicious","sad","R",tears="crying")
                        m "I think I might know a way to speed this up."
                        call lun_main("really?","base","mad","sad","R",tears="crying")
                        call lun_main("what are--","soft","seductive","sad","R",tears="crying")
                        ">You quickly move your hands up and grab a hold of her supple breasts through her vest."
                        call lun_main("!!!!","clench","wide","mad","mid",tears="crying")
                        ">Luna's body quivers as her hips roll against you."
                        m "*mmm* that's it, [luna_name]..."
                        call lun_main("...","base","mad","sad","down",tears="crying")
                        m "I think someone's enjoying herself."
                        call lun_main("What?","base","mad","sad","R",tears="crying")
                        call lun_main("You think I enjoy this? Feeling your disgusting old cock grind against me?","base","mad","sad","down",tears="crying")
                        m "{size=-2}*ahhh*...{/size}"
                        call lun_main("while you paw at me like some filthy old pervert?","base","suspicious","sad","empty",tears="crying")
                        m "{size=+4}*aghhh*!{/size}"
                        call lun_main("you really are a filthy old man, aren't you...","base","suspicious","sad","R",tears="crying")
                        g4 "{size=+4}*Argh*! that's it, [luna_name]! here it comes!{/size}"
                        call lun_main("!!!!","clench","wide","sad","down",tears="crying")
                        ">You start shooting a massive load against Luna's ass"

                        call cum_block

                        g4 "*Argh*!"
                        call lun_main(".....","mad","wide","base","down",tears="crying")

                        show screen blkfade
                        with d3

                        ">Luna stands up from your lap."

                        call lun_chibi_scene("reset", "desk", "base")
                        call lun_main(xpos="mid", ypos="base", flip=False)
                        hide screen blkfade
                        with d3

                        call lun_main("*hmph*","base","suspicious","angry","mid",tears="crying")
                        m "ah... gods that was good"
                        call lun_main("I think I'd like to leave now [lun_genie_name]...","base","seductive","base","R",tears="soft")

            "-Ask Nicely-" if lun_dom >= lun_sub:
                if lun_dom < 4:
                    $ lun_dom += 1

                $ current_payout = 250
                m "can you please sit on my lap [luna_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("Alright, because you asked so nicely...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "*mmmm*"
                ">You start to feel yourself get hard against her ass."
                call lun_main("...","base","seductive","angry","down")
                call lun_main("You're pathetic...","base","seductive","angry","R")
                call lun_main("The world's greatest wizard...","base","seductive","base","R")
                call lun_main("More like the world's greatest pervert.","base","suspicious","angry","down")
                ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crotch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed, are you?","soft","seductive","angry","down")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","base","mad","angry","R")
                m "I don't recall begging."
                call lun_main("*Hmmm*...","base","seductive","angry","R")
                ">Luna stands up slowly."

                call lun_chibi_scene("reset", "by_desk", "back")
                call lun_main(xpos="mid", ypos="base", flip=False)
                with d3

                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","base","seductive","raised","mid")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forth on your lap"
                call lun_main("You're so hard...","base","seductive","mad","down")
                m "*mmmm*"
                call lun_main("I bet you'd cum if I kept going, wouldn't you...","base","seductive","raised","R")
                m "yes..."
                call lun_main("you better be prepared to pay extra for the privilege...","base","angry","angry","R")
                m "of course..."
                call lun_main("...","base","mad","angry","R")
                ">Luna starts rolling her hips, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","down")
                m "of course [luna_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","angry","R")
                m "*mmm*, just a little more..."
                call lun_main("pervert...","base","seductive","base","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}*mmmm*...{/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(*agh*... almost there...){/size}"
                call lun_main("Come for me...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."

                call cum_block

                g4 "*Argh*! YES!"
                call lun_main("*ugh*... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "*ugh*, that's enough now [luna_name]."
                call lun_main("Who says you get to decide when this ends?","upset","suspicious","angry","R")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "*ah*, please, not after I just came."
                call lun_main("really?","base","mad","raised","R")
                call lun_main("But you sounded so sincere earlier when you were begging for this.","soft","seductive","sad","R")
                call lun_main("Surely you don't want it to end already?","base","seductive","angry","R")
                ">she pushes hard against your cock."
                g11 "*ah*..."
                call lun_main("That's it pervert, just keep enjoying yourself.","base","mad","angry","down")
                g11 "I can't, it's too sensitive..."
                call lun_main("I don't see how that's my problem.","base","mad","sad","R")
                ">She starts moving as fast as she can."
                g11 "{size=-2}*ahhh*...{/size}"
                call lun_main("come on pervert...","base","suspicious","angry","R")
                g11 "{size=+4}*aghhh*!{/size}"
                call lun_main("shoot another filthy load...","base","suspicious","mad","R")
                g4 "{size=+4}*Argh*! It's too much!{/size}"
                call lun_main("{heart}{heart}{heart}","base","suspicious","mad","down")
                ">You start shooting another load against the inside of your sodden cloak."

                call cum_block

                g4 "*Argh*!"
                call lun_main("good boy...","base","seductive","mad","R")

                show screen blkfade
                with d3

                ">Luna stands up from your lap."

                call lun_chibi_scene("reset", "desk", "base")
                call lun_main(xpos="mid", ypos="base", flip=False)
                hide screen blkfade
                with d3

                call lun_main("*hmph* You nasty old pervert!","base","suspicious","angry","mid")
                m "*ah*..."
                call lun_main("Enjoy yourself a little too much did we?","base","angry","mad","R")
                m "That was too much [luna_name]..."
                call lun_main("Stop complaining. I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")

            "-Beg-" if lun_dom >= 3:
                if lun_dom < 4:
                    $ lun_dom += 1

                $ current_payout = 250
                m "can you please sit on my lap [luna_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("keep going...","base","suspicious","base","R")
                m "please, place your perfect little ass on my lap, princess..."
                call lun_main("that's better...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."

                call lun_chibi_scene("sit_on_lap")
                call lun_main(xpos="left", ypos="low", flip=True)
                with d3

                m "*mmmm*"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","angry","down")
                call lun_main("that's it [lun_genie_name]...","base","seductive","base","R")
                call lun_main("just sit back and enjoy yourself...","base","seductive","base","R")
                call lun_main("enjoy the feeling of your disgusting old cock rubbing against me...","base","suspicious","angry","down")
                ">Luna starts moving her hips back and forth."
                m "ah..."
                call lun_main("*hmph* that's it... tell me how good it feels.","soft","seductive","angry","down")
                m "w-what?"
                call lun_main("tell me how good it feels to rub that filthy cock of yours against me...","base","mad","angry","R")
                m "..."
                call lun_main("go on... or else...","base","seductive","angry","R")
                m "alright... I'll do it."
                call lun_main("good boy...","base","seductive","base","R")
                m "it's like I'm rubbing up against a...{w=0.5} cloud..."
                call lun_main("a cloud?","upset","seductive","raised","R")
                m "I mean it's soft..."
                ">Luna slowly grinds against your shaft."
                call lun_main("I suppose that's better than nothing...","base","angry","raised","R")
                m "*mmmm*, keep going [luna_name]..."
                call lun_main("pervert...","base","suspicious","mad","R")
                m "yes..."
                ">Luna starts rolling her hips, your cock pressed between her cheeks."
                m "{size=-2}*mmmm*...{/size}"
                call lun_main("Come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(*agh*... almost there...){/size}"
                call lun_main("Come for me...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."

                call cum_block

                g4 "*Argh*... YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, no more please [luna_name]."
                call lun_main("good boy...","base","seductive","mad","R")

                show screen blkfade
                with d3

                ">Luna stands up from your lap."

                call lun_chibi_scene("reset", "desk", "base")
                call lun_main(xpos="mid", ypos="base", flip=False)
                hide screen blkfade
                with d3

                call lun_main("*hmph* You're such nasty old [lun_genie_name]!","base","suspicious","angry","mid")
                call lun_main("But I suppose I don't mind, as long as I get my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")

        if lun_dom >= lun_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."

        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna {number=current_payout} gold."
        if current_payout <= 50:
            call lun_main("(only {number=current_payout}?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    else:
        # Fourth time, with Hermione
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "Can I offer you another seat [luna_name]?"
        call lun_main("so you want another lap dance...","normal","seductive","angry","mid")
        m "if it's not too much trouble..."
        call lun_main("not at all...","base","seductive","base","R")
        call lun_main("but just for fun... why don't you get hermione up here?","base","angry","sad","down")
        m "really?"
        call lun_main("...","normal","angry","angry","mid")
        m "Well, I'm not going to say no to that!"
        call lun_main("good... let me just get in position first...","base","seductive","angry","mid")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."

        $ luna_chibi.zorder = desk_zorder - 1
        call lun_chibi("stand", "by_desk", "back")
        call lun_main(xpos="left")
        hide screen blkfade
        with d3

        ">Luna lightly sits on your lap."

        call lun_chibi_scene("sit_on_lap")
        call lun_main(xpos="left", ypos="low", flip=True)
        with d3

        m "*mmmm*"
        ">You start to feel yourself get hard against her ass"
        call lun_main("go on... bring her up here...","upset","mad","angry","R")
        ">You summon Hermione up to your office."

        call her_walk(action="enter", xpos="desk", ypos="base")
        call ctc

        call her_main("hello [genie_name]!", "base", "closed", "base", "mid", xpos="base", ypos="base")
        call her_main("Hey Luna!{w=0.5} oh, has he got you on lap dance duty today then?", "smile", "happyCl", "base", "mid",emote="happy")
        call lun_main("if you can even call it that...","normal","seductive","angry","R")
        call lun_main("most of the time he just makes me grind up against him while he creams his robe...","base","base","base","down")
        call lun_main("I feel bad for the elves who have to clean it up...","base","mad","angry","down")
        ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crotch."
        call her_main("*mmm*, so what am I here for then?", "base", "narrow", "base", "mid_soft")
        m "*ah*... ask Luna..."
        call lun_main("I was thinking you could give him a little show while I grind a load out of him...","normal","wide","sad","R")
        call her_main("*mmmm*, what did you have in mind?", "base", "squint", "base", "mid")
        call lun_main("Playing with those nice tits of yours would probably do it...","base","base","sad","R")
        m "*ah*... yes..."
        call her_main("probably...", "base", "narrow", "worried", "down")
        call her_main("but are you sure it's just him who wants a show?", "base", "squint", "base", "mid")
        call lun_main("what?","open","wide","sad","mid", cheeks="blush")
        ">Luna starts bouncing faster on your lap."
        call lun_main("what are you talking about?","normal","wide","sad","down", cheeks="blush")
        call her_main("from the looks of it, you don't need any help cranking a nice big load out of him...", "open", "narrow", "worried", "down")
        call her_main("so the only reason you'd bring me up here, to show off my tits...", "base", "narrow", "base", "mid_soft")
        call her_main("is so you can get a look at them as well...", "base", "squint", "base", "mid")
        call her_main("not that I mind...", "smile", "base", "base", "R")
        $ hermione.strip("robe", "accessory")
        call her_main("I just want you to be honest...", "base", "happy", "base", "mid")
        call lun_main("...","normal","mad","sad","R", cheeks="blush")
        call lun_main("Fine...","upset","mad","sad","down", cheeks="blush")
        call her_main("say it...", "base", "squint", "base", "mid")
        call lun_main("I want to look at your boobs, alright!?","open","happyCl","sad","mid", cheeks="blush")

        ">Upon hearing those words, Hermione quickly removes her top and bra."

        $ hermione.strip("top", "bra")

        call her_main("see, that wasn't so hard now was it?", "base", "squint", "base", "mid")
        call lun_main("no...","base","seductive","sad","mid", cheeks="blush")
        ">Luna slows down, but starts grinding her mound hard against your cock."
        call her_main("why don't you two perverts just sit back and relax...", "base", "narrow", "worried", "down")
        call set_her_action("lift_breasts")
        call her_main("while I give you something fun to look at, okay?", "grin", "base", "base", "R")
        call lun_main("yes Hermione...","base","base","sad","mid", cheeks="blush")
        m "Yes..."
        call lun_main("*mmmmm*, he's so hard...","base","seductive","sad","down", cheeks="blush")
        call set_her_action("pinch")
        call her_main("I can imagine...", "grin", "narrow", "base", "dead")
        m "*ugh*..."
        call lun_main("he's probably going to cum soon...","base","mad","sad","R", cheeks="blush")
        m "probably..."
        call her_main("and what about you?", "base", "narrow", "base", "mid_soft")
        call set_her_action("covering")
        call her_main("how do you feel?", "base", "narrow", "worried", "down")
        call lun_main("so good...","base","seductive","sad","down", cheeks="blush")
        call lun_main("...","base","mad","sad","up", cheeks="blush")
        ">Luna tilts her hips back, grinding as much of her pussy against you as possible."
        ">you swear you can feel her wetness seeping through your robe."
        m "*ah*..."
        call set_her_action("pinch")
        call her_main("good...", "open", "base", "base", "R")
        call lun_main("*ah*...","base","angry","sad","up", cheeks="blush")
        ">Luna starts rubbing hard against your lap."
        m "{size=-2}*mmmm*...{/size}"
        call lun_main("yes...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("lift_breasts")
        call her_main("why don't you two see if you can cum together?", "base", "narrow", "base", "mid_soft")
        g4 "{size=+4}*agh*... almost there...{/size}"
        call lun_main("m-me too...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("pinch")
        call her_main("cum for me, you nasty perverts!", "base", "squint", "base", "mid")
        g4 "{size=+4}YES! YES! YES! *Argh!*{/size}"
        call lun_main("*ah*... {heart}{heart}{heart}","open","angry","sad","up", cheeks="blush")
        ">You start shooting your load against the inside of your cloak as you feel an explosion of wetness from Luna's pussy."

        call cum_block

        g4 "*Argh*! YES!"
        call lun_main("*ugh*... amazing...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("covering")
        call her_main("*mmmm*...", "base", "narrow", "base", "mid_soft", cheeks="blush")
        call lun_main("...","base","seductive","sad","up", cheeks="blush")
        call lun_main("......","base","angry","sad","down", cheeks="blush")
        call lun_main(".........","base","seductive","sad","R", cheeks="blush")
        ">Luna keeps rubbing her sensitive pussy slowly against your cock."
        g4 "*ugh*, that's enough now [luna_name]."
        call lun_main("alright...","normal","base","sad","down", cheeks="blush")

        show screen blkfade
        with d3

        ">Luna stands up from your lap."

        $ hermione.wear("top")
        $ hermione.wear("bra")

        call lun_chibi_scene("reset", "by_desk", "back")
        call lun_main(xpos="mid", ypos="base", flip=False)
        hide screen blkfade
        with d3

        #FIXME Ensure Luna + Hermione dolls do not overlap here

        call her_main("feel better you two?", "base", "narrow", "base", "mid_soft")
        call lun_main("yes...","base","mad","sad","up", cheeks="blush")
        m "ah... you sluts..."
        call her_main("well come on then Luna, we've got some studying to do. Can you pay us now, [genie_name]?", "base", "narrow", "worried", "down")

        m "Alright, alright. Here's your gold and points."
        $ gryffindor += 25
        $ ravenclaw += 25
        m "Fifteen points to Gryffindor and Ravenclaw."
        $ gold -= 80
        $ luna_gold += 40
        m "and here's your gold."
        ">You hand Luna and hermione forty gold each."
        call her_main("Thank you [genie_name]!", "base", "base", "base", "mid")
        call lun_main("... Thank you [lun_genie_name].","normal","seductive","sad","R")
        ">Luna and hermione leave your office, talking as they go."

        $ hermione_busy = True

    hide screen hermione_main
    hide screen luna_main
    with d3

    call gen_chibi("sit_behind_desk")
    pause.2

    call play_sound("door")
    call lun_chibi("hide")
    call her_chibi("hide")

    $ luna_busy = True

    call update_luna

    jump main_room
