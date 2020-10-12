# Astoria Gift Responses

label give_ast_gift(gift_item):
    $ gave_astoria_gift = True
    hide screen astoria_main
    with d5
    call ast_main(xpos="mid", ypos="base", trans=d5)

    if gift_item == lollipop_ITEM:

        if ast_whoring < 6:
            call ast_main("A lollipop?", mouth="open", face="neutral")
            call ast_main("Why are you giving me sweets, I'm not a kid!", face="angry")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("A lollipop?", mouth="open", face="neutral")
            call give_gift(">You give the lollipop to Astoria...", gift_item)
            call ast_main("why are you being so nice to me...", face="angry")
            call ast_main("Although... the other students haven't had any left since the last Hogsmeade trip.", mouth="open", face="neutral")
            call ast_main("They'll be so jealous!", mouth="grin", face="happy")
            call ast_mood(-1)
        else:
            call ast_main("A lollipop?", mouth="open", face="neutral")
            call give_gift(">You give the lollipop to Astoria...", gift_item)
            call ast_main("That's going to take all day to suck on...")
            call ast_main("I guess my mouth will be too busy to do anything else for the entire day!")
            call ast_mood(-2)

    elif gift_item == chocolate_ITEM:

        if ast_whoring < 6:
            call ast_main("Some chocolate?", mouth="open", face="neutral")
            call ast_main("Don't you have any dung-bombs?")
            call ast_main("They're way more fun!")
            call ast_mood(0)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Some chocolate?", mouth="open", face="neutral")
            call give_gift(">You give the chocolate to Astoria...", gift_item)
            call ast_main("Thank you, [ast_genie_name].",mouth="open",face="neutral")
            call ast_main("I don't know what I did to deserve it.",mouth="annoyed",pupils="R",face="neutral")
            call ast_main("But I'm not going to say no...",face="happy")
            call ast_mood(-1)
        else:
            call ast_main("Some chocolate?", mouth="open", face="neutral")
            call give_gift(">You give the chocolate to Astoria...", gift_item)
            call ast_main("Did you hear chocolate is supposed to be an aphrodisiac?")
            call ast_main("Although it was a muggle that came up with that one so I doubt there's any truth to it.")
            call ast_main("Oh well, that sucks doesn't it?")
            call ast_mood(-2)

    elif gift_item == plush_owl_ITEM:

        if ast_whoring < 6:
            call ast_main("An owl plushie?", mouth="open", face="neutral")
            call ast_main("Why are you giving me this?")
            call ast_main("Toys are for children...")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("An owl plushie?", mouth="open", face="neutral")
            call give_gift(">You give the stuffed toy to Astoria...", gift_item)
            call ast_main("I don't use stuffed toys...", mouth="open", face="annoyed")
            call ast_main("I know someone that hates owls though... I'll put this in front of her face when she's waking up...", mouth="annoyed", pupils="R", face="neutral")
            call ast_mood(-1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("An owl plushie?", mouth="open", face="neutral")
            call give_gift(">You give the stuffed toy to Astoria...", gift_item)
            call ast_main("Do I look like a girl that plays with toys?")
            call ast_main("Actually, don't answer that...")
            call ast_main("Guess it'd be rude not to take it...")
            call ast_mood(-1)
        else:
            call ast_main("An owl plushie?", mouth="open", face="neutral")
            call give_gift(">You give the stuffed toy to Astoria...", gift_item)
            call ast_main("If you want to give me toys you better be prepared for me to call you daddy...")
            call ast_main("So, thank you...")
            call ast_main("Daddy...")
            call ast_mood(-3)

    elif gift_item == butterbeer_ITEM:

        if ast_whoring < 6:
            call ast_main("Butterbeer?", mouth="smile", face="happy")
            call give_gift(">You give the bottle to Astoria...", gift_item)
            call ast_main("Time to get smashed!", face="happy")
            call ast_main("The other students will be so jealous I got beer into the school...", mouth="annoyed", face="angry")
            call ast_mood(-2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Butterbeer?", mouth="smile", face="happy")
            call give_gift(">You give the bottle to Astoria...", gift_item)
            call ast_main("Don't you have something stronger?", pupils="mid", face="annoyed")
            call ast_main("Like something you can't get in the school usually?", pupils="R", face="annoyed")
            call ast_main("Fine, I'll take it!", mouth="smile", face="happy")
            call ast_mood(-1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Butterbeer?", face="annoyed")
            call give_gift(">You give the bottle to Astoria...", gift_item)
            call ast_main("This watered down piss-water can barely get a house elf tipsy.")
            call ast_main("Actually, that gives me an idea...")
            call ast_mood(-1)
        else:
            call ast_main("Butterbeer?", mouth="open", face="neutral")
            call give_gift(">You give the bottle to Astoria...", gift_item)
            call ast_main("It's more of a cider really isn't it?", face="neutral")
            call ast_main("Thanks!", mouth="smile", face="happy")
            call ast_mood(-2)

    elif gift_item == science_mag_ITEM:
        if ast_whoring < 6:
            call ast_main("(...)", pupils="down", face="annoyed")
            call ast_main("Creating your own itch powder using household ingredients?", mouth="open", pupils="down", face="annoyed")
            call ast_main("Is the kitchen even open to students?", pupils="down", face="annoyed")
            call ast_main("What am I supposed to do with this, [ast_genie_name]?", face="annoyed")
            call ast_mood(0)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Magazines?", mouth="open", face="annoyed")
            call give_gift(">You give an assortment of educational magazines to Astoria...", gift_item)
            call ast_main("Making your own stink bombs...", face="annoyed")
            call ast_main("Looks like I might be able to make these in potions class...")
            call ast_main("If Snape doesn't catch me doing it.", mouth="clench", face="annoyed")
            call ast_mood(-1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Magazines?", mouth="angry", face="angry")
            call ast_main("You want me to do more school work?", mouth="annoyed", face="angry")
            call ast_mood(1)
        else:
            call ast_main("magazines?", mouth="open", face="annoyed")
            call give_gift(">You give an assortment of educational magazines to Astoria...", gift_item)
            call ast_main("I was hoping for something a bit more risqué...", face="annoyed")
            call ast_mood(0)

    elif gift_item == girls_mag_ITEM:
        if ast_whoring < 6:
            call ast_main("Girl magazines?", mouth="open", face="annoyed")
            call ast_main("This is that trash my sister reads.", mouth="clench", pupils="down", face="annoyed")
            call ast_main("Such a massive waste of time...", face="annoyed")
            call ast_mood(0)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Girl magazines?", face="disgusted")
            call give_gift(">You give an assortment of rather girly magazines to Astoria...", gift_item)
            call ast_main("I'll take it for the free mascara sample. I once drew a uni-brow on someone with it.", face="happy")
            call ast_mood(-1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Girl magazines?", face="annoyed")
            call give_gift(">You give an assortment of rather girly magazines to Astoria...", gift_item)
            call ast_main("Well, I am a girl so of course I'd want it!", face="annoyed")
            call ast_mood(-1)
        else:
            call ast_main("Girl magazines?", face="annoyed")
            call give_gift(">You give an assortment of rather girly magazines to Astoria...", gift_item)
            call ast_main("Don't I look hot enough for you [ast_genie_name]?", mouth="open", eyes="closed", face="annoyed")
            call ast_main("I'm just teasing you, I'll have it.", face="happy")
            call ast_mood(-1)

    elif gift_item == adult_mag_ITEM:
        if ast_whoring < 6:
            call ast_main("Adult magazines?", mouth="clench", face="disgusted")
            call ast_main("I'm good thanks.", face="disgusted")
            call ast_mood(0)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Adult magazines?", face="annoyed")
            call give_gift(">You give an assortment of adult magazines to Astoria...", gift_item)
            call ast_main("Of course I read them. I'm an adult after all, it's in the name.", mouth="annoyed", pupils="R", face="angry")
            call ast_mood(-1)
        else:
            call ast_main("Adult magazines?", face="annoyed")
            call give_gift(">You give an assortment of adult magazines to Astoria...", gift_item)
            call ast_main("This is that magazine Tonks was reading during our writing test...", pupils="down", face="annoyed")
            call ast_main("Perhaps I'll wave it at her so she thinks I stole it...", mouth="smile", pupils="mid", face="angry")
            call ast_mood(-1)

    elif gift_item == porn_mag_ITEM:
        if ast_whoring < 6:
            call ast_main("Porn magazines?", face="disgusted")
            call give_gift(">You give an assortment of pornographic magazines to Astoria...", gift_item)
            call ast_main("I'll take it!", mouth="grin", face="happy")
            call ast_main("I'll put one in Susan's bag when she's not looking. Can't wait to see that cows face when her friends notice.", mouth="open", face="angry")
            call ast_main("Thank you, [ast_genie_name].", face="happy")
            call ast_mood(-1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Porn magazines?", face="annoyed")
            call ast_main("Why do you have these?", face="annoyed")
            call ast_main("Give them to Susan...", pupils="R", face="annoyed")
            call ast_mood(0)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Porn magazines?", face="annoyed")
            call give_gift(">You give an assortment of pornographic magazines to Astoria...", gift_item)
            call ast_main("That's some extreme stuff you got there...", face="disgusted")
            call ast_main("BDSM, what does that stand for...", pupils="down", face="disgusted")
            call ast_main("She looks like she's enjoying it. That's not fun...")
            call ast_main("Although...")
            call ast_mood(-1)
        else:
            call ast_main("Porn magazines?", face="happy")
            call give_gift(">You give an assortment of pornographic magazines to Astoria...", gift_item)
            call ast_main("Is this where you get your ideas from?", face="angry")
            call ast_main("A swing? Why would you have that in a porn ma... oh there's the next page.", pupils="down", face="disgusted")
            call ast_main("Yeah fuck it, give it here...", mouth="grin", face="angry")
            call ast_mood(-2)

    elif gift_item == krum_poster_ITEM:
        if ast_whoring < 6:
            call ast_main("Viktor Krum?", face="annoyed")
            call ast_main("Is that the Quidditch player everyone seems to fancy?", mouth="open", pupils="mid", face="annoyed")
            call give_gift(">You give the poster to Astoria...", gift_item)
            call ast_main("*Hmph*, I guess I'll take it if he's that popular...", mouth="annoyed", pupils="R", face="neutral")
            call ast_mood(0)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Viktor Krum?", face="annoyed")
            call ast_main("Bet he could crush m... someone with his bare hands.", face="disgusted")
            call ast_main("Give it here...", face="happy")
            call give_gift(">You give the poster to Astoria...", gift_item)
            call ast_mood(-1)
        else:
            call ast_main("Viktor Krum?", face="happy")
            call ast_main("His trousers aren't even off. What's the point...", face="angry")
            call ast_mood(1)

    elif gift_item == sexy_lingerie_ITEM:
        if ast_whoring < 6:
            call ast_main("Lingerie?", face="disgusted")
            call ast_main("Sexy Lingerie?!?")
            call ast_main("Why do you care so much about what I wear? Isn't this shitty school uniform enough for you?", face="angry")
            call ast_mood(2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Lingerie?", mouth="open", face="neutral")
            call ast_main("I... No, I'd just end up looking like a tramp!", face="angry")
            call ast_mood(0)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Lingerie?", face="annoyed")
            call ast_main("Sexy...", pupils="down", face="annoyed")
            call ast_main("Why not, I don't know if you could tell but I'm a bit of a rebel. Might even wear these in class.", mouth="grin", face="angry")
            call give_gift(">You give the sexy lingerie to Astoria...", gift_item)
            call ast_mood(-1)
        else:
            call ast_main("Lingerie?", face="annoyed")
            call give_gift(">You give the sexy lingerie to Astoria...", gift_item)
            call ast_main("Is this is the kind of clothes you want your students to dress in from now on?", face="annoyed")
            call ast_main("*Heh*- I don't blame you, the school uniform is the most basic piece of trash ever without some spice...", face="annoyed")
            call ast_mood(-1)

    elif gift_item == sexy_stockings_ITEM :
        if ast_whoring < 6:
            call ast_main("Stockings?", face="disgusted")
            call ast_main("What happened to the dress code at this place?")
            call ast_main("What next, shorter skirts?", face="angry")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Stockings?", mouth="open", face="neutral")
            call give_gift(">You give the stockings to Astoria...", gift_item)
            call ast_main("Seems pretty elastic... I could totally lob some stink bombs with these.", mouth="grin", face="angry")
            call ast_mood(-1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("Stockings?", face="annoyed")
            call ast_main("Hah, you fool! With these you wont be able to stare at my legs anymore!", mouth="grin", face="angry")
            call give_gift(">You give the stockings to Astoria...", gift_item)
            call ast_mood(-2)
        else:
            call ast_main("Stockings?", face="annoyed")
            call ast_main("These are almost as see-through as your wicked intentions...", mouth="grin", face="angry")
            call give_gift(">You give the stockings to Astoria...", gift_item)
            call ast_main("Disgusting...", face="angry")
            call ast_mood(-1)

    elif gift_item == pink_condoms_ITEM:
        if ast_whoring < 6:
            call ast_main("Condoms?", face="disgusted")
            call ast_main("Yeah, no... I'll take them but there's not going to be any dick going near these bad boys...", face="annoyed")
            call ast_main("These will be the perfect thing to fill with water and drop down the staircase...", mouth="smile", face="angry")
            call give_gift(">You give the pack of Condoms to Astoria...", gift_item)
            call ast_main("Cheers for the ammo, [ast_genie_name].", face="happy")
            call ast_mood(-2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Condoms?", face="neutral")
            call ast_main("Oh, thank you so much! I'll prick some holes in these and hand them out at once!", mouth="grin", face="angry")
            call ast_main("What?", face="annoyed")
            call ast_main("I see your concern... They probably would be able to trace it back to me.", face="annoyed")
            call ast_main("Oh well, a gift is a gift.", face="neutral")
            call give_gift(">You give the pack of Condoms to Astoria...", gift_item)
            call ast_mood(0)
        else:
            call ast_main("Condoms?", face="annoyed")
            call ast_main("Why would I need condoms when I could just go in raw?", mouth="grin", face="angry")
            call ast_main("*Ha-Ha-Hah* The look on your face, now that's something money can't buy.", face="happy")
            call give_gift(">You sheepishly give the pack of Condoms to Astoria...", gift_item)
            call ast_main("*Hmm*.... yeah why not.", face="neutral")
            call ast_mood(-1)

    elif gift_item == vibrator_ITEM:
        if ast_whoring < 6:
            call ast_main("A vibrator?", face="disgusted")
            call ast_main("Gross, where did you even get that from?", face="angry")
            call ast_mood(2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("A vibrator?", face="disgusted")
            call ast_main("Get the fuck out...", face="angry")
            call ast_main("Oh right, I'm in your office... yeah that's going to be solid no on that one.", face="annoyed")
            call ast_mood(1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("A vibrator?", face="disgusted")
            call ast_main("Hold on a second, that's the noise I've been hearing in the girls chambers!", face="happy")
            call ast_main("Do they work?", face="happy")
            call ast_main("I mean, I'll take it I guess.", face="neutral")
            call give_gift(">You give the vibrator to Astoria...",gift_item)
            call ast_mood(-1)
        else:
            call ast_main("A vibrator?", face="neutral")
            call give_gift(">You give the vibrator to Astoria...",gift_item)
            call ast_main("That's disgusting! What a disgusting old man you are. Well aren't you being disgusting...", face="angry")
            call ast_main("Disgusting...", face="angry")
            call ast_main("Give it here.", face="happy")
            call ast_mood(-2)

    elif gift_item == anal_lube_ITEM:
        if ast_whoring < 6:
            call ast_main("Lube?", mouth="open", face="neutral")
            call ast_main("I know the perfect staircase for this!", face="happy")
            call give_gift(">You give the jar of lube to Astoria...", gift_item)
            call ast_main("Thank you, [ast_genie_name].", face="happy")
            call ast_mood(-1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Anal Lube?", mouth="smile", face="happy")
            call ast_main("Swiggity swooty I'm coming for that booty!", mouth="smile", face="angry")
            call ast_main("Come on now, what's with that dry humour. Maybe you could use some of that lube?", face="annoyed")
            call give_gift(">You cautiously give the jar of lube to Astoria...", gift_item)
            call ast_main("Boo!", face="annoyed")
            call ast_main("*ha-ha-ha*!", face="happy")
            call ast_mood(-2)
        else:
            call ast_main("Anal Lube?", face="happy")
            call give_gift(">You give the jar of lube to Astoria...", gift_item)
            call ast_main("Why would I need this, surely the initial pain is the best part...", face="angry")
            call ast_main("Oh, for me? Duh!", face="annoyed")
            call ast_main("Yeah, actually I'll take it...", face="happy")
            call ast_mood(-2)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if ast_whoring < 6:
            call ast_main("Handcuffs? And what.... a ball gag?", face="disgusted")
            call ast_main("I don't know what you're trying to insinuate.", face="angry")
            call ast_main("The cuffs could be useful but why the ball gag?", face="disgusted")
            call ast_main("I'd rather not.", face="annoyed")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("Handcuffs? And a Ball gag?", face="annoyed")
            call give_gift(">You give the handcuffs to Astoria...", gift_item)
            call ast_main("I can break these cuffs!", face="angry")
            call ast_main("*HNNNNNGH!", face="angry")
            call ast_main("I can't break those cuffs...", face="annoyed")
            call ast_main("Do you have a key?", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("Handcuffs? And a Ball gag?", face="happy")
            call give_gift(">You give the handcuffs to Astoria...", gift_item)
            call ast_main("So I guess these are one of those BDSM items?", face="neutral")
            call ast_main("Colour me intrigued...", face="happy")
            call ast_mood(-1)

    elif gift_item == anal_plugs_ITEM:
        if ast_whoring < 6:
            call ast_main("anal plugs?", face="disgusted")
            call ast_main("Yuck, what the hell is wrong with you... do you know where these go?", face="angry")
            call ast_main("Of course you do... you detestable dingbat.", face="angry")
            call ast_mood(2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("anal plugs?", face="disgusted")
            call ast_main("Why don't you try and sit on one yourself...", face="angry")
            call ast_mood(1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("anal plugs", face="disgusted")
            call give_gift(">You give the anal plugs to Astoria...", gift_item)
            call ast_main("Why are you giving me this?", face="annoyed")
            call ast_main("I'll take it I guess...", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("anal plugs?", face="neutral")
            call give_gift(">You give the anal plugs to Astoria...", gift_item)
            call ast_main("You do know these hurts a bit if you're not used to them?", face="annoyed")
            call nar(">Astoria absent-mindedly pockets the anal plug.")
            call ast_main("Don't see why you'd give these out as if they were sweets...", mouth="annoyed", face="neutral")
            call ast_mood(-1)


    elif gift_item == testral_strapon_ITEM:
        if ast_whoring < 6:
            call ast_main("A strap-on?", face="disgusted")
            call ast_main("Why would you give me this... it's so ribbed...", face="angry")
            call ast_main("As if anyone would want something like that!", face="angry")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("A strap-on?", face="disgusted")
            call ast_main("What do you want me to do with this?", face="annoyed")
            call ast_main("Well I know what you want me to do with it.", face="annoyed")
            call ast_main("It's not happening...", face="angry")
            call ast_mood(0)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("A strap-on?", face="angry")
            call give_gift(">You give the strap-on to Astoria...", gift_item)
            call ast_main("I'll strap it on your forehead and make you into a sex unicorn!", mouth="grin", face="angry")
            call ast_main("I read about people having sex on top of a unicorn...", face="disgusted")
            call ast_main("Bit of an odd segment that one was...", face="annoyed")
            call ast_mood(-1)
        else:
            call ast_main("A strap-on?", face="annoyed")
            call give_gift(">You give the strap-on to Astoria...", gift_item)
            call ast_main("It says Thestral on the side...", face="annoyed")
            call ast_main("Isn't' that the creature only people that has seen someone die can see?")
            call ast_main("That makes the person who made he mould kinda fucked up if you think about it...", face="disgusted")
            call ast_main("I like it...", face="happy")
            call ast_mood(-2)

    elif gift_item == broom_2000_ITEM:
        if ast_whoring < 6:
            call ast_main("A broom?", face="neutral")
            call ast_main("What's that sticking out on the top? That's not going to help me fly!", face="annoyed")
            call ast_mood(1)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("A broom?", face="neutral")
            call give_gift(">You give the broom to Astoria...", gift_item)
            call ast_main("Now if anything will motivate you to fly, that will...", mouth="grin", face="angry")
            call ast_main("Bit awkward during broom care though...", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("A broom?", face="happy")
            call give_gift(">You give the broom to Astoria...", gift_item)
            call ast_main("Now that will keep you sturdy.", mouth="grin", face="angry")
            call ast_main("What a depraved little invention...", mouth="smile", face="angry")
            call ast_main("Totally something I'd come up with!")
            call ast_main("You look sceptical...", face="annoyed")
            call ast_mood(-1)

    elif gift_item == sexdoll_ITEM:
        if ast_whoring < 6:
            call ast_main("A sex doll?", face="disgusted")
            call ast_main("That's gross [ast_genie_name]!", face="angry")
            call ast_main("Yuck, it smells gross too!", face="angry")
            call ast_mood(2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("A sex doll?", face="disgusted")
            call ast_main("This is literally worthless to me, why would you even consider this a good gift?", face="angry")
            call ast_mood(1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("A sex doll?", face="angry")
            call give_gift(">You give the doll to Astoria...", gift_item)
            call ast_main("I hope you got this for cheap. It looks awful...", face="annoyed")
            call ast_main("I mean... why thank you, I shall cherish this forever!", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("A sex doll?", face="disgusted")
            call give_gift(">You give the doll to Astoria...", gift_item)
            call ast_main("But I'm a girl...", face="annoyed")
            call ast_main("I'll leave it in the Slytherin common room to see if anyone has balls enough to takes it...", mouth="grin", face="angry")
            call ast_mood(-1)

    elif gift_item == anal_beads_ITEM:
        if ast_whoring < 6:
            call ast_main("anal beads?", face="disgusted")
            call ast_main("Like, ones that you putt in your ass?", face="angry")
            call ast_main("What... the hell!", face="angry")
            call ast_mood(2)
        elif ast_whoring > 5 and ast_whoring < 12:
            call ast_main("anal beads?", face="disgusted")
            call ast_main("Put it up your own ass and I'll let er rip!", face="angry")
            call ast_mood(1)
        elif ast_whoring > 11 and ast_whoring < 18:
            call ast_main("anal beads?", face="disgusted")
            call ast_main("Why would I need these?", face="annoyed")
            call ast_main("I'll pass...", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("anal beads?", face="neutral")
            call ast_main("Sounds painful", face="annoyed")
            call give_gift(">You give the anal beads to Astoria...", gift_item)
            call ast_main("And they're green... Did you get these made just for me?", mouth="annoyed", face="neutral")
            call ast_mood(-1)

    elif gift_item == wine_ITEM:
        if ast_whoring < 6:
            call ast_main("Wine?", face="disgusted")
            call give_gift(">You give the wine to Astoria...", gift_item)
            call ast_main("You're joking right?", face="annoyed")
            call ast_main("Snape would murder me if he saw me bringing alcohol into the common room.", face="angry")
            call ast_main("I can't make you shut up after hours even without alcohol in your system...", face="annoyed")
            call ast_main("Such a slimy slithering killjoy...", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("Wine?", face="happy")
            call ast_main("Well aren't we fancy?", face="neutral")
            call give_gift(">You give the wine to Astoria...", gift_item)
            call ast_main("This is the real shit. Look at the date on that.", face="neutral")
            call ast_main("You really are ancient if you bought it new...", face="happy")
            call ast_mood(-1)

    elif gift_item == firewhisky_ITEM:
        if ast_whoring < 6:
            call ast_main("Firewhisky?", face="neutral")
            call ast_main("That's the stuff Tonks always reeks off.", face="disgusted")
            call ast_main("I'm not gonna drink whatever she does.", face="annoyed")
            call ast_main("It'd be like wearing old peoples perfume!", face="annoyed")
            call ast_mood(0)
        else:
            call ast_main("Firewhisky?", face="happy")
            call ast_main("Fine, I'll give in. If Tonks likes it so much it can't be that bad...", face="happy")
            call give_gift(">You give the firewhisky to Astoria...", gift_item)
            call ast_main("*Hmm*... not made using real fire.. well that's bloody obvious...", face="neutral")
            call ast_main("Might experience a slight pain and burning sensation when consuming...", face="disgusted")
            call ast_main("Why didn't you say so before!", face="angry")
            call ast_main("I might even take a sip or two myself...", face="happy")
            call ast_mood(-1)

    call ast_main(xpos="base",ypos="base", trans=d5)

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

    $ was_negative = ast_mood > 0
    $ ast_mood = max(min(ast_mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, ast_mood, value)

    hide screen blktone5
    return
