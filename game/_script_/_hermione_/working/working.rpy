
# Maid Job
label job_1:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph!*..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    show screen blkfade
    with d5

    # Setup
    call play_sound("equip_inventory")
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_maid)
    pause 2.5
    hide screen blkfade
    with d5

    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
    pause.8

    m "Off you go then..."

    call her_walk(action="leave")

    $ hermione_busy = True
    $ current_job = 1

    jump main_room

label maid_responses:
    $ payment = renpy.random.randint(10, 25)

    call her_walk(action="enter", xpos="mid", ypos="base")

    call her_main("", "base", "base", "base", "mid", xpos="right",ypos="base")
    pause.5

    menu:
        "\"How was your day?\"":
            if day_random <= 4:
                her "It was as normal a day of cleaning rooms could be."
                her "Although considering that I'm supposed to be in class during the day I guess it's not that normal."
                m "Don't worry [hermione_name], you'll get your points."
                m "Just think of how happy your friends will be when they win the house cup this year."
                her "I suppose..."
                m "Twenty points to Gryffindor"
            elif day_random <= 8:
                call her_main("Do I really have to keep doing this?", "normal", "narrow", "base", "R_soft")
                m "What do you mean, [hermione_name]?"
                call her_main("It's so degrading... I have to clean other students rooms!", "open", "narrow", "worried", "down")
                m "You can stop any time."
                call her_main("I can?", "soft", "narrow", "worried", "mid_soft")
                g9 "Certainly, I'll just get one of those Slytherin floozies that you are always on about."
                m "I'm sure that they'd jump at the chance to make some points for their house."
                m "They'd probably even do it for next to nothing, if not free."
                call her_main("Fine, I get your point. It's just, surely there are other ways for you to earn money [genie_name]?", "upset", "closed", "base", "mid")
                call her_main("I mean you're the school headmaster, can't you just file some reports and get paid by the ministry?", "base", "base", "base", "R")
                m "I can, it's just not as enjoyable."
                call her_main("*Hmph*... Can I at least get my points now?", "angry", "closed", "angry", "mid")
                m "Certainly, twenty points to Gryffindor."
            else:
                call her_main("I think you need to start enforcing harsher punishment for sexual harassment.", "mad", "base", "angry", "mid")
                call her_main("*Hmph*... Can I at least get my points now?", "angry", "closed", "angry", "mid")
                m "Certainly, twenty points to Gryffindor."
        "-Dismiss her-":
            call her_main("Here's your payment.", "base", "base", "base", "mid")
            ">You receive {number=payment} gold coins."
            m "Well done [hermione_name], twenty points to Gryffindor."

    call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")

    $ gryffindor+= 20
    $ game.gold += payment

    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)

    $ hermione_busy = True
    $ current_job = 0

    jump main_room_menu

# Barmaid Job
label job_2:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph*!..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    show screen blkfade
    with d5
    # Setup
    call play_sound("equip_inventory")
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_maid)
    pause 2.5
    hide screen blkfade
    with d5

    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
    pause.8

    m "Off you go then..."

    call her_walk(action="leave")

    $ hermione_busy = True
    $ current_job = 2

    jump main_room

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)

    call her_walk(action="enter", xpos="mid", ypos="base")

    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base")
    pause.5

    menu:
        "\"How was your day?\"":
            her "Fine..."
            m "Anything unusual happen?"
            her "Not really, I just served people drinks."
            m "Well in that case twenty points to Gryffindor."
            her "Thank you, [genie_name], here's your payment."
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive {number=payment} gold coins."
            m "Well done [hermione_name], twenty points to Gryffindor."

    her "Thank you, [genie_name]."

    $ gryffindor+= 20
    $ game.gold += payment

    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)

    $ hermione_busy = True
    $ current_job = 0
    jump main_room_menu

