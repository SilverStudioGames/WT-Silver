label hermione_map_BJ:
    stop weather

    $ renpy.call('forest_BJ_'+str(forest_BJ_progress))
    $ hermione_busy = True
    call set_her_map_location("gryffindor_room")

    jump return_office

label forest_BJ_1: #BJ in the forest interrupted by moaning myrtle
    show screen blkfade
    with d3

    call play_music("night_outside")
    call play_sound("walking_on_grass")

    ">Sure enough, the map seems to {b}magically{/b} guide you to the girl, alone in the midnight air..."
    ">Seemingly scraping some resin off a tree..."

    $ hermione.wear("all")
    # TODO: Add robe force equip.

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    m "Miss Granger? What are you doing out here at this time of night?"
    call her_main("[genie_name]! I, ugh, I wasn't doing anything bad, I swear!", "angry", "wide", "base", "R", xpos="base", ypos="base", trans=d5)
    m "..."
    call her_main("Ugh, fine! If you must know, I was out here gathering up some mastic resin.", "upset", "narrow", "worried", "down")
    call her_main("I know Students aren't {i}technically{/i} supposed to touch the stuff since it's normally just used to make belch powder...", "annoyed", "base", "base", "R")
    call her_main("But I'm using it in my research for a non addictive analgesic!", "open", "closed", "base", "mid")
    m "Whatever..."

    menu:
        "-Let her get back to her botany-":
            m "Well I better leave you be then..."
            call her_main("Really?", "upset", "wide", "worried", "shocked")
            "You mean you don't want to..."
            m "Maybe some other time."
            call her_main("...", "upset", "narrow", "worried", "down")
            show screen blkfade
            with d3
            ">You turn away from the miffed girl."
            m "..."
            m "(What's wrong with me?)"
            return
        "-Ask for a blowjob-":
            m "Well, seeing that we're all alone out here..."
            call her_main("Oh... I, um, guess we are...", "open", "wide", "base", "R")
            m "Wanna fool around?"
            call her_main("Oh thank goodness... I thought you were going to murder me for a second there...", "base", "happyCl", "base", "mid",trans=hpunch)
            m "What? How could you think such a thing!"
            m "I don't know if I'll be able to--"
            call her_main("How about I make it up to you with my mouth then, *Hmm*?", "base", "narrow", "base", "mid")
            m "Done."
            $ forest_BJ_progress = 2

    show screen blkfade
    with d3

    ">The girl softly lays her robe on the cool grass before kneeling down on it in front of your steaming cock."

    $ ccg1 = "blank"
    $ ccg2 = 1
    $ ccg3 = "overlay"
    hide screen hermione_main
    hide screen blkfade
    with d3

    her "*Mmmm*... I don't think I'll ever get sick of this cock..."
    m "It'll get sick of having to wait for you to put it in your mouth though."
    $ ccg2 = 2
    her "*Hmph*... now, now, [genie_name], patience is a virtue..."
    $ ccg2 = 3
    her "Besides, doesn't my hand feel nice?"
    m "Not as nice as your mouth."
    her "Alright then... Have it your way."
    $ ccg2 = 4
    ">Hermione leans forward and engulfs the head of your cock in her mouth."
    anon "{size=-4}Wow...{/size}"
    $ ccg2 = 5
    her "!!!"
    her "Did you hear something?"
    m "What? I don't believe so..."
    m "Not unless you count the sound of you sucking away..."
    m "Speaking of which..."
    $ ccg2 = 6
    her "..."
    $ ccg2 = 7
    ">Hermione goes back to work, slobbering her way up and down your cock."
    m "Gods... they'd make you a queen for sucking cock like this in Agrabah..."
    $ ccg2 = 8
    her "(Where?)"
    m "*Mmmmm*... Fuck yes..."
    anon "{size=-8}*te-he-he-he*...{/size}"
    $ ccg2 = 5
    her "!!!"
    $ ccg2 = 9
    her "Tell me you heard something that time sir!"

    menu:
        "-Tell her to get back to work-":
            m "All I hear is a mouth that needs to get back to sucking."
            $ ccg2 = 10
            her "Not now sir!"
            her "I think there's someone else here..."
            her "Or something else..."
            m "Wait..."
            m "You don't mean..."
        "-Agree with her-":
            $ ccg2 = 10
            m "You might be right..."
            m "Did it sound like someone laughing?"
            her "Yeah..."
            her "{size=+10}Show yourselves!!!{/size}"

    $ ccg1 = "m1"
    myr "*Te-he-he-he*... Hi Hermione..."
    $ ccg2 = 11
    with hpunch
    g4 "{size=+10}AH! A G-G-GHOST!{/size}"
    myr "*ha-ha-ha-hah*!"
    myr "Good one Dumbledore! You always were a joker."
    her "Myrtle!"
    her "This isn't what it looks like!"
    myr "Isn't it?"
    myr "I think it looks lovely..."
    her "*Argh*! Please don't tell anyone!!!"
    show screen blkfade
    with d3

    ">Hermione hastily covers up and sprints away angrily as the ghostly apparition fades away..."
    m "What was that..."
    ">You stumble back to your office in a confused and blue-balled stupor..."

    return


