

### Snape Intro ###

# First time genie meets snape

label snape_intro_E1:
    call play_music("dark_fog")
    call play_sound("door")

    call sna_chibi("stand","door","base", flip=False)
    with d3
    pause.3

    call bld
    g4 "{size=-3}(An Indigenous life form!?){/size}"
    hide screen bld1

    call chibi_emote("thought", "snape")
    pause 1

    call bld
    m "{size=-3}(looks human enough...){/size}"
    m "{size=-3}(Maybe if I just act cool he'll leave...?){/size}"

    call chibi_emote("hide", "snape")

    call sna_walk("mid", "base")
    pause.2

    call sna_main("","snape_01", xpos="base", ypos="base", trans=d3)
    call ctc

    who2 "Albus... Do you have a moment?"
    hide screen snape_main
    with d3

    menu:
        m "..."
        "\"Actually I'm a bit busy.\"":
            call sna_main("","snape_04", trans=d3)
            who2 "Well, aren't you always, Albus?"
        "\"Of course. What is it?\"":
            call sna_main("","snape_06", trans=d3)
        "\"And Albus to you too.\"":
            call sna_main("","snape_05", trans=d3)
            who2 "What?"
            call sna_main("","snape_04")
            who2 "Albus I'm not in the mood for your... shenanigans."
        "\"Take me to your leader.\"":
            call sna_main("","snape_01", trans=d3)
            who2 "What?"
            who2 "*Hmm*...?"
            who2 "You mean the Minister for Magic?"
            call sna_main("","snape_03")
            who2 "I would rather avoid having to deal with that bureaucrat..."
            m "Fine, never mind... How can I be of help?"

    call sna_main("","snape_06")
    who2 "I have something important I need to discuss with you..."
    who2 "I think we need to revise our admittance policy."
    m "................?"
    call sna_main("","snape_03")
    who2 "Half of my... so-called \"pupils\" are nothing but annoying maggots that make my life miserable on a daily basis."
    m "................"
    call sna_main("","snape_06")
    who2 "Most of them belong to your precious Gryffindor house of course..."
    m "......?"
    call sna_main("","snape_03")
    who2 "The wretched Weasley family, that noisy Granger girl and of course the hero of all the juvenile delinquents around the globe..."
    call sna_main("","snape_08")
    who2 "{size=+3}The Potter boy!{/size}"
    call sna_main("","snape_01")
    who2 "Mark my words, Albus. The Gryffindor house will become this school's undoing!"
    m "...................."
    call sna_main("","snape_01")
    who2 "Nothing but annoying maggots, the lot of them!"
    call sna_main("","snape_06")
    who2 "And if that wasn't enough, now they spread all sorts of nasty rumours about the teachers!"
    who2 "Particularly about yours truly..."
    m "......................"
    call sna_main("","snape_05")
    who2 "You don't believe those rumours, do you Albus?"

    menu:
        m ".............."
        "\"Well, of course not!\"":
            call sna_main("","snape_09")
            who2 "Good..."
            who2 "You know me better than that. I wouldn't care for such things..."
        "\"Where there's smoke, there's fire.\"":
            call sna_main("","snape_10")
            who2 "Albus?! You can't be serious!"
            who2 "Those are nothing but filthy lies, I'm telling you!"

    m "........................."
    call sna_main("","snape_04")
    who2 "Well, those wretched brats left me completely exhausted. I think I will retire for today."
    call sna_main("","snape_09")
    who2 "................"

    stop music fadeout 5.0

    call sna_walk(action="leave")

    call bld
    m "*Hmm*..."
    m "So that tall, broody dude mistook me for someone else...?"
    m "Which means I must be shrouded in a concealment spell..."
    m "........."
    m "So basically, I'm a genie disguised as a human, who is in turn disguised as another human..."
    m "No, that's not stupid at all..."
    call bld("hide")

    $ snape_intro.E1_complete = True
    $ ss_event_pause += 1

    jump day_start


