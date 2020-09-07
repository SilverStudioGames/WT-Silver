

### Tonks Chitchats ###

label tonks_chit_chat:
    $ chitchated_with_tonks = True

    $ renpy.dynamic("chitchat_choices")
    $ chitchat_choices = set(range(1, 32))

    # Don't talk about Metamorphmagi if Genie doesn't know Tonks is one
    if not tonks_morph_known:
        $ chitchat_choices -= set([4, 9, 19, 24, 29, 30])

    # Don't talk about Susan if Genie doesn't know her yet
    if not susan_unlocked:
        $ chitchat_choices -= set([1])

    $ random_number = renpy.random.choice(list(chitchat_choices))

    # Chitchats #TODO 3, 10 should check if you've done some amount of public favours
    if random_number == 1:
        call ton_main("Susan is such a lovely girl...","open","base","base","mid")
        call ton_main("But she really isn't very confident in her body...","open","base","raised","R")
        call ton_main("I do hope your little games can help her open up a bit...","base","base","base","mid")

    elif random_number == 2:
        call ton_main("Teaching has been so much fun!", "grin", "base", "raised", "mid")
        call ton_main("It's so much better than working at the Ministry.", "open", "closed", "annoyed", "mid")
        call ton_main("I can't believe how much time I spent in that shit-hole...","base","base","angry","R")

    elif random_number == 3:
        call ton_main("I spotted another cute girl in my class today...", "soft", "base", "base", "R")
        call ton_main("I hope she's into points as much as the rest.", "horny", "narrow", "raised", "mid")

    elif random_number == 4:
        call ton_main("Since Metamorphmagi can change their skin, I sometimes just don't bother wearing any clothes.", "soft", "base", "shocked", "mid")
        call ton_main("I once changed the colour of my skin and made it look like a tight shirt...", "grin", "narrow", "base", "R")
        call ton_main("I might have worked topless once or twice...","horny","base","raised","mid")

    elif random_number == 5:
        call ton_main("Don't tell professor McGonagall, but I once used her appearance to search one of the student's underwear drawer...", "grin", "closed", "worried", "mid")
        call ton_main("They didn't suspect a thing.", "soft", "wink", "base", "mid")

    elif random_number == 6:
        call ton_main("Being a teacher sure has its perks. If I was caught with firewhisky as a student I would've gotten expelled.", "soft", "closed", "annoyed", "mid")
        call ton_main("Now I can have as much as I like, even share some every once in a while.", "grin", "wink", "base", "mid")

    elif random_number == 7:
        call ton_main("I sometimes wonder if I should have gone into the medicine field...", "open", "narrow", "base", "R")
        call ton_main("I could've had Madam Pomfrey's job by now...", "normal", "base", "base", "mid")
        call ton_main("Maybe I could ask her if she needs any assistance on my off hours.", "soft", "base", "base", "R")

    elif random_number == 8:
        call ton_main("I feel like I have a lot more in common with the students than the other teachers...", "open", "base", "base", "R")
        call ton_main("They're all so old...", "normal", "base", "base", "up")
        call ton_main("Madam Hooch is cool though, she and I roll the same way... in more ways than one.", "soft", "base", "base", "mid")

    elif random_number == 9:
        call ton_main("I often got detentions by morphing into prefects...", "normal", "base", "base", "R")
        call ton_main("It was worth it though as I had free range to the prefects' bathroom...", "base", "wide", "base", "mid")

    elif random_number == 10:
        call ton_main("I had to keep one of the students after class for special tutoring.", "open", "base", "base", "R")
        call ton_main("As a defence against the dark arts teacher it is my job to protect them against both outside threats and inner demons...","open","base","base","L")
        call ton_main("She has a lot to learn but it's getting there.","horny","base","raised","L")

    elif random_number == 11:
        call ton_main("Snape doesn't seem to like me much...","base","base","base","R")
        call ton_main("First I thought it was because I stole a girding potion in my youth...","open","base","base","L")
        call ton_main("But it seems to be more because he wants my job...","open","base","raised","mid")
        call ton_main("The sunlight could probably do him some good.","base","base","angry","mid")

    elif random_number == 12:
        call ton_main("When I first saw Snape I thought he must be a vampire...","open","base","base","mid")
        call ton_main("Turns out he's just a normal dude with pale skin...","open","base","base","R")
        call ton_main("If he were a vampire I would have been all over him...","horny","base","raised","R")

    elif random_number == 13:
        call ton_main("Good students get a little star from me in the corner on each test.","open","base","base","mid")
        call ton_main("That doesn't necessarily mean good grades though...","base","base","base","mid")

    elif random_number == 14:
        call ton_main("We had an accident involving pixies in class today. I can't believe they haven't been taken out of the curriculum.","open","base","base","R")
        call ton_main("One of the students had her clothes completely destroyed...","open","base","base","mid")
        call ton_main("Actually, maybe the pixies aren't that bad...","base","base","base","down")

    elif random_number == 15:
        call ton_main("I'm not going to throw any of the other teachers under the broom about their teaching methods, but...","open","base","base","down")
        call ton_main("I try to not take away points for simple mistakes, I was pretty clumsy myself...", "soft", "base", "shocked", "downR")
        call ton_main("I like to reward my students rather than punishing them...", "base", "narrow", "shocked", "mid")

    elif random_number == 16:
        call ton_main("There's a secret passage to Honeydukes right outside my classroom...", "soft", "base", "base", "mid")
        call ton_main("Having free access to the sweetshop has been a real benefit to reward my students.","base","base","base","R")

    elif random_number == 17:
        call ton_main("I hope I'll have enough time to have a positive influence on this school and the students...","open","base","base","L")
        call ton_main("If I can't make a mark in the school I should at least be able to make one on the students.", "horny", "narrow", "base", "mid")

    elif random_number == 18:
        call ton_main("Becoming an auror is extremely difficult and the job is almost entirely dominated by men...", "upset", "narrow", "worried", "R")
        call ton_main("I think I made the right choice of becoming a teacher.", "open", "closed", "shocked", "mid")

    elif random_number == 19:
        call ton_main("Most of my abilities are based around emotions...","open","base","base","mid")
        call ton_main("My hair can go red when I'm upset or angry...", "upset", "base", "base", "mid")
        call ton_main("Don't tell anyone but my natural hair colour is actually more brown...","open","base","base","R")
        call ton_main("People think it's pink but that's because I'm horny all the time.","base","base","base","down")

    elif random_number == 20:
        call ton_main("My mother was a pure-blood but was burned off the Black family tree after marrying a muggle-born...","open","base","base","down")
        call ton_main("Some people won't understand but I think you should be allowed to love whoever you want...","open","base","base","mid")

    elif random_number == 21:
        call ton_main("Don't tell anyone but I must have spent a fortune on Tolipan Blemish Blitzer in my time studying at Hogwarts...", "open", "narrow", "base", "downR")
        call ton_main("My parents thought I was just being clumsy and needed replacement materials but most of the money they sent me was spent on beauty and hair products...", "annoyed", "base", "base", "R")

    elif random_number == 22:
        call ton_main("I only really chased after boys during school because all the other girls did...","open","base","raised","down")
        call ton_main("Secretly I just wanted them to chase after me instead...", "normal", "base", "base", "L")

    elif random_number == 23:
        call ton_main("I learned a lot being tutored by Alastor Moody...", "soft", "base", "base", "mid")
        call ton_main("Never thought I'd end up being a teacher myself...","open","base","raised","down")
        call ton_main("Though my methods are slightly different to his...", "soft", "base", "base", "downR")

    elif random_number == 24:
        call ton_main("There are rumours that Snape has set up an Age Line in his office to keep students away from his private stash...", "normal", "narrow", "base", "R")
        call ton_main("Won't stop me borrowing some polyjuice potions though... Not that I need them...","open","base","base","R")
        call ton_main("But maybe I can find a girl that doesn't mind drinking it and have some fun.","horny","base","raised","R")

    elif random_number == 25:
        call ton_main("I don't like when people call me Nymphadora... It's Tonks!", "annoyed", "base", "annoyed", "mid")
        call ton_main("Last time someone called me that, I used a engorgement charm on him.","open","base","angry","R")
        call ton_main("Don't ask me what I aimed at...", "crooked_smile", "base", "base", "up")

    elif random_number == 26:
        call ton_main("My favourite creature has to be the were-wolf...", "open", "closed", "base", "mid")
        call ton_main("their beast-like nature excites me...", "soft", "narrow", "base", "mid")
        call ton_main("In another lifetime maybe...","base","base","raised","down")

    elif random_number == 27:
        call ton_main("The students laughed when I accidentally tripped during my last lesson...","open","base","base","R")
        call ton_main("Little did they know I got a good view whilst on the ground...", "horny", "narrow", "raised", "stare")

    elif random_number == 28:
        call ton_main("One of the girls had their boggart turn into a student pointing and laughing at her...","open","base","base","R")
        call ton_main("I'm going to teach her to not be ashamed of her body.", "soft", "narrow", "base", "mid")

    elif random_number == 29:
        call ton_main("I'm a metamorphmagus. I can change my appearance at will...","open","base","base","mid")
        call ton_main("Makes spying on the other teachers and students a lot easier...", "grin", "base", "raised", "mid")

    elif random_number == 30:
        call ton_main("I can change the shape and length of my tongue any way I want.","open","base","base","mid")
        call ton_main("Imagine the possibilities...", "open_wide_tongue2", "narrow", "base", "mid")

    elif random_number == 31:
        call ton_main("Today I taught the students about the {i}Tanglepest{/i}...","open","base","base","mid")
        call ton_main("A foul creature that is drawn to footwear...","open","base","base","R")
        call ton_main("It doesn't actually exist, I just wanted an excuse to have the students show me their feet.","horny","base","base","mid")
    return
