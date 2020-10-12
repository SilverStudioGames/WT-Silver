

label luna_favour_7: #Luna and Hermione Sex #DONE

    m "Luna."
    call lun_main("yes sir...","base","base","sad","mid")
    m "Today I have a new type of favour for you."
    call lun_main("really?","base","wide","base","mid")
    m "Today, we'll be--"
    call lun_main("Wait!","base","wide","angry","mid")
    call lun_main("Before you ask me...","base","seductive","sad","R")
    call lun_main("can you please summon Hermione?","normal","seductive","sad","mid")
    m "You don't even know what I'm going to ask you yet!"
    call lun_main("I have a fair idea sir...","base","angry","angry","mid")
    call lun_main("And if it's alright with you, I'd prefer that Hermione be here as well.","base","seductive","sad","R")
    m "well, I'm not going to say no to that!"
    call lun_main("Thank you, sir...","base","happyCl","sad","mid")
    ">You summon Hermione up to your office."
    call her_walk(action="enter", xpos="right", ypos="base")
    call lun_main(xpos="mid", flip=True)
    call her_main("Hey Luna!!!", "grin", "wink", "base", "L", xpos="base", ypos="base", trans=d3)
    call her_main("[genie_name].", "normal", "happyCl", "base", "mid")
    call her_main("So what does he want from us today?", "smile", "narrow", "base", "mid_soft")
    call her_main("Another blowjob?", "grin", "base", "base", "R")
    call lun_main("He hasn't even asked yet.","base","seductive","sad","R")
    call lun_main("I wanted you to be here for it.","base","suspicious","sad","mid")
    call her_main("you mean...", "shock", "happy", "base", "mid_soft")
    call her_main("*N'awww* that's so sweet Luna.", "grin", "base", "base", "mid_soft")
    call her_main("You better ask her nicely sir!", "mad", "slit", "low", "stare")
    m "You don't even know what--"
    call her_main("Everyone knows what you're going to ask for next sir.", "open", "closed", "base", "mid")
    call her_main("At least try and make it a little romantic for her...", "smile", "base", "base", "mid_soft")
    m "Romantic?"
    call her_main("Work something out!", "open", "base", "angry", "mid")
    call lun_main("You really don't need to worry about it [lun_genie_name]...","normal","base","sad","down")
    call her_main("Shh! Your first time needs to be at least a little bit special, Luna!", "upset", "narrow", "angry", "R")
    m "..."
    m "Luna Lovegood."
    m "Would you do me the honour?"
    call lun_main("...","base","wide","sad","mid", flip=False, trans=d3)
    call her_main("(That's the corniest thing I've ever heard...)", "open", "wink", "base", "mid")
    call lun_main("I...","base","wide","sad","R")
    call lun_main("I......","normal","wide","sad","R")
    call lun_main("I can't!","upset","wide","sad","down")
    call her_main("What?", "shock", "wide", "base", "stare")
    call her_main("Why not Luna? We've talked about this...", "soft", "base", "worried", "mid")
    call her_main("We even spent all weekend \'practising\'...", "normal", "base", "worried", "R")
    call lun_main("I know...","pout","base","mad","R")
    call lun_main("It's just...","soft","base","sad","down")
    call lun_main("I don't think I can handle it...","upset","base","sad","R")
    call lun_main("I'm not like you... I can't be good at everything...","open","happyCl","sad","mid")
    show screen blkfade

    "*SLAP*"
    ">You close your eyes and recoil, expecting the stinging in your face to start any moment, however it never comes."
    hide screen blkfade
    with d3

    ">Instead, you notice a bright red mark starting to form across Luna's face."
    call her_main("You need to stop thinking that right now!", "open", "base", "angry", "mid")
    call lun_main("but I'm not as--","pout","base","sad","R", cheeks="blush")
    call her_main("Luna... you have to Stop measuring yourself against other people.", "open", "wink", "base", "mid")
    call her_main("You're the cutest, nicest, zaniest girl at this school and I don't know what's happened to you recently, but you need to just calm down and enjoy your life.", "open", "wink", "base", "mid")
    call lun_main("but...","normal","wide","sad","down", cheeks="blush",tears="crying")
    call her_main("*Shhh*... It's okay...", "soft", "base", "base", "mid_soft")
    call her_main("Why don't we start by enjoying our headmaster's big cock, *Hmm*?", "grin", "happy", "base", "mid_soft")
    call her_main("Would that make you feel a little better?", "smile", "wink", "base", "mid")
    call lun_main("y-yes...","base","seductive","sad","R", cheeks="blush",tears="crying")
    show screen blkfade
    with d3

    hide screen luna_main
    hide screen hermione_main
    her "Good... Now let's take our clothes off and hop up onto his desk!"
    lun "Hermione... I'm still not so sure about this..."
    lun "I don't know if I'm ready..."
    her "*Shhh*, It's alright... I'll go first OK?"
    lun "Really? You'd do that for me?"
    her "Of course! Besides, I don't really mind doing it..."
    her "I'm sure you'll love it as well!"
    lun "I hope so..."
    her "Are you ready, [genie_name]?"

    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_1"
    $ ccg2 = "herm_1"
    $ ccg3 = "blank"
    show screen ccg
    hide screen bld1
    hide screen blkfade
    with d3

    m "I sure am!"
    call ctc

    menu:
        "-Be gentle...-":
            ">You take a hold of Hermione's legs, slowly parting them as you push the head of your cock up against her tender pussy."
            $ ccg2 = "herm_2"
            her "Now just take it slowly [genie_name], so Luna can get a good idea of what she's--"
            ">You slide the head of your cock softly into her waiting pussy."
            $ ccg2 = "herm_3"
            call ctc
            her "{heart}ah{heart}"
            m "*Mmmm*, that's it slut... we can take it nice and slow..."
            ">You slide the rest of your cock into her needy hole."
            $ ccg2 = "herm_4"
            her "ah{heart}{heart}{heart}..."

        "-Be rough!-":
            ">You take a hold of Hermione's legs, lining up the head of your cock with her tender pussy."
            her "Now just take it slowly, so Luna can get an idea of--"
            ">You slam into her, burying your cock to the hilt."
            her "!!!"
            g4 "*Mmmm*, that's it slut... You're still so tight."
            her "ah{heart}{heart}{heart}... this is..."

    call ctc
    her "So {heart}gooood{heart}..."
    $ ccg1 = "luna_2"
    lun "*mmm*..."
    g4 "{size=+10}Here we go!{/size}"
    ">You start thrusting into and out of hermione, her pussy spasms around your hard member."
    $ ccg2 = "herm_5"
    her "ah{heart}... ah{heart}... ah{heart}..."
    her "{size=-8}harder...{/size}"
    $ ccg1 = "luna_3"
    lun "What's that Hermione?"
    her "{size=-5}harder...{/size}"
    $ ccg1 = "luna_4"
    lun "I think you better stop sir... it sounds like you might be hurting her!"
    $ ccg2 = "herm_6"
    her "HARDER!!!"
    g4 "Ugh... take this you filthy whore!"
    $ ccg1 = "luna_5"
    lun "..."
    her "Yes, yes!"
    her "I'm a nasty little whore..."
    $ ccg2 = "herm_7"
    her "Getting {heart}fucked{heart} silly in front of her best friend..."
    $ ccg1 = "luna_6"
    lun "(best?...)"
    $ ccg2 = "herm_8"
    her "I'm even going to cum in front of her!"
    $ ccg2 = "herm_5"
    her "ah... here I..."
    $ ccg1 = "luna_7"
    lun "Already?"
    her "Y-y-yes... {size=+5}I'm-- {heart}{heart}{heart}{/size}"
    $ ccg2 = "herm_9"
    her "{size=+5}CUMMING!!!{/size}"
    ">Hermione's cunt shakes violently as her eyes roll back into her head..."
    call ctc
    $ ccg2 = "herm_10"
    m "Ugh... that's it girl..."
    $ ccg2 = "herm_11"
    her "sooooo goooooooooooood...{heart}{heart}{heart}"
    $ ccg1 = "luna_8"
    lun "wow..."
    ">You pull your rock hard cock out of Hermione's needy hole, despite her best efforts to wrap her legs around your torso."
    $ ccg2 = "herm_12"
    her "Just... a little longer [genie_name]..."
    m "Now, now, [hermione_name]... don't be greedy..."
    $ ccg2 = "herm_13"
    her "..."
    her "You're right [genie_name]..."
    $ ccg2 = "herm_14"
    her "Sorry Luna..."
    $ ccg2 = "herm_15"
    her "I'm just such a greedy little cock-slut..."
    call ctc
    $ ccg1 = "luna_9"
    lun "I know..."
    $ ccg2 = "herm_14"
    her "..."
    ">You move away from Hermione's sweaty body and over to Luna's milky white form."
    $ ccg1 = "luna_10"
    ">You grab a hold of her legs, lining up your cock with her dripping cunt."
    m "Are you ready, [lun_name]?"
    $ ccg1 = "luna_11"
    lun "I... I think so..."
    $ ccg1 = "luna_12"
    lun "Are you sure everything will be fine, Hermione?"
    $ ccg2 = "herm_16"
    $ ccg1 = "luna_13"
    ">Hermione gently takes a hold of Luna's hand."
    call ctc
    her "I promise."
    $ ccg1 = "luna_14"
    lun "Thanks Hermione-*eeeehhhh*- {heart}"
    ">You decide to interrupt the cute moment by slowly forcing the head of your cock into Luna's soft pussy."
    $ ccg1 = "luna_15"
    lun "ah... it's... so hot..."
    call ctc
    $ ccg2 = "herm_17"
    her "*mmmm*, yeah it is..."
    $ ccg1 = "luna_16"
    lun "ah...{heart}{heart}{heart}"
    her "*Mmmm*, she seems to like it, [genie_name]..."
    $ ccg1 = "luna_17"
    ">Luna barely muffles a timid little moan in response."
    $ ccg2 = "herm_18"
    her "Maybe she's ready for a little more?"
    $ ccg1 = "luna_18"
    lun "ah... yes..."
    lun "Just please... go slowly sir..."
    her "*Hmm*, I'm not sure he'll be able to control himself."
    show screen blkfade
    with d3
    ">Hermione leans over and whispers into Luna's ear."
    $ ccg_folder = "luna_kiss"
    $ ccg1 = "1"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    her "I know I wouldn't."
    call ctc
    show screen blkfade
    with d3
    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_18"
    $ ccg2 = "herm_18"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    ">As if to punctuate the end of Hermione's sentence, you slowly thrust the rest of your length into Luna's tight fuckhole."
    hide screen blkfade
    with hpunch
    $ ccg1 = "luna_19"
    lun "{size=+10}!!!{/size}"
    $ ccg1 = "luna_20"
    lun "*Ahhhhhhh*"
    $ ccg2 = "herm_19"
    her "*Mmmm*, maybe that was a little too much sir..."
    m "ugh... I couldn't help myself."
    ">You slowly pull your cock out of her, until only the tip remains, before thrusting forward, again burying it in its newfound home."
    g4 "Fuck she's so tight..."
    g4 "I can barely move..."
    $ ccg1 = "luna_20"
    lun "*ah-a-ahhhhh*..."
    ">You slowly start to settle into a deep, rhythmic motion with your hips. Each thrust eliciting a gentle moan from Luna's lips."
    $ ccg2 = "herm_20"
    her "How is she [genie_name]?"
    m "incredible..."
    $ ccg1 = "luna_21"
    lun "thank you sir..."
    $ ccg1 = "luna_22"
    ">You begin to notice tears are starting to form in the corners of Luna's eyes."
    $ ccg2 = "herm_16"
    her "Is everything alright Luna?"
    $ ccg2 = "herm_18"
    her "It's not hurting too much is it?"
    $ ccg1 = "luna_23"
    lun "I-It's nothing!"
    $ ccg2 = "herm_17"
    her "Are you sure? If it's too much we can stop..."
    $ ccg1 = "luna_24"
    lun "No!"
    lun "It's just... I'm... just..."
    lun "So..."
    $ ccg1 = "luna_25"
    lun "Happy..."
    ">You notice Luna and Hermione's hands tremble as Hermione squeezes hers tightly around Luna's."
    $ ccg2 = "herm_21"
    her "So you like it?"
    $ ccg1 = "luna_26"
    lun "Ah..."
    lun "yes... I think so..."
    $ ccg1 = "luna_27"
    lun "It's a little painful... but it's..."
    $ ccg1 = "luna_26"
    lun "ah...{heart}{heart}{heart}"
    $ ccg1 = "luna_25"
    lun "Still nice..."
    $ ccg2 = "herm_19"
    her "Yay!!! I knew you'd love it! This is going to be so much fun from now on!"
    $ ccg1 = "luna_29"
    lun "From... now on?"
    her "{i}Duh{/i}... You don't think Dumbledore's going to be happy with only fucking that yummy pussy once, do you?"
    $ ccg1 = "luna_24"
    lun "ah...{heart}{heart}{heart} I guess n-not..."
    $ ccg2 = "herm_18"
    her "I know I wouldn't..."
    $ ccg1 = "luna_29"
    lun "w-what?"
    $ ccg2 = "herm_17"
    her "*shhh*... just enjoy yourself."
    $ ccg1 = "luna_26"
    lun "a-alright...{heart}"
    g4 "Gods you're tight..."
    $ ccg1 = "luna_25"
    lun "Ah... thank you... sir..."
    $ ccg2 = "herm_21"
    her "Good girl, he likes it when you call him that."
    $ ccg1 = "luna_18"
    lun "Really?"
    $ ccg2 = "herm_18"
    her "*Mhmmm*... He likes it even more when you tell him what you're feeling."
    $ ccg1 = "luna_23"
    lun "I-I don't know... ah...{heart} if I could do that..."
    lun "It's too embarrassing!"
    $ ccg2 = "herm_17"
    her "I'd like it too..."
    $ ccg1 = "luna_18"
    lun "..."
    lun "Well, alright..."
    $ ccg1 = "luna_21"
    lun "It's... ah...{heart} it's like he's scratching an itch I never knew I had."
    her "*mmmmm*, I know that itch..."
    lun "ah...{heart} does it go away?"
    $ ccg2 = "herm_18"
    her "eventually... but not for long..."
    $ ccg1 = "luna_17"
    lun "ah...{heart}"
    $ ccg1 = "luna_20"
    lun "You mean?"
    $ ccg2 = "herm_19"
    her "*Mhmmm*... Don't worry, I'm sure Dumbledore will be more than happy to scratch it for you..."
    $ ccg2 = "herm_18"
    her "Or if he's too busy... well... you could always come to my room..."
    $ ccg1 = "luna_17"
    lun "{heart}{heart}{heart}"
    $ ccg1 = "luna_18"
    lun "a-alright..."
    $ ccg_folder = "luna_kiss"
    $ ccg1 = "2"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    her "{size=-5}good girl{/size}"
    call ctc
    ">As hermione whispers to Luna, you feel her pussy squeeze around your cock."
    show screen blkfade
    with d3
    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_18"
    $ ccg2 = "herm_18"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    g9 "*Mmmm* yes!"
    g9 "Do that again [hermione_name]!"
    $ ccg2 = "herm_22"
    her "Do what?"
    g9 "call her a good girl!"
    $ ccg1 = "luna_16"
    lun "{heart}{heart}{heart}"
    g9 "Ugh... by the gods! Her cunt goes wild every time!"
    $ ccg1 = "luna_30"
    lun "d-don't... {heart}ah...{heart}"
    $ ccg2 = "herm_17"
    her "*Ohhh*..."
    $ ccg2 = "herm_19"
    her "Someone's got a nasty little fetish don't they?"
    $ ccg1 = "luna_24"
    lun "No... it's not like that!"
    $ ccg1 = "luna_22"
    lun "It's just... *mmmm*...{heart}{heart}"
    lun "That's what... ah...{heart}"
    $ ccg1 = "luna_21"
    lun "That's what {heart}daddy{heart} used to call me..."
    $ ccg2 = "herm_18"
    her "And hearing us call you a {b}good girl...{/b}"
    $ ccg1 = "luna_16"
    lun "*mmmmm*{heart}{heart}"
    g9 "Fuck yes..."
    $ ccg2 = "herm_17"
    her "Makes your pussy feel good?"
    $ ccg1 = "luna_20"
    lun "Y-y-yes...{heart}"
    $ ccg1 = "luna_24"
    lun "Is that wrong?"
    $ ccg2 = "herm_23"
    her "no!"
    $ ccg2 = "herm_24"
    her "It's perfectly natural for you to get turned on by us calling you a good girl--"
    $ ccg1 = "luna_17"
    lun "a{heart}a{heart}*ahhhhh*{heart}"
    $ ccg2 = "herm_25"
    her "just like your {b}daddy{/b} used to..."
    $ ccg1 = "luna_31"
    lun "{size=+10}!!!{/size}"
    $ ccg1 = "luna_32"
    lun "*mmmm* I think I'm getting close Hermione!"
    g9 "*argh*!!! Me too!"

    menu:
        "-Cum inside-":
            g9 "GET READY SLUTS!"
            $ ccg1 = "luna_33"
            lun "W-w-what?"
            $ ccg2 = "herm_26"
            her "Aren't you going to pull out [genie_name]?"
            g9 "HERE IT COMES!!!"
            $ ccg2 = "herm_27"
            her "I guess not then..."
            $ ccg1 = "luna_34"
            lun "You don't mean..."
            g9 "ARGH!!!"
            ">Your cock explodes inside Luna, unleashing a deluge of your thick seed into her tight little pussy."
            g9 "BY THE NINE DIVINES!"
            $ ccg1 = "luna_35"
            lun "it's {heart} I can't {heart} what {heart}*ahhhhhhhhh*{heart}{heart}{heart}"
            $ ccg1 = "luna_36"
            lun "..."
            $ ccg2 = "herm_25"
            her "*Mmmm*, just enjoy it Luna..."
            $ ccg2 = "herm_24"
            her "Be a {b}good girl{/b} for daddy and just let him pump you full of cum..."
            $ ccg1 = "luna_37"
            lun "{heart}ah{heart}"
            $ ccg2 = "herm_26"
            her "*mmmm*"
            her "{b}good{/b}"
            $ ccg1 = "luna_36"
            lun "*mmm*{heart}{heart}"
            $ ccg2 = "herm_25"
            her "{b}girl{/b}"
            $ ccg1 = "luna_38"
            lun "ah...{heart}{heart}{heart}{heart}"
            call ctc
            show screen blkfade
            with d3
            ">It all proves too much for Luna, who passes out on your desk, cum still seeping out of her well used pussy."

        "-Cum all over her-":
            g9 "GET READY SLUTS!"
            $ ccg1 = "luna_33"
            lun "W-w-what?"
            g9 "HERE IT COMES!!!"
            $ ccg2 = "herm_24"
            her "*mmm*... do it [genie_name]!"
            $ ccg1 = "luna_39"
            lun "ah-ah-ah..."
            g9 "ARGH!!!"
            ">You pull your cock out at the last second, jerking it furiously as you shoot rope after rope of thick cum."
            g9 "BY THE NINE DIVINES!"
            $ ccg1 = "luna_40"
            lun "it's {heart} I can't {heart} what {heart}*ahhhhhhhhh*{heart}{heart}{heart}"
            $ ccg1 = "luna_41"
            lun "..."
            $ ccg2 = "herm_25"
            her "*Mmmm*, just enjoy it Luna..."
            $ ccg2 = "herm_24"
            her "Be a {b}good girl{/b} for daddy and just let him coat you with his nasty cum..."
            $ ccg1 = "luna_42"
            lun "ah {heart} don't {heart} call {heart} it {heart} nasty... {heart}{heart}{heart}"
            $ ccg2 = "herm_26"
            her "*mmmm*"
            her "{b}good{/b}"
            $ ccg1 = "luna_43"
            lun "*mmm*{heart}{heart}"
            $ ccg2 = "herm_25"
            her "{b}girl{/b}"
            $ ccg1 = "luna_44"
            lun "*ah*...{heart}{heart}{heart}{heart}"
            call ctc
            show screen blkfade
            with d3
            ">It all proves too much for Luna, who passes out on your desk, coated in a thick layer of your cum."

    $ luna_wear_top = False
    $ luna_wear_bottom = False
    $ luna_wear_bra = False
    $ luna_wear_panties = False
    call update_lun_uniform

    call gen_chibi("sit_behind_desk")
    call lun_chibi("lie","on_desk","on_desk")
    call her_chibi("stand","desk","base")
    hide screen ccg
    hide screen blkfade
    with d3

    call her_main("I think you broke her...", "grin", "wink", "base", "mid")
    m "She's fine..."
    m "If I remember correctly, you had a similar response to your first time as well..."
    call her_main("[genie_name]!", "shock", "happy", "base", "mid_soft")
    m "Anyway, are you able to take her back to her room?"
    call her_main("I'm not allowed in the Ravenclaw common room...", "base", "narrow", "base", "R_soft")
    call her_main("So I guess I'll just have to take her back to my room...", "grin", "narrow", "base", "down")
    m "I'm sure that's the only reason why..."
    call her_main("I don't have any idea what you're talking about sir...", "base", "narrow", "base", "R_soft")

    $ luna_wear_top = True
    $ luna_wear_bottom = True
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    call update_lun_uniform

    ">With a flick of Hermione's wand, Luna's clothes slither back onto her naked form."
    call her_main("Wingardium Leviosaaaaa!", "open", "happyCl", "base", "mid")

    call lun_chibi("lie","on_desk",320)
    with d3

    ">Luna's body lifts gently into the air, as if she was the star of a magic show."

    call her_main("I better be off, [genie_name], it's getting a little late.","grin","happy",xpos="base",ypos="base")

    m "Goodnight, [hermione_name]."
    call her_main("Goodnight {size=-5}daddy{/size}...", "grin", "slit", "low", "stare")
    hide screen hermione_main
    with d3

    call her_chibi("stand","desk","base",flip=True)
    call her_walk("door")
    call her_chibi(flip=False)

    call lun_walk("door") # Actually floats
    call lun_chibi("leave")
    call her_walk(action="leave")

    $ hermione_busy = True
    $ luna_busy = True

    jump main_room
