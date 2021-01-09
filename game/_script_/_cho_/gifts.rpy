### Give Cho Gift ###

label give_cho_gift(gift_item):
    $ gave_cho_gift = True

    if gift_item == lollipop_ITEM:
        if cho_tier <= 1:
            call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("My team captain hasn't let me buy any to keep my blood sugar balanced, whatever that means.",mouth="soft",face="annoyed")
            call give_gift(">You give the sweets to Cho...",gift_item)
            call cho_main("But thanks, [cho_genie_name].",face="neutral")
            call cho_mood(-2)
        elif cho_tier == 2:
            call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the sweets to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name] I do think I deserve one at least after winning our first match.","smile","base","base","L")
            call cho_mood(-2)
        elif cho_tier == 3:
            call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("But we're up against Gryffindor soon, I don't want to get addicted to sugar...",mouth="soft",face="annoyed")
            call give_gift(">You give the sweets to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].","smile","base","base","L")
            call cho_mood(-1)
        else:
            call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the sweets to Cho...",gift_item)
            call cho_main("I'll keep it for later, I like licking it in front of my teammates to tease them a bit.","open","base","raised","mid")
            call cho_main("*Mmmh*, but in the future... I'm more of a savoury kind of girl when it comes to sucking on things...","horny","wink","base","mid")
            call cho_main("But thanks, [cho_genie_name].","smile","base","base","L")
            call cho_mood(-1)

    elif gift_item == chocolate_ITEM:
        if cho_tier <= 1:
            call cho_main("Chocolate?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("I probably shouldn't... although.",pupils="R",face="horny")
            call give_gift(">You give the chocolate to Cho...",gift_item)
            call cho_main("I'll take it, [cho_genie_name]!",face="happy")
            call cho_mood(-2)
        elif cho_tier == 2:
            call cho_main("Chocolate... now that would be a treat...",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the chocolate to Cho...",gift_item)
            call cho_main("What the heck, I deserve it.","smile","base","base","L")
            call cho_main("Thank you, [cho_genie_name].","open","base","base","L")
            call cho_mood(-2)
        elif cho_tier == 3:
            call cho_main("Chocolate?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("But we're up against Gryffindor soon, I don't want to get addicted to sugar...",mouth="soft",face="annoyed")
            call give_gift(">You give the chocolate to Cho...",gift_item)
            call cho_main("Thanks","base","base","base","L")
            call cho_mood(-1)
        else:
            call cho_main("Chocolate?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the chocolate to Cho...",gift_item)
            call cho_main("YES!","smile","base","base","L")
            call cho_main("I've been trying to stay away from it but since the season is over I can have as much as I'd like...","open","wide","base","L")
            call cho_main("Within reason.","base","base","base","L")
            call cho_mood(-2)

    elif gift_item == plush_owl_ITEM:
        if cho_tier <= 1:
            call cho_main("A toy?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            call cho_main("My team would probably laugh if they saw me with this...",mouth="open",face="annoyed")
            call cho_main("I guess it's cute...",face="annoyed")
            call cho_mood(0)
        elif cho_tier == 2:
            call cho_main("A toy?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            call cho_main("That's very nice of you [cho_genie_name] but I'd probably be made fun of owning this...","annoyed","base","base","mid")
            call cho_main("I guess I could give it to someone.","open","base","base","down")
            call cho_mood(0)
        elif cho_tier == 3:
            call cho_main("A toy?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            call cho_main("I'm not a child [cho_genie_name]...","annoyed","base","base","mid")
            call cho_main("Thank you I guess...","open","base","base","down")
            call cho_mood(0)
        else:
            call cho_main("A toy?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            call cho_main("Not the kind of Toy I'd like...", "horny", "narrow", "raised", "mid")
            call cho_main("Thank you I suppose.","annoyed","base","base","mid")
            call cho_mood(0)

    elif gift_item == butterbeer_ITEM:
        if cho_tier <= 1:
            call cho_main("Butterbeer?",face="disgusted",xpos="mid",ypos="base")
            call cho_main("Isn't this supposed to be alcoholic? I'm not supposed to drink during the season...",face="annoyed")
            call cho_mood(1)
        elif cho_tier == 2:
            call cho_main("Butterbeer?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Yes, I'll take it... turns out my team mates had been lying about the alcohol content to mess with me.", "open", "narrow", "base", "mid")
            call cho_main("I guess I'll finally find out what I've been missing out on!","soft","base","raised","L")
            call give_gift(">You give the Butterbeer to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-2)
        elif cho_tier == 3:
            call cho_main("Butterbeer?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("It's a bit tame isn't it? I chugged a lot of it after our last win and can't say I felt a buzz even.", "open", "narrow", "base", "L")
            call give_gift(">You give the Butterbeer to Cho...",gift_item)
            call cho_main("Thank you I suppose, [cho_genie_name].",face="neutral")
            call cho_mood(0)
        else:
            call cho_main("Butterbeer?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Don't you have any firewhisky?","annoyed","base","base","mid")
            call give_gift(">You give the Butterbeer to Cho...",gift_item)
            call cho_main("Thank you I suppose, [cho_genie_name].",face="neutral")
            call cho_mood(0)

    elif gift_item == science_mag_ITEM:
        if cho_tier <= 1:
            call cho_main("Oh, I heard that they put out a new formula for broom polish in this issue.",mouth="open",pupils="R",face="neutral",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        elif cho_tier == 2:
            call cho_main("*Hmm*... Broom aerodynamics and how to utilise your opponents slipstream...",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Interesting...","smile","base","base","mid")
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        elif cho_tier == 3:
            call cho_main("Five steps to modify your brooms legally...",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Sounds useful.","smile","base","base","mid")
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        else:
            call cho_main("Experts guide, How to maintain and store your Quidditch gear.",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Isn't that what a broom closet is for?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)

    elif gift_item == girls_mag_ITEM:
        if cho_tier <= 1:
            call cho_main("Girls magazines, what do you think I am... a gi--",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("I'm good thank you...","open","base","base","L",xpos="mid",ypos="base")
            call cho_mood(0)
        elif cho_tier == 2:
            call cho_main("Girls magazines?",pupils="down",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            call cho_main("I don't usually read these types of magazines, the boys used to make fun of me for it.",face="annoyed")
            call cho_main("But they can't get into the girls dorm.",face="neutral")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        elif cho_tier == 3:
            call cho_main("Girls magazines?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            call cho_main("They do have some interesting stuff on skincare I suppose...","annoyed","closed","base","mid")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        else:
            call cho_main("Girls magazines?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("I did enjoy last months issue about cultural appropriation with traditional clothing...","smile","base","base","mid")
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            call cho_main("Don't tell the boys I said that.","soft","closed","base","mid")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)

    elif gift_item == adult_mag_ITEM:
        if cho_tier <= 1:
            call cho_main("Adult magazines?", "angry", "wide", "raised", "mid",xpos="mid",ypos="base")
            call cho_main("This is highly inappropriate [cho_genie_name]!", "scream", "narrow", "raised", "mid")
            call cho_main("Is this the kind of thing you usually give to people?","angry","base","base","L")
            call cho_mood(1)
        elif cho_tier == 2:
            call cho_main("Adult magazines?",face="disgusted",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of adult magazines to Cho...",gift_item)
            call cho_main("These people do have nice, posture...",face="horny")
            call cho_main("I... I guess they could be useful.",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        elif cho_tier == 3:
            call cho_main("Adult magazines?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("They're all so fit in these magazines, totally my type.","open","wide","raised","down")
            call cho_main("Does this one model in the nude?","horny","base","base","L")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-1)
        else:
            call cho_main("Adult magazines?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Wow, look at that guys abs...","horny","base","base","down")
            call cho_main("And that girls...","soft","base","raised","down")
            call cho_main("I'll take it.", "open", "narrow", "base", "mid")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-2)

    elif gift_item == porn_mag_ITEM:
        if cho_tier <= 1:
            call cho_main("What is this!?!", "angry", "wide", "raised", "mid",xpos="mid",ypos="base")
            call cho_main("Porn magazines?", "open", "wide", "angry", "mid")
            call cho_main("Sir, why would you even think of giving me something like this?", "scream", "narrow", "angry", "L",xpos="mid",ypos="base")
            call cho_main("","angry","base","angry","down")
            call cho_mood(3)
        elif cho_tier == 2:
            call cho_main("What is this?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Porn magazines? Sir, that's too much even for you...", "annoyed", "narrow", "base", "down")
            call cho_main("Is that a snitch in her sna-- No... just no...","open","wide","raised","down")
            call cho_main("","angry","base","angry","down")
            call cho_mood(2)
        elif cho_tier == 3:
            call cho_main("What's this?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give an assortment of porn magazines to Cho...",gift_item)
            call cho_main("What's with these positions? Is that a broom handle up her...",mouth="open",eyes="wide",eyebrows="raised",pupils="down")
            call cho_main("Oh my...",mouth="soft",pupils="R",face="disgusted")
            call cho_mood(0)
        else:
            call cho_main("Porn magazines?",pupils="down",face="horny",xpos="mid",ypos="base")
            call cho_main("Ooh, are those two doing it on a broom? That's impressive...","open","wide","raised","down")
            call cho_main("[cho_genie_name], this is naughty. Even for you...","horny","wink","base","L")
            call cho_main("I've got my eyes on you.", "base", "narrow", "raised", "L")
            call give_gift(">You give an assortment of porn magazines to Cho...",gift_item)
            call cho_main("Thank you.","smile","base","base","mid")
            call cho_mood(-3)

    elif gift_item == krum_poster_ITEM:
        if cho_tier <= 1:
            call cho_main("A Viktor Krum poster?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Professor, he doesn't have his shirt on!","scream","wide","base","down")
            call cho_main("That's...{w=0.3} highly inappropriate...", "open", "narrow", "base", "downR")
            call cho_main("I can't...{w=0.3} I can't accept this.","upset","closed","base","mid")
            call cho_main("","base","base","base","mid")
            call cho_mood(0)
        elif cho_tier == 2:
            call cho_main("A Viktor Krum poster?",mouth="soft",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("He really is quite muscular isn't he...","open","narrow","base","down")
            call cho_main("I'll use it...","smile","base","base","mid")
            call give_gift(">You give the poster to Cho...",gift_item)
            call cho_main("As a motivational poster that is!","open","wide","raised","L")
            call cho_main("Thank you [cho_genie_name].",face="neutral")
            call cho_mood(-2)
        elif cho_tier == 3:
            call cho_main("A Viktor Krum poster?",mouth="smile",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Wasn't his nudes leaked in Wizard Hunks weekly?","open","narrow","base","mid")
            call cho_main("...","angry","wide","raised","down")
            call cho_main("Not that I'd read such a thing.","upset","base","base","downR")
            call give_gift(">You give the poster to Cho...",gift_item)
            call cho_main("Thank you [cho_genie_name].",face="neutral")
            call cho_mood(-3)
        else:
            call cho_main("A Viktor Krum poster?",mouth="scream",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("I'll take that if you don't mind.",pupils="downR",face="horny")
            call give_gift(">You give the poster to Cho...",gift_item)
            call cho_main("(...)",mouth="soft",pupils="up",face="horny")
            call cho_main("I love it, [cho_genie_name].",pupils="mid",face="horny")
            call cho_mood(-5)

    elif gift_item == sexy_lingerie_ITEM:
        if cho_tier <= 1:
            call cho_main("Lingerie?", "annoyed", "narrow", "raised", "down",xpos="mid",ypos="base")
            call cho_main("Sir, are you expecting me to wear this?","open","wide","raised","mid")
            call cho_main("Are you insane?!","scream","wide","raised","L")
            call cho_main("No thank you...","open","base","angry","down")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(2)
        elif cho_tier == 2:
            call cho_main("Lingerie?", "annoyed", "narrow", "base", "down",xpos="mid",ypos="base")
            call cho_main("Why would I want this? I have plenty of clothes I like already...","open","wide","raised","down")
            call cho_main("I'll pass on that one, thanks.","base","base","base","mid")
            call cho_mood(0)
        elif cho_tier == 3:
            call cho_main("Lingerie?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Seems pretty flexible. I might be able use these when stretching.",mouth="annoyed",pupils="down",face="annoyed")
            call give_gift(">You give the lingerie to Cho...",gift_item)
            call cho_main("Thank you [cho_genie_name]",face="neutral")
            call cho_mood(-2)
        else:
            call cho_main("Lingerie?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Sexy... Did you pick them out yourself?","horny","wide","base","down")
            call cho_main("You've got good taste... I tore mine last year during the ball...","base","base","raised","mid")
            call cho_main("Well, they got torn at one point at least...", "smile", "narrow", "base", "down")
            call give_gift(">You give the lingerie to Cho...",gift_item)
            call cho_main("Thank you [cho_genie_name]",face="neutral")
            call cho_mood(-3)

    elif gift_item == sexy_stockings_ITEM :
        if cho_tier <= 1:
            call cho_main("stockings?", "annoyed", "narrow", "raised", "down",xpos="mid",ypos="base")
            call cho_main("Surely that must be against some kind of dresscode...","open","wide","raised","mid")
            call cho_main("I'll pass...","open","base","angry","down")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(1)
        elif cho_tier == 2:
            call cho_main("Stockings?", "annoyed", "narrow", "base", "down",xpos="mid",ypos="base")
            call cho_main("I guess I wont get sunburnt on my legs wearing these...","open","narrow","base","mid")
            call give_gift(">You give the lingerie to Cho...",gift_item)
            call cho_main("Thank you [cho_genie_name]",face="neutral")
            call cho_mood(-1)
        elif cho_tier == 3:
            call cho_main("Stockings?", "annoyed", "narrow", "base", "down",xpos="mid",ypos="base")
            call cho_main("I can almost see right through these...",mouth="annoyed",pupils="down",face="annoyed")
            call give_gift(">You give the lingerie to Cho...",gift_item)
            call cho_main("Thank you [cho_genie_name]",face="neutral")
            call cho_mood(-2)
        else:
            call cho_main("Stockings?", "annoyed", "narrow", "base", "down",xpos="mid",ypos="base")
            call cho_main("But my legs gets to itchy in these, I'd rather go without any leggings...","open","narrow","base","mid")
            call cho_mood(0)

    elif gift_item == pink_condoms_ITEM:
        if cho_tier <= 1:
            call cho_main("Condoms?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("You're expecting me to go and fuck the teachers, is that what you want?", "scream", "narrow", "raised", "L")
            call cho_main("I'm not one of those Slytherin skanks that impale themselves on the daily.", "angry", "narrow", "base", "mid")
            call cho_main("You can take those and go fuck yourself with them...", "soft", "narrow", "angry", "mid")
            call cho_mood(2)
        elif cho_tier == 2:
            call cho_main("Condoms?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("I'm not the kind of girl to go around banging everything I come across...","soft","base","base","down")
            call cho_main("Thanks but no thanks...","open","base","base","mid")
            call cho_mood(1)
        elif cho_tier == 3:
            call cho_main("Condoms?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Are you expecting that I should use these? I know safe sex is important and all but I know what you're insinuating.","angry","narrow","raised","L")
            call cho_main("Keep them...","soft","base","base","down")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(0)
        else:
            call cho_main("Condoms?",pupils="down",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give a pack of condoms to Cho...", gift_item)
            call cho_main("I do surround myself with mostly boys, so having these at hand could be useful...",pupils="downR",face="horny")
            call cho_main("Thank you for your concerns, [cho_genie_name]...",mouth="soft",pupils="mid",face="neutral")
            call cho_mood(-2)

    elif gift_item == vibrator_ITEM:
        if cho_tier <= 1:
            call cho_main("A vibrator?", mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Sir, are you out of your mind?","scream","wide","raised","L")
            call cho_main("I'm your student for crying out loud, giving gifts in general is a bit weird but sex toys...","angry","wide","base","mid")
            call cho_main("Seriously?!","scream","wide","raised","L")
            call cho_mood(3)
        elif cho_tier == 2:
            call cho_main("A vibrator?",mouth="open",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base")
            call cho_main("Why would you give me that...","angry","base","base","down")
            call cho_main("Give it to Granger, I'm sure she'd love to accept a sex toy from her headmaster.","smile","narrow","angry","mid")
            call cho_mood(2)
        elif cho_tier == 3:
            call cho_main("A vibrator?",face="horny",xpos="mid",ypos="base")
            call cho_main("Sir, I don't think this would be appropriate to bring to my dorm...", "soft", "narrow", "base", "down")
            call cho_main("The girls... they'd hear it... not that I want it or anything!","quiver","wide","base","downR")
            call cho_mood(0)
        else:
            call cho_main("A Vibrator?",face="horny",xpos="mid",ypos="base")
            call give_gift(">You give the vibrator to Cho...", gift_item)
            call cho_main("Ahh, It does promote a healthy lifestyle...",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="happy")
            call cho_mood(-3)

    elif gift_item == anal_lube_ITEM:
        if cho_tier <= 1:
            call cho_main("A lubricant?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("What the hell, why do you think this is an appropriate gift? What's wrong with you...","angry","wide","raised","L")
            call cho_main("Senile old man...", "angry", "narrow", "base", "mid")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("A lubricant?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("*Ew* Why are you giving me this... when would I ever have the need for lube.","angry","wide","raised","down")
            call cho_main("Give it to one of those Slytherin skanks, they probably go through a ton of it every week.", "base", "narrow", "raised", "mid")
            call cho_mood(3)
        elif cho_tier == 3:
            call cho_main("Anal lube?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Why would I need something like this? The broom goes under my butt, not in my butt...","soft","wide","raised","L")
            call cho_mood(0)
        else:
            call cho_main("Anal Lubricant?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give the jar of anal lube to Cho...", gift_item)
            call cho_main("You should've given me this yesterday, [cho_genie_name].",mouth="soft",face="annoyed")
            call cho_main("I haven't been able to sit on a broom all day after yesterday's game...",mouth="annoyed",pupils="down",face="annoyed")
            call cho_mood(-5)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if cho_tier <= 1:
            call cho_main("Ball gag... and cuffs?",pupils="down",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Wait, is this a sex thing?","soft","wide","raised","mid")
            call cho_main("Professor, that's disgusting... why would you give me this.","angry","wide","raised","mid")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("Ball gag and cuffs?",pupils="down",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Sir, this is highly inappropriate gift to give to a student!", "scream", "narrow", "raised", "mid")
            call cho_main("Why would you give me these, how is this going to help me with Quidditch?","angry","base","base","mid")
            call cho_mood(3)
        elif cho_tier == 3:
            call cho_main("Ball gag and cuffs?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("I prefer not to lock myself up, I'm a free spirit.","soft","base","raised","L")
            call cho_main("Thanks... but no thanks.","open","base","base","mid")
            call cho_mood(0)
        else:
            call cho_main("Ball gag and cuffs?",pupils="down",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give the ball gag and cuffs to Cho...", gift_item)
            call cho_main("How progressive... do they require a safe-word to open?",face="horny")
            call cho_main("Wait, how would a safe-word work when you have a ball in your mouth...",mouth="quiver",eyes="wide",eyebrows="raised",pupils="down")
            call cho_mood(-3)

    elif gift_item == anal_plugs_ITEM:
        if cho_tier <= 1:
            call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("That's disgusting... why do you think it's a good idea to give these to me?","angry","wide","raised","L")
            call cho_main("That one has a tail on it...", "angry", "narrow", "raised", "mid")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Why do you have these? They're not used are they...","angry","wide","raised","L")
            call cho_main("*Ew* Just, no...", "open", "narrow", "raised", "mid")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(3)
        elif cho_tier == 3:
            call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Sir, are you expecting me to wear this?","angry","base","base","L")
            call cho_main("During Quidditch?","angry","wide","raised","L")
            call cho_main("No, no, no, no no.", "open", "narrow", "raised", "mid")
            call cho_main("NO!","scream","wide","raised","mid")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(2)
        else:
            call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give a set of anal plugs to Cho...", gift_item)
            call cho_main("But these would stick out under my robes...",face="annoyed")
            call cho_main("Maybe people would just think it's a tail or something...",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-2)

    elif gift_item == testral_strapon_ITEM:
        if cho_tier <= 1:
            call cho_main("Is that a strap-on?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call cho_main("It's huge!","scream","wide","raised","L")
            call cho_main("I mean, why are you showing me this?", "annoyed", "narrow", "base", "mid")
            call cho_main("get it away from me.", "soft", "narrow", "base", "mid")
            call cho_mood(3)
        elif cho_tier == 2:
            call cho_main("A strap-on?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call cho_main("Seriously? Why are you giving me this...","angry","wide","base","down")
            call cho_main("That's disgusting...", "open", "narrow", "base", "mid")
            call cho_mood(2)
        elif cho_tier == 3:
            call cho_main("A strap-on?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call cho_main("But it's so big...","horny","wide","raised","mid")
            call cho_main("I.. I don't want it...", "open", "narrow", "base", "down")
            call cho_main("","base","base","base","mid")
            call cho_mood(0)
        else:
            call cho_main("A strap-on?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call give_gift(">You give the thestral strap-on to Cho...", gift_item)
            call cho_main("How would that even fit in anyone?",mouth="quiver",eyes="wide",eyebrows="raised",pupils="down")
            call cho_mood(-1)

    elif gift_item == broom_2000_ITEM:
        if cho_tier <= 1:
            call cho_main("A broom... yes! Finally something better than my old--",mouth="scream",eyes="wide",eyebrows="raised",pupils="down",xpos="mid",ypos="base")
            call cho_main("Hold on, is that a double ended dildo sticking out of it?!?","angry","wide","base","mid")
            call cho_main("What's wrong with you?","scream","wide","base","L")
            call cho_main("Get that away from my... from me!", "angry", "narrow", "base", "mid")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("Is that a broom with dildos on it?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call cho_main("Professor, seriously... why... just why.", "angry", "narrow", "base", "mid")
            call cho_mood(2)
        elif cho_tier == 3:
            call cho_main("A broom?", "open", "wide", "worried", "down",xpos="mid",ypos="base")
            call cho_main("A sex broom? Where did you even get this...","open","wide","raised","mid")
            call cho_main("No..{w=0.3} I don't...{w=0.3} I don't want that.","horny","narrow","base","mid")
            call cho_mood(0)
        else:
            call cho_main("Is that a Lady Speed Stick-2000, with a built-in vibrator and pulse function?",mouth="scream",eyes="wide",eyebrows="raised",pupils="down",xpos="mid",ypos="base")
            call give_gift(">You give the broom to Cho...", gift_item)
            call cho_main("I mean, it's a nice broom alright...",pupils="downR",face="horny")
            call cho_main("But, to be honest, [cho_genie_name]...",mouth="soft",pupils="down",face="horny")
            call cho_main("I can't wait to try it out!",pupils="mid",face="happy")
            call cho_mood(-6)

    elif gift_item == sexdoll_ITEM:
        if cho_tier <= 1:
            call cho_main("A sex doll? What the heck... why do you have this?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("And more importantly...","smile","closed","base","mid")
            call cho_main("{size=+4}Why are you giving it to me?{/size}","scream","wide","base","L")
            call cho_main("You disgust me...", "open", "narrow", "angry", "mid")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("A sex doll?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Why would you give this to me? Wait, did you use this?","angry","wide","base","L")
            call cho_main("Get it away from me...","open","wide","raised","L")
            call cho_mood(3)
        elif cho_tier == 3:
            call cho_main("A sex doll?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Why would I need this, it's a girl doll...","annoyed","wide","base","L")
            call cho_main("I mean, why would I need a sex doll in general. I'm not into this sort of thing...","open","wide","raised","mid")
            call cho_mood(1)
        else:
            call cho_main("A sex doll?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give the sex doll to Cho...", gift_item)
            call cho_main("It says Joanne on it...",face="disgusted")
            call cho_main("I leave it in the boys changing room, should be a good reward after a practice.",face="annoyed")
            call cho_mood(-7)

    elif gift_item == anal_beads_ITEM:
        if cho_tier <= 1:
            call cho_main("Anal beads?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Yeah, that's not going anywhere near their intended target...","angry","wide","raised","L")
            call cho_mood(4)
        elif cho_tier == 2:
            call cho_main("Anal beads?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("How... where did you...","angry","wide","raised","L")
            call cho_main("*Gross!", "open", "narrow", "raised", "mid")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(3)
        elif cho_tier == 3:
            call cho_main("Anal beads?",face="annoyed",xpos="mid",ypos="base")
            call cho_main("Sir, how would I be able to sit on a broom if I used these?","angry","base","base","L")
            call cho_main("Not that I would ever use them!","angry","wide","raised","L")
            call cho_main("Get those away from me!", "open", "narrow", "raised", "mid")
            call cho_main("","annoyed","base","base","mid")
            call cho_mood(2)
        else:
            call cho_main("Anal beads?",face="annoyed",xpos="mid",ypos="base")
            call give_gift(">You give the anal beads to Cho...", gift_item)
            call cho_main("Surely my butt would hurt after using these...",face="annoyed")
            call cho_main("Although I do have a cushioning charm on my broom for a reason...",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood(-2)

    elif gift_item == wine_ITEM:
        if cho_tier <= 2:
            call cho_main("A wine bottle?", face="annoyed", xpos="mid", ypos="base")
            call cho_main("[cho_genie_name], I cannot drink alcohol, it would ruin my career..", "open", "narrow", "angry", "mid")
            call cho_mood(4)
        else:
            call cho_main("A wine bottle?", face="neutral", xpos="mid", ypos="base")
            call cho_main("Thank you, [cho_genie_name] but I can't take it.",face="neutral")
            call cho_main("{size=-4}Maybe to celebrate after I win the Quidditch Cup..{/size}",face="horny")
            call cho_mood(0)

    elif gift_item == firewhisky_ITEM:
        call cho_main("Firewhisky?",face="happy",xpos="mid",ypos="base",trans=d5)
        call cho_main("Why are you giving it to me?","annoyed","wide","base","L")
        call cho_mood(0)

    call cho_main(xpos="base", ypos="base", trans=d5)

    $ renpy.jump_out_of_context("cho_requests")

label cho_mood(value=0):
    show screen blktone
    with d3

    if value > 0:
        if value == 1:
            "Cho's mood worsened slightly."
        else:
            "Cho's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Cho's mood has improved slightly."
        else:
            "Cho's mood has improved significantly."
    else:
        "Cho's mood hasn't changed."

    $ was_negative = cho_mood > 0
    $ cho_mood = max(min(cho_mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, cho_mood, value)

    hide screen blktone
    return
