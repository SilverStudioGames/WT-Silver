
screen weasley_store_room():
    tag room_screen

    if game.daytime:
        add "images/rooms/weasley_store/store_day.webp"
    else:
        add "images/rooms/weasley_store/store_night.webp"

    use ui_top_bar

    zorder 0

label open_weasley_store:
    show screen blkfade
    with d3

    call room("weasley_store")
    call gen_chibi("hide")

    call play_music("weasley_store")

    if store_intro_done:
        call gen_chibi("stand", "left", "base")
        call hide_blkfade
    else:
        call gen_chibi("stand", 0, "base")
        call hide_blkfade

        call gen_walk("left", "base")

    pause.2

    #$ renpy.block_rollback()

    call store_chit_chat

    $ store_category = 0 # Reset Button
    $ store_menu = True #Displays item's gold value.
    $ transit_time = renpy.random.randint(1, 5)
    $ store_cart = {}

    jump gift_shop_menu

label store_chit_chat:
    if not store_intro_done:
        $ store_intro_done = True
        fre "Professor Dumbledore? What are you doing here? I thought you didn't leave your office anymore."
        ger "You're not here to shut us down are you?"
        m "Shut you down? What for?"
        fre "NOTHING!"
        # ger "We certainly aren't selling potions that we stole from Snape."
        fre "No prohibited goods being sold here."
        ger "None at all!"
        fre "But if we did sell them--"
        ger "--Which we don't--"
        fre "They would be sold at the best prices in the school."
        ger "Unbeatable."
        # m "Hmmmm. What sort of potions are you \'not\' selling?"
        # fre "Well we aren't selling polyjuice potion."
        # ger "Wouldn't dream of it."
        m "What sort of items are you \"not selling\"?"
        ger "We have books, treats, and knick-knacks for sale."
        fre "Take a look."

    # After talking to Snape about Cho.
    # If you haven't yet beaten the Quiz.
    elif ss_he.cho_E1 and quidditch_book_1_ITEM.unlocked == False and cho_quiz.complete == False:
        m "Boys..."
        twi "Hello again mister Dumbledore sir..."
        ger "What can we do for you?"
        m "Just having a look around at your fine merchandise..."
        fre "If you're worried, don't be... Everything is completely above board and procured from totally legitimate sources."
        ger "No stolen goods here..."
        m "I wasn't looking out for stolen goods in particular, should I?"
        ger "Oh, well..."
        ger "Of course you weren't..."
        m "Seems like I can't find what I'm looking for anyway..."
        fre "Well, if you're looking for something in particular then we could always look into procuring said item."
        ger "What type of object are you looking for?"
        m "Well... as you boys may know, the Quidditch season is starting soon..."
        fre "Yes?"
        m "Well, I realised that I haven't actually gone in depth with the sport yet."
        fre "I find that hard to believe... You're telling me that {b}the{/b} Dumbledore doesn't know anything about Quidditch?"
        ger "Explains why you'd always just stare out in the distance and just clap politely..."
        m "I was always more fond of Basketball myself."
        fre "Sounds like the muggle sport our dad always goes on about..."
        fre "But in any case, since both George and I are on the Gryffindor team."
        m "You are?"
        ger "Yes... don't you keep any kind of records on these things?"
        m "Of course, I'm just... forgetful when it comes to names, that's all."
        ger "Understandable..."
        m "But, as I said, I'd like to get a run-through of the basics of Quidditch this year."
        m "You don't happen to have a Quidditch book to refresh my memories?"
        fre "Of course, you can have ours. We know it off by heart at this point!"

        $ quidditch_book_1_ITEM.unlocked = True
        $ quidditch_book_1_ITEM.unlockable = False # Makes it clickable in the menu.
        call give_gift(">You have unlocked a new book to read!", quidditch_book_1_ITEM)

        m "Great, thanks again boys..."
        twi "Don't mention it..."
        twi "Make sure to take notes!"
        m "Are you assuming your headmaster doesn't know how studying works?"
        fre "Of course not..."
        #ger "Anyway... if you need anything else we should have another book coming in at some point which is not just about the basics of Quidditch..."

    elif deck_unlocked and her_know_cards and not twins_know_cards:
        m "Hello boys."
        twi "Good day professor\nDumbledore, sir."
        m "I'm looking to acquire some Wizard cards."
        call play_sound("spit")
        fre "Wizard cards....*spit*"
        ger "Why would you want any of those?"
        m "What does one do with playing cards... play the game of course."
        fre "Well, we got some of our own to see if it was worth stocking them, but none for sale."
        ger "The profit margin was way to low... something about import tax."
        ger "We would have to sell a lot of them to make good profit."
        m "I see... so there's no way you'd stock them?"
        fre "Wizard cards hasn't been popular in ages..."
        ger "It does have potential though, not everyone at Hogwarts is going to be into dueling... or chess."
        fre "How about this... we did acquire a set of cards to try the game out."
        m "So..."
        ger "If you beat us we'll do a trial run and stock some cards for the students."
        twi "\"There's no way this\nold man would ever beat us.\""
        $ twins_know_cards = True
        jump twins_duel_menu

    elif twins_cards_stocked and not twins_second_win and not twins_cards_stocked_talk:
        m "Well, well. Looking good as always boys!"
        twi "..."
        m "In a professional sense that is, don't you worry... How are things going?"
        ger "Ah, yes... you were right sir, we've seemed to have struck gold with Wizard Cards."
        g9 "Glad to hear it."
        fre "In fact, we've sold out on our first batch."
        g4 "What, where am I supposed to get my cards then?"
        ger "Surely a professional like you would only need to win your cards?"
        m "Oh... yes of course, a professional like me..."
        fre "Anyway, we've gone ahead and put up a official unofficial tier system ladder."
        m "Unofficial... Official, you say?"
        ger "Yes, as we mentioned... there isn't really any official tournament rules."
        fre "We've sort of kept it that way in that we'll let the people playing set their own wagers and challenges to climb the ladder."
        fre "Any normal game will make you one token richer and once the agreed upon winning conditions for a challenge is reached you'll get three tokens."
        ger "And whatever other forfeit your opponent might have added."
        fre "Three challenges won will let you climb to the next tier."
        ger "Which lets you challenge even higher skilled players."
        m "And by skilled you mean players with better cards?"
        fre "Something like that."
        m "I see..."
        m "How do I know which players are currently in my tier?"
        fre "Ah yes, there's a notice board behind us. You should see some people that you know on it."
        ger "Snape was in here earlier to pick up some tokens."
        m "Snape was in here, he doesn't disapprove of your business?"
        fre "He was using a polyjuice potion to disguise himself as a student."
        ger "But that weird walk of his where he sort of slides across the floor gives him away a mile off."
        fre "Tell you what, let's set a wager right now. Usually we'd make it a bit more difficult but since you gave us the idea for this."
        ger "Beat us again and we'll give you three tokens."
        m "That's it? Sounds a bit out of character for you guys making it this easy."
        fre "Let's call it an insurance so that we can continue our business."
        ger "There's no way you'll beat us again anyway."
        $ twins_cards_stocked_talk = True
        jump twins_duel_menu

    else:
        if twins_interest:
            $ twins_interest = False
            twi "Greetings Dumbledore, sir!"
            m "Hello boys."
            m "I'm here to pick up my weekly cut of profits."
            twi "Of course!"

            $ her_help = 0
            if her_shop_help:
                ger "Miss Granger has helped us with promotions this week so that means more profits."
                $ her_help = 200
                $ her_shop_help = False

            $ shop_profit = renpy.random.randint(50+her_help, 300)
            ger "Here, your weekly cut."
            call give_reward("You've received "+str(int(shop_profit*twins_profit))+" gold.", "interface/icons/gold.webp")

            $ game.gold += int(shop_profit*twins_profit)
            ger "..."
            twi "Did you need anything else?"

        else:
            twi "Hello Professor! Came here to buy?"

        if twins_know_cards:
            twi "Or duel?"
            label twins_menu:
            menu:
                "-Buy something-":
                    pass
                "-Let's duel- {image=interface/icons/small/cards.webp}":
                    label twins_duel_menu:
                    if geniecard_level < 2:
                        menu:
                            "-First Duel-":
                                jump twins_first_duel
                            "-Challenge-" if twins_first_win:
                                jump twins_second_duel
                            "-You need to beat the first duel-" (style="disabled") if not twins_first_win:
                                jump twins_duel_menu
                            "-Never mind-":
                                twi "Your loss professor."
                                pass
                    else:
                        jump twins_random_duel

    return

