

#Spell Training.

label imperio_spell_1_training: #first level imperio spell

    #Spell Intro.
    if ast_spell_progress == 0:
        #talk about needing to practice the spell, what it does new and about sitting on lap
        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade")
        m "So I managed to get a book of brand new spells of an old friend of mine."
        m "Apparently he made them himself..."
        call ast_main("Really? So no one else knows them?","happy","base","base","mid")
        m "Not a soul."
        call ast_main("cool...","grin","happyCl","base","mid")
        call ast_main("So can I see it?","grin","angry","angry","mid")
        m "Sure, just come hop up on my lap and we can start reading it together."
        call ast_main("WHAT???","scream","wide","wide","wide")
        call ast_main("Why do I have to sit up on your lap?","open","angry","angry","mid")
        call ast_main("It was bad enough that you made me go hang out with that old hag...","disgust","angry","angry","R")
        call ast_main("Why can't I just use a chair?","disgust","angry","angry","mid")
        m "I only have one chair..."
        call ast_main("There is another chair right here! Dumby!!!","scream","wide","wide","mid")
        m "No that's..."
        m "My antique shelve..."
        g9 "Besides, it'll be fun!"
        call ast_main("Fun?","pout","angry","angry","mid")
        g9 "It'll be fun for me..."
        call ast_main("Ugh...","disgust","ahegao","ahegao","ahegao")
        call ast_main("At least tell me what the spell does and I'll decide...","open","closed","base","mid")
        m "OK, let me just open it up."
        call ctc

        call ast_main("","pout","narrow","narrow","mid")
        pause.5
        call nar(">You try to open the spell book only to find it doesn't budge.")
        m "(What gives?)"
        call ast_main("Come on, old man...","pout","narrow","narrow","L")
        m "I... can't open it..."
        call ast_main("What? You're not that weak are you, dumby?","tongue_silly","angry","angry","mid")
        m "I'm not a damn cripple!"
        call ast_main("Pffft, I think most cripples can open a book.","smile","base","base","mid")
        pause.8
        m "I think it's magically locked..."
        call ast_main("Really? It must be powerful then...","worried","wide","wide","wide")
        call ast_main("Does it say anything on the cover?","open","base","base","mid") #need soggy to draw the book here
        m "No..."
        call ast_main("And on the back?","pout","base","base","R")
        m "Noth- no wait, there's a poem."
        call ast_main("What does it say, dumby!","grin","angry","angry","mid")
        m "When venus and mars meet, all my knowledge shall be at your feet..."
        call ast_main("What does that mean?!","open","wide","wide","mid")

        label astoria_book_question:
            menu:
                "-We have to be touching to open it-":
                    pass
                "-We have to wait until venus and mars are aligned-":
                    call ast_main("But that could take forever!","open","ahegao","ahegao","ahegao")
                    call ast_main("It's gotta be something else dumby!","pout","angry","angry","mid")
                    jump astoria_book_question
                "-We've gotta get some ancient gods to hook up-":
                    call ast_main("Stop being such a dumby!","pout","narrow","narrow","R")
                    jump astoria_book_question

        call ast_main("Oh... is that why you wanted me to sit on your lap?","disgust","base","base","down")
        m "o-of course... why else would I ask?"
        call ast_main("hmpf...","pout","angry","angry","R")
        call ast_main("well alright... Just don't try anything funny!","open","closed","base","mid")

        hide screen astoria_main
        hide screen bld1
        call blkfade

        call nar(">Astoria hops up onto your lap.")

        #Set up CG scene here.
        $ ccg_folder = "astoria_sit"
        $ ccg("e6","b3","m1")

        pause.5
        hide screen blkfade
        with fade

        ast "I guess this isn't too bad..."
        $ ccg("e3","b0","m0")
        ast "Now let's start reading!"
        m "(Snape better not have booby trapped this...)"
        call nar(">You and astoria begin to turn the pages together, words begining to manifest on the pages.","start")
        call nar(">As astoria flicks through the pages you hear a slow sexual moan eminate from between the covers...","end")
        $ ccg("e1","b1","m1")
        ast "Did the book just moan?"
        m "I think so..."
        $ ccg("e3","b0","m0")
        ast "Cool! All the scary spell books in the forbidden section of the library do to that too!"
        $ ccg("e0","b1","m3")
        ast "Although they don't normally sound like this..."
        m "Let's just see what the first spell is shall we?"
        call nar(">Astoria slowly opens the book, turning it to the first spell she can find.")
        $ ccg("e0","b0","m3")
        ast "\"imperio of the heart\""
        $ ccg("e1","b3","m1")
        ast "Imperio?!?!"
        $ ccg("e6","b3","m1")
        ast "Everyone and their dumb dog knows this one!"
        m "What's the heart mean?"
        $ ccg("e2","b3","m1")
        ast "Who cares! This isn't secret at all!"
        m "Just wait a second now, lets at least read the first line."
        $ ccg("e6","b1","m4")
        ast "Fine..."
        $ ccg("e0","b1","m4")
        ast "\"Imperio of the heart is a forbidden variant of the unforgivable curse.\""
        ast "\"Whereas the regular imperio only allows control over the victims mind, imperio of the heart allows the caster-\""
        ast "\"to implant desires into the heart of their victim whilst leaving the mind untouched...\""
        ast "..."
        $ ccg("e7","b1","m1")
        ast "What's that supposed to mean then Dumby?"
        m "I think it means you can make Susan want stuff?"
        $ ccg("e7","b2","m4")
        ast "Couldn't I do that with the regular spell?"
        m "I'm not sure..."
        m "Although when you cast it on her the other day she did seem to lose her free will."
        m "So maybe this lets her keep it?"
        $ ccg("e0","b1","m4")
        ast "Hmmmm..."
        $ ccg("e7","b1","m3")
        ast "So this spell lets us change what she wants? But not control her completely?"
        $ ccg("e7","b3","m1")
        ast "That seems worse than the regular version!"
        m "Not if you want to hide the fact that you've cast it on her."
        $ ccg("e0","b0","m0")
        ast "Ohhhh... so that means we can change stuff about her without her realising?"
        m "It would seem so."
        $ ccg("e3","b0","m1")
        ast "That is cool!"
        $ ccg("e3","b3","m2")
        ast "Maybe we could change her into a big slut who walks around school with her gross boobs hanging out."
        call nar(">You feel yourself starting to harden at the idea.")
        m "Hmmm..."
        $ ccg("e7","b4","m1")
        ast "Dumby!!!"

        call blkfade

        call nar(">Astoria quickly hops off your lap in response.")

        #Hide CG scene.
        hide screen ccg

        pause.5
        hide screen blkfade

        call ast_main("What the hell was that?!","scream","closed","angry","mid",trans="fade")
        m "I have no idea what you are talking about..."
        call ast_main("You better keep those nasty thoughts to yourself, old man!","scream","angry","angry","angry")
        call ast_main("Or you'll have to go and kiss that granny's feet yourself!","clench","angry","angry","angry")
        m "Fine... I'm sorry..."
        call ast_main("...","pout","angry","angry","R")

        hide screen bld1
        hide screen astoria_main
        call blkfade

        call nar(">Astoria hops back on to your lap.")

        $ ast_spell_progress = 1

    if ast_spell_progress < 4:
        call astoria_spell_practice
        if ast_spell_progress < 4:
            call play_sound("door")
            hide screen astoria_main
            hide screen bld1
            hide screen blkfade
            with fade

            if daytime:
                jump night_start
            else:
                jump day_start

    call ast_main("Don't worry, we can try it out later sir.","smile","base","base","mid")
    m "I look forward to it."
    m "Goodnight astoria."
    call ast_main("night dumby!","grin","closed","base","mid")
    hide screen astoria_main
    with d3
    pause.5

    call nar(">Astoria queitly walks out of your office, a small smirk forming in the corner of her mouth.")

    call popup("Astoria has learned a new spell!", "Congratulations!", "interface/icons/head/head_astoria_2.png")

    if daytime:
        jump night_start
    else:
        jump day_start


