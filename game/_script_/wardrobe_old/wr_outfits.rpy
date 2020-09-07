#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

### Equip Outfit ###
label equip_outfit:
    #Luna
    if active_girl == "luna":
        jump equip_lun_outfit
    #Susan
    if active_girl == "susan":
        jump equip_sus_outfit

# ### Equip Hermione's Outfit ###
# label equip_her_outfit:
    # if her_mood >= 1:
        # jump equipping_failed

    # if outfit_choice != hermoine_outfit_GLBL or outfit_choice == hermoine_outfit_GLBL:
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hide_transitions = False
            # $ hermione_xpos = 665

            # # Outfits
            # if outfit_choice == hg_outfit_maid_ITEM:
                # m "Do you know what a maid is?"
                # call her_main("Of course I know...", "open", "base", "base", "mid")
                # call her_main("Wait, why would you ask me that?", "normal", "slit", "low", "stare")
                # g9 "I would like you to be my maid."
                # if her_whoring >= 11: #Success
                    # call her_main("Your maid? Does that mean I have to wear one of those silly outfits?", "open", "wink", "base", "mid")
                    # g9 "Absolutely!"
                    # call her_main("...", "normal", "narrow", "worried", "down")
                    # call her_main("Fine...", "open", "base", "base", "R")
                    # call her_main("And you expect me to clean up for you too?", "open", "wink", "base", "mid")
                    # m "No, actually. Just put on the outfit."
                    # call her_main("Alright...", "smile", "base", "base", "mid")
                # else: #Fail
                    # call her_main("Your maid? [genie_name] isn't it the house elves job to clean up the rooms?", "open", "base", "base", "mid")
                    # call her_main("(Not that I approve of this horrible house-elf enslavement...)", "annoyed", "narrow", "angry", "R")
                    # call her_main("I have more important things to attend to. I have no time to clean up behind you...", "open", "closed", "base", "mid")
                    # call her_main("Unless... there are some points in it for me...", "soft", "base", "base", "R")
                    # m "No points..."
                    # g9 "But I've got this cute outfit for you!"
                    # call her_main("No thank you, [genie_name]...", "open", "closed", "base", "mid")
                    # call her_main("Outfits don't win house cups...", "soft", "base", "angry", "mid")
                    # m "(Damn her...)"
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_outfit_pirate_ITEM:
                # m "Know anything about pirates [hermione_name]?"
                # call her_main( "They pillage and kill people.","open","base")
                # m "..."
                # m "How do you feel about wearing a pirates outfit?"
                # if her_whoring >= 5: #Success
                    # call her_main( "Depends...[genie_name] what kind of pirate are we talking about?","base","base")
                    # m "The adventurous type for sure."
                    # call her_main( "I don't know...","open","base")
                    # m "The kind that fights a corrupt government for the good of the people."
                    # call her_main("...", "open", "narrow", "base", "down")
                    # m "It will feel very empowering I'm sure."
                    # m "The female pirates were said to have a very good relationship with their crew."
                    # call her_main( "Fine... shipmate [genie_name].","crooked_smile","base")
                # else: #Fail
                    # call her_main( "Doesn't really sound like my kind of thing to be honest [genie_name].","base","baseL")
                    # m "I thought you might be a fan of seamen..."
                    # call her_main( "I don't really have anything against seamen... but pirates aren't really the same thing.","open","base")
                    # m "Butt pirates?"
                    # call her_main( "What?","base","base")
                    # call her_main( "It's a bit to revealing... drop it for now okay?","disgust","base")
                    # m "Fair enough, I'm sure we'll find something you'd like to wear."
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 5."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_outfit_japan_ITEM:
                # m "Hogwarts isn't the only school with a dress code you know."
                # call her_main( "I know that, I'm a muggle born after all.","open","base")
                # m "Right, would you put this Japanese schoolgirl outfit on?"
                # if her_whoring >= 8: #Success
                    # call her_main( "Cute, where did you even get this? I didn't know you've visited Japan.","base","base")
                    # m "It's a replica..."
                    # call her_main( "Oh... well, the colour is nice.", "grin","base")
                    # call her_main( "I guess I could wear it for a bit.", "grin","happyCl")
                # else: #Fail
                    # call her_main( "I'd rather not be accused of stirring cultural appropriation.", "annoyed","base")
                    # m "Cultural what now?"
                    # call her_main( "Never mind.", "annoyed" ,"angryCl")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 8."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_outfit_christmas_ITEM:
                # m "You better watch out--"
                # m "You better not cry--"
                # call her_main("Sir?", "open", "wink", "base", "mid")
                # g9 "Santa Claus is going to town!"
                # if her_whoring >= 17: #Success
                    # call her_main("Oh...", "soft", "base", "base", "R")
                    # call her_main("Am I on the naughty list, mister Santa?", "soft", "narrow", "base", "mid_soft",cheeks="blush")
                    # g4 "You are!"
                    # call her_main("Does that mean I'm not getting any presents?", "base", "narrow", "base", "mid_soft")
                    # m "No [hermione_name]..."
                    # g9 "Santa is gonna stuff your stockings real good!"
                    # m "But first, put on that outfit, would you..."
                    # call her_main("Of course.", "base", "narrow", "base", "mid_soft")
                # else: #Fail
                    # call her_main("Don't you mean, is coming to town?", "open", "wink", "base", "mid")
                    # g9 "Damn right he's going to cum!"
                    # call her_main("You aren't making any sense, [genie_name]!", "annoyed", "base", "base", "R")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_outfit_present_ITEM:
                # if her_whoring >= 20: #Success
                    # m "[hermione_name], did you know today is my birthday?"
                    # call her_main("Oh really, [genie_name]? Your birthday?", "base", "narrow", "base", "mid_soft")
                    # g9 "It is!"
                    # if not birthday_happened:
                        # $ birthday_happened = True
                        # call her_main("(I highly doubt that...)", "base", "base", "base", "R")
                    # else:
                        # call her_main("(What a poor liar...)", "base", "base", "base", "R")
                    # call her_main("Well in that case...", "open", "narrow", "base", "mid_soft")
                    # call her_main("What does our birthday boy wish for his special day?", "open", "closed", "base", "mid")
                    # call her_main("You can have anything you want!", "soft", "narrow", "base", "mid_soft")
                    # g4 "(Hot damn!)"
                    # g9 "How about your body?"
                    # call her_main("Hmm... my body?", "base", "narrow", "base", "mid_soft")
                    # call her_main("... completely naked... wrapped in a tight ribbon for you to unwrap...", "open", "narrow", "base", "R_soft")
                    # call her_main("... and play with...", "open_tongue", "narrow", "base", "mid_soft")
                    # call her_main("I bet you would like that, [genie_name]?", "base", "narrow", "base", "mid_soft")
                    # g9 "Indeed I would!"
                    # call her_main("Well then, Happy Birthday, [genie_name].", "soft", "narrow", "base", "mid_soft")
                # else:
                    # m "[hermione_name], did you know it's my birthday today?"
                    # if not birthday_happened:
                        # $ birthday_happened = True
                        # call her_main("It is? But I've read in the daily prophet that your birthday is on the--", "open", "base", "base", "R")
                        # m "No no, it's today!"
                        # call her_main("*uhm*... Ok... Happy bithday then, [genie_name].", "soft", "base", "base", "mid")
                        # m "Would you grant me a wish?"
                        # call her_main("Of course.", "base", "base", "base", "mid")
                        # g9 "Could you dress up as my present?"
                        # m "Just put this on."
                        # call nar(">You hand her the ribbon.")
                    # else:
                        # call her_main("Sure, [genie_name]... Just like last time you said that.", "open", "base", "base", "R")
                        # m "(Shit, she's right! I've already used that card.)"
                        # call her_main("What is it you want, [genie_name]?", "clench", "narrow", "annoyed", "mid")
                        # g9 "Could you dress up as my present?"
                        # call her_main("That again... [genie_name], do you happen to have some sort of... unpacking fetish?", "open", "narrow", "annoyed", "mid")
                        # m "I've never had a childhood..."
                        # m "Just put this on."
                        # call nar(">You hand her the ribbon.")
                    # call her_main("I'm supposed to wrap it around me?", "open", "wink", "base", "mid")
                    # m "Yes. But first you need to get naked."
                    # if her_whoring < 5:
                        # call her_main("What?", "shock", "wide", "base", "stare")
                        # call her_main("Are you out of your mind, [genie_name]?", "open", "closed", "angry", "mid")
                        # call her_main("Never ask me something like this again!", "angry", "base", "angry", "mid")
                    # else:
                        # call her_main("Typical...", "open", "closed", "base", "mid")
                        # call her_main("I'm sorry, [genie_name]. But this just sounds like just another one of your silly ideas...", "open", "narrow", "annoyed", "mid")
                    # m "But... my birthday!"
                    # if not birthday_happened:
                        # call her_main("Birthday or not, I would never do such a thing! For anyone!", "scream", "closed", "angry", "mid")
                    # else:
                        # call her_main("It's not your birthday!", "scream", "base", "angry", "mid")
                        # m "Alright, alright... No need to scream like that."
                    # call her_main("(What a perv...)", "annoyed", "narrow", "angry", "R")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 20."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_gamble_slut_ITEM:
                # m "You know that card game that we've been playing?"
                # call her_main("Wizard Cards?", "open", "base", "base", "mid")
                # call her_main("Yes... What about it?", "normal", "slit", "low", "stare")
                # g9 "So, apparently since I've been so successful at it... I've received this outfit from trading in those tokens."
                # if her_whoring >= 15: #Success
                    # call her_main("Hmm, a bit tight it seems. The hat is cute though.", "open", "wink", "base", "mid")
                    # g9 "So you'll wear it?"
                    # call her_main("...", "normal", "narrow", "worried", "down")
                    # call her_main("Fine...", "open", "base", "base", "R")
                    # call her_main("You did beat me fair and square...", "open", "wink", "base", "mid")
                    # m "Great, perhaps you'll win next rematch..."
                    # call her_main("Perhaps...", "smile", "base", "base", "mid")
                # else: #Fail
                    # call her_main("And what? [genie_name] You're expecting me to just wear this thing because you've won it?", "open", "base", "base", "mid")
                    # call her_main("(Does he think he can play me like he plays cards?)", "annoyed", "narrow", "angry", "R")
                    # call her_main("Now, if you excuse me I have more important things to do...", "open", "closed", "base", "mid")
                    # call her_main("Unless you needed anything else?", "soft", "base", "base", "R")
                    # m "..."
                    # g9 "But, I won... fair and square."
                    # call her_main("You may be a winner, [genie_name] but you have yet to learn how to play your cards right with me.", "open", "closed", "base", "mid")
                    # call her_main("Card master...", "crooked_smile", "wink", "base", "mid")
                    # m "(Damn it...)"
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 15."
                    # jump return_to_wardrobe

            # # Costumes
            # if outfit_choice in [hg_costume_power_girl_ITEM,hg_costume_ms_marvel_ITEM]:
                # m "Are there any heroines you know of?"
                # if her_whoring >= 11: #Success
                    # call her_main("You mean like superheroines?", "open", "wink", "base", "mid")
                    # m "Yep"
                    # if outfit_choice == hg_costume_power_girl_ITEM:
                        # m "I've got this Power Girl outfit I would like you to wear..."
                    # if outfit_choice == hg_costume_ms_marvel_ITEM:
                        # m "I have this outfit for you. It's Miss Marvel's!"
                    # call nar(">You hand her the outfit.")
                    # call her_main("Fine. I'll wear it.", "soft", "base", "base", "R")
                    # m "You will?"
                    # call her_main("Of course! I like her. She's a great role model for girls, after all!", "open", "closed", "base", "mid")
                    # if outfit_choice == hg_costume_power_girl_ITEM:
                        # call her_main("Although... That cleavage on her is a bit much.", "disgust", "narrow", "worried", "down")
                        # g9 "But that's the best part!"
                        # call her_main("Why doesn't that suprise me. That you would think so...", "annoyed", "base", "angry", "mid")
                    # call her_main("Just let me put it on...", "smile", "narrow", "base", "mid_soft")
                # else: #Fail
                    # call her_main("Of course!", "open", "base", "worried", "R")
                    # call her_main("Rowena Ravenclaw, Helga Hufflepuff, Isolt Sayre, Joan of Arc...", "open", "base", "worried", "R")
                    # call her_main("I can name you hundreds! All witches I admire and look up to!", "grin", "closed", "base", "mid")
                    # m "(Who?)"
                    # m "No no, I'm talking about Comic books! Superheroes!"
                    # call her_main("Oh...", "soft", "slit", "low", "stare")
                    # call her_main("[genie_name], how do you even know about such things? Comics?", "soft", "wink", "base", "mid")
                    # g9 "I know all about human activities and pleasures!"
                    # call her_main("Muggle activities? Well of course, somebody as wise as you would be knowledged about all sorts of things.", "open", "base", "base", "R")
                    # call her_main("I myself don't think too highly of comic books, [genie_name].", "soft", "slit", "low", "stare")
                    # call her_main("Not to mention the contumelious treatment and over-sexualisation of female heroines.", "soft", "slit", "low", "stare")
                    # call her_main("It's disgusting...", "open", "closed", "base", "mid")
                    # call her_main("I have to refuse, [genie_name]!", "annoyed", "base", "angry", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe


            # if outfit_choice == hg_costume_harley_quinn_ITEM:
                # m "Know anything about Batman?"
                # call her_main( "Uh, do you mean like vampires?","soft","narrow")
                # m "No, he's a comic book character."
                # call her_main( "Comics are usually a bit to unrealistic to me.","base","base")
                # m "\"In a world with actual wizards, Batman is too unrealistic?\""
                # m "I'd like you to try out this villain outfit."
                # if her_whoring >= 14: #Success
                    # call her_main( "I don't know, sell it to me.","base","base")
                    # m "Uh, she's a misunderstood girl in love with one of the main characters enemies."
                    # call her_main( "I feel misunderstood at times too, does she get her love in the end?","base","narrow")
                    # m "Well, it's complicated. There's a bunch of different itterations too."
                    # call her_main("Will you stop talking about it if I put it on?", "annoyed", "base", "worried", "mid"
                    # m "Yes."
                    # call her_main( "Fine." ,"base","base")
                # else: #Fail
                    # call her_main("No thanks, it seems a bit too tight for me.", "soft", "base", "worried", "mid"
                    # m "\"I'll loosen you up soon enough.\""
                    # call her_main( "What are you looking at. Is it something I said?","base","narrow")
                    # m "Oh, nothing my dear... I was just meditating."
                    # call her_main("\"More like, falling asleep.\"", "base", "squint", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 14."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_costume_tifa_ITEM:
                # m "Do you know anything about video games [hermione_name]?"
                # call her_main( "I was usually too busy reading at home to have time for such things, why?", "soft","narrow")
                # m "I'd like you to put this Tifa outfit for me"
                # if her_whoring >= 11: #Success
                    # call her_main( "Why do you even know anything about video games professor?" ,"soft","narrow")
                    # m "Some people say video games are art miss Granger."
                    # call her_main( "And?" ,"soft","narrow")
                    # m "And art is important muggle study material."
                    # call her_main( "It does look creative." ,"soft","narrow")
                    # m "You'd look great in it I'm sure."
                    # call her_main( "Okay, thank you." ,"soft","narrow")
                # else: #Fail
                    # call her_main( "I'd rather just wear my own clothes..." ,"soft","narrow")
                    # call her_main( "suspenders has never really been my kind of thing." ,"soft","narrow")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_costume_lara_croft_ITEM:
                # m "[hermione_name]..."
                # m "I'd like you to dress up."
                # call her_main("As what?", "open", "base", "worried", "R")
                # g9 "As the greatest british female archaeologist who's ever lived!"
                # call her_main("Gertrude Bell?", "grin", "closed", "base", "mid")
                # m "What?"
                # m "No... I'm talking about Lara Croft..."
                # if her_whoring >= 17:
                    # call her_main("...", "annoyed", "narrow", "worried", "down")
                    # call her_main("Fine, if I have to.", "open", "closed", "base", "mid")
                    # call her_main("Let me go and change.", "annoyed", "base", "base", "R")
                # else:
                    # call her_main("*uhm*... who?", "soft", "wink", "base", "mid")
                    # m "She's a video game character."
                    # call her_main("What?", "scream", "wide", "base", "stare")
                    # call her_main("In that case, absolutely not!", "scream", "closed", "angry", "mid")
                    # m "Why not?"
                    # call her_main("Video games are for idiots.", "annoyed", "narrow", "angry", "R")
                    # m "..."
                    # m "(No they aren't...)"
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # if outfit_choice in [hg_witch_ITEM,hg_witch_skimpy_ITEM]:
                # m "[hermione_name], have you ever heard about witches?"
                # call her_main("[genie_name]? I am a witch?", "soft", "slit", "low", "stare")
                # m "Oh right..."
                # m "To my defense, you don't look much like one..."
                # call her_main("I don't? How are witches supposed to look?", "open", "base", "base", "mid")
                # m "Well, normally they'd wear stuff like witch-hats... frills... and capes!"
                # call her_main("Capes?", "disgust", "wink", "base", "mid")
                # if her_whoring >= 17: #Success
                    # m "Here it is."
                    # call nar(">You hand her the outfit.")
                    # call her_main("It looks really old-fashioned...", "disgust", "narrow", "worried", "down")
                    # if outfit_choice == hg_witch_skimpy_ITEM:
                        # call her_main("And why is there a hole down there?", "disgust", "slit", "low", "stare")
                        # g9 "It's great, isn't it!"
                        # call her_main("No it isn't! Do you really expect me to show of my pussy like that, to everyone?", "angry", "base", "angry", "mid")
                        # m "Well, only to me..."
                        # m "I believe you can cover it up with a spell or something..."
                        # call her_main("Oh...", "annoyed", "narrow", "worried", "down")
                        # call her_main("You should have told me that first!", "annoyed", "narrow", "annoyed", "mid")
                    # else:
                        # g9 "It's great, isn't it!"
                        # call her_main("Not really...", "annoyed", "narrow", "worried", "down")
                    # g9 "Just put it on, my little witch."
                    # call her_main("Fine... Give me a minute...", "smile", "base", "base", "R")
                # else: #Fail
                    # call her_main("Capes are silly, [genie_name].", "open", "closed", "base", "mid")
                    # call her_main("I have to refuse.", "annoyed", "base", "base", "mid")
                    # m "I can respect that opinion."
                    # m "(Is she nuts? Capes are awesome...)"
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 17."
                    # jump return_to_wardrobe

            # if outfit_choice in [hg_costume_elizabeth_ITEM,hg_costume_yennefer_ITEM]:
                # m "[hermione_name], I have a new outfit for you!"
                # call her_main("A new outfit? You mean as a gift?", "open", "wink", "base", "mid")
                # m "Yes. It's a character from a video-ga--"
                # show screen blktone
                # call her_main("...", "normal", "base", "angry", "mid")
                # m "I mean... she's a famous, ugh... witch?"
                # hide screen blktone
                # call her_main("...", "smile", "base", "base", "mid")
                # m "(Phew, that was close...)"
                # call nar(">You hand her the outfit.")
                # if her_whoring >= 11: #Success
                    # call her_main("It does look nice...", "soft", "narrow", "worried", "down")
                    # if outfit_choice == hg_costume_elizabeth_ITEM:
                        # call her_main("(I really like her necklace...)", "smile", "narrow", "worried", "down")
                    # if outfit_choice == hg_costume_yennefer_ITEM:
                        # call her_main("(I really like her scarf...)", "smile", "narrow", "worried", "down")
                    # call her_main("Let me put it on real quick.", "smile", "narrow", "base", "mid_soft")
                # else: #Fail
                    # call her_main("It's a corset, [genie_name]!", "open", "wink", "base", "mid")
                    # m "So what?"
                    # call her_main("It's too tight! How am I even supposed to breathe in it?", "open", "closed", "base", "mid")
                    # m "Breathing is overrated..."
                    # call her_main("I have to refuse, [genie_name].", "normal", "base", "base", "mid")
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # # Dresses
            # if outfit_choice == hg_dress_dancer_ITEM:
                # if her_whoring >= 11: #Success
                    # m "Giuchie, Giuchie, ya-ya..."
                    # call her_main("Da-Da", "soft", "narrow", "base", "R_soft")
                    # m "Mocha Chocalata..."
                    # call her_main("Ya-Ya", "soft", "narrow", "annoyed", "up")
                    # g9 "Voulez vous coucher avec moi?"
                    # call her_main("............", "open_tongue", "narrow", "annoyed", "up")
                    # m "Girl?..."
                    # call her_main("....................", "open_tongue", "slit", "worried", "ahegao")
                    # m "(Did she just break?)"
                    # m "Snap out of it, [hermione_name]! I need you to put on this outfit here..."
                    # call her_main("What just happened?!", "open", "wide", "base", "stare",trans=hpunch)
                    # call her_main("Oh right. The outfit! Give me a second!", "angry", "happyCl", "worried", "mid",cheeks="blush")
                # else: #Fail
                    # m "Giuchie, Giuchie, ya ya..."
                    # call her_main("(...?)", "normal", "wink", "base", "mid")
                    # m "Mocha Chocalata..."
                    # call her_main("(...!)", "clench", "wide", "base", "stare")
                    # call her_main("[genie_name], what are you doing?", "shock", "happyCl", "worried", "mid")
                    # m "I'm singing... Don't you like that song?"
                    # call her_main("No... {size=-10}Please stop.{/size}", "disgust", "base", "base", "mid")
                    # m "Fine..."
                    # if cheats_active or game_difficulty <= 2:
                        # ">Try again at Whoring level 11."
                    # jump return_to_wardrobe

            # if outfit_choice == hg_dress_yule_ball_ITEM:
                # if not ball_quest.E3_complete: # Dialogue for before she needs the dress.
                    # m "Would you like to wear your new dress?"
                    # call her_main("A dress? What would I need a dress for?", "open", "wink", "base", "mid")
                    # m "Well I just thought you'd look pretty in one so I--"
                    # call her_main("I appreciate your concernes, [genie_name], but I'm not the type of girl who likes to wear dresses.", "scream", "wide", "base", "stare")
                    # call her_main("Especially in school. I have to refuse", "normal", "base", "base", "mid")
                    # jump return_to_wardrobe

                # elif ball_quest.E3_complete and not ball_quest.gave_dress:
                    # # You gift Hermione her dress event. Does not trigger the countdown anymore. Talk to hermione to start the ending now.
                    # hide screen wardrobe_old
                    # with d3
                    # pause.5
                    # jump ball_quest_E5

                # else:
                    # m "Remember that dress I gave you?"
                    # call her_main("Of course! How could I ever forget!", "open", "wide", "base", "stare")
                    # call her_main("Thank you so much, [genie_name]!", "grin", "happyCl", "base", "mid")
                    # her "You got me a new ball dress?"
                    # m "Indeed I did, but you'll have to earn it."
                    # call her_main("Of course!", "angry", "wide", "base", "stare")
                    # call her_main("Let me try it on!", "base", "base", "base", "R",cheeks="blush")




            # hide screen hermione_main
            # with d3
            # pause.5

            # call set_her_outfit(outfit_choice)

            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else: # No chit-chat

            # if outfit_choice == hg_dress_yule_ball_ITEM:
                # if ball_quest.E3_complete and not ball_quest.gave_dress:
                    # # You gift Hermione her dress event. Does not trigger the countdown anymore. Talk to hermione to start the ending now.
                    # $ hide_transitions = False
                    # hide screen wardrobe_old
                    # with d3
                    # pause.5
                    # jump ball_quest_E5

            # $ hide_transitions = True
            # hide screen hermione_main

            # call set_her_outfit(outfit_choice)

            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old

    # else: # Unequip
        # if wardrobe_chitchat_active:
            # hide screen hermione_main
            # with d3

            # $ hide_transitions = False #activates dissolve in her_main
            # $ hermione_xpos = 665

            # m "[hermione_name], could you take off that outfit again?"

            # call her_main("Of course, [genie_name].", "base", "base", "base", "mid")

            # hide screen hermione_main
            # with d3
            # pause.5

            # call set_her_outfit(None)

            # call her_main(xpos="wardrobe")
            # $ hide_transitions = True
            # call screen wardrobe_old

        # else:
            # $ hide_transitions = True
            # hide screen hermione_main

            # call set_her_outfit(None)

            # call her_main(xpos="wardrobe")
            # call screen wardrobe_old



### Equip Luna's Outfit ###
label equip_lun_outfit:
    if (outfit_choice != luna_outfit_GLBL) or (outfit_choice == luna_outfit_GLBL and not luna_wear_outfit):

        call set_lun_outfit(outfit_choice)

        jump return_to_wardrobe

    else: # Unequip

        call set_lun_outfit(None)

        jump return_to_wardrobe

### Equip Susan's Outfit ###
label equip_sus_outfit:
    if (outfit_choice != susan_outfit_GLBL) or (outfit_choice == susan_outfit_GLBL and not susan_wear_outfit):

        call set_sus_outfit(outfit_choice)

        hide screen wardrobe_old
        call screen wardrobe_old

    else: # Unequip

        call set_sus_outfit(None)

        jump return_to_wardrobe
