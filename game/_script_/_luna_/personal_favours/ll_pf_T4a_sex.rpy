
label ll_pf_sex:
    # Common start label

    $ ll_pf_sex.start()

    label end_luna_sex_event:

    if lun_whoring < 12:
        $ lun_whoring += 1

    jump end_luna_event

label ll_pf_sex_T1_intro:
    # Luna and Genie have sex by the lake

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    call lun_walk("mid", action="enter")

    if daytime:
        call lun_main("Good morning, [lun_genie_name]!","base","happyCl","sad","mid",cheeks="blush", xpos="mid" , ypos="base")
    else:
        call lun_main("Good evening, [lun_genie_name]!","base","happyCl","sad","mid",cheeks="blush", xpos="mid" , ypos="base")

    g9 "Miss Lovegood!{w=0.3} Here to surprise me again?"

    call lun_main("I found a cure, [lun_genie_name]!","base","happyCl","base","mid")
    call lun_main("A way for both of us to get rid of our wrackspurts at once!","base","wide","base","mid")
    g9 "You don't say!"
    m "[lun_name], you weren't the only one thinking of something ingenious to get rid of those nasty beasts!"
    g9 "I could teach you a thing or two!{w} After you've shown me your suggestion..."
    call lun_main("That's very exciting, don't you think? We can finally get rid of this scourge once and for all!","base","happyCl","base","mid")
    call lun_main("Everyone deserves to hear about it!","base","happyCl","base","mid")

    m "Why don't you fill me in first... What's your solution?"
    call lun_main("Of course, Sir...{w=0.3} But you'd have to...","open","wink","sad","mid")
    call lun_main("Sir could you please...{w=0.3} follow me?","base","wink","sad","R")
    m "Follow you? To where?"
    call lun_main("Let's find somewhere the wrackspurts won't bother anyone.","base","base","sad","mid")
    m "Hmm...{w=0.3} A desolate and quiet place would be perfect..."
    call lun_main("I can give you a tour of the school while we're at it!","base","wink","base","mid")
    call lun_main("And once we've found a spot you can tell me about your ideas!","base","wink","base","mid")
    g9 "Sounds like a plan! Let's go!"
    call lun_main("Great! Please follow me, Sir...","base","happyCl","sad","mid")

    # Roll out...
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base")
    hide screen bld1
    with d3

    call lun_walk(action="leave")

    call gen_walk(action="leave")

    show screen blkfade
    with d3

    ">You and Luna gently meander around the grounds together, all the while Luna happily explains its history."
    call lun_main("And this is the school library...","open","closed","base","mid")
    m "This place is huge! We could definitely find somewhere to do it in here!"
    call lun_main("I wouldn't recommend it... If we accidentally get cum on any of the books they'll probably attack us...","open","angry","sad","downL")
    m "(Is she being serious?)"
    m "Well, where do you suggest?"
    call lun_main("hmmm, we need somewhere we don't have to worry about being found...","pout","seductive","sad","down")
    call lun_main("And also somewhere the wrackspurts we expel won't bother anyone...","pout","angry","sad","downL")
    call lun_main("...","pout","closed","sad","mid")
    call lun_main("I know, let's go to the lake! Wrackspurts hate cold water!","open","wide","base","mid")
    m "They do?"
    call lun_main("Of course! Just think about how much a cold shower gets rid of them.","base","happyCl","mad","mid")
    m "You're a clever one."
    call lun_main("Thank you, [lun_genie_name]!","base","happyCl","base","mid")

    call ll_pf_sex_T1_lake_sex

    jump end_luna_event


label ll_pf_sex_T1_E1:
    # Luna and Genie have sex by the lake again

    g9 "Miss Lovegood! Would you like me to teach you about dispelling those wacky wrackspurts again?"
    call lun_main("I'd love to, [lun_genie_name].","soft","seductive","base","mid")
    g9 "Splendid!"
    m "Let's go for a trip to the lake again, shall we?"
    call lun_main("Of course! [lun_genie_name]!","base","happyCl","mad","mid")

    call ll_pf_sex_T1_lake_sex

    jump end_luna_event


