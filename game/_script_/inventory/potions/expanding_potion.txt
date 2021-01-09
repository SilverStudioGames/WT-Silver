# Breast expansion - Until chibis are added for it tifucking won't be written (ayylmao)
label potion_scene_2_1_1:
    m "Guess what I have for you today."
    call her_main("Is it another foul tasting potion that will try transform me into a hideous animal?", "open", "closed", "angry", "mid")
    m "Well I mean this one smells nice."
    call her_main("Will it taste nice though?", "open", "base", "base", "mid")
    m "Only one way to find out."
    call nar(">You hand her the potion and she brings it up to her nose.")
    call her_main("Well you're right, it does smell good. Let's find out if it tastes good...", "base", "base", "base", "mid")
    call her_chibi("drink_potion","mid","base")

    call nar(">She drinks the potion at a leisurely pace.")
    call her_main("Ahhh.", "base", "happyCl", "base", "mid")
    call her_main("", "smile", "narrow", "base", "mid_soft")
    call her_chibi("stand","mid","base")

    her "That wasn't actually that bad."
    call her_main("So, now that I've had the potion, will you tell me what it's supposed to do?", "angry", "wink", "base", "mid")
    m "No need to ruin the fun, it should take effect relatively quickly."
    call her_main("Well what am I supposed to do until then?", "base", "narrow", "base", "mid_soft")
    m "You could show me your tits."
    call her_main("I don't think so [genie_name], you're only paying me for drinking the potion.", "open", "closed", "base", "mid")
    call her_main("If you expect to see me without my shirt on then you'll have to try a little harder.", "base", "squint", "base", "mid")
    m "Oh I wouldn't be so sure of that."
    call her_main("So is that what it does? Makes me show you my breasts? Is it some sort of mind control potion?", "base", "base", "base", "mid")
    m "Mind control? Where's the fun in that? No, this is something much more entertaining."
    call her_main("Well it better happen soon otherwise I'm lea--", "annoyed", "narrow", "angry", "R")
    call nar(">You notice her breasts start to expand ever so slightly.") #Start using facial expressions mixed with Captain Nemo art
    call her_main("...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("As I said, something better happen soon or I'm leaving.", "annoyed", "base", "worried", "R")
    m "I wouldn't worry about it, from the looks of it, it's already started."
    call her_main("Why, what's wrong with me?", "open", "base", "base", "mid")
    m "There's nothing wrong with you. If anything, it's an improvement."
    call her_main("What is?", "annoyed", "narrow", "annoyed", "mid")
    call nar(">She starts patting down her body. Checking to see if she has grown any new ears or a tail.")
    call her_main("I don't see what you could be...", "open", "narrow", "worried", "down")
    call nar(">She grabs her breasts to check them.")
    call her_main("!!!", "angry", "narrow", "base", "down")
    call her_main("Have my breasts gotten bigger?", "angry", "wide", "base", "stare")
    m "About time you noticed."
    call her_main("Why would you make my breasts bigger? They're already big enough!", "angry", "base", "base", "mid")
    m "You know what they say, can't have too much of a good thing."
    call her_main("It's the other way around [genie_name].", "annoyed", "narrow", "annoyed", "mid")
    m "Is it? Well I prefer my version."
    call her_main("Well how big are they supposed to--", "angry", "narrow", "base", "down")
    call nar(">Her breast swell up again.")
    call her_main("You can't be serious. At this rate they're going to rip my shirt.", "angry", "wide", "base", "stare")
    m "Well they should stop there."
    call her_main("Good, they're big enough as is.", "angry", "base", "angry", "mid")

    menu:
        "-Send her to class-":
            m "You're right, I suppose they are big enough."
            m "Well that's all for today, twenty points to Gryffindor."
            call her_main("That's all? You're not going to make me do something else?", "shock", "wide", "base", "stare")
            m "Why would I, I asked you to drink a potion and you drank it. You're free to leave."
            call her_main("Thank you [genie_name], I'll head back to my room.", "smile", "base", "base", "R")
            m "Room? It's time for class [hermione_name]. What do you think Professor Snape will say once he hears that you skipped class?"
            call her_main("Well I can't be expected to go like this.", "disgust", "narrow", "base", "mid_soft")
            m "Why not? Everything is covered."
            call her_main("Barely. And what will people think of me.", "angry", "narrow", "base", "down")
            m "Just tell them that you are still developing. I'm sure that they're used to enormous breasts anyway, what's a few extra sizes."
            call her_main("... Fine. Just promise me that they won't get any bigger.", "upset", "closed", "base", "mid")
            m "I can't promise that, you're still in school. A lot of girls don't stop growing until they're thirty."
            call her_main("You know what I mean [genie_name].", "scream", "base", "angry", "mid", emote="angry")
            m "I'm afraid that I don't, [hermione_name], now you'd best hurry if you don't want to be late."
            call her_main("... Yes [genie_name].", "annoyed", "narrow", "annoyed", "mid")

            call her_walk(action="leave")

            $ hermione_busy = True

            call set_her_action("expand_breasts")

            jump main_room
            # End scene

        "-Play with her breasts-": #TODO Whoring check
            pass

    m "Well that's a matter of personal opinion."
    m "Now how would you like to earn some additional points?"
    call her_main("I want an extra 40.", "annoyed", "narrow", "annoyed", "mid")
    m "I haven't even told you what I want to--"
    call her_main("If you want to touch my breasts it will be an extra forty points.", "annoyed", "narrow", "angry", "R")
    m "Deal."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call nar(">Hermione walks over to behind your desk, her breasts swaying rhythmically as she moves.")
    pause .8

    hide screen hermione_main
    # call set_her_action("lift_top")
    call her_chibi_scene("grope_tits")
    call hide_blkfade

    call her_main("Well...", "upset", "wink", "base", "mid",xpos="mid",ypos="base")
    call nar(">You reach out and grab her breasts through her stretched shirt.")
    call her_main("!!!", "angry", "wide", "base", "stare")
    call her_main("Please be gentle [genie_name]. They seem to be much more sensitive than usual, it must be the potion.", "angry", "base", "base", "mid")
    m "Well I'll take that into account..."
    call nar(">You take a breast in each hand and start kneading them with your fingers.")
    call her_main("...", "open", "closed", "base", "mid")
    m "They're certainly much larger than usual."
    call her_main("... yes", "soft", "narrow", "annoyed", "up")
    call nar(">You continue massaging them gently through her shirt. Pulling them apart and then pressing them into one another.")
    call her_main("... It feels like they're getting--", "angry", "narrow", "base", "down")
    call ctc

    call set_her_action("expand_breasts")
    with vpunch

    call her_main("!!!", "angry", "wide", "base", "stare")
    call her_main("You said that they wouldn't get any bigger! Now how would you explain this?!", "scream", "base", "angry", "mid",emote="angry")
    m "Don't worry about that [hermione_name], worry about earning your forty points."
    call her_main("Just hurry up.", "annoyed", "narrow", "annoyed", "mid")
    menu: # TODO Add titfuck writing here
        # "-Suck her nipples-":
        #     pass
        # "-Titfuck her-":
        #     m "Well come here then!"
        #     hide screen hermione_main
        #     call blkfade
        #     jump start_titfuck
        "-Play with her nipples-":
            pass

    call nar(">You take her exposed breasts back into your hands and continue massaging")

    call her_main("sir... they seem to have become more sensitive...", "base", "narrow", "base", "up")
    call her_main("Please don't do anything sudden.", "soft", "narrow", "annoyed", "up")
    m "Like this?"
    call nar(">You take both nipples between your thumb and index finger.")
    call her_main("!!!", "scream", "wide", "base", "stare")
    call her_main("Please stop... it's too much, it's like my nipples are on fire.", "shock", "happyCl", "worried", "mid")
    m "Shhhh, just be still, it'll all be over soon."
    call nar(">You start rolling her nipples in between your fingers.")
    call her_main("...", "open", "happyCl", "worried", "mid")
    call nar(">You feel her push her crotch against your thigh.")
    m "Feeling a little aroused are we?"
    call nar(">You start to pinch and pull her nipples.")
    call her_main("Ohhh...", "soft", "narrow", "annoyed", "up")
    call nar(">She starts grinding herself against your thigh.")
    m "Well, well, well, you are sensitive now aren't you? Trying to grind out an orgasm on your headmaster's leg, how shameless."
    call her_main("...", "grin", "narrow", "base", "dead")
    m "Well let's see if we can do something about that."
    call nar(">You start alternating pinching and pulling her nipples hard, pulling the nipples out as far as you can and then pushing them back into her breast.")
    call her_main("!!!", "scream", "wide", "base", "stare")
    her "I-I-I'm cumming!"
    call nar(">She starts grinding hard against your leg as a wet spot starts to form on her skirt.")
    m "What a naughty little slut."
    call nar(">She breathes heavily as she rests against you")

    call blkfade
    pause 1
    hide screen hermione_main
    hide screen blktone
    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    pause.5

    call her_main("Will... that be all [genie_name]?", "soft", "narrow", "annoyed", "up")
    m "Yes [hermione_name]. You can go now."
    pause.2

    call her_walk(action="leave")

    $ her_potions_drunk.add("expansion")
    $ her_potions_drunk.add("breast_expansion")

    $ hermione_busy = True

    jump main_room

# Breast expansion return
label potion_scene_2_1_2:
    #TODO Event: Hermione comes back after having her breasts expand in class


# Ass expansion
label potion_scene_2_2:
    m "[hermione_name], I have another potion for you to try today."
    call her_main("Another one? Where are you getting these?", "open", "squint", "base", "mid")
    m "That's of no concern to you. What should concern you is the twenty points that you are able to earn should you drink it."
    call her_main("... Fine, give me the bottle.", "normal", "squint", "angry", "mid")
    call nar(">She takes a quizzical smell of the bottle.")
    call her_main("At least this one smells good.", "base", "base", "base", "mid")

    call her_chibi("drink_potion","mid","base")
    pause 2

    call nar(">She drinks the whole potion over a series of gulps.")

    call her_chibi("stand","mid","base")
    pause.5

    call her_main("Ahhh, that was good! So what was it?", "grin", "happyCl", "worried", "mid",emote="sweat")
    m "The effects should be visible soon enough."
    call her_main("Well can you at least give me a hint?", "open", "base", "base", "mid")
    m "Let's just say that it's a redistribution of ass{w}ets." ###Added {w} instead of your ...
    call her_main("What do you mean by--", "annoyed", "narrow", "angry", "R")
    call nar(">Hermione turns pale as she starts to feel her body churn.")
    call her_main("What's going on. It feels like my insides are moving.", "angry", "wide", "base", "stare")
    call her_main("And my ass, it feels so... good.", "soft", "narrow", "annoyed", "up")
    call nar(">You start to notice her ass increase in size.") #Use bigger butt from Captain Nemo
    call her_main("It feels too sensitive... I have to take my skirt off", "angry", "wide", "base", "stare")

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("panties")
    call set_her_action("lift_skirt")
    pause.5

    $ hermione.strip("bottom")
    call set_her_action("none","skip_update")

    call her_main("", "silly", "slit", "worried", "ahegao",cheeks="blush")
    pause.8

    call her_main("", "soft", "wide", "base", "stare")
    call ctc

    call her_main("Something is happening with my body, [genie_name]!", "open", "narrow", "base", "down")
    call ctc

    call set_her_action("expand_ass")
    with vpunch

    call her_main("", "angry", "narrow", "base", "down")
    call ctc


    call her_main("ughhh, my ass has gotten bigger!", "angry", "narrow", "base", "down")
    call her_main("Is that what this potion's supposed to do? Making my ass big?", "upset", "closed", "base", "mid")
    m "Evidently."
    call her_main("Why does my ass feel so good?", "soft", "narrow", "annoyed", "up") #new
    call nar(">Hermione keeps rubbing her ass, rolling her fingers across her expanded buttocks.")
    m "*Hmm*... It's not supposed to, but I guess every case is different."
    call her_main("It's just so sensitive... [genie_name] do you think that you could... massage me?", "grin", "narrow", "base", "dead")
    m "Well I mean I'm hardly going to say no am I."
    hide screen hermione_main
    hide screen bld1
    with d3

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call nar(">Hermione hops over to your desk, her ass bouncing as she moves, and presents herself to you.")
    pause 1

    call her_chibi_scene("behind_desk_back")
    call hide_blkfade
    call ctc

    show screen bld1
    show screen blktone
    call her_main("Please [genie_name]... please take advantage of me...", "open", "happyCl", "worried", "mid",xpos="mid",ypos="base")
    m "As you command."
    call nar(">You take her engorged buttocks in your hands. Each one is now much larger than before.")

    call her_chibi_scene("grope_ass_back")
    with d3

    m "Well this potion certainly is effective."
    call nar(">You start firmly stroking her ass cheeks. Pulling them apart to reveal her asshole and then squishing them together.","start")
    call nar(">Seeing her tight asshole gives you an idea.","end")

    menu: #Thought about adding a rimming option here but the chibis don't really support it
        "-Finger her asshole-":
            call nar(">You pull her asscheeks open again to show her puckered hole.")
            m "Let's see how sensitive you really are."
            call nar(">You start teasing the entrance with your finger, circling the entrance slowly.")
            call her_main("!!!", "shock", "happyCl", "worried", "mid")
            call her_main("[genie_name] please... I'm too sensitive. If you do that, \nI'm not sure I'll be able to control myself.", "soft", "narrow", "annoyed", "up")
            hide screen hermione_main
            m "Well in that case..."
            call nar(">You slowly pull your finger away from her asshole.")
            call her_main("Thank you--", "soft", "narrow", "annoyed", "up")
            call nar(">And then fully insert it.")
            call her_main("...", "angry", "wide", "base", "stare")
            her "..."
            her "..."
            call her_main("{size=-10}I'm cumming{/size}", "scream", "wide", "base", "stare")
            hide screen hermione_main
            m "What was that?"
            call nar(">You start turning your finger.")
            call her_main("{size=+10}I'm cumming!{/size}", "scream", "happyCl", "worried", "mid")
            call nar(">Her asshole starts quivering around your finger.")
            hide screen hermione_main
            m "What a little anal slut. I wonder what you'll do once I try this."
            call nar(">You start pumping your finger in and out of her shivering asshole.")
            call her_main("!!!", "shock", "happyCl", "worried", "mid")
            call her_main("I'm cumming again!", "open", "happyCl", "worried", "mid")
            m "So soon?"
            call her_main("I can't stop! Please [genie_name], please, no more!", "angry", "wide", "base", "stare")

            menu:
                "-Stop-":
                    m "Well, I suppose that's enough for now..."
                    call nar(">You pull your finger out of her asshole and she immediately slumps over your desk.")
                    call her_main("That was... great...", "grin", "narrow", "base", "dead")
                    call nar(">She lies on your desk, breathing heavily.")
                "-Keep Going-":
                    m "What was that [hermione_name]? It almost sounded like you asked me to stop."     ###Or would it be better if she start to tear up and cry a bit?
                    call nar(">You increase the pace.")
                    call her_main("Please...", "open", "happyCl", "worried", "mid")
                    m "Please what?"
                    call nar(">You insert a second finger.")
                    call her_main("Please... stop... you'll break me...", "angry", "narrow", "base", "down")
                    call nar(">You grab her hip with one hand and keep finger fucking her asshole.")
                    call her_main("...", "shock", "happyCl", "worried", "mid")
                    call her_main("...", "scream", "happyCl", "worried", "mid")
                    call nar(">You feel her body go limp as her asshole relentlessly quivers around your fingers.")
                    m "There, wasn't that nice?"
                    call nar(">You slow down and pull out of her asshole.")
                    call her_main("... yeeess...[genie_name]...", "grin", "narrow", "base", "dead")
                    m "Good girl."

            m "Well you best be off to class."
            call her_main("... With my butt looking like this?", "angry", "narrow", "base", "down")
            m "I'm sure no one will be able to tell \nwith your skirt on. Now hurry up \nI have things to attend to."
            call blkfade
            pause 1

            hide screen bld1
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")

            hide screen blktone
            hide screen bld1
            call hide_blkfade
            pause.5

            show screen bld1
            call her_main("Yes [genie_name].", "base", "narrow", "worried", "down")
            m "Oh I almost forgot, twenty points to Gryffindor!"
            $ gryffindor += 20
            call her_main("Oh... right, the points. Thank you.", "grin", "narrow", "base", "dead")
            call nar(">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it.")
            call her_main("...", "open", "narrow", "worried", "down")

        "-Hot dog her-" if her_whoring >= 17:
            m "Bend over [hermione_name]."
            call nar(">Before she even has a chance to react you push her forward over your desk.")
            call her_chibi_scene("sex_hotdog")
            with d3
            call her_main("!!!", "angry", "wide", "base", "stare")
            call her_main("What are you going to do [genie_name]?", "angry", "wink", "base", "mid")
            hide screen hermione_main
            m "Well seeing as how your ass has become so fucking huge I thought I may as well put it to good use."
            call nar(">You pull you cock out from your robes and place it on top of her ass crack.")
            call her_main("Your not going to fuck my asshole are you [genie_name]?", "grin", "narrow", "base", "dead")
            hide screen hermione_main
            m "Not your asshole, [hermione_name], I intend to fuck your entire ass!"
            call nar(">You grab a firm hold of her cheeks and pull them apart, allowing your shaft to rest in between, on top of her asshole.")
            m "A perfect fit wouldn't you say?"
            call her_main("What do you--", "angry", "base", "base", "mid")
            hide screen hermione_main
            call nar(">You squeeze her ass-cheeks back together around your cock and start pumping in between them.")
            call her_main("!!!", "grin", "narrow", "annoyed", "up")
            hide screen hermione_main
            m "Fuck, your ass is so soft. It's like fucking a pillow."
            call her_main("Ahhh...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("Please, [genie_name]...", "silly", "narrow", "annoyed", "up")
            hide screen hermione_main
            m "Ughh, this feels so good, we might have to make this permanent."
            call her_main("Permanent?", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            hide screen hermione_main
            m "You wouldn't mind, would you?"
            m "Having me use your ass as a sex-toy everyday."
            call her_main("...", "angry", "squint", "base", "mid",cheeks="blush")
            hide screen hermione_main
            m "I asked you a question, [hermione_name]."
            call her_main("... no [genie_name]...", "silly", "narrow", "base", "dead")
            hide screen hermione_main
            call nar(">You feel her asshole starts to quiver as you glide over it.")
            m "Of course you wouldn't, you're enjoying this more than I am, aren't you?"
            call her_main("... yes... I'm loving... you using my ass as your toy...", "silly", "narrow", "annoyed", "up")
            hide screen hermione_main
            m "That's it girl, here I come!"
            call nar(">With one final thrust you cum, covering her fat ass with your seed.")

            call her_chibi_scene("sex_cum_out")
            call cum_block
            call ctc

            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.webp"
            m "Ughhh"
            m "All over your fucking back."
            call nar(">You fall back into your chair, spent.")
            m "You may go now [hermione_name]."
            call blkfade
            pause 1

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")

            hide screen blktone
            hide screen bld1
            call hide_blkfade
            pause.5

            show screen bld1
            call her_main("... With my butt looking like this?", "angry", "squint", "base", "mid",cheeks="blush")
            m "I'm sure no one will be able to tell with your skirt on. Now hurry up, I feel like a nap."
            #call her_main("Yes [genie_name].", "angry", "squint", "base", "mid",cheeks="blush")
            m "Oh I almost forgot, twenty points to Gryffindor!"
            $ gryffindor += 20
            call her_main("Oh... right, the points. Thank you.", "grin", "narrow", "annoyed", "up")
            call nar(">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it.")

            call nar(">Your cum is still visible on her ass.")
            call her_main("...", "open", "closed", "base", "mid")


    hide screen hermione_main
    $ uni_sperm = False
    hide screen chair_left
    hide screen desk
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    with d3

    call her_walk(action="leave")

    $ her_potions_drunk.add("expansion")
    $ her_potions_drunk.add("ass_expansion")

    $ hermione_busy = True

    call update_her_uniform

    jump main_room

        #will add this later
        #"-Fuck her ass-" if her_whoring >= 22:
