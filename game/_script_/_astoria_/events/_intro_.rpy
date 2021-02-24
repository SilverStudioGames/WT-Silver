

### Astoria Intro ###

### Event 1 ###
# Tonks tells you about a student that has used the Imperius curse at school.
# You need to ask Snape and Hermione to help find the student.

label astoria_intro_E1:
    if "poster_1_store" not in tonks_mail_list:
        $ tonks_mail_list.append("poster_1_store")

    stop music fadeout 1.0
    call play_sound("knocking")
    "*knock-knock-knock*"

    ton "[ton_genie_name], may I come in?"
    ton "We have to talk about some recent events that happened..."
    ton "It's quite urgent..."

    menu:
        m "(...)"
        "\"Yes, come in!\"":
            ton "Thank you..."

        "\"Not now!\"":
            ton "I'm sorry Sir, but I'm afraid this can't wait."
            ton "I'm coming in..."

    # Tonks walks in.
    call ton_walk(action="enter", xpos="desk", ypos="base")

    call play_music("tonks")
    call ton_main("Good evening, [ton_genie_name].", "base", "base", "base", "mid", xpos="mid", ypos="base")
    m "[tonks_name]..."
    call ton_main("I'm terribly sorry for bursting in like this!", "open", "base", "raised", "R")
    m "What in the world got you so flustered?"
    call ton_main("We might be in big trouble, [ton_genie_name]!", "open", "base", "worried", "mid")

    call play_music("playful_tension")
    g9 "Miss Tonks... Have you been a bad girl?"
    call ton_main("I'm not joking, [ton_genie_name]!", "soft", "base", "annoyed", "mid")
    call ton_main("Something terrible has happened at school today!", "open", "closed", "annoyed", "R")
    call ton_main("I believe one of our students has conducted some highly illegal activities against another student!", "normal", "base", "annoyed", "downR")
    call ton_main("We have to take action!{w=0.6} The last thing we need is for this to reach the Ministry's attention!","open","base","angry","mid")
    m "So? Isn't it your task to cover up that sort of stuff?"
    call ton_main("Yes, but...","upset","base","worried","down")
    call ton_main("Please, [ton_genie_name]! I can't cover this up all on my own!","open","base","worried","mid")
    call ton_main("I require your help...", "upset", "base", "worried", "mid")
    m "My help, you say?"
    call ton_main("Yes...","base","base","worried","down")

    menu:
        m "(...)"
        "\"How exactly can I help you?\"":
            pass

        "\"I'm busy right now...\"":
            call ton_main("Busy with what exactly?","open","base","raised","mid")
            m "...................."
            call ton_main("[ton_genie_name]?", "mad", "base", "angry", "mid")
            m "Please give me a minute... I'm still thinking..."
            call ton_main("We don't have time for this!", "normal", "base", "angry", "mid")
            m "I have all the time in the world, darling..."
            m "I'm immortal..."
            call ton_main("Could you please just listen to me?", "mad", "closed", "angry", "mid")

        "\"What's in it for me?\"":
            call ton_main("Are you seriously asking me that?", "clench", "shocked", "shocked", "stare")
            call ton_main("If this doesn't get dealt with immediately they'll have us both locked up in a cell in Azkaban, do you hear me?!", "mad", "base", "angry", "mid")
            m "Loud and clear..."
            m "I'll be locked up in a cell - together with you..."
            g9 "I can think of many fates worse than that, if I'm honest."
            call ton_main("Weren't you so scared of that very thing before?","open","base","raised","mid")
            g9 "Not when I'm accompanied by someone as lovely as you!"
            call ton_main("................", "annoyed", "base", "annoyed", "R")
            call ton_main("You are clearly insane!","open","base","angry","mid") # Annoyed
            call ton_main("Fine... Tell me what you want so we can continue...", "upset", "base", "base", "mid")
            m "*Hmm*..."

            $ d_flag_01 = False

            label astoria_intro_E1_choices:

            menu:
                m "How about you..."
                "\"Pull on my finger...\"" if d_flag_01 == False:
                    $ d_flag_01 = True
                    call ton_main("I'm sorry?","open","base","raised","mid")
                    g9 "Come on. It's an old trick we Genies like to do!"
                    m "It's harmless, I swear..."
                    call ton_main(".............","upset","base","angry","R")
                    call ton_main("Very well...","open","closed","base","mid")
                    pause.2

                    # Tonks walks over.
                    call hide_characters
                    hide screen bld1
                    show screen blkfade
                    with d3

                    # Genie and Tonks stand behind the desk.
                    $ genie_chibi.zorder = 1
                    $ tonks_chibi.zorder = 1
                    call ton_chibi("stand",275,"behind_desk")
                    call gen_chibi("stand",190,"behind_desk")
                    hide screen blkfade
                    with fade
                    pause.8

                    call bld
                    g9 "Now pull it."
                    call ton_main("..................................", "disgust", "base", "annoyed", "down", ypos="head")
                    m "Try a bit harder..."
                    call ton_main("..............................................", "normal", "base", "angry", "down")
                    call bld("hide")
                    pause.2
                    with hpunch
                    pause.5

                    call bld
                    g4 "Why isn't this working?!"
                    m "(Oh, that's right...)"
                    m "(I forgot we Genies are unable to fart...)"
                    call ton_main("Are we done here?","open","closed","base","mid")
                    m "Want to give it one more try?"
                    call ton_main("I think not...", "open", "base", "annoyed", "R")
                    call ton_main("I expected a bit more from a Genie... A magic trick, perhaps?", "upset", "base", "annoyed", "down")
                    m "I've told you, I can't do magic anymore..."
                    call ton_main("How very disappointing...","open","closed","base","mid")
                    call ton_main("I'm starting to have my doubts that you ever were a Genie...", "mad", "base", "base", "R")
                    m "Sorry about that..."
                    m "Can I ask you for something else?"
                    call ton_main("Still? Even after disappointing me like this?", "upset", "base", "annoyed", "mid")
                    m "Please?"
                    call ton_main("*Ugh*... Fine...", "upset", "narrow", "annoyed", "R")
                    show screen blkfade
                    hide screen bld1
                    with d3

                    $ genie_chibi.zorder = 2 # Default
                    $ tonks_chibi.zorder = 3 # Default
                    call gen_chibi("sit_behind_desk")
                    call ton_chibi("stand","desk","base")

                    hide screen blkfade
                    call ton_main("","upset","base","base","mid", xpos="mid", ypos="base", trans=fade)

                    jump astoria_intro_E1_choices

                #"\"Blow me!\"":
                #    call ton_main("Blow you? With my mouth?","base","base","base","mid")
                #    m "Yes, please."
                #    call ton_main("On your dick, I imagine?","base","base","base","mid")
                #    g9 "Yes, if you would..."
                #    call ton_main("Very well...","base","base","base","mid")
                #    call ton_main("Get it out for me, would you...","base","base","base","mid") # Naughty look
                #    g9 "!!!"
                    # Tonks walks over.
                    # Blkfade.
                    # Genie and Tonks stand behind the desk.
                    # Genie has his dick in hand, jerking off.

                #    call nar(">To your surprise, Tonks \"blows\" a gust of wind over \"your cock\"...")
                #    call ton_main("There, all done.","base","base","base","mid")
                #    m ".............."
                #    call ton_main("What? I did what you asked for... I blew your cock...","base","base","base","mid")
                #    m "......................"
                #    call ton_main("Now, could we get back to discuss what I came here for in the first place?","base","base","base","mid")
                #    m "Fine. I know when I'm outwitted..."
                #    call ton_main("I will suck your delicious cock some other time, [ton_genie_name]... I promise!","base","base","base","mid")
                #    call ton_main("But right now we simply don't have time to fool around I'm afraid...","base","base","base","mid")

                "\"Send Nudes.\"":
                    call ton_main("Nudes, [ton_genie_name]?", "annoyed", "base", "raised", "mid")
                    g9 "Yes! Send me some nude pictures of yourself!"
                    g9 "A poster, maybe?"
                    call ton_main("Oh...","upset","base","base","down")
                    call ton_main("A poster, you say?...","horny","base","base","mid")
                    call ton_main("What are you gonna do with it? Put it on your wall and fap to it?","horny","base","angry","mid")
                    g9 "You can count on that!"
                    call ton_main("Hold on!{w} Are you going to hang it up here? In your office?!", "open", "wide", "shocked", "stare")
                    m "Sure... It's not like there are that many other rooms I can go to..."
                    call ton_main("(Oh my... So everyone would be able to see it...)","upset","base","worried","R", hair="horny")
                    call ton_main("(All those girls that come in here...)","upset","base","base","ahegao")
                    call ton_main("(As long as my face isn't on it, this shouldn't be too bad...)", "mad", "base", "worried", "down")
                    call ton_main("...","upset","base","worried","R")
                    call ton_main("Very well, I shall send you an owl with it tomorrow morning, [ton_genie_name].","base","base","base","mid")
                    g9 "Sweet!"
                    call ton_main("Now, here is what I'll require your help with...","open","closed","base","mid")

                    if "poster_1_gift" not in tonks_mail_list:
                        $ tonks_mail_list.append("poster_1_gift")
                        $ tonks_mail_list.remove("poster_1_store")

    call ton_main("This girl I've told you about, Susan Bones?", "soft", "base", "shocked", "mid")
    call ton_main("The one with--", "base", "base", "base", "R")
    g9 "With the giant tits!"
    call ton_main("... The one with the unfortunate luck of being a constant target of bullying and harassment!", "mad", "closed", "base", "mid") # Annoyed
    m "Yes, that too..."
    call ton_main("That poor girl! She cried the entire time when she told me about what happened...", "open", "base", "worried", "down")
    call ton_main("I can't believe she got hit by a curse!", "mad", "base", "angry", "down") # Angry
    m "At least she isn't dead..."
    call ton_main("No, of course not!","open","base","angry","mid")
    m  "Or Injured?"
    call ton_main("Thankfully not...","upset","base","base","R")
    m "And nobody tried to shrink her tits?"
    call ton_main("Don't be silly...","open","closed","base","mid")
    m "Then what are you concerned about exactly?"

    call ton_main("This is something quite serious!", "mad", "base", "worried", "mid")
    call ton_main("If we don't find the culprit of this, and find them quickly, the Ministry will be on our toes by tomorrow!","open","base","angry","mid")
    m "That bad, *huh*?"
    call ton_main("Yes, I'm afraid...","upset","base","worried","down")
    call ton_main("She was the target of an \"unforgivable curse!\"","open","base","worried","mid")
    m "A curse?..."
    m "Like...{w=0.5} The c-word?"
    call ton_main("No! A magical curse!{w} not an insult...", "mad", "closed", "annoyed", "mid")
    call ton_main("Those curses are a major transgression of Ministry laws!","open","base","angry","mid")
    call ton_main("If you are caught having cast even one of them they will put you in Azkaban for the rest of your life!", "open", "shocked", "worried", "mid")
    call ton_main("Sharing a room with a whole bunch of Dementors!","upset","base","angry","mid")
    m "Dement-{w=0.6}ors?"
    m "Is it like a nursing home or something?"
    call ton_main("No, I've told you before!", "mad", "closed", "angry", "mid")
    call ton_main("Azkaban is a prison! With Dementors roaming all over it...", "open", "narrow", "annoyed", "mid")
    call ton_main("Believe me, you wouldn't want to be around them, I tell you that much...","open","base","angry","R")
    m "(Does she hate old people as well now?)"

    call ton_main("Should the Ministry find out about what happened to... Miss Bones.", "upset", "shocked", "worried", "R")
    g9 "*He-he-he!*..."
    call ton_main("Which they most certainly will, as her aunt is head of the Ministry's department for \"Magical Law Enforcement\"...", "open", "closed", "worried", "down")
    call ton_main("Our whole operation would be busted! And we'd get locked up once and for all!", "upset", "base", "worried", "mid")

    m "So, are we in trouble?"
    call ton_main("Not yet...", "open", "closed", "worried", "mid")
    call ton_main("Luckily I was able to erase Susan's memory of the ordeal with the obliviate spell.", "mad", "base", "worried", "downR")
    m "You can do that? Neat..."
    call ton_main("But, if this should happen to her again, I doubt there is much I could do to prevent her from telling her aunt right away...","open","base","worried","R")
    m "So what do you suggest we do?"
    call ton_main("Find the student who cursed her, and then talk some sense into her so that she never does it again...","open","closed","base","mid")
    m "Find{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8} her?"
    call ton_main("Yes! She heard a girl's voice in her head - while she was under the influence of the imperius curse...","open","base","angry","mid")
    call ton_main("Who told her{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8} to lift up her top.","upset","base","worried","R")
    g9 "Oh yes?"
    call ton_main("The imperius curse can make people do {b}unspeakable things{/b} against their will!","open","closed","angry","mid")
    call ton_main("I have no doubt that someone as sweet and good-hearted as Susan wouldn't know how to defend herself against it...", "open", "base", "worried", "mid")
    call ton_main("So... She showed her breasts to a bunch of other students...{w=1.4} unfortunately...", "upset", "base", "worried", "R")
    g9 "I wish I could have been there to stop it!"
    call ton_main("Of course you do...","open","closed","base","mid")
    call ton_main("That's sadly all the information I can share...", "annoyed", "base", "annoyed", "down")
    call ton_main("Nobody there saw who might have cursed her...","open","base","worried","mid")

    m "Should we get some help finding her?" # "her" because they know it's a girl
    call ton_main("*Hmmm*... Good idea.", "normal", "base", "base", "R")
    m "Shall I ask Snape? Maybe even Miss Granger?"
    call ton_main("Yes. Professor Snape might prove himself useful for once...","open","base","base","down")
    call ton_main("I don't know about Granger... She'd need to keep quiet at all costs!", "normal", "base", "raised", "down")
    call ton_main("The Ministry can't know about this!","open","base","angry","mid")
    m "Yes. Yes..."
    call ton_main("Well, I should get going... there are a couple of students I'd like to question.","open","base","worried","R")
    m "Good luck, then."
    call ton_main("Talk to you soon, [ton_genie_name].", "normal", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    m "I should definitely get Snape on this..."
    m "And Granger..."
    g9 "Or I could jerk off instead!" # Achievement if you do, maybe?
    g9 "Yes that seems like a good idea right now!"

    # TODO: Add hidden achievement called "Follow the script!" and unlock it if you jerk off after this scene. Maybe add some Susan smut writing for the jerk-off session?

    $ tonks_busy = True
    $ astoria_intro.E1_complete = True

    jump main_room


### Event 2 - Hermione ###
# You astk Hermione to find the student.

label astoria_intro_E2_hermione:
    m "I require your help with something."
    m "Tonks came by earlier and informed me about a student making a ruckus."
    m "I-- *Uhm*...{w} She thought maybe you could be of help finding her?"
    call her_main("Of course, Sir.", "base", "happyCl", "base", "mid")
    m "Apparently a student got hit by an \"unforgivable curse\" here at the school."
    call her_main("AN unforgivable CURSE!!!", "scream", "wide", "base", "stare", trans=hpunch)
    call her_main("AT our school?!", "shock", "wide", "base", "mid")
    call her_main("SOMEONE COULD BE DEAD!", "scream", "wide", "base", "R")
    call her_main("OR TORTURED!!", "disgust", "happyCl", "worried", "mid")
    call her_main("OR WORSE!!!", "disgust", "base", "worried", "R")
    m "really?"
    call her_main("Those are the only things that can happen with an unforgivable curse, [genie_name]!", "angry", "base", "worried", "mid")
    m "of course... I'm just making sure you were aware of them..."
    call her_main("It's the first lesson we ever received in defence against the dark arts.", "open", "closed", "base", "mid")
    m "Well, one's been cast somewhere in the school."
    m "and I need your help finding out who did it..."
    call her_main("Why do you need my help?", "soft", "wink", "base", "mid")
    call her_main("Surely you're able to detect them?", "base", "base", "base", "mid")
    m "Unfortunately not... I must have been... asleep... when the thing happened..."
    m "I missed my chance, so to speak..."
    call her_main("So how do you expect me to find out who did it?", "soft", "base", "base", "R")
    m "I'm certain that it's the work of another student..."
    m "(or Snape has finally snapped...)"
    m "so I'll need you to go undercover to find out who."
    call her_main("really? You're depending on me to find a criminal student within our school?", "soft", "narrow", "base", "down",cheeks="blush")
    m "If it's not too much troub--"
    call her_main("I'd be honoured, [genie_name]!", "scream", "closed", "base", "mid")
    call her_main("It's no doubt the work of one of those despicable slytherins...", "open", "closed", "angry", "mid")
    call her_main("Nothing would give me greater pleasure than to see scum like that sent to Azkaban...", "angry", "narrow", "angry", "R")

    # Genie already knows about Azkaban.
    #m "And what's Azkaban?"
    #call her_main("... Is this another test sir?", "open", "wink", "base", "mid")
    #m "Sure..."
    #call her_main("Of course! I know everything about it!", "smile", "happy", "base", "mid_soft")
    #call her_main("It's the prison of the damned... An impenetrable rocky outcrop surrounded by the harsh North Sea...", "open", "happyCl", "base", "mid")
    #call her_main("the guards are the deathly eaters of all happy thoughts and emotions known as dementors...", "open", "narrow", "angry", "R")
    #call her_main("They endlessly patrol the prison, devouring all hope from the prisoners, driving them mad within a few days...", "open", "base", "angry", "mid")
    #call her_main("Tormenting them relentlessly for the rest of their miserable lives...", "grin", "happyCl", "base", "mid")
    #call her_main("And the perfect place to house all those dirty slytherins!", "angry", "base", "angry", "mid")

    menu:
        m "(...)"
        "\"just find her...\"":
            call her_main("Very well, Sir...", "soft", "base", "base", "R")

        "\"No one's getting sent to Azkaban...\"":
            m "By the gods, [hermione_name], what's wrong with you?"
            call her_main("What are you talking about, [genie_name]?", "open", "base", "base", "R",cheeks="blush")
            call her_main("Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse...", "open", "closed", "base", "mid")
            m "I've been given special permission to punish them as I see fit."
            call her_main("Oh...", "annoyed", "base", "base", "mid")
            call her_main("So no Azkaban?", "soft", "base", "base", "R")
            m "Not unless they've killed someone..."
            call her_main("Really? So there's still a chance?", "base", "narrow", "base", "mid_soft")
            m "Only if you find a body..."
            call her_main("yay!", "smile", "happyCl", "base", "mid")

    call her_main("Consider it done, [genie_name]!", "open", "closed", "base", "mid")

    call her_walk(action="leave")

    call bld
    if astoria_intro.E2_snape:
        m "I wonder if she'll find her before Snape..."
    else:
        m "I should probably tell Snape as well..."

    $ hermione_busy = True
    $ astoria_intro.E2_hermione = True

    jump main_room


### Event 2 - Snape ###
# You ask Snape to find the student.

label astoria_intro_E2_snape:
    m "Tonks came by earlier and informed me about one of your students causing trouble."
    call sna_main("Really?","snape_03") #No xpos change.
    call sna_main("Why are you telling me?","snape_04")
    m "Apparently somebody got hit by something called an \"unforgivable\" curse at the school..."
    call play_sound("scratch")
    call sna_main("","snape_11")
    with hpunch
    pause.2

    call sna_main("Shit... this isn't good...","snape_08")
    m "She worries that the ministry might find out about it if we don't do anything."
    call sna_main("This really isn't good...","snape_07")
    call sna_main("If they send an auror here they might find out what we've been doing!","snape_10")

    m "Didn't they already do that?"
    call sna_main("We got lucky with Tonks, but if they were to send another Auror investigating the curses.","snape_03")
    call sna_main("They might get wind of all the favour trading that we've been doing as well.","snape_10")
    call sna_main("Fucking our students isn't something teachers are supposed to do genie!","snape_25")
    sna "We can't risk receiving any more attention on the matter."
    call sna_main("If an auror finds out what's going on here we're both going to Azkaban!","snape_16")
    m "so what are we going to do?"
    call sna_main("We'll just have to make sure that no more curses are cast...","snape_01")
    m "How do we manage that?"
    call sna_main("We have to find out who's been casting them.","snape_24")
    call sna_main("Normally the real Dumbledore would be able to detect who had cast them, but seeing as how you're here instead...","snape_06")
    call sna_main("We'll have to find them the old-fashioned way.","snape_10")
    m "So you want me to launch a manhunt?"
    call sna_main("Are you crazy? We can't let anyone know what's happened. All the students will panic thinking someone's been murdered...","snape_16")
    call sna_main("It's probably just an imperio or crucio that's been cast.","snape_24")
    call sna_main("I'll start the search immediately. In the meantime, just stay here and keep yourself busy.","snape_10")
    m "You don't want my help?"
    call sna_main("Not really... Tonks and I will get this situation under control.","snape_02")
    if astoria_intro.E2_hermione:
        m "And Granger..."
        call sna_main("Have you told her about this?!","snape_03")
        m "Sure... She seemed eager to help."
        call sna_main("Of course she did...","snape_06")
        call sna_main("(You bloody fool...)","snape_35")

    call sna_main("Don't worry, I'll find that student in no time. You shall see...","snape_02")

    call sna_walk(action="leave")

    call bld
    m "What a drama queen..."

    $ snape_busy = True
    $ astoria_intro.E2_snape = True

    jump main_room


### Event 3 ###
# Hermione brings Astoria to you.
# Snape scolds her and Tonks gives her detention.

label astoria_intro_E3:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*knock* *knock* *knock*"
    m "(...)"

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    menu:
        m "..."
        "\"What?\"":
            pass
        "\"Not now...\"":
            pass

    with hpunch
    femv "Stop pulling me!"
    her "Shut it already!"
    femv "Why did you drag me here?"
    her "You know very well why I brought you!"
    femv "Let me go you filthy mudblo--"
    call play_sound("thump")

    m "Who's there?"
    her "*Shhhhh*- now!"
    m "..."
    her "It's Hermione Granger, Sir."
    her "Although... I'm not alone."
    m "Come in."

    call her_walk(action="enter", xpos="desk", ypos="base")

    call play_music("hermione")
    call her_main("Hello sir.","normal","happy", xpos="mid", ypos="base")
    m "I thought you said you weren't alone?"
    call her_main("I'm not.", "annoyed", "narrow", "base", "R_soft")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.2

    call her_chibi("stand","desk",flip=True)
    pause.5

    call her_main("Get in here, Astoria!", "annoyed", "narrow", "angry", "R", ypos="head", flip=True)
    ast "{size=+2}{b}No!{/b}{/size}"
    call her_main("Do you want to make this worse?", "scream", "closed", "base", "mid", trans=hpunch)
    ast "no..."
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand","desk","base", flip=False)
    pause.2

    call play_sound("door")
    call ast_chibi("stand","door","base")
    with d3
    pause.8

    # Astoria enters.
    call ast_walk(500,"base")

    call play_music("playful_tension")
    call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base", flip=False)
    call ast_main("...","annoyed","base","worried","R", xpos="right", ypos="base")

    m "..."
    m "And who's this?"
    call her_main("Astoria Greengrass, Sir.", "soft", "narrow", "annoyed", "mid", xpos="560", ypos="base") # Hermione moves closer.
    call her_main("You asked me to bring you the person who cast the unforgivable curse, Sir.", "soft", "narrow", "annoyed", "mid")
    call her_main("And here she is.", "grin", "base", "angry", "mid")
    m "I thought it would be some angsty girl who listens to death metal - or something..."
    m "Not some innocent looking girl--"
    call ast_main("I am not!","clench","narrow","angry","mid")
    call ast_main("You don't know what you're talking about, you ancient old man!","annoyed","narrow","angry","R")
    m "(Oh, you have no idea...)"

    call her_main("What's going to be her punishment, Sir?", "soft", "base", "angry", "mid")
    call ast_main("Punishment? I didn't do anything!","clench","base","worried","mid")
    call her_main("You know very well what you did!", "angry", "closed", "angry", "mid")
    call her_main("Sir, I overheard her boasting about it in the library - to a group of Slytherins.", "annoyed", "narrow", "worried", "mid_soft")
    call her_main("By the sounds of it, she used Imperio to control another student!", "annoyed", "base", "base", "mid")
    call ast_main("I did not!","annoyed","base","worried","L")

    call her_main("Shall I go fetch a vial of veritaserum from Professor Snape, sir?", "grin", "base", "base", "mid")
    call ast_main("V-veritaserum?!","clench","base","worried","mid")
    call ast_main("That's illegal!","clench","base","base","mid")
    call her_main("Not when you've been casting unforgivable curses - you evil little witch!", "grin", "base", "angry", "mid")
    call ast_main("Fine!","clench","closed","angry","mid")
    call ast_main("I'll tell you what happened, Sir...", "open","narrow","base","mid")
    call ast_main("But only if this Gryffindor leaves!","annoyed","narrow","base","mid")
    call her_main("Not a chance!", "angry", "closed", "angry", "mid")

    $ d_flag_01 = False

    menu:
        m "(...)"
        "\"You're dismissed, Miss Granger!\"":
            call her_main("What?!", "open", "wide", "worried", "shocked")
            pass

        "\"Go and fetch Snape!\"":
            $ d_flag_01 = True
            pass

    call her_main("But Sir, I'd really like to know what her punishment is going to be!", "angry", "base", "base", "mid")

    m "That's none of your concern."
    call her_main("Yes it is! And I demand to be rewarded!", "angry", "closed", "angry", "mid")
    call her_main("Given that I was the one who caught her, I think it's only fair!", "annoyed", "base", "angry", "mid")

    m "(...)"
    menu:
        "\"Not now, Miss Granger...\"":
            m "We'll talk about your reward later..."
            call her_main("But!", "disgust", "narrow", "worried", "down")
            m "No butts..." # deliberate.
            call her_main("*Hmph*", "annoyed", "narrow", "angry", "R")
            call her_main("Fine...", "open", "closed", "angry", "mid")
            $ her_mood += 12

        "\"How about some house points instead?\"":
            call her_main("*Hmm*...", "annoyed", "narrow", "angry", "R")
            call her_main("How many house points?", "soft", "base", "angry", "mid")

            menu:
                m "(...)"
                "\"How about ten?\"":
                    call her_main("Ten?", "disgust", "base", "worried", "mid")
                    call her_main("I expected more for this, Professor!", "open", "base", "angry", "mid")
                    m "Take 'em or leave 'em..."
                    call her_main("...", "annoyed", "narrow", "angry", "R")
                    call her_main("Very well...", "open", "closed", "base", "mid")
                    $ her_mood += 6
                    $ gryffindor += 10

                "\"You'll get twenty.\"":
                    call her_main("...", "annoyed", "base", "base", "R")
                    call her_main("I suppose that's fair.", "open", "closed", "base", "mid")
                    $ her_mood = 0
                    $ gryffindor += 20

    call her_main("In a few days everyone at Hogwarts will know what happened to her...", "grin", "base", "angry", "mid")
    call her_main("When she's sent to Azkaban!", "soft", "squint", "angry", "mid")
    m "Nobody's going anywhere, except for you, Miss Granger..."

    if d_flag_01:
        m "Now go and fetch Snape for me."
    else:
        m "You may leave..."

    call her_main("...", "annoyed", "narrow", "angry", "R")
    call ast_main("*cough*... {size=-4}mudblood...{/size}","annoyed","narrow","angry","L")
    call her_main("*Tzzzs!*...", "angry", "closed", "angry", "mid")
    if d_flag_01:
        call her_main("I'll go {i}fetch{/i} professor Snape then...", "annoyed", "narrow", "angry", "R")
    else:
        call her_main("I'll go back to class then...", "annoyed", "narrow", "angry", "R")
    call her_main("Good day, Professor.", "open", "base", "angry", "mid")
    stop music fadeout 2.0

    call her_walk(action="leave")
    pause.2

    call ast_walk(460,"base")
    pause.2

    call ast_main("...","annoyed","base","base","L")
    m "..."

    call ast_main("Now what, sir?","annoyed","base","worried","mid")
    if d_flag_01:
        m "You'll find out when professor Snape gets here."
    else:
        m "You'll find out once I've summoned professor Snape."
        m "Give me a second..."
    call ast_main("...","annoyed","narrow","worried","down")
    call ast_main("(Better him than any of the other teachers...)","clench","narrow","base","down")

    $ snape_chibi.zorder = 4 # In front of Astoria
    call sna_walk(action="enter", xpos="mid", ypos="base")

    call play_music("snape")
    $ astoria_zorder = 13
    call ast_main("","annoyed","base","worried","R", xpos="400", ypos="base")
    call sna_main("You wanted to see me?","snape_09", xpos="600", ypos="base")
    call ast_main("...","annoyed","narrow","worried","L")
    call sna_main("Astoria?!","snape_05")
    call sna_main("Why is one of my students in your office? Don't tell me you...","snape_03")
    m "It's not that sort of visit."
    call sna_main("Really? Then what's she doing here?","snape_01")
    m "She's the one who cast that curse."
    call sna_main("Truthfully? A Slytherin?","snape_05")
    call sna_main("I expect better than this from my students, Miss Greengrass...","snape_10")

    call sna_main("The very first lesson I give you is don't--","snape_08")
    call sna_main("get--","snape_08", trans=hpunch)
    call sna_main("caught!","snape_15", trans=hpunch)
    pause.5

    call sna_main("Do you have anything to say for yourself?","snape_10")
    call ast_main("I-I'm sorry, sir... It won't happen again.","clench","narrow","base","down")
    call sna_main("Who did you cast it on you little idiot?","snape_32")
    call ast_main("Susan Bones, Sir...","annoyed","narrow","base","down")
    call sna_main("The Hufflepuff cow--","snape_44")
    call sna_main("*Ahem*...","snape_09")
    m "..."
    call sna_main("That cowardly Hufflepuff girl?","snape_38")
    call ast_main("Yes.","open","narrow","worried","L")
    call ast_main("I... might have used Imperio to embarrass her a little...","smile","narrow","worried","mid")
    call sna_main("Well as long as you only cast it once...","snape_09")
    call sna_main("We have to make sure this stays under wraps.","snape_34")
    call sna_main("Miss Greengrass, you will not mention this incident to any other student or teacher, am I clear?","snape_35")
    call ast_main("Yes Sir, I promise...","annoyed","narrow","worried","down")
    call sna_main("You should count yourself lucky the ministry hasn't been notified...","snape_31")
    call sna_main("Miss Tonks has been kind enough to wipe the co--","snape_01")
    call sna_main("Susan's memory of the event.","snape_03")
    call sna_main("You owe her big time...","snape_25")
    call ast_main("Of course...","annoyed","narrow","worried","L")
    call sna_main("I'll leave her punishment to the two of you...","snape_04")
    call sna_main("I have someone--","snape_09")
    call sna_main("*Uhm*... I've got an appointment to attend to in my office.","snape_35")
    m "Naturally..."
    call sna_main("Until next time... Albus.","snape_09")
    m "And Albus to you--"
    g4 "I mean..."
    g9 "Until next time!"
    call sna_main("...","snape_04")

    # Snape leaves and runs into Tonks.
    call play_music("stop")
    call sna_walk(660,"base")

    # Equip Tonks default clothing.
    $ ton_outfit_last.save() # Store current outfit.
    $ tonks.equip(ton_outfit_default)

    call play_sound("door")
    call ton_chibi("stand",780,"base")
    with d3
    pause.2

    call ast_chibi("stand","desk","base", flip=True)
    with d3

    call ton_main("Snape. How good to see you!", "soft", "shocked", "base", "mid", hair="neutral", ypos="head")
    call sna_main("Save your compliments for someone else... I'm in a bit of a hurry.","snape_03", ypos="head")
    call ton_main("Still mad at me for taking your post?","base","base","angry","mid")
    call ton_main("I'd be willing to compensate you for it, you know...","horny","base","base","mid", hair="horny")
    call sna_main("...","snape_12")
    m "*Ahem*..."
    call sna_main("Would you mind?","snape_12")
    call ton_main("Sure...{heart}","horny","base","angry","mid")
    call sna_main("Stepping aside.","snape_18")
    call ton_main("Oh, okay...", "annoyed", "closed", "base", "mid")

    call sna_walk(action="leave")
    pause.2
    $ snape_chibi.zorder = 2 # Reset zorder

    call ton_walk(500,"base")
    call ast_chibi("stand","desk","base", flip=False)
    with d3

    call play_music("tonks")
    pause.1
    call ast_main("","annoyed","base","base","mid", xpos="right", ypos="base", flip=False)
    call ton_main("Hello, Professor.","base","base","base","mid", hair="neutral", xpos="base", ypos="base")

    call ton_main("Astoria? What are you doing here?","upset","base","worried","L")
    call ton_main("You didn't cause any mischief, I hope.", "open", "narrow", "base", "L")
    call ast_main("Of course not.","annoyed","base","worried","down")
    call ton_main("Wait. Is she the one who cursed Susan?", "clench", "wide", "shocked", "stare")
    call ton_main("","upset","base","worried","mid")
    m "Yep."
    call ton_main("(Oh shit!)","horny","base","raised","L", hair="horny")

    call ast_main("I'm really sorry! I promise I won't ever cast it again!","open","narrow","base","R")
    call ton_main("Really? It was you who cast the spell?", "grin", "base", "raised", "L")
    call ast_main("...","annoyed","narrow","worried","down")
    call ton_main("It couldn't possibly have been someone as cute as you!", "soft", "base", "raised", "down")
    call ast_main("...","clench","narrow","worried","down") # Embarrassed, stares down.
    call ast_main("Please don't send me to Azkaban!","scream","closed","base","mid")
    call ast_main("","annoyed","narrow","base","down")
    call ton_main("Don't worry, It won't come to that...", "grin", "narrow", "base", "down")
    call ton_main("The ministry isn't going to lock away such a cute little thing like yourself...","base","base","base","L")
    call ton_main("{size=+2}Over a little harmless fun.{/size} {heart}", "horny", "base", "shocked", "L")

    call ton_main("It's just the Imperius curse.", "grin", "base", "raised", "R")
    call ton_main("Most students don't have the guts to cast crucio on another person...", "base", "narrow", "base", "down")
    call ton_main("Let alone Avada Kedavra...", "soft", "closed", "shocked", "mid")

    m "..."
    call ton_main("So, you had some fun with Susan, I gather?", "base", "narrow", "base", "L")
    call ton_main("Want to tell me what you made her do?","horny","base","angry","L")
    m "(Doesn't she already know that?)"
    call ast_main("I might have made her show her boobs to some second years...","annoyed","narrow","base","R")
    call ton_main("*ha-ha-ha-ha!*", "silly", "happyCl", "base", "mid", trans=hpunch)
    call ast_main("Just for a second!","clench","base","base","mid")
    m "(what's going on here?)"
    call ton_main("Is that all?", "open", "base", "raised", "L")
    call ton_main("You probably did Susan some good then...", "crooked_smile", "base", "raised", "mid")
    call ton_main("She sure needs to loosen up a bit.", "soft", "base", "base", "R")

    call ton_main("She always has been very sensitive about her body for some reason.","base","base","raised","mid")
    call ast_main("So I'm not going to get in trouble?","open","base","worried","mid")
    call ton_main("I didn't say that... You still cast a very serious spell...", "base", "base", "annoyed", "L")
    call ast_main("","annoyed","base","base","mid")
    call ton_main("A couple of hours of detention with me should be an appropriate punishment for casting an unforgivable curse.","open","base","base","L")
    call ton_main("Wouldn't you agree, Professor?","base","base","raised","mid")

    $ d_flag_01 = False

    menu:
        m "(...)"
        "\"Seems reasonable to me.\"":
            call ast_main("Really? Only detention?","smile","base","base","mid")
            call ton_main("I'm very much looking forward to it.","base","happyCl","base","mid")
            call ast_main("Wicked!","clench","narrow","angry","down")

        "\"Why don't you just reward her at this point...\"":
            $ d_flag_01 = True

            call ast_main("What?","smile","base","angry","mid")
            call ton_main("*Hmm*... I agree.","horny","base","raised","L")
            m "Miss Tonks, I was being sarcastic..."
            call ton_main("But you're right though, Professor!", "grin", "base", "shocked", "mid")
            call ton_main("Casting the Imperius curse at her age is no easy task!","open","closed","base","mid")
            call ton_main("A girl with that type of...{w=0.3} talent, is a rare thing.","horny","base","raised","L") # Horny
            call ton_main("I would say, fifty points for Slytherin should be appropriate.", "base", "base", "annoyed", "mid")
            call ast_main("!!!","clench","base","base","mid")
            g4 "(If Hermione hears about this - she'll {i}Abra Kadabra{/i} my head off!)"
            g4 "(And not the one on my shoulders...)"
            call ton_main("But you'll still have to visit me for detention.", "open", "base", "annoyed", "L")
            call ast_main("I guess I can do that...","smile","base","base","R")
            call ton_main("Wonderful.","base","happyCl","base","mid")
            $ slytherin += 50

    call ton_main("That should be all for now, Astoria.","open","base","base","L")
    call ast_main("...","annoyed","base","base","down")
    call ton_main("Have a good night, cutie.","base","happyCl","base","mid")
    call ast_main("*Uhm*...{w=0.3} Good night then.","open","base","base","mid")

    # Astoria leaves.
    call play_music("stop")
    call hide_characters
    call ast_chibi("stand","desk","base", flip=True)
    hide screen bld1
    with d3
    pause.1

    call ast_walk(action="leave")
    pause.1

    call ton_walk("desk","base")

    call play_music("playful_tension")
    call ton_main("She's {size=+5}so cute!{/size} Isn't she? {heart}", "base", "base", "raised", "R", xpos="mid", ypos="base")

    if d_flag_01:
        m "You gave her fifty house points..."
        g4 "For what you previously described as a serious crime?"
        call ton_main("I know! I shouldn't have rewarded her, but...","upset","closed","worried","mid")
        call ton_main("Did you see how her face lit up!", "grin", "narrow", "raised", "mid")
        call ton_main("I thought we were supposed to encourage our students, [ton_genie_name].", "upset", "base", "shocked", "down")
        m "Don't put this on me..."
        call ton_main("Fine, maybe I got a bit too excited...", "mad", "base", "worried", "mid")

    else:
        m "A couple of hours of detention..."
        m "For what you previously described as a serious crime?"
        call ton_main("Did I go too soft on her?","upset","base","worried","mid")
        m "Oh, don't get me wrong. I couldn't care less about this school."
        m "I'm not even supposed to be here..."
        call ton_main("Fair enough...", "normal", "base", "raised", "R")

    m "We should have a chat about Astoria again..."
    m "Discuss the severity of her... \"detention.\""
    call ton_main("Of course, [ton_genie_name].", "annoyed", "base", "raised", "downR")
    call ton_main("I'm glad we're on the same page...{heart}", "grin", "closed", "base", "mid")
    m "Until next time, [tonks_name]."
    call ton_main("Until next time!{heart}","base","happyCl","base","mid")
    call play_music("stop")

    call ton_walk(action="leave")

    call bld
    m "(...)"
    m "(I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed up for...)"

    # Reset Tonks.
    $ tonks.equip(ton_outfit_last)

    $ hermione_busy = True
    $ snape_busy = True
    $ tonks_busy = True

    $ astoria_intro.E3_complete = True

    jump main_room


### Tonks Hangout Event 1 ###
# Tonks wantes to teach Astoria the Imperius curse.

label nt_he_astoria_E1:
    call ton_main("So about this girl.","open","closed","base","mid")
    m "You're going to have to be more specific."
    call ton_main("Astoria Greengrass.", "open", "wide", "base", "mid")
    m "Ah yes, the hot-headed one."
    call ton_main("Yes, she's pretty cute isn't she...","base","happyCl","base","mid")
    call ton_main("I wouldn't mind giving her a thorough robe inspection - if you know what I'm saying.", "horny", "base", "raised", "mid", hair="horny")
    call ton_main("This girl...{w=0.5} she's special...{w=0.8} different...","open","base","base","R", hair="neutral")
    m "You've got the hots for this girl?"
    call ton_main("She's a Slytherin!", "mad", "base", "raised", "mid")
    m "People keep saying that as if I'd know what the problem is."
    call ton_main("Oh yes... I guess I'm a teacher now - so I should be more impartial...", "upset", "base", "raised", "down")
    call ton_main("Old habits, I suppose.", "soft", "base", "base", "R")
    call ton_main("But no, it's not that.", "open", "base", "base", "mid")

    call ton_main("This girl you see, she's cursed... and it's quite a hefty curse at that!", "open", "narrow", "worried", "R")
    m "You don't say..."
    #call ton_main("This girl is cursed... and it's quite a problem.","base","base","base","mid")
    #m "Don't you mean this cursed girl {i}is{/i} a problem?"
    #call ton_main("No, she's cursed. Quite a hefty curse at that!","base","base","base","mid")
    #m "..."
    call ton_main("Her family - the Greengrass family - is quite infamous in the wizarding world.", "open", "base", "base", "L")
    call ton_main("They're known for being a very high class family of witches and wizards...", "open", "base", "raised", "R")
    call ton_main("Some of them are very stuck-up and spoiled, for that reason.", "upset", "base", "base", "R")
    call ton_main("It's quite the norm for most pure-blood families, actually.","open","closed","base","mid")
    m "Get to the point..."
    call ton_main("*Sigh*", "disgust", "base", "base", "down")
    call ton_main("One of the Greengrass ancestors was put under a blood curse, and I fear that parts of this curse have trickled down through the generations and surfaced in Astoria.", "upset", "base", "worried", "mid")
    call ton_main("Its original purpose was to bring down the family and make them appear weak in the eyes of the wizarding community.", "normal", "base", "base", "R")
    call ton_main("Every now and then one of the family members would become frail and live a short life.", "normal", "closed", "worried", "mid")
    m "Oh shit..."
    call ton_main("Yeah...","upset","base","worried","down")
    m "Hey, at least it's not the other way round, am I right..."
    m "Immortality can be quite the curse too you know..."
    call ton_main("Yes, I can see how much you're hurting inside...", "normal", "base", "base", "R")
    call ton_main("The opportunity to have sex with some of the most attractive women in all of history must really suck.", "soft", "base", "raised", "mid")
    m "I'll live with it..."

    call ton_main("Fortunately this curse has faded after many generations, but in turn it appears to have evolved into something else...","open","closed","base","mid")
    m "How would you know?"
    call ton_main("I'm an auror...", "base", "shocked", "base", "mid")
    m "Is that your answer for everything now?"
    call ton_main("Just trust me...","open","closed","base","mid")
    call ton_main("The nature of it is quite familiar to me.", "open", "base", "base", "R")
    call ton_main("I have strong reasons to believe that this girl is...", "upset", "closed", "angry", "R")
    call ton_main("She's...","upset","base","worried","down")
    m "She's what?"
    call ton_main("She's asexual!", "mad", "shocked", "worried", "mid")
    m "..."
    call ton_main("You don't believe me?", "mad", "narrow", "base", "down")
    m "Oh no, I believe you."
    m "..."
    m "Mind explaining to me what asexual's supposed to mean?"
    call ton_main("You don't know?", "open", "shocked", "raised", "mid")
    call ton_main("Well that's not too surprising - all things considered...", "normal", "narrow", "base", "L")
    call ton_main("It means she experiences no sexual desires or attractions. To anything!", "annoyed", "narrow", "shocked", "mid")
    g4 "WHAT?!"
    call ton_main("I know!", "mad", "base", "worried", "mid")
    m "By the great desert sands... That's a curse worse than death."
    call ton_main("The curse has seemingly gone from killing off random members of their family to preventing new members from being born.","upset","base","base","R")
    #g4 "Wait, since when can spells change their outcome like that?"
    m "Magic doesn't make any fucking sense in this universe..."
    call ton_main("Hey, it makes perfect sense!","open","base","angry","mid")
    call ton_main("...","upset","base","worried","R")
    call ton_main("In any case, I'd like to keep an eye on her - if you don't mind.","open","base","angry","mid")
    m "Go right ahea--"
    call ton_main("Maybe even teach her how to cast Imperio properly.", "annoyed", "base", "base", "R")
    m "..."
    with hpunch
    g4 "Hold on a second...{w=0.8} what?!"
    g4 "You want to teach this {b}sadist{/b} how to cast those illegal curses?"
    m "That's what caused all this trouble in the first place!"
    call ton_main("Don't worry, I'm just gonna teach her the basics...","open","closed","base","mid")
    call ton_main("I won't allow her to go out and curse students at random.", "mad", "closed", "annoyed", "mid")
    call ton_main("But... Maybe this can help ignite that \"sexual urge\" - deep inside of her...", "mad", "base", "raised", "R")
    call ton_main("She clearly isn't ready to do it with some boy...","open","base","raised","mid")
    call ton_main("Or you, for that matter.", "upset", "base", "raised", "R")
    m "If she's really cursed with \"Asexuality\" - then I don't want to have her anywhere close to me."
    call ton_main("It's not contagious, you numpty!", "open", "base", "annoyed", "mid")
    call ton_main("Have you not been paying attention? It's a family curse!", "mad", "base", "angry", "mid")
    m "..."
    call ton_main("That being said, I'd rather have her do it with me...", "base", "base", "raised", "R", hair="horny")
    m "Are we still talking about the curse thingy?"
    call ton_main("Yes...", "soft", "narrow", "raised", "downR")
    m "So your goal is to get rid of this curse by somehow awakening her sexuality?"
    call ton_main("It might not be that easy, but I think it would be a good start.","open","base","base","L")
    call ton_main("I must at least know if my theory is correct...", "normal", "base", "base", "R")
    m "I don't see how this \"Imperio\" thing plays into it, but if you say so..."
    call ton_main("I'll speak to Miss Greengrass.","open","base","base","mid")
    call ton_main("I doubt she'll have many objections...","base","happyCl","base","mid")

    ">You ask Tonks to explain asexuality to you some more..."
    ">You still can't wrap your mind around the fact that such a horrible thing exists..."

    $ nt_he.astoria_E1 = True

    jump main_room


### Event 4 ###
# Astoria summon unlock.
# If you pick the wrong choice Astoria won't return for a week and ignores you.

label astoria_intro_E4:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*knock* *knock* *knock*"
    m "(...)"

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    menu:
        m "..."
        "\"Who is it?\"":
            ast "Professor, may I come in?"
            g4 "It's that accursed, cursed girl!"
            ast "Sir?"

        "\"Not now...\"":
            ast "But, Professor Tonks told me you wanted to speak with me."
            m "She did?"
            ast "Yes."

    menu:
        m "..."
        "\"Come in.\"":
            ast "..."
            pass

        "\"I'm busy.\"":
            ast "*Uhm*..."
            ast "Very well, Sir."
            ast "I shall be back tomorrow..."
            m "..."

            $ ag_event_pause += 1
            $ astoria_busy = True

            jump main_room

    call ast_walk("desk","base")
    pause.2

    call play_music("astoria")
    call ast_main("Hello, Professor.","smile","base","base","mid", xpos="mid", ypos="base")
    call ast_main("Professor Tonks told me to talk to you, Sir.","open","base","base","R")
    m "....................."
    m "She did?"
    call ast_main("Yes, Sir...","annoyed","base","base","mid")
    m "(Shit, was I supposed to do anything with her?)"
    call ast_main("....................","annoyed","base","base","R")
    m  "(Oh that's right. Freeing her from her curse...)"
    call ast_main("Sir, If there's nothing you need of me then I'd like to leave...","open","narrow","base","mid")

    menu:
        m "..."
        "\"What about your detention?\"":
            call ast_main("Oh...","clench","base","base","down")
            m "If I recall correctly, we have yet to discuss your punishment."
            call ast_main("So you didn't forget about that...","clench","base","worried","mid")
            pass

        "\"You still need to be punished!\"":
            call ast_main("Punished?!","clench","base","base","mid")
            call ast_main("I thought I was only getting detention?","open","base","worried","mid")
            m "Yes, detention."
            pass

        "\"Fine by me...\"": # Fails.
            call ast_main("I'll head back to the dungeons then.","smile","base","base","R")
            m "See ya."

            # Astoria leaves.
            call ast_walk(action="leave")

            call bld
            m "I'd better not mention this to Tonks..."
            m "I'm sure she'll come back for her punishment."

            $ ag_event_pause += 7 # Returns a week later.

            jump main_room

    m "It's just a couple of hours with your teacher."
    g9 "I'm sure you'll enjoy it!"
    call ast_main("If you say so, Sir.","open","closed","base","mid")
    call ast_main("...","annoyed","narrow","base","R")
    call ast_main("Would it be okay if I go there some other time?","open","base","base","mid")
    m "Are you trying to weasel yourself out of your punishment?"
    call ast_main("No?","annoyed","base","base","mid")
    call ast_main("It's just that... I really don't have time right now...","open","base","base","down")
    m "..."
    m "I'll allow it. But just this once!"
    call ast_main("Thank you!","smile","closed","base","mid")
    m "You're dismissed..."
    call ast_main("...","grin","base","angry","R")

    # Astoria leaves.
    call ast_walk(action="leave")

    call bld
    m "..."
    g9 "I'd like to go on detention with that nympho myself!"
    m "That girl should consider herself lucky..."

    $ astoria_busy = True

    $ astoria_unlocked = True
    $ astoria_wardrobe_unlocked = True # TODO: Move to a proper event once they've been added.
    $ achievement.unlock("unlockast", True)
    call popup("{size=-4}You can now summon Astoria into your office.{/size}", "Character unlocked!", "interface/icons/head/astoria.webp")

    $ astoria_intro.E4_complete = True

    jump main_room
