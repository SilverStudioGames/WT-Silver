# Luna Gift Responses

label give_lun_gift(gift_item):
    hide screen luna_main
    with d5
    call lun_main(xpos="mid",ypos="base",trans=d5)

    $ gave_luna_gift = True

    if gift_item == lollipop_ITEM:
        lun "A lollipop?"
        call give_gift(">You give the lollipop to Luna...", gift_item)
        lun "My father always believed that you should always have something sugary around in case any baby unicorns come to visit."
        lun "Thank you, [lun_genie_name]."

    elif gift_item == chocolate_ITEM:
        lun "Chocolate?"
        call give_gift(">You give the chocolate to Luna...", gift_item)
        lun "*Aaah*, I heard these helps with dementia... Or was it Dementors?"

    elif gift_item == plush_owl_ITEM:
        lun "A plush owl?"
        call give_gift(">You give the owl plushie to Luna...", gift_item)
        lun "I love owls... Always had a few around me growing up, delivering the newspaper my father publishes."

    elif gift_item == butterbeer_ITEM:
        lun "Butterbeer?"
        call give_gift(">You give the bottle to Luna...", gift_item)
        lun "How did you know? I didn't wear my cork necklace today."
        lun "Thank you, [lun_genie_name]."

    elif gift_item == science_mag_ITEM:
        lun "Magical creatures weekly?"
        call give_gift(">You give an assortment of educational magazines to Luna...", gift_item)
        lun "Thestrals and their link with death..."
        lun "Interesting..."

    elif gift_item == girls_mag_ITEM:
        call give_gift(">You give the girls magazine to Luna...",gift_item)
        #Add text

    elif gift_item == adult_mag_ITEM:
        call give_gift(">You give the adult magazine to Luna...",gift_item)
        #Add text

    elif gift_item == porn_mag_ITEM:
        call give_gift(">You give the porn magazine to Luna...",gift_item)
        #Add text

    elif gift_item == krum_poster_ITEM:
        call give_gift(">You give the poster to Luna...",gift_item)
        #Add text

    elif gift_item == sexy_lingerie_ITEM:
        call give_gift(">You give the lingerie to Luna...",gift_item)
        #Add text

    elif gift_item == sexy_stockings_ITEM :
        call give_gift(">You give the stockings to Luna...",gift_item)
        #Add text

    elif gift_item == pink_condoms_ITEM:
        call give_gift(">You give the condoms to Luna...",gift_item)
        #Add text

    elif gift_item == vibrator_ITEM:
        call give_gift(">You give the vibrator to Luna...",gift_item)
        #Add text

    elif gift_item == anal_lube_ITEM:
        call give_gift(">You give the anal lube to Luna...",gift_item)
        #Add text

    elif gift_item == ballgag_and_cuffs_ITEM:
        call give_gift(">You give the handcuffs to Luna...",gift_item)
        #Add text

    elif gift_item == anal_plugs_ITEM:
        call give_gift(">You give the anal plugs to Luna...",gift_item)
        #Add text

    elif gift_item == testral_strapon_ITEM:
        call give_gift(">You give the strap-on to Luna...",gift_item)
        #Add text

    elif gift_item == broom_2000_ITEM:
        call give_gift(">You give the broom to Luna...",gift_item)
        #Add text

    elif gift_item == sexdoll_ITEM:
        call give_gift(">You give the doll to Luna...",gift_item)
        #Add text

    elif gift_item == anal_beads_ITEM:
        call give_gift(">You give the anal beads to Luna...",gift_item)
        #Add text

    elif gift_item == wine_ITEM:
        call give_gift(">You give the wine to Luna...", gift_item)
        #Add text

    elif gift_item == firewhisky_ITEM:
        call give_gift(">You give the firewhisky to Luna...", gift_item)
        #Add text

    hide screen luna_main
    with d5
    call lun_main(xpos="base",ypos="base",trans=d5)

    return

label lun_mood(value=0):
    show screen blktone
    with d3

    if value > 0:
        if value == 1:
            "Luna's mood worsened slightly."
        else:
            "Luna's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Luna's mood has improved slightly."
        else:
            "Luna's mood has improved significantly."
    else:
        "Luna's mood hasn't changed."

    $ was_negative = lun_mood > 0
    $ lun_mood = max(min(lun_mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, lun_mood, value)

    hide screen blktone
    return