label imperio_spell_2_training: #second level imperio spell
    if ast_spell_progress == 0:
        #talk about what it does new and about sitting on lap


        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade")
        m "ready to practice the next spell?"
        ast "Uh huh!"
        pass

        $ ast_spell_progress = 1

    if ast_spell_progress < 4:
        call astoria_spell_practice
        if ast_spell_progress < 4:
            call play_sound("door")
            hide screen astoria_main
            hide screen bld1
            with d3

            if daytime:
                jump night_start
            else:
                jump day_start

    call popup("Astoria has learned a new spell!", "Congratulations!", "interface/icons/head/head_astoria_2.png")

    if daytime:
        jump night_start
    else:
        jump day_start


label imperio_spell_3_training: #third level imperio spell
    if ast_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        call ast_main("So are you ready to learn the final imperio spell, [ast_genie_name]?","grin","angry","angry","mid",xpos="right",ypos="base",trans="fade")
        m "Ready as I'll ever be..."

        $ ast_spell_progress = 1

    if ast_spell_progress < 4:
        call astoria_spell_practice
        if ast_spell_progress < 4:
            call play_sound("door")
            hide screen astoria_main
            hide screen bld1
            with d3

            if daytime:
                jump night_start
            else:
                jump day_start

    call popup("Astoria has learned a new spell!", "Congratulations!", "interface/icons/head/head_astoria_2.png")

    if daytime:
        jump night_start
    else:
        jump day_start


