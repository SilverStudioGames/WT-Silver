
### Hermione Intro ###

### Event 1 ###
# Fist visit of Hermione.

label hermione_intro_E1:
    stop music fadeout 1.0
    pause 1

    # Force default outfit for first event.
    $ hermione.equip(her_outfit_default)

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "*huh*?"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    pause.7

    m "Somebody is knocking on the door..."
    m "Crap... I'm supposed to avoid any human contact!"
    m "*Hmm*... What are the chances that the thing knocking on my door is not human?"
    m "Yeah, quite slim..."

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "Persistent little bastard..."

    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.

    menu:
        m "..."
        "\"Who is it?\"":
            $ d_flag_01 = True
            call bld
            femv "It's me, professor..."
            femv "Hermione Granger. Can I come in?"
            m "{size=-4}(It's that woman who's been harassing me with her letters lately...){/size}"

            menu:
                m "..."
                "\"Go away, please. I'm busy.\"":
                    call bld
                    her "But, professor, I really need to talk to you..."
                    m "..........................................."
                    her "Professor? I'm coming in!"
                    m "{size=-4}(Crap...){/size}"
                "\"Yes, yes, you can come in.\"":
                    pass

        "\"Come in!\"":
            pass
        "\"Go away!\"":
            call bld
            femv "But, professor, I really need to talk to you..."
            m "..........................................."
            femv "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"
        "\"................\"":
            call bld
            femv "Professor, are you there?"
            m "{size=-4}(Go away...){/size}"
            femv "Professor, I really need to talk to you..."
            m "..........................................."
            her "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"

    call bld("hide")
    pause.2

    call play_sound("door")
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call bld
    if d_flag_01:
        g9 "{size=-3}(This is the Granger girl? Well, well, well.){/size}"
    else:
        m "A girl?!!"

    call her_walk("mid", "base")
    pause.5

    call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
    call ctc

    call her_main("Good morning, professor.", "normal", "base", "base", "mid")

    menu:
        "\"Good morning, Hermione.\"" if d_flag_01:
            call her_main("{size=-4}(At least he remembers my name.){/size}", "base", "base", "base", "mid")
        "\"Good morning... girl.\"" if not d_flag_01:
            call her_main("{size=-4}(\"Girl\"?){/size}", "normal", "squint", "worried", "mid")
        "\"Good morning, child.\"":
            call her_main("{size=-4}(\"Child\"...?){/size}", "upset", "narrow", "worried", "mid")
        "\"Greetings fellow human!\"":
            call her_main("Are you alright, professor?", "normal", "squint", "worried", "mid")
            m "Why, of course, I'm a human after all!"
            call her_main("...", "normal", "base", "low", "mid")
            call her_main("Are you sure, professor? I can call for madam Pomfrey to examine you...", "open", "base", "worried", "mid")
            $ renpy.sound.play("sounds/punch01.mp3")
            with hpunch
            g4 "{size=+4}NO!{/size}"
            pause 1.0
            m "Err...{w=0.5} I mean, no thank you dear child, it won't be necessary."
            call her_main("If you say so, professor...", "annoyed", "base", "worried", "L")
            call her_main("*clears throat*", "normal", "closed", "base", "mid")
        "\"................................\"":
            call her_main("...........", "normal", "base", "base", "mid")
            m "................................."
            call her_main(".....*ahem*......", "open", "closed", "angry", "mid")

    call play_music("chipper_doodle")

    call her_main("I am very busy with my class schedule, but I kept my morning free today so that I could see you, professor.", "open", "closed", "base", "mid")
    her "You probably know why I am here too."
    call her_main("The issue I have been fruitlessly trying to bring to your attention lately.", "open", "closed", "angry", "mid")
    her "I cannot understand why you are not acting to stop that nonsense, professor!"
    her "This simply cannot continue!"
    call her_main("The inequality is starting to affect all of the houses...", "open", "base", "base", "mid")
    her "Simply because Gryffindor has more integrity than the rest..."
    her "Do you think it's fair that the people who deserve to be in the lead are being pushed back instead?"
    her "Do you think that's fair, professor? Do you?"
    call her_main("", "normal", "base", "base", "mid")
    m "{size=-4}(Would you look at that pretty little thing?){/size}"
    m "{size=-4}(Look at her going on and on about something... She's adorable.){/size}"
    m "{size=-4}(Damn, I haven't seen a woman in weeks.){/size}"

    menu:
        "\"(I will jerk off a little while she talks.)\"":
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.5

            show screen bld1
            call nar(">You reach under the desk and grab your cock...")

            $ her_jerk_off_counter += 1
            $ jerked_off_during_hermione_intro = True #Affects next conversation with Snape.
            $ masturbating = True

        "\"(No, that's stupid! I Need to behave!)\"":
            $ masturbating = False

    m "Yes, keep on going, dear."
    call her_main("\"Yes\"?! So you think it's fair?", "angry", "base", "angry", "mid")
    m "Oh, of course not, I meant \"no\". But keep on going anyway..."
    call her_main("That's a relief. I'm glad that you agree with me, professor...", "soft", "closed", "base", "mid")
    call her_main("As I was saying, the whole issue is simply ridiculous and I cannot believe that it is taking place in our day and age!", "open", "closed", "angry", "mid")

    if masturbating:
        call nar("*Fap-fap-fap*","start")
        call nar(">You keep on stroking your cock...","end")
    else:
        m "I see..."

    call her_main("I mean, I would understand if something like this were to occur during the middle ages...")
    her "But we left the middle ages behind a long time ago, did we not?"

    if masturbating:
        g9 "{size=-4}(Would you look at those rosy cheeks? I want to poke 'em with my cock.){/size}"
        call nar(">You keep stroking your cock...")
    else:
        m "*Ehm*... I suppose you did. I mean, we did."

    call her_main("So it hurts the whole house point distribution system.")
    her "But it doesn't even stop there!"
    her "It hurts our entire educational system as well..."
    her "And more importantly, the motivation among students is steadily decreasing due to it!"

    if masturbating:
        m "{size=-4}(Look at those huge knockers on you, girl!){/size}"
        m "{size=-4}(Yes... I want to squeeze my dick between them...){/size}"

    her "As you can see, the situation is dire..."
    call her_main("But we can still set everything right...", "open", "base", "base", "mid")
    her "As the president of our school's Student Representative Body..."
    her "I have a few suggestions on how to do that more efficiently."

    if not masturbating:
        m ".............."

    her "First of all, the house point system needs to be maintained!"
    call her_main("You need to control the point distribution better, sir.", "open", "base", "base", "mid")

    if masturbating:
        g4 "{size=-4}(Yes, you are a whore... A nasty little whore... I bet you love to suck cocks... Don't you? Yes, I bet you do...){/size}"
        call nar(">You stroke your rock-hard cock ferociously!")

    her "Of course you agree with me on this, professor, do you not?"

    if masturbating:
        g4 "{size=-4}*Panting heavily*{/size}"
        call her_main("Professor...?", "normal", "squint", "angry", "mid")
        g4 "{size=-4}(Crap. What does she want now?){/size}"
        g4 "Yes, it's all true. Please keep going..."
        her "*Ehm*... So, as I was saying..."
        m "{size=-4}(Oh... That was a good jerk-off session, but I'm getting dangerously close to the \"grand finale\".){/size}"
        m "{size=-4}(Maybe I should stop before I get myself into trouble.){/size}"

        menu:
            "\"(Yes, time to actually listen to her.)\"":
                $ masturbating = False

                call hide_characters
                hide screen bld1
                with d3

                call gen_chibi("sit_behind_desk")
                with d3
                pause.5

            "\"(No! I want to keep on jerking off!)\"":
                m "Yes, yes! *pants*"

    if not masturbating:
        m "{size=-4}(Do I? I honestly don't give a damn...){/size}"
        m "*Err*... I suppose I do..."
        call her_main("{size=-4}(\"Suppose\"?){/size}", "annoyed", "base", "base", "mid")
        call her_main("{size=-4}(When did Professor Dumbledore become so... apathetic?){/size}", "annoyed", "base", "worried", "R")

    call her_main("Another measure you could take into consideration is tightening your control over the staff...", "open", "closed", "angry", "mid")
    her "Especially the teachers..."
    call her_main("I hope I'm not stepping out of line here, sir, but some of the teachers really do require supervision...", "normal", "base", "base", "mid")

    if masturbating:
        g4 "{size=-4}(Yes! You little whore! You little fucking whore!) *Panting*{/size}"
    else:
        m "......................."

    call her_main("I understand that you may not have time for this, professor. After all, you are the headmaster of our school, and a very busy man.", "open", "closed", "angry", "mid")
    her "Being a top student is hard on me as well, sometimes..."

    if masturbating:
        g4 "{size=-4}(She said \"hard-on\"!) *Panting*{/size}"

    her "But you could delegate that task to me..."
    her "Just put your faith in me, professor."

    if masturbating:
        call her_main("Yes, you can do it! Just put it in me, sir!", "base", "base", "base", "mid")
        stop music fadeout 1.0

        g4 "{size=-4}(Oh crap, that did it!) *Argh!*{/size}"
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.2

        call cum_block

        call gen_chibi("cum_behind_desk")
        with d3
        pause 3

        call her_main("Professor?! What is going on...?", "angry", "wide", "base", "mid", trans=d3)

        g4 "*Ah*... YESSSSS.....!"
        call cum_block
        her "...???"
        g4 "*breathing heavily* Yes! yes..."

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.5

        m "Yes, girl. It's all exactly as you say and I will.... take care of it all."
    else:
        m "Alright... I will think about your proposal, I promise."

    call play_music("chipper_doodle")

    call her_main("Really?", "normal", "squint", "angry", "mid")
    her "*Hmm*..........."

    call her_main("That's a relief! Thank you, professor.", "open", "closed", "angry", "mid")

    if masturbating:
        m "No, no, thank you..."
        call her_main("*Hmm*...", "normal", "squint", "angry", "mid")

    call her_main("My classes are about to start, so I'd better go now.", "open", "closed", "angry", "mid")
    call her_main("Thank you for your time...", "base", "base", "base", "mid")
    call her_main("Have a good day, professor.", "base", "base", "base", "mid")

    call her_walk(action="leave")

    if masturbating:
        m "{size=-4}(This was awesome...) *Panting*{/size}"
        m "{size=-4}(My trousers are ruined though...){/size}"
    else:
        m "................."
        m "(She is cute, but quite a piece of work...)"

    call gen_chibi("sit_behind_desk")
    with d3

    $ snape_busy = True # No point in calling him during the day.
    $ hermione_intro.E1_complete = True

    jump end_hermione_event


