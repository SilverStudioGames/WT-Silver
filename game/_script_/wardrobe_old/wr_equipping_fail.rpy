

# label equipping_failed:

    # if her_mood >= 1 and her_mood <=5:
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hermione_xpos = 665
            # $ hide_transitions = False #activates dissolve in her_main

            # m "[hermione_name]..."
            # m "Would you wear this--"
            # call her_main("I'm sorry [genie_name]...", "open", "closed", "base", "mid")
            # call her_main("But I don't feel like dressing up for you today.", "open", "base", "worried", "R")
            # m "Any chance I could convince you otherwise?"
            # call her_main("Hmm...", "annoyed", "base", "base", "mid") #very upset, default
            # call her_main("I want 5 house points! And that's no guarantee that I'm actually going to wear...", "open", "closed", "base", "mid")
            # call her_main("Whatever it is you want me to put on.", "annoyed", "narrow", "annoyed", "mid")

            # menu:
                # "-Give her the points-":
                    # m "alright, [hermione_name]... here are your points..."
                    # m "ahe--hem..."
                    # m "Five points for Gryffindor!"
                    # m "Was that good enough for you?"
                    # call her_main("...", "normal", "base", "base", "mid")
                    # call her_main("Thank you, [genie_name].", "soft", "base", "base", "R")
                    # m "Great, now I forgot what I wanted you to wear..."
                    # $ gryffindor += 5
                    # $ her_mood = 0
                # "-Don't give her the points-":
                    # m "I don't think so, missy!"
                    # call her_main("...", "annoyed", "squint", "angry", "mid")
                    # call her_main("Fine!", "angry", "base", "angry", "mid")
                    # call her_main("I don't want them anyway!", "annoyed", "narrow", "worried", "down")
                    # m "You sure?"
                    # call her_main("Tzzz--", "angry", "base", "angry", "mid")
        # else:
            # hide screen hermione_main
            # with d3
            # ">Hermione is mad at you! She won't wear it!"
            # menu:
                # ">You can give Gryffindor points to better her mood."
                # "-5 points for Gryffindor!-":
                    # $ gryffindor += 5
                    # $ her_mood = 0
                    # ">Hermione is no longer mad at you!"
                    # call set_her_face(mouth="happy", eyes="neutral")
                # "-Don't bother-":
                    # call set_her_face(mouth="angry", eyes="angry")

        # $ hide_transitions = True
        # call her_main(xpos="wardrobe")
        # call screen wardrobe_old


    # if her_mood >= 6 and her_mood <=10:
        # if wardrobe_chitchat_active:
            # $ hide_transitions = False
            # hide screen hermione_main
            # with d3
            # m "[hermione_name]..."
            # m "I'd like you to wear--"
            # call her_main("No, [genie_name]...", "open", "closed", "base", "mid",xpos="base") #525=default Hermione xpos
            # call her_main("I'm still mad at you for what you did!", "open", "base", "worried", "R")
            # m "Will you wear it if I give Gryffindor some points?"
            # call her_main("...", "annoyed", "squint", "base", "mid")
            # call her_main("Fifteen house points!", "open", "base", "base", "mid")
            # call her_main("And maybe I will wear it.-- Only maybe!", "open", "base", "base", "R")

            # menu:
                # "-Give her the points-":
                    # m "alright, [hermione_name]... here are your points..."
                    # m "Fifteen points..."
                    # g4 "for Gryffindor!"
                    # m "Was that good enough for you?"
                    # call her_main("(It's so easy to get points out of him!)", "soft", "base", "base", "R")
                    # call her_main("Thank you,[genie_name].", "open", "closed", "base", "mid")
                    # m "No problem. Now put on... {w=0.9}what was it again?"
                    # $ gryffindor += 15
                    # $ her_mood = 0
                # "-Don't give her the points-":
                    # m "I'm already giving you new clothing! Isn't that enough?"
                    # call her_main("No it's not enough, [genie_name]!", "open", "closed", "base", "mid")
                    # call her_main("I want those points!", "angry", "base", "angry", "mid")
                    # call her_main("(You can shove those clothes up your ass...)", "annoyed", "narrow", "angry", "R")
                    # m "I'm not giving you the points, [hermione_name]."
                    # call her_main("Tzzz--", "angry", "base", "angry", "mid")
                    # call her_main("Well then wear your... {w=0.5}-stuff yourself!", "scream", "closed", "angry", "mid")
                    # m "Wouldn't look good on me..."
                    # call her_main("I don't care.", "annoyed", "narrow", "annoyed", "mid")
        # else:
            # hide screen hermione_main
            # with d3
            # ">Hermione is really mad at you! She won't wear it!"
            # menu:
                # ">You can give Gryffindor points to better her mood."
                # "-15 points for Gryffindor!-":
                    # $ gryffindor += 15
                    # $ her_mood = 0
                    # ">Hermione is no longer mad at you!"
                    # call set_her_face(mouth="happy", eyes="neutral")
                # "-Don't bother-":
                    # call set_her_face(mouth="angry", eyes="angry")

        # $ hide_transitions = True
        # call her_main(xpos="wardrobe")
        # call screen wardrobe_old


    # if her_mood >= 11:
        # if wardrobe_chitchat_active:
            # $ hide_transitions = False #activates dissolve in her_main
            # hide screen hermione_main
            # with d3
            # m "[hermione_name]..."
            # m "Would you please--"
            # call her_main("No--", "open", "closed", "base", "mid",xpos="base") #525=default Hermione xpos
            # call her_main("...", "annoyed", "narrow", "annoyed", "mid")
            # m "I just want you to wear--"
            # call her_main("I SAID NO, [genie_name]!", "scream", "closed", "angry", "mid")
            # call her_main("tzzzz...", "annoyed", "narrow", "angry", "R")
            # g4 "Fine! {w=0.9}Forget it."
        # else:
            # hide screen hermione_main
            # with d3
            # ">Hermione is really mad at you! There is no point in trying to make her wear it!"
            # call set_her_face(mouth="angry", eyes="angry")


        # $ hide_transitions = True
        # call her_main(xpos="wardrobe")
        # call screen wardrobe_old