#susan event labels are on the other page.
label hornify_spell_1_training: #first level hornify spell
    #Start grinding her hips in front of genie
label hornify_spell_2_training: #second level hornify spell
    #Takes her top of and starts shaking her boobs for genie
label hornify_spell_3_training: #third level hornify spell
    #Plays with herself in front of astoria and genie


label slutify_spell_1_training: #first level sluttify spell
    #Underwear becomes slutty
label slutify_spell_2_training: #second level sluttify spell
    #Skirt becomes short, vest only and slutty Underwear
label slutify_spell_3_training: #third level sluttify spell
    #Pink heart dress and no underwear


label orgasmio_spell_1_training: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2_training: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3_training: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times


label astoria_lap_sit_0_1:
    call nar(">Astoria lightly hops up onto your lap.")
    $ ccg("e6","b1","m3")
    ast "I suppose this isn't too bad..."
    $ ccg("e7","b0","m1")
    ast "At least your fat thighs are softer than the wood benches in the library..."
    m "Just start reading the spell..."
    $ ccg("e6","b1","m4")
    ast "Do I have to..."
    $ ccg("e0","b1","m4")
    ast "It looks kind of hard..."
    m "Didn't you beg me to teach you this sort of stuff?"
    $ ccg("e7","b4","m1")
    ast "I thought it would be easier than this dumby!"
    m "Tough..."
    $ ccg("e0","b1","m4")
    call nar(">You and Astoria spend the night pouring over the spell book, both of you talking about how you think it works...")
    call nar(">Your growing interest in the foreign magic distracts you from Asoria's incestant wiggling...")
    $ ccg("e2","b2","m1")
    ast "ah.... I think I better go to bed now dumby..."
    m "So soon? But we've still got so many pages left..."
    $ ccg("e7","b4","m1")
    ast "Tough!"
    m "Oh alright... I might stay up a little longer then..."
    ast "Don't read ahead!"
    m "Fine..."
    $ ccg("e7","b0","m1")
    ast "Good... Night dumby!"

    call nar("With a cheerful grin, astoria hops off your lap and out of your office.")

    return

label astoria_lap_sit_0_2:
    call nar(">Astoria lightly hops up onto your lap.")
    $ ccg("e7","b1","m3")
    ast "Do I really have to sit here?"
    m "Is it that bad?"
    $ ccg("e6","b1","m4")
    ast "I guess not..."
    $ ccg("e7","b1","m3")
    ast "But can't you just get another chair?"
    m "There's the one next to the fire."
    $ ccg("e6","b1","m1")
    ast "That wood one?"
    $ ccg("e7","b4","m1")
    ast "It looks so uncomfortable!"
    m "well then you'll just have to make do with my lap."
    $ ccg("e2","b4","m1")
    ast "Fine!"
    call nar(">You and Astoria spend the night reading over the spell, both of you silently reading along...")
    $ ccg("e0","b0","m0")
    ast "next page!"
    m "Already? I've still got a few lines left..."
    $ ccg("e7","b4","m0")
    ast "Ugh! You're such a slow reader dumby!"
    m "You're right... It must be because it's so late..."
    $ ccg("e7","b2","m1")
    ast "Can't we keep going?"
    m "Not if you expect me to keep up..."
    $ ccg("e2","b4","m4")
    ast "*hmph* I'm not going to put up with your slowness old man..."
    ast "I may as well go to bed."
    $ ccg("e6","b4","m4")
    ast "night dumby..."
    call nar("With a sullen put, astoria hops off your lap and out of your office.")

    return

label astoria_lap_sit_0_3:
    call nar(">Astoria lightly hops up onto your lap.")
    $ ccg("e7","b0","m1")
    ast "Can we start reading now?"
    m "Ready when you are."
    $ ccg("e0","b0","m1")
    ast "Good... I can't wait to learn a {b}fun{/b} spell."
    $ ccg("e7","b4","m1")
    ast "Do you know what your stupid school tried to teach me today?"
    m "I have no idea..."
    $ ccg("e6","b4","m4")
    ast "They insisted I learn spells for locating the nearest dragons..."
    ast "You even have to specify which type!"
    $ ccg("e7","b4","m1")
    ast "When am I ever going to use that?"
    m "When you're looking for a pile of gold?"
    $ ccg("e7","b4","m4")
    ast "..."
    $ ccg("e7","b1","m4")
    ast "Just open the book dumby."
    call nar(">You and Astoria read the book long into the night, occasionaly asking the other questions...")
    $ ccg("e0","b2","m0")
    ast "ugh... that's the end of the spell..."
    $ ccg("e7","b0","m1")
    ast "should we bring susan up here?"
    m "probably not... it's getting a little late..."
    $ ccg("e7","b4","m1")
    ast "Can't we do it now?"
    m "I don't think she'll be up."
    $ ccg("e6","b2","m4")
    ast "alright... we can try it out on her later..."
    $ ccg("e7","b2","m3")
    ast "goodnight dumby..."
    m "goodnight astoria."
    call nar("With tired face, astoria hops off of your lap and out of your office.")

    return



