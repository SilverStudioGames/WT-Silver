

### Snape Hangout Event ###

label snape_hangout:

    call setup_fireplace_hangout(char="snape")

    $ ss_he_counter += 1
    if wine_ITEM.owned >= 1:
        $ wine_ITEM.owned -= 1

    $ ss_he_drink.start()

    label snape_hangout_continue:
        hide screen bld1
        show screen with_snape(ani=False)
        with fade
        call bld


    ### Intro Events ###
    # Events are located in the character's intro file.

    # Hermione
    if hermione_intro.E1_complete and not ss_he.hermione_E1:
        jump ss_he_hermione_E1 # Fist discussion about Hermione with Snape.
    if hermione_intro.E2_complete and not ss_he.hermione_E2:
        jump ss_he_hermione_E2 # Second discussion about Hermione with Snape.

    # Tonks
    if tonks_intro.E1_complete and not ss_he.tonks_E1:
        jump ss_he_tonks_E1
    if tonks_intro.E3_complete and not ss_he.tonks_E2:
        jump ss_he_tonks_E2
    if ss_he.tonks_E2 and not ss_he.tonks_E3:
        jump ss_he_tonks_E3

    # Cho
    if cho_intro.E2_complete and not ss_he.cho_E1:
        jump ss_he_cho_E1
    if cho_quiz.lost and not quidditch_book_1_ITEM.unlocked and not cho_quiz.complete and not ss_he.cho_E2:
        # After failing the Quiz.
        jump ss_he_cho_E2


    ### General Events ###
    # Events are located here.

    # Hermione
    if hg_strip.trigger and not ss_he.hermione_strip: #After second dance where Snape entered room.
        jump ss_he_hermione_strip # Get to invite Snape to watch.

    # (Quidditch) Ask Snape for help with Slytherins.
    if cho_quid.E6_complete and not cho_quid.E9_complete:
        jump cho_quid_E9

    ### Snape Stories ###
    # Events are located here.

    if sna_support < 15:
        $ random_number = 1
    else:
        $ random_number = renpy.random.randint(1, 3)

    if random_number == 1:
        if sna_support < 15:
            $ sna_support += 1
        $ ss_he_story.start()

    label end_snape_hangout:
        show screen with_snape(ani=True)
        call bld
        call notes
        ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."

    label end_snape_hangout_points:

    if sna_friendship < 100:
        if weather in ("rain", "blizzard"):
            # Rain puts him in a good mood.
            $ sna_friendship += 2

        if game.difficulty < 2:
            $ sna_friendship += 5
        elif game.difficulty == 2:
            $ sna_friendship += 4
        else:
            $ sna_friendship += 3

    if sna_friendship > 100:
        $ sna_friendship = 100

    if game.daytime:
        jump night_start
    else:
        jump day_start



label ss_he_wine_intro:
    call bld
    m "Look what I've got!"
    call sna_main("*Hmm*...?","snape_05", ypos="head")
    call sna_main("Let me see...")
    pause.1

    # Show wine
    call give_reward(">You hand over the bottle you found in the cupboard to professor Snape...", gift="interface/icons/wine.webp", sound=False)

    call sna_main("This one has got to be from Albus' personal stash!","snape_24")
    call sna_main("Some pricey and incredibly rare stuff.","snape_06")
    m "Shall we then?"
    call sna_main("We most certainly shall!","snape_02")

    jump snape_hangout_continue


label ss_he_wine_intro_E2:
    call bld
    m "Care for another bottle?"
    pause.1

    call give_reward(">You hand over the bottle you found in the cupboard to Professor Snape...",gift="interface/icons/wine.webp", sound=False)

    call sna_main("Another bottle of Dumbledore's wine?","snape_05", ypos="head")
    call sna_main("Did you find Albus' secret stash or was it his personal wine cellar?","snape_05")
    m "It's more of a \"wine cabinet\", I'd say."
    m "And I believe there is more where this came from..."
    call sna_main("Seriously, how big is that stash?","snape_05")
    g9 "Why don't we find out?"
    call sna_main("It's sure good to be us! let's uncork that bastard!","snape_02")

    jump snape_hangout_continue


