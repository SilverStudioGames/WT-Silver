
label ll_pf_masturbate:
    # Common start label

    $ ll_pf_masturbate.start()

    label end_luna_masturbate_event:

    if lun_whoring < 3:
        $ lun_whoring += 1

    jump end_luna_event


label ll_pf_masturbate_T1_intro:

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    m "Come in..."

    call lun_walk("desk", action="enter")
    pause.5

    call lun_main("Hello, Sir...","base","happyCl","base","mid",xpos="right",ypos="base")
    m "Miss Lovegood. So, Did the {i}wickerspats{/i} leave you alone today?"
    call lun_main("Not at all! They were worse than ever!","upset","base","angry","R")
    m "Really?"
    call lun_main("Really, sir. And I don't think it's just me they're affecting either.","normal","base","sad","mid")
    call lun_main("I fear the whole school is becoming overrun!","normal","wide","sad","mid")
    m "What makes you say that?"
    call lun_main("The way people are acting...","normal","angry","sad","R")
    call lun_main("It's very strange, don't you think sir?","upset","angry","sad","mid")
    m "(Like this crazy bitch can call anyone strange!)"
    m "Strange how?"
    call lun_main("it's Their auras sir!","normal","closed","sad","R")
    m "Oh..."
    call lun_main("They're far too red!","normal","angry","sad","mid")
    m "Too red?"
    call lun_main("I'm afraid so...","upset","angry","sad","R")
    m "And you think these {i}wackspots{/i} are to blame?"
    call lun_main("I'm not sure...","normal","seductive","sad","down")
    call lun_main("According to my father's bestiaries, they should only ever produce a grey tinge to an aura...","normal","seductive","sad","R")
    call lun_main("For them to be making auras red...","upset","wide","sad","down")
    call lun_main("It could be very dangerous!","normal","wide","sad","mid")
    m "(*Pffft*... auras...)"
    m "Yes, I see how that could be dangerous..."
    call nar(">Luna starts grinding her thighs together.")
    call lun_main("yes...","base","seductive","sad","down")
    call lun_main("So, about this itch, sir...","base","seductive","sad","mid")
    m "Yes."
    call lun_main("Did you say you had some way to get rid of it?","normal","seductive","sad","mid")
    m "I did."
    call lun_main("Well...","upset","seductive","sad","R")
    m "First things first, I need something from you, Miss Lovegood."
    call lun_main("Something from me?","pout","wide","sad","mid")
    m "Yes, I need a promise."
    call lun_main("Oh...","normal","base","sad","R")
    call lun_main("Alright then!","base","happyCl","sad","mid")
    m "I haven't even told you what it is yet."
    call lun_main("Don't worry sir, I trust you!","base","wide","base","mid")
    m "(This might be too easy even!)"
    m "Yes... the techniques I'm going to be showing you are proprietary, so I'm going to have to make you promise not to talk to anyone about what goes on in this room."
    call lun_main("Techniques...","normal","seductive","sad","R")
    call lun_main("Proprietary...","upset","seductive","sad","down")
    call lun_main("I'm not sure I understand, sir.","normal","seductive","sad","mid")
    m "Well, if what you're saying is correct, even if I use some powerful magic to remove them..."
    m "(I hope she buys this...)"
    m "They'll soon be back, and in greater numbers."
    call lun_main("...","normal","seductive","sad","R")
    m "(Did she buy it?)"
    call lun_main("Yes, You're right, sir.","normal","closed","sad","R")
    m "(YES!)"
    call lun_main("But are there really techniques to dispel them?","normal","seductive","raised","mid")
    m "There are, but as I said, if you want to learn them you'd have to promise not to tell anyone what happens here."
    call lun_main("I suppose that's only fair, This information would be worth more than a snorkack sighting!","base","base","sad","mid")
    m "..."
    m "It's Not just the techniques Miss Lovegood."
    m "You must promise not to tell anyone anything about what happens in this room, no matter what."
    call lun_main("But...","normal","seductive","sad","R")
    call nar(">You can see Luna is awkwardly rocking her pelvis.")
    call lun_main("*Nngh* Alright then...","base","seductive","sad","mid")
    call lun_main("I solemnly swear that I will tell no one what happens within these hallowed walls...","normal","closed","base","R")
    m "Fantastic!"
    call lun_main("So, can you please teach me the techniques, sir?","base","wide","sad","mid")
    call nar(">There's a desperate need in Luna's eyes that excites you to no end.")
    m "Yes, yes. I think I've made you wait long enough."
    call lun_main("Thank you so much!","base","happyCl","base","R")
    m "No need to thank me, Miss Lovegood, I'm simply doing what any good teacher should."
    m "Now, stand in the middle of the room for me."
    hide screen luna_main
    with d3

    call lun_main("Is Here okay?","pout","base","sad","mid",xpos="mid",ypos="base")
    m "Perfect."
    m "Before we begin I have to explain a few things."
    call nar(">Luna stares at you intently.")
    call lun_main("...","normal","angry","sad","mid")
    m "From what I can tell these {i}rockspits{/i} seem to have infected an unusual part of your body."
    call lun_main("Yes... Normally they only make your head fuzzy.","pout","angry","sad","R")
    m "And how do you get rid of them in that situation?"
    call lun_main("By thinking positive thoughts, sir...","base","happyCl","sad","R")
    m "Correct."
    m "So, in your current situation, you simply need to focus positive thoughts on the affected area."
    call lun_main("...","normal","base","raised","R")
    call lun_main("How do I do that?","upset","base","sad","mid")
    m "We'll try some self-applied massage to the area to start with."
    call lun_main("So I just start massaging the area that they're making fuzzy?","soft","base","sad","mid")
    m "That's correct, I'll be here to give you some guidance."
    call lun_main("Thank you, Sir!","base","happyCl","sad","R")
    m "You're quite welcome."
    call lun_main("...","base","base","sad","down")
    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely acknowledging the nature of her actions.")
    call lun_main("Ah...","normal","seductive","sad","down")
    m "Is everything alright, Miss Lovegood?"
    call lun_main("Ah...{w=0.3} of course!","base","wide","sad","mid")
    call lun_main("It's just a little sensitive...","base","seductive","sad","down")
    m "That's to be expected. Keep going."
    call lun_main("Ah...{w=0.3} yes sir...","normal","happyCl","sad","R")
    g4 "..."
    call lun_main("Ah...{w=0.3} is this how it should be done?","pout","base","sad","mid")
    m "As long as it's feeling good I'm sure it's working. If you keep this up, you'll soon be rid of those nasty wickerspoons."
    call lun_main("That's nice...","base","closed","sad","R")
    call lun_main("...","normal","base","sad","mid")
    call lun_main("Are you sure this will work, sir?","soft","seductive","sad","mid")
    m "Of course I am! Do you doubt the powerful {i}Dumbelldoor{/i}?"
    call lun_main("Certainly not, sir...","normal","wide","sad","R")
    call lun_main("It's just...","normal","seductive","sad","down")
    call lun_main("I'm not sure this is going to get rid of them...","pout","seductive","sad","mid")
    m "What makes you say that?"
    call lun_main("Do you remember how I said the {i}wickerspats{/i} were like a nasty itch, sir?","normal","seductive","sad","R")
    m "I do."
    call lun_main("As nice as this massage feels...","normal","seductive","sad","down")
    call lun_main("It's not really scratching that itch sir...","pout","angry","sad","mid")
    call lun_main("... am I doing it wrong, sir?","normal","seductive","sad","mid")
    m "Certainly not, but this is worse than I feared."
    call lun_main("really?","normal","wide","sad","mid")
    m "Yes. It would seem that those nasty critters are trying to hide."
    call lun_main("Hide? Where?","normal","wide","sad","down")
    m "Well, as long as you're still feeling that itch they can't have gone far."
    m "But this means you'll have to chase them down."
    call lun_main("Chase them down?","normal","seductive","raised","mid")
    m "Don't worry, I'll be here to guide you through it."
    call lun_main("Thank you, sir.","base","base","sad","R")
    m "First, close your eyes."
    call lun_main("...","normal","happyCl","sad","R")
    m "Very good. Now I want you to block everything else out."
    call lun_main("Alright, sir...","upset","happyCl","sad","R")
    m "Imagine it's just you, alone in your room."
    call lun_main("Yes...","normal","happyCl","sad","R")
    m "Nice and cozy. Not a care in the world."
    call lun_main("...","base","happyCl","sad","R")
    m "Now, focus on where the itch is strongest."
    call lun_main("Ah...{w=0.3} Alright...","base","happyCl","base","R")
    m "I want you to chase that feeling with your fingers."
    call lun_main("...","normal","happyCl","base","R")
    m "Focus on catching it."
    call lun_main("I can't...","pout","happyCl","sad","R")
    call lun_main("It's like trying to grab rays of sunlight...","normal","happyCl","sad","R")
    m "Don't try to grab a hold of it, just brush against it with the tips of your fingers."
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("*Ah*...","base","happyCl","sad","R")
    call lun_main("*Mmm*...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("I'm close sir...","base","happyCl","sad","R")
    m "Good. Just keep your eyes closed and focus on your fingers."
    call lun_main("{heart}","grin","happyCl","base","R")
    call lun_main("*Ah*... I think it's working, sir!","base","happyCl","sad","R")
    call lun_main("I think I'm about to catch it!","base","happyCl","base","R")
    m "*Shhh*, don't speak, just focus..."
    call lun_main("Okay...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("*Ah*...","grin","happyCl","sad","R")
    call lun_main("{heart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("*Ah*...{w=0.3} sir...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("*Ah*...","grin","seductive","sad","R")
    call lun_main("I think I've almost got it...","grin","happyCl","sad","R")
    m "*Shhh*..."
    call lun_main("*Ah*...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("*Mmmm*...","base","happyCl","angry","mid")
    call lun_main("*Ah*...","grin","happyCl","angry","mid")
    call lun_main("*A-ah*...","base","seductive","sad","down")
    call lun_main("Yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("*Ah*... *ah*...{heart}","grin","seductive","sad","R")
    call lun_main("{size=+4}*Mmm*...{w=0.3} yes...{heart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}*ah*...{w=0.3} ah...{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","base","empty")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("*Ah*! I think they're attacking me, sir!","base","wide","sad","mid")
    call lun_main("!!!","base","base","sad","empty")
    m "Is everything okay?"
    call lun_main("*Ah*...{w=0.4} Yes sir...{heart}","normal","seductive","sad","R")
    call lun_main("It's just...","base","seductive","sad","R")
    m "..."
    call lun_main("I-I've never...","normal","seductive","sad","R")
    call lun_main("...","base","seductive","sad","down")
    call lun_main("{size=-5}Ah...{/size}","base","seductive","sad","R")
    m "So, have the {i}wickspots{/i} left you alone?"
    call lun_main("I think so, sir...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her hand out from under her skirt.")
    call lun_main("At least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic! Will that be all then, Miss Lovegood?"
    call lun_main("OH... Did you want me to leave already, sir?","normal","seductive","sad","down")
    m "If there's nothing else I can help you with."
    call lun_main("I suppose not... but what if the feeling comes back, sir?","upset","seductive","sad","R")
    call lun_main("Should I try and get rid of them myself?","normal","seductive","sad","down")
    m "Certainly not!"
    call lun_main("Really? Why not?","normal","wide","sad","mid")
    m "As I said earlier, Miss Lovegood, these techniques are to be kept secret."
    m "Not to mention dispelling {i}wankspits{/i} in your common room could lead to a school wide outbreak."
    call lun_main("So what can I do if they come back?","normal","base","sad","mid")
    m "If you ever feel like you need to relieve yourself of those pesky little things again, my door is always open."
    call lun_main("Are you sure, sir?","normal","seductive","sad","mid")
    call lun_main("I wouldn't want to bother you...","normal","seductive","sad","R")
    m "You'd be doing no such thing! Besides, I've been meaning to test these sort of techniques for a while now."
    m "If anything you'll be helping me with important research."
    call lun_main("Really? Thank you very much, sir.","base","wide","base","mid")
    call lun_main("Hopefully they leave me alone, but if not I'll come and visit you again.","base","base","sad","R")
    m "I look forward to it."
    call lun_main("...","base","seductive","sad","mid")

    call lun_walk(action="leave")

    call bld
    m "(What an odd girl...)"

    jump end_luna_event


label ll_pf_masturbate_T1_E1:
    # Luna masturbates for Genie and then he cums on her face

    $ ll_event_pause += renpy.random.randint(1, 2)

    call lun_main("","base","base","base","mid")
    m "Miss Lovegood. How have you been?"
    call lun_main("Alright... but the wrackspurts seem to have come back..","upset","base","angry","R")
    m "Again? So soon?"
    call lun_main("I'm afraid so [lun_genie_name]...","normal","base","sad","mid")
    call lun_main("Every time I think about what we did in here...","normal","wide","sad","mid")
    call lun_main("It just makes them feel so much... stronger...","normal","angry","sad","R")
    m "Yes... They must be afraid of my powerful techniques..."
    call lun_main("Do you think so?","normal","closed","sad","R")
    m "I do..."
    m "Why else would they attack you when you think about curing yourself of them?"
    call lun_main("You're right...","normal","angry","sad","mid")
    m "So... Are you ready to try and dispel them again?"
    call lun_main("Only if it's not too much trouble [lun_genie_name]... I wouldn't want to disturb you...","upset","angry","sad","R")
    m "Please, as headmaster it's my duty to make sure my students are safe..."
    call lun_main("You're right...","normal","seductive","sad","down")
    call lun_main("I just feel guilty coming up here so often...","normal","seductive","sad","R")
    m "Don't..."
    ">Luna starts grinding her thighs together."
    call lun_main("Okay...","base","seductive","sad","down")
    call lun_main("So, is it okay if I start scratching...","base","seductive","sad","mid")
    m "I don't see why not."
    m "Please, why don't you come a bit closer..."

    call lun_walk("desk")

    call ll_pf_masturbate_T1_start

    $ luna_l_arm = 1
    m "Feeling better?"
    call lun_main("Yes. I'm feeling much better now.","normal","seductive","sad","down")
    m "Glad I could be of help..."
    call lun_main("Thank you, [lun_genie_name]!","normal","seductive","sad","mid")
    call lun_main("I have to head back to my dorms now...","upset","seductive","sad","R")

    call lun_walk(action="leave")

    call bld
    m "(What an odd girl...)"

    jump end_luna_masturbate_event


label ll_pf_masturbate_T1_E2:
    # Luna masturbates for Genie

    $ ll_event_pause += renpy.random.randint(1, 2)

    m "So, Miss Lovegood, To what do I owe the pleasure today?"
    call lun_main("Ah... I was hoping that I could... Um...","normal","seductive","sad","mid")
    call lun_main("I know you must be very busy with school management...","normal","wide","sad","mid")
    call lun_main("And I promise that I wouldn't ask unless it was of the utmost importance!","soft","base","sad","R")
    m "Get on with it, [luna_name]."
    call lun_main("Can I... get some more wrackspurts out? Please?","normal","wink","sad","mid")
    m "*Hmm*... Again? So soon?"
    call lun_main("If you think that it's too much for you to handle, we could slow down a bit...","normal","seductive","sad","R")
    m "Nonsense! I could never abandon my students in their hour of need."
    call lun_main("You mean it's okay if I?","normal","wide","sad","mid")
    call lun_main("Oh... Thank you, thank you, thank you!","smile","happyCl","base","R")

    call lun_walk("desk")

    call ll_pf_masturbate_T1_start

    call ll_pf_masturbate_T1_continue

    m "Will that be all then, Miss Lovegood?"
    call lun_main("I suppose... Although I think I could go--","normal","seductive","sad","down")
    call lun_main("No...{w=0.3} I better get to bed...","upset","seductive","sad","R")
    call lun_main("Thanks again, [lun_genie_name]!","normal","seductive","sad","down")

    call lun_walk(action="leave")

    call bld
    m "(She really is a bit loony...)"

    jump end_luna_masturbate_event


label ll_pf_masturbate_T1_E3:
    # Luna masturbates for Genie and then he cums on her face

    call lun_main("","base","closed","angry","mid", xpos="mid", ypos="base")
    m "[luna_name], are those wrackspurts still causing you--"

    call lun_walk("desk")

    $ luna_l_arm = 4

    call nar(">Luna quickly puts her hand down her skirt, not even waiting on your reply.")
    call lun_main("Ah... I'm sorry [lun_genie_name]... I just...{w=0.3} needed... this...{heart}","base","seductive","sad","up")
    m "You seem relieved..."
    call lun_main("Ah... {heart} yes...","base","wide","sad","mid")
    call lun_main("These visits are starting to become all I can think about...","base","seductive","sad","down")
    m "*Hmm*...{w=0.3} Do you think that's a bad thing?"
    call lun_main("Ah...{w=0.3} of course not!","normal","happyCl","sad","R")
    call lun_main("It just...*Hngh*{w=0.3} means that it's working...","pout","base","sad","mid")
    call lun_main("If only I could spend all day up here...","base","base","sad","mid")
    m "Do you think a full day of treatment would get rid of them?"
    call lun_main("Ah...","base","base","sad","mid")
    call lun_main("Probably not...","soft","seductive","sad","mid")
    call lun_main("But...","base","wide","sad","R")
    call lun_main("Ah...","base","seductive","sad","down")
    call lun_main("I think...{w=0.3} It'd probably feel...","soft","seductive","sad","mid")
    call lun_main("Nice...{heart}{heart}{heart}","base","seductive","sad","R")
    m "Speaking of feeling nice..."
    call lun_main("Ah...{w=0.3} I think I'm...{w=0.5} Cumming [lun_genie_name]...","open_tongue","seductive","sad","down")
    call lun_main("Ah...{heart}","base","seductive","sad","mid")
    call lun_main("*Mmmmm*{heart}","base","seductive","sad","mid")
    call lun_main("Ah...{w=0.3} I'm cumming...{heart}{heart}","base","wide","sad","up")
    m "*Mmmmm*, that's it girl..."
    call lun_main("Ah...{heart}","soft","seductive","sad","down", cheeks="blush")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">Her fingers keep casually stroking her needy slit.","end")
    m "It seems those {i}wickedspots{/i} have been giving you a fair bit of grief, haven't they?"

    menu:
        "-Start jerking off-":
            call ll_pf_masturbate_T1_jerk_off
        "-Just keep watching-":
            call ll_pf_masturbate_T1_continue

    m "Will that be all, Miss Lovegood?"
    lun "Oh, um.{w=0.3} Yes..."

    lun "I'll see you next time those wrackspurts come up again..."
    m "See that you do."
    lun "Yes, [lun_genie_name]..."

    call lun_walk(action="leave")

    jump end_luna_masturbate_event


label ll_pf_masturbate_T1_start: # Call label
    # Luna starts to masturbate

    call lun_main("...","pout","base","sad","mid", xpos="mid", ypos="base", trans=fade)
    m "That's it..."
    m "Begin when you're ready, Miss Lovegood."

    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely waiting for you to finish your sentence.")
    call lun_main("Ah...{w=0.3} thank you [lun_genie_name]...","normal","seductive","sad","down")
    m "You seem relieved..."
    call lun_main("Ah...{w=0.3} of course... I've been waiting to come here since yesterday...","base","wide","sad","mid")
    call lun_main("I think Those slimy wrackspurts have infested the common room...","base","seductive","sad","down")
    m "That's quite possible..."
    call lun_main("Ah...{w=0.3} ah...","normal","happyCl","sad","R")
    call lun_main("But getting rid of them...{w=0.4} feels...{w=0.4} so...{w=0.3} so...{w=0.3} good...","pout","base","sad","mid")
    call lun_main("I'm almost glad I've got them...","pout","base","sad","mid")
    m "The positive feelings you have are your body's reactions to the {i}wickerspats{/i} being expelled."
    call lun_main("Really?","base","closed","sad","R")
    call lun_main("Ah...","normal","base","sad","mid")
    call lun_main("I must...{w=0.3} ah...{w=0.3} Be expelling a lot then...","soft","seductive","sad","mid")
    call lun_main("In fact...","normal","wide","sad","R")
    call lun_main("Ah...","normal","seductive","sad","down")
    call lun_main("I think...{w=0.3} ah...{w=0.3} I'm about to...{w=0.3} ah...","pout","seductive","sad","mid")
    call lun_main("*Mmmm*, it's just like...{w=0.2} last time...","normal","seductive","sad","R")
    m "Oh, are you cumming already?"

    if ll_pf_masturbate.counter < 3:
        # Luna learns the meaning of cumming
        call lun_main("Cumming?","normal","seductive","sad","down")
        call lun_main("What's?{w=0.3} Ah...{heart}","pout","angry","sad","mid")
        call lun_main("Cumming?{heart}","normal","seductive","sad","mid")

    call lun_main("Ah...{w=0.3} I'm cumming...{heart}{heart}","normal","wide","sad","mid")
    m "*Mmmmm* that's it girl..."
    call lun_main("Ah...{heart}","normal","wide","sad","down")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">However, despite this, her fingers remain a flurry of movement under her skirt.","end")
    m "It seems those {i}wickedspots{/i} have been giving you a fair bit of grief, haven't they?"
    call lun_main("Ah...{heart}yes{heart}","normal","seductive","sad","mid")
    m "Don't worry, that should sort them out for now..."

    return


label ll_pf_masturbate_T1_continue: # Call label
    # Luna continues to masturbate

    call lun_main("*Ummm*...","base","base","sad","R")
    m "What's wrong?"
    call lun_main("...","normal","happyCl","sad","R")
    call lun_main("Is it...","upset","happyCl","sad","R")
    call lun_main("Okay if I do it once more?","normal","happyCl","sad","R")
    m "What?"
    call lun_main("If you need to do other things I can leave!","base","happyCl","sad","R")
    m "There's no need for that! You can stay here as long as you like..."
    m "I was just a little surprised that you needed to go again is all..."
    call lun_main("Ah...{w=0.3} well...","base","happyCl","base","R")
    call lun_main("These wrackspurts...","normal","happyCl","base","R")
    call lun_main("Ah...","pout","happyCl","sad","R")
    call lun_main("They've been very tiresome...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("Besides...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("Ah...","base","happyCl","sad","R")
    call lun_main("I've been... waiting for this all day...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("Standing here...","base","happyCl","sad","R")
    m "..."
    call lun_main("{heart}{heart}{heart}","grin","happyCl","base","R")
    call lun_main("In front of my headmaster...","base","happyCl","sad","R")
    call lun_main("While he helps me to...","base","happyCl","base","R")
    m "*Shhh*, don't speak, just focus..."
    call lun_main("Okay...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("Ah...","grin","happyCl","sad","R")
    call lun_main("{heart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("Ah... [lun_genie_name]...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("Ah...","grin","seductive","sad","R")
    call lun_main("I think I've almost got them...","grin","happyCl","sad","R")
    m "*Shhh*..."
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("*Mmmm*...","base","happyCl","angry","mid")
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call lun_main("A-ah...","base","seductive","sad","down")
    call lun_main("Yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("Ah...{w=0.3} ah...{heart}","grin","seductive","sad","R")
    call lun_main("{size=+4}*Mmm*...{w=0.2} Yes...{heart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}*ah*...{w=0.3} *oh*...{w=0.3} Frickity Frack!!!{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","sad","mid")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("Ah! Thank you, [lun_genie_name]!","base","wide","sad","mid")
    call lun_main("!!!","base","wide","sad","mid")
    m "Is everything okay?"
    call lun_main("Ah...{w=0.4} yes{heart} thank you{heart} [lun_genie_name]...{heart}","normal","seductive","sad","R")
    m "So, have the {i}wickspots{/i} left you alone now?"
    call lun_main("I think so, [lun_genie_name]...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her sopping wet hand out from under her skirt as the liquid slowly starts dripping onto the floor.")
    call lun_main("At least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic!"

    return


label ll_pf_masturbate_T1_jerk_off: # Call label
    # Genie jerks off while Luna masturbates and ends up cumming on her face

    m "Truth be told they've begun to affect me as well..."
    call lun_main("What? They got you too?","base","angry","sad","mid")
    m "I was afraid this might happen with you dispelling all of your own wrackspurts into this room..."
    m "This is why I didn't want you doing this outside the office..."
    call lun_main("It could have been a disaster [lun_genie_name]...","base","angry","sad","mid")
    call lun_main("But will you be alright?","soft","wink","raised","mid")
    m "Oh, don't worry about me... I'm a {i}master{/i} when it comes to this..."
    call lun_main("Of course... These are your techniques after all...","base","happyCl","sad","mid")
    call lun_main("Would it...","base","seductive","sad","R")
    call lun_main("Would it be okay if I watched [lun_genie_name]?","base","annoyed","sad","mid")
    call lun_main("Just as a way to improve my own technique!","base","wink","base","mid")
    m "*Mmmm*, I see nothing wrong with it..."
    m "Here, I'll give you a nice view..."
    show screen blkfade
    hide screen luna_main
    with d3

    ">With that, you slowly rise out of your chair as your cock strains against your robe, brought furiously to life by Luna's performance."
    ">You then walk around your desk to stand in front of the pale blonde..."
    m "Here we go..."
    ">As you pull your cock from underneath your robe you're met with a shocked gasp from Luna."
    lun "It's so..."
    lun "can I..."
    lun "..."

    ">Before you can say anything else, Luna instinctively drops to her knees."
    $ ccg_folder = "luna_facial"
    $ ccg1 = "1"
    $ ccg2 = "genie"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    lun "Wow..."
    m "This is the place that those nasty little {i}whiskersprouts{/i} like to hide on me..."
    $ ccg1 = "2"
    lun "It's...{w=0.3} big..."
    m "It is..."
    $ ccg1 = "3"
    lun "How often do you have to get rid of them?"
    m "Maybe once or twice a day..."
    $ ccg1 = "4"
    lun "Only twice?"
    m "It depends on the day..."
    ">You begin stroking your cock. The thick stream of pre-cum dripping from the tip easily lubricates your entire length."
    $ ccg1 = "1"
    m "*Ugh* Yeah...{w=0.3} that's it..."
    lun "..."
    $ ccg1 = "5"
    lun "Anything I should be looking for in particular?"
    m "Nothing in particular... just focus on taking it all in..."
    $ ccg1 = "6"
    lun "Taking it all in..."
    ">Luna stares intently at your cock for a few seconds before suddenly snapping from her reverie."
    $ ccg1 = "7"
    lun "Okay [lun_genie_name], I'll take it all in!"
    ">Before you even have time to react, Luna swoops her head in towards your cock, placing her nostrils at the head."
    $ ccg1 = "8"
    ">Luna takes a huge breath inwards, closing her eyes as she does."
    $ ccg1 = "9"
    lun "Huh...{w=0.3} It doesn't smell like I thought it would..."
    m "What did you think it would smell like?"
    $ ccg1 = "8"
    lun "Spices!"
    m "..."
    m "And what did it smell like?"
    $ ccg1 = "10"
    lun "*Hmm*... It reminds me of a certain Bertie Bott's Every-Flavour bean I once had..."
    $ ccg1 = "11"
    lun "It wasn't very good... But it wasn't bad..."
    m "Well now that you've taken it all--"
    ">As if to purposely interrupt you, Luna leans in and quickly runs her tongue across the tip of your sensitive cock."
    $ ccg1 = "12"
    m "What!"
    $ ccg1 = "13"
    lun "I was just--"
    m "*Argh*, you've done it now!"
    m "here it comes You little minx!"
    $ ccg1 = "14"
    lun "Here comes what--"
    m "*ARGH*!!!"
    ">As if in retaliation for her previous interruption, your cock now interrupts Luna's sentence with a thick deluge of semen."
    $ ccg1 = "15"
    m "There it is you horny little thing... here's what you wanted..."
    $ ccg1 = "16"
    lun "Oh..."
    $ ccg1 = "17"
    lun "What's this?"
    m "*Argh*..."
    $ ccg1 = "18"
    lun "It smells...{w=0.3} so..."
    $ ccg1 = "19"
    lun "Goood..."
    $ ccg1 = "20"
    lun "Can I...{w=0.3} Taste it?"
    m "I don't see why not."
    lun "..."
    $ ccg1 = "21"
    $ ccg2 = "blank"
    ">Luna slowly pulls a strand of your thick cum before closely examining it."
    $ ccg1 = "22"
    lun "My spectrespecs are detecting so much magic..."
    lun "I've never seen anything like this before..."
    m "It's called cum."
    lun "Cum..."
    $ ccg1 = "23"
    ">With that, Luna finally decides to taste your essence."
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "25"
    lun "!!!"
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "26"
    lun "It's..."
    lun "It's......"
    $ ccg1 = "27"
    lun "It's perfect... it's just the best..."
    m "*Mmm*... that's it...{w=0.3} you always know what to say..."
    $ ccg1 = "28"
    lun "I'm not just..."
    $ ccg1 = "29"
    lun "How can you make this?"
    $ ccg1 = "28"
    lun "There's so much magic..."
    $ ccg1 = "30"
    lun "It's incredible..."
    $ ccg1 = "31"
    lun "It's soaking in through my skin...{w=0.3} I can't..."
    lun "The wrackspurts... I think this is..."
    $ ccg1 = "32"
    lun "Ah...{w=0.3} I think I should probably leave now [lun_genie_name]..."
    m "You're not going to clean yourself up first?"
    $ ccg1 = "33"
    lun "Oh..."
    lun "If it's okay with you [lun_genie_name]... I might clean myself up back in my room..."
    m "Whatever suits you, Miss Lovegood..."
    $ ccg1 = "30"
    lun "Thank you, [lun_genie_name]...{w=0.3} for... everything..."

    show screen blkfade
    hide screen luna_main
    hide screen ccg
    with d3

    call lun_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3

    return


label ll_pf_masturbate_T1_E2_old:  # Not in use. Old writing.

    $ lun_whoring = 2
    $ ll_event_pause = 3

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    lun "Can I please come in, [lun_genie_name]?"
    call nar(">There's a desperate twang to Luna's voice.")

    menu:
        "-Let her in-":
            m "Of course."
        "-mess with her-":
            m "Who is it?"
            lun "Luna Lovegood, [lun_genie_name]..."
            lun "May I please come in?"
            m "Luna who?"
            lun "Lovegood, [lun_genie_name]..."
            m "Oh miss Lovegood! Come in..."

    call lun_walk("mid", action="enter")
    pause.5

    call lun_main("...","pout","annoyed","sad","R",cheeks="blush",xpos="right",ypos="base")
    m "Miss Lovegood..."
    m "What can I help you with today?"
    call lun_main("I-I...{w=0.3} need...","soft","seductive","sad","down")