#
label astoria_lap_sit_1_1:
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.")
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.")
    $ ccg("e0","b1","m1")
    ast "According to the guide, this one is called imperio tempus..."
    $ ccg("e7","b0","m0")
    ast "It allows us to permanently set commands for the person we curse..."
    m "That seems useful!"
    $ ccg("e7","b0","m2")
    ast "And fun!"
    $ ccg("e0","b1","m1")
    ast "Hmmm... This one seems a lot harder than the last one though..."
    m "Do you think you'll be able to cast it?"
    $ ccg("e7","b4","m1")
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly pour over the book, your eyes occasionaly drifting shut...")
    $ ccg("e7","b4","m1")
    ast "Wake up dumby!"
    m "I'm up!"
    $ ccg("e7","b4","m4")
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    $ ccg("e7","b4","m1")
    ast "Well stop it!"
    $ ccg("e0","b1","m4")
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    $ ccg("e7","b1","m4")
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    $ ccg("e6","b4","m4")
    ast "Pfft, figures."
    $ ccg("e7","b4","m1")
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.")

    return

label astoria_lap_sit_1_2:
    call nar(">Astoria slowly hops up onto your lap, quietly opening the book.")
    $ ccg("e0","b2","m3")
    m "What's the matter? You seem a little tired."
    $ ccg("e7","b4","m1")
    ast "Am not!"
    $ ccg("e6","b1","m4")
    ast "I just had a long day is all..."
    ast "Ms Sprout made us spend all day plucking mandrakes to make juice..."
    $ ccg("e2","b4","m1")
    ast "They're really hard to pull out!"
    m "I bet..."
    m "If you're feeling tired, we can go through this tomorrow."
    $ ccg("e7","b4","m1")
    ast "I'm not tired!"
    m "If you say so..."
    call nar(">You begin to read over the complex spell, Astoria taking far longer to read through the pages...")
    $ ccg("e2","b1","m4")
    ast "..."
    m "Are you ready to read the next page?"
    $ ccg("e0","b1","m4")
    ast "yea..."
    $ ccg("e2","b2","m3")
    call nar(">As you turn the page you start to feel Astoria's body go limp on your lap.")
    m "Hmmm, poor little thing..."
    call nar(">You nudge astoria on the back slightly.")
    $ ccg("e5","b4","m4")
    ast "W-what... Keep your hands of me old man!"
    m "Pfft... I think it's time you went to bed."
    $ ccg("e2","b2","m1")
    ast "I told you, I'm not *yawn* tired..."
    m "..."
    $ ccg("e6","b2","m4")
    ast "Fine... we can keep reading tomorrow I guess."
    $ ccg("e7","b2","m4")
    ast "Night dumby..."
    m "Goodnight Astoria."
    call nar("With tired expression, astoria hops off of your lap and slowly out of your office.")

    return

label astoria_lap_sit_1_3:
    call nar(">Astoria effortlessly hops up onto your lap, eager to start reading the final parts of the spell.")
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's go! We're almost done!"
    m "Alright..."
    call nar("You and Astoria turn to one of the last pages and start reading over where you left off.")
    $ ccg("e0","b1","m4")
    ast "Hmmm... we might need to go back a little bit..."
    m "Why?"
    $ ccg("e6","b1","m4")
    ast "I don't really remember this..."
    $ ccg("e3","b1","m5")
    ast "I might have fallen asleep last time..."
    m "I thought you weren't tired?"
    $ ccg("e6","b4","m1")
    ast "Shut up dumby, no one likes a smarty pants!"
    m "You're telling me..."
    call nar(">You and Astoria turn back a few pages and continue reading...")
    $ ccg("e1","b0","m2")
    ast "That's it!"
    m "Finally..."
    $ ccg("e7","b4","m1")
    ast "*hmph* we would have been done faster if you didn't ask me what every second word meant!"
    m "I'm just testing you..."
    $ ccg("e6","b4","m4")
    ast "Pfft!"
    $ ccg("e7","b4","m1")
    ast "I don't even know how you got to be headmaster here without knowing what wingardium leviosa does..."
    m "Uhhh, my work here's mostly administrative..."
    ast "Administering your grossness on the other girls more like!"
    m "Speaking of which... How about we get susan bones up here?"
    $ ccg("e7","b5","m1")
    ast "At this hour?"
    $ ccg("e7","b4","m1")
    ast "I don't think so dumby..."
    m "ugh... fine..."
    call nar("Astoria hops off of your lap.")

    return