### Snape Hangout Event 1 ###
# Snape shares his opinion of Hermione with you.

label ss_he_hermione_E1:
    call sna_main("...........................","snape_31", ypos="head")
    m "...............................?"
    call sna_main("I hate her so much...","snape_08")

    menu:
        "\"Yeah! That bitch!\"":
            call sna_main("Good to know that we are on the same page...","snape_01")
            call sna_main("That girl...","snape_31")
        "\"You hate who?\"":
            call sna_main("Why would you ask that?","snape_01")
            call sna_main("That Hermione girl of course!","snape_01")
        "\"Is she that bad?\"":
            call sna_main("She is the worst!","snape_01")

    call sna_main("A top student...","snape_31")
    call sna_main("Leads all sorts of extracurricular activities and clubs...","snape_08")
    call sna_main("the president of the school's Student Representative Body...","snape_08")
    call sna_main("Likely to become the head girl soon...","snape_08")
    call sna_main("................","snape_31")
    call sna_main("............","snape_08")
    with hpunch
    call sna_main("{size=+7}I hate that fucking witch!!!{/size}","snape_33")
    g4 "{size=-4}(What the...?){/size}"
    call sna_main("..............","snape_31")
    call sna_main("She used to be just an annoyance, but these days...","snape_31")
    call sna_main("She's become a full-fledged menace...","snape_01")
    call sna_main("That witch is officially my least favourite student in the entire school now...","snape_01")
    m "What about that Potter boy?"
    call sna_main("The Potter boy? Ha! Who's that!?","snape_34")
    call sna_main("No, I'm serious...","snape_01")
    call sna_main("I will go as far as to say that Potter and his wretched father combined...","snape_01")
    call sna_main("Have never caused me as much grief as this little witch does lately...","snape_01")
    m "Now, now. We both know that's not true..."
    call sna_main("Yeah... You're probably right...","snape_31")
    call sna_main("That bastard James Potter really did a number on me--","snape_35")
    call sna_main("Wait, how do you know this?","snape_34")

    menu:
        "\"Well... I've read the books...\"":
            call sna_main("What? What books?","snape_34")
            m "Nah, never mind. I'm a genie, remember? I know things..."
            call sna_main("*Hmm*... And yet you need me to teach you stuff...","snape_37")
            m "Well, I told you. My magic is acting up in your world..."
            call sna_main("Sure, sure...","snape_37")
            m "......"
        "\"You mentioned the potter boy earlier.\"":
            call sna_main("I did? I don't remember.","snape_05")
            call sna_main("No matter.","snape_09")

    m "She came by the other day, by the way..."
    call sna_main("Who did?","snape_38")
    m "The Hermione girl..."
    call sna_main("What?!","snape_01")
    call sna_main("I thought we agreed on the \"no human contact\" rule.","snape_31")
    call sna_main("(Even though lately I've been wondering whether or not she is human at all...)","snape_35")
    m "I know... She kinda forced her way in..."
    call sna_main("I imagine she did...","snape_01")
    call sna_main("What did she want?","snape_01")

    if jerked_off_during_hermione_intro:
        m "I'm not sure..."
        call sna_main("...?","snape_39")
        m "I was jerking off the entire time she was talking..."
        call sna_main("You've been...","snape_31")
        call sna_main("... doing what?","snape_14")
        m "Hey, don't judge me!"
        m "You don't know what it's like to be cooped up in this tower like a prisoner!"
        call sna_main("You... y-you...","snape_12")
        call sna_main("*snickers*......","snape_13")
        call sna_main("*Ha*... *ha-ha*... *HA-HA-HA*!!!","snape_28")
        m "Wha--? What did I say?"
        call sna_main("*Ha-ha-ha*! You are amazing!","snape_42")
        call sna_main("Are all genies so... wonderfully nihilistic?","snape_42")
        m "Yeah... We immortals tend to not give a fuck."
        call sna_main("Understandable...","snape_37")
        call sna_main("Unfortunately, us mere mortals cannot afford such a luxury...","snape_39")
    else:
        m "Not sure... She was talking a lot..."
        m "Something about some {i}grief-n-door{/i} points... and..."
        m "Er... I wasn't paying attention to be honest..."
        call sna_main("Nah... Probably another load of self-righteous crap...","snape_01")
        call sna_main("She is famous for that...","snape_35")

    call sna_main("I have a class early tomorrow, so let us call it a night.","snape_01")
    m "What about you teaching me magic and stuff?"
    call sna_main("Yeah, absolutely...","snape_38")
    call sna_main("Next time...","snape_38")
    m "Alright..."

    "> Your meeting comes to an end, and you decide to go to sleep."

    $ ss_he.hermione_E1 = True

    jump end_snape_hangout_points

