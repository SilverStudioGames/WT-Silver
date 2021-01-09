
label summon_susan:

    $ active_girl = "susan"
    $ last_character = "susan"

    $ susan_busy = True

    call update_susan

    call play_music("susan")
    call play_sound("door")

    call sus_chibi("stand","mid","base")
    with d3

    if one_of_ten < 4:
        if game.daytime:
            call sus_main("Good day, [sus_genie_name].","base","base","base","mid",xpos="base",ypos="base")
        else:
            call sus_main("Good evening, [sus_genie_name].","base","base","base","mid",xpos="base",ypos="base")
    elif one_of_ten < 7:
        call sus_main("How can I help you, [sus_genie_name]?","base","base","worried","R",xpos="base",ypos="base")
    else:
        call sus_main("You wanted to see me, [sus_genie_name]?","base","base","worried","down",xpos="base",ypos="base")

    label susan_requests:

    call sus_main(xpos="base", ypos="base")

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if not chitchated_with_susan:
                call susan_chit_chat
                jump susan_talk
            else:
                jump susan_talk

        "-Sexual favours-" (icon="interface/icons/small/condom.webp", style="disabled") if False:
            $ TBA_message()
            jump susan_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if susan_wardrobe_unlocked:
            hide screen sus_main with d1
            $ gui.in_context("wardrobe")
            with d2
            jump susan_requests

        "-Hidden-" (style="disabled") if not susan_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump susan_requests

        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_susan_gift:
            hide screen susan_main with d1
            call gift_menu
            jump susan_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp", style="disabled") if gave_susan_gift:
            $ TBA_message()
            #m "I already gave her a gift today. Don't want to spoil her too much..."
            jump susan_requests


        # Dismiss
        "-Dismiss her-":
            if game.daytime:
                call sus_main("I will go back to classes then, [sus_genie_name].","base","base","base","down")
            else:
                call sus_main("*Ehm*... good night then, [sus_genie_name].","base","base","base","down")

            call play_sound("door")

            $ susan_busy = True

            jump main_room



label susan_talk:
    menu:
        #"--":
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ sus_genie_name = "Sir"
                    call sus_main("Very well, [sus_genie_name].","base","base","base","mid")
                    jump susan_talk
                "-Dumbledore-":
                    $ sus_genie_name = "Dumbledore"
                    call sus_main("Okay, [sus_genie_name].","base","base","worried","down")
                    jump susan_talk
                "-Professor-":
                    $ sus_genie_name = "Professor"
                    call sus_main("Of course, [sus_genie_name].","base","base","base","R")
                    jump susan_talk
                "-Old man-":
                    $ sus_genie_name = "Old man"
                    call sus_main("That wouldn't be very polite, Professor.","open","closed","base","mid")
                    m "Don't worry, [susan_name]. I always tell my students to call me silly names."
                    g9 "It helps bonding with them!"
                    call sus_main("If you say so... *Ehm*, [sus_genie_name].","base","base","base","mid")
                    g4 "And soon I'm going to bond with your tits!"
                    jump susan_talk
                "-Genie-":
                    $ sus_genie_name = "Genie"
                    call sus_main("I... *Ehm*--","upset","base","base","L")
                    call sus_main("Do all the people call you that?","upset","narrow","worried","mid")
                    m "Yes-yes--, everybody!"
                    m "It's perfectly normal!"
                    call sus_main("(...)","upset","base","worried","down")
                    call sus_main("O-okay then... [sus_genie_name].","base","base","worried","R")
                    jump susan_talk
                "-Lord Voldemort-":
                    $ sus_genie_name = "Lord Voldemort"
                    call sus_main("Why would you want me to call you that?","open","closed","worried","mid")
                    call sus_main("We aren't supposed to mention his name!","open","narrow","worried","down")
                    m "It's only a name girl..."
                    call sus_main("It's the name of, you-know-who!","upset","closed","worried","mid")
                    call sus_main("That name really creeps me out, Professor!","open","closed","worried","mid")
                    m "I don't want my students to be scared of a name, Susan! It's practice."
                    m "Come on... say it."
                    call sus_main("Okay...","open","narrow","worried","down")
                    call sus_main("V-Voldemort...","upset","closed","worried","mid")
                    jump susan_talk
                "-Daddy-":
                    $ sus_genie_name = "Daddy"
                    call sus_main("Sir, no!","scream","closed","worried","mid")
                    call sus_main("I can't possibly call you that!","scream","wide","angry","wide")
                    m "But I want you to."
                    g9 "There's no harm in calling me Daddy."
                    call sus_main("But that's!--","open","narrow","angry","mid")
                    call sus_main("(This is wrong, Susan!)","upset","narrow","worried","down")
                    call sus_main("Alright... Professor-- *Eeeeh*... D-Daddy.","base","closed","worried","mid")
                    jump susan_talk
                "-Master-":
                    $ sus_genie_name = "Master"
                    call sus_main("M-Master?","upset","narrow","base","mid")
                    call sus_main("I don't think I should call my teachers that.","open","closed","worried","mid")
                    m "No-no--, that's what you call your teachers nowadays!"
                    m "But only call me that!"
                    call sus_main("*Ehm*... Very well, [sus_genie_name].","upset","narrow","worried","R")
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", sus_genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump susan_talk
                    else:
                        $ sus_genie_name = temp_name
                        call sus_main("*Ehm*... Okay. I will call you [sus_genie_name].","upset","narrow","base","L")
                    jump susan_talk
                "-Never mind-":
                    jump susan_requests


        "-From now on I will refer to you as-":
            menu:
                "-Miss Bones-":
                    $ susan_name = "Miss Bones"
                    call sus_main("Of course, [sus_genie_name].","base","base","base","mid")
                    jump susan_talk
                "-Girl-":
                    $ susan_name = "Girl"
                    call sus_main("I'm okay with that, [sus_genie_name].","base","base","worried","R")
                    jump susan_talk
                "-Cow-":
                    $ susan_name = "Cow"
                    call sus_main("Why would you want to call me that, [sus_genie_name]?","upset","narrow","worried","down")
                    call sus_main("The other girls already call me that and I hate it...","open","base","worried","down")
                    m "You poor poor thing!"
                    m "You see, if someone like me would call you that, maybe it wouldn't affect you as much."
                    call sus_main("I--... You might be right.","upset","narrow","base","down")
                    call sus_main("You can call me a Cow, [sus_genie_name].","base","base","base","mid")
                    jump susan_talk
                "-Slut-":
                    $ susan_name = "Slut"
                    call sus_main("[sus_genie_name]!","scream","closed","angry","R")
                    call sus_main("You can't be serious!","scream","wide","base","wide")
                    m "Why not. Nobody has to know..."
                    call sus_main("How could you even think of me like that!","open","base","worried","down")
                    call sus_main("I'm not a... slut.","upset","narrow","worried","R")
                    m "Of course not. This is just to strengthen your self-esteem."
                    m "Trust me, I know what I'm doing."
                    m "Being called a slut always boosts a girls confidence!"
                    call sus_main("R-really?","open","base","base","mid")
                    m "Yes. Now... shall we try it?"
                    call sus_main("... alright, [sus_genie_name]...","upset","narrow","worried","R")
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", susan_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump susan_talk
                    else:
                        $ susan_name = temp_name
                        call sus_main("I don't like it, but--","open","closed","worried","mid")
                        call sus_main("Promise you'll only call me that when we are alone.","upset","base","worried","mid")
                        g9 "Promised!"
                    jump susan_talk
                "-Never mind-":
                    jump susan_talk


        "-Never mind":
            jump susan_requests
