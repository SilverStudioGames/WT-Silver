
label luna_intro_E1:

    # Setup
    $ luna_name = "???"
    $ d_flag_01 = False
    $ d_flag_02 = None
    $ d_flag_03 = [False, False, False, False, False]

    pause .8
    $ renpy.sound.play("sounds/snore1.mp3")

    m "*Snore*{w=2.0}{nw}"
    m "Yes..."

    pause 1.0
    $ renpy.sound.play("sounds/snore3.mp3")

    m "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
    m "Let's weigh those melons then shall we..."

    pause 1.0
    $ renpy.sound.play("sounds/snore2.mp3")

    m "......{w=0.5}*Snore*{w=1.0}{nw}"
    g9 "Can't find the scales... will have to use my hands..."

    stop music fadeout 8.0

    call lun_walk(action="enter")
    call chibi_emote("thought", "luna")
    pause 1
    call chibi_emote("hide", "luna")
    call lun_walk("410", speed=0.7)
    call play_sound("kick")
    show screen gfx_effect(428, 365, img="smoke", zoom=0.25)
    with hpunch

    pause 0.5

    $ renpy.sound.play("sounds/MaleGasp.mp3")
    g4 "M-My cabbages!"
    m "..............."
    m "...Hello?"

    lun "*Mmh*"

    m "What the hell are you doing in my office?"
    lun "I can't find them, daddy..."
    g4 "Daddy?"
    lun "My glasses..."
    m "You're...{w=0.4} looking for your glasses?"
    m "Why would your glasses be in here?"
    m "Hold on..."

    call play_music("luna")

    show screen chair_left
    show screen desk
    call gen_chibi("stand", 225, "base")
    with fade

    pause 1

    call gen_walk(path=[(230, 470), (440, 470), (450, 430)])
    call gen_chibi("stand", 450, "base", flip=False)
    with d3

    pause 0.5

    #Genie walks over behind Luna who doesn't turn around
    m "(Is this girl sleepwalking?)"
    g9 "Whoa, check out these melons!"
    g4 "(Shit.... I said that out loud.)"
    m "(Guess she really must be sleepwalking...)"
    m "(Although, maybe I could test it somehow just to be sure...)"

    menu:
        m "(What kind of {i}examination{/i} should I perform?)"
        "-Oral examination-":
            $ d_flag_01 = True
            m "So... What's your name?"
            lun "...Wrackspurts..."
            m "Charming..."
            m "(I suppose that is a plausible name in this world...)"
            $ luna_name = "Miss Backspurts?"

        "-Hands-on examination-":
            pause 0.5
            $ mouse_slap()
            lun "No!"
            g4 "..."
            lun "The Nargles..."
            m "The what now?"
            lun "*Inaudible mumbling*..."
            m "*Hmm*..."

        "-Shock therapy-":
            $ renpy.sound.play("sounds/zipper.mp3")
            call gen_chibi("dick_out", 450, "base", flip=False)
            with d3
            pause 0.5
            g9 "What do you think about this?"
            lun "...Crumple-Horned Snorkack..."
            m "...Well, that's just rude..."
            pause 0.5
            $ renpy.sound.play("sounds/zipper.mp3")
            call gen_chibi("stand", 450, "base", flip=False)
            with d3

    # Genie walks back to his chair and sits down
    m "(What a strange girl...)"
    m "(Although the crazies usually give the best blowjobs...)"
    m "(Well, now I'm hard...)"

    menu:
        "-Jerk off-":
            m "(Even after thousands of years, this is a new one even for me...)"

            $ renpy.sound.play("sounds/zipper.mp3")
            call gen_chibi("jerk_off", 450, "base", flip=False)
            with d3

            m "..."
            m "Hey, you could at least talk dirty or something."
            lun "I feel...{w} tingling..."
            g9 "Nice..."
            lun "Crawling on my skin..."

            $ renpy.sound.play("sounds/zipper.mp3")
            call gen_chibi("stand", 450, "base", flip=False)
            with d3

            g4 "..."
            m "(Yeah, this is not going to work...)"
            m "(Better let someone else deal with this one...)"

        "-Don't-":
            m "(This is so weird, she's just standing there...)"
            m "(I better get someone to deal with this...)"

    hide screen chair_left
    hide screen desk
    call gen_chibi("sit_behind_desk")
    with fade

    label luna_intro_E1.choices:

    menu:
        "-Summon Snape-" if not d_flag_03[0]:
            $ d_flag_02 = d_flag_02 or "snape"
            $ d_flag_03[0] = True
            "> You put your palms on your temples, attempting to summon Snape, but nothing happens." # X-Man reference
            m "*Hmm*... He must be dead..."
            g4 "Dead drunk..."

            jump .choices

        "-Summon Tonks-" if not d_flag_03[1]:
            $ d_flag_02 = d_flag_02 or "tonks"
            $ d_flag_03[1] = True
            "> You try to summon Tonks."
            pause 0.2
            $ renpy.sound.play("sounds/magic3.mp3")
            "> The spell fizzles."
            m "*Hmm*..."
            m "(Don't think that worked... Is she sleeping?)"

            jump .choices

        "-Summon Satan-" if not d_flag_03[2]:
            $ d_flag_02 = d_flag_02 or "satan"
            $ d_flag_03[2] = True

            m "I summon thee... Satan."
            pause 1
            m "*heh* I just as I exp--"
            $ renpy.play('sounds/attack_snape2.ogg')
            show pentogram onlayer screens at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
            with d5

            pause 0.5
            m "Uh-oh..."
            call blkfade
            hide pentogram onlayer screens
            centered "{size=+7}{color=#cbcbcb}20 minutes later...{/color}{/size}"

            g9 "*Ha-ha*... Good one! Alright, talk to you later Belzebub!"
            "Belzebub" "Ah, don't be so formal, just call me Bub."
            "Belzebub" "If you ever need some latest {i}hot{/i} news, I'm your guy."
            call give_reward("> Satan's phone number has been added to your contacts list.", "interface/icons/phone.webp")
            g9 "Thanks Bub, will do!"

            "Bub" "Take care!"
            $ renpy.play('sounds/attack_snape2.ogg')

            call hide_blkfade

            m "..."
            m "He's such a nice guy, I don't understand why people hate him so much."

            if d_flag_03[3]:
                m "(And he at least answered the call, unlike the guy upstairs...)"
                $ renpy.sound.play("sounds/thunder.ogg")
                with flash
                g4 "!!!"
                m "...Sorry."

            m "Anyway... What was I doing?"

            lun "*Snore*..."
            m "Right..."

            jump .choices

        "-Summon God-" if not d_flag_03[3]:
            $ d_flag_03[3] = True
            "> Nothing happened."
            m "Figures..."

            jump .choices

        "-Summon Hermione-":
            $ d_flag_02 = d_flag_02 or "hermione"
            pass

        "-Summon Jafar-" if not d_flag_03[4]:
            $ d_flag_03[4] = True
            g4 "Who the fuck made this an option?!"

            jump .choices

    call blkfade
    "> You summon Hermione to your office."
    call hide_blkfade

    call her_walk("mid", action="enter")

    m "Ah, Miss Granger..."
    her "[genie_name]... do you know what time it is--" #Eyes closed, looking tired
    her "Luna? what are you doing here?!?" #shocked

    if d_flag_01:
        m "(Didn't she say her name was backspurts or something?)"

    $ luna_name = "Miss Luna?"

    her "Don't tell me--"
    m "Quiet, girl."
    m "She's sleepwalking..."
    her "She's...{w=0.4} Oh, I see..."
    lun "So warm..."
    her "..." #weirded out
    m "Can you do something?"
    her "Do what exactly? I have heard you're not supposed to wake up someone that is sleepwalking..."
    m "Then just escort her back to her bed..."
    her "She's from Ravenclaw, I don't have access to their dormitory, so why me?"

    if d_flag_02 == "hermione":
        m "You were the obvious choice, Miss Granger."
    elif d_flag_02 == "satan":
        m "Nobody else seemed to be picking up my calls..."
        m "Well, except..."
        her "Except?"
        m "Satan."
        her "Satan...?"
        m "Never mind."
        her "..........."
    else:
        m "Nobody else seemed to be picking up my calls..."

    m "Anyway,{w=0.2} how am I supposed to know that she's a Ravenclaw?"
    m "She's not wearing her school uniform, is she?"
    her "I thought our headmaster was supposed to know all of our students..."
    m "Even my knowledge has its limits, dear child."
    her "Oh I know exactly what's occupying your mind." # Rolls eyes
    her "Anyhow, why didn't you escort her back yourself, professor?"


    menu:
        "\"I don't know where this Ravenglove dormitory is...\"":
            her "It's Ravenclaw, [genie_name]..."
            m "Tomato, tomatoe."
            her "Anyway, what do you mean you don't know where their dormitory is, that doesn't make sense."
            m "Girl, I'm starting to lose my patience..."
            m "Just get this weirdo out of here, will you?"
        "-Dismiss the question-":
            m "Just get this weirdo out of here, please."

    her "[genie_name]!" # Gasp
    lun "It tickles..."
    her "......" # Looks at Luna, puzzled.
    her "She...{w=0.4} She's not a weirdo... She's just a bit... Loony..."
    m "I don't care how you call it, just escort miss {i}Loony{/i} back to her bed...."
    her "I can't, I'm not allowed in their dormitory as I have already said..."
    g4 "Bloody hell, there's always {i}something{/i}..."

    if d_flag_02 == "tonks":
        # tonks enters (wearing something sexy)
        call ton_walk("mid", 460, action="enter")

        ton "*Yawn* Sorry I'm late, [ton_genie_name]."
        m "You took your damn time."
        ton "I was in the middle of... something important."
        m "Important, hmm..."
    else:
        her "I suggest you should summon a teacher to escort her back."
        m "Very well... I will summon--"
        her "Anyone but Snape!"
        lun "*wah* *wah*... *wah*."
        her "Shush! You're okay Luna, professor Snake is not allowed here."
        m "..."
        m "Fine. I'll just get Professor Tonks up here..."

        call blkfade
        nar "> You attempt to summon Tonks to your office."
        call hide_blkfade

        m "..."
        call ton_walk("mid", 460, action="enter")
        ton "You called..."

    her "Professor!" #Wide eyed
    ton "*Oooh* What's this? A slumber party?"
    g9 "It is now!"
    g9 "Let me search for my bathrobe real quick."
    her "Professor, that's not why we asked her here."
    m "Right... Tonks, we may require your assistance here..."
    ton "Assistance? With what--"
    lun "Wrackspurts!"
    ton "Ah... Miss Lovegood."

    if d_flag_01:
        g9 "Luna Love-good... *heh*, that's funny."
        ton "What's funny?"
        m "I said it out loud, didn't I..."
        m "Anyway--"

    $ luna_name = "Miss Lovegood"

    m "This so called Miss {i}Lovegood{/i} sleep-walked in here."
    ton "How am I not surprised."
    her "P-Professor, what are you wearing?!"
    g4 "Yes, Miss Tonks. What in the great desert sands are you wearing?"
    g9 "Is this a school or a brothel?"

    # Fun option
    menu:
        ton "It's my nightgown... You don't like it?" # Flirtatious

        "\"I love it!\"":
            g9 "You look like a slut!"

        "\"You look like a slut!\"":
            g9 "I love it!"

    her "Professor!"
    her "How could you say such a thing!"
    ton "Yes, what a rude thing to say to your staff. {heart}"
    m "I'm a man of simple truths, simply stating the obvious."
    ton "So my current attire is too slutty for you, huh?"
    g9 "I didn't say that, Miss Tonks..."
    g9 "I said you look like a slut. Big difference."
    her "What if a student would see you professor?! You can't walk around the castle wearing... this!"
    ton "Quit worrying. Nobody is going to see me this late at night..."
    ton "After all, it's already past curfew."
    ton "Students should be in their beds, including you, Miss Granger."
    her "But professor Dumbledore asked me to--"
    ton "You just head back to bed, and I'll make sure Miss Lovegood gets back safe and sound to her dormitory..."
    her "Okay..." #annoyed
    ton "Good girl."

    call her_walk("door")

    her "Good night then..." #annoyed, flipped
    ton "Sleep tight, Miss Granger..." # Tongue in cheek

    call her_walk(action="leave")

    # Tonks should maybe talk to Genie about the situation some more here.

    ton "Very well then..."
    ton "Come on, Miss Lovegood, let's get you back to bed..."

    #Tonks walks to the door

    lun "But I'm not tired mummy..."
    ton "..." #wide eyed
    m "What a weirdo..."
    ton "Just...{w=0.4} be a good girl and follow me back to bed..."
    lun "Yes, mummy..."

    call lun_walk("door")

    ton "Don't worry about her, she'll be fine."
    m "I won't."

    call ton_walk("door", action="leave")
    call lun_walk(action="leave")

    m "This place never ceases to amaze me..."
    m "..."
    m "At least that weirdo isn't my problem anymore..."
    m "Time to get back to sleep."

    jump day_start