### Event 2 ###
# Second visit from Hermione. Says she sent a letter to the Minestry.
# Takes place after first special event with Snape, where he just complains about Hermione.

label hermione_intro_E2:
    stop music fadeout 3.0
    call play_sound("knocking")
    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            m "(It's that witch again...)"
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $ achievement.unlock("knock")
                    $ hg_event_pause += 1
                    jump main_room

                "\"Of course. Come on in.\"":
                    pass

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            $ achievement.unlock("knock")
            $ hg_event_pause += 1
            jump main_room

        "\"Yes, come in.\"":
            pass

        "\"...................................\"":
            call play_sound("knocking")
            "*Knock-knock-knock*!"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    # Let Hermione in.
    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    call play_music("chipper_doodle")
    call her_main("", "normal", "base", "base", "mid", xpos="base", ypos="base")
    call ctc

    call her_main("Good morning, professor Dumbledore.", "open", "closed", "angry", "mid")

    menu:

        "\"Good morning, child.\"":
            call her_main("{size=-4}(Again with the \"child\"...){/size}", "annoyed", "squint", "angry", "mid")
            call her_main("Sir, I would appreciate it if you would treat me as an equal...", "open", "closed", "angry", "mid")
            m "{size=-4}(I'm literally millions of years older than you, witch. We are anything but equal.){/size}"
            m "...................."
            call her_main("................", "annoyed", "squint", "angry", "mid")
        "\"Good morning, miss Granger.\"":
            her "*Ehm*... so, about the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            call her_main("................", "annoyed", "squint", "angry", "mid")

    her "I see that no matter what I do I simply cannot get through to you, sir."
    call her_main("So in light of your negligence, I decided to take the initiative myself!", "open", "closed", "angry", "mid")
    m "Did you now...?"
    her "Yes! We, the proud students of Hogwarts, detest sexism..."
    her "No individual shall be treated differently based on his or her gender."
    m "But--"
    call her_main("Please, let me finish, professor!", "angry", "base", "angry", "mid")
    call her_main("I'm organizing the \"Men's rights movement\" in our school!", "open", "closed", "angry", "mid")
    g4 "Oh boy, this is just so typical!"
    g4 "Blame everything on--"
    stop music fadeout 1.0
    m "Wait, did you say {size=+5}MEN'S{/size} rights movement?"
    call play_music("chipper_doodle")
    call her_main("You have no idea how hard it is to be a boy in our school these days...", "open", "base", "worried", "mid")
    menu:
        "\"Didn't see this one coming...\"":
            call her_main("No, you did not, because you refuse to listen to us, sir!", "open", "closed", "angry", "mid")
            her "But we will make you hear us..."
        "{size=-3}\"That's literally the dumbest idea I've ever heard.\"{/size}":
            call her_main("I knew you would say something like that...", "normal", "squint", "angry", "mid")

    call her_main("Did you know that some of the girls in this school are now selling favours for house points...?", "annoyed", "squint", "angry", "mid")
    her "Sometimes even for good grades..."
    m "Really?"
    call her_main("Nobody from the Gryffindor house of course...", "open", "closed", "angry", "mid")
    her "And that's what puts us at a disadvantage -- our integrity!"
    her "As for the boys -- they have to work ten times harder than the girls simply to pass a test..."
    her "Or, if they are lucky enough, to get one meagre house point..."
    call her_main("This is sexism in its purest form!", "open", "base", "base", "mid")
    menu:
        m "..."
        "\"What do you want me to do?\"":
            call her_main("Nothing!", "normal", "base", "base", "mid")
            m "Great. I'm good at that."
        "\"I'm not sure what to say...\"":
            call her_main("You do not need to say anything anymore, professor.", "normal", "base", "base", "mid")
        "\"You are being ridiculous!\"":
            call her_main("Am I? Well, we'll see...", "normal", "squint", "angry", "mid")

    call her_main("I have already sent a letter to the ministry of magic.", "open", "closed", "angry", "mid")

    $ renpy.music.set_volume(0.0, 1.0)
    pause 1.0
    $ renpy.music.set_pause(True, channel="music")
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    $ renpy.music.set_pause(False, channel="music")
    $ renpy.music.set_volume(1.0, 1.0)
    her "I'm sorry, but you left me no choice, professor."

    her "Now, if you'll excuse me, I must get to my classes..."

    call her_walk(action="leave")

    call bld
    m "...................."

    $ snape_busy = True # No point in calling him during the day.
    $ hermione_intro.E2_complete = True

    jump end_hermione_event


### Snape Hangout Event 2 ###
# You scheme a plan to take down Hermione.