#
label astoria_lap_sit_2_1:
    call nar(">Astoria quickly hops up onto your lap.")
    $ ccg("e7","b0","m1")
    ast "Let's go dumby!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the final version of the imperio spell.")
    $ ccg("e1","b0","m1")
    ast "wow... this one gives us complete control over someone..."
    m "How's that different from the regular one?"
    $ ccg("e7","b4","m1")
    ast "You know how dumby! regular imperio only controls someone's mind..."
    ast "And it doesn't last forever..."
    $ ccg("e1","b1","m1")
    ast "Apparently this one allows us to change how they \'perceive the world\'..."
    $ ccg("e6","b0","m1")
    ast "Whatever that means... plus it lasts forever!"
    m "So basically it allows us to do anything with susan..."
    $ ccg("e7","b4","m1")
    ast "Anything I want!"
    m "Don't I get a-"
    $ ccg("e3","b0","m0")
    ast "Nope! Now let's keep reading..."
    call nar(">You and Astoria star to pour over the book, astoria seeming to need to reread several pages to fully understand them...")
    $ ccg("e0","b1","m4")
    ast "This seems pretty hard..."
    $ ccg("e2","b1","m4")
    ast "I wish my Latin were better."
    m "Here, I'll read it for you."
    $ ccg("e7","b5","m1")
    ast "You can read Latin?"
    m "Of course! I was there when they invented it!"
    $ ccg("e3","b5","m0")
    ast "Wow... you really are old!"
    m "More than you know..."
    $ ccg("e6","b0","m1")
    ast "Well you can read it to me later, I promised Pansy I'd hang out tonight."
    m "alright then..."
    call nar("You close the book as astoria hops off of your lap and out of your office.")

    return

label astoria_lap_sit_2_2:
    call nar(">Astoria hops up onto your lap, wiggling her little butt as she settles in.")
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's finish this spell so we can try it already!"
    $ ccg("e3","b0","m1")
    ast "I've even been practicing my Latin!"
    m "*yawn* old on a second..."
    $ ccg("e7","b4","m4")
    ast "What's wrong dumby, you're not going to fall asleep are you?"
    m "No... It's just Ms Granger has been tiring me out a little..."
    $ ccg("e7","b5","m1")
    ast "Hermione? You don't mean..."
    m "Forget I said anything."
    $ ccg("e6","b1","m4")
    ast "Hmmm, alright... let's just read the book old man."
    call nar(">You and astoria start to read over the complex spell. Your knowledge of latin proving essential to the small witch's understanding.")
    $ ccg("e7","b4","m1")
    ast "That's not a real word!"
    m "Yes it is..."
    $ ccg("e6","b4","m4")
    ast "Pffft... whoever made this dumb language is dumber than you dumby!"
    m "Ugh..."
    call nar(">You and astoria return to the book...")
    $ ccg("e0","b4","m1")
    ast "ugh... whoever wrote this book has terrible handwriting!"
    m "alright, I think we better call it there for tonight."
    $ ccg("e7","b4","m1")
    ast "*hmph* What? Why?!"
    m "I think someone's a little overtired..."
    $ ccg("e2","b4","m1")
    ast "I am not!"
    $ ccg("e7","b4","m1")
    ast "You're overtired!"
    m "Ugh, well either way, we can keep reading this later..."
    $ ccg("e6","b4","m3")
    ast "fine... but you're the one with the problem!"
    m "...."
    $ ccg("e2","b4","m4")
    call nar("Astoria pouts, then hops off your lap and leaves the office.")

    return

label astoria_lap_sit_2_3:
    call nar(">Astoria leaps into your lap as if you were santa claus at christmas time...")
    $ ccg("e7","b0","m1")
    ast "Let's go dumby! We're almost at the end!"
    m "Almost..."
    $ ccg("e0","b0","m0")
    call nar(">You and Astoria turn to bookmarked page and start reading over the final pages of the spell.")
    $ ccg("e3","b0","m0")
    ast "Wow... I think I'm finally getting good at Latin!"
    m "You're alright..."
    $ ccg("e3","b0","m2")
    ast "I'm the best!"
    m "Ugh..."
    m "Well come on then, why don't you read the next page out loud then?"
    $ ccg("e6","b4","m1")
    ast "Fine!"
    call nar(">You and Astoria slowly read over the next few pages, Astoria stumbling over every second word...")
    $ ccg("e3","b0","m2")
    ast "Done! I told you I was the best Dumby!"
    m "You sure showed me..."
    $ ccg("e6","b4","m4")
    ast "*hmph*"
    m "Want to practice it now?"
    $ ccg("e7","b4","m1")
    ast "We would have been able to if you had been able to read the last page in less than an hour!"
    $ ccg("e6","b2","m3")
    ast "It's too late now..."
    m "You read the last page!"
    $ ccg("e2","b4","m1")
    ast "Well it doesn't matter now anyways, I wanna go to bed."
    m "Fine... I suppose it is getting a little late."
    $ ccg("e7","b0","m0")
    ast "At least you can read a clock!"
    call nar(">With a teasing look on her face, astoria hops off of your lap and out of your office.")

    return


