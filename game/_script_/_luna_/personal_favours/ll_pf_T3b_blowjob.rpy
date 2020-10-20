
label ll_pf_blowjob:
    # Common start label

    $ ll_pf_blowjob.start()

    label end_luna_blowjob_event:

    if lun_whoring < 9:
        $ lun_whoring += 1

    jump end_luna_event


label ll_pf_blowjob_T1_intro:
    # Luna gentle BJ where she just happily sucks and lick it like a lollipop for an hour.
    # This random event unlocks the favor, after it you get the menu option in her favor menu.

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    g4 "Yeah--"

    call lun_walk("mid", action="enter")
    pause.5

    call lun_main("Hello, [lun_genie_name]! Lovely day today isn't it?","base","happyCl","base","mid", xpos="mid", ypos="base")
    m "(...)"
    g9 "It is now..."
    call lun_main("*Aww*... that's so nice!","base","wink","sad","mid")
    m "What brings you up to my office today then Miss Lovegood?"
    m "Those troublesome little {i}wrockspoons{/i} giving you grief again?"
    call lun_main("Not exactly...","soft","seductive","sad","down")
    m "Oh... Something else I can help you with then?"
    call lun_main("Well... I was just walking past when I remembered how those nasty wrackspurts affected you the other day...","open","base","sad","R")
    call lun_main("They aren't by any chance bothering you at the moment, are they [lun_genie_name]?","base","wink","sad","mid")
    m "Now that you mention it, they have been giving me a little trouble..."
    m "But I'm much too tired to relieve myself of them... I'm such an old man you see..."
    call lun_main("Really?","soft","wide","sad","mid")
    call lun_main("So you won't...","pout","annoyed","sad","down")
    call lun_main("...","normal","annoyed","sad","R")
    call lun_main("Is there any way I could help?","base","wink","sad","mid")
    m "*Hmmmm*... There is a special technique that I've been developing..."
    m "I'm not sure you're ready for it though..."
    call lun_main("Please, [lun_genie_name]! I know I can handle it!","base","wide","sad","mid")
    m "If you insist..."
    m "Just make sure you don't let anyone else know about this..."
    call lun_main("I wouldn't dare...{w=0.3} A cure for wrackspurts would be the talk of the magical world...","base","wide","angry","mid")
    m "Yes..."
    call lun_main("So what does this technique involve?","base","wink","sad","mid")
    m "It involves you sucking the nasty things out of me."
    call lun_main("Sucking them out!?","scream","wide","mad","mid")
    m "(I'm not sure if she'll fall for th--)"
    call lun_main("That's brilliant!","open","happyCl","base","mid")
    m "...{w} It is?"
    call lun_main("Of course!","base","base","sad","L")
    call lun_main("Everyone knows wrackspurts can't survive in someone's stomach!","base","happyCl","base","mid")
    m "Very good Miss Lovegood... I see you know your...{w} magic..."
    call lun_main("*Mhmm*! it also allows you to just sit there while I get rid of them!","base","seductive","base","down")
    m "You expect me to just sit here while you suck them out?"
    call lun_main("*Mhmm*!","base","happyCl","base","mid")
    m "And you want that?"
    call lun_main("Only if it isn't too much trouble, [lun_genie_name], I know you must be busy...","normal","wink","sad","R")
    m "No trouble at all..."
    call lun_main("Hooray!","base","wide","base","empty")
    call lun_main("Now, how does this secret technique work?","base","wink","raised","mid")
    m "Well... since you offered to do this while I'm sitting, why don't you come over here?"
    call lun_main("Can I hide under your desk?","base","base","base","mid")
    m "You don't have to, I can turn the chair around."
    call lun_main("Oh no, I want to...","base","wink","sad","R")
    call lun_main("I've always been rather fond of small spaces like that...","base","base","sad","down")
    call lun_main("When I was a little girl, I used to hide in the roots of a huge {i}Wiggentree{/i} near our home...","soft","seductive","sad","down")
    call lun_main("I've never felt as safe as I did when I was under the roots of that tree...","base","happyCl","base","mid")
    call lun_main("It was as if the wood would wrap around me to hug me when it was cold out...","base","seductive","base","R")
    call lun_main("...","base","seductive","sad","down")
    m "..."
    m "Feel free to crawl under the desk if you want..."
    call lun_main("Thank you, [lun_genie_name]...","base","happyCl","base","mid")

    call lun_walk("desk")

    call ll_pf_blowjob_T1_under_desk

    call lun_main("Those nasty wrackspurts sure were giving you trouble, weren't they [lun_genie_name]?","base","seductive","sad","mid",xpos="right",ypos="base")
    m "Yeah... sure..."
    call lun_main("Well if they bother you again just let me know!","base","happyCl","base","mid")
    call lun_main("Getting all of them out was a bit of a struggle...","soft","suspicious","sad","R")
    call lun_main("But I think we did it!","base","happyCl","base","mid")
    m "You sure did..."
    m "Now if you don't mind Miss Granger..."
    call lun_main("Lovegood, [lun_genie_name]...","pout","wink","sad","mid")
    m "Right, right... miss Love... {b}good{/b}..."
    m "This encounter with those...{w=0.4} things... has left me rather exhausted..."
    call lun_main("Oh...","soft","wide","base","mid")
    call lun_main("Of course, [lun_genie_name]! I best be off to divination class anyway...","base","base","sad","R")
    call lun_main("Just make sure you let me know if you need any help with those wrackspurts again!","base","seductive","sad","mid")
    call lun_main("(I can't believe they taste so good...)","base","seductive","sad","empty")
    m "You'll be the first to know."
    call lun_main("Thanks, [lun_genie_name]! Have a nice day!","base","happyCl","base","mid")

    call lun_walk(action="leave")

    call bld
    m "..."

    jump end_luna_event


label ll_pf_blowjob_T1_E1:
    # Second "lesson" in removing wrackspurts

    $ ll_event_pause += renpy.random.randint(1, 2)

    call lun_main("","base","happyCl","base","mid", xpos="mid", ypos="base", trans=fade)
    m "*Argh*... these {i}wankspurts{/i} are causing a fair bit of swelling..."
    call lun_main("They are?!","pout","wide","sad","mid")
    m "Indeed. I think it's about time I taught you another important method to treat them."
    call lun_main("Another technique?","base","wide","base","mid")
    m "Only if you want to learn it."
    call lun_main("Of course!","base","happyCl","base","mid")
    call lun_main("They're all I can think about, [lun_genie_name]!","base","seductive","sad","R")
    call lun_main("And these lessons have been so much fun...","base","wink","sad","mid")
    call lun_main("I definitely want to learn more!","base","happyCl","base","mid")
    m "Then do I have the lesson for you..."
    m "Come over here and we'll start..."
    call lun_main("Yay!","smile","happyCl","sad","mid")

    call lun_walk("desk")

    call ll_pf_blowjob_T1_under_desk

    call lun_main("Have a nice day, [lun_genie_name]!","base","happyCl","base","mid")

    call lun_walk(action="leave")

    call bld
    m "(...)"

    jump end_luna_blowjob_event


label ll_pf_blowjob_T1_E2:
    # Luna gentle BJ for about 9 hours and 14 orgasms from Genie

    $ ll_event_pause += renpy.random.randint(1, 2)

    call lun_main("","base","happyCl","base","mid", xpos="mid", ypos="base", trans=fade)
    m "Miss Lovegood, care to help me with my {i}wackspurts{/i} infection again?"
    call lun_main("You are lucky, [lun_genie_name]!{w=0.4} Because today is a Sunday!","base","seductive","sad","mid")
    m "It is?"
    call lun_main("Of course! Can't you tell how happy mister Sun is?","base","wide","base","mid")
    m "..."
    call lun_main("Because it's mister Sun's happy day...","base","seductive","base","mid")
    call lun_main("I don't have any classes...","base","seductive","sad","R")
    call lun_main("So I was wondering...{w=0.4} maybe I could get a few more of those nasty wrackspurts out for you?","base","wink","angry","mid")
    call lun_main("I just feel so bad knowing that I gave them to you...","pout","wide","sad","mid")
    m "You shouldn't blame yourself."
    call lun_main("But I do!","open","wide","sad","mid")
    call lun_main("The idea of all those nasty things being trapped in there...","base","seductive","sad","empty",cheeks="blush")
    call lun_main("Causing so much discomfort...","upset","seductive","sad","downL",cheeks="blush")
    call lun_main("It's all I've been able to think about!","base","angry","angry","empty",cheeks="blush")
    m "I suppose if it's been bothering you so much, I could let you get a few out."
    call lun_main("Oh! Thank you, thank you, thank you!","open","happyCl","base","mid",cheeks="blush")
    call lun_main("You don't even know how much better I'll feel once I get them {i}all{/i} out!","base","angry","angry","empty",cheeks="blush")
    m "I don't think you--"

    # TODO Inline the script from this label in this one, since it's only called here (and it's not a menu-driven branch either)
    call ll_pf_blowjob_T1_marathon

    m "You don't intend to walk to your dorm like that do you?"
    call lun_main("Of course! I intend to wear these wrackspurt corpses with pride!","base","happyCl","base","mid",cheeks="blush")
    call lun_main("It should serve as a warning to the other wrackspurts around the school!","base","angry","angry","mid",cheeks="blush")
    m "Oh, well... don't let me stop you then."
    call lun_main("Plus, I think I'll be able to make a lovely perfume out of it...","base","wink","sad","mid",cheeks="blush")
    m "..."
    ">Luna takes in a deep breath."
    call lun_main("*Agh*.... it reminds me of my old {i}Wiggentree{/i}... and my new friend!","base","happyCl","sad","mid",cheeks="blush")

    call lun_walk(action="leave")

    #$ luna_wear_cum = False

    call bld
    m "..."
    m "I still can't move..."
    m "eh..."
    m "*Zzzz*..."

    jump end_luna_blowjob_event