label close_weasley_store:
    hide screen weasley_store_menu
    hide screen list_menu
    hide screen gift
    with d1

    menu:
        ger "Are you finished professor?"

        "-Yes-":
            pass
        "-No-":
            jump gift_shop_menu

    if store_cart:
        if transit_time > 1:
            menu:
                fre "Would you like to add a next-day delivery service?"
                "\"Yes, please. (25 gold)\"" if game.gold >= 25:
                    $ game.gold -= 25
                    $ transit_time = 1
                "\"Yes, please. (25 gold)\"" (style="disabled") if game.gold < 25:
                    ger "It would appear you have spend all your money, Professor."
                    fre "I'm afraid you will have to wait a while longer for your delivery."
                    m "(Greedy bastards...)"
                "-No thanks-":
                    pass

        $ _tmp = "tomorrow." if transit_time == 1 else "in 1 to {} days.".format(str(transit_time))

        fre "Thank your for shopping at \"Weasley & Weasley\". Your order shall be delivered [_tmp]"
    else:
        ger "We get new goods every week--"
        fre "--maybe we'll have something you like next time."

    twi "Goodbye!"

    show screen blkfade
    with d5

    python:
        store_menu = False #Displays item's gold value.

        Parcel(contents=[(k, v) for k, v in store_cart.iteritems()], wait=transit_time).send()

        store_cart = {}

    jump main_room