### Astoria Imperio Training ###

label ag_st_imperio:

    "Dev Note" "You send Astoria to Tonks"

    $ ag_st_imperio.inProgress = True

    jump main_room


label ag_se_imperio_sb: # Move label

    $ ag_se_imperio_sb.start()

    label end_ag_se_imperio_sb:

    jump main_room


label ag_st_imperio_E1:

    ton "Good evening, Professor."
    m "You are back."
    ton "Yes we are."
    ast "......................" # embarrassed
    g9 "Astoria! How was your training?"
    ast "................................"
    ton "It went very well, I'd say."
    ton "I instructed her on how to cast the curse properly."
    ton "The right wand movement,...the correct pronunciation..."
    ton "There's a lot to it!"
    ton "One mishap with those - and the curse might backfire!"
    ton "Sending you straight to St. Mungos hospital - quacking like a duck!"
    ton "I'd say she was very lucky using it on Susan..."
    ast "I knew exactly what I was doing..."
    ton "Of course you did, princess." # Happy
    ast "................................." # annoyed

    ton "Now, shall we get started?"
    ast "Get started - with what?"
    ton "Continuing your training, of course!"
    ton "I'd like you to cast the Imperius curse now... On another person."
    ast "Wait- what?"
    ast "I thought I wasn't allowed to ever use it again?"
    ton "You aren't...that is correct."
    ton "However, you are hereby given special permission!"
    ast "Really?" # happy
    ton "Yes, dear!"
    ton "I believe our Professor would have no objection with that..."
    ton "Would you, Professor?"
    ast "Please, Professor!"
    m "*Uhm*... Sure... Go ahead."
    ton "Splendid!"
    ast "Yes!" # Evil face

    ton "You can cast it, as long as it's under the surveillance of a teacher..."
    ton "And only within the walls of this room!" # stern
    ast "Right here? In front of Professor Dumbledore?"
    ton "Naturally!"
    ast "But who do I I cast it on? Susan?"
    ton "Not this time, sweetheart."
    ton "Today, I'd like you to cast it on me, if you don't mind..."
    ast "Wicked!"
    ton "Let's give this old man a quick demonstration of your talents, shall we..."
    m ".............................."

    ton "Just like we practiced..."
    ton "Do the movement with your wand, and then you say-"
    ast "Imperio!" # angry scream
    ton "Yes..."
    ton "...................."
    ton "You don't have to scream the words, darling."
    ton "What's crucial is that your mind is focused and-{w=2.0}{nw}"

    # Astoria casts imperio.
    ast "IMPERIO!{w=0.8}{nw}" # Screams it even louder
    # screenshake & chibi animation.

    ton "*Aaaaaah*..." # inhales
    ton "........................." # slight ahegao
    ast "......................" # clenched teeth
    m "What's happening to her?"
    ast "I just cast the spell on her..."
    ast "Now she should be under my command!"
    g9 "You don't say?"
    g9 "I love magic!"
    ast "What shall I do, Professor?"
    m "I don't know... Why are you asking me?"
    m "Did you not discuss this with her beforehand?"
    ast "No. All we did was some theoretical practice of the spell..."
    ast "I need to tell her to do something...or..."
    ast "I don't know... Maybe say something?"
    ton "*Hmmm*... Something..."
    m "What?"
    ast "She did it!"
    g4 "Something what?"
    ast "No, she just said what I asked her to say!"
    m "Oh..."
    ast "I believe it's working!"

    ast "*Uhm*... Professor Tonks, you can now speak freely!"
    ton "............................"
    ton "Oh... can I?..."
    ton "Thank you..."
    ast "She can hear me!"
    ton "You have a really cute voice..."
    ast "................"
    m "Try something else now."
    ton "I feel so good!"
    ton "What is happening to me?"
    ton "Are you playing with me?"
    ton "I want you to play with me!" # horny
    m "I think she's tripping..."
    ast "No! Keep - standing - still!"
    ton "Ok..................."
    g9 "This is quite funny to watch!"
    g9 "Can you make her *oink?*"
    ast "*oink?*"
    m "You know, like a pig..."
    ast "Yes, we can try that!"
    ast "Professor Tonks, I demand that you *oink!*"
    ton "*Huh?*..."
    ast "*oink!*"
    ton "..................."
    ast "Do it already!"
    ast "*oink!*{w=0.8}-*oink!*{w=0.8}-*oink!*" # Angry
    g9 "*he-he-he!*"
    ast "*oink*...{w=0.8} you pig!" # Screaming
    m "I don't believe she's going to do it..."
    ast "But!"
    m "It's pointless, girl... You can stop now..."
    ast "............................."

    # Tonks reverts back.

    ton "Oh my..."
    ton "Well that was fun!" # Happy
    ast "No it wasn't!"
    ast "Why weren't you doing pig noises!"
    ast "You refused to do what I demanded!"
    ton "Yes I did!"
    ton "It was quite easy, actually."
    ast "*Hnghhh!*"
    ton "Don't worry. You'll have better luck next time..."
    ton "Just try a bit harder."
    ast "..................................."
    ton "Thank you for your assistance, Professor."
    ton "You can have Astoria visit me again for our next training session..."
    m "Very well."
    ton "I can't wait!" # Happy
    ast "........................"
    ton "Have a good night, Professor."
    ton "Come on, Astoria. I shall escort you back to your dormitory..."
    ast "................................................."

    # They both leave.

    jump main_room