label ll_pf_blowjob_T1_E3:
    # Luna regular BJ for about 5 hours with Luna masturbating the whole time

    call lun_main("","base","base","base","mid", xpos="mid", ypos="base", trans=fade)
    m "[luna_name], would you like to help me with those nasty {i}wackspurts{/i} again?"
    call lun_main("I'd love to, [lun_genie_name]!","base","happyCl","base","mid",cheeks="blush")
    m "..."
    m "You're not going to paralyse me again are you?"
    call lun_main("Oh... not if you don't want me too...","base","wink","sad","mid",cheeks="blush")
    m "I do not."
    call lun_main("Sorry... I thought you'd like it... Is there anything I can do to make it up to you?","base","seductive","sad","downL",cheeks="blush")
    m "Hopping under the desk would be a good start."
    call lun_main("Really? I was worried you'd be mad at me!","base","wide","sad","mid",cheeks="blush")
    m "Well, so long as you do a good job making it up to me..."
    call lun_main("Don't worry sir, I'll do my best!","base","mad","sad","mid",cheeks="blush")
    m "About that..."

    #TODO Maybe add "Luna walks around your desk" transition?

    menu:
        "-Face fuck her to teach her a lesson!-":
            call ll_pf_blowjob_T1_facefuck
            # Luna finds out Genie's true identity in this part
            $ lun_genie_name = "genie"

        "-Let her do her own thing...-":
            call ll_pf_blowjob_T1_slapping

        "-Summon Somebody!-":
            call ll_pf_blowjob_T1_summon

    # Luna has left
    jump end_luna_blowjob_event


label ll_pf_blowjob_T1_under_desk: # Call label
    call hide_characters
    show screen blkfade
    with d5

    ">Luna quickly walks around your desk and crawls underneath..."
    if ll_pf_blowjob.counter == 1:
        m "Are you okay down there?"

    pause.5

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"genie_robe.webp"
    $ lun_cg_dick         = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0
    #$ luna_wear_top       = True
    $ lunCG(pupil='left', eye='wide', mouth='open', eyebrow='base', cheeks='base', extra_1='blank', extra_2='blank', extra_3='blank', tears='blank', body='base')

    if ll_pf_blowjob.counter == 1:
        # Luna is amazed by the dirty desk
        show screen luncg
        hide screen blkfade
        with d5
        lun "My goodness...{w=0.4} I've never seen so much..."
        m "Oh yeah...{w=0.4} that..."
        $ lunCG(pupil='ahegao', eye='closed', mouth='base')
        lun "There's more magic in here than under my Wiggentree!"
        m "Wait..."
        m "Magic?"
        $ lunCG(pupil='up', eye='base')
        lun "Can't you feel it, [lun_genie_name]?"
        $ lunCG(pupil='up', eye='seductive', mouth='open_tongue')
        lun "It's so heavy in the air... It's {i}all{/i} over the wood..."
        $ lunCG(pupil='base', eye='mad')
        lun "You can almost taste it..."
        ">Luna takes a deep breath of the air under your soiled desk..."
        $ lunCG(pupil='base', eye='mad', mouth='base')
        lun "Wow..."
        m "Are you sure you're okay down there? I haven't cleaned it since...{w=0.5} well...{w=0.5} ever..."
        lun "I'm... great..."
        $ lunCG(pupil='ahegao', eye='closed')
        lun "Now..."
        ">Luna takes another deep breath..."
        $ lunCG('talk', 'seductive', 'sad', 'up')
    else:
        # Reveal CG with the correct expression
        $ lunCG('talk', 'seductive', 'sad', 'up')
        show screen luncg
        hide screen blkfade
        with d5

    lun "Are you ready to teach me this new technique?"
    m "(She's got to be in on this... No one could be this oblivious...)"
    g9 "Certainly!"
    m "(Still, better not to look a gift horse in the mouth...)"
    m "Now, I'm going to need you to open your mouth..."
    $ lunCG('base', 'seductive', 'sad', 'dick', cheeks='blush')
    lun "okay!"
    $ lunCG('open_tongue', 'base', 'sad', 'up')
    lun "Agh..."
    m "..."

    menu:
        "-Take your cock out-":
            ">While the naive blonde sits under your desk, you decide it's finally time for her to get to work."
            ">You slowly pull your hardening cock from underneath your robe."
            $ lunCG('open', 'wide', 'base', 'dick', pos=1)
            lun "..."
            $ lunCG('talk', 'wide', 'sad', 'dick')
            lun "{size=-5}wow...{/size}"
            m "Now this special technique requires you to suck those nasty little critters out of the affected area..."
            m "For me that's right here..."
            ">You give your thick cock a lazy stroke to emphasise."
            $ lunCG('base', 'wink', 'base', 'up')
            lun "Is there any way in particular that you want me to suck it?"
            m "Imagine it's a tasty lollipop..."
            m "Just don't bite it."
            $ lunCG('base', 'seductive', 'sad', 'dick')
            lun "Okay then..."
            ">Without any further delay, Luna hops forward to take the head of your cock in her mouth."

        "-Shove it in her mouth!-":
            m "Open wide!"
            $ lunCG('wide', 'closed', 'sad', 'dick')
            lun "*Aaaahh*..."
            #">As the naive blonde kneels under your desk with her mouth open wide, you decide to reward her eagerness..."
            ">You quickly slip your hard cock from underneath your robe into the girl's warm mouth."

        "-Make her take it out-":
            m "Now, I'm a little tired..."
            m "So why don't you open my robe for me and pull out the \"affected area\"..."
            $ lunCG('base', 'seductive', 'sad', 'dick')
            lun "Of course, [lun_genie_name]..."
            ">Luna reverently opens your robe and softly withdraws your hard cock."
            $ lunCG('open_tongue', 'base', 'sad', 'up')
            lun "What do you..."
            $ lunCG('open', 'wide', 'base', 'dick')
            lun "What now, [lun_genie_name]?"
            m "Put the tip in your mouth and Imagine it's a tasty lollipop..."
            m "Just don't bite it."
            $ lunCG('base', 'seductive', 'sad', 'dick')
            lun "*Mhmm*!"
            $ lunCG('wide', 'closed', 'base', 'up')
            lun "Okay then!"
            ">Without any further delay, Luna hops forward to take the head of your cock in her mouth."

    $ lunCG('sucking', 'seductive', 'sad', 'base', pos=3)
    ">Luna begins sucking in earnest as her tongue starts darting along the underside of the head of your sensitive cock at a blistering pace."
    $ lunCG('sucking', 'angry', 'mad', 'down', pos=6)
    g4 "By the gods girl!"
    $ lunCG('sucking', 'wide', 'sad', 'up', pos=4)
    lun "*Ish -omhing whon-*? (Is something wrong?)"
    ">Luna somehow manages to form her muffled question without even slowing her tongue."
    g4 "N-no, of course not...{w=0.3} You're doing great..."
    $ lunCG('sucking', 'wink', 'sad', 'up', pos=5)
    lun "*Hi hm*? (I am?)"
    g4 "Yes..."
    $ lunCG('sucking', 'seductive', 'sad', 'up', pos=3)
    lun "*Hnnk hoo hrr*! (Thank you, [lun_genie_name]!)"
    ">In response to your misguided praise, Luna's tongue starts to move event faster."
    g4 "*Argh*..."
    $ lunCG('sucking', 'angry', 'mad', 'down', pos=5)
    lun "(Those wrackspurts must really be affecting him...)"
    $ lunCG('sucking', 'wide', 'mad', 'down', pos=8)
    lun "(I better try even harder!)"
    g4 "Would you please slow down miss Lovegood!"
    $ lunCG('sucking', 'wink', 'base', 'up', pos=3)
    ">Luna takes your cock out of her mouth."
    g4 "Ah..."
    $ lunCG('base', 'seductive', 'sad', 'up', pos=1)
    lun "Was I doing a bad job, [lun_genie_name]?"
    m "You were just going a little--"
    $ lunCG('pout', 'wide', 'sad', 'up', pos=1)
    lun "I knew I was hurting you!"
    $ lunCG('pout', 'base', 'sad', 'down', pos=1)
    lun "Maybe we should stop?"
    m "What? Gods no!"
    $ lunCG('pout', 'wink', 'sad', 'up', pos=1)
    lun "But wasn't I doing it wrong?"
    m "Of course not..."
    $ lunCG('talk', 'seductive', 'sad', 'up', pos=1)
    lun "Why did you ask me to slow down then?"
    m "I didn't... It was those nasty {i}wrinklespores{/i}!"
    m "They must have made me say it so you'd leave them alone..."
    $ lunCG('pout', 'mad', 'mad', 'dick', pos=1)
    lun "Those tricky little..."
    $ lunCG('base', 'angry', 'angry', 'dick', pos=1)
    lun "Don't worry, [lun_genie_name], I'll have them out in no time!"
    ">With that, Luna resumes her rapid licking of your cock."
    $ lunCG('sucking', 'angry', 'mad', 'down', pos=5)
    g4 "A-Ah..."
    g4 "G-good work miss Lovegood..."
    $ lunCG('sucking', 'closed', 'sad', 'up', pos=8)
    lun "*Hnnk hoo hrr*! (Thank you, [lun_genie_name]!)"
    show screen blkfade
    with d3

    $ lunCG('sucking', 'seductive', 'sad', 'dick', pos=5)
    ">Over the next hour, Luna continues to hide under your desk as she relentlessly assaults your cock."
    ">She has an uncanny ability to tell when you're about to cum and slows to a halt every time."
    hide screen blkfade
    with d3

    g4 "I-I think this is it... again..."
    $ lunCG('sucking', 'angry', 'mad', 'dick', pos=6)
    lun "*Hmmmm*..."
    $ lunCG('sucking', 'closed', 'base', 'up', pos=3)
    lun "*Hhhoohhyyy*! (okay!)"
    m "Oh, thank--"
    ">Before you can finish your sentence, Luna suddenly thrusts her head forward, forcing your cock down her throat."
    $ lunCG('sucking', 'angry', 'sad', 'up', pos=10)
    g4 "OH GODS!"
    g4 "HERE IT COMES!"
    ">You grab the desk to steady yourself as your balls begin to contract and fire out one of the largest loads of your life."
    call cum_block
    $ lunCG('sucking', 'angry', 'mad', 'down', pos=5, extra_1='cum_2')
    lun "!!!"
    g4 "Oh fuck...{w=0.3} fuck yes!!!"
    call cum_block
    $ lunCG('sucking', 'wide', 'sad', 'dick', pos=8)
    ">Your cock continues to fire shot after shot down her throat and into her stomach."
    ">Eventually this proves too much for the girl, forcing her to pull back until your cock rests in her mouth..."
    $ lunCG('sucking', 'angry', 'sad', 'up', pos=3)
    ">Causing your cum to shoot directly into the poor girl's mouth, quickly filling her cheeks and spurting out of her nose..."
    $ lunCG('sucking', 'mad', 'sad', 'ahegao', pos=3, extra_1='cum_3')
    lun "{size=+10}!!!{/size}"
    g4 "FUCK YES!!!"
    $ lunCG('full', 'seductive', 'sad', 'dick', pos=1)
    ">The sheer force of your orgasm causes white dots to scatter across your vision."
    $ renpy.play('sounds/gulp.mp3')
    $ lunCG('talk', 'angry', 'sad', 'ahegao', pos=1)
    pause 1
    show screen blkfade
    with d5
    ">In the afterglow of this enormous climax, all that can be heard is Luna slowly slurping up your cum under the desk."
    hide screen luncg
    ">Once done, she eventually decides to crawl out..."

    call lun_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3
    pause.5

    return