# Gryffindor Cheerleader Job (Needs outfit)
label job_3:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph*!..."
    elif her_whoring <= 15:
        call her_main("Yes, [genie_name]...", "normal", "base", "base", "R")
    else:
        call her_main("As you wish, [genie_name].", "open", "base", "base", "mid")

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    if hg_cheer_g_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_g_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_g_ITEM)
    hide screen blkfade
    with d5

    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
    pause.8

    g9 "You look great!"
    call her_main("Thank you...", "base", "happyCl", "base", "mid")
    m "Off you go then..."

    call her_walk(action="leave")

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 3

    jump main_room

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)

    call her_walk(action="enter", xpos="mid", ypos="base")

    if hg_cheer_g_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_g_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_g_ITEM)

    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base")
    pause.5

    menu:
        "\"How was your day?\"":
            if day_random <= 2:
                call her_main("It was good [genie_name], I think that the team morale has really started to go up.", "base", "base", "base", "mid")
                m "How so?"
                call her_main("Well, since I've started they seem to have improved their tactics.", "open", "base", "base", "mid")
                call her_main("They also seem much happier. Harry is always looking at me with a smile on his face.", "base", "base", "base", "mid")
                m "And does he look at you a lot?"
                call her_main("Of course he does, we're good friends.", "open", "base", "base", "mid")
                m "\"I'm sure that must be the reason...\""
                call her_main("Well here's the money, [genie_name].", "base", "base", "base", "mid")
                ">You receive [payment] gold coins."
                m "Well done, [hermione_name], twenty points to Gryffindor."
            elif day_random >= 3 and day_random <= 5:
                call her_main("Tiring. This cheering thing really is quite exhausting.", "open", "base", "worried", "mid")
                m "Anything interesting happen?"
                call her_main("Not unless you count me almost dropping my pom pom.", "normal", "base", "base", "mid")
                m "I don't... Well, did they pay you?"
                call her_main("Of course, here you are [genie_name].", "open", "base", "base", "mid")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], twenty points to Gryffindor."
            elif day_random >= 6 and day_random <= 8:
                call her_main("Very well thank you, all the boys said that I helped keep their spirits up.", "open", "base", "base", "mid")
                m "{size=-5}I'm sure that wasn't the only thing you've helped stay up...{/size}"
                call her_main("What was that [genie_name]?", "open", "squint", "base", "mid")
                m "I was just saying that I'm sure you did a stand up job."
                call her_main("I think so...", "base", "happyCl", "base", "mid")
                m "Well, did they pay you for raising their \"spirits\"?"
                call her_main("Of course they did.", "open", "base", "base", "mid")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], twenty points to Gryffindor."
            elif day_random >=9 and her_reputation <= 15:
                m "You seem very chipper today."
                call her_main("Of course I am, we won!", "base", "base", "base", "mid")
                m "Won?"
                call her_main("We won! We beat Slytherin in a practice match.", "smile", "happyCl", "base", "mid")
                m "You seem a little bit overexcited for just a practice match."
                call her_main("Well it was such a great game. Not to mention that we got to rub it in those Slytherin students faces afterwards.", "smile", "base", "base", "R")
                g9 "Well I'm glad that you are enjoying your work."
                call her_main("I am [genie_name]. Given that most of the \"work\" I've done to help my house is kept private, it feels good to be able to do something public once.", "open", "base", "base", "mid")
                m "Not to mention you get paid for it..."
                call her_main("Oh, right, Here you are...", "soft", "base", "base", "R")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], twenty points to Gryffindor."
            else:
                call her_main("We won! We managed to beat Slytherin.", "base", "base", "base", "mid")
                m "That must have been very exhilarating. I'm sure your cheering gave the extra motivation needed to win."
                call her_main("I think it did [genie_name]. They were all very excited to receive their reward for winning the game.", "base", "happyCl", "base", "mid")

                menu:
                    "-Reward?-":
                        m "What reward did you promise them?"
                        call her_main("Well I was quite keen to ensure our victory against Slytherin that I may have promised that I would give each of them a blowjob if they won.", "grin", "base", "base", "R")
                        m "You gave every team member a blowjob after the game?"
                        call her_main("And the water boy...", "smile", "narrow", "base", "mid_soft")
                        m "How did you even manage that? Did have to crawl around the locker room on your knees?"
                        call her_main("Of course not, they all patiently waited on their turn...", "scream", "closed", "angry", "mid")
                        m "Who doesn't love a queue..."
                        m "So they queued up... And then?"
                        call her_main("Well I did what I said I would, I'm not the kind of person to lie am I?", "annoyed", "base", "worried", "R")
                        call her_main("So, I gave them the reward I promised... And surely you of all people would know how a blowjob works.", "annoyed", "happy", "base", "R")
                        m "That's not quite what I meant."
                        m "You just look rather..."
                        m "Clean, that's all."
                        call her_main("Oh, well...", "base", "narrow", "worried", "down",cheeks="blush")
                        call her_main("I didn't want to make a mess", "soft", "narrow", "base", "down",cheeks="blush")
                        call her_main("Anyhow, I'm glad I did it. I can't wait to rub it in Astoria's face tomorrow...", "smile", "base", "base", "mid")
                        m "I'm glad you think it was worth it. Did they pay you?"
                    "-Okay-":
                        m "I'm sure it was worth it. Did they pay you?"

                her "Of course they did [genie_name], here you are."
                m "Well done [hermione_name], twenty points to Gryffindor."

        "-Dismiss her-":
            call her_main("Here's your payment [genie_name].", "soft", "base", "base", "R")
            m "Well done [hermione_name], twenty points to Gryffindor."

    call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
    ">You receive [payment] gold coins."
    $ gryffindor+= 20
    $ game.gold += payment

    call her_walk(action="leave")

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0
    jump main_room_menu



