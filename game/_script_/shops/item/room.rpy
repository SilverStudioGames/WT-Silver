screen weasley_store_room():
    tag room_screen

    if game.daytime:
        add "images/rooms/weasley_store/store_day.webp"
    else:
        add "images/rooms/weasley_store/store_night.webp"

    use ui_top_bar

    zorder 0

label item_store:
    show screen blkfade
    with d3

    call room("weasley_store")
    call gen_chibi("stand", 0, "base")
    call gen_walk(xpos="left", ypos="base")
    call play_music("weasley_store")

    hide screen blkfade
    with d3

    if not item_store_intro_done:
        $ item_store_intro_done = True
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

    elif ss_he.cho_E1 and not quidditchguide_ITEM.unlocked and not cho_quiz.complete:
        $ quidditchguide_ITEM.unlocked = True
        # After talking to Snape about Cho.
        # If you haven't yet beaten the Quiz.
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
        fre "Of course, you can have ours--"
        call play_sound("kick")
        with hpunch
        fre "Blimey!"
        ger "What Freddy wanted to say is--"
        ger "You can have ours, for 200 gold coins."
        m "......"
        m "Great, thanks again boys..."
        ger "Don't mention it..."
        fre "...Make sure to take notes!"
        m "Are you assuming your headmaster doesn't know how studying works?"

        call play_sound("kick")
        with hpunch

        fre "*Cries out like a hurt puppy*"
        ger "Of course not, professor, Fred was just joking, right Fred?"
        fre "....Yes sir, just kidding..."
        m "Right..."
        ger "We've put the book in \"Quest Items\" section, can't miss it."

    elif deck_unlocked and her_know_cards and not twins_know_cards:
        m "Hello boys."
        twi "Good day professor\nDumbledore, sir."
        m "I'm looking to acquire some Wizard cards."
        call play_sound("spit")
        fre "Wizard cards....*spit*"
        ger "Why would you want any of those?"
        m "What does one do with playing cards... Play the game of course."
        fre "Well, we got some of our own to see if it was worth stocking them, but none for sale."
        ger "The profit margin was way to low... Something about import tax."
        ger "We would have to sell a lot of them to make good profit."
        m "I see... So there's no way you'd stock them?"
        fre "Wizard cards hasn't been popular in ages..."
        ger "It does have potential though, not everyone at Hogwarts is going to be into duelling... Or chess."
        fre "How about this... We did acquire a set of cards to try the game out."
        m "So..."
        ger "If you beat us we'll do a trial run and stock some cards for the students."
        twi "(There's no way this\nold man would ever beat us.)"
        $ twins_know_cards = True
        jump twins_duel_menu

    elif twins_cards_stocked and not twins_second_win and not twins_cards_stocked_talk:
        m "Well, well... Looking good as always boys!"
        twi "..."
        m "In a professional sense that is... Don't you worry."
        m "So, How are things going?"
        ger "You were right sir! We've seemed to have struck gold with Wizard Cards."
        g9 "Glad to hear it."
        fre "We've gone ahead and put up a official unofficial tier system ladder."
        m "Unofficial... Official, you say?"
        ger "Yes, as we mentioned... There isn't really any official tournament rules."
        fre "We've sort of kept it that way in that we'll let the people playing set their own wagers and challenges to climb the ladder."
        fre "Any normal game will make you one token richer and once the agreed upon winning conditions for a challenge is achieved then you'll get three tokens!"
        fre "Three challenges won will let you climb to the next tier."
        ger "Which lets you challenge even higher skilled players."

        call nar(">Only first tier with Snape, Hermione and Twins is available for now.")

        m "And by skilled you mean players with better cards?"
        fre "Something like that."
        m "I see..."
        # m "How do I know which players are currently in my tier?"
        # fre "Ah yes, there's a notice board behind us. You should see some people that you know on it."
        ger "I must say, the game has really taken off... Even Snape came to pick up some tokens earlier."
        m "Really? I'd think he would disapprove of your business."
        fre "He was using a Polyjuice potion to disguise himself as a student."
        ger "But that weird walk of his where he sort of slides across the floor gives him away a mile off."
        fre "Tell you what, let's set a wager right now."
        fre "We'd usually make it a bit more difficult but since you gave us the idea for this."
        ger "Beat us again and we'll give you three tokens and a card."
        m "That's it? Sounds a bit out of character for you guys to make it this easy."
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

    call shop_item

    twi "Come again!"

    call gen_walk(xpos=0, ypos="base", speed=1.5)

    jump main_room