label ss_he_wine_repeat:
    call bld
    m "Look what I've got!"
    pause.1

    call give_reward(">You hand over the bottle you found in the cupboard to Professor Snape...",gift="interface/icons/wine.webp", sound=False)

    call sna_main("Another one?","snape_05", ypos="head")

    $ random_number = renpy.random.randint(1, 6)
    if random_number == 1:
        call sna_main("Splendid!","snape_02")
    elif random_number == 2:
        call sna_main("Well done, my friend!","snape_02")
    elif random_number == 3:
        call sna_main("Lately I am having a hard time drinking anything but this!","snape_02")
    elif random_number == 4:
        call sna_main("Great! I feel less stressed out already!","snape_02")
    elif random_number == 5:
        call sna_main("This just keeps getting better and better!","snape_02")
    else:
        call sna_main("Let's uncork that bastard!","snape_02")

    jump snape_hangout_continue



### Events ###

label ss_he_hermione_strip:
    # TAKES PLACE AFTER Hermione has danced for you and Snape.
    call sna_main("So...","snape_31", ypos="head")
    call sna_main("You got the girl to strip for you...","snape_35")
    call sna_main("And you didn't even invite me?!","snape_08")
    m "Well..."
    m "I don't think the girl would be willing to--"
    call sna_main("Those naked, perfectly shaped breasts...","snape_40")
    call sna_main("Those magnificent long legs...","snape_41")
    call sna_main("Her ample and tender behind...","snape_40")
    call sna_main("I've seen everything...","snape_41")
    call sna_main("I've seen it all!","snape_46")
    m "(...)"
    call sna_main("As much of a nuisance I think the girl is...","snape_43")
    call sna_main("{size=+7}I could stare at those tits all day!!!{/size}","snape_33")
    m "..."
    call sna_main("You've got to invite me next time, my friend!","snape_35")
    call sna_main("My life depends on it!","snape_36")

    menu:
        m "..."
        "\"Sure, why the hell not.\"":
            pass
        "\"*Uhh*\"":
            pass

    call sna_main("Splendid!","snape_45")
    call sna_main("I can hardly wait, I tell you!","snape_37")
    call sna_main("Do you think she will let me touch them...?","snape_47")

    ">You spend the rest of the evening in Snape's company talking about Hermione's naked breasts."

    $ ss_he.hermione_strip = True

    hide screen bld1
    with d3
    call notes

    jump day_start



### Snape Narrative ###