# Slytherin Cheerleader Job
label job_4:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph*!..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes, [genie_name]..."
    else:
        her "As you wish, [genie_name]."

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    if hg_cheer_s_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_s_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_s_ITEM)
    hide screen blkfade
    with d5


    call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base",trans=fade)
    pause.8

    g4 "You look incredible!"
    call her_main("Thank you...", "base", "happyCl", "base", "mid")
    m "Off you go then..."

    call her_walk(action="leave")

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 4

    jump main_room

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)

    call her_walk(action="enter", xpos="mid", ypos="base")

    if hg_cheer_s_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_s_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_s_ITEM)

    if day_random >=9 and her_reputation > 15:
        $ uni_sperm = True
        call her_main("", "base", "narrow", "base", "up",xpos="right",ypos="base")
    else:
        call her_main("", "base", "base", "base", "mid",xpos="right",ypos="base")
    pause.5

    menu:
        "-Ask her about her day-":
            if day_random <= 2:
                m "How was your day today [hermione_name]?"
                call her_main("Exhausting... Those Slytherin pigs insisted that I cheer for their entire practice session.", "open", "closed", "angry", "mid")
                her "They were hardly playing the game by the end. They were just standing there watching me."
                m "Well what was your routine?"
                call her_main("Mostly star jumps while I cheered \"Go Slytherin!\".", "annoyed", "squint", "angry", "mid")
                m "So you were just jumping up and down? That doesn't seem like a very intricate cheer."
                call her_main("It isn't but it's what they insisted I do.", "annoyed", "narrow", "angry", "R")
                m "Well it definitely sounds like you earned your points."
                m "Thirty points to Gryffindor."
            elif day_random >= 3 and day_random <= 5:
                m "How was your day today [hermione_name]?"
                call her_main("Uneventful. I completed my routine and then went back to my room...", "open", "squint", "base", "mid")
                m "You didn't talk to anyone?"
                call her_main("I make a point of trying to avoid Slytherin student as best I can. ", "annoyed", "narrow", "angry", "R")
                m "Are they really that unbearable?"
                call her_main("Yes...", "open", "closed", "angry", "mid")
                m "Well, you earned your points."
                m "Thirty points to Gryffindor."
            elif day_random >= 6 and day_random <= 8:
                m "Hello [hermione_name]."
                call her_main("Hello [genie_name].", "normal", "base", "base", "mid")
                m "How did everything go today?"
                call her_main("Very well. In fact I think I might be doing too well.", "annoyed", "base", "worried", "R")
                m "How so?"
                call her_main("I think that my cheering is having too much of an positive effect.", "open", "base", "worried", "mid")
                call her_main("I'm not sure that I want the Slytherin team to improve, let alone because of me...", "open", "base", "worried", "R")
                m "Just think about how you're helping your house in other ways."
                call her_main("I suppose you're right [genie_name].", "open", "base", "base", "mid")
                m "Of course I am... Now, did they pay you?"
                call her_main("Yes [genie_name].", "base", "base", "base", "mid")
                m "Well done [hermione_name], twenty points to Gryffindor."
            elif day_random >=9 and her_reputation > 15:
                call her_main("[genie_name], something must be done about those Slytherin boys...", "open", "closed", "angry", "mid")
                call her_main("It's bad enough that I have to cheer for them but they are being a little bit touchy.", "annoyed", "narrow", "angry", "R")
                m "Touchy?"
                call her_main("Yes, they keep groping me. It's highly inappropriate and it interrupts my routine.", "scream", "closed", "angry", "mid")
                m "You kept dancing while they groped you?"
                call her_main("Of course, I'm there to complete a job. I'm not getting distracted just because of a few boys.", "open", "closed", "angry", "mid")
                m "Well what would you have me do?"
                call her_main("Speak to Professor Snape, tell him to chastise them. They'll listen to him...", "angry", "base", "angry", "mid")
                m "Very well, I'll speak to him. Although I'm not sure it will have the effect you're hoping for."
                call her_main("It better, otherwise I wont put my full effort into this...", "normal", "squint", "angry", "mid")
                m "{size=-5}I'm sure that'll show them.{/size}"
                call her_main("What was that [genie_name]?", "open", "squint", "base", "mid")
                m "Nothing [hermione_name], I'll speak to Professor Snape tonight..."
            else:#Comes back with cum on her
                m "What the hell happened to you?"
                call her_main("I did my job [genie_name].", "angry", "narrow", "base", "down")
                m "What are you talking about? You were supposed to be a cheerleader."
                m "You know, cheering..."
                m "And all that."
                call her_main("I am [genie_name]. I just performed a different type of cheer today.", "soft", "narrow", "annoyed", "up")
                m "And by that you mean jerking off the entire Slytherin team?"
                call her_main("Well that's not how it started. I was initially just giving them a bit of a dance in the locker room...", "angry", "narrow", "base", "down")
                her "And one thing led to another."
                m "Fine, I don't want to hear it. How much did they pay you for this \"cheering\"?"
                call her_main("Pay me?", "silly", "narrow", "base", "dead")
                m "You are supposed to be paid for this [hermione_name]."
                call her_main("Oh... I must have forgotten. Sorry [genie_name]", "base", "base", "base", "R",cheeks="blush")
                m "Fine, but you aren't getting any points."
                call her_main("Of course [genie_name]. Will that be all?", "base", "base", "base", "mid")
                m "Yes, you're free to go now."
                call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")
                jump end_her_working_no_payment
        "-Dismiss her-":
            call her_main("Here's your payment.", "open", "base", "base", "mid")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], thirty points to Gryffindor."

    call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")
    ">You receive [payment] gold coins."
    $ gryffindor+= 30
    $ game.gold += payment

    label end_her_working_no_payment:

    call her_walk(action="leave")

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0
    $ uni_sperm = False
    jump main_room_menu