screen weasley_store_menu():
    tag store_menu
    zorder 6

    vbox:
        pos (825, 120)
        spacing 5

        button:
            xysize (84, 34)
            idle_background gui.format("interface/general/{}/button_select.webp")
            hover_background gui.format("interface/general/{}/button_select_hover.webp")

            text "Gifts" align (0.5, 0.5) size 16
            action [SetVariable("store_category", 0), Jump("gift_shop_menu")]

        button:
            xysize (84, 34)
            idle_background gui.format("interface/general/{}/button_select.webp")
            hover_background gui.format("interface/general/{}/button_select_hover.webp")

            text "Books" align (0.5, 0.5) size 16
            action [SetVariable("store_category", 1), Jump("book_shop_menu")]

        #button:
            #xysize (84, 34)
            #idle_background gui.format("interface/general/{}/button_select.webp")
            #hover_background gui.format("interface/general/{}/button_select_hover.webp")

            #text "Potions" align (0.5, 0.5) size 16
            #action [SetVariable("store_category", 2), Jump("shop_potion_menu")]

        if twins_cards_stocked:
            button:
                xysize (84, 34)
                idle_background gui.format("interface/general/{}/button_select.webp")
                hover_background gui.format("interface/general/{}/button_select_hover.webp")

                text "Tokens" align (0.5, 0.5) size 16
                action [SetVariable("store_category", 3), Jump("token_shop_menu")]

#Gifts
label gift_shop_menu:
    show screen weasley_store_menu

    $ item_list = filter(lambda x : x.unlocked, Item.get_instances_of_type("gift"))

    show screen list_menu("gift_shop_menu", "Gifts", ("Beverages", "Candy", "Mags", "Toys"), item_list)
    with d3

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, Item):
        call object_gift_block(_return)
        jump gift_shop_menu

    elif _return == "Close":
        jump close_weasley_store

    jump .interact


label object_gift_block(item):
    hide screen weasley_store_menu
    hide screen list_menu
    $ the_gift = item.get_image()
    show screen gift
    with d3

    ">[item.description]"
    $ cost2 = item.cost * 2
    $ cost3 = item.cost * 4
    $ cost4 = item.cost * 8

    menu:
        "-Buy 1 for ([item.cost] gold)-":
            call object_purchase_item(item, 1)
        "-Buy 2 for ([cost2] gold)-":
            call object_purchase_item(item, 2)
        "-Buy 4 for ([cost3] gold)-":
            call object_purchase_item(item, 4)
        "-Buy 8 for ([cost4] gold)-":
            call object_purchase_item(item, 8)
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return

label object_purchase_item(item, quantity):
    $ order_cost = item.cost*quantity
    if game.gold >= (order_cost):
        $ game.gold -= order_cost

        $ store_cart.setdefault(item, 0)
        $ store_cart[item] += quantity
    else:
        m "I don't have enough gold."

    hide screen gift
    with d3

    return