label ag_st_imperio_E2:

    ton "Hello, Professor."
    ast "........................."
    m "Back already?"
    ton "Yes, I gave Astoria a couple more pointers on how to improve the persuasiveness of the curse..."
    ton "The trick is to not lose your temper after casting it!"
    ast "........................."
    ton "This should be fun!"
    m "Very good."

    ton "Now, Astoria, just as last time - you will cast the Imperius curse on me..."
    ton "And I'll do my best to resist-"

    # Astoria casts the curse.
    ast "IMPERIO" # Screams
    # Screenshake

    g9 "Damnit, girl!"
    m "Give me a warning next time. You scared the crap out of me..."
    ast "Sorry Professor!" # Cute face

    ton ".........................."
    ton "*uhhhh*... I looooooove this!"
    ton "It's like - I'm floating..."
    ton "It feels...sooooooooooooo...goooooooooooood!"
    m "(Is she getting off on this?)"

    ast "What shall I have her do, Professor?"

    m "..........."
    menu:
        "Have her turn around.":
            ast "Yes, that's a good idea!"
            ton "................................"
            ast "Professor Tonks, I command you to turn around."
            ton "*Huh?*"
            ast "Turn around!" # louder
            m "Remember what she said about your temper, Astoria..."
            ast "Oh... yes Sir! Of course..."
            ast "Turn around."
            ton "......................"

            # Tonks turns around. (mirror sprite)

        "Ask her to remove her coat.":
            ast "Yes, that should be easy."
            ton "................................"
            ast "Tonks, I command you to remove your coat."
            ton "*Huh?*"
            ast "Come on, do it!"
            m "Try saying the magic word..."
            ast "Imperio? But I already did-"
            m "No... Ask her politely..."
            ast "Oh! I got it!"
            ast "Professor Tonks, please remove your coat for me..."
            ton "*Hmmm*... okay..."

            # Tonks removes her coat.


    ast "Yes, she did it!"
    ast "What shall I have her do next?"
    m "*hmmm*................."

    $ d_flag_01 = False

    label ag_st_imperio_E3_choices:

    menu:
        m "Make her..."
        "Do pig-noises again!" if not d_flag_01: # Jumps back to choices.
            ast "Do a pig-noise?"
            ton "*oink!*"
            ast "She did it!"
            g9 "Well done!"
            ast "Do it again!"
            ton "*oink!*"
            ast "*hi-hi-hi-hi!*"
            m "I believe that's enough-"
            ast "Do it again! Ten times!" # Angry
            ton "*oink*{w=0.8}-*oink*{w=0.8}-*oink*{w=1.2}-*oink*{w=0.8}-*oink*{w=1.4}-*oink*{w=1.4}-*oink*{w=1.6}-*oink*{w=2.0}-*oink*{w}-*oink!*"
            m "......................."
            ast "Agai-"
            g4 "That's enough, Astoria!"
            ast "Fine..."

            # Tonks returns to normal

            ton "Oh wow..."
            ton "You made me squeal like a pig!" # Happy
            ton "That was quite good!"
            ast "Thank you!"
            m "......................"
            m "I have to say, I'm not that impressed..."
            ton "You aren't?"
            ast "But, Professor!"
            m "Tonks, would you please do the noise again..."
            ton "The noise, Professor?"
            m "Yes. Squeal for me."
            ton "*oink*-*oink!*"
            g9 "See, I don't even have to use magic to make her do it!"
            ton "Very funny, Sir..."
            m "I'd like us to try this again..."
            ton "Right now? Are you sure?"
            g4 "(I want to see some tits - damnit! Or hear her talk dirty...)"
            m "Yes, cast that spell again, Astoria..."
            ast "Very well, Sir..."

            # Astoria casts imperio.
            ast "Imperio!"

            ton "*hmmm*............."
            ast "And now?"

            $ d_flag_01 = True

            jump ag_st_imperio_E3_choices

        "Let her say something naughty!": # Fails
            ast "*Huh?*..."
            g9 "Wouldn't you like to hear your teacher say something shameful?"
            ast "Yes!"
            ast "And what exactly?"
            m "I don't know... You should think of something..."
            m "You're the one with the magic-stick, after all..."
            ton "......................."
            ast "Okay... Professor Tonks..."
            ast "I want you to repeat after me..."
            ton "..................................."
            ast "I - am - a-"
            ton "I am a..."
            ast "dirty! - filthy! - pig!"
            ton "..................................."
            ast "Go on and say it!"
            ast "I'm a dirty - filthy - pig!"
            ton "*hi-hi!*..................................."
            ast "SAY IT!" # Scream
            g4 "Time-out!"
            ast "No! She has to do what she's told!"
            m "She clearly isn't going to..."
            m "We should take a break here..."
            ast "......................."

            # Tonks returns to normal.

            ton "*huh*..."
            ton "Well that was something, wasn't it?" # cheerful
            ast ".................................."
            m "You resisted her curse again."
            ton "Yes..."
            ton "I'm sorry, honey!"
            ast ".................................."
            ton "You can't expect to succeed right away now, can you?"
            ton "To master a spell it takes time - and regular practicing..."
            ton "Or else anyone could do it."
            ton "We'll try again next time..."
            ast "............................"
            ton "Have a good night, Professor."
            ton "After you, Astoria."
            ast "..........................."

            # They both leave

            # Event fails.
            $ ag_st_imperio.fail()

            jump main_room

        "Make her show us those tits!": # Succeeds
            ast "What?"
            g9 "Have her show us her breasts!"
            ast "Professor?!" # Shocked
            m "You did the same to Susan, didn't you?"
            ast "Yes, but..."
            ast "I doubt Professor Tonks would be ok with that!"
            m "Did you have those concerns with Susan as well?"
            m "Just try it."
            m "She can refuse to do it if she doesn't want to..."
            ast "I suppose..."
            ast "Professor Tonks, I'd like you to show us your..."
            ast "*uhm*..."
            ast "Your breasts!" # embarrassed
            ton "Oh..."
            ton "............................"
            g4 "(Fingers crossed!)"
            ton "............................" # Clenched teeth
            ast "I think she's struggling!"
            g4 "Very good, girl!"
            g4 "Pressure her more! I want to see those puppies!"
            ast "Professor Tonks, show us your breasts! Now!"
            m "(It was easier for her to resist doing pig-noises...)"
            m "(Could it be that she wants to show them to us? And is resisting that inner urge?)"
            ton "................................" # Really struggling!
            g4 "What a slut!" # Small text
            ast "Come on, do it!"
            ton "*Hnnnngh!*..."
            ton "*Aaaaahhh*................................" # Relieved
            m "I think she's done..."
            ast "What?"
            m "She broke the curse. You can stop now..."
            ast "*Aww*..."
            ast "If you say so, Professor..."

            # Tonks returns to normal.

            ton "Ouch... That was painful!"
            ton "You nearly got me there."
            ast "Did I really?"
            ton "Yes, well done, Astoria!"
            ast "Thank you!"
            m "Was it really such a struggle for you to not get your breasts out?"
            ton "*Uhm*..."
            ton "Yes!" # Embarrassed
            g9 "*He-he-he!*"
            ton "Shall we wrap it up for today?"
            ton "I'm sure next time you'll have better luck, Astoria."
            ast "Okay..."
            ton "Have a good night, Professor!"
            m "See ya..."

            # They both leave

            # Event succeeds

            jump main_room


label ag_st_imperio_E3:
    # Astoria is more confident this time.
    # Tonks sais that she almost want to do the command.
    # Atoria lightens up hearing that.
    # Tonks encourages her more, but to no success.
    # Next time it will be a success for sure!
    # Astoria leaves. After she's left, Tonks tells you how she barely felt anything...

    "Dev Note" "Add 3rd event here."

    jump main_room

label ag_st_imperio_E4:
    # Tonks taught her Astoria a new trick on how to make the imperio curse be more potent.
    # You need to charm the person you cast on. Compliment them. Flirt with them.
    # Tonks makes it appear as if it works. Takes off her vest, and then shows her breasts.
    # Astoria is getting cocky and demands Tonks to do more.
    # Tonks refuses which makes Astoria even angrier.

    "Dev Note" "Add 4th event here."

    jump main_room

label ag_st_imperio_E5:
    # Tonks strips in front of genie.
    # She mostly did it to make Astoria look good.
    # She wasn't really affected by the imperio curse, but she played along.
    # She said it's not enough to harm a trained Auror, but it will be enough to be successful on a weak student.

    "Dev Note" "Add 5th event here."

    call nar(">Astoria has \"mastered\" the imperio curse!")

    $ ag_st_imperio.complete = True

    jump main_room
