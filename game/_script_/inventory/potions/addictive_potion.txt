
# Cum addiction - work in progress, has some scenes adjusted for it
label potion_scene_3_1_1:
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    if not her_potions_drunk:
        her "A potion?"
        her "What is it going to do?"
        m "Well, that's going to be a surprise..."
        if her_whoring <= 17: #Under when she stops caring about points too Much
                her "And you'll pay me if I drink this?"
                m "Of course...{w} I'll give you thirty points for the Gryffindor house."
    else:
        call her_main("What does this one do?", "normal", "squint", "angry", "mid")
        m "As always, it's going to be a surprise."
        if her_whoring <= 17: #Under when she stops caring about points too Much
                her "And you'll pay me if I drink this?"
                m "Of course...{w} I'll give you thirty points for the Gryffindor house."

    #TODO There are many more potions she could mention
    if "cat_polyjuice" in her_potions_drunk:
        call her_main("You're not going to try to transform me into a cat again are you [genie_name]?", "normal", "squint", "angry", "mid")
        call her_main("", "normal", "squint", "angry", "mid")
        m "Of course not, now would you kindly drink the potion?"
    elif "breast_expansion" in her_potions_drunk:
        call her_main("You're not going to make my breasts expand again are you [genie_name]?", "normal", "squint", "angry", "mid")
        call her_main("", "normal", "squint", "angry", "mid")
        m "Of course not, now would you kindly drink the potion?"
    else:
        m "Now would you kindly drink the potion?"
        her "Fine..."

    $ renpy.sound.play("sounds/bottle.mp3")

    call her_main("...", "annoyed", "narrow", "angry", "R")

    if her_whoring <= 12 and her_cum_potion_fail == 0: #Too low
        call her_chibi("drink_potion","mid","base")
        call nar(">Hermione cautiously takes a small sip of the potion.")
        call her_main("", "cum", "happyCl", "worried", "mid")
        pause .5
        call her_chibi("stand","mid","base")

        call her_main("This isn't a potion! This is just a bottle full of your cum!", "scream", "closed", "angry", "mid")
        m "Wait, how could you tell if there's cum in there?"
        her "So you did put cum in there!"
        m "I didn't say that..."
        m "Although, if I did... what did you think of the taste?"
        her "Are you crazy? You came in a bottle and served it to me and then has the audacity to ask if I liked the taste?"
        her "What's wrong with you?"
        her "I'm leaving..."
        call her_walk(action="leave")
        m "(Damn, looks like she didn't drink enough for the effect to kick in. I guess she has to trust me more before drinking this one...)"
        $ her_cum_potion_fail += 1
        $ her_mood += 10
        $ hermione_busy = True
        jump main_room
        # End scene
    elif her_whoring <= 12 and her_cum_potion_fail > 0: # Too low and failed previously
        call nar(">Hermione takes a whiff of the potion contents.")
        $ renpy.play('sounds/sniff.mp3')
        pause 0.5
        call her_main("*Ughhh*{w=0.5}{nw}", "disgust", "slit", "low", "stare")
        with hpunch
        call her_main("This isn't a potion! This is just a bottle full of your cum!", "scream", "closed", "angry", "mid")
        g4 "How did you know?"
        call her_main("It reeks of semen ", "angry", "base", "angry", "mid")
        her "I can't believe you were going to make me drink that..."
        her "I'm leaving..."
        call her_walk(action="leave")
        m "(Damn, looks like she won't even consider tasting it. I guess she has to trust me more before drinking this one...)"
        $ her_cum_potion_fail += 1
        $ her_mood += 10
        $ hermione_busy = True
        jump main_room
        # End scene
    else:
        if "cum_addiction" not in her_potions_drunk: # First time
            call her_chibi("drink_potion","mid","base")
            call nar(">Hermione cautiously takes a small sip of the potion.")
            call her_main("", "cum", "happyCl", "worried", "mid")
            pause .5
            call her_chibi("stand","mid","base")

            call her_main("Is this bottle full of your cum?", "disgust", "closed", "angry", "mid")
            call her_main("Ughhh and it's cold as well.", "disgust", "slit", "low", "stare")
            m "So it just tastes like cum to you?"
            call her_main("Of course it does, what else would it taste like?", "angry", "base", "angry", "mid")
            call nar(">Hermione starts unconsciously licking her lips.")
            her "I can't believe you were going to make me drink that..."
            call nar(">Without thinking of what she's doing she downs the rest of the potion.")
        else: #Tried and drank the potion successfully before
            #TODO Johnny add writing here please :)
            pass

    $ renpy.sound.play("sounds/gulp.mp3")
    call her_chibi("drink_potion","mid","base")
    call her_main("", "cum", "happyCl", "worried", "mid")
    pause .5
    call her_chibi("stand","mid","base")

    call her_main("At least warn me next time you make me drink your cum, [genie_name].", "open", "base", "worried", "R")
    m "What do you mean next time?"
    call her_main("Well, you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock.", "annoyed", "narrow", "annoyed", "mid")
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    call her_main("Is that all then, [genie_name]?", "annoyed", "narrow", "angry", "R")
    m "Yes [hermione_name], that will be all."
    call her_main("Thank you, [genie_name].", "open", "squint", "base", "mid")
    call nar(">Hermione hurriedly leaves the room with the remainder of the potion firmly in her grasp.")

    hide screen hermione_main
    call her_walk(action="leave")

    $ her_potions_drunk.add("addiction")
    $ her_potions_drunk.add("cum_addiction")

    $ her_cum_potion_return = True
    $ hermione_busy = True
    jump main_room

