
# Slytherin Luna either reverts back to her old self or remains changed (forever)
label luna_reversion_event:
    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if lun_whoring <= 9:
        $ lun_whoring += 1

    call play_music("chipper_doodle")

    $ luna_zorder = 16 # Needed for handjob pose

    if lun_sub > lun_dom:
        # Sub intro
        m "[luna_name]..."
        call lun_main("yes, [lun_genie_name]...","normal","suspicious","sad","down")
        m "Do you know what a handjob is?"
        call lun_main("What?","upset","base","mad","mid")
        m "It's where you wrap your hand around--"
        call lun_main("I know what they are!","pout","wide","angry","mid")
        m "Fantastic!"
        call lun_main("...","upset","angry","angry","R")

    else:
        # Dom intro
        m "[luna_name]?"
        call lun_main("yes, [lun_genie_name]...","normal","base","angry","R")
        m "Do you happen to know what a handjob is?"
        call lun_main("...","normal","angry","angry","mid")
        m "..."
        m "Well if it's not too much trouble..."
        call lun_main("...","normal","angry","angry","R")
        call lun_main("Go on...","normal","angry","angry","R")

    menu:
        "-Tell her to give you a handjob-" if lun_sub >= 7:
            $ current_payout = 80
            if lun_sub <= 8:
                $ lun_sub += 1
            $ luna_choice = 1
            m "Well seeing as how you're familiar with the concept, how about a practical demonstration."
            call lun_main("...","upset","suspicious","angry","R")
            call lun_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?","upset","wide","raised","mid")
            call lun_main("It's bad enough that I have to stand here while you touch yourself...","normal","mad","angry","mid")
            call lun_main("But that's where I draw the line, [lun_genie_name]!","upset","suspicious","mad","mid")
            m "*Hmm*..., well alright then, I'm not going to force you into anything."
            call lun_main("Thank you...","upset","suspicious","sad","R")
            m "That will be all for today, [luna_name], you may leave now."
            call lun_main("Alright, [lun_genie_name]...","normal","suspicious","sad","mid")
            call lun_main("(Good work finally standing up to him!)","base","happyCl","sad","R")
            ">Luna turns around to leave your office."
            m "Oh, one last thing..."
            call lun_main("...","normal","angry","sad","mid")
            m "Could you send the first Slytherin girl you see to my office?"
            call lun_main("What! Why?","pout","wide","angry","mid")
            m "Well seeing as how you're not able to give me a little attention, I figure that one of those Slytherin sluts will."
            m "They'll probably even do it for half the price..."
            call lun_main("...","upset","angry","angry","mid")
            call lun_main("......","normal","suspicious","sad","down")
            call lun_main(".........","upset","seductive","sad","mid",tears="soft")
            call lun_main("{size=-5}Fine{/size}...","normal","seductive","sad","down")
            m "What was that, [luna_name]?"
            call lun_main("{size=+5}Fine!{/size} I'll jerk that disgusting, old, filthy, wrinkly old cock of yours!","clench","wide","sad","mid")
            m "Fantastic! Let me just stand up."
            call lun_main("You're despicable...","upset","mad","angry","mid")

        "-Ask for a handjob-" if lun_sub > lun_dom:
            $ current_payout = 120
            if lun_sub <= 8:
                $ lun_sub += 1
            $ luna_choice = 2
            m "Well seeing as how you're familiar with the concept..."
            call lun_main("...","upset","angry","mad","mid")
            call lun_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?","upset","wide","raised","mid")
            call lun_main("It's bad enough that I have to stand here while you touch yourself...","normal","mad","sad","mid")
            m "There'll be a hefty reward..."
            call lun_main("...","upset","suspicious","sad","down")
            call lun_main("......","base","suspicious","sad","R")
            call lun_main("I expect that my father's magazine will also sell a few more copies...","normal","angry","sad","mid")
            m "Of course..."
            call lun_main("Fine...","upset","suspicious","sad","down")
            m "Fantastic! Let me just stand up."
            call lun_main("*Hmph* Don't expect that you'll be cumming anywhere near me though!","upset","mad","mad","mid")

        "-Ask for a handjob politely-" if lun_sub < lun_dom:
            $ current_payout = 160
            if lun_dom <= 8:
                $ lun_dom += 1
            $ luna_choice = 3
            m "Seeing as how you're so skilled at everything you turn your hand towards..."
            call lun_main("*Mhmmm*...","upset","suspicious","angry","R")
            m "I was hoping you could turn your hand towards my cock."
            call lun_main("...","normal","mad","base","R")
            m "please..."
            call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
            call lun_main("Isn't it enough that I let you touch yourself...","upset","suspicious","mad","R")
            m "There'll be a hefty reward..."
            call lun_main("...","upset","mad","mad","R")
            call lun_main("......","normal","mad","angry","mid")
            call lun_main("Well since you asked so nicely...","base","mad","base","mid")
            m "..."
            call lun_main("Get over here...","base","angry","mad","mid")
            m "Fantastic! Let me just stand up."
            call lun_main("(This couldn't get any easier)","base","mad","angry","R")

        "-Beg for a handjob-" if lun_dom >= 7:
            $ current_payout = 200
            if lun_dom <= 8:
                $ lun_dom += 1
            $ luna_choice = 4
            m "Well if it's not too much trouble..."
            call lun_main("*Mhmmm*...","upset","suspicious","angry","R")
            m "I was hoping you could..."
            call lun_main("...","normal","mad","base","R")
            m "give me one..."
            call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
            m "If it's not too much trouble..."
            call lun_main("Well I suppose I probably should.","base","seductive","base","R")
            call lun_main("Who knows who you'll call up here if I don't...","base","mad","mad","mid")
            m "Thank you..."
            call lun_main("...","upset","mad","mad","R")
            call lun_main("......","normal","mad","angry","mid")
            call lun_main("However, I do expect to be fairly compensated...","base","mad","base","mid")
            m "Of course."
            call lun_main("Good. Now Get over here...","base","angry","mad","mid")
            m "Fantastic! Let me just stand up."
            call lun_main("(This couldn't get any easier...)","base","mad","angry","R")
            call lun_main("(I'll be the only person in his will by the end of the month at this rate...)","base","suspicious","mad","mid")

    if luna_choice <= 2:
        jump luna_revert_1
    else:
        jump luna_revert_2


