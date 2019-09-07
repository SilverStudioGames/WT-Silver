# Astoria Gift Responses

label give_ast_gift(gift_item):
    $ gave_astoria_gift = True

    if gift_item == lollipop_ITEM:
        call ast_main("A lollipop?",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the lollipop to Astoria...", gift_item)
        call ast_main("I told you, I'm not a kid...",face="angry")
        call ast_main("Although, the other students haven't had any left since the last Hogsmeade trip.",mouth="open",face="neutral")
        call ast_main("They'll be so jealous!",mouth="grin",face="happy")
        call ast_mood(-1)

    elif gift_item == chocolate_ITEM:
        call ast_main("Some chocolate?",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the chocolate to Astoria...", gift_item)
        call ast_main("Thank you, [ast_genie_name].",mouth="open",face="neutral")
        call ast_main("I could put some on a chair and then...",mouth="pout",pupils="R",face="neutral")
        call ast_main("Hi-hi,... Just imagine the mess it's going to make one someone's pants!",face="happy")
        call ast_mood(-1)

    elif gift_item == plush_owl_ITEM:
        call ast_main("An owl plushie?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the stuffed toy to Astoria...", gift_item)
        call ast_main("I don't use stuffed toys...",mouth="open",face="annoyed")
        call ast_main("I know someone that hates owls though... I'll put this in front of her face when she's waking up...",mouth="pout",pupils="R",face="neutral")
        call ast_mood(-1)

    elif gift_item == butterbeer_ITEM:
        call ast_main("Butterbeer?",face="happy",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the bottle to Astoria...", gift_item)
        call ast_main("I thought you couldn't bring this into the school?",face="happy")
        call ast_main("They'll be so jealous...",mouth="pout",face="angry")
        call ast_mood(-1)

    elif gift_item == science_mag_ITEM:
        call ast_main("(...)",mouth="pout",pupils="down",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of educational magazines to Astoria...", gift_item)
        call ast_main("Creating your own itch powder using household ingredients?",mouth="open",pupils="down",face="annoyed")
        call ast_main("Is the kitchen open to students?",mouth="disgust",pupils="down",face="annoyed")
        call ast_main("What am I supposed to do with this, [ast_genie_name]?",mouth="pout",face="annoyed")
        call ast_mood(0)

    elif gift_item == girls_mag_ITEM:
        call ast_main("Girl magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of rather girly magazines to Astoria...", gift_item)
        call ast_main("I'll take it for the free mascara sample. I once drew a uni-brow on someone with it.",face="happy")
        call ast_mood(-1)

    elif gift_item == adult_mag_ITEM:
        call ast_main("Adult magazines?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of adult magazines to Astoria...", gift_item)
        call ast_main("Of course I read them. I'm an adult after all, it's in the name.",mouth="pout",pupils="R",face="angry")
        call ast_mood(-1)

    elif gift_item == porn_mag_ITEM:
        call ast_main("Porn magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of pornographic magazines to Astoria...", gift_item)
        call ast_main("I'll take it!",mouth="grin",face="happy")
        call ast_main("I'll put one in Susan's bag when she's not looking. Can't wait to see that cows face when her friends sees it.",mouth="open",face="angry")
        call ast_main("Thank you, [ast_genie_name].",face="happy")
        call ast_mood(-1)

    elif gift_item == krum_poster_ITEM:
        call ast_main("Viktor Krum?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call ast_main("Is that the Quidditch player everyone seems to fancy?",mouth="open",pupils="mid",face="annoyed")
        call give_gift(">You give the poster to Astoria...", gift_item)
        call ast_main("Hmph, I guess I'll take it if he's that popular...",mouth="pout",pupils="R",face="neutral")
        call ast_mood(0)

    elif gift_item == sexy_lingerie_ITEM:
        call ast_main("Lingerie?",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call ast_main("Is that French or something?",mouth="pout",face="annoyed")
        call give_gift(">You give the sexy lingerie to Astoria...", gift_item)
        call ast_main("Seems pretty elastic though... I could totally lob some stink bombs with these.",mouth="grin",face="angry")
        call ast_mood(-1)

    elif gift_item == pink_condoms_ITEM:
        call ast_main("Are those water balloons?",mouth="happy",face="happy",xpos="mid",ypos="base",trans="d5")
        call ast_main("Heck yeah, they don't sell any of these big types in Hogsmeade.",mouth="grin",face="angry")
        call give_gift(">You give the pack of \"water balloons\" to Astoria...", gift_item)
        call ast_main("Thank you, [ast_genie_name].",face="happy")
        call ast_mood(-2)

    elif gift_item == vibrator_ITEM:
        call give_gift(">You give the vibrator to Astoria...",gift_item)
        #Add text

    elif gift_item == anal_lube_ITEM:
        call ast_main("Lube?",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call ast_main("I know the perfect staircase for this!",face="happy")
        call give_gift(">You give the jar of lube to Astoria...", gift_item)
        call ast_main("Thank you, [ast_genie_name].",face="happy")
        call ast_mood(-1)

    elif gift_item == ballgag_and_cuffs_ITEM:
        call give_gift(">You give the handcuffs to Astoria...", gift_item)
        #Add text

    elif gift_item == anal_plugs_ITEM:
        call give_gift(">You give the anal plugs to Astoria...", gift_item)
        #Add text

    elif gift_item == testral_strapon_ITEM:
        call give_gift(">You give the strap-on to Astoria...", gift_item)
        #Add text

    elif gift_item == broom_2000_ITEM:
        call give_gift(">You give the broom to Astoria...", gift_item)
        #Add text

    elif gift_item == sexdoll_ITEM:
        call give_gift(">You give the doll to Astoria...", gift_item)
        #Add text
        
    elif gift_item == wine_ITEM:
        call give_gift(">You give the wine to Astoria...", gift_item)
        #Add text
            
    elif gift_item == firewhisky_ITEM:
        call give_gift(">You give the firewhisky to Astoria...", gift_item)
        #Add text

    call ast_main(xpos="base",ypos="base", trans="d5")
    return

label ast_mood(value=0):
    show screen blktone5
    with d3

    if value > 0:
        if value == 1:
            "Astoria's mood worsened slightly."
        else:
            "Astoria's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Astoria's mood has improved slightly."
        else:
            "Astoria's mood has improved significantly."
    else:
        "Astoria's mood hasn't changed."

    $ ast_mood = max(min(ast_mood+value, 100), 0)
    hide screen blktone5
    return