label ss_he_story_E1:
    call bld
    m "Alright. Teach me your wand-based magic now."
    call sna_main("Sure, I could do that...","snape_23", ypos="head")
    call sna_main("Or I could tell you some more about those ripe slytherin sluts...","snape_02")
    g9 "The latter, please."
    call sna_main("Great... Get a load of this then...","snape_13")
    pause.1
    call blktone

    ">You spend the evening by discussing all sorts of inappropriate things with Professor Snape."
    ">You feel a faint bond forming between you two..."
    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E2:
    call bld
    m "For our little enterprise to succeed..."
    m "You need to be more generous with these house point things..."
    call sna_main("Right, of course...","snape_09", ypos="head")
    call sna_main("Miss Granger will require a strong incentive...","snape_09")
    call sna_main("So putting my house in the lead is essential...","snape_09")
    call sna_main("Could take time though...","snape_06")
    m "Take time?"
    m "Why not just award a couple of hundred points to Slytherin and be done with it?"
    call sna_main("No, we need to be discreet with this...","snape_24")
    call sna_main("Awarding a whole bunch of points to my house without any reason could draw in unnecessary attention...","snape_05")
    m "*Hmm*... I see your point..."
    call blktone

    ">You spend the evening by conspiring against Hermione with professor Snape..."
    ">The faint bond of friendship between you two strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E3:
    call sna_main("Have you heard of that \"men's rights movement\" nonsense?","snape_01", ypos="head")
    call sna_main("She is smart, popular and has a will of iron...","snape_01")
    call sna_main("Lately I am starting to feel very doubtful about our whole plan...","snape_06")
    m "You shouldn't though..."
    call sna_main("Is that so...","snape_26")
    m "It may take some time, but I {size=+5}will{/size} break her."
    m "Just trust me."
    call sna_main("Alright...","snape_26")
    call sna_main("What choice do I have but to hope for the best...?","snape_06")
    call blktone

    ">You spend the evening by dreading the uncertain future with professor Snape."
    ">A faint bond of trust is forming between you two."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E4:
    call sna_main("Tell me something, Genie...","snape_24", ypos="head")
    m "Yes?"
    call sna_main("Do you believe in the theory of parallel worlds?","snape_25")
    m "Well, it's hard not to. All things considered."
    call sna_main("True...","snape_23")
    call sna_main("So, you think somewhere out there is another version of me?","snape_05")
    m "Probably..."
    call sna_main("*Hmm*...","snape_23")
    call sna_main("Severus Snape - the ever cheerful white mage...","snape_23")
    m "Sure, why not?"
    call sna_main("What unsettling imagery you put into my mind...","snape_03")
    m "How about another version of that Granger girl?"
    call sna_main("Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!","snape_02")
    m "And what if in that other world the cheerful Severus teams up with some bizarre version of me?"
    m "And maybe together we train the slut Hermione to be a proper girl and a good student?"
    call sna_main("Ha-ha-ha! That's hilarious!","snape_28")
    pause.1
    call blktone

    ">You spend the evening by discussing science, metaphysics, philosophy and sluts."
    ">the bond of friendship between you and Professor Snape strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points