label forest_BJ_2:
    $ forest_BJ_progress = 3
    show screen blkfade
    with d3

    call play_music("night_outside")
    call play_sound("walking_on_grass")

    $ hermione.wear("all")
    # TODO: Add robe force equip.

    ">The map yet again leads you to the curly haired girl, alone at the edge of the forest, picking mushrooms."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    m "More late night gardening?"
    pause.1
    call her_main("{size=+10}[genie_name]!{/size}", "shock", "wide", "base", "stare", xpos="base", ypos="base", trans=hpunch)
    call her_main("Ugh... Don't startle me like that!", "annoyed", "base", "base", "R")
    call her_main("And yes, I've been collecting some mushroom samples.", "soft", "base", "base", "mid")
    m "Cool..."
    call her_main("So what are you doing out here?", "base", "base", "base", "mid")
    call her_main("I thought you didn't leave your office anymore?", "soft", "squint", "base", "mid")
    m "Oh, you know me... Always looking to connect with my students..."
    call her_main("*Mhmmm*... So that's what you're down here for then? To {i}connect{/i}?", "base", "happy", "base", "mid")
    m "Always..."
    call her_main("Fine... Just let me take my robe off...", "base", "base", "base", "R")
    show screen blkfade
    with d3

    ">Hermione quietly folds up her robe and places it on the cold ground before kneeling down on it."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 12
    $ ccg3 = "overlay"
    show screen ccg
    hide screen hermione_main
    hide screen blkfade
    with d3

    m "So you're not worried about that ghost?"
    her "You mean Myrtle? You know She's harmless..."
    $ ccg2 = 10
    her "It's the gossip I'm worried about..."
    m "Gossip?"
    $ ccg2 = 13
    her "Stop playing dumb, [genie_name]! Everyone knows Myrtle's the biggest gossip in the history of gossips..."
    $ ccg2 = 4
    ">Hermione quickly pops your cock into her mouth in between her words..."
    $ ccg2 = 10
    her "*pop* Not to mention she never forgets! She's {b}still{/b} going on about the whole McCartney thing..."
    $ ccg2 = 8
    her "*shlrp* *schkk* *slurp*"
    m "*Mmmm*..."
    m "So have you heard any gossip floating around then?"
    $ ccg2 = 10
    her "Surprisingly not..."
    $ ccg2 = 14
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 13
    her "although She probably wouldn't want to upset you..."
    $ ccg2 = 4
    her "*shlrp* *schkk* *slurp*"
    m "*Mmmm*..."
    $ ccg2 = 10
    her "Still... I didn't think she'd be able to help herself..."
    $ ccg2 = 14
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 15
    her "Albus Dumbledore having his {b}cock{/b} sucked by Hermione Granger..."
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 12
    her "It'd be the gossip of the century..."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    m "You almost sound disappointed that she didn't tell anyone."
    $ ccg2 = 17
    her "What? How could you say such a thing!"
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 19
    her "I'd never be able to show my face around Hogwarts again..."
    $ ccg2 = 20
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "Everyone would just be imagining me on me knees..."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "{b}Covered{/b} in your thick spunk..."
    $ ccg2 = 20
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 17
    her "Word would probably even get back to mom and dad..."
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 19
    her "Imagine what they'd think of their little girl..."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "sucking all that cum out her headmaster's fat, {size=+2}juicy,{/size} {size=+2}cock...{/size}{heart}"
    g9 "ARGH THAT's IT GIRL!"
    g9 "HERE IT COMES"
    $ ccg2 = 22
    ">You grab a hold of the back of Hermione's head and thrust forward, planting your cock firmly down her throat."
    $ ccg1 = "m1"
    myr "Wow... I didn't think you'd fit it all in..."
    $ ccg2 = 23
    her "!!!"
    ">Not even the sudden appearance of a ghost can stop your colossal orgasm at this point..."
    g9 "ARGH!!!"
    ">You start firing off a thick deluge of cum down Hermione's tender throat, the presence of someone else only serving to coax more out of your balls..."
    $ ccg2 = 24
    call cum_block
    her "!!!!!!"
    $ ccg2 = 25
    call cum_block
    g9 "Gods I Needed this!"
    $ ccg2 = 26
    myr "So much...{heart}{heart}{heart}"
    $ ccg2 = 25
    ">Your hips continue to pump more and more cum down hermione's throat."
    $ ccg2 = 26
    her "..."
    $ ccg2 = 25
    myr "Bye Hermione{heart}{heart}{heart}"
    show screen blkfade
    with d3

    ">Eventually your orgasm subsides and you allow your softening member to slide out of hermione's cum coated throat."

    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3

    call her_main("I can't believe you just did that?", "shock", "base", "angry", "mid")
    m "really? After everything we've done?"
    call her_main("It's a figure of speech! And More importantly...", "angry", "closed", "angry", "mid")
    call her_main("{size=+10}You just came down my throat in front of moaning myrtle!{/size}", "scream", "closed", "angry", "mid")
    call her_main("She's going to tell everyone about this now!", "annoyed", "base", "angry", "mid")
    m "So? Doesn't everyone sort of know by now anyway?"
    call her_main("*Argh*! That's not the point and you know it!", "annoyed", "squint", "angry", "mid")
    call her_main("You can't keep treating me like your {heart}dirty{heart} little {b}cumdump{/b} to use as you please!", "angry", "squint", "base", "mid")
    call her_main("To coat in your filthy nasty {b}{heart}cum{heart}{/b}...", "angry", "narrow", "base", "dead")
    call her_main("In front of whoever, or whatever, you want...", "angry", "narrow", "annoyed", "up")
    call her_main("...", "angry", "narrow", "base", "dead")
    call her_main("Well... I hope you've learned your lesson!", "angry", "narrow", "base", "up")
    call her_main("I'm going to go back and...", "angry", "narrow", "base", "up")
    call her_main("*ge*-Clean! myself off...", "open", "squint", "worried", "up")
    call her_main("And remember...", "open", "narrow", "base", "up")
    call her_main("no {size=-1}more... {size=-1}{b}cum{/b}... {size=-1}all... {size=-1}over... {size=-1}me... {size=-1}please...{heart}{heart}{heart}{/size}", "angry", "narrow", "base", "dead")
    show screen blkfade
    with d3

    ">With that, hermione staggers back to the castle, still coated in your thick layer of seed."

    return


