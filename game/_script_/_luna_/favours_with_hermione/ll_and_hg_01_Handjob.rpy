
# Luna (converted) handjob with Hermione
label luna_favour_5:

    if lun_whoring <= 11:
        $ lun_whoring += 1
        m "[luna_name], how would you feel about selling another favour?"
        call lun_main("...","base","seductive","angry","mid")
        call lun_main("What is it this time [lun_genie_name]?","base","angry","angry","R")
        m "Well, do you remember how we had a little fun with miss Granger the other day?"
        call lun_main("...","base","seductive","angry","mid")
        call lun_main("go on...","base","suspicious","angry","R")
        m "how would you feel about bringing her up her for a little more fun?"
        call lun_main("You really are a disgusting pervert aren't you?","base","angry","mad","mid")
        m "..."
        call lun_main("Aren't you...","normal","suspicious","angry","mid")
        m "Yes..."
        call lun_main("at least you're honest about it...","base","mad","sad","R")
        call lun_main("Which is more than I can say for that two-faced slut hermione...","upset","wide","mad","mid")
        m "So you're OK with having a little fun with her?"
        call lun_main("on one condition.","base","angry","mad","mid")
        m "Name it."
        call lun_main("I'm in control. No matter what.","normal","mad","angry","R")
        call lun_main("Even if you think what's happening is too mean...","upset","mad","angry","mid")
        call lun_main("I am in control... got it?","normal","suspicious","mad","mid")
        m "Done."
        call lun_main("alright then...","base","happyCl","sad","mid")
        call lun_main("I also expect to be paid 150 gold for my troubles...","normal","angry","sad","mid")
        m "Certainly."
        call lun_main("...","base","seductive","angry","R")
        call lun_main("Now [lun_genie_name]...","upset","angry","mad","mid")
        m "Alright then..."
        ">You pay Luna 150 gold."
        $ gold -=150
        $ luna_gold += 150
        call lun_main("thank you [lun_genie_name]...","normal","angry","sad","R")
        call lun_main("...","normal","angry","raised","mid")
        call lun_main("Well come on then, summon her...","pout","mad","angry","mid")
        ">You summon Hermione - somehow..."

        call her_walk(action="enter", xpos="right", ypos="base")

        $ luna_flip = -1
        $ luna_r_arm = 2
        call update_her_uniform

        call her_main("hello Prof--", "soft", "base", "base", "R",xpos="base",ypos="base")
        call her_main("Luna! what are you doing here?", "angry", "wide", "base", "stare")
        call lun_main("same thing as you...","base","seductive","angry","mid", xpos=390)
        call her_main("Oh, um... you must be here to... help Professor Dumbledore then...", "open", "base", "worried", "R")
        call lun_main("*Mhmmm*...","base","angry","sad","mid")
        call her_main("So, ugh... what does Dumbledore need our help with?", "open", "base", "worried", "mid")
        call lun_main("Probably emptying those nasty balls of his...","upset","mad","angry","mid")
        call her_main("!!!", "angry", "wide", "base", "stare")
        call her_main("Luna! what are you talking about?", "angry", "base", "worried", "mid")
        call her_main("Are you okay?", "annoyed", "base", "worried", "R")
        call lun_main("Come on now hermione... it wouldn't be the first time you've helped old Dumbledore like this?","base","angry","angry","R")
        call lun_main("would it...?","normal","angry","angry","mid")
        call her_main("I have no idea what you're talking about!", "scream", "closed", "angry", "mid")
        call her_main("Professor Dumbledore must be mistaken...", "scream", "closed", "angry", "mid")
        call her_main("M-Maybe he needs to go to the nurses and have his mind checked...", "scream", "closed", "angry", "mid")
        call lun_main("So you're not selling favours to Dumbledore in exchange for points?","normal","suspicious","raised","mid")
        call her_main("certainly not! I'd never do something so underhanded!", "scream", "happyCl", "worried", "mid")
        call lun_main("Really?","upset","angry","raised","mid")
        call her_main("Of course not! I'm shocked you even have to ask!", "annoyed", "base", "worried", "R")
        call lun_main("So you're comfortable saying that after you've had a sip of some veritaserum?","normal","mad","mad","mid")
        call her_main("!!!", "angry", "wide", "base", "stare")
        call her_main("O-O-Of course... but as you know, that potion's banned...", "open", "closed", "base", "mid")
        call lun_main("Not for the illustrious Professor Dumbledore!","base","seductive","sad","R")
        call lun_main("Isn't that right sir?","upset","angry","mad","R")
        m "Oh, um yes of course I can get that easily..."
        m "(What the hell is veritaserum?)"
        call her_main("!!!", "annoyed", "squint", "angry", "mid") #angry face
        call her_main("surely you know there's no need for that sir!", "normal", "squint", "angry", "mid") #angry face
        m "..."
        call her_main("...", "annoyed", "squint", "angry", "mid")
        call lun_main("...","base","angry","base","mid")
        call her_main("Fine! I admit it!", "scream", "happyCl", "worried", "mid")
        call lun_main("See... Isn't it better to tell the truth?","base","mad","sad","mid")
        call her_main("...", "normal", "happyCl", "worried", "mid")
        call her_main("So is that why I've been brought here? To be ridiculed!?", "angry", "base", "angry", "mid")
        call her_main("I'm not ashamed of what I've done for my house!", "annoyed", "narrow", "annoyed", "mid")
        call lun_main("No, you've been brought here to sell Dumbledore one of those favours.","base","seductive","angry","mid")
        call her_main("What?", "upset", "wink", "base", "mid")
        call her_main("Why are you here then?", "soft", "base", "base", "mid")
        call lun_main("To help you.","base","angry","sad","mid")
        call her_main("...", "annoyed", "base", "angry", "mid")
        call her_main("Help how?", "disgust", "narrow", "base", "mid_soft")
        call lun_main("Why don't you take your clothes off and I'll show you...","base","mad","sad","mid")
        call her_main("[genie_name]... please...", "scream", "happyCl", "worried", "mid")
        m "I'm sorry [hermione_name], my hands are tied..."
        call her_main("...", "normal", "happyCl", "worried", "mid")
        call her_main("Do I have to?", "angry", "happyCl", "worried", "mid",emote="sweat")
        call lun_main("Of course not... So long as you don't mind me telling your precious \"MRM\" what's been going on.","base","mad","mad","mid")
        call her_main("...", "mad", "base", "worried", "mid", tears="soft")
        call her_main("FINE!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
        call her_main("I see how it is!", "annoyed", "narrow", "annoyed", "mid", tears="crying")
        ">Hermione pulls off her top in a huff."

        hide screen hermione_main
        $ hermione.strip("bra", "top")

        call her_main("Feel free to humiliate me!", "angry", "base", "angry", "mid",tears="crying")
        ">Hermione angrily removes her skirt."

        call her_main("for trying to do what's right!", "annoyed", "narrow", "annoyed", "mid", tears="crying")
        ">Hermione stands naked before you and Luna. Her face is contorted in what seems like an equal mix of rage and embarrassment."
        call her_main("there! are you happy now you two?", "annoyed", "narrow", "annoyed", "mid")
        m "Yes--"
        call lun_main("almost...","base","seductive","sad","down")
        call lun_main("now why don't you get on your knees...","upset","angry","angry","mid")
        call her_main("!!!", "angry", "wide", "base", "stare",tears="crying")
        call her_main("please, Luna... I'm {size=-2}sorry {size=-2}about {size=-2}what I said to you the other day...{/size}", "annoyed", "narrow", "worried", "down",tears="crying")
        call lun_main("then kneel...","normal","suspicious","sad","mid")

        hide screen luna_main
        hide screen hermione_main
        hide screen bld1
        # Hermione chibi kneels
        call her_chibi("sit_naked", "mid", "base")
        call lun_chibi("stand", "right", "base")
        with d3
        call ctc

        call her_main("...","annoyed","narrow","annoyed","up", xpos="right", ypos=200)
        call lun_main("there... isn't this simpler? Is this not your natural state?","normal","base","angry","down", xpos="base",flip=False)
        call her_main("...","annoyed","narrow","worried","down")
        call lun_main("now... I'll need your help for this next bit Professor.","base","seductive","sad","R")
        m "What do I need to do?"
        call lun_main("come and stand before your star student.","base","angry","angry","down")

        show screen blkfade
        hide screen bld1
        with d3

        ">You get up out of your chair and walk over to the two girls."

        show screen chair_left
        show screen desk
        call gen_chibi("stand", "desk", "base")
        hide screen blkfade
        with d3
        call ctc

        ">Hermione looks up at you with a pleading expression."
        call her_main("[genie_name]... please... what's going on?","mad","base","worried","mid",tears="soft")
        call lun_main("I said that you're here to sell a favour.","normal","angry","angry","down")
        call lun_main("Isn't that you want? To sell favours to Dumbledore?","base","seductive","sad","mid")
        call her_main("I want... I want Gryffindor to win the house cup...","open","narrow","worried","down")

        if gryffindor > slytherin:
            call lun_main("But Gryffindor is already ahead by "+str(gryffindor-slytherin)+" points...","pout","angry","raised","down")
            call lun_main("do you really think that they need any more points to win?","base","angry","sad","down")
            call her_main("...","soft","happy","base","R")
        else:
            call lun_main("do you really think it's fair for you to win by selling your body?","normal","mad","angry","down")
            call lun_main("*tch* *tch* *tch* what would your parents think?","pout","angry","angry","down")
            call her_main("they wouldn't understand...","annoyed","narrow","angry","R")

        show screen blkfade
        hide screen bld1
        with d3

        ">Luna puts her hand in your robes and quickly pulls out your hardening cock."

        # Handjob pose
        $ luna_r_arm = 3
        $ luna_zorder = 16
        $ hermione_zorder = 17
        call her_main()
        call lun_main(xpos=390, flip=False)
        call gen_main(face="grin", base="open", xpos=300, ypos=0)

        call gen_chibi("dick_out", "desk", "base")

        hide screen blkfade
        with d3
        call ctc

        call gen_main("!!!","grin")
        call lun_main("Just admit it...","base","mad","sad","mid")
        call lun_main("you're a slut...","base","suspicious","base","mid")
        call her_main("{size=-5}no... I'm... a good student...{/size}","open","base","base","R")
        call ctc

        ">Luna starts sliding her smooth hand up and down your cock."
        call lun_main("*hmmmm*... I'm not so sure a good student would do this...","pout","seductive","sad","R")
        call her_main("...","soft","happy","base","R")
        call lun_main("kneel willingly in front of their headmaster..","base","angry","angry","down")
        call her_main("...","grin","narrow","annoyed","up")
        call lun_main("naked...","base","mad","angry","mid")
        call her_main("...","angry","narrow","base","down")
        call lun_main("While another student jerks him off...","base","seductive","sad","R")
        call her_main("...","soft","narrow","annoyed","up")
        call lun_main("Waiting patiently to be covered in cum...","grin","mad","sad","down")
        call her_main("{heart}{heart}{heart}","grin","narrow","base","dead")
        call ctc

        call lun_main("in fact, I can think of only one sort of student who'd do that...","base","seductive","angry","down")
        call lun_main("do you know what sort of student that is hermione?","base","angry","sad","mid")
        call her_main("ah...{heart} a...","soft","happy","base","R")
        call lun_main("*Mhmmm*, go on...","base","seductive","angry","down")
        call her_main("ah...{w} a slut...{heart}","open","base","base","R")
        call lun_main("good girl...","base","seductive","sad","down")
        call her_main("{heart}{heart}{heart}","grin","narrow","base","dead")
        m "Ah... almost there [luna_name]..."
        ">Luna gives your cock a hard squeeze."
        g9 "Ah!"
        call lun_main("not yet old man!","upset","mad","mad","mid")
        call lun_main("she hasn't learnt her lesson yet!","base","mad","mad","down")
        m "What else does she need to do?"
        call lun_main("...","pout","angry","angry","R")
        call lun_main("Lick it...","upset","mad","sad","down")
        call her_main("...","shock","wide","base","stare")
        call her_main("OK...","soft","happy","base","R")
        ">Hermione opens her mouth and puts out her tongue."
        call her_main("ah...","open_wide_tongue","happy","base","R", ypos=230)
        call lun_main("...","upset","angry","angry","mid")
        call lun_main("seems like I have to do everything then...","normal","suspicious","angry","R")
        ">Luna pulls you forward, harshly, by your cock into Hermione's open mouth."
        g4 "!!!"

        $ luna_xpos += 50
        $ genie_xpos += 50

        call her_main("...","open_wide_tongue","narrow","annoyed","up")
        ">Hermione starts running her tongue along the length of your cock, lubricating it while Luna continues to stroke."
        g4 "Ah!!!"
        g4 "This is it sluts!"
        call lun_main("do it...","base","seductive","sad","mid")
        call her_main("*mmmm*...{heart}{heart}{heart}","open_wide_tongue","narrow","annoyed","up")
        call lun_main("cover the slut...","base","angry","mad","down")
        g9 "*Argh*! by the gods {size=+10}YES!{/size}"

        $ luna_xpos -= 50
        $ genie_xpos -= 50

        g9 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
        show screen white
        pause.1
        $ hermione.set_cum(face="light")
        $ luna_r_arm = 4
        hide screen white
        pause.2
        show screen white
        $ hermione.set_cum(face="heavy")
        pause .1
        hide screen white
        with hpunch

        ">You erupt over Hermione's face, coating her in a thick layer of spunk."
        call her_main("!!!!","silly","narrow","base","up",cheeks="blush")
        g9 "{size=+10}YES!{/size}"
        $ luna_r_arm = 3
        call lun_main("*mmmm*, good girl...","base","seductive","sad","down")
        ">Luna's hand slowly continues to stroke your cock, jerking out the last couple of drops of sperm onto Hermione's nose."
        call ctc

        call lun_main("perfect...","base","base","sad","down")
        call her_main("...","grin","narrow","base","dead")
        m "that was fantastic!"

        # Reset zorder
        $ hermione_zorder = 15
        $ luna_zorder = 15
        call lun_main()
        call her_main()

        show screen blkfade
        hide screen bld1
        with d3

        ">Feeling satisfied, you return to sit down at your desk."

        $ luna_r_arm = 1
        hide screen genie_main
        call gen_chibi("sit_behind_desk")

        hide screen blkfade
        with d3

        call lun_main("...","base","seductive","sad","mid")
        $ luna_flip = -1
        $ luna_xpos = 300

        if luna_addicted == True:
            call lun_main("well it's not over yet...","base","seductive","sad","R")
            call her_main("... what?","mad","wide","base","stare",cheeks="blush")
            call her_main("why?","open","base","base","R",cheeks="blush")
            call lun_main("Just look at you!","grin","wide","sad","down")
            call lun_main("Covered in the [lun_genie_name]s delicious cum!","base","seductive","sad","down")
            call her_main("delicious...","disgust","narrow","base","down")
            call her_main("Do you want me to clean myself up?","upset","wink","base","mid")
            call lun_main("And waste all that perfectly good cum one some tart like you?!","upset","wide","angry","down")
            call lun_main("No, I think I'll have to clean this mess up myself...","base","wide","sad","down")
            ">You notice a hunger in Luna's eyes..."
            call her_main("does that mean...","disgust","narrow","base","mid_soft")
            call lun_main("come on hermione, we don't have all day...","normal","angry","angry","R")
            call lun_main("transfiguration starts in 5 minutes...","upset","angry","mad","R")
            call lun_main("so hurry up...","normal","angry","angry","down")
            call her_main("(I can't be late to Professor's McGonagall class...)","annoyed","narrow","worried","down")
            call her_main("I'm not sure what you want me to do...","annoyed","narrow","angry","R")
            call lun_main("stand up now slut...","normal","suspicious","mad","down")
            call her_main("...","annoyed","base","angry","mid")

            hide screen hermione_kneel
            $ hermione_xpos = 480
            show screen hermione_main
            with d3

            ">Hermione slowly stands up, her face still covered in cum..."
            call lun_main("*mmmmm*... look at you... you smell so good...","base","base","sad","empty", cheeks="blush")
            $ luna_xpos = 600
            $ luna_r_arm = 2
            ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
            call her_main("!!!", "angry", "wide", "base", "stare")
            m "(woah...)"
            $ luna_xpos = 630
            call lun_main("*mmmmm*... you taste even better...","base","happyCl","sad","mid")
            call her_main("...", "open", "happyCl", "worried", "mid")
            ">Hermione stands still, letting Luna slowly wipe the cum from her face..."
            $ hermione.set_cum(face="light")
            call her_main("...", "shock", "happyCl", "worried", "mid")
            call lun_main("*mmmmm*...","full","happyCl","sad","mid")
            ">Luna slowly fills her mouth with cum before eventually swallowing."
            call lun_main("*gulp*","base","seductive","sad","empty")
            ">Eventually she finally gets the last strand into her mouth."
            $ hermione.set_cum(None)
            call her_main("...", "disgust", "narrow", "base", "down")
            call lun_main("...","full","happyCl","sad","mid")
            call lun_main("*gulp*","base","seductive","sad","empty")
            call her_main("...", "annoyed", "base", "worried", "R")
            $ luna_l_arm = 2
            $ luna_flip = 1
            $ luna_xpos = 300
            call lun_main("Well, I better be off to... class...","base","base","angry","R")
            call lun_main("Goodbye [lun_genie_name]...","base","seductive","sad","mid")
            call lun_main("Goodbye slut...","normal","angry","angry","R")

            call lun_chibi("leave")

            ">Luna quietly exits the room."

            call update_luna
            $ luna_busy = True

            ">Hermione quietly gets dressed, a shocked look on her face..."

        else:
            call lun_main("well it's not over yet...","base","suspicious","angry","R")
            call her_main("... what?","mad","wide","base","stare",cheeks="blush")
            call her_main("why?","open","base","base","R",cheeks="blush")
            call lun_main("Just look at the mess you made!","normal","angry","angry","down")
            call lun_main("You'll have to clean that up before you can go to class!","base","angry","mad","down")
            call her_main("well normally I just go the prefects' bathroom...","annoyed","base","worried","R")
            call her_main("or I use a towel...","annoyed","narrow","worried","down")
            call her_main("{size=-5}but never Scourgify for some reason...{/size}","annoyed","narrow","angry","R")
            call lun_main("And waste all that perfectly good cum the Professor gave you?!","upset","wide","angry","down")
            call lun_main("No, I think I'll have to stay here and make sure you dispose of it properly...","base","angry","angry","down")
            call her_main("does that mean...","angry","wide","base","stare")
            call lun_main("come on hermione, we don't have all day...","base","seductive","sad","down")
            call lun_main("transfiguration starts in 5 minutes...","normal","angry","angry","down")
            call her_main("(I can't be late to Professor's McGonagall class...)","angry","narrow","base","down")
            call lun_main("now dispose of that cum like a good little slut...","base","mad","sad","down")
            call her_main("...","soft","narrow","annoyed","up")
            ">Hermione slowly starts using her fingers to push your cum into her mouth."
            $ luna_l_arm = 4
            call lun_main("*mmmmm*... that's it... make sure you get it all slut...","base","seductive","sad","down", cheeks="blush")
            m "(woah...)"
            ">Hermione slowly continues to clear her face of cum."
            $ hermione.set_cum(face="light")
            call her_main("...","full_cum","narrow","base","dead")
            ">She fills her mouth with cum before eventually swallowing."
            call her_main("*gulp*","cum","happyCl","worried","mid")
            ">Eventually she finally gets the last strand into her mouth."
            $ hermione.set_cum(None)
            call her_main("...","full_cum","narrow","base","dead")
            call lun_main("see, good sluts don't waste anything do they?","grin","seductive","sad","down")
            call her_main("...","full_cum","narrow","base","dead")
            $ luna_l_arm = 2
            call lun_main("Well, I better be off to... class...","base","base","angry","R")
            call lun_main("Goodbye [lun_genie_name]...","base","seductive","sad","mid")
            call lun_main("Goodbye slut...","normal","angry","angry","R")

            call lun_chibi("leave")

            call update_luna
            $ luna_busy = True

            call her_main("","cum","happyCl","worried","mid")
            ">Hermione swallows the last mouthful of your cum."
            call her_main("*gulp*","cum","happyCl","worried","mid")
            call her_main("*mmmm*...{heart}{heart}{heart}","grin","narrow","base","dead")
            ">She picks herself up from the floor gracefully. Getting dressed before turning to address you."

        $ hermione.wear("bra", "top")

        call her_chibi("stand","mid","base")

        call her_main("[genie_name], what on earth was that all about?!", "scream", "closed", "angry", "mid", xpos="mid", ypos="base")
        call her_main("Why on earth was Luna in here?", "annoyed", "narrow", "angry", "R")
        call her_main("how on earth does she know about me selling favours?", "angry", "base", "angry", "mid")
        if luna_addicted == True:
            call her_main("And {size=+5}why on earth{/size} does she love the taste of your cum?", "angry", "base", "angry", "mid",emote="angry")
        m "I can explain everything..."
        call her_main("Please do...", "annoyed", "narrow", "annoyed", "mid")
        m "do you remember how you yourself described Luna Lovegood as crazy?"
        call her_main("Of course. Everyone knows she's Loony Luna.", "annoyed", "narrow", "angry", "R")
        m "Well I was testing out some new magic..."
        m "And I'm attempting to cure her of her previous condition..."
        m "(I hope she believes this crap...)"
        call her_main("Really?", "shock", "wide", "base", "stare")
        call her_main("But isn't messing around with her mind a little...", "soft", "happy", "base", "R")
        call her_main("unethical?", "angry", "narrow", "base", "down")
        m "Yes, well normally you'd be right, but this is more of a curing of an existing mental condition."
        m "Think about it like I'm trying to cure her of Asperger syndrome."
        call her_main("Actually sir, Asperger's has been reclassified as part of the autism spectrum and is no longer considered its own syndrome.", "open", "closed", "base", "mid")
        m "..."
        m "(Of course she'd know that...)"
        m "Well anyway, my point is there's nothing untoward happening."
        call her_main("...", "annoyed", "narrow", "angry", "R")
        call her_main("Alright then...", "open", "closed", "base", "mid")
        call her_main("But why is she so mean?", "open", "happyCl", "worried", "mid")
        m "I'm not sure. Maybe that's the true her."
        call her_main("I guess that's not impossible...", "annoyed", "narrow", "worried", "down")
        call her_main("But why was she jerking you off?", "open", "narrow", "worried", "down")
        m "Oh um..."
        m "Well that sort of just happened during my evaluation..."
        m "She wanted to help her father's magazine in any way possible, and one thing led to another..."
        if luna_addicted == True:
            call her_main("what about the her loving the taste of your sperm?", "angry", "squint", "base", "mid",cheeks="blush")
            m "Honestly I'm not really sure about that."
            m "I think that's just her being weird..."
        call her_main("...", "annoyed", "base", "angry", "mid")
        call her_main("ugh, fine...", "annoyed", "base", "base", "R")
        call her_main("I guess...", "annoyed", "narrow", "angry", "R",cheeks="blush")
        m "So you don't mind helping out with her in the future?"
        call her_main("What? I have to spend more time with her?", "soft", "wide", "base", "stare")
        call her_main("But she's weird...", "open", "happyCl", "worried", "mid",cheeks="blush")
        m "We can work on that. Besides, don't you want to help out one of your friends?"
        call her_main("*Hmmm*, I suppose that you're right [genie_name].", "annoyed", "closed", "base", "mid")
        call her_main("I can't imagine that the daydreaming Luna would do too well in the real world.", "open", "happy", "base", "mid",cheeks="blush")
        call her_main("and as her friend It's my responsibility to try and save her from that!", "open", "base", "base", "R",cheeks="blush")
        call her_main("!!!", "soft", "wide", "base", "stare")
        call her_main("Maybe we could even have study sessions together!", "grin", "base", "base", "R")
        call her_main("I've always wanted someone to study with! Normally it's only ever Harry and I'm pretty sure he's just there to stare at my boobs...", "annoyed", "narrow", "annoyed", "mid")
        call her_main("(Not that I mind...)", "open", "base", "base", "R")

        m "I'm sure she'd be happy to spend some more time with you."
        call her_main("Do you think so sir? She seemed pretty mean today.", "open", "narrow", "worried", "down")
        m "She'll come around, just give it time."
        call her_main("I hope so sir! A Ravenclaw study buddy would be great!", "smile", "happyCl", "base", "mid",emote="happy")
        m "(more like fuck buddy...)"
        call her_main("...", "base", "happyCl", "base", "mid")

        m "Anyway, thanks for your help today."
        call her_main("anything for my friends [genie_name]...", "soft", "happy", "base", "R")
        m "(Does that mean me?)"
        m "Yes, well, sixty points to Gryffindor!"
        $ gryffindor += 60
        call her_main("Thank you [genie_name]...", "open", "base", "base", "R")

        call her_walk(action="leave")

        jump end_hermione_event

    elif lun_whoring <= 12: #second time
        $ lun_whoring += 1
        $ luna_payout = 150
        $ hermione_payout = 40
        m "How would you feel about another handjob involving Miss Granger?"
        call lun_main("Really?","normal","angry","raised","mid")
        call lun_main("You want to bring her into this again?","upset","mad","angry","mid")
        m "If it's not too much of an issue..."
        call lun_main("*Hmph* so long as you pay me I don't care about you dragging that little hussy up here...","normal","suspicious","angry","R")
        m "Fantastic! I'll summon her now."
        call lun_main("...","upset","suspicious","angry","R")

        ">You summon Hermione to your office."

        call her_walk(action="enter", xpos="right", ypos="base")

        $ luna_r_arm = 2

        call her_main("Hello [genie_name]...", "base", "base", "base", "mid",xpos="base",ypos="base")
        call her_main("Hello Luna...", "open", "squint", "base", "mid")
        call lun_main("Hermione...","normal","suspicious","angry","mid", xpos="mid", flip=True)
        call her_main("What are you doing here?", "annoyed", "narrow", "angry", "R")
        call lun_main("Getting ready to Jerk Dumbledore off onto your face...","base","seductive","angry","mid")
        call her_main("Oh...", "annoyed", "base", "base", "mid")
        call her_main("again?", "upset", "wink", "base", "mid")
        m "Can you blame me?"
        call her_main("I suppose not...", "grin", "base", "base", "R")
        call lun_main("well then...","normal","mad","angry","mid")
        call her_main("what?", "annoyed", "base", "angry", "mid")
        call lun_main("hurry up and strip so we can get this over with...","normal","suspicious","angry","R")
        call her_main("Why do I always have to strip?", "scream", "closed", "angry", "mid")
        call lun_main("because I said so...","upset","suspicious","base","mid")
        call lun_main("unless you don't want to...","normal","angry","base","R")
        call her_main("I suppose I don't mind. It just seems a little unfair that it's only me though...", "annoyed", "narrow", "annoyed", "up")
        call lun_main("tough.","upset","suspicious","mad","mid")

        menu:
            "-Make Luna strip-":
                m "Now, now, Miss Granger is right. It seems only fair for both of you to go nude."
                call lun_main("...","normal","wide","angry","R")
                call her_main("Come on Luna... we're both girls, there's no need to be embarrassed.", "grin", "base", "base", "R")
                call lun_main("embarrassed? hardly.","normal","suspicious","angry","R")
                call her_main("well hurry up and strip then. I thought you wanted to get this over with?", "smile", "base", "base", "R")
                call lun_main(".........","normal","angry","mad","mid")
                call lun_main("Fine... But I expect extra for this [lun_genie_name]!","normal","base","angry","R")

            "-Agree with Luna-":
                m "Now, now, Listen to Luna [hermione_name]."
                call her_main("What? Why?", "angry", "base", "angry", "mid")
                m "Well, if we're being honest, it's mainly because I want to see your naked body again..."
                call her_main("oh... well alright then.", "base", "happy", "base", "mid")
                call lun_main("and you don't want to see me naked?","normal","mad","angry","mid")
                m "I didn't mean it like--"
                call lun_main("*hmph* I suppose I'll strip then [lun_genie_name]... Just so you remember who has the better body.","normal","seductive","angry","mid")
                call lun_main("But I expect extra for this [lun_genie_name]!","upset","angry","angry","R")

        m "sure. I'll add another forty gold."
        $ luna_payout += 40
        call her_main("If she's getting extra then I want some more points!", "scream", "closed", "angry", "mid")
        m "whatever. An extra twenty points for Gryffindor then."
        $ hermione_payout += 20
        call her_main("yay!", "smile", "base", "base", "R")
        call lun_main("I still can't believe you get excited over points.","normal","suspicious","angry","up")
        call her_main("Why? Don't you want to see that look of excitement on the faces of your friends when they win the house cup?", "base", "happy", "base", "mid")
        call her_main("and the look of disappointment on those nasty Slytherins when they lose!", "base", "narrow", "base", "up")
        call lun_main("*pfft*, friends...","normal","base","mad","R")
        call her_main("*aww*... Luna...", "open", "base", "worried", "mid")
        call lun_main("Just shut up and strip, slut.","upset","mad","mad","mid")
        call her_main("fine...", "annoyed", "narrow", "worried", "down")
        show screen blkfade
        with d3

        $ hermione.strip("all")

        #$ luna_wear_top = False
        #$ luna_wear_bra = False
        ##$ luna_wear_bottom = False
        #$ luna_wear_panties = False
        #call update_lun_uniform

        ">Luna and Hermione both strip in front of you."
        ">You can hardly believe your eyes as they slowly strip down in front of each other."
        ">As they're putting their clothes in a pile you get up from your desk and whip your cock out from in between your robes."
        call lun_main("On your knees then, slut...","base","seductive","angry","mid")

        # Hermione chibi kneels
        hide screen luna_main
        hide screen hermione_main
        hide screen bld1
        call her_chibi("sit_naked", "mid", "base")
        call lun_chibi("stand", "right", "base")

        show screen chair_left
        show screen desk
        call gen_chibi("dick_out", "desk", "base")

        hide screen blkfade
        with d3

        call ctc

        $ luna_r_arm = 3
        $ luna_flip = 1
        $ luna_zorder = 16
        $ hermione_zorder = 17

        # Handjob pose
        call her_main(xpos="right", ypos=200)
        call lun_main(xpos=390, flip=False)
        call gen_main(face="grin", base="open", xpos=300, ypos=0)

        with d3

        call her_main("...","base","closed","base","mid")
        ">Luna slowly starts jerking your cock in front of Hermione's face."
        ">Her technique is rough and inexperienced, but decent enough."
        call lun_main("*mmmm*, that's it [lun_genie_name]...","base","seductive","angry","mid")
        call her_main("...","annoyed","base","worried","R")
        call her_main("......","annoyed","base","angry","mid")
        call her_main(".........","annoyed","narrow","annoyed","mid")
        call lun_main("something wrong hermione?","normal","angry","angry","down")
        call her_main("no...","annoyed","narrow","worried","down")
        call lun_main("Good. maybe you should--","base","seductive","angry","down")
        call her_main("You're doing it all wrong!","scream","base","angry","mid",emote="angry")
        call lun_main("What?","normal","wide","base","down")
        call her_main("that's not how he likes it.","annoyed","narrow","angry","R")
        call lun_main("are you sure? He seems to be enjoying it to me...","upset","angry","angry","down")
        call her_main("he's just being nice. You need to focus on the tip with the palm of your hand more.","annoyed","base","angry","mid")
        call her_main("otherwise he doesn't shoot nearly as much...","annoyed","narrow","annoyed","mid")
        call lun_main("*hmph*","normal","angry","angry","R")
        call lun_main("Why don't we ask the old pervert who he prefers then...","normal","mad","mad","down")
        call her_main("alright. Who do you prefer [genie_name]?","annoyed","base","base","mid")

        menu:
            "-Luna-":
                call her_main("What!","angry","base","angry","mid",emote="angry")
                call her_main("That's ridiculous! I'm much better than her at giving handjobs!","annoyed","narrow","annoyed","mid")
                call lun_main("It's about more than just jerking his cock hermione.","base","angry","base","mid")
                call her_main("like what?","annoyed","narrow","angry","R")
                call lun_main("it's about excitement...","base","seductive","angry","mid")
                ">Luna gives your cock light squeeze."
                m "Ah..."
                call her_main("*hmph* at least let me show you how it's done...","disgust","narrow","base","mid_soft")
                call her_main("I'm sure you'll find plenty of ways to \"excite\" him from the floor.","annoyed","narrow","annoyed","mid")
            "-Hermione-":
                call lun_main("WHAT?","upset","wide","base","mid")
                ">Luna gives your cock a painful squeeze, bordering on bruising it."
                call gen_main("AH!","angry", base="hard")
                call her_main("Don't take it too hard Luna, I just have a \"little\" more experience.","base","happyCl")
                ">Luna lets go of your cock."
                call gen_main(face="base")
                $ luna_r_arm = 1
                call lun_main("*hmph*, I suppose you're right. You've probably spent all year with your hands wrapped around any cock you could find.","upset","suspicious","mad","mid")
                call her_main("Hey!","annoyed","narrow","annoyed","mid")
                call lun_main("Am I wrong?","base","angry","angry","mid")
                call her_main("...","disgust","narrow","base","down")
                call her_main("at least let me show you how it's done...","annoyed","narrow","annoyed","mid")

        call lun_main("whatever...","normal","suspicious","angry","R")
        call her_main("...","base","base","base","R")

        show screen blkfade
        with d3

        ">Hermione grabs a hold of your cock while she and Luna switch places."
        ">You're unable to deny that she's much more experienced than Luna, as she is quickly bringing you to the edge."

        # Handjob pose with Luna on knees
        # Note: chibis can't be posed for this part
        $ hermione_zorder = 14
        call lun_main(xpos="right", ypos=200)
        call her_main(xpos=425, ypos="base", flip=False)
        call gen_main(face="grin",base="hard",xpos=300,ypos=0)

        hide screen blkfade
        with d3

        m "Ah... this is it [hermione_name]... not long now."
        call her_main("*mmm*, that's it [genie_name]. just enjoy yourself.", "open", "base", "base", "L")
        call lun_main("as if he could...","normal","angry","angry","R")
        g9 "ah..."
        call lun_main("go on [lun_genie_name], tell her I'm better.","normal","mad","angry","up")
        ">you can barely mutter more than a guttural moan in response."
        g9 "Ugh..."
        call lun_main("...","normal","suspicious","angry","up")
        call lun_main("tell her I'm better!","upset","suspicious","mad","up")
        g9 "*mmmm*"
        call her_main("I'm not sure he can hear you... He must be enjoying himself too much.", "open", "narrow", "worried", "down")
        call her_main("speaking of which... are you ready [genie_name]?", "soft", "happy", "base", "R")
        g9 "*Ugh*... yes... here it comes sluts!"
        call her_main("well why don't I show Luna here how to give a proper handjob.", "base", "narrow", "worried", "down")
        call lun_main("...","normal","seductive","sad","R")
        call her_main("See, he likes it when you do this with your palm...", "base", "squint", "base", "mid")
        call cum_block
        #$ luna_wear_cum = True

        g4 "{size=+5}ARGH! by the gods YES!!!{/size}"
        g4 "{size=+5}WHAT ARE YOU DOING GIRL!?!?!{/size}"
        ">Your cock explodes over Luna's face, covering her until you can barely make out her features."
        $ luna_cum = 12
        call lun_main("*mmmmm*...","base","wide","sad","mid")
        call her_main("that's it, just let out all that {b}nasty{/b} cum.", "grin", "narrow", "annoyed", "up")

        ">Luna collects a strand of cum on the end of her finger, staring at it intently before putting it into her mouth."
        call lun_main("{heart}{heart}{heart}","base","angry","angry","mid")
        call lun_main("it's not nasty!","base","seductive","angry","mid")
        call her_main("oh that's right... I almost forgot how much of a cumslut you are.", "angry", "narrow", "base", "down")
        call lun_main("I am not!","normal","angry","angry","up")
        call her_main("so you're not going to eat all of that \"delicious\" cum on your face then?", "base", "squint", "base", "mid")
        call lun_main("...","base","seductive","angry","mid")
        ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
        $ luna_cum = 13
        call lun_main("...","full","seductive","sad","empty")
        call her_main("that's it Cumslut...", "base", "narrow", "base", "mid_soft")
        call lun_main("{heart}{heart}{heart}","base","happyCl","sad","mid")
        call ctc

        $ luna_cum = 14
        call lun_main("...","full","seductive","sad","empty")
        call her_main("keep going...", "base", "narrow", "worried", "down")
        call lun_main("{heart}{heart}{heart}","base","happyCl","sad","mid")
        $ luna_cum = 15
        call lun_main("...","full","seductive","sad","empty")
        call her_main("*mmmm*...", "grin", "base", "base", "R")
        call lun_main("{heart}{heart}{heart}","base","happyCl","sad","mid")
        #$ luna_wear_cum = False
        call lun_main("...","full","seductive","sad","empty")
        call lun_main("*gulp*","base","happyCl","sad","mid")
        call lun_main("ah...","base","happyCl","sad","mid")
        call lun_main("amazing...","base","seductive","sad","up")
        call lun_main("I didn't know it was possible for someone to cum so much...","base","base","sad","up")
        call her_main("well of course you didn't. I'm surprised you were able to make him cum at all!", "open", "closed", "base", "mid")
        call her_main("what with that shoddy technique of yours...", "annoyed", "squint", "base", "mid")
        call lun_main("it's not that bad...","normal","angry","sad","up")
        call her_main("whatever you have to tell yourself...", "open", "closed", "base", "mid")
        call lun_main("...","normal","mad","angry","up")
        call lun_main("fine... I'm not as good at giving handjobs as you...","normal","suspicious","base","R")
        call lun_main("but that's only because you've spent the entire year in here Whoring yourself out to our headmaster!","normal","suspicious","mad","up")
        call her_main("well I can teach you a few things if you'd like.", "smile", "base", "base", "R")
        call lun_main("what?","pout","angry","base","up")
        call lun_main("why would you help me?","normal","angry","sad","up")
        call her_main("I wouldn't be doing it for free...", "open", "base", "base", "R")
        call lun_main("...","normal","seductive","angry","mid")
        call lun_main("what do you want?","upset","suspicious","sad","up")
        call her_main("before I tell you, you have to answer one question...", "open", "base", "base", "R")
        call lun_main("alright...","normal","suspicious","angry","mid")
        m "(*ugh*... I need to sit down after all that.)"
        hide screen hermione_main
        hide screen luna_main
        hide screen genie_main
        show screen blkfade
        with d3

        ">You slowly move back to your desk and sit down while hermione and luna continue talking."

        $ luna_l_arm = "1"
        $ luna_r_arm = "1"

        call lun_main(xpos="base", ypos="base")
        call her_main(xpos="right", ypos="base", flip=True)

        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","mid","base", flip=True)
        hide screen blkfade
        with d3

        call lun_main("","normal","suspicious","angry","mid")

        call her_main("how are your grades?", "soft", "narrow", "base", "mid_soft")
        call lun_main("WHAT?","open","wide","sad","mid")
        call lun_main("my grades? why do you care?","pout","angry","angry","mid")
        call her_main("it's a simple question...", "base", "narrow", "worried", "down")
        call lun_main("well I'm not going to answer it...","upset","mad","mad","mid")
        call her_main("if you don't want to answer, I'm sure Dumbledore would be more than happy to...", "base", "narrow", "base", "mid_soft")
        call lun_main("...","upset","suspicious","mad","mid")
        call lun_main("......","upset","mad","angry","mid")
        call lun_main(".........","normal","angry","angry","mid")
        call lun_main(".............","normal","suspicious","angry","R")
        call lun_main("fine...","normal","suspicious","sad","R")
        ">Luna lists her marks across all subjects, most of them bordering on a pass and fail with the exception of divination."
        call her_main("what? so low? How do you expect to get a job at the ministry of magic with marks like that?", "scream", "wide", "base", "mid")
        call lun_main("...","normal","suspicious","sad","down")
        call her_main("at this rate you'll have to get a job in the muggle world.", "disgust", "narrow", "base", "down")
        call lun_main("you think I don't know that? why do you think I agreed to all this in the first place...","upset","angry","angry","mid")
        call lun_main("Just stop humiliating me and tell me your stupid demand!","upset","mad","angry","mid")
        call lun_main("What is it anyway? Do you expect me to walk around the school half naked?","upset","suspicious","angry","R")
        call her_main("Of course not...", "open", "base", "worried", "mid")
        call lun_main("then what?","normal","angry","mad","mid")
        call her_main("In exchange for me teaching you how to be a better lover, I want you to be my study buddy.", "open", "closed", "base", "mid")
        call lun_main("...","upset","suspicious","angry","mid")
        call lun_main("what?","normal","wide","sad","mid")
        call lun_main("why would you of all people need a study buddy? Aren't your grades perfect?","normal","suspicious","angry","mid")
        call her_main("of course... but that's not why I want a study buddy.", "soft", "base", "base", "R")
        call her_main("It gets lonely in the library sometimes...", "annoyed", "narrow", "angry", "R")
        call her_main("Plus I've always wanted a Ravenclaw to study with, but all the other girls refuse to even talk to me.", "open", "base", "worried", "mid")
        call her_main("Harry and Ron have just been staring at my tits the whole time.", "open", "closed", "angry", "mid")
        call her_main("{size=-5}Not that I really mind...{/size}", "base", "narrow", "base", "up")
        call her_main("Think about all the fun we can have! You could even quiz me on advanced transmogrification!", "smile", "happyCl", "base", "mid")
        call lun_main("...","normal","angry","angry","mid")
        call her_main("We could also work on your grades!", "base", "happyCl", "base", "mid")
        call her_main("If you work hard, we can get them up before the {i}O.W.L.{/i}s!", "grin", "base", "base", "R")
        call lun_main("Whatever... As long as you teach me how to wring as much gold out of the old man's balls as possible, I don't care...","pout","suspicious","angry","R")
        call her_main("Hurray!", "grin", "happyCl", "worried", "mid")
        m "I'm still here you know."
        call her_main("Of course you are, professor.", "grin", "base", "base", "R")
        call lun_main("...","normal","suspicious","base","R")
        call her_main("Well then, let's go Luna, we still have got a little bit of free time before classes.", "smile", "base", "base", "R")
        call her_main("Perhaps we should visit the library.", "smile", "happyCl", "base", "R")
        call lun_main("You want to go there now?","normal","wide","angry","mid")
        call her_main("No offence, but with your grades it's better to start early.", "grin", "happyCl", "worried", "mid",emote="sweat")
        call her_main("No time to waste. {heart}", "base", "happyCl", "worried", "mid")
        m "It's not going to impact our \"lessons\", I hope?"
        call her_main("of course not, [genie_name]...", "grin", "base", "base", "R")
        call lun_main("*tch*","normal","angry","angry","mid")
        m "In that case, here's your payment, [hermione_name]."
        $ gryffindor += hermione_payout
        m "{number=hermione_payout} points to Gryffindor!"
        call her_main("Thank you, [genie_name].", "base", "closed", "base", "mid")
        $ luna_gold += luna_payout
        $ gold -= luna_payout
        m "And of course, {number=luna_payout} gold coins for Luna."
        ">You hand Luna the pile of coins."
        $ luna_flip = 1
        call lun_main("Thank you, [lun_genie_name]...","normal","closed","mad","R")

        hide screen luna_main
        hide screen hermione_main
        show screen blkfade
        with d3

        ">Luna and hermione quickly get dressed before leaving the room together."

        #call load_luna_clothing_saves
        #call update_lun_uniform

        $ hermione.wear("all")

        show screen luna_main
        show screen hermione_main
        hide screen blkfade
        with d3

        call her_main("this is going to be so much FUN!", "grin", "narrow", "annoyed", "up")
        call her_walk(action="leave")

        call lun_main("(What have I agreed to...)","normal","suspicious","sad","down")
        call lun_walk(action="leave")

        $ luna_busy = True
        $ hermione_busy = True

        jump end_hermione_event


    else: #third handjob event, needs to be repeatable
        if lun_whoring <= 13:
            $ lun_whoring += 1
        label luna_handjob_hermione_call:
            pass
        m "How about another handjob, [luna_name]?"
        call lun_main("sure... do you want hermione here as well?","normal","suspicious","angry","R")
        m "You read my mind!"
        call lun_main("alright, but I expect to be the one doing the... job.","normal","angry","base","R")
        m "if you insist."
        call lun_main("...","normal","seductive","base","mid")
        call lun_main("just hurry up and bring her up here...","normal","seductive","base","R")
        ">You summon hermione to your office."
        call play_sound("door")

        call her_walk(action="enter", xpos="right", ypos="base")

        call lun_main(xpos="mid", ypos="base", flip=True)

        call her_main("hello, [genie_name]!", "base", "happyCl", "base", "mid", xpos="base", ypos="base")
        call her_main("hello, Luna!", "smile", "happyCl", "base", "mid")
        m "You seem cheerful."
        call her_main("why wouldn't I be? are we going to work on handjobs today?", "open", "base", "base", "R")
        call lun_main("just hurry up and get on your knees slut...","upset","seductive","angry","mid")
        call her_main("someone's eager!", "smile", "happyCl", "base", "mid",emote="happy")
        call lun_main("...","base","suspicious","angry","mid")

        show screen blkfade
        with d3

        ">You stand up from your desk while hermione slowly strips and kneels in front of you."

        $ hermione.strip("all")

        # Hermione chibi kneels
        hide screen luna_main
        hide screen hermione_main
        hide screen bld1
        call her_chibi("sit_naked", "mid", "base")
        call lun_chibi("stand", "right", "base")

        show screen chair_left
        show screen desk
        call gen_chibi("dick_out", "desk", "base")

        hide screen blkfade
        with d3

        call ctc


        $ luna_zorder = 16
        $ hermione_zorder = 17

        # Handjob pose
        $ luna_r_arm = 2

        call her_main(xpos="right", ypos=200)
        call lun_main(xpos=390, flip=False)
        call gen_main(face="grin", base="hard", xpos=300, ypos=0)
        with d3

        call her_main("Aren't you going to get naked as well Luna?","annoyed","narrow","angry","R")
        call lun_main("Why would I do that?","normal","angry","mad","R")
        call her_main("As I have told you before, it's better if you're naked while you stroke it.","annoyed","narrow","angry","R")
        call lun_main("...","normal","angry","angry","mid")
        call lun_main("Fine...","normal","suspicious","sad","R")
        call her_main("Great!","base","base","base","mid")
        call lun_main("I expect something extra for doing this, [lun_genie_name]!","normal","seductive","angry","R")
        g9 "That seems fair."
        call lun_main("...","normal","suspicious","angry","mid")

        show screen blkfade
        with d3

        ">Luna slowly strips as well, carefully putting her clothes in a pile next to hermione's."

        #$ luna_wear_top = False
        #$ luna_wear_bra = False
        ##$ luna_wear_bottom = False
        #$ luna_wear_panties = False
        #call update_lun_uniform
        call lun_main()

        hide screen blkfade
        with d3

        call lun_main("Happy now?","normal","angry","angry","mid")
        m "Very."
        call lun_main("Good... Let's just get this over with.","normal","angry","mad","R")
        call her_main("...","annoyed","squint","angry","mid")
        call lun_main("What is it, Hermione?","normal","suspicious","angry","mid")
        call her_main("Could you at least try and act as if you like it a little more?","open","squint","base","mid")
        call lun_main("Fine, whatever...","normal","suspicious","angry","R")
        call her_main("Awesome!","base","narrow","worried","down")
        $ luna_r_arm = 3
        ">Luna spits into her hand before wrapping it around your cock."
        ">She's barely started stroking it, but you can already tell her technique has improved significantly."
        m "*Mmmm*, yes that's it slut."
        m "Just like that."
        call lun_main("...","base","seductive","angry","mid")
        call her_main("You're doing good Luna... Now try focusing on the tip a little more, like I showed you.","base","narrow","base","mid_soft")
        call lun_main("Like this?","normal","seductive","sad","mid")
        ">Luna wraps her hand around the head of your cock, rotating her hand slightly as she pumps her hand."
        m "*Ugh*... yes..."
        call her_main("Good... Now go back to caressing the shaft.","open","closed","base","mid")
        call her_main("Try not to focus on one area for too long...","open","closed","base","mid")
        call lun_main("Okay...","base","angry","sad","mid")
        ">This continues for a while, Luna listening intently to Hermione's instructions."
        g9 "*Ugh*... I'm getting close!"
        call her_main("Alright, slow down a little...","base","narrow","worried","down")
        call lun_main("Why? Isn't he about to cum?","upset","wide","sad","mid")
        g9 "Don't slow down now!"
        call her_main("*shhh* [genie_name], I'm trying to give lessons here!","upset","closed","base","mid")
        g9 "..."
        ">Luna slows her hand back down, bringing you almost painfully back from the edge of orgasm."
        call her_main("Continuing, if you keep teasing him, it will make him cum much harder.","grin","narrow","base","dead")
        call her_main("I read about this technique in \"witches weekly\"... it's called edging!","base","narrow","worried","down")
        call lun_main("*hmmm*, and you're sure it's safe?","normal","seductive","raised","mid")
        call lun_main("He almost seems like he's in pain...","base","seductive","angry","mid")
        ">Luna gives your cock a hard squeeze as she looks sadistically at your cock."
        $ genie_face = "characters/genie/face/angry.webp"
        g4 "*ah*!"
        $ genie_face = "characters/genie/face/grin.webp"
        call her_main("Trust me, he's enjoying it...","open","closed","base","mid")
        call her_main("He will thank you later, once you {i}let{/i} him cum.","grin","narrow","annoyed","up")
        call lun_main("*mmmmm*... I like the sound of that.","base","mad","mad","mid")
        $ genie_face = "characters/genie/face/angry.webp"
        g4 "(I'm about to explode!)"
        call her_main("Juuuust a while longer...","angry","wink","base","mid")
        call her_main("It can get a little... frustrating if you do it for too long.","base","narrow","worried","down")
        call lun_main("Really? I don't mind that...","base","mad","mad","mid")
        g4 "I do!"
        call lun_main("Fine then... How should I finish him off?","base","seductive","angry","down")
        call her_main("hmmm...","base","squint","base","mid")
        show screen blkfade
        with d3

        $ genie_face = "characters/genie/face/base.webp"
        ">Hermione slowly stands up and whispers something into Luna's ear before kneeling back down."
        hide screen blkfade
        with d3

        call lun_main("Are you sure?","base","wide","sad","mid")
        call her_main("Oh trust me, he will love it...","grin","base","base","R")
        m "love what?"
        call lun_main("Quiet, [lun_genie_name]!","normal","mad","angry","mid")
        ">Luna gives your cock another painful squeeze before resuming stroking the length of it."
        $ genie_face = "characters/genie/face/angry.webp"
        g4 "*Ah*!"
        $ genie_face = "characters/genie/face/open.webp"
        m "can you stop that?"
        call lun_main("I'll stop it once you learn to be quiet.","pout","suspicious","angry","mid")
        $ genie_face = "characters/genie/face/base.webp"
        m "..."
        call her_main("*mmmm*... that's it Luna...","soft","narrow","annoyed","up")
        call her_main("he's almost there... do it now.","grin","narrow","base","dead")
        call her_main("*aahhhh*...","open_wide_tongue","happy","base","R", ypos=230)
        ">Hermione opens her mouth as wide as she can while Luna pulls you forward by your cock into her eager hole."

        $ genie_face = "characters/genie/face/angry.webp"
        g4 "!!!"
        call her_main("*hommmph*...","open_wide_tongue","narrow","annoyed","up")
        call lun_main("there we go...","base","seductive","sad","mid")

        ">Hermione starts eagerly lapping at the head of your cock while Luna starts furiously stroking your shaft."
        g4 "{size=+5}FUCK YES!!!{/size}"
        g4 "{size=+5}here it comes, you sluts!{/size}"

        ">Luna continues stroking your cock at a blistering pace while hermione moves backwards slightly, leaving her mouth open and waiting."

        g4 "{size=+10}*ARGHHH*!!!!{/size}"
        show screen white
        pause.1
        $ hermione.set_cum(face="light")
        hide screen white
        pause.2
        show screen white
        pause .1
        $ hermione.set_cum(face="heavy")
        hide screen white
        with hpunch

        g4 "{size=+5}*ugh*! YES!!!{/size}"
        call lun_main("So much...","base","wide","sad","mid")
        call her_main("...","full_cum","narrow","base","dead")
        call her_main("*gulp*","cum","happyCl","worried","mid")
        call her_main("*Mmm*... I told you it would make him cum more...","grin","narrow","base","dead")
        call lun_main("even so...","base","seductive","sad","mid")
        ">Luna stares at hermione with a fierce hunger in her eyes."
        call lun_main("stand up... please...","normal","seductive","sad","mid")
        ">Exhausted from the handjob, you decide to take a seat while Hermione and Luna clean up."
        call her_main("only because you asked nicely...","open","base","base","R")
        hide screen genie_main
        hide screen hermione_kneel
        hide screen luna_main
        show screen blkfade
        with d3

        ">Hermione slowly stands up, her face simply drenched in cum..."

        $ hermione_zorder = 15
        $ luna_r_arm = 1

        call lun_main(xpos="mid", flip=True)
        call her_main(xpos="right", ypos="base")

        call reset_genie

        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","mid","base")
        call update_her_uniform

        hide screen blkfade
        with d3

        call lun_main("*mmmmm*... just look at you... you look so... delicious...","base","base","sad","empty", cheeks="blush")
        call her_main("...", "open", "base", "base", "R")

        $ luna_r_arm = 2

        ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
        call her_main("go on...", "soft", "narrow", "annoyed", "up")
        m "(*mmmm*...)"
        call lun_main("*mmmmm*... you taste even better...","base","happyCl","sad","mid")
        call her_main("...", "grin", "narrow", "base", "dead")
        ">Hermione stands still, letting Luna slowly wipe the cum from her face..."
        $ hermione.set_cum(face="light")
        call her_main("that's it... make sure you get it all...", "base", "narrow", "worried", "down")
        call lun_main("*mmmmm*...","full","happyCl","sad","mid")
        ">Luna slowly fills her mouth with cum before swallowing all of it."
        call lun_main("*gulp*","base","seductive","sad","empty")
        ">Eventually she gets the last strand into her mouth."
        $ hermione.set_cum(None)
        call her_main("better?", "base", "narrow", "base", "mid_soft")
        call lun_main("...","full","happyCl","sad","mid")
        call lun_main("*gulp*","base","seductive","sad","empty")
        call lun_main("much.","base","seductive","sad","empty")
        call her_main("good.", "base", "squint", "base", "mid")

        menu:
            "-Ask about study sessions-":
                m "So how have your recent study sessions been going?"
                $ luna_l_arm = 2
                call lun_main("they've been OK...","normal","suspicious","sad","R")
                call her_main("stop being such a negative nancy, Luna. They have been amazing [genie_name]!", "smile", "happyCl", "base", "mid",emote="happy")
                call lun_main("...","normal","suspicious","sad","down")
                call her_main("Luna quizzed me on advanced transmogrification spells, advanced potion recipes and even complex herbology!", "smile", "happyCl", "base", "mid")
                call lun_main("I don't even thinks she needs quizzing, she got everything right...","upset","angry","angry","R")
                call her_main("the tutoring was even better!", "base", "happyCl", "base", "mid")
                call her_main("we studied transfiguration, D.A.D.A, handjobs, potions, titjobs, spells, dirty talk and Herbology!", "grin", "base", "base", "R")
                m "sounds like quite the lesson..."
                call lun_main("......","normal","seductive","sad","R")
                call her_main("If we keep these sessions up I'm sure Luna will pass her {i}O.W.L.{/i}s with flying colours!", "base", "happy", "base", "mid")
                call lun_main(".........","base","seductive","sad","down")

                if not luna_herm_talk:
                    $ luna_herm_talk = True
                    call her_main("I can't wait to see what mark she gets when she has to do them!", "smile", "happyCl", "base", "mid",emote="happy")
                    call lun_main("I think you mean when {b}we{/b} have to do them...","normal","suspicious","angry","mid")
                    call her_main("Oh, I don't have to do my {i}O.W.L.{/i}s anymore...", "base", "happyCl", "base", "mid")
                    call lun_main("What? Why not?","normal","wide","sad","mid")
                    call her_main("Do you want to tell her or should I?", "base", "narrow", "worried", "down")
                    m "(I have no idea what she's talking about)"
                    m "Why don't you fill her in?"
                    call her_main("alright then...", "base", "narrow", "base", "mid_soft")
                    call her_main("I already did my {i}O.W.L.{/i}s last year.", "grin", "happyCl", "worried", "mid",emote="sweat")
                    call lun_main("Really? How?","normal","angry","sad","mid")
                    call her_main("Well, I'd already been testing myself on past years' exams since I was a third year.", "grin", "happyCl", "worried", "mid")
                    call her_main("Last year I finally felt that I was ready for the real thing. So I spoke to Professor Dumbledore and Professor McGonagall.", "base", "base", "base", "R")
                    call her_main("I explained my situation and they agreed to test me early.", "base", "base", "base", "R")
                    call her_main("I got the highest mark since Dumbledore himself took them!", "smile", "happyCl", "base", "mid",emote="happy")
                    call lun_main("Wait... If you've already completed your {i}O.W.L.{/i}s, why are you still at school?","upset","suspicious","angry","mid")
                    call her_main("I didn't want to miss out on school work or spending time with my friends...", "base", "happyCl", "base", "mid")
                    call her_main("So I've just been doing additional study in the library after classes in exchange for a special recommendation from the school.", "smile", "happyCl", "base", "mid")
                    call her_main("although recently I've been spending most of my free time in here...", "base", "narrow", "worried", "down")
                    call lun_main("but why did you want to study with me then? Surely you don't need the quizzing anymore?","normal","mad","raised","mid")
                    call her_main("I've always wanted to practise teaching and I get to help out my friend while I do it!", "grin", "base", "base", "R")
                    call lun_main("Friend?","normal","suspicious","sad","mid")
                    call her_main("of course we're friends Luna! Maybe even best friends after all this...", "base", "happy", "base", "mid")
                    call lun_main("...","normal","seductive","sad","mid")
                    call lun_main("whatever...","normal","angry","angry","R",tears="soft")
                    call lun_main("if you two are done talking I'm going to class...","normal","mad","angry","mid",tears="soft")

                    ">Luna quickly gets dressed before leaving."

                    #call load_luna_clothing_saves
                    #call update_lun_uniform

                    call lun_walk(action="leave")

                    call her_main("...", "annoyed", "base", "worried", "R")
                    call her_main("did she seem ok to you sir?", "annoyed", "base", "worried", "R")
                    m "I think so. She's probably just not used to you being nice to her."
                    call her_main("maybe... If it's alright with you I might go check up on her.", "angry", "base", "worried", "mid")
                    m "Suit yourself. I'm getting pretty sleepy anyway."
                    call her_main("thank you, [genie_name].", "base", "happyCl", "worried", "mid")
                    hide screen hermione_main
                    with d3

                    ">Hermione puts her clothes back on and then heads after Luna."

                    $ hermione.wear("all")

                    call her_walk(action="leave")

                else:
                    jump luna_her_hj_end

            "-let them go-":
                label luna_her_hj_end:
                    m "Alright, you two can go now."
                    $ luna_l_arm = 2
                    call lun_main("*hmph*, not before you pay us!","normal","angry","angry","R")
                    m "Right, nearly forgot."
                    call her_main("...", "annoyed", "squint", "base", "mid")
                    $ gryffindor += 50
                    m "Fifty points to Gryffindor!"
                    call her_main("thank you [genie_name]...", "base", "closed", "base", "mid")
                    call lun_main("...","normal","seductive","base","R")
                    $ luna_gold += 150
                    $ gold -= 150
                    m "150 gold for Luna."
                    call lun_main("thanks [lun_genie_name]...","normal","seductive","base","R")
                    call her_main("...", "annoyed", "narrow", "angry", "R")
                    m "if that's all, I think I need a nap."
                    call her_main("alright then...", "base", "base", "base", "mid")
                    ">Hermione and Luna get dressed before leaving your office together."
                    hide screen luna_main
                    hide screen hermione_main

                    #call load_luna_clothing_saves
                    #call update_lun_uniform

                    $ hermione.wear("all")

                    with d3
                    pause.8

                    call lun_chibi("hide")
                    call her_chibi("hide")
                    with d3

                    call play_sound("door")

                    ">You can hear them talking and laughing together as they shut your door."

    $ luna_busy = True
    $ hermione_busy = True

    jump end_hermione_event
