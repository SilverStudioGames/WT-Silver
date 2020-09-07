#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\"

### Change Hair Style ###
### Change Hair Color ###


label change_hair:
    #Luna
    if active_girl == "luna":
        jump change_lun_hair
    #Susan
    if active_girl == "susan":
        jump change_sus_hair


### Change Hermione's Hair Color ###

# label change_her_hair:

    # #if hair_color_choice == h_hair_color:
    # #    $ hide_transitions = True
    # #    #">She's already wearing that!" #Remove line. Just for testing.
    # #    jump return_to_wardrobe

    # if her_mood >= 1:
        # jump equipping_failed

    # else:
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hermione_xpos = 665
            # $ hide_transitions = False #activates dissolve in her_main


            # #Change Hair-Style
            # if hair_style_choice == "curly" and h_hair_style != "curly":
                # m "[hermione_name]..."
                # m "Could you wear your hair normal for me?"
                # call her_main("Of course, [genie_name].", "soft", "base", "base", "mid")
                # call her_main("Let me just change it.", "base", "base", "base", "mid")

                # hide screen hermione_main
                # with d3

                # pause.5

                # call set_her_hair(style=hair_style_choice)
                # call compliment_her_hair_style

                # if hair_color_choice != h_hair_color:
                    # m "There is something else I would like you to do, [hermione_name]..."
                    # call her_main("Of course, [genie_name].", "base", "base", "base", "mid")

            # if hair_style_choice == "updo" and h_hair_style != "updo":
                # m "[hermione_name]..."
                # m "Could you tie your hair up for me?"
                # call her_main("Of course, [genie_name].", "soft", "base", "base", "mid")
                # call her_main("Let me just change it.", "base", "base", "base", "mid")

                # hide screen hermione_main
                # with d3

                # pause.5

                # call set_her_hair(style=hair_style_choice)
                # call compliment_her_hair_style

                # if hair_color_choice != h_hair_color:
                    # m "There is something else I would like you to do, [hermione_name]..."
                    # call her_main("Of course, [genie_name].", "base", "base", "base", "mid")

            # if hair_style_choice == "bobcut" and h_hair_style != "bobcut":
                # m "[hermione_name]..."
                # m "Could you wear your hair short for me?"
                # call her_main("Of course, [genie_name].", "soft", "base", "base", "mid")
                # call her_main("Let me just change it.", "base", "base", "base", "mid")

                # hide screen hermione_main
                # with d3

                # pause.5

                # call set_her_hair(style=hair_style_choice)

                # if hair_color_choice != h_hair_color:
                    # m "There is something else I would like you to do, [hermione_name]..."
                    # call her_main("Of course, [genie_name].", "base", "base", "base", "mid")

            # #Change Hair-Color
            # if hair_color_choice == h_hair_color:
                # jump return_to_wardrobe
            # else:
                # if hair_style_choice != h_hair_style:
                    # m "[hermione_name]..."

            # #Brown #Done
            # if hair_color_choice == "brown":
                # m "I want you to change your hair back to brown."
                # if her_whoring < 5:
                    # call her_main("Gladly, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("(I hate having people stare at me...)", "annoyed", "narrow", "annoyed", "up")
                    # call her_main("I will go and change it.", "base", "base", "base", "R")
                # elif her_whoring < 11:
                    # call her_main("Of course, [genie_name].", "open", "base", "base", "mid")
                    # call her_main("Let me go change it.", "base", "base", "base", "mid")
                # elif her_whoring < 20:
                    # call her_main("Sure, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("Let me just change it.", "base", "narrow", "base", "mid_soft")
                # else: #20+
                    # call her_main("Brown, [genie_name]?", "upset", "wink", "base", "mid")
                    # call her_main("(But I liked having my hair stand out...)", "annoyed", "narrow", "worried", "down")
                    # call her_main("Fine, [genie_name]... {w=0.9}let me go change it.", "base", "base", "base", "R")

            # #Blonde #Done
            # elif hair_color_choice == "blonde":
                # m "Would you dye your hair blonde for me?"
                # if her_whoring >= 5:
                    # if her_whoring < 11:
                        # call her_main("Blonde?...", "upset", "wink", "base", "mid")
                        # call her_main("(It looks decent enough... {w=0.9}maybe I should try something new once in a while...)", "annoyed", "narrow", "worried", "down")
                        # call her_main("Ok, [genie_name]... {w=0.9}Let me go change it.", "base", "base", "base", "mid")
                    # elif her_whoring < 20:
                        # call her_main("Blonde?", "base", "base", "base", "mid")
                        # call her_main("Alright, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change it real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("That barely even looks like blonde!", "annoyed", "narrow", "worried", "down")
                        # call her_main("Don't you have anything brighter?", "angry", "wink", "base", "mid")
                        # m "You going to wear it or not?"
                        # call her_main("Fine... Let me go change it.", "annoyed", "narrow", "annoyed", "mid")
                # else:
                    # call her_main("No thank you, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("I like my hair how it is.", "open", "base", "worried", "R")
                    # call her_main("I have to refuse!", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # #Red #Done
            # elif hair_color_choice == "red":
                # m "Would you dye your hair red for me?"
                # if her_whoring >= 5:
                    # if her_whoring < 11:
                        # call her_main("Red, [genie_name]?", "open", "base", "base", "mid")
                        # call her_main("It looks a lot like Ginny's hair-colour...", "base", "narrow", "worried", "down")
                        # m "Genie?"
                        # call her_main("Ginny Weasley, [genie_name].", "open", "closed", "base", "mid")
                        # m "..."
                        # call her_main("(...?)", "angry", "wink", "base", "mid")
                        # m "Of course! That Weasely... uhh--sister...?"
                        # call her_main("Yes, [genie_name].", "open", "squint", "base", "mid")
                        # m "(I wonder if she is hot...)"
                        # m "(The girl says she is a redhead...)"
                        # g9 "(She has to be!)"
                        # call her_main("I will go and change my hair, [genie_name].", "open", "base", "base", "R")
                    # elif her_whoring < 20:
                        # call her_main("Oh wow, it looks pretty. I really like it!", "soft", "base", "base", "mid")
                        # call her_main("It will make me look just like Ginny!", "smile", "happyCl", "base", "mid")
                        # call her_main("(although she's a bit shorter than me... and her hair isn't as curly.)", "annoyed", "base", "base", "mid")
                        # call her_main("(I wonder if the teachers will notice should we switch places in class...)", "grin", "narrow", "annoyed", "up")
                        # call her_main("(Only one way to find out!)", "smile", "narrow", "base", "mid_soft")
                        # call her_main("Let me go change it!", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("You want me to be a redhead, hmm...?", "base", "narrow", "base", "mid_soft")
                        # call her_main("You know what they say about redheads, [genie_name].", "smile", "narrow", "base", "mid_soft")
                        # call her_main("Let me go change it for you.", "soft", "base", "base", "mid")
                # else:
                    # call her_main("No thank you, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("I like my hair how it is.", "open", "base", "worried", "R")
                    # call her_main("I have to refuse!", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # #Crimson #Done
            # elif hair_color_choice == "crimson":
                # m "Would you dye your hair crimson for me?"
                # if her_whoring >= 8:
                    # call her_main("It is a really nice colour, [genie_name].", "soft", "base", "base", "mid")
                    # call her_main("Let me go change it real quick.", "base", "base", "base", "mid")
                # else:
                    # call her_main("That's a bit much don't you think?", "angry", "happyCl", "worried", "mid")
                    # call her_main("(I'm not dying my hair red to look like some harlot.)", "annoyed", "base", "base", "R")
                    # call her_main("I have to refuse, [genie_name]!", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe

            # #Black #Done
            # elif hair_color_choice == "black":
                # m "Would you dye your hair black for me?"
                # if her_whoring >= 8:
                    # if her_whoring < 17:
                        # call her_main("Black, [genie_name]?", "annoyed", "narrow", "worried", "down")
                        # call her_main("(It does look nice.)", "annoyed", "base", "base", "R")
                        # call her_main("I will try it! Let me go and change it.", "soft", "base", "base", "R")
                    # else: #17+
                        # call her_main("Sure, [genie_name]!", "base", "narrow", "base", "mid_soft")
                        # call her_main("I really like that colour!", "smile", "happyCl", "base", "mid")
                        # call her_main("Let me just change it.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("Black, [genie_name]?", "open", "squint", "base", "mid")
                    # call her_main("Black isn't really my colour.", "soft", "base", "base", "R")
                    # call her_main("I don't think it will suit me, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("I have to refuse.", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe

            # #Green #Done
            # elif hair_color_choice == "green":
                # m "Would you dye your hair for me again?"
                # call her_main("Of course, [genie_name]. In which colour?", "open", "base", "base", "mid")
                # g9 "Slytherin Green!"
                # if her_whoring >= 11:
                    # if her_whoring < 17:
                        # call her_main("Sure, why not.", "soft", "base", "base", "R") #soft, baseL
                        # call her_main("Green is just a colour, [genie_name]!", "open", "base", "base", "mid")
                        # call her_main("Wear it on my head doesn't mean I support Slytherin!", "open", "closed", "base", "mid")
                        # call her_main("(It will look awfully suspicious for a Gryffindor though...)", "annoyed", "base", "worried", "R")
                        # call her_main("Just let me go change it.", "base", "base", "base", "mid")
                    # else: #17+
                        # call her_main("Yes, [genie_name].", "base", "base", "base", "mid")
                        # call her_main("To tell you a secret...", "soft", "base", "base", "R")
                        # call her_main("Green is my favourite colour.", "base", "narrow", "base", "mid_soft")
                        # m "Really? what about red?"
                        # call her_main("Hmm... no, [genie_name].", "annoyed", "base", "base", "R")
                        # call her_main("Red is such an aggressive colour.", "open", "narrow", "worried", "down")
                        # call her_main("Green one the other hand is soft and sweet...", "soft", "base", "base", "R")
                        # call her_main("It always reminds me of nature, grassy fields in the summer, the smell of flowers everywhere...", "open", "base", "base", "R")
                        # call her_main("I really love it!", "smile", "happyCl", "base", "mid")
                        # call her_main("Let me go change it for you.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("What?!", "angry", "base", "angry", "mid")
                    # call her_main("I'm not going to walk around school parading as some Slytherin joke-mascot!", "scream", "closed", "angry", "mid")
                    # call her_main("I definitely refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # #Blue #Done
            # elif hair_color_choice == "blue":
                # m "Would you dye your hair blue for me?"
                # if her_whoring >= 11:
                    # call her_main("Sure, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("Let me go change.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("I'm not going to dye my hair blue for you, [genie_name]!", "open", "closed", "angry", "mid")
                        # call her_main("If you want your own parrot, then you should just buy one!", "angry", "base", "angry", "mid")
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 11."
                        # jump return_to_wardrobe
                    # else: #5-10
                        # call her_main("Really, [genie_name]?", "annoyed", "squint", "base", "mid")
                        # call her_main("You want me to look like a lesbian that bad?", "open", "narrow", "annoyed", "mid", cheeks="blush")
                        # call her_main("I'm going to refuse!", "annoyed", "base", "base", "R")
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 11."
                        # jump return_to_wardrobe

            # #Purple #Done
            # elif hair_color_choice == "purple":
                # m "Would you dye your hair purple for me?"
                # if her_whoring >= 11:
                    # call her_main("Sure, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("Let me go change.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("Purple?", "angry", "wink", "base", "mid")
                    # call her_main("I do like the colour, but...", "soft", "base", "base", "R")
                    # call her_main("I don't think I want to wear it on my head...", "annoyed", "narrow", "annoyed", "up")
                    # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # #Pink #Done
            # elif hair_color_choice == "pink":
                # m "Would you dye your hair pink for me?"
                # if her_whoring >= 14:
                    # call her_main("Of course, [genie_name]!", "smile", "narrow", "base", "mid_soft")
                    # call her_main("I love pink!!!", "soft", "base", "base", "R")
                    # call her_main("Hi-hi--", "smile", "happyCl", "base", "mid")
                    # call her_main("Let me go change.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("Dye my hair...", "angry", "base", "angry", "mid") #mad, angry
                    # call her_main("Dye my hair Pink?... {w=0.9}Pink?!", "angry", "base", "angry", "mid",emote="angry")
                    # call her_main("I can't dye my hair pink, [genie_name]!", "scream", "happyCl", "worried", "mid")
                    # call her_main("(What does he think I am? Some cheap dress-up doll?)", "annoyed", "narrow", "angry", "R")
                    # call her_main("It's an ugly colour anyway.", "open", "closed", "base", "mid")
                    # call her_main("I definitely refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 14."
                    # jump return_to_wardrobe

            # #White #Done
            # elif hair_color_choice == "gray":
                # m "Dye your hair white for me."
                # if her_whoring >= 17:
                    # call her_main("Alright, [genie_name].", "smile", "base", "base", "R")
                    # call her_main("Let me go change.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("No, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("I'm not going to run around school looking like some grandma!", "annoyed", "narrow", "annoyed", "mid")
                    # call her_main("I refuse!", "annoyed", "base", "base", "R")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # hide screen hermione_main
            # with d3

            # pause.5

            # call set_her_hair(color=hair_color_choice)


            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else:

            # $ hide_transitions = True
            # call set_her_hair(style=hair_style_choice)
            # call her_main(xpos="wardrobe")

            # if hair_color_choice == h_hair_color:
                # call screen wardrobe_old

            # if hair_color_choice == "blonde" and her_whoring <= 5:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 2."
                # jump return_to_wardrobe
            # if hair_color_choice == "red" and her_whoring <= 5:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 2."
                # jump return_to_wardrobe
            # if hair_color_choice == "crimson" and her_whoring <= 8:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 8."
                # jump return_to_wardrobe
            # if hair_color_choice == "black" and her_whoring <= 8:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 8."
                # jump return_to_wardrobe

            # if hair_color_choice == "green" and her_whoring <= 11:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 11."
                # jump return_to_wardrobe
            # if hair_color_choice == "blue" and her_whoring <= 11:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 11."
                # jump return_to_wardrobe
            # if hair_color_choice == "purple" and her_whoring <= 11:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 11."
                # jump return_to_wardrobe
            # if hair_color_choice == "pink" and her_whoring <= 14:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 14."
                # jump return_to_wardrobe
            # if hair_color_choice == "gray" and her_whoring <= 17:
                # ">She won't wear that colour just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 17."
                # jump return_to_wardrobe

            # $ hide_transitions = True
            # call set_her_hair(color=hair_color_choice)
            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old