label ll_pf_blowjob_T1_marathon: # Call label
    # Luna paralyses you and sucks you off for 9 hours...
    call hide_characters
    show screen blkfade
    with d5

    ">Luna quickly hops over to her favourite spot in the room, your cum-soaked desk, and kneels before you."

    #TODO See if this can be rewritten using lunCG (images from luna_desk2)
    $ ccg_folder = "luna_desk"
    $ ccg("38","blank","blank")

    hide screen blkfade
    with d5

    lun "*Hmmmm*... you don't know how heavy on my mind this has been, sir..."
    $ ccg("37")
    lun "All those nasty wrackspurts churning around in you..."
    $ ccg("38")
    lun "But don't worry sir! I've got a foolproof plan to drag every single one off them out!"
    m "Oh really? And what does this plan involve?"
    $ ccg("39")
    lun "The first part was the hardest...{w=0.3} {i}Gillyweed{/i} isn't an easy thing to get..."
    $ ccg("40")
    lun "But being able to breathe without using my throat will be worth it!"
    m "I'm liking the sound of this plan already!"
    m "What's part two?"
    $ ccg("39")
    lun "It's the easiest part! All I need is my wand!"
    m "What's that for--"
    $ ccg("15")
    show screen white
    $ renpy.play('sounds/magic2.mp3')
    lun "PETRIFICUS TOTALUS!"
    ">Your body cements itself in place as you lose complete control from the neck down."
    hide screen white
    $ ccg("39")
    m "What have you done!? I can't move!"
    $ ccg("41")
    lun "Calm down sir, I'm not going to hurt you."
    m "Then why can't I move!?"
    $ ccg("36")
    lun "I was just a little worried that those nasty wrackspurts would try to make us stop before we were finished..."
    m "(Oh no...)"
    m "What do you mean by... finished?"
    $ ccg("37")
    lun "I already told you that I'm going to get {b}ALL{/b} of those tast-- *ehh*... nasty wrackspurts out, didn't I?"
    $ ccg("39")
    lun "The petrification charm is just so you don't hurt yourself."
    m "Lun--"
    ">Before you're able to protest any further, your jaw locks in place..."
    lun "Shh... that's it...{w=0.4} Just imagine that you're under the Wiggentree..."
    $ ccg("36")
    lun "We've got the whole day to look forward to..."
    m "(oh... no...)"
    $ ccg("37")
    lun "Well, let's get started shall we?"
    show screen blkfade
    with d2
    pause 0.3
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    gen "!!!!!!!"
    pause 0.5
    centered "{size=+7}{color=#cbcbcb}Three hours later...{/color}{/size}"
    pause 0.5
    $ ccg("blank","blank","blank", "luna_bj_loop_1")
    hide screen blkfade
    with d3
    call ctc

    m "Please Luna... you have to stop now..."
    g4 "four times is enough..."
    $ ccg("42","blank","blank")
    lun "Those tasty wrackspurts really have a hold on you don't they?"
    ">Luna gives your stressed balls a playful squeeze."
    $ ccg("43")
    lun "*Mmmm*... I can still feel so much magic in here..."
    $ ccg("44")
    lun "well, back to work!"
    $ ccg("blank","blank","blank", "luna_bj_loop_1")
    ">Luna's head dives forward as she gleefully pushes your cock down her soft, magically smooth throat. "
    lun "*glck-glck-glck*"
    ">Once more, the room falls into silence, save for the melodic sound of Luna's constant and unyielding throat-fucking..."
    show screen blkfade
    with d3
    pause 0.5
    centered "{size=+7}{color=#cbcbcb}A few hours later...{/color}{/size}"
    $ ccg("blank","blank","blank", "luna_bj_loop_2")
    pause 0.5
    hide screen blkfade
    with d3
    lun "*glck-glck-glck*"
    g4 "Please... I'm..."
    lun "*glck-glck-glck*"
    g4 "ARGH!!!"
    lun "*glck-glck-glck*"
    ">Luna doesn't even acknowledge your cries for help, and starts humming a merry tune instead..."
    lun "*glck-hm-ha-glck-huu-glck*"
    g4 "NO!!!"
    ">The vibrations from her humming push you over the edge, earning an excited chirp from Luna as you fire another painful load into her stomach."
    call cum_block
    g4 "*Arghhhhhh*..."
    m "Don't you... need to stop..."
    m "for lunch... or something..."
    $ ccg("f44")
    lun "*Slrp-pop*"
    pause 0.5
    $ renpy.play('sounds/gulp.mp3')
    $ ccg("45","blank","blank")
    pause 0.5
    lun "After swallowing all these wrackspurts?{w=0.4} I don't think I'll need dinner sir, let alone lunch!"
    m "please..."
    $ ccg("46")
    lun "*Shhhh*, it's okay sir... Just let me get rid of these tasty little wrackspurts and then you can have a good night's sleep..."
    $ ccg("47")
    lun "Goodness knows they haven't been letting me get one lately..."
    $ ccg("48")
    lun "I've been plotting out my revenge on them all week..."
    lun "Now..."
    $ ccg("blank","blank","blank", "luna_bj_loop_2")
    lun "*glck-glck-glck*"
    ">Luna renews her attack on your cock, sweeping her tongue along the underside as she slams the tip down her throat..."
    m "ARGHHH!"
    show screen blkfade
    with d5
    pause 0.5
    stop music fadeout 1.5

    # Next part of the day
    call defer_daytime_change(not game.daytime)
    centered "{size=+7}{color=#cbcbcb}An eternity later...{/color}{/size}"
    pause 0.5
    stop bg_sounds fadeout 3.0
    hide screen blkfade
    with d3

    g4 "Please... i can't... not any more... I'll die..."
    lun "*glck-glck-glck*"
    g4 "PLEASE..."
    lun "*glck-glck-glck*"
    g4 "*ARGHH*!!! FUCKING UGH ARGHHHHHH!!!"
    call cum_block
    $ ccg("53","blank","blank")
    lun "*glck-glck-glck*"
    call cum_block
    g4 "!!!!!!!"
    lun "*glck-glck-glck*"
    pause 0.5
    $ renpy.play('sounds/gulp.mp3')
    pause 1.5
    g4 "Ugh.."
    pause 1.5
    $ renpy.play('sounds/kiss.mp3')
    $ ccg("45")
    lun "*Slrp-pop*"
    ">Luna finally pulls away from your cock."
    lun "I think that's probably enough..."
    $ ccg("47")
    lun "Even if I do think there were still a few too many wrackspurts in that last load..."
    $ ccg("45")
    lun "Don't worry though, we can get them later!"
    m "No... not again... I can't..."
    $ ccg("49")
    lun "Of course you can! How else are we going to rid the school of them?"
    m "I... suppose so..."
    m "But... at least give me a few days to recover..."
    $ ccg("50")
    lun "A few days?!"
    m "At least..."
    $ ccg("51")
    lun "Alright..."
    lun "I might not have been so thorough today if I knew you'd take so long to recover!"
    m "Well, at least you've learned a valuable lesson."
    $ ccg("45")
    lun "I suppose I did! I think five hours is probably the limit from now on."
    m "Five!...{w=0.5} just hurry up and get yourself cleaned up, I'm about to pass out..."
    $ ccg("52")
    lun "Clean up? Why?"

    show screen blkfade
    with d5

    show screen luna_main
    hide screen ccg
    $ luna_cum = 11
    $ genie_base = "characters/genie/base/base.webp"
    #$ luna_wear_cum = True

    hide screen blkfade
    with d5

    return


