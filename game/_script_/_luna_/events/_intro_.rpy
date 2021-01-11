
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

    call play_music("luna", fadein=5.0)
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

            call blkfade
            call gen_chibi("dick_out", 450, "base", flip=False)
            pause 1
            call hide_blkfade
            g9 "What do you think about this?"
            lun "...Crumple-Horned Snorkack..."
            m "...Well, that's just rude..."
            pause 0.5
            with d3

    # Genie walks back to his chair and sits down
    m "(What a strange girl...)"
    m "(Although the crazies usually give the best blowjobs...)"
    m "(Well, now I'm hard...)"

    menu:
        "-Jerk off-":
            m "(Even after thousands of years, this is a new one even for me...)"

            call blkfade
            call gen_chibi("jerk_off", 450, "base", flip=False)
            pause 1
            call nar("*Fap* *Fap* *Fap*...")
            call hide_blkfade

            m "..."
            m "Hey, you could at least talk dirty or something."
            lun "I feel...{w} tingling..."
            g9 "Nice..."
            lun "Crawling on my skin..."

            call gen_chibi("dick_out", 450, "base", flip=False)
            g4 "..."
            m "(Yeah, this is not going to work...)"
            call blkfade
            call gen_chibi("stand", 450, "base", flip=False)
            pause 1
            call hide_blkfade
            m "(Better let someone else deal with this one...)"

        "-Don't-":
            call blkfade
            call gen_chibi("stand", 450, "base", flip=False)
            call hide_blkfade
            pause 1
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
            m "*heh*... Just as I exp--"
            $ renpy.play('sounds/attack_snape2.ogg')
            show pentogram onlayer screens at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
            with d5

            pause 0.5
            m "Uh-oh..."
            call blkfade
            hide pentogram onlayer screens
            centered "{size=+7}{color=#cbcbcb}20 minutes later...{/color}{/size}"

            g9 "*Ha-ha*... Good one! Alright, talk to you later Beelzebub!"
            "Beelzebub" "Ah, don't be so formal, just call me Bub."
            "Beelzebub" "If you ever need some latest {i}hot{/i} news, I'm your guy."
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
    her "Do what exactly? I thought you weren't supposed to wake somebody up that is sleepwalking..."
    m "Then just escort her back to her bed..."
    her "She's from Ravenclaw, I don't have access to their dormitory, so why me?"

    if d_flag_02 == "hermione":
        m "You were the obvious choice, Miss Granger."
    elif d_flag_02 == "satan": #TODO This flag doesn't seem to work it defaults to else (I picked all options before Hermione)
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
    m "Even my immense knowledge has its limits dear..."
    her "(Clearly there's more important things occupying your mind...)" # Rolls eyes
    her "How come you haven't escorted her back yourself, professor?"


    menu:
        "\"I don't know where this Ravenglove dormitory is...\"":
            her "It's Ravenclaw, [genie_name]..."
            m "Yes, that's what I said..."
            her "You said--"
            her "What do you mean you don't know where their dormitory is?"
            m "Girl, I'm starting to lose my patience..."
            m "Just get this weirdo out of here, will you?"
        "-Dismiss the question-":
            m "Just get this weirdo out of here, please."

    her "[genie_name]!" # Gasp
    lun "It tickles..."
    her "......" # Looks at Luna, puzzled.
    her "She...{w=0.4} She's not a weirdo... She's just a bit... Loony..."
    m "I don't care how you call it, just escort miss {i}Loony{/i} back to her bed...."
    her "I can't!"
    m "..."
    her "As I've already said, professor... I'm not allowed in their dormitory."
    g4 "Bloody hell, there's always {i}something{/i}..."

    if d_flag_02 == "tonks": #TODO This flag doesn't seem to work either. Is it cause it's not saving multiple flags?
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
        lun "*Sniff*..."
        her "Shush now... It's okay Luna, professor Snape is not allowed here."
        m "..."
        m "Fine. I'll just get Professor Tonks up here..."

        call blkfade
        call nar("> You attempt to summon Tonks to your office.")
        call hide_blkfade

        m "..."
        call ton_walk("mid", 460, action="enter")
        ton "You called..."

    her "Professor!" #Wide eyed
    ton "*Oooooh* What's this? A slumber party?" #TODO can we have a mix of small and big letters in the "oooooh"?
    g9 "It is now!"
    g9 "Let me search for my bathrobe real quick."
    her "P-Professor, that's not why we asked her here."
    m "Right... Tonks, we may require your assistance here..."
    ton "Assistance? With what--"
    lun "Wrackspurts!"
    ton "Ah... Miss Lovegood."

    if d_flag_01:
        g9 "Luna Love-good... *heh*, that's funny."
        ton "What's funny?"
        m "Love...{w=0.4} Good...{w=0.6} Get it?"
        ton "..."
        m "Anyway..."

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
    her "How could you say such a thing!?"
    ton "Yes... Such a rude thing to say to your staff. {heart}"
    m "I'm a man of simple truths, I'm only stating the obvious."
    ton "So my current attire is too slutty for you, huh?"
    g9 "I didn't say that, Miss Tonks..."
    g9 "I said you look like a slut... There's a difference."
    her "What if a student saw you professor?! You can't walk around the castle wearing... This!"
    ton "Quit worrying. Nobody is going to see me this late at night."
    ton "After all, it's already past curfew..."
    ton "Students should be in their beds, including you, Miss Granger."
    her "But professor Dumbledore asked me to--"
    ton "You just head back to bed, and I'll make sure Miss Lovegood gets back safe and sound to her dormitory..."
    her "Okay..." #annoyed
    ton "Good girl."

    call her_walk("door")

    her "Good night then..." #annoyed, flipped
    ton "Sleep tight, Miss Granger..." # Tongue in cheek

    call her_walk(action="leave") #TODO Hermione pops above Tonks Chibi when leaving

    # Tonks should maybe talk to Genie about the situation some more here.

    ton "Very well then..."
    ton "Come on, Miss Lovegood, let's get you back to bed..."

    #Tonks walks to the door

    lun "But I'm not tired mummy..."
    ton "..." #wide eyed
    m "What a weirdo..."
    ton "Just...{w=0.4} be a good girl and follow me back to bed..."
    lun "Yes, mummy..."

    call lun_walk("door") #TODO Luna moves above Tonks Chibi when leaving

    ton "Don't worry about her, she'll be fine."
    m "I won't."

    call ton_walk("door", action="leave") #TODO is it possible for both to leave at the same time?
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
        g4 "(Look at the tits on this girl, such a lovely profile!)"
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

    lun "Why, I've never seen anything like this before, and never so clear..."

    if masturbating:
        g9 "There's more where that came from."
        lun "So you can see {i}them{/i} too Professor?"
        m "See what?"
        lun "*sigh* Just as expected."
        lun "You could see them if you had one of these."
    else:
        m "I can't see anything."
        lun "Of course you can't, Professor."
        lun "Because you don't have these!"

    "> Luna points to the oddly shaped glasses on her nose."
    m "Those goofy looking glasses?"
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
            g4 "*G-G-Ghe* Ghosts!"
            lun "Well, I don't know about ghosts--"
            m "Quick, I need to call someone..."
            lun "Oh, who you gonna call?"
            g9 "Luigi, he's clearly the superior choice when it comes to fighting ghosts."
            lun "Who, sir?"
            g4 "Who... How do you not know... The inventor of the Luigi board?"
            lun "*Huh*?"
            m "Never mind."
            m "If not ghosts..."

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

    m "What are you seeing in this room exactly?"
    lun "Wrackspurts, sir, and lots of them too!"

    #$ renpy.play('sounds/magic1.ogg')
    #show layer screens at uvlight
    #show screen spectrevision
    #if not renpy.mobile:
    #    show screen spectrevision_cursor
    #with d9

    #pause 0.5
    #"> The world around you starts shifting."

    #m "..."
    #$ renpy.play('sounds/magic1.ogg')
    #show layer screens
    #hide screen spectrevision
    #hide screen spectrevision_cursor
    #with d9

    m "Brackspurts?"
    lun "Wrackspurt sir..."
    m "I see..."
    m "(Is she making all this shit up, or am I supposed to know about these things?)"
    m "Well I can't say I've ever come across these whackspurs you speak of."
    lun "There's a whole section dedicated to them in the quibbler, it's a quite fascinating read you know."
    m "Pretend that I don't know..."
    lun "The quibbler is my daddy's magazine, sir."
    m "So is that why you're here?"
    m "To advertise your fathers magazine?"
    m "Now I must say that's quite bold for a student to just waltz into their headmasters office and chill their--"
    lun "Oh... No sir!"
    lun "I'm just worried that we might have an infestation on our hands and--"
    #Luna eyes down
    pause .5
    call nar("Luna gives you an uncomfortable look and then turns her gaze to floor.")
    m "An infestation?"
    lun "Yes sir. I've come across several swarms of them in a fair few places recently."
    lun "They appeared quite docile at first but recently they've started to become quite problematic..."
    m "Well I sure would love to be able to help Miss Lovegood, but as I said this is the first time I even heard about these things..."
    lun "*Oh*... But you can help, sir!"
    lun "You're the most powerful wizard there is so if anyone could deal with them it'd be you..."
    m "Well... I'm not usually the person to brag but..."
    g9 "I am known to have slung some seriously powerful spells around back in the day..."
    lun "Oh thank you sir, I knew you'd be able to help!"
    m "Why of course, anything for a student in--"
    g4 "Hold on, I didn't actually say yes yet!"
    lun "So I think what would be best is if you'd read my daddy's magazine..."
    m "(Is she even listening?)"
    lun "I'm sure once you've read through all of it you'll be able to use your immense knowledge to find a solution..."
    g9 "Of course!"
    g9 "I am all knowing after all!"
    m "(Or am I? I don't even know anymore...)"
    g4 "(Wait... She did it again!)"
    lun "Thank you sir..."
    m "Now hold on for a second..."
    lun "Let me know what you think of the paper once you've read it!"
    m "What paper?"
    lun "The quibbler!"
    m "Oh... right..."
    lun "I'll leave you to it then."
    m "You do that..."

    call lun_walk("door", "base")
    call lun_chibi(flip=False)
    with d3

    lun "See you later, sir."

    call lun_walk(action="leave")

    m "(No wonder Hermione called her Loony... Her mind might as well be in another dimension...)"
    m "(Where am I even supposed to get that bloody magazine from?)"

    if store_intro_done:
        m "(*Hmm*... I'm sure someone's bound to have it.)"
        m "(Maybe it's time to look around the castle a bit more...)"
    else:
        m "(Well... Hopefully the twins carries it...)"

    #TODO unlock luna Summon. Keep all options locked except for Talk which provides hints if you get stuck (buy quibbler etc written in spectrequest file). Luna's other options unlocks after finishing those quests once private favours start.
    #TODO she also looks mad in her summon menu atm

    jump main_room