# #


# label compliment_her_hair_style:
    # if her_whoring < 5:
        # call her_main("Like this, [genie_name]?", "soft", "base", "base", "mid")
        # m "This look really suits you, [hermione_name]."
        # call her_main("Thank you, [genie_name].", "base", "base", "base", "R",cheeks="blush")
    # elif her_whoring < 11:
        # call her_main("...", "base", "happyCl", "base", "mid")
        # call her_main("Do you like it, [genie_name]?", "grin", "wink", "base", "mid",cheeks="blush")
        # m "Indeed I do, [hermione_name]."
        # call her_main("Thank you.", "base", "base", "base", "mid")
    # elif her_whoring < 20:
        # call her_main("How do I look?", "open", "closed", "base", "mid")
        # m "You look very lovely, [hermione_name]!"
        # call her_main("Glad to hear that, [genie_name].", "base", "narrow", "base", "mid_soft")
    # else: #20+
        # if h_hair_style == "curly":
            # call her_main("Do you like my long hair, [genie_name]?", "base", "narrow", "base", "mid_soft")
            # m "I do, [hermione_name]"
            # call her_main("I prefer wearing my hair open like this.", "open", "closed", "base", "mid")
            # call her_main("Makes it easier to grab and pull...", "base", "narrow", "base", "mid_soft")
            # call her_main("Like a leash!", "smile", "base", "angry", "mid")
            # g4 "You dirty slut!"
        # else:
            # call her_main("Do you like it, [genie_name]?", "base", "narrow", "base", "mid_soft")
            # call her_main("Does this hair make me look...", "base", "base", "base", "mid")
            # call her_main("Slutty?", "base", "narrow", "base", "mid_soft")
            # g4 "Ugh!--You can bet your perfect ass on it!"
            # g9 "Why don't you come over here and I give your hair some lotion!"
            # call her_main("[genie_name] you should know that I already used some rather expensive lotion this morning and--", "open", "closed", "base", "mid")
            # m "I just want to shower them in my cum, girl..."
            # call her_main("Oh--", "soft", "base", "base", "mid")
            # call her_main("...", "soft", "base", "base", "R",cheeks="blush")
            # call her_main("(What a great idea.)", "base", "happyCl", "base", "mid")
            # call her_main("Maybe next time, [genie_name].", "smile", "base", "base", "R")

    # return


label change_lun_hair:
    call set_lun_hair(hair_style_choice, hair_color_choice)

    jump return_to_wardrobe

label change_sus_hair:
    call set_sus_hair(hair_style_choice, hair_color_choice)

    jump return_to_wardrobe