label forest_BJ_3: #Complete BJ with Myrtle appearing after the cumshot
    $ forest_BJ_progress = 4
    show screen blkfade
    with d3

    call play_music("night_outside")
    call play_sound("walking_on_grass")

    $ hermione.wear("all")
    # TODO: Add robe force equip.

    ">Surely enough, the handwritten words \"Hermione Granger\", manage to lead you to the lone girl at the edge of an imposing forest."
    ">However she doesn't seem preoccupied with her usual botany."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    m "Aren't you usually out her to collect some forbidden plant, [hermione_name]?"
    call her_main("Not always... Sometimes I just come out her to enjoy the cool air...", "soft", "base", "base", "R", xpos="base", ypos="base", trans=d5)
    m "I see..."
    m "So you're not waiting out here for your headmaster to arrive, just so you can suck his cock in public?"
    call her_main("What! o-of course not!", "base", "narrow", "worried", "down")
    call her_main("I'm just out here to admire the moon!", "base", "base", "base", "R")
    m "What moon?"
    ">Hermione frantically looks to the cloudy sky, unable to even glimpse the moon through the impenetrable greyness."
    call her_main("Oh... um...", "open", "happy", "base", "R")
    m "It's alright for you to admit that you're a dirty little cumslut, miss Granger."
    call her_main("It's not like that!", "upset", "narrow", "annoyed", "mid")
    call her_main("{size=-4}I just like sucking your dick, OK...{/size}", "upset", "narrow", "base", "R_soft")
    m "So you don't want me to cover you in cum like the cumslut you are?"
    call her_main("...", "base", "narrow", "worried", "down")
    call her_main("Ugh...", "base", "narrow", "base", "dead")
    show screen blkfade
    with d3

    ">Hermione studiously removes, folds and lays her robe on the cool night grass."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 15
    $ ccg3 = "overlay"
    show screen ccg
    hide screen hermione_main
    hide screen blkfade
    with d3

    her "Maybe I wouldn't have ended up a dirty little cumslut if your dick wasn't so nice..."
    #Have her suck his cock
    $ ccg2 = 16
    pause
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 17
    her "*Ah*....{heart}{heart}{heart}"
    her "Thank you for being here tonight, [genie_name]...."
    $ ccg2 = 16
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 19
    her "I wasn't sure if you were going come..."
    $ ccg2 = 18
    her "*glck* *shlrp* *Gluck*"
    m "If you want me to keep cumming, I suggest you do a little less talking..."
    $ ccg2 = 20
    her "*Khes* *sh-r*! (Yes sir!)"
    $ ccg2 = 27
    ">In response, hermione thrusts her entire lithe frame forwards, forcing your thick cock all the way down her throat."
    $ ccg2 = 28
    g9 "Ugh.... that's it, [hermione_name]!"
    $ ccg2 = 29
    m "How are you able go so deep?..."
    $ ccg2 = 17
    her "*Hmm*... I had a good teacher."
    $ ccg2 = 19
    m "As flattered as I am..."
    ">You softly low your hand on to the back of the little sluts head..."
    $ ccg2 = 30
    g9 "THIS!"
    pause
    $ ccg2 = 31
    g9 "Can't be taught!"
    $ ccg2 = 30
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 31
    ">You vigorously start fucking the poor girls throat with little regard for her well being."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    g9 "You were born a cocksucker."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    g9 "It's just taken you until now to realise."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    $ ccg1 = "m2"
    $ ccg2 = 33
    ">You're so focussed in your face fuck session you almost fail to notice the ghostly apparition of an attractive little witch appear behind Hermione."
    $ ccg2 = 32
    g4 "!!!"
    $ ccg2 = 33
    ">Before you even have time to scream, Myrtle, raises her finger to her lips, shushing you."
    $ ccg2 = 32
    ">Instead, it appears like she only wants to watch hermione have her throat fucked silly..."
    $ ccg2 = 34
    g9 "Well if it's a show you want, {size=+3}it's{/size} {size=+3}a{/size} {size=+3}show{/size} {size=+3}you'll{/size} {size=+3}get!{/size}"
    $ ccg2 = 35
    her "???"
    $ ccg2 = 34
    ">Coaxed on by the prospect of an ethereal audience, you begin to get into a firm, rough rhythm of properly fucking hermione's throat raw."
    $ ccg2 = 35
    her "*glck*-*glck*-*glck*!!"
    $ ccg2 = 34
    her "*glck*{heart}*glck*{heart}*glck*"
    $ ccg2 = 35
    myr "..."
    $ ccg2 = 34
    her "*Slurp*! *Gulp*! *Slurp*!"
    $ ccg2 = 35
    m "Yes, like that... that's a good little slut..."
    $ ccg2 = 34
    her "*Slurp*! *Slurp*! *Slurp*!"
    $ ccg2 = 35
    m "Deeper now."
    $ ccg2 = 34
    her "*Slurp*! *Slurp*! *Slurp*!"
    $ ccg2 = 35
    m "Come on cock-slut."
    $ ccg2 = 36
    her "*Slurp*! *Gobble*! *Gobble*!"
    $ ccg2 = 37
    g4 "Deeper now!"
    $ ccg2 = 36
    her "*Gobble-gobble-slurp-gobble*!"
    $ ccg2 = 37
    g4 "Yes, like that!"
    $ ccg2 = 36
    her "{size=+5}*Gobble-gobble-slurp-gobble*!{/size}"
    $ ccg2 = 34
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    $ ccg2 = 35
    g9 "See? Your body was made for this..."
    $ ccg2 = 36
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 37
    g9 "Made to take my cock!"
    $ ccg2 = 36
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 37
    g9 "Any time of day!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35
    g9 "Anywhere you can get it!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 37
    g9 "And in front of anyone who will watch you!"
    $ ccg2 = 38
    her "{size=+10}!!!{/size}"
    $ ccg2 = 37
    myr "*he-he-he*... Hi Hermione..."
    $ ccg2 = 36
    her "*glck* Sto--{w=0.3}! *glck*{heart}*glck*"
    $ ccg2 = 37
    ">Hermione starts to struggle against you in her embarrassment, her face turns a deep red and tears start to roll down her face."
    $ ccg2 = 36
    ">Unfortunately for petite witch, her shame only serves to intensify your pleasure."
    $ ccg2 = 37
    g9 "ARGH, HERE IT COMES SLUT!"
    $ ccg2 = 36
    call cum_block

    g4 "{size=+7}ARGH!{/size}"
    $ ccg2 = 37
    g4 "{size=+7}Eat my cum, slut!{/size}"
    $ ccg2 = 34
    call cum_block
    $ ccg2 = 39
    call cum_block

    ">Your cock starts firing off a huge load against the back of the poor girls throat, quickly overflowing up through her nostrils and back at you."

    her "{size=+14}!!!{/size}"
    $ ccg2 = 40

    myr "{size=+3}Oh{/size} {size=+3}my{/size} {size=+3}God!{/size}"
    $ ccg2 = 39
    call cum_block

    myr "I've never seen this much cum in my whole life or even since then!"
    $ ccg2 = 40
    myr "Here Dumbledore, shoot some more!"
    $ ccg2 = 39
    show screen blkfade
    with d3
    $ ccg1 = "m3"

    ">Moaning Myrtle rises up from the dewy ground and flashes her see-through breasts towards you."
    $ ccg2 = 41
    hide screen blkfade
    with d3
    call cum_block

    g4 "{size=+7}ARGH! YES!!!{/size}"
    $ ccg2 = 42
    ">With your orgasm renewed by the sight of some heavenly cans, you begin shooting cum down hermione throat anew."
    $ ccg2 = 41
    call cum_block

    her "*gulp* *gargggglelggg* *gobble*...."
    $ ccg2 = 42
    call cum_block

    myr "More, Dumbledore, more!"
    $ ccg2 = 41
    call cum_block
    g4 "{size=+15}ARGH!!!!{/size}"
    $ ccg2 = 42
    call cum_block

    her "*gllllgggggg*..."
    $ ccg2 = 41
    call cum_block
    myr "{size=+14}MORE!!!{/size}"
    $ ccg2 = 42
    call cum_block
    show screen blkfade
    hide screen ccg
    with d3

    ">Eventually, your orgasm comes to a halt and you finally pull your sloppy cock out of Hermione's well used hole..."
    ">She collapses onto her robe, no longer held up by your member."
    m "You did good, [hermione_name]..."
    m "Wouldn't you say the same, ghost?"
    m "Ghost?"
    m "Oh well..."
    ">You notice Hermione start to shiver in the cold air..."
    m "I suppose I better get you back to your room."
    ">You wrap her robe over her like a blanket and carry her back to her room."
    ">You softly place her into her bed and pull up her sheets."

    menu:
        m "(Should I clean her up a bit?)"
        "-clean her up-":
            m "(I suppose I should..."
            ">You use a rag and wipe her face clean."
            her "*zzz* no... *zzz* I wanna be a.. *zzz* cumslut... *zzz*"
            m "*Shhh*... Don't worry, [hermione_name], I will give you more tomorrow."
        "-leave her be-":
            m "(She looks better like this anyway...)"
            ">As you turn to leave, you notice a content smile form over Hermione's face as she pulls her sheets up over her shoulders."
            her "{size=-4}Night sir...{/size}"
            her "{size=-8}I love you...{/size}"

    ">You turn and leave the warm room and return to your cold, dark office..."

    return

