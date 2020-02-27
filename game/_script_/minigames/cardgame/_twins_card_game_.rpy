label twins_first_duel:
    call play_music("grape_soda")

    $ renpy.call_in_new_context("start_duel", twins_first_deck)
        
    if duel_response == "Close":
        jump twins_duel_cancel
    elif not duel_response == "win":
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1

    if not twins_first_win:
        twi "No way!"
        ger "You must've been cheating."
        m "It's all in the cards boys."
        ger "I can see that... perhaps it's worth stocking some after all."
        fre "Indeed, if the cards you have play such a big role..."
        ger "You'd have to buy more and more for any chance to win."
        fre "And we..."
        twi "We'll be rich!"
        m "So you'll stock some?"
        ger "Absolutely! We'll send you an owl when it's ready and if they sell well we'll play you again."
        twi "And we'll win next time!"
        m "We'll see about that, I can't have students going around showing up to their headmaster can I..."
        $ twins_first_win = True
        $ twins_cards_delay = twins_cards_delay+day
        pass
    else:
        twi "Not again.."
        m "Tough luck boys."
        pass

    "You return to your office."

    $ tokens += 1

    jump main_room

label twins_second_duel:
    if twins_cards_stocked == False:
        m "(I need to wait for an owl from them before we can duel again)"
        jump twins_duel_menu

    fre "Good luck."
    ger "You'll need it."

    play music "music/vs_twins.ogg" fadein 1.0
    play sound "sounds/Genie_VS_Twins_Teleport.mp3"
    show screen genie_vs_twins
    show screen move_genie
    pause 1
    show screen move_twins
    pause 3.5
    hide screen move_twins
    hide screen move_genie
    show screen genie_vs_twins_smile
    with flash
    pause
    hide screen genie_vs_twins_smile
    hide screen genie_vs_twins

    $ renpy.call_in_new_context("start_duel", twins_second_deck, twins_after)
        
    if duel_response == "Close":
        jump twins_duel_cancel
        
    elif  not duel_response == "win":
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if not twins_second_win:
        fre "I feel like we should have foreseen this."
        ger "I blame Trelawney on this, she said that luck would be on our side today..."
        fre "Well, a promise is a promise. Here's your reward..."
        ger "And we also heard about your wins against Snape so here's some extra tokens."
        fre "Make sure to come back and spend those tokens in our token shop."
        $ card_rand_twins = renpy.random.choice([[card_fred, "fred"], [card_george, "george"]])
        $ unlocked_cards += [card_rand_twins[0]]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/%s_v1.png" % str(card_rand_twins[1]))
        $ twins_second_win = True
        $ tokens += 3
    else:
        twi "Not again.."
        m "Tough luck boys."
        $ tokens += 1

    "You return to your office."
    jump main_room
    
