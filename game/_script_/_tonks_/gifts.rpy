### Give Tonks Gift ###

label give_ton_gift(gift_item):
    $ gave_tonks_gift = True

    if gift_item == lollipop_ITEM:
        call ton_main("A lollipop?",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the lollipop to Tonks...", gift_item)
        call ton_main("I know the perfect student to give this to.",face="happy")
        call ton_friendship(1)

    elif gift_item == chocolate_ITEM:
        call ton_main("*Mhmm*, Chocolate!",pupils="down",face="happy",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the chocolate to Tonks...", gift_item)
        call ton_main("It's said that chocolate is a very effective mood enhancer after a Dementor attack.",mouth="open",face="happy")
        call ton_main("That's because chocolate is considered to be a great aphrodisiac...",face="horny")
        call ton_main("I'll keep this for one of my private lessons.",face="happy")
        call ton_friendship(1)

    elif gift_item == plush_owl_ITEM:
        call ton_main("An Owl?",face="neutral",xpos="mid",ypos="base",trans=d5)
        call ton_main("Oh, it's a toy... Haven't seen one of these in a while.",face="disgusted")
        call give_gift(">You give the stuffed owl to Tonks...",gift_item)
        call ton_main("Okay, for nostalgias sake then...",face="neutral")
        call ton_friendship(0)

    elif gift_item == butterbeer_ITEM:
        call ton_main("Butterbeer?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("Don't you have anything stronger?",mouth="open",face="annoyed")
        call give_gift(">You give the bottle to Tonks...", gift_item)
        call ton_main("Just joking, I'll save it for when I've got company.",face="happy")
        call ton_friendship(1)

    elif gift_item == science_mag_ITEM:
        call ton_main("Jinxes and sphinxes? These could help for some of my lessons.",mouth="open",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give an assortment of educational magazines to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(0)

    elif gift_item == girls_mag_ITEM:
        call ton_main("Some girl magazines? I could definitely put these in my classroom.",mouth="open",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give an assortment of rather girly magazines to Tonks...", gift_item)
        call ton_main("The girls do love staying after hours to socialise.",face="happy")
        call ton_friendship(0)

    elif gift_item == adult_mag_ITEM:
        call ton_main("Adult magazines?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("Wont be the first time I've slipped one in the stack of magazines in my classroom",face="horny")
        call give_gift(">You give an assortment of adult magazines to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(1)

    elif gift_item == porn_mag_ITEM:
        call ton_main("Porn magazines?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("I already know most positions in this book already of course...",face="happy")
        call give_gift(">You give an assortment of pornographic magazines to Tonks...", gift_item)
        call ton_main("Although...",face="horny")
        call ton_main("I'll keep them. Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(1)

    elif gift_item == krum_poster_ITEM:
        call ton_main("That's that Krum boy is it?",face="horny",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the poster to Tonks...", gift_item)
        call ton_main("Nice figure, could set a good mood in the classroom... Or my office.",pupils="down",face="happy")
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(1)

    elif gift_item == sexy_lingerie_ITEM:
        call ton_main("Oh, I see you're a man with a sense of style.",mouth="open",pupils="down",face="happy",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the sexy lingerie to Tonks...", gift_item)
        call ton_main("If it were up to me these would be part of the school uniform...",face="happy")
        call ton_friendship(1)

    elif gift_item == sexy_stockings_ITEM :
        call ton_main("Nice, I have a pair just like these...",mouth="open",pupils="down",face="happy",xpos="mid",ypos="base",trans=d5)
        call ton_main("Although another pair without holes in them wont hurt...",face="happy")
        call give_gift(">You give the sexy stockings to Tonks...", gift_item)
        call ton_friendship(1)

    elif gift_item == pink_condoms_ITEM:
        call ton_main("Some condoms?",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give some condoms to Tonks...", gift_item)
        call ton_main("Safe sex is important...",face="neutral")
        call ton_main("I don't remember taking sex ed when I was in school... maybe I was too busy experimenting it myself that day...",face="horny")
        call ton_friendship(1)

    elif gift_item == vibrator_ITEM:
        call ton_main("A vibra-- back massager?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("Mm, Mine seemingly went missing from my desk. This should do if it doesn't turn up again.",face="annoyed")
        call give_gift(">You give the vibrator to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(1)

    elif gift_item == anal_lube_ITEM:
        call ton_main("That's one big jar of Anal lube you have there.",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the jar of lube to Tonks...", gift_item)
        call ton_main("What's the difference between this and regular lube?",mouth="open",face="disgusted")
        call ton_main("Seems like it might be enough to cover the whole body...",mouth="open",face="happy")
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(1)

    elif gift_item == ballgag_and_cuffs_ITEM:
        call ton_main("Ball gag and cuffs?",pupils="down",face="happy",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the ball gag and cuffs to Tonks...", gift_item)
        call ton_main("These are pretty cute. Should come in handy during my.... private lessons.",face="horny")
        call ton_friendship(1)

    elif gift_item == anal_plugs_ITEM:
        call ton_main("Some anal plugs?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("Wow, this is what they use these days? Very colourful...",face="happy")
        call give_gift(">You give an assortment of anal plugs to Tonks...", gift_item)
        call ton_main("I think I might leave some in one of the desks...",face="horny")
        call ton_friendship(1)

    elif gift_item == testral_strapon_ITEM:
        call ton_main("Is that a strap-on?", "open", "wide", "shocked", "stare", xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the thestral strap-on to Tonks...", gift_item)
        call ton_main("This will be a perfect addition to my collection...",face="angry")
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(2)

    elif gift_item == broom_2000_ITEM:
        call ton_main("I don't remember the brooms looking like this when I took flying lessons...",face="angry",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the broom to Tonks...", gift_item)
        call ton_main("Seems like a good way to stay put on the broom though... unless you lose focus.",mouth="open",face="happy")
        call ton_main("Which you probably will with this...",face="horny")
        call ton_friendship(3)

    elif gift_item == sexdoll_ITEM:
        call ton_main("a sex doll?",face="horny",xpos="mid",ypos="base",trans=d5)
        call ton_main("Not too useful for me, but I might put it in one of our secret gift exchanges.",mouth="open",face="horny")
        call give_gift(">You give the sex doll to Tonks...", gift_item)
        call ton_main("They'll gossip for weeks wondering who it's from.",face="horny")
        call ton_friendship(1)

    elif gift_item == anal_beads_ITEM:
        call ton_main("anal beads?",face="disgusted",xpos="mid",ypos="base",trans=d5)
        call ton_main("It's a bit short but I'll take it...",face="happy")
        call give_gift(">You give the anal beads to Tonks...", gift_item)
        call ton_main("Thanks...",face="horny")
        call ton_friendship(1)

    elif gift_item == wine_ITEM:
        if not firewhisky_ITEM.unlocked:
            call ton_main("A bottle of wine?",face="neutral",xpos="mid",ypos="base", trans=d5)
            call ton_main("I was hoping for something with a bit more \'punch\'.",mouth="open", pupils="R", face="neutral")
            call ton_friendship(0)
        else:
            call ton_main("I had told you before I don't particularly like wine..", face="sad", xpos="mid",ypos="base", trans=d5)
            call ton_friendship(-1)

    elif gift_item == firewhisky_ITEM:
        call ton_main("Firewhisky?",face="happy",xpos="mid",ypos="base",trans=d5)
        call ton_main("*Mmm*.. My favourite. But let's save it for later, shall we?", face="horny")
        call ton_friendship(0)

    call ton_main(xpos="base", ypos="base",trans=d5)

    return

label ton_friendship(value=0):
    show screen blktone
    with d3

    if value > 0:
        if value == 1:
            "Tonks likes you a bit more now."
        else:
            "Tonks likes you more now."
    elif value < 0:
        if value == -1:
            "Tonks didn't seem to like that."
        else:
            "Tonks likes you a bit less now."
    else:
        "Tonks' friendship towards you hasn't changed much."

    $ ton_friendship = max(min(ton_friendship+value, 100), 0)
    hide screen blktone
    return