label ss_he_story_intro_E5:
    call sna_main("So... How is our little plan coming along?","snape_05", ypos="head")
    call sna_main("Is that wretched girl giving you trouble?","snape_05")

    menu:
        "\"Yeah. She's stubborn.\"":
            call sna_main("No surprise there...","snape_06")
        "\"No, not really...\"":
            call sna_main("Seriously?","snape_05")
            call sna_main("Interesting...","snape_05")

    call sna_main("But you are positive you will be able to break her?","snape_01")
    m "Oh, absolutely."
    m "It may take some time though..."
    call sna_main("Well, we do have time...","snape_06")
    call sna_main("You are still pretty much powerless, right?","snape_05")
    m "Yeah, pretty much..."
    call sna_main("Splendid!","snape_02")
    m "......................."
    call sna_main("I mean, it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?","snape_29")
    m "Right..."
    call blktone

    ">Professor Snape seems to feel awkward about benefiting from your misery..."
    call notes
    ">The bond of friendship between you two strengthens slightly..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_E6:
    call bld
    m "So, tell me about those Slytherin sluts some more!"
    call sna_main("What can I say? Life's been good to me lately, my friend.","snape_23", ypos="head")
    call sna_main("These days I have a whole harem of skimpy students to choose from.","snape_22")
    g9 "Nice!"
    call sna_main("Yes. Thanks to you, I can do whatever the bloody hell I want!","snape_02")
    call sna_main("And more importantly...","snape_02")
    call sna_main("Whoever the hell I want!","snape_13")
    m "Seriously?"
    call sna_main("Well, sort of...","snape_09")
    call sna_main("Obviously I don't actually walk around and \"do whoever I want\"...","snape_09")
    call sna_main("But you wouldn't believe what some of those girls are willing to do in exchange for house points!","snape_13")
    call sna_main("Or even for the mere promise of good grades...","snape_22")
    pause.1
    call blktone

    ">Professor Snape's usual cold exterior disintegrates before your eyes..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E7:
    call sna_main("So, back in your world you are some kind of all-powerful being?","snape_05", ypos="head")
    m "Yeah, sort of..."
    call sna_main("Then how come you do the bidding of that Jasmine woman?","snape_05")
    m "Oh... Well..."
    m "... she is a princess."
    call sna_main("So?","snape_05")
    call sna_main("Is she your princess? You are not even human.","snape_05")
    call sna_main("Did you swear your loyalty to her?","snape_05")
    m "Not really..."
    call sna_main("Why do you even bother then?","snape_06")
    call sna_main("The way I see it, you are an all-powerful being and she is just some muggle...","snape_09")
    m "She's a what?"
    call sna_main("A human... She's just a human...","snape_25")
    call sna_main("So why bother trying to please her?","snape_05")
    m "Well it's complicated..."
    call sna_main("..............","snape_05")
    m ".................."
    call sna_main("She's hot, isn't she?","snape_02")
    m "Smoking..."
    call sna_main("Gotcha.","snape_23")
    pause.1
    call blktone

    ">You and professor Snape share a bittersweet moment of complete male solidarity."
    ">The bond of your friendship strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E8:
    call bld
    call sna_main("Do you think if we wanted to...","snape_05", ypos="head")
    call sna_main("We could bring the public flogging back?","snape_05")
    m "What do you mean?"
    call sna_main("Well, years ago flogging was a completely acceptable measure of punishment for the students.","snape_06")
    call sna_main("*Sigh* Simpler times...","snape_06")
    call sna_main("These days students just completely lack discipline...","snape_16")
    call sna_main("I would like nothing more than to publicly flog every single one of them...","snape_16")
    call sna_main("Especially the girls...","snape_22")
    m "*Hmm*... Fine by me..."
    m "But won't a reform like that attract unnecessary attention towards us?"
    call sna_main("Yes. You are right of course.","snape_29")
    call sna_main("I am getting greedy...","snape_29")
    call sna_main("I'm getting drunk with power, my friend!","snape_28")
    call sna_main("And this exquisite wine does not improve my judgment in the slightest either!","snape_28")
    pause.1
    call blktone

    ">Professor Snape seems to be completely at ease around you now."
    ">The bond of male friendship between you two strengthens even more.\n>Slytherin house point payouts have increased formidably..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E9: # Replace this event.
    call sna_main("... so, after that I return back to Russia, right?","snape_24", ypos="head")
    g4 "Back to Russia?"
    call sna_main("But wait, it gets worse.","snape_01")
    call sna_main("Apparently I am fluent in Russian now.","snape_05")
    g4 "Wait, what?"
    call sna_main("And I am this miserable muggle guy who lives in this shithole of a town full of run-down buildings.","snape_06")
    call sna_main("I try to make a living by drawing comics and creating games with \"Ren'Py\"...","snape_06")
    call sna_main("And that is so bizarre because I don't even know what a \"Ren'Py\" is!","snape_24")
    m "*Hmm*... Then what happened?"
    call sna_main("Not much... Mostly worked my ass off for months...","snape_05")
    call sna_main("Then managed to create a relatively successful game somehow...","snape_05")
    call sna_main("Eventually began to make decent money with my craft...","snape_24")
    call sna_main("And then, just when I was about to allow myself to feel hopeful about the future...","snape_06")
    call sna_main("I woke up...","snape_04")
    call sna_main("....................","snape_09")
    m "......................"
    call sna_main("What do you think all of that means?","snape_05")
    m "Some form of self insert, probably."
    call sna_main("What?","snape_05")
    m "Just ignore the whole thing."
    m "A silly dream, nothing more."
    call sna_main("Felt more like a nightmare...","snape_29")
    pause.1
    call blktone

    ">Professor Snape trusts you more than he used to..."
    ">(To the point where he doesn't think twice about sharing his weird-ass dreams with you)."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E10:
    call sna_main("What is the meaning of life, Genie?","snape_29", ypos="head")
    g4 "What?"
    call sna_main("Since you are an all-powerful being, you've got to know things like that, right?","snape_05")
    m "Maybe..."
    call sna_main("Great. Tell me then.","snape_06")
    m "*Hmm*... You sure you're ready for this?"
    call sna_main("Yes. Lay it on me, friend.","snape_05")
    m "Alright then..."
    call sna_main("................!","snape_01")
    m "It's plastic..."
    call sna_main("I beg your pardon?","snape_05")
    m "it's plastic..."
    call sna_main("I don't get it...","snape_25")
    m "This planet plans to evolve into something else in a million years or so..."
    m "In order to do that it needs a special kind of material that it can't produce on its own."
    m "So it spawns a new form of life - humans."
    call sna_main("..............","snape_11")
    m "You wanted to know the purpose of your existence?"
    m "It's to produce plastic. Simple as that."
    call sna_main("Are you fucking kidding me?!","snape_30")
    call sna_main("No, no... That can't be it...","snape_26")
    g9 "He-he..."
    call sna_main("Are you pulling my leg?","snape_25")
    g9 "You should've seen your face."
    call sna_main("You really had me worried there, you bloody non-human bastard!","snape_15")
    g9 "I know! It was hard to resist..."
    call blktone

    ">You spend the evening by skilfully avoiding a whole variety of similar questions."
    ">Despite your refusal to cooperate the bond of friendship between you two strengthens yet again."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E11:
    call sna_main("So... Back in your world, do you people have a country named England?","snape_05", ypos="head")
    m "We used to..."
    call sna_main("What happened?","snape_26")
    m "\"The great catastrophe\"..."
    m "It incinerated most of the worlds population in a matter of hours..."
    call sna_main("................","snape_26")
    m "Turning about eighty percent of the planet's surface into a scorching desert..."
    m "And the remaining twenty percent into an icy wasteland..."
    m "............."
    call sna_main("That is...","snape_26")
    call sna_main("Horrible...","snape_06")
    call sna_main("Are you sure that you want to return to that place?","snape_25")
    m "Of course."
    m "It may be a bit barbaric, but hey... it's home."
    call blktone

    ">Professor Snape finds a new level of respect for you..."
    ">The bond of friendship between you two solidifies."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E12:
    call sna_main("I've been thinking about what you've said the other day...","snape_09", ypos="head")
    call sna_main("About your home world being nothing but a scorched desert and all...","snape_09")
    m "Yes?"
    call sna_main("Do you think Albus will be alright there?","snape_06")
    m "Oh, absolutely!"
    m "Since I quite literally replaced him in his chair..."
    m "He probably replaced me in exactly the same place back in Agrabah."
    call sna_main("Agrabah?","snape_05")
    m "Yes... A very big city."
    m "One of the few that rose after the great catastrophe."
    m "Probably the biggest of them all as well..."
    m "The heart of the human civilization if you will."
    call sna_main("I am relieved to hear that...","snape_23")
    m "Sure..."
    m "Although if your Albus friend really materialised in exactly the same spot I occupied before I cast the spell..."
    m "I suppose the princess could have him beheaded..."
    call sna_main("WHAT?!","snape_01")
    m "But the probability of that happening is very slim..."
    m "About five percent... Maybe ten... Twenty percent tops."
    call sna_main(".......................................................","snape_03")
    pause.1
    call blktone

    ">Professor Snape seems grateful to you for (sort of) putting his concerns about Albus Dumbledore's well-being to rest..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E13:
    call sna_main("You know what?","snape_01", ypos="head")
    m "What?"
    call sna_main("For the first time in a very long time...","snape_01")
    call sna_main("I think...","snape_03")
    call sna_main("I am actually content with the way my life is going.","snape_25") # 0_0
    call sna_main("What an unsettling feeling...","snape_26")
    m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
    call sna_main("Could be.","snape_22")
    call sna_main("Nonetheless, training that girl had such a great impact on my life...","snape_24")
    call sna_main("And even the school itself...","snape_24")
    m "In other words you are getting less broody and you blame me."
    call sna_main("Something like that...","snape_23")
    call sna_main("I'm losing my dark presence, man.","snape_28") # :)
    pause.1
    call blktone

    ">Professor Snape really did become a little more cheerful lately..."
    ">He even looks younger now than back when you first met him..."
    ">Professor Snape's feeling of gratitude fortifies the bond of your friendship."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_E14:
    call sna_main("... so she says: \"Sir, could you choke me a little, please!\"","snape_02", ypos="head")
    call sna_main("And I am happy to oblige of course!","snape_13")
    call sna_main("So, I choke that little bitch while I'm fucking her, right?","snape_19")
    call sna_main("And she rolls her eyes up to the point where I can't even see her pupils anymore!","snape_19")
    call sna_main("Her face turns to a cute tint of purple and she's barely breathing.","snape_19")
    call sna_main("So I think that maybe I should loosen up my grip a little...","snape_14")
    call sna_main("And that's when the bitch starts to cum!","snape_21")
    m "Sweet! And then you woke up?"
    call sna_main("What? No, it actually happened.","snape_05")
    call sna_main("I finally nailed that blond witch from Slytherin.","snape_13")
    g9 "Nice!"
    call sna_main("I know.","snape_13")
    call sna_main("She is pretty twisted though...","snape_25")
    call sna_main("And I mean really fucking messed up.","snape_26")
    g9 "Our type of girl!"
    call sna_main("Exactly!","snape_22")
    pause.1
    call blktone

    ">You and professor Snape bond over the similarities of your taste in women."
    ">The bond of your friendship has never been stronger."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points


