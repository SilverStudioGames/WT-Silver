label xmas_2020:

    # Setup
    $ hermione_chibi.zorder = 4

    $ fire_in_fireplace = True
    show screen fireplace_fire
    $ set_weather("overcast")
    play weather "sounds/wind_long_loop.mp3" fadein 2 fadeout 2
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
    call play_music("anguish")
    call hide_blkfade
    show screen chair_left
    show screen desk
    call gen_chibi("hide")

    nar "T'was the night before Christmas on a cold winter night."
    nar "We see the headmasters room but there's no one in sight."
    nar "No sound but the wind as the storm outside roars."
    nar "But then a man enters, as he never knocks on any doors."

    call sna_walk(action="enter")
    pause 0.5
    call sna_main("Genie I wanted--", "snape_01", trans=d3)
    hide screen snape_main
    with d3
    nar "Said the man as he entered."
    call sna_walk("desk", "base")
    call sna_main("Never here when you need him...", "snape_01", trans=d3)
    call sna_main("Are genies always this self-centred?", "snape_01")
    call sna_main("Another walk to the pub if I want to get pissed...", "snape_01")
    call sna_main("Another--", "snape_01")

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
    call sna_main("Genie of course... You think I'd fall for that fake beard again?", "snape_01", trans=d3)

    san_[1] "I think you must be mistaken."
    hide screen snape_main
    hide screen bld1
    with d3
    nar "Said Santa to the man."
    show screen bld1
    with d3
    san_[1] "I'm not Genie, I'm Santa!"
    san_[1] "I deliver presents!"
    san_[1] "That's the plan!"

    san_[1] "I bring cheers and presents, to all across the land."
    call sna_main("Are you sure about that? I don't see a sack in your hand...", "snape_01", trans=d3)
    hide screen snape_main
    with d3
    san_[1] "Be patient dear boy... Don't you give me that face."
    san_[1] "Your gift will get here soon through this office fireplace."
    hide screen bld1
    with d3

    nar "With a big puff of smoke and a whiz and a whirl, an elf stood before them."

    call ton_chibi(xpos=700, ypos="base")
    show screen xmas_bag((750, 290))
    call teleport((680+75, 460))

    show screen bld1
    with d3
    san_[1] "Now check out this girl!"

    call ton_main("", "horny", "narrow", "base", "mid", hair="happy", xpos="mid", trans=d3)
    call ctc
    hide screen tonks_main
    call sna_main("Now that is a present!", "snape_01", trans=d3)
    call sna_main("You've outdone yourself.", "snape_01")
    hide screen snape_main
    san_[1] "That's not your present, that's my sexy helper elf..."

    call ton_main("Eye's up here boy...", "base", "base", "base", "mid", trans=d3)
    call ton_main("Your present is in this sack...", "base", "base", "base", "mid")
    call ton_main("These milkers belong to Santa!", "base", "base", "base", "mid")
    san_[1] "They're my after-work Christmas snack!"

    hide screen tonks_main
    hide screen bld1

    call ton_chibi(flip=True)
    with d3

    nar "And with a swish of her wand his present was revealed."

    hide screen xmas_bag
    show screen xmas_bagfloor((750, 290))
    call her_chibi(xpos=750, ypos=460)
    call play_sound("magic")
    with flash

    call ton_chibi(flip=False)
    with d3

    call her_main("", "base", "base", "base", "mid", trans=d3)
    nar "In front of him a girl, no longer concealed."
    nar "With a bow around her pussy and ribbons around her tits."

    hide screen hermione_main
    with d3

    call sna_main("Now that's a proper present!", "snape_01", trans=d3)
    hide screen snape_main
    with d3
    san_[1] "Now unwrap those naughty bits!"

    call ton_main("Wait, I just remembered, don't unwrap the present yet!", "base", "base", "base", "mid", trans=d3)
    call ton_main("If he's not been good this year then a gift he cannot get.", "base", "base", "base", "mid")
    hide screen tonks_main
    with d3

    san_[1] "I'm certain he's been good... Now unwrap her I insist!"

    call ton_main("I'm not so sure myself... His offences fill this list.", "base", "base", "base", "mid", trans=d3)
    hide screen tonks_main
    with d3

    san_[1] "Then read it for me elf... I'm sure it will be quick..."
    hide screen bld1
    with d3
    nar "The elf then unrolled it... A scroll six inches thick."

    call ton_main("Inflating the points gained to put the Slytherins in the lead...", "base", "base", "base", "mid", trans=d3)
    hide screen tonks_main
    with d3

    call her_main("What?", "base", "base", "base", "mid", trans=d3)
    hide screen hermione_main
    with d3

    san_[1] "That can't be true!"
    call sna_main("Mere fabrications that, indeed...", "snape_01", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("Teaching plenty of classes despite that he's blind drunk.", "base", "base", "base", "mid", trans=d3)
    call sna_main("I can't believe they bought that it was {i}\"Essence du Skunk\"{/i}...", "snape_01", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("Punishing students for talking in class...", "base", "base", "base", "mid")
    call sna_main("They were breaking the rules!", "snape_01", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("So is slapping their ass...", "base", "base", "base", "mid")
    san_[1] "Well I'm sure they're all right... It was only a slap..."
    call ton_main("I'm not done yet santa, there's more...", "base", "base", "base", "mid")
    san_[1] "What the crap..."

    call ton_main("Stealing mounds of sweets and sniffing girls hair...", "base", "base", "base", "mid")
    call sna_main("Now let's be reasonable for a minute, this list isn't fair!", "snape_01",trans=d3)
    hide screen snape_main
    with d3

    san_[1] "I think he's got a point, at least he didn't curse..."
    call ton_main("You say that but now, is when the list is getting worse...", "base", "base", "base", "mid")

    call ton_main("He's bought blowjobs with house points... Now that doesn't sound great...", "base", "base", "base", "mid")
    san_[1] "A misprint I'm sure!"
    call ton_main("The list says thirty-eight...", "base", "base", "base", "mid")

    call ton_main("Wrapped around his finger... This is making me sick...", "base", "base", "base", "mid")
    call ton_main("This list is massive!", "base", "base", "base", "mid")
    san_[1] "Then just skim it real quick..."

    call ton_main("Taking girls books and replacing it with smut...", "base", "base", "base", "mid")
    call ton_main("Punishing them for it by spanking their butt...", "base", "base", "base", "mid")

    call sna_main("She had it coming I tell you... That girl was a whore...", "snape_01", trans=d3)
    hide screen snape_main
    with d3

    call ton_main("See what I mean Santa?", "base", "base", "base", "mid")
    call ton_main("And this list has even more...", "base", "base", "base", "mid")

    call ton_main("Confiscating panties... Cumming on floors...", "base", "base", "base", "mid")
    call ton_main("Spying in the toilets...", "base", "base", "base", "mid")
    call ton_main("Never knocks on any doors...", "base", "base", "base", "mid")

    san_[1] "Never knocks on any doors?!"
    nar "Said Santa at last."
    san_[1] "Now that's a big offence!"
    call ton_main("You really think so Santa?", "base", "base", "base", "mid")
    call sna_main("Blast...", "snape_01", trans=d3)
    hide screen snape_main
    with d3

    san_[1] "Sexual acts is one thing... But not knocking on doors!"
    san_[1] "A man without manners is what Santa Clause abhors."
    san_[1] "I can't give you a gift but I offer this advice."
    san_[1] "Most things I will ignore but good manners deem you nice."

    san_[1] "Now ladies it's time to leave, it is a busy time of year..."
    san_[1] "Let us empty this sack and spread my Christmas cheer."
    call ton_main("This meeting took way too long so we better spread it quick...", "base", "base", "base", "mid")
    call ton_main("I hope I get overtime for this...", "base", "base", "base", "mid")
    hide screen tonks_main
    with d3
    san_[1] "I'll let you ride my magic di--"

    call gen_chibi("hide")
    call ton_chibi("hide")
    call her_chibi("hide")
    call play_sound("magic")
    show screen xmas_smoke
    with flash

    #Effect and then they're gone

    nar "Smoke then filled the room and then slowly dispersed, his present now gone..."
    call sna_main("Santa, You're the worst!", "snape_01", trans=d3)
    nar "With the man's final words left echoing across the halls."
    nar "He had to spend another Christmas with the bluest of blue balls..."

    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen xmas_bagfloor
    hide screen xmas_smoke
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