label forest_BJ_4: #Moaning myrtle dirty talk (Repeatable) (Threaten to expose)
    $ forest_BJ_progress = 3 #Repeats 3rd event after this one.
    show screen blkfade
    with d3

    call play_music("night_outside")
    call play_sound("walking_on_grass")

    $ hermione.wear("top")
    $ hermione.wear("bottom")

    ">Once more, the marauders map leads you to Hermione at the edge of the forest, waiting patiently, apparently having dropped all pretences botanical."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    m "[hermione_name]..."
    call her_main("About time you got here, [genie_name]!", "upset", "narrow", "annoyed", "mid", xpos="base", ypos="base", trans=d5)
    call her_main("Do you know how long I've been waiting out here in the cold?", "annoyed", "happy", "base", "mid")

    menu:
        "-Sorry-":
            m "Sorry about that..."
            m "I'll try and be on time for our blowjobs from now on."
            call her_main("Good... It's the least you can do...", "base", "closed", "angry", "mid")
        "-You know where my office is-":
            call her_main("*Hmph*...", "upset", "narrow", "angry", "R")

    show screen blkfade
    with d3

    ">Hermione then kneels down onto the pillow and rug she must have lain down before your arrival."
    ">You quickly walk over to the small girl and present her your thick cock."

    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 15
    $ ccg3 = "overlay"
    hide screen hermione_main
    show screen ccg
    hide screen blkfade
    with d3

    her "*Mmmmm*..."
    $ ccg2 = 17
    her "This almost makes waiting out in the cold worth it..."
    m "Only almost?"
    her "Well it's not the real reason I'm down here, [genie_name]..."
    $ ccg2 = 19
    her "this is..."
    $ ccg2 = 16
    ">Hermione quickly pops her head forward, wrapping her soft lips around the tip of your shaft."
    her "*Mmmmm*"
    $ ccg2 = 18
    her "*slurp* *glck* *slrp*"
    $ ccg2 = 20
    m "*Ughhhh*.... that's it, [hermione_name]..."
    m "Be a good little cockslut for you headmaster..."
    $ ccg2 = 16
    her "*slurp*{heart}*slurp*{heart}*glck*"
    #Myrtle fade in
    $ ccg1 = "m2"
    m "And for Casper the slutty ghost here..."
    $ ccg2 = 43
    her "*slurp*!!!*slurp*!!!*glck*"

    menu:
        "Once again, Hermione tries to pull herself of your cock..."
        "-Let her-":
            ">Reluctantly, you allow the girl to pull herself of your throbbing member..."
            $ ccg2 = 10
            her "Myrtle! What are you doing here again?"
            myr "Aren't I allowed a bit of fun in my afterlife?"
            myr "It's not like I ever got any when I was alive..."
            $ ccg2 = 6
            her "Oh alright then..."
            $ ccg2 = 10
            her "Just don't go blabbing to everyone in the girls' bathroom, OK?"
            myr "Deal..."
            m "Good... Now why don't you just sit back and enjoy the show then..."
        "-Face fuck her-":
            pass

    $ ccg2 = 28
    ">you place your hand on the back of Hermione's head and pull her hard into your waiting cock, impaling the poor girls throat... "
    $ ccg2 = 29
    her "{size=+10}!!!{/size}"
    $ ccg2 = 30
    g4 "Ugh... fuck yes..."
    $ ccg2 = 31
    her "{size=+5}*Gobble-gobble-slurp-gobble!* !!!{/size}"
    $ ccg2 = 30
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    $ ccg2 = 31
    myr "Wow... you're so rough on her..."
    $ ccg2 = 32
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 33
    g9 "Ugh... don't worry... she loves it..."
    $ ccg2 = 32
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 33
    g9 "She's probably wetter than the nile down there..."
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 32
    myr "You think so?"
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 33
    g9 "Go see for yourself!"
    $ ccg2 = 32
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 33
    myr "..."
    $ ccg2 = 32
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 33
    $ ccg1 = "blank"
    ">Myrtle floats down into the earth."
    $ ccg2 = 34
    her "{size=+10}!!!{/size}"
    $ ccg2 = 35
    myr "She's dripping!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35
    myr "Not to mention she isn't wearing any panties!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35
    g4 "She stopped wearing them months ago."
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35
    $ ccg1 = "m2"
    myr "Hermione! You horny little slut!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35
    myr "Just wait until the girls' bathrooms hear about tonight!"
    $ ccg2 = 34
    her "{size=+5}*glck*HNNOOO*glck*{/size}"
    $ ccg2 = 44
    myr "So long as you're alright with that, Sir... I don't have to mention you! It can just be Hermione!"
    $ ccg2 = 34
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 35

    menu:
        "\"Go nuts\"":
            $ ccg2 = 34
            myr "Really?"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}PRFFSSRR!!!{heart}*glck*{/size}"
            $ ccg2 = 34
            myr "Oh thank you, thank you, thank you!"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
            $ ccg2 = 34
            myr "This is going to be the best decade of my afterlife!"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
            $ ccg2 = 34
        "\"you can say it was me\"":
            $ ccg2 = 34
            myr "{size=+2}{b}Really?{/b}{/size}"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}WHHTT!!!{heart}*glck*{/size}"
            $ ccg2 = 34
            myr "Oh thank you, thank you, thank you!"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
            $ ccg2 = 34
            myr "This is going to be the best decade of my afterlife!"
            $ ccg2 = 35
            her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"

    $ ccg2 = 34
    myr "I can't wait to tell everyone!!!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "I'll go to rave-NO the Slytherin bathroom first!"
    $ ccg2 = 44
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then Gryffindor!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "Ravenclaw!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "Hufflepuff!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "The prefects' bathroom!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then the teachers!"
    $ ccg2 = 35
    her "{size=+5}*glck*{heart}*glck*{heart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then Hogsmeade!"
    $ ccg2 = 35
    myr "{size=+2}THEN{/size} {size=+2}THE{/size} {size=+2}WHOLE{/size} {size=+2}WORLD!!!{/size}"
    $ ccg2 = 34
    g9 "ARGH, HERE IT COMES SLUTS!"
    $ ccg2 = 35
    g4 "{size=+7}ARGH!{/size}"
    $ ccg2 = 34
    g4 "{size=+7}Eat my cum, slut!{/size}"
    show screen blkfade
    with d3

    $ ccg1 = "blank"
    ">At the edge of your orgasm, Hermione forcefully pushes herself off your dick and wraps your cock in her hands and hair."
    $ ccg2 = 45
    hide screen blkfade
    with d3

    her "{size=+5} That's it, Professor, Cum for me! Cover me in front of Myrtle!{/size}"
    with hpunch
    g4 "{size=+5}What the hell is this?!{/size}"
    $ ccg2 = 46
    her "{size=+5}Cum on sir! Aren't I your dirty little cumslut?{/size}"
    g4 "*Argh*! You cum obsessed whore!"
    $ ccg2 = 45
    her "{size=+5}Yes I am!{/size}"
    her "{size=+5}Nothing but your cum hungry little slut, sir!{/size}"
    $ ccg2 = 47
    her "{size=+5}Now why don't you show Myrtle here what a real load looks like!{/size}"
    with hpunch
    g4 "{size=+7}Argh!!!{/size}"
    g4 "{size=+7}Take this, then!!!{/size}"

    show screen white
    pause .1
    hide screen white
    with hpunch
    $ ccg2 = 48
    her "{size=+5}*Ah*! Yes, sir! Yes! cum all over me!{/size}"
    show screen white
    pause.1
    hide screen white
    $ ccg2 = 49
    pause.2
    show screen white
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+7}*ARGH*!{/size}"
    g4 "{size=+7}*Argh*!!! YES!!!{/size}"
    $ ccg2 = 50
    her "{heart}{heart}{heart}{heart}"
    show screen blkfade
    with d3

    #Genie and Hermione back in the forest...
    $ ccg1 = "blank"
    $ ccg2 = "blank"
    $ ccg3 = "blank"

    call her_main("Wait, where's Myrtle?", "angry", "narrow", "worried", "mid_soft")
    m "Oh, she left as soon as I gave her the OK to blab on about you."
    call her_main("WHAT?", "scream", "wide", "base", "stare")
    call her_main("you mean she didn't see any of...", "upset", "narrow", "annoyed", "mid")
    call her_main("(I got my hair all sticky for nothing...)", "upset", "narrow", "worried", "down")
    m "So are you going to clean yourself up and get dressed?"
    call her_main("I'll get dressed...", "soft", "base", "base", "R")
    call her_main("but If it's all the same to you, I might leave the cum on...", "base", "narrow", "base", "dead")
    m "Good girl..."
    show screen blkfade
    with d3

    ">You and Hermione walk back to the castle together, Hermione complaining about how rude Myrtle was for missing the cum shot the whole way..."

    return




