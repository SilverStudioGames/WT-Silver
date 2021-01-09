
# Hermione Gift Responses

label give_her_gift(gift_item):
    hide screen hermione_main
    with d5
    call her_main(xpos="mid",ypos="base",trans=d5)

    $ gave_hermione_gift = True

    if gift_item == lollipop_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A lollipop?", "base", "base", "base", "mid")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-5)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Candy?", "normal", "base", "base", "mid")
            call her_main("Candy is for kids, [genie_name].", "open", "base", "base", "mid")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you...", "annoyed", "base", "worried", "R")
            call her_mood(-5)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Candy?", "normal", "base", "base", "mid")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("*Ehm*... Sure, thanks...", "open", "squint", "base", "mid")
            call her_mood(-5)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A lollipop?", "base", "base", "base", "mid")
            call her_main("Clever girls use candy like this as a \"weapon\".", "smile", "base", "base", "R")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
            call her_mood(-5)

    elif gift_item == chocolate_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A chocolate bar?", "base", "base", "base", "mid")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-10)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A chocolate bar?", "normal", "base", "base", "mid")
            call her_main("*Hmm*...", "annoyed", "squint", "angry", "mid")
            call her_main("That thing about fairies...")
            call her_main("That is a joke of some sort, right?", "open", "base", "worried", "mid")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you...", "soft", "base", "base", "mid")
            call her_mood(-10)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A chocolate bar?", "normal", "base", "base", "mid")
            call her_main("I just like the way it crunches, [genie_name]! N-not the taste...", "grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("*Ehm*... Sure, thanks...", "base", "base", "base", "mid")
            call her_mood(-10)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A chocolate bar?", "base", "base", "base", "mid")
            call her_main("You spoil me, [genie_name].", "smile", "base", "angry", "mid")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you.", "base", "squint", "base", "mid")
            call her_mood(-10)

    elif gift_item == plush_owl_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A stuffed owl?", "base", "base", "base", "mid")
            call her_main("It's cute...", "base", "base", "base", "mid")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-7)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A plush toy?", "open", "base", "worried", "mid")
            call her_main("I like it!", "base", "base", "base", "mid")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-10)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A toy?", "base", "base", "base", "mid")
            call her_main("Toys are for kids, [genie_name].", "open", "base", "base", "mid")
            call her_main("But I'll take it...", "annoyed", "base", "worried", "R")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-15)
        elif her_whoring >= 18: # Lv 7+
            call her_main("This is one of those adult toys isn't it?", "disgust", "narrow", "base", "mid_soft")
            call her_main("There's got to be a switch or a button somewhere...", "open", "narrow", "worried", "down")
            call her_main("So... Does it vibrate or something?", "base", "narrow", "worried", "down")
            call her_main("Oh...?", "open", "happy", "base", "mid",cheeks="blush")
            call her_main("So it is really just a plush toy then?")
            call her_main("Shame...", "angry", "narrow", "base", "down")
            call her_main("I mean, thank you, [genie_name].", "angry", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_mood(-4)

    elif gift_item == butterbeer_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Butterbeer?", "base", "base", "base", "mid")
            call her_main("Are you sure about that, [genie_name]?", "open", "squint", "base", "mid")
            call her_main("It does contain alcohol, you know...", "base", "base", "base", "mid")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("Thank you.", "base", "base", "base", "mid")
            call her_mood(-3)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Butterbeer, [genie_name]?", "open", "base", "worried", "mid")
            call her_main("To let you in on a little secret, [genie_name]...", "open", "base", "base", "mid")
            call her_main("I'm a big fan of this completely harmless beverage.", "base", "base", "base", "mid")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-10)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Butterbeer?", "base", "base", "base", "mid")
            call her_main("Thank you, [genie_name].", "grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("I shall drink this with the girls later.", "base", "base", "base", "mid")
            call her_mood(-15)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Butterbeer...?", "base", "base", "base", "mid")
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("I shall drink this later with the boys.", "base", "base", "base", "mid")
            call her_main("Err... I meant to say with the girls, of course.", "open", "base", "base", "R",cheeks="blush")
            call her_mood(-20)

    elif gift_item == science_mag_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("\"Popular magic\" magazines?", "base", "base", "base", "mid")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!", "base", "base", "base", "mid")
            call her_main("I will use them for my research!")
            call her_mood(-15)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Sometimes I find information in magazines that I could never find in a book...", "base", "base", "base", "mid")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!", "base", "base", "base", "mid")
            call her_main("I will use them for my research!")
            call her_mood(-10)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Oh...", "open", "base", "base", "mid")
            call her_main("Yes, I used to read magazines like that a lot...", "base", "base", "base", "mid")
            call her_main("Lately not so much though...", "open", "base", "worried", "R")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!", "base", "base", "base", "mid")
            call her_mood(-3)
        elif her_whoring >= 18: # Lv 7+
            call her_main("*Ehm*...", "open", "base", "worried", "R")
            call her_main("To be honest, magazines like that lost their appeal to me completely lately...", "open", "squint", "base", "mid")
            call her_main("But I don't mind taking them off you hands anyway, [genie_name].", "open", "base", "worried", "mid")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you.", "soft", "base", "base", "R")
            call her_mood(0)

    elif gift_item == girls_mag_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("*Hmm*?", "soft", "base", "base", "mid")
            call her_main("This is the sort of press some Slytherin bimbo would appreciate.", "annoyed", "squint", "base", "mid")
            call her_main("I am way above silly magazines like that, [genie_name].", "open", "closed", "base", "mid")
            call her_mood(0)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("I don't read magazines of that nature, [genie_name]...", "open", "closed", "angry", "mid")
            call her_main("................", "soft", "base", "base", "R")
            call her_main("But I could give it a try just to humour you I suppose...", "open", "closed", "angry", "mid")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!", "open", "squint", "base", "mid")
            call her_mood(-5)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("I ashamed to admit this, but...", "open", "base", "worried", "R")
            call her_main("I really enjoy reading magazines like that lately...", "grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "open", "squint", "base", "mid")
            call her_mood(-15)
        elif her_whoring >= 18: # Lv 7+
            call her_main("The Latest edition of \"Girlz\"?!", "angry", "wide", "base", "stare")
            call her_main("I can't have enough of that brilliant magazine!", "grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "open", "squint", "base", "mid")
            call her_mood(-15)

    elif gift_item == adult_mag_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Are that...?", "open", "base", "base", "mid")
            call her_main("Adult magazines, [genie_name]?", "open", "base", "base", "mid")
            call her_main("Given to me by An esteemed wizard of your status?", "annoyed", "narrow", "angry", "R")
            call her_main("[genie_name], surely you could find a more productive way to spend your free time.", "disgust", "narrow", "base", "mid_soft")
            call her_main("And I most definitely would not have use for those...", "angry", "base", "angry", "mid")
            call her_mood(7)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Adult magazines?", "angry", "base", "angry", "mid")
            call her_main("[genie_name], I have no interest in things like that.", "annoyed", "narrow", "angry", "R")
            call her_main("And how is this an appropriate present for one of your students, [genie_name]?", "angry", "base", "angry", "mid")
            call her_mood(3)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Adult magazines?", "open", "base", "base", "mid")
            call her_main("[genie_name], this is such an inappropriate present for a girl like me...", "angry", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_item)
            call her_main("I shall throw these away myself...", "annoyed", "narrow", "annoyed", "mid")
            call her_mood(-8)
        elif her_whoring >= 18: # Lv 7+
            call her_main("The New edition of \"L.o.v.e.\"!!!", "smile", "happyCl", "base", "mid")
            call her_main("Err.. I mean, adult magazines?", "angry", "wink", "base", "mid")
            call her_main("This is a little inappropriate...")
            call her_main("But I will take them...", "base", "happyCl", "base", "mid")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_item)
            call her_main("thank you, [genie_name].", "base", "happyCl", "base", "mid")
            call her_mood(-15)

    elif gift_item == porn_mag_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("*Hmm*... What is this?", "base", "base", "base", "mid")
            call her_main("[genie_name], those are porn magazines!", "scream", "wide", "base", "stare")
            call her_main("Shame on you, [genie_name]!", "angry", "base", "angry", "mid",cheeks="blush")
            call her_mood(15)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Porn magazines?", "shock", "wide", "base", "stare")
            call her_main("[genie_name], what do you expect me to do with those?", "open", "narrow", "worried", "down")
            call her_main("Research them?", "annoyed", "narrow", "annoyed", "mid")
            call her_main("Despicable!", "scream", "base", "angry", "mid",emote="angry")
            call her_mood(8)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("That's hardcore porn, [genie_name].", "open", "base", "base", "mid")
            call her_main("Which is a completely inappropriate gift for a girl like me!", "angry", "happyCl", "worried", "mid",emote="sweat")
            call her_main("..............", "angry", "narrow", "base", "down")
            call her_main("But I will take them...", "angry", "base", "base", "mid")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_item)
            call her_main("And I shall throw them in the trash, where they and... girls who like these things belong...", "annoyed", "narrow", "annoyed", "mid")
            call her_mood(0)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Pornography?", "shock", "wide", "base", "stare")
            call her_main("................", "angry", "narrow", "base", "down")
            call her_main("How can women even agree to do things like that, [genie_name]?", "angry", "base", "base", "mid")
            call her_main(".................", "angry", "narrow", "base", "down")
            call her_main("Alright, I shall accept them...", "upset", "closed", "base", "mid")
            call her_main("Solely for research purposes of course...", "open", "base", "base", "R",cheeks="blush")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == krum_poster_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A Quidditch poster?", "annoyed", "narrow", "worried", "down")
            call her_main("What am I supposed to do with it, [genie_name]?", "annoyed", "narrow", "annoyed", "mid")
            call her_main("No, thank you.", "annoyed", "closed", "base", "mid")
            call her_mood(0)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A Quidditch poster?", "annoyed", "narrow", "worried", "down")
            call her_main("*Hmm*...", "annoyed", "narrow", "annoyed", "mid")
            call her_main("I think I saw this player once or twice...", "annoyed", "narrow", "worried", "down")
            call her_main("He is that Durmstrang student, right?", "base", "base", "base", "mid")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call her_mood(-5)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A Viktor Krum poster, [genie_name]?", "annoyed", "narrow", "worried", "down")
            call her_main("Can't say that I care much for Quidditch, but...", "open", "squint", "base", "mid")
            call her_main("I can see why the girls find the brutish physique of some players appealing...", "open", "narrow", "worried", "down")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call her_mood(-15)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A Viktor Krum poster?!", "scream", "wide", "base", "mid")
            call her_main("Thank you, [genie_name]!", "grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call her_main("Can't wait to hang it over my bed!", "smile", "base", "base", "R")
            call her_main("The girls will go green with envy...", "smile", "narrow", "base", "mid_soft")
            call her_mood(-25)

    elif gift_item == sexy_lingerie_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("lingerie?", "angry", "narrow", "base", "down")
            call her_main("[genie_name], I cannot accept a gift like this from you...", "upset", "closed", "base", "mid")
            call her_mood(10)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("sexy lingerie?", "angry", "narrow", "base", "down")
            call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].", "angry", "base", "base", "mid")
            call her_main("(It's pretty though).........", "angry", "narrow", "base", "down")
            call her_mood(0)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("sexy lingerie?", "base", "narrow", "worried", "down")
            call her_main("[genie_name] that is so inappropriate...", "angry", "wink", "base", "mid")
            call give_gift(">You give the lingerie to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "R",cheeks="blush")
            call her_mood(-7)
        elif her_whoring >= 18: # Lv 7+
            call her_main("sexy lingerie?", "base", "narrow", "worried", "down")
            call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?", "grin", "narrow", "base", "dead")
            call her_main("Oh... I mean, thank you, [genie_name].", "angry", "wink", "base", "mid")
            call give_gift(">You give the lingerie to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == sexy_stockings_ITEM :
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Stockings?", "base", "narrow", "worried", "down")
            call her_main("[genie_name], are you insinuating that I wear these?", "angry", "closed", "base", "mid")
            call her_mood(8)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Sexy stockings?", "angry", "narrow", "base", "down")
            call her_main("Isn't this a bit inappropriate, [genie_name]?", "annoyed", "base", "base", "mid")
            call her_mood(0)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Sexy stockings?", "base", "narrow", "worried", "down")
            call her_main("Thank you I guess...", "base", "wink", "base", "mid",cheeks="blush")
            call give_gift(">You give the stockings to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "R",cheeks="blush")
            call her_mood(-8)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Sexy stockings?", "base", "narrow", "worried", "down")
            call her_main("These are almost completely transparent, [genie_name]!", "grin", "wide", "base", "mid")
            call give_gift(">You give the stockings to Hermione...",gift_item)
            call her_mood(-10)

    elif gift_item == pink_condoms_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Condoms?!", "angry", "wide", "base", "stare")
            call her_main("[genie_name], I wouldn't even know what to do with them...", "scream", "closed", "angry", "mid")
            call her_mood(6)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("... Condoms?", "normal", "squint", "angry", "mid")
            call her_main("*Ehm*... Is this a part of some new Hogwarts sex ed program or something?", "open", "closed", "angry", "mid")
            call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...", "open", "base", "base", "R",cheeks="blush")
            call her_mood(0)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A pack of condoms?", "normal", "base", "base", "mid")
            call her_main("[genie_name], what possible use could I have for those?")
            call her_main("Well, I shall accept them simply because it is rude to refuse a gift...", "open", "closed", "angry", "mid")
            call give_gift(">You give a pack of condoms to Hermione...", gift_item)
            call her_mood(-3)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A pack of condoms?", "open", "squint", "base", "mid")
            call her_main("I appreciate your concern, [genie_name]. Thank you.", "base", "narrow", "base", "mid_soft")
            call give_gift(">You give a pack of condoms to Hermione...", gift_item)
            call her_mood(-4)

    elif gift_item == vibrator_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A magic wand?", "base", "base", "base", "mid")
            call her_main("No, it doesn't look like--", "soft", "base", "base", "mid")
            call her_main(".........?")
            call her_main("!!!", "angry", "wide", "base", "stare")
            call her_main("[genie_name]!", "angry", "base", "angry", "mid",cheeks="blush")
            call her_main("This is just beyond inappropriate!", "scream", "closed", "angry", "mid")
            call her_mood(10)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Is this what I think it is?", "angry", "narrow", "base", "down")
            call her_main("[genie_name], let me remind you that I belong to the noble house of Gryffindor.", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("A present like that would be appropriate for a girl from Slytherin, [genie_name].", "upset", "closed", "base", "mid")
            call her_mood(10)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Is that a... vibrator?", "angry", "narrow", "base", "down")
            call her_main("The design...")
            call her_main("it reminds me of my wand...")
            call her_main("Did you have this custom made for me [genie_name]?", "angry", "narrow", "base", "down")
            call her_main("This is inappropriate...", "scream", "closed", "angry", "mid")
            call her_main("But I shall take it nonetheless...", "annoyed", "base", "worried", "R")
            call give_gift(">You give the vibrator to Hermione...",gift_item)
            call her_mood(0)
        elif her_whoring >= 18: # Lv 7+
            call her_main("This vibrator...", "open", "base", "worried", "mid")
            call her_main("It's... calling out for me...", "open", "base", "worried", "R")
            call her_main("But not in a dirty way, [genie_name].", "disgust", "narrow", "base", "mid_soft")
            call give_gift(">You give the vibrator to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == anal_lube_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("I don't know what this is...", "open", "base", "base", "mid")
            call her_main("But I have the feeling that the jar is full of something vile and inappropriate...", "angry", "base", "angry", "mid")
            call her_main("No, thank you, [genie_name].")
            call her_mood(6)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("*Hmm*...", "annoyed", "narrow", "worried", "down")
            call her_main("I think I know what this is...", "disgust", "narrow", "base", "mid_soft")
            call her_main("But why would you give something like this to one of your pupils, [genie_name]?")
            call her_main("No, thank you.", "annoyed", "narrow", "angry", "R")
            call her_mood(2)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Anal lubricant?", "angry", "narrow", "base", "down")
            call her_main("*Ehm*.. well... I know this girl...", "open", "base", "base", "R",cheeks="blush")
            call her_main("I mean I don't know her, she is a friend of a friend...")
            call her_main("Yes, I will take this for her...")
            call give_gift(">You give the jar to Hermione...",gift_item)
            call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_mood(0)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Anal lubricant, [genie_name]?", "base", "narrow", "worried", "down")
            call her_main("I know a couple of girls who would do anything for a commodity like that.", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("Thank for looking out for us, [genie_name].", "base", "narrow", "base", "mid_soft")
            call give_gift(">You give the jar to Hermione...",gift_item)
            call her_mood(-5)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("What is this?", "angry", "narrow", "base", "down")
            call her_main("Is this like one of those adult toys?", "angry", "squint", "base", "mid",cheeks="blush")
            call her_main("What woman in her right mind would subject herself to a humiliation like that?", "scream", "closed", "angry", "mid")
            call her_main("And what possible use could I have for such objects?", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("This is just insulting, [genie_name]...", "angry", "base", "angry", "mid",cheeks="blush")
            call her_mood(10)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], do you not realise how inappropriate it would be for me to accept a present like that?", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("And I would not even know what to do with them anyway...", "open", "base", "base", "R",cheeks="blush")
            call her_main("I mean these fluffy things are obviously handcuffs...", "angry", "narrow", "base", "down")
            call her_main("But this ball... *ehm*...")
            call her_main("[genie_name], please...", "upset", "closed", "base", "mid")
            call her_main("Just put them away.")
            call her_mood(5)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A month ago I would've felt insulted to receive a gift like this...", "upset", "closed", "base", "mid")
            call her_main("But by now I know that some girls really do find pleasure in toys like...", "angry", "narrow", "base", "down")
            call her_main("But I assure you that I am not one of them, [genie_name].", "upset", "closed", "base", "mid")
            call her_main("But I know a girl who knows a girl who is into things like...", "open", "base", "base", "R",cheeks="blush")
            call her_main("Yes, I shall take these to her...", "base", "base", "base", "R",cheeks="blush")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_item)
            call her_mood(-9)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A ball gag and handcuffs?", "open", "happy", "base", "mid",cheeks="blush")
            call her_main("This is completely inappropriate, [genie_name].", "angry", "wink", "base", "mid") # :)
            call her_main("But a gift is a gift, right?", "base", "squint", "base", "mid")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == anal_plugs_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("*Hmm*...?", "base", "base", "base", "mid")
            call her_main("Are those like key chain toys?", "soft", "base", "base", "mid")
            call give_gift(">You give the anal plugs to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
            call her_mood(-8)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("those are some of those anal things, aren't they?", "angry", "base", "angry", "mid",cheeks="blush")
            call her_main("[genie_name] this is nothing but a weapon meant to oppress women!")
            call her_main("Despicable!", "upset", "closed", "base", "mid")
            call her_mood(15)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Yes, I know that some girls have *uhm*...", "upset", "closed", "base", "mid")
            call her_main("Have use for things such as these...", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("But not me, [genie_name].")
            call her_main("No, thank you.", "upset", "closed", "base", "mid")
            call her_mood(0)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Anal plugs?", "angry", "narrow", "base", "down")
            call her_main("I have no use for things like that, [genie_name]...", "angry", "base", "base", "mid")
            call her_main("They are so pretty though...", "angry", "wink", "base", "mid")
            call her_main(".....................", "angry", "narrow", "base", "down")
            call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].", "soft", "narrow", "annoyed", "up")
            call give_gift(">You give the anal plugs to Hermione...",gift_item)
            call her_main("But I shall never use them of course...", "open", "closed", "base", "mid")
            call her_main("................", "base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == testral_strapon_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("What is that?", "angry", "wide", "base", "stare")
            call her_main("An artefact of some sort or a trophy?", "open", "base", "base", "mid")
            call her_main("So well-crafted...", "base", "base", "base", "mid")
            call her_main("Are you sure that it's alright for me to have it, [genie_name]?", "base", "base", "base", "mid")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call her_main("Thank you very much, [genie_name]. I promise to take good care of it.", "open", "closed", "base", "mid")
            call her_mood(-20)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("!!!", "angry", "wide", "base", "stare")
            call her_main("That is...", "angry", "narrow", "base", "down")
            call her_main("But it doesn't even look... human...")
            call her_main("I mean...", "annoyed", "narrow", "angry", "R")
            call her_main("[genie_name], do you have no shame?!", "scream", "base", "angry", "mid",emote="angry")
            call her_main("Presenting a thing like that to a pupil?!")
            call her_main("..................", "open", "narrow", "worried", "down")
            call her_main("Please put it away, [genie_name].", "angry", "base", "angry", "mid")
            call her_mood(15)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("That thing...", "angry", "narrow", "base", "down")
            call her_main("Is that the actual size of the... of the real \"thing\"?", "angry", "base", "base", "mid")
            call her_main("I mean...", "open", "base", "base", "R",cheeks="blush")
            call her_main(".......................", "angry", "narrow", "base", "down")
            call her_main("Is this like a party prank prop?", "angry", "base", "base", "mid")
            call her_main("It's so well-crafted though...", "angry", "narrow", "base", "down")
            call her_main("I will take it...", "normal", "happyCl", "worried", "mid")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call her_mood(-10)
        elif her_whoring >= 18: # Lv 7+
            call her_main("It's... It's magnificent, [genie_name]...", "shock", "wide", "base", "stare")
            call her_main("Is it really modelled after a thestral?", "open", "base", "base", "R",cheeks="blush")
            call her_main("But the creatures are invisible...", "open", "happy", "base", "mid",cheeks="blush")
            call her_main("..................", "angry", "narrow", "base", "down")
            call her_main("Breathtaking...", "grin", "narrow", "base", "dead")
            call her_main("Not in the way you think, [genie_name]...", "upset", "closed", "base", "mid")
            call her_main("I am merely admiring the craftsmanship...", "open", "closed", "base", "mid")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call her_main("Thank you for the gift, [genie_name].", "base", "squint", "base", "mid")
            call her_mood(-30)

    elif gift_item == broom_2000_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A broom...?", "base", "base", "base", "mid")
            call her_main("*Hmm*...", "normal", "base", "base", "mid")
            call her_main("What is that silly-looking thing attached to it?", "normal", "squint", "angry", "mid")
            call her_main("Is it like a saddle...?", "open", "squint", "base", "mid")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you for the gift, [genie_name].", "open", "base", "worried", "mid")
            call her_mood(-20)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A broom...?", "base", "base", "base", "mid")
            call her_main("*Hmm*...", "normal", "squint", "angry", "mid")
            call her_main("It's a sex-toy of some sort, isn't it?", "angry", "base", "angry", "mid")
            call her_main("But it is so well crafted...", "open", "narrow", "worried", "down")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "upset", "closed", "base", "mid")
            call her_mood(-20)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A broom...?", "angry", "narrow", "base", "down")
            call her_main("*Hmm*...")
            call her_main("What kind of saddle is that...?", "disgust", "narrow", "base", "mid_soft")
            call her_main("Well, doesn't matter.", "open", "closed", "base", "mid")
            call her_main("Refusing an expensive gift like that would be rude...")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "upset", "closed", "base", "mid")
            call her_mood(-30)
        elif her_whoring >= 18: # Lv 7+
            call her_main("A broom...", "base", "narrow", "worried", "down")
            call her_main("*Hmm*...")
            call her_main("That saddle, [genie_name]...", "open", "base", "base", "R",cheeks="blush")
            call her_main("It was designed especially for witches, was it not?", "open", "happy", "base", "mid",cheeks="blush")
            call her_main("I am not sure whether this is inappropriate or clever...", "annoyed", "narrow", "annoyed", "mid")
            call her_main("But this is a brilliant piece of engineering either way...", "base", "squint", "base", "mid")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")
            call her_mood(-30)

    elif gift_item == sexdoll_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Is this...", "shock", "wide", "base", "stare")
            call her_main("A sex doll?!", "angry", "happyCl", "worried", "mid",emote="sweat")
            call her_main("[genie_name]!!!", "scream", "happyCl", "worried", "mid")
            call her_mood(20)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A sex doll?", "shock", "wide", "base", "stare")
            call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...", "upset", "closed", "base", "mid")
            call her_mood(20)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A sex doll...", "angry", "narrow", "base", "down")
            call her_main("This is a little inappropriate...", "upset", "closed", "base", "mid")
            call her_main("But maybe we could use it for a prank or something...", "base", "narrow", "worried", "down")
            call give_gift(">You give the blow-up doll to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "narrow", "worried", "down")
            call her_mood(-10)
        elif her_whoring >= 18: # Lv 7+
            call her_main("the Joanne sex doll?", "annoyed", "narrow", "worried", "down")
            call her_main("I Can't say that I approve of this...", "open", "base", "base", "R",cheeks="blush")
            call her_main("But I know Harry would love to have a go at it...", "base", "narrow", "worried", "down")
            call give_gift(">You give the blow-up doll to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "R",cheeks="blush")
            call her_mood(-30)

    elif gift_item == anal_beads_ITEM:
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("*Hmm*...?", "base", "base", "base", "mid")
            call her_main("Is this a necklace?", "soft", "base", "base", "mid")
            call give_gift(">You give the anal beads to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            call her_mood(-8)
        elif her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("This is one of those butt... bead things, aren't they?", "angry", "base", "angry", "mid",cheeks="blush")
            call her_main("[genie_name] get them away from me!")
            call her_main("Gross!", "upset", "closed", "base", "mid")
            call her_mood(15)
        elif her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("That's not a necklace...", "upset", "closed", "base", "mid")
            call her_main("I wouldn't have any use for this...", "open", "narrow", "annoyed", "mid", cheeks="blush")
            call her_main("Thanks but no thanks [genie_name].", "upset", "closed", "base", "mid")
            call her_mood(0)
        elif her_whoring >= 18: # Lv 7+
            call her_main("Anal beads?", "angry", "narrow", "base", "down")
            call her_main("Obviously I don't need this sort of thing, [genie_name]...", "angry", "base", "base", "mid")
            call her_main("Although it's got a nice colour...", "angry", "wink", "base", "mid")
            call her_main(".....................", "angry", "narrow", "base", "down")
            call her_main("Fine, I'll use them as an armband, [genie_name].", "soft", "narrow", "annoyed", "up")
            call give_gift(">You give the anal beads to Hermione...",gift_item)
            call her_main("But I wont use them for their intended purpose...", "open", "closed", "base", "mid")
            call her_main("................", "base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == wine_ITEM or gift_item == firewhisky_ITEM:
        if her_whoring <= 6  and her_whoring <= 11:
            call her_main("[genie_name]?! Drinking alcohol on school grounds is forbidden..","open", "base", "angry", "mid")
            call her_main("And you as a headmaster should know it!", "upset", "base", "angry", "mid")
            call her_mood(10)
        elif her_whoring <= 12 and her_whoring <= 17:
            call her_main("But, [genie_name].. I can't drink alcohol.", "base", "narrow", "worried", "down")
            call her_main("I guess I could use it for some potion mixing though..", "open", "base", "base", "R")
            call give_gift(">You give the "+str(gift_item.name)+" bottle to Hermione...", gift_item)
            call her_main("", "base", "base", "base", "R")
            call her_mood(-5)
        elif her_whoring >= 18:
            call her_main("But, [genie_name].. You know I can't drink..","soft","base", cheeks="blush")
            call her_main("I get drunk too fast and I might do something I'll regret later.", "open", "base", "base", "R", cheeks="blush")
            call her_main("", "base", "base", "base", "R", cheeks="blush")
            call her_mood(0)
        else:
            call give_gift(">You give the "+str(gift_item.name)+" bottle to Hermione...", gift_item)
            call her_main("Thank you, [genie_name], I'll ask Ginny to drink some with me later.", "soft", "base", "base", "mid", cheeks="blush")
            call her_mood(-20)

    hide screen hermione_main
    with d5
    call her_main(xpos="base",ypos="base",trans=d5)

    $ renpy.jump_out_of_context("hermione_requests")

label her_mood(value=0):
    show screen blktone
    with d3

    if value > 0:
        if value == 1:
            "Hermione's mood worsened slightly."
        else:
            "Hermione's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Hermione's mood has improved slightly."
        else:
            "Hermione's mood has improved significantly."
    else:
        "Hermione's mood hasn't changed."

    $ was_negative = her_mood > 0
    $ her_mood = max(min(her_mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, her_mood, value)

    hide screen blktone
    return