# Event 2

# Sanpe talks to genie about hermione, snape becomes suspicious

label snape_intro_E2:
    call play_music("dark_fog")

    call sna_walk(action="enter", xpos="mid", ypos="base")

    call bld
    m "{size=-3}(That broody guy again...){/size}"
    call sna_main("","snape_01",xpos="base",ypos="base")
    who2 "Albus!"
    m "Hey.......... you..."
    who2 "You need to do something about that Granger girl..."
    call sna_main("","snape_06")
    who2 "Honestly... I'm running out of ways to punish that... that..."
    call sna_main("","snape_04")
    who2 "That little witch!"

    menu:
        m "..."
        "\"Granger? Hermione Granger, right?\"":
            who2 "Yes, her..."
            who2 " She also happens to be a part of the \"Potter gang\"."
        "\"I got your back, Jack, witches be crazy!\"":
            who2 "What...? Albus you behave oddly lately."
            who2 "Is everything alright?"
            menu:
                m "..."
                "\"Yes, I'm fine. Go on.\"":
                    who2 "If you say so..."
                "\"You know me. I love my shenanigans.\"":
                    who2 "*Hmm*....."

        "\".....................................................\"":
            pass

    who2 "Remember how back in the days they used to publicly flog the students?"
    who2 "I swear if we could bring that back all of our problems would be solved..."
    who2 "Yes... I would gladly tie that girl to a flogging pole in front of the entire school..."
    call sna_main("","snape_20")
    who2 "Then lift her skirt up, and..."
    call sna_main("","snape_12")
    who2 "*Khem*! Sadly, nowadays we teachers are severely limited in the disciplinary measures we have at our disposal..."
    who2 "I know you are just as powerless as I am in this matter, but I'm telling you, that girl had better stop testing my patience."

    menu:
        m "..."
        "\"I'll take care of that little whore!\"":
            call sna_main("","snape_05")
            who2 "...?!"
            who2 "Albus..."
            who2 "You are acting strange lately..."
        "\"Nobody ever said this job would be easy.\"":
            call sna_main("","snape_06")
            who2 "Sometimes I feel like I would rather deal with a classroom full of Dementors..."
        "\"You will feel better tomorrow.\"":
            call sna_main("","snape_06")
            who2 "You are probably right..."

    who2 "*Hmm*..."
    call sna_main("","snape_06")
    who2 "Perhaps I'd better go get some sleep."
    who2 "I need to be in my top shape every morning..."
    who2 "You can't show weakness to those brats or they will swallow you whole..."
    call sna_main("","snape_24")
    who2 "Good night, Albus."

    call sna_walk("door", "base")
    pause.2

    who2 "................."

    call sna_chibi("stand","door","base",flip=False)
    with d3
    pause.2

    who2 "One more thing..."
    show screen bld1
    show screen snape_main
    with d3
    who2 "You should ignore any lies you hear about me and those slytherin girls..."
    hide screen snape_main
    with d3
    m "Got it."

    hide screen bld1
    call sna_chibi("stand","door","base",flip=True)
    with d3
    pause.2

    call sna_chibi("leave")

    $ snape_intro.E2_complete = True
    $ ss_event_pause += 1

    jump day_start


# Event 3

# Snape comes in, has a talk with Genie, then the duel starts.

