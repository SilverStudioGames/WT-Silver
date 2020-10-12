

### Susan Imperio Events ###

label ag_se_imperio_sb: # Move label
    $ astoria_chibi.zorder = 4 # In front of Susan.
    $ ag_se_imperio_sb.start()

    label end_ag_se_imperio_sb:

    # Reset
    $ astoria_chibi.zorder = 3 # Default

    $ astoria_busy = True
    $ susan_busy = True

    jump main_room



label ag_se_imperio_sb_E1:
    call play_music("stop")
    call hide_characters
    call ast_chibi("stand","mid","base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base")
    pause.2

    call sus_main("Hello, [sus_genie_name]. You wanted to see me?.","open","base","worried","mid", xpos="right", ypos="base")

    call play_music("astoria")
    call ast_main("Hey [ast_susan_name]!","grin","narrow","base","L", xpos="base", ypos="base")
    call sus_main("Astoria? What are you doing here?","open","base","worried","R")
    call ast_main("Oh, don't mind me...","base","base","base","R")

    call ast_chibi("wand",530,"base")
    call ast_main("I'm only here to put a curse on you.","grin","narrow","angry","mid")
    call sus_main("P-Put a curse on me?!!","open","wide","worried","wide")

    call ast_chibi("wand_casting",530,"base")
    call sus_main("No! Professor, do someth--","scream","wide","worried","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch)

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("W-what are you--","open","wide","worried","wide")
    call nar(">Susan's eyes flicker and a blank expression spreads across her face.")
    call sus_main("-doing...","upset","base","base","up")
    call sus_main("...","upset","narrow","base","up")

    call ast_chibi("wand",530,"base")
    call ast_main("OK, so what should we do now?","grin","base","angry","mid",xpos="close",ypos="base")
    call ast_main("We could do whatever we want [ast_genie_name]!","open","base","base","R")
    m "How about we have her take her clothes off?"
    call ast_main("All of them?!","clench","base","worried","mid")
    m "What? Didn't that work last time?"
    g9 "Maybe she secretly wants to be a exhibitionist!"
    call ast_main("I only made her take her top off.","open","base","base","mid")
    g9 "Then there you go!"
    call ast_main("OK...","smile","base","base","L")
    call ast_main("Susan, are you listening?","open","closed","base","mid")
    call sus_main("Yes...","upset","narrow","worried","up")
    call ast_main("Good, I want you to pay attention.","open","base","base","L")
    call sus_main("...","base","narrow","base","up")
    call ast_main("And...","base","narrow","base","R")
    call ast_main("Wait a second... [ast_genie_name], what's the point if it's just you and I who see it?","annoyed","base","base","mid")
    g9 "It's the perfect place to start."
    m "Now tell her to lift up her top..."
    call ast_main("Very well, [ast_genie_name]...","clench","base","base","L")
    call ast_main("Susan, I want you to show us your...{w} your...{w} Show us your boobs!","clench","base","base","L")
    call sus_main("...","base","narrow","base","mid")

    call play_sound("gulp")
    call sus_main("*gulp*","upset","closed","worried","down")

    call play_sound("gulp")
    g4 "*Gulp!*"

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    pause.5

    m "Oh no, Miss Bones!"
    g9 "What are you doing?!"
    hide screen bld1
    with d3
    pause.8

    call gen_chibi("jerk_off_behind_desk")
    pause.5

    call ast_main("...","annoyed","narrow","base","mid")
    call sus_main("I-I-I'm sorry, Professor Dumbledore, I don't know what's come over me...","open","narrow","worried","down")
    call sus_main("I'm Sorry you have to see this...","upset","closed","base","mid")
    call ast_main("See what Suzy?","grin","narrow","angry","mid")
    call sus_main("My gross boobs...","open","closed","worried","mid")
    call ast_main("(I knew they were gross!)","grin","base","angry","L")
    call sus_main("Please Sir--","open","narrow","worried","mid")
    call sus_main("Don't think less of me...","upset","closed","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "{size=+10}Nice!{/size}"
    call ast_main("Sir!","scream","closed","angry","mid")
    m "What? You can't blame me for this!"
    call ast_main("I thought we we're doing this so I could cast the spell more successfully","clench","narrow","angry","mid")
    call ast_main("(Please stop...)","annoyed","narrow","angry","R",cheeks="blush")
    m "Don't you think her breasts are pretty?"
    call ast_main("{b}No!{/b} they're huge and soft and squishy and, and, and... gross!","clench","closed","angry","mid")
    g9 "You're right about them looking huge and soft..."
    call ast_main("Sir!","clench","narrow","angry","mid")
    call sus_main("Did I do something wrong?","upset","narrow","worried","R")
    call ast_main("Oh shut up, [ast_susan_name]!","scream","base","angry","L")
    call sus_main("[ast_susan_name]!? W-why are you always being so mean to me?","open","wide","worried","wide")
    call ast_main("Pfft... you know...","annoyed","narrow","angry","R")
    call sus_main("A-{w=0.3}Are you just going to let her say that, s-sir?","scream","base","angry","mid")
    g4 "What's that?"
    m "I was a little...{w=0.4} *ugh*... distracted..."

    call nar(">You keep stroking your rock-hard cock whilst marvelling at Susan's heaving chest.")
    g4 "(So big, soft and squishy...)"
    call sus_main("Sir, what are you?--","upset","base","worried","down")
    call ast_main("Alright, I think you're enjoying this a little too much!","clench","base","angry","mid")
    m "Just give me a minute..."
    pause.2

    call play_music("stop")
    call hide_characters
    call ast_chibi("reset",530,"base")
    hide screen bld1
    with fade
    pause.8

    call ast_main("","annoyed","base","angry","R")
    call sus_main("W-w-what...","open","base","base","up")

    call nar(">Susan's eyes flicker once more as the blank expression spreads across her face.")

    call gen_chibi("sit_behind_desk")
    with d3
    pause.1

    call play_music("astoria")
    g4 "(Damn it! Why did she do that?)"
    call sus_main("...","upset","base","worried","down")
    call ast_main("Put your clothes on, Suzy.","smile","base","base","mid")
    call sus_main("...","upset","narrow","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("","upset","narrow","worried","mid")
    pause.5
    call nar(">Susan begins dressing herself in silence...")

    hide screen susan_main
    $ susan_wear_top = True
    call update_sus_uniform
    call sus_main("","upset","narrow","base","mid")
    pause.5
    call nar(">Her eyes unfocused, staring blankly into space.")

    m "Aww... why would you do that?"
    call ast_main("You were getting too excited, old man.","clench","base","angry","mid")
    m "So what?"
    call ast_main("How am I going to get any better if you keep distracting me!","annoyed","narrow","angry","R")
    m "Couldn't you at least make her dance or something..."
    call ast_main("We could do that...","annoyed","base","base","L")
    m "Then why don't we?"
    call ast_main("Because it's boring!","annoyed","narrow","base","ahegao")
    call ast_main("I want to do something fun!","open","closed","base","mid")
    m "Ugh... fine..."
    call ast_main("But not today...","annoyed","base","base","mid")
    call ast_main("I should put Bessy here back in her barn before people start to notice.","grin","base","angry","L")
    call sus_main("(*Hmm*...)","upset","wide","worried","wide")
    m "Alright..."
    call ast_main("Just call me for the next practice session!","smile","narrow","base","mid")
    m "Will do."
    m "Oh, please take Susan to professor Tonks' to be obliterated..."
    call ast_main("Obliviated?","base","base","worried","mid")
    m "Yeah, that!"
    call ast_main("Can't you do it?","annoyed","base","base","mid")
    m "My wand casting hand is a bit tired for some reason..."
    call ast_main("Fine...","annoyed","base","worried","R")
    if daytime:
        call ast_main("Have a nice day, Sir!","grin","closed","base","mid")
        m "You too..."
    else:
        call ast_main("Night then, Sir!","grin","closed","base","mid")
        m "Good night..."

    call ast_walk("door","base")
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    call ast_main("Come on Suzy, time to give professor Tonks a visit.","open","base","base","mid", ypos="head")
    call sus_main("...","upset","narrow","worried","down", ypos="head")

    call sus_walk(action="leave")

    call ast_main("(This is so much fun!)","grin","closed","base","mid")

    call play_sound("door")
    call hide_characters
    call ast_chibi("hide")
    hide screen bld1
    with d3
    pause.5

    call bld
    m "(Maybe leaving Tonks out of this was a bad idea...{w} Nah... {w=0.3} She's had her fun...)"

    # Increase affection once (this is the first event)
    if ag_se_imperio_sb.counter == 1:
        $ ast_whoring += 1

    jump end_ag_se_imperio_sb


label ag_se_imperio_sb_E2:
    call ast_main("Let's try something else this time!","grin","narrow","base","mid", xpos="close", ypos="base", trans=fade)
    g9 "Of course!"
    call ast_main("Great, I can't wait to see the look on Susan's dumb face...","grin","closed","base","mid")
    m "Let me just bring her up here."

    call play_music("stop")
    m "..."
    call ast_main("...","annoyed","base","base","R")

    call hide_characters
    call ast_chibi("stand",530,"base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base")
    pause.2


    call sus_main("You wanted to see me, [sus_genie_name]?","open","base","worried","mid", xpos="right", ypos="base")
    call sus_main("Astoria? Why are you here?","open","base","worried","R")

    call play_music("astoria")
    call ast_main("Oh... no reason...","annoyed","base","base","down", xpos="base", ypos="base")
    call sus_main("Is there something wrong, Professor?","upset","base","worried","mid")
    m "As a matter of fact there is..."
    call sus_main("R-really? Is this about me returning my books to the library a day late?","open","wide","base","wide")
    call sus_main("I swear it won't happen again!","open","closed","worried","mid")
    m "What? No, I'm afraid there's an issue with your uniform..."
    call sus_main("Oh... Is it because I'm not wearing the school robe?","open","base","worried","down")
    call sus_main("I can wear it from now on if you like!","upset","base","base","mid")
    m "Actually, Wearing too many clothes is the problem."
    call sus_main("W-w-what???","scream","wide","base","wide")
    call sus_main("You can't be serious sir!","open","wide","base","mid")
    m "I am, Ms Bones..."
    g9 "Hiding away those glorious milk duds of yours is a serious offence!"
    call sus_main("","open","wide","base","wide")
    call ast_main("(*Pffft*, gloriously gross)","annoyed","base","angry","R")
    call sus_main("P-professor Dumbledore! Why would you want me to do s-something like that!","scream","base","angry","mid", trans=hpunch) #Perhaps she should be a bit intrigued =Blush

    call ast_chibi("wand",530,"base")
    call sus_main("I think I better go...","upset","closed","worried","mid")
    call ast_chibi("wand_casting",530,"base")
    call ast_main("","grin","base","angry","L")
    pause.5

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("...","upset","narrow","base","mid", xpos="right", ypos="base")
    call ast_main("*ha-ha-ha-ha!*","grin","closed","base","mid", xpos="base", ypos="base")
    call ast_main("Her face was priceless when you said milk duds...","grin","base","base","L")
    m "You liked that?"
    call ast_main("Of course! Anything to bring Bessy here down a peg.","smile","base","base","L")

    call ast_chibi("wand",530,"base")
    call ast_main("So what should we make her do today, [ast_genie_name]?","smile","base","base","mid")
    m "Something fun, perhaps?"
    call ast_main("*Hmm*...","annoyed","narrow","base","R")
    m "Maybe something a little more... adventurous?"
    call ast_main("You mean like making her show you her milk duds?","upset","narrow","base","mid")
    m "Well if you insist..."
    call ast_main("*ugh*... you're such a filthy pervert!","clench","narrow","angry","mid")
    m "We can do something else if you--"
    call ast_main("I didn't say no...","upset","closed","base","mid")
    m "Oh... well how about you make it so--"
    call ast_main("I get to choose, [ast_genie_name]!","scream","closed","angry","mid")
    m "What? Why?"
    call ast_main("Because it's my spell and my wand!","open","narrow","angry","mid")
    call ast_main("Not to mention you'd probably do something over the top and gross...","open","narrow","angry","R")
    m "Probably..."
    m "So what's your plan?"
    call ast_main("Just wait and see old man!","clench","narrow","angry","mid")
    call ast_main("Susan, can you hear me?","open","closed","base","L")
    call sus_main("Yes...","upset","narrow","base","up")
    call ast_main("You now have an uncontrollable urge to take your top off, OK?","open","closed","base","mid")
    call sus_main("Okay...","upset","narrow","worried","mid")
    call ast_main("Awesome! Now act like you normally would, [ast_susan_name]!","grin","base","angry","L")
    call sus_main("...","upset","narrow","base","up")

    hide screen blktone
    call nar(">The blank expression slowly fades from Susan's eyes...")
    call sus_main("ugh...","upset","narrow","base","up")
    call sus_main("What happened?","open","narrow","worried","mid")
    call ast_main("Nothing Suzy, Dumbledore was just explaining how your uniform wasn't up to scratch.","grin","base","base","mid")
    call sus_main("My uniform... You're right... Too many clothes...","open","narrow","worried","down")
    call sus_main("I need to take off my top...","open","base","worried","down")
    call ast_main("*Mhmm*, that's right, Suzy... Why don't you show the old man here your gross boobs... Don't you think he's old?","grin","base","angry","mid")
    call sus_main("I... I suppose...","upset","narrow","worried","L")
    call ast_main("That's right... Only a nasty slut would show her boobs to such a wrinkly old man...","grin","narrow","angry","L")
    m "Hey!"
    call ast_main("Quiet sir... don't ruin my fun!","clench","narrow","angry","mid")
    m "Fine..."
    call sus_main("I-I'm not a slut...","upset","narrow","worried","down")
    call ast_main("Well I'm sure you'll be able to keep your top on then, [ast_susan_name].","open","closed","base","mid")
    call sus_main("I... There's something wrong sir!","open","base","worried","mid")
    call sus_main("I can't help it...","upset","narrow","worried","down")
    call ast_main("","grin","base","angry","L")
    pause.2

    hide screen susan_main
    $ susan_wear_top = False
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "Nice!"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerk_off_behind_desk")
    pause.8

    call ast_main("[ast_genie_name]! Are you touching yourself?","scream","base","base","mid")
    m "Ugh... can you blame me?..."
    g4 "It's not every day you get to see a rack like this..."
    call ast_main("Well stop it! It's gross!","clench","narrow","angry","mid")
    m "Alri--"
    call sus_main("Please sir... it's too much!","open","closed","base","mid")
    call sus_main("It's bad enough that I can't help showing you my breasts...","open","closed","worried","mid")
    call ast_main("Wait...","smile","base","base","mid")
    call ast_main("Keep going, sir!","clench","narrow","angry","mid")
    m "What?"
    call sus_main("What?","scream","wide","base","mid")
    call ast_main("Well if Bessy here hates it... Then I love it!","clench","narrow","angry","L")
    call ast_main("Besides, it's not like I can see anything under the desk.","open","closed","base","mid")
    call sus_main("(...)","upset","closed","worried","mid")
    m "So you're OK with this?"
    call ast_main("*Mhmm*... just don't expect me to touch it old man!","upset","narrow","angry","mid")
    call sus_main("W-why is this happening!","open","closed","base","mid")
    call ast_main("No one asked you, slut!","clench","narrow","angry","L")
    call sus_main("I am not a slut!","scream","closed","angry","mid")
    call sus_main("", "upset")
    call ast_main("Ha! You're standing here, letting old man dumbledore ogle your fat tits while he jerks his wrinkly old cock!","open","closed","base","mid")
    call ast_main("If that's not a slut then I don't know what is!","clench","narrow","angry","L")
    m "(There's no way Tonks would allow this, perhaps this was a good idea after all...)"
    call sus_main("I-- don't know why I'm doing this...","upset","narrow","worried","mid")
    call sus_main("You probably cursed me!","open","suspicious","angry","mid")
    call ast_main("Duh!","grin","narrow","angry","L")
    call sus_main("Well stop it!","open","base","angry","R")
    call ast_main("*Nuh-uh*!","open","closed","base","mid")
    call sus_main("Please Astoria...","upset","narrow","worried","down")

    call nar(">You start to zone out as the two girls argue, focusing on Susan's heaving bosom.")
    g4 "Ugh yeah... that's it..."
    call ast_main("You can leave once Dumbledore here's done.","open","closed","base","mid")
    call sus_main("What? you mean I have to wait until he...","open","base","worried","mid")
    call sus_main("This is unbelievable!","scream","base","angry","mid")
    call sus_main("I'm going to report both of you to the ministry of magic!","open","closed","angry","mid")
    call sus_main("My aunt is the head of the department of magical law enforcement you know!","open","base","angry","mid")
    call ast_main("yeah... I've met your creepy old aunt.","annoyed","narrow","base","R")
    call sus_main("What? Did you curse her too, you evil little witch?","open","wide","base","R")
    call ast_main("I wish...","annoyed","narrow","base","R")
    call sus_main("Well she's going to lock both of you away in Azkaban!","open","closed","angry","mid")
    call sus_main("You'll never see me or anyone else again...","scream","closed","angry","mid")
    call ast_main("Yeah, sure!","grin","base","angry","L")
    call sus_main("Ugh! You're both sick!","open","narrow","angry","mid")
    g4 "*Mmmm*, keep shaking those tits of yours..."
    g4 "I'm almost there {b}slut!{/b}"
    call sus_main("I am not a {size=+10}slut!{/size}","scream","closed","angry","mid",trans=vpunch)
    call nar(">As Susan yells at the top of her voice, the effort causes her gigantic tits to rise and slap back together.")
    call sus_main("","open")

    g4 "{size=+10}HERE IT COMES!{/size}"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("cum_behind_desk")
    call cum_block
    g4 "{size=+10}AHHH... YESS!!!!{/size}"
    call ast_main("Woah... I didn't think you'd have that much in you, sir...","clench","base","base","mid")

    call sus_main("{size=+10}*Hmph*! I hope you Enjoy Azkaban, perverts!{/size}","scream","narrow","angry","down")
    call sus_main("","upset")

    call ast_main("","annoyed","narrow","base","R")
    call gen_chibi("cum_behind_desk_done")
    pause.5

    call nar(">As you shoot your massive load Susan's leg twitches slightly...")

    call ast_main("Let's delve deeper shall we...","grin","narrow","angry","L")
    m "W-what?"
    call ast_main("Suzy, can you hear me?","open","base","base","L")
    call sus_main("Yes...", "open")
    call sus_main("", "upset")
    call ast_main("She's just so easy to put under the spell...","base","narrow","worried")
    call ast_main("Nothing like Tonks, there's something wrong here...",eyes="base",pupils="R")
    m "W-what do you mean?"
    call ast_main("Quiet!","clench","base","base","mid")
    g4 "..."
    call ast_main("Suzy, I want you to speak the truth and nothing but the truth, okay?","open","base","base","L")
    call sus_main("Okay...","open")
    call sus_main("", "upset")
    m "What are you--"
    call ast_main("...","upset","base","base","mid") # Stares at you
    g4 "..."
    call ast_main("Suzy, do you like baring your chest to the headmaster?","open","base","base","L")
    call ast_main("Are you just another one of those closeted sluts?","clench","narrow")
    m "(Oh shit...)"
    call sus_main("I... I...","open","base","worried")
    call ast_main("Tell me!","scream")
    call ast_main("","clench")
    call sus_main("I...{w=0.8} I do!","open","closed")
    call ast_main("I knew it!","scream","narrow","angry") # Angry
    call sus_main("","upset","narrow")
    call ast_main("Where's the fun if she's enjoying it!","clench",pupils="mid")
    m "*Errr-*"
    call ast_main("I want to humiliate this cow, but she's just another slut!","scream")
    m "A closeted slut..."
    call ast_main("Excuse me?",mouth="open",eyebrows="worried")
    call ast_main("",mouth="upset")
    m "Miss Greengrass... is there any other Hufflepuff students you know of selling favours?"
    call ast_main("Why would I know or care what Hufflepuffs are doing?",mouth="clench")
    m "Just because she enjoys it doesn't mean it's not humiliating for her..."
    m "What would the other Hufflepuffs think of her if she knew what you have her do?"
    call sus_main("...", "upset","narrow","base","down")
    call ast_main("What do you mean?","upset","base","base")
    m "Ask her the right questions..."
    call ast_main("...",eyes="closed")
    call ast_main("Suzy!","open","narrow","base","L")
    call ast_main("","base")
    call sus_main("...",pupils="mid")
    call ast_main("Are you ashamed of what you've done?","open","base")
    call ast_main("","base")
    call sus_main("Yes...","open","base")
    call sus_main("!!!","grin","eager",pupils="L") # Smiles
    call ast_main("Would your house think less of you if they knew what you're doing here?","grin")
    call sus_main("Yes...",pupils="R")
    m "Well, there you go!"
    call ast_main("*ha-ha-ha!*","smile")
    m "(Nailed it...)"
    m "So, are we continuing with the training?"
    call ast_main("Of course we are! I want to be able to put every student at the school under my spell!",eyebrows="angry",pupils="mid")
    call ast_main("",eyes="closed")
    g4 "..."
    m "Then wouldn't the reason for Susan's shame go away as well?"
    call ast_main("And they will all be under my comm--","scream","closed")
    call ast_main("Oh yeah, that's true...","open","base","base","mid")
    call ast_main("...","annoyed")

    call ast_main("Suzy, put your clothes back on.","grin","base","base","L")

    call sus_main("","base","narrow","base","mid")
    pause.5
    call nar(">Susan begins dressing herself in silence...")

    hide screen susan_main
    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("","base","narrow","base","mid")
    pause.5

    call play_music("stop")
    call hide_characters
    call ast_chibi("reset",530,"base")
    call ast_walk("door","base")
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    call play_music("astoria")
    call ast_main("Come on Suzy, time to give professor Tonks another visit","open","base","base","L", ypos="head")
    call sus_main("...","upset", ypos="head")

    call sus_walk(action="leave")

    if daytime:
        call ast_main("See you, [ast_genie_name]!","grin","closed","base","mid")
        m "..."
    else:
        call ast_main("Good night then, Sir!","grin","closed","base","mid")
        m "Good night."

    call play_sound("door")
    call hide_characters
    call ast_chibi("hide")
    hide screen bld1
    with d3
    pause.5

    # Increase affection once (this is the second event)
    if ag_se_imperio_sb.counter == 2:
        $ ast_whoring += 1

    jump end_ag_se_imperio_sb


label ag_se_imperio_sb_E3:
    call ast_main("","smile","base","base","mid",xpos="close",ypos="base",trans=fade)
    m "Ready for another go with the curse?"
    call ast_main("You bet [ast_genie_name]! I can't wait to see the look on Suzy's stupid face this time!","grin","narrow","angry","down")
    m "Shall I bring her up here?"
    call ast_main("Do you even need to ask?","smile","narrow","base","mid")
    m "I suppose not..."

    call play_music("stop")
    call hide_characters
    call ast_chibi("stand",530,"base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base")
    pause.2

    call sus_main("You wanted to see me sir?","open","base","worried","mid", xpos="right", ypos="base")
    call sus_main("Astoria?...","upset","base","worried","R")
    call sus_main("What are you doing here?","upset","narrow","worried","R")

    call play_music("astoria")
    call ast_chibi("wand",530,"base")
    call ast_main("Yeah yeah, whatever...","open","base","base","R", xpos="base", ypos="base")

    call ast_chibi("wand_casting",530,"base")
    call sus_main("Well I'm not sure why I was brought here...","open","base","worried","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans=hpunch)

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("Wait, what--","open","wide","base","wide")
    m "Couldn't even wait this time?"
    call ast_main("Quiet old man.","open","narrow","angry","mid")
    call ast_chibi("wand",530,"base")
    call ast_main("Susan, I want you to keep listening to my commands and act normally as you take your top off!","smile","narrow","angry","L")
    g4 "!!!"

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","base","worried","mid")
    pause.5

    call nar(">As Susan begins to talk her arms seem to have a mind of their own, quietly removing her top as she speaks.")
    call sus_main("Was this about the l-library books that I returned a day late s-sir?","open","narrow","worried","down")
    call sus_main("I promise it won't happen again...","upset","closed","worried","mid")
    g9 "Don't you worry about the books, Ms Bones!"
    call sus_main("T-Then what is it?","base","narrow","base","mid")
    call ast_main("Just get those milk bags out!","clench","narrow","angry","L")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","base","base","base","mid")
    pause.5

    g4 "(!!!)"
    call ast_main("Maybe it's because of you showing off your gross boobs?","annoyed","base","base","R")
    call sus_main("Astoria! H-how can you say something so rude! I'd never...","open","closed","angry","mid")
    call sus_main("","upset","wide","worried","down",trans=hpunch)
    pause.8
    call nar(">Susan's eyes drift down to her exposed chest.")
    call sus_main("WHAT?!?!?","scream","wide","worried","down")
    call sus_main("I'm so sorry, professor Dumbledore!","upset","closed","worried","mid")
    call sus_main("I don't know what's come over me!","open","closed","base","mid")
    call ast_main("Maybe it's just because you're a nasty slut!","annoyed","base","base","L")
    call sus_main("I am not a {size=+10}slut{/size}, Astoria!","scream","closed","angry","mid")
    call ast_main("*Pfft*... we both know that's not true... We both know you love showing your headmaster those oversized bean bags of yours...","annoyed","base","base","R")
    call sus_main("I-- don't know why this is happening...","open","wide","worried","wide")
    call sus_main("You must have cursed me!","scream","narrow","angry","R")
    call ast_main("Bingo!","grin","base","angry","L")
    call sus_main("Professor! You h-have to stop her!","scream","wide","base","mid")
    hide screen astoria_main
    with d3
    m "Ugh... I'm afraid not Susan..."
    call ast_main("","grin","narrow","angry","L",xpos="base",ypos="base")
    call sus_main("WHAT?!","scream","wide","base","wide")
    call sus_main("W-w-w-well my aunt will just send you--","upset","narrow","angry","mid")

    call nar(">Astoria strengthens her grip on her wand, increasing the effect the spell has on Susan.")

    call sus_main("to... Azkaban...","open","narrow","base","up")
    call sus_main("...","upset","narrow","base","mid")
    call ast_main("Alright... that'll shut her up...{w} what should we make her do this time, [ast_genie_name]?","grin","base","base","mid",xpos="close",ypos="base")
    m "*Hmm*... Are you actually going to let me choose this time or are you just asking to be annoying?"
    call ast_main("Hey! I am not annoying!","scream","closed","angry","mid",trans=hpunch)
    m "Well are you going to let me pick then?"
    call ast_main("Fine... Just nothing too disgusting!","clench","narrow","base","mid")
    call ast_main("Or boring... that'd be even worse!","upset","narrow","angry","mid")

    m "Alright well, first things first..." #I'll add a menu here with more options once art assets are drawn for them

    hide screen blktone
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerk_off_behind_desk")
    pause.8

    show screen bld1
    call nar(">Your hands sneak under your desk and around your engorged cock.")
    g9 "That's better..."
    call ast_main("(...)","annoyed","narrow","angry","R")
    m "What?"
    call ast_main("I told you not to be boring! We already did this last time!","open","closed","base","mid")
    g9 "If this is too boring, why don't you get her to suck me off?"
    call ast_main("Sir! I said it shouldn't be something disgusting...","clench","base","base","mid")
    call ast_main("I don't wanna have to see your nasty old cock!","clench","narrow","angry","R")
    m "Ugh... Fine... What do you want to do then?"
    call ast_main("Well seeing as how you asked...","open","closed","base","mid")
    call ast_main("Suzy, are you listening?","open","narrow","base","L")

    show screen blktone
    call sus_main("yes...","upset","narrow","base","up")
    call ast_main("I want you to crawl under the headmaster's desk.","grin","base","base","L")
    m "I thought you didn't want her to suck me off?"
    call ast_main("Shut it, and stop being so disgusting!","scream","closed","angry","mid")
    call sus_main("...","upset","narrow","base","up")
    call ast_main("Now go, [ast_susan_name]!","grin","narrow","angry","mid")

    call hide_characters
    call sus_chibi("hide")
    hide screen blktone
    call blkfade

    call nar(">Susan slowly starts walking around your desk before obediently crawling under.")
    pause.5
    hide screen blkfade
    call ast_main("","smile","base","base","down",xpos="mid",ypos="base",trans=fade)
    hide screen bld1
    call ctc

    show screen blktone
    call ast_main("And you're not allowed to come out until I say so.","open","closed","base","mid")
    sus "yes..."
    call ast_main("And if you actually are just a slut then let that slut out! Show us you really love it!","clench","narrow","base","down")
    sus "... Love it?"
    sus "I love it..."
    call ast_main("Good!","clench","base","angry","L")
    m "Isn't that a little much?"
    call ast_main("*Pfft*! That's rich coming from you sir!","annoyed","narrow","base","mid")
    call ast_main("If it was up to me she'd be clucking like a chicken right now!","annoyed","narrow","angry","R")
    call ast_main("Not doing nasties with her mouth!","clench","narrow","base","down")
    m "Fair enough..."
    call ast_main("But you've helped me so take this as a reward...","annoyed","narrow","base","mid")
    call ast_main("Now, make sure to give Susan a reward for being so obedient as well...","open","closed","angry","mid")
    m "You don't have to tell me twice!"
    call nar(">You renew your efforts, encouraged by the image of the well-endowed redhead hidden under your desk.")
    call ast_main("And Suzy...","open","narrow","base","down")
    sus "Yes..."
    call ast_main("Time for you to wake up...","grin","narrow","angry","down")
    sus "..."

    call play_music("susan")
    hide screen blktone
    hide screen bld1
    with d3
    pause.5
    show screen bld1
    with hpunch
    sus "W-w-what's happening?"
    call play_sound("kick")
    with vpunch
    pause.2
    sus "Ouch..."
    pause.5
    sus "Where am I?"
    call ast_main("Don't you remember crawling under your headmaster's desk, begging him to jerk his nasty old cock for you?","open","closed","base","mid")
    with hpunch
    sus "WHAT?"
    sus "I'd never do something like that!"
    call ast_main("Really? Because it sure looks like you did...","grin","base","base","R")
    sus "I--"
    sus "I don't know why..."
    call ast_main("If you don't like it down there, why don't you just hop out then?","annoyed","base","base","R")
    sus "I can't!"
    call ast_main("Really? why's that, Suzy?","grin","narrow","base","down")
    sus "I don't know... I just can't!"
    call ast_main("*Hmm*... it must be because you're such a nasty little slut then...","open","closed","base","mid")
    with hpunch
    sus "I-- I am not!"
    call ast_main("Are you sure?","grin","base","angry","down")
    sus "I... Y-yes..."
    call ast_main("because it sure doesn't look like that...","open","narrow","base","down")
    call ast_main("In fact, it looks like you're the nastiest little slut this school has ever seen!","grin","closed","base","mid")
    g4 "That's it, Astoria..."
    sus "Professor... {b}please...{/b}"
    call ast_main("Please what, Susan?","open","closed","base","mid")
    call ast_main("Please stop?","open","narrow","base","down")
    call ast_main("Or please coat me in cum?","clench","narrow","angry","down")
    with hpunch
    sus "ASTORIA!"
    call ast_main("Answer the question, Suzy...","open","base","base","mid")
    sus "..."
    sus "Please sir..."
    sus "{size=-3}Coat{/size} {size=-3}me{/size} {size=-3}in{/size} {size=-3}your{/size} {size=-3}cum...{/size}"
    call ast_main("I knew it!","scream","base","angry","L")
    call ast_main("You're a dirty little slut after all aren't you!","clench","narrow","angry","down")
    sus "I am not! I don't know why I'm down here!"
    call ast_main("Alright then... if you're such a good girl...","open","closed","base","mid")
    call ast_main("Why don't you tell me what it's like down there?","smile","narrow","base","down")
    sus "Down here?"
    sus "Under professor Dumbledore's desk?"
    call ast_main("*Mhmm*... I bet it's nasty down there...","clench","narrow","angry","down")
    call ast_main("It probably smells gross with all the yucky cum he shoots against that desk of his...","open","base","base","R")
    call ast_main("Not to mention his big, smelly old cock...","annoyed","narrow","base","ahegao")
    m "*Ahem*..."
    call ast_main("Quiet, sir!","clench","narrow","angry","mid")
    call ast_main("So go on, Suzy... tell me what it's like...","open","closed","base","mid")

    sus "It... It's--"
    call nar(">you hear Susan take a deep breath before she begins to speak.")
    sus "{size=+10}It's incredible!{/size}"
    call ast_main("","grin","narrow","angry","mid")
    sus "Everything about it is fantastic!"
    call ast_main("","smile","base","base","mid")
    sus "The cum stains on the back of the desk..."
    call ast_main("","clench","narrow","base","mid")
    sus "The thick smell of semen in the air..."
    call ast_main("","clench","narrow","base","R")
    sus "The way Dumbledore's stroking his {b}cock{/b}..."
    call ast_main("","smile","narrow","angry","R")
    sus "That cock... that's the best part..."
    sus "I just want to--"
    call ast_main("(*Eeeegh*...)","scream","closed","angry","mid",trans=hpunch)

    sus "..."
    call nar(">You hear Susan's words trail off into nothingness as she takes another breath...")
    sus "I wish I could live down here! Is that what you wanted to hear you evil witch?!"
    call ast_main("Almost...","grin","narrow","base","down")
    call ast_main("I want you to tell me the truth... say you're a slut...","grin","base","angry","mid")
    call ast_main("Then I'll let you go...","open","closed","base","mid")
    sus "Really?"
    sus "Alright..."
    sus "{size=-5}I'm a...{/size} {size=-3}slut...{/size}"
    call ast_main("*Hmm*... I'm not sure I heard anything. What about you, sir?","annoyed","base","base","R")
    m "Ah...{w=0.3} almost..."
    call ast_main("Go on Suzy... one more time...","smile","narrow","base","down")
    with hpunch
    sus "I'm a slut, OK!"
    g4 "Ah... YES..."
    sus "I'm a nasty slut who crawled under her headmaster's desk and--"

    g4 "HERE IT COMES SLUT!"
    hide screen bld1
    call gen_chibi("cum_behind_desk")
    call cum_block
    sus "No wait! Astoria, you said I could go--"
    call cum_block
    g4 "ARGHHHH!!!"
    call nar(">Susan's sudden yelps prove too much for you as your cock begins to fire off an immense load onto Susan's face...")
    g4 "HERE IT IS SLUT!!!"
    call cum_block
    sus "..."

    call ast_main("That's it, [ast_genie_name]! Make sure you get it all out...","grin","narrow","angry","mid")
    g4 "*Ahhh*... don't worry about that..."
    call nar(">You give your cock a few final pumps, working out the last of your load onto Susan's waiting face...")

    call gen_chibi("cum_behind_desk_done")
    pause.5
    g4 "There we go..."
    call ast_main("Nice work, [ast_genie_name]...","open","closed","base","mid")
    call ast_main("You can come out now, Suzy...","smile","narrow","base","down")
    sus "..."

    call play_music("stop")
    hide screen astoria_main
    call blkfade

    call nar(">Susan slowly crawls out from under your desk...")

    call sus_chibi("stand","desk","base")
    call ast_chibi("reset",530,"base")
    $ susan_face_covered = True
    hide screen blkfade
    call sus_main("","upset","narrow","worried","L",xpos="right",ypos="base",trans=fade)
    call ctc

    call play_music("astoria")
    call ast_main("Oh my god! He absolutely covered you!","scream","base","base","mid",xpos="base",ypos="base")
    call sus_main("...","upset","narrow","base","L")
    call ast_main("I didn't know you had it in you, sir!","clench","base","base","mid")
    call ast_main("Nice work!","annoyed","base","base","mid")
    m "Thanks..."
    call ast_main("And Suzy... that look suits you.","grin","narrow","angry","L")
    call sus_main("Are you done, Astoria?","open","narrow","base","L")
    call ast_main("Yes, you can get dressed.","smile","narrow","base","L")

    call nar(">Susan slowly wipes the cum from her face as she gets dressed.")

    hide screen susan_main
    $ susan_face_covered = False
    call sus_main("I hope you two are happy...","upset","narrow","base","down")

    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform

    if daytime:
        call ast_main("We're going to be late for classes, Suzy!","annoyed","narrow","base","R")
        call ast_main("Let's head to Tonks' study, shall we?...","smile","narrow","base","R")
        sus "..."
        m "See ya..."
        call ast_main("Until next time, [ast_genie_name]!","grin","closed","base","mid")
    else:
        call ast_main("It's getting a bit late Suzy, let's head to Tonks' study...","annoyed","narrow","base","R")
        sus "..."
        m "Ugh... *Uhm*... good night."
        call ast_main("Good night, [ast_genie_name]!","grin","closed","base","mid")

    call play_sound("door")
    call hide_characters
    call ast_chibi("leave")
    call sus_chibi("leave")
    hide screen bld1
    with d3
    pause.8

    call bld
    m "(That girl is even worse than me...)"

    $ susan_wardrobe_unlocked = True
    if ast_whoring < 24: # Save compatibility
        $ ast_whoring = 24

        $ TBA_message("This concludes all events for Susan and Astoria as of version %s." % title_version)
        $ TBA_message("Susan's wardrobe has been unlocked!")
        $ TBA_message("Astoria's affection stat has been maxed out.\nYou can now use all of her wardrobe options.")

    # Increase affection once (this is the third event)
    #if ag_se_imperio_sb.counter == 3:
    #    $ ast_whoring += 1

    jump end_ag_se_imperio_sb
