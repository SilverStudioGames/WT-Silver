

### Tier 2 (pre Slytherin) ###

label cho_panties_response_T2:
    $ has_cho_panties = False
    call play_sound("door")
    call cho_chibi("stand","mid","base")
    with d3

    call play_music("cho")
    call cho_main("Hello, [cho_genie_name].", "soft", "narrow", "worried", "mid", xpos="right", ypos="base")
    m "Sup..."
    call cho_main("*Uhm*...", "annoyed", "narrow", "worried", "R")
    call cho_main("I forgot to take my underwear with me the last time I was here.", "soft", "narrow", "worried", "downR", cheeks="blush")

    if cho_panties_soaked:
        g9 "Your panties! Of course, [cho_name]!{w} I've got them right here..."
        call cho_walk("desk", "base")
        pause .8

        call cho_main("(...)", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade) # Evil stare.
        m "What?"
        call cho_main("(...)", "annoyed", "narrow", "angry", "R")
        m "Anything wrong?"
        call cho_main("They are covered in semen.", "soft", "narrow", "base", "R")
        m "What was that?"
        call cho_main("Semen, Sir!", "scream", "narrow", "angry", "mid", trans=hpunch) # Scream
        call cho_main("", "annoyed", "narrow", "angry", "mid")
        g4 "You are correct!{w} They are indeed covered in a thick load of filthy, nasty reeking semen!"
        g9 "Who could have done this?!"
        call cho_main("I don't know... why don't we inquire how they got here in the first place...", "open", "base", "base", "R")
        call cho_main("Didn't I take off my panties while I was stripping for you?", "soft", "narrow", "base", "mid")
        m "That is correct."
        call cho_main("And you had my panties this whole time?", "soft", "narrow", "raised", "mid")
        m "Yup."
        call cho_main("And you just gave them back to me covered in spunk...", "annoyed", "narrow", "base", "mid")
        m "That makes sense to me..."
        call cho_main("So you admit that you did it?", "soft", "narrow", "angry", "mid")
        m "It's not my cum..."
        call cho_main("*Argh*!", "angry", "narrow", "angry", "mid", trans=hpunch)
        call cho_main("Well whose is it then?{w} The house-elves?", "soft", "narrow", "base", "mid")
        m "*Uhm*...{w} Yes?"
        call cho_main("It's disgusting!", "annoyed", "narrow", "base", "down")
        call cho_main("I better get them cleaned immediately...", "angry", "narrow", "worried", "down")

        call cho_walk("door", "base")

        call bld
        m "Where are you going?"

        call cho_chibi("leave")

        call bld
        m "(...)"

        $ cho_mood += 6
        $ cho_busy = True

        $ cho_panties_soaked = False

        $ achievement.unlock("pantiesfapcho")

        jump main_room

    else:
        g9 "Your panties, that's right!{w} I've got them right here..."

        $ renpy.sound.play("sounds/sniff.mp3")
        call nar(">You bring the panties to your nose and give them one last sniff.")

        g4 "*Aaahhh*!{w} Wonderful!"
        call cho_main("(...)", "annoyed", "narrow", "base", "mid")
        m "There, take them..."

        call cho_walk("desk", "base")
        pause .8

        call cho_walk("mid", "base")
        call cho_chibi("stand", "mid", "base", flip=False)
        with d3
        pause .2

        call cho_main("Thank you, Sir.", "base", "base", "base", "mid")
        m "You're welcome..."

        jump cho_requests