label ll_pf_sex_T1_E2:
    # Luna and Genie have sex in the office when someone walks in
    # This event should be repeatable to see all variations

    m "How are you feeling today, [lun_name]?"
    call lun_main("Happier now that I'm in here!","base","happyCl","base","mid")
    m "Fantastic... Now, would you be interested in expelling a few more wookspoons together?"
    call lun_main("{b}Together{/b}? You mean...","base","seductive","sad","mid", cheeks="blush")
    call lun_main("Oh, thank you, thank you, thank you, [lun_genie_name]!","base","happyCl","sad","mid", cheeks="blush")

    call hide_characters
    show screen blkfade
    with d5

    ">Before you can say anything else, Luna throws her clothes to the floor and starts desperately thrusting her ass towards you."
    m "Gods, you're a needy little whore, aren't you?"
    lun "{i}yes{/i}..."
    m "Mmmm"

    $ lun_cg_path         = "images/CG/luna_fucking/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"blank.webp"
    $ lun_cg_dick         = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0

    ">Tired of talking, you decide to end the poor girl's suffering by slamming into her needy little fuckhole."

    $ lunCG(pupil='up', eye='wide', mouth='open_tongue', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', overlay='fade', tears='blank', body='base')
    show screen luncg

    hide screen blkfade
    with d5

    lun "{size=+10}{heart}!!!{heart}{/size}"
    m "That's it you little slut!"
    $ lunCG('open', 'furious', '', 'ahegao')
    lun "{size=-4}{heart}wow...{heart}{/size}"
    $ lunCG('base', 'angry', 'base', 'up')
    ">She starts grinding her hips against you immediately, desperate for as much stimulation as she can get."
    m "Ugh... steady on there, [lun_name], we've only just started!"
    $ lunCG('open', 'seductive', 'sad', 'dl')
    lun "{heart}a-ah... I can't... [lun_genie_name]... it's just... too... {heart}{b}goood{/b}...{heart}"
    $ lunCG('open_tongue', 'furious', '', 'up')
    ">Not content to just stand there, you start thrusting back into Luna's tight pussy."
    $ lunCG(pupil='ahegao', eye='seductive', mouth='open_tongue', extra_1='speed')
    lun "{heart}ah...{heart}the wrackspurts...{heart} they're going...{heart}aaaahhh..."
    m "I already told you-- *Argh*... They're not real!"
    $ lunCG('open', 'wide', '', 'dr')
    lun "Ugh... I can see... them... ah...{heart}{heart} with my own two... eyes..."
    $ lunCG('base', 'seductive', '', 'left')
    lun "Can't you see them? The red mist..."
    $ lunCG('base', 'tired', '', 'dl')
    lun "There's so many... You should be able to almost... ah... make them out..."
    m "..."
    m "(Am I going crazy?)"

    call play_sound("knocking")
    "*knock-knock-knock*"

    m "Crap!"
    $ lunCG('base', 'wink', 'base', 'left')
    lun "Ah... who do you... think it is?"
    m "Umm... It's probably--"

    show screen blkfade
    with d5

    $ random_number = renpy.random.randint(1, 10)

    menu:
        "\"I have no clue...\"" if astoria_unlocked or tonks_unlocked:
            # Randomly select a visitor

            if random_number in [1,2,3] and astoria_unlocked and ag_st_imperio.counter > 0:
                # Astoria
                if "astoria" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("astoria")
                    call ll_pf_sex_T1_ast_1
                else:
                    call ll_pf_sex_T1_ast_2

            elif random_number in [3,4,5] and tonks_unlocked:
                # Tonks
                if "tonks" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("tonks")
                    call ll_pf_sex_T1_ton_1
                else:
                    call ll_pf_sex_T1_ton_2

            else:
                # Hermione
                if "hermione" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("hermione")
                    call ll_pf_sex_T1_her_1
                else:
                    call ll_pf_sex_T1_her_2

        "\"Hermione maybe?\"" if game_difficulty <= 2:
            # Hermione
            if "hermione" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("hermione")
                call ll_pf_sex_T1_her_1

        "\"Astoria, that sadist!\"" if game_difficulty <= 2 and astoria_unlocked and ag_st_imperio.counter > 0:
            # Astoria
            if "astoria" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("astoria")
                call ll_pf_sex_T1_ast_1
            else:
                call ll_pf_sex_T1_ast_2

        "\"Tonks, your teacher...\"" if game_difficulty <= 2 and tonks_unlocked:
            # Tonks
            if "tonks" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("tonks")
                call ll_pf_sex_T1_ton_1
            else:
                call ll_pf_sex_T1_ton_2

    jump end_luna_sex_event


label ll_pf_sex_T1_E3:
    # Luna and Genie have sex in her bedroom

    m "Mmmm, you know, I think you might be on to something with these rookiesports..."
    m "I haven't been able to get that tight little pussy of yours out of my mind!"
    call lun_main("Really?","soft","base","sad","mid")
    call lun_main("For you to think about it too...","pout","angry","sad","R")
    call lun_main("They must truly be out of control...","soft","wide","sad","down")
    m "Mind giving me a hand getting rid of them?"
    call lun_main("Of course!","open","wide","sad","mid")
    call lun_main("I mean... No! I don't mind...","base","annoyed","sad","R", cheeks='blush')
    call lun_main("Can we please... just...","base","seductive","sad","mid")
    call lun_main("They've been bothering me as well...","base","seductive","sad","down")
    m "Well, in that case... why don't you bend over so we can get to work?"
    call lun_main("Oh um... about that...","soft","annoyed","sad","mid")
    m "Is something wrong?"
    call lun_main("No! It's not that I don't want to do it...","open","wide","base","mid")
    call lun_main("It's just this office has so many in here already...","soft","angry","sad","down")
    call lun_main("I don't think there's any more room for them...","soft","base","sad","R")
    m "So you want to go somewhere else?"
    call lun_main("If that's okay with you...","soft","wink","sad","R")
    m "Got anywhere in mind?"
    call lun_main("Well... I've been wanting to try out your technique somewhere we can lie down...","soft","angry","sad","R")
    call lun_main("Would you like to... Come to my bedroom, [lun_genie_name]?","base","seductive","sad","mid")
    m "Is a girl as gorgeous and kind as you inviting me to her bed?"
    m "I don't think any man on the planet could turn you down."
    call lun_main("...","base","angry","sad","down")

    show screen blkfade
    with d3

    $ ccg_folder = "luna_bedsex"
    $ ccg("base","blank","blank")

    ">Luna leads you through the dark and cavernous halls of hogwarts."
    m "Woah, the stairs move around? Isn't that dangerous?"
    lun "Only if you're not paying attention!"
    m "..."

    hide screen blkfade
    with d3

    ">You safely manage to navigate to Luna's secluded room, hidden towards the base of Ravenclaw's imposing dorm tower."
    m "Wow... This room's fantastic! It's practically as big as my office! And you have two beds!"
    call lun_main("Well, the other one doesn't belong to me.","soft","wink","sad","mid")
    m "Oh... So you're boarding with another chick?"
    call lun_main("Mhmm!","base","happyCl","sad","mid")

    menu:
        "\"Ever fool around?\"":
            call lun_main("Fool around? Like a pillow fight?","soft","wink","raised","mid")
            m "That's a good start, but I was thinking more along the lines of..."
            g9 "Getting rid of some wricklespots together."
            call lun_main("Oh...","base","wide","sad","down")
            call lun_main("No, nothing like that together.","soft","annoyed","sad","mid")
            call lun_main("Although I think Cho is fighting her own battles against them some nights...","pout","angry","sad","down")

        "\"Who is your roomie?\"":
            call lun_main("Cho!","open","happyCl","base","mid")

    m "Cho Chang?"
    call lun_main("Yep! You've probably seen her play quidditch!","soft","happyCl","base","mid")
    call lun_main("Actually... have you seen her play quidditch?","soft","wink","sad","mid")
    call lun_main("I don't know exactly how long you've been here instead of Dumbledore.","base","closed","base","mid")
    m "I've seen her play."
    call lun_main("Goodie!","base","happyCl","base","mid")
    call lun_main("So, um... is it alright... can we... start... now... {size=-4}please{/size}...","soft","seductive","sad","R")
    m "if you insist..."

    show screen blkfade
    with d3

    ">Led on by Luna's ignorant desperation, you take the naive girl to her bed, revelling in its softness before guiding the needy slut onto your lap."

    $ lun_cg_path         = "images/CG/luna_bedsex/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"blank.webp"
    $ lun_cg_dick         = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0

    hide screen luna_main
    hide screen ccg

    $ lunCG(pupil='up', eye='base', mouth='open_tongue', eyebrow='sad', cheeks='blush', extra_1='hand', extra_2='blank', extra_3='blank', overlay='overlay', tears='blank', body='base')
    show screen luncg
    hide screen blkfade
    with d3
    call ctc

    $ lunCG('talk', 'seductive', 'sad', 'dl')
    lun "Wow... doing this... it's so... different..."
    m "You're telling me!"
    m "(This is the first good bed I've lain down on in years!)"
    $ lunCG('open_tongue', 'angry', 'sad', 'up')
    lun "Ah... The wrackspurts... they're going wild..."
    $ lunCG('base', 'tired', 'sad', 'dl')
    lun "Ah... It's... incredible..."
    $ lunCG('open_tongue', 'seductive', 'sad', 'dr', extra_2='speed')
    lun "Being in control like this"
    $ lunCG('base', 'angry', 'sad', 'right')
    lun "Not to mention..."
    $ lunCG('base', 'seductive', 'sad', 'up')
    lun "Ah..."
    $ lunCG('talk', 'furious', 'sad', 'dl')
    lun "Having you so deep inside me..."
    $ lunCG('base', 'excited', 'sad', 'up')
    lun "it's incredible..."
    m "Mmmm..."
    $ lunCG('talk', 'base', 'sad', 'ur', extra_2='blank')
    lun "The wrackspurts... they--"
    m "(Not these things again... I better change the subject...)"

    menu:
        "-Call her a cumslut-":
            m "That's enough, {b}cumslut{/b}!"
            $ lunCG('talk', 'excited', 'sad', 'right')
            lun "Mmmm, I am a cumslut aren't I?"
            m "The best..."
            $ lunCG('base', 'wink', 'raised', 'dl')
            lun "It's not my fault your cum's so yummy!"
            $ lunCG('open_tongue', 'furious', 'sad', 'ur')
            lun "It's because of your genie magic!"
            m "Yeah, yeah, I'm sure..."
            $ lunCG('talk', 'wide', 'sad', 'dl')
            lun "It is! It's {b}amazing{/b}..."
            m "That still doesn't explain it. I've lived lifetimes on this planet and others."
            $ lunCG('base', 'excited', 'sad', 'right')
            m "In that time, I've never come across a bigger cumslut than you."
            m "Not even Hermione."
            $ lunCG('talk', 'base', 'sad', 'dr')
            lun "Ah..."
            $ lunCG('talk', 'seductive', 'sad', 'dl')
            lun "Well... the wrackspurts... and Lovegoods..."
            $ lunCG('base', 'angry', 'sad', 'right')
            lun "We're more susceptible to magic than regular witches..."
            $ lunCG('talk', 'furious', 'sad', 'up')
            lun "It must be... All of that combined... that makes your cum... so {b}special{/b}..."
            m "Yeah, yeah..."
            $ lunCG('base', 'angry', 'sad', 'dr')
            lun "Ugh... I can't wait for you to give me some more..."
            $ lunCG('talk', 'seductive', 'sad', 'dl')
            lun "Don't hold back... let it all out..."

        "-Fuck it, talk about wrackspurts again-":
            m "They feel good, don't they?"
            $ lunCG('talk', 'excited', 'sad', 'up')
            lun "Ugh... so good..."
            $ lunCG('talk', 'tired', 'sad', 'right')
            lun "I wish we could just stay like this all day, {b}everyday{/b}..."
            m "Careful what you wish for, [lun_name]..."
            $ lunCG('base', 'wink', 'raised', 'dl')
            lun "Mmmm, why?"
            $ lunCG('talk', 'wink', 'sad', 'dl')
            lun "I thought you said I don't get any wishes?"
            m "That's true... But a wish like that?"
            m "I might just make an exception."
            $ lunCG('base', 'seductive', 'sad', 'dr')
            lun "Mmmm... Just the idea of you granting a wish like that..."
            $ lunCG('base', 'angry', 'sad', 'up')
            lun "..."
            $ lunCG('base', 'wink', 'raised', 'dl')
            lun "Are you sure I don't get any wishes, [lun_genie_name]?"
            m "No lamp, no wishes. Those are the rules."
            $ lunCG('pout', 'angry', 'sad', 'right')
            lun "Hmph... Maybe I should try a-- *ah*...{heart} a summoning spell..."
            m "I'm not sure that would work... Besides, what do you need a wish for?"
            ">You grab a hold of Luna's hips and go to town on the needy fuckslut."
            $ lunCG('open_tongue', 'furious', 'sad', 'up')
            lun "Ohh... wow... I...{heart}"
            m "You've got everything you could ever want right here!"
            $ lunCG('talk', 'furious', 'sad', 'ur')
            lun "Ah... the wrackspurts... we need to do something about--"
            ">Tired of hearing about this again, you decide to slam into the blabbering girl to shut her up."
            $ lunCG('open_tongue', 'furious', 'sad', 'ahegao')
            lun "{heart}{heart}{heart}"

        "-Talk about the bed-":
            m "Fuck me, this feels incredible..."
            $ lunCG('base', 'seductive', 'sad', 'dl')
            lun "It does... doesn't it?"
            m "Not the sex."
            $ lunCG('pout', 'tired', 'base', 'dr')
            lun "Oh."
            m "Don't get me wrong, the sex is great!"
            $ lunCG('pout', 'tired', 'sad', 'right')
            lun "..."
            m "I just haven't been in a proper bed since... I can't remember when..."
            $ lunCG('talk', 'wide', 'raised', 'dl')
            lun "Really?"
            $ lunCG('base', 'furious', 'sad', 'dl')
            lun "Ugh... you poor thing..."
            $ lunCG('talk', 'seductive', 'sad', 'dl')
            lun "Where have you been... ah...{heart} sleeping?"
            m "I just fall asleep in my chair most nights..."
            $ lunCG('talk', 'wide', 'sad', 'dl')
            lun "Your chair?"
            $ lunCG('talk', 'tired', 'sad', 'dr')
            lun "That must be so uncomfortable!"
            m "You get used to it."
            $ lunCG('talk', 'seductive', 'sad', 'dl')
            lun "You know... ah...{heart}"
            $ lunCG('base', 'seductive', 'sad', 'right')
            lun "You're welcome to..."
            $ lunCG('talk', 'furious', 'sad', 'ur')
            lun "Spend some more time... in this bed..."
            $ lunCG('talk', 'tired', 'sad', 'dr')
            lun "If you like."
            m "As much as I'd love to spend every single night in here with you..."
            $ lunCG('base', 'wide', 'sad', 'dl')
            lun "{heart}{heart}{heart}"
            m "I'm not sure what would happen if people found out you slept with your headmaster every night..."
            $ lunCG('talk', 'wide', 'sad', 'dl')
            lun "But you're not my headmaster, you're my genie!"
            m "Even still."
            $ lunCG('pout', 'furious', 'sad', 'right')
            lun "..."
            ">You decide to cheer the girl up by bouncing her enthusiastically on your cock."
            $ lunCG('open_tongue', 'furious', 'sad', 'up')
            lun "{heart}{heart}{heart}"

    m "Ugh... here it comes, you nasty little slut!"
    $ lunCG('open_tongue', 'angry', 'sad', 'up')
    lun "Ah... yes!!!..."
    $ lunCG('talk', 'furious', 'sad', 'up')
    lun "Luna's eyes roll upwards into her head as the pleasure proves too much for her."
    g9 "Take this, you needy little whore!"
    $ lunCG('open_tongue', 'wide', 'sad', 'dick', extra_2='cum_1')
    ">You begin to pump a gigantic load into the gleeful girl as she is almost too enamoured in her own lust to notice."
    $ lunCG('open', 'angry', 'sad', 'ahegao')
    lun "ah..."
    $ lunCG('base', 'seductive', 'sad', 'dl')
    lun "{heart}{heart}{heart}"

    hide screen luncg
    show screen blkfade
    with d3

    ">Eventually it all proves too much for the both of you, as you collapse onto the bed and quickly succumb to sleep."
    ">As soon as you wake up, you decide to avoid any confrontation and sneak out before anyone notices you."

    jump end_luna_sex_event


label ll_pf_sex_T1_lake_sex: # Call label
    # Luna and Genie have sex at the lake

    show screen blkfade
    with d3

    ">Luna grabs your hand and leads you down to the lakeside, out into the open moonlight."

    $ ccg_folder = "luna_fucking"
    $ ccg("lake_1","blank","blank")

    call lun_main(None, "open","seductive","sad","mid") # Set expression before hiding blackfade

    hide screen blkfade
    with d3

    call lun_main("Is this alright, [lun_genie_name]?","open","seductive","sad","mid")
    m "This seems as good a place as any."
    call lun_main("So can you finally teach me?","soft","wide","base","mid")
    m "Oh, alright then... Because you asked so nicely..."
    call lun_main("Oh thank you, thank you, thank you!","open","happyCl","base","mid")
    call lun_main("So how does it work?","open","wink","sad","mid")
    m "You'll need to take your top off."
    call lun_main("Okay!","base","happyCl","base","mid")
    #$ luna_wear_top = False
    ">Without even the slightest bit of hesitation, Luna rips off her top and throws it to the ground."
    call lun_main("What's next?","base","seductive","sad","mid")
    m "Bend over."
    call lun_main("{heart}{heart}{heart}","base","seductive","sad","empty")

    hide screen luna_main
    show screen blkfade
    with d3

    ">Without saying anything, Luna bends over, desperate to give herself to you."
    m "Now pull down your skirt..."
    lun "{heart}!!!{heart}"
    ">Luna enthusiastically yanks down her skirt and panties, revealing her sopping pussy."
    lun "Please, [lun_genie_name]..."

    menu:
        "-Tease her-":
            ">You step forwards and gently start rubbing the head of your cock against her wet entrance."
            lun "a-ah..."
            ">Luna desperately starts thrusting towards you, begging for penetration."
            lun "Please, [lun_genie_name], I need it..."
            m "Need what?"
            lun "Your cock...{w=0.3} please, I need it...{w=0.3} The wrackspurts..."
            ">Luna's hips continue to buck in the air almost pathetically."
            lun "I-I-I--"
            pass
        "-Slam it in!-":
            pass

    hide screen ccg
    pause .5
    $ lun_cg_path         = "images/CG/luna_fucking/"
    $ lun_cg_base         = lun_cg_path+"lake_2.webp"
    $ lun_cg_genie        = lun_cg_path+"blank.webp"
    $ lun_cg_dick         = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0
    #$ luna_wear_top       = True
    $ lunCG(pupil='up', eye='excited', mouth='open_tongue', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', tears='blank', body='base')
    show screen luncg

    hide screen blkfade
    with d3

    ">Tired of talking, you decide to end the poor girl's suffering by slamming into her needy little fuckhole."
    lun "{size=+10}{heart}!!!{heart}{/size}"
    m "That's it you little slut!"
    $ lunCG(pupil='up', eye='seductive', mouth='base')
    lun "{size=-5}{heart}wow...{heart}{/size}"
    $ lunCG(pupil='left', eye='seductive', mouth='open')
    ">Even before you're able to start fucking the girl at a steady pace, her hips start violently slamming against you."
    m "Ugh... steady on there, [lun_name], we've only just started!"
    $ lunCG(pupil='dr', eye='furious', mouth='open')
    lun "{heart}a-ah...{w=0.3} I can't...{w=0.3} [lun_genie_name]...{w=0.3} it's just...{w=0.3} too... {heart}{b}goood{/b}...{heart}"
    $ lunCG(pupil='up', eye='furious', mouth='open_tongue', extra_1='speed')
    ">All you can do is stand there as Luna fucks herself senseless on your cock."
    lun "{heart}ah...{heart}the wrackspurts...{heart}{w=0.3} they're going...{heart}{w=0.3} aaaahhh..."
    $ lunCG(pupil='dl', eye='tired', mouth='pout')
    lun "I'm almost...{w=0.3} sad to lose...{w=0.3} them...{heart}{heart}"
    $ lunCG(pupil='ahegao', eye='furious', mouth='open_tongue', overlay='fade')
    lun "They feel {heart}{b}amazing{/b}...{heart}"
    m "About that..."
    $ lunCG(pupil='left', eye='wink', mouth='base')
    lun "W-what?"
    m "This isn't wickspots or whatever you call them..."
    $ lunCG(pupil='left', eye='wide', mouth='open')
    lun "It isn't?... then... ah...{heart} what's this feeling..."
    m "This is sex..."
    $ lunCG(pupil='dr', eye='tired', mouth='pout', extra_1='blank')
    ">Luna's hips slam into you and hold there."
    lun "Oh..."
    m "..."
    $ lunCG(pupil='dl', eye='seductive', mouth='base')
    lun "Hmmm..."
    $ lunCG(pupil='left', eye='wink', mouth='base')
    lun "So, sex forces us to eject the wrackspurts... but the feeling good is normal?"
    m "..."
    m "You got it."
    $ lunCG(pupil='up', eye='furious', mouth='open', extra_1='speed')
    ">Luna's hips resume their assault, desperate to make up for the lost time."
    $ lunCG(pupil='left', eye='seductive', mouth='base')
    lun "So we're... using {b}sex{/b}... to eject them..."
    m "..."
    $ lunCG(pupil='dr', eye='mad', mouth='base')
    lun "That... would explain... the red tint... to their aura..."
    m "(Does this bitch ever shut up?)"
    ">Weary of her analysis you begin to take matters into your own hands."
    $ lunCG(pupil='ahegao', eye='furious', mouth='open')
    ">Grabbing a hold of her hips, you start to fuck the witch in earnest."
    g4 "take this, slut!"
    $ lunCG(pupil='ahegao', eye='furious', mouth='open_tongue', tears='tears')
    lun "{size=+10}{heart}!!!{heart}{/size}"
    $ lunCG(pupil='ahegao', eye='furious', mouth='wide')
    lun "a-ahhhhh..."
    ">You keep pounding her from behind. Luna's lovely breasts jiggle a little with every thrust."
    ">You turn your attention to her butt. It's so milky and pert. She's such a needy slut."
    $ lunCG(pupil='right', eye='wide', mouth='wide', extra_3='spanking')
    $ renpy.play('sounds/slap.mp3')
    lun "ah...{heart}{heart}{heart}"
    ">You give her buttocks another loud slap."
    $ lunCG('open_tongue', 'furious', 'mad', 'up')
    $ renpy.play('sounds/slap.mp3')
    lun "Thank you, [lun_genie_name]."
    ">Feeling that you're getting close, you pick up the pace."
    $ lunCG(eyebrow='sad', eye='furious', pupil='ahegao', mouth='wide')
    lun "Yes! Yes! Thank you! Thank you! I'm almost... almost...{heart}{heart}{heart}{heart}"
    $ lunCG(eyebrow='mad', eye='furious', pupil='ahegao', mouth='open_tongue')
    ">You feel Luna's tight cunt start to spasm and grip down hard on your cock."
    m "Argh! You dirty little slut! Who said you could cum yet!"
    $ lunCG(pupil='left', eye='furious', mouth='open')
    lun "I had too, [lun_genie_name]."
    ">Her hips refuse to slow their pace as she speaks."
    $ lunCG(pupil='ahegao', eye='furious', mouth='base')
    lun "I {b}need{/b} it..."
    $ lunCG(pupil='up', eye='wide', mouth='wide', extra_2='cum_1')
    ">You let out a roar and start cumming uncontrollably right into her pussy."
    lun "ahh!{heart} Yes!{heart} ah...{heart} it's so {b}hot{/b}...{heart}"
    $ lunCG(pupil='ahegao', eye='furious', mouth='open_tongue')
    lun "Your cum is {b}filling{/b} me up..."
    $ lunCG(pupil='dl', eye='tired', mouth='open')
    lun "It's...{w=0.4} {size=-3}I...{/size}{w=0.4} {size=-4}I'm cumming...{/size}{w=0.4} {size=-5}{heart}again...{heart}{/size}"
    ">You keep firing cum deep inside her pussy until the last drop."
    $ lunCG(mouth='open_tongue', eye='furious', eyebrow='sad', pupil='ahegao')
    ">You can see that Luna is still trying to thrust into you, but with multiple orgasms taking over her body, her legs refuse to cooperate."

    hide screen luncg
    show screen blkfade
    with d3

    ">Luna tries to keep going but collapses on the ground with a thump after you pull out of her."
    m "Ugh...{w} I suppose I better carry her back, she'll freeze out here otherwise."

    menu:
        "-Carry her back to her room-":
            pass

        "-Wipe your cock on her first-":
            m "(Should I?)"
            m "(Eh, why not?)"
            ">You take your softening cock and start smearing the end of it across her nose and face."
            lun "..."
            lun "{size=-4}thank you...{/size}"

    ">You softly pick the cum coated girl up off the cold grass, cradling her in your arms as you take her to her dorm."
    lun "..."
    lun "{size=-4}you really are a genie, aren't you?{/size}"

    pause 2

    return


label ll_pf_sex_T1_her_1: # Call label
    # Hermione walks in first time
    call hide_characters
    show screen blkfade
    with d5

    $ lun_cg_path         = "images/CG/luna_fucking/"
    $ lun_cg_base         = lun_cg_path+"base_2.webp"
    $ lun_cg_xpos         = -200

    $ lunCG('open', 'wide', 'base', 'right', body='base')
    show screen luncg
    hide screen blkfade
    with d5

    call play_sound("door")
    call her_main("[genie_name], I hope you're not too busy to--", "smile", "happyCl", "base", "mid", xpos="base", ypos="base")
    call her_main("[genie_name], Luna! What are you two doing?!", "soft", "wide", "worried", "shocked", trans=hpunch)
    m "ah... Isn't it obvious?"
    call her_main("Ugh... Why are you two fucking then?", "scream", "base", "angry", "mid")
    lun "Mmmm... we're getting rid... of some nasty wrackspurts!"
    call her_main("You're still going on about that? I told you before, you're just horny!", "angry", "closed", "angry", "mid")
    $ lunCG(mouth="open", eye="seductive", eyebrow="base", pupil="right")
    lun "Stop... *ah*... being so closed... minded Hermione..."
    lun "I bet you... didn't even realise that... Dumbledore was a genie at first!"
    call her_main("My goodness, you're such an {b}idiot{/b}!", "scream", "base", "angry", "mid")
    lun "Don't be mean Hermione... is it the wrackspurts that are bothering you?"
    lun "I'm sure that we can teach you how to get rid of them by yourself!"
    call her_main("I know how to play with myself...", "annoyed", "base", "angry", "mid")
    $ lunCG(mouth="open", eye="base", eyebrow="base", pupil="right")
    lun "oh..."
    lun "Well if you just want to watch us, I don't mind..."
    call her_main("Don't you have any shame!?", "soft", "base", "angry", "mid")
    $ lunCG(mouth="open_tongue", eye="base", eyebrow="base", pupil="ahegao")
    lun "mmmm... why should I be ashamed... this feels so {b}good{/b}..."
    call her_main("I know it feels good... but you shouldn't let other people watch you do it...", "annoyed", "narrow", "angry", "R")
    call her_main("Imagine if the whole school found out!", "soft", "base", "angry", "mid")
    $ lunCG(mouth="open", eye="seductive", eyebrow="base", pupil="ahegao")
    lun "Oh, that would be {b}fantastic{/b}!"
    lun "Imagine me... being the person to teach the world how to dispel wrackspurts!"
    call her_main("So you'd be okay with everyone knowing you've had Dumbledore's cock in you?", "annoyed", "closed", "base", "mid")
    $ lunCG(mouth="base", eye="happyCl", eyebrow="base", pupil="right")
    lun "I'd give the school a demonstration if I could!"
    call her_main("*Ugh*... I can't believe how fucking {b}dirty{/b} you are...", "soft", "narrow", "base", "R_soft")
    call her_main("I just thought you were an idiot...", "disgust", "narrow", "base", "mid_soft")
    call her_main("But now... I see you've been a bimbo this whole time without even realizing...", "upset", "narrow", "annoyed", "up")
    $ lunCG(mouth="open", eye="base", eyebrow="sad", pupil="right")
    lun "A bimbo?"
    call her_main("*Uh-huh*... You're just Dumbledore's dumb, blonde bimbo...", "soft", "narrow", "angry", "R")
    $ lunCG(mouth="open", eye="seductive", eyebrow="base", pupil="ahegao")
    lun "..."
    call her_main("Well, I think I better give you two some alone time...", "soft", "base", "angry", "mid")
    $ lunCG(mouth="open", eye="wink", eyebrow="base", pupil="right")
    lun "You don't want to stay?"
    call her_main("I need to take care of something... Until then...", "soft", "narrow", "base", "down")
    call her_main("Why don't you just let him empty his balls in you?", "angry", "base", "angry", "mid")
    call hide_characters
    show screen blkfade
    with d5

    $ lun_cg_base = lun_cg_path+"base.webp"
    $ lun_cg_xpos = 0

    ">Hermione shakes her head in disapproval before turning around to leave the room."

    $ lunCG(mouth="base", eye="base", eyebrow="base", pupil="ahegao")

    hide screen blkfade
    with d5

    lun "I'm glad I've got a good friend like Hermione..."
    m "..."
    $ lunCG(mouth="open_tongue", eye="seductive", eyebrow="raised", pupil="ahegao")
    lun "I wish... she could have stayed though..."
    lun "Maybe... I should have asked if... she wanted to take turns..."
    lun "That was probably... rude of me..."
    m "You'd take turns?"
    $ lunCG(mouth="base", eye="seductive", eyebrow="base", pupil="ahegao")
    lun "Of course, sharing is w-what friends do."
    g4 "You filthy slut!"
    ">You start slamming into Luna at full pace."
    g4 "Here it comes you bimbo!"
    ">With that, you start unloading into Luna's pussy."
    call cum_block
    $ lunCG(mouth="wide_tongue", eye="base", eyebrow="base", pupil="ahegao")
    lun "*a-a-ahh*..... soo... goooood..."
    m "..."

    hide screen luncg
    show screen blkfade
    with d5

    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    call lun_main("{heart}{heart}{heart}","soft","seductive","base","up", ypos="head")
    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "Are you good to make your own way back?"
    call lun_main("*ah*... y-y-yea...","base","seductive","base","up", ypos="head")
    m "Awesome, I'm just gonna... take a nap..."

    ">With that, the two of you doze off."
    ">When you wake you find only a Luna shaped cum stain on your desk."

    return


label ll_pf_sex_T1_her_2: # Call label
    # Hermione walks in again (repeatable)

    #TODO Needs posing (disabled event for now)

    call her_main("[genie_name], I really need a good--", "smile", "happyCl", "base", "mid")
    call her_main("Oh... Hello, Luna.", "smile", "happyCl", "base", "mid")
    her "Figures I'd find you up here..."
    m "Why's that?"
    lun "..."
    her "Hmph... I think you know what I'm talking about..."
    menu:
        "-The cum-":
            m "The cum?"
            her "Of course it's the cum!"
        "-The wrackspurts-":
            m "The {i}wricklespots{/i} things?"
            ">You continue to slam into Luna, unperturbed by the conversation."
            her "The--"
            her "You're not going on about that complete nonsense as well as you [genie_name]?"
            her "I expect better from you when it comes to unsubstantiated claims of magical beings."
            lun "ah... but hermione... they are real..."
            her "Shut it! Even if they are, that's not what I'm talking about?"
            m "Then what?"
            her "I'm talking about the fact that you keep sending Luna to class covered in cum!"
    m "Is it that big a deal?"
    lun "I don't think people mind too much Hermione."
    lun "Especially once I explain it to them!"
    her "That's the problem! Everyone's so confused about why you're doing it!"
    her "They're not sure if you're a slut or a simpleton!"
    m "Now, now... I seem to remember a few occasions where you've been out and about with a little something on your person."
    lun "You have?"
    her "That's different! I had the decency to actually feel shame!"
    her "You don't care at all, do you, Luna?"
    lun "Should I?"
    her "Ugh!"
    m "What's the real problem here Hermione?"
    lun "ah..."
    her "What?"
    lun "Gen-um-Dumbledore is right hermione..."
    her "(?)"
    lun "There's something else that's wrong. We've been friends long enough for me to know."
    her "There's nothing wrong!"
    m "..."
    lun "..."
    her "I just think it's funny that whenever I wear even a little bit of cum around the school--"
    her "Every student decides it's their business and that they should get to shout whatever slur they want across the halls at me..."
    her "But when Luna does it, no one so much as bats an eye!"
    lun "Mmmm, they know I'm trying to help them..."
    her "No they don't! All they know is that you're crazy!"
    lun "Hey! You know I don't like that word, Hermione!"
    her "..."
    her "Sorry Luna... it's just..."
    lun "I know..."
    her "Y-You do?"
    lun "I do... And I'm sorry..."
    her "..."
    lun "I'll try and be a little more considerate..."
    her "Thank you..."
    ">With that Hermione looks thankfully at Luna before turning and leaving your office."
    m "What was all that about?"
    lun "Oh, couldn't you tell?"
    lun "Hermione was just a little jealous I think..."
    lun "You might need to have a conversation with her about the wrackspurts effects on your emotions."
    lun "And to tell her you care about--"
    ">Before Luna can prattle on any longer, your hips start helplessly firing their load into the Ravenclaw."
    g9 "HERE'S YOUR CONVERSATION SLUT!"
    g9 "ARGH!!!"
    $ lunCG('open_tongue', 'furious', 'base', 'ahegao')
    ">Your cock explodes inside Luna, unleashing a deluge of your thick seed into her tight little pussy."
    g9 "FUCK YES!!!"
    $ lunCG('open_tongue', 'wide', 'sad', 'ahegao')
    lun "it's{heart}I can't{heart}what{heart}ahhhhhhhhh{heart}{heart}{heart}"
    $ lunCG('base', 'angry', '', 'ahegao')
    lun "..."
    $ lunCG('open', 'tired', '', 'ahegao')
    lun "mmm{heart}{heart}"
    lun "ah...{heart}{heart}{heart}{heart}"

    hide screen luncg
    show screen blkfade
    with d3

    m "Gods that was good..."
    lun "ah..."
    ">With that, you let Luna recover before letting her slip out of your office and back to school."

    return


label ll_pf_sex_T1_ast_1: # Call label
    # Astoria walks in first time

    call hide_characters
    show screen blkfade
    with d5

    $ ast_seen_lun_sex = True

    ">No sooner is the name out of your mouth than a blast of light shoots from the keyhole of your door."
    ast "Alohomora!"
    call play_sound("door")
    ">Your door bursts open to reveal a troublesome witch."

    $ lun_cg_path        = "images/CG/luna_fucking/"
    $ lun_cg_base        = lun_cg_path+"base_2.webp"
    $ lun_cg_xpos        = -200

    $ lunCG('open', 'wide', 'base', 'right', body='base')
    call ast_main(None,"smile","closed","base","mid", xpos="base", ypos="base") # Show before hiding blackfade
    show screen luncg
    hide screen blkfade
    with d5

    call ast_main("Ready to continue our impe--","smile","closed","base","mid", xpos="base", ypos="base")
    $ lunCG('open', 'wide', '', 'right')
    m "!!!"
    lun "!!!"
    call ast_main("{size=+10}[ast_genie_name]!{/size} {i}What{/i} are you doing?","scream","base","worried","mid")
    $ lunCG('base', 'wink', '', 'right')
    lun "Oh... hello, Astoria..."
    $ lunCG('pout', 'tired', 'sad', 'right')
    call ast_main("I wasn't speaking to you, Lovegood! I thought I was the only one to cast imperio around here, [ast_genie_name]!","upset","narrow","angry","mid")
    $ lunCG('base', 'seductive', '', 'dl')
    call ast_main("It's no fair that you get to play around with other students on your own!", "annoyed", "closed","angry", "mid")
    $ lunCG('open', 'angry', '', 'up')
    m "It's not what you think, Astoria..."
    $ lunCG('open', 'wide', '', 'ahegao')
    call ast_main("What, so I'm supposed to think that Loony Luna just bent over and begged you to screw her?!", "upset","closed","angry","mid")
    $ lunCG(pupil='right')
    call ast_main("Speaking of which...", "annoyed", "closed","base", "mid")
    $ lunCG('base', 'tired', '', 'dl')
    call ast_main("{size=+3}Why {size=+3}haven't {size=+3}you {size=+3}two {size=+3}{b}stopped{/b}!?!{/size}","scream","narrow","angry","mid")
    $ lunCG('open', 'tired', '', 'right')
    lun "Sorry... Astoria... but this... is an emergency..."
    $ lunCG('open_tongue', 'furious', '', 'up')
    lun "I had a wrackspurt attack and needed help to purge them..."
    call ast_main("Wrackspurt?...", "annoyed", "narrow","angry", "mid")
    $ lunCG('base', 'seductive', '', 'right')
    call ast_main("Ugh... I always knew you ravenclaw girls were \"special\"...", "upset","narrow","base","R")
    $ lunCG('open', 'wide', '', 'up')
    call ast_main("But you really take the cake, Luna...", "upset","narrow","angry","mid")
    $ lunCG('base', 'happyCl', 'sad', 'right')
    lun "Thank you, Astoria! I love cake."
    $ lunCG('open_tongue', 'furious', 'sad', 'up', extra_1='speed')
    call ast_main("So, is she just like this then [ast_genie_name]?", "upset","narrow","angry","mid")
    m "Pretty much..."
    $ lunCG('open', 'angry', '', 'up')

    if ast_whoring > 7: # Level estimated to coincide with second Imperio with Susan event
        call ast_main("Well, I guess this is okay then...", "annoyed", "narrow","angry", "R")
        $ lunCG('open_tongue', 'furious', '', 'ahegao')
        call ast_main("So long as you clean this room afterwards, it reeks in here!", "upset","narrow","angry","mid")
        $ lunCG('base', 'angry', 'sad', 'right')
    else:
        $ ast_mood += 5

    lun "Isn't it {b}great{/b}?"
    call ast_main("No! It smells gross! I can hardly breathe!", "upset","narrow","angry","mid")
    $ lunCG('open', 'wide', 'base', 'up')
    lun "Those are probably the wrackspurts... We can teach you how to get rid of them if you'd like."
    $ lunCG('open', 'seductive', 'base', 'right')
    call ast_main("No thanks.","upset","narrow","angry","mid")
    $ lunCG('base', 'furious', 'sad', 'right')
    lun "At least watch us finish then..."
    call ast_main("What? {i}Why?{/i}", "annoyed", "narrow","angry", "mid")
    $ lunCG('open', 'wide', '', 'right')
    lun "You should know... how to expel them..."
    $ lunCG('open', 'furious', '', 'up')
    lun "It's just... the {b}best{/b}..."
    $ lunCG('base', 'wink', '', 'right')
    call ast_main("You want me to watch while he--", "upset","base","worried","mid")
    g4 "Argh... This is it whores!"
    $ lunCG('open_tongue', 'furious', '', 'ahegao', extra_2='cum_1')
    call ast_main("!!!", "upset","base","worried","mid")
    lun "Yes!"
    g4 "ARGH!!!"
    ">You grab a tight hold of Luna's hips as you start to wildly fill her up with your cum."
    call ast_main("...","upset","narrow","angry","mid")
    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    $ lunCG('open_tongue', 'wide', '', 'ahegao')
    lun "{heart}{heart}{heart}"

    hide screen astoria_main
    hide screen luncg
    show screen blkfade
    with d3

    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "enjoyed the show?"
    ">You look around but can't find any trace of the small witch."
    call lun_main("*ah*... y-y-yea...","base","seductive","base","up", ypos="head")
    m "Awesome, I'm just gonna... take a nap..."

    ">With that the two of you doze off."
    ">When you wake you find only a Luna shaped cum stain on your desk."

    return


label ll_pf_sex_T1_ast_2: # Call label
    # Astoria walks in again (repeatable)
    call hide_characters
    show screen blkfade
    with d5

    #Upset at [ast_genie_name] for banging Luna again
    #Comes in after Luna is covered in cum
    #Starts shaming Luna about the smell of the room and her being a cumslut
    #Complains about all big boobed girls being sluts
    #Cum all over her as Astoria watches
    $ lun_cg_path        = "images/CG/luna_fucking/"
    $ lun_cg_base        = lun_cg_path+"base_2.webp"
    $ lun_cg_xpos        = -200

    $ lunCG('open', 'wide', 'base', 'right', body='base')
    show screen luncg
    hide screen blkfade
    with d5

    call play_sound("door")
    call ast_main("[ast_genie_name]!","smile","closed","base","mid", xpos="base", ypos="base")
    lun "Ah... Astoria..."
    call ast_main("Are you two going at it again?","upset","narrow","angry","mid")
    m "Take a guess."
    $ lunCG(pupil='up', eye='furious', mouth='open_tongue', extra_1='speed')
    call ast_main("Ugh! How am I ever supposed to learn any magic if you two won't stop shagging like rabbits?", "annoyed", "narrow","angry", "mid")
    $ lunCG('base', 'seductive', '','right')
    lun "Ah..."
    m "I don't know Astoria, what you're watching here is pretty magical if you ask me."
    $ lunCG('open', 'seductive', '', 'up')
    call ast_main("Pfft... I'd hardly call an old perv like you banging a {b}bimbo{/b} \"magical\"!","upset","narrow","angry","R")
    m "Mmmm, it feels pretty magical..."
    m "Why don't you stay and watch... You might learn something."
    $ lunCG('base', 'furious', '', 'right')
    lun "Ah... yes... stay, Astoria..."
    $ lunCG('open', 'furious', 'base', 'ahegao')
    lun "You should... ah... learn how to get rid of wrackspurts."
    call ast_main("Again with your made up mumbo jumbo?!","open","narrow","angry","mid")
    call ast_main("If you want to be gross with him, just say so...", "upset","narrow","angry","R")
    $ lunCG('open', 'wide', 'sad', 'right', tears='tears')
    lun "Ah... I'm serious..."
    $ lunCG('open_tongue', 'wide', '', 'up')
    lun "They're real... and they... ah... make your head... all fuzzy..."
    $ lunCG('open_tongue', 'angry', '', 'ahegao')
    lun "Sometimes... I can barely... think about anything but {i}this{/i}..."
    $ lunCG('base', 'angry', 'base', 'ahegao')
    call ast_main("You're just a big boobed bimbo!","scream","narrow","angry","mid")
    call ast_main("All of you big boobed girls are the same!", "upset","narrow","angry","mid")
    $ lunCG('open', 'furious', 'sad', 'ahegao')
    lun "Ah..."

    #TODO Astoria could refer to other girls depending on whether they've achieved certain "status" (whoring level/completed event)
    call ast_main("If it's not you fucking your headmaster every chance you can get, it's Susan strutting around the halls...", "annoyed", "narrow","angry", "R")
    $ lunCG('base', 'angry', '', 'ahegao')
    if her_whoring >= 15:
        call ast_main("Or Hermione Granger being the big-titted slut that she is...","clench","narrow","angry","L")

    $ lunCG('base', 'seductive', '', 'right')
    call ast_main("It's ridiculous!","upset","narrow","angry","R")
    $ lunCG('base', 'wink', '', 'right')
    lun "Ah... It's not that..."
    $ lunCG('open', 'wide', '', 'right')
    g9 "ARGH! HERE IT COMES SLUTS!"
    $ lunCG('open_tongue', 'angry', '', 'ahegao')
    lun "Yes..."
    call ast_main("I think I'm going to leave...", "annoyed", "narrow","angry", "R")
    $ lunCG('open', 'wide', 'sad', 'right')
    lun "Ah... No... stay..."
    $ lunCG('base', 'wide', '', 'ahegao')
    lun "You need to see... them..."
    call ast_main("See who?", "annoyed", "narrow","angry", "mid")
    $ lunCG('base', 'wide', '', 'right')
    lun "The wrackspurts..."
    g9 "HERE'S YOUR ROCKSPORTS SLUT!"
    g9 "ARGH!!!"
    call ast_main("...", "upset","base","worried","mid")
    $ lunCG('open_tongue', 'furious', 'base', 'ahegao')
    ">Your cock explodes inside Luna, unleashing a deluge of your thick seed into her tight little pussy."
    g9 "FUCK YES!!!"
    $ lunCG('open_tongue', 'wide', 'sad', 'ahegao')
    lun "it's{heart}I can't{heart}what{heart}ahhhhhhhhh{heart}{heart}{heart}"
    $ lunCG('base', 'angry', '', 'ahegao')
    lun "..."
    call ast_main("Wow...", "upset","base","worried","mid")
    $ lunCG('open', 'tired', '', 'ahegao')
    lun "{heart}ah...{heart} Did you see... them?"
    call ast_main("*Pffft*", "upset","narrow","angry","mid")
    call ast_main("The only thing I saw was a super slut getting banged by her gross old headmaster!","scream","narrow","angry","mid")
    $ lunCG('base', 'seductive', '', 'dl')
    lun "mmm{heart}{heart}"
    hide screen astoria_main
    with d3
    ">With that, Astoria turns and leaves, a confused look plastered across her face."
    lun "ah...{heart}{heart}{heart}"

    hide screen luncg
    show screen blkfade
    with d3

    m "Gods that was good..."
    call lun_main("*ah*...","soft","seductive","base","up", ypos="head")
    if daytime:
        ">You let Luna recover for a while until she is somewhat capable again to head back to her classes."
    else:
        ">You let Luna recover for a while until she is somewhat capable again to walk back to her room."

    return


label ll_pf_sex_T1_ton_1: # Call label
    # Tonks walks in first time
    call hide_characters
    show screen blkfade
    with d5

    $ ton_seen_lun_sex = True

    $ lun_cg_path      = "images/CG/luna_fucking/"
    $ lun_cg_base      = lun_cg_path+"base_2.webp"
    $ lun_cg_xpos      = -200

    $ lunCG('open', 'wide', 'base', 'right', body='base')
    show screen luncg
    hide screen blkfade
    with d5

    call play_sound("door")
    call ton_main("Professor Dumbledore!","horny","base","raised","L", xpos="base", ypos="base")
    lun "!!!"
    $ lunCG('open', 'seductive', 'sad', 'dr')
    m "!!!"
    $ lunCG('base', 'wide', 'base', 'right')
    call ton_main("I didn't think you'd be able to land a grade-a bird like this, you old horndog!","horny","base","raised","L")
    $ lunCG('open', 'seductive', 'sad', 'up')
    call ton_main("How'd you manage this one then? Love potion? Points? Gold?","base","base","raised","L")
    $ lunCG('open', 'wink', 'base', 'right')
    lun "He's helping me... ah... get rid of... my wrackspurts!"
    call ton_main("...","horny","base","base","L")
    $ lunCG('open', 'seductive', 'sad', 'up')
    call ton_main("Mind control?","open","base","raised","L")
    m "Nope."
    $ lunCG('open_tongue', 'furious', 'sad', 'up')
    call ton_main("Then should I ask what the hell a \"wrackspurt\" is?","base","base","raised","L")
    m "Ugh... Luna can explain them..."
    $ lunCG('base', 'seductive', 'sad', 'right')
    lun "Ah... they're nasty little... mmmm... creatures that make... ah... you want... mmm... to {b}fuck{/b}."
    $ lunCG(pupil='up', eye='furious')
    call ton_main("...","horny","base","raised","L")
    $ lunCG('open', 'wink', 'sad', 'right')
    lun "You should... ah... be careful, professor Tonks... {heart} we're expelling a lot... of them... {heart}"
    $ lunCG('base', 'seductive', 'sad', 'dl')
    call ton_main("Really? And how will I know if these \"wrackspurts\" are after me...?","horny","base","raised","L")
    $ lunCG('base', 'angry', 'base', 'dr')
    lun "You'll feel... ah... hot...{heart} down there..."
    call ton_main("Oh... I see...","horny","base","raised","L")
    $ lunCG('base', 'furious', 'sad', 'right')
    call ton_main("You know, you should come visit me after hours, Miss Lovegood. I think I might also be able to help you out...","horny","base","raised","L")
    m "Hey!"
    $ lunCG('base', 'seductive', 'sad', 'dl')
    lun "Ah... thank you... {heart} Ms tonks... but I don't think... ah... you'll {i}taste{/i} as good..."
    call ton_main("Now, now, you don't know that... I taste like {b}heaven{/b}...","base","base","raised","L")
    $ lunCG('base', 'furious', 'mad', 'ahegao')
    lun "There's just... ah{heart} no way... you can... taste half as good... {heart}"
    $ lunCG('open_tongue', 'seductive', 'sad', 'dr')
    ">Tonks hand disappears down the front of her pants."
    call ton_main("Oh I see how it is...","horny","base","raised","L")
    $ lunCG('open', 'wink', 'sad', 'right')
    lun "Ah... you do?"
    $ lunCG('base', 'seductive', 'sad', 'right')
    call ton_main("Uh-huh... You're just Dumbledore's dirty, little, cumslut... aren't you?","base","base","raised","L")
    $ lunCG('open', 'happyCl', 'base', 'dr')
    lun "That's it!"
    $ lunCG('open', 'base', 'sad', 'right')
    call ton_main("So you admit it then?","horny","base","base","L")
    $ lunCG('base', 'wide', 'base', 'right')
    lun "Of course! I'm proud... to be a cumslut!"
    $ lunCG('open', 'happyCl', 'sad', 'dr')
    lun "As an auror you should... ah{heart} know the importance of... mmm{heart} warding off evil magic!"
    $ lunCG('open', 'seductive', 'sad', 'up')
    call ton_main("There's warding...","base","base","base","L")
    $ lunCG('open_tongue', 'furious', 'sad', 'ahegao')
    call ton_main("And then there's just being covered in cum...","base","base","raised","L")
    $ lunCG('open', 'tired', 'sad', 'dl')
    lun "Oh..."
    $ lunCG('open', 'happyCl', 'base', 'right')
    lun "They're both fun!"
    $ lunCG('open', 'seductive', 'base', 'up')
    call ton_main("Fuck... you've really done a number on her, haven't you, Dumbledore?","horny","base","raised","L")
    m "She was like this from the start..."
    $ lunCG('base', 'happyCl', 'base', 'dr')
    lun "Mhmm!"
    call ton_main("Then you've lucked out on finding the horniest little nymph to ever live...","horny","base","base","L")
    $ lunCG('open', 'angry', 'mad', 'right')
    lun "I am not... a nymph!"
    $ lunCG('open', 'angry', 'sad', 'up')
    call ton_main("Anyway... all this talk of how much you love your headmaster's yummy cum...","base","base","raised","L")
    $ lunCG(pupil='right')
    call ton_main("I want to see it...","horny","base","raised","L")
    $ lunCG(pupil='dl')
    m "See what?"
    call ton_main("Her, covered in it...","horny","base","base","L")
    $ lunCG('open', 'wide', 'base', 'right')
    lun "You do?"
    $ lunCG('open_tongue', 'angry', 'sad', 'ahegao')
    call ton_main("Ugh... you bet... nothing like seeing your students soaking in their headmaster's spunk...","base","base","raised","L")
    lun "{heart}{heart}{heart}"
    show screen blkfade
    with d3

    menu:
        "Where should you cum?"
        "-On her face-":
            $ lun_cg_path         = "images/CG/luna_desk2/"
            $ lun_cg_base         = lun_cg_path+"base.webp"
            $ lun_cg_genie        = lun_cg_path+"genie_robe.webp"
            $ lun_cg_xpos_abs     = 0
            $ lun_cg_ypos_abs     = 0
            $ lun_cg_xpos         = 0
            $ lun_cg_ypos         = 0
            $ lunCG(pupil='up', eye='excited', mouth='base', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', tears='blank', pos=1, body='base')

            m "On your knees slut!"
            $ lunCG('sucking', 'seductive', 'sad', 'up', pos=8)
            lun "Mhmm!"
            hide screen blkfade
            with d3

            ">Luna quickly hops off the desk and kneels in front of your cock."
            $ lunCG('open', 'wink', 'base', 'up', pos=1)
            lun "Need me to--"
            g4 "Shut up!"
            $ lunCG('base', 'base', 'sad', 'up')
            lun "..."
            g4 "Ugh... here it is you little whore!"
            ton "..."
            ">Eager to show off to your audience, you shoot a colossal load of cum over Luna's waiting face."
            $ lunCG('open_tongue', 'seductive', 'sad', 'ahegao', extra_1='cum_3')
            lun "{heart}{heart}{heart}"
            lun "{size=-4}thank you...{/size}"

            show screen blkfade
            with d3

            $ lun_cg_path         = "images/CG/luna_fucking/"
            $ lun_cg_base         = lun_cg_path+"base_2.webp"
            $ lun_cg_genie        = lun_cg_path+"blank.webp"
            $ lun_cg_dick         = lun_cg_path+"blank.webp"
            $ lun_cg_xpos_abs     = 0
            $ lun_cg_ypos_abs     = 0
            $ lun_cg_xpos         = -200
            $ lun_cg_ypos         = 0
            $ lunCG(pupil='ahegao', eye='furious', mouth='base', eyebrow='sad', cheeks='blush', extra_1='cum_3', extra_2='blank', extra_3='blank', tears='mascara', body='base')

            ">Tonks' fingers noticeably begin to speed up."

            hide screen blkfade
            with d3

        "-Inside her-":
            g4 "ARGH!!! TAKE IT ALL YOU LITTLE WHORE!"
            $ lunCG('open', 'angry', 'sad', 'ahegao', extra_1='cum_3')
            ">You start filling up poor Luna as her hungry pussy does its best to milk you dry."
            $ lunCG('open_tongue', 'furious', 'sad', 'ahegao')
            lun "Oh thank you! thank you! thank you!"
            call ton_main("Wow...","horny","base","raised","L")
            $ lunCG('open_tongue', 'furious', 'sad', 'right')
            lun "Ugh...{heart} it's like he's... pumped me full of magic..."
            ">Tonks' fingers noticeably begin to speed up."
            $ lunCG('open_tongue', 'furious', 'sad', 'ahegao')

    call ton_main("Mmmm, damn... where were all these sluts when I was in school?","horny","base","raised","L")
    call ton_main("aah...{w=0.4} Well, this has certainly been... fun...","horny","base","raised","L")
    call ton_main("But I think I best be on my way... I need to take care of some \"rockspoons\" of my own...","base","base","raised","L")
    $ lunCG('base', 'seductive', 'sad', 'right')
    lun "Ugh... You don't want to see us go again?"

    ">With that, Luna slips your softening cock back into her tight hole."
    m "Ugh... can't we have a break first?"
    $ lunCG('pout', 'seductive', 'sad', 'left')
    lun "..."
    ">Luna simply looks back at you with the eyes of a puppy dog begging for a treat."
    m "Fine... just start off slowly this time..."
    $ lunCG('base', 'wink', 'base', 'left')
    lun "That's no fun..."
    $ lunCG('open', 'angry', 'sad', 'up', extra_2='speed')
    call ton_main("Wow... you two really are about to go again, aren't you?","base","base","raised","L")
    $ lunCG('open', 'wink', 'sad', 'right')
    lun "You don't have to... a-ah...{heart} stay if you don't want to..."
    call ton_main("Oh... {w=0.5}I may as well stick around for a little bit longer...","base","base","raised","L")
    $ lunCG('open_tongue', 'furious', 'sad', 'up')
    ">Tonks' angrily fingers her cunt while she stares hungrily at Luna's bouncing boobs."

    show screen blkfade
    with d3
    pause 2
    hide screen blkfade
    with d3

    g9 "NO! MORE!"
    $ lunCG('base', 'angry', 'sad', 'left')
    lun "Pleaaaaaase!"
    call ton_main("Yeah, you can make it one more round Dumbledore!","horny","base","raised","L")
    $ lunCG('base', 'tired', 'sad', 'dl')
    g9 "I've already gone four rounds!"
    $ lunCG('open', 'wide', 'sad', 'left')
    lun "But there are still so many--"
    $ lunCG('pout', 'tired', '', 'dl')
    g9 "Well, too bad, I'm about to pass out."
    call ton_main("Hmmm, he's probably right, Luna... He is pretty old.","base","base","raised","L")
    $ lunCG('pout', 'angry', 'sad', 'right')
    lun "That shouldn't matter!"
    $ lunCG('pout', 'angry', 'sad', 'dr')
    call ton_main("It's also getting rather late. As your teacher, it is my responsibility to make sure you follow curfew.","base","base","raised","L")
    $ lunCG(pupil='dl')
    m "The whole cum bath thing is okay though?"
    call ton_main("Surprisingly, there's nothing about a \"cum bath\" in the teachers handbook...","horny","base","raised","L")
    m "Fair enough. You two going to bed suits me anyway."
    $ lunCG('open', 'tired', 'sad', 'right')
    call ton_main("Well, come on then, Luna, hurry up and get dressed! I'll walk you home.","horny","base","raised","L")
    $ lunCG('base', 'base', 'sad', 'dr')
    lun "Alright then professor Tonks..."
    show screen blkfade
    with d3

    call hide_characters
    call lun_chibi("stand","mid","base", flip=True)
    hide screen luncg
    $ luna_cum = 9
    #$ luna_wear_cum = True
    hide screen blkfade
    with d3

    ">With an airy smile, Luna picks up her clothes and puts them on over her cum soaked body."
    call lun_main("","base","base","base","mid", xpos="mid", ypos="base", flip=True)
    call ton_main("Aren't you going to scourgify yourself before we go?","base","base","raised","L", xpos="base", ypos="base")
    call lun_main("What, Why?","base","wink","raised","mid")
    call ton_main("No offence honey, but you reek... I'm feeling light headed just standing next to you.","base","base","raised","L")
    call lun_main("Oh that's just the wrackspurts! Their corpses can have that effect on people.","base","happyCl","base","mid")
    call lun_main("I {b}love{/b} the smell myself... Besides, I need to wear them to act as a warning to the other wrackspurts while I sleep!","base","angry","sad","up")
    call ton_main("You mean you expect me to walk you back to your room covered head to toe in cum?","horny","base","base","L")
    call lun_main("You don't have to... I can make my own way back.","base","wink","sad","mid")
    call ton_main("I wouldn't miss this for the world... All we need is a leash and we can cross a line off my bucket list.","horny","base","raised","L")
    call lun_main("What?","open","wink","base","mid")
    call ton_main("Never mind, let's just go before the prefects start whining about curfew.","base","base","raised","L")

    show screen blkfade
    with d3

    ">With that, tonks walks off with the cum-soaked Luna."
    m "Finally... I thought they'd never leave..."
    ">You collapse into your chair and doze off only seconds later."

    pause 1.5

    return


label ll_pf_sex_T1_ton_2: # Call label
    # Tonks walks in again (repeatable)
    call hide_characters
    show screen blkfade
    with d5

    $ lun_cg_path      = "images/CG/luna_fucking/"
    $ lun_cg_base      = lun_cg_path+"base_2.webp"
    $ lun_cg_xpos      = -200

    $ lunCG('open', 'wide', 'base', 'right', body='base')
    show screen luncg
    hide screen blkfade
    with d5

    call play_sound("door")
    call ton_main("Ugh... are you two going at it again?","open","base","raised","mid", xpos="base", ypos="base")
    $ lunCG('base', 'seductive', 'base', 'right')
    lun "Ah... these wrackspurts... ah... are quite... powerful..."
    call ton_main("Mmmm, I can believe that... In fact...","horny","base","base","L")
    ">Tonks slides a hand down her pants."
    $ lunCG('base', 'angry', 'sad', 'up')
    call ton_main("Ah... it looks like they're affecting me too...","open","base","raised","down")
    m "..."
    $ lunCG('open', 'wide', 'base', 'right')
    lun "So quick! Ah... You better stay here... ah... to let them all out..."
    call ton_main("I wouldn't miss a show like this for the world...","horny","base","base","mid")
    $ lunCG('base', 'base', 'sad', 'up')
    call ton_main("I'd normally have to pay a fortune to see this.", "open", "base", "shocked", "mid")
    m "Maybe I should start charging?"
    $ lunCG('pout', 'wink', 'sad', 'left')
    call ton_main("I could say the same to you...","open","base","base","mid")
    $ lunCG('base', 'angry', 'sad', 'left')
    call ton_main("Although, as an auror, I think my charges would be a little more severe...","horny","base","angry","L")
    m "Watch away then..."
    ">Tonks starts violently fingering herself under her pants."
    call ton_main("Mmmm, don't mind if I do...","horny","base","angry","L")
    $ lunCG('open', 'seductive', 'sad', 'up', extra_2='speed')
    ">The room falls silent, save for the rhythmic noise of Luna being fucked and the quiet squelching coming from her perverted teacher."
    $ lunCG('open_tongue', 'base', 'sad', 'ahegao')
    lun "Ah... ah... ah..."
    $ lunCG('base', 'wink', 'base', 'right')
    call ton_main("So, Luna.","open","base","base","L")
    $ lunCG('open_tongue', 'seductive', 'sad', 'up')
    lun "Yes... ah..."
    $ lunCG('base', 'tired', 'sad', 'right')
    call ton_main("Will you be needing another escort to your room today?","base","base","angry","L")
    $ lunCG('base', 'wink', 'base', 'left')
    lun "Oh, well I don't think I really need one..."
    $ lunCG('open', 'wide', 'sad', 'right')
    lun "But I'd be happy for the company. I always love to make new friends!"
    $ lunCG('base', 'base', 'base', 'up')
    call ton_main("I can see that... Will you also be wearing a fresh load of your headmaster's cum while we walk?","horny","base","angry","mid")
    $ lunCG('open', 'angry', 'sad', 'right')
    lun "Of course!"
    $ lunCG('open_tongue', 'seductive', 'sad', 'ahegao')
    call ton_main("Ugh... {heart}fuck{heart}... that's it...","open","base","angry","L")
    call ton_main("Last time I walked you home...","open","base","base","ahegao")
    $ lunCG('base', 'wink', 'sad', 'right')
    lun "{heart}Ah... yes? ah...{heart}"
    call ton_main("God, I've never been so turned on in my life!","horny","base","angry","ahegao")
    $ lunCG('open_tongue', 'seductive', 'sad', 'right')
    call ton_main("Watching everyone in the school turn to look at you...","open","base","base","L")
    $ lunCG('open_tongue', 'angry', 'mad', 'up')
    call ton_main("Coated in the biggest fucking load of cum...","open","base","base","ahegao")
    $ lunCG('wide', 'angry', 'sad', 'ahegao')
    lun "Ah...{heart}"
    $ lunCG('open', 'angry', 'sad', 'right')
    call ton_main("And no one said a word...","base","base","base","L")
    call ton_main("They just {b}fucked{/b} you with their eyes...","horny","base","base","mid")
    $ lunCG('open_tongue', 'wide', 'sad', 'right')
    lun "They did?{heart}"
    $ lunCG(pupil='up')
    call ton_main("Can you blame them? You were such pretty, well-fucked mess...","horny","base","base","mid")
    call ton_main("Ugh... I stayed up all night fingering myself to the sight of you...","open","base","angry","ahegao")
    $ lunCG('base', 'seductive', 'sad', 'right')
    lun "Ah... you did?"
    $ lunCG('base', 'angry', 'sad', 'up')
    call ton_main("Mhmmm... I'll probably do it again tonight...","open","base","base","L")
    lun "Careful... ah... you might release... too many wrackspurts..."
    $ lunCG('open', 'angry', 'sad', 'left')
    call ton_main("Oh... Will that make all my students nice and slutty like you?","horny","base","raised","L")
    $ lunCG('base', 'tired', 'sad', 'up')
    lun "It-- ah... it could."
    $ lunCG('open_tongue', 'angry', 'mad', 'ahegao')
    call ton_main("Mmmm, fantastic...","open","base","angry","mid")
    lun "Fantastic? Why...{w=0.3} ah...{w=0.3} would you..."
    ">Before Luna can say anymore, you grab onto her hips before slamming into her."
    lun "Ah...{heart}{heart}{heart}"
    g9 "Here it comes you cumsluts!"

    menu:
        "-Cum inside-":
            $ lunCG('open_tongue', 'mad', 'angry', 'ahegao', extra_1='cum_1')
            ">You start unloading into Luna's pussy."
            $ lunCG('open_tongue', 'angry', 'mad', 'ahegao')
            lun "a-a-ahh..... soo... goooood..."
            m "..."
            $ lunCG('wide', 'mad', 'angry', 'ahegao')
            ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
            $ lunCG('base', 'mad', 'mad', 'ahegao')
            lun "{heart}{heart}{heart}"
            ">You slump back into your chair, leaving Luna on your desk, leaking cum."
            $ lunCG('open_tongue', 'angry', 'angry', 'ahegao')
            call ton_main("Dumbledore, what do you think you're doing?", "open", "wide", "shocked", "mid")
            m "Busting a load?"
            call ton_main("Inside her! Now she won't be able to show off what a little cumslut she is!","open","base","angry","mid")
            $ lunCG('base', 'angry', 'sad', 'left')
            lun "ah..."
            m "You're just upset you don't get to lead her around like a trophy."
            $ lunCG('open', 'tired', 'sad', 'left')
            call ton_main("Ugh...","horny","base","base","L")
            $ lunCG('open_tongue', 'seductive', 'sad', 'dr')
            call ton_main("At least try and get a little on her as well next time.","base","base","angry","r")
            $ lunCG('open_tongue', 'tired', 'sad', 'dl')
            lun "..."
            m "I'll try. Now, are you ready to take Miss Lovegood to her room?"
            $ lunCG('open_tongue', 'tired', 'sad', 'dr')
            call ton_main("I suppose so... Not that there's much point if she isn't covered in cum...","base","base","angry","R")

        "-Coat her face-":
            m "On your knees slut!"
            lun "Okay!"
            show screen blkfade
            with d5
            $ lun_cg_path         = "images/CG/luna_desk2/"
            $ lun_cg_base         = lun_cg_path+"base_2.webp"
            $ lun_cg_genie        = lun_cg_path+"blank.webp"
            $ lun_cg_xpos_abs     = 0
            $ lun_cg_ypos_abs     = 0
            $ lun_cg_xpos         = -200
            $ lun_cg_ypos         = 0
            $ lunCG(pupil='up', eye='excited', mouth='base', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', tears='blank', pos=1, body='base')
            hide screen blkfade
            with d5
            ">Luna quickly hops off the desk and kneels in front of your cock."
            $ lunCG('open_tongue', 'seductive', 'sad', 'dick')
            lun "{heart}{heart}{heart}"
            $ lunCG('open_tongue', 'seductive', 'sad', 'up')
            g4 "Ugh... here it is you little whore!"
            $ lunCG('open_tongue', 'seductive', 'sad', 'dick', extra_1='cum_3')
            call ton_main("...","horny","base","base","L")
            ">Eager to show off to your audience you fire off a colossal load over cum over luna's waiting face."
            $ lunCG('open_tongue', 'angry', 'sad', 'up')
            lun "{heart}{heart}{heart}"
            $ lunCG('base', 'seductive', 'sad', 'up')
            lun "{size=-5}thank you...{/size}"
            ">Tonks' fingers noticeably begin to speed up."
            $ lunCG('base', 'seductive', 'sad', 'left')
            call ton_main("Mmmm, damn... that's hot...","horny","base","base","L")
            m "Ready to take Miss Lovegood home?"
            $ lunCG('base', 'wink', 'base', 'left')
            call ton_main("You bet! I hope you don't mind taking the long route, Luna...","horny","base","raised","L")

    hide screen luncg
    show screen blkfade
    with d3

    ">With that, Tonks leads Luna out into the halls and takes her back to her room."
    ">You doze off seconds after they leave."

    return