label twins_random_duel:
    if first_random_twins:
        $ first_random_twins = False
        m "How about another game?"
        twi "Sure, why not."
        fre "But let's make it a bit interesting."
        m "I was going to suggest something similar but go on..."
        ger "Let's make a wager."
        m "Okay, what kind of wager are you thinking of?"
        ger "How about a monetary one?"
        m "Of course, what else is there in this world other than monetary rewards?"
        fre "That's what we thought."
        ger "Okay, how about..."
        ger "If you win we'll give you a cut from our weekly shop profits."
        m "That confident are we?"
        fre "Of course."
        m "Well, if it's a monetary reward you're looking for then..."
        m "How about if I lose, I'll give you ten gold?"
        ger "Let me just do some maths real quick."
        ger "..."
        ger "...carry the one..."
        m "Finished?"
        ger "Just a second..."
        ger "Done!"
        if gold < 10:
            ger "Unfortunately we will have to refuse."
            g4 "Why?"
            fre "The further extension to fractional values of your current income in the first instance on the establishment of a method of algebraical evolution which bears the same relation to arithmetical evolution that algebraical division bears to arithmetical division gives unsatisfactory results."
            m "...........what?"
            ger "It means you're broke, sir."
            fre "Come back with your offer when you have more gold, professor."
            m "Fine.."
            m "(Kids nowadays..)"
            "You return to your office."
            jump main_room
        ger "Yes, that is quite satisfactory..."
        fre "This deal is only until we leave Hogwarts by the way..."
        m "Obviously..."
        fre "Just making sure that we have all grounds covered."
        m "Let's begin..."
    elif twins_profit == 0.2:
        m "Ready for another wager?"
        ger "No, I think we've had quite enough of a dent in our profit margin..."
        fre "We're almost half way to where we were before we introduced the card game."
        g4 "Only half?"
        ger "Yes, we still need to think about growth."
        m "\"I should've asked for a cut to begin with.\""
        m "\"Well, hopefully if I can get Hermione to help them promote their shop I'll get more that week...\""
        jump twins_menu
    else:
        m "Ready for another wager?"
        twi "Why not..."
        ger "If you win we'll give you another 1%% from our weekly profits."
        m "Is there a limit?"
        fre "Of course... but you're not going to reach it..."
        m "..."
        m "Okay, well... If you two win then I'll give you ten gold."
        ger "One second, professor."
        "> George takes out a calculator and starts calculating something."
        if gold < 10:
            ger "We have to refuse."
            m "Why?"
            fre "Long explanation or short?"
            menu:
                "-Long-":
                    fre "The further extension to fractional values of your current income in the first instance on the establishment of a method of algebraical evolution which bears the same relation to arithmetical evolution that algebraical division bears to arithmetical division gives unsatisfactory results."
                "-Short-":
                    ger "You are broke, sir."
            fre "Come back with your offer when you have more gold, professor."
            m "Fine.."
            "> You return to your office."
            jump main_room
        ger "Acceptable..."
        twi "Let's play."
       
    call play_music("cardgame")
       
    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, twins_after, [0, True, True, False], random_player_deck)
        
    if duel_response == "Close":
        jump twins_duel_cancel
        
    elif  not duel_response == "win":    
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if twins_random_win:
        twi "No!"
        ger "How did you even do that, we weighed these packs for a reason..."
        m "You did what, sorry?"
        fre "Don't mind him, he doesn't know what he's saying when he's angry."
        m "..."
        m "So, we had a deal."
        fre "Yes, about that..."
        m "You're not backing out are you?"
        fre "Of course not, I just wanted to make sure we're on the same page about this."
        fre "We'll send you your cut once a week..."
        ger "The amount may vary obviously."
        fre "It all depends of how many sales we get that week."
        fre "We're always looking to have someone help with promoting the shop and card game."
        m "\"Sounds like something Hermione might be able to do.\""
        m "\"After some convincing...\""
        m "Okay, and I pick it up here or?"
        fre "Yes, you can pick it up here, once a week..."
        ger "I guess you're a part owner now, congratulations!"
        m "I suppose I am..."
        fre "Anything else?"
        m "No."
        m "Unless..."
        twi "Unless?"
        m "Unless you're willing to do another wager?"
        fre "We're not giving you another cut that big again..."
        m "Well, how about a lower percentage? I'll adjust my wager as well."
        ger "We'll think about it..."

        call give_reward("You have received 5% of the twins profits", "interface/icons/cards.png")
        $ twins_profit += 0.05
        $ twins_random_win = False
        $ tokens += 3
    elif twins_profit == 0.2:
        fre "Nice job but you've reached the cap I'm afraid."
        ger "Yeah, don't want to go minus do we?"
        $ tokens += 1
    else:
        twi "Not again..."
        m "Time to pay up boys."
        ger "Fine... we'll up your profits by 1%%..."
        $ tokens += 1
        $ twins_profit += 0.01

    "You return to your office."
    jump main_room
    
label twins_duel_lost:
    stop music fadeout 1
    if geniecard_level == 2:
        m "..."
        m "It would appear that I may have lost this one..."
        twi "It seems so."
        m "Well, here's your reward..."
        $ gold -= 10
        
    menu:
        "-Rematch-":
            jump twins_duel_menu
        "-Be a loser-":
            pass

    ger "Cards not in your favour professor? Maybe next time..."
    "You return to your office."

    jump main_room

label twins_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    ger "Cards not in your favour professor? Maybe next time..."
    "You return to your office."

    jump main_room

screen genie_vs_twins():
    zorder 15
    add "images/cardgame/VS/background_twins.png" xalign 0.5 yalign 0.5
screen move_twins():
    zorder 16
    add "images/cardgame/VS/twins_01.png" at move_in(300, 1)

screen genie_vs_twins_smile():
    zorder 16
    add "images/cardgame/VS/genie_04.png"
    add "images/cardgame/VS/twins_02.png"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def twins_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play( "sounds/card_punch%s.mp3" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        rnd_text = twins_speech_card[renpy.random.randint(0,len(twins_speech_card)-1)]
        #$ rnd_twin = renpy.random.choice = [fre, goe]

        if renpy.random.randint(0, 1) == 0:
            renpy.say(fre, rnd_text)
        else:
            renpy.say(ger, rnd_text)
        renpy.music.set_volume(1.0)
        return