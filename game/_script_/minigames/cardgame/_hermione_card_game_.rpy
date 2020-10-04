

# Hermione Duel Menu

label hermione_cardgame_menu:
    if her_know_cards == False:
        m "[hermione_name]..."
        call her_main( "Yes, [genie_name]?","base","base")
        m "Are you familiar with Wizard Cards?"
        call her_main( "I've heard of it... it used to be a popular card game a decade or so ago.","annoyed","squint")
        g9 "So, would you like to play it?"
        call her_main("Do they even make the cards still? I don't think there's anyone in Hogsmeade stocking them.", "normal", "squint", "base", "mid")
        call her_main( "So I wouldn't be able to play against you...","base","base")
        call her_main( "Unless Fred and Geo...","clench","wide")
        m "Unless... who now?"
        call her_main("\"Hermione... learn to keep your mouth shut.\"", "mad", "wide", "base", "R")
        m "[hermione_name]..."
        call her_main("I'm sorry sir, I should have told you...", "open", "base", "worried", "mid")
        call her_main("Fred and George have a secret shop set up in the school.", "normal", "base", "worried", "R")
        m "I see..."
        call her_main( "Please don't tell them I told you.","open","happyCl")
        m "So you say they might have some cards?"
        call her_main("Wha... yes, maybe.", "base", "base", "base", "mid_soft")
        call her_main("You're not going to shut them down?", "angry", "squint", "base", "mid")
        m "Why should I? It's a free market is it not?"
        g9 "A little bit of competition with Hoemead is good for consumers."
        call her_main("But... I mean, yes of course.", "annoyed", "base", "worried", "mid")
        m "So you'll play if they stock some cards?"
        call her_main("I mean...", "soft", "narrow", "base", "down")
        m "If they don't get shut down I mean."
        call her_main( "Oh, yes of course I'll play.","shock","wide")
        call her_main("...", "soft", "wide", "worried", "stare")
        call her_main("Anything else you needed or am I free to go?", "base", "base", "worried", "mid")
        $ her_know_cards = True
        jump hermione_requests

    elif her_know_cards and twins_know_cards == False:
        m "(I should talk to Fred and George about wizard cards first.)"
        jump hermione_requests

    elif her_know_cards and twins_know_cards and not twins_cards_stocked:
        m "(I have to convince Fred and George to start stocking up cards in their shop first.)"
        jump hermione_requests

    elif twins_cards_stocked_talk and not her_cards_stocked_talk:
        m "Hello again [hermione_name]."
        call her_main( "Hello [genie_name].","base","base")
        m "I wanted to thank you for mentioning the Weasley shop."
        call her_main("You're not shutting them down are you?", "soft", "narrow", "worried", "down")
        m "Of course not, where else am I supposed to get my supplies from?"
        call her_main("Oh, yes... where.", "normal", "narrow", "base", "down")
        g9 "In fact, I noticed that you were on the list."
        call her_main("What list? Have I done something wrong?", "soft", "base", "worried", "mid")
        m "The tier list for the card game of course."
        call her_main("Ah, yes...", "normal", "base", "base", "mid_soft")
        call her_main("I went there to see if you had shut them down and ended up with a deck of cards.", "mad", "closed", "angry", "mid")
        g9 "\"Sounds like even I could learn some bartering tricks from those two.\""
        m "So, how about some practice rounds then?"
        call her_main(" I've only recently started playing so I'm not that good yet.", "base", "narrow", "base", "mid_soft")
        m "Don't worry, after a few practice rounds you'll get up to speed, when you're ready we'll play the real challenge..."
        $ her_cards_stocked_talk = True
        jump hermione_duel_menu

    else:
        if geniecard_level < 2:
            label hermione_duel_menu:
            menu:
                "-First Duel-":
                    jump hermione_first_duel
                "-Second Duel-" if her_first_win:
                    jump hermione_second_duel
                "-You need to beat the first duel-" (style="disabled") if not her_first_win:
                    jump hermione_duel_menu
                "-Challenge-" if her_second_win:
                    jump hermione_third_duel
                "-You need to beat the second duel-" (style="disabled") if not her_second_win:
                    jump hermione_duel_menu
                "-Never mind-":
                    jump hermione_requests
        else:
            jump hermione_random_duel