label ss_he_hermione_E2:
    call bld
    m "......................."
    m "Hermione Granger came by again..."
    call sna_main("Don't mention the witch's name when I'm off duty...","snape_01", ypos="head")
    call sna_main("...............","snape_31")
    call sna_main("Dammit! I am a grown man, Albus!","snape_08")
    m "My name is not--"
    call sna_main("An esteemed wizard...","snape_08")
    m "Well, alright, let it out..."
    call sna_main("How come one tiny... cunt, is able to cause me so much grief?!","snape_31")
    call sna_main("I thought with you as my ally I will have a chance to--","snape_32")
    m "To unclench?"
    call sna_main("Yeah, that could be the word...","snape_31")
    call sna_main("But all I did was give her more leverage to harass me with...","snape_43")
    call sna_main("She's even turning the teachers against me now...","snape_43")
    call sna_main(".................","snape_08")
    call sna_main("She must go...","snape_35")
    m "What do you mean?"
    with hpunch
    call sna_main("{size=+6}We have to get rid off of her!{/size}","snape_33")
    g4 "Like, literally?"
    call sna_main("Do I have any other choice?","snape_34")
    m "You're joking, right?"
    call sna_main("Do I look like I'm joking?","snape_34")
    call sna_main("Can you do this for me?","snape_39")
    m "*Ehm*..."
    m "Even if I agreed to murdering someone..."
    m "Genies can't kill..."
    call sna_main("Rats!","snape_35")
    m "And we frown upon murderers..."
    if jerked_off_during_hermione_intro:
        call sna_main("Really? I thought you didn't give a fuck...","snape_44")
        m "to a certain degree..."
        m "I don't mind swinging my \"sword\" in front of the girl--"
        m "--but stabbing her with one is another thing."
        call sna_main(".............","snape_35")
    call sna_main("Well... don't mind me then...","snape_31")
    call sna_main("I'm all talk...","snape_31")
    call sna_main("I would never cause harm to one of my students...","snape_31")
    call sna_main("(... permanently that is.)","snape_08")
    m "Listen, if she bugs you so much, why not just find a less radical way to deal with her?"
    call sna_main("Nah... Flogging has been outlawed for years now...","snape_35")
    m "That's not what I mean..."
    call sna_main("*huh*?","snape_01")
    m "She is a top student, right?"
    call sna_main("Yes, damn her. The girl is a hard worker, I will give her that.","snape_31")
    m "She also has a reputation for being self-righteous."
    call sna_main("Oh, yes!","snape_34")
    m "And she thinks that she is better than everyone else..."
    call sna_main("Where are you going with this?","snape_44")
    m "Well, it seems like all of her power comes from her reputation..."
    call sna_main("......................?","snape_39")
    m "What if we take that away from her?"
    call sna_main("That would shut her up I suppose...","snape_38")
    call sna_main("But how? She's practically a saint--","snape_31")
    call sna_main("Even students who hate her secretly admire her.","snape_35")
    call sna_main("She hasn't failed a single test in her entire time here...--","snape_31")
    call sna_main("She is always way ahead of schedule...","snape_31")
    call sna_main("Damn, how I hate it when she corrects me during my classes...","snape_08")
    call sna_main("And thanks to her the Gryffindor house is way ahead of everybody else now...","snape_34")
    call sna_main("Even Slytherin is no match for them this year...","snape_35")
    call sna_main("........................","snape_43")
    call sna_main("Dammit... I need more wine...","snape_34")
    m "The wine can wait. Hear me out!"
    call sna_main("*Huh*...?","snape_01")
    m "*Hmm*... Let us..."

    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label .choices:

    menu:
        m "..."
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            call sna_main("What? You mean grade her unfairly?","snape_01")
            call sna_main("Nah... Dumbledore would never allow--","snape_31")
            call sna_main("Wait a second!","snape_37")
            m "Exactly!"
            call sna_main("You're right! I can grade her tests unfairly! I could even persuade other teachers to do the same!","snape_02")
            call sna_main("I could say that the order comes from you...","snape_02")
            call sna_main("And when the real Dumbledore shows up I will pretend that I had no idea that he was away...","snape_45")
            m "Works for me."
            call sna_main("*Err*...","snape_38")
            call sna_main("This is still you, genie, right?","snape_38")
            m "Yeah, yeah, still here..."
            call sna_main("OK, good.","snape_02")

        "{size=-3}\"Make sure Gryffindor loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            call sna_main("You mean to just start subtracting points from them for no good reason?","snape_01")
            call sna_main("Oh, I like that!","snape_02")
            call sna_main("There are a couple of Slytherin girls who are long overdue for receiving some extra house points as well.","snape_46")
            call sna_main("Oh, this will work out magnificently!","snape_45")
            call sna_main("You are a Genius!","snape_02")
            m "Yes, I am a genius genie. What are the odds of that..."

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            call sna_main("Tarnish her reputation?","snape_01")
            call sna_main("But the girl is incorruptible...","snape_01")
            m "Nonsense!"
            m "All we need to do is convince her that she needs to make some sacrifices \"for the greater good\"."
            call sna_main("Oh, but of course...","snape_37")
            call sna_main("She would gladly \"Get her hands dirty\" to save the honour of her precious Gryffindor house!","snape_47")
            call sna_main("And when she does, we will have the leverage we need...","snape_37")

    if d_flag_01 and d_flag_02 and d_flag_03:
        pass
    else:
        m "Nextly--"
        jump ss_he_hermione_E2.choices

    call sna_main("This could actually work!","snape_37")
    m "I think so too."
    call sna_main("Oh, I feel so alive tonight!","snape_45")
    call sna_main("Pour me another goblet!","snape_28")
    call sna_main("Potions class will start late tomorrow!","snape_45")
    m "Although....."
    m "I do feel like the measures are a little severe."
    m "I mean, she's just a girl..."
    call sna_main("Just a girl?","snape_36")
    call sna_main("Oh no, no, no...","snape_36")
    call sna_main("She is the embodiment of pure evil!","snape_32")
    call sna_main("If we don't do this now...","snape_31")
    call sna_main("One of those days I may just snap and {i}Avada Kedavra{/i} her!","snape_08")
    m "You'll do what?"
    call sna_main("Murder her for real!","snape_32")
    m "Alright, alright... got it."
    m "Let's choose the lesser of two evils then."
    call sna_main("Yes...","snape_35")
    call sna_main("Now, pour me some more wine.","snape_34")

    ">You spend the rest of the evening in Snape's company drinking your worries away."

    $ ss_he.hermione_E2 = True
    $ ss_event_pause += 1
    $ chair_OBJ.hidden = False

    jump end_snape_hangout_points

### Event 3 ###
# Third visit, after second special date with Snape.
# Hermione complains that she almost failed a test. (EVENING EVENT!)