label snape_intro_E3:
    call play_music("dark_fog")

    call sna_walk(action="enter", xpos="mid", ypos="base")

    call sna_main("","snape_01",xpos="base",ypos="base")
    call ctc

    who2 "Good evening, Albus."
    who2 "I want to talk to you about those damn brats again..."
    who2 "But first I want to ask you something..."
    call sna_main("","snape_05")
    who2 "Have you noticed anything strange going on around here lately?"

    menu:
        m "..."
        "{size=-2}\"Like you being especially whiny?\"{/size}":
            who2 "What? B-but..."
            call sna_main("","snape_06")
            who2 "Well, perhaps you are right..."
        "{size=-2}\"That owl is fetching my mail, man!\"{/size}" if owl_away_counter != 0:
            who2 "An owl? What about it?"
            call sna_main("","snape_25")
            who2 "That's not what I mean..."
            call sna_main("","snape_29")
            who2 "Well, never mind..."
        "{size=-2}\"No, not really. It's just business as usual.\"{/size}":
            who2 "*Hmm*... Maybe I'm just being paranoid..."

    call sna_main("","snape_24")
    who2 "The reason why I'm here today is the \"Potter Gang\"."
    call sna_main("","snape_01")
    who2 "There are only so many points I can subtract from the Gryffindor house, you know..."
    who2 "And the Granger girl became the worst of them lately..."
    call sna_main("","snape_06")
    who2 "She practically leads the onslaught."
    call sna_main("","snape_05")
    who2 "Speaking of which, has she been sending you any letters lately?"

    menu:
        m "..."
        "\"Hermione Granger? No, Nothing from her.\"":
            who2 "I see... So she's been bluffing then."
            call sna_main("","snape_16")
            who2 "What an annoying witch."
        "\"Yes... Every damn day...\"" if letter_hg_2.read:
            who2 "Really now?"
            who2 "Any lies about me in particular?"
            who2 "I hope you know better than to listen to the likes of her..."

    call sna_main("","snape_03")
    who2 "She would never admit it, but I know she's been spreading those nasty rumours about me around the school..."
    call sna_main("","snape_29")
    who2 "*Tsk*... Noisy little...... witch."
    call sna_main("","snape_09")
    who2 "I would never stoop so low as to trade house points in exchange for sexual favours..."
    who2 "I mean, sure, we use house points to motivate students, but that's completely different..."
    who2 "I can't speak for the rest of the staff though..."
    call sna_main("","snape_13")
    who2 "The stories I hear about Minerva McGonagall and those poor Gryffindor freshmen may be true..."
    call sna_main("","snape_01")
    who2 "Well, I just wanted to make sure that you take those rumours about me for what they are..."
    who2 "Nasty lies made up by a bunch of spoiled--"

    who2 "Oh.... Before I go..."
    who2 "There is one thing I meant to ask you for a while now..."
    call sna_main("","snape_09")
    who2 "........................."
    call sna_main("","snape_05")
    who2 "What is my name?"

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    menu:
        m "..."
        "\"What? What kind of question is that?\"":
            call sna_main("","snape_06")
            who2 "You are right..."
            who2 "Forgive me... I'm just being paranoid I suppose..."
            call sna_main("","snape_05")
            who2 "But you can never be too cautious with rumours about  \"you know who\" still being alive and all..."
        "\"Tall broody guy?\"":
            call sna_main("","snape_06")
            who2 "Albus, lately you adopted a peculiar sense of humour, that I do not care for in a slightest..."
            who2 "Maybe you should spend a little less time in the company of that big oaf Hagrid."
        "-Use magic to get the right answer-":
            $ d_flag_01 = True
            hide screen snape_main
            with d3
            call nar(">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer.")
            call sna_main("","snape_03")
            who2 "!!?"
            m "What kind of question is this, Severus?"
            who2 "Forgive me... I'm just being paranoid I suppose..."

    call sna_main("","snape_06")
    who2 "Well, good night, Albus."

    call sna_walk("door", "base")
    pause.2

    stop music fadeout 1.0
    call bld
    who2 "........................"

    # Hide Snape chibi and fade to black
    hide screen snape_chibi
    show screen blkfade
    with d3

    $ renpy.play('sounds/07_run.mp3')
    pause 2
    g4 "???"

    show screen snape_defends
    hide screen bld1
    call hide_blkfade

    call play_music("hitman") #TENSE THEME
    call ctc

    call bld
    if d_flag_01:
        call sna_main("Who are you, scum!","snape_34", ypos="head", wand=True)
        g4 "What? It's me... *Ehm*... {i}Abius{/i}! I mean, Albus!"
        call sna_main("You cannot fool me.","snape_32", wand=True)
        call sna_main("Just now, you used some sort of alien magic!","snape_32", wand=True)
        call sna_main("Reveal your true self to me now, fiend! Who are you?!","snape_34", wand=True)
    else:
        call sna_main("My name is Severus Snape!", ypos="head", wand=True)
        call sna_main("Now, who might you be...?","snape_01", wand=True)

    g4 "!!!"
    call sna_main("Easy now... Just answer my question.","snape_01", wand=True)
    m "Alright, alright. Just calm down, would you?"
    call sna_main("........","snape_01", wand=True)

    label no_wait:
    menu:
        m "..."
        "\"I am not your enemy.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            call sna_main("That's the first thing an enemy would say.","snape_01", wand=True)
        "\"I'm just a tourist. I'll be leaving now.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            call sna_main("You are not going anywhere.","snape_01", wand=True)
        "\"I work for {i}Albis Doomblebore{/i}!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            call sna_main("It's Albus Dumbledore, you moron!","snape_01", wand=True)

    if d_points == 2:
        pass
    else:
        jump no_wait

    call sna_main("Who sent you here? What did you do with the real \nAlbus?","snape_01", wand=True)
    call sna_main("Shed your disguise and reveal your true self at once, \nthis is your last warning!","snape_01", wand=True)

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label no_wait_2:
    menu:
        m "..."
        "\"I can't. It's hard to explain...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            call sna_main("I have no interest in your explanations. I wouldn't \nbelieve a single word you'd say anyway!","snape_01", wand=True)
        "\"Stop threatening me, human!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            call sna_main("\"Human\"?","snape_01", ypos="head", wand=True)
            call sna_main("Are you implying that you are {size=+5}not{/size} one?","snape_01", wand=True)
            call sna_main("What are you then?! Dispel your cloaking charm immediately or else!","snape_01", wand=True)
        "\"I mean you no harm, I swear!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            call sna_main("Is that so?","snape_01")
            call sna_main("Prove it then. Dispel your cloaking charm now!","snape_01", wand=True)

    if d_points == 2:
        pass
    else:
        jump no_wait_2

    call sna_main("I've heard enough!","snape_01", wand=True)
    g4 "By the great desert sands! Would you let me explain, human?!"
    call sna_main("There is nothing left to explain!","snape_01", wand=True)
    call sna_main("Since you refuse to cooperate, I'll be taking you \ninto custody by force!","snape_01", wand=True)
    g4 "What?! Wait!"

    $ snape_intro.E3_complete = True
    if skip_duel == True:
        $ snape_intro.duel_complete = True
        jump snape_lost

    stop music
    call play_music("boss")
    call play_sound("glass_break")

    pause.1

    hide screen bld1
    show screen snape_glass
    $ renpy.pause(2.3, hard=True)

    jump duel