#Books & Scrolls
label book_shop_menu:
    if not book_store_intro_done:
        hide screen weasley_store_menu
        hide screen list_menu
        with d3

        fre "These books are mostly light erotica..."
        ger "Some of the girls insisted that I order them in."
        $ book_store_intro_done = True
        pause.5

    show screen weasley_store_menu

    $ item_list = [filter(lambda x: not (x.unlocked or x.unlockable), y) for y in [
        book_list.fiction_books,
        book_list.read_books + book_list.write_books,
        forbidden_scroll_list + scroll_list_A + scroll_list_B + scroll_list_C
    ]]

    show screen list_menu("book_shop_menu", "Books & Scrolls", ("Fictional", "Educational", "Scrolls"), item_list)
    with d3

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, Item):
        if _return.type == "book":
            call purchase_book(_return)
        elif _return in forbidden_scroll_list:
            call purchase_forbidden_scroll(_return)
        else:
            call purchase_scroll(_return)
        jump book_shop_menu

    elif _return == "Close":
        jump close_weasley_store

    jump .interact

    jump book_shop_menu

label purchase_book(item):
    hide screen weasley_store_menu
    hide screen list_menu
    $ the_gift = item.get_image()
    show screen gift
    with d3
    ">[item.description]"
    menu:
        "-Buy the book for [item.cost] gold -":
            if game.gold >= item.cost:
                $ game.gold -= item.cost
                $ item.unlocked = True
                "Book [item.name] has been added to your collection."
            else:
                m "I don't have enough gold."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return

label purchase_forbidden_scroll(item):
    hide screen weasley_store_menu
    hide screen list_menu
    with d3

    if not hg_sex.trigger:
        m "What's in this scroll?"
        ger "Don't worry about it."
        m "Why?"
        ger "You're not ready for what's in this scroll."
        m "Well, that just makes me want it more."
        ger "Too bad, professor."
        m "(Perhaps I should check it out later...)"
        return

    m "What's this scroll?"
    fre "It is one of the components needed for a forbidden spell."
    ger "Acquired completely legitimately I might add!"
    m "What does it do?"
    fre "It transforms you into... something."
    m "Like what?"
    fre "We don't know, it could be anything."
    ger "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe inspiring dragon."
    m "Not sure I'd really want to transform into any of those..."
    ger "Well... those are just theories, we've not been able to use the scroll to find the second component ourselves."
    m "Really? Now that's is surprising."
    fre "Yes, although it's blank for some reason... not really anything new to us as we used to have a ma--"
    ger "massive amounts of scrolls just like this one!"
    ger "Yep... lot's of them, shame they all burnt."
    fre "What are you-- *HHNG*"
    fre "Oh! I see... Yes, very unfortunate..."
    m "That is unfortunate... Well I'm sure I'll manage."
    m "Ok, well how much is the scroll?"
    ger "Five hundred gold coins."
    g4 "Five hundred!? Why on earth is it so expensive?"
    fre "Forbidden magic is quite a risky and expensive endeavour Professor, We'll sell it for no less than five hundred."

    menu:
        "-Buy the scroll ([item.cost] gold)":
            if game.gold >= item.cost:
                m "Fine, here's the money"
                ger "Thank you very much"
                $ the_gift = item.get_image()
                show screen gift
                with d3
                $ game.gold -= item.cost
                $ item.unlocked = True
                call update_quest_items
                ">Forbidden scroll has been added to your inventory."
                hide screen gift
                with d3
            else:
                m "I don't have enough gold."
                fre "Perhaps later then."
        "-No thanks-":
            m "No thanks, not right now."
            fre "Perhaps later then."

    return

label purchase_scroll(item):
    hide screen weasley_store_menu
    hide screen list_menu
    $ the_gift = item.get_image() # SACRED SCROLL.
    show screen gift
    with d3
    ">A scroll containing sacred knowledge.\n(May also contain spoilers)."
    menu:
        "-Buy the scroll ([item.cost] gold)-":
            if game.gold >= item.cost:
                $ game.gold -= item.cost
                $ item.unlocked = True
                ">A New scroll has been added to your sacred scrolls collection."
            else:
                m "I don't have enough gold."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return