label hermione_intro_E3:
    stop music fadeout 1.0
    call play_sound("knocking")
    "*Knock-knock-knock*!"

    her "Professor, I'm coming in!"
    m "...."

    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    call play_music("chipper_doodle")

    call her_main("", "annoyed", "squint", "angry", "mid", xpos="base", ypos="base")
    call ctc

    call her_main("Good evening, Professor.", "annoyed", "narrow", "angry", "R")

    menu:
        "-stare full of hatred-":
            call her_main("You can stare at me all you want, sir.", "normal", "squint", "angry", "mid")
            her "It will not make the problems of this school go away."
        "-sigh of exasperation-":
            call her_main("Is this a bad time?", "normal", "base", "base", "mid")
            call her_main("Well, since I'm already here...", "open", "base", "base", "mid")
        "\"....................................\"":
            call her_main("Professor?", "open", "base", "base", "mid")
            m "Yes, yes..."

    call her_main("Something... bizarre has happened today...", "open", "closed", "angry", "mid")
    call her_main("I'm not sure how to describe this...", "normal", "squint", "angry", "mid")
    call her_main("................................", "annoyed", "squint", "angry", "mid")
    call her_main("I think I almost failed a test...", "annoyed", "narrow", "angry", "R")

    menu:
        "\"That happens to students sometimes.\"":
            call her_main("To other students, yes. But not to me, sir!", "annoyed", "narrow", "angry", "R")
            call her_main("Never to me...", "soft", "base", "base", "R")
        "{size=-5}\"Way to go, Snape!\"{/size}":
            call her_main("Excuse me?", "normal", "base", "base", "mid")
            m "What?"
            m "Oh, I said, that's too bad. How are you holding up?"
            call her_main(".................", "normal", "squint", "angry", "mid")
        "\"So why tell me?\"":
            her "Because... this is not an ordinary event!"

    her "I'm not sure what is going on here..."
    m "An evil scheme against you, miss Granger?"
    call her_main("This is not a laughing matter, Sir.", "normal", "base", "angry", "mid")
    call her_main("You should consider me a \"measuring stick\" for our educational system.", "open", "closed", "angry", "mid")
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    m "Is that so...?"
    call her_main("Yes, professor. Something went terribly wrong today...", "normal", "squint", "angry", "mid")
    call her_main(".................................", "annoyed", "narrow", "angry", "R")
    call her_main("But what if it didn't?", "open", "base", "worried", "mid")
    her "What if all the tests will be this difficult from now on?"

    menu:
        "\"You should study more, girl!\"":
            call her_main("But I studied all night for this test!", "upset", "base", "base", "mid", tears="soft")
        "\"There, there... It'll be alright.\"":
            call her_main("No it won't! This is a catastrophe!", "mad", "happyCl", "worried", "mid", tears="soft_blink")

    call her_main("And the worst part is that I think I might be the only one who failed...", "angry", "base", "base", "mid", tears="soft")
    call her_main("How will this make me look?", "angry", "base", "base", "mid", tears="soft")
    call her_main("I will know for sure when we get the results though...", "normal", "base", "base", "R", tears="soft")
    call her_main("Yes, I'm sure everyone else failed as well...", "soft", "base", "base", "R")
    call her_main("I mean, they must have, right?", "open", "base", "worried", "mid")
    call her_main(".....................", "soft", "base", "base", "R")
    call her_main(".... right?", "open", "base", "worried", "mid")

    $ d_flag_01 = False

    label .choices:
    menu:
        "{size=-3}\"Of course. You are a top student after all.\"{/size}":
            call her_main("Exactly...", "annoyed", "squint", "angry", "mid")
            her "Or at least I used to be until today..."
            call her_main("I cannot believe this is happening!", "mad", "happyCl", "worried", "mid", tears="soft_blink")
        "{size=-3}\"You could prepare better if I were to tutor you.\"{/size}":
            $ tutoring_offer_made = True
            call her_main("*Hmm*...", "annoyed", "squint", "base", "mid")
            call her_main("Yes, that could help I suppose...", "soft", "base", "base", "R")
            call her_main("I appreciate your offer, professor, but...", "open", "base", "base", "mid")
            call her_main("The best tutor is a book, and I have the entire Hogwarts library at my disposal.", "open", "closed", "base", "mid")
            call her_main("I don't think it would be necessary, sir. But...", "soft", "base", "base", "mid")
            her "May I think about it?"
            m "Don't take too long..."
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            call her_main("Yes, I suppose we will...", "soft", "base", "base", "mid")
        "{size=-3}\"You need to put my cock in your mouth.\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            m "You need to put my co--"
            call her_main("*huh*?", "soft", "base", "base", "mid")
            m "{size=-4}(No, I can't actually say that...){/size}"
            call her_main("......?", "annoyed", "squint", "base", "mid")
            jump hermione_intro_E3.choices

    m "............"
    call her_main("I'm sorry, professor, I'm probably just overreacting anyway...", "grin", "happyCl", "worried", "mid", emote="sweat")
    call her_main("But you must understand that my reputation is at stake here!", "open", "base", "base", "mid")
    call her_main("There's gotta be something wrong with the test...", "annoyed", "narrow", "angry", "R")
    her "And although the entire class might have failed, I probably still got the most points on the test..."
    her "As usual..."
    call her_main("Well, I'd better go now. We have another \"MRM\" meeting today.", "open", "closed", "angry", "mid")
    her "I will let you know about the new ideas we come up with."
    m "I can hardly wait..."
    call her_main("Well, if there is nothing else, I have a studying schedule to keep.", "open", "closed", "base", "mid")
    m "By all means..."

    call her_walk(action="leave")

    $ snape_busy = False
    $ hermione_intro.E3_complete = True

    jump end_hermione_event

### Event 4 ###
# Hermione complains that she did fail the test. (EVENING EVENT!)

label hermione_intro_E4:
    stop music fadeout 1.0

    # Gryffindor gets shafted by Snape and has 50% of Slytherin's points.
    $ gryffindor = int(slytherin*0.5)
    call update_ui_points

    # Wear default outfit. She's in shock so she didn't change.
    $ hermione.equip(her_outfit_default)

    call her_walk(action="enter", xpos="mid", ypos="base")

    call bld
    her "....................."
    m "???"

    call her_walk("desk", "base")

    call bld
    her "............"
    m "Miss Granger?"
    her "..............................."
    m "Miss Granger?!!"

    call her_main("", "upset", "narrow", "base", "stare", tears="mascara", xpos="right", ypos="base")
    call ctc

    call her_main("*huh*?", "upset", "narrow", "base", "mid", tears="mascara")
    call her_main("Oh, I'm already here?", "upset", "narrow", "base", "L", tears="mascara")
    call her_main("I'm sorry, sir... I...", "upset", "narrow", "base", "down", tears="mascara")
    call her_main("..................", "angry", "narrow", "base", "down", tears="mascara")
    call her_main("It seems that I did...", "angry", "happyCl", "base", "dead", tears="mascara")
    call her_main("I did... *Ehm*...", "normal", "happyCl", "base", "dead", tears="mascara")
    call her_main("... I failed that test after all.", "open", "happyCl", "base", "dead", tears="mascara")
    call her_main("On top of that I... caused my house to lose a lot of points...", "disgust", "narrow", "base", "down", tears="mascara")
    call her_main("I'm sorry, professor...", "upset", "happyCl", "worried", "mid", tears="mascara_soft_blink")
    call her_main("I'm not sure why I'm here...", "upset", "happyCl", "worried", "mid", tears="tears_mascara_crying_blink")
    call her_main("I think I'd better go...", "angry", "happyCl", "worried", "mid", tears="mascara_soft_blink")
    call her_main("...................", "angry", "happyCl", "worried", "mid", tears="tears_mascara_crying_blink")

    call her_walk(action="run", xpos="door", speed=2, reduce=True)
    call her_chibi("leave")

    call bld
    m "............."
    m "She will be alright..."
    m "I think..."

    $ hermione_intro.E4_complete = True

    jump end_hermione_event

### Event 5 ###
# Hermione comes after her breakdown (when she failed the test).
# She is asking for tutoring.
# Tutoring unlocked!