label ss_he_story_intro_E15:
    call sna_main("It's been a while now...","snape_05", ypos="head")
    m "What do you mean?"
    call sna_main("The spell that brought you here...","snape_24")
    call sna_main("You said it would wear off in time...","snape_24")
    call sna_main("Do you feel any different?","snape_05")
    m "No... Not really..."
    m "Maybe it needs more time?"
    call sna_main("Could be...","snape_01")
    call sna_main("Or there could be something else...","snape_01")
    m "Like what?"
    call sna_main("No idea...","snape_09")
    call sna_main("But I shall give this some more thought...","snape_09")
    call sna_main("Oh, and one more thing...","snape_24")
    m "*Hmm*...?"
    call sna_main("This time of the year is usually pretty busy...","snape_24")
    call sna_main("Even more so now when I need to constantly cover up for Albus' absence.","snape_24")
    m "..................."
    call sna_main("I'm not sure how often I will be able to spend my evenings with leisurely drinking wine anymore...","snape_06")
    m "Really?"
    call sna_main("Yes...","snape_06")
    call sna_main("I'll still be around for a quick chat from time to time, but that's about it.","snape_06")
    m "I see..."
    m "I will have to find another way of spending my evenings from now on then..."
    call sna_main("I'm sure miss Granger will be happy to help.","snape_02")
    m "Yes, for as long as Slytherin is in the lead."
    call sna_main("Seriously? She still cares about that?","snape_05")
    m "Very much so."
    call sna_main("Well in that case I shall personally ensure that the Slytherin house gets as many house points as possible.","snape_23")
    pause.1
    call blktone

    ">Your friendship level with professor Snape reached its maximum value."
    ">Congratulations. If this were a \"Dating Sim\" you would be getting the ending with Severus Snape."
    ">The Slytherin house point payout has increased greatly and reached its maximum level as well."

    call hide_blktone

    jump end_snape_hangout_points


label sly_plus:
    call notes
    ">The Slytherin house point payout has increased..."
    return