#Send Hermione to work, promoting the card game.

label job_5:
    $ menu_x = 0.5 #Menu position is back to default. (Center).

    if first_time_cardgame_work:
        call her_main("But... why do you want me to help them promote their shop?", "annoyed", "closed", "base", "mid")
        g9 "That is my business."
        call her_main("What do you want me to tell them then?", "open", "narrow", "worried", "mid_soft")
        m "Just ask them if they have a need for any help promoting their card game."
        g9 "If they're as business minded as I assume then there's no way they'd say no."
        g9 "And make sure you ask them for payment."
        call her_main("Fine...", "base", "closed", "base", "mid")
        call her_main("I'll see you tonight.", "open", "base", "base", "mid")
        m "Forgetting something?"
        call her_main("... Just hand it over.", "disgust", "narrow", "worried", "down", cheeks="blush")

        if her_whoring < 19:
            # Failstate
            call her_main("I know I said I'd help them but you want me to wear... this?", "open", "base", "angry", "mid")
            m "Of course, is that going to be a problem?"
            call her_main("Yes!", "angry", "base", "angry", "mid")
            her "I can't believe you've done this."
            call her_main("Did you have this commissioned?", "open", "squint", "angry", "mid")
            m "The twins sold it to me..."
            her "Of course they did..."
            m "So it's a...{w=0.4}{nw}"
            call her_main("Of course it's a no", "shock", "base", "angry", "mid")
            $ her_mood += 5
            jump working_menu

        $ first_time_cardgame_work = False
        $random_choice = renpy.random.randint(0,3)

        if random_choice == 0:
            call her_main("Why are the cards placed like that?", "mad", "narrow", "worried", "down")
            call her_main("...", "normal", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("Fine...", "open", "narrow", "base", "down", cheeks="blush")
        elif random_choice == 1:
            call her_main("...", "normal", "base", "worried", "mid", cheeks="blush")
            call her_main("Well, if it stops you from deducting those points.", "open", "happyCl", "worried", "mid", cheeks="blush")
            call her_main("I'll do it.", "base", "wink", "base", "mid")
        elif random_choice == 2:
            call her_main("It's a bit revealing... but I'll do it.","smile","happy", cheeks="blush")
            call her_main("For Gryffindor house obviously!", "open", "happyCl", "base", "mid", cheeks="blush")
        else:
            call her_main("That doesn't leave a lot to the imagination...", "smile", "happy", "base", "mid")
            call her_main("At least the straps should cover my nipples...", "open", "wink", "base", "mid")
            call her_main("I'll do it...","normal","happy", cheeks="blush")


    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5

    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_poker)

    hide screen blkfade
    with d5
    g9 "Looking great!"
    call her_main("Thank you...","open","happy", cheeks="blush")
    m "Off you go then..."

    call her_walk(action="leave")
    $ hermione_busy = True
    $ current_job = 5

    jump main_room