label ll_pf_blowjob_T1_slapping: # Call label
    call hide_characters
    show screen blkfade
    with d5

    ">You quickly take out your hard cock and slap it against Luna's naive nose a few times."

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"genie_robe.webp"
    $ lun_cg_overlay      = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0

    $ lunCG(pupil='dick', eye='excited', mouth='base', eyebrow='sad', cheeks='blush', pos=1, extra_1='blank', extra_2='blank', extra_3='blank', tears='blank', body='base')

    show screen luncg
    hide screen blkfade
    with d5

    m "I expect you to make it up to my cock miss lovegood."
    $ lunCG(pupil='up',eye='wide', mouth='open')
    lun "Oh no, is he upset with me?"
    m "Very... I think he'll need a lot of attention before feeling any better."
    $ lunCG(pupil='dick',eye='excited', mouth='base')
    lun "*Mmmm*, what sort of attention?"
    $ lunCG(eye='excited', xpos=20, ypos=20)
    ">You place the tip of your cock against the airheaded girl's lips."
    m "*Shhhh*..."
    $ lunCG(pupil='up')
    ">You slowly start rubbing the tip over her soft lips, a drop of pre-cum smearing across them like lip gloss."
    m "Why don't you start with a nice kiss?"
    lun "..."
    $ lunCG(pupil='dick',eye='closed', mouth='open_tongue')
    ">Luna doesn't even acknowledge you with a response, instead preferring to lose herself in the act of making out with your cock..."
    m "*Ughhh*, that's it..."
    $ lunCG(pupil='up', eye='seductive', mouth='sucking', pos=3)
    ">Luna's eyes drift up as she slowly envelops the tip of your cock, her tongue rushing forward to begin licking it rapidly..."
    m "*Mmmm*... That's a good start... He might forgive you after all..."
    $ lunCG(eye='closed', pos=3)
    lun "*Hyyy*!"
    $ lunCG(pupil='dick', eye='seductive', mouth='open', pos=1)
    ">In a moment of joy, Luna takes your cock from her mouth before unleashing a flurry of kisses on the tip..."
    $ lunCG(pupil='up', eye='wide', mouth='base', pos=1)
    $ renpy.play('sounds/kiss.mp3')
    lun "Thank you,{w=0.2}{nw}"
    $ renpy.play('sounds/kiss.mp3')
    lun "Thank you,{fast} thank you,{w=0.2}{nw}"
    $ renpy.play('sounds/kiss.mp3')
    lun "Thank you, thank you,{fast} thank you!"
    m "If you really want him to forgive you, maybe put him back in your mouth..."
    lun "Okay!"
    $ lunCG(pupil='dick', eye='angry', mouth='sucking', pos=4)
    ">Luna thrusts her head forwards, swallowing half of your cock while running her tongue along the underside."
    m "*mmmm*"
    $ lunCG(pupil='right', pos=6)
    m "*Ughhh*... that's it...{w=0.3} keep going... just like that..."
    lun "*hhhkkyyy*..."

    #Maybe have a loop here
    ">You feel your load slowly start to build as Luna lovingly works your shaft."

    menu:
        "-Blow it on her face-":
            $ lunCG(pupil='up', eye='wide', pos=8)
            g9 "Alright slut, here it comes!"

        "-Shoot it down her throat-":
            $ lunCG(pupil='dick', pos=8)
            g9 "Ugh...{w=0.3} You are just too good at this..."
            $ lunCG(pos=10)
            g9 "I don't think I can help myself..."
            ">With that you put your hand on the back of Luna's head, grabbing a handful of her blonde locks before pulling her forward and pushing your cock into her throat."
            $ lunCG(pupil='up', eye='wide', pos=6, extra_3='hand')
            lun "!!!"
            $ lunCG(pupil='ahegao', eye='angry', pos=12)
            g9 "*Ughh* that's the fucking spot!"
            $ lunCG(pos=6)
            lun "..."
            $ lunCG(pupil='up', pos=12)
            g9 "This is what you deserve after what you did last time!"
            $ lunCG(pos=5)
            lun "..."
            $ lunCG(pupil='dick', pos=13)
            g9 "Not that you'll mind, you nasty little freak..."
            $ lunCG(pos=6)
            g9 "I bet you're loving this, aren't you?"
            $ lunCG(pupil='dick', eye='seductive', pos=11)
            lun "{heart}{heart}{heart}"
            $ lunCG(pupil='right', pos=5)
            g9 "Cumslut that you are..."
            $ lunCG(pos=13)
            g9 "Here's your reward!"
            $ lunCG(pupil='ahegao', eye='wide', pos=15)
            ">With that, you unleash a colossal load down her throat!"
            $ lunCG(pos=7)
            call cum_block
            pause 1.0
            lun "!!!"
            $ lunCG(pos=15)
            g9 "*Ughh*... my balls have been aching ever since you drained them, you little semen demon!"
            $ lunCG(pos=6)
            g9 "This should be a good chance to empty them..."
            $ lunCG(pos=3)
            ">You tighten your grip on her hair, pulling her head back until just the tip of your cock rests in her mouth."
            $ lunCG(pupil='up', eye='wide', pos=5)
            g9 "*Mmmm*, this way you should get to taste it too..."
            $ lunCG(pupil='dick')
            ">Almost instantly you fill Luna's cheeks to the brim..."
            $ lunCG(pupil='ahegao')
            lun "{heart}{heart}{heart}"
            $ lunCG(pupil='dick')
            g9 "This isn't too much is it?"
            $ lunCG(pupil='ahegao', eye='wide', pos=15, extra_2='cum_4', tears='mascara')
            ">You pull her head forwards, viciously forcing all the cum pooled in her mouth to come flying out the poor girl's nose..."
            $ lunCG(pupil='ahegao', eye='sad', pos=6)
            g9 "*Mmmm*, I love it when this happens..."
            $ lunCG(pos=14)
            lun "{heart}{heart}{heart}"
            $ lunCG(pos=4)
            g9 "The best part of this is..."
            $ lunCG(pos=15)
            lun "{heart}{heart}{heart}"
            $ lunCG(pos=6, extra_1='cum_2')
            m "I know that this is all you'll be smelling for the next week..."
            $ lunCG(pos=16)
            lun "{heart}{heart}{heart}"
            $ lunCG(pos=6)
            m "It'll find it's way into every nook and cranny of your nose..."
            $ lunCG(pos=15)
            m "And it will be the only thing you'll be able to think about..."
            $ lunCG(pos=7)
            lun "{heart}{heart}{heart}"
            $ lunCG(pos=13)
            m "Is this how much of a dirty little cumslut you really are?"
            $ lunCG(pos=14)
            lun "{heart}{heart}{heart}{heart}{heart}{heart}"
            ">You feel Luna's body starting to violently shudder as her hips spasm and liquid runs down her thighs onto the floor..."
            g9 "Alright slut, here it comes again{b}{/b}!"

    $ lunCG(pos=8)

    menu:
        "\"Shut up and take this!\"":
            $ lunCG(pupil='dick', eye='wide', mouth='open_tongue', extra_1='cum_1', pos=1)
            ">You begin firing off one of the largest loads of your life, taking care to make sure every square inch of the girl receives a thick coating of spunk."
            call cum_block
            $ lunCG(extra_1='cum_3', eye='mad')
            g9 "Ugh... this is what you deserve."
            $ lunCG(pupil='up', eye='seductive')
            lun "Why?"
            g9 "You know why!"
            $ lunCG(pupil='dick', extra_1='cum_3')
            g9 "If you act like a filthy cumslut then you should expect to be treated like one..."
            $ lunCG(pupil='ahegao', eye='angry')
            lun "..."
            ">Your orgasm comes to a close..."
            $ lunCG(mouth='base', eye='sad')
            g9 "*Mmmm*... I think i might have treated you more like a cumrag if I'm being honest..."

        "\"Do an ahegao face!\"":
            $ lunCG(pupil='up', eye='wink', mouth='open_tongue', extra_1='cum_1', pos=1)
            lun "A what face?"
            g9 "Just stick your tongue out and look up while doing a silly face!"
            $ lunCG(pupil='left', eye='sad', mouth='pout')
            lun "?"
            $ lunCG(pupil='ahegao', eye='sad', mouth='open_tongue')
            lun "Ah..."
            g9 "Oh that's it! Here it comes you hungry little cumslut!"
            ">You begin firing a huge load, coating the poor girl in a thick layer of cum..."
            call cum_block
            $ lunCG(pupil='dick', eye='sad', mouth='open_tongue', extra_1='cum_3')
            lun "{heart}{heart}{heart}"
            g9 "ugh yes...{w=0.3} take this slut..."
            lun "Ah..."

        "\"Cry!\"":
            $ lunCG(pupil='up', eye='sad', mouth='pout', pos=1)
            lun "Why?"
            g9 "Do you want to get covered in cum or not?"
            $ lunCG(pupil='down', eye='sad', mouth='pout', pos=1)
            lun "You mean if I don't cry..."
            $ lunCG(pupil='left', eye='sad', mouth='open', tears='tears')
            lun "You won't cover me in wrackspurts?"
            g9 "Well--"
            $ lunCG(pupil='up', eye='wide', mouth='wide')
            lun "*sob* That's so mean sir! *sob*"
            $ lunCG(pupil='dick', eye='sad', mouth='open')
            lun "*sob* You'd make me go to class without... *sob*"
            lun "*sob* You'd have so many left in you! *sob*"
            g9 "Ugh, that's it slut! Here it comes!"
            $ lunCG(pupil='up', eye='sad', mouth='pout')
            lun "*sob* Yee-ee-s *sob*"
            ">With that, you begin firing a huge load, coating the poor girl in a thick layer of cum..."
            call cum_block
            $ lunCG(pupil='ahegao', eye='wide', mouth='base', extra_1='cum_3')
            $ lunCG(pupil='ahegao', eye='closed', mouth='base')
            lun "*sob* {heart} *sob* {heart} *sob* {heart} *sob*"
            $ lunCG(pupil='ahegao', eye='seductive')
            g9 "ugh yes...{w=0.3} take this, slut..."
            $ lunCG(pupil='dick')
            lun "*sob* *mmmm*... *sob*"
            $ lunCG(pupil='up')
            g9 "OH fuck...{w=0.3} That shouldn't feel so good..."
            $ lunCG(pupil='up', eye='wink', mouth='open')
            lun "why not?"
            $ lunCG(pupil='dick', eye='wide', mouth='pout')
            m "*Shhh*..."
            $ lunCG(pupil='up', eye='wide', mouth='pout')
            ">You place the tip of your cock against her lips to silence the cum-soaked girl..."

    $ lunCG('open', 'angry', 'sad', 'dick', pos=2)
    lun "wow..."
    $ lunCG(pupil='up')
    lun "You're..."
    $ lunCG('base', 'seductive', 'sad', 'up', pos=0)
    lun "You're just the {b}best{/b}!"
    $ lunCG(pupil='up', eye='closed', mouth='open_tongue', pos=1)
    ">Luna leans forward, placing a kiss on the end of your cock before quietly whispering something to it..."
    $ lunCG(pupil='dick', eye='angry', mouth='open')
    lun "{size=-5}Thank you...{/size}"
    $ lunCG(pupil='up', eye='wink', mouth='base', pos=1)
    lun "Now, I think I better be going sir..."
    $ lunCG('base', 'angry', 'angry', 'dick')
    lun "Unless you have any more wrackspurts that you need me to take care of..."
    $ lunCG('base', 'wink', 'sad', 'up')
    m "For goodness sake girl!"
    lun "..."
    $ lunCG(pupil='up', eye='closed')
    m "You can go now..."
    $ lunCG(pupil='up', eye='closed', mouth='open')
    lun "Yes, sir..."

    hide screen luncg
    show screen blkfade
    with d5

    call lun_chibi("stand", "desk", "base")
    call lun_main("","base","happyCl","base","mid", cheeks="blush", xpos="mid", ypos="base")

    $ luna_cum = "12"
    #$ luna_wear_cum = True
    hide screen blkfade
    with d5

    m "Aren't you forgetting something?"
    call lun_main("Probably! I'm not the best when it comes to that.","soft","seductive","sad","down", cheeks="blush")
    m "Don't you think you should clean yourself off a little before you head back to your room?"
    call lun_main("Oh, don't worry sir, I'm not going to my room, I'm going to the potions lab.","smile","happyCl","base","mid", cheeks="blush")
    call lun_main("Oh, I {i}did{/i} forget something!","soft","wide","base","mid", cheeks="blush")
    m "What's that?"
    call lun_main("What's a slut, sir?","soft","wink","base","mid", cheeks="blush")
    m "A slut?"
    call lun_main("Yes... You called me a slut when I was getting rid of the wrackspurts!","smile","happyCl","base","mid", cheeks="blush")
    m "Oh, *uhh*... It's someone who loves...{w=0.3} doing what we're doing..."
    call lun_main("Really? So does that mean a cumslut is someone who loves cum?","base","seductive","base","mid", cheeks="blush")
    m "Yep."
    call lun_main("Then I must be the biggest cumslut in the whole wide world!","smile","happyCl","base","mid", cheeks="blush")
    m "..."
    call lun_main("Well, too-da-loo sir!","base","happyCl","base","mid", cheeks="blush")

    call lun_walk(action="leave")

    return