# Event 4

# THE TALK AFTER THE DUEL ENDS.

label snape_intro_E4:
    $ potions = 0 #Makes sure there are no potions left in the possessions.

    stop music fadeout 2.0

    call bld
    g4 "*Panting*"
    g4 "Ready to talk now?!"
    call sna_main("(... i-impossible...)","snape_36", ypos="head")

    call play_music("dark_fog")

    m "I told you that you're no match for me..."
    m "You did give me a good run for my money though..."
    call sna_main("The way you conjure the spells with your bare hands...","snape_01")
    call sna_main("No human could do that... who--","snape_01")
    call sna_main("{size=+5}What are you?{/size}","snape_32")
    call sna_main("Some sort of shapeshifting demon summoned by \"you know who\"?","snape_01")
    m "Summoned by whom?"
    call sna_main("By \"you know who\"!","snape_31")
    m "What?"
    call sna_main("......................","snape_35")
    m "............................"
    m "Listen, I'm not a demon..."
    m "And I sure as heck don't work for \"I don't know who\"!"
    call sna_main(".............................","snape_01")
    m "I've been *Ehm*..."
    m "... Conducting an experiment back in my world, during which something went wrong and I ended up here."
    m "That's all..."
    call sna_main("..........................","snape_01")
    call sna_main("What became of the real Albus Dumbledore then?","snape_01")
    m "I'm sure he is fine."
    m "He's Probably feeling as surprised about finding himself in my world as I am about finding myself here..."
    call sna_main("....................................","snape_01")
    call sna_main("When did this happen?","snape_01")
    m "Four days ago..."
    call sna_main("Can you go back?","snape_01")
    m "I think so..."
    call sna_main("Why didn't you then?","snape_31")
    m "Not sure..."
    m "The Magic of this world is so bizarre... Perhaps I just got curious."
    call sna_main("...................","snape_01")
    call sna_main("You need to fix this...","snape_01")
    m "Fix what?"
    call sna_main("Everything. You need to bring back Albus and leave our world.","snape_32")

    menu:
        m "..."
        "\"Yes, yes, I know. Off I go then.\"":
            m "Yes, yes, I know..."
            m "Well, off I go then. Sorry for the ruckus."
            call sna_main("No harm done...","snape_01")
        "\"But I like it here! Can't I stay?\"":
            call sna_main("Absolutely not.","snape_01")
            call sna_main("Whoever you are, you are not from this plane of existence.","snape_01")
            call sna_main("Your very presence here upsets the natural order of things.","snape_01")
            call sna_main("And these days this school needs a proper headmaster more than ever.","snape_01")

    call sna_main("Have a safe trip home now.","snape_01")
    m "*Ehm*... Thank you, mister Severus. Good luck with your students and the \"potter gang\"."
    call sna_main("\"The potter gang\"?","snape_01")
    call sna_main("Oh, right, those buggers...","snape_35")

    menu:
        "-Undo the spell-":
            $ renpy.play('sounds/fire_woosh.mp3')
    menu:
        "-Undo the spell-":
            $ renpy.play('sounds/fire_woosh.mp3')
    menu:
        "-Undo the spell-":
            $ renpy.play('sounds/fire_woosh.mp3')

    m "(Something's not right, I can't undo the spell...)"
    call sna_main("Did it work? Albus, is that really you?","snape_01")

    menu:
        m "..."
        "\"Yeah, that's me. So good to be back!\"":
            call sna_main("Glad to have you back, old friend. Are you alright?","snape_01")
            m "I'm fine, Severus, thank you."
            call sna_main("How was it, in that other world?","snape_01")
            m "A lot of sand and very hot, but other than that quite pleasant."
            call sna_main("I see... Did you miss your brother?","snape_01")
            menu:
                m "..."
                "\"Yes, I missed you so much!\"":
                    call sna_main(".......................","snape_01")
                    call sna_main("Yeah, right...","snape_01")
                "\"I don't have a brother, Severus.\"":
                     call sna_main("........................","snape_01")
                     call sna_main("You may not have one, but the real Albus Dumbledore does.","snape_01")
                "-Use magic to get the right answer-":
                    call nar(">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer.")
                    m "My little brother Aberforth? Why would I miss him?"
                    call sna_main("I can feel it whenever you use your alien magic...","snape_01")

        "\"Nope. It's still me. The non-human guy.\"":
            pass

    call sna_main("Why are you still here, creature?","snape_01")
    m "I'm not sure... I tried to undo the spell but nothing happened..."
    call sna_main("Marvellous...","snape_35")
    call sna_main("What does this mean? So You're staying here for good?","snape_01")
    m "Of course not..."
    m "Me being here at all is only possible because the spell is compensating for the unbalance caused by itself..."
    m "said spell will wear off eventually and I shall be pulled back into my world."
    m "Likewise, your Dumbledore-friend shall be pulled back here."
    call sna_main("I see...","snape_01")
    call sna_main("How long until the spell wears off?","snape_01")

    menu:
        m "..."
        "\"A couple of days.\"":
            call sna_main("I see...","snape_01")
        "\"A week or so...\"":
            call sna_main("*Hmm*.... A week, huh...","snape_01")
        "\"Could be months...\"":
             call sna_main("That long?","snape_01")
             call sna_main("Now isn't that just \"perfect\"?","snape_01")
        "\"I have no clue...\"":
            call sna_main(".....................","snape_01")
            call sna_main("Splendid...","snape_31")

    m "Alright, to be honest I'm not sure where to go from here..."
    m "All this time I thought I could undo the spell whenever I wanted to..."
    call sna_main("...................................................","snape_01")
    call sna_main("..................................","snape_01")
    call sna_main("...................","snape_01")
    m "Snape?"
    call sna_main("...................................................","snape_01")
    m "Severus?"
    call sna_main("Yes, yes...","snape_34")
    call sna_main("Listen, it's very late, and too much has happened already...","snape_01")
    call sna_main("I need to process all of this.","snape_35")
    call sna_main("I will come to see you tomorrow, after my classes.","snape_01")
    call sna_main("Until then, keep your true identity and our conversation a secret, alright?","snape_34")
    m "Not a problem."
    call sna_main("Alright then...","snape_01")
    call sna_main("But before I go, I have one more question...","snape_01")
    m "I'm listening..."
    call sna_main("........","snape_31")
    call sna_main("If you are not a human, then...","snape_01")
    call sna_main("What are you?","snape_35")
    m "... I'm a genie."
    call sna_main("A genie?","snape_01")
    m "Yes, I possess phenomenal cosmic powers and all that..."
    call sna_main("Seriously?","snape_01")
    m "Oh, yes."
    call sna_main("Unbelievable...","snape_01")
    call sna_main("Well, I'll see you tomorrow.... genie.","snape_01")
    m "I'll be here..."

    call sna_main("(A genie? Now that's new...)","snape_35")

    hide screen duel
    $ snape_intro.E4_complete = True

    jump day_start