label hermione_helping_selling_cards:
    $ current_job = 0
    $ random_choice = renpy.random.randint(1,4)

    if her_shop_help_first:
        $ her_shop_help_first = False
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Good...", "normal", "happy", "base", "mid")
        call her_main("Still not that comfortable wearing the outfit you provided though so I just stood behind the shop counter today.", "open", "closed", "base", "mid")
        call her_main("Apparently we sold a lot more items than usual though.","base","happy", cheeks="blush")
        g9 "Great news, I bet the twins are ecstatic."
        call her_main("Indeed, It was nice seeing them in such high spirits.", "open", "happyCl", "base", "mid", cheeks="blush")
        call her_main("Whilst I might not agree with all their business methods I think they might become great salesmen some day.", "base", "happy", "base", "mid")
        g9 "Seems to me like they are already..."
        m "So, how come you had such a surge in new customers?"
        call her_main("No idea, maybe the card game got more people interested in browsing the rest of their stock.", "annoyed", "happy", "base", "R")
        call her_main("They actually had some problems with people stealing things before I started working there though.", "open", "closed", "base", "mid")
        m "And this stopped after you started working there?"
        call her_main("Well, probably not because of it. They put in some anti thieving measures.", "base", "base", "base", "mid")
        m "Patent pending?"
        call her_main("It's pretty clever actually, they put up a mirror behind the counter so that when I have to turn around and grab something I'll be able to see if anyone takes anything.", "smile", "wink", "base", "mid")
        g9 "\"Yeah, I'm sure that's why they put the mirror there...\""
        m "Sounds like you're doing a great job."
        call her_main("Thanks!","open","happy", cheeks="blush")
        call her_main("Here's your payment.", "open", "base", "base", "mid")
        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        m "Well done [hermione_name], fifteen points to Gryffindor."
        $ gryffindor += 15

    if random_choice == 1:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("It was fine, the outfit is a bit chilly though.", "normal", "happy", "base", "mid_soft")
        m "So, no other complications?"
        call her_main("Well...", "soft", "narrow", "worried", "down", cheeks="blush")
        call her_main("The twins asked me to give out some free promotional starter packs.", "open", "happy", "base", "mid", cheeks="blush")
        m "Yes?"
        m "Sounds like a great way to get people into playing..."
        call her_main("Well, I didn't have anywhere to store the packs as you could imagine.", "base", "narrow", "worried", "down", cheeks="blush")
        call her_main("So I had to resort to putting them behind my suspenders and the top of my stockings...", "open", "closed", "base", "mid", cheeks="blush")
        call her_main("And one customer got a bit...", "normal", "closed", "base", "mid", cheeks="blush")
        call her_main("Touchy.", "base", "narrow", "annoyed", "up", cheeks="blush")
        m "I see..."
        call her_main("I did get a bit agitated at one point actually...", "open", "closed", "base", "mid", cheeks="blush")
        g4 "They didn't fire you did they?"
        call her_main("No!", "mad", "wide", "base", "mid")
        call her_main("The customer was quite apologetic actually and bought a bunch of things.", "smile", "closed", "angry", "mid")
        call her_main("The twins obviously took the credit for getting such a big sale and seemed rather pleased with themselves.", "crooked_smile", "narrow", "annoyed", "mid")
        call her_main("I'm fine with them believing they had anything to do with it though.", "smile", "closed", "base", "mid")
        m "How noble of you..."
        call her_main("Here's your payment.", "open", "base", "base", "mid")
        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        m "Well done [hermione_name], twenty points to Gryffindor."
        $ gryffindor += 20
    elif random_choice == 2:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Awful...", "normal", "narrow", "worried", "down")
        m "Really, why is that?"
        call her_main("Well, I'm not actually angry...", "open", "base", "base", "mid")
        call her_main("Just a bit annoyed, that's all.", "annoyed", "closed", "base", "mid")
        m "With?"
        call her_main("Myself...", "open", "base", "worried", "R", cheeks="blush")
        call her_main("We've set up a practice day where you get to borrow a deck of cards to get more people into the game.", "normal", "happy", "base", "mid")
        g9 "Sounds like a good idea, get people invested."
        call her_main("Well, that was fine and all until the amount of new people interested started to slow down.", "open", "narrow", "worried", "down")
        m "I see, so I expect the responsibility fell on you as you're the one meant to promote the game?"
        call her_main("Yes... I thought it was a great idea so if it ended up not working out then it would look very bad on my part.", "normal", "closed", "base", "mid")
        m "So, you had to stop the practice sessions?"
        call her_main("No, that's not why I'm annoyed...", "annoyed", "happy", "base", "R")
        call her_main("In my haste to find a solution I thought it would be a great idea to play a few rounds of strip cards to get more people interested.", "open", "narrow", "base", "down", cheeks="blush")
        call her_main("...", "angry", "closed", "angry", "mid", cheeks="blush")
        call her_main("I've played enough not to be beaten by a new player I thought.", "mad", "narrow", "angry", "R", cheeks="blush")
        g9 "Of course, you've played against me after all..."
        call her_main("...", "base", "base", "angry", "mid")
        m "Sorry, go on."
        call her_main("Well, I managed to get a bunch of people into the card game so practice day is still on the schedule.", "annoyed", "closed", "angry", "mid")
        g9 "That's good!"
        call her_main("Though I might reconsider the whole strip card idea...", "angry", "narrow", "worried", "down", cheeks="blush")
        call her_main("I lost pretty quickly...", "normal", "closed", "base", "mid", cheeks="blush")
        call her_main("It turned out they had been cheating the whole time...", "normal", "base", "base", "mid", cheeks="blush")
        g9 "Well, cheaters never prosper..."
        call her_main("That's not true in this case... they prospered alright.", "open", "happy", "base", "R", cheeks="blush")
        call her_main("In any case, they seemed... happy, they bought a bunch of things so that makes me...", "normal", "base", "base", "mid")
        call her_main("Happy as well...", "angry", "closed", "base", "mid", cheeks="blush")
        g9 "A job well done then, I bet the twins are very grateful for your contribution."
        call her_main("Thank you.", "annoyed", "happyCl", "base", "mid", cheeks="blush")
        call her_main("Anyway...", "base", "base", "base", "mid")
        call her_main("Here's your payment.", "open", "base", "base", "mid")
        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        m "Well done [hermione_name], twenty-five points to Gryffindor."
        $ gryffindor += 25
    elif random_choice == 3:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Great, they held a card game tournament today.", "base", "base", "base", "mid")
        g4 "Wait, a tournament? How come I wasn't invited?"
        call her_main("It was students only obviously...", "open", "happy", "base", "R")
        m "Oh... of course."
        call her_main("There were way more participants than I expected seeing that there was an entry fee.", "base", "closed", "base", "mid", cheeks="blush")
        m "Must've been a great prize pool then..."
        call her_main("That's the weird thing. The prize pool only amounted do about half of the total entry fee amount.", "open", "base", "base", "mid")
        call her_main("Apparently... someone had gone around spreading the rumour that the winner would...", "normal", "narrow", "worried", "down")
        call her_main("Get a go with me if they won the tournament...", "annoyed", "narrow", "base", "down", cheeks="blush")
        g9 "And did they?"
        call her_main("Of course that was never on the table...", "base", "base", "angry", "mid", cheeks="blush")
        g9 "On a desk then?"
        call her_main("Well...", "annoyed", "base", "base", "mid", cheeks="blush")
        call her_main("The winner did end up standing there with such an expectant look on his face after everyone had left...", "open", "narrow", "worried", "down", cheeks="blush")
        m "..."
        call her_main("So I told him that whatever he was expecting it wasn't happening.", "angry", "narrow", "angry", "R", cheeks="blush")
        call her_main("He seemed so disheartened so I felt a bit bad about the whole thing...", "open", "closed", "angry", "mid")
        call her_main("So, since I didn't want to bring his feeling of victory down I figured since some students had spread the rumour they'd assume the worst anyway...", "open", "base", "angry", "mid", cheeks="blush")
        call her_main("So I put my hand down his pants and fiddled around a bit whilst letting the guy get a peek behind my suspenders.", "grin", "base", "angry", "mid", cheeks="blush")
        g9 "Good on you!"
        call her_main("You don't think that was a bit much?", "annoyed", "base", "base", "mid", cheeks="blush")
        g9 "No! That was the right thing to do in that situation."
        m "There wasn't a lot you could do about the rumours even if nothing had happened he'd probably lie about it anyway."
        g9 "You most likely ended up making that guys night."
        call her_main("More like month... seeing how much he...", "open", "narrow", "worried", "down", cheeks="blush")
        call her_main("Anyway...", "normal", "base", "base", "mid")
        call her_main("glad you agree.", "base", "happy", "base", "mid_soft")
        call her_main("Here's your payment.", "open", "base", "base", "mid")
        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        m "Well done [hermione_name], twenty-five points to Gryffindor."
        $ gryffindor += 25
    else:
        $ hermione.set_cum(hair="light")
        call her_main("", "cum", "narrow", "base", "dead")
        m "What happened to you?"
        call her_main("What do you mean...", "open", "narrow", "worried", "mid_soft")
        call her_main("Oh, that...", "base", "narrow", "worried", "down", cheeks="blush")
        m "Yes, that..."
        call her_main("There's a good explanation for this.", "normal", "narrow", "base", "down", cheeks="blush")
        m "..."
        m "Go on."
        call her_main("Oh, sorry... Well, I was trying out a new sales tactic...", "open", "happy", "base", "R", cheeks="blush")
        m "Something the twins came up with I assume?"
        call her_main("No, I read about it in one of their books actually.", "grin", "happy", "base", "mid_soft")
        call her_main("Much like how you should always put the most lucrative cheap items at the counter to make the customer...", "open", "base", "base", "mid")
        g4 "Get on with it."
        call her_main("Fine...", "annoyed", "narrow", "base", "R_soft", cheeks="blush")
        call her_main("I read that by putting the customer in a state of peace and happiness it would make them more susceptible to making hasty decisions.", "smile", "happyCl", "base", "mid", cheeks="blush")
        g9 "Didn't think you'd be interested in such... unorthodox sales tactics..."
        call her_main("I was curious to see if it would work more than anything else.", "base", "closed", "base", "mid", cheeks="blush")
        call her_main("I tried it out to test the legitimacy of the claims in that book of theirs...", "open", "base", "base", "mid")
        m "of course..."
        m "And how many times did you test this... theory of yours."
        call her_main("There's no conclusion to be made by just testing a theory once [genie_name].", "normal", "closed", "angry", "mid")
        call her_main("Anyway...", "open", "base", "base", "mid")
        call her_main("Here's your payment.", "open", "base", "base", "mid")
        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        m "Well done [hermione_name], thirty points to Gryffindor."
        $ gryffindor += 30

    her "Good night, sir."
    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)
    $ hermione.set_cum(None)
    jump main_room_menu