label hermione_map_sex:
    #Genie notices hermione walking past the courtyard on the map and has the
    #option to intercept her option to come behind and scare her or to
    #approach her normally
    #Hermione says that she was coming back late from the library
    #Standard sex scene with a focus on the fact that they could be caught at any time
    #Option to humiliate her based on either the shame of doing this in public or to tell her that all her teachers want to fuck her
    #Cum in her in front of Moaning myrtle
    #end
    ">This time, the marauders map leads you to Hermione walking through the halls bordering the courtyard."
    ">You start to stalk her as a lion would its prey wondering how to best approach the girl..."
    menu:
        "-Surprise her-":
            "asd"
            pass
        "-Greet her-":
            "asd"
            pass

    m "*Mmmm*, gods your pussy is just the best..."
    her "*A-Ah*... thank you..."
    m "*Ugh*... so what are you doing out here at this hour anyway?"
    her "I was -- *ah* {heart} at the library..."
    m "*Mmmm*, what were you reading? Dick-sucking 101?"
    her "*Ah*...{heart} I'd like to think... *ah*{heart} that I'm past the 101 stage [genie_name]..."
    m "True, you could probably write the book!"
    her "*Mmmmm*...{heart} I'd probably have to... *ah*{heart} use a pseudonym..."
    m "Really? Worried about people finding out what a dirty little cock-slut you are?"
    her "I am not a--"
    ">You interrupt her ministrations with a forceful thrust deep into her pussy."
    her "{heart}Ah!!!{heart}"
    m "You were saying?"
    her "*Ah*...{heart}fine..."
    her "have it your way then..."
    m "I intend to!"
    m "Besides, if you really were worried about people finding out about you then you probably wouldn't be fucking your headmaster in public!"
    her "*Ah*...{heart} that's not-- *Ah*...{heart} this isn't my fault...{heart}"
    m "Really? And just how am I expected to turn up a chance to fuck this tight little cunt!"
    her "*A-Ah*... {heart}you're Professor{heart} Dumbledore{heart}... You should...{heart}"
    m "The gods themselves wouldn't miss an opportunity like this..."
    her "...{heart}"
    m "I think it's about time you just come to admit what a needy little fuck hole you really are..."
    her "*Ah*...{heart}a-all right...{heart}"
    m "Go on then slut... yell it out!"
    her "*Ah*...{heart}I-I can't!{heart} people will hear!"
    m "Good! A whore like you deserves an audience..."
    her "{heart}...{heart}"
    ">Despite feeling her pussy spasm hard around your cock the girl remains silent..."
    her "..."
    her "{size=+5}*Ah*... fuck me harder!{/size}"
    m "That's it slut! Louder!"
    ">Hermione turns her head around, looking you square in the eye with a desperate yet smug look plastered over her face..."
    her "Make. me."
    ">Her sultry challenge ignites a flame in your core."
    g4 "MAKE YOU?"
    g4 "I'll MAKE YOU SCREAM SO LOUD THE WHOLE SCHOOL WILL HEAR YOU!"
    ">With that your hips go into overdrive as you plough the ever loving shit out of the poor girl."
    her "{size=+10}{heart}!!!{heart}{/size}"
    g4 "Tell me what you are!"
    her "{size=+10}{heart}A WHORE! [genie_name]'s WHORE!{heart}{/size}"
    g4 "LOUDER!"
    her "{size=+10}{heart}I'm A CUMSLUT! I'm a bitch in heat!{heart}{/size}"
    her "{size=+10}{heart}JUST FUCK ME HARDER!!!{heart}{/size}"
    g4 "LIKE THIS?"
    her "{size=+10}{heart}*ughhh*....{heart}{/size}"
    her "{size=+10}MORE!{/size}"
    ">As you and Hermione make as much noise as possible through the hallowed Hogwarts halls, a soft blue glow begins to appear in front of Hermione."
    myr "Hello again Hermione..."
    myr "\"Professor\"..."
    her "{size=+10}Myrtle!{/size} W-w-what are you doing here?"
    myr "Well seeing as how I'm usually the only person moaning at this time of night I figured I better come take a look..."
    myr "But when I heard \"I'm a cumslut\"... I knew it had to be you two..."
    her "G-go -{heart}*Ah*...{heart}- go away Myrtle!"
    ">Enjoying feeling Hermione squirm at the mixture of shame and pleasure as you plow into her only spurs you on..."
    myr "And miss the only exciting thing that happens in this dull school? I think not..."
    her "*Ah*...{heart}"
    myr "Besides... I think you like being watched... Don't you Hermione?"
    her "*Ah*...{heart} of course-- *Ugh*...{heart} - not..."
    myr "Really? You mean you don't like me watching you be treated like a filthy little piece of fuck-meat?"
    her "*Ah*...{heart}{heart}{heart} no..."
    myr "I'm not so sure..."
    myr "What about you then? Do you like being watched..."
    ">Myrtle throws a knowing grin your way."
    m "I live for fucking pieces of ass like this!"
    m "Plus it's not like I have to worry about people watching me..."
    her "..."
    myr "You're right... Everyone's going to be far more interested in watching little miss Granger be fucked senseless."
    her "*Ah*...{heart}"
    myr "Isn't that right Hermione? I bet you'd love to be fucked within an inch of your life in front of the whole school!"
    ">Hermione's pussy grips hard onto your cock..."
    her "{heart}N-no!{heart} Don't s-say things like that!"
    g4 "Ugh... She's squeezing my cock like a vice!"
    myr "Did just the thought of that get you all hot an bothered?"
    her "*Ah*...{heart}no--{heart}"
    myr "The thought of being drenched in cum--"
    her "*Ah*...{heart}"
    myr "While Dumbledore breeds you like the whore you are..."
    her "{heart}{heart}{size=+5}*Mmmm*...{/size}{heart}{heart}"
    myr "While the school watches on..."
    her "{heart}{heart}{size=+10}*Ah*...{/size}{heart}{heart}"
    myr "Along with {i}mummy{/i} and {b}daddy{/b}..."
    her "{heart}{heart}{size=+15}!!!{/size}{heart}{heart}"
    ">It all proves too much for Hermione, causing her hips to buck wildly, desperate for any additional stimulation."
    g4 "That's it whore! You've done it now!"
    ">You grab onto Hermione's hips and start pumping for dear life."
    her "{heart}{heart}{size=+5}No! I just came! STOP!!!{/size}{heart}{heart}"
    ">The halls resonate with Hermione's incoherent moans and the forceful slapping of her ass against your hips."
    g4 "TAKE THIS!!!"
    ">You dump your load into Hermione's limp body as you hold her up."
    her "*Ahhh*..."
    g4 "Take this you filthy whore!"
    ">As you keep pumping more and more cum into Hermione's tightness, Myrtle watches on with a perverted smile..."
    her "....."
    myr "Wow... {w=0.3} And here I thought I was a moaner..."
    her "......."
    #FTB
    ">You let go of hermione, letting her slump to the ground with a squelch, landing in a pool of your combined juices.."
    #Take Hermione back to her room and leave Myrtle alone to masturbate
