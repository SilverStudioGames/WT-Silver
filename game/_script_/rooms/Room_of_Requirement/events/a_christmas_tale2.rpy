
default persistent.xmas_2020 = False

label a_christmas_tale2:
    # Proxy label to allow launching the story from within mirror of erised
    # because it's not possible to jump directly including parameters. Sadface.
    call santas_little_helper(False)
    jump enter_room_of_req

label santas_little_helper(dream=True):
    if not dream:
        $ temp_date = day
        $ temp_gold = gold
        $ temp_day = daytime
        $ temp_color = interface_color
        $ temp_weather = weather

        call play_music("stop")
        call room("main_room")
        show screen blkfade
        with d5
        hide screen owl

        centered "{size=+7}{color=#cbcbcb}Santa's Little Helper{/color}{/size}"

        $ daytime = False
        call update_interface_color
    else:
        call play_music("stop")
        $ renpy.sound.play("sounds/snore1.mp3")
        gen "*Snore*{w=2.0}{nw}"
        call blkfade

    # Unlock and apply deco
    $ fireplace_xmas_ITEM.unlocked = True
    $ phoenix_xmas_ITEM.unlocked = True
    $ owl_xmas_ITEM.unlocked = True

    $ fireplace_deco_OBJ.room_image = fireplace_xmas_ITEM.id
    $ fireplace_xmas_ITEM.active = True

    $ phoenix_deco_OBJ.room_image = phoenix_xmas_ITEM.id
    $ phoenix_xmas_ITEM.active = True

    $ owl_deco_OBJ.room_image = owl_xmas_ITEM.id
    $ owl_xmas_ITEM.active = True

    # Setup
    $ ton_outfit_last.save() # Store current outfit.
    $ her_outfit_last.save() # Store current outfit.

    $ tonks.equip(ton_outfit_elf)
    $ hermione.equip(her_outfit_ribbon)

    $ hermione_chibi.zorder = 4

    $ fire_in_fireplace = True
    show screen fireplace_fire
    $ set_weather("snow")
    play weather "sounds/wind_long_loop.mp3" fadein 2 fadeout 2
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0

    show screen chair_left
    show screen desk
    call gen_chibi("hide")

    hide screen blkfade
    with d5

    call play_music("anguish")
    show screen bld1
    with d3
    nar "T'was the night before Christmas on a cold winter night."
    nar "We see the headmasters room but there's no one in sight."
    nar "No sound but the wind as the storm outside roars."
    nar "But then a man enters, as he never knocks on any doors."

    call sna_walk(action="enter")
    pause 0.5
    call sna_main("Genie I wanted--", "snape_06", trans=d3)
    hide screen snape_main
    with d3
    nar "Said the man as he entered."
    call sna_walk("desk", "base")
    call sna_main("Never here when you need him...", "snape_01", trans=d3)
    call sna_main("Are genies always this self-centred?", "snape_29")
    call sna_main("Another walk to the pub if I want to get pissed...", "snape_06")
    call sna_main("Another--", "snape_04")

    hide screen snape_main
    hide screen bld1
    with d3

    nar "Interrupted dialogue as the room filled with mist."
    nar "With three booming ho's, Santa Clause appeared."

    $ renpy.sound.play("sounds/fire_woosh.mp3")
    $ fire_in_fireplace = False
    stop bg_sounds
    hide screen fireplace_fire
    show screen genie_santa_chibi(620, 170, flip=True)
    call teleport((620+75, 440))
    call sna_chibi(flip=True)
    with d3
    call sna_main("Genie of course... You think I'd fall for that fake beard?", "snape_05", trans=d3)

    san_[1] "I think you must be mistaken."
    hide screen snape_main
    hide screen bld1
    with d3
    nar "Said Santa to the man."
    show screen bld1
    with d3
    san_[1] "I'm not Genie, I'm Santa!"
    san_[1] "I deliver presents!"
    san_[2] "That's the plan!"

    san_[1] "I bring cheers and presents, to all across the land."
    call sna_main("Are you sure about that? I don't see a sack in your hand...", "snape_01", trans=d3)
    hide screen snape_main
    with d3
    san_[1] "Be patient dear boy... Don't you give me that face."
    san_[1] "Your gift will get here soon through this office fireplace."
    hide screen bld1
    with d3

    nar "With a big puff of smoke and a whiz and a whirl, an elf stood before them."

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430))
    show screen xmas_bag((750, 290))
    call teleport((680+75, 460))

    show screen bld1
    with d3
    san_[2] "Now check out this girl!"

    call ton_main("", "horny", "narrow", "base", "mid", hair="happy", xpos="mid", trans=d3)
    call ctc
    hide screen tonks_main
    call sna_main("Now that is a present!", "snape_13", trans=d3)
    call sna_main("You've outdone yourself.", "snape_20")
    hide screen snape_main
    san_[1] "That's not your present, that's my sexy helper elf..."

    call ton_main("Eye's up here boy...", "base", "base", "base", "mid", hair="happy", trans=dissolve)
    call ton_main("Your present is in this sack...", "soft", "narrow", "base", "down", hair="happy")
    call ton_main("These milkers belong to Santa!", "horny", "narrow", "base", "L", hair="horny")
    san_[2] "They're my after-work Christmas snack!"

    hide screen tonks_main
    hide screen bld1

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430), xzoom=-1)
    with d3

    nar "And with a swish of her wand his present was revealed."

    hide screen xmas_bag
    show screen xmas_bagfloor((750, 290))
    show ch_hem ribbon zorder hermione_chibi.zorder at Transform(pos=(785, 450), xzoom=1)
    #call her_chibi(xpos=750, ypos=460)
    call play_sound("magic")
    with flash

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430), xzoom=1)
    with d3

    call her_main("", "soft", "base", "base", "mid", cheeks="blush", trans=dissolve)
    nar "In front of him a girl, no longer concealed."
    nar "With a bow around her pussy and ribbons around her tits."

    hide screen hermione_main
    with d3

    call sna_main("Now that's a proper present!", "snape_13", trans=d3)
    hide screen snape_main
    with d3
    san_[2] "Now unwrap those naughty bits!"

    call ton_main("Wait, I just remembered, don't unwrap the present yet!", "mad", "shocked", "base", "L", hair="happy", trans=dissolve)
    call ton_main("If he's not been good this year then a gift he cannot get.", "open", "closed", "shocked", "mid", hair="happy")
    hide screen tonks_main
    with d3

    san_[2] "I'm certain he's been good... Now unwrap her I insist!"

    call ton_main("I'm not so sure myself... His offences fill this list.", "upset", "narrow", "base", "down", hair="happy", trans=dissolve)
    hide screen tonks_main
    with d3

    san_[1] "Then read it for me elf... I'm sure it will be quick..."
    hide screen bld1
    with d3
    nar "The elf then unrolled it... A scroll six inches thick."

    call ton_main("Inflating the points gained to put the Slytherins in the lead...", "open", "base", "raised", "down", hair="happy", trans=dissolve)
    hide screen tonks_main
    with d3

    call her_main("What?", "clench", "happy", "angry", "mid", trans=dissolve)
    hide screen hermione_main
    with d3

    san_[1] "That can't be true!"
    call sna_main("Mere fabrications that, indeed...", "snape_35", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("Teaching plenty of classes despite that he's blind drunk.", "upset", "base", "shocked", "down", hair="happy", trans=dissolve)
    call sna_main("I can't believe they bought that it was {i}\"Essence du Skunk\"{/i}...", "snape_45", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("Punishing students for talking in class...", "open", "closed", "base", "mid", hair="happy")
    call sna_main("They were breaking the rules!", "snape_07", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("So is slapping their ass...", "disgust", "narrow", "base", "mid", hair="happy")
    san_[1] "Well I'm sure they're all right... It was only a slap..."
    call ton_main("I'm not done yet santa, there's more...", "annoyed", "narrow", "base", "L", hair="happy")
    san_[1] "What the crap..."

    call ton_main("Stealing mounds of sweets and sniffing girls hair...", "normal", "base", "raised", "down", hair="happy")
    call sna_main("Now let's be reasonable for a minute, this list isn't fair!", "snape_18",trans=d3)
    hide screen snape_main
    with d3

    san_[1] "I think he's got a point, at least he didn't curse..."
    call ton_main("You say that but now, is when the list is getting worse...", "disgust", "base", "base", "mid", hair="happy")

    call ton_main("He's bought blowjobs with house points... Now that doesn't sound great...", "open", "narrow", "base", "down", hair="happy")
    san_[2] "A misprint I'm sure!"
    call ton_main("The list says thirty-eight...", "mad", "wide", "base", "down", hair="happy")

    call ton_main("Wrapped around his finger... This is making me sick...", "upset", "base", "base", "down", hair="upset")
    call ton_main("This list is massive!", "clench", "wide", "annoyed", "down", hair="angry")
    san_[1] "Then just skim it real quick..."

    call ton_main("Taking girls books and replacing it with smut...", "disgust", "narrow", "base", "down", hair="happy")
    call ton_main("Then punishing them for it by spanking their butt...", "annoyed", "narrow", "annoyed", "mid", hair="happy")

    call sna_main("She had it coming I tell you... That girl was a whore...", "snape_12", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("See what I mean Santa?", "disgust", "base", "base", "L", hair="disgusted")
    call ton_main("And this list has even more...", "upset", "base", "base", "down", hair="happy")

    call ton_main("Confiscating panties... Cumming on floors...", "soft", "base", "annoyed", "down", hair="happy")
    call ton_main("Spying in the toilets...", "disgust", "narrow", "base", "down", hair="disgusted")
    call ton_main("Never knocks on any doors...", "open", "closed", "base", "mid", hair="happy")

    san_[1] "Never knocks on any doors?!"
    nar "Said Santa at last."
    san_[1] "Now that's a big offence!"
    call ton_main("You really think so Santa?", "annoyed", "wide", "raised", "mid", hair="happy")
    call sna_main("Blast...", "snape_11", trans=d3)
    hide screen snape_main
    with d3

    san_[1] "Sexual acts is one thing... But not knocking on doors!"
    san_[1] "A man without manners is what Santa Clause abhors."
    san_[1] "I can't give you a gift but I offer this advice."
    san_[1] "Most things I will ignore but good manners deem you nice."

    san_[1] "Now ladies it's time to leave, it is a busy time of year..."
    san_[1] "Let us empty this sack and spread my Christmas cheer."
    call ton_main("This meeting took way too long so we better spread it quick...", "mad", "base", "base", "L", hair="happy")
    call ton_main("I hope I get overtime for this...", "annoyed", "base", "base", "R", hair="happy")
    hide screen tonks_main
    with d3
    san_[2] "I'll let you ride my magic di--"

    call gen_chibi("hide")
    #call ton_chibi("hide")
    #call her_chibi("hide")
    hide ch_hem ribbon
    hide ch_ton elf
    call play_sound("magic")
    show screen xmas_smoke
    with flash

    #Effect and then they're gone

    nar "Smoke then filled the room and then slowly dispersed, his present now gone..."
    call sna_main("Santa, You're the worst...", "snape_03", trans=d3)
    nar "With the man's final words left echoing across the halls."
    nar "He had to spend another Christmas with the bluest of blue balls..."

    call hide_characters
    with d5

    # Unlock outfit message. Should only appear once.
    if not her_outfit_ribbon.unlocked or not ton_outfit_ribbon.unlocked:
        call unlock_clothing(text=">Several new clothing items for Hermione have been unlocked!", item=her_outfit_ribbon)
        call unlock_clothing(text=">Several new clothing items for Tonks have been unlocked!", item=ton_outfit_ribbon)

        $ unlock_clothing_compat(item=her_hat_elf)
        $ unlock_clothing_compat(item=her_outfit_xmas)
        $ unlock_clothing_compat(item=ton_outfit_elf)
        $ unlock_clothing_compat(item=ton_outfit_xmas)
        $ unlock_clothing_compat(item=ton_bra_pasties2)
        $ unlock_clothing_compat(item=ton_piercing1_nipple_bells)

    # Reset clothing.
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)

    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen xmas_bagfloor
    hide screen xmas_smoke

    # Mark as complete
    $ persistent.xmas_2020 = True

    if not dream:
        $ daytime = temp_day
        $ weather = temp_weather
        call update_interface_color

        return

    jump day_start

screen xmas_bag(pos):
    zorder 5
    add "images/misc/bag.webp" zoom 0.5 pos pos

screen xmas_bagfloor(pos):
    zorder 2
    add "images/misc/bag_floor.webp" zoom 0.5 pos pos

screen xmas_smoke:
    zorder 10
    add "xmas_smoke"

image xmas_smoke:
    "images/misc/smoke.webp"
    align (0.5, 0.5)
    zoom 0.55
    subpixel True

    parallel:
        linear 2.5 yoffset -10
        linear 2.5 yoffset 10
        repeat

    parallel:
        linear 5.0 xoffset 20
        linear 5.0 xoffset -20
        repeat