# Reversion event
# Result: Ability to redo all Luna's favours with the real Luna
label luna_revert_1:
    hide screen bld1
    show screen chair_left
    show screen desk
    call gen_chibi("stand", "desk", "base")
    call lun_chibi("stand", "mid", "base")
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    ">You stand up and walk around your desk, standing in front of Luna."
    ">You open your cloak and pull out your cock."

    call gen_chibi("dick_out")
    with d3

    m "Well..."
    call gen_main(None, "grin", "hard", xpos=300, ypos=0)
    call lun_main("...","normal","seductive","base","down")
    ">Luna looks hesitantly at your cock."
    call lun_main("......","normal","closed","sad","down")
    ">She slowly takes a hold of it with her right hand."
    hide screen luna_main
    $ luna_r_arm = 3
    $ luna_xpos = 390
    show screen luna_main
    with d3
    call gen_main("!!!", "grin", "hard", xpos=300, ypos=0)
    call lun_main("It's so big...","base","seductive","sad","down")
    call lun_main("(I can't even fit my hand around it.)","base","seductive","sad","R")
    m "Why don't you try grabbing it with both hands, [luna_name]..."
    call lun_main("Alright...","base","suspicious","sad","down")
    ">Luna slowly wraps both hands around your cock."
    m "*Mmmm*, that's it. Now start moving your hands back and forth."
    call lun_main("......","normal","seductive","base","down")
    ">Luna starts moving her hands back and forth along the length of your cock."
    m "Yes, that's it..."
    call lun_main("...","base","suspicious","sad","down")
    m "*Mmmm*, yes... not bad, [luna_name], have you been practising?"
    call lun_main("What? Of course not!","normal","wide","angry","mid")
    m "well, I expect you to start practising from now on!"
    call lun_main("on what?","normal","angry","raised","mid")
    m "My cock, of course!"
    call lun_main("[lun_genie_name]!","clench","mad","angry","mid")
    m "I'm kidding, [luna_name]."
    call lun_main("oh...","soft","suspicious","sad","R")
    m "But I do expect you to improve..."
    call lun_main("Doesn't this feel good?...","pout","mad","raised","mid")
    m "It's alright..."
    call lun_main("Well, what do I need to do differently?","normal","suspicious","sad","R")

    menu:
        "\"Take your shirt off\"":
            $ luna_choice = 1
            call lun_main("My shirt? Really?","soft","angry","angry","mid")
            m "It'd make this go a lot faster."
            call lun_main("...","upset","suspicious","sad","down")
            call lun_main("Fine...","normal","mad","sad","mid")
            call lun_main("But I expect to be paid extra!","upset","closed","angry","down")
            $ current_payout += 20
            m "It's a deal."
            call lun_main("...","upset","suspicious","sad","down")
            ">Luna slowly takes off her top, placing it on the floor."
            hide screen luna_main
            #$ luna_wear_top = False
            call lun_chibi("stand")
            call lun_main("There...","normal","seductive","sad","mid")
            call lun_main("Is that enough, [lun_genie_name]?","upset","angry","angry","R")
            m "Almost... hands back on the cock, [luna_name]..."
            call lun_main("...","base","seductive","sad","down")
            ">Luna slowly wraps her hands back around your cock and starts pumping."

        "\"Faster\"":
            $ luna_choice = 2
            call lun_main("Like this?","base","angry","sad","mid")
            ">Luna starts moving her hands up and down your cock a little faster."
            m "*mmmm*..."
            call lun_main("Is this fast enough, [lun_genie_name]?","base","seductive","sad","R")
            m "Almost..."
            call lun_main("...","upset","suspicious","sad","down")
            ">She speeds up the pace."
            call gen_main("Ah!","angry","base","mid")
            call lun_main("What?","normal","wide","base","mid")
            m "Well if you go that fast the friction's a little painful"
            call lun_main("Really? I'll slow down then...","upset","suspicious","sad","down")
            m "No need for that, [luna_name], a little spit should solve the problem."
            call lun_main("...","normal","mad","angry","mid")
            call lun_main("You want me to spit on your cock?","upset","suspicious","sad","R")
            m "Just a little bit."
            call lun_main("...","upset","mad","sad","mid")
            call lun_main("......","upset","angry","sad","R")
            call lun_main("*Ptew*","open_tongue","annoyed","sad","down")
            ">Luna spits into her hand before placing it back on your cock."

    call gen_main("*Mmmm*... yes that's it, [luna_name]...","grin")
    call lun_main("...","base","seductive","base","mid")
    g9 "Just keep pumping those hands up and down."
    call lun_main("......","base","seductive","sad","R")
    if luna_choice == 1:
        g9 "Why don't you give those milky tits of yours a nice shake?"
        call lun_main("[lun_genie_name]...","base","seductive","base","R")
        call lun_main("(A little shake won't hurt...)","base","closed","base","down")
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        g9 "*Mmmm*, yes... how about a little more spit, [luna_name]?"
        g9 "Just to make sure everything is nice and lubricated..."
        call lun_main("...","base","seductive","base","R")
        call lun_main("Alright...","base","seductive","base","down")
        call lun_main("*Ptew*","open_tongue","annoyed","sad","down")
        ">Luna spits into her hand again and places it back on your cock."
    ">She starts pumping your cock even faster."
    g9 "Gods yes..."
    g9 "(This is it, where should I cum?)"

    menu:
        "-On her face-":
            ">You place your hand on top of Luna's head and slowly try to force it down to your crotch."
            ">Her slender hands don't stop sliding up and down your length."
            call lun_main("[lun_genie_name]!!!","clench","wide","sad","mid")
            g9  "*Shhh*, [luna_name], I'm just giving you a closer look."
            call lun_main("...","normal","mad","sad","down")
            call lun_main("{size=-5}please sir...{/size}","upset","seductive","sad","R",tears="crying")
            g9  "What, [luna_name]?"
            call lun_main("Please don't...","upset","suspicious","sad","down",tears="crying")
            g9  "*mmmm*..."
            call lun_main("cum on my--","upset","seductive","sad","down",tears="crying")
            hide screen luna_main
            with d3

            #$ luna_wear_cum = True
            $ luna_cum = 7
            call gen_chibi("cum_close")
            call cum_block

            call lun_main("!!!!!!","mad","wide","sad","mid")
            g9  "*Argh*! by the gods {size=+10}YES!{/size}"
            g9  "{size=+10}TAKE IT ALL!{/size}"

        "-On her body-":
            ">You place your hand on Luna's shoulder."
            ">Her slender hands don't stop sliding up and down your length."
            call lun_main("[lun_genie_name]...","clench","wide","sad","mid")
            g9  "*Shhh* [luna_name], just keep stroking."
            call lun_main("...","normal","mad","sad","down")
            call lun_main("{size=-5}please sir...{/size}","upset","seductive","sad","R",tears="crying")
            g9  "what, [luna_name]?"
            call lun_main("Please don't...","upset","suspicious","sad","down",tears="crying")
            g9  "*mmmm*"
            call lun_main("cum on me--","upset","seductive","sad","down",tears="crying")
            hide screen luna_main
            with d3

            #$ luna_wear_cum = True
            $ luna_cum = 3
            call gen_chibi("cum_close")
            call cum_block

            call lun_main("!!!!!!","mad","wide","sad","mid")
            g9  "*Argh*! by the gods {size=+10}YES!{/size}"
            g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"

    call gen_chibi("cum_close_done")
    g9  "*mmmm*....."
    m "That hit the spot..."
    call lun_main("[lun_genie_name]!","disgust","mad","angry","mid")
    call lun_main("How could you!","clench","angry","mad","mid")
    m "*Ahh*... that was fantastic, slut..."
    call lun_main("[lun_genie_name]!!!","open","angry","mad","mid")

    #Hermione Enters.

    call her_walk(action="enter", xpos="right", ypos="base")

    call her_main("[genie_name], I hope you don't mind me coming in unannounced...", "angry", "closed", "base", "mid",xpos="base",ypos="base")

    call reset_genie
    $ luna_flip = -1
    $ luna_r_arm = 2

    call lun_main("...","upset","wide","sad","mid", xpos="mid",ypos="base")
    call her_main("But I really need a good--", "angry", "narrow", "base", "down")
    call her_main("...", "shock", "wide", "base", "stare")
    call her_main("{size=+5}WHAT{/size}", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("","upset","wide","sad","down")
    call her_main("{size=+10}THE{/size}", "angry", "base", "angry", "mid")
    call lun_main("","upset","wide","sad","R")
    call her_main("{size=+15}FRICK!{/size}", "scream", "base", "angry", "mid",emote="angry")
    call lun_main("It's not what it looks--","clench","seductive","sad","R")
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call her_main("{size=+15}Petrificus Totalus!{/size}", "scream", "base", "angry", "mid",emote="angry",trans=hpunch)
    ">Hermione pulls out her wand with surprising speed and paralyses Luna."
    call lun_main("!!!","clench","wide","sad","mid")
    m "(Whoa...)"
    call her_main("Honestly, sir, what are you thinking!", "annoyed", "narrow", "annoyed", "mid")
    call her_main("If you need your filthy old cock jerked so badly you should just call me!", "annoyed", "narrow", "angry", "R")
    call lun_main("???","upset","wide","sad","R")
    call her_main("But to be doing this with Luna Lovegood...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("She's not even a {size=+5}Gryffindor!{/size}", "angry", "base", "angry", "mid")
    m "I wasn't pay--"
    call her_main("Shut up!", "scream", "base", "angry", "mid",emote="angry")
    call her_main("How did you even get Luna to agree to this, sir?", "annoyed", "narrow", "annoyed", "mid")
    call her_main("I don't even think she knows what house she's in half the time.", "angry", "base", "angry", "mid")
    call her_main("I can't imagine her sense of house pride is large enough to warrant this...", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("","normal","wide","sad","down")
    m "I can explain this..."
    call her_main("Really? {w=0.4}Go on...", "angry", "base", "angry", "mid")
    m "Well I was sitting here alone in my office."
    m "(What else can I do...)"
    m "When all of a sudden this weird hat on the shelf behind me starts talking!"
    call her_main("...", "annoyed", "squint", "base", "mid")
    call her_main("Are you serious, sir?", "annoyed", "base", "angry", "mid")
    m "I knew you wouldn't believe--"
    call her_main("Of course I believe you! It's the sorting hat!", "angry", "base", "angry", "mid")
    m "(I keep forgetting that this place is magic...)"
    m "Yes, well... the \"sorting\" hat mentioned that it may have made a mistake with the sorting of some students."
    hat "..."
    m "So it offered to use \"Legitimacy\" or something to fix--"
    call her_main("You performed {i}Legilimency{/i}?", "angry", "wide", "base", "stare")
    call her_main("On a {size=+5}student{/size}!?", "scream", "base", "angry", "mid",emote="angry")
    m "It's not that bad, surely..."
    call her_main("Sir, it's bad enough to use Legilimency to read someone's mind...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("but to use it to change their mind...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("I didn't even think it was possible...", "angry", "base", "angry", "mid")
    m "So it's ok then?"
    call her_main("It's pretty frickin' far from OK...", "scream", "base", "angry", "mid",emote="angry")
    call her_main("You have to Change her back!", "annoyed", "narrow", "annoyed", "mid")
    m "Really? But this has been pretty fun."
    call her_main("I can't even believe I have to tell you how wrong this is sir!", "angry", "base", "angry", "mid")
    call her_main("Change her back now or I tell the ministry everything.", "scream", "closed", "angry", "mid")
    m "What about your house--"
    call her_main("{size=+10}NOW!{/size}", "scream", "base", "angry", "mid",emote="angry")
    m "Alright, alright, sheesh..."
    m "{size=-5}(these bitches be crazy!){/size}"
    m "Let me just get the hat."
    ">You reach around and pull the old leathery hat down from the dusty cupboard."
    hat "*Ughh*... Gently does it now."
    call her_main("Put it on her head.", "annoyed", "narrow", "annoyed", "mid")
    hat "Well if it isn't Miss Granger..."
    call her_main("...", "annoyed", "narrow", "angry", "R")
    ">You place the sorting hat gently on top of Luna's head."
    m "There."
    call her_main("Well, change her back!", "annoyed", "narrow", "annoyed", "mid")
    hat "Are you sure? She seemed much more entertaining this way..."
    call her_main("Do. {size=+5}it. {size=+5}NOW!{/size}", "angry", "base", "angry", "mid")
    hat "Alright, alright. Sheesh."
    hat "You don't seem this bossy when you're in here normally..."
    call lun_main("!!!","upset","wide","sad","mid")
    call her_main("{size=+5}Shut up!{/size}", "scream", "closed", "angry", "mid")
    hat "One boring old Lovegood, coming right up."
    call lun_main("???","upset","wide","sad","R")
    call lun_main("......","normal","wide","sad","down")
    call lun_main(".....","normal","wide","sad","mid")
    call lun_main("....","upset","wide","sad","empty")
    call lun_main("...","normal","wide","sad","empty")
    hat "There, she's back to normal... {size=-8}sadly{/size}"
    call her_main("Are you certain?", "annoyed", "narrow", "annoyed", "mid")
    hat "Yes, I'm sure of it. Can I go back up on the shelf now?"
    call her_main("Fine...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("But if you ever try anything else like this again...", "annoyed", "narrow", "angry", "R")
    call her_main("...", "annoyed", "narrow", "annoyed", "mid")
    ">You decide to place the hat back on the top of the cupboard."
    m "There, all better. now we can forget this whole thing ever happened."
    call her_main("You're not serious, are you?", "annoyed", "narrow", "annoyed", "mid")
    m "What? Miss Lovegood is back to normal..."
    call her_main("You're not getting away with this, sir.", "annoyed", "narrow", "annoyed", "mid")
    m "I'm not sure what you're referring to?"
    call her_main("What I'm referring to?", "angry", "base", "angry", "mid")
    call her_main("Luna {size=+2}Lovegood{/size} is {size=+10}COVERED {/size}in your cum!", "angry", "base", "angry", "mid",emote="angry")
    m "Oh..."
    call her_main("more importantly, How many points did you pay her?", "annoyed", "narrow", "annoyed", "mid")

    menu:
        "\"None\"":
            call her_main("What?", "disgust", "narrow", "base", "mid_soft")
            call her_main("I'm supposed to believe that she came up to your office...", "annoyed", "narrow", "annoyed", "mid")
            call her_main("And let you jerk your disgusting old cock in front of her...", "angry", "base", "angry", "mid")
            call her_main("For free?", "annoyed", "narrow", "annoyed", "mid")
            ">You raise your hand to the air."
            m "Scout's honour!"
            call her_main("...", "disgust", "narrow", "base", "mid_soft")
            m "Besides, surely you'd notice a jump in Ravenclaw points?"
            call her_main("I suppose you're right...", "annoyed", "narrow", "angry", "R")
            call her_main("If the sorting hat had manipulated her then doing this isn't out of the question.", "annoyed", "narrow", "angry", "R")
            call her_main("{size=-5}(But for her to do it so willingly...){/size}", "annoyed", "narrow", "angry", "R")
        "\"I paid her in gold.\"":
            call her_main("Gold?", "disgust", "narrow", "base", "mid_soft")
            m "Gold."
            call her_main("So, no points?", "annoyed", "narrow", "annoyed", "mid")
            m "Not one."
            call her_main("I suppose that's OK then...", "annoyed", "narrow", "angry", "R")
            call her_main("{size=-5}(Why don't I ever get paid in gold...){/size}", "annoyed", "narrow", "annoyed", "mid")
            call her_main("{size=-5}(No, Hermione! If I did that I'd be a prostitute...){/size}", "normal", "happyCl", "worried", "mid")
            call her_main("{size=-5}{heart}{heart}{heart}{/size}", "grin", "narrow", "annoyed", "up")

    call her_main("Well regardless, she has to be punished.", "annoyed", "narrow", "annoyed", "mid")
    m "Wait, she's being punished?"
    call her_main("Of course!", "annoyed", "narrow", "angry", "R")
    call her_main("Seeing as how you didn't give Ravenclaw any points, you haven't done anything wrong.", "annoyed", "squint", "base", "mid")
    call her_main("But her...", "annoyed", "squint", "angry", "mid")
    ">Hermione glares at the still frozen Luna Lovegood."
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("She needs a punishment.", "smile", "base", "angry", "mid")
    m "What are you thinking of?"
    call her_main("*Hmm*...", "annoyed", "narrow", "angry", "R")
    call her_main("Sorting hat!", "annoyed", "narrow", "annoyed", "mid")
    hat "W-w-what? I'm trying to go to sleep..."
    call her_main("How long until Luna's back to normal?", "soft", "base", "angry", "mid")
    hat "I'm not exactly sure... Probably twenty minutes."
    hat "Until then she'll pretty much be in a fairly lucid and suggestible state."
    call her_main("Good...", "smile", "base", "angry", "mid")
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call lun_main("","soft","wide","raised","mid",trans=hpunch)
    call her_main("Liquescimus Corporis!", "scream", "closed", "angry", "mid")
    ">Another flash of light as Luna becomes unpetrified."
    call lun_main("Ugh... where am I?","normal","suspicious","sad","R")
    call her_main("*Shhh*, it's alright.", "base", "narrow", "base", "mid_soft")
    call lun_main("Hermione? What's happening?","normal","suspicious","sad","mid")
    call her_main("Nothing... Professor Dumbledore and I just needed your help.", "base", "narrow", "worried", "down")
    call lun_main("With what?","upset","angry","sad","mid")
    call lun_main("And what's this stuff on--","open","mad","sad","R")
    call her_main("*Shhh*, that doesn't matter right now.", "soft", "happy", "base", "R")
    call her_main("Just head back to your common room...", "open", "base", "base", "R")
    m "is that really--"
    ">Hermione glares at you."
    call her_main("...", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("Alright, I'll go back to my common room...","upset","suspicious","sad","mid")
    call her_main("That's right...", "soft", "happy", "base", "R")

    call gen_chibi("dick_out")
    call lun_walk(action="leave")

    call her_main("Well, now that that's over...", "annoyed", "narrow", "angry", "R")
    call her_main("I think I'll be leaving as well...", "annoyed", "base", "angry", "mid")
    m "Don't you want to stay a little longer?"
    call her_main("I don't think so, sir...", "disgust", "narrow", "base", "mid_soft")

    call her_walk(action="leave")

    $ luna_reverted = True
    $ luna_reverted_intro = True
    $ luna_wardrobe_unlocked = False
    $ lun_whoring = 0
    $ ll_event_pause += 3

    call update_luna

    $ hermione_busy = True

    jump end_hermione_event


# Non-reversion event
# Result: Ability to get Luna to summon hermione for threesome (Planned future event)
label luna_revert_2:
    show screen blkfade
    with d5
    ">You stand up and walk around your desk, standing in front of Luna."
    hide screen bld1
    show screen chair_left
    show screen desk
    $ luna_chibi.zorder = 4
    call gen_chibi("stand", "desk", "base")
    call lun_chibi("stand", "mid", "base")
    hide screen blkfade
    with d5
    call ctc

    ">You open your cloak and pull out your cock."
    call gen_chibi("dick_out")
    with d3

    m "Well..."
    call lun_main("...","upset","angry","angry","mid")
    ">Luna looks down at your cock."
    call lun_main("Disgusting...","base","suspicious","mad","mid")
    ">She takes a firm hold of it with her right hand"
    $ luna_r_arm = 3
    $ luna_xpos = 390
    call gen_main("!!!", "grin", "hard", xpos=300, ypos=0)
    call lun_main("*Hmph* At least it isn't small...","base","seductive","angry","mid")
    call lun_main("(I can't even fit my hand around it.)","base","seductive","mad","down")
    ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
    m "Why don't you try grabbing it with both hands, [luna_name]..."
    call lun_main("*Hmph*... you wish!","base","mad","angry","mid")
    m "..."
    ">Luna starts moving her hand back and forth along the length of your cock."
    m "Yes, that's it..."
    call lun_main("(Men really are the worst)","upset","suspicious","mad","down")
    m "*Mmmm*, yes... just like that, [luna_name]..."
    call lun_main("Is this good, [lun_genie_name]?","soft","annoyed","sad","mid")
    m "yes, yes, this is amazing..."
    call lun_main("good...","base","suspicious","sad","mid")
    call lun_main("but...","normal","suspicious","sad","R")
    call lun_main("Do you need a little more encouragement?","base","mad","sad","mid")
    m "What are you thinking of?"
    call lun_main("......","base","suspicious","mad","mid")

    menu:
        "-Luna takes her top off-":
            ">Luna slowly removes her vest and starts to unbutton her top."
            m "*Mmmm*"
            ">She takes her shirt off and places it onto the floor."
            hide screen luna_main
            #$ luna_wear_top = False
            $ luna_choice = 1
            call lun_chibi("stand")
            call lun_main("There...","base","mad","sad","R")
            m "Very nice, [luna_name]!"
            call lun_main("...","normal","angry","sad","mid")
            call lun_main("Thank you sir...","base","angry","sad","mid")
            ">She places her hands back around your cock."
            call lun_main("*Mmm*, much better...","base","seductive","angry","mid")
            m "Gods yes."
            call lun_main("...","base","seductive","angry","mid")
            call lun_main("I'd take my bra off as well...","normal","seductive","sad","R")
            call lun_main("But I don't think you'd be able to stop yourself from cumming on the spot, would you?","base","mad","mad","mid")
            g4 "probably not!"
            call lun_main("...","base","suspicious","angry","mid")
            ">Luna starts pumping your cock a little faster."

        "-Luna teases you-":
            $ luna_choice = 2
            call lun_main("Come on Professor...","base","mad","sad","R")
            ">Luna starts moving her hands up and down your cock a little faster."
            m "*mmmm*..."
            call lun_main("Get a nice big load ready for me...","normal","angry","sad","mid")
            m "Ah yes..."
            call lun_main("get ready to cum all over your student.","base","angry","sad","mid")
            ">She speeds up the pace."
            call gen_main("Ah...","angry","base","mid")
            call lun_main("What's wrong?","normal","angry","raised","mid")
            m "Well if you go that fast the friction's a little painful."
            call lun_main("Really?...","base","mad","angry","mid")
            ">Luna doesn't slow down. If anything she speeds up slightly."
            g4 "Ah!"
            call lun_main("...","base","suspicious","mad","mid")
            g4 "[luna_name]..."
            call lun_main("*Hmmm*, do You want me to spit on your cock then?","base","seductive","raised","mid")
            g4 "Just a little bit..."
            call lun_main("...","base","seductive","angry","mid")
            call lun_main("......","base","seductive","mad","mid")
            g4 "Please..."
            call lun_main("Good boy.","base","angry","angry","mid")
            call lun_main("*Ptew*","open_tongue","seductive","angry","downL")
            ">Luna spits into her hand before placing it back on your cock."

    call gen_main("*Mmmm*, yes that's it, [luna_name]...","grin")
    call lun_main("...","base","angry","angry","mid")
    g9  "Just keep pumping that hand up and down."
    call lun_main("......","base","mad","mad","mid")
    if luna_choice == 1:
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        call lun_main("*Ptew*","open_tongue","angry","mad","downL")
        ">Luna spits into her hand again and places it back on your cock."
    ">She then starts pumping your cock even faster."
    g9  "Gods yes..."
    g9  "(This is it, where should I cum?)"

    menu:
        "-On her face-":
            ">You place your hand on top of Luna's head and slowly try to force it down to your crotch."

        "-On her tits-":
            ">You place your hand on Luna's shoulder and slowly try to force her down to your crotch."

    call lun_main("[lun_genie_name]!!!","clench","angry","mad","mid")
    call lun_main("You're not trying to cum on me are you?","upset","mad","mad","mid")
    g9  "Ah, [luna_name], I'm almost there."
    call lun_main("Well...","upset","suspicious","mad","mid")
    ##$ luna_wear_bottom = False
    call lun_chibi("stand")
    ">Luna quickly pulls down her skirt."
    g9  "!!!"
    call lun_main("You cum...","upset","mad","mad","mid")
    g9  "Ah..."
    ">Luna slowly pulls her panties forward, exposing her pussy to the air."
    ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
    call lun_main("Where I tell you...","upset","suspicious","mad","mid")
    g9  "*mmmm*"
    call lun_main("Now...","normal","mad","mad","mid")
    call lun_main("Cum.","base","seductive","angry","mid")

    #$ luna_wear_cum_under = True
    $ luna_cum = 10
    call gen_chibi("cum_close")
    call cum_block

    ">You start shooting your load directly into Luna's panties, coating her pussy in cum."
    g9  "*Argh*! by the gods {size=+10}YES!{/size}"
    call lun_main("...","base","seductive","base","down")
    call lun_main("(It's so warm...)","base","seductive","sad","R")
    g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    g9  "*mmmm*....."

    call gen_chibi("cum_close_done")

    m "That hit the spot..."
    call lun_main("{heart}{heart}{heart}","base","seductive","sad","mid")
    call lun_main("[lun_genie_name]!","base","mad","mad","mid")
    call lun_main("How could you! Cumming on your students {size=-10}pussy{/size}...","base","angry","angry","mid")
    m "*Ahh*... that was fantastic slut..."
    call lun_main("[lun_genie_name]...","base","suspicious","angry","R")

    # Hermione Enters

    call her_walk(action="enter", xpos="right", ypos="base")

    call her_main("[genie_name], I hope you don't mind me coming in unannounced...", "angry", "closed", "base", "mid",xpos="base",ypos="base")
    call her_main("But I really need a good--", "angry", "narrow", "base", "down")

    hide screen luna_main
    $ luna_flip = -1
    $ luna_r_arm = 2
    show screen luna_main
    with d3

    call lun_main("","normal","wide","sad","mid",xpos="mid",ypos="base")
    call lun_main("...","upset","angry","mad","mid")
    call her_main("...", "scream", "wide", "base", "mid")
    call her_main("{size=+5}WHAT{/size}", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("","normal","angry","angry","mid")
    call her_main("{size=+10}THE{/size}", "angry", "base", "angry", "mid")
    call lun_main("","normal","mad","angry","mid")
    call her_main("{size=+15}FRICK!{/size}", "scream", "base", "angry", "mid",emote="angry")
    call her_main("What on earth is going on--", "angry", "base", "angry", "mid")
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg') # Not loud
    call lun_main("{size=+15}Petrificus Totalus!{/size}","open","angry","mad","mid",trans=hpunch)
    ">Luna pulls out her wand with surprising speed and paralyses Hermione."
    call her_main("!!!", "soft", "wide", "worried", "shocked")
    m "(Whoa...)"

    hide screen luna_main
    $ luna_flip = 1
    show screen luna_main
    with d3

    call lun_main("","upset","mad","mad","mid",xpos="mid",ypos="base")
    ">Luna turns back around to face you, leaving Hermione paralysed in the middle of the room. "
    call lun_main("{size=+15}What is the meaning of this?{/size}","upset","angry","mad","mid")
    m "I don't know, Miss Granger must have come up here to ask for something."
    call lun_main("The door was locked!","clench","suspicious","angry","mid")
    call lun_main("And everyone knows your door is enchanted against every spell possible!","pout","mad","mad","mid")
    m "(It is?)"
    call lun_main("So she must have had a key...","pout","seductive","mad","down")
    m "..."
    call lun_main("Why does she have a key, [lun_genie_name]?","upset","suspicious","mad","mid")
    m "Ah... um..."

    menu:
        "\"To buy favours\"":
            pass

        "\"I don't know\"":
            call lun_main("...","pout","suspicious","mad","mid")
            call lun_main("Really? You don't know...","clench","mad","mad","mid")
            m "No idea..."
            call lun_main("Well then, we'll just have to ask hermione...","pout","angry","mad","R")
            call her_main("...", "open", "wide", "base", "stare")
            call lun_main("I'm sure that some Veritaserum will clear things up...","clench","angry","mad","mid")
            call her_main("!!!", "angry", "wide", "base", "stare")
            m "(Is that bad?)"
            ">Hermione gives you a pleading look with her eyes."
            call her_main("...", "angry", "happyCl", "worried", "mid", tears="crying")
            m "(Probably...)"
            m "Um..."
            call lun_main("Go on old man...","normal","suspicious","mad","mid")
            m "She's here to buy favours..."

    call lun_main("{size=+5}WHAT{/size}","upset","wide","mad","mid")
    call lun_main("To think that I came here and let you leer at my body...","clench","suspicious","mad","mid")
    call lun_main("While you stroked that filthy cock of yours...","clench","mad","mad","mid")
    call lun_main("and all the while you've been throwing your gold away to some \"Gryffin-{size=+5}WHORE{/size}\"!","upset","angry","mad","mid")
    call lun_main("well then, How much have you paid her?","normal","suspicious","angry","mid")

    hide screen luna_main
    $ luna_flip = -1
    show screen luna_main
    with d3

    call lun_main("How much have you wasted on this fat-assed tart?","upset","mad","mad","mid")

    $ point_estimate = max(15, gryffindor-200)
    m "All up? probably about {number=point_estimate} points..."

    hide screen luna_main
    $ luna_flip = 1
    show screen luna_main
    with d3

    call lun_main("{number=point_estimate}... {w=0.4}points?","normal","angry","raised","mid")
    m "you know, for \"Gremlindoor\"..."
    call lun_main("...","normal","seductive","raised","mid")
    call lun_main("*ha-ha-ha-ha*!","smile","happyCl","base","mid")
    call her_main("...", "annoyed", "narrow", "angry", "R")
    m "..."

    hide screen luna_main
    $ luna_flip = -1
    show screen luna_main
    with d3

    ">Luna turns back around to face hermione."
    call lun_main("really? you sell your body for points?","grin","seductive","base","L")
    call her_main("...", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("Oh right, I suppose I should probably undo that.","pout","angry","angry","mid")
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg') # Not loud
    call her_main("", "soft", "wide", "base", "stare",trans=hpunch)
    call lun_main("Liquescimus Corporis!","open","seductive","angry","mid")
    ">Another flash of light as Hermione becomes normal again."
    call lun_main("","base","seductive","base","R",xpos="mid",ypos="base")
    call her_main("Professor! What is the meaning of this!", "scream", "closed", "angry", "mid")
    call her_main("And what were the two of you doing before I got here?", "angry", "base", "angry", "mid")
    call lun_main("oh... I was just helping out Professor Dumbledore...","normal","seductive","base","down")
    call her_main("helping out how?", "annoyed", "narrow", "annoyed", "mid")
    call lun_main("just to relieve some... tension. {w=0.4}Don't worry he isn't going to pay me in points... *tssk*","base","angry","base","L")
    call her_main("what?", "angry", "base", "angry", "mid",emote="angry")
    call her_main("[genie_name]! What are you doing!", "scream", "closed", "angry", "mid")
    m "Ah..."
    call lun_main("don't blame him. It's not his fault you fail to satisfy...","base","mad","angry","mid")
    call her_main("You... you...", "annoyed", "narrow", "annoyed", "mid")
    call her_main("{size=+10}You Stupid whore!{/size}", "angry", "base", "angry", "mid")
    call her_main("{size=+15}You're nothing more than a prostit-{/size}", "angry", "base", "angry", "mid",emote="angry")
    call lun_main("{size=+15}Petrificus totalus!{/size}","open","mad","mad","mid", trans=hpunch)
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg') # Not loud
    ">Luna petrifies Hermione for the second time."
    call lun_main("","normal","mad","mad","mid")
    call her_main("!!!", "angry", "wide", "base", "stare")
    call her_main("...", "angry", "base", "angry", "mid")
    ">Hermione stares at Luna with a blind rage."
    m "Should you really be doing that?"

    hide screen luna_main
    $ luna_flip = 1
    show screen luna_main
    with d3

    call lun_main("*Hmph*!","upset","seductive","angry","R")
    ">Luna huffs, ignoring the question."
    call lun_main("Honestly, [lun_genie_name], I don't know what you see in her...","normal","angry","angry","mid")
    call ctc

    call lun_main("So, how should we punish her?","grin","seductive","base","R")
    call her_main("!!!", "angry", "wide", "base", "stare")
    m "Punish her?"
    call lun_main("Of course! For what she said.","smile","seductive","angry","mid")
    call her_main("...", "clench", "narrow", "base", "down")
    call lun_main("You're not going to let her get away with that are you?","upset","angry","mad","mid")

    m "I wasn't... Suppose I should let you get back at her for calling you a--"
    call lun_main("Yes, that's right.","base","seductive","base","down")

    hide screen luna_main
    $ luna_flip = -1
    show screen luna_main
    with d3

    ">Luna turns to face hermione."
    call lun_main("*Hmm*... what should I do...","base","mad","mad","mid")
    call lun_main("...","base","seductive","angry","mid")
    call her_main("...", "open", "wide", "base", "stare")
    call lun_main("I've got it!","grin","wide","angry","mid")
    hide screen hermione_main
    hide screen luna_main
    hide screen bld1
    with d3

    ">Luna places her hands on Hermione's shoulders and gently forces her paralysed body to her knees."
    call lun_chibi("stand","right","base")
    call her_chibi("kneel","mid","base",flip=True)
    call gen_chibi("dick_out")
    call ctc

    call lun_main("That should be about right...","base","seductive","angry","mid")
    call lun_main("wait...","normal","seductive","base","mid")

    if luna_wear_top:
        hide screen luna_main
        #$ luna_wear_top = False
        show screen luna_main
        call lun_chibi("stand")
        with d3
        ">Luna quickly removes her top."

    ">Luna places her hand on Hermione's chin and gently turns her head upwards."
    call lun_main("Perfect...","grin","seductive","base","mid")
    call her_main("...","annoyed","base","worried","R",xpos="right",ypos=200)
    call lun_main("Now, before you so rudely decided to interrupt us, Professor Dumbledore made a nasty mess...","base","seductive","base","down")
    call her_main("...","angry","base","worried","mid")
    call lun_main("I was going to go back to my room and tidy up before class but seeing as how your interruption has taken so long, you'll have to tidy me up instead.","base","seductive","angry","R")
    call her_main("...","normal","happyCl","worried","mid")

    hide screen luna_main
    #$ luna_wear_panties = False
    show screen luna_main
    with d3

    ">Luna slowly pulls down her panties, revealing her cum-soaked pussy."
    call her_main("!!!","disgust","slit","low","stare")
    call lun_main("Well... get to work!","grin","mad","base","mid")
    ">Hermione glares at Luna."
    call her_main("...","annoyed","narrow","annoyed","mid")
    call lun_main("*Sigh* I guess I have to do everything then!","base","angry","angry","mid")
    show screen blkfade

    hide screen hermione_kneel
    # Luna's sprite posing is no longer compatible with Hermione's, and should be removed or replaced with CG
    #$ luna_l_arm = 3
    #$ luna_xpos=635
    #$ hermione_ypos=390
    ">Luna thrusts her mound forward, grinding it under Hermione's nose and against her closed mouth."
    hide screen blkfade

    call her_main("!!!","angry","happyCl","worried","mid")
    m "!!!"
    call lun_main("*Mmmm*, that's it...","base","seductive","base","down")
    call lun_main("who's a good girl...","grin","seductive","base","mid")
    call her_main("!!!","normal","happyCl","worried","mid")
    call lun_main("*mmmm*... smells good doesn't it, slut?","base","seductive","base","down")
    call lun_main("*mmmm*... you look like you want more though...","grin","seductive","angry","down")
    # $ luna_xpos = 550
    # $ luna_l_arm = 1
    ">Luna takes a step back from Hermione's face."
    call lun_main("Such a pretty face...","base","seductive","sad","mid")
    ">Luna places her thumb into Hermione's paralysed mouth, slowly opening it."
    call her_main("...","open_tongue","narrow","angry","R")
    ">She grabs a hold of her tongue and slowly pulls it out until it hangs from her mouth."
    call her_main("!!!","open_wide_tongue","closed","angry","mid")
    m "(...)"
    call lun_main("*Shhh*....","normal","seductive","sad","down")
    # $ luna_xpos=635
    # $ luna_l_arm = 3
    ">Luna steps forward, placing her cum coated pussy on top of hermione's open mouth."
    call her_main("!!!","open_wide_tongue","base","angry","mid")
    call lun_main("*Shhh*.... *mmmm*, that's not bad...","grin","seductive","base","mid")
    call her_main("...","open_wide_tongue","base","base","mid")
    call her_main("...","open_wide_tongue","happy","base","mid")
    call her_main("......","open_wide_tongue","narrow","base","down")
    call her_main(".........","open_wide_tongue","narrow","angry","up",cheeks="blush")
    call lun_main("Good girl...","grin","seductive","angry","mid")
    call lun_main("Just enjoy yourself...","base","seductive","angry","mid")
    call lun_main("We both know who's the real slut now don't we?...","upset","angry","mad","mid")
    call her_main("...","open_wide_tongue","narrow","angry","up",cheeks="blush")
    call lun_main("Don't we?","grin","suspicious","mad","mid")
    call her_main("*yeessh*...","open_wide_tongue","narrow","annoyed","up")
    ">Hermione barely manages a muffled response."
    g9  "(This is too much!)"

    menu:
        "-Join in-" if False:
            # Have sex with hermione while Luna grinds on her face
            # Needs chibi/CG work (not likely if Slytherin Luna is to be written out of the game)
            show screen blkfade

            ">You walk over to Hermione's kneeling form and pick up her limber body."
            call lun_main("Hey! I wasn't finished with her!","base","seductive","base","down")
            m "Don't worry, I'm just repositioning her. You can still have your fun."
            ">You carry Hermione's stiff, paralysed form over to your desk, placing her gently on top of it."
            hide screen blkfade

            call lun_main("...","base","seductive","base","down")
            m "*Hmm*... I wonder if..."
            ">You start bending Hermione's limbs, finding that they move easily but lock into place when you stop pushing."
            m "Huh, she's just like a Barbie doll!"
            call her_main("*hro-hessor*!","angry","wink","base","mid")
            ">You bend her over your desk with her face pointing towards Luna."
            m "There, I trust you're still able to administer your punishment [luna_name]?"
            call lun_main("*Mmmm*, I think so...","base","seductive","base","down")
            ">Luna walks over to hermione and presses her pussy back onto the girl's open tongue."
            call lun_main("Ah... {heart}","base","seductive","base","down")
            call her_main("...","angry","wink","base","mid")
            ">You slowly lift Hermione's skirt."
            call her_main("!!!","angry","wink","base","mid")
            ">Revealing her sopping pussy."
            m "*Mmmm*..."
            m "Come on Barbie..."
            ">You thrust your full length into Hermione's cunt!"
            g9  "Let's go party!"
            call her_main("{heart}{heart}{heart}","angry","wink","base","mid")
            g9  "Gods yes!"
            call lun_main("*mmmm* {heart}","base","seductive","base","down")
            ">You start fucking hermione in earnest."
            call lun_main("so, [lun_genie_name]...","base","seductive","base","down")
            call lun_main("How long has this been going on?","base","seductive","base","down")
            m "With miss Granger? A while..."
            call lun_main("figures...","base","seductive","base","down")
            call lun_main("You always were a teacher's pet weren't you...","base","seductive","base","down")
            call her_main("{heart}{heart}{heart}","angry","wink","base","mid")
            call lun_main("I bet you even came here on your own didn't you...","base","seductive","base","down")
            call lun_main("Eager to sell your body for a few lousy points...","base","seductive","base","down")
            g9  "Yes..."
            call her_main("...","angry","wink","base","mid")
            call lun_main("just so your house can win the cup this year...","base","seductive","base","down")
            call lun_main("you know no one cares about the house cup don't you?","base","seductive","base","down")
            ">You start thrusting even harder into Hermione's dripping pussy."
            call her_main("*yesh-heeyyy-hoooo*!!!","angry","wink","base","mid")
            call lun_main("Let's see the shall we...","base","seductive","base","down")
            call lun_main("Professor...","base","seductive","base","down")
            m "*Ah*... yes?"
            call lun_main("Who won the house cup when you were in school...","base","seductive","base","down")
            m "(Shit! I have no idea who won the lousy cup when {i}Dumbiedoor{/i} was a kid.)"
            m "*Um*... *ah*..."
            ">Hermione's pussy squeezes around your cock."
            m "It seems to have... *ah*... slipped my mind."
            call lun_main("see...","base","seductive","base","down")
            call lun_main("Even Dumbledore doesn't remember who won when he was a student...","base","seductive","base","down")
            call her_main("...","angry","wink","base","mid")
            #hermione tears
            call lun_main("so that means you've done all this for nothing...","base","seductive","base","down")
            call lun_main("all the times you've sold your body...","base","seductive","base","down")
            call lun_main("all the times you've humiliated yourself...","base","seductive","base","down")
            call lun_main("even lying here eating me out while your precious dumbledore fucks you...","base","seductive","base","down")
            g9  "Yes..."
            call her_main("...","angry","wink","base","mid")
            g9  "*Argh*!"
            call lun_main("you did it all just because you wanted to...","base","seductive","base","down")
            call her_main("...","angry","wink","base","mid")
            g9  "{size=+5}yes!!!!{/size}"
            call lun_main("you...","base","seductive","base","down")
            call lun_main("filthy...","base","seductive","base","down")
            call lun_main("slut...","base","seductive","base","down")
            with hpunch

            g9  "{size=+7}*Argh*, TAKE THIS!!!{/size}"
            call cum_block
            $ hermione.set_cum(face="light")
            g9  "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"
            call cum_block
            $ hermione.set_cum(face="heavy")
            hide screen bld1
            with d3
            call ctc

            show screen bld1
            with d3

        "-Start jerking off-":
            # Jerk off and cum on Hermione
            show screen blkfade
            hide screen genie_main
            hide screen hermione_kneel
            hide screen luna_main
            with d3

            ">You grab your hardening cock that's still sticking out of your robe."
            lun "*Mmmm*, it's about time you started disciplining your students properly."
            m "Maybe you're right."

            call gen_chibi("jerk_off","desk","base")
            hide screen bld1
            hide screen blkfade
            with d3

            call ctc

            ">You start stroking your cock, aiming it directly at hermione's face"

            call lun_main("I'm always right...","grin","mad","base","R")
            with d3

            call her_main("...","open_wide_tongue","narrow","base","down")

            m "Yes... that's it slut."
            call lun_main("*Mmmm*, I can see what you like about her...","base","seductive","base","mid")
            ">Luna grinds herself hard against Hermione's mouth."
            call her_main("...","open_wide_tongue","narrow","annoyed","up")
            call lun_main("She's much more tenable with her mouth full...","grin","mad","base","mid")
            g9  "You're telling me!"
            call lun_main("so how long has this been going on, [lun_genie_name]?","base","mad","angry","R")
            m "A while now..."
            call lun_main("That doesn't surprise me...","upset","seductive","base","mid")
            call lun_main("I always figured Hermione was a repressed slut...","base","seductive","angry","mid")
            call lun_main("I bet she even came to you didn't she?","base","seductive","angry","R")
            call her_main("...","open_wide_tongue","narrow","angry","up",cheeks="blush")
            m "Ah... yes, she did."
            call lun_main("Typical...","upset","angry","angry","mid")
            call lun_main("It figures that the head of the \"MRM\" would be a slut...","base","mad","mad","mid")
            call her_main("...","open_wide_tongue","narrow","annoyed","up")
            call lun_main("desperate to sell her body...","grin","suspicious","angry","mid")
            call lun_main("all for a few points...","base","seductive","base","mid")
            m "Yes... keep going..."
            call lun_main("*Aww*, Do you enjoy it when I degrade her, [lun_genie_name]?","base","angry","sad","R")
            g9  "Gods yes!"
            call lun_main("good...","base","seductive","angry","R")
            call lun_main("because I expect you to coat this slut in your \"enjoyment\"...","grin","angry","angry","mid")
            g9  "Don't you worry!"
            g9  "One fresh load cumming right up!"
            call lun_main("hear that hermione?","grin","mad","mad","mid")
            call her_main("...","open_wide_tongue","narrow","base","down")
            call lun_main("you're headmaster has a nice load of cum ready for you...","base","suspicious","angry","mid")
            call lun_main("if you're lucky he might even give Gryffindor some points...","smile","seductive","base","down")
            g9  "Yes..."
            call her_main("...","open_wide_tongue","closed","angry","mid")
            call lun_main("*Aww*, you look so upset...","normal","seductive","sad","down")
            call lun_main("don't be sad... this is what you were born for...","grin","seductive","sad","mid")
            call her_main("...","open_wide_tongue","narrow","annoyed","up")
            ">You start beating your meat with renewed determination!"
            call lun_main("you should be proud to take a thick load of cum from your headmaster...","base","angry","sad","down")
            call lun_main("speaking of which... are you ready [lun_genie_name]?","base","seductive","angry","R")
            g9  "*Argh*! by the nine gods yes!"
            call lun_main("then cum!","grin","suspicious","angry","R")
            hide screen luna_main
            with d3

            call gen_chibi("cum_close")
            call cum_block

            g9  "{size=+7}*Argh*, TAKE THIS!!!{/size}"
            call cum_block

            ">Luna takes a step back as you simply erupt over Hermione's petrified expression."
            lun "Cover this slut!"
            call ctc

            g9  "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            g9  "take it all, bitch!"
            her "!!!"
            call cum_block
            ">You feel like your cumming more then you've ever cum in your life..."

            show screen blkfade
            $ hermione.set_cum(face="heavy")
            # $ luna_xpos = 550
            # $ luna_l_arm = 1
            call gen_chibi("cum_close_done")

            show screen luna_main
            hide screen blkfade
            with fade

            call her_main("!!!","grin","narrow","annoyed","up")

            call her_main("...","open_wide_tongue","narrow","annoyed","up")
            ">Hermione kneels before you, unable to move as her face is plastered with more cum than you've ever seen."
            ">You can barely make out her features through a wall of whiteness."

    m "Gods yes... that was amazing..."
    hide screen luna_main
    hide screen hermione_main
    hide screen bld1
    show screen blkfade
    with d3

    $ luna_flip = 1

    #call load_luna_clothing_saves

    #$ luna_wear_cum_under = False

    call gen_chibi("sit_behind_desk")
    call lun_chibi("stand")

    ">Luna quickly puts her panties and clothes back on."

    hide screen blkfade
    with d3
    pause.5

    call her_main(None,"silly","narrow","base","dead",xpos="mid")
    call lun_main("I'm glad you enjoyed yourself, [lun_genie_name]...","base","seductive","base","R",xpos="close",ypos="base")
    call her_main("...","silly","narrow","base","dead")
    call lun_main("but How much would you say you enjoyed yourself?","base","angry","angry","mid")
    m "A lot..."
    call lun_main("And if you had to put a number on your enjoyment?","upset","mad","angry","mid")
    m "Oh... um I'd say about 250?"
    call lun_main("Fantastic!","base","happyCl","base","mid")
    m "..."
    m "Here's your payment, [luna_name]."
    $ game.gold -= 250
    $ luna_gold += 250
    call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
    call lun_main("Well, I best be off then. I'm late for class.","normal","seductive","angry","R")
    m "Aren't you going to fix up Hermione first?"
    call her_main("...","silly","narrow","annoyed","up")
    call lun_main("Really? You're too lazy to cast a few simple spells?","normal","angry","angry","mid")
    m "Ah... I'm a little tired after all that..."
    m "I think it's for the best if you did it."
    call lun_main("Fine... I suppose you'll want me to wipe her memories too?","normal","seductive","base","R")
    m "Wipe her memories?"
    call her_main("???","angry","happyCl","worried","mid")
    call lun_main("Of course. I mean what we just did to her was a little questionable...","normal","angry","angry","mid")
    call lun_main("A memory charm would probably be for the best.","base","mad","base","R")
    call her_main("!!!","annoyed","narrow","annoyed","mid")
    m "(I think I've underestimated the magic at this school...)"
    m "Ah sure... why not..."
    call lun_main("I guess I'll clean her up as well...","normal","suspicious","angry","mid")
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call lun_main("Scourgify!","open","suspicious","angry","mid")
    $ hermione.set_cum(None)
    ">All the cum vanishes from Hermione's body."
    call her_main("...","annoyed","base")
    m "Woah..."
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call lun_main("Obliviate!","open","angry","angry","mid")
    ">Another flash of light as Hermione's eye's glaze over."
    call her_main("...","soft","narrow","base","dead")
    m "..."
    show screen white
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    with hpunch
    call her_main("","soft","wide")
    call lun_main("Liquescimus Corporis!","open","suspicious","mad","mid")
    ">Hermione collapses to the floor in a limp heap."
    call her_main("*agh*...","shock","narrow","base","dead")

    # Hermione didn't undress
    # m "(Is it over?)"
    # show screen white
    # pause .1
    # hide screen white
    # $ renpy.play('sounds/magic4.ogg')   #Not loud.
    # call lun_main("vestimenta lacus!","open","mad","angry","mid")
    # ">All of Hermione's clothes wriggle like worms back onto her body."
    # hide screen luna_main
    # with d3

    call lun_main("There...","normal","angry","angry","R")
    call lun_main("Will that be all [lun_genie_name]?","base","suspicious","angry","mid")
    m "That will do for now, [luna_name]."
    ">Luna turns to leave your office with Hermione still in a heap on the floor."
    call lun_main("See you next time...","base","suspicious","mad","mid")

    call lun_walk(action="leave")

    m "[hermione_name]? Are you OK?"
    call her_main("*agh*... what happened?", "open", "narrow", "worried", "down",ypos="head",xpos="base")
    call her_main("Was Luna Lovegood here?", "upset", "wink", "base", "mid")
    m "Who?"
    call her_main("never mind...", "normal", "happyCl", "worried", "mid")
    call her_main("I think I'm going go now [genie_name]...", "angry", "happyCl", "worried", "mid",emote="sweat")
    m "Alright, well have a nice day."
    call her_main("ugh...", "disgust", "narrow", "base", "down")
    call her_main("(I could have sworn Luna was here...)", "annoyed", "base", "worried", "R")
    call her_main("(Wait, what was I doing here...)", "annoyed", "squint", "base", "mid")
    call update_luna
    call her_chibi("stand", ypos="base")
    with d3
    pause .5
    call her_walk(action="leave")

    $ luna_busy = True
    $ hermione_busy = True

    jump end_hermione_event
