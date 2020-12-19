label hg_wager_bj:
    g9 "Well if you want to avoid losing the points you could come over here and get on your knees."
    g9 "And put my dick in your mouth!"
    if her_whoring < 15:
        call her_main("I don't want to lose those points, but that is too much!", "angry", "base", "angry", "mid")
        call her_main("Isn't there anything else I could do?", "open", "base", "base", "mid")
        g4 "You're no fun!"
        g9 "Come over here and let me give your butt a squeeze, then I'll only deduct ten points from Gryffindor."
        if her_whoring < 9:
            call her_main("No! what kind of girl do you take me for [genie_name]!", "scream", "base", "angry", "mid")
            m "Fine, twenty points from Gryffindor!"
            $ gryffindor -= 20
            pause.5
            call her_chibi("leave","door","base")
        else:
            call her_main("Okay, I can do that...", "open", "base", "base", "mid_soft", cheeks="blush")
            call her_main("", "base", "base", "base", "mid_soft")
            g9 "Well, get over here then!"
            call her_walk("desk", "base", reduce=0.8)
            call blkfade
            call her_main("Should I turn around, [genie_name]?", "open", "happyCl", "worried", "mid")
            call her_main("", "upset", "base", "worried", "mid")
            m "No, not this time."
            call her_main("Okay then...", "annoyed", "narrow", "base", "R_soft")
            call gen_chibi("hide")
            call her_chibi_scene("behind_desk_front")
            with d1
            $ menu_x = 0.5
            $ menu_y = 0.3 # Menu is moved up.
            call hide_blkfade
            call ctc
            call her_chibi_scene("grope_ass_front")
            with d1
            m "Have you been working out [hermione_name]? This feels great!"
            call her_main("No... can we just get this over with?", "annoyed", "narrow", "base", "mid_soft")
            call her_main("{size=-5}All this because of a stupid card game{/size}.", "upset", "happyCl", "worried", "mid")
            m "I know, we should definitely do this again."

            if hg_strip.trigger: #If snape walked in during the dance favour.
                call play_music("dark_fog")

                call sna_walk(action="enter", xpos="mid", ypos="base")

                call sna_main( "Hello Geni--", face="snape_09")
                call sna_main( "What do we have here?!?", face="snape_20")
                call her_main("{size=+5}Professor Snape?!{/size}", "shock", "wide", "worried", "shocked", xpos="left",ypos="base")
                call her_main("It's not what it looks like!", "scream", "wide", "base", "R")
                hide screen hermione_main
                call sna_main( "So you're not having your headmaster feel you up?", face="snape_05")
                call sna_main( "And enjoying it, by the looks of it!", face="snape_02")
                call her_main("I knew playing another round of cards wasn't a good idea...", "mad", "happyCl", "worried", "mid", cheeks="blush")
                call her_main("...", "annoyed", "narrow", "annoyed", "mid", cheeks="blush")
                call her_main("Take your hands off me now!!", "scream", "closed", "angry", "mid", cheeks="blush")
                m "Fine, calm down miss Granger"
                call her_main("Don't tell me to calm down!!!", "scream", "base", "angry", "mid", cheeks="blush")
                hide screen hermione_main
                call sna_main("Don't feel as if you have to stop on my behalf.", face="snape_01")
                m "Fine, I'll stop... But I'm still taking twenty points from Gryffindor!"
                call her_chibi_scene("behind_desk_front")
                with d1
                ">You take your hands off Hermione"
                call gen_chibi("sit_behind_desk")
                call her_chibi("stand",410,"base", flip=True)
                call sna_main("The perfect Hermione Granger letting her headmaster feel her up over a card game and some house points!", face="snape_02")
                call sna_main("How sweet...", face="snape_03")
                call her_main("Can I leave now?", "annoyed", "narrow", "worried", "down", flip=True)
                m "You are excused miss Granger, but I will be taking twenty points from Gryffindor."
                $ gryffindor -= 20 #should take gryffindor points and then hermione leaves

                call her_walk(action="leave")

                call sna_main("How did you talk her into that?", face="snape_02")
                m "We made a bet involving house points and she lost, why did you have to barge your way in like that?"
                m "It was just getting good!"
                call sna_main("You should hang a tie on the door or something!", face="snape_03")
                call sna_main("How was I supposed to know you were busy with the girl?", face="snape_04")
                g4 "Just knock next time!"
                m "It's not like I know how to lock that door..."
                g4 "Can't a mythical creature feel up a schoolgirl in peace around here?"
                call sna_main("Fine, I'll leave you to it, the less I have to see that girl the better...", face="snape_06")

                call sna_walk(action="leave")

            else : #If she hasn't stripped twice.
                call her_main("No, it's bad enough doing this to gain house points, it's much worse to prevent losing them!", "clench", "narrow", "angry", "R")
                m "You don't enjoy it? Even a little?"
                call her_main("No, Sir. I'm just doing this to fix the problem I created...", "disgust", "narrow", "base", "mid_soft")
                m "Well, to each their own, I am enjoying this very much!"
                call her_main("Are you done yet?", "disgust", "narrow", "base", "R_soft")
                m "Fine, I'll let you go..."
                call her_chibi_scene("behind_desk_front")
                with d1
                m "I'll only take ten points from Gryffindor as we agreed."
                m "Ten Points from Gryffindor!"
                $ gryffindor -= 10
                call blkfade
                call her_chibi("stand","mid","base")
                call gen_chibi("sit_behind_desk")
                call hide_blkfade
                call her_main("Thank you, [genie_name].", "open", "base", "base", "mid")
                hide screen hermione_main
                with d3

                call her_walk(action="leave")

    else: #If her whoring is higher than 15 (when she can do blowjob favour)
        call her_main("Gryffindor really can't afford to lose twenty points...", "soft", "base", "worried", "mid")
        call her_main("Okay then, I'll do it.", "open", "closed", "base", "mid")
        if hg_pf_blowjob.points > 0: #if shes done the blowjob favour these show
            call her_main("Not like I haven't done it before.", "base", "happy", "base", "mid_soft", cheeks="blush")
            if her_whoring > 18:
                call her_main("And it does feel good having my mouth full of your cock...", "soft", "happyCl", "base", "mid", cheeks="blush")
        m "Get over here then!"
        call her_walk("desk", "base", reduce=0.8)
        call blkfade
        call play_music("playful_tension")
        hide screen hermione_main
        show screen chair_left
        call her_chibi_scene("bj")
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc
        call her_main("*Urk*, *Slurp*, *Gobble*", "open_wide_tongue", "closed", "base", "mid", ypos="head", flip=False) #should have her head showing while sucking his cock.
        m "Oh, that's great!"
        g4 "Put some work into it."
        call her_main("*Gulp*, *Gobble*, *Gltch*", "open_wide_tongue", "narrow", "worried", "mid_soft")
        m "Your mouth feels amazing, you're a natural!"
        call her_chibi_scene("bj_pause")
        call her_main("I'm glad you like it [genie_name].", "open", "happy", "base", "mid", cheeks="blush")
        call her_chibi_scene("bj")
        call her_main("*Gobble*, *Slurp*, *Gobble*", "open_wide_tongue", "closed", "base", "mid", cheeks="blush")

        call play_music("dark_fog")#Snape walks in

        call sna_walk(action="enter", xpos="mid", ypos="base")

        call sna_main("", face="snape_01",xpos="base",ypos="base")
        call ctc

        with hpunch
        call sna_main("I want a rematch!", face="snape_07")
        call her_chibi_scene("bj_pause")
        m "{size=-5}Don't stop, [hermione_name]...{/size}"
        g4 "What do you mean, rematch? I beat you fair and square!"
        call her_chibi_scene("bj")
        call her_main("*Slurp*, *Gulp*, *Urk*", "open_wide_tongue", "happyCl", "worried", "mid", cheeks="blush", ypos="head", flip=False)
        call sna_main("I'm certain you were cheating, my deck is way better than yours.", face="snape_06")
        call sna_main("Hold on... what's that noise?", face="snape_03")
        m "Probably ghosts...{w} This place must be haunted."
        g9 "And I'm better than you, just accept it."
        call her_main("*Gulp*, *Gobble*, *Gltch*", "open_wide_tongue", "happyCl", "worried", "mid", cheeks="blush")
        call sna_main("{size=-5}That doesn't sound like any ghost I've ever heard...{/size}", face="snape_01")
        call sna_main("Are you sure?", face="snape_05")
        call her_main("*Slurp*, *Gobble*, *Urk*")
        call sna_main("There it is again!", face="snape_25")
        m "Yes, definitely ghosts..."
        g9 "Are you changing the subject now because you can't accept the fact I beat you at wizard cards!"
        g4 "{size=-5}I'm about to cum [hermione_name]!{/size}"
        call her_main("*Gurk*, *Gulp*, *Gulp*", "open_wide_tongue", "base", "worried", "mid", cheeks="blush")
        call sna_main("No, something is going on here, what are you doing?", face="snape_07")
        m "... Just standing at my desk."
        hide screen snape_main
        menu:
        #Tell him not to worry about it.
        #Tell him the ghost is gone.
            "-Tell him not to worry about it-":
                g4 "There's nothing suspicious happening here...{w} {size=-5}Ugh!{/size}"
                pause.5
                call her_chibi_scene("bj_cum_in")
                call cum_block
                g4 "{size=+7}*ARGH*!{/size}"
                call her_main("...", "full", "wide", "worried", "stare")
                call sna_main("...", face="snape_25")
                g4 "..."
                call sna_main("*Hmm*...{w} it seems the weird sound is gone.", face="snape_04")
                m "Oh... yes, seems like it..."
                call sna_main("I bet it was peeves again...", face="snape_16")
                call sna_main("I'll leave you to it then...", face="snape_03")
                call her_main("...", "full_cum", "narrow", "base", "down", cheeks="blush")

                call sna_walk("door", "base") #snape walks to the door, pauses on gulp sound

                $ renpy.play('sounds/gulp.mp3')
                call her_main("{heart}*Gulp* {heart}", "cum", "narrow", "annoyed", "up")
                call sna_main("...", face="snape_07", flip=True)
                pause.2
                call blkfade
                $ renpy.play('sounds/07_run.mp3') #snape runs back and draws his wand
                hide screen snape_main
                $ snape_chibi.zorder = desk_zorder + 1
                call sna_chibi("wand_defend", "mid")
                pause 1
                hide screen blkfade
                $ renpy.music.play("music/Hitman.mp3")
                call her_chibi_scene("bj_pause")
                g4 "...?!"
                call sna_main("Reveal yourself! I won't let you harm him!", face="snape_10", wand=True)
                g4 "Severus, wait!"
                call sna_main("I knew something was wrong from the start, you can't hide from me, now reveal yourself or prepare to die!", face="snape_30", wand=True)
                if not hg_strip.trigger: #if hermione hasn't stripped twice
                    m "What are you doing Severus?"
                    call her_main("...", "soft", "base", "worried", "mid", cheeks="blush")
                    m "You're being very strange..."
                    g9 "I didn't know you cared so much about my well being..."
                    call sna_main("But... I swear I heard something...", face="snape_14", wand=True)
                    g4 "..."
                    call sna_main("I guess I must've imagined it... I'll just go then.", face="snape_14", wand=True)
                    call sna_chibi("stand","mid","base",flip=True) #snape turns and leaves
                    hide screen bld1
                    with d3
                    stop music fadeout 2

                else: #if hermione has stripped twice (so snape walked in on her)
                    show screen desk(437) # Desk was shifted during blowjob
                    call gen_chibi("dick_out", 260, 205+250)
                    call her_chibi("stand",220,"base", flip=True)
                    call sna_main("Miss Granger?! I thou-- I...", face="snape_14", wand=True)
                    hide screen snape_main
                    call sna_chibi("stand",460,"base")
                    $ renpy.music.play("music/Dark Fog.mp3")
                    if her_whoring > 20:
                        call her_main("Hello, Professor Snape.", "cum", "base", "base", "mid", xpos="left", ypos="base", flip=True)
                        call her_main("I was just giving the headmaster some help with an ‘itch'", "soft", "base", "base", "mid_soft", flip=True)
                        call sna_main("I see... I was expecting a poor excuse, your honesty is admirable...", face="snape_02")
                        call her_main("...", "base", "base", "base", "mid_soft", cheeks="blush", flip=True)
                        call sna_main("Well, in that case I hope you don't mind giving me a scratc...{w=1.0}{nw}", face="snape_13")
                    else: #whoring of 20 or less
                        call her_main("Oh, hello there professor...", "cum", "base", "worried", "mid", cheeks="blush", xpos="left", ypos="base", flip=True)
                        call her_main("I was just helping the headmaster with some cleaning under his desk.", "open", "happyCl", "worried", "mid", cheeks="blush")
                        $ random_choice = renpy.random.randint(0, 2)
                        if random_choice == 0:
                            call sna_main("Sure... And I live a double life as a death eater...", face="snape_02")
                        elif random_choice == 1:
                            call sna_main("Sure... And I'm the sheriff of Nottingham...", face="snape_02")
                        else:
                            call sna_main("Sure... And my name is {i}Hans Gruber{/i}...", face="snape_02")
                    m "I believe that your work is done Miss Granger, I'll refrain from deducting those points..."
                    call sna_main("Avoiding house point deductions are we? Is it that simple to get in your pants miss Granger?", face="snape_01")
                    call sna_main("If I had known...", face="snape_20")
                    call her_main("In your dreams...!", "mad", "narrow", "annoyed", "mid")
                    call sna_main("In any case, you're a lucky man... Albus.", face="snape_13")
                    call sna_main("I'll leave you two to it...", face="snape_02")
                    call sna_chibi("stand","mid","base",flip=True) #snape turns and leaves
                    hide screen bld1
                    with d3

                pause.2

                call sna_walk(action="leave")
                $ snape_chibi.zorder = 3

                pause.2
                m "Well, that was something..."
                $ uni_sperm = False
                if her_whoring < 20: #if she has lower whoring than 21
                    call her_main("That was mortifying!", "angry", "closed", "angry", "mid")
                    call her_main("How could you make me keep going?!?", "angry", "base", "angry", "mid")
                    m "Well, you were down there already, how could I not?"
                    call her_main("I can't believe you...", "angry", "closed", "angry", "mid")
                    call her_main("I'm going now, don't expect me to do anything for you any time soon!", "clench", "base", "angry", "mid")
                    $ her_mood += 10
                else: #if whoring is higher than 20
                    call her_main("The old me would have been embarrassed by that...", "clench", "narrow", "worried", "mid_soft", cheeks="blush")
                    call her_main("But I thought it was hot!", "grin", "happy", "base", "mid_soft", cheeks="blush")
                    g9 "I bet you did!"
                    call her_main("I can't believe that just happened!", "smile", "base", "base", "mid_soft")
                    m "You did a great job, I'll try to win even harder next time!"
                    call her_main("Thank you [genie_name]... Anyway, I must be going...", "open", "base", "base", "mid")
                    call blkfade
                    call her_chibi("stand","mid","base")
                    call gen_chibi("sit_behind_desk")
                    hide screen blkfade
                    if daytime:
                        call her_main("Bye then...", "smile", "base", "base", "mid")
                        m "Bye, [hermione_name]."
                    else:
                        call her_main("Good night.", "open", "base", "base", "mid")
                        m "Good night, [hermione_name]"
            "-Tell Him the ghost is gone-":
                g4 "Wait..."
                call her_main("*Glick*?", "open_wide_tongue", "wide", "base", "R")
                m "No, I think I should be able to exorcise these spirits myself..."
                call sna_main("You can do that?",face="snape_11")
                if her_whoring > 20:
                    call her_main("*Slurp*, *Slurp*, *Gobble*", "open_wide_tongue", "narrow", "annoyed", "up", cheeks="blush")
                    g4 "*Ghh*, of...{w=0.3} of course I can..."
                    call sna_main("I didn't think you could still use your powers like that...", face="snape_01")
                    call her_main("*Gltch*, *Slurp*, *Gobble*", "open_wide_tongue", "squint", "worried", "up", cheeks="blush")
                    g4 "What?{w} Oh, yeah...{w=0.2} of course I can, I've exercised plenty..."
                    call her_main("*Gulp*, *Gulp*, *Gobble*")
                    g4 "ARGH...{w} plenty!"
                    call sna_main("Are you...","snape_05")
                    menu:
                        "-Try to get him to Leave-":
                            g4 "Fine? Yes, I just need some concentration...{w} It'd be easier if you left me to it, the final expulsion could become quite messy..."
                            call her_main("...?", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
                            call sna_main("Well, I'd love to see that...","snape_02")
                            g4 "No...{w=0.4} *Gngh*...{w=0.2} Trust me, You don't...{w=0.4} Now, if you could..."
                            call sna_main("Fine, but you're going to have to teach me how to do that later...","snape_01")
                            g4 "Not sure if that's..."
                            call her_main("*Slurp*, *Slurp*, *Gobble*")
                            g4 "Oh, holy spirit that resides in this place..."
                            call her_main("*Slurp*, *Slurp*, *Urk*", "open_wide_tongue", "squint", "worried", "up", cheeks="blush")
                            g4 "Please help me release this anguish...{w} I mean, let me help release you from this anguish."
                            call sna_main("Well, you seem to know what you're doing so I'll leave you to it...","snape_05")
                            hide screen bld1
                            with d3
                            pause.2

                            call sna_walk(action="leave")

                            g4 "And not a moment to soon.... Take this you whore!"
                            call her_chibi_scene("bj_cum_in")

                            call cum_block
                            pause 1
                            call her_chibi_scene("bj_pause")
                            call her_main("*Mmmh*!!", "full_cum", "wide", "base", "stare", cheeks="blush")
                            $ renpy.play('sounds/gulp.mp3')
                            call her_main("{heart}*Gulp* {heart}", "cum", "narrow", "annoyed", "up")
                            m "Who said you could continue?"
                            call her_main("From my perspective it looks like you appreciated the initiative...", "cum", "base", "base", "mid_soft")
                            m "..."
                            m "Fine, I won't deduct those points..."
                            call her_main("Thank you...", "smile", "base", "base", "mid")
                            call blkfade
                            call her_chibi("stand","mid","base")
                            call gen_chibi("sit_behind_desk")
                            hide screen blkfade
                            call her_main("In that case I'll take my leave...", "smile", "happy", "base", "mid_soft", ypos="base")
                            call her_chibi("leave","door","base")
                            g9 "That girl..."
                        "-Let her keep going and deal with the aftermath-":
                            m "Yeah... I'm good."
                            call her_main("*Slurp*, *Slurp*, *Gobble*")
                            call sna_main("Is there anything I could assist with?","snape_04")
                            with hpunch
                            g4 "{size=+7}What?!?{/size}"
                            call her_main("...?", "open_wide_tongue", "wide", "worried", "stare", cheeks="blush")
                            call sna_main("With the exorcism...", face="snape_05")
                            m "Oh..."
                            call her_main("*Slurp*, *Slurp*, *Slurp*", "open_wide_tongue", "happyCl", "worried", "mid", cheeks="blush")
                            m "No... It's all good... I can feel the ghostly presence being expelled as we speak..."
                            g4 "Now take this you whore!"
                            call her_chibi_scene("bj_cum_in")
                            call cum_block
                            g4 "..."
                            call sna_main("...",face="snape_14")
                            m "..."
                            call sna_main("I had no clue exorcism would be this...",face="snape_03")
                            call sna_main("Extreme...","snape_02")
                            g9 "Hah, yeah...{w=0.3} But I've done this plenty of times..."
                            m "Actually, there's quite a bit of ghostly residue I have to deal with now so it might be best if..."
                            call sna_main("Whatever, I'd just leave it to the house elves...","snape_03")
                            m "It's not as simple as it may seem, it's not like warm water is going to do it..."
                            call sna_main("Fine, I'll head off in that case.","snape_01")
                            hide screen bld1 #should go black
                            with d3
                            pause.2

                            call sna_walk(action="leave")

                            m "You can come out now [hermione_name]..."
                            call her_chibi_scene("bj_pause")
                            call her_main("Thank you for your ghostly residue, [genie_name]", "cum", "narrow", "worried", "mid_soft")
                            m "You're welcome, I can't believe he bought it..."
                            call her_main("What do you expect from the head of Slytherin?", "crooked_smile", "narrow", "base", "R_soft")
                            m "yes...{w=0.3} Well...{w=0.3} I think that's enough for today."
                            call blkfade
                            call her_chibi("stand","mid","base")
                            call gen_chibi("sit_behind_desk")
                            hide screen blkfade
                            call her_main("", "base", "happy", "base", "mid_soft", ypos="base")
                            m "You've done more than enough to save those points."
                            call her_main("Thank you, [genie_name].", "smile", "happy", "base", "mid_soft")
                            if daytime: #should play if day time
                                call her_main("Bye then...", "open", "base", "base", "mid")
                                m "Bye, [hermione_name]."
                            else:
                                call her_main("Good night.", "open", "base", "base", "mid")
                                m "Good night, [hermione_name]"
                            $ uni_sperm = False
                        "-Try something crazy- {image=interface/cards.webp}":
                            m "Oh yes, I'm...{w=0.3} ugh...{w=0.3} fine."
                            m "But for some reason I feel like playing some cards."
                            call sna_main("In a moment like this?", face="snape_02")
                            m "Yes, I think the ghost may have been a gambler during their lifetime..."
                            jump bj_duel_game
                else: #whoring not higher than 21
                    call her_chibi_scene("bj_pause")
                    call her_main("*Mmphaa*...", "open_tongue", "narrow", "annoyed", "up")
                    m "Hold on...{w} Yes, I think the ghostly presence has departed..."
                    call sna_main("Already?",face="snape_05")
                    g4 "Yes, they must've felt how powerful my exorcism abilities were and moved on somewhere else..."
                    call sna_main("Well that's no fun... I was hoping to see it happen for myself.",face="snape_03")
                    m "Trust me, there's not going to be any watching going on here..."
                    call sna_main("...",face="snape_05")
                    call sna_main("Anyway, I was coming to see if you were up for another round of cards...", face="snape_01")
                    call sna_main("But I suppose you're quite spent after that whole ordeal.", face="snape_02")
                    #
                    #
                    menu:
                        "\"*Hmm*.. Actually..\" {image=interface/cards.webp}":
                            g9 "I don't see why not... I don't have anything else going on at the moment..."
                            label bj_duel_game:
                            call her_main("...", "open_wide_tongue", "narrow", "annoyed", "mid")
                            call her_chibi_scene("bj")
                            call her_main("*Slurp*, *Slurp*, *Gobble*")
                            g4 "*Gngh*..."
                            call sna_main("In that case, let's begin...", face="snape_02")
                            # Gamestart
                            call snape_special_duel
                            # After game
                            call her_chibi_scene("bj_cum_in")
                            call cum_block
                            pause 3
                            if duel_response == "draw":
                                m "I'm spent..."
                                call sna_main("So no rematch?", face="snape_05")
                                g4 "Wha--"
                                m "Yes, definitely no rematch..."
                                m "I'm not sure I could handle another one of those for at least thirty minutes..."
                                call sna_main("That's oddly specific...", face="snape_04")
                                m "You're oddly specific..."
                                call sna_main("...", face="snape_03")
                                m "I don't know what that means..."
                                call sna_main("I feel like understand you less and less by the day...", face="snape_01")

                                call sna_walk(action="leave")

                                call her_chibi_scene("bj_pause")
                                call her_main("So, no rematch then?", "crooked_smile", "narrow", "base", "mid_soft")
                                g9 "As I said, at least not for another thirty minutes..."
                                call her_main("So I assume I'm not losing those points anymore?", "open", "narrow", "worried", "mid_soft")
                                m "Definitely not..."
                                if daytime:
                                    call her_main("Great, goodbye for now then [genie_name]...", "base", "base", "base", "mid")
                                else:
                                    call her_main("Great, good night then... [genie_name].", "base", "base", "base", "mid")
                                m "{size=-8}That girl is crazy...{/size}"
                            elif duel_response == "loss" or duel_response == "Close":
                                call sna_main("Yes... I knew I'd make you bust this time!", face="snape_02")
                                m "Trust me..."
                                m "You had nothing to do with that..."
                                call sna_main("Sure I didn't, how about you hand me a bottle of that fine wine to celebrate the occasion...", face="snape_20")
                                label bj_duel_game_menu:
                                menu:
                                    "{color=[menu_disabled]}-Give him the bottle-{/color}" if wine_ITEM.number <= 0:
                                        "> You don't have any bottles of wine left"
                                        jump bj_duel_game_menu
                                    "-Give him the bottle-" if wine_ITEM.number > 0:
                                        $ wine_ITEM.number -= 1
                                        g4 "Fine..."
                                        g9 "I feel like I won in the end anyway..."
                                        call sna_main("That literally makes no sense...", face="snape_04")
                                        call sna_main("You clearly can't overcome the dreading feeling of such an explosive victory...", face="snape_02")
                                        m "Something like that..."
                                        m "Just take the wine and leave..."
                                        m "I need to reflect on my previous life decisions."

                                        call sna_walk(action="leave")

                                        m "Get out of there... life decisions."
                                        call her_chibi_scene("bj_pause")
                                        call her_main("Happy?", "normal", "happyCl", "base", "mid", cheeks="blush")
                                        m "I just lost the game and one of my bottles of wine..."
                                        call her_main("And a higher than average amount of 2 to 5ml by the looks of it...", "open", "narrow", "worried", "down", cheeks="blush")
                                        g9 "That is true..."
                                        call her_main("are you still deducting those points [genie_name].", "normal", "narrow", "base", "down", cheeks="blush")
                                    "-Don't give him anything-":
                                        m "Get out..."
                                        call sna_main("Someone's a sore loser...", face="snape_13")
                                        m "Aching..."
                                        m "Now get out..."
                                        if sna_friendship >= 30:
                                            call sna_main("Fine, but next time I'm playing you for one of those bottles...", face="snape_03")
                                        else:
                                            call sna_main("Fine...", face="snape_03")

                                        call sna_walk(action="leave")

                                        call her_chibi_scene("bj_pause")
                                        call her_main("Happy?", "normal", "happyCl", "base", "mid", cheeks="blush")
                                        g4 "What are you talking about? How could I be happy in a moment like this..."
                                        call her_main("But I just made you...", "open", "base", "worried", "mid", cheeks="blush")
                                        g4 "I just lost that god damn game cause I couldn't concentrate!"
                                        call her_main("Well, I did what you asked me!", "mad", "narrow", "angry", "R", cheeks="blush")
                                        call her_main("So I'd very much appreciate if you didn't deduct those points!", "open", "closed", "angry", "mid", cheeks="blush")
                                menu:
                                    "-Only deduct the twenty-":
                                        g4 "You should be happy that I'm not deducting more!"
                                        g4 "Twenty points from Gryffindor!"
                                        $ gryffindor -= 20
                                        call her_main("...", "base", "base", "angry", "mid")
                                        call her_main("What ever...", "open", "closed", "angry", "mid")
                                        $ her_mood += 15
                                    "-Deduct even more-":
                                        m "Oh, don't you worry..."
                                        call her_main("...")
                                        g4 "Forty points from Gryffindor!"
                                        $ gryffindor -= 40
                                        call her_main("What, you can't do that!", "shock", "wide", "worried", "stare")
                                        g4 "Of course I can, I'm the headmaster!"
                                        call her_main("I can't believe you've done this...", "mad", "base", "angry", "mid")
                                        m "Suck it up..."
                                        call her_main("{size=-5}That's what I did...{/size}", "open", "narrow", "annoyed", "mid", cheeks="blush")
                                        m "Excuse me?"
                                        call her_main("Never mind...", "clench", "narrow", "angry", "R")
                                        $ her_mood += 25
                                    "-Let her go-":
                                        m "No, I feel like I've reached a net gain somehow during this whole ordeal..."
                                        call her_main("...", "normal", "base", "base", "mid")
                                        m "A net gain is when...{nw}"
                                        call her_main("I know what it means...", "open", "narrow", "base", "mid_soft")
                                        m "Right."
                                        if daytime:
                                            call her_main("good day to you then sir.", "base", "base", "base", "mid")
                                        else:
                                            call her_main("Good night then...", "base", "base", "base", "mid")
                            else:
                                call sna_main("...", face="snape_18")
                                g4 "Did I say that aloud?"
                                call sna_main("Yes...", face="snape_12")
                                m "I meant to say bore..."
                                m "Take that..."
                                call sna_main("...", face="snape_05")
                                m "You bore..."
                                call sna_main("...", face="snape_05")
                                call sna_main("What kind of trash talk is that... seriously, you need to step up your game.", face="snape_06")
                                m "No you..."
                                call sna_main("That's fair...", face="snape_03")
                                call sna_main("I'll take my leave in that case...", face="snape_01")

                                call sna_walk(action="leave")

                                call her_chibi_scene("bj_pause")
                                call her_main("Did you just call me a...{nw}")
                                m "Snape..."
                                # Easter egg start
                                $ tried_rollback = False
                                show screen rollback_check
                                $ renpy.block_rollback()
                                m "If you {w=0.25}{b}{u}{i}scrolled back{/i}{/u}{/b}{w=0.25} you'd clearly see that I called Snape that..." ####
                                #***Goes back to reality***
                                label hg_wager_bj_secret_end:
                                if not tried_rollback:
                                    hide screen rollback_check
                                    $ renpy.block_rollback()
                                    call her_main("If I do what back?", "annoyed", "narrow", "base", "mid_soft")
                                    m "Never mind..."
                                else:
                                    $ achievement.unlock("flashback")
                                    call her_main("........", "annoyed", "narrow", "worried", "down")
                                m "We're done for today [hermione_name]."
                                call her_main("What about the points...", "annoyed", "narrow", "worried", "down")
                                g4 "Points?"
                                g9 "Oh yes, the points!"
                                g9 "Twenty points to Gryffindor..."
                                $ gryffindor += 20
                                call her_main("That's not...", "normal", "narrow", "base", "down")
                                call her_main("Thank you...", "open", "closed", "base", "mid")
                                if daytime:
                                    call her_main("Goodbye then [genie_name].", "base", "base", "base", "mid")
                                else:
                                    call her_main("Good night then [genie_name].", "base", "base", "base", "mid")
                            call blkfade
                            hide screen blkfade
                            jump end_hermione_event
                        "\"I'll pass\"":
                            pass
                    #
                    #
                    m "Yes, I'm not in the mood now anyway..."
                    call sna_main("...",face="snape_05")
                    call sna_main("I'll just go then.",face="snape_01")
                    hide screen bld1
                    with d3
                    pause.2

                    call sna_walk(action="leave")

                    m "..."
                    g4 "... Why did you stop?"
                    call her_main("What?", "annoyed", "narrow", "annoyed", "mid")
                    call her_main("I thought you wanted me to...", "clench", "narrow", "worried", "down")
                    m "If I wanted you to then I would've said so..."
                    call her_main("I could continue if you want me to...", "soft", "base", "base", "mid_soft")
                    m "No, the mood's ruined now..."
                    call her_main("Are you still taking those points away?", "open", "base", "base", "mid")
                    menu:
                        "-No-":
                            m "No, you're excused..."
                            call her_main("Thank you professor...", "smile", "happy", "base", "mid_soft")
                        "-Yes-":
                            g4 "Of course I am, you didn't finish the job!"
                            call her_main("...", "annoyed", "wide", "base", "stare")
                            call her_main("But, Snape was going to...", "open", "happyCl", "worried", "mid")
                            call her_main("...", "upset", "narrow", "worried", "down")
                            call her_main("Fine...", "clench", "narrow", "annoyed", "mid")
                            m "Twenty Points from Gryffindor!"
                            $ gryffindor -= 20
                            $ her_mood += 10

        $ hg_pf_blowjob.points += 1
        $ hg_pf_blowjob.counter += 1
        $ achievement.unlock("headlib")
    call blkfade
    hide screen blkfade

    jump end_hermione_event

label hg_wager_bj_secret:
    hide screen rollback_check
    hide screen hermione_main
    call blkfade
    $ renpy.block_rollback()
    call her_chibi_scene("bj")
    call sna_chibi("stand",460,"base")
    pause 1.0
    show screen hg_wager_bj_secret
    call hide_blkfade
    $ renpy.block_rollback()
    g9 "Yeeeeees!{w=0.5}{nw}"
    call cum_block
    g4 "Go fuck yourself Snape, take that you fucking whore!"
    call sna_main("...", face="snape_11")
    g9 "Yeah! What do you have to say about that... Slut!"
    call sna_main("...", face="snape_11")
    g9 "Slam dunk!"
    g9 "Another victory in the bag, eat my shit!"

    call blkfade
    call her_chibi_scene("bj_pause")
    call sna_chibi("hide")
    hide screen snape_main
    hide screen hg_wager_bj_secret
    pause 1.0
    call hide_blkfade

    $ renpy.block_rollback()
    g9 "\"And then I totally just shat all over the game board...\""

    jump hg_wager_bj_secret_end

screen hg_wager_bj_secret():
    zorder 4
    add im.MatrixColor("images/rooms/overlays/g_circular.webp", im.matrix.saturation(0.0)*im.matrix.brightness(0.7))

    text "Replay" pos (50, 50) size 40 color "#FFF" outlines [(5, "#000", 0, 0)] at blink

screen rollback_check():
    tag rollback_check
    if not tried_rollback:
        key "rollback" action [SetVariable("tried_rollback", True), Jump("hg_wager_bj_secret")]