label hermione_first_duel:
    call play_music("grape_soda")

    $ renpy.call_in_new_context("start_duel", her_first_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if not her_first_win:
        call her_main("Well, that's interesting. I was sure that my deck would've been balanced enough...", "angry", "closed", "angry", "mid")
        g9 "It's just a practice round, I'm sure you'll do better next time."
        call her_main("Your smile says otherwise.", "mad", "narrow", "angry", "R")
        m "..."
        $ her_first_win = True
        pass
    else:
        call her_main("This game is stupid!", "angry", "closed", "angry", "mid")
        pass

    $ tokens += 1

    jump main_room

label hermione_second_duel:
    call play_music("grape_soda")

    $ renpy.call_in_new_context("start_duel", her_second_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if not her_second_win:
        call her_main("I got 5 boosters, how isn't that enough to build a better deck than yours?", "mad", "narrow", "annoyed", "mid")
        m "It's more important where you place those cards..."
        call her_main("I know what I'm doing...", "open", "closed", "angry", "mid")
        g9 "So, do you want to take a break?"
        call her_main("No, I'm ready...", "soft", "narrow", "worried", "mid_soft")
        m "You sure?"
        call her_main("I said I'm ready.", "clench", "base", "angry", "mid")
        $ her_second_win = True
        jump hermione_duel_menu
        pass
    else:
        call her_main("This game is stupid!", "angry", "closed", "angry", "mid")
        pass

    $ tokens += 1

    jump main_room

label hermione_third_duel:
    call her_main( "I'll make my house proud, you'll see.","grin","happy")
    call her_main("Wait, I should have asked for point for this.", "shock", "wide", "worried", "shocked")
    g9 "Too late, here we go."
    hide screen hermione_main
    call play_music("cardgame")
    play sound "sounds/Genie_VS_Hermione4.mp3"
    show screen genie_vs_hermione
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_hermione
    pause 3
    hide screen move_genie
    hide screen move_hermione
    show screen genie_vs_hermione_smile
    with hpunch
    stop music fadeout 0
    pause
    hide screen versus
    hide screen genie_vs_hermione
    hide screen genie_vs_hermione_smile
    play music "music/vs_hermione.mp3"

    $ renpy.call_in_new_context("start_duel", her_third_deck, her_after)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if her_third_win == False:
        call her_main("Nooo, how's this even possible?", "clench", "wide", "worried", "shocked")
        call her_main("I'm supposed to be the smartest girl in my year...", "mad", "wide", "worried", "stare")
        g9 "Looks like Wisdom beats intelligence..."
        call her_main("You don't have to patronise me, I'll get you next time. You'll see.", "upset", "squint", "base", "mid")
        g9 "You seem to have forgotten something..."
        call her_main("Fine...", "angry", "narrow", "base", "mid_soft")
        call her_main("Here...", "mad", "narrow", "base", "mid_soft")
        $ unlocked_cards += [card_her_librarian]
        call give_reward("You have received a card!", "images/cardgame/t1/hermione/her_librarian_v1.webp")
        $ her_third_win = True
        $ tokens += 3
    else:
        $ tokens += 1

    call play_sound("door")
    $ hermione_busy = True

    jump main_room

label hermione_random_duel:
    m "Ready for another game of cards?"

    if her_whoring < 8:
        call her_main("You've already challenged me though...", "open", "happy", "base", "R")
        call her_main("and I lost.", "annoyed", "narrow", "worried", "down")
        g9 "What if we made it a wager..."
        call her_main("Like gambling? No thank you!", "clench", "narrow", "annoyed", "mid")
        m "It's not gambling, just a friendly house point wager..."
        call her_main("Sounds like gambling to me...", "normal", "squint", "base", "mid")
        m "So, how about it?"
        call her_main("I'll pass, [genie_name]...", "open", "base", "worried", "R")

        m "\"Seem like she's a bit to pure minded to accept any kind of wager right now...\""
        jump hermione_requests
    else:
        call her_main("You've already challenged me though...", "open", "happy", "base", "R")
        call her_main("and I lost.", "annoyed", "narrow", "worried", "down")
        g9 "What if we made it a wager..."
        call her_main("Gambling you mean?", "open", "base", "worried", "mid")
        m "Not for money obviously."
        call her_main("What are you suggesting then?","base","happy", cheeks="blush")
        m "Well, I was thinking house points."
        call her_main("House points...", "normal", "happy", "base", "R")
        call her_main("How would this work then?", "open", "happy", "base", "mid")
        m "Well, if you win I'll give you ten points to Gryffindor."
        call her_main("Only 10?", "annoyed", "narrow", "base", "mid_soft")
        m "Twenty then..."
        call her_main("And if I lose?", "open", "happy", "base", "R")
        m "I'll take the same amount away."
        m "\"As if she's going to let that happen...\""
        call her_main("...","normal","happyCl", cheeks="blush")
        call her_main("Okay... In that case to make it fair, let's add these extra rules...", "open", "happy", "base", "mid_soft")

    label hermione_random_duel_rematch:

    call play_music("cardgame")

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, her_after, [5, False, False, True], random_player_deck)

    if duel_response == "Close":
        jump her_duel_cancel
    elif duel_response == "draw":
        jump her_duel_draw
    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if not her_random_win:
        $ her_random_win = True
        $ tokens += 3
    else:
        $ tokens += 1

    m "Seems like I've won this one [hermione_name]."
    call her_main("I noticed...", "normal", "base", "worried", "R")
    m "You do know what this means, don't you?"
    call her_main("...", "normal", "base", "worried", "mid")
    g9 "This means I'm going to have to deduct twenty points from the Gryffindor house."
    call her_main("Please, don't. I don't want the others to wake up tomorrow wondering why there's twenty house points missing...", "open", "happyCl", "worried", "mid")
    m "Well, in that case..."

    menu:
        "-Send Hermione to work, promoting the card game-" if not cardgame_work:
            $ cardgame_work = True
            g9 "In that case, I think I have a good idea for a job..."
            call her_main("A job?", "open", "happy", "base", "mid")
            m "Yes, I'd like you to start helping the twins promote the card game..."
            call her_main("I can do that...", "base", "base", "worried", "mid", cheeks="blush")
            call her_main("But not today if that's okay with you.", "open", "narrow", "worried", "down")
            g9 "That's fine, wouldn't want you to go there looking as defeated as you are at the moment."
            call her_main("...", "normal", "happy", "base", "R", cheeks="blush")
            call her_main("Did you need anything else?", "open", "base", "base", "mid_soft", cheeks="blush")
            call give_reward("Hermione can now work by helping the twins promote the card game.", "interface/icons/icon_gambler_hat.webp")
            jump hermione_requests
        "-Ask for a blowjob instead-":
            jump hg_wager_bj
        "-Deduct the points-":
            pass

    m "No, sorry miss Granger... Minus twenty points from Gryffindor..."
    call her_main("...", "disgust", "narrow", "worried", "down")
    call her_main("Fine, that's fair...", "open", "narrow", "base", "down")
    call her_main("But I'm done playing for today...", "normal", "happyCl", "worried", "mid", cheeks="blush")
    $ gryffindor -= 20

    call play_sound("door")
    $ hermione_busy = True

    jump main_room

label her_duel_draw:
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel_rematch
        "-Stop playing-":
            pass

    her "Okay, another time then..."
    jump main_room

label her_duel_lost:
    stop music fadeout 1

    if geniecard_level > 1:
        her "Hah, told you I'd do it!"
        her "I'll take those points now."
        m "Fine, twenty to gryffindor."
        $ gryffindor += 20

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel
        "-Be a loser-":
            pass
    her "Cards not in your favour [genie_name]? Maybe next time..."

    jump main_room

label her_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    her "Cards not in your favour [genie_name]? Maybe next time..."

    jump main_room

screen genie_vs_hermione():
    zorder 15
    add "images/cardgame/VS/background_twins.webp" xalign 0.5 yalign 0.5
screen move_hermione():
    zorder 16
    add "images/cardgame/VS/hermione_01.webp" at move_in(300, 0.5)

screen genie_vs_hermione_smile():
    zorder 16
    add "images/cardgame/VS/genie_03.webp"
    add "images/cardgame/VS/hermione_02.webp"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def her_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play("sounds/card_punch%s.mp3" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        her_speech = her_speech_card[renpy.random.randint(0,len(her_speech_card)-1)]
        renpy.say(her, her_speech)
        renpy.hide_screen("hermione_main")
        renpy.music.set_volume(1.0)
        return