label ll_pf_blowjob_T1_facefuck: # Call label
    # Luna facefuck transitional part
    call hide_characters
    show screen blkfade
    with d5

    ">You put your hand on the back of the unsuspecting girl's head..."

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_overlay      = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0

    $ lunCG('open', 'wide', 'base', 'up', extra_1='blank', extra_2='hand', extra_3='blank', pos=1, cheeks='blush', tears='blank', body='base')

    show screen luncg
    hide screen blkfade
    with d5

    $ lunCG('', 'base', '', 'up')
    m "I was thinking we could have another lesson today..."
    $ lunCG('base', 'wide', '', 'up')
    lun "Really? What sort?"
    m "Well, today I'll be teaching you what happens when you decide to paralyse your headmaster and suck their cock for hours on end..."
    $ lunCG('base', 'wink', '', 'up')
    lun "Oh... and what's that?"
    m "This happens, miss Lovegood, this happens..."
    $ lunCG(pupil='base', eye='wide', mouth='sucking', pos=14)
    ">With no more warning, you grab a handful of the blonde's locks and pull her head forward, forcing your cock down Luna's throat."
    $ lunCG(pupil='up', eye='wide', pos=7)
    m "You see, I wasn't the biggest fan of having you come in..."
    $ lunCG(pupil='dick', eye='wide', pos=15)
    ">You begin pumping Luna's head back and forth, hitting the back of her throat each time."
    $ lunCG(pupil='ahegao', eye='wide', pos=8, tears='mascara')
    lun "*glck-glck-glck*"
    $ lunCG(pupil='ahegao', eye='angry', pos=14)
    m "paralyse me..."
    $ lunCG(pos=5)
    lun "*glck-glck-glck*"
    $ lunCG(pupil='ahegao', eye='mad', pos=15)
    m "AND THEN PROCEED TO SUCK ME OFF FOR AN ENTIRE DAY!"
    $ lunCG(pupil='ahegao', eye='seductive', pos=6)
    lun "*glck* {heart} *glck* {heart} *glck* {heart}"
    $ lunCG(pupil='ahegao', eye='seductive', pos=15)
    m "And if you want cum so much, just beg for it like a normal cumslut!"
    $ lunCG(pupil='ahegao', eye='seductive', pos=6)
    lun "*glck* {heart} *glck* {heart} *glck* {heart}"
    $ lunCG(pupil='up', eye='wink', pos=14)
    m "Speaking of, ready for your first load, slut?"
    $ lunCG(pupil='dick', eye='wide', pos=6)
    lun "*glck* {heart} *glck-mmmhhmmmm-glck* {heart}"
    $ lunCG(pupil='ahegao', eye='seductive', pos=15, extra_1='cum_1')
    m "Good girl! Here it comes!!!"
    $ lunCG(pupil='ahegao', eye='seductive', pos=6)
    ">You start shooting the first of many loads down Luna's throat."
    $ lunCG(pupil='ahegao', eye='angry', pos=13)
    m "Ughhh... here you are, slut... here's your favourite meal!"
    $ lunCG(pupil='ahegao', eye='seductive', pos=6, extra_1='cum_3')
    lun "*glck* {heart} *glck* {heart} *mmmhhmmmm-glck* {heart} *glck*"
    $ lunCG(pupil='ahegao', eye='mad', pos=14)
    ">After the first three shots, you feel your orgasm start to subside."
    $ lunCG(pupil='ahegao', eye='seductive', pos=6)
    m "Ughh... I don't think that's going to be enough of a load to satisfy a nasty little cumslut like you now, is it?"
    $ lunCG(pupil='dick', eye='base', pos=16)
    lun "*glck* {heart} *glck* {heart} *glck* {heart}"
    $ lunCG(pupil='up', eye='seductive', pos=6)
    ">You muster what little genie magic you can and focus it on your empty balls."
    $ lunCG(pupil='ahegao', eye='seductive', pos=15)
    lun "*glck* {heart} *glck!!!* ... *Gulp* {heart} *glck* {heart}"
    $ lunCG(pupil='dick', eye='wide', pos=16)
    ">Your weakening cock to comes back to life, firing a inhumane volley of cum into the girl's stomach."
    $ lunCG('sucking', 'wide', 'sad', 'ahegao', pos=6, extra_3='cum_4')
    m "That's better! This is what a cumslut like you deserves!"
    $ lunCG(pos=10)
    ">Both of Luna's hands have managed to sneak under her skirt and are now a blur of movement..."
    $ lunCG(pos=3)
    lun "*Gulp* {heart} *glck* {heart} *Gulp* {heart} *glck* {heart}"
    $ lunCG(pos=11)
    m "Ughhh... If you had just asked..."
    $ lunCG(pos=4)
    lun "*Gulp* {heart} *glck* {heart} *Gulp* {heart} *glck* {heart}"
    $ lunCG(pos=14)
    m "Instead I have to teach you a lesson."
    $ lunCG(pos=1)
    ">You pull luna's limp head off your cock as it continues to fire off round after round..."
    $ lunCG('wide', 'closed', '', 'up')
    lun "*GASP* *cough* *cough* *cough*"
    $ lunCG('open', 'wide', '', 'up')
    m "Mmmmm, that's it, just let me cover you..."
    $ lunCG('base', 'wide', '', 'up')
    lun "..."
    m "Anything to say for yourself, cumslut?"
    $ lunCG('pout', 'wink', '', 'left')
    lun "..."
    $ lunCG('open', 'sad', '', 'dick')
    lun "{size=-5}T-Thank you...{/size}"
    m "What was that? I don't think I could hear you through all that cum..."
    $ lunCG('open', 'sad', '', 'up')
    lun "Thank you sir..."
    m "(what?)"
    $ lunCG('open', 'sad', '', 'left')
    lun "You're the only person who has taken me seriously with the wrackspurts..."
    $ lunCG('base', 'seductive', '', 'up')
    lun "And you've been so nice..."
    $ lunCG('open', 'wide', '', 'dl')
    lun "And taught me so many things..."
    $ lunCG('open', 'sad', '', 'down')
    lun "And this cum..."
    $ lunCG('open', 'wide', '', 'up')
    lun "It's so good! It's as if it's made of pure magic!"
    $ lunCG('open', 'base', '', 'dick')
    lun "Thank you, thank you, thank you!"
    $ lunCG(pupil='up')
    lun "You're the best genie ever!"
    $ lunCG(pupil='dick', eye='closed', mouth='sucking', pos=3)
    ">With that, Luna willingly resumes sucking on your cock, shamelessly slobbering over every inch of it..."
    $ lunCG(pupil='ahegao', eye='seductive', mouth='sucking', pos=4)
    m "ugh... I'm glad you've learned your lesson."
    m "I {i}am{/i} the best genie ever..."
    play sound "sounds/scratch.wav"
    $ lunCG(pos=6)
    m "Wait...{w=0.5} Did you just say {b}GENIE{/b}?!"
    $ lunCG(pupil='up', eye='closed', mouth='open', pos=1)
    lun "*Slrp-pop*!"
    $ lunCG(pupil='up', eye='wink', mouth='pout', pos=1)
    lun "*Mhmmm*? I mean you are a genie, aren't you?"
    m "Well, yes..."
    $ lunCG('base', 'base', '', 'up')
    m "But how do you know that? I thought I looked like Dumbydoo or whoever..."
    $ lunCG('base', 'closed', '', 'up')
    lun "Only when I'm not wearing my spectrespecs!"
    m "Those glasses?... So you've known the whole time?"
    $ lunCG('open', 'base', '', 'dl')
    lun "Well, I didn't know you were a genie until I tasted this..."
    $ lunCG(pupil='ahegao', eye='seductive', mouth='open_tongue', pos=2)
    ">She gives the end of your dick a quick lick."
    $ lunCG(pupil='up', eye='wide', mouth='base', pos=1)
    lun "I don't think any other creature could make something so tasty..."
    $ lunCG('open', 'closed', '', 'up')
    lun "Not even a unicorn..."
    m "So you don't care I'm a genie?"
    $ lunCG('base', 'base', '', 'up')
    lun "Nope! Not unless it bothers you..."
    m "As long as you keep sucking cock like that, you can think I'm the prince of persia..."
    m "Just don't expect any wishes."
    $ lunCG('pout', 'wink', '', 'dl')
    lun "Oh... Why not?"
    m "You have to rub my lamp to get wishes and I'm pretty sure that thing is all the way back in Agrabah."
    $ lunCG('base', 'seductive', '', 'dick')
    lun "*Awww*... rubbing this doesn't count?"
    ">Luna gives your cock a playful few strokes."
    m "Afraid not, although this job would be a lot better if it did."
    $ lunCG('base', 'closed', '', 'up')
    lun "Oh well... I guess that your yummy cummy will just have to do."
    $ lunCG(pupil='dick', eye='mad', mouth='base', eyebrow='angry')
    lun "Speaking of..."
    $ lunCG('sucking', 'angry', 'sad', 'ahegao', pos=14)
    ">Luna throws her head onto your cock again."
    m "Steady on there girl... Don't you think you've had enough cum for one day?"
    $ lunCG('pout', 'sad', 'sad', 'up', pos=1)
    lun "What? Already? But there's still so much magic..."
    $ lunCG('base', 'wide', '', 'dick')
    lun "{heart}{heart}{heart}"
    $ lunCG('pout', 'sad', '', 'up')
    lun "Can't we keep going? There must be so many wrackspurts left in you..."
    m "(Oh right... those things...)"
    $ lunCG('open', 'sad', '', 'up')
    m "Quite right... it seems that you're bringing in more {i}wookiesports{/i} than I can deal with..."
    m "I'll have to teach you an advanced method for getting rid of them in both of us at once."
    $ lunCG('base', 'wide', '', 'up')
    lun "Really? You have something like that?"
    $ lunCG('open', 'sad', '', 'up')
    lun "That could solve the school's wrackspurt infestation in no time!"
    $ lunCG('pout', 'seductive', '', 'up')
    lun "could you teach it to me now? Pleeeease..."
    m "Ugh... I think I need a bit of a nap after that... not to mention you could use a shower..."
    $ lunCG('base', 'wink', '', 'up')
    lun "And waste this? I told you that I'm using it to make a perfume to ward off those wrackspurts."
    $ lunCG('pout', 'seductive', '', 'dl')
    lun "I'm even thinking of selling it to the other students to help slow down those nasty things..."
    m "Whatever... just do it somewhere else... I need a nap..."
    $ lunCG('base', '', 'base', 'up')
    lun "Okay, Mister Genie, sir!"
    m "Genie is fine."
    m "And only call me that when we're alone in this office. Outside, I'm Dumbledore."
    $ lunCG('base', '', 'sad', 'dick')
    lun "Of course... Have a nice nap,{w=0.5} Genie..."

    hide screen luncg
    show screen blkfade
    with d5

    call lun_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d5

    call lun_walk(action="leave")

    return


