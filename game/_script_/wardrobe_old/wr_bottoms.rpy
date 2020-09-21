#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_bottom:
    #Susan
    if active_girl == "susan":
        jump equip_sus_bottom

### Equip Bottom ###

# DO NOT REMOVE! We will re-use the dialogues.

# label equip_her_bottom:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\"

    # if skirt_choice == h_bottom:
        # $ hide_transitions = True
        # #">She's already wearing that!" #Remove line. Just for testing.
        # jump return_to_wardrobe

    # if hermione_action in ["hands_behind","covering","fingering","covering_top","pinch","hands_cuffed","milk_breasts"]:

        # $ hide_transitions = True
        # hide screen hermione_main
        # with d3
        # ">Hermione is currently posing... naked.\nWould you like her to get dressed?"
        # menu:
            # "-Make her get dressed-":
                # call set_her_action("none","update")
                # hide screen hermione_main

            # "-nvm-":
                # show screen hermione_main
                # with d3
                # jump return_to_wardrobe

    # if her_mood >= 1:
        # jump equipping_failed

    # else:
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hermione_xpos = 665
            # $ hide_transitions = False #activates dissolve in her_main

            # m "[hermione_name]..."

            # ### Uniform Skirts ###

            # #Uniform Skirt Very Long #Done
            # if skirt_choice == "skirt_1":
                # m "Would you wear your school skirt for me? The very long one."
                # if her_whoring < 8:
                    # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                # elif her_whoring < 11:
                    # call her_main("Alright... sure, why not.", "base", "narrow", "worried", "down")
                    # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                # elif her_whoring < 20:
                    # call her_main("Are you sure, [genie_name]?", "disgust", "narrow", "base", "down")
                    # call her_main("That thing looks rather plain...", "open", "closed", "base", "mid")
                    # call her_main("I would much rather wear one a bit shorter!", "angry", "wink", "base", "mid")
                    # m "No, [hermione_name]. Wear the long one..."
                    # call her_main("Ugh... Fine.", "disgust", "narrow", "base", "down")
                    # call her_main("Let me just change it.", "annoyed", "narrow", "annoyed", "mid")
                # else: #20+
                    # call her_main("Are you serious?", "angry", "wink", "base", "mid")
                    # call her_main("That thing is soooooo ugly!", "annoyed", "narrow", "annoyed", "up")
                    # call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!", "disgust", "slit", "low", "stare")
                    # m "No, [hermione_name]. Wear the long one..."
                    # call her_main("Fine... Just let me change it...", "disgust", "narrow", "base", "mid_soft")

            # #Uniform Skirt Long #Done
            # elif skirt_choice == "skirt_2":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you."
                # if her_whoring >= 5:
                    # if her_whoring < 8:
                        # call her_main("...", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("Fine.", "open", "closed", "base", "mid")
                        # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                    # elif her_whoring < 11:
                        # call her_main("Sure, why not.", "base", "narrow", "worried", "down")
                        # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                    # elif her_whoring < 20:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("... that old thing?", "annoyed", "narrow", "angry", "R")
                        # m "Sure, is that a problem?"
                        # call her_main("...", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("I suppose not...", "annoyed", "narrow", "worried", "down")
                        # call her_main("It's just so plain!", "annoyed", "narrow", "angry", "R")
                # else:
                    # call her_main("I'm sorry, [genie_name].", "base", "base", "base", "mid")
                    # call her_main("But that would be against the Hogwarts rules for proper school attire!", "open", "closed", "base", "mid")
                    # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # #Uniform Skirt Medium Length #Done
            # elif skirt_choice == "skirt_3":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you."
                # if her_whoring >= 8:
                    # if her_whoring < 11:
                        # call her_main("Alright... sure, why not.", "base", "narrow", "worried", "down")
                        # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                    # elif her_whoring < 20:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me go and change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("(...)", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("(At least it is short enough...)", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("OK, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("I'm sorry, [genie_name].", "base", "base", "base", "mid")
                        # call her_main("But that would be against the Hogwarts rules for proper school attire!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # else:
                        # call her_main("That's way too short, [genie_name]!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse!", "annoyed", "squint", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe

            # #Uniform Skirt Short #Done
            # elif skirt_choice == "skirt_4":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you."
                # if her_whoring >= 14:
                    # if her_whoring < 20:
                        # call her_main("Sure, why not.", "soft", "base", "base", "R")
                        # call her_main("Let me change it real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("(...)", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("(At least it is short enough...)", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("OK, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("I'm sorry, [genie_name].", "base", "base", "base", "mid")
                        # call her_main("But that would be against the Hogwarts rules for proper school attire!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # else:
                        # call her_main("That's way too short, [genie_name]!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse!", "annoyed", "squint", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 14."
                    # jump return_to_wardrobe

            # #Uniform Skirt Shortest #Done
            # elif skirt_choice == "skirt_5":
                # m "Would you wear your school skirt for me? The shortest one you have."
                # if her_whoring >= 17:
                    # if her_whoring < 23:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #23+
                        # call her_main("(That old thing?)", "annoyed", "narrow", "worried", "down")
                        # call her_main("Can't I wear something a little shorter?", "open", "base", "base", "R",cheeks="blush")
                        # m "I don't think they make anything shorter."
                        # call her_main("I guess This will just have to do then...", "open", "narrow", "base", "up",cheeks="blush")
                        # call her_main("Let me go change...", "base", "narrow", "base", "up",cheeks="blush")
                # else:
                    # if her_whoring < 5:
                        # call her_main("I'm sorry, [genie_name].", "base", "base", "base", "mid")
                        # call her_main("But that would be against the Hogwarts rules for proper school attire!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # else:
                        # call her_main("How... How short?!", "shock", "wide", "base", "stare")
                        # call her_main("Is that another one of your silly jokes, [genie_name]?", "angry", "base", "worried", "mid")
                        # call her_main("No, please, don't tell me.", "open", "closed", "base", "mid")
                        # call her_main("I don't even want to know...", "annoyed", "base", "worried", "R")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # elif skirt_choice == "skirt_7":
                # m "Would you wear your school skirt for me? But open up the front a bit."
                # if her_whoring >= 17:
                    # if her_whoring < 20:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("... that old thing?", "annoyed", "narrow", "angry", "R")
                        # m "Sure, is that a problem?"
                        # call her_main("...", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("I suppose not...", "annoyed", "narrow", "worried", "down")
                        # call her_main("It's just so plain!", "annoyed", "narrow", "angry", "R")
                # else:
                    # if her_whoring < 5:
                        # call her_main("I'm sorry, [genie_name].", "base", "base", "base", "mid")
                        # call her_main("But that would be against the Hogwarts rules for proper school attire!", "open", "closed", "base", "mid")
                        # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # else:
                        # call her_main("Open up the front?!", "shock", "wide", "base", "stare")
                        # call her_main("Is that another one of your silly jokes, [genie_name]?", "angry", "base", "worried", "mid")
                        # call her_main("No, please, don't tell me.", "open", "closed", "base", "mid")
                        # call her_main("I don't even want to know...", "annoyed", "base", "worried", "R")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe


            # ### Uniform Skirts Low ###

            # #Uniform Skirt Low Very Long #Done
            # elif skirt_choice == "skirt_1_low":
                # m "Would you wear your school skirt for me? The very long one. But pull it down a bit."
                # if her_whoring >= 8:
                    # if her_whoring < 11:
                        # call her_main("Alright... sure, why not.", "base", "narrow", "worried", "down")
                        # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                    # elif her_whoring < 20:
                        # call her_main("Are you sure, [genie_name]?", "disgust", "narrow", "base", "down")
                        # call her_main("That thing looks rather plain...", "open", "closed", "base", "mid")
                        # call her_main("I would much rather wear one a bit shorter!", "angry", "wink", "base", "mid")
                        # m "No, [hermione_name]. Wear the long one..."
                        # call her_main("Ugh... Fine.", "disgust", "narrow", "base", "down")
                        # call her_main("Let me just change it.", "annoyed", "narrow", "annoyed", "mid")
                    # else: #20+
                        # call her_main("Are you serious?", "angry", "wink", "base", "mid")
                        # call her_main("That thing is soooooo ugly!", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!", "disgust", "slit", "low", "stare")
                        # m "No, [hermione_name]. Wear the long one..."
                        # call her_main("Fine... Just let me change it...", "disgust", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("Pull my skirt down?!", "shock", "wide", "base", "stare")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "angry", "base", "angry", "mid")
                        # call her_main("How can you even suggest such a thing!", "angry", "happyCl", "worried", "mid")
                        # call her_main("(disgusting old fool...)", "annoyed", "narrow", "annoyed", "mid")
                    # else:
                        # call her_main("No, [genie_name].", "open", "closed", "base", "mid")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("My panties would be visible...", "disgust", "narrow", "base", "down")
                        # m "That's kind of the point, [hermione_name]."
                        # call her_main("I refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe

            # #Uniform Skirt Low Medium Length #Done
            # elif skirt_choice == "skirt_2_low":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                # if her_whoring >= 11:
                    # if her_whoring < 14:
                        # call her_main("Alright... sure, why not.", "base", "narrow", "worried", "down")
                        # call her_main("Let me go and change real quick.", "base", "base", "base", "mid")
                    # elif her_whoring < 20:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me go and change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("(...)", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("(At least it is short enough...)", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("OK, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("Pull my skirt down?!", "shock", "wide", "base", "stare")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "angry", "base", "angry", "mid")
                        # call her_main("How can you even suggest such a thing!", "angry", "happyCl", "worried", "mid")
                        # call her_main("(disgusting old fool...)", "annoyed", "narrow", "annoyed", "mid")
                    # else:
                        # call her_main("No, [genie_name].", "open", "closed", "base", "mid")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("My panties would be visible...", "disgust", "narrow", "base", "down")
                        # m "That's kind of the point, [hermione_name]."
                        # call her_main("Besides, the length you suggested is way too short!", "open", "closed", "base", "mid")
                        # call her_main("I refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # #Uniform Skirt Low Short #Done
            # elif skirt_choice == "skirt_3_low":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                # if her_whoring >= 17:
                    # if her_whoring < 20:
                        # call her_main("Of course, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me go and change real quick.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("(...)", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("(At least it is short enough...)", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("OK, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me just change real quick.", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("Pull my skirt down?!", "shock", "wide", "base", "stare")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "angry", "base", "angry", "mid")
                        # call her_main("How can you even suggest such a thing!", "angry", "happyCl", "worried", "mid")
                        # call her_main("(disgusting old fool...)", "annoyed", "narrow", "annoyed", "mid")
                    # else:
                        # call her_main("No, [genie_name].", "open", "closed", "base", "mid")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("My panties would be visible...", "disgust", "narrow", "base", "down")
                        # m "That's kind of the point, [hermione_name]."
                        # call her_main("Besides, the length you suggested is way too short!", "open", "closed", "base", "mid")
                        # call her_main("I refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # #Uniform Skirt Low Shortest (Micro Skirt) #Not implemented.
            # elif skirt_choice == "skirt_4_low":
                # m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                # if her_whoring >= 20:
                    # call her_main("Alright...", "base", "narrow", "worried", "down")
                    # call her_main("I wouldn't even mind if it were a bit shorter, you know...", "soft", "narrow", "base", "mid_soft")
                    # m "I don't think you can  make it any shorter than that, [hermione_name]."
                    # call her_main("Shame...", "annoyed", "narrow", "worried", "down")
                # else:
                    # if her_whoring < 5:
                        # call her_main("Pull my skirt down?!", "shock", "wide", "base", "stare")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "angry", "base", "angry", "mid")
                        # call her_main("How can you even suggest such a thing!", "angry", "happyCl", "worried", "mid")
                        # call her_main("(disgusting old fool...)", "annoyed", "narrow", "annoyed", "mid")
                    # else:
                        # call her_main("No, [genie_name].", "open", "closed", "base", "mid")
                        # call her_main("I'm not pulling my skirt down for you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
                        # call her_main("My panties would be visible...", "disgust", "narrow", "base", "down")
                        # m "That's kind of the point, [hermione_name]."
                        # call her_main("Besides, the length you suggested is way too short!", "open", "closed", "base", "mid")
                        # call her_main("I refuse!", "annoyed", "narrow", "annoyed", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 20."
                    # jump return_to_wardrobe


            # ### Cheerleader Skirts ###

            # #Uniform Skirt Cheerleader Slytherin #Done
            # elif skirt_choice in ["skirt_cheer_g","skirt_cheer_s","skirt_cheer_r","skirt_cheer_h"] or skirt_choice in ["skirt_cheer_sexy_g","skirt_cheer_sexy_s","skirt_cheer_sexy_r","skirt_cheer_sexy_h"]:
                # if skirt_choice in ["skirt_cheer_s","skirt_cheer_r","skirt_cheer_h"] or skirt_choice in ["skirt_cheer_sexy_s","skirt_cheer_sexy_r","skirt_cheer_sexy_h"]: # No gryffindor!
                    # m "Would you wear this cheerleader skirt for me?"
                    # if her_whoring >= 11:
                        # if her_whoring < 14:
                            # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                                # call her_main("But [genie_name], that's for Slytherins!", "angry", "wink", "base", "mid")
                            # if skirt_choice in ["skirt_cheer_r","skirt_cheer_sexy_r"]:
                                # call her_main("But [genie_name], that's for Ravenclaws!", "angry", "wink", "base", "mid")
                            # if skirt_choice in ["skirt_cheer_h","skirt_cheer_sexy_h"]:
                                # call her_main("But [genie_name], that's for Hufflepuffs!", "angry", "wink", "base", "mid")
                            # m "And?"
                            # call her_main("I'm a Gryffindor!", "annoyed", "narrow", "annoyed", "mid")
                            # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                                # call her_main("(A muggle-born on top of that.)", "disgust", "narrow", "base", "down")
                            # call her_main("I can't wear this!", "open", "happyCl", "worried", "mid")
                            # m "Why not?"
                            # call her_main("I've already told you, I'm a Gryffindor!", "annoyed", "narrow", "annoyed", "up")
                            # m "(...)"
                            # g9 "(I've got an idea!)"
                            # g4 "[hermione_name], I completely forgot to mention!"
                            # m "As the top student of Gryffingdoor, you were selected to switch places with a fellow student form another house!"
                            # m "As a form of bonding method... To bring the four houses closer together!"
                            # call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!", "disgust", "narrow", "base", "mid_soft")
                            # g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students!"
                            # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                                # m "Especially Gryffindor and Slytherin!"
                                # m "I mean, do you like being called a mudblood every day by them?"
                                # call her_main("No, [genie_name].", "angry", "wink", "base", "mid")
                                # m "Or when they call you a slut..."
                                # g4 "Or a whore!"
                                # g9 "Or bitch!"
                                # g4 "Or... a whore!"
                                # g4 "Or--"
                                # call her_main("I get your point, [genie_name]!!!", "scream", "happyCl", "worried", "mid",cheeks="blush")
                            # m "I'm giving you an opportunity to better your relationship with them!"
                            # m "Now are you going to wear this for me or not?..."
                            # call her_main("(...)", "annoyed", "narrow", "angry", "R")
                            # call her_main("Fine, [genie_name]... Let me just put it on.", "annoyed", "narrow", "annoyed", "mid")
                        # elif her_whoring < 20:
                            # call her_main("Fine, [genie_name].", "soft", "narrow", "annoyed", "up")
                            # call her_main("(How humiliating to wear this as a Gryffindor...)", "disgust", "slit", "low", "stare")
                            # call her_main("Let me just change it.", "soft", "base", "base", "R")
                        # else: #20+
                            # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                                # call her_main("Of course I will wear it!", "smile", "base", "angry", "mid")
                                # call her_main("Gimme-Gimme--Gimme!!!", "smile", "happyCl", "base", "mid")
                                # call her_main("(I'm definitely going to root for them on the next game!)", "soft", "base", "base", "R",cheeks="blush")
                                # call her_main("(If they are winning I won't have to wear this thing long anyway!)", "base", "narrow", "base", "mid_soft")
                                # call her_main("Whoooo, go Slytherin!", "smile", "happyCl", "base", "mid")
                            # else:
                                # call her_main("If I really have to...", "annoyed", "narrow", "annoyed", "mid")
                                # call her_main("Let me just change it.", "soft", "base", "base", "R")
                    # else:
                        # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                            # call her_main("In green?", "shock", "wide", "base", "stare")
                        # if skirt_choice in ["skirt_cheer_r","skirt_cheer_sexy_r"]:
                            # call her_main("In blue?", "shock", "wide", "base", "stare")
                        # if skirt_choice in ["skirt_cheer_h","skirt_cheer_sexy_h"]:
                            # call her_main("In yellow?", "shock", "wide", "base", "stare")
                        # call her_main("Are you serious, [genie_name]?", "angry", "base", "angry", "mid")
                        # call her_main("Are you sure you didn't just pick the wrong colour for me?", "annoyed", "squint", "base", "mid")
                        # if skirt_choice in ["skirt_cheer_s","skirt_cheer_sexy_s"]:
                            # m "(Something tells me she doesn't want to wear green stuff.)"
                            # m "(Is she allergic to grasshoppers or something?)"
                        # else:
                            # m "(Could have sworn I picked the right colour for her...)"
                        # m "Forget about it, girl."
                        # call her_main("I will!", "annoyed", "narrow", "annoyed", "mid")
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 11."
                        # jump return_to_wardrobe

                # else: #Gryffindor #Base color and red color.
                    # m "Could you wear your cheerleader skirt for me?"
                    # if her_whoring >= 5:
                        # if her_whoring < 11:
                            # call her_main("Of course, [genie_name]!", "soft", "base", "base", "R",cheeks="blush")
                            # call her_main("Let me go change.", "base", "base", "base", "mid")
                        # else:
                            # call her_main("Alright, [genie_name]!", "soft", "base", "base", "mid")
                            # call her_main("Let me just change it.", "base", "narrow", "base", "mid_soft")
                    # else:
                        # call her_main("I don't know, [genie_name].", "annoyed", "narrow", "worried", "down")
                        # call her_main("I'm not the cheerleader type!", "angry", "wink", "base", "mid")
                        # call her_main("While I like the idea of supporting my house in Quidditch...", "open", "closed", "base", "mid")
                        # call her_main("My priority is to secure this years house cup instead!", "open", "base", "base", "R")
                        # call her_main("I have to refuse, [genie_name].", "soft", "base", "base", "mid")
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 5."
                        # jump return_to_wardrobe


            # ### trousers ###

            # #Pants Jeans Long #Done
            # elif skirt_choice == "pants_jeans_long":
                # m "Could you wear these trousers for me?"
                # if her_whoring >= 0:
                    # if her_whoring < 5:
                        # call her_main("[genie_name], I don't really like wearing jeans in school!", "disgust", "narrow", "worried", "down")
                        # m "But you wore it before?"
                        # call her_main("Yes, because it was raining.", "soft", "narrow", "worried", "down")
                        # call her_main("That was just an exception, [genie_name]. Girls are supposed to wear skirts here at Hogwarts!", "open", "closed", "base", "mid")
                        # call her_main("At all times!", "open", "base", "base", "mid")
                        # m "So what you are telling me is, you broke the rules?"
                        # call her_main("No I did not, [genie_name]!", "clench", "closed", "angry", "mid")
                        # call her_main("(I had no choice...)", "annoyed", "narrow", "angry", "R")
                        # m "Stop with the excuses and put on those jeans, [hermione_name]."
                        # call her_main("Fine, [genie_name]. If I have to.", "open", "closed", "base", "mid")
                        # call her_main("(Just hope those Slytherins will stop calling me mudblood because of this...)", "annoyed", "narrow", "angry", "R")
                    # elif her_whoring < 11:
                        # call her_main("Sure, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me go change.", "base", "base", "base", "mid")
                    # else:
                        # call her_main("But they are so long, [genie_name]!", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("I can't even show off my legs in those!", "annoyed", "base", "angry", "mid")
                        # call her_main("(They make my ass look amazing though...)", "disgust", "narrow", "base", "down")
                        # call her_main("(Now that I think about it...)", "annoyed", "narrow", "annoyed", "up")
                        # call her_main("Fine, I will wear them.", "base", "narrow", "base", "mid_soft")
                # else:
                    # pass

            # #Pants Jeans Short #Done
            # elif skirt_choice == "pants_jeans_short":
                # m "Could you wear those trousers for me?"
                # if her_whoring >= 5:
                    # if her_whoring < 11:
                        # call her_main("Sure, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("Let me go change.", "base", "base", "base", "mid")
                    # else: #20+
                        # call her_main("Alright, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("(They are sooo tight... I can barely even fit my ass into them...)", "soft", "narrow", "annoyed", "up")
                        # call her_main("Let me put them on for you.", "base", "narrow", "base", "mid_soft")
                # else:
                    # call her_main("I'm sorry, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("But I don't think I should wear trousers like those on school grounds...", "open", "closed", "base", "mid")
                    # call her_main("(They look really nice though...)", "base", "narrow", "worried", "down")
                    # call her_main("(Maybe next time...)", "base", "base", "base", "R")
                    # call her_main("I have to refuse.", "soft", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # #Pants Retro Shorts #Done
            # elif skirt_choice == "pants_retro_shorts":
                # m "I want you to wear these trousers for me."
                # if her_whoring >= 17:
                    # if her_whoring < 20:
                        # call her_main("(These trousers look so short...)", "disgust", "narrow", "base", "down")
                        # call her_main("(My ass is gonna be on display the whole time in those...)", "open_tongue", "narrow", "base", "up",cheeks="blush")
                        # call her_main("Alright, [genie_name].", "smile", "happyCl", "base", "mid")
                        # call her_main("Let me just change it.", "base", "narrow", "base", "mid_soft")
                    # else: #20+
                        # call her_main("Alright, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("I bet you love how my ass looks in those.", "smile", "narrow", "base", "mid_soft")
                        # g9 "You bet I do!"
                        # call her_main("Glad to hear that, [genie_name].", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("No, [genie_name].", "open", "happyCl", "worried", "mid")
                        # call her_main("I will not wear trousers that short here in school!", "angry", "base", "worried", "mid")
                        # call her_main("(What is he thinking?!...)", "annoyed", "narrow", "angry", "R")
                    # else:
                        # call her_main("I'm sorry, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("But I don't think I should wear trousers like those on school grounds...", "open", "closed", "base", "mid")
                        # call her_main("(They look really nice though...)", "base", "narrow", "worried", "down")
                        # call her_main("(Maybe next time...)", "base", "base", "base", "R")
                        # call her_main("I have to refuse.", "soft", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # #Pants Rocker Shorts #Done
            # elif skirt_choice == "pants_rocker":
                # m "I want you to wear these trousers for me."
                # if her_whoring >= 17:
                    # if her_whoring < 23:
                        # call her_main("(These trousers are so short...)", "disgust", "narrow", "base", "down")
                        # call her_main("(I'm such a pervert!)", "open_tongue", "narrow", "base", "up",cheeks="blush")
                        # call her_main("Alright, [genie_name].", "smile", "happyCl", "base", "mid")
                        # call her_main("Let me just change it.", "base", "narrow", "base", "mid_soft")
                    # else:
                        # call her_main("Alright, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("I bet you love how my ass looks in those.", "smile", "narrow", "base", "mid_soft")
                        # g9 "You bet I do!"
                        # call her_main("Glad to hear that, [genie_name].", "base", "narrow", "base", "mid_soft")
                # else:
                    # if her_whoring < 5:
                        # call her_main("What?!...", "angry", "base", "angry", "mid")
                        # call her_main("What?!... What is this?", "angry", "base", "angry", "mid",emote="angry")
                        # m "I just said those are--"
                        # call her_main("[genie_name]!", "shock", "wide", "base", "stare")
                        # call her_main("You can't just hand underwear to your students!", "angry", "base", "worried", "mid")
                        # m "Underwear?"
                        # call her_main("Yes, underwear! Panties!", "open", "happyCl", "worried", "mid")
                        # call her_main("What else can you possibly call this?", "annoyed", "narrow", "annoyed", "mid")
                        # m "That's a perfectly fine pair of jeans!"
                        # m "No need to make such a fuss about them!... Just put them on!"
                        # call her_main("No I will not!", "scream", "happyCl", "worried", "mid")
                        # call her_main("(Not in a million years...)", "angry", "base", "angry", "mid")
                    # elif her_whoring < 11:
                        # call her_main("I'm sorry, [genie_name].", "open", "happyCl", "worried", "mid")
                        # call her_main("But I will not wear trousers that short on school grounds!", "angry", "base", "worried", "mid")
                        # call her_main("(What is he thinking?!...)", "annoyed", "narrow", "angry", "R")
                    # else:
                        # call her_main("I'm sorry, [genie_name].", "soft", "base", "base", "R")
                        # call her_main("But I don't think I should wear trousers like those on school grounds...", "open", "closed", "base", "mid")
                        # call her_main("(They look really nice though...)", "base", "narrow", "worried", "down")
                        # call her_main("(Maybe next time...)", "base", "base", "base", "R")
                        # call her_main("I have to refuse.", "soft", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe
            # else:
                # pass

            # hide screen hermione_main
            # with d3

            # pause.5

            # call set_her_bottom(skirt_choice)

            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else:
            # #Change this to:
            # #if skirt_choice == wardrobe_item and Whoring < wardrobe_item.whoring_requirement:
            # #    ">She won't wear that skirt just yet."
            # #    if cheats_active or game_difficulty <= 2:
            # #        ">Try again at Whoring level "+ ""wardrobe_item.whoring_requirement +"."
            # #    jump return_to_wardrobe

            # #Uniform
            # if skirt_choice == "skirt_2" and her_whoring < 5:
                # ">She won't wear that skirt just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 5."
                # jump return_to_wardrobe
            # if skirt_choice == "skirt_3" and her_whoring < 8:
                # ">She won't wear that skirt just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 8."
                # jump return_to_wardrobe
            # if skirt_choice == "skirt_4" and her_whoring < 14:
                # ">She won't wear that skirt just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 14."
                # jump return_to_wardrobe
            # if skirt_choice in ["skirt_5","skirt_7"] and her_whoring < 17:
                # ">She won't wear that skirt just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 17."
                # jump return_to_wardrobe

            # if skirt_choice == "uni_top_cheer" and her_whoring < 5:
                # if (h_bottom_color == "green" or h_bottom_color == "dark_green" or h_bottom_color == "blue" or h_bottom_color == "dark_blue" or h_bottom_color == "yellow"):
                    # if her_whoring < 11:
                        # ">She won't wear that skirt just yet."
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 11."
                        # jump return_to_wardrobe
                # else: #Gryffindor
                    # ">She won't wear that skirt just yet."
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # if skirt_choice == "uni_top_cheer_skimpy" and her_whoring < 8:
                # if (h_bottom_color == "green" or h_bottom_color == "dark_green" or h_bottom_color == "blue" or h_bottom_color == "dark_blue" or h_bottom_color == "yellow"):
                    # if her_whoring < 11:
                        # ">She won't wear that skirt just yet."
                        # if cheats_active or game_difficulty <= 2:
                            # ">Try again at Whoring level 11."
                        # jump return_to_wardrobe
                # else: #Gryffindor
                    # ">She won't wear that skirt just yet."
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe


            # #Uniform Low
            # if skirt_choice == "skirt_1_low" and her_whoring < 8:
                # ">She won't wear that top just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 8."
                # jump return_to_wardrobe
            # if skirt_choice == "skirt_2_low" and her_whoring < 11:
                # ">She won't wear that top just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 11."
                # jump return_to_wardrobe
            # if skirt_choice == "skirt_3_low" and her_whoring < 17:
                # ">She won't wear that top just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 17."
                # jump return_to_wardrobe
            # if skirt_choice == "skirt_4_low" and her_whoring < 20:
                # ">She won't wear that top just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 20."
                # jump return_to_wardrobe


            # #Pants
            # if skirt_choice == "pants_jeans_short" and her_whoring < 5:
                # ">She won't wear those trousers just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 5."
                # jump return_to_wardrobe
            # if skirt_choice == "pants_retro_shorts" and her_whoring < 17:
                # ">She won't wear those trousers just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 17."
                # jump return_to_wardrobe
            # if skirt_choice == "pants_rocker" and her_whoring < 17:
                # ">She won't wear those trousers just yet."
                # if cheats_active or game_difficulty <= 2:
                    # ">Try again at Whoring level 17."
                # jump return_to_wardrobe



            # else:
                # pass

            # $ hide_transitions = True
            # call set_her_bottom(skirt_choice)
            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old

### Equip Susan's Bottom ###
label equip_sus_bottom:
    call set_sus_bottom(skirt_choice)

    jump return_to_wardrobe