label hermione_intro_E5:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="desk", ypos="base")

    call play_music("chipper_doodle")
    call her_main("Good morning, Professor.", "base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    m "(So She doesn't even bother to knock anymore?)"
    m "How can I help you today, miss Granger?"
    call her_main("Well, first of all, I am terribly sorry about yesterday's display, sir...", "open", "closed", "angry", "mid")
    call her_main("I've never failed a test in my life, so I wasn't sure how to react...", "open", "squint", "base", "mid")
    call her_main("But I'm all better now...", "open", "closed", "angry", "mid")

    menu:
        "\"Glad to hear it.\"":
            pass
        "\".........\"":
            pass

    her "I will not take much of your time, I promise..."

    if tutoring_offer_made:
        her "I am here to take you up on your offer."

        menu:
            "\"What offer?\"":
                her "A while back you offered to tutor me, sir..."
                menu:
                    "\"Oh... That offer has expired.\"":
                        call her_main("It...", "open", "base", "base", "mid")
                        call her_main("Expired, sir?", "angry", "base", "base", "mid")
                        call her_main("B-but...", "open", "base", "worried", "mid")
                        call her_main("But I require tutoring, and you are the smartest wizard I know...", "annoyed", "base", "worried", "mid")
                        call her_main("Please, sir. I really need your help.", "angry", "base", "worried", "mid")
                        menu:
                            "\"Show me your tits and it's a deal!\"":
                                call her_main("m-my...?", "shock", "wide", "base", "stare")
                                call her_main("............", "angry", "base", "angry", "mid")
                                her "....."
                                with hpunch
                                call her_main("{size=+5}Professor Dumbledore!!!{/size}", "scream", "closed", "angry", "mid")
                                m "{size=-5}(Well, at least I tried...){/size}"
                                her "I am not some Slytherin floozy!"
                                m "Of course not, miss Granger."
                                m "It was a test...{w=0.5} You passed. Good job."
                                call her_main("What...?", "open", "base", "base", "mid")
                                call her_main("Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir.", "grin", "happyCl", "worried", "mid", emote="sweat")
                                m "My offer is still valid. If you want me to then I can tutor you."
                                call her_main("..............", "annoyed", "base", "worried", "R")
                            "\"Well, alright, alright...\"":
                                pass
                    "\"Oh, that's right. Great.\"":
                        pass

            "\"Splendid! Starting today?\"":
                pass
    else:
        call her_main("I... *Ehm*...", "normal", "squint", "angry", "mid")
        her "Sir, I hope this is not too much to ask..."
        m "Yes?"
        her "*Ehm*... would it be alright if..."
        her "..............."
        call her_main("do You think you could tutor me a little, sir?", "annoyed", "squint", "angry", "mid")
        menu:
            "\"I suppose that is possible.\"":
                pass
            "\"*Hmm*... I'm quite busy actually.\"":
                call her_main("Sir, please, you are the smartest wizard I know!", "open", "base", "worried", "mid")
                m "{size=-4}(You have no idea, little witch.){/size}"
                m "Well, it could be arranged, I suppose..."

    call her_main("Thank you, sir. I am very grateful.", "base", "base", "base", "mid")
    call her_main("Just let me know when, and I will bring my books!", "open", "closed", "base", "mid")
    call her_main("I must study even harder from now on...", "annoyed", "squint", "angry", "mid")
    call her_main("And I'll be taking private lessons from you, sir, as often as possible.", "base", "base", "base", "mid")
    call her_main("But that's not all...", "normal", "squint", "angry", "mid")
    her "The \"MRM\" shall investigate our education system much closer now..."
    her "I think some sort of foul play might be taking place..."
    m "*exagerrated gasp* No way!"
    her "I have a list of suspects already but I will get back to you on this later..."
    m "*Ehm*... alright..."
    call her_main("Oh, my classes are about to start. I'd better go...", "open", "base", "worried", "R")
    call her_main("Good day to you, sir.", "base", "happyCl", "base", "mid")

    call her_walk(action="leave")

    stop music fadeout 1.0

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher", True)
    call popup("{size=-4}You can now summon Hermione into your office.{/size}", "Character unlocked!", "interface/icons/head/hermione.webp")

    $ tutoring_hermione_unlocked = True

    $ hermione_intro.E5_complete = True #Allows next event to start.
    $ hg_event_pause += 2

    jump end_hermione_event

### Tonks Hangout Event ###
# Tonks will help convince Hermione to buy favours.

label nt_he_hermione_E1:
    call ton_main("So, that Granger girl is causing you two trouble?","open","base","base","mid", ypos="head", flip=False)
    m "Quite a bit. She's not too thrilled on the idea of favour trading."
    call ton_main("Maybe I can be of help with her?", "base", "base", "base", "mid")
    call ton_main("I can be very convincing.", "horny", "narrow", "annoyed", "mid")
    m "What are you suggesting?"
    call ton_main("To persuade her into having a try of it herself, for a start...","open","base","base","R")
    call ton_main("Convince her that trading favours isn't all bad.","base","base","base","mid")
    m "That would indeed be very helpful. She's stubborn in that regard."
    call ton_main("You don't have to tell me. She's been lecturing me about those \"sexual favours\" since the very day I got here...", "upset", "base", "base", "R")
    call ton_main("But I shouldn't complain about that...", "open", "closed", "base", "mid")
    call ton_main("Hearing those naughty words spill out of her gorgeous little mouth really gets me going!", "soft", "narrow", "base", "R", hair="horny")
    g9 "I can imagine so."
    call ton_main("When she describes all the wrongdoings of those \"filthy Slytherin girls\"...", "soft", "base", "shocked", "stare")
    call ton_main("How could I possibly get tired of that!", "crooked_smile", "narrow", "base", "stare")
    call ton_main("I'm very glad I decided to join you two.","open","base","base","down")
    call ton_main("As an Auror It's just constant busy work...", "open", "base", "raised", "mid")
    call ton_main("Not to mention the hours.", "mad", "base", "base", "down")
    call ton_main("And the mortality rate...","upset","base","worried","R")
    call ton_main("If I had known the benefits of being a teacher at Hogwarts, I would have signed up straight away!","horny","base","base","up")

    if game.daytime:
        ">You spend the afternoon conspiring against Hermione with Tonks..."
    else:
        ">You spend the evening conspiring against Hermione with Tonks..."
    call notes
    ">You feel a faint bond forming between you two..."

    $ nt_he.hermione_E1 = True

    jump end_tonks_hangout_points

### Event 6 ###
# Hermione comes and asks to buy a favour from her.

label hermione_intro_E6:
    stop music fadeout 1.0
    call play_sound("knocking")
    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            m "(It's that witch again...)"
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $ achievement.unlock("knock")
                    $ hg_event_pause += 1
                    jump main_room

                "\"Of course. Come on in.\"":
                    pass

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            $ achievement.unlock("knock")
            $ hg_event_pause += 1
            jump main_room

        "\"Yes, come in.\"":
            pass

        "\"...................................\"":
            call play_sound("knocking")
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    call her_walk(action="enter", xpos="mid", ypos="base")

    call play_music("chipper_doodle")

    call her_main("Good day, professor...", "soft", "base", "base", "R", xpos="base", ypos="base", trans=d3)
    her "........................"
    call her_main("........................", "annoyed", "base", "worried", "R")
    her "........................"
    call her_main("*Ehm*......", "open", "base", "base", "mid")
    call her_main(".................", "annoyed", "base", "worried", "R")
    m "What is it, miss Granger?"
    call her_main("Well... *Ehm*.", "open", "base", "base", "mid")

    if gryffindor < slytherin:
        call her_main("You see... The Gryffindor house is not in the lead anymore...", "open", "base", "worried", "R")
    else:
        call her_main("You see... The Gryffindor house is struggling with points...", "open", "base", "worried", "R")

    call her_main("And... everyone is working so hard...", "annoyed", "base", "worried", "R")
    call her_main("And they look up to me for help but I don't know what to do...", "disgust", "base", "worried", "down")
    m "............................"
    call her_main("Professor Dumbledore...", "open", "base", "worried", "mid")

    $ renpy.music.set_volume(0.0, 1.0)
    pause 1.0
    $ renpy.music.set_pause(True, channel="music")
    call her_main("I want you to buy a favour from me!", "open", "happyCl", "worried", "mid")
    call her_main("", "normal", "happyCl", "worried", "mid")
    g4 "(What in the...?!)"
    $ renpy.music.set_pause(False, channel="music")
    $ renpy.music.set_volume(1.0, 1.0)

    menu:
        "\"You mean like a sexual favour?\"":
            call her_main("*Ehm*... I'm not sure...", "angry", "wink", "worried", "mid", emote="sweat")
            her "The kind that would gain our house additional points..."
            call her_main("I could write an essay for you or...", "open", "base", "worried", "R")
            call her_main("Or maybe clean your tower...?", "angry", "wink", "worried", "mid", emote="sweat")
            m "{size=-4}(Clean my tower? Heh... There's gotta be dirty joke in there somewhere...){/size}"
            m "Well, alright then, I think we can figure something out."
        "\"Well, if you insist...\"":
            pass
        "\"I don't think so, miss Granger.\"":
            call her_main("B-but... We need the points...", "open", "base", "worried", "mid")
            call her_main("Professor, please, I am really desperate...", "open", "squint", "low", "mid")
            m "Desperate you say...?"
            m "Well, alright..."

    call her_main("Really?", "silly", "base", "base", "mid")
    call her_main("Thank you, professor...", "base", "happyCl", "base", "mid")
    call her_main("So... What will it be?", "base", "base", "base", "mid")

    $ d_flag_01 = False

    label .choices:
    $ current_favor = ""

    menu:
        "\"Show me your tongue...\"":
            $ current_favor = "show_tongue"
        "\"Stand there. Let me look at you\"":
            $ current_favor = "stand_there"
        "\"Make a silly face...\"":
            $ current_favor = "silly_face"
        "\"Say \"I've been a bad girl\"\"":
            $ current_favor = "bad_girl"
        "\"Blow me\"" if not d_flag_01:
            $ d_flag_01 = True
            g9 "(*heh*, if only that worked...)"
            m "(I don't think she's ready for that just yet)"
            m "(Let's start with something simpler.)"
            jump hermione_intro_E6.choices

    call her_main("*Ehm*...", "angry", "base", "base", "mid")
    call her_main("How many house points will I get for that...?", "angry", "wink", "base", "mid")

    menu:
        "\"One point.\"":
            if not current_favor in ["show_tongue", "stand_there"]:
                call her_main("I don't think it's worth it then...", "annoyed", "base", "worried", "mid")
                jump hermione_intro_E6.choices
            $ current_payout = 1
        "\"Five points.\"":
            if not current_favor in ["show_tongue", "stand_there", "silly_face"]:
                call her_main("I don't think it's worth it then...", "annoyed", "base", "worried", "mid")
                jump hermione_intro_E6.choices
            $ current_payout = 5
        "\"Ten points.\"":
            call her_main("(So little...?)", "annoyed", "base", "worried", "down")
            $ current_payout = 10
        "\"Twenty points.\"":
            call her_main("(Wow. That's quite a lot for such simple request...)", "base", "base", "base", "mid")
            $ current_payout = 20

    call her_main("Em, alright...", xpos="mid", ypos="base", trans=fade)

    if current_favor == "show_tongue":
        call her_main("M-my... tongue, sir?", "grin", "happyCl", "worried", "mid", emote="sweat")
        m "Yes, girl. Open your mouth, and show me your tongue."
        call her_main("{size=-4}(What an odd request...){/size}", "annoyed", "narrow", "angry", "R")
        call her_main("*Ehm*... well, alright then...", "soft", "squint", "worried", "mid")
        call her_main("Here...", "open", "squint", "base", "mid")
        call her_main(".............", "open_tongue", "narrow", "base", "mid_soft")
        call her_main(".............", "open_tongue", "narrow", "base", "L")
        call her_main(".................", "open_tongue", "narrow", "angry", "R")

        menu:
            "\"Very good. Here are your points.\"":
                pass
            "\"Not good enough. You can do better\"":
                call her_main("...............", "annoyed", "narrow", "angry", "R")
                call her_main("Alright, I will try to do better, sir...", "open", "closed", "angry", "R")
                call her_main("How about this?", "open", "base", "worried", "mid")
                call her_main("*A-a-ah*.........", "scream", "base", "base", "R")
                call her_main("............................", "open_wide_tongue", "happy", "base", "R")
                call her_main("......................................", "open_wide_tongue", "narrow", "base", "down")
                her "...................................................................."
                call her_main(".......................................................................................................", "open_wide_tongue", "closed", "angry", "mid")
                call her_main("*khow* *ish* *thish*?", "open_wide_tongue", "base", "annoyed", "mid")

                menu:
                    "\"Good enough. Here, your points.\"":
                        pass
                    "\"Keep that mouth open.\"":
                        call her_main(".......", "open_wide_tongue", "happy", "worried", "mid")
                        call her_main("{size=-4}(My mouth is starting to hurt...){/size}", "open_wide_tongue", "happy", "worried", "mid")
                        call ctc
                        m "Alright, that's enough."
                        call her_main("{size=-4}(Finally...){/size}", "annoyed", "narrow", "base", "R")
    elif current_favor == "stand_there":
        call her_main("So, I just have to stand here then...?", "soft", "base", "base", "mid")

        $ d_flag_01 = "mid"
        $ d_flag_02 = 0

        label .stand_there_choices:

        if d_flag_02 >= 3:
            call her_main("Professor, could you make up your mind already?!", "angry", "base", "annoyed", "R", trans=dissolve)
            m "Alright, alright, there's no need to get worked up about it, sheesh."
        else:
            menu:
                "\"No, come closer\"" if d_flag_01 == "mid":
                    $ d_flag_01 = "desk"
                    $ d_flag_02 += 1
                    her "*Ehm*... alright..."
                    call her_walk("desk", "base")

                    jump hermione_intro_E6.stand_there_choices
                "{size=-4}\"On second thought, go back to the middle\"{/size}" if d_flag_01 == "desk":
                    $ d_flag_01 = "mid"
                    $ d_flag_02 += 1
                    her "*Ehm*... alright..."
                    call her_walk("mid", "base")
                    call her_chibi("stand", flip=False)
                    with d3

                    jump hermione_intro_E6.stand_there_choices
                "\"Yes, stand right where you are.\"":
                    pass

        call her_main(".................................", "annoyed", "base", "annoyed", "R", trans=d3)

        menu:
            m "*Hmm*..."
            "\"The uniform suits you, miss Granger...\"":
                call her_main("............", "soft", "base", "base", "R",cheeks="blush")
                call her_main("Thank you, professor...", "open", "base", "base", "R",cheeks="blush")
                call her_main("", "base", "base", "base", "R",cheeks="blush")
            "\"You have a nice body, miss Granger...\"":
                call her_main("!!?", "soft", "wide", "base", "stare")
                call her_main("..............", "annoyed", "narrow", "angry", "R",cheeks="blush")
                call her_main("Thank you, professor...", cheeks="blush")
            "\"That's enough. Here are your points...\"":
                jump hermione_intro_E6.end
    elif current_favor == "silly_face":
        call her_main("A silly face then...", "grin", "happyCl", "worried", "mid", emote="sweat")
        her "Let's see..."
        label .silly_face_choices:

        call her_main("How about this one?", "silly", "base", "base", "squint")

        menu:
            "\"Good! Very stupid! I mean, silly.\"":
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                pass

        call her_main(".........", "annoyed", "narrow", "angry", "R")
        call her_main("What about this one then?", "disgust", "slit", "low", "stare")

        menu:
            "\"*Ha-ha*! You look like an idiot!\"":
                jump hermione_intro_E6.end
            "\"No, not stupid enough.\"":
                pass

        call her_main(".........", "annoyed", "narrow", "angry", "R")
        call her_main("What if I do it like this?", "full", "slit", "worried", "ahegao")

        menu:
            "\"Good! Very stupid.\"":
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                pass

        call her_main(".........", "annoyed", "narrow", "angry", "R")
        call her_main("I give up...", "upset", "narrow", "worried", "down")

        menu:
            "\"*Ha-ha-ha*, perfect!\"":
                call her_main("What?", "open", "base", "angry", "mid")
                call her_main("But that's my normal face!", "angry", "base", "angry", "mid")
                g9 "*he-he-he* Don't get mad, [hermione_name], I'm just messing with you."
                m "Although you look cute when you're upset."
                call her_main(".......", "annoyed", "base", "worried", "R", cheeks="blush")
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                jump hermione_intro_E6.silly_face_choices
    elif current_favor == "bad_girl":
        call her_main("I...", "normal", "squint", "angry", "mid")
        call her_main("I have been a very bad girl...", "open", "squint", "angry", "R")
        g9 "Have you been a very, very, very bad girl?"
        call her_main("*Umm*... Maybe?", "grin", "wink", "worried", "mid")

        $ d_flag_01 = False

        label .bad_girl_choices:
        menu:
            g9 "..."
            "\"Do you need to be punished?\"":
                call her_main("Do I need to... be punished?", "open", "base", "worried", "mid")
                call her_main("*Ehm*...", "upset", "base", "base", "down")
                her "....................."
                call her_main("Well, I am not perfect, if that's what you mean, sir...", "annoyed", "narrow", "angry", "R")
                call her_main("But do I need to be punished?", "annoyed", "base", "base", "R")
                call her_main("Is this really for me to decide...? I mean...", "normal", "squint", "angry", "mid")
                call her_main("What does this have to do with anything?", "open", "squint", "angry", "mid")
                call her_main("", "normal", "squint", "angry", "mid")
                m "You are overanalysing this, girl."
                m "Just say that you need to be punished!"
                call her_main("Fine. I need to be punished!", "angry", "base", "angry", "mid")
                call her_main("{size=-5}(And I truly do think so sometimes...){/size}", "normal", "narrow", "worried", "down")
                m "That's a good girl."
                call her_main("................??", "annoyed", "base", "base", "R")
                m "Now that wasn't hard at all, was it?"
                call her_main("N-no , sir, I guess not...", "angry", "happyCl", "worried", "R")
                call her_main("", "annoyed", "base", "worried", "R")
                m "Alright then..."
            "\"Do you want to get spanked?\"":
                call her_main("Do I want to...", "open", "base", "worried", "mid")
                call her_main("Get s-spanked??", "angry", "wide", "base", "stare")
                call her_main("*Tsk*!", "angry", "base", "angry", "mid")
                call her_main("Professor, I don't think I'm comfortable with--", "open", "closed", "angry", "mid")
                m "Apologies, let me rephrase the question..."
                m "How badly do you need those points?"
                call her_main("..................", "annoyed", "squint", "angry", "mid")
                call her_main("Yes, sir. I do need to get spanked.", "open", "closed", "angry", "mid")
                m "Alright, that's good enough for now..."
                call her_main("{size=-4}(For now?){/size}", "normal", "squint", "angry", "mid")
            "\"Bend over!\"" if not d_flag_01:
                $ d_flag_01 = True
                m "{size=-5}(Too early for this... I need to reel her in first.){/size}"
                jump hermione_intro_E6.bad_girl_choices

    label .end:
        if current_payout == 1:
            m "{number=current_payout} point to the Gryffindor house."
        else:
            m "{number=current_payout} points to the Gryffindor house."
        $ gryffindor += current_payout

    call her_main("..... Yay!.......", "grin", "happyCl", "worried", "mid", emote="sweat")
    her "This was quite easy..."
    call her_main("Do you think you could buy some more favours from me in the future, professor?", "grin", "wink", "worried", "mid")

    menu:
        "\"I don't think that's a good idea.\"":
            call her_main("Please, professor...", "angry", "base", "worried", "mid")
            her "We really need those points..."
            m "......."
            call her_main("You are an esteemed wizard and to be honest...", "annoyed", "base", "worried", "R")
            her "The only person in this school whom I don't mind asking for this..."
            m "Well, when you put it that way..."
        "\"That's a possibility...\"":
            pass

    call her_main("Thank you, professor. Thank you so much!", "smile", "happyCl", "base", "mid")
    call her_main("Well... I suppose I'd better go now...", "base", "base", "base", "mid")
    m "............"

    call her_walk("door", "base")
    pause.3

    # Hermione inner thoughts
    show screen blktone
    with d3

    if current_favor == "show_tongue":
        call her_main("{size=-4}(*Hmm*...){/size}", "annoyed", "narrow", "worried", "down", ypos="head", flip=False, trans=d3)
        call her_main("{size=-4}(Students show teachers their tongues all the time...){/size}", "soft", "base", "base", "R")
        call her_main("{size=-4}(Although that's usually when the teacher is not looking...){/size}", "base", "narrow", "base", "R_soft")
        call her_main("{size=-4}(But there is nothing wrong with what I did today...){/size}", "annoyed", "base", "base", "L")
        call her_main("{size=-4}(I earned my house extra points...){/size}", "smile", "happyCl", "base", "mid")
    elif current_favor == "stand_there":
        call her_main("{size=-4}(I can just stand there and let the professor look at me...){/size}", "annoyed", "base", "base", "R", ypos="head", flip=False, trans=d3)
        call her_main("{size=-4}(There is nothing wrong with that... nothing at all...){/size}", "base", "closed", "base", "mid")
    elif current_favor == "silly_face":
        call her_main("{size=-4}(Stupid face...){/size}", "silly", "base", "base", "squint", ypos="head", flip=False, trans=d3)
        call her_main("{size=-4}(Stupid face...){/size}", "disgust", "happy", "base", "squint")
        call her_main("{size=-4}(I need to practise this.){/size}", "base", "happyCl", "base", "mid")
    elif current_favor == "bad_girl":
        call her_main("{size=-4}(I'm a bad girl...){/size}", "angry", "base", "angry", "stare", ypos="head", flip=False, trans=d3)
        call her_main("{size=-4}(I am a very bad girl...){/size}", "base", "base", "angry", "stare")
        call her_main("{size=-4}(Yes, I can say things like that easily...){/size}", "smile", "happyCl", "base", "mid")
        call her_main("{size=-4}(I guess I'm a born actress...){/size}", "base", "happyCl", "base", "mid")

    hide screen blktone
    call her_chibi("leave")
    with d3

    stop music fadeout 1.0

    call popup("You have unlocked the ability to buy sexual favours from Hermione.", "Congratulations!", "interface/icons/head/hermione.webp")

    $ hermione_wardrobe_unlocked = True
    $ hermione_favors = True

    $ hermione_intro.E6_complete = True

    jump end_hermione_event
