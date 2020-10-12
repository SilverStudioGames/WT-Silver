
### Talk with Cho ###

label cc_pf_talk:

    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"

    if cc_pf_talk.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_favor_menu.personal

    # Start Event
    $ cc_pf_talk.start()

    # End Event Jump
    label end_cho_talk_event:

        if cho_tier == 1:
            if cho_whoring < 3: # Points til 3
                $ cho_whoring += 1

        elif cho_tier == 2:
            if cho_whoring < 9: # Points til 9
                $ cho_whoring += 1

    jump end_cho_event

### Tier 1 (pre Hufflepuff) ###

label cc_pf_talk_T1_intro_E1:
    m "Let's have a little chat shall we."
    g9 "Just to get to know each other a little bit better."
    call cho_main("Of course, Sir.", "smile", "base", "base", "mid")
    m "First, I'd like you to come a bit closer."
    call cho_main("Very well, [cho_genie_name]...", "soft", "base", "base", "R")

    call cho_walk("desk", "base")
    call play_music("cho")
    call cho_main(face="happy", xpos="mid", ypos="base", trans=d3)
    call ctc

    call cho_main("What would you like to talk about?", "soft", "base", "base", "mid")
    m "Do you have a boyfriend, Miss Chang?"
    call cho_main("Excuse me?", "open", "wide", "base", "mid", trans=hpunch) # Shocked
    m "I asked if you have boyfriend. Anybody you fool around with?"
    call cho_main("Me? Professor? Ha--{w=0.4} hav--{w=0.4} a boyfriend?", "open", "wide", "base", "R", cheeks="blush") # Reluctant, Embarassed
    g9 "Or a girlfriend! That would be even better, now that I think about it!"
    call cho_main("Sir that's--{w=0.3} that's not something a headmaster should be concerned about.", "soft", "happyCl", "worried", "L", cheeks="blush")
    call cho_main("And I don't see how this information would be of importance for my training.", "open", "wide", "raised", "downR", cheeks="blush")
    call cho_main("Why would it matter if--{w=0.5} Even if I did I'd--", "soft", "wide", "base", "down", cheeks="blush")
    g9 "So you don't have one?"
    call cho_main("You're making me nervous, [cho_genie_name]. {heart}", "horny", "narrow", "worried", "R", cheeks="blush")
    m "(So cute.{w=0.5} Perhaps this is something I could push her further on...)"

    call cho_main("Sir, I do not have a boyfriend at the moment.", "soft", "closed", "angry", "mid")
    call cho_main("I hope that answers your question.", "annoyed", "narrow", "base", "mid")
    g9 "So, a girlfriend then?"
    call cho_main("!!!", "angry", "wide", "raised", "mid", cheeks="blush")
    call cho_main("No. Why would you even think that, [cho_genie_name]?!", "open", "closed", "angry", "mid")
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "(She doesn't seem that keen on the subject, perhaps I could tell her...)"

    label .choices:
    menu:
        "\"It's important to open up to your headmaster.\"":
            m "Emphasis on \"opening up\"..."
            call cho_main("I don't think that will be necessary, [cho_genie_name].", "annoyed", "narrow", "angry", "mid")
            m "There's a lot more to gather from discussing previous life choices than you might think."
            m "You get to learn a lot about the way someone has matured by previous experiences..."
            m "Like a first kiss, who it was with, and so on..."
            call cho_main("You think I'm mature?", "soft", "base", "base", "mid")
            g4 "(That's what she's focusing on?)"
            m "*Ahem*, yes.{w=0.5} Of course you are, don't you think so?"
            call cho_main("Well, my previous boyfriend didn't seem to think so...", "open", "base", "raised", "R")
            m "So you did have one?"
            call cho_main("*Ugh*{w=0.8} Fine...{w=0.8} I'll tell you about him...", "soft", "narrow", "base", "down")

            pass

        "\"It's okay if you like girls...\"":
            if cho_mood == 0:
                $ cho_mood += 1
            m "Swinging the other way, you know..."
            call cho_main("What?", "angry", "wide", "base", "mid")
            m "Some people like flicking the bean rather than rubbing a wand..."
            call cho_main("*Uhm*, I never said I minded either way...", "quiver", "narrow", "worried", "R")
            m "So you have had a girlfriend?"
            call cho_main("I'd rather not talk about it right now...", "soft", "narrow", "worried", "mid")
            m "(Damn, maybe that's not the way to go about this, maybe instead I could tell her...)"

            jump cc_pf_talk_T1_intro_E1.choices

        "\"Let me tell you something about my own previous relationships...\"":
            if cho_mood == 0:
                $ cho_mood += 1
            call cho_main("Sir, I'd rather not hear a boring old tale about any of your old flames...", "open", "narrow", "base", "R")
            g9 "Oh they weren't boring at all!"
            call cho_main("*Hmm*?", "annoyed", "narrow", "base", "mid")
            g9 "They were very intimate..."
            call cho_main("???", "annoyed", "base", "raised", "mid")
            g4 "Very sexual!"
            call cho_main("!!!", "annoyed", "wide", "base", "mid")
            g9 "Lots of acrobatic stuff!"
            call cho_main("NO Sir, please!{w=0.5} I don't want to know any of that!", "scream", "closed", "angry", "mid", trans=hpunch)
            call cho_main("(Gross!{w=0.5} Keep it to yourself...)", "angry", "narrow", "worried", "R")
            m "I just wanted to expand my backstory a little bit...{w=0.5} What's so wrong with that..."

            jump cc_pf_talk_T1_intro_E1.choices

    # Cedric Diggory
    call cho_main("Cedric Diggory was my boyfriend during the time Hogwarts was hosting the \"triwizards tournament\".", "soft", "base", "base", "R")
    m "(They host tournaments here? Interesting...)"
    call cho_main("That year was the most fun I've ever had!", "smile", "base", "base", "mid")
    m "Was he that good?"
    call cho_main("What?{w=0.5} No, Sir, not because of him!{w} The tourney, [cho_genie_name]!", "soft", "narrow", "base", "mid")
    m "Sure..."
    call cho_main("We should have it every year if you were to ask me!", "open", "closed", "base", "mid")
    g9 "(A cosplay tournament is what this school needs...)"
    call cho_main("Sir that would be great!", "smile", "narrow", "base", "mid")
    g4 "(Wait, wait!{w=0.8} A \"nude\" cosplay tournament!{w=0.6} Even better!)"
    g4 "(Is it even cosplay if they're naked?)"
    call cho_main("And with new contestants every month! You've got to do this, Sir!", "smile", "base", "base", "mid")
    m "I'll think about it..."

    m "Now tell me, how come you two ended up together?"
    call cho_main("Oh. Well...", "soft", "base", "base", "down")
    call cho_main("I have this thing for...{w=0.5} athletes.", "horny", "base", "base", "down")
    call cho_main("Cedric was the representative champion of our school, so of course I had to date him.", "horny", "base", "worried", "down")
    m "Of course..."
    m "(She's into athletes, so so...)"
    g4 "(You should see me, girl. I'm shredded!)"
    m "(Too bad you can only see the body of that wrinkly old geezer...)"
    m "(Maybe there's like a steroid spell...)"
    g4 "{size=-4}Plexus Maximus!{/size}"
    call cho_main("Did you say something?", "soft", "base", "raised", "mid")
    m "Oh, it was nothing... go on."

    call cho_main("Anyway, Cedric even put his life at risk during the whole thing.", "open", "base", "base", "R")
    m "Oh you poor, poor thing..."
    m "I can see why you didn't want to mention him before then..."
    call cho_main("Why?", "soft", "narrow", "raised", "mid")
    m "He surely will be missed."
    call cho_main("Sir?", "angry", "narrow", "base", "mid")
    m "Died just the way he lived...{w} as a plot device."
    call cho_main("Sir, Cedric isn't dead.", "open", "narrow", "angry", "mid")
    m "Oh...{w=0.3} he's not?"
    call cho_main("No!", "annoyed", "narrow", "angry", "mid")
    m "I could've sworn I read that somewhere..."
    m "Are you sure he's still around?{w=0.6} What if he {b}did{/b} die, but then he returned from the dead?"
    g4 "For all you know he could be a vampire!"
    call cho_main("Sir, you're talking nonsense...", "annoyed", "narrow", "angry", "R")
    call cho_main("Please don't joke about your student like that. It's so unlike you...", "open", "closed", "base", "mid")
    call cho_main("He's one of your bests! The best student Hufflepuff has ever seen!", "open", "base", "base", "mid")
    m "A Hufflepuff? Well, that explains everything..."
    m "If he's such an exceptionally great student, then why aren't you two still together?"
    call cho_main("Things didn't work out, naturally...", "open", "base", "raised", "R")
    call cho_main("The tourney ended, and he didn't win, so...", "soft", "base", "raised", "down")
    m "So you two broke up?... Because he didn't win?"
    call cho_main("That was one of the reasons...", "soft", "base", "base", "downR")
    call cho_main("There is also the fact that he's on the Hufflepuff Quidditch team, as their Seeker.", "open", "base", "base", "mid")
    call cho_main("It's our last shot at winning the Quidditch house cup, for the both of us.", "angry", "base", "base", "down")
    call cho_main("We'd constantly be at each other's throats.", "soft", "narrow", "angry", "mid")
    g4 "Intriguing!"
    m "You are missing out, girl..." # Small text
    g9 "{size=-4}Hate-sex is the best!{/size}" # Small text
    call cho_main("I didn't quite hear that, Sir.", "base", "base", "base", "mid")
    m "Who else did you do it with?"
    call cho_main("Do it with?", "soft", "narrow", "raised", "mid") # Shocked
    m "Smooching, kissing, snogging...{w=0.8} whatever you call it nowadays..."
    call cho_main("With all due respect, Professor, it's very odd that you'd ask me about those sort of things...", "open", "closed", "base", "mid")
    call cho_main("But... you {b}are{/b} helping me.{w=0.8} So I guess I owe you that much...", "annoyed", "base", "base", "R")
    g9 "That's what I wanted to hear."

    # Fleur
    call cho_main("Well, Cedric wasn't the only one I was with during the year of the tourney...", "open", "base", "raised", "down")
    g9 "Is that so...{w} feel free to elaborate!"
    call cho_main("I was sort of dating somebody else...", "soft", "base", "worried", "downR")
    call cho_main("At the same time.", "horny", "base", "worried", "R") # Embarrassed
    m "No{w} way!"
    g4 "You were cheating on that {i}Hufflepuffer{/i}?"
    call cho_main("I wouldn't call it cheating, Professor. It wasn't even that serious with Cedric to begin with.", "annoyed", "narrow", "base", "mid")
    call cho_main("I had a unique opportunity, that's all...", "soft", "base", "base", "R")
    call cho_main("One of those \"no strings attached\" kind of things... Trying out new stuff...", "smile", "base", "base", "downR")
    m "Like what?"
    call cho_main("Dating a girl, for example.", "base", "narrow", "base", "mid")
    g9 "(Finally this is getting interesting!)"
    call cho_main("She was one of the students from Beauxbatons.", "soft", "base", "base", "downR")
    m "(...)"
    call cho_main("A French girl.", "soft", "base", "base", "down")
    g9 "And I hope you also {i}frenched{/i} that french girl!"
    call cho_main("Among other things...", "angry", "closed", "worried", "mid") # Super embarrassed
    call cho_main("(Why am I telling him this?)", "horny", "narrow", "worried", "R")
    g9 "And who was it?"
    call cho_main("Fleur Delacour.{w} She was also a champion at the tourney.", "soft", "base", "worried", "mid")
    g4 "I'm in shock!"

    # Viktor
    call cho_main("Then there also was Viktor Krum who--", "open", "base", "base", "R")
    with hpunch
    g4 "Slow down, girl! I'm still not over the fact that you made out with a girl!"
    call cho_main("", "annoyed", "narrow", "base", "mid")

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            call bld

        "-Participate in the conversation-":
            $ masturbating = False

    g9 "I want to hear everything!"

    call cho_main("I'm sorry, Sir. It's just that...", "open", "closed", "raised", "mid")

    if daytime:
        call cho_main("I'm really late for classes. May we postpone this talk to some other time?", "soft", "narrow", "worried", "R")
    else:
        call cho_main("It's getting really late. May we postpone this talk to some other time?", "soft", "narrow", "worried", "R")

    if masturbating:
        g4 "What? Please don't go now. I've only just started!"
        call cho_main("Started with what, [cho_genie_name]?", "annoyed", "narrow", "angry", "mid")
        g4 "I'll give you ten house points if you stay!{w=0.8} Just a tiny bit longer!"
        call cho_main("And what makes you believe that I'd agree to such a thing?{w=0.8} Getting rewarded with points for doing nothing?", "open", "closed", "base", "mid")
        call cho_main("Earning house points in such a way is despicable, and it would be unfair towards the other school houses, as well as my fellow students...", "open", "narrow", "base", "mid")
        call cho_main("", "annoyed", "narrow", "angry", "mid")
        g4 "Fifty points?"
        call cho_main("I have to go now, Sir.", "annoyed", "narrow", "angry", "R")
        m "(Fuck me...)"

        call gen_chibi("sit_behind_desk")
        with d3
        pause .8

        call cho_main("Until next time!", "soft", "narrow", "base", "mid")

    else:
        m "Okay, girl. You may leave..."
        call cho_main("Thank you, Sir.", "base", "base", "base", "down")
        call cho_main("See you next time.", "smile", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(...)"
    if masturbating:
        m "Well, I got blue-balled..."
        m "Feel like I've deserved it..."

    jump end_cho_talk_event

label cc_pf_talk_T1_intro_E2:
    g9 "Get closer, [cho_name]..."
    call cho_main("...", "annoyed", "base", "base", "down")

    call cho_walk("desk", "base")
    call play_music("cho")
    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    pause .5

    call cho_main("Another talk, Professor?", "soft", "narrow", "angry", "mid")
    call cho_main("Are we going to discuss my previous relationships again?", "open", "narrow", "base", "R")
    m "I don't know.{w=1.0} Would you like to?"
    call cho_main("I'd rather not.", "soft", "narrow", "angry", "mid")
    m "Tell me about yourself then."
    call cho_main("Of course, [cho_genie_name].", "smile", "base", "base", "mid")
    call cho_main("We had a training session yesterday. ", "soft", "base", "base", "R")
    m "Training session?"
    call cho_main("Yes. We are preparing ourselves for the Quidditch match against Hufflepuff.", "open", "narrow", "base", "mid")
    call cho_main("Our team really believes that we have a chance to win this time!", "smile", "base", "base", "mid")
    call cho_main("They got a huge boost of confidence after I told 'em that the {i}great Albus Dumbledore{/i} would be training us himself!", "base", "narrow", "base", "mid")
    m "Are you getting along with your team well?"
    call cho_main("I'd say so.{w=1.0} But there has been a time when...", "soft", "base", "base", "mid")
    call cho_main("Let's just say that it has been difficult for me at first. After all Quidditch is largely dominated by men...", "open", "narrow", "worried", "down")
    call cho_main("Getting accepted into our Quidditch team was a challenge. I really had to prove I was worth it.", "soft", "narrow", "worried", "mid")
    g9 "And how exactly did you manage that? Mind spilling the beans?"
    call cho_main("Through diligence, expertise, and determination!", "open", "closed", "base", "mid")
    call cho_main("", "normal", "base", "base", "mid")
    m "(...)"
    m "I was sort of expecting something else entirely but... you do you..."
    call cho_main("And as you can see -- it did work out in my favour, Sir.", "smile", "base", "base", "mid")
    call cho_main("Very few teams have allowed a female player into their ranks over the past years.", "open", "narrow", "angry", "R")
    call cho_main("And I've been the only female seeker at this school in over half a century!", "open", "wide", "base", "mid")
    call cho_main("Can you even believe that, [cho_genie_name]?", "soft", "base", "raised", "mid")
    m "(Half a century? That's like a coffee break for me girl...)"
    call cho_main("I don't want to brag, [cho_genie_name], but the role of a seeker is {b}the{/b} most important position in a team by far!", "smile", "narrow", "base", "mid")
    call cho_main("If you don't have a good seeker, you have no chance of winning!", "soft", "closed", "base", "mid")
    m "Which is why you need my help so badly..."
    m "Because you are great at it..."
    call cho_main("That we're losing is neither my fault, nor my team's, [cho_genie_name]!", "open", "base", "angry", "mid")
    m "So whose is it then?"
    call cho_main("The enemy team's, obviously!", "soft", "narrow", "angry", "mid")
    call cho_main("They are cheating! And they have done so for years!", "mad", "narrow", "angry", "R")
    call cho_main("This is my last chance! And I'm growing more and more desperate with my situation...", "mad", "narrow", "angry", "mid")
    m "(...)"

    menu:
        "-Jerk off while she is talking-":
            hide screen cho_main
            hide screen bld1
            with d5
            pause .5

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            $ cho_jerk_off_counter += 1
            $ masturbating = True

        "-Participate in the conversation-":
            $ masturbating = False

    call cho_main("Ever since I was a little girl -- Quidditch has been my dream...", "soft", "narrow", "worried", "down")
    call cho_main("[cho_genie_name], can you imagine how {b}hard{/b} it was for me?", "soft", "narrow", "worried", "mid")
    if masturbating:
        g4 "{size=-4}(Yes, yes... It's so hard for you, you little slut!!!){/size}"
    call cho_main("How difficult it was for me at first?", "open", "narrow", "worried", "R")
    call cho_main("Getting accepted?", "soft", "closed", "worried", "mid")
    if masturbating:
        g4 "{size=-4}(I'd accept your ass on my cock if you're in such a need for acceptance, you whore!){/size}"
    call cho_main("I'm the only female in my team. Constantly surrounded by other men...", "soft", "base", "worried", "down")
    if masturbating:
        g4 "{size=-4}(Yes! Yes! And they all would like to have their way with you!){/size}"
    else:
        m "(Quite a sausage-party this Quidditch I have to admit.)"
        g4 "(Maybe telling Hermione off was a bad idea after all...)"
        g9 "(An \"all female\" team would be more fun to watch...)"
    call cho_main("I can constantly feel their gazes behind my back...", "disgust", "base", "worried", "down")
    call cho_main("My own team, [cho_genie_name]!{w} They treat me like the plague!", "upset", "base", "worried", "mid")
    call cho_main("They ignore me during classes...", "soft", "closed", "base", "mid")
    call cho_main("When we're in our dormitories they are going out of their way to not cross paths with me...", "annoyed", "narrow", "angry", "R")
    call cho_main("And in the showers they're scared to even look at me!", "angry", "narrow", "angry", "mid")
    if masturbating:
        g4 "{size=-4}(Yes, yes!{w=0.5} Even in the showers you whore--){/size}"
        with hpunch
        m "Wait a bloody minute!{w} You shower {b}with{/b} your team?"
    else:
        m "The showers?{w} You shower {b}with{/b} your team?"
    call cho_main("Of course, [cho_genie_name]. It was after my request, after all.", "soft", "base", "raised", "mid")
    g4 "No kidding?"
    call cho_main("They shouldn't exclude me from team activities just because I'm a girl.", "open", "base", "base", "R")
    call cho_main("It makes absolutely no difference!", "base", "base", "base", "mid")
    if masturbating:
        g4 "You are naked with them? In the showers?"
    else:
        m "Just to be clear. You are naked with them, in the shower."
    call cho_main("Of course we're all naked, [cho_genie_name]!", "soft", "base", "angry", "mid")
    call cho_main("Why would I take showers with my clothes still on?", "soft", "closed", "base", "mid")

    # Genie cums.
    if masturbating:
        g4 "{size=-4}(You exhibitionist slut!){/size}"
        g4 "*Argh* {size=-4}(Here it comes!){/size}"

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call bld
        g4 "*heavy breathing* {size=-4}(Take it!){/size}"

        call cum_block
        call cho_main("", "base", "narrow", "base", "mid")
        g4 "*Argh*! {size=-4}(Shower in this, you slut!){/size}"

        call cum_block
        call cho_main("[cho_genie_name], are you alright?", "soft", "base", "base", "mid")
        call cho_main("You're sweating and breathing quite heavily...", "annoyed", "base", "worried", "mid")

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        call cho_main("Shall I get Madam Pomfrey to check on you--", "soft", "narrow", "base", "mid")
        g4 "No, no! I'm..."
        m "I'm done.{w=0.3} Let's get back to the topic."
        call cho_main("Which was?", "open", "base", "raised", "mid")
        m "You taking a shower with your \"teammates\"..."
        call cho_main("(...)", "annoyed", "narrow", "angry", "mid") # Annoyed

    m "Don't you think, the fact that they've seen you naked hasn't affected any of their actions?"
    call cho_main("Why would it, [cho_genie_name]? We're all adults here...", "soft", "closed", "base", "mid")
    m "Maybe that's your response to it, girl."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    g9 "Maybe your \"teammates\" aren't as... \"mature\" as you."
    call cho_main("I've known my team for years.{w=0.6} We're all professionals!", "soft", "narrow", "base", "mid")
    m "Let me ask you a question..."
    m "In the showers,{w=0.3} do they all have their backs turned towards you?"
    call cho_main("I don't know. Maybe they-- *uhm*...", "open", "base", "base", "mid")
    call cho_main("!!!", "normal", "wide", "base", "mid") # Cho remembers something?!
    call cho_main("", "normal", "happyCl", "worried", "mid", cheeks="heavy_blush")
    pause .6
    g9 "Yes?{w=0.3} What is it?"
    call cho_main("May I... May I leave, [cho_genie_name]?", "soft", "narrow", "worried", "mid", cheeks="blush")
    g9 "Don't want to tell me?"
    call cho_main("No.", "disgust", "happyCl", "worried", "mid", cheeks="blush")
    m "Fine...{w=0.3} you may leave..."
    call cho_main("Thank you, [cho_genie_name].", "open", "narrow", "worried", "mid", cheeks="blush")

    # Cho very slowly walks out of your office...
    call cho_walk(action="leave")

    call bld
    m "(...)"
    g9 "(That just gave me an idea!)"
    stop music fadeout 1.0

    $ cho_requests_unlocked = True
    call popup("You can now buy \"Public Requests\" from Cho!", "Congratulations!", "interface/icons/head/cho.webp")

    jump end_cho_talk_event

label cc_pf_talk_T1_E3:
    m "Care to tell me more about Quidditch?"
    call cho_main("Of course, [cho_genie_name].", "smile", "base", "base", "R")
    call cho_main("I always love talking about Quidditch!", "base", "base", "base", "mid")
    m "Yeah, yeah... I know."
    m "First, come closer. Let me have a good look at you!"
    call cho_main("Yes, Sir.", "base", "base", "base", "mid")

    call play_music("cho")
    call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    call cho_main("Anything specific you'd like to know?", "soft", "base", "base", "mid")
    m "Yes. Let's talk some more about Diggory..."
    g9 "Your ex-boyfriend."
    call cho_main("{size=-4}I knew I shouldn't have told him...{/size}", "disgust", "narrow", "base", "down", cheeks="blush")
    call cho_main("Sir, Why do you have to keep bringing that up?", "soft", "narrow", "base", "mid")
    call cho_main("What's past is in the past...", "annoyed", "narrow", "angry", "R")
    m "I believe otherwise..."
    g4 "Have you already forgotten that he's our enemy?!"
    m "Your relationship with him is of the utmost importance right now!"
    m "I need to know every tiny bit of detail about the two of you."
    m "His sexual preferences. Secret fetishes he might have. That sort of stuff..."
    call cho_main("Sir that's a very personal thing to ask for!", "open", "narrow", "base", "mid")
    call cho_main("I will not tell you about any of that!", "annoyed", "narrow", "angry", "mid")
    m "[cho_name], we need to find something we can use against him. To our advantage!"
    call cho_main("And you believe that that would help us win?", "open", "narrow", "angry", "mid")
    m "Precisely."
    call cho_main("(...)", "annoyed", "narrow", "angry", "R")
    call cho_main("Very well, [cho_genie_name]...", "open", "closed", "angry", "mid")
    call cho_main("I'll tell you what I know about him.", "open", "narrow", "base", "mid")
    call cho_main("Cedric was always a bit of a loner...", "annoyed", "narrow", "base", "R")
    call cho_main("He was cold. Focused. Never showed too much affection towards me. Except for--", "open", "base", "angry", "downR")
    call cho_main("(...)", "annoyed", "narrow", "base", "R")
    m "Yes? Go on..."
    call cho_main("I believe he had a bit of an obsession with my panties, Sir.", "soft", "narrow", "base", "mid")
    if not cho_quid.hufflepuff_prepared:
        m "A panties obsession? So so..."
    else:
        g9 "*Ha!* Called it!"
    call cho_main("It was almost creepy how often he tried to look up my skirt...", "angry", "wide", "base", "mid")
    call cho_main("I mean who would do such a thing?", "soft", "base", "base", "mid")
    m "Yes, yes... how terrible of him..."

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            call bld
            g9 "Please tell me more about your panties!"

        "-Participate in the conversation-":
            $ masturbating = False
            m "(No, I need to focus!)"
            m "(This might be useful information in our game against him...)"
            m "Please, carry on..."
            call cho_main("Of course, Sir.", "base", "base", "base", "mid")

    if masturbating:
        call cho_main("That's an oddly specific question, don't you think?", "soft", "base", "raised", "mid")
        g4 "Come on, girl! Which were the ones he liked the most?"
        call cho_main("*Uhm*...", "annoyed", "base", "base", "R")
        call cho_main("I never wore panties too often...", "angry", "narrow", "base", "downR")
        call cho_main("At least not those fancy ones the other girls are wearing.", "soft", "narrow", "base", "mid")
        g4 "*Argh*! {size=-4}(I'd love to see those!){/size}"
        call cho_main("If you can even call them that...", "annoyed", "narrow", "base", "R")
        call cho_main("Most of them look like shoelaces!", "annoyed", "narrow", "angry", "R")
        g4 "{size=-4}(What a bunch of sluts!){/size}"
        call nar("*Fap* *Fap* *Fap*...")
        call cho_main("You should see them, [cho_genie_name]!", "annoyed", "narrow", "angry", "mid")
        call cho_main("They're all a bunch of sluts!!!", "soft", "narrow", "angry", "mid")
        call cho_main("They wear their skirts so low -- you just have to wonder how they haven't fallen off yet...", "soft", "narrow", "base", "downR")
        g4 "{size=-4}(Indeed, I'd love to see that!){/size}"
        call cho_main("And pull their panty-string up and over their hip bones...", "soft", "narrow", "base", "mid")
        g4 "{size=-4}(Yes! So fucking slutty!){/size}"
        call cho_main("They look like arrows pointing down at their \"Snitch\", if you get what I mean...", "angry", "narrow", "angry", "mid")
        g4 "*Argh!* {size=-4}(Those cheap whores!){/size}"
        call cho_main("As if they give any boy an open invitation to lay with them...", "soft", "narrow", "angry", "R")
        g4 "*Fuck!* {size=-4}(That did it!!!){/size}"

        # Genie cums.
        call hide_characters
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call cho_main("As for me, panties have to be practical, first and foremost!", "soft", "closed", "base", "mid")
        g4 "*Ahg!* {size=-4}(So you can quickly get them off, you whore!){/size}"

        call cum_block
        call cho_main("And there needs to be enough fabric to soak up all the sweat...", "soft", "narrow", "base", "R")
        g4 "{size=-4}(I bet you are so wet right now too!){/size}"

        # Genie finished.
        call hide_characters
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        call cho_main("(...)", "annoyed", "narrow", "base", "mid")
        call cho_main("Sir, would it be alright if I head off now?", "soft", "base", "base", "R")
        g9 "Already? Do you have to be somewhere?"
        call cho_main("No?", "soft", "base", "base", "mid")
        g9 "Did our little talk about panties maybe... excite you?"
        call cho_main("What? No of course not!", "angry", "wide", "base", "mid")

        if daytime:
            call cho_main("I simply have to go to my next lesson...", "soft", "closed", "base", "mid")
            call cho_main("Or I will be late again.", "annoyed", "base", "base", "R")
        else:
            call cho_main("But if you expect me to do well during our next Hufflepuff game, then I'll require some sleep...", "soft", "base", "base", "R")

        m "Of course. You may go..."
        call cho_main("Thank you, Sir.", "base", "base", "base", "mid")
        call cho_main("Until next time.", "smile", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        call bld
        g9 "Sweet little wank I had there."
        m "(...)"
        m "I hope she'll show me her panties as well eventually..."
        g9 "Would love to see them!"

        jump end_cho_talk_event

    else:
        call cho_main("He'd always walk behind me when we went up the stairs, to get a better view I bet...", "soft", "narrow", "angry", "R")
        m "Did you ever show them to him?"
        call cho_main("My panties?", "soft", "base", "raised", "mid")
        m "No, your good manners...{w} Yes your panties!"
        call cho_main("Why would I have wanted to?", "soft", "narrow", "raised", "mid")
        m "What kind of girl doesn't show her panties to her beloved?"
        call cho_main("I beg your pardon?!", "angry", "wide", "raised", "mid")

        if not cho_quid.hufflepuff_prepared:
            m "But, that made me think..."
            m "If he's as obsessed with panties as you say, why don't we use that information to our advantage?"
            call cho_main("Like how?", "soft", "narrow", "raised", "mid")
            m "We use them as a distraction!"
            m "Now we only have to find out how to show them off properly during the game."
            call cho_main("I have to say I don't like this notion one bit.", "annoyed", "narrow", "base", "mid")
            call cho_main("But it might be worth a try...", "soft", "narrow", "base", "R")
        else:
            m "Well, it worked."
            m "Beating him at {i}Quayditch{/i} was almost too easy!"
            call cho_main("Quidditch, Sir...", "soft", "closed", "base", "mid")
            m "All we had to do was put some good-old panties in front of his face..."
            call cho_main("", "annoyed", "narrow", "base", "mid")
            g4 "And he was like a wild goat chasing after them!"
            call cho_main("A goat?", "soft", "narrow", "raised", "mid")
            m "Yes. Don't you have those here?"
            call cho_main("Goats don't chase after panties, Sir...", "soft", "narrow", "base", "R")
            m "They do where I'm from..."
            call cho_main("(...)", "annoyed", "narrow", "angry", "R")
            call cho_main("But you were correct with your assumption, Sir.", "soft", "closed", "base", "mid")
            call cho_main("I'm surprised how well that worked out in our favour.", "annoyed", "base", "raised", "down")
            call cho_main("He really {b}does{/b} love panties...", "soft", "narrow", "base", "mid")
            m "I mean who doesn't..."

        call cho_main("Sir, if you don't mind...", "soft", "closed", "base", "mid")
        if daytime:
            call cho_main("I'm already late for classes.", "soft", "narrow", "base", "R")
            call cho_main("I really should be going now...", "angry", "narrow", "worried", "mid")
        else:
            call cho_main("It's getting late.", "soft", "narrow", "base", "mid")
            call cho_main("I really should head to bed now...", "angry", "narrow", "worried", "mid")

        m "Of course. You are dismissed."
        call cho_main("Thank you, Sir.", "base", "base", "base", "mid")
        if daytime:
            call cho_main("Until next time.", "smile", "narrow", "base", "mid")
        else:
            call cho_main("Have a good night.", "smile", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        call bld
        m "I wonder what colours they are..."
        m "Or if she's even wearing any.{w} You never know..."

        jump end_cho_talk_event

### Tier 2 (pre Slytherin) ###

label cc_pf_talk_T2_intro_E1:
    m "Miss Chang, it's time we have another chat."
    m "Please come a bit closer..."
    call cho_main("Yes, Sir.", "base", "base", "base", "mid")

    call play_music("cho")
    call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    m "Tell me, how have you been?"
    g9 "I bet a lot has changed for you after your big win!"
    call cho_main("More or less...", "soft", "base", "raised", "mid")
    call cho_main("School has been rather uneventful the past couple of days.", "soft", "base", "base", "R")
    call cho_main("That is, if constantly getting bullied is the new norm at this school...", "annoyed", "narrow", "angry", "mid")
    m "Bullied by whom?"
    call cho_main("The Slytherin Quidditch team!{w=0.6} They've been total dicks lately...", "open", "narrow", "angry", "mid")
    m "You don't say.{w=0.8} Why is that?"
    call cho_main("Because they are scared of us, I wager...", "soft", "narrow", "angry", "downR")

    call cho_main("We'll be playing against them next.", "annoyed", "narrow", "base", "R")
    call cho_main("And of course they have to behave like the absolute worst!", "soft", "narrow", "angry", "mid")
    call cho_main("They deserve to be publicly disgraced in front of the whole school!{w=0.8} The whole lot of them!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("I'll make sure of it, [cho_genie_name]!{w=0.6} The Slytherin team will lose!", "mad", "narrow", "angry", "mid")
    g9 "(And I'll win my bet with Snape even sooner! Sweet!)"
    m "Anything you can tell me about them?{w=0.6} Are they better than Hufflepuff?"
    call cho_main("They are, by quite a bit.", "annoyed", "base", "base", "mid")
    call cho_main("However, Hufflepuff only had one really good player. Which was Cedric.", "soft", "base", "base", "R")
    call cho_main("Slytherin on the other hand, they are almost unbeatable!", "angry", "wide", "base", "mid")
    call cho_main("They might even be better than Gryffindor...", "annoyed", "base", "base", "up")
    m "You don't say. So why are they next and not Gryffindor?"
    call cho_main("Because of their seeker, Sir.", "soft", "narrow", "base", "mid")
    call cho_main("He's so...{w=0.6} so bad!", "clench", "narrow", "base", "R", cheeks="blush")
    m "Who is?"
    call cho_main("Draco Malfoy, Sir.", "open", "closed", "base", "mid")
    m "(The cocky fella! Snape mentioned him before...)"
    call cho_main("They've been continuously harassing my team...", "annoyed", "narrow", "angry", "R")
    call cho_main("Well, mostly me actually.", "angry", "narrow", "base", "downR") # Embarrassed

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            show screen blktone5 # Gets removed by `call nar()`
            show screen bld1
            with d3
            m "(Just to make this clear, I'm not getting off because I like the thought that she's getting bullied...)"
            call nar(">Right...")
            g4 "I hope you fought back those bullies?"
            call cho_main("Of course, [cho_genie_name]!", "base", "base", "base", "mid")

        "-Participate in the conversation-":
            $ masturbating = False
            m "(No, I need to focus!)"
            m "So... would you like to report them?"
            call cho_main("No, Sir.", "soft", "closed", "base", "mid")
            m "No?"

    call cho_main("I do not endorse their behaviour, Sir.{w=0.6} And I hope no other student has to share the same harassment that I received.", "soft", "narrow", "angry", "mid")
    call cho_main("{size=-4}Unless maybe Granger...{/size}", "annoyed", "narrow", "angry", "R") # Small text.
    call cho_main("But{w=0.3}, watching them succumb to me has been rather fun...", "base", "narrow", "angry", "mid")
    m "Succumb to you?"
    call cho_main("Yes.{w=0.3} They're so desperately trying to embarrass me.{w=0.6} To make me doubt myself before the big game...", "smile", "narrow", "angry", "mid")

    if masturbating:
        g4 "Those asshole bullies...{w=0.6} Show them who's boss!"
    else:
        g9 "And a strong, independent woman like yourself would never be intimidated by puny Slytherins!"
        call cho_main("Of course not, Sir.", "soft", "closed", "base", "mid")
        g4 "I'm so proud!"

    call cho_main("After all I'm only a small, helpless girl{w=0.6}, and they are a group of strong, ruthless alpha males!", "soft", "base", "worried", "R", cheeks="blush")
    call cho_main("Their attempts are pathetic!", "angry", "narrow", "angry", "mid")
    call cho_main("They are pathetic!!!", "clench", "narrow", "angry", "mid", trans=hpunch)
    call cho_main("Trying to lift my skirt with first-year spells...", "soft", "narrow", "angry", "R")
    call cho_main("Stealing my underwear while I'm taking a shower after practice...", "angry", "narrow", "angry", "downR")
    if masturbating:
        g4 "*Argh!* {size=-4}(Dirty panty muggers!){/size}"
    call cho_main("They even had the audaciousness to write \"Cho, the Ravenclaw ho\" on the blackboard during divination class.", "open", "narrow", "angry", "mid")
    if masturbating:
        g4 "{size=-4}(They must have seen your future, you whore!){/size}"
    call cho_main("Half the class saw it before I could get there...{w=0.8} Not that I care much about it...", "annoyed", "narrow", "base", "downR", cheeks="blush")
    call cho_main("If I'm honest, I'm surprised they could even spell my name correctly...", "soft", "narrow", "angry", "mid")
    if masturbating:
        call nar("*Fap* *Fap* *Fap*...")
    call cho_main("They think they can intimidate me. But that's where they are mistaken!", "angry", "narrow", "angry", "down")

    if masturbating:
        call cho_main("They should be scared of me, [cho_genie_name]!", "soft", "narrow", "angry", "mid")
        g4 "{size=-4}(Yes! Show them, you slut!){/size}"
        call cho_main("Of what {b}I'm{/b} capable of!", "clench", "base", "angry", "mid")
        g4 "*Argh*! (I'm getting close!)"
        call cho_main("Scared of what's about to come!", "soft", "narrow", "angry", "mid")

        # Genie cums.
        g4 "{size=-4}(Yes! Yes!{w=0.6} It's coming!){/size}"
        call hide_characters
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call bld
        g4 "*Argh*! {size=-4}(Take it!){/size}"

        call cum_block
        g4 "*Panting* {size=-4}(You fucking slut!){/size}"

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        call cho_main("", "annoyed", "narrow", "base", "mid")
        m "(*Phewwww*...)"
        m "(That was nice.)"
        call cho_main("Are you feeling well, Sir?", "open", "narrow", "raised", "mid")
        g9 "Never felt better!"
        call cho_main("That's good to hear.", "smile", "base", "base", "mid")

    m "I'm glad you aren't letting yourself get oppressed by those Slytherins."
    call cho_main("Not in a million years!", "base", "narrow", "base", "mid")
    m "Admirable."

    m "Anything else you could tell me about their team?{w=0.6} Anything that could help us?"
    m "Did you maybe fool around with their seeker as well?"
    call cho_main("Malfoy?", "soft", "wide", "base", "mid") # Shocked
    call cho_main("*Tzzzz*!{w=0.3} I'd never surround myself with that Slytherin scum!", "angry", "closed", "angry", "mid")
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "I guess you and Granger have at least some things in common..."
    call cho_main("His {b}daddy{/b} bought their whole team new brooms, which is the only reason they've even let him in.", "soft", "narrow", "raised", "mid")
    m "His \"daddy?\""
    call cho_main("His father, Sir.", "soft", "closed", "angry", "mid")
    m "Oh. I thought you might be talking about a different \"daddy.\""
    call cho_main("Very funny, [cho_genie_name]...", "annoyed", "narrow", "angry", "R")
    call cho_main("If you don't mind, Sir.", "soft", "closed", "base", "mid")

    if daytime:
        call cho_main("Classes are about to start, and I'm already late for them...", "open", "narrow", "base", "R")
        call cho_main("I hope it would be okay if I leave?", "soft", "narrow", "base", "mid")
    else:
        call cho_main("It's getting late and I have to go and get some sleep...", "open", "narrow", "base", "R")
        call cho_main("I hope you don't mind, Sir?", "soft", "narrow", "base", "mid")

    m "Not at all. You may go now."
    call cho_main("Thank you, Sir.", "smile", "base", "base", "mid")
    call cho_main("Until next time...", "base", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_talk_event

label cc_pf_talk_T2_intro_E2:
    m "Would you mind if we had another chat?"
    call cho_main("Of course not, [cho_genie_name]!", "smile", "base", "base", "mid")
    m "Come closer then..."

    call play_music("cho")
    call cho_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    m "How's school? Have anything to tell me?"
    call cho_main("Quite a bit, Sir!", "smile", "happyCl", "base", "mid")
    call cho_main("I feel like people have shown me more affection ever since our game against Hufflepuff.", "base", "base", "base", "mid")
    m "You don't say..."

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            call cho_main("", "soft", "base", "base", "up")
            g4 "*Agh*! Go on!"
            call cho_main("What?", "soft", "narrow", "raised", "mid")
            call cho_main("Oh, I'm sorry, Sir.{w=0.6} Of course!", "soft", "wide", "base", "mid")
            call cho_main("I had my head in the clouds there for a second.", "smile", "happyCl", "base", "mid")

        "-Participate in the conversation-":
            $ masturbating = False
            m "Do you have any idea why that might be?"
            call cho_main("Because of our win, why else!", "smile", "narrow", "base", "mid")
            m "And it had nothing to do with the fact that half the school got to see your panties?"
            call cho_main("No! Of course not!", "soft", "narrow", "angry", "mid")
            call cho_main("Please don't try to diminish my achievement, Sir!", "annoyed", "narrow", "base", "R")

    call cho_main("It's like I'm a celebrity now!{w=0.6} I'm getting so much attention!", "soft", "base", "base", "R")
    call cho_main("It never happened that Ravenclaw won a game.{w=0.6} And I made that possible!", "smile", "base", "base", "mid")
    if masturbating:
        g4 "{size=-4}And soon you'll be on your knees thanking me for it!{/size}"
    else:
        m "Hey! Don't you forget about me!"
        m "Where would you be without the great {i}Dooblydore{/i}..."
        call cho_main("Of course, Sir!", "clench", "happyCl", "worried", "mid", cheeks="blush")
        call cho_main("Sorry, Sir!", "soft", "narrow", "worried", "mid", cheeks="blush")

        menu:
            m "(Maybe it wouldn't be such a bad idea to...)"
            "-Jerk off while she's talking-":
                $ cho_jerk_off_counter += 1
                $ masturbating = True

                hide screen cho_main
                call nar(">You reach under the desk and grab your cock...")

                call gen_chibi("jerk_off_behind_desk")
                with d3
                pause .8

                call bld
                m "Please, don't let me interrupt your thought..."
                g9 "I'd like to hear more!"

            "-Participate in the conversation-":
                $ masturbating = False
                m "(No, I need to focus!)"
                m "Please, don't let me interrupt your thought..."
                m "Continue..."

        call cho_main("Of course, Sir.", "base", "base", "base", "mid")

    call cho_main("It's fun receiving all of the boys attention!{w=0.8} And seeing how jealous it makes all of the girls!", "soft", "base", "base", "mid")
    call cho_main("Especially Granger!", "smile", "narrow", "base", "mid")
    if masturbating:
        g4 "{size=-4}Yes, the Gryffindor whore!{/size}"
    call cho_main("You should have seen her face, [cho_genie_name]!", "soft", "narrow", "angry", "mid")
    call cho_main("She's so angry at me! I love it!", "smile", "happyCl", "base", "mid")
    call cho_main("She can't even bear to look at me anymore.", "grin", "narrow", "angry", "mid")
    call cho_main("You should know, for whatever reason, almost all of Hufflepuff blames her for helping Ravenclaw secure the win!", "soft", "base", "base", "R")
    call cho_main("She announced several times that Hufflepuff was leading in points, when they actually weren't!", "smile", "narrow", "angry", "mid")
    call cho_main("Which resulted in Hufflepuff playing far more defensively, when they should have been aggressive!", "base", "narrow", "base", "mid")
    if masturbating:
        g4 "{size=-4}Oh you are one of those girls! I like going aggressive!{/size}"
    call cho_main("I caught the Snitch at just the right time!{w=0.6} If Hufflepuff had gone too far in the lead, we would have lost!", "open", "narrow", "angry", "mid")
    call cho_main("I really need to thank Granger the next time I see her.{w=0.6} I owe her a great deal...", "soft", "narrow", "angry", "R")
    if masturbating:
        g4 "{size=-2}I'd love to watch you \"thank her!\"{/size}"
        call cho_main("Maybe I'll do something fun with her the next time I see her...", "base", "narrow", "base", "R")
        call cho_main("Do something that would rile her up even more!", "smile", "narrow", "angry", "downR")
    else:
        g9 "Yes? And how exactly would you \"thank her?\""
        call cho_main("I don't know. Maybe something that would rile her up even more...", "annoyed", "base", "base", "downR")
    call cho_main("Like a kiss on her cheek, or an uncomfortably long hug!", "soft", "narrow", "base", "mid")
    call cho_main("Or I'll do something more sinister! Something she'd never expect!", "base", "base", "base", "R")
    if masturbating:
        g4 "*Ugh*! {size=-2}Like what?{/size}"
    else:
        m "More sinister? Like what?"
    call cho_main("Give her a proper kiss on the lips, perhaps?", "soft", "narrow", "angry", "mid")
    with hpunch
    g4 "!!!"
    call cho_main("Yes! I bet a prude like her would be {b}so{/b} shocked by that!{w=0.8} I might even be her first!", "soft", "base", "angry", "downR", cheeks="blush")

    # Forced to jerk off.
    if masturbating:
        g4 "{size=-4}Yes! You fucking sluts!{/size}"
    else:
        g4 "(Fuck it, this is too much!)"

        menu:
            "-Flog the dong-":
                pass
            "-Practice Onanism-":
                pass
            "-Diddle do-":
                pass

        $ cho_jerk_off_counter += 1
        $ masturbating = True

        hide screen cho_main
        call nar(">You reach under the desk and grab your cock...")

        call gen_chibi("jerk_off_behind_desk")
        with d3
        pause .8

        call bld
        g4 "Please, continue!"

    call cho_main("Just thinking about her puffy pink lips...", "annoyed", "narrow", "angry", "down", cheeks="blush")
    g4 "{size=-2}Yes! Yes!{/size}"
    call cho_main("I should make her choke on my tongue, whether she likes it or not...", "clench", "narrow", "angry", "downR")
    g4 "{size=-2}Yes! That would be so fucking hot!{/size}"
    call cho_main("Push her against a wall and force it into her bitch mouth!", "angry", "narrow", "angry", "down")
    g4 "*Argh!* {size=-2}You fucking sluts!{/size}"
    call cho_main("And then I pull her vest over her stupidly large breasts...", "smile", "narrow", "angry", "L")
    call cho_main("And embarrass her in front of the whole class!", "soft", "base", "base", "up")
    call cho_main("Show everyone her ridiculous {b}cow tits!{/b}", "soft", "narrow", "angry", "up")
    g4 "{size=-2}Yes!!!{/size} {size=-4}(I'm almost there!){/size}"
    call cho_main("She deserves it...", "angry", "closed", "angry", "R", cheeks="blush")
    call cho_main("That know-it-all, pretentious little bitch!", "soft", "narrow", "angry", "downR", cheeks="blush")

    # Genie cums.
    g4 "{size=-2}Yes, yes! You nasty slut!{/size}"
    call hide_characters
    hide screen bld1
    with d3

    call cum_block
    call gen_chibi("cum_behind_desk")
    with d3
    pause .8

    call bld
    g4 "*Argh*! {size=-4}Take it!{/size}"
    call cho_main("Oh, I'm so sorry, Sir.", "soft", "narrow", "base", "mid")
    call cho_main("I forgot I was talking to you for a second!", "angry", "closed", "worried", "mid")

    call cum_block
    g4 "*Argh* {size=-4}You lesbian slut!{/size}"
    call cho_main("I hope you didn't hear any of it! I would never do--", "soft", "narrow", "worried", "mid")

    call cum_block
    call cho_main("Sir?!", "annoyed", "narrow", "raised", "mid")
    call cum_block
    pause .8

    call cho_main("[cho_genie_name]! What the bloody hell are you doing?!", "angry", "wide", "base", "mid", cheeks="heavy_blush", trans=hpunch)
    m "{size=-4}(Oh no!){/size}"
    g4 "{size=-4}(I'm busted!){/size}"

    # Genie stops.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call gen_chibi("cum_behind_desk_done")
    pause .8

    call cho_main("", "clench", "wide", "base", "mid", cheeks="blush")
    g4 "Nothing, I was just--"
    call cho_main("Don't tell me you were...", "disgust", "happyCl", "worried", "mid", cheeks="heavy_blush")
    g4 "I was merely scratching my leg!"
    call cho_main("Don't lie to me, [cho_genie_name]!{w=0.6} I know exactly what you were doing!", "clench", "narrow", "angry", "mid")
    call cho_main("{size=+4}You were touching yourself!{/size}", "scream", "closed", "angry", "mid", trans=hpunch) # Scream
    call cho_main("", "angry", "narrow", "angry", "mid")
    g4 "{size=-2}Not so loud! People might hear you!{/size}"
    call cho_main("Why would you think I care?!", "open", "narrow", "angry", "L", cheeks="blush")
    call cho_main("You were wanking off!", "soft", "wide", "base", "mid", cheeks="blush")
    m "No I wasn't..."
    call cho_main("In front of your own student!", "disgust", "happyCl", "worried", "down", cheeks="heavy_blush")
    m "(...)"
    m "Stop making a big deal out of it, would you?"
    call cho_main("So you're admitting that you did it!", "angry", "narrow", "angry", "mid")
    m "Fine... I don't care at this point..."
    call cho_main("That's disgusting!", "soft", "narrow", "base", "mid")
    m "You're making an even bigger fuzz about it than Hermione..."
    call cho_main("Good for her!", "angry", "closed", "angry", "mid")
    call cho_main("Maybe you should call her up here to clean up your mess as well!", "soft", "narrow", "base", "mid")
    call cho_main("And lick it all up!{w} I bet she'd love that!!!", "angry", "narrow", "angry", "mid")
    m "(...)"
    call cho_main("I'm leaving.", "disgust", "happyCl", "worried", "mid", cheeks="blush")
    call cho_main("Have a nice day, [cho_genie_name]!", "soft", "narrow", "angry", "mid", cheeks="blush")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(I really did make a mess...)"
    m "(Maybe I {b}should{/b} get Hermione to clean it up for me?)"
    g9 "(With her mouth!)"
    m "(..........)"
    m "(Aaaaaaand I'm hard again...{w} Maybe some other time...)"

    $ cho_mood += 9

    jump end_cho_talk_event


label cc_pf_talk_T2_E3:

    call play_music("cho")
    call cho_main("", "annoyed", face="neutral", xpos="mid", ypos="base", trans=fade)
    pause .5

    g9 "[cho_name], how is school life?"
    m "I need to stay \"on top\" of all the latest \"hot goss\"..."
    call cho_main("Sir, I don't tend to pay attention to that sort of stuff.", "soft", "closed", "base", "mid")
    m "You must at least have heard something raunchy here at the school?"
    call cho_main("*Uhm*...{w} well...", "annoyed", "base", "base", "R")

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            call cho_main("", "base", "base", "base", "mid")
            m "You don't mind if I..."
            call cho_main("Mind what?!", "soft", "base", "raised", "mid")
            call cho_main("!!!", "upset", "wide", "base", "mid", cheeks="blush") # Shocked
            m "I have needs, girl."
            call cho_main("Gross!!!", "angry", "closed", "angry", "mid")
            call cho_main("[cho_genie_name], might I suggest that you sort out those needs on your own then?", "soft", "narrow", "angry", "R")
            call cho_main("Without me...", "soft", "narrow", "angry", "mid")
            m "What a Bummer...{w=0.6} Last time you were such a great aid..."
            call cho_main("What?! When did I ever help you with that?", "soft", "wide", "base", "mid")
            g9 "When you told me about that little fantasy you had with Granger!"
            call cho_main("You shouldn't have paid attention to any of that!", "mad", "happyCl", "worried", "mid", cheeks="blush")
            g9 "But I did!"
            m "I could just tell Hermione that you're into her, you know..."
            call cho_main("I am so not into her!", "clench", "narrow", "angry", "mid", cheeks="blush")
            call cho_main("(...)", "annoyed", "narrow", "angry", "R", cheeks="heavy_blush") # Embarrassed
            g9 "Yes you are! Don't you dare lie to me...{w=0.6} Or yourself for that matter."
            call cho_main("(...)", "annoyed", "narrow", "angry", "downR", cheeks="blush")
            m "So...{w=0.3} Will you honour the deal and aid me or what?"
            call cho_main("Fine...{w=0.3} If you can't help yourself.", "soft", "narrow", "angry", "mid")
            g9 "Great!{w=0.3} Pretend like I'm not even there!"
            call cho_main("I more likely will be pretending that {b}I'm{/b} not here...", "soft", "narrow", "angry", "downR", cheeks="blush") # Small text

        "-Participate in the conversation-":
            $ masturbating = False
            m "(Seems like I'm not feeling the need to jack off today...)"
            m "(Might as well pay attention for once.)"
            m "Very well then..."

    m "Why don't you tell me some more about..."
    call cho_main("The Slytherins? Gladly!", "open", "narrow", "angry", "mid")
    m "(I was going to say Hermione but sure...)"

    # Malfoy
    call cho_main("It was only yesterday that I had that stinking Malfoy boy snickering behind my back as I walked past him.", "open", "narrow", "angry", "R")
    if masturbating:
        call cho_main("I can only imagine the things that were on his mind...", "annoyed", "narrow", "angry", "downR")
    else:
        m "Yeah? Like what?"
        call cho_main("It's obvious if you ask me, Sir.", "open", "closed", "base", "mid")
        call cho_main("After all, he's just like any boy at this school...{w=0.6} They are all pervs.", "annoyed", "narrow", "angry", "mid")
    call cho_main("He even had the audaciousness to whistle at me, in front of everybody!", "soft", "narrow", "base", "mid")
    call cho_main("And shout about what a \"great arse\" I have, and that he couldn't wait to \"beat it!\"", "soft", "narrow", "angry", "mid")
    if masturbating:
        g4 "Great minds...{w=0.2} *Argh!* think alike!"
    else:
        g9 "Seems to me like he enjoyed the view!"
    call cho_main("Next time he does it I'll turn him into a filthy ferret, I swear!", "clench", "narrow", "angry", "down")
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    if masturbating:
        g4 "{size=-4}(You can do whatever you want with me too, if that's what turns you on baby!){/size}"
        g4 "{size=-4}(I'd love to be your little pet ferret!){/size}"
    else:
        m "Your ass is a real head turner, isn't it?"
        call cho_main("To be frank with you, Sir...{w=0.6} I would be disappointed if it wasn't.", "base", "narrow", "base", "mid")
        m "Why don't you tease him a bit more then? Get him hooked on it..."
        m "It would be to our benefit, don't you think?"
        call cho_main("*Hmm*{w=0.3} Yes I could give him a peak once or twice.", "annoyed", "base", "base", "R")
        call cho_main("For as long as I don't have to let him touch it.", "soft", "narrow", "angry", "mid")
        m "..."
        m "Anything else you could tell me?"

    # Crabbe & Goyle
    if masturbating:
        call cho_main("Then there are the two Slytherin beaters, Crabbe and Goyle...", "soft", "narrow", "base", "mid")
    else:
        call cho_main("Well, there are also the Slytherin beaters, Crabbe and Goyle...", "soft", "narrow", "base", "mid")
    call cho_main("Malfoy's extraordinarily dense thugs...", "angry", "closed", "angry", "mid")
    call cho_main("They've been strutting around school with their two bats...", "soft", "narrow", "angry", "mid")
    call cho_main("Hitting any girl's bum that happens to be in their reach...", "annoyed", "narrow", "angry", "R")

    if masturbating:
        call cho_main("It's like they use them as target practice.", "soft", "narrow", "angry", "mid")
        g4 "*Argh*! {size=-4}(How nasty!){/size}"
        call cho_main("I dare them to try it on me, those bastards!", "clench", "narrow", "angry", "R")
        g4 "*Yes*! {size=-4}(You deserve a good spanking!){/size}"
        call cho_main("I saw them go after Katie Bell today.", "soft", "narrow", "base", "mid")
        call cho_main("She was carrying a whole bunch of books...{w=0.8} so she couldn't simply run off or drop them.", "open", "narrow", "angry", "mid")
        call cho_main("She would have probably beaten them up immediately if that wasn't the case. Those cowards...", "angry", "narrow", "angry", "mid")
        g4 "*Yes*! {size=-4}(I wouldn't mind borrowing one of those bats!){/size}"
        call cho_main("They really did her dirty, Sir.{w} Even pulled down her skirt before they ran off!", "annoyed", "narrow", "base", "mid")
        g4 "What a bunch of daredevils!"
        call cho_main("Her bum was so red afterwards...{w=0.6} It was hard not to look at it...", "soft", "narrow", "base", "down", cheeks="blush")
        g4 "Fuck yeah! (You'd love to bury your face in some girl's ass, don't you?!)"
        call cho_main("She really does have a cute bum...", "horny", "narrow", "base", "downR", cheeks="heavy_blush")
        g4 "But not as cute as Granger's, right?"
    else:
        call cho_main("They aren't even allowed to make use of any Quidditch equipment outside the Quidditch pitch area!", "soft", "narrow", "angry", "R")
        m "Aren't you a bit too harsh on them?"
        call cho_main("Sir, since when is sexual harassment tolerated at this school?", "angry", "closed", "angry", "mid")
        m "I bet there are many girls that enjoy the occasional spanking..."
        call cho_main("What?", "soft", "wide", "base", "mid")
        m "Next time you should ask one of those girls..."
        call cho_main("Why would anyone enjoy that?{w=0.6} How ridiculous.", "soft", "narrow", "angry", "mid")
        m "They might just be too embarrassed to admit it..."
        call cho_main("", "annoyed", "narrow", "base", "mid")
        m "I'm sure miss Granger wouldn't be afraid to admit it, don't you think?"

    call cho_main("Granger?", "annoyed", "narrow", "angry", "R")
    call cho_main("Don't even talk to me about her...", "annoyed", "narrow", "angry", "mid")
    call cho_main("She's a hypocrite and a slut...", "soft", "closed", "base", "mid")
    call cho_main("And I hate her...", "soft", "narrow", "angry", "mid")
    call cho_main("If you could make her die of embarrassment, I'd be more than thankful for it...", "annoyed", "narrow", "angry", "mid")
    g9 "Embarrass her?{w=0.3} How?"
    g9 "Share some of your ideas with me! I'd love to hear them!"
    call cho_main("Very well...", "soft", "closed", "base", "mid")
    call cho_main("(...)", "annoyed", "base", "base", "R") # Thinks
    call cho_main("(...................)", "annoyed", "narrow", "angry", "R") # Thinks harder
    if masturbating:
        g4 "Please?!"
    else:
        m "Anything?"
    call cho_main("Oh, I know!", "smile", "wide", "base", "mid")
    call cho_main("Strip her down, and put her in a pillory!{w=0.8} -- In the middle of the Quidditch pitch!", "smile", "narrow", "angry", "mid")
    g9 "Kinky! I like it!"
    call cho_main("And let the entire school watch her as she's getting pounded by a horde of centaurs!!!", "mad", "narrow", "angry", "mid")

    if masturbating:
        g4 "*Argh!*{w=0.3} {size=-4}(What the hell?){/size}"
        call cho_main("While there are bludgers flying around -- hitting her disgusting udders...", "soft", "narrow", "angry", "mid")
        g4 "{size=-4}(That sounds really painful!){/size}"
        call nar("*Fap* *Fap* *Fap*!")
        call cho_main("Maybe another centaur takes her from the front...", "open", "narrow", "angry", "R")
        g4 "*Agh*!{w=0.3} {size=-4}(I won't last long if she continues like this!){/size}"
        call cho_main("And once those two are done breeding her, they trade places with another batch.", "clench", "narrow", "angry", "R")
        g4 "*Ahh* {size=-4}(This is getting too crazy!){/size}"
        call cho_main("Or even better, let some trolls have their way with her!{w=0.8} Let them rip her apart!", "clench", "base", "angry", "downR")
        g4 "*Fuck!* {size=-4}(Come on! Unload! Before it's too late!!!){/size}"

        # Genie cums.
        call hide_characters
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call bld
        g4 "{size=-4}(Yes! Here it comes!){/size}"

        call cum_block
        g4 "*Agh*! {size=-4}(Here comes another!){/size}"

        call cum_block
        m "*Phew*... {size=-4}(That was close!){/size}"

        # Genie stops.
        hide screen bld1
        with d3
        pause .2

        call gen_chibi("cum_behind_desk_done")
        pause .8

        call cho_main("And put a large bucket under her, so when they--", "soft", "closed", "base", "mid")
        g4 "Stop! No more!"
        call cho_main("", "annoyed", "base", "base", "mid")
        g4 "I've heard enough!"
        call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
        g4 "That was...{w=0.3} Very good."
        call cho_main("Are we done here, Sir?", "soft", "narrow", "angry", "mid")

    else:
        m "(...)"
        call cho_main("While there are bludgers flying around, hitting her disgusting udders...", "soft", "narrow", "angry", "downR")
        m "*Uhm*..."
        call cho_main("What?!", "angry", "narrow", "angry", "mid", trans=hpunch) # Angry
        m "Don't you think that's a bit extreme?"
        call cho_main("Why? For putting Granger in her natural habitat?", "annoyed", "narrow", "angry", "mid")
        call cho_main("Enclosed on a vast grassy field...", "soft", "closed", "base", "mid")
        call cho_main("Getting bred by a horde of bulls!", "soft", "narrow", "base", "mid")
        call cho_main("A cow like her would love it...", "annoyed", "narrow", "base", "downR", cheeks="blush")
        m "You seem very interested in the thought of it."
        g9 "From my perspective -- it appears that the worse you talk about her -- the more attracted to her you truly are!"
        call cho_main("Rubbish...", "soft", "narrow", "base", "mid", cheeks="blush")
        g9 "Girl, you are in denial!"
        call cho_main("I am not!", "clench", "closed", "angry", "mid", cheeks="blush")
        call cho_main("Sir are we done here?", "soft", "narrow", "angry", "mid")

    if daytime:
        call cho_main("I'm late for classes.", "soft", "narrow", "angry", "R")
    else:
        call cho_main("I need to get some sleep.", "soft", "narrow", "angry", "R")

    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "*Uhm*... Sure..."
    m "I suppose we can wrap things up here."
    m "You are dismissed..."
    call cho_main("Thank you, Sir.", "soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(Well that was weird.)"
    m "(That girl has a very wild imagination, I got to say...)"
    m "(Although I have to admit, I'm a bit of a fanboy now...)"
    g4 "Go! Go! Ravenclaw!"

    jump end_cho_talk_event
