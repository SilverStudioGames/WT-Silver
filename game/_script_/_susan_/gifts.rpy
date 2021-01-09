# Susan Gift Responses

label give_sus_gift(gift_item):
    hide screen susan_main
    with d5
    call sus_main(xpos="mid",ypos="base",trans=d5)

    $ gave_susan_gift = True

    if gift_item == lollipop_ITEM:
        call give_gift(">You give the lollipop to Susan...",gift_item)
        #Add text

    elif gift_item == chocolate_ITEM:
        call give_gift(">You give the chocolate to Susan...",gift_item)
        #Add text

    elif gift_item == plush_owl_ITEM:
        call give_gift(">You give the plush owl to Susan...",gift_item)
        #Add text

    elif gift_item == butterbeer_ITEM:
        call give_gift(">You give the butterbeer to Susan...",gift_item)
        #Add text

    elif gift_item == science_mag_ITEM:
        call give_gift(">You give the educational magazine to Susan...",gift_item)
        #Add text

    elif gift_item == girls_mag_ITEM:
        call give_gift(">You give the girls magazine to Susan...",gift_item)
        #Add text

    elif gift_item == adult_mag_ITEM:
        call give_gift(">You give the adult magazine to Susan...",gift_item)
        #Add text

    elif gift_item == porn_mag_ITEM:
        call give_gift(">You give the porn magazine to Susan...",gift_item)
        #Add text

    elif gift_item == krum_poster_ITEM:
        call give_gift(">You give the poster to Susan...",gift_item)
        #Add text

    elif gift_item == sexy_lingerie_ITEM:
        call give_gift(">You give the lingerie to Susan...",gift_item)
        #Add text

    elif gift_item == sexy_stockings_ITEM :
        call give_gift(">You give the stockings to Susan...",gift_item)
        #Add text

    elif gift_item == pink_condoms_ITEM:
        call give_gift(">You give the condoms to Susan...",gift_item)
        #Add text

    elif gift_item == vibrator_ITEM:
        call give_gift(">You give the vibrator to Susan...",gift_item)
        #Add text

    elif gift_item == anal_lube_ITEM:
        call give_gift(">You give the anal lube to Susan...",gift_item)
        #Add text

    elif gift_item == ballgag_and_cuffs_ITEM:
        call give_gift(">You give the handcuffs to Susan...",gift_item)
        #Add text

    elif gift_item == anal_plugs_ITEM:
        call give_gift(">You give the anal plugs to Susan...",gift_item)
        #Add text

    elif gift_item == testral_strapon_ITEM:
        call give_gift(">You give the strap-on to Susan...",gift_item)
        #Add text

    elif gift_item == broom_2000_ITEM:
        call give_gift(">You give the broom to Susan...",gift_item)
        #Add text

    elif gift_item == sexdoll_ITEM:
        call give_gift(">You give the doll to Susan...",gift_item)
        #Add text

    elif gift_item == anal_beads_ITEM:
        call give_gift(">You give the anal beads to Susan...",gift_item)
        #Add text

    elif gift_item == wine_ITEM:
        call give_gift(">You give the wine to Susan...", gift_item)
        #Add text

    elif gift_item == firewhisky_ITEM:
        call give_gift(">You give the firewhisky to Susan...", gift_item)
        #Add text


    hide screen susan_main
    with d5
    call sus_main(xpos="base",ypos="base",trans=d5)

    jump susan_requests

label sus_mood(value=0):
    show screen blktone
    with d3

    if value > 0:
        if value == 1:
            "Susan's mood worsened slightly."
        else:
            "Susan's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Susan's mood has improved slightly."
        else:
            "Susan's mood has improved significantly."
    else:
        "Susan's mood hasn't changed."

    $ was_negative = sus_mood > 0
    $ sus_mood = max(min(sus_mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, sus_mood, value)

    hide screen blktone
    return