label ll_pf_blowjob_T1_summon:
    # You summon Hermione while Luna sucks you off under your desk.

    call hide_characters
    show screen blkfade
    with d5

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"genie_robe.webp"
    $ lun_cg_overlay      = lun_cg_path+"blank.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0
    $ lunCG(pupil='dick', eye='excited', mouth='sucking', eyebrow='sad', cheeks='blush', pos=5, extra_1='cum_3', extra_2='hand', extra_3='blank', tears='mascara', body='base')

    show screen luncg
    hide screen blkfade
    with d5

    g4 "{size=+5}You greedy little slut! Take this!{/size}"
    $ lunCG('', 'wide', '', 'ahegao', pos=12)
    lun "*gulp* *gulp* *gulp*"
    $ lunCG('', 'angry', '', 'ahegao', pos=16)
    ">You fire your third load of the day into Luna's hungry mouth."
    $ lunCG('', 'seductive', '', 'up', pos=6)
    lun "*gulp* {heart} *gulp* {heart} *gulp*"
    $ lunCG('', 'seductive', '', 'dick', pos=9)
    m "Fuck, that's good... Ugh..."
    $ lunCG('', 'sad', '', 'dick', pos=3, extra_2='blank')
    ">Sensing that your orgasm has ended, Luna begins to slow down, sucking the end of your cock to nurse it back to health..."
    lun "*glck* {heart} *slrp* {heart} *glck*"
    m "Ugh... I should... mmmm... do some work... or something..."
    $ lunCG('', 'wink', '', 'up', pos=4)
    lun "*glck* {heart} *slrp* {heart} *glck*"

    menu:
        "-Try and do some paperwork-":
            ">Not wanting to lose the entire day to Luna's blowjobs, you begin to write out a report for the ministry."
            m "Yes... school activities..."
            $ lunCG('', 'seductive', '', 'dick', pos=6)
            lun "*glck* {heart} *slrp* {heart} *glck*"
            m "..."
            "*scribble*{w=0.5} *scribble*{w=0.5} *scribble*{w=0.5} *scribble*"
            m "There, all done!"
            $ lunCG('sucking', 'wink', 'base', 'up', pos=13)
            lun "*glck* {heart} *slrp* {heart} *glck*"
            $ lunCG('', 'seductive', '', 'down', pos=5)
            m "(It only took three hours and twice as many orgasms)"
            $ lunCG('', 'angry', '', 'dick', pos=10)
            lun "*glck* *slrp* *glck*"
            m "Just a quick read-through before I send this off to the ministry..."
            m "..."
            $ lunCG('', 'seductive', '', 'up', pos=6)
            lun "*glck* *slrp* *glck*"
            m "......"
            $ lunCG('wide_tongue', 'seductive', '', 'dick', pos=1)
            lun "*Slrp* *pop*"
            $ lunCG('base', 'wink', '', 'up', pos=1)
            lun "How's the report, [lun_genie_name]?"
            m "Unless you consider a three page report about how you suck cock useful..."
            m "Then it's trash..."
            $ lunCG('open', 'wide', 'sad', 'up')
            lun "Wait... You wrote a report on how I..."
            $ lunCG('', 'seductive', '', 'up')
            lun "Can I have it? Please, [lun_genie_name]!"
            m "Sure, it's not like I can send it to the ministry anyway."
            $ lunCG('base', 'closed', 'base', 'up',)
            lun "Oh thank you, thank you, thank you! I can't wait to read it tonight."
            m "Until then..."
            $ lunCG('base', 'wide', 'base', 'dick',)
            lun "Oh, right!"
            $ lunCG('sucking', 'angry', 'sad', 'up', pos=13)
            lun "*glck* {heart} *slrp* {heart} *glck*"
            m "Ugh... that's it slut..."

        "-Summon someone-":
            pass

    m "(Maybe I should bring Hermione up here while this is going on...)"
    # m "(Maybe I should bring someone up here while this is going on...)"
    # menu :
    #     "-Hermione-":
    #         pass

    # First time Hermione is brought up
    # Will need a check if Luna intro is is moved
    m "(That slut will probably get off on it.)"
    $ lunCG('sucking', 'seductive', 'sad', 'dick', pos=6)

    ">Without a second thought, you summon Hermione up to your office to take your mind off Luna's endless cocksucking."

    #TODO Split screen uses disembodied dick, needs custom image to fix
    hide screen luncg
    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base_2.webp" # Split-screen
    $ lun_cg_genie        = "blank"
    $ lun_cg_xpos_abs     = -275
    show screen luncg

    call her_main("You wanted to see me [genie_name]?", "smile", "happyCl", "base", "mid", xpos="base", ypos="base", trans=fade)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    m "Mmmmm... That I did..."
    $ lunCG(pupil='ahegao', eye='angry', pos=13)
    call her_main("Ugh... This room reeks! Open a window or something...", "disgust", "squint", "base", "mid")
    m "The window doesn't shut."
    $ lunCG(pos=6)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    call her_main("Then maybe try cumming a bit less...", "disgust", "narrow", "annoyed", "mid")
    m "If I do that I'm not sure you'll be able to win the house cup..."
    $ lunCG('', '', '', 'dick', pos=14)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    $ lunCG(pos=6)
    m "Speaking of which..."
    $ lunCG(pos=13)
    call her_main("oh...", "smile", "narrow", "worried", "mid_soft")
    $ lunCG(pos=8)
    call her_main("What will it be today then [genie_name]?", "smile", "squint", "base", "mid")
    $ lunCG(pos=14)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    $ lunCG(pos=6)
    call her_main("Do you want me to suck your cock?", "base", "narrow", "base", "down")
    $ lunCG(pos=12)
    call her_main("Or maybe you want to bend me over your desk again... {heart}{heart}{heart}", "smile", "squint", "angry", "mid")
    $ lunCG(pos=8)
    m "I love your enthusiasm... but let's just start with a nice look at your tits..."
    $ lunCG(pos=15)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    call her_main("Oh... alright then...", "soft", "narrow", "worried", "mid_soft")

    call play_music("playful_tension") # SEX THEME.
    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")
    with d5
    pause .5
    call her_main("", "soft", "narrow", "base", "down")
    call ctc

    $ lunCG('sucking', 'seductive', 'sad', 'dick', pos=13)
    m "Ugh... that's it, slut..."
    $ lunCG(pos=8)
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    call her_main("...", "smile", "narrow", "worried", "down")
    m "Mmmm... Make them jiggle!"
    $ lunCG(pupil='up', eye='wide', pos=16)
    ">You start bucking your hips to facefuck Luna while Hermione unknowingly spurs you on..."
    $ lunCG(pos=13)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=15)
    m "Oh fuck yes... just like that..."
    $ lunCG(pos=11)
    call her_main("Is something going--", "upset", "squint", "base", "mid")
    m "Shut up and get naked [hermione_name]!"
    $ lunCG(pos=15)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=15)
    call her_main("...", "smile", "narrow", "base", "down")
    $ lunCG(pos=10)
    ">Hermione stares at your desk while stripping down to nothing."
    pause 0.2
    $ lunCG(pos=13)
    $ hermione.strip("bra")
    pause 0.5
    $ lunCG(pos=10)
    ">One piece after another..."
    $ lunCG(pos=15)
    $ hermione.strip("bottom")
    pause 0.5
    $ lunCG(pos=10)
    $ hermione.strip("panties")
    pause 0.5
    if hermione.is_any_worn("clothes"):
        $ hermione.strip("all")
        pause 0.5
    $ lunCG(pos=12)
    call her_main("So... who's hiding under the desk?", "smile", "narrow", "base", "down")
    $ lunCG(pos=9)
    lun "*glck* *slrp* *glck*"
    m "Ugh... what do you mean?"
    $ lunCG(pos=16)
    call her_main("Please, I can hear them sucking you off from here.", "smile", "narrow", "base", "mid_soft")
    $ lunCG('', 'wide', '', 'dl', pos=9)
    lun "*glck* *slrp* *glck*"
    $ lunCG('', '', '', 'dick', pos=12)
    call her_main("I'm just curious who you managed to get...", "soft", "narrow", "base", "down")
    $ lunCG(pos=10)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=13)
    call her_main("Anyone I know?", "smile", "happy", "base", "mid")
    m "I believe... argh... you've met..."
    $ lunCG(pos=7)
    call her_main("Hmmmm... It's not a slytherin is it?", "upset", "squint", "base", "mid")
    m "Which colour are they again?"
    $ lunCG(pos=14)
    call her_main("The green ones you decrepit old perv!", "open", "base", "angry", "mid")
    $ lunCG(pos=9)
    lun "*glck* *slrp* *glck*"
    $ lunCG('', '', '', 'up', pos=15)
    m "Mmmm... she's not a slytherin then..."
    call her_main("Hmmm... She certainly doesn't have any shame by the sounds of it, so she's not a hufflepuff...", "upset", "narrow", "angry", "R")
    $ lunCG(pos=10)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=13)

    #TODO Make Hermione's posing fit better with the dialogue (until walk around desk)
    call her_main("It has to be a Gryffindor! They're the only ones brave enough to try this...", "open", "happy", "base", "mid_soft")
    lun "*glck* *slrp* *glck*"
    call her_main("Ginny, is that you?! I told you to stay away from Dumbledore!", "smile", "happyCl", "base", "mid")
    m "Wrong, she's in the blue house."
    call her_main("A ravenclaw? But which ravenclaw girl would be stupid enough to--", "smile", "happyCl", "base", "mid")
    call her_main("...", "smile", "happyCl", "base", "mid")
    lun "*glck* *slrp* *glck*"
    #TODO Check if Hermione has caught you with Luna before and the hat was involved (doesn't happen on normal path)
    call her_main("It's Luna again isn't it?", "smile", "happyCl", "base", "mid")
    m "..."
    call her_main("That hat better not have been involved!", "smile", "happyCl", "base", "mid")
    m "Scout's honour."
    call her_main("We'll see about that...", "smile", "happyCl", "base", "mid")

    call hide_characters
    show screen blkfade
    with d5

    ">Before you can say anything, Hermione walks around your desk to check on Luna."

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base.webp"
    $ lun_cg_genie        = lun_cg_path+"genie_robe.webp"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0

    $ lunCG('wide_tongue', 'seductive', '', 'dick', pos=1, body='base')

    show screen luncg
    hide screen blkfade
    with d5

    lun "*slrp* *pop*"
    $ lunCG('base', 'wink', '', 'left', pos=1)
    lun "Hi Hermione! Nice work guessing that it was me!"
    her "..."
    her "What are you doing Luna?"
    $ lunCG('base', 'angry', 'mad', 'dick')
    lun "Getting rid of wrackspurts! There's so many!"
    her "..."
    her "God you're stupid... well, At least I know why the room stinks of cum now..."
    $ lunCG('base', 'wide', 'sad', 'ahegao')
    lun "Isn't it great? I'm thinking about using it to make a perfume!"
    her "(Idiot)"
    her "At least I know this is the real you..."
    $ lunCG('', 'wink', '', 'left')
    lun "You do? Thanks for checking, sometimes I'm not so sure myself!"
    her "..."
    $ lunCG('base', 'angry', 'mad', 'dick')
    lun "Now if it's okay Hermione, I think I better get back to work, I've got only six rounds out so far."

    show screen blkfade
    with d5

    ">Without any hesitation, Luna returns to shamelessly sucking your cock in front of Hermione."

    $ lun_cg_path         = "images/CG/luna_desk2/"
    $ lun_cg_base         = lun_cg_path+"base_2.webp" # Split-screen
    $ lun_cg_genie        = "blank"
    $ lun_cg_xpos_abs     = -275

    $ lunCG('sucking', 'seductive', 'angry', 'dick', pos=14, body='base')

    call her_main()

    hide screen blkfade
    with d5

    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=8)
    call her_main("Six times already? How long does she stay under there?", "disgust", "slit", "low", "stare")
    m "She'd live under there if she could..."
    $ lunCG('', '', '', 'ahegao', pos=13)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=5)
    call her_main("So what? Did you call me up here to give you a little show while Luna Lovegood sucks you off all day?", "upset", "squint", "base", "mid")
    $ lunCG(pos=8)
    m "Pretty much... It was getting a little boring with just the two of us..."
    $ lunCG(pos=13)
    call her_main("Ugh... You're such a pig!", "base", "squint", "base", "mid")
    $ lunCG('', 'angry', '', 'dick', pos=6)
    m "So you don't want to earn some points for your house?"
    $ lunCG(pos=14)
    call her_main("I didn't say no... I just wanted to make sure you know how perverted this is!", "smile", "slit", "low", "stare")
    $ lunCG(pos=8)
    lun "*glck* *slrp* *glck*"
    $ lunCG('', 'wide', '', 'up', pos=12)
    call her_main("You hadn't even locked your door!", "grin", "narrow", "angry", "R")

    # Hermione starts touching herself
    $ hermione.set_pose("masturbate")
    $ hermione.set_body_zorder(armright=3)
    $ hermione.set_body(armleft="on_pussy", armright="on_tits")

    $ lunCG('', 'angry', '', 'up', pos=8)
    call her_main("What if someone else walked in while this was going on?", "grin", "narrow", "angry", "dead")
    $ lunCG(pos=10)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=4)
    call her_main("Do you think they wouldn't be able to hear it?", "grin", "narrow", "base", "dead")
    $ lunCG(pos=8)
    call her_main("To {b}smell{/b} it?", "open_tongue", "narrow", "angry", "dead")
    $ lunCG('', 'mad', '', 'ahegao', pos=14)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=4)
    call her_main("But maybe that's what you two want...", "grin", "narrow", "worried", "down")
    $ lunCG(pos=8)
    call her_main("Maybe you were waiting for someone else to walk in and catch you...", "grin", "narrow", "base", "down")
    $ lunCG(pos=12)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=16)
    call her_main("Is that what you wanted [genie_name]? Some cute little thing to walk in and unknowingly be forced into watching you cum in front of them...", "smile", "narrow", "angry", "dead")
    $ lunCG('', 'wide', '', 'up', pos=13)
    call her_main("To be forced into breathing in this thick musk...", "disgust", "narrow", "angry", "dead")
    $ lunCG(pos=10)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=7)
    call her_main("Imagine if it was a first year? What would you do then?", "grin", "happy", "base", "mid")
    $ lunCG(pos=9)
    call her_main("Would you do the right thing and send them away?", "smile", "happy", "base", "mid")
    $ lunCG('', 'mad', '', 'dick', pos=11)
    lun "*glck* *slrp* *glck*"
    call her_main("Or would you make them stay...", "grin", "squint", "base", "mid")
    $ lunCG(pos=13)
    g4 "Mmmm..."
    $ lunCG(pos=15)
    lun "*glck* *slrp* *glck*"
    $ lunCG(pos=16)
    call her_main("Make them watch while you bust your seventh load of the day down Luna's throat!", "grin", "narrow", "base", "mid_soft")
    $ lunCG(pos=14)
    g4 "ARGHH, this is it you sluts!"
    $ lunCG('sucking', 'wide', 'sad', 'right', pos=16)
    ">You start shooting another gargantuan load into Luna's mouth."
    $ lunCG('', '', '', 'up')
    lun "*glp* *glp* *glp*"
    $ lunCG(pupil='ahegao')
    g4 "Mmmm..."
    $ lunCG('', 'seductive', '', 'ahegao')
    lun "*glp* *glp* *glp*"
    $ lunCG('sucking', 'angry', 'angry', 'ahegao')

    # Reset pose
    $ hermione.set_body_zorder(armright=0)
    $ hermione.set_body(armleft="down", armright="down")
    $ hermione.set_pose(None)

    call her_main("I guess that answers that...", "smile", "happyCl", "base", "mid")
    call her_main("I think I better be going then.", "smile", "happyCl", "base", "mid")
    m "Ugh... yes... good... bye..."
    $ lunCG('sucking', 'seductive', 'sad', 'ahegao', pos=7)
    lun "*glck* *slrp* *glck*"
    call her_main("Have a nice day you two!", "smile", "happyCl", "base", "mid")
    $ lunCG('sucking', 'seductive', 'sad', 'dick', pos=3)

    ">Your vision starts to fade to black as Luna suckles your wilting cock back to life..."

    call hide_characters
    hide screen luncg
    show screen blkfade
    with d5

    ">By the time you wake up, Luna is gone and the sun has set."
    ">All that's left is a puddle of cum under the desk and an aching in your balls."

    call lun_chibi("hide")
    call gen_chibi("sit_behind_desk")

    $ hermione.wear("top", "bra", "bottom", "panties")

    hide screen blkfade
    with d5

    return


label ll_pf_blowjob_T1_old_writing: # Not in use. Old writing.

    m "Well... Now that you mention it... What's your class schedule like for today?"
    call lun_main("Hmmmm... not too busy. I have divination at eleven and... um... herbology at two!","base","happyCl","sad","mid",cheeks="blush")
    m "I think I might need to write you a note explaining your absence from class then."
    call lun_main("Really? Why's that?","base","happyCl","sad","mid",cheeks="blush")
    m "Those nasty wickerspoons are bothering me again, quite badly I'm afraid."
    call lun_main("They are?!","base","happyCl","sad","mid",cheeks="blush")
    m "Indeed. I'm thinking you'll need to spend the whole day seeing to them."
    call lun_main("the {b}whole{/b} day?...","base","happyCl","sad","mid",cheeks="blush")
    m "Unless, of course, you'd prefer to go to your classes?"
    call lun_main("No, no, no! I'll help you!","base","happyCl","sad","mid",cheeks="blush")
    m "Fantastic... Shall we begin then?"
    call lun_main("{b}yes{/b}... thank you [lun_genie_name]...","base","happyCl","sad","mid",cheeks="blush")
