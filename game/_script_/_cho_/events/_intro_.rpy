

### Cho Intro ###

### Event 1 ###
# Cho first events your office, complaining about Hermione.
# Hermione enters and they have a fight.

label cho_intro_E1:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "(...)"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "(Who's that?)"
    m "(Can't be Hermione, she never knocks anymore.)"
    m "(...)"
    g9 "I bet it's another girl!"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "Please, give me a moment..."
    g4 "I just need to--{w} *urgh*!"
    call play_sound("equip_inventory")
    m "Adjust my pants...{w} There we go."

    $ d_flag_01 = False

    menu:
        "\"Who is it?\"":
            $ d_flag_01 = True

            call bld
            cho "Cho Chang, Sir."
            g4 "(Such a cute name... please be hot, please be hot...!)"
            cho "May I come in?"
            g9 "Please have nice tits!"
            cho "Sir?"
            m "Oh, right... Come in."

        "\"Come in!\"":
            pass


    # Cho enters your office for the first time.
    call cho_walk(660, "base", action="enter")

    call play_music("cho")
    call cho_main("Good morning, Sir.", "base", "base", "base", "mid", xpos="mid", ypos="base")
    call ctc

    menu:
        "\"Hello, Miss Chang.\"" if d_flag_01 == True:
            call cho_main("Hello to you too, Professor.", "smile", "base", "base", "mid")

        "\"Hello, Princess.\"":
            call cho_main("*Uhm*...", "annoyed", "wide", "base", "mid")
            call cho_main("Sir, I'd much prefer not to be called nicknames.", "open", "closed", "base", "mid")
            call cho_main("Mutual respect is very important for a student-teacher relationship to work.", "open", "base", "base", "down")
            m "(She must be fun at parties..)"
            call cho_main("I'd much prefer if you called me Cho, or Miss Chang...", "open", "base", "raised", "mid")
            g9 "And how is that any different..."
            call cho_main("It's my name, Sir!", "annoyed", "narrow", "base", "mid")
            m "I see..."
            m "Very well... Miss Chang it is..."
            call cho_main("Thank you.", "smile", "base", "base", "mid")
            call cho_main("Anyway...", "silly", "happyCl", "base", "mid")

        "\"Hey there, Chap.\"":
            call cho_main("Sir?", "clench", "wide", "base", "mid")
            m "What?"
            call cho_main("I'm a girl!", "angry", "narrow", "angry", "mid")
            g4 "Oh, of course you are... You just seemed a bit..."
            call cho_main("A bit what?", "annoyed", "narrow", "angry", "mid")
            m "(Don't say tomboy-ish, don't say tomboy-ish...)"

            menu: # doesn't matter what you pick
                "\"Tomboyish\"":
                    pass
                "\"Flat\"":
                    pass
                "\"Short\"":
                    pass

            call cho_main("What? Professor how dare you suggest I--", "clench", "wide", "base", "mid")
            g4 "Hold on!"
            m "Silly me I forgot where I put my glasses."
            call cho_main("", "annoyed", "narrow", "angry", "mid")
            m "You have to excuse my poor eye-sight."
            m "I'm very,{w} very,{w} very,{w} very old."
            m "You're clearly \"not\" a boy..."
            g9 "(Smooth...)"
            call cho_main("Right... well since you seem unable to see very well...", "open", "narrow", "base", "downR")
            m "..."
            call cho_main("It's Cho Chang.", "base", "narrow", "base", "mid")
            m "Ah, Miss Chang..."
            m "(Should I know who she is?)"
            call cho_main("Yes, anyway...", "open", "closed", "base", "mid")

        "\"Xiao Hua...\"":
           call cho_main("*Uhm*... thanks...", "normal", "narrow", "raised", "mid")
           call cho_main("But I don't speak that much Mandarin, Sir.", "open", "closed", "base", "mid")
           call cho_main("I was actually born here...", "base", "narrow", "base", "mid")
           g4 "Where?"
           call cho_main("In Scotland, Sir.", "angry", "wink", "base", "mid")
           call cho_main("People always act surprised when they find that out.", "open", "base", "base", "R")
           call cho_main("It doesn't help that my name sounds so Asian...{w} Cho Chang...", "annoyed", "narrow", "angry", "up")
           m "..."
           call cho_main("Anyway...", "open", "closed", "base", "mid")


    call cho_main("I'm terribly sorry for bothering you, Sir.{w=0.8} I hope I'm not interrupting anything important.", "open", "base", "worried", "mid")
    m "No worries, I can always spare some of my...{w=0.6} valuable time...{w=1.0} *Ahem*{w=0.6} for my dear students..."
    g9 "What's on your mind?"

    # Talk about her issue with Hermione
    call cho_main("It's-- It's Hermione Granger, Sir.", "annoyed", "narrow", "worried", "R")

    menu:
        m "(...)"
        "-The Granger girl?-":
            m "What did she do this time?"
            pass
        "-That troublemaker...-":
            g9 "I promise you, I'll give her a good {i}ole fashioned spanking{/i} next time I see her."
            call cho_main("A Spanking?", "angry", "wide", "base", "mid")
            call cho_main("And why would you do that, Professor?", "open", "narrow", "raised", "mid")
            call cho_main("(He really must be old...{w} They probably did stuff like that all the time back in the day...)", "angry", "narrow", "worried", "downR")
            pass

    call cho_main("Well Sir, it's about that new movement of hers...", "open", "closed", "base", "mid")
    m "The \"Men's rights movement?\" I'm familiar."
    call cho_main("Not that one, Sir...{w=0.8} The other one...", "open", "narrow", "worried", "downR")
    g4 "Oh good...{w=0.5} another one..."
    call cho_main("Yes... And you need to stop it Professor!", "angry", "base", "base", "mid")
    call cho_main("Her{w=0.5} \"Quidditch equality movement.\"", "soft", "narrow", "angry", "mid")
    m "Her what now?"
    call cho_main("I know! It's absolutely ridiculous...{w=0.5} It's going to ruin the sport for all of us!", "clench", "base", "worried", "mid")

    m "Sport? Which sport?"
    call cho_main("Quidditch!", "scream", "narrow", "angry", "mid")
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "(Quidditch? What a stupid name for a sport.)"
    call cho_main("The movements' goal is to grant a larger portion of our female students the ability to play.", "open", "narrow", "base", "down")
    m "And...{w} that's a bad thing?"
    call cho_main("Her way of going about to achieve it is...", "annoyed", "narrow", "angry", "R")
    call cho_main("Granger is trying to separate us into male and female teams.", "annoyed", "narrow", "worried", "mid")
    call cho_main("She believes it would put girls on an equal playing field against other girl teams.", "open", "closed", "worried", "mid")
    call cho_main("But what she's forgetting is that all the female players who made it into a team are already considered a valuable asset -- or they wouldn't be there!", "open", "narrow", "angry", "R")
    call cho_main("I worked hard to be at the same level as my fellow teammates...", "annoyed", "narrow", "worried", "downR")
    call cho_main("Splitting us up into a male and female league would just bring on girls that are just there to flaunt their bodies, instead of taking the sport seriously...", "open", "narrow", "angry", "downR")
    m "Doesn't sound like the worst idea honestly..."
    call cho_main("Sir... I've trained all my life to be where I'm at.", "clench", "narrow", "angry", "mid")
    call cho_main("Just as hard as all the other great female Quidditch players of history!", "scream", "closed", "angry", "mid")
    call cho_main("They played side by side with men... Earning their place amongst the best!", "open", "narrow", "angry", "down")
    call cho_main("It never mattered what gender they were.", "angry", "narrow", "angry", "mid")
    call cho_main("To be shoved aside and forced to play alongside a collection of mediocre amateurs...", "clench", "closed", "angry", "down")
    call cho_main("If this goes through it'd mean that I would never get a proper chance at winning the Quidditch cup!", "clench", "closed", "angry", "mid")
    m "Right..."
    call cho_main("Sir... This would destroy the foundations of the entire sport, traditions going back centuries...", "open", "narrow", "angry", "down")
    m "Now, I think you're being a bit overdramatic Miss--"
    call cho_main("I'd get even less attention as one of the few girls in the league!", "open", "narrow", "angry", "mid")
    m "Ah... So that's where the problem lies."

    call cho_main("Sir, could you please talk to her? I'd be very grateful if you did.", "upset", "base", "worried", "mid")
    call cho_main("I would be forever in your debt.", "soft", "narrow", "base", "mid")
    m "Forever in my debt you say?"
    call cho_main("Yes, Professor. I'd do anything if you make this right.", "smile", "base", "angry", "mid")
    call cho_main("Anything!", "clench", "narrow", "angry", "mid")
    g9 "It's your lucky day, Miss Chang!"
    m "I will gladly talk to Miss Granger, but in return..."
    g9 "How about you come over here and suck on my--"

    # Hermione walks in
    stop music fadeout 1.0
    call hide_characters
    with d3

    call play_sound("door")
    call her_chibi("stand", "door", "base")

    call her_main("Professor I'm sorry to bother you but I wanted to...", "open", "closed", "base", "mid", ypos="head", flip=False)
    call her_main("!!!", "normal", "wide", "base", "stare", trans=hpunch)

    call her_walk(570, "base")
    call her_chibi("stand",570,"base",flip=True)
    pause .5

    play music "music/deadly-roulette-by-kevin-macleod.mp3" fadein 1 fadeout 1
    call cho_main("", "annoyed", "narrow", "angry", "downR", xpos="base", ypos="base")
    call her_main("Cho...{w=0.5} How nice to see you here...", "open", "closed", "base", "mid", xpos="mid", ypos="base", flip=True)
    call her_main("And why are you here exactly?", "annoyed", "narrow", "annoyed", "L")

    call cho_main("Oh, you know...{w=0.5} Just having a discussion with our dear headmaster...", "soft", "base", "base", "R")

    $ renpy.sound.play("sounds/slap_03.mp3")
    call her_main("{size=-5}Bitch...{/size}", "angry", "closed", "angry", "mid", trans=hpunch)

    $ renpy.sound.play("sounds/slap_02.mp3")
    call cho_main("{size=-5}Whore...{/size}", "clench", "closed", "angry", "mid", trans=hpunch)
    call her_main("...", "normal", "squint", "angry", "L", cheeks="blush")
    call cho_main("...", "upset", "narrow", "base", "L")
    call her_main("So... What have you been discussing?{w=0.4} Anything I should know?", "open", "squint", "base", "mid", cheeks="blush")
    call cho_main("Oh, it's nothing that you need to worry your pretty little head about...", "smile", "narrow", "angry", "L")
    m "(This could take a while...)"


    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while they talk.)\"":
            call hide_characters
            with d3
            pause .2

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .5

            $ cho_jerk_off_counter += 1
            $ her_jerk_off_counter += 1
            $ jerked_off_during_cho_intro = True # Optional dialogue with Snape.

            $ masturbating = True

        "\"(I should probably listen to them.)\"":
            $ masturbating = False

    # Masturbating
    if masturbating:
        call nar(">You pull your cock out and begin masturbating... focusing on the now heated argument between the two girls in front of you.")

        show screen cho_main
        call her_main("Oh yeah, well... I bet it can't be anything good seeing how you usually act around men...", "mad", "narrow", "angry", "R")
        call cho_main("What's that supposed to mean?!?", "clench", "narrow", "angry", "L")
        call her_main("You know exactly what I mean...", "crooked_smile", "narrow", "base", "R_soft")
        call her_main("I heard about how you were flaunting those... \"things\" of yours at Seamus Finnigan.", "crooked_smile", "narrow", "base", "R_soft")
        with hpunch
        call cho_main("\"Things?\"", "angry", "wide", "base", "L")
        call cho_main("Oh, miss perfect Hermione Granger.{w=0.8} Too afraid to even use the word \"tits\"...", "open", "narrow", "angry", "L")
        call her_main("Well yours hardly qualify as such...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        call cho_main("How dare you!", "clench", "closed", "angry", "mid")
        call cho_main("And so what? What's wrong with being confident about your body...", "open", "narrow", "angry", "L")
        call cho_main("You should try it some time... You might even get a boyfriend one day...", "smile", "narrow", "angry", "L")
        call cho_main("Though what do I know...", "open", "closed", "base", "mid")
        call cho_main("I didn't need to get my teeth shortened so I wouldn't be confused for a rabbit!", "open", "narrow", "angry", "L")
        call her_main("...", "normal", "narrow", "angry", "down", cheeks="blush")
        call cho_main("Not that anyone would even see them through that horribly bushy hair of yours...", "smile", "narrow", "angry", "L")
        call her_main("Well, I heard that you were caught snogging someone in one of the carriages after the triwizard tournament.", "soft", "closed", "base", "mid", cheeks="blush")
        call her_main("I'm sure that will go down in the Hogwarts book of history...", "grin", "narrow", "base", "mid", cheeks="blush")
        g9 "(How naughty, didn't expect such indecent behaviour from a girl with such a cute face...)"
        call cho_main("Yeah? You ever even kissed a boy before, Granger?", "soft", "narrow", "raised", "L")
        call her_main("", "normal", "base", "worried", "R", cheeks="blush")
        call cho_main("And I'm talking about a real kiss, and not your daddy kissing you good night...", "soft", "narrow", "raised", "L")
        call her_main("Oh...{w=0.5} Of course I have!", "angry", "base", "worried", "R", cheeks="blush")
        call her_main("Just because I don't jump on every opportunity to glimpse random boys' wands...", "soft", "closed", "base", "mid", cheeks="blush")
        call her_main("Unlike some other girls at this school...", "normal", "narrow", "angry", "L", cheeks="blush")
        call her_main("That doesn't mean I've never kissed anyone...", "soft", "base", "worried", "mid", cheeks="blush")
        g9 "..."
        call her_main("And I didn't need to have my breasts enlarged so that I wouldn't be confused for a boy!", "annoyed", "narrow", "annoyed", "L", cheeks="blush")
        call cho_main("Oh yeah... Like you haven't been flaunting yours around either...", "open", "narrow", "angry", "L")
        call cho_main("Don't you try and act all innocent!", "angry", "narrow", "angry", "L")
        call her_main("As If...", "normal", "narrow", "annoyed", "mid", cheeks="blush")
        call cho_main("I wouldn't doubt that's why you're here in the first place!", "open", "closed", "base", "mid")
        call cho_main("To push your stupid agendas, whilst you push your breasts together at the same time.", "clench", "narrow", "angry", "L")
        g4 "{size=-4}You fucking sluts!{/size}"

        # Genie cums
        call hide_characters
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        g4 "*heavy breathing* {size=-4}Fuck yes...{/size}"

        call cum_block

        g4 "*Argh!* {size=-4}You whores!{/size}"

        stop music fadeout 2.0
        call cho_main("Sir?", "soft", "narrow", "base", "mid")

        m "(Shit...)"

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        call cho_main("Sir, I'm sorry about all this... it's not what I came here for...", "open", "closed", "worried", "mid")
        m "Oh, of course not!"
        call cho_main("Please consider what we've talked about...", "smile", "base", "worried", "mid")
        m "Certainly..."

        # Cho walks to the door and stops.
        call cho_walk("door", "base")
        pause .8
        call cho_chibi("stand", "door", "base")
        with d3
        pause .8

        call cho_main("{size=-4}You have fun now... getting at that wand of his...{/size}", "angry", "narrow", "angry", "L")
        call her_main("*Tzzzh!*...", "clench", "closed", "angry", "mid")


    # Not masturbating
    else:
        m "Ladies, no arguing now..."
        m "You're in the headmaster's office, surely there's a time and place."
        call her_main("...", "annoyed", "narrow", "base", "R_soft")
        call cho_main("*Hmph*... There's no argument here...", "open", "narrow", "angry", "L")
        call cho_main("I'm sure that Hermione's reasons for interrupting are totally valid...", "upset", "narrow", "angry", "L")
        call her_main("And I'm sure Cho wasn't just coming here to flaunt her body...", "soft", "closed", "base", "mid")
        call cho_main("What's that supposed to mean?!?", "clench", "narrow", "angry", "L", trans=hpunch)
        m "(I guess I'll just have to wait this one out..)"

        # Black screen
        call hide_characters
        call blkfade
        pause 2

        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

        pause 1
        call hide_blkfade

        $ renpy.sound.play("sounds/snore1.mp3")
        gen "*Snore*{w=2.0}{nw}"
        call her_main("", "annoyed", "narrow", "annoyed", "R")
        call cho_main("As if I'm going to believe that nonsense, Granger!", "angry", "narrow", "base", "L", trans=hpunch)
        $ renpy.sound.play("sounds/snore2.mp3")
        gen "......{w=0.5}*Snore*{w=1.0}{nw}"
        call her_main("I had completely legitimate reasons for coming here...", "soft", "closed", "base", "mid")
        call her_main("You tell her Professor!", "open", "narrow", "annoyed", "mid")
        $ renpy.sound.play("sounds/snore3.mp3")
        gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
        call her_main("Professor!", "scream", "base", "angry", "mid", trans=hpunch)
        g4 "*Grunt* {size=-4}Huh, what?{/size}"
        call her_main("I always have a valid reason for coming here, don't I?", "base", "base", "base", "mid")
        m "Of course you--"
        call cho_main("Always? So you \"do\" come here often!", "smile", "narrow", "base", "L")
        call her_main("So what...", "angry", "closed", "angry", "mid")
        m "Ladies, I think it's time to--"
        call cho_main("Don't worry about it Sir, I was just about to leave anyway...", "soft", "narrow", "angry", "mid")
        call her_main("...", "annoyed", "narrow", "angry", "R")

        # Cho walks to the door and stops.
        call cho_walk("door", "base")
        pause .8
        call cho_chibi("stand", "door", "base")
        with d3
        pause .8

        call cho_main("Professor, please do consider what we discussed earlier...", "soft", "closed", "base", "mid", trans=d3)
        m "Of course."
        call her_main("*Hmm*?", "normal", "squint", "base", "mid", trans=d3)

        stop music fadeout 2.0

    hide screen cho_main
    hide screen hermione_main
    with d3

    # Cho leaves
    pause .2
    call cho_chibi("stand", "door", "base",flip=True)
    with d3
    pause .5

    call cho_chibi("leave")

    call her_chibi("stand", "mid", "base",flip=False)

    call her_main("...", "annoyed", "base", "angry", "mid", xpos="base", ypos="base", flip=False, trans=d3)
    m "..."
    call her_main("You're buying favours from her aren't you?", "soft", "narrow", "base", "mid_soft")
    m "I'm--"
    call her_main("I knew it!", "angry", "base", "angry", "mid")
    g4 "Now, if you could just listen for a second!"
    call her_main("I don't want to hear it!", "open", "closed", "base", "mid")
    call her_main("I'm leaving.", "normal", "squint", "angry", "mid")

    # Hermione leaves
    call her_walk(action="leave")

    # Hermione Mood down
    $ her_mood += 6
    $ hermione_busy = True

    $ cho_intro.E1_complete = True

    m ".......{w=0.5}women..."

    jump main_room_menu


### Event 2 ###
# Cho complains about Hermione again.
# You need to talk to Hermione and have her drop her Quidditch movement.

label cho_intro_E2:
    stop music fadeout 1.0
    call play_sound("door")
    call cho_chibi("stand", "door", "base")
    with d3
    pause .5
    call cho_chibi("stand", "door", "base",flip=True)
    with d1
    call play_sound("bump")
    pause .8
    call cho_chibi("stand", "door", "base",flip=False)
    with d1
    pause .3
    call cho_walk("desk", "base")
    pause .2

    call cho_main("I hate her!", "scream", "closed", "angry", "mid", xpos="mid", ypos="base", trans=hpunch)
    call cho_main("", "clench", "narrow", "angry", "mid")

    g9 "Miss Chang! My favourite student!"
    g9 "I'm so glad to see you. Is there something I can--"

    call play_music("hitman")
    call cho_main("Cut the crap, Professor!{w=0.6} I know you've told her!", "soft", "narrow", "angry", "mid")
    g4 "{size=-4}Please don't hurt me.{/size}"
    call cho_main("How could you have done this?{w=0.6} Sending this dim-witted Gryffindor tramp after me?", "open", "narrow", "angry", "mid")
    g4 "W-who?"
    call cho_main("Granger!", "scream", "closed", "angry", "mid", trans=hpunch)
    g4 "Aaa-h!" # Girly scream
    call cho_main("Gryffindor's role model student...", "angry", "narrow", "angry", "mid")
    call cho_main("She's out there spreading mean rumours about me!", "open", "narrow", "angry", "R")
    m "How mean are we talking?"
    call cho_main("The worst kind! That I'm cheating at Quidditch!", "angry", "narrow", "angry", "down")
    call cho_main("How am I cheating, Professor? Ravenclaw is always in last place?!", "soft", "narrow", "worried", "downR")
    call cho_main("Not to mention that she's told everyone that I'm whoring myself out to my other classmates, and even my teachers!", "open", "narrow", "angry", "L")
    call cho_main("I did none of that, Professor! None!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("And she still won't lay off her stupid equality movement thing!", "annoyed", "narrow", "angry", "mid")
    m "You need to calm down, girl."
    call cho_main("{size=-4}When I'm out of here I'm going to rip that bitch's head off...{/size}", "clench", "narrow", "angry", "downR")
    g4 "(Yikes!)"
    m "I could hear that."
    call cho_main("Good. Then you already know what I'm willing to do if this continues...", "open", "closed", "angry", "mid")
    call cho_main("If you can't stop her, Professor, Then I will!", "open", "base", "angry", "mid")
    call cho_main("And rest assured that I will end her!", "soft", "narrow", "angry", "mid")

    menu:
        m "(...)"
        "\"Sure, go for it!\"":
            call cho_main("What?", "annoyed", "narrow", "angry", "mid")
            call cho_main("Sir, I'm not joking around. This is serious!", "open", "base", "angry", "mid")
            call cho_main("Tell Granger to keep her bushy head out of it!", "clench", "narrow", "angry", "mid")
            m "Fine, whatever... This isn't worth the drama..."
            m "(I can just bribe Granger with some house-points anyway.)"
            m "I shall talk to her."

        "\"I'd prefer you didn't...\"":
            call cho_main("Then do something about it!", "clench", "closed", "angry", "mid")
            call cho_main("And don't even think about calling me to your office again...", "open", "narrow", "angry", "mid")
            call cho_main("Not until you've dealt with that skank!", "clench", "narrow", "angry", "mid")
            call cho_main("Do I make myself clear, Sir?", "scream", "closed", "angry", "mid", trans=hpunch)
            call cho_main("", "angry", "narrow", "angry", "mid")
            m "I suppose..."

    # Back to cheerful.
    call play_music("night")
    call cho_main("Good.", "base", "base", "base", "mid")
    m "(...)"
    call cho_main("Have a nice evening, Professor.", "smile", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "I better talk to Hermione about this..."
    m "Or Snape first. Maybe he can help me more."
    g4 "With his unfailing wisdom."
    m "Who am I even kidding..."

    $ hermione_busy = True
    $ snape_busy = False

    $ cho_intro.E2_complete = True

    jump main_room_menu


### Snape Hangout Event 1 ###
# You tell Snape about Cho's visit.

label ss_he_cho_E1:
    call bld
    m "I had another girl visiting me the other day."
    call sna_main("I told you not to get involved with the outside world.", "snape_09", ypos="head")
    call sna_main("I hope you were smart enough to not let her into your office.", "snape_05")
    g9 "How couldn't I let her in? She sounded cute."
    call sna_main("Why doesn't that surprise me...", "snape_06")
    call sna_main("And who was this girl?", "snape_03")

    menu:
        "\"Her name was Cho Chan.\"":
            call sna_main("Cho Chang?", "snape_01")
            m "No, I'm sure it was \"Chan\"."
            call sna_main("I know my students names, Genie.", "snape_04")

        "\"I can't remember. I got too distracted by her legs...\"":
            call sna_main("Can you describe her?", "snape_05")
            call sna_main("Hair colour, height, her uniform colour? Anything?", "snape_02")
            m "I believe she was Asian."
            call sna_main("Cho Chang?", "snape_10")
            m "Bless you."
            call sna_main("No. That's her name.", "snape_08")
            call sna_main("We only have one Asian girl at our school.", "snape_24")
            call sna_main("You'd think as the only wizard school in all of Britain, our school would be more diverse...", "snape_09")

    call sna_main("And what did she want from you exactly?", "snape_05")
    m "She asked me a couple of things about Quidditch."
    call sna_main("Of course.", "snape_09")
    call sna_main("Her entire world revolves around that stupid broomstick rally.", "snape_08")
    m "I take it that you aren't a fan?"

    m "She could be a great candidate for our little training scheme."
    call sna_main("What? Do you want to turn her into a slut too?", "snape_01")
    m "Not only that. I believe she could be of help to deal with the Granger girl as well."
    call sna_main("Interesting. It seems like you have already made plans for her.", "snape_02")
    m "I thought of a couple of things."
    call sna_main("You have my attention!", "snape_13")

    $ d_flag_01 = False
    $ d_flag_02 = False

    label discuss_cho_plan:
        if d_flag_01 and d_flag_02:
            jump discussed_cho_plan

    menu:
        "\"Help her win the Quidditch cup\"" if not d_flag_01:
            $ d_flag_01 = True

            call sna_main("And help her win against Slytherin?", "snape_16")
            call sna_main("I can't agree to that, Genie. As much as I'd like to see the Potter boy demoralised by losing to a girl...", "snape_10")
            call sna_main("Or Malfoy for that matter... He's been way too cocky lately.", "snape_08")
            m "Who?"
            call sna_main("A student of mine... Rich parents, bought his way into our Quidditch team... Spoiled beyond belief.", "snape_29")
            m "Didn't you say you don't care much about Quidditch?"
            call sna_main("Of course I don't... But a win is a win.", "snape_09")
            call sna_main("Besides, Ravenclaw doesn't have a chance against Slytherin.", "snape_03")
            call sna_main("They are notoriously bad at Quidditch. And they have been for years.", "snape_02")
            m "You sound very confident."
            g9 "Want to bet on it?"
            call sna_main("A bet? How very enticing!", "snape_20")
            call sna_main("How much are you willing to bet?", "snape_18")
            m "Twenty bucks?"
            call sna_main("Don't you mean gold?", "snape_05")
            m "Twenty... gold then..."
            call sna_main("That's barely worth it.", "snape_04")
            call sna_main("How about two thousand gold?", "snape_13")

            if game.gold < 2000:
                m "I don't have that much gold."
                call sna_main("Well, you have plenty of time to gather that amount.", "snape_22")
            else:
                m "Are you feeling \"that\" confident?"
                call sna_main("About Slytherin winning the cup?", "snape_20")
                call sna_main("Absolutely!", "snape_22")

            call sna_main("So, what do you say? Want to take the bet?", "snape_13")
            m "Under one condition."
            m "You won't cheat, and you won't give Slytherin any unfair advantages."
            call sna_main("I'd never think of it.", "snape_09")
            m "So, you want to take on the bet?"
            call sna_main("Of course, I have no doubt Slytherin will win the cup.", "snape_02")
            call sna_main("At least Quidditch will be worth watching now. I can't say no to some good old gambling.", "snape_20")
            call sna_main("But how will you help Miss Chang in Quidditch? You know nothing about it!", "snape_05")

            menu:
                "\"I'll just read a book about it\"":
                    call sna_main("You are really planning to take this bet seriously, aren't you?", "snape_04")
                    m "You have no idea! I'll do anything to get into that girl's panties."
                    call sna_main("Blinded by the sweet love for a girl...", "snape_13")
                    call sna_main("You have already lost, my friend!", "snape_21")
                    m "We'll see about that."
                    m "(Now, where could I get a book about Quidditch from...)"

                "\"I trust my instincts!\"":
                    call sna_main("Your instincts?", "snape_14")
                    m "Never underestimate the capabilities of a Genie..."
                    call sna_main("(...)", "snape_12")

            #TODO If you've not picked the other option (Help her win the Quidditch cup)
                #call sna_main("So, that's in then? You're staking both your money and the chance at getting in this girls panties on Ravenclaw winning the cup?", "snape_01")
                #g4 "You bet I-- No wait! Of course that's not all of it!"
                #m "*Err*..."
                #m "Oh! I'm also planning to..."

            jump discuss_cho_plan

        "\"Have her and Hermione go at each other\"" if not d_flag_02:
            $ d_flag_02 = True

            call sna_main("Granger? Why her?", "snape_05")
            m "They absolutely despise each other."
            call sna_main("They do?", "snape_20")
            m "Yes. They had a little confrontation here in my room..."
            call sna_main("A confrontation? So so...", "snape_13")
            call sna_main("What was it about?", "snape_20")

            if jerked_off_during_hermione_intro and jerked_off_during_cho_intro:
                m "I have no idea. I jerked off during their whole exchange."
                call sna_main("You did that again? And neither of them realised?", "snape_22")
                m "Didn't seem like it. They were too occupied with insulting each other..."

            elif jerked_off_during_cho_intro:
                m "I have no idea. I jerked off during their whole exchange."
                call sna_main("You did what?", "snape_15")
                m "I jerked off.{w} Beat my meat.{w} Wrestled the snake.{w} Whatever you want to call it."
                m "Don't tell me you never do it..."
                call sna_main("Not in front of my students!", "snape_07")
                call sna_main("How did neither of them realise what you were doing?", "snape_10")
                m "They were too occupied with insulting each other..."
                call sna_main("I can imagine that...", "snape_20")

            else:
                m "Some nonsense about wasting my time."
                call sna_main("Which they probably did?", "snape_05")
                m "Yeah. But I slept through most of it..."
                call sna_main("I wish I could do the same.", "snape_09")
                call sna_main("Zone out and dream of stuffing that witch's relentless mouth!", "snape_06")
                m "I feel you..."

            call sna_main("*Hmm*... That reminds me of something I witnessed at the end of last year...", "snape_23")
            call sna_main("Granger was scolding the poor girl for kissing a boy in the hallways.", "snape_20")
            m "Hot...{w} What happened then?"
            call sna_main("They were screaming and grabbing at each other's hair before I had the chance to interfere.", "snape_18")
            call sna_main("I ended up taking fifty points from Gryffindor. I should have taken at least one hundred now that I think about it...", "snape_22")
            m "Does she often do things like that?"
            call sna_main("Are you kidding? All the bloody time!", "snape_17")
            call sna_main("Granger is a nuisance to everyone. Didn't I already tell you that?", "snape_16")
            m "No. I meant the Cho girl..."
            g9 "Does she make out with boys often?"
            call sna_main("How should I know. I'm not her stalker.", "snape_12")
            m "Well, if what you've said is true... Training her should be a piece of cake."
            g9 "And what a delicious piece of cake it will be!"

            #TODO If you've not picked the other option (Have her and Hermione go at each other)
                #call sna_main("So, how are you planning on achieving all this exactly?", "snape_01")
                #call sna_main("Surely you can't rely on Miss perfect to get anywhere with this girl...", "snape_04")
                #m "No, but I'm sure she'll play her part in the next step of my plan with Miss Chang..."
                #call sna_main("Which is?", "snape_05")

            jump discuss_cho_plan


    # Ending
    label discussed_cho_plan:

    show screen with_snape(ani=True)
    show screen bld1
    call notes
    ">You spend the rest of the evening in Snape's company, talking about Cho's impressive thighs."

    hide screen bld1
    with d3

    $ ss_he.cho_E1 = True

    jump day_start


### Hermione Talk 1 ###
# You talk to Hermione to drop her Quidditch movement. You then summon Cho.
# Cho is now unlocked and you can summon her.

label cho_intro_E3:

    call her_main("", xpos="mid", ypos="base", trans=fade)

    # Intro
    if not cho_intro.E3_intro:
        $ cho_intro.E3_intro = True

        m "I got some word about you that needs to be addressed..."
        call her_main("About what? Am I in trouble for anything?", "soft", "wide", "base", "mid")
        m "Miss Chang..."
        call her_main("Oh...", "annoyed", "narrow", "base", "up")
        call her_main("What about her...", "annoyed", "base", "angry", "mid")
        m "Well, it has come to my attention that you've been spreading false rumours about her."
        call her_main("And? It's well deserved in my opinion...", "soft", "narrow", "annoyed", "mid")
        m "Well, don't you feel like it's unbefitting of you to publicly talk badly about another student?"
        call her_main("...", "annoyed", "narrow", "base", "down")
        g9 "Surely that isn't something to expect from Gryffindor's finest..."
        call her_main("Did Cho put you up to this?", "normal", "squint", "base", "mid")
        g4 "..."
        m "(She's onto me!)"
        m "Of course not... it was another teacher, actually."
        call her_main("Who was it?", "open", "base", "angry", "mid")
        m "Not important..."
        call her_main("It was Snape wasn't it...", "annoyed", "narrow", "base", "mid_soft")
        g4 "(She's good!)"
        m "Well, I'd like you to stop and that's all that matters..."
        m "And that includes the..."
        m "Quidditch...{w} whatever it was...{w} movement."

    # Repeat
    else:
        m "[hermione_name], there is something we need to talk about."
        call her_main("Is it about Cho again?", "annoyed", "squint", "base", "mid")
        m "Yes indeed."
        m "I'd like you to stop your..."
        m "Quidditch...{w} something something...{w} movement."

    if her_whoring < 4: # If you haven't groped her breasts or ass yet.
        call her_main("My \"Quidditch equality movement\"?", "soft", "base", "base", "mid")
        call her_main("But Sir, I'm on the verge of a breakthrough with it!", "soft", "closed", "base", "mid")
        call her_main("I worked very hard on gathering all records of past Quidditch matches, throughout the complete history of Quidditch!", "open", "wink", "base", "mid")
        call her_main("You'd be surprised just how few female--", "soft", "closed", "base", "mid")
        m "I'll give you ten house points."
        call her_main("Ten points?", "soft", "wide", "base", "stare", trans=hpunch)
        call her_main("Sir do you even realise how much time it took me to do all that research?", "angry", "squint", "angry", "mid")
        m "Twenty?"
        call her_main("Two hundred!", "angry", "closed", "angry", "mid")
        g4 "Two hundred? Are you nuts?"
        call her_main("And just points isn't going to cut it...", "open", "closed", "base", "mid")
        m "Then what else?"
        call her_main("*Uhm*...", "annoyed", "base", "base", "R")
        m "You're testing my patience Miss Granger..."
        call her_main("Oh, I know!{w=0.5} I want a seat in the teacher stands during the Quidditch matches!", "smile", "happyCl", "base", "mid")
        call her_main("Cho would be so jealous if she saw me sitting near the commentator and teachers...", "grin", "narrow", "base", "mid_soft")
        m "So, you want both two hundred points and a seat in the teacher stands..."
        call her_main("Yes...", "base", "happy", "base", "mid_soft")

        menu:
            m "(...)"
            "\"Very well...\"":
                m "Anything else?"
                call her_main("Well...", "soft", "happy", "base", "R")
                m "Don't push your luck..."
                call her_main("No, I think that should do...", "smile", "happyCl", "base", "mid")
                m "Two hundred points to Gryffindor...{w=0.6} Happy?"
                $ gryffindor += 200

                call her_main("If I'm truly honest with you Sir,{w=0.6} My plans weren't that popular with the Quidditch teams in any case.", "soft", "narrow", "base", "mid_soft")
                m "I can't imagine why..."
                pass

            "\"I don't think so!\"":
                call her_main("What?... Why?!", "shock", "wide", "base", "stare", trans=hpunch)
                m "Because you are being unreasonable."
                call her_main("But you made it sound like it was something important to you!", "disgust", "narrow", "worried", "mid_soft")
                m "And you believe that I'd just throw point at you because of that?"
                call her_main("{size=-4}It was worth a try...{/size}", "annoyed", "narrow", "worried", "down")
                m "Try to remember this, Miss Granger. You can't rip me off that easily."
                call her_main("*Tzzzz*- I don't need your points anyway.", "angry", "base", "angry", "mid")
                g9 "You may leave now."
                call her_main("I will!{w} Good day, Sir!", "open", "closed", "angry", "mid")

                call her_walk(action="leave")

                call bld
                m "She might forget all about it in time."
                m "I can ask her again once I've trained her some more..."
                m "Maybe then she'll be persuaded more easily."

                $ her_mood += 6
                $ hermione_busy = True

                jump main_room


    elif her_whoring < 21:
        call her_main("Oh... My \"Quidditch equality movement\"?", "soft", "base", "base", "mid")
        m "That's the one."
        call her_main("It never really got off the ground...", "open", "base", "base", "R")
        call her_main("No pun intended...", "base", "closed", "base", "mid")
        m "(...)"
        call her_main("To be honest, I don't have that much time apart from my visits here and studying...", "open", "narrow", "worried", "down")
        call her_main("I might consider dropping it.", "base", "base", "base", "R")
        call her_main("Even though it would take away the immense pleasure of seeing Cho getting all worked up about it...", "grin", "base", "base", "mid")
        m "(...)"
        call her_main("There is something I'd like from you in return, [genie_name].{w=0.8} Or else I'll just continue with it!", "base", "narrow", "base", "mid_soft")
        m "Go on girl."
        m "Tell me what you want."
        m "What you really{w}, really want..."
        call her_main("Very well, [genie_name].", "soft", "base", "base", "R")
        call her_main("I'll tell you what I want!", "open", "closed", "base", "mid")
        call her_main("What I really, really want!", "grin", "narrow", "base", "mid_soft")
        g9 "{size=-4}Nice!{/size}"
        call her_main("I'd like a seat in the teacher stands, during the Quidditch matches..", "open", "closed", "base", "mid")
        m "Is that all?"
        call her_main("Oh, and a hundred points for Gryffindor...", "grin", "base", "base", "R")
        m "(...)"
        m "I'd say fifty would be more appropriate in this instance..."
        call her_main("Sir, it took a lot of effort to gather all those records of past Quidditch matches, throughout the whole history of Quidditch.", "open", "closed", "base", "mid")
        g4 "fifty points..."
        call her_main("(...)", "annoyed", "narrow", "angry", "R")
        call her_main("Very well then.", "soft", "closed", "base", "mid")
        m "Fifty points, to the Gryffindor house..."
        $ gryffindor += 50
        call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")

    else:
        call her_main("My what?", "open", "narrow", "base", "mid_soft")
        m "Your Quidditch movement."
        m "Regarding the male and female roles in Quidditch..."
        call her_main("Oh. I barely even remember that I did that.", "annoyed", "narrow", "base", "R_soft")
        m "So it wouldn't be an issue for you to drop it?"
        call her_main("I guess so...", "soft", "narrow", "worried", "down")
        call her_main("Although, if I were to drop it...", "open", "narrow", "base", "down")
        m "Yes?"
        call her_main("I want a seat in the teacher stands during Quidditch matches though!", "grin", "narrow", "base", "mid_soft")
        m "I'm sure that could be arranged..."
        call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")

    call her_main("[genie_name], may I ask.{w=0.6} What exactly were you and Cho talking about when I entered your office?", "open", "base", "base", "R")
    m "Oh. She just wanted my help with Quidditch."
    call her_main("*Pffff*-{w=0.4} Why doesn't it surprise me that she'd need your help with it.", "grin", "narrow", "base", "R_soft")
    call her_main("How else could she possibly win that stupid Quidditch cup...", "soft", "closed", "angry", "mid")
    m "I thought that cup was so important to you?"
    call her_main("I couldn't care less about it, [genie_name].", "open", "closed", "base", "mid")
    call her_main("The only cup that is worth winning is the {i}house cup{/i}.", "open", "narrow", "base", "R_soft")
    call her_main("They're completely different...", "annoyed", "base", "angry", "mid")
    m "Totally different..."

    if her_whoring < 18:
        call her_main("It's the most prestigious award one could earn for your school house!{w=0.6} The Quidditch cup is nothing in comparison...", "open", "closed", "base", "mid")
        call her_main("Why are students even allowed to play this silly sport at our School?", "annoyed", "narrow", "annoyed", "mid")

    if her_whoring < 8:
        call her_main("They're given the privilege of attending one of the most prestigious wizarding schools in the world...", "open", "narrow", "angry", "R")
        call her_main("And they're wasting their time with some silly sports game that will get them nowhere...", "open", "base", "angry", "mid")
        m "Yes. Because why enjoy yourself when you could study instead..."
        call her_main("Exactly!", "normal", "closed", "base", "mid")
        m "(She's so predictable.)"

    m "Well... The quidditch teams are none of your concern anymore..."
    m "You'll tell Cho that you are sorry about your previous interferences."
    call her_main("(...)", "annoyed", "base", "angry", "mid")
    m "And that the \"Quidditch equality movement\" will be...{w} \n\"no more.\""

    if her_whoring < 18:
        call her_main("Do I really have to do all that?", "upset", "base", "base", "R")
        m "If you want to keep on buying favours from me."
        call her_main("*Ugh*...{w=0.4} Very well, I guess...", "soft", "narrow", "worried", "down")
    else:
        call her_main("Sure, whatever...", "open", "narrow", "base", "R_soft")


    # Summon Cho
    g9 "Great!"
    g9 "Let's call her up here then..."
    call her_main("What? Now?", "clench", "wide", "base", "stare")

    # Hermione quickly gets dressed.
    if not hermione.is_worn("top") or not hermione.is_worn("bottom"):
        call her_main("Wait, she can't see me like this!", "disgust", "narrow", "worried", "down")

        hide screen hermione_main
        with d3
        pause .8

        m "(...)"

        $ hermione.wear("all")
        pause .5

    else:
        hide screen hermione_main
        hide screen bld1
        with d3
        pause .5

    # Cho enters the office.
    call cho_walk(580, "base", action="enter")

    call cho_main("Hello, Sir.{w=0.6} You've called for me?", "base", "base", "base", "mid", xpos="base", ypos="base")
    call her_main("", "normal", "closed", "base", "mid", xpos="450", ypos="base")
    call cho_main("Granger...", "soft", "narrow", "angry", "L")
    call her_main("Chang...", "annoyed", "narrow", "angry", "R")
    m "Go on, girl. Tell her."
    call cho_main("Tell me what?", "smile", "narrow", "angry", "mid")
    call her_main("...", "annoyed", "narrow", "base", "up")
    call her_main("About my \"Quidditch equality movement\"...", "normal", "closed", "base", "mid")
    call cho_main("Did our Professor finally convince you what a terrible idea it would be?", "soft", "narrow", "angry", "mid")
    m "Actually, I still think granting more people the ability to--"
    call cho_main("*Shhsh!* Professor!{w=0.6} I'd like to hear it from her.", "annoyed", "narrow", "angry", "mid")
    call cho_main("I'm going to enjoy this!", "horny", "narrow", "base", "L")
    call her_main("...", "annoyed", "base", "angry", "mid")
    call her_main("*Sigh*{w=0.6} I will end my movement, and I won't interfere with Quidditch again...", "open", "closed", "base", "mid") #[Looking bored]
    call cho_main("This is amazing! I feel as if it's my birthday!", "smile", "base", "base", "mid")
    call her_main("After all, Quidditch is a huge waste of everyone's time.{w=0.6} Including mine...", "soft", "narrow", "base", "R_soft") #[Still looking bored]
    call cho_main("You're just jealous that I'm better than you at something.", "smile", "narrow", "angry", "L")
    call her_main("I am not jealous!", "angry", "closed", "angry", "mid")
    m "You may go now, Miss Granger."
    call her_main("(...)", "annoyed", "base", "angry", "mid")
    call her_main("Until next time, Sir.", "normal", "closed", "base", "mid")
    call her_main("...", "annoyed", "narrow", "base", "R_soft")

    # Hermione leaves after glaring one last time at Cho.
    call her_walk("door", "base")
    pause .2
    call her_chibi("stand", "door", "base",flip=False)
    with d3
    pause .2

    call her_main("*glare*", "normal", "base", "angry", "mid", ypos="head", flip=False)
    # Add Cho glaring back with her 'head' image.

    call her_chibi("stand", "door", "base",flip=True)
    with d3
    pause .8

    call her_chibi("leave")
    with d3
    pause .5

    call cho_main("Thank you for getting her off my back, Professor.", "base", "base", "base", "mid")
    m "No problem."
    call cho_main("Now, if you'll excuse me. I'm expected back on the Quidditch pitch.", "open", "closed", "base", "mid")
    call cho_main("Just call me whenever I can be of service.", "soft", "narrow", "base", "mid")
    g9 "I will."
    call cho_main("Good day, Professor.", "smile", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "That went better than expected."

    # You can now summon Cho Chang to your office.
    stop music fadeout 1.0

    $ cho_unlocked = True
    $ achievement.unlock("unlockcho", True)
    call popup("{size=-4}You can now summon Cho into your office.{/size}", "Character unlocked!", "interface/icons/head/cho.webp")

    # End of Intro.
    $ hermione_busy = True
    $ cho_busy = True

    $ cho_intro.E3_complete = True

    jump main_room