# Scene where Hermione comes back addicted to your cum
label hg_pp_cumaddict_intro:
    $ her_cum_potion_return = False

    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.2
    call her_main("What the hell did you do to me?", "scream", "happyCl", "worried", "mid", xpos="mid", ypos="base", trans=hpunch)
    m "Whatever are you talking about, [hermione_name]?"
    call her_main("Ughh, it doesn't matter, just let me suck it.", "annoyed", "base", "worried", "R")
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    call her_main("You know exactly what you did to me. Now let me suck your filthy old cock.", "angry", "base", "angry", "mid")

    menu:
        "-Let her suck your dick-":
            m "Well if you insist, [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            call her_main("Fine. Please let me suck your dick [genie_name].", "upset", "wink", "base", "mid")
            m "*Hmm*... I don't think that was sincere enough."
            call her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.", "angry", "happyCl", "worried", "mid",emote="sweat")
            m "Much better."
    label hg_pp_cumaddict_sucking:

    call blkfade
    pause 1
    hide screen hermione_main
    show screen chair_left
    call her_chibi_scene("bj_pause")
    hide screen blkfade
    with d5

    show screen bld1
    call her_chibi_scene("bj")
    call nar(">As soon as you remove your cock from your robe Hermione is on top of you.")
    call her_main("", "disgust", "narrow", "base", "mid_soft")
    call her_chibi_scene("bj_pause")
    her "Do you have any idea how hard it was sitting through classes today?"
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    call her_main("", "annoyed", "narrow", "angry", "R")
    call her_chibi_scene("bj_pause")
    her "Being this aroused."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Gobble!* *Slurp!*"
    call her_main("", "grin", "base", "base", "R")
    call her_chibi_scene("bj_pause")
    her "With no way to relieve myself."
    her "I tried everything."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Gobble!* *Slurp!* *Slurp!*"
    call her_main("", "smile", "narrow", "base", "mid_soft")
    call her_chibi_scene("bj_pause")
    her "I even masturbated in the girls' bathroom."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    call her_main("", "annoyed", "narrow", "annoyed", "mid")
    call her_chibi_scene("bj_pause")
    her "But nothing worked."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("", "base", "narrow", "base", "up")
    call her_chibi_scene("bj_pause")
    her "All I could think about was the taste of your filthy cum."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Gulp!* *Gulp!*"
    m "My my, someone is becoming quite the slut, wouldn't you say [hermione_name]?"
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("", "open_tongue", "narrow", "base", "mid_soft")
    call her_chibi_scene("bj_pause")
    her "You know why this is happening to me."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Slurp!* *Gulp!*"
    call her_main("", "smile", "narrow", "base", "mid_soft")
    call her_chibi_scene("bj_pause")
    her "Whatever was in that delicious potion you made me drink this morning."
    hide screen hermione_main
    call her_chibi_scene("bj")
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    call her_chibi_scene("bj_pause")
    call her_main("I'm sure there was something else in there.", "angry", "wink", "base", "mid")
    hide screen hermione_main
    call her_chibi_scene("bj")
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    call her_main("", "base", "squint", "base", "mid")
    call her_chibi_scene("bj_pause")
    her "..."
    hide screen hermione_main
    call her_chibi_scene("bj")
    her "*Slurp!* *Slurp!* *Gulp!*"
    call nar(">She is incredibly enthusiastic. You can feel your load building.")

    menu:
        "-Cum down her throat-":
            m "Here it comes, slut!"
            call nar(">Hermione quickly swallows the majority of your shaft. You can feel the tip of your head pressed against the entrance to her throat.")
            m "You'll have to do better than that if you want your reward [hermione_name]."
            call nar(">You place your hands on the back of her head pull her head into you.")
            call her_main("{size=+7}!!!{/size}", "scream", "happyCl", "worried", "mid")
            with vpunch
            hide screen hermione_main
            call nar(">The sensation of entering her throat sends you over the edge.")
            m "Better start swallowing slut!"
            call nar(">You start pumping your thick load directly into her stomach.")
            call cum_block
            call her_chibi_scene("bj_cum_in")
            call nar(">Hermione's eyes widen and tears form as she senses your semen enter her.")
            call cum_block
            call her_main("hhaanooo hhhheerrr", "scream", "wide", "base", "stare")
            hide screen hermione_main
            call nar(">Her hands shoot down into her panties as she starts violently orgasming.","start")
            call nar(">The sight of her pleasuring herself as you use her throat only prolongs your orgasm.","end")
            m "You dirty little slut. Getting off on your headmaster sticking his cock down your throat."
            m "I bet you're loving this, being used as nothing more than a toy."
            call nar(">She says nothing but quickens the pace of her masturbation.","start")
            call nar(">You finally pull out of her eager mouth with a satisfactory pop.","end")
            call her_chibi_scene("bj_pause")
            call her_main("It won't stop!", "shock", "happyCl", "worried", "mid")
            hide screen hermione_main
            m "What won't?"
            call her_main("I-I can't stop cumming [genie_name]...", "angry", "base", "base", "mid")
            hide screen hermione_main
            call nar(">The stimulation proves too much and she passes out.")

        "-Cum in her mouth-":
            m "This is it, girl! Get ready!"
            call nar(">Hermione starts swirling her tongue and focusing on the tip of your shaft.")
            g4 "That's done it slut! Start swallowing!"
            call nar(">You explode into her mouth.")
            call cum_block
            call her_chibi_scene("bj_cum_in")
            call her_main("mmmmmmm... *gulp* *gulp*", "full_cum", "narrow", "base", "dead")
            hide screen hermione_main
            call nar(">Hermiones eyes go blank as she starts swallowing down your load.")
            call cum_block
            m "That's it, swallow it down like a good girl. You earned your prize."
            call her_main("*gulp* *gulp* *gulp* *gulp*", "cum", "happyCl", "worried", "mid")
            hide screen hermione_main
            call nar(">As she swallows you notice her legs start to convulse as she starts to orgasm.")
            call her_main("*gulp* *gulp* *gulp* ", "full_cum", "narrow", "base", "dead")
            hide screen hermione_main
            call nar(">You finally remove your shaft from her hungry mouth.")
            call her_chibi_scene("bj_pause")
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            call nar(">You wipe yourself clean on the tip of her nose.")
            call her_main("...", "cum", "happyCl", "worried", "mid")
            hide screen hermione_main
            m "There, much better."
            call nar(">Her legs have not stopped quivering since you first came.")
            m "Well aren't you going to say anything [hermione_name]?"
            call her_main("Thank you maste--", "silly", "narrow", "base", "dead")
            hide screen hermione_main
            call nar(">She collapses into a heap on the ground with her legs still shaking.")

        "-Cum on her face-":
            m "Get ready, girl! here it comes!"
            call nar(">Hermione increases her efforts and starts focusing on the head of your penis.")
            m "Not so quick [hermione_name]."
            call her_chibi_scene("bj_pause")
            call nar(">You quickly pull your penis out from her mouth.")
            call her_main("What are you doing [genie_name]?", "shock", "wide", "base", "stare")
            hide screen hermione_main
            m "Giving you your well earned reward."
            call cum_block
            call her_chibi_scene("bj_cum_out")
            $ uni_sperm = True
            call nar(">You start pumping your cock quickly and explode all over the witch's face")
            m "Take it you filthy cum slut!"
            call cum_block
            call her_main("{size=+5}!!!{/size}", "soft", "narrow", "annoyed", "up")
            hide screen hermione_main
            call nar(">Hermione immediately starts masturbating shamelessly in front of you.")
            call her_main("{size=+5}I'm cumming{/size}", "angry", "base", "base", "mid")
            with vpunch
            hide screen hermione_main
            m "What was that [hermione_name]?"
            call her_main("I-I'm cumming again?!", "scream", "wide", "base", "stare")
            with hpunch
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old man's cum."
            call her_main("No. Please stop, I'll--", "angry", "happyCl", "worried", "mid", emote="sweat")
            with vpunch
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off on being used as a toy."
            call her_main("I-I'm cumming again [genie_name]. It won't stop...", "scream", "happyCl", "worried", "mid")
            hide screen hermione_main
            call nar(">Hermione's voice trails off as she passes out from overstimulation.")

        "-Cum on the floor-":
            m "I'm cumming, whore!"
            call her_main("mmmmmmmm...", "open_wide_tongue", "base", "base", "mid")
            hide screen hermione_main
            call nar(">She attempts to bury her face into your crotch but you put your palm on her forehead and push her away.")
            call her_chibi_scene("bj_pause")
            call her_main("[genie_name], what are you doing?", "angry", "wide", "base", "stare")
            hide screen hermione_main
            m "giving you your reward!"
            call nar(">After a few quick pumps you point your dick at the floor and explode.")
            call cum_block
            #TODO Add chibi animation: Genie cums on floor in front of Hermione
            call her_main("PROFESSOR! Why would you waste that?", "angry", "narrow", "base", "down")
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            call her_main("I'm not going to eat that. The floor in here is disgusting.", "angry", "base", "base", "mid")
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            call her_main("TOMORROW MORNING!? I can't wait that long! Can't you just cum again?", "angry", "wide", "base", "stare")
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            call her_main("... Fine.", "upset", "closed", "base", "mid")
            hide screen hermione_main
            call nar(">She begrudgingly starts scooping your cum off the floor with her fingers.")
            #TODO Add chibi animation (?): Hermione eats cum off the floor

            menu:
                "-Watch her-":
                    call her_main("", "full_cum", "narrow", "base", "dead")
                    call nar(">She scoops up as much as she can into her palm and quickly moves it to her mouth.","start")
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    call her_main("What do you mean not with my fingers? How else am I supposed to eat it?", "angry", "base", "base", "mid")
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    call her_main("You expect me to LICK your old cum off the floor?", "angry", "narrow", "base", "down")
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    call her_main("...", "angry", "base", "base", "mid")
                    hide screen hermione_main
                    call nar(">She bends over with her head to the floor.")
                    call her_main("(This is so degrading...)", "open_wide_tongue", "base", "angry", "mid")
                    hide screen hermione_main
                    call nar(">She puts her tongue out licks your cum.","start")

            call nar(">The effect is instantaneous.","end")
            call her_main("{size=-4}I-I'm cumming...{/size}", "cum", "happyCl", "worried", "mid")
            hide screen hermione_main
            m "What was that?"
            call her_main("I'm cumming!", "silly", "narrow", "base", "dead")
            with vpunch
            hide screen hermione_main
            call nar(">Hermione's hand shoots under her skirt as she starts violently orgasming.")
            call her_main("What's wrong with me [genie_name]?", "silly", "narrow", "annoyed", "up")
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            call her_main("I can't stop cumming...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            hide screen hermione_main
            call nar(">Hermione loses conciousness.")

    hide screen hermione_main
    call blkfade

    menu:
        "-Carry her back to her room as is-":
            call nar(">You pick her limp body up and carry her to her room.","start")
            call nar(">As you enter the dormitory you hear her talk in her sleep.","end")
            call her_main("Of course I swallow... just form a line...", "open", "happyCl", "worried", "mid")
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.")
            m "Sleep tight, slut."

        "-Clean her up and take her back to her room-":
            $ uni_sperm = False
            call nar(">You pick her limp body up and carry her to her room.","start")
            call nar(">As you enter the dormitory you hear her mumble in her sleep.","end")
            call her_main("You want a kiss [genie_name]? Of course I don't mind...", "open", "closed", "base", "mid")
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.")
            m "Sleep tight, [hermione_name]."

    if her_whoring <= 17: #When she still cares about points (Defined at the start)
        m "Thirty points to Gryffindor..."
        $ gryffindor += 30

    hide screen hermione_main
    hide screen ctc
    call gen_chibi("sit_behind_desk")
    hide screen blktone

    call hide_blkfade

    $ hermione_busy = True
    jump main_room

label hg_pp_cumaddict_E1: #Repetitive version where she doesn't faint after the event maybe?

    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.2

    call her_main("Take off your pants! No questions!", "scream", "happyCl", "worried", "mid", xpos="mid", ypos="base", trans=hpunch)
    m "Hold on a minute, what are you--"
    call her_main("Shut it, just let me suck it.", "annoyed", "base", "worried", "R")
    m "...."

    menu:
        "-Let her suck your dick-":
            g9 "Be my guest, [hermione_name]."
        "-Make her apologise first-":
            m "I don't think that you deserve to suck my dick after being this rude."
            m "Maybe if you apologised..."
            call her_main("......", "upset", "wink", "base", "mid")
            m "No? Well in that case...{w=0.5}{nw}"
            call her_main("{size=+5}I'm sorry!{/size}", "scream", "closed", "angry", "mid")
            call her_main("Please let me suck your dick [genie_name]...", "annoyed", "closed", "base", "mid")
            m "*Hmm*... I don't think that was sincere enough."
            call her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.", "soft", "base", "worried", "mid")
            m "Much better."
    jump hg_pp_cumaddict_sucking # <-- Jumps to blowjob section from the intro, you can replace it with new writing if you'd like.




label potion_scene_7: #TODO hyper sensitivity potion
    m "I'd like you to drink a potion today."
    her "Alright then."
    m "Just like that? No putting up a fight or demanding to know what it is?"
    her "Would you tell me what it is?"
    m "No, probably not."
    her "Then why ask?"
    m "Fair enough, here it is."
    menu:
        "-Drop it on her chest-":
            pass
            #jump potion_scene_7_1 <- label does not exist
        "-Hand it to her-":
            pass
            #jump potion_scene_7_2 <- label does not exist
        "-Drop it on her skirt-":
            pass
            #jump potion_scene_7_3 <- label does not exist



### HYPER SENITIVITY POTION ###

label potion_scene_3_2_1: #TODO Hyper sensitive breasts potion
    call nar(">You fumble with the potion, spilling it over Hermione's front, soaking her shirt through.")
    her "Professor! What were you thinking?"
    call nar(">You place the still half full bottle back on your desk in front of you.")
    m "It was an accident, my hands aren't what they once were."
    her "Ughhh, now I'm going to have to go change before classes."
    her "I expect to be compensated accordingly."
    m "Ok, ok. How about I give you a nice massage to calm you down."
    her "A massage? That's hardly fair compensation!"
    m "Are you sure?"
    her "Positive."
    m "Ok, I'll make a bet with you then."
    her "... Go on..."
    m "I'll start massaging you. If you don't like it after two minutes then you can tell me to stop."
    her "And what do I get for telling you to stop?"
    m "two hundred points."
    her "two hundred points!"
    m "But if you don't ask me to stop I get to massage you for as long as I like, wherever I like."
    her "Deal."
    m "Are you sure?"
    her "No offence [genie_name], but I think I can resist a massage for two hundred points."
    m "you sound confident. Care to raise the stakes?"
    her "Are you saying that I can earn more than two hundred points?"
    m "five hundred."
    her "{size=+10}Five HUNDRED!{/size}" #size up
    her "Deal."
    m "I haven't even told you what happens if you lose."
    her "it doesn't matter. For five hundred points I would turn down a massage from Viktor Krum himself."
    m "Well for the sake of the bet I'll explain anyway."
    m "I expect you to strip naked if you want to be massaged after your two minutes are up."
    her "Naked!"
    m "Only if you lose."
    her "Well I suppose that's OK then, it's not like I'll have to do it."
    m "well are you ready?"
    her "Yes, let's make it quick. I have to go back to the dorms and change after this. My shirt is soaked through."
    call nar(">Hermione walks over and stands in front of you.")
    her "So what's your plan? Do you expect me to give in just because you rub my shoulders?"
    m "Shoulders? Who said anything about shoulders?"
    her "Are you going to grope my butt again?"
    m "No, no. Today we're sticking with the fundamentals."
    call nar(">You grab her breasts through her soaked shirt.")
    her "!!!"
    m "There we are. I'll start the time now shall I?"
    her "What is wrong with me?"
    m "Nothing, apart from underestimating your elders."
    her "My breasts... they're on fire."
    m "If they were I think I would know."
    call nar(">You gently roll her nipples between your thumbs and forefingers.")
    her "!!!"
    her "Please [genie_name], you have to stop."
    m "You're not allowed to ask me to stop until the two minutes are up."
    m "And by my count there's still over a minute and a half to go."
    call nar(">You kneed her breasts firmly.")
    her "I'm calling off the bet..."
    m "Now now, no one likes a quitter."
    her "This isn't a joke, it feels like..."
    her "It feels amazing..."
    m "I told you I'm good."
    her "No [genie_name], this is the best thing I've ever felt."
    her ""

label potion_scene_3_2_2: #TODO Hyper sensitive mouth/throat potion

label potion_scene_3_2_3: #TODO Hyper sensitive pussy potion


# Hypno potion
label potion_scene_3_3_1:
    m "[hermione_name], I have another special potion for you today."
    call her_main("Who are you even buying these off?", "normal", "squint", "angry", "mid")
    m "A good magician never tells."
    call her_main("Magician? You're a wizard, and this better not have any long-term side effects.", "normal", "squint", "angry", "mid")
    if "cat_polyjuice" in her_potions_drunk:
        call her_main("I'm still coughing up fur balls every now again from that polyjuice potion.", "normal", "squint", "angry", "mid")
    m "Of course it won't, now would you kindly drink the potion."
    call her_main("...", "annoyed", "narrow", "angry", "R")
    call her_chibi("drink_potion","mid","base")
    with d3
    call nar(">Hermione cautiously starts drinking the potion.")
    call her_main("", "cum", "happyCl", "worried", "mid")
    pause .5
    call her_chibi("stand","mid","base")

    call her_main("This isn't bad at all.", "base", "happy", "base", "mid")
    call her_main("I feel...", "base", "happyCl", "base", "mid")
    m "You feel what?"
    call her_main("I-I feel grea--", "annoyed", "narrow", "worried", "down")
    call nar(">Hermione's eyes go blank and she stares forward blankly.")
    call her_main("What am I?", "grin", "narrow", "base", "dead")
    m "*Uhm*..."
    m "(Should have thought of something. At least the potion seems to work. Let's see...)"

    #TODO Reconsider the use of menu here, there is only one option
    menu:
        "-You're an airheaded bimbo-":
            show screen blktone
    #call set_h_hair(hair_style="B",color=2)
    call her_main("I am an airheaded bimbo who only wants to make people happy...", "soft", "narrow", "base", "dead")
    menu:
        "-You love being covered in my cum-":
            pass

    call her_main("I love being covered in your cum...", "soft", "narrow", "base", "dead")
    menu:
        "-Your breasts are incredibly sensitive to pleasure-":
            pass
    call her_main("My breasts are incredibly sensitive to pleasure......", "soft", "narrow", "base", "dead")
    pause.5

    hide screen blktone
    call nar(">Hermione closes her eyes and appears to nod off.")
    call her_main("......", "base", "closed", "base", "mid")
    call her_main("Where am I?", "upset", "wink", "base", "mid")
    m "You're in my office."
    call her_main("I am?", "upset", "wink", "base", "mid")
    call her_main("How did I get here?", "upset", "wink", "base", "mid")
    m "You walked in here about two minutes ago."
    call her_main("Huh, I must have forgotten, silly old me.", "base", "happy", "base", "mid")
    call her_main("So professor, what am I doing here?", "base", "narrow", "worried", "down")
    call her_main("Aaaaaaah!!!!", "shock", "happyCl", "worried", "mid",cheeks="blush")
    call her_main("What happened to my outfit?!", "shock", "narrow", "base", "down")
    call her_main("I can't be seen wearing all this stuff!!!", "disgust", "narrow", "worried", "down")
    $ hermione.strip("robe", "accessory")

    if hermione.is_worn("top"):
        call set_her_action("lift_top")
        pause .5

        $ hermione.strip("top")
        call set_her_action("none","skip_update")
        pause .5

        call her_main("That's soooooo much better!", "soft", "narrow", "annoyed", "up")

    if hermione.is_worn("bottom"):
        call her_main("It really suuuuucks that I have to wear anything at all in this boring nunnery...", "annoyed", "narrow", "annoyed", "up")
        call her_main("(Why can't I wear something shorter. A skirt, but...)")
        call her_main("(A reeealy short one!!!{heart}{heart}{heart})",face="horny")

        call set_her_action("lift_bottom")
        pause.5

        $ hermione.strip("bottom")
        call set_her_action("none","skip_update")
        pause.5

        call her_main("I bet you like watching me strip mistah{heart}", "smile", "narrow", "base", "mid_soft")

    call her_main("I'm not sure what under-thingies I should wear though...", "annoyed", "narrow", "base", "down")
    call her_main("Definitely something in pink!!!", "smile", "happyCl", "base", "mid")
    hide screen hermione_main
    call blkfade

    call nar(">Hermione pulls out her wand and casts a spell...")

    # TODO: Hermione's bimbo clothes should be temporary for this potion. revamp this event.
    # Setting up Bimbo clothes
    # Blonde hair
    # Override body?
    # add special face layer?

    pause.5
    call her_main("", "base", "narrow", "base", "mid_soft")
    call hide_blkfade
    call ctc

    call her_main("Do you like it mistah?", "grin", "happyCl", "base", "mid")

    menu:
        g9"!!!"
        "-You look amazing!-":
            call her_main("Thank youuuuu!!!{heart}{heart}{heart}", "grin", "narrow", "annoyed", "up")
            call her_main("Aaaaanyway...", "open", "base", "base", "R")
            call her_main("Is there anything you want from me mistah... I'll do anything!{heart}", "soft", "narrow", "base", "mid_soft")
        "-Where is your badge, cumslut?!-":
            call her_main("Oh no I forgot that!", "soft", "wide", "base", "stare")
            call her_main("I'm soooo sorry!!!", "shock", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("It's this one, isn't it...", "soft", "narrow", "worried", "down")
            call nar(">Hermione conjures an \"I {heart} Cum\" badge, which magically attaches itself to her breasts.")

            # TODO: Uncomment once badges have been added.
            # hermione.equip(cumslut_badge)

            call her_main("Yay! Do you like it?", "grin", "happyCl", "base", "mid")
            call her_main("Anything else you want from me mistah?... I'll do anything!{heart}", "soft", "narrow", "base", "mid_soft")

    m "I'm just going to ask you a few questions."
    call her_main("(...)", "annoyed", "base", "angry", "mid")
    call her_main("(And here I was hoping he'd just ask to fuck...)", "annoyed", "narrow", "angry", "R")
    call her_main("(Questions are so boooring! I hope they are at least naughty...)", "annoyed", "narrow", "annoyed", "up")
    call her_main("Are those questions going to be hard, mistah?","grin", "base", "worried", "mid", emote="sweat")
    call her_main("I don't like hard questions.", "grin", "happyCl", "worried", "mid")
    m "Don't worry they'll be nice and easy for you."
    call her_main("yay!", "smile", "happyCl", "base", "mid")
    m "First question, Who are you?"
    call her_main("That's an easy one! I'm Hermione Granger, the prettiest girl in the whole school!", "smile", "happyCl", "base", "mid",emote="happy")
    m "And what are your hobbies?"
    call her_main("Doing my makeup{heart}, dancing{heart} and dressing happy{heart}!", "base", "happyCl", "base", "mid")
    m "Dressing happy?"
    call her_main("You know, wearing nice things to make other people happy!{heart}", "base", "narrow", "base", "up")
    m "You like making people happy?"
    call her_main("Of course mistah professor, making people happy{heart} makes me happy{heart}!", "smile", "happyCl", "base", "mid")
    call her_main("Once I finish school I want to get a job where all I do is make people happy{heart}!", "base", "happyCl", "base", "mid")
    m "Ok, final question"
    m "How would you like to make yourself happy?"
    call her_main("Make myself happy?", "annoyed", "narrow", "worried", "down")
    call her_main("But I'm already happy, silly!", "base", "happyCl", "base", "mid")
    m "Even happier."
    call her_main("Even happier? {size=+10}YAY!{/size}", "smile", "happyCl", "base", "mid",emote="happy")
    call her_main("So how am I going to be happier? Am I going to get naked?", "grin", "base", "base", "R")
    m "That'd be a good start."
    $ hermione.strip("robe", "accessory")
    call her_main("{heart}AAAAAAWWWEEESOOOOOOOOMMME!{heart}", "grin", "narrow", "annoyed", "up")

    call set_her_action("lift_top")
    pause .5

    $ hermione.strip("top")
    $ hermione.strip("bra")
    call set_her_action("none","skip_update")
    pause.5

    call her_main("You know they don't let us walk around naked at school?", "annoyed", "narrow", "angry", "R")
    m "Really? I can't imagine why not."
    call her_main("I know right? It's like so dumb! Everyone would just be happier{heart} if they got to be naked.", "soft", "narrow", "annoyed", "up")

    call set_her_action("lift_skirt")
    pause.5

    $ hermione.strip("bottom")
    $ hermione.strip("panties")
    call set_her_action("none","skip_update")
    pause.5

    call her_main("I know everyone who sees me naked is happy!", "base", "narrow", "base", "mid_soft")
    m "You've certainly made me happy."
    call her_main("Thanks mistah professor sir! That makes me so happy{heart}!", "grin", "happyCl", "worried", "mid")
    m "(I don't think I can stand her saying the word happy much more...)"
    m "Now Hermione, I want you to touch your breasts."
    call nar(">Hermione moves her hands up to her breasts")
    call set_her_action("lift_breasts")

    call her_main("Like this? This feels sooooo gooood!", "base", "narrow", "worried", "down")
    call her_main("It's like mah hands are moving on their own...", "soft", "narrow", "annoyed", "up")
    call her_main("It's soooo goodd but It's weeeiiird... I need something... anything...", "open", "happyCl", "worried", "mid")
    m "Would you like to touch yourself down there?"
    call her_main("Yes mistah [genie_name]. please.", "shock", "happyCl", "worried", "mid")

    menu:
        "-make her beg-":
            m "I want you to beg."
            call her_main("Please mistah sir...", "shock", "happyCl", "worried", "mid")
            m "Please what?"
            call her_main("Ohmigawd Please let me touch myself down there... I'll do anything...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "Anything?"
            call her_main("Anything. I just need to feel happy...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "Tell me what you are and I'll let you."
            call her_main("I'm Hermione, the school slut.", "grin", "narrow", "annoyed", "up")
            m "More."
            call her_main("geez, I'm a dumb bimbo fuckbunny... that just wants to feel happy...", "silly", "narrow", "annoyed", "up")
            m "And what makes you happy?"
            call her_main("Making you happy{heart} [genie_name].", "silly", "narrow", "base", "dead")
            m "Good girl."
        "-let her touch herself-":
            m "Go on then."
            call her_main("Thank you soooo{heart} much [genie_name]!", "silly", "narrow", "annoyed", "up")

    call set_her_action("covering")
    call her_main("This is soooo goood", "grin", "narrow", "annoyed", "up")
    call her_main("Mistah [genie_name] can you please do something for me?", "grin", "wink", "base", "mid",cheeks="blush")
    m "What's that?"
    call her_main("If it's not tooo much trouble could you...", "silly", "narrow", "annoyed", "up")
    call nar(">Hermione starts pinching her nipple.")
    call set_her_action("pinch")
    call her_main("could you please cum on me?", "open_tongue", "narrow", "base", "up",cheeks="blush")
    m "Well if it makes you happy."
    call nar(">you stand up and head towards her.")
    call her_main("thank you, thank you thank you! You're the best headmaster {size=+5}EVER!{/size}", "smile", "happyCl", "base", "mid",emote="happy")

    hide screen hermione_main
    call blkfade

    call gen_chibi("jerk_off","desk","base")
    show screen chair_left
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call set_her_action("covering")
    call her_main("...", "base", "narrow", "base", "up")
    call set_her_action("pinch")
    call her_main("I don't know how other girls do it...", "annoyed", "narrow", "worried", "down")
    m "Do what?"
    call her_main("Stop themselves from coming here and getting you to cover them in yummy cummy!", "annoyed", "narrow", "worried", "down")
    call set_her_action("covering")
    call her_main("I mean I can barely stop mahself coming here everyday!", "smile", "happyCl", "base", "mid")
    m "That's it..."
    call set_her_action("pinch")
    call her_main("*Hmmm*... I just luv playin' with mah boobies{heart}{heart}{heart}", "base", "narrow", "base", "up")
    call her_main("They're just so soft...", "open", "narrow", "base", "up",cheeks="blush")
    call set_her_action("covering")
    call her_main("And they feel soo good. They're really sensi--", "base", "narrow", "base", "up",cheeks="blush")
    call her_main("Sensi--", "base", "narrow", "base", "up",cheeks="blush")
    call set_her_action("pinch")
    call her_main("What's the word?", "annoyed", "narrow", "base", "up",cheeks="blush")
    m "Sensitive."
    call set_her_action("covering")
    call her_main("That's right they're really sensitive!", "silly", "narrow", "base", "up",cheeks="blush")
    m "So am I..."
    call her_main("Are you going to cum?", "open_tongue", "narrow", "base", "up",cheeks="blush")
    call set_her_action("pinch")
    call her_main("Please do it on my face!", "open_tongue", "narrow", "base", "up",cheeks="blush")
    call her_main("No wait my tits...", "scream", "happyCl", "worried", "mid",cheeks="blush")
    call set_her_action("covering")
    call her_main("No wait my face!", "silly", "narrow", "base", "up",cheeks="blush")

    #TODO Fix: Chibi cumshot position in the following segment
    menu:
        "-Cum on her face-":
            g4 "Here it comes slut!"
            call her_main("{heart}!!!{heart}", "shock", "wide", "base", "stare",cheeks="blush")
            call gen_chibi("cum","desk","base")
            $ u_sperm = "characters/hermione/face/auto_07.webp"
            $ uni_sperm = True
            g4 "that's it, all over your face."
            call set_her_action("pinch")
            call her_main("...{heart}{heart}{heart}", "silly", "narrow", "base", "up",cheeks="blush")
        "-Cum on her tits-":
            g4 "Here it comes fuckbunny!"
            call her_main("{heart}{heart}{heart}", "shock", "wide", "base", "stare",cheeks="blush")
            call gen_chibi("cum","desk","base")
            $ u_sperm = "characters/hermione/face/auto_02.webp"
            $ uni_sperm = True
            g4 "All over your tits."
            call set_her_action("pinch")
            call her_main("It's so warm...{heart}{heart}{heart}", "silly", "narrow", "base", "up",cheeks="blush")
        "-cover her in cum-":
            g4 "Here it comes whore!"
            call her_main("{heart}{heart}{heart}", "shock", "wide", "base", "stare",cheeks="blush")
            call gen_chibi("cum","desk","base")
            $ u_sperm = "characters/hermione/face/auto_05.webp"
            $ uni_sperm = True
            g4 "that's right slut, All over you."
            call set_her_action("pinch")
            call her_main("{heart}{heart}{heart}", "silly", "narrow", "base", "up",cheeks="blush")

    call gen_chibi("hold_dick","desk","base")
    call her_main("...", "grin", "narrow", "annoyed", "up")
    $ hermione_dribble = True
    call her_main("That felt {size=+5}SOOOOO!{/size} good!", "silly", "narrow", "annoyed", "up")
    call set_her_action("lift_breasts")

    call her_main("Can we do it again! Please! Pretty please! Pretty please with cum on top!", "silly", "narrow", "base", "dead")
    m "Not today."
    call her_main("Awwwwww.", "shock", "happyCl", "worried", "mid")

    hide screen hermione_main
    call blkfade

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade

    call her_main("Well ok... I suppose I'll head to class then.", "open", "narrow", "worried", "down")
    m "About that. I think it'd be better if you went back to your dorm."
    call her_main("Why's that mistah [genie_name] sir?", "annoyed", "base", "base", "mid")
    m "I think you need to have a little nap and let this wear off."
    call her_main("whatever you say sir!", "annoyed", "closed", "base", "mid")
    call set_her_action("none","skip_update")
    call her_main("And thanks again!{heart} You're the best!", "smile", "happyCl", "base", "mid",emote="happy")

    call her_walk(action="leave")

    call bld
    m "(Maybe I should have told her to get dressed first...)"

    # Note: these items can also be bought
    $ cum_badge_ITEM.unlocked = True
    $ lipstick_pink_ITEM.unlocked = True
    call give_reward(">Hermione can now use pink lipstick and wear the \'cum\' badge!","interface/icons/lipstick_pink.webp")

    call reset_hermione

    $ her_potions_drunk.add("hypno")

    $ hermione_busy = True
    jump main_room


### AHEGAO POTION ###
#TODO Ahegao potion is incomplete (only a sex scene with broken CG)
label potion_scene_3_4_1:
    m "How long until your next class [hermione_name]?"
    call her_main("about fifteen minutes sir.", "open", "base", "base", "mid")
    m "in that case I think you might have to be a little late."
    call her_main("what? why?", "open", "base", "worried", "mid")
    g4 "Well, it might be a bit hard for you to attend class with my cock buried in your tight little pussy."
    call her_main("Oh...", "soft", "happy", "base", "R")
    m "That's not going to be a problem is it [hermione_name]?"
    call her_main("of course not [genie_name]! Let me just take my clothes off...", "grin", "narrow", "annoyed", "up")

    show screen blkfade
    with d3
    hide screen bld1
    call her_chibi("hide")
    #SEX
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("ahhhhhhhhh....{heart}", "scream", "wide", "base", "stare")
    hide screen hermione_main
    call gen_chibi("hide")
    $ ccg_folder = "herm_sex"
    $ ccg1 = "blank"
    $ ccg3 = "blank"
    $ ccg2 = 1
    show screen ccg
    hide screen blkfade
    with d3
    her "*Ah*...{heart}"
    g4 "*mmmm*, you like that don't you slut?"
    $ ccg2 = 2
    her "yes...{heart}"
    $ ccg2 = 3
    her "even though I have to miss class..."
    $ ccg2 = 4
    her "I Honestly don't care...{heart}"
    $ ccg2 = 5
    her "This just feels too goooood..."
    pause
    ">You quietly pull out the small vial from your pocket and pull the stopper out."
    $ ccg2 = 6
    her "Mmmm, don't slow down [genie_name]..."
    g4 "You asked for it!"
    ">You speed up the pace as you go to pour a drop onto her ass, your hand barely managing to stay stable..."
    $ ccg2 = 7
    her "Harder [genie_name]!!!"
    pause
    ">You feel hermione suddenly push her pussy back towards you, causing you to spill about a quarter of the vial onto her ass..."
    $ ccg3 = "p1"
    m "..."
    $ ccg2 = 8
    her "What was that?"
    m "*Ugh*... nothing... just a bit of spit. Keep going slut."
    $ ccg2 = 9
    her "*Ah*...{heart} alright then..."
    ">You quickly put the stopper back into the vial and slip it back into your robes."
    $ ccg2 = 10
    her "*Ah*... *ah*... *ah*..."
    pause
    $ ccg2 = 11
    her "[genie_name], you think you could... *ah*..."
    g4 "What is it slut?"
    $ ccg2 = 12
    her "Could you please... spank me... *ah*...?"
    g4 "of course!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass a hard spank, accidentally causing the potion to explode out from underneath your hand, coating her even more."
    $ ccg3 = "p2"
    $ ccg2 = 13
    pause
    her "{size=+10}!!!{/size}"
    ">Hermione's sopping cunt starts contracting around your cock uncontrollably."
    g4 "Mmmm, cumming already slut?"
    $ ccg2 = 14
    her "Y-yes...{heart}{heart}{heart}{heart}{heart}{heart}"
    $ ccg2 = 15
    her "I{heart} can't{heart} stop..........{heart}{heart}{heart}"
    ">True to her word, you don't feel an end to her relentless spasming."
    g4 "I love it when cum on my cock whore!"
    $ ccg2 = 16
    pause
    her "no...{heart} sir...{heart} you...{heart} don't...{heart} understand...{heart}"
    $ ccg2 = 17
    her "It...{heart} won't...{heart} stop...{heart}"
    g4 "I don't see how that's my problem!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, savoring the feeling of another orgasm flowing through the witch."
    $ ccg2 = 18
    her "{size=+10}!!!{/size}"
    $ ccg2 = 19
    her "it's......{heart} {heart} "
    $ ccg2 = 20
    pause
    her "my{heart}  whole{heart}  body...{heart}{heart}{heart} "
    g4 "Speak up slut!"
    $ ccg2 = 21
    her "My body's...{heart} {heart} on fire..."
    $ ccg2 = 22
    her "I can't...{heart}"
    $ ccg2 = 23
    her "why...{heart}"
    $ ccg2 = 24
    her "Why {heart}does {heart}it {heart}feel {heart}this {heart}goooooooooood...{heart}{heart}{heart}"
    g4 "enjoying yourself are we?"
    $ ccg2 = 25
    her "No...{heart} *ah*... yesssss....{heart}"
    $ ccg2 = 26
    her "it's like...{heart}"
    $ ccg2 = 27
    her "each time you thrust...{heart}{heart} that big fat {heart}cock{heart} in me...{heart}"
    $ ccg2 = 28
    pause
    her "it's like I {heart}{heart}cum{heart}{heart}..."
    her "But it never resets..."
    $ ccg2 = 29
    her "Each time is just another stronger {heart}orgasm{heart}..."
    $ ccg2 = 30
    her "{size=+10}AND{heart} THEY{heart} NEVER{heart} STOOO{heart}OOOP!!!!!!{/size}"
    g4 "Sounds nice... and what about when I give your fat ass a nice... slap?"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, holding your hand against her warm flesh, swirling the potion around underneath it."
    $ ccg2 = 31
    her "{size=+20}{heart}{heart}!!!{heart}{heart}{/size}"
    $ ccg2 = 32
    her "{heart}my{heart} {heart}brain...{heart}"
    $ ccg2 = 33
    her "You're{heart} going{heart} to{heart} kill{heart} me...{heart}"
    g4 "Stop being so overdramatic..."
    pause
    $ ccg2 = 34
    her "I'm not...{heart}"
    her "*Ah*.....{heart} some....{heart} thing....{heart} is....{heart} wrong....{heart}"
    ">Hermione's words start to slow, eventually only being able to mutter a squeak of a word every time you thrust into her."
    g4 "Maybe it was the potion I poured all over your ass earlier?"
    $ ccg2 = 35
    her "{size=+20}{heart}{heart}what?{heart}{heart}{/size}"
    g4 "Don't worry, the effects should wear off in about an hour..."
    $ ccg2 = 36
    her "{size=+20}!!!!!!!{/size}"
    g4 "In the mean time, why don't you just sit back and enjoy the ride."
    $ ccg2 = 37
    her "{heart}e-e-enjoy....{heart}"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    $ ccg2 = 38
    pause
    her "{size=+20}!!!!!!!{/size}"
    $ ccg2 = 39
    her "Pleeeease...{heart}{heart}{heart}"
    $ ccg2 = 40
    her "my...{heart}mind...{heart}is...{heart}breaking...{heart}"
    ">You start to pick up the pace, treating her as nothing more than your mewling fuckmeat..."
    g4 "MMMM, you always know what to say to get me going!!"
    $ ccg2 = 41
    her "...{heart}{heart}{heart}"
    ">Eventually the endless spasming of her drenched pussy around your cock proves too much."
    g4 "Ah!!! Here It comes whore!"
    $ ccg2 = 42
    pause
    her "{heart}........{heart}"
    ">You start firing cum directly into her womb."
    $ ccg3 = "s4"
    $ ccg2 = 43
    pause
    her "{heart}!!!{heart}"
    g4 "TAKE THIS!!!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass one last slap, stinging your hand as you shoot the last rope into her waiting cunt."
    $ ccg3 = "s5"
    $ ccg2 = 44
    pause
    her "{heart}........{heart}"
    her "{heart}...............{heart}"
    $ ccg2 = 45
    pause
    her "{heart}.......................{heart}"
    show screen blkfade
    with d3
    ">Eventually hermione's eyes roll back into her head as she collapses forward onto your desk."
    ">you carry her unconscious body back to her room to sleep the last of the potion off."
    hide screen ccg
    hide screen hermione_main
    call her_chibi("hide")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3

    $ hermione_busy = True
    call music_block
    jump main_room
