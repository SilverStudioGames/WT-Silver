
label anal_pirate_event:
    # Mirror story: A booty at sea

    call room("main_room")
    show screen blkfade
    with d3

    call reset_menu_position

    centered "{size=+7}{color=#cbcbcb}A booty at sea{/color}{/size}"

    "This story is a rewrite of the \"Time for anal\" personal favour. And the genie is a pirate? Who knows... Enjoy."

    menu:
        "-Part one-":
            $ d_flag_01 = 0
        "-Part two-":
            $ d_flag_01 = 1
        "-Part three-":
            $ d_flag_01 = 2

    call music_block
    call her_chibi("stand","mid","base")
    call hide_blkfade

    if d_flag_01 == 0:
        call anal_pirate_event_1
    elif d_flag_01 == 1:
        call anal_pirate_event_3
    elif d_flag_01 == 2:
        call anal_pirate_event_3

    hide screen hermione_main
    call blkfade

    stop music fadeout 1.0
    stop bg_sounds

    hide screen ccg

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    call her_main("Thank you, captain...", "grin", "base", "base", "mid",xpos="right",ypos="base", cheeks="blush")

    call her_walk(action="leave")

    #TODO Unlock pirate outfit
    # if not hg_outfit_pirate_ITEM.unlocked:
    #     call unlock_clothing(">Congratulations! You have unlocked a new outfit!",hg_outfit_pirate_ITEM)

    if not card_exist(unlocked_cards, card_maslab):
        call give_reward("Ye plundered a special card from 'er cavern.", "images/cardgame/t1/genie_realm/maslab_v1.webp")
        $ unlocked_cards += [card_maslab]

    call blkfade
    #TODO Unequip the temporary pirate outfit
    call her_chibi("hide")
    hide screen main_room

    jump enter_room_of_req


label anal_pirate_event_1: # Call label
    m "lass... I'd like you to roleplay with me."
    call her_main("captain...?", "annoyed", "squint", "base", "mid")
    m "How familiar ye be wit' th' term \" Swabbing ye poop deck\"?"

    call her_main("Ninety galleon points...", "annoyed", "narrow", "annoyed", "mid")
    m "Wha'?"
    call her_main(".............................", "disgust", "narrow", "base", "mid_soft")
    m "Ah, well then lass. Ninety galleon points 'tis."
    call blkfade
    hide screen hermione_main
    $ renpy.play('sounds/cloth_sound.mp3')
    pause 2

    call anal_pirate_event_common_1_2

    return

label anal_pirate_event_2: # Call label
    m "lass?"
    call her_main("captain?", "soft", "base", "base", "mid")
    m "I shall be takin' ye on another voyage today..."
    call her_main(".............", "open", "squint", "base", "mid")
    m "Care t' guess wha' th' destination will be?"
    m "You have t' guess three times to find out."
    call her_main("...........", "annoyed", "squint", "angry", "mid")
    call her_main("Booty plundering?", "disgust", "narrow", "base", "mid_soft")
    g4 "Wha..........?!"
    g4 "How did ye...?"
    call her_main("You seem like a booty pirate kind of a man. captain...", "angry", "base", "angry", "mid")
    m "I'm not sure you know what that means, lass..."
    hide screen hermione_main
    with d3

    call anal_pirate_event_common_1_2

    return