label shop_potion_menu:
    hide screen weasley_store_menu
    hide screen list_menu
    with d3

    python:
        potion_menu = []
        potion_menu.append(("-Questions acquiring items-", "questions"))
        for potion in potion_lib.get_buyables():
            if her_whoring < potion.whoring_rec:
                potion_menu.append(gui.menu_item(potion.name, "her_whoring", style="disabled"))
            else:
                potion_menu.append(("-"+potion.name+"-",potion))
        potion_menu.append(("-Never mind-", "nvm"))
        potion_choice = renpy.display_menu(potion_menu)
    if isinstance(potion_choice, Potion):
        python:
            potion_menu = []
            potion_menu.append(("-Buy the potion for "+str(potion_choice.cost)+" Gold-", potion_choice))
            potion_menu.append(("-Never mind-", "nvm"))
            choice = renpy.display_menu(potion_menu)
        if isinstance(choice, Potion):
            if game.gold >= potion_choice.cost:
                $ game.gold -= potion_choice.cost
                $ potion_inv.add(potion_choice.id)
                $ renpy.say(m, potion_choice.name+" acquired, although it's missing a key ingredient...")
            else:
                $ renpy.say(m, "I don't have enough gold.")
        jump shop_potion_menu
    if potion_choice == "questions":
        menu:
            "-Knotgrass-":
                m "Do you know where I can find \"Knotgrass\"?"
                fre "You can sometimes find Knotgrass by the forbidden forest."
            "-Root of Aconite-":
                m "Do you know where I can find \"Root of Aconite\"?"
                ger "Root of Aconite can be found down by the lake."
            "-Wormwood-":
                m "Do you know where I can find \"Wormwood\"?"
                ger "Wormwood is sometimes found in the forbidden forest."
            "-Niffler's Fancy-":
                m "Do you know where I can find \"Niffler's Fancy\"?"
                fre "*Hmm*... I think I heard that it's found by the lake."
        jump shop_potion_menu
    if potion_choice == "her_whoring":
        "Hermione must be \"Trained\" more before you can purchase this."
    if potion_choice == "nvm":
        pass
    $ store_category = 0
    jump gift_shop_menu




# Token Shop
label token_shop_menu:
    show screen weasley_store_menu

    $ item_list = [filter(lambda x: not (x.hidden or x.unlocked), y) for y in [
        [hg_poker],
        fireplace_deco_list+cupboard_deco_list+wall_deco_list+misc_deco_list+misc_hat_list,
        [lootbox_quest_ITEM]
    ]]

    show screen list_menu("token_shop_menu", "Token Shop", ("Outfits", "Decorations", "Other"), item_list)
    with d3

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, Item):
        call purchase_deco(_return)
        jump token_shop_menu

    elif _return == "Close":
        jump close_weasley_store

    jump .interact

label purchase_deco(item):
    hide screen weasley_store_menu
    hide screen list_menu
    $ the_gift = item.get_image()
    show screen gift
    with d3
    ">[item.description]"

    if item.type == "outfit_token":
        $ item_token_str = "A new \"%s\" outfit has been added to Hermione's wardrobe." % item.name
        $ item_token_type = " outfit"
    elif item.type == "quest item":
        $ item_token_str = "\"%s\" has been added to your quest items." % item.name
    else:
        $ item_token_str = "%s has been added to your decoration menu." % item.type
        $ item_token_type = ""
    menu:
        "-Buy [item.name][item_token_type] for [item.cost] tokens -" if not item.type == "quest item":
            if tokens >= item.cost:
                $ tokens -= item.cost
                $ item.unlocked = True
                "[item_token_str]"

                if len(filter(lambda x: x.unlocked==False, wall_deco_list)) <= 0:
                    $ achievement.unlock("postman")
                if len(filter(lambda x: x.unlocked==False, misc_hat_list)) <= 0:
                    $ achievement.unlock("hats")
            else:
                m "I don't have enough tokens."
        "-Buy [item.name] for [item.cost] gold coins -" if item.type == "quest item":
            if game.gold >= item.cost:
                $ game.gold -= item.cost
                $ item.owned += 1
                call update_quest_items
                "[item_token_str]"
            else:
                m "I don't have enough gold."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return