# Event 5

# Snape visits you after the dual (next evening).

label snape_intro_E5:
    call play_music("dark_fog")

    call sna_walk(action="enter", xpos="mid", ypos="base")

    call sna_main("","snape_01",xpos="base",ypos="base")

    sna "..................."
    m "Good evening..."
    sna "Is the spell still in effect?"
    m "Yes. very much so."
    sna "I see..."
    sna "Last night I gave our little.... conundrum some thought."
    sna "And I think I came up with a solution..."
    m "Really? Great! I'm listening."

    call sna_main("Let's just roll with it...","snape_29")
    m "Excuse me?"
    call sna_main("Well what else could we do?","snape_06")
    sna "Normally I would alert the ministry of magic and let them take care of this mess..."
    sna "But I'd rather avoid any dealings with those rotten bureaucrats this time..."
    call sna_main("Also, losing a headmaster, even temporarily, could hurt the school's reputation...","snape_10")
    sna "And what if your spell wears off tomorrow, or even tonight?"
    call sna_main("I see no reason to start a commotion...","snape_09")
    m "*Hmm*..."
    call sna_main("So we shall keep the charade going for now...","snape_03")

    m "By doing what exactly?"
    call sna_main("Just act like Albus always does: never leave this tower and try to avoid any human contact...","snape_05")
    m "That..."
    m "Sounds..."
    g4 "Incredibly boring!"
    g4 "What am I supposed to do here?"
    call sna_main("You are a Genie. Conjure up some sort of entertainment for yourself.","snape_01")
    m "My magic doesn't seem to be working properly here for some reason..."
    m "And my lamp is literally worlds away..."
    call sna_main("Well, what do you expect me to do about that?","snape_03")
    sna "Send you a couple of girls from Slytherin maybe?"
    g9 "I have no idea what Slytherin is, but I think that would work..."
    call sna_main("That was a joke, obviously.","snape_04")
    call sna_main("Although...","snape_09")
    sna "*Hmm*..."
    call sna_main("Well, in any case, I don't see how entertaining {size=+7}you{/size} is {size=+7}my{/size} problem.","snape_01")
    m "Oh, but it is!"
    m "I'm immortal and all-powerful..."
    m "Being bored is one of the worst things that could happen to me!"
    g4 "And I have a thing against being cooped up in small spaces with nothing to do!"
    g4 "I may lose my mind..."
    g4 "Oh! Ah! I think it's happening already!"
    call sna_main(".......","snape_03")
    g4 "I'm losing my mind! It's getting hard to breathe!"
    call sna_main("....","snape_04")
    g4 "It's so dark..."
    g4 "Are you still here?"
    call sna_main("....","snape_03")
    m "........."
    call sna_main("Are you done?","snape_10")
    m "Yes..."
    m "Seriously though, I don't see how this whole affair benefits me at all."
    call sna_main("Do you have any choice?","snape_01")
    m "I do..."
    m "Instead of sitting here on my ass all day and being quiet I could explore your world..."
    call sna_main("*Hmm*...","snape_03")
    call sna_main("Well, alright, what do you want?","snape_01")
    m "Teach me your magic..."
    call sna_main("My magic?","snape_05")
    m "Yes... The way you conjure up your spells is..."
    m "Intriguing..."
    call sna_main("*Hmm*...","snape_04")
    call sna_main("Agreed.","snape_06")
    m "Oh, and send me some of those Slytherin girls as well.."
    call sna_main("...............","snape_05")
    sna "........................."
    call sna_main("Ha-ha-ha!!!","snape_28")
    m "What? What did I say?"
    call sna_main("A-ha-ha-ha-ha...","snape_28")
    call sna_main("No, no, my apologies...","snape_02")
    sna "It's just that to me you still look and sound like Albus..."
    sna "To hear Professor Dumbledore say things like \"Send me some of those girls\"..."
    call sna_main("It's hysterical... ","snape_22")
    call sna_main("But you wouldn't understand...","snape_09")
    m "Heh..."
    g9 "Send those whores up, Severus. I'm feeling lonely tonight."
    call sna_main("Ha-ha-ha! Stop it, you're killing me!","snape_28")
    sna "A-Ha-ha-ha!"
    m "No, I'm serious... Is it possible?"
    call sna_main("*Hmm*...","snape_02")
    sna "We'll see..."
    sna "You being our new headmaster presents me with interesting possibilities..."
    sna "I need some time to figure out how to use this situation to my advantage."
    m "You mean {size=+7}our{/size} advantage, right?"
    call sna_main("Oh, yes. Yes, of course...","snape_06")
    sna "Well, I think we are done for today..."
    call sna_main("Good night... genie.","snape_24")
    m "Yes. Good night, Severus."

    call sna_walk("door", "base")
    pause.2

    call sna_main(".................","snape_06", ypos="head")
    call sna_main("\"Send those whores up, Severus!\" Ha-ha-ha..","snape_28")

    call sna_chibi("leave")

    call bld
    m "*Hmm*... "
    m "I Suppose I'll just curl up in a ball on top of this desk as usual..."
    pause.2

    $ snape_unlocked = True
    # Silently add an achievement, then display a popup message.
    $ achievement.unlock("unlocksna", True)
    call popup("{size=-4}You can now summon Snape into your office.{/size}", "Character unlocked!", "interface/icons/head/snape.webp")
    $ snape_intro.E5_complete = True

    call tutorial("hangouts")

    jump day_start
