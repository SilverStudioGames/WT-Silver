

label hg_tutor_start:

    # Tier 1
    if her_tutoring == 1:
        jump hg_tutor_E1
    elif her_tutoring == 2:
        jump hg_tutor_E2
    elif her_tutoring == 3:
        jump hg_tutor_E3

    # Tier 2
    elif her_tutoring == 4 and her_tier >= 2:
        jump hg_tutor_E4
    elif her_tutoring == 5 and her_tier >= 2:
        jump hg_tutor_E5

    # Tier 3
    elif her_tutoring == 6 and her_tier >= 3:
        jump hg_tutor_E6
    elif her_tutoring == 7 and her_tier >= 3:
        jump hg_tutor_E7

    # Tier 4
    elif her_tutoring == 8 and her_tier >= 4:
        if adult_mag_ITEM.owned >= 1: # Adult magazines
            jump hg_tutor_E8
        else:
            m "I need to buy adult magazines for this lesson."
    elif her_tutoring == 9 and her_tier >= 4:
        if porn_mag_ITEM.owned >= 1: # Porn magazines
            jump hg_tutor_E9
        else:
            m "I need to buy porn magazines for this lesson."

    # Tier 5
    elif her_tutoring == 10 and her_tier >= 5:
        if vibrator_ITEM.owned >= 1: # Vibrator
            jump hg_tutor_E10
        else:
            m "I need to buy a vibrator for this lesson."
    elif her_tutoring == 11 and her_tier >= 5:
        if anal_plugs_ITEM.owned >= 1: # Anal plugs
            jump hg_tutor_E11
        else:
            m "I need to buy anal plugs for this lesson."

    # Tier 6
    elif her_tutoring == 12 and her_tier >= 6:
        jump hg_tutor_E12
    elif her_tutoring == 13 and her_tier >= 6:
        jump hg_tutor_E13
    elif her_tutoring == 14 and her_tier >= 6 and hg_sex.trigger and hg_anal.trigger:
        jump hg_tutor_E14
    elif her_tutoring == 15:
        m "(I have taught her everything there was to teach.)"
    else:
        m "(She's not ready for her next lesson yet.)"

    jump hermione_requests

label hg_tutor_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call her_main("[genie_name], I'm very thankful that you're doing this for me.", "open", "base", "base", "mid")
    m "Doing what?"
    call her_main("My tutoring lessons...", "soft", "squint", "base", "mid")
    call her_main("I hope you're still planning to lecture me, [genie_name]?", "annoyed", "base", "base", "mid")
    g9 "Oh, I'll give you a lecture for sure."
    call her_main("Shall I go and fetch my books, then?", "open", "squint", "base", "mid")
    m "What?"
    call her_main("My Books, [genie_name]. I need to study them more for my tests.", "soft", "base", "base", "R")
    call her_main("All the knowledge I need is in those books!", "annoyed", "narrow", "angry", "R")
    m "Books can't teach you everything, girl... Some knowledge only comes with practice and experience!"
    m "(I'm really just going to make this shit up as I go, ain't I?)"

    call her_main("Maybe... I mean, as the head of Hogwarts you probably know best.", "annoyed", "squint", "base", "mid")
    m "Sometimes you seem to forget that, Miss Granger."
    call her_main("That sounded like something professor Snape would say...", "open", "squint", "base", "mid")
    call her_main(".........", "annoyed", "squint", "base", "mid")
    call her_main("Sorry about that, he thinks he's always right and it annoys me.", "smile", "happyCl", "base", "mid")
    m "..........."
    call her_main("Sir?", "soft", "base", "base", "R")
    m "We're going to have to do it my way."

    $ d_flag_01 = False
    $ d_flag_02 = False

    menu:
        m "..."
        "-No books-":
            $ d_flag_01 = True

            m "Rule number one, no books allowed past this door."
            call her_main("Too bad, I love books.", "annoyed", "narrow", "worried", "down")
            g9 "{size=-4}And soon you'll love cock!{/size}"
            call her_main("Yes?", "soft", "base", "base", "mid", trans=d5)
            m "I didn't say anything..."
            call her_main("If you say so, [genie_name].", "open", "base", "base", "R")
        "-No back talk-":
            $ d_flag_02 = True

            m "First rule, no back talking."
            call her_main("Of course, sir!", "base", "squint", "base", "mid")
            m "Good."

    m "Now it's time we talk about your future, child."
    call her_main("I'm not a child anymore, professor!", "normal", "squint", "angry", "mid")

    if d_flag_01:
        m "You know what, let's add a second rule--"
        g4 "No back talking!"
        call her_main("B-but...--", "open", "happy", "worried", "mid")

    m "What did I just say?"
    call her_main("S-sorry...", "annoyed", "squint", "worried", "R")

    if d_flag_02:
        m "Let's add a second rule on top of the first one--"
        g4 "No{w=0.3} more{w=0.3} books!"
        m "They're an obsolete and inferior medium anyway, you don't need them."
        call her_main("(Too bad, I love books...)", "annoyed", "narrow", "worried", "down")

    m "Continuing--"
    m "I can tutor you, but you need to understand certain things about magic."
    m "With proper training, you can learn to increase your magic ability."
    call her_main("Yes?", "soft", "base", "base", "mid")
    m "Certain emotions like love and hate, pleasure and pain..."
    g9 "{size=-2}(If she falls for that, I'm a true genius!){/size}"
    call her_main("I've been studying magic for years and I've never heard of such a thing.", "normal", "base", "base", "mid")
    g4 "{size=-2}(Shit.){/size}"
    m "And that's exactly why you're still a child. You still have much to learn about magic."
    call her_main("Please stop that, professor. Nobody considers me a child anymore.", "open", "squint", "worried", "mid")
    m "Yes, technically..."
    call her_main("Technically?!", "annoyed", "base", "base", "mid")
    g4 "Enough of this. You came to me asking for my help, and if it starts like this--"
    call her_main("Yes, I suppose you are right...", "angry", "base", "worried", "mid")
    call her_main("Alright, I'm ready to study hard with you!", "base", "base", "base", "mid")
    g9 "{size=-2}Yes, we will study hard-on going forward!{/size}"
    call her_main("What was that?", "open", "narrow", "annoyed", "mid", cheeks="blush")
    call her_main("", "normal", "narrow", "annoyed", "mid", cheeks="blush")
    m "Uh, yes I'm glad you're beginning to understand, child."
    her "..........."
    m "Alright, I want you to take some time and think about what I've said. Next time we'll start with your first lesson."
    call her_main("Can't we start now?", "open", "base", "base", "mid")
    m "Miss Granger, you're not the only student I must take care of."
    call her_main("You're tutoring someone else?", "open", "wide", "base", "mid")
    m "{size=-2}(If only...){/size}"
    m "I must take care of all the students of this school."
    m "But yes, there is another girl who needs..."
    call her_main("A Slytherin girl?!", "shock", "wide", "base", "mid_soft")
    g9 "That is none of your business, miss Granger."
    call her_main("Yes, professor. I'm sorry, but with all the recent events I'm a little on edge.", "angry", "base", "angry", "mid")
    m "Apology accepted, and now goodnight!"
    call her_main("Good night, professor, and thanks again for taking some of your precious time to help me.", "base", "base", "base", "mid")

    call her_walk("door", "base")

    call her_main("{size=-4}(I'm glad the professor agreed to tutor me!){/size}", "base", "happyCl", "worried", "mid", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}", "annoyed", "base", "base", "R")

    call her_chibi("leave")

    $ her_tutoring = 2
    jump end_hermione_event

label hg_tutor_E2:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Miss Granger, time for your first lesson."
    call her_main("Yes, professor.", "soft", "base", "base", "R")
    m "Have you thought about what we discussed?"
    call her_main("Not really, I'm not sure what you mean by \"emotions.\"", "normal", "base", "base", "mid")
    g9 "{size=-2}(You'll learn soon enough, girl.){/size}"
    m "For example, what was your state of mind when you heard those rumours about the Slytherin girls?"
    call her_main("Please don't bring that up, sir! it really makes me mad!", "clench", "base", "worried", "stare")
    m "And what is this feeling?"
    call her_main("...{w=0.5}an emotion, I suppose...", "normal", "base", "base", "mid")
    m "Yes, and don't you have emotions you prefer over others?"
    call her_main("When I have the best score on a test.", "smile", "happyCl", "base", "mid")
    m "{size=-2}(This girl is a monomaniac...){/size}"
    m "Don't you have other passions, things you like to do?"
    call her_main("Yes! Studying and reading books.", "smile", "happyCl", "base", "mid")
    g4 "{size=-2}(By all the ancient gods...){/size}"
    m "Things are not going in the right direction..."
    call her_main("And what direction is that, sir?", "normal", "base", "base", "mid")
    g9 "{size=-2}(You impaled on my cock!){/size}"
    m "Adulthood, Miss Granger, adulthood..."
    call her_main("I am by far the most mature of my peers, professor. What more can you ask?", "open", "closed", "base", "mid")
    m "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn."
    m "I'm tired of all this, and I have work to do."
    m "Goodnight, {i}child{/i}."
    call her_main("Tutoring one of those filthy Slytherin girls, maybe?", "open", "narrow", "annoyed", "mid", cheeks="blush")
    m "Maybe that's the right direction, think about what all those girls do with professors."
    call her_main("But...{w=0.5} that's so wrong...{w=0.8} I don't know if I want to think about that.", "open", "base", "base", "mid")
    m "If you want to progress and to restore the Gryffindor pride, you must!"
    call her_main("Yes, you're right! It's my mission! I'll do my best, professor.", "grin", "base", "angry", "mid", cheeks="blush")
    g9 "{size=-2}(She is so naive, it's adorable.){/size}"
    m "Good, now time to go to bed, child."
    call her_main("{size=-2}(*Tsh*... Like I'm going to bed at this time, I need to study more.){/size}", "normal", "squint", "angry", "mid")

    call her_walk("door", "base")

    call her_main("{size=-4}(Filthy whores...){/size}", "angry", "closed", "angry", "mid", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels so good!){/size}", "base", "happyCl", "worried", "mid", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 3
    jump end_hermione_event