label anal_pirate_event_common_1_2: # Call label
    #TODO Equip pirate outfit
    #call h_equip_temp_outfit(hg_outfit_pirate_ITEM)
    call hide_blkfade

    call her_main("...........", "annoyed", "base", "worried", "R")
    m "Time to get me ole cannon out..."
    call her_main(".................", "angry", "happyCl", "worried", "mid",emote="sweat")
    call blkfade
    call play_sound("climb_desk")
    pause 2
    m "*Hmm*..."
    $ renpy.play('sounds/boing02.mp3')
    call her_main("!!!", "angry", "wide", "base", "stare", ypos="head", flip=False)
    call play_sound("slap")
    g4 "Blistering barnacles!"
    call her_main("Ouch!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
    m "Jus' try t' loosen up a wee, would ye?"
    call her_main("I be tryin'!", "angry", "base", "base", "mid",tears="soft")
    m "Aye, wha' if I do this...?"
    $ renpy.play('sounds/boing03.mp3')
    call her_main("Ouch! Wha' are ye doin', captain?", "mad", "happyCl", "worried", "mid",tears="soft_blink")
    m "Aye, this won't work either..."
    m "*Hmm*..."
    m "Har har, I reckon I know wha' we should do."
    m "..."
    menu:
        "{size=-3}\"I reckon I'll raise the anchor 'n jus' set sail!\"{/size}":
            play music "music/pirate.mp3" fadein 1 fadeout 1
            play bg_sounds "sounds/CreakingShip.mp3"

            call her_main("Just set sail, captain?!", "angry", "wide", "base", "stare", ypos="head", flip=False)
            $ renpy.play('sounds/spit.mp3')
            g4 "*SPIT!*"
            call her_main("What are ye doing you Seadog!", "scream", "happyCl", "worried", "mid")
            call her_main("No, cap'n, Belay that! Ye're nah in open waters--", "open", "base", "base", "mid")
            m "No needs, raise the anchor! Heave Ho!"
            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            call her_main("ARGH!", "angry", "base", "base", "mid",tears="soft")
            call her_main("Ouch! Ouch! Ouch!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
            g4 "Nigh-on in! Me ship has left ye harbour lass!"
            call her_main("No, ye're hurtin' me! Ye be hurtin' me!", "scream", "happyCl", "worried", "mid")
            g4 "Yo Ho Ho!"
            call her_main("Blisterin' Barnacles! It hurts!", "scream", "happyCl", "worried", "mid")
            g4 "Shut it, lass! I be approaching ye secret cavern!"
            g4 "Yer cavern be so tight 'tis completely un-plunderable!"
            call her_main("Then stop, Scallywag!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
            m "Neigh! We needs t' excavate yer cavern a wee!"
            call her_main("But I don't wants ye t'!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
            m "Aye? How do ye expect scallywags t' farrg ye up yer arse then?"
            call her_main("Wha' scallywags?", "shock", "happyCl", "worried", "mid")
            g4 "Ye know... scallywags."
            g4 "Argh, Blimey... Me cannon be to wide now."
            call her_main("Stop then! Avast, captain!", "open", "happyCl", "worried", "mid")
            call her_main("Change course captain, I've changed me mind! I don't needs ninety galleon points!")
            g4 "I reckon I be right on course..."

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")
            g4 "Yo Ho Ho!!!"

            if use_cgs:
                call blkfade
                $ ccg_folder = "herm_sex"
                $ ccg1 = 1
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                $ hermione_zorder = -1
                hide screen hermione_main
                show screen ccg
                call hide_blkfade
            else:
                call her_chibi_scene("sex_slow")
                with d5

            call her_main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!", "scream", "wide", "base", "stare")
            g4 "Let us pump this wee cavern full o' seamen then, savvy?"
            $ ccg1 = 19
            call her_main("Aye... , I jus' wants this t' end...", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="crying")
            g4 "Agh... Ye wants this voyage t' end sooner?"
            g4 "I smell mutiny, do ye want to walk the plank?"
            $ ccg1 = 18
            call her_main("*sob!* How?", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            g4 "Ye know..."
            call her_main("Aye...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            $ ccg1 = 20
            call her_main("I be a wench??", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            g9 "Yes ye be!"
            $ ccg1 = 21
            call her_main("*Sob!* I be a wench...", "angry", "squint", "base", "mid",cheeks="blush")
            call her_main("I love t' suck ye pegleg...")
            $ ccg1 = 22
            call her_main("'n now me wee asshole be gettin' ripped t' pieces... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            g4 "Shiver Me Timbers!"
            g4 "Agrh! Thar She Blows!"
            $ ccg1 = 23
            call her_main("No! Be it gettin' bigger?! I be like a harpoon!", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "ARGH!"

        "{size=-3}\"Lather me cannon balls first. Lubricate me pegleg!\"{/size}":
            call her_main("Oh... Alright...", "open", "base", "base", "mid", ypos="head", flip=False)
            play music "music/pirate.mp3" fadein 1 fadeout 1
            play bg_sounds "sounds/CreakingShip.mp3"

            call her_chibi_scene("bj")

            hide screen blktone
            hide screen bld1
            call hide_blkfade
            call ctc

            call her_main("*Slurp!* *Slurp!* *Slurp!*")
            m "Aye... good..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Yarr, I reckon that be enough. Back on th' ship now."

            call her_chibi_scene("sex_pause", trans=fade)

            # On the desk
            call her_main(".............", "open", "base", "base", "mid")
            g4 "Aye! Sail, Ho!!"
            call her_main("Ouch!", "scream", "happyCl", "worried", "mid")
            m "Relax lass. Approaching harbour."

            if use_cgs:
                show screen blkfade
                with d5
            pause.2

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")

            if use_cgs:
                $ ccg_folder = "herm_sex"
                $ ccg1 = 1
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                $ hermione_zorder = -1
                hide screen hermione_main
                show screen ccg
                hide screen blkfade
                with d5
            else:
                call her_chibi_scene("sex_slow", trans=d5)
                with d5

            g4 "Argh!!!"
            $ ccg1 = 14
            call her_main("Ye... ye...", "scream", "wide", "base", "stare")
            $ ccg1 = 6
            call her_main("Ye ship be to great", "shock", "happyCl", "worried", "mid")
            g4 "Let us pump this wee cavern full o' seamen then, savvy?"
            $ ccg1 = 21
            call her_main(".....................", "angry", "squint", "base", "mid",cheeks="blush")
            call ctc

            $ ccg1 = 18
            call her_main(".....................", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Ye be fine thar, wench?"
            $ ccg1 = 20
            call her_main("Blisterin' Barnacles... Ye be... turnin' me folds inside out... captain.", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            $ ccg1 = 21
            call her_main("Me stitches be breaking", "angry", "squint", "base", "mid",cheeks="blush")
            m "Aye..."
            m "Maybe me cannon needs swabbin'...?"
            m "Go below deck, lass. swabb me cannon some more."
            $ ccg1 = 20
            call her_main("Wha'? But...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            $ ccg1 = 18
            call her_main("But it be rusty... 'tis been in me bilge.", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Aye, 'tis been abaft, but that's nah nigh ye bilge."
            m "Heave ho landlubber or me ship be sinkin', lass. Swab me cannon some more."
            $ ccg1 = 21
            call her_main("...........", "shock", "base", "base", "R",cheeks="blush",tears="soft")

            # Sucking
            hide screen ccg
            call her_chibi_scene("bj")
            with fade
            call ctc

            call her_main("*Slurp!* *Slurp!* *Slurp!*", ypos="head", flip=False)
            m "Aye... good lass..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Can ye taste yer arse on me cannon?"
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Aye, Maybe that be enough."

            if use_cgs:
                $ ccg_folder = "herm_sex"
                $ ccg1 = 18
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                $ hermione_zorder = -1
                hide screen hermione_main
                show screen ccg
                with fade
            else:
                call her_chibi_scene("sex_slow")
                with fade
            call ctc

            call her_main("*Ah*...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "We be smooth sailing lass?"
            $ ccg1 = 20
            call her_main("It still be hurting...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("But th' storm has passed.")
            m "I'll adjust th' sails fer now..."
            $ ccg1 = 21
            call her_main("*Ah*... I be greatful, captain.", "angry", "squint", "base", "mid",cheeks="blush")
            m "Oh... aye... ye secret cavern be great..."
            $ ccg1 = 18
            call her_main("...........", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Oh... Ye cavern be perfect, lass..."
            $ ccg1 = 29
            call her_main("................", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
            m "Why are ye bein' so quiet lass?"
            $ ccg1 = 20
            call her_main("'cause 'tis cavern be too shallow for ye ship...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("'n I jus' wants ye t' cum sooner, captain...")
            m "So ye stifle yer cries o' pain?"
            $ ccg1 = 22
            call her_main("Aye captain. *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Nah on me ship lass."
            m "Sob, scream 'n cry as much as ye wish!"
            $ ccg1 = 20
            call her_main("B-but--", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "That shall make me cannon ready t' fire in ye broadside."
            $ ccg1 = 22
            call her_main("be this true? *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            $ ccg1 = 18
            call her_main("*Sob!* Me hull! *Sob!* It be taking in water! *Sob!*", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Aye, ye ship be sinking... ye booty be mine."
            $ ccg1 = 24
            call her_main("*SOB!*", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "Ye poor wee sprog..."
            m "A grand, wicked pirate be plunderin' yer booty!"
            $ ccg1 = 25
            call her_main("*SOB!* Yeees! *SOB!*", "scream", "squint", "base", "mid",cheeks="blush",tears="messy")
            g4 "Take me seamen!"
            $ ccg1 = 30
            call her_main("No, I'm scared! *SOB!*", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="messy")

        "{size=-3}\"Let me oil ye up.\"{/size}":
            call play_music("playful_tension")
            call her_chibi_scene("sex_pause", trans=fade)
            call her_main("oil, cap'n?!", "angry", "wide", "base", "stare")
            m "Blimey! Just stay still."
            "*Squeeze!*"
            call her_main("Ahhh! Shiver me timbers, It's cold!", "scream", "happyCl", "worried", "mid")
            call nar(">Ye thoroughly oil 'er cavern.")
            m "Sail ho!"
            call her_main("Nay, cap'n, wait! Maybe--", "angry", "base", "worried", "mid")
            call nar(">Alas! Ye align thee tip of yer dick with 'er slimey winky cavern and push fore.")

            if use_cgs:
                show screen blkfade
                with d5
            pause.2

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("ARGH!", "shock", "base", "base", "mid", tears="soft")
            call nar(">Yer cock fully penetrating her as thee oil does its job.")
            g4 "Farrg me!"

            if use_cgs:
                $ ccg_folder = "herm_sex"
                $ ccg1 = 11
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                $ hermione_zorder = -1
                hide screen hermione_main
                show screen ccg
                hide screen blkfade
                with d5
            else:
                call her_chibi_scene("sex_slow", trans=d5)

            call her_main("Ouch! Ouch! Ouch!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
            $ ccg1 = 1
            call her_main("No, ye're hurtin' me! Ye be hurtin' me!", "scream", "happyCl", "worried", "mid")
            g4 "*Argh* Farrg, I can nah pull out!"
            $ ccg1 = 11
            call her_main("Sink me! It hurts!", "scream", "happyCl", "worried", "mid")
            g4 "Then stop clenching on me so hard, ye wench!"
            g4 "Yer cavern be so tight I can nah even move!"
            $ ccg1 = 19
            call her_main("Do somethin'!", "mad", "happyCl", "worried", "mid",tears="soft_blink")
            g4 "I be tryin', wench!"
            $ ccg1 = 20
            call her_main("Then try harder!", "scream", "base", "angry", "mid",tears="soft")
            call slap_her
            $ ccg1 = 23
            call her_main("..........!", "scream", "wide", "worried", "mid",tears="soft")
            g4 "Shut th' Davy Jones' locker up, strumpet!"
            g4 "'tis..."
            call slap_her
            g4 "'tis...{fast} yer..."
            call slap_her
            g4 "'tis... yer...{fast} bloody..."
            call slap_her
            g4 "'tis... yer... bloody... {fast}fault!"
            $ ccg1 = 22
            call slap_her
            pause 1.0
            call play_sound("boing")
            with hpunch
            if not use_cgs:
                call her_chibi_scene("sex_pause", trans=d5)
            pause 1.0
            m "Oh, 'tis worked."

            call her_main("*sob!*", "mad", "base", "angry", "down",cheeks="blush",tears="soft")
            call her_main("... me cavern... me poor cavern... *sob*","mad", "base", "angry", "mid",cheeks="blush",tears="soft")
            g9 "In that case, let's try it again."
            $ ccg1 = 19
            call her_main("No! Avast! Cap'n!", "open", "wide", "worried", "mid",cheeks="blush",tears="soft")
            call her_main("I 'ave changed me mind!",cheeks="blush",tears="soft")
            m "'twill be fine this time, trust me..."

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            $ ccg1 = 23
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")
            g4 "YARR!!!"

            if not use_cgs:
                call her_chibi_scene("sex_slow", trans=d5)

            call her_main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!", "scream", "wide", "base", "stare")
            g4 "I shall pump this wee cavern full o' seamen then, savvy?"
            $ ccg1 = 24
            call her_main("Aye... , I jus' wants this t' end...", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="crying")
            g4 "Agh... Ye wants 'tis t' end sooner?"
            g4 "Help me out then!"
            call her_main("*sob!* How?", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            g4 "Ye know..."
            call her_main("Oh...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            call her_main("I be a wench??", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            g9 "Aye ye be!"
            $ ccg1 = 23
            call her_main("*Sob!* I be a wench...", "angry", "squint", "base", "mid",cheeks="blush")
            $ ccg1 = 18
            call her_main("I love t' suck pegleg...")
            $ ccg1 = 20
            call her_main("'n now me wee cavern be gettin' ripped apart... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            g4 "Aye! Aye!"
            g4 "Agrh! AYE!"
            $ ccg1 = 19
            call her_main("No! Be it gettin' bigger?! I be yellow-bellied!", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "ARGH!"

    menu:
        "-Sink her vessel, fill her up-":
            g4 "Argh!"
            $ ccg1 = 1
            $ renpy.play('sounds/fuse.mp3')
            call her_main("No! AH!", "scream", "wide", "base", "stare", ypos="head", flip=False)
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)
            else:
                $ ccg3 = "s1"
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            call ctc

            $ ccg1 = 23
            call her_main("AH! ME BILGE IS FILLING UP! Sink Me!{heart}{heart}{heart}", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "Aye, ye wench! I be shooting me cannons!"
            $ ccg1 = 24
            call her_main("Me hull is splintering, spare me Captain!", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            g4 "Ye're nah sunk yet!"
            $ renpy.play('sounds/cannon.mp3')
            with hpunch
            $ ccg1 = 23
            call her_main("No, I be already full! Stop cummin', ye bastard!", "scream", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "Shut th' farrg up, wench! Ye still be afloat!"
            $ ccg1 = 25
            call her_main("No! Me stomach! Me ship will capsize!", "scream", "squint", "base", "mid",cheeks="blush",tears="messy")
            $ renpy.play('sounds/cannon.mp3')
            with hpunch
            g4 "ARGH!"
            $ ccg1 = 23
            call her_main("No! I reckon me bilge be flooded... I must get t' me pumps.", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            $ renpy.play('sounds/cannon.mp3')
            with hpunch
            $ ccg1 = 26
            play sound "sounds/burp.mp3"
            call her_main("{size=+7}*BURP!*!!!!!{/size}", "full", "wide", "worried", "stare",tears="messy")
            $ ccg1 = 27
            call her_main(".......................", "full", "base", "base", "mid",tears="messy")
            call her_main(".............")
            $ renpy.play('sounds/gulp.mp3')
            $ ccg1 = 28
            call her_main("{size=+7}*GULP!*{/size}", "cum", "happyCl", "worried", "mid")
            $ ccg1 = 24
            call her_main("*SOB!* I HATE YOU...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            $ ccg1 = 25
            call her_main("{size=+5}I HATE YE'N AND YER RUSTY OLE CANNON!{/size}", "scream", "base", "angry", "mid",cheeks="blush",tears="messy")
            call her_main("{size=+5}I HATE YE'N! YE HEAR ME?!{/size}")
            g4 "Agh... Dead men tell no tales, wench!"
            $ ccg1 = 24
            call her_main("*sob!* *Sob!*...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")

            # After cum inside
            if not use_cgs:
                call her_chibi_scene("sex_cum_in_done", trans=d5)

            $ ccg1 = 22
            call her_main("*Sob!*...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Whew!... I reckon me gunpowder needs restocking in the next harbour.' it be."
            m "Ye afloat lass?"
            call her_main("Aye... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Is that sea water in ye eyes?"
            call her_main("Me bilge is flooded, but me pumps be workin, captain...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Aye, ye took me cannonfire broadside, Ye be a well built vessel ..."
            call her_main("Thank ye captain...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            hide screen bld1
            with d3
            call ctc

            call blkfade
            hide screen ccg
            hide screen blkfade
            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            $ hermione_zorder = 15 # Reset zorder
            $ hermione.set_cum(pussy="light")

            call her_main("I apologise for saying that I hate you, captain...", "base", "base", "base", "R",cheeks="blush",tears="mascara", ypos="head", flip=False)
            call her_main("And your cannon is not rusty...",cheeks="blush",tears="mascara")
            call her_main("I don't know what's gotten into me...", "grin", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            g9 "My cannonfire!"
            call her_main("I suppose it's when you call me a \"wench\". I know that it's just roleplay...", "grin", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            m "Aye, sure..."
            m "Does it still hurt?"
            call her_main("A little...", "open", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            call her_main("I also feel full and warm inside...", "grin", "closed", "base", "mid",cheeks="blush",tears="mascara")
            m "You plan to keep it in? My cum I mean."
            call her_main("Aye..", "grin", "narrow", "base", "mid_soft",cheeks="blush",tears="mascara")

            if daytime:
                call her_main("I hope I won't spring a leak during my classes...",cheeks="blush",tears="mascara")
            else:
                call her_main("I hope it won't spring a leak before I get to my cabin...",cheeks="blush",tears="mascara")

            m "Well, good luck on your voyage."
            call her_main("Can I get paid now please?", "grin", "closed", "base", "mid",cheeks="blush",tears="mascara")

        "-Spread yer cannon fire o'er er hull-":
            $ renpy.play('sounds/fuse.mp3')
            g4 "*argh*"
            g4 "{size=+6}Fire!{/size}"
            hide screen bld1
            with d3

            call cum_block
            $ renpy.play('sounds/cannon.mp3')
            with hpunch

            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)
            else:
                $ ccg3 = "s3"
            call cum_block
            $ hermione.set_cum(crotch="light")
            call ctc

            $ ccg1 = 7
            call her_main("*Ah*...{heart}{heart}{heart}", "silly", "narrow", "base", "dead", ypos="head", flip=False)
            g4 "Aye!!! All over yer hold!"
            $ ccg1 = 8
            call her_main("*Ah*... No, me hull!", "silly", "narrow", "annoyed", "up")
            hide screen bld1
            with d3
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            with hpunch
            call ctc

            hide screen ccg
            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            $ hermione_zorder = 15 # Reset zorder

            m "Well, I'm done... You can get off my ship now."
            call her_main("Yes, captain...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft", ypos="head", flip=False)
            m "You feeling alright?"
            call her_main("Yes, captain. It still hurts a little, but...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "But what?"
            call her_main("But in a good way... captain.", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "In a good way, *huh*?"
            g9 "Heh... You naughty, little pirate."
            call her_main("Can I my get my share of the booty now, captain?", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")

    return


label anal_pirate_event_3: # Call label
    m "How about another booty plunderin, lass?"
    call her_main("Of course, captain.", "base", "narrow", "base", "up")
    g9 "Raise anchor, you little tart!"

    #TODO Equip pirate outfit
    #call h_equip_temp_outfit(hg_outfit_pirate_ITEM)

    stop music fadeout 1.0
    hide screen hermione_main
    call blkfade

    call her_main("........", "annoyed", "base", "worried", "R", ypos="head", flip=False)
    m "*Hmm*..."
    call her_main("...........", "open", "base", "base", "mid")
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("Ooooohhhhhhhhhhhh....{heart}", "scream", "wide", "base", "stare")

    if use_cgs:
        $ ccg_folder = "herm_sex"
        $ ccg1 = 15
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        $ hermione_zorder = -1
        hide screen hermione_main
        show screen ccg
        hide screen blkfade
    else:
        call her_chibi_scene("sex_slow", trans=d5)

    g4 "Oh, ye-es!"
    call her_main("*Ah*...", "soft", "narrow", "annoyed", "up")
    m "It seems like yer cavern be a bit more welcomin', lass."
    $ ccg1 = 31
    call her_main("*Ah*... It still be a bit tight.", "base", "narrow", "base", "mid_soft")
    call her_main("'n , jus' call me \"wench\", captain.", "base", "squint", "base", "mid")
    g4 "*Agh*! Ye wench! Ye always get me wit' yer words!"

    play music "music/pirate.mp3" fadein 1 fadeout 1
    play bg_sounds "sounds/CreakingShip.mp3"
    $ ccg1 = 32
    call her_main("*Ah*... *Ah*...", "open", "closed", "base", "mid")
    call her_main("*Ah*...")
    $ ccg1 = 31
    call her_main("captain?", "base", "narrow", "base", "mid_soft")
    m "Aye, wench?"
    $ ccg1 = 12
    call her_main("*Ehm*...", "angry", "base", "base", "mid")
    $ ccg1 = 13
    call her_main("Would ye settle down fer me, captain?", "angry", "narrow", "base", "down")
    with hpunch
    g4 "{size=+9} WHAT?!{/size}"
    g4 "Don't tell me ye're expecting cargo, lass!"
    $ ccg1 = 33
    call her_main("Ye seamen don't put no cargo in me bilge, captain...", "angry", "wink", "base", "mid")
    m "Wha' be this natter o' settlin down then?"
    $ ccg1 = 12
    call her_main("Ye misunderstood me captain.", "angry", "base", "base", "mid")
    $ ccg1 = 13
    call her_main("I meant t' say, would ye stop plunderin for a lass {size=+5}like{/size} me?", "angry", "narrow", "base", "down")
    $ ccg1 = 11
    call her_main("I would ne'er propose t' a scallywag wit' his pegleg in me arse, captain...", "angry", "happyCl", "worried", "mid",emote="sweat")
    m "Good. 'cause I don't reckon any scallywag would be able t' say \"neigh\" to you lassie."
    $ ccg1 = 32
    call her_main("Ah{heart}...", "open", "closed", "base", "mid")
    $ ccg1 = 13
    call her_main("Wha' I meant... ah{heart}... {w}t' say was ah{heart}... {w}do ye reckon any pirate would ever ah{heart}... {w}leave th' sea fer a lass like me?", "angry", "narrow", "base", "down")
    m "*huh*?"
    call her_main("I mean, wit' all that booty plunderin happenin' lately... *ah*{heart}...", "angry", "narrow", "base", "down")
    call her_main("I can nah help but feel like me hull is scratched... leakin even.")
    call her_main("'n in a no way untarnished...")
    $ ccg1 = 33
    call her_main("Who would wants t' settle fer a lass like that.", "angry", "base", "base", "mid")

    menu:
        m "..."
        "{size=-3}\"I would leave me ship in a heartbeat!\"{/size}":
            $ ccg1 = 10
            call her_main("What?", "open", "base", "base", "mid", ypos="head", flip=False)
            m "Aye, if only a lass like ye would board me ship..."
            $ ccg1 = 34
            call her_main("... Aye...{heart}", "base", "base", "base", "R")
            call her_main("..............", "base", "happy", "base", "mid")
            $ ccg1 = 35
            call her_main("Aye if only a lass like I, cap'n? So, why neigh me?", "soft", "base", "base", "mid")
            m "*huh*?"
            m "Wha' do ye mean \"why\", wench?"
            m "Ye be right out of harbour 'n ye only just set sail..."
            m "Tight cabin, shimering tits, 'n wet wee powder pan..."
            $ ccg1 = 32
            call her_main("*Ah*...{heart}", "open", "closed", "base", "mid")
            m "Ye will make some lucky scallywag a mighty happy one, some day, wench."
            m "*Ehm*, I mean, lass."
            $ ccg1 = 15
            call her_main("No, \"wench\" be good. you be calling me that more, captain.", "silly", "narrow", "annoyed", "up")
            m "Thar, ye see? Ye be a great catch, I be tellin' ye, wench."
            $ ccg1 = 22
            call her_main("*Ah*...{heart} Thank you, captain.", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "*huh*?"
            m "Ye helm be leakin."

        "{size=-3}\"A pirate not plunderin t' be wit' ye be o' th' picture\"{/size}":
            $ ccg1 = 13
            call her_main("I be thinkin that...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying", ypos="head", flip=False)
            m "Oh... I jus' love that wee cavern o' yers!"
            $ ccg1 = 11
            call her_main(".....................", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            $ ccg1 = 22
            call her_main("Aye... Aft all th' thin's I had t' do fer me crew...")
            call her_main("... nah one we pirate would leave th' sea fer me...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "Oh, they be leavin th's sea fer ye alright!"
            $ ccg1 = 19
            call her_main("Wha'? But ye said...", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "T' plunder yer cave, lass. But they'd go back t' sea."
            m "But as a cannon swabber ye be a great catch!"
            $ ccg1 = 14
            call her_main("Aye?", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "Ye pullin' me pegleg?!"
            m "Young, hot 'n slutty. Ye could 'ave any scallywag ye wants!"
            m "Or a landlubber or whatever ye be after..."
            $ ccg1 = 17
            call her_main("I reckon ye may be right, captain.", "base", "narrow", "worried", "mid_soft",cheeks="blush",tears="soft")
            m "I always be right, wench."
            m "Now wiggle that wee arse o' yers a wee."
            $ ccg1 = 11
            call her_main("Like this?", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m  "Aye, that be a good wench."
            $ ccg1 = 16
            call her_main("I be a wench, aren't I?", "silly", "narrow", "base", "dead")
            m "Ye jus' sold me yer asshole fer ninety galleon points. What ye be calling that?"
            $ ccg1 = 22
            call her_main("Yes, yes...{heart} I be nothing but a wench...{heart}", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "Ye helm be leakin."

    $ ccg1 = 8
    call her_main("Not only me helm, captain...{heart}{heart}{heart}", "silly", "narrow", "base", "dead")
    m "Not just ye helm?"
    $ ccg1 = 9
    call her_main("I'm cumming captain...{heart}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
    g4 "Agh! My cock!"
    g4 "Relax your muscles a little, would you?"
    $ ccg1 = 6
    call her_main("BUT I'M CUMMING!{heart}{heart}{heart}", "open", "happyCl", "worried", "mid")
    g4 "Fine! 'ave it yer way wench!"
    with hpunch
    $ ccg1 = 7
    call her_main("{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}", "scream", "wide", "base", "stare")
    g4 "{size=+7}Argh!{/size}"

    $ renpy.play('sounds/fuse.mp3')
    g4 "!!!"
    menu:
        "-Sink her vessel, fill her up-":
            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)
            else:
                $ ccg3 = "s1"
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            with hpunch
            $ hermione.set_cum(pussy="light")
            call ctc

            call her_main("!!!", "scream", "wide", "base", "stare", ypos="head", flip=False)
            m "Shiver me timbers! Argh!"
            $ ccg1 = 8
            call her_main("Ah!{heart} 'tis fillin' me up!{heart} me bilge is takin in water!{heart}", "silly", "narrow", "annoyed", "up")
            m "'tis nah water, wench!"
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            with hpunch
            $ ccg1 = 16
            call her_main("Ah! I BE A WENCH!!!!{heart}{heart}{heart}", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="crying")
            $ renpy.play('sounds/cannon.mp3')
            with hpunch
            m "*Agh*!"
            $ ccg1 = 15
            call her_main("*Ah*...{heart} yer seamen, captain...{heart}", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "Aye, my seamen..."
            $ ccg1 = 22
            call her_main("*Ah*...{heart}", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "......"

        "-Spread yer cannon fire o'er er hull-":
            hide screen bld1
            with d3

            $ renpy.play('sounds/cannon.mp3')
            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)
            else:
                $ ccg3 = "s3"
            call cum_block
            with hpunch
            $ hermione.set_cum(crotch="light")
            call ctc

            $ ccg1 = 17
            call her_main("Ah-aha! Ye're cummin'! {heart}{heart}{heart}", "silly", "narrow", "base", "dead", ypos="head", flip=False)
            g4 "{size=+7}Aye I do, wench{/size}"
            $ ccg1 = 16
            $ hermione.set_cum(crotch="heavy")
            call her_main("Blisterin' Barnacles, me too! Me too!", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="messy")
            g4 "{size=+7}FARRRGIN' WENCH!{/size}"
            $ renpy.play('sounds/cannon.mp3')
            call cum_block
            with hpunch
            $ ccg1 = 19
            call her_main("*Ah*...{heart} yer cum...{heart}", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            $ ccg1 = 17
            call her_main("Ye covered me whole deck{heart}{heart}{heart}")
            g4 "Aye!!! All o'er yer hull!"
            $ renpy.play('sounds/cannon.mp3')
            with hpunch
            $ hermione.set_cum(body="heavy")
            $ ccg1 = 22
            call her_main("Shiver me timbers... 'tis so hot!", "silly", "narrow", "annoyed", "up")

    #Ending
    call hide_characters
    show screen blkfade
    with d7

    hide screen ccg
    call her_chibi_scene("sex_pause", trans=fade)

    $ hermione_zorder = 15

    m "Well, tis been intense..."
    call her_main("*Ah-ha*...{heart} *ah*...{heart}", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy", ypos="head", flip=False)
    m "Ye be fine lass?"
    call her_main("I reckon so... I be nah sure...", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("I reckon I may still be leakin', captain.", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("Or maybe nah...", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("Everythin' be in a daze... 'n me legs feel so weak...")
    call her_main("Can I jus' get paid now, captain?")

    stop music fadeout 1.0

    return
