

### Hermione Chitchats ###

label chit_chat:
    #$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.


    ### WHORING LEVEL 01 ###
    if her_whoring >= 0 and her_whoring <= 2:
        if one_of_ten == 1:
            call her_main("Maybe, if I'd work harder, I could squeeze a few more classes into my schedule...", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 2:
            call her_main("Actually, I don't mind being called a \"know-it-all\".", "open", "closed", "angry", "mid")
            her "I think it's rather flattering..."
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 3:
            call her_main("The basilisk, also known as the king of serpents.", "open", "closed", "angry", "mid")
            her "{i}Herpo the Foul{/i} was the first to breed a Basilisk."
            her "He accomplished that by--"
            call her_main("Oh, I'm sorry, professor, we have another test tomorrow...", "open", "base", "worried", "R")
            her "I Just want to make sure that I'm ready..."
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 4:
            call her_main("If my body wouldn't require sleep...", "open", "base", "worried", "R")
            call her_main("I would be able to spend twice as much time with studying!?", "angry", "wide", "base", "stare")
            call her_main("I wonder if there's a spell for that...", "open", "base", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 5:
            call her_main("So far professor Trelawney did not teach me a single piece of any actual knowledge, sir.", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 6:
            call her_main("If only more students were honest, responsible and diligent like me.", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 7:
            call her_main("How can some people be so ignorant to the world's problems?", "open", "closed", "angry", "mid")
            her "Personally, I think that every single one of us should work harder to make our world a better place."
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 8:
            call her_main("It's been raining quite a lot lately...", "open", "base", "worried", "R")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 9:
            call her_main("Very few people know this...", "open", "base", "worried", "R")
            call her_main("... But I really like chocolate.", "base", "base", "base", "mid")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 10:
            call her_main("I am sorry sir, but I don't really have time for idle chat chats...", "base", "base", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")


    ### WHORING LEVEL 02 ###
    if her_whoring >= 3 and her_whoring <= 5:
        if one_of_ten == 1:
            call her_main("I read somewhere that a full moon often makes it easier to concentrate at a task at hand...", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 2:
            call her_main("I love nothing more than to curl up by a fireplace during a rainstorm with a good book...", "base", "base", "base", "mid")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 3:
            call her_main("A peculiar rumour concerning professor Snape has been circulating in the school lately...", "open", "base", "worried", "R")
            call her_main("No, I probably shouldn't...", "soft", "base", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 4:
            call her_main("Despite the questionable nature of the favours you have been buying from me lately, sir...", "open", "closed", "angry", "mid")
            her "I am grateful to you for your help..."
            call her_main("Gryffindor needs those points now more than ever...", "annoyed", "squint", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 5:
            call her_main("Why Quidditch is so popular among the girls is simply beyond me...", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 6:
            call her_main("The \"Men's Rights Movement\" is steadily gaining popularity.", "open", "closed", "angry", "mid")
            her "It's very fulfilling to know that you are helping to improve our society."
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 7:
            call her_main("The Hogwarts school library is considered to be quite extensive...", "open", "closed", "angry", "mid")
            call her_main("Still, I can't help but wish that it'd be bigger...", "open", "squint", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 8:
            call her_main("As one of the top students in this school I have a reputation to keep...", "open", "base", "worried", "R")
            her "People look up to me..."
            call her_main("... So, your discretion is very appreciated, sir.", "open", "base", "base", "mid")
            call her_main("", "annoyed", "base", "worried", "R")

        elif one_of_ten == 9:
            call her_main("That favour I sold you the other say, sir...", "open", "base", "worried", "mid")
            call her_main(".......", "normal", "happyCl", "worried", "mid")
            call her_main("I only agreed to it because the needs of my house always come first.", "open", "narrow", "worried", "down")
            call her_main("I just wanted you to know that, sir...", "upset", "closed", "base", "mid")

        elif one_of_ten == 10:
            call her_main("The \"Autumn Ball\" is still several months away...", "open", "closed", "angry", "mid")
            call her_main("But some girls are already discussing what kind of dress they are going to wear...", "open", "base", "worried", "mid")
            call her_main("", "annoyed", "narrow", "annoyed", "mid")


    ### WHORING LEVEL 03 ###
    if her_whoring >= 6 and her_whoring <= 8:
        if one_of_ten == 1:
            call her_main("Do you remember when you asked me to show you my panties for the first time sir?", "open", "closed", "angry", "mid")
            her "I was so furious with you then..."
            call her_main("Now I see that I was just being selfish...", "annoyed", "squint", "angry", "mid")
            her "After all, the honour of my house is at stake here..."
            call her_main("And that shall be my one and only concern!", "normal", "squint", "angry", "mid")

        elif one_of_ten == 2:
            call her_main("The rate at which the Slytherin house has been gaining points lately is simply ridiculous.", "open", "closed", "angry", "mid")
            call her_main("I think professor Snape might be behind it.", "angry", "base", "angry", "mid")
            call her_main("You should look into this, sir.", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 3:
            call her_main("Ashwinder eggs, rose thorns, moonstone...", "open", "base", "worried", "R")
            call her_main("*huh*? Am I thinking out loud again?", "open", "base", "worried", "mid")
            call her_main("I apologise...", "grin", "happyCl", "worried", "mid",emote="sweat")
            call her_main("It's just that we have another test soon...", "soft", "base", "base", "R")

        elif one_of_ten == 4:
            call her_main("I dislike the entire house of Slytherin with all my heart, sir.", "angry", "base", "angry", "mid")

        elif one_of_ten == 5:
            call her_main("Hogwarts has really become a second home to me lately...", "open", "closed", "base", "mid")
            call her_main("I don't even miss my parents nearly as much anymore...", "annoyed", "narrow", "worried", "down")
            call her_main("Come to think of it I don't miss them at all...", "angry", "wide", "base", "stare")
            call her_main("I'm an awful daughter...", "angry", "narrow", "base", "down")

        elif one_of_ten == 6:
            call her_main("*Yawn*! I read about this technique that supposedly allows you to cut your sleep time in half...", "annoyed", "narrow", "annoyed", "up")
            call her_main("It don't think it's working though.... *Yawn*!", "annoyed", "narrow", "worried", "down")

        elif one_of_ten == 7:
            call her_main("Even after I graduate from Hogwarts I plan to keep on working hard.", "open", "closed", "angry", "mid")
            call her_main("If I give it my all I can make this world a better place, I know it!", "open", "base", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 8:
            call her_main("Somehow I have the feeling that this year will become a pivotal turning point in my life...", "open", "base", "worried", "mid")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 9:
            call her_main("Some of the less travelled school corridors are not very well lit and rather dusty...", "open", "closed", "angry", "mid")
            her "Please take care of this, sir..."
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 10:
            call her_main("I've read about this thing called \"Time-Turner\".", "open", "base", "base", "mid")
            her "It allows the user to control the flow of time..."
            call her_main("Having a device like that would do wonders for my schedule...", "open", "closed", "base", "mid")
            call her_main("", "annoyed", "squint", "base", "mid")


    ### WHORING LEVEL 04 ###
    if her_whoring >= 9 and her_whoring <= 11:
        if one_of_ten == 1:
            call her_main("My \"men's rights movement\" has been losing its popularity lately...", "open", "base", "worried", "mid")
            call her_main("It's as if people don't even care!", "annoyed", "narrow", "angry", "R")

        elif one_of_ten == 2:
            call her_main("Thank you for buying all those favours from me, sir.", "open", "closed", "angry", "mid")
            call her_main("Some of them were borderline inappropriate, sure...", "normal", "squint", "angry", "mid")
            call her_main("But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground.", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 3:
            call her_main("Quidditch is stupid!", "angry", "base", "angry", "mid")
            call her_main("There. I said it.", "annoyed", "squint", "base", "mid")

        elif one_of_ten == 4:
            call her_main("Sir, there is something about professor Snape that I think you should know...", "open", "base", "base", "mid")
            call her_main(".................", "open", "base", "worried", "R")
            call her_main(".........................", "annoyed", "squint", "angry", "mid")
            call her_main("*Ehm*... Never mind...", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 5:
            call her_main("Some of the Slytherin girls sell sexual favours almost openly these days...", "open", "closed", "angry", "mid")
            call her_main("You need to put an end to such practices, sir.", "open", "base", "base", "mid")
            call her_main("(I can barely keep up...)", "annoyed", "narrow", "angry", "R")

        elif one_of_ten == 6:
            call her_main("Life works in mysterious ways...", "open", "base", "worried", "R")
            call her_main("Wouldn't you agree, sir?", "open", "squint", "base", "mid")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 7:
            call her_main("Slytherins...", "angry", "base", "angry", "mid",emote="angry")
            call her_main("", "angry", "base", "angry", "mid")

        elif one_of_ten == 8:
            call her_main("I've been spending so much time in your office lately, sir...", "open", "base", "worried", "R")
            call her_main("If I'm not careful some people may think that I have become your pet...", "open", "base", "worried", "mid")
            call her_main("I meant to say the teacher's pet...", "angry", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "normal", "happyCl", "worried", "mid")

        elif one_of_ten == 9:
            call her_main("My favourite colours?", "open", "base", "base", "mid")
            call her_main("scarlet and gold of course!", "open", "base", "base", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 10:
            call her_main("Is it weird that my best friends are boys?", "open", "base", "worried", "R")
            call her_main("", "base", "base", "base", "mid")


    ### WHORING LEVEL 05 ###
    if her_whoring >= 12 and her_whoring <= 14:
        if one_of_ten == 1:
            call her_main("Sir, with all due respect...", "normal", "squint", "angry", "mid")
            her "Professor Snape's debauchery is getting out of hand!"
            call her_main("You must do something, sir.", "open", "base", "worried", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 2:
            call her_main("I am willing to go to great lengths to insure the superiority of my house...", "open", "closed", "angry", "mid")
            her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir."
            call her_main("{size=-4}(Like some sort of prostitute-witch...){/size}", "angry", "narrow", "base", "down")

        elif one_of_ten == 3:
            call her_main("What will it be today, sir?", "annoyed", "narrow", "annoyed", "mid")

        elif one_of_ten == 4:
            call her_main("lately I have not been studying nearly as much as I used to...", "open", "base", "worried", "mid")
            call her_main("Am I losing my motivation?", "open", "base", "worried", "R")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 5:
            call her_main("My least favourite subject?", "open", "squint", "base", "mid")
            call her_main("Divination.", "annoyed", "squint", "angry", "mid")

        elif one_of_ten == 6:
            call her_main("My father used to say: \"Magic is just science we don't understand yet\".", "open", "base", "base", "mid")
            call her_main("He couldn't be more wrong of course...", "open", "base", "worried", "R")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 7:
            call her_main("Despite everything...", "open", "closed", "angry", "mid")
            call her_main("I am thankful that you keep on buying favours from me, sir...", "open", "base", "worried", "R")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 8:
            call her_main("It's quite cold outside today, isn't it?", "open", "base", "base", "mid")
            call her_main("", "soft", "base", "base", "mid")

        elif one_of_ten == 9:
            call her_main("The \"Autumn Ball\" will be soon...", "open", "base", "base", "mid")
            call her_main("", "soft", "base", "base", "mid")

        elif one_of_ten == 10:
            call her_main("People hardly show up for my \"men's rights movement\" meetings at all anymore...", "open", "base", "worried", "R")
            call her_main("", "soft", "base", "base", "R")


    ### WHORING LEVEL 06 ###
    if her_whoring >= 15 and her_whoring <= 17:
        if one_of_ten == 1:
            call her_main("Would you like me to show you my breasts today, sir?", "open", "narrow", "worried", "down")
            call her_main("Yes... I would willingly expose myself to you, professor...", "base", "narrow", "base", "up")
            call her_main("That's how selfless I am!", "annoyed", "narrow", "annoyed", "mid")

        elif one_of_ten == 2:
            call her_main("I can't help but feel bad for the house elves who do my laundry...", "open", "base", "base", "mid")
            call her_main("I mean, all those dreadful semen stains...", "open", "narrow", "worried", "down")
            call her_main("", "angry", "narrow", "base", "down")

        elif one_of_ten == 3:
            call her_main("it Doesn't matter how many times you ask me this, sir...", "open", "base", "base", "mid")
            her "The answer shall remain the same..."
            call her_main("I have nothing but resentment for the Slytherins!", "angry", "base", "angry", "mid")
            call her_main("", "annoyed", "narrow", "angry", "R")

        elif one_of_ten == 4:
            call her_main("When I think about all the favours I sold you over these last months, sir...", "open", "base", "base", "mid")
            call her_main("Although I do feel a little bit embarrassed...", "open", "narrow", "worried", "down")
            call her_main("I also feel very proud of myself.", "upset", "closed", "base", "mid")

        elif one_of_ten == 5:
            call her_main("I still dedicate a lot of my time to studying...", "open", "base", "base", "mid")
            her "But not nearly as much of it as I used to..."
            call her_main("Somehow I just don't enjoy studying at all anymore...", "open", "base", "worried", "mid")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 6:
            call her_main("Gryffindor shall get the house cup this year!", "open", "closed", "angry", "mid")
            call her_main("{size=-4}(Even if it should cost me my dignity...){/size}", "angry", "narrow", "base", "down")
            call her_main("", "upset", "closed", "base", "mid")

        elif one_of_ten == 7:
            call her_main("I don't mind the autumn weather...", "open", "base", "base", "mid")
            call her_main("But my favourite season is winter.", "open", "closed", "base", "mid")
            call her_main("", "soft", "base", "base", "mid")

        elif one_of_ten == 8:
            call her_main("I used to look down on girls who spend too much time with worrying about the way they look...", "open", "base", "base", "mid")
            her "But I was wrong to do so..."
            her "I am starting to understand how important it really is for a girl to look pretty."
            call her_main("...............", "annoyed", "base", "worried", "R")
            call her_main("I've been on a diet lately...", "angry", "wink", "base", "mid")
            call her_main("", "angry", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "normal", "happyCl", "worried", "mid")

        elif one_of_ten == 9:
            call her_main("Lately I've been feeling rather confident around the boys...", "open", "base", "base", "mid")
            call her_main("I think I have you to thank for that, sir.", "base", "base", "base", "mid")

        elif one_of_ten == 10:
            call her_main("My favourite subject?", "open", "base", "base", "mid")
            call her_main("*Hmm*...", "soft", "base", "base", "R")
            call her_main("I suppose that would be \"charms\"...", "open", "base", "base", "mid")
            call her_main("", "soft", "base", "base", "mid")


    ### WHORING LEVEL 07 ###
    if her_whoring >= 18 and her_whoring <= 20:
        if one_of_ten == 1:
            call her_main("Just let me know what will be required of me today, sir.", "open", "closed", "angry", "mid")
            call her_main("", "normal", "base", "base", "mid")

        elif one_of_ten == 2:
            call her_main("I barely study at all anymore...", "open", "base", "worried", "mid")
            her "Despite that my popularity among the other students seems to be growing..."
            call her_main("*Hmm*...", "soft", "base", "base", "R")

        elif one_of_ten == 3:
            call her_main("I wouldn't say \"no\" to a bottle of butterbeer right about now...", "smile", "narrow", "base", "mid_soft")
            call her_main("", "grin", "base", "base", "R")

        elif one_of_ten == 4:
            call her_main("What is it sir? Do you have another present for me?", "base", "base", "base", "mid")
            call her_main("Oh... I see...", "annoyed", "narrow", "angry", "R")

        elif one_of_ten == 5:
            call her_main("I am doing well, thank you for asking.", "base", "base", "base", "mid")

        elif one_of_ten == 6:
            call her_main("Do I look fat to you sir?", "open", "base", "worried", "mid")
            call her_main("I wonder if the diet is working...", "annoyed", "base", "worried", "R")

        elif one_of_ten == 7:
            call her_main("I remember that I used to say that books were my friends...", "open", "closed", "base", "mid")
            call her_main("Now that sounds so lame.", "grin", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "soft", "base", "base", "mid")

        elif one_of_ten == 8:
            call her_main("Add Ashwinder's egg to cauldron...", "open", "closed", "angry", "mid")
            her "Then add horseshoe reddish and heat..."
            her "Then juice a squill bulb..."
            call her_main("Or was it a dash of thyme first?", "open", "base", "worried", "R")
            call her_main("..............", "soft", "base", "base", "R")
            call her_main("Oh, who cares?", "grin", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 9:
            call her_main("Do You think I am wearing enough make-up, sir?", "open", "base", "base", "mid")
            her "Wearing too much would look vulgar..."
            call her_main("But wearing too little would make me look plain...", "soft", "base", "base", "R")
            call her_main("I don't want to look plain!", "annoyed", "narrow", "angry", "R")

        elif one_of_ten == 10:
            call her_main("Would you like to see my tits today, sir?", "smile", "narrow", "base", "mid_soft")
            call her_main("Twenty-five house points, please.", "smile", "base", "angry", "mid")
            call her_main("", "upset", "closed", "base", "mid")


    ### WHORING LEVEL 08+ ###
    if her_whoring == 21:
        if one_of_ten == 1:
            call her_main("Do You have any adult magazines you don't need, sir?", "open", "base", "base", "R",cheeks="blush")
            call her_main("", "base", "base", "base", "R",cheeks="blush")

        elif one_of_ten == 2:
            call her_main("If you need anything [genie_name], just ask okay?", "open", "base", "base", "mid")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 3:
            call her_main("It's been getting so cold lately...", "open", "base", "base", "mid")
            call her_main("I hope it's going to start snowing soon...", "base", "base", "base", "mid")

        elif one_of_ten == 4:
            call her_main("Jump and scream for the Gryffindor team!", "open", "closed", "base", "mid")
            call her_main("So daring and bold, sporting red and gold!", "smile", "happyCl", "base", "mid",emote="happy")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 5:
            call her_main("I hope the ball goes smoothly...", "open", "base", "worried", "R")
            call her_main("", "soft", "base", "base", "R")

        elif one_of_ten == 6:
            call her_main("I wonder what Ginny is going to wear for the ball...", "base", "base", "base", "mid")

        elif one_of_ten == 7:
            call her_main("Considering the nature of the favours you keep buying from me sir...", "open", "closed", "base", "mid")
            call her_main("I seldom bother to put on underwear at all anymore...", "open", "base", "worried", "mid")

        elif one_of_ten == 8:
            call her_main("Sir, could you put your penis in my mouth?", "angry", "base", "base", "mid")
            call her_main("Sir, I am begging you...", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("Fifty-five points, please!", "smile", "base", "angry", "mid")
            call her_main("", "angry", "wink", "base", "mid")

        elif one_of_ten == 9:
            call her_main("I have read this one article about the positive effects of semen on a woman's skin...", "open", "closed", "base", "mid")
            call her_main("I wonder where their information is coming from...", "base", "narrow", "base", "mid_soft")
            call her_main("Did the magazine conduct research of some sort?", "angry", "wink", "base", "mid")
            call her_main("", "base", "narrow", "base", "mid_soft")

        elif one_of_ten == 10:
            call her_main("It goes like this...", "open", "closed", "base", "mid")
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            call her_main("And Slytherin is not even on the list!", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("", "upset", "closed", "base", "mid")

    if her_whoring >= 22:
        if one_of_ten == 1:
            call her_main("If you ever need some \"help\", sir, please let me know.", "open_wide_tongue", "base", "base", "R",cheeks="blush")
            ">She suggestively jerks her hand"
            call her_main("", "base", "base", "base", "R",cheeks="blush")

        elif one_of_ten == 2:
            call her_main("I am sorry to bother you with this, sir...", "open", "base", "base", "mid")
            her "But do you have any condoms?"
            call her_main("Sadly the ones I've bought are already gone...", "annoyed", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "base", "base", "base", "R")

        elif one_of_ten == 3:
            call her_main("It's been getting so cold lately...", "open", "base", "base", "mid")
            call her_main("I hope it's going to start snowing soon...", "base", "base", "base", "mid")
            call her_main("You will let me wear a coat at least right?", "angry", "happyCl", "worried", "mid",emote="sweat")
            call her_main("", "base", "narrow", "base", "mid_soft")

        elif one_of_ten == 4:
            call her_main("Jump and scream for the Gryffindor team!", "open", "closed", "base", "mid")
            call her_main("So daring and bold, sporting red and gold!", "smile", "happyCl", "base", "mid",emote="happy")
            call her_main("", "base", "base", "base", "mid")

        elif one_of_ten == 5:
            call her_main("Sir, I have a favour to ask...", "base", "base", "worried", "mid")
            call her_main("Could help me with the dress later, sir?", "base", "base", "base", "R")
            call her_main("I could use some of your... insight", "soft", "narrow", "base", "mid_soft",cheeks="blush")
            call her_main("", "base", "narrow", "base", "mid_soft")

        elif one_of_ten == 6:
            call her_main("I can't believe I was such a prude before.", "angry", "base", "worried", "mid")
            call her_main("Meeting you was the best thing that has happened to me, sir.", "smile", "narrow", "base", "mid_soft")
            call her_main("", "base", "narrow", "base", "mid_soft")

        elif one_of_ten == 7:
            call her_main("Considering the nature of the favours you keep buying from me sir...", "open", "closed", "base", "mid")
            call her_main("I seldom bother to put on underwear at all anymore...", "open", "base", "worried", "mid")
            call her_main("(Not that I complain anyway..)", "soft", "narrow", "annoyed", "up")

        elif one_of_ten == 8:
            call her_main("Sir, could you put your penis in my mouth?", "angry", "base", "base", "mid")
            call her_main("Sir, I am begging you...", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("Fifty-five points, please!", "smile", "base", "angry", "mid")
            call her_main("(Although I wouldn't mind doing it for free..).", "smile", "narrow", "annoyed", "up")

        elif one_of_ten == 9:
            call her_main("Remember when I told you about this one article...", "open", "closed", "base", "mid")
            her "It was about the positive effects of semen on a woman's skin."
            call her_main("I tested it recently...", "base", "narrow", "base", "mid_soft")
            call her_main("And it actually works!", "smile", "narrow", "base", "mid_soft")
            call her_main("My skin definitely is getting softer.", "smile", "closed", "base", "mid")
            call her_main("", "base", "narrow", "base", "mid_soft")

        elif one_of_ten == 10:
            call her_main("It goes like this...", "open", "closed", "base", "mid")
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            call her_main("And Slytherin is not even on the list!", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("", "upset", "closed", "base", "mid")
    return