label luna_intro_E2:
    #Next morning
    #Luna knocks on door

    stop music fadeout 1.0
    call play_sound("knocking")
    "*knock-knock-knock*"

    m "Who is it?"
    lun "Luna."
    m "Who?"
    lun "Luna Lovegood, Sir."
    m "Love... good?"
    lun "Yes!"
    m "(I don't remember ordering any foreign prostitutes...)"
    g9 "(Maybe Snape has finally sent one of his Slytherin whores.)"

    menu:
        "-Invite them in-":
            g9 "Enter!"

        "\"I'm busy!\"":
            m "Come back tomorrow."
            lun "Oh, okay."
            lun "I'll come back tomorrow then."

            jump main_room

    call lun_walk(action="enter")
    pause 0.5

    m "{size=-4}Oh... It's miss Loony.{/size}"
    call play_music("luna")
    #lun "Please don't call me that, Sir.."
    #m "My apologies, child."
    #m "Please come closer."

    call lun_walk("desk")

    call lun_main("", "base", "base", "base", "mid", trans=d3)
    pause 1

    g4 "(Look at the baby blues on that girl!)"
    g9 "(She looks even better awake!)"
    m "(I think I'm getting a boner...)"

    menu:
        "-Jerk off-":
            call gen_chibi("jerk_off_behind_desk")
            with d3
            "> You drop down your pants and start jerking off."
            $ masturbating = True

        "-Behave-":
            $ masturbating = False

    if masturbating:
        g9 "Miss *ah* Love-good... What can I do you for?"
    else:
        m "Miss Lovegood... What can I help you with?"

    lun "*Hmm*..."

    if masturbating:
        "> *fap-fap-fap*!"
        g4 "(Look at the breasts on this girl, such a lovely profile!)"
        g9 "(And that lush blonde hair! I'd love to wrap it around my dick!)"
    else:
        m "Miss Lovegood?"

    call lun_walk(600, 460)
    call lun_chibi(flip=True)
    ">Luna absent-mindedly starts looking around your room."

    if not masturbating:
        m "*Uhh* Hello?"

    call lun_walk("mid", "base")

    m "(What's wrong with this girl?)"

    if masturbating:
        g9 "(Whatever. As long as I can beat my meat in peace.)"
        "> *fap-fap-fap*"

    call lun_walk("desk", "base")
    pause 0.25
    call lun_chibi(flip=True)
    with d3

    "> Luna turns around and bends down slightly, examining the floor tiles, giving you an eyeful of her round butt without realising."

    if masturbating:
        with hpunch
        g4 "(Holy shit that ass!)"
        "> {size=+3}*{b}fap{/b}-fap-{b}fap{/b}*{/size}"
        g4 "*Ugh*... (I'm getting close.)"
        lun "There's such a strange aura in here..."
        g4 "(Yes! It's the aura of me going crazy for you, you fucking slut!)"
        "> {size=+3}*{b}fap{/b}-fap-{b}fap{/b}*{/size}"
    else:
        lun "There's such a strange aura in here..."
        lun "It's like a big hollow tree..."
        m "(Oh, good... She's a hippie...)"

    call lun_chibi(flip=False)
    with d3

    ">Luna finally turns to face you."

    if masturbating:
        g4 "(Yes, yes! You little slut! Here it comes!)"
        call gen_chibi("cum_behind_desk")
        call cum_block
        lun "Whoa!"
        call cum_block
        lun "There's so much!"
        g4 "*Argh*... (It's all yours...)"
        lun "They're flying everywhere! How impressive!"
        g4 "Yes! (All because of you, you silly-hot bimbo!)"
        call cum_block
        g4 "*Argh*-- fuck! *heavy panting*"
        call gen_chibi("cum_behind_desk_done")
        with d3
        m "That was... that was awesome."
    else:
        lun "Whoa!"
        m "What? Is there something on my face?"
        m "Actually, first of all... What are you even wearing?" # Luna ignores him.
        pause 1
        lun "This room is full of them!"
        m "(She ignored my question...)"
        m "Full of what?"
        lun "Wrackspurts!"
        m "Not this again..."

    lun "I've never seen anything like this before, and never so clear..."

    if masturbating:
        g9 "There's more where that came from."
        lun "So you can see {i}them{/i} too Professor?"
        m "I can't see anything."
        m "(Besides the residue of my cum, but she doesn't need to know that.)"
        lun "*sigh* Just as expected."
        lun "You could see them if you had one of these."
    else:
        m "I can't see anything."
        lun "Of course you can't, Professor."
        lun "Because you don't have these!"

    "> Luna points to the oddly shaped glasses on her nose."
    m "These goofy looking glasses?"
    m "Are you planning on winning the masquerade ball or what?"
    lun "Don't be fooled by their look professor, these glasses are infused with magic."
    lun "They are called {i}Spectrespecs{/i}!"

    menu:
        "\"Spectre-- what?\"":
            lun "Spectrespecs!"
            lun "They allow the wielder to see things that are there, but hidden."
            m "And that vapor ware thing on your nose is supposed to help you with that?"
            lun "*uh-huh!*"
            m "Great..."

        "\"Spectres as in ghosts?\"":
            g4 "There are ghosts in here?!"
            lun "Well, I don't know about ghosts--"
            m "Quick, I need to call someone..."
            lun "Oh, who you gonna call?"
            g9 "Luigi, he's clearly the superior choice when it comes to fighting ghosts."
            lun "Who, sir?"
            m "Never mind."

        "\"The theory of the parable fourth dimensional tuples.\"":
            lun "I'm sorry, sir?"
            m "*sigh* I'm talking about the four-dimensional space, {size=-1}a mathematical{/size} {size=-2}extension of the concept{/size} {size=-3}of three-dimensional or 3D space.{/size} {size=-5}Three-dimensional space{/size}{size=-7} is the simplest possible abstraction of the observation that one only needs three numbers, called dimensions, to describe the sizes or locations of objects in the everyday world.{/size}{size=-10}For example, the volume of a rectangular box is found by measuring and multiplying its length, width, and height (often labeled x, y, and z)...{/size}"
            call blkfade
            centered "{size=+7}{color=#cbcbcb}5 minutes later...{/color}{/size}"
            call hide_blkfade
            m "...and this is how your glasses work, right?"
            lun "I... Maybe?" # Puzzled
            m "Don't they teach you basic physics in this school?"
            m "No matter."

    m "So, can you see any Wickedysports in this room?"
    lun "Wrackspurts, sir, and yes, there's many of them."
    lun "Why don't you try wearing the glasses yourself, sir?"

    menu:
        "\"Sure, why the hell not.\"":
            m "Give me those glasses and I'll have a look..."

        "\"You're not pulling my leg?\"":
            lun "I am not, Sir."
            m "*Hm*, Fine."

        "\"I am not wearing {b}THAT{/b}\"":
            m "*Nuh-uh* Not a chance. They look silly."
            lun "It doesn't matter how they look as long as they're practical."
            m "I'm not putting them on."
            lun "Please sir, can't you make an exception?" # Pouts
            lun "It's really important to me..."
            m "(Damn, she's cute when she's pouting.)"
            m "Fine, but just this once."

    $ renpy.play('sounds/magic1.ogg')
    show layer screens at uvlight
    show screen spectrevision
    if not renpy.mobile:
        show screen spectrevision_cursor
    with d9

    pause 0.5
    "> The world around you starts shifting."

    g9 "Holy shit, that's so cool!"
    g9 "I'm keeping them!"
    lun "Sir, those are my Spectrespecs..."
    m "So? I'll give them back soon enough."
    lun "But..."
    m "They aren't {i}soulbound{/i}, are they?" # Did we make a joke like this before?
    lun "I'm sorry, Sir, but I don't like lending my personal belongings to other people."
    lun "Usually I never get them back when I do..."
    m "Not even for a day? Surely you can trust me."
    lun "Professor, you should get your own pair of Spectrespecs."
    m "..."
    $ renpy.play('sounds/magic1.ogg')
    show layer screens
    hide screen spectrevision
    hide screen spectrevision_cursor
    with d9
    "> You take the glasses off and hand them over."
    m "Here, you Scrooge McDuck..."
    lun "Thank you professor."
    lun "If you'd like the get a pair of your own, you can get them with the newest issue of the Quibbler."
    lun "On page 6 they have a whole section on Wrackspurts! It's quite fascinating to read through."
    m "The what now?"
    m "(Is she making all that shit up, or should I know about these things?)"
    m "So, how do I get them again?"
    lun "*sigh* Let me repeat."
    lun "First you have to buy the latest issue of The Quibbler."
    lun "And you should really read through all of it."
    lun "There's quite the informative article about Womps on page 9!"
    lun "I was blown away when I found out that womps can sometimes--"
    m "(I'm starting to lose my patience with this girl.)"
    g4 "Yes, yes... but what about the glasses? How do I actually {b}get{/b} them?"
    lun "Oh, that's quite easy!"
    lun "There's a quiz on the last page you'll need to complete."
    lun "Once filled in, cut it out and send it to the address mentioned in the article talking about Wrackspurts."
    lun "A day or two later you'll receive your glasses."
    lun "It's that simple."
    m "That simple *huh*..."

    menu:
        "\"Too much effort...\"":
            lun "Well."
            lun "They're a reward for proving your wit and cunning, after all."
            m "Pass..."
            lun "Give it a chance, Professor. Quizzes are fun!"
            m "Agree to disagree."
            lun "Surely an esteemed wizard like yourself would have no trouble but with a simple quiz."
            m "(She got me there...)"
            m "I guess..."
            lun "That's settled then."

        "\"How about I buy yours instead.\"":
            m "I can give you anything you want."
            m "Gold... house points... I got it all, just name me your price."
            lun "I'm afraid they are not for sale, Sir."
            m "{size=-4}Dammit...{/size}" # small text
            lun "If you want them, you got to earn them."
            lun "Okay then."

    ####
    # Shouldn't Luna be used to being a loner?
    # I don't like this part in particular because she's too honest about herself. ~Loafy
    #
    # TODO: Delete this comment once this is resolved.
    ####

    lun "Please call me once you got the glasses, Professor."
    lun "Or... call me any time, really. I'd love to talk to somebody from time to time."
    m "Don't you have any friends?"
    lun "Well, not friends in a conventional sense, but I manage."
    m "(Damn. That's the saddest thing I've heard all day.)"
    lun "Anyway, let me know what you think of the paper once you've read it."
    m "What paper?"
    lun "The quibbler!"
    #">Luna gestures towards the magazine."
    lun "Hopefully you'll be able to find some more information on how to deal with them in there."
    m "You can count on me."
    #lun "Or maybe we could get daddy to help?"
    #g4 "No!"
    # lun "..."
    #m "I mean...{w} I'm sure the paper shall suffice..."
    #m "In fact, I plan reading it in just a moment."
    #lun "Oh, of course sir!"
    lun "I'll leave you to it then."
    m "You do that..."

    call lun_walk("door", "base")
    call lun_chibi(flip=False)
    with d3

    lun "If you find yourself with any time spare, then there's a great article about shungite on page thirty-seven."
    m "Let's focus on those spurts for now."
    lun "Okay, see you later then!"

    call lun_walk(action="leave")

    m "(No wonder Hermione called her Loony.)"
    m "Where could I get that magazine from? The Twins?"
    m "Maybe they have it in stock. I should ask them..."

    jump main_room