label hg_tutor_E3:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So, have you thought about emotions and their usefulness in the practice of magic?"
    call her_main("Yes, first I tried to cast a spell while thinking of the behaviour of those Slytherin girls.", "open", "closed", "base", "mid")
    call her_main("It made me so angry and confused that I lost my focus and failed miserably.", "annoyed", "base", "base", "mid")
    call her_main("I don't think it helps at all.", "annoyed", "squint", "base", "mid")
    m "That's your problem Miss Granger, you think you already know the answer and don't follow my instructions."
    m "I don't care about the behaviour of those girls."
    call her_main(".........", "annoyed", "narrow", "annoyed", "up")
    call her_main("Sorry about that, {w=0.5}again.", "open", "squint", "base", "mid")
    m "I need you to focus on what those girls do with professors, not their behaviour in general."
    call her_main("But...", "open", "base", "base", "mid", cheeks="blush")
    m "Last time you were talking about your sacred duty and at the first hurdle you hesitate."
    call her_main("{size=-2}(\"Sacred\"? Don't exaggerate, old man){/size}", "annoyed", "narrow", "worried", "down")
    call her_main("{size=-2}(Or not! Maybe I'll be remembered later for being the saviour of the Gryffindor house!){/size}", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("Yes, you're right! It {b}is{/b} my sacred duty!", "smile", "base", "base", "R")
    g9 "{size=-2}(It works every time, it's too easy... She looks so proud of herself.){/size}"
    call her_main("I'll do my best, professor!", "open", "base", "base", "mid", cheeks="blush")
    g9 "I'm excited too... uh, I'm sure you will."
    call her_main("I'm glad you have such high confidence in me.", "grin", "happyCl", "worried", "mid")
    m "And I'm glad you're starting to believe in this. I think you have the potential to master this branch of magic."
    call her_main("You seem tired, professor.", "open", "squint", "base", "mid")
    g11 "{size=-2}(Tired of waiting to annihilate your ass.){/size}"
    call her_main("Yes, professor?", "annoyed", "base", "base", "mid")
    g9 "Yes we can!"
    m "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?"
    call her_main("Sleep? I must study first.", "open", "closed", "base", "mid")
    m "I wasn't thinking about that, but you're right, time to go to bed!"
    m "Just make sure to think about what you learned today."

    call her_walk("door", "base")

    call her_main("{size=-4}(*Hmm*... I wonder what he {b}was{/b} thinking about.){/size}", "base", "narrow", "base", "down", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Probably all the problems caused by those harlots.){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush")
    call her_main("{size=-4}(Well, I will never be like them, so no need to worry.){/size}", "silly", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 4
    jump end_hermione_event

label hg_tutor_E4:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call her_main("Sir, I want to apologise for doubting you.", "open", "base", "base", "mid")
    m "Yes?"
    call her_main("Your \"atypical\" method works!", "angry", "happyCl", "worried", "mid", emote="sweat")
    m "{size=-2}(Impossible!){/size}"
    m "It works? I mean, yes, naturally it works!"
    m "I'm glad you've succeeded. Now tell me more."
    call her_main("I managed to levitate a heavy rock while thinking about the behaviour of two girls I saw earlier in the library.", "open", "closed", "base", "mid")
    call her_main("Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that.", "mad", "base", "angry", "mid", cheeks="blush")
    her "It felt weird but... {w=0.5}good at the same time."
    m "{size=-2}(She is so ignorant of life! Unbelievable.){/size}"
    m "You've never felt such a sensation before?"
    call her_main("Generally I get angry and rush to stop such behaviour.", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("But yesterday, I don't know, I just watched without interrupting them.", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("And when I pictured it, as you told me to, it worked.", "open", "base", "base", "mid", cheeks="blush")
    call her_main("I feel at the same level as those harlots, I'm so ashamed.", "angry", "base", "angry", "mid", cheeks="blush")
    m "But you succeeded."
    g9 "{size=-2}(To my surprise...){/size}"
    call her_main("Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="sweat")
    g9 "{size=-2}(In your dreams.){/size}"
    m "Good, good. Now I want to know more about those two girls."
    call her_main("It's not very relevant, professor. And I'm not sure this is appropriate.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "How will you improve yourself if I can't guide you?"
    m "And for that, I must know more."
    call her_main("Alright, but it's embarrassing.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    g9 "{size=-2}(Ooh, I hope they were naked!){/size}"
    call her_main("I went to the library to study interactions between plants...", "open", "closed", "base", "mid")
    g11 "{size=-2}(Yeah, yeah, come on...){/size}"
    call her_main("... and I heard muffled sounds.", "base", "base", "base", "R", cheeks="blush")
    call her_main("I was hoping to catch a teacher doing bad things with one of those Slytherin whores.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("I slowly headed towards the sounds and I discovered two girls in an alcove.", "open", "base", "base", "mid", cheeks="blush")
    call her_main("I remained hidden to observe them.", "grin", "wink", "base", "mid", cheeks="blush")
    g11 "{size=-2}(Come on!){/size}"
    call her_main("Yes, professor?", "base", "narrow", "base", "up", cheeks="blush")
    m "Yes, no, please continue."
    call her_main("They were kissing passionately.", "open", "happyCl", "worried", "mid", cheeks="blush")
    g9 "And? And?"
    call her_main("And a moment later they began to...", "open", "closed", "base", "mid")
    call her_main("They began to...", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("They began to touch their breasts!", "scream", "wide", "base", "stare", cheeks="blush")
    m "They were naked, I hope?"
    call her_main("What?", "open", "happy", "base", "mid", cheeks="blush")
    her "No, fortunately they were dressed."
    call her_main("How can such a thing happen in our beloved school!", "angry", "base", "angry", "mid", cheeks="blush")
    m "But you kept watching, didn't you?"
    call her_main("Only for educational purposes.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    g9 "{size=-2}(\"Educational purposes\"... ha-ha, I've never heard a worse excuse!){/size}"
    m "And during all this time you didn't feel a certain need?"
    call her_main("To my shame, yes. Like I said before, I felt kind of warm inside.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Like when I have to pee but... different. Better.", "disgust", "narrow", "base", "down", cheeks="blush")
    m "This good sensation... next time you experience it, let it come."
    call her_main("But...", "open", "base", "base", "mid", cheeks="blush")
    m "It's the only way to get better, Miss Granger."
    m "If you suppress it, it won't work."
    call her_main("Ok...{w=0.3} I'll try my best.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    her "But to be honest, sir, I thought you were going to punish those two sluts."
    m "Can you provide proof of their crime? No?"
    m "Even I can't punish students without proof of any wrongdoing."
    g11 "{size=-2}(With the possible exception of you!){/size}"
    m "Anyway, you've done well. I think it will be enough for this lesson."
    m "Remember what I've told you, and good night!"
    call her_main("Good night, professor.", "base", "base", "base", "mid")

    call her_walk("door", "base")

    call her_main("{size=-4}(Well, I'll try to investigate those two girls again.){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Like a real anthropologist!){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush")
    call her_main("{size=-4}(Yes, that's right. Hermione the anthropologist!){/size}", "base", "happyCl", "worried", "mid", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 5

    if her_whoring < 9:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E5:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So, any luck with your \"studies?\""
    call her_main("Yes! When you hear the results of my hunt, you'll be proud of me!", "base", "happyCl", "base", "mid")
    m "{size=-2}(\"Hunt?\"){/size}"
    m "Your \"hunt,\" Miss Granger?"
    call her_main("Yes, professor!", "smile", "happyCl", "base", "mid")
    call her_main("Like an explorer in the wild jungle, I tracked those two filthy animals.", "base", "narrow", "worried", "mid_soft", cheeks="blush")
    call her_main("With success, sir!", "smile", "happyCl", "base", "mid", cheeks="blush", emote="happy")
    call her_main("Hogwarts has so many dark and discreet corners...", "annoyed", "base", "base", "mid")
    call her_main("Believe me, it wasn't easy, professor.", "base", "narrow", "worried", "mid_soft")
    m "I'm sure you gave it your best."
    m "But right now I await your report."
    call her_main("Yes, but before that I want to clarify that my report is purely for scientific purposes.", "soft", "base", "base", "R")
    m "{size=-2}(Sure...){/size}"
    call her_main("So I tracked down those two harlots to an area in the attic.", "open", "closed", "base", "mid")
    call her_main("Which, by the way, seems to be the meeting place for girls of this... sort.", "annoyed", "squint", "base", "mid")
    m "And what is your opinion on them?"
    call her_main("At least they don't sleep with professors in exchange for house points.", "open", "squint", "base", "mid")
    call her_main("", "annoyed", "squint", "base", "mid")
    m "And that's it?"
    m "No \"this behaviour must be severely punished?\""
    m "Are you attracted to girls of this sort, Miss Granger?"
    call her_main("What? I'm not a-- I mean no, Sir.", "open", "base", "worried", "mid", cheeks="blush")
    m "Alright, alright, back to your report, if you please."
    call her_main("{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("{size=-2}(Hermione, pull yourself together! You're not a harlot!){/size}", "mad", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("No, I'm not!", "annoyed", "narrow", "worried", "down", cheeks="blush")
    m "Excuse me?"
    call her_main("Uh... Yes, my report. My {b}scientific{/b} report.", "open", "base", "base", "mid", cheeks="blush")
    m "{size=-2}(Yeah, we get it...){/size}"
    call her_main("So, like before, they started by kissing passionately.", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("With the tongue and everything!", "open", "base", "base", "R", cheeks="blush")

    menu:
        "-Start jerking off-":
            $ masturbating = True
            hide screen hermione_main
            hide screen blktone
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerk_off_behind_desk")
            with d3
            call ctc

        "-Just listen-":
            $ masturbating = False
            pass

    call her_main("", "open", "base", "base", "mid", cheeks="blush")
    g9 "And? And?"
    call her_main("They pulled up their shirts and caressed each other's breasts.", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("{size=-2}(Their beautiful and tempting breasts...){/size}", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing.", "silly", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-2}(I can't believe I said that!){/size}", "base", "narrow", "base", "up", cheeks="blush", tears="sweat")
    call her_main("They were very excited, and I could see their panties become wet.", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("Disgusting.", "annoyed", "narrow", "base", "up", cheeks="blush")
    if masturbating:
        g9 "{size=-2}(Yes... yes...){/size}"
    call her_main("One of the girls went crazy and inserted her fingers into the other's \"thing,\" and worked them furiously.", "silly", "base", "worried", "mid", cheeks="blush")
    call her_main("Soon imitated by her girlfriend.", "base", "narrow", "angry", "mid", cheeks="blush")
    call her_main("Those whores came so hard I'm sure they heard the screams on the other side of the grounds!", "soft", "narrow", "base", "mid", cheeks="blush")

    if masturbating:
        call her_main("{size=-2}(And I had to bite my lip, or else they would've heard me too...){/size}", "clench", "narrow", "base", "down", cheeks="blush")
        hide screen hermione_main
        with d3

        call cum_block

        g11 "Yes! That's the stuff!"
        hide screen bld1
        with d1
        call gen_chibi("cum_behind_desk")
        call cum_block
        call ctc

        call gen_chibi("cum_behind_desk_done")
        with d3

        if hg_jerkoff.trigger:
            call her_main("Professor!", "angry", "base", "angry", "mid", cheeks="blush")
            m "You enjoyed it too, so don't act all innocent."
            m "Anyway, I hope it was revealing."

            $ her_mood += 7
        else:
            call her_main("Professor?", "annoyed", "base", "base", "mid", cheeks="blush")
            m "Ah, Yes... I hope it was revealing."

    else:
        m "You enjoyed it too."
        call her_main("Maybe...", "annoyed", "narrow", "angry", "R", cheeks="blush")
        m "Anyway, I hope it was revealing."

    call her_main("\"Revealing?\" I'm not sure what you mean by that.", "open", "squint", "base", "mid")
    call her_main("You're the headmaster, act as such!", "open", "base", "base", "mid")
    call her_main("Do all you can to stop those acts of debauchery!")
    call her_main("", "annoyed", "narrow", "angry", "R")
    m "Yes, of course."
    m "{size=-2}(Hypocrite...){/size}"
    m "You said that those girls became wet."
    g9 "Weren't you a little too?"
    call her_main("When I went to bed I noticed it, yes.", "disgust", "narrow", "base", "down", cheeks="blush")
    call her_main("Apparently bad fluids are released from your body when you have faced such acts.", "mad", "wide", "base", "stare", cheeks="blush")
    m "No, they aren't bad. It happens when you're excited."
    call her_main("No way! I can control myself!", "scream", "happyCl", "worried", "mid", cheeks="blush", tears="soft_blink")
    call her_main("", "angry", "base", "angry", "mid", cheeks="blush")
    m "No one can control their base desires."
    m "Consider this well, and enjoy your night, Miss Granger."
    call her_main("Good night, professor.", "annoyed", "base", "worried", "R")

    call her_walk("door", "base")

    call her_main("{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(I lost control, it won't happen again!){/size}", "shock", "narrow", "base", "down", cheeks="blush")
    call her_main("{size=-4}(Good thing I'm not a degenerate like those filthy girls!){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 6

    if her_whoring < 9:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E6:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Bravo, last time you experienced your first \"emotion.\""
    call her_main("Yes, I remember. But I still don't see the link with magic.", "open", "squint", "base", "mid")
    m "{size=-2}(Me neither...){/size}"
    m "If you want to progress, you have to go a little further than a simple observation."
    m "You'll need to participate."
    call her_main("What! No way I'll participate in such debauchery!", "scream", "closed", "base", "mid", cheeks="blush")
    call her_main("How can you even suggest such a thing!", "angry", "base", "angry", "mid")
    m "Oh you don't have to go that far in one go."
    call her_main("I'm not sure I want to go there at all.", "open", "closed", "base", "mid")
    m "How many times do I have to remind you why you're doing this?"
    call her_main("Yes but...", "open", "base", "base", "mid")
    m "But what?"
    call her_main("A girl like me shouldn't stoop to such practices.", "annoyed", "squint", "base", "mid")
    m "A girl like you should use all means at their disposal in order to excel."
    her "..........."
    call her_main("Alright, but this must remain between us.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("You cannot disclose this to other professors, especially professor Snape!", "annoyed", "narrow", "worried", "down")
    m "Oh, I have no intention of sharing alright."
    g9 "{size=-2}(You're mine.){/size}"
    m "Speaking of you with professor Snape."
    call her_main("Well, what must I do now?", "open", "closed", "base", "mid")
    m "Come here."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade
    call ctc

    call bld
    m "Have you ever touched yourself?"
    call her_main("Professor!", "annoyed", "narrow", "angry", "mid", cheeks="blush", xpos="mid", ypos="base")
    call her_chibi_scene("grope_ass_front")
    with d7

    call nar(">You touch her leg with your hands.")
    m "Please answer the question, Miss Granger. Have you ever touched yourself?"
    call her_main("No, it's... it's wrong!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "But when you looked at these girls, you felt certain emotions."
    call her_main("Yes... and?", "annoyed", "base", "base", "mid", cheeks="blush")
    m "You didn't feel the need to touch yourself?"
    call her_main("Yes... but I resisted.", "soft", "narrow", "base", "up", cheeks="blush")
    call nar(">You start to caress her thigh.")
    call her_main("Professor...", "open", "happyCl", "worried", "mid", cheeks="blush")
    m "And you felt those emotions without even touching yourself."
    call her_main("Yes...", "open", "base", "base", "mid", cheeks="blush")
    g9 "{size=-2}(What a slut!){/size}"
    if hermione.is_worn("panties"):
        call nar(">You move forward to her panties.")
    else:
        call nar(">You move forward to her pussy.")
    call her_main("", "open", "happyCl", "worried", "mid", cheeks="blush")
    m "Good."

    call her_chibi_scene("behind_desk_front")
    with d3

    call nar(">You stop caressing her.")
    call her_main("Why... why did you stop?", "mad", "wide", "base", "stare", cheeks="blush")
    m "Oh, because I need you to think about all this before we meet again."
    call her_main("But...", "mad", "wide", "base", "stare", cheeks="blush")
    m "Good night, my dear."
    call her_main("Good night, professor.", "annoyed", "base", "worried", "R")

    hide screen hermione_main
    call blkfade

    "You dismiss Hermione."

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    call hide_blkfade

    call her_walk("door", "base")

    call her_main("{size=-4}(This is wrong...){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(I shouldn't listen to him.){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("{size=-4}(And yet...){/size}", "base", "narrow", "base", "down", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 7

    if her_whoring < 12:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E7:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So, have you started practising my teachings?"
    call her_main("I don't even know where to start.", "open", "squint", "base", "mid")
    m "You see, the secret is to stimulate appropriate areas."
    m "Areas which are more sensitive than others."
    call her_main("You mean my intimate areas, sir?!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Well, they're called intimate for a reason."
    m "You said you've never touched yourself because it was wrong."
    m "But it's never wrong to exercise ones body in order to reach a new level of consciousness."
    g4 "{size=-2}(The things I have to make up...){/size}"
    m "You can begin with your breasts, for example."
    m "But you shouldn't only caress your nipples but also grab your tits and squeeze them."
    m "And in the meanwhile, you can think of those two girls."
    g9 "Or what you want to do with those girls."
    call her_main("What makes you think... No, I don't want...", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="sweat")
    call her_main("I definitely don't want to have {b}anything{/b} to do with those harlots!", "scream", "happyCl", "worried", "mid", cheeks="blush")
    m "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls."
    call her_main("I...{w=0.3} I honestly don't know what to think anymore.", "mad", "base", "angry", "mid", cheeks="blush")
    her "At the moment my feelings are so confusing..."
    g9 "{size=-2}(Exactly what I was hoping!){/size}"
    call her_main("I'm happy to earn points for my house and at the same time I feel so ashamed.", "angry", "squint", "base", "mid", cheeks="blush", tears="soft")
    her "And the same goes for your lessons."
    m "Yet you can't deny your progress in the practice of magic."
    call her_main("Yes...{w=0.2} perhaps you're right.", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    m "You have to let it go, Miss Granger, follow your instincts!"
    g9 "{size=-2}(Grab my cock and wank it savagely!){/size}"
    call her_main("I'm not sure if...", "open", "narrow", "worried", "mid_soft", cheeks="blush")
    m "Enough procrastination, time for practice!"
    m "Come here."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    ">Hermione walks towards your desk."
    ">You grab her tits and massage them softly."
    pause .5

    call her_chibi_scene("grope_tits")
    with d1
    hide screen blkfade
    call her_main("", "open", "happyCl", "worried", "mid", cheeks="blush", xpos="mid", ypos="base")
    call ctc

    call bld
    m "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas."
    m "It's not enough if I do it myself, you need to practise when you're alone."
    call her_main("", "upset", "happyCl", "worried", "mid", cheeks="blush")
    m "Like in your bed or in the shower, for example."
    call nar(">You keep massaging her tits...")
    call her_main("", "open", "happyCl", "worried", "mid", cheeks="blush")
    call nar(">You feel her nipples becoming hard.")
    call her_main("Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!", "open", "base", "base", "mid", cheeks="blush")
    m "Don't let old prejudices weigh you down. You're a girl with great potential."
    call nar(">You gently squeeze her nipples through the fabric.")
    call her_main("Ah, thank you professor.", "open", "narrow", "base", "up", cheeks="blush")
    m "A girl with a brilliant mind."
    call nar(">You increase your grip on her nipples.")
    m "A girl who will become a woman of exception."
    call her_main("*Ahh* yes... I'm already a woman of exception!", "grin", "base", "angry", "mid", cheeks="blush")
    m "(...)"
    call nar(">You firmly pinch her nipples.")
    call her_main("*Ahhh* {heart} not so hard...", "silly", "happyCl", "worried", "mid", cheeks="blush", tears="soft")

    hide screen hermione_main
    call blkfade
    call nar(">You abruptly stop.")
    pause .5
    call her_main("*Hmph*...{w=0.3} Why did you stop, [genie_name]?", "clench", "base", "worried", "mid", cheeks="blush", emote="angry", ypos="head", flip=False, trans=d3)
    m "Lesson is over. Time to practise by yourself."

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    hide screen blkfade

    call her_main("...........", "annoyed", "narrow", "worried", "R", cheeks="blush", xpos="mid", ypos="base", trans=fade)
    m "Good night, my little witch."
    call her_main("Good night, professor, and thank you for this lesson.", "base", "happyCl", "base", "mid")
    call her_main("{size=-2}(I just wish it had lasted longer...){/size}", "annoyed", "squint", "base", "mid", cheeks="blush")

    call her_walk("door", "base")

    call her_main("{size=-4}(\"My little witch?\"){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Why not, after all...){/size}", "base", "narrow", "base", "up", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 8

    if her_whoring < 12:
        $ her_whoring += 1

    jump end_hermione_event


label hg_tutor_E8:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So, Miss Granger, have you practised my teachings?"
    call her_main("Yes...{w=0.2} a little.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "And?"
    call her_main("It feels even better when I'm naked.", "smile", "happyCl", "base", "mid", cheeks="blush", emote="happy")
    call her_main("{size=-2}(Oh no, I shouldn't have said that...){/size}", "mad", "wide", "base", "stare", cheeks="blush")
    m "Well come here and undress, we'll practise."
    call her_main("Completely?!", "annoyed", "base", "worried", "mid", cheeks="blush")
    m "No, only the top will suffice."
    g9 "{size=-2}(For the moment...){/size}"
    call her_main("I'll be showing you my breasts without even earning any points?", "open", "squint", "base", "mid")
    m "You can't have both points and lessons."
    call her_main("Okay...", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="sweat")

    $ hermione.strip("robe", "accessory")
    call her_chibi("lift_top")

    call set_her_action("lift_top")

    $ hermione.strip("top")
    pause .5

    call her_main("Like that?", "annoyed", "narrow", "angry", "R", cheeks="blush")

    if hermione.is_worn("bra"):
        m "Without your bra Miss Granger..."
        pause .5
        $ hermione.strip("bra")
        call her_main()
        pause .5

    m "Yes, and now come here."
    call her_main("........", "annoyed", "closed", "base", "mid", cheeks="blush")
    call her_main("", "base", "closed", "base", "mid")
    m "Now."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    ">Hermione slowly walks towards your desk."
    ">She tries not to bounce her tits without much success..."
    call her_chibi_scene("behind_desk_show_tits")
    with d1

    hide screen blkfade
    call her_main("", "base", "closed", "base", "mid", xpos="mid", ypos="base")
    call ctc

    call bld
    m "Now let's get serious if you want to."
    g9 "{size=-2}(Well, even if you don't...){/size}"

    hide screen hermione_main
    call blkfade

    ">You grab her tits and squeeze them gently."

    call her_chibi_scene("grope_tits")
    call hide_blkfade
    call ctc

    call her_main("Professor, what are you doing?", "disgust", "narrow", "base", "down", cheeks="blush")
    g9 "Teaching you, dear, teaching you."
    m "Doesn't it feel good?"
    call her_main("A little...", "base", "closed", "base", "mid")
    m "Your hard nipples say the contrary."
    m "I can stop if you want."
    call her_main("Yeah sure!", "grin", "base", "angry", "mid", cheeks="blush")
    call her_main("Suck them professor.", "silly", "narrow", "base", "up", cheeks="blush")
    g9 "As you wish, princess."
    call her_main("", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">You suck her nipples with devotion.")
    call her_main("Yes {heart} like that.", "silly", "narrow", "base", "up", cheeks="blush", tears="sweat")
    call nar(">You start to chew on her nipples.")
    call her_main("*Ahh*, no... Don't.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    call nar(">You chew on them even harder.")
    call her_main("Not that hard, I will...", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "{size=-2}(Time for the grand finale!){/size}"

    if hermione.is_worn("panties"):
        ">You quickly slip your hand into her panties and rub her pussy furiously."
    else:
        ">You quickly move your hand toward her pussy and rub it furiously."

    call her_main("Yes! {heart}", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    her "I... I..."
    g9 "Came, my dear."

    hide screen hermione_main
    call blkfade
    call ctc

    call set_her_action("none","update")

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade

    call her_main("Is the lesson over professor?", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    m "Not if you don't want it to be."
    call her_main("Maybe it's enough for tonight.", "open", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("After all, you have a lot of work to do.", "soft", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    m "Sure."
    m "But before that I have a little present for you."

    call give_gift(">You give an assortment of adult magazines to Hermione.",adult_mag_ITEM)

    m "I hope this will help you in your studies."
    call her_main("Yes, certainly.", "base", "closed", "base", "mid", cheeks="blush", tears="mascara")
    call her_main("Thank you and good night professor.", "base", "narrow", "base", "mid", cheeks="blush", tears="mascara")

    hide screen hermione_main
    call blkfade

    "You dismiss Hermione."
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    call her_walk("door", "base")

    call her_main("{size=-4}(I'm such a slut...){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Cumming in front of my professor...){/size}", "base", "narrow", "base", "down", cheeks="blush")
    call her_main("{size=-4}(I definitely need to do that again!){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 9

    if her_whoring < 18:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E9:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So tell me, were your readings enlightening?"
    call her_main("I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too.", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Maybe it's time to discover new areas to stimulate."
    call her_main("You mean my pussy, right?", "open", "squint", "base", "mid")
    call her_main("I'm not an idiot, professor.", "annoyed", "narrow", "angry", "R")
    m "If it doesn't suit you, we can stop here."
    call her_main("And if I said stop?", "annoyed", "squint", "base", "mid")
    g4 ".........."
    call her_main("*Ha-ha*, you should have seen your face!", "smile", "base", "angry", "mid", cheeks="blush")
    call her_main("With all your recent lessons you can imagine that this area isn't a \"no man's land\" anymore.", "smile", "base", "base", "R")
    g4 "Have you slept..."
    call her_main("No I haven't! I'm not a harlot who offers her pussy to every boy around.", "scream", "closed", "base", "mid", cheeks="blush")
    m "{size=-2}(Good, your pussy is mine alone!){/size}"
    call her_main("", "annoyed", "narrow", "annoyed", "up")
    g9 "{size=-2}(Although I may agree to share it with other girls...){/size}"
    m "I'm happy you're behaving honourably, Miss Granger."
    call her_main("Ha, who'd have guessed!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Yes, I'm glad that my favourite student is not wasting her precious time with boys."
    her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
    m "Enough of this! Now take off your shirt and come here."
    call her_main("Here we go for another \"lesson\".", "open", "squint", "base", "mid")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")

    if hermione.is_worn("bra"):
        call her_main("...", ypos="head", flip=False, trans=d3)
        m "And your bra..."

        $ hermione.strip("bra")

    call her_main("........", "annoyed", "closed", "base", "mid", cheeks="blush", ypos="head", flip=False, trans=d3)

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade
    call ctc

    call her_main("And free tits again, enjoy!", "grin", "base", "angry", "mid", cheeks="blush", xpos="mid", ypos="base")
    m "I definitely intend to."
    g9 "Now take off your skirt."
    pause .8

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    call set_her_action("None")
    pause .5

    call her_main("", "base", "base", "base", "R", cheeks="blush")
    call ctc

    if hermione.is_worn("panties"):
        call her_main("You love my pussy don't you?", "base", "narrow", "base", "up", cheeks="blush")
        g9 "Oh yes, I love your smell, especially when you're wet."
        call her_main("Professor...", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="sweat")
        call her_chibi_scene("grope_ass_front")
        with d3
        call nar(">You caress her clit.")
        call her_main("Professor!", "mad", "wide", "base", "stare", cheeks="blush")
    else:
        call her_main("You love my panties don't you?", "base", "narrow", "base", "up", cheeks="blush")
        g9 "Oh yes, I love their smell, especially when you're wet."
        call her_main("Professor...", "angry", "happyCl", "worried", "mid", cheeks="blush", emote="sweat")
        call her_chibi_scene("grope_ass_front")
        with d3
        call nar(">You caress her clit through the fabric.")
        call her_main("Professor!", "mad", "wide", "base", "stare", cheeks="blush")
        m "Now take them off."

        $ hermione.strip("panties")
        call set_her_action("pinch")

        call nar(">She slowly lowers her panties.")

        call set_her_action("None")

        call her_chibi_scene("behind_desk_front")
        call her_main("", "base", "closed", "base", "mid")
        call ctc

    m "What's great, you see, is that I have two hands."
    m "One can caress your clit while the other can play with your pussy."
    call nar(">You move from words to deeds and penetrate her already wet pussy with ease.")

    call her_chibi_scene("grope_ass_front")
    with d3

    call her_main("Yes, you're probably right.", "grin", "base", "angry", "mid", cheeks="blush")
    m "Probably?!"
    call nar(">While you're moving your finger in her pussy, you take over her clit with your thumb.")
    call her_main("*Haa* {heart} I'm only your humble student, I wouldn't know such naughty things.", "silly", "narrow", "base", "up", cheeks="blush")
    m "One finger is rarely enough even with a tight pussy like yours."
    call nar(">You insert a second finger in her tight and warm pussy...")
    call her_main("Yesss {heart} I'll try to remember your teachings.", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">You increase the pace and feel her pussy tighten on your fingers.")
    m "Maybe a third finger?"
    call her_main("Don't be so bold.", "grin", "base", "angry", "mid", cheeks="blush", tears="soft")
    call nar(">Her whole body starts shaking as you increase your ramming.")

    call her_chibi_scene("grope_ass_front_fast")
    with d3

    call her_main("Noo {heart}{w=0.2} not so fast I will...", "open_tongue", "narrow", "base", "up", cheeks="blush")
    call nar(">You increase your pace even more.")
    call her_main("I will I will...", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "Time to get serious."
    call nar(">You force your soaked thumb into her butthole.")
    call her_main("*Haaaaa* {heart} yesss! {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "Lucky girl."

    call blkfade

    hide screen hermione_main
    call her_chibi_scene("behind_desk_front")
    call hide_blkfade

    call her_main("I'm sure this lesson will be of great help tonight.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("And the other nights. {heart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "Always glad to help my little witch in her studies."
    call her_main("\"Studies,\" yes, that's right.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    m "And to aid your studies I have even more scientific materials."

    call give_gift(">You give an assortment of porn magazines to Hermione.",porn_mag_ITEM)

    call her_main("I promise to study them every night until I commit their lessons to memory!", "grin", "closed", "base", "mid", cheeks="blush", tears="mascara")
    call her_main("Thank you and good night, professor.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    m "Good night, my favourite little witch."

    hide screen hermione_main
    call blkfade

    "You dismiss Hermione."
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    call her_walk("door", "base")

    call her_main("{size=-4}(Favourite...){/size}", "base", "narrow", "base", "up", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(*Hmm*... Could there be another one?){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("{size=-4}(I better do my best to remain his favourite!){/size}", "base", "happyCl", "worried", "mid", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 10

    if her_whoring < 18:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E10:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "Miss Granger, have you had an enjoyable night?"
    call her_main("You shouldn't ask such things, Professor.", "open", "closed", "base", "mid")
    m "I have to make sure my students have a pleasant nights rest."
    call her_main("With your teachings and your \"scientific\" literature, indeed.", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    call her_main("I'll become proficient in human anatomy with all this documentation.", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "Do you need some scientific instruments for your research?"
    call her_main("They could come in handy.", "grin", "wink", "base", "mid", cheeks="blush")
    call her_main("As long as it's not your dick.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("{size=-2}(Not that I don't appreciate it but no points no cock!){/size}", "smile", "base", "angry", "mid", cheeks="blush")
    m "Miss Granger! This is a serious matter!"
    call her_main("Sure...", "annoyed", "squint", "base", "mid")
    m ".........."
    call her_main("So what's my gift this time?", "open", "squint", "base", "mid")

    call give_gift(">You give the vibrator to Hermione",vibrator_ITEM)

    call her_main("And I suppose you want me to test this in front of you?", "open", "closed", "base", "mid")
    g9 "Of course."
    call her_main("Where is the educational purpose in all of this?", "annoyed", "squint", "base", "mid")
    m "Good question. Improving your skills?"
    call her_main("At what? Magic?", "mad", "base", "angry", "mid", cheeks="blush")
    m "Certainly."
    her "........."
    call her_main("I have one request though.", "open", "base", "base", "R", cheeks="blush")
    call her_main("If I'm going to masturbate I don't want to be the only one. So enjoy the free show.", "open", "happyCl", "worried", "mid", cheeks="blush")
    g9 "With pleasure!"
    call nar(">You reach under the desk and grab your cock.")

    hide screen hermione_main
    call blkfade

    call gen_chibi("jerk_off_behind_desk")
    with d3

    call hide_blkfade

    call her_main("{size=-2}(Thinking of the headmaster masturbating makes me wet already {heart}){/size}", xpos="mid", ypos="base")
    call her_main("{size=-2}(I've become such a whore. Not that I don't enjoy it...){/size}", "smile", "base", "angry", "mid", cheeks="blush")
    call her_main("So... where do we start?", "open", "happy", "base", "mid", cheeks="blush")

    if hermione.is_worn("bra"):
        m "Take off your shirt and bra, I want to see your tits."
        pause .5

        call set_her_action("lift_top")
        pause .5

        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top")
        $ hermione.strip("bra")
        call set_her_action("None")
        pause .5

    else:
        m "Take off your shirt, I want to see your tits."
        pause .5

        call set_her_action("lift_top")
        pause .5

        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top")
        call set_her_action("None")
        pause .5

    her "You love them don't you?"
    g9 "Oh yes..."
    her "Having watched the other girls I now know why."
    her "Those breasts are so tempting."
    call her_main("Big or small, I want to hold them in my hands and suck the nipples.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "Me too, me too!"
    m "Now remove your skirt!"
    pause .5

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    call set_her_action("None")
    pause .5

    call ctc

    her "Good idea."
    call her_main("Sometimes I wish I could do this with others girls.", "open", "happy", "base", "mid", cheeks="blush")
    call her_main("Masturbate naked in front of each other.", "open", "narrow", "base", "up", cheeks="blush")
    if hermione.is_worn("panties"):
        g9 "Yes go on, take off your panties!"
        her "Your wish is my command."
        pause .5

        call set_her_action("pinch")
        pause .5

        $ hermione.strip("panties")
        call set_her_action("None")
        pause .5

        $ u_tears_pic = "characters/hermione/face/e_her_tears_02b.webp"
        call ctc

        call her_main("And mine is to touch another girl's pussy.", "silly", "narrow", "base", "up", cheeks="blush")
    else:
        call her_main("Touch her pussy like I'm touching mine now.", "silly", "narrow", "base", "up", cheeks="blush")

    if hermione.is_any_worn("clothes"):
        m "Get rid off the rest of your silly attire."
        $ hermione.strip("all")

    ### Milestone ###
    $ hg_masturbated.triggered()

    $ hermione.set_pose("masturbate")
    $ hermione.set_body(armleft="on_pussy")
    #call set_her_action("pinch")
    pause .5

    call her_main("Caress it.", "open_tongue", "narrow", "base", "up", cheeks="blush")

    call set_her_action("fingering")
    pause .2

    call her_main("Insert my fingers into her wet pussy.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    g11 "Yes, yes! Now the vibrator!"

    hide screen hermione_main
    call blkfade

    ## TODO: show vibrator pose
    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armleft="on_pussy", armright="on_tits")

    hide screen blkfade
    call her_main()
    call ctc

    call her_main("Oh I had forgotten about it already.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    call her_main("I want to hear her moan as I work my fingers.", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    her "Hear her cum!"
    call her_main("Like me! *Aaah* yesssss! {heart} {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call ctc

    g11 "Ahh! You little whore!!!"
    call gen_chibi("cum_behind_desk")
    her "The vibrator... *aaah* I'm still cumming!!"
    g11 "Take this!"

    hide screen hermione_main
    call blkfade

    ">Hermione catches her breath and puts her clothes back on."

    # Reset pose
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("cum_behind_desk_done")
    hide screen blkfade

    call her_main("I hope you enjoyed it as much I did.", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara", xpos="mid", ypos="base", trans=fade)
    m "Oh fuck yes, you're doing great, my little witch!"
    g9 "Very good!"
    call her_main("Thank you, professor.", "grin", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    m "After all this, you need to rest."
    call her_main("Oh yes. Good night professor.", "grin", "closed", "base", "mid", cheeks="blush", tears="mascara")
    m "Good night, my dirty little slut."

    call her_walk("door", "base")

    call her_main("{size=-4}(Rest...){/size}", "base", "narrow", "base", "down", cheeks="blush", tears="mascara", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Not before I've played with this marvelous toy again){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("{size=-4}(And again){/size}", "silly", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")

    call her_chibi("leave")

    $ her_tutoring = 11

    if her_whoring < 21:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E11:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "So... I hope my lessons are paying off."
    call her_main("You mean, by making me more \"open\" to the wonders of adulthood?", "open", "squint", "base", "mid")
    m "Among other things..."
    call her_main("That's what I thought.", "annoyed", "squint", "base", "mid")
    call her_main("But to be honest, I was looking forward to this lesson.", "open", "closed", "base", "mid")
    call her_main("{size=-2}(Maybe, I shouldn't have said that){/size}", "angry", "wide", "base", "stare")
    call her_main("{size=-2}(He's gonna ravage me on his desk, isn't he?){/size}", "angry", "happyCl", "worried", "stare", cheeks="blush")
    #call her_main("{size=-2}(Not that I would mind...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
    #call her_main("{size=-2}(And I could ask him for points afterwards...){/size}", "smile", "base", "base", "R")
    m "Miss Granger? Are you alright?"
    call her_main("Yes professor! Sorry, I was thinking of my next exam.", "grin", "wink", "base", "mid", cheeks="blush")
    m "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise."
    call her_main("I would love that!", "open", "happyCl", "worried", "mid", cheeks="blush")
    m "So, anal stimulation..."
    call her_main("Ah! I knew you would say that.", "smile", "base", "angry", "mid", cheeks="blush")
    her "{size=-2}(Once again, not that I mind...){/size}"
    call her_main("{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}", "base", "narrow", "base", "up", cheeks="blush")
    m "Come again, Miss Granger?"
    call her_main("In this school nobody can compete with me, right professor?", "smile", "happyCl", "base", "mid", cheeks="blush", emote="happy")
    call her_main("In any field!", "smile", "base", "angry", "mid", cheeks="blush")
    m "In any field? I'm not sure."
    m "You still have things to learn..."
    call her_main("What?! What are we waiting for then?", "scream", "closed", "base", "mid", cheeks="blush")
    call her_main("", "normal", "narrow", "angry", "mid", cheeks="blush")

    call set_her_action("lift_top")
    pause .2

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")
    pause .5
    $ hermione.strip("bra")
    call ctc
    call set_her_action("None")

    call nar(">She rips off her shirt and rushes to your desk.")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("grope_ass_back")
    call hide_blkfade
    call ctc

    call bld
    m "We haven't even started yet and you're already wet, my adorable slut."

    show screen blktone
    call her_main("It's you and your dirty talk!", "annoyed", "narrow", "angry", "R", cheeks="blush", xpos="mid", ypos="base")
    her "Talking about anal insertions, asshole licking and... and..."
    call her_main("Fisting!", "open", "narrow", "base", "up", cheeks="blush")
    m "I never mentioned any of that."
    call her_main("Oh. You didn't?", "annoyed", "narrow", "base", "up", cheeks="blush")
    call her_main("Well maybe you didn't but you {b}were{/b} thinking about it!", "base", "narrow", "base", "up", cheeks="blush")
    g9 "Maybe."
    g9 "Your ass is so luscious I could eat it."
    call her_main("My point exactly!", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("Enough talking, old man. Get to work!", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    m "I haven't even given you your gift yet!"
    m "I'll just put it where you'll be sure to find it."
    m "So, can we start the lesson?"
    call her_main("Yes for Merlin's sake!", "open", "base", "base", "mid", cheeks="blush")
    m "But before that..."
    call her_main("If you say another word I swear I will go back to my dorm right now!", "scream", "base", "angry", "mid", cheeks="blush", emote="angry")
    call nar(">You suddenly insert the anal plug.")
    call her_main("Yesss {heart} like that!", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">You remove it just as quickly while giving her butt a loud slap.")

    call play_sound("boing")
    with flashbulb
    call play_sound("slap_1")
    with hpunch

    call her_main("Yessss more! {heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "As you wish, princess."
    call nar(">You promptly insert and remove it.")

    call play_sound("boing")
    pause .1
    call play_sound("slap_1")
    with hpunch

    call her_main("More!!", "open_tongue", "narrow", "base", "up", cheeks="blush")

    call play_sound("boing")
    pause .1
    call play_sound("slap_1")
    with hpunch

    $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.webp"
    call her_main("*Aaaah* {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")

    call play_sound("boing")
    pause .1
    call play_sound("slap_1")
    with hpunch

    m "You can touch yourself too, you know."
    $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.webp"
    call her_main("I can't.", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
    call her_main("{size=-2}(But tonight...){/size}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    m "I'll handle it then."
    call nar(">You finger both her butthole and her pussy.")
    call her_main("Nooo it's too much! {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "Faster? No problem!"
    call her_chibi_scene("grope_ass_back_fast")
    call her_main("*Aaah* You're killing me! {heart}", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    call her_main("{size=-2}(And I love it){/size}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "More fingers?"
    call her_main("No more pleassse.", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    m "Actually, it wasn't a question."
    call her_main("If you keep this pace I will...", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    call nar(">You feel her muscles tighten on your fingers.")
    call her_main("Come!!", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "Good girl."
    her "Keep it up, I..."
    call her_main("Yessss... {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    m "I can keep this up as long as you please."
    call her_main("Nooooo {heart} I will die!", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g9 "In ecstasy."
    call her_main("*Aahh* not again {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    hide screen hermione_main
    hide screen bld1
    hide screen blktone
    with d3

    call her_chibi_scene("behind_desk_back")
    with d3
    pause .5

    call bld
    m "I think you've had enough for one night."
    call her_main("Yes I... I better go.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    m "You forgot your gift."
    call nar(">You promptly insert the butt plug.")
    with hpunch
    call her_main("*Aaaaaaah*", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")

    hide screen hermione_main
    with d3
    call her_chibi_scene("lie_on_desk", trans=d5)
    pause .5

    show screen bld1
    call nar(">She collapses panting on the desk.")
    g9 "Best view in the world."
    pause .8

    call blkfade
    ">After a while, she puts her shirt back on."

    $ hermione.wear("all")

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    hide screen blkfade

    call her_main("Thank you for everything, professor.", "soft", "narrow", "base", "mid", tears="mascara", xpos="mid", ypos="base", trans=fade)
    call her_main("It was very...{w=0.5} enlightening.", "grin", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("But please, try to go easy on me next time.", "grin", "closed", "base", "mid", cheeks="blush", tears="mascara")
    g9 "I have absolutely no idea what you mean by that."
    call her_main("Good night professor.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    m "Good night, my dear anal whore."
    call her_main("Professor...", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")

    call her_walk("door", "base")

    call her_main("{size=-4}(Finally tonight I'll just go to bed.){/size}", "base", "happyCl", "worried", "mid", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(That was a little too intense...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("{size=-4}(Not that I'm complaining...){/size}", "silly", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 12

    if her_whoring < 21:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E12:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], I have something for you."
    call her_main("Another gift for me?", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("Please, please.", "open", "happyCl", "worried", "mid", cheeks="blush")
    m "You weren't this excited last time when I gave you a present..."
    call her_main("Oh don't worry, it was just a moment of weakness.", "smile", "base", "angry", "mid", cheeks="blush")
    her "I'm ready now!"
    call her_main("{size=-2}(My body perhaps not...){/size}", "annoyed", "narrow", "worried", "down")
    m "Did you have fun with your anal plug?"
    call her_main("Y-yes... I wear it sometimes...", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("But I cut the tail!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    her "{size=-2}(No way I could walk around like that...){/size}"
    m "And you like it?"
    call her_main("It's very...{w=0.5} stimulating. It helps me whenever I cast a spell.", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    m "Tell me the truth Miss Granger, you wear it all the time, don't you?"
    call her_main("Nooo...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("Maybe...", "open_tongue", "narrow", "base", "up", cheeks="blush")
    her "........"
    m "Don't be ashamed, it's alright my little whore."
    call her_main("I wear it all the time and...{w=0.3} I love it!", "smile", "happyCl", "base", "mid", cheeks="blush", emote="happy")
    g9 "{size=-2}(Marvellous){/size}"
    m "I've taught you good."
    call her_main("To be a slut? Yes you have...", "open", "closed", "base", "mid")
    call her_main("And now I want more, so where is my gift?!", "annoyed", "squint", "base", "mid")
    m "There, there."

    call give_gift(">You give the anal beads to Hermione",anal_beads_ITEM)

    call her_main("Oh! That's even better than a butt plug.", "shock", "wide", "base", "stare", cheeks="blush")
    g9 "And they can be useful for your pussy too."
    call her_main("So many possibilities...", "smile", "base", "angry", "mid", cheeks="blush")
    her "... so little time."
    call her_main("I suppose you want me to try them out?", "smile", "happyCl", "base", "mid")
    her "Or would you rather try them out on me yourself?"
    g9 "Oh yes."
    call her_main("I don't even know why I'm asking...", "annoyed", "narrow", "annoyed", "up")
    call her_main("{size=-2}(Old pervert...){/size}", "open", "happyCl", "worried", "mid", cheeks="blush")

    call set_her_action("lift_top")
    pause .5

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")
    with d3
    pause .5
    $ hermione.strip("bra")
    with d3
    pause .5

    call her_main("My tits are the best in all of Hogwarts!", "silly", "narrow", "base", "up", cheeks="blush")
    m "Have you been with many girls to say that?"
    call her_main("I wish...", "grin", "narrow", "base", "up", cheeks="blush")
    g9 "I can tutor you on that too."
    call her_main("Maybe we should finish this lesson first.", "base", "narrow", "base", "up", cheeks="blush")
    m "Oh, we have time."
    call her_main("Speaking of that...", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_back")
    with d1
    call hide_blkfade
    call ctc

    call bld
    g9 "As always, it's a delightful view."
    call blktone
    call her_main("I'm glad you love it.", "angry", "happyCl", "worried", "mid", cheeks="blush", xpos="mid", ypos="base")

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    $ hermione.strip("panties")
    call set_her_action("None")
    pause .5

    call her_main("Can we start now?", "grin", "base", "angry", "mid", cheeks="blush")
    g9 "I suppose you want them in your ass?"
    call her_main("Naturally.", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-2}(I'll try them in my pussy later tonight){/size}", "base", "closed", "base", "mid")
    call her_chibi_scene("grope_ass_back")
    call nar(">You push the first bead in with ease.")
    her "*Mmm*... {heart}"
    m "How many do you think you can take, my dear?"
    call her_main("How many have you got?", "base", "narrow", "base", "up", cheeks="blush")
    g9 "That's the spirit!"
    call nar(">You push another one inside with little resistance.")
    call her_main("Yess {heart} one more please.", "open", "narrow", "base", "up", cheeks="blush")
    call nar(">You feel the beads sink deeper when you push the third one inside.")
    call her_main("*Ohhh*, they're... they're moving {heart}.", "grin", "narrow", "base", "up", cheeks="blush")
    call nar(">The fourth takes some work before it pops in.")
    call her_main("Ah {heart} ah {heart}", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">You push the last one forcefully inside.")
    call her_main("*Ahhhhh* {heart} delightful.", "open_tongue", "narrow", "base", "up", cheeks="blush")
    her "They're so deep in my ass... almost like your cock."
    g9 "I can..."
    call her_main("No you can't! My butthole is too tight for both.", "annoyed", "closed", "base", "mid", cheeks="blush")
    call her_main("{size=-2}(But it's such a good idea){/size}", "grin", "narrow", "base", "up", cheeks="blush")
    m "I'm sure there's still room for at least one finger."
    call nar(">You finger her butthole gently.")
    call her_main("*Ahh*... {heart}{w=0.5} *aah*... {heart}", "silly", "narrow", "base", "up", cheeks="blush")
    call her_main("W-What did I say...", "grin", "narrow", "base", "up", cheeks="blush")
    call nar(">You wiggle the finger inside.")
    call her_main("You never listen, [genie_name]!", "grin", "narrow", "base", "up", cheeks="blush")
    m "What can I say, I just know what's best for you, my little witch."
    call nar(">You pick up the pace.")
    call her_main("Yesss! {heart}", "grin", "narrow", "base", "up", cheeks="blush")
    m "I thought you didn't want the finger?"
    g9 "In that case, one more finger."
    call nar(">She shivers when you insert a second finger.")
    call her_main("*Ahh* noo... no more please.", "open_wide_tongue", "narrow", "worried", "up", cheeks="blush")
    call her_main("My butthole is stretched so wide!", "open", "narrow", "base", "up", cheeks="blush")
    g9 "Your butthole is doing great."
    call nar(">You finger her butthole fiercely.")
    call her_chibi_scene("grope_ass_back_fast")
    call her_main("Nooo... *aahh* {heart}", "clench", "narrow", "worried", "mid_soft", cheeks="blush")
    m "Your pussy is getting neglected. We need to fix that!"
    call nar(">You start fingering her pussy with your other hand. She is panting heavily.")
    call her_main("Ah... ah... like that yesss {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call nar(">You suddenly pull out all the beads.")
    call her_main("*Ahhhhhh*!!", "grin", "narrow", "base", "dead", cheeks="blush", tears="messy")
    call nar(">And insert four fingers in her ass.")
    call her_main("I'm cumming, [genie_name]... I cumming!", "silly", "narrow", "base", "up", cheeks="blush")
    m "If you must..."
    call nar(">You continue to work her ass while you finger her pussy.")
    her "No don't I..."
    call her_main("Cummm {heart} {heart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("Agaaain *aaah* {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g11 "Sorry my little anal whore but I'm starting to get tired."
    call her_main("Don't you dare stop now!", "scream", "base", "angry", "mid", cheeks="blush", tears="messy", trans=hpunch)
    call her_main("Just a little more pleassse {heart}", "grin", "narrow", "base", "dead", cheeks="blush", tears="messy")
    call her_main("Because I will...", "grin", "narrow", "base", "dead", cheeks="blush", tears="messy")
    call her_main("Come again!!", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    hide screen hermione_main
    call blkfade

    ">There's a small puddle on your desk from her juices. You slowly remove your fingers."

    call her_chibi_scene("lie_on_desk")
    call hide_blkfade
    pause .5

    call her_main("*Pant* *pant*", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("I feel completely ravaged but happy.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("Thank you professor, for letting me discover such great sensations.", "grin", "narrow", "base", "mid_soft", cheeks="blush", tears="mascara")
    call her_main("But I'm exhausted so good night.", "grin", "closed", "base", "mid", cheeks="blush", tears="mascara")
    hide screen hermione_main
    call blkfade

    ">She puts her shirt back on and rushes to the door."

    $ hermione.wear("all")

    call her_chibi("stand","door","base",flip=True)
    call gen_chibi("sit_behind_desk")
    call hide_blkfade
    pause .5

    call bld
    m "Come back here, girl."
    g11 "I need your mouth, I can't hold it anymore."
    pause .5

    call her_chibi("stand","door","base")
    pause .5

    call her_main("Professor!", "open", "happy", "base", "mid", cheeks="blush")
    call her_main(".........", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("Can I have points for this?", "mad", "wide", "base", "stare", cheeks="blush")
    g11 "Now!"
    hide screen hermione_main
    call blkfade

    ">She comes back and does not seem particularly upset."

    call her_chibi_scene("bj")
    call hide_blkfade
    call ctc

    call bld
    her "*Slurp*! *Slurp*! *Gulp*!"
    g9 "Yes, like that..."
    call nar(">Hermione eagerly sucks your dick.")
    m "You seem to be in a hurry. Is it because you're not getting points for this?"
    m "Consider it a payment for your private lessons."
    her "*Mmmh*..."
    m "Next time, come with your robe and your robe only."
    call nar(">She briefly nods.")
    her "*Slurp*! *Gulp*! *Slurp*!"
    g9 "You're doing great my little whore, I will..."
    g11 "Yes!"

    call cum_block
    call her_chibi_scene("bj_cum_in")
    hide screen bld1
    with d3

    her "*Gobble*! *Gobble*! *Gobble*!"
    call ctc

    g9 "Good girl, you swallowed it all!"
    call blkfade

    ">She wipes her mouth."
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade
    call ctc

    call her_main("Sir, I still think I deserve some...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Good night, my dear child."
    call her_main(".........", "annoyed", "narrow", "base", "up", cheeks="blush")
    call her_main("Good night, professor.", "annoyed", "closed", "base", "mid", cheeks="blush")

    call her_walk("door", "base")

    call her_main("{size=-4}(Sucking his cock without getting any points!){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(If he hadn't made me come so hard...){/size}", "base", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-4}(*sigh* Although I guess it's not that high a price...){/size}", "base", "narrow", "base", "down", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 13

    if her_whoring < 24:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E13:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    ####################
    ### Robe Section ###
    ####################

    #call her_main("Oh! I can't believe I forgot! Stay where you are, I'll be right back!", "mad", "wide", "base", "stare", cheeks="blush")
    #hide screen hermione_main
    #call play_sound("door")
    #call blkfade

    #call play_sound("door")
    #pause .3

    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_2_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_2_s.webp"
    #call set_her_action("naked") #Removes all clothes.
    #$ hermione_wear_robe = True

    #call her_chibi("stand","door","base")
    #call hide_blkfade

    #call her_walk("mid", "base")

    #call her_main("{size=-4}*panting*{/size} Oh good, you're still here.", "open", "base", "base", "mid", cheeks="blush", xpos="right", ypos="base")
    #m "Is it safe to assume you have honoured my request this time?"
    #call her_main("I thought it was obvious.", "open", "happy", "base", "mid", cheeks="blush")
    #call her_main("I even had to hide in an alcove to avoid getting noticed on my way here!", "open", "base", "base", "mid", cheeks="blush")
    #call her_main("It was so embarrassing!", "open", "happyCl", "worried", "mid", cheeks="blush")
    #call her_main("{size=-2}(And exciting!){/size}", "open", "happyCl", "worried", "mid", cheeks="blush")
    #m "Are you sure you're not wearing anything underneath?"
    #call nar(">Hermione opens up her cloak a little.")
    #pause .2

    #hide screen hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.webp"
    #call her_main("", "open", "happy", "base", "mid", cheeks="blush")
    #call ctc

    #call her_main("Does this answer your question?", "open", "happy", "base", "mid", cheeks="blush")
    #m "Not really. It's hard to tell from this distance. I mean, it's so dark..."
    #call her_main("...", "annoyed", "narrow", "base", "up")
    #pause .2

    #hide screen hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_open_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_open_s.webp"
    #call her_main("", "base", "closed", "base", "mid", cheeks="blush", trans=d5)
    #call ctc

    #call her_main("Is that better?", "base", "narrow", "base", "mid_soft", cheeks="blush")
    #g9 "Oh yes, definitely. Well done, my girl."

    #hide screen hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.webp"


    call her_main("Alright then, can we start the lesson now?", "smile", "base", "angry", "mid", cheeks="blush")
    m "Maybe, I don't know... do you like butterbeer?"
    call her_main("You know I do. What's that got to do with...", "soft", "base", "base", "R", cheeks="blush")
    g9 "......."
    call her_main("Do you mean...{w=0.3} no, no way professor!", "scream", "wide", "base", "stare", cheeks="blush")
    m "Oh, rest assured, we won't start with the bottom end."
    call her_main("Still, professor, this is so dirty...", "silly", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-2}(And exciting!){/size}", "silly", "narrow", "base", "up", cheeks="blush")
    call her_main("Moreover, my butthole isn't stretched enough.", "annoyed", "closed", "base", "mid", cheeks="blush")
    g4 "Are you kidding me, with all your training!"
    call her_main("And what a training!", "annoyed", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-2}(Good thing I practised by myself, otherwise...){/size}", "angry", "happyCl", "worried", "mid", cheeks="blush")
    g4 "Now stop making up excuses!"
    m "I can see you rubbing your thighs from excitement!"
    call her_main("I thought it was so dark in here...", "open", "happy", "base", "mid", cheeks="blush")
    call her_main("*Humm*...{w=0.3} Okay, but you better start out easy on me.", "annoyed", "squint", "base", "mid")
    g9 "I'm always gentle with you, [hermione_name]."
    call her_main("Yeah, obviously...", "annoyed", "narrow", "annoyed", "up")
    m "{size=-2}(It's not as if you don't like it rough){/size}"
    m "Alright, my desk.{w=0.3} You{w=0.5}, naked{w=0.6}, now!"

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
    pause .5

    ">Hermione slowly slides down her robe and climbs up your desk."

    $ hermione.strip("robe")

    call her_chibi("dance","on_desk","on_desk")
    # call her_main(animation=bob)

    call hide_blkfade
    pause 1

    call blktone
    call her_main("You're crazy for my body, aren't you?", xpos="mid", ypos="base")
    m "Why do you ask..."
    call her_main("Because a girl likes to be complimented, professor!", "annoyed", "squint", "base", "mid")
    call her_main("Especially when she's about to do these kinds of things!", "annoyed", "narrow", "annoyed", "up")
    m "I meant, of course you have a amazing body! That's not up to question."
    call her_main("Best in the school?", "base", "narrow", "base", "up", cheeks="blush")
    m "......{w=0.3} Yeah, yeah, best in the school."
    call her_main("I can tell you're lying!", "mad", "base", "angry", "mid", cheeks="blush")
    m "Miss Granger, I've lived for a very long time and believe me, I have seen few women with a body like yours."
    m "And definitely none in this school."
    m "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}"
    m "{size=-2}(I wonder if I can fire him for that...){/size}"
    call her_main("Thank you, professor.", "open", "happyCl", "worried", "mid", cheeks="blush")
    call her_main("Feel free to use my body as you please.", "angry", "happyCl", "worried", "mid", cheeks="blush")
    m "{size=-2}(*sigh* women...){/size}"
    m "Bend over the desk my dear little witch."
    call her_main("{size=-2}(It starts with my dear little witch and ends up with my dear anal whore...){/size}", "annoyed", "narrow", "base", "up", cheeks="blush")
    call her_main("{size=-2}(*sigh* men...){/size}", "annoyed", "narrow", "base", "up", cheeks="blush")
    call her_main("As you wish my dear {b}old{/b} headmaster.", "open", "happy", "base", "mid", cheeks="blush")
    m "{size=-2}(If you knew how old I actually am...){/size}"
    call her_main(animation=None)
    hide screen hermione_main
    call blkfade

    ">Hermione languorously climbs down your desk and bends over it."

    call her_chibi_scene("lie_on_desk", trans=d5)

    call her_main("I'm ready, [genie_name].", ypos="head", flip=False, trans=d3)

    call give_gift(">You take an empty butterbeer bottle, spit on the neck, and push it inside her butthole.",butterbeer_ITEM)

    call her_chibi_scene("lie_on_desk_fingering_slow")
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    call ctc

    call her_main("*Mmm*... Yes... like that.", "base", "narrow", "base", "up", cheeks="blush", xpos="mid", ypos="base", flip=True)
    call her_main("My pussy feels lonely without your care.", "grin", "wink", "base", "mid", cheeks="blush")
    call nar(">You start to finger her pussy too.")
    m "Poor little thing."
    call her_main("What's better in life than this professor?", "open", "narrow", "base", "up", cheeks="blush")
    m "Oh, I don't know."
    call her_main("Thank you for letting me discover such pleasures.", "open", "happyCl", "worried", "mid", cheeks="blush")
    g9 "{b}My{/b} pleasure."
    call her_main("It's even better when it's mutual, isn't it?", "open", "happy", "base", "mid", cheeks="blush")
    m "*Hmm*... Yes you're right... I'm glad you feel that way."
    call her_main("Now a little deeper please.", "soft", "base", "base", "R", cheeks="blush")
    call nar(">You push the whole bottle neck up inside her asshole.")
    call her_main("*Ohhh* yesss! {heart}", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("More, faster!", "open", "narrow", "base", "up", cheeks="blush")
    call her_chibi_scene("lie_on_desk_fingering")
    call nar(">You rotate the bottle while going back and forth deeper and deeper.")
    call her_main("Yessss, don't forget my pussy. {heart}", "grin", "narrow", "base", "up", cheeks="blush")
    g9 "Oh, your pussy better be ready for what's coming!"
    call nar(">You insert all four fingers in her sopping wet pussy.")
    call her_main("Sweet Circe, *aah* *ah*, that's too much! {heart}", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    m "Nothing is too much for my little whore."
    call nar(">You increase the pace of both hands.")
    call her_main("No, no, yes, yessss! {heart}", "grin", "narrow", "base", "dead", cheeks="blush", tears="messy")
    call nar(">Most of the bottle is inside her now, leaving just enough to get a good grip.")
    m "Push the bottle, push it!"
    call nar(">Whenever she pushes it back you do the same in the other direction.")
    call her_main("This is, this is, *aaaah*!!! {heart}{heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call nar(">Her whole body convulses as she comes hard.")
    hide screen hermione_main
    call blkfade

    call her_chibi_scene("lie_on_desk_fingering_pause")
    pause .3
    call hide_blkfade
    call ctc

    call her_main("*Panting* *panting*", "grin", "narrow", "base", "dead", cheeks="blush", tears="messy", ypos="head", flip=False, trans=d3)
    call her_main("P-professor...{w=0.3} I'm so happy right now.", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    g9 "Glad to hear it."
    hide screen hermione_main
    call blkfade

    ">After a while, she makes herself somewhat presentable."

    #$ hermione_wear_robe = True

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade

    call bld
    m "Sweet dreams my little princess."
    call her_main("You too, professor.", "open", "base", "base", "mid", cheeks="blush", xpos="mid", ypos="base", flip=False)
    g9 "They are always sweet with you around."
    call her_main("Thank you.", "base", "narrow", "base", "up", cheeks="blush")
    m "And next time bring your books, I'll help you with your revisions."

    call her_walk("door", "base")

    call her_main("{size=-4}(Yes, sweet dreams...){/size}", "base", "happyCl", "worried", "mid", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(Sweet and wet!){/size}", "silly", "narrow", "base", "mid_soft", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 14

    if her_whoring < 24:
        $ her_whoring += 1

    jump end_hermione_event

label hg_tutor_E14:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    #call her_main("I'll go get my books right away, sir!", "soft", "base", "base", "R")
    #hide screen hermione_main
    #call play_sound("door")
    #call blkfade
    #pause 1

    #call set_her_action("hold_book")

    #call play_sound("door")
    #pause .3

    #call hide_blkfade
    #call ctc

    #call her_main("Revisions are a serious matter, [genie_name]!", "open", "base", "worried", "mid")
    #m "{size=-2}(My cock in your ass is a serious matter...){/size}"
    #m "In this regard, I kinda lied, it's more of a mock exam than revisions."
    #call her_main("What a surprise!", "annoyed", "narrow", "base", "up", cheeks="blush")

    m "[hermione_name], today I'd like to examine if you've been keeping up with your tutoring lessons..."
    g9 "And make sure you've been working out your butthole."
    call her_main("........", "annoyed", "narrow", "base", "up", cheeks="blush")
    g9 "With my cock."
    call her_main("I see...", "annoyed", "base", "base", "R")
    call her_main("I'm not against that but I bet I'll gain no points for this?", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "I'm helping you with your revisions, why should you be getting points for that?"
    call her_main("And what revisions...", "annoyed", "closed", "base", "mid", cheeks="blush")
    call her_main("Alright, since you have helped me a lot, I'm in.", "base", "base", "base", "R", cheeks="blush")
    call her_main("{size=-2}(I give myself away for free now, what a bad whore I make){/size}", "base", "narrow", "worried", "mid_soft", cheeks="blush", tears="soft")
    m "Come here and strip."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    hide screen hermione_main
    with d3

    #call set_her_action("naked")
    #call set_her_action("hold_book")
    $ hermione.strip("all")

    call her_chibi_scene("lie_on_desk")
    hide screen bld1
    call hide_blkfade
    call ctc

    show screen blktone
    call her_main(xpos="mid", ypos="base")
    g9 "You can open a book if you want."
    call her_main("I should read about this spell called \"the Clap\"!", "annoyed", "closed", "base", "mid", cheeks="blush")

    hide screen hermione_main
    call nar(">You take advantage of her moment of distraction to force you cock into her butthole.")

    call her_chibi_scene("sex_naked_slow")
    hide screen bld1
    with d1
    with hpunch
    pause .8

    call her_main("Ah, you brute {heart}", "grin", "narrow", "base", "up", cheeks="blush")
    m "Your butthole is the perfect fit, not too tight and not too stretched!"
    call her_main("You've trained me well...", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">You caress her clit while fucking her.")
    call her_main("*Mmmh*, yes {heart}", "open", "narrow", "base", "up", cheeks="blush")
    g9 "You love it don't you?"
    call her_main("Your cock in my ass, oh yes.", "base", "narrow", "base", "up", cheeks="blush")
    m "Even without points?"
    call her_main("Don't make me regret agreeing to this.", "upset", "happyCl", "worried", "mid", cheeks="blush")
    m "Say you love it even without points."
    call her_chibi_scene("sex_naked")
    call nar(">You increase the pace.")
    call her_main("*Ahh* yesss {heart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
    call her_main("I'm such a whore, I love sex even for free.", "mad", "wide", "base", "stare", cheeks="blush")
    g9 "You know it!"
    call her_main("Don't make it a habit.", "open", "happy", "base", "mid", cheeks="blush")
    m "......"
    call nar(">You pull out your cock and roughly shove it back inside.")
    with hpunch
    call her_main("*Aaaaah* {heart}", "open", "narrow", "annoyed", "up", cheeks="blush")
    call her_main("I love being sodomised savagely by my headmaster.", "silly", "narrow", "base", "up", cheeks="blush")
    call nar(">And again.")
    with hpunch
    her "Yessss {heart}"
    call her_main("I love his big cock in my ass.", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    call nar(">You slap her butt-cheek.")
    call play_sound("slap_1")
    with hpunch
    call her_main("And being punished for my sluttiness.", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    call play_sound("slap_1")
    with hpunch
    call her_main("*Aah*, like this, punish me more master {heart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    call play_sound("slap_1")
    with hpunch
    call her_main("Yess!", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call play_sound("slap_1")
    with hpunch
    call her_main("More!", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call play_sound("slap_1")
    with hpunch
    call her_main("I'm about to...", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")
    call play_sound("slap_1")
    with hpunch
    pause .1
    call play_sound("slap_1")
    with hpunch
    pause .1
    call her_main("Cuuuum {heart} {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    call her_chibi_scene("sex_naked_fast")
    call nar(">You fuck her butthole fiercely.")
    call her_main("Yes, yes, again, *aaaah* {heart}", "open_wide_tongue", "narrow", "base", "up", cheeks="blush")
    g11 "Yes, my little whore, yes!"
    call her_chibi_scene("sex_naked_cum_out")
    call her_main("*Panting* *panting*", "open", "narrow", "worried", "mid_soft", cheeks="blush", tears="mascara")
    call her_chibi_scene("sex_naked_cum_out_done")
    g11 "*Panting* *panting*"

    hide screen hermione_main
    call blkfade

    hide screen hermione_main
    call her_chibi_scene("lie_on_desk")
    pause 1
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    pause .8

    call bld
    m "*sigh* that was, that was..."
    call her_main("Marvellous {heart}", "smile", "base", "base", "R")
    call her_main("I'm so glad you agreed to tutor me, professor...", "silly", "narrow", "base", "up", cheeks="blush")
    call her_main("Your lessons have changed my life so much!", "smile", "base", "angry", "mid", cheeks="blush")
    g9 "{size=-2}(Victory!){/size}"
    call her_main("But if you think you can fuck me all the time without giving me points...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("You're dreaming!", "annoyed", "narrow", "base", "up", cheeks="blush")
    m "{size=-2}(*Ohhh*...){/size}"
    m "Even occasionally?"
    her "......."
    call her_main("Only if you are well-behaved...", "soft", "base", "base", "R", cheeks="blush")
    g9 "I'm the most well-behaved professor in the whole school!"
    call her_main("Sure.", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call her_main("{size=-2}(At least, you're not the worst...){/size}", "annoyed", "narrow", "base", "up", cheeks="blush")
    m "Good night, [hermione_name]."
    call her_main("Good night, [genie_name].", "base", "base", "base", "R", cheeks="blush")

    hide screen hermione_main
    call blkfade

    ">You dismiss Hermione."
    ">She puts her clothes back on without haste."

    call play_sound("equip")
    $ hermione.wear("all")
    pause 1

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade
    pause 1

    call her_walk("door", "base")

    call her_main("{size=-4}(He's hardly Prince Charming but...){/size}", "base", "narrow", "base", "mid_soft", cheeks="blush", ypos="head", flip=False, trans=d3)
    call her_main("{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}", "grin", "narrow", "base", "up", cheeks="blush")

    call her_chibi("leave")

    $ her_tutoring = 15

    if her_whoring < 24:
        $ her_whoring += 1

    jump end_hermione_event
