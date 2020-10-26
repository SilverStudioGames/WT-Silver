

# Snape Duel Menu

label snape_duel_menu:
    if geniecard_level == 1:
        if not snape_know_cards:
            m "Ever heard of Wizard Cards?"
            call sna_main("What about them?","snape_05")
            g9 "Do you have any?"
            call sna_main("I do, I collected some when I was younger... never played though.","snape_09")
            m "Why not?"
            call sna_main("Didn't really have anyone to play with so I stopped buying them.","snape_06")
            m "Up for a game or two?"
            call sna_main("...", "snape_03")
            call sna_main("Why not...", "snape_02")
            m "What do I get if I win?"
            call sna_main("What do you mean? There never used to be prizes in Wizard Cards...","snape_01")
            g4 "What..."
            m "No wonder this game never took off..."
            m "Let's just play a few practice rounds for now then."
            call sna_main("And then?","snape_05")
            m "..."
            m "And then we'll think about prizes."
            call sna_main("...","snape_01")
            call sna_main("Fine, I'm confident enough to beat a beginner.","snape_06")
            call sna_main("But first a bit of practice...","snape_02")
            g9 "Let's play."
            $ snape_know_cards = True

        menu:
            "-First Duel-":
                jump snape_first_duel
            "-Second Duel-" if snape_first_win:
                jump snape_second_duel
            "-You need to beat the first duel-" (style="disabled") if not snape_first_win:
                jump snape_duel_menu
            "-Challenge-" if snape_second_win:
                jump snape_third_duel
            "-You need to beat the second duel-" (style="disabled") if not snape_second_win:
                jump snape_duel_menu
            "-Never mind-":
                jump snape_ready

    else:
        m "Up for another game?"
        if not snape_wager_talk:
            sna "With you?"
            sna "..."

            if sna_friendship < 30:
                call sna_main("no...", "snape_03")
                g4 "Why not."
                m "What if we did a game as a part of a wager?"
                call sna_main("A wager...","snape_09")
                call sna_main("No, I have better things to do right now...","snape_06")
                m "(He doesn't seem that keen, maybe I should ask again when we know each other a bit better.)"
                call nar(">Improve your relationship with Snape before trying again.")
                jump snape_ready

            call sna_main("Do you know how hard it is to progress with this game with no one to play against?","snape_03")
            call sna_main("I even traded some of my potion ingredients to some weird guy in knockturn alley for one of the old booster packs...","snape_01")
            call sna_main("Turns out... that card I gave you, whilst not very powerful was quite a rare one.","snape_08")
            m "Sounds like a you problem."
            g9 "I've done fine by just winning cards..."
            m "So, you've played a lot of games since our last match I assume?"
            call sna_main("...","snape_29")
            m "That's what I thought..."
            g4 "What's the point in owning the cards if you're not going to play?"
            call sna_main("I suppose...","snape_09")
            m "How about we do a wager?"
            call sna_main("A wager?","snape_05")
            g9 "Yes, how about just one token and a wager on top of that to make it interesting."
            call sna_main("...","snape_04")
            call sna_main("Fine, but only if it's on equal terms...","snape_10")
            g4 "What does that mean?"
            call sna_main("It means, you set your prize and I'll set mine accordingly.","snape_03")
            m "Okay, so..."
            m "If you win I'll give you some wine."
            call sna_main("Don't you provide me with plenty of wine anyway?","snape_05")
            m "I mean, I could stop doing it. The office has my name on it after all and last I checked that means whatever is in it belong to me as well."
            sna "..."
            g9 "In a figurative way obviously. It doesn't actually have my name on the door."
            call sna_main("Obviously...","snape_03")
            m "It's not like this office came with any of those slytherin sluts you have yet to share with me..."
            call sna_main("Fine, if that's your only proposal. If you win then I'll give you something from my personal collection.","snape_03")
            g4 "Like what?"
            call sna_main("You'll see...","snape_02")
            m "(Must be something good if he's not going to tell me...)"
            g9 "I'm in."

            $ snape_wager_talk = True
            if wine_ITEM.owned < 1:
                sna "Show me the bottle."
                m "What?"
                sna "I want to see the wine first."
                m "I don't have one, right now..."
                sna "That's a shame, the wager will have to wait then."
                m "Damn...!"
                m "(I should see if I could find some more wine in that cupboard, or perhaps check the local store...)"
                jump snape_ready

        else:
            if wine_ITEM.owned < 1:
                sna "Do you have it?"
                m "What?"
                sna "The wine of course!"
                m "I don't..."
                sna "That's a shame, our wager will have to wait then."
                m "Can't we just duel anyway? Im not intending to lose..."
                sna "Neither am I."
                sna "No wine, no duel."
                m "Damn!"
                m "(I should see if I could find some more wine in that cupboard, or perhaps check the local store...)"
                jump snape_ready

            $ one_of_ten = renpy.random.randint(1, 10)

            if one_of_ten == 1:
                call sna_main("Sure, let's do it!","snape_02")
            elif one_of_ten == 2:
                call sna_main("Is there another bottle in it for me?","snape_05")
                g9 "If you win..."
                call sna_main("Good.","snape_02")
                call sna_main(" Then let's begin...","snape_02")
            elif one_of_ten == 3:
                call sna_main("Same wager?","snape_05")
                m "Sure."
                call sna_main("Okay then...","snape_01")
                call sna_main("Let's do it.","snape_02")
            elif one_of_ten == 4:
                call sna_main("Always!","snape_02")
                call sna_main("I'll make sure you lose this time Genie...","snape_01")
            elif one_of_ten == 5:
                call sna_main("My stock is filled so why not...","snape_03")
                g9 "Great."
                call sna_main("Good luck... you'll need it.","snape_02")
            elif one_of_ten == 6:
                call sna_main("You don't have to ask me twice.","snape_02")
            elif one_of_ten == 7:
                call sna_main("Prepare to lose!","snape_10")
                m "..."
                m "Let's just play..."
            elif one_of_ten == 8:
                call sna_main("I've been practising, there's no way I'll lose.","snape_10")
                m "Are you sure about that?"
                call sna_main("Yes, I came here to win...","snape_08")
            elif one_of_ten == 9:
                call sna_main("You're going to lose this time...","snape_04")
                g9 "In your dreams..."
            else:
                call sna_main("Of course!","snape_02")
                call sna_main("But I think we should up our wager a bit...","snape_02")
                m "In what way?"
                call sna_main("I was thinking maybe you could send the Granger girl to my room tonight if I win.","snape_20")
                if hg_pr_kiss.counter >= 3 or her_reputation >= 21:
                    m "We'll see about that."
                else:
                    m "I doubt she would agree to that."
                m "Let's just stick to the original bet for now..."
                call sna_main("Fine...","snape_06")

        jump snape_random_duel



label snape_first_duel:
    call sna_main("A bit dusty but this should do!","snape_03")
    m "You, or the deck?"
    call sna_main("I... the deck, obviously.","snape_14")
    call sna_main("Let's do this.","snape_17")

    call play_music("grape_soda")

    $ renpy.call_in_new_context("start_duel", snape_first_deck)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade
    call sna_main("Maybe I should've gone over the rules a bit more before trying this game again...","snape_05")
    call sna_main("Well played though.","snape_04")

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ snape_busy = True

    $ achievement.unlock("Cardwin")
    $ snape_first_win = True
    $ tokens += 1

    jump main_room



label snape_second_duel:
    call sna_main("That first one was just a warm up, there's no way you'll beat me this time!","snape_16")
    g9 "Time to get our decks out."
    call sna_main("....","snape_25")
    call sna_main("Let's just play.","snape_04")

    call play_music("grape_soda")

    $ renpy.call_in_new_context("start_duel", snape_second_deck)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade
    call sna_main("Not again... I swear these cards used to be good when I bought them.","snape_07")
    call sna_main("They must've made them obsolete to get you to buy more.","snape_04")
    call sna_main("So deliciously mischievous.","snape_02")

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    if not her_know_cards:
        call bld
        g9 "This is awesome, I wonder if Hermione would want to play against me..."

    $ snape_busy = True

    $ snape_second_win = True
    $ tokens += 1

    jump main_room



label snape_third_duel:
    if her_know_cards == False:
        m "(I should probably see if Hermione is interested and practise some more before challenging Snape.)"
        jump snape_duel_menu

    if twins_cards_stocked_talk == False:
        m "(I should wait for an owl from Fred and George and train with Hermione first.)"
        jump snape_duel_menu

    m "So, how about that prize?"
    call sna_main("Again with the prize...","snape_01")
    m "I'm bored okay... and I like prizes..."
    call sna_main("Fine, I challenge you!!","snape_10")
    m "..."
    call sna_main("You don't say it like that anymore?","snape_05")
    m "No, that's lame."
    call sna_main("You're not going to beat me again genie, I've practised with the greatest Wizard cards player there is!","snape_02")
    m "Me?"
    call sna_main("I... no, of course not.","snape_14")
    call sna_main("Let's do this.","snape_17")
    call sna_main("Show me what you got genie... beat me and I'll give you a card from my collection and 3 tokens.","snape_18")
    m "Bring it."

    call play_music("cardgame")
    play sound "sounds/Genie_VS_Snape.mp3"
    show screen genie_vs_snape
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_snape
    pause 2.5
    hide screen move_genie
    hide screen move_snape
    show screen genie_vs_snape_smile
    pause
    hide screen versus
    hide screen genie_vs_snape
    hide screen genie_vs_snape_smile

    $ renpy.call_in_new_context("start_duel", snape_third_deck, snape_after)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if snape_third_win == False:
        call sna_main("Impossible, what's wrong with these cards...","snape_05")
        m "They're old, that's what."
        m "Now to the prize..."
        call sna_main("Fine, here's your tokens and one of my precious cards...","snape_05")
        call sna_main("(You were a good card my boy. But it's time to grow up.)","snape_05")
        $ snape_third_win = True
        $ unlocked_cards += [card_snape]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/snape_v1.webp")
        $ tokens += 3
    else:
        $ tokens += 1

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ snape_busy = True

    jump main_room

label snape_random_duel:
    call play_music("cardgame")

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, snape_after, [renpy.random.randint(0,3), False, True, False], random_player_deck)

    if duel_response == "Close":
        $ wine_ITEM.owned -= 1
        jump snape_duel_cancel
    elif duel_response == "draw":
        jump snape_duel_draw
    elif not duel_response == "win":
        $ wine_ITEM.owned -= 1
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade

    # TODO: Uncomment parts of code once potions have been fixed.

    # python:
        # rand_ing_or_pot = random.choice(potion_lib.lib)
        # potion_inv.add(rand_ing_or_pot)

    if not random_snape_win:
        $ random_snape_win = True

        m "Yes!"
        g9 "No wine for you.."
        call sna_main("...","snape_04")
        g9 "Now, how about that prize we discussed."
        call sna_main("Ah, yes... something from my collection.","snape_05")
        call give_reward("You've received a bottle of grape juice from Snape!", "interface/icons/item_potion.webp") # <--
        #call give_reward("You've received "+rand_ing_or_pot.name+" from Snape!", "interface/icons/item_potion.webp")
        g4 "What the fuck is this..."
        call sna_main("As I said...","snape_01")
        call sna_main("Something from my collection...","snape_02")
        m "..."
        call sna_main("I'm the potions master, what did you think it was going to be?","snape_03")
        m "I don't know... Like a whip or something?"
        call sna_main("Hey, just because I reside in the dungeon...","snape_07")
        g9 "I bet you do have a whip..."
        call sna_main("Well...","snape_12")
        m "Whatever, I'll take it."
        #call sna_main("What, the whi...","snape_18")
        #call sna_main("Oh, the potion ingredient...","snape_14")
        call sna_main("There's plenty more where that came from if you want another game...","snape_24")
        m "..."
        m "I'll think about it."

    else:
        $ random_choice = renpy.random.randint(0, 3)
        if random_choice == 0:
            g9 "Another victory in the bag..."
            call sna_main("I don't get it...","snape_03")
            call sna_main("... You must've been cheating.","snape_04")
            m "Skill... it's called skill."
        elif random_choice == 1:
            call sna_main("Not again... did you look at my cards before the game?","snape_10")
            m "How would I have done that?"
            call sna_main("I don't know...","snape_08")
            call sna_main("Some kind of Genie hocus pocus?","snape_07")
            m "..."
            call sna_main("Did I just...","snape_25")
            m "Yeah, a little bit..."
            call sna_main("I'm just going to leave this here...","snape_14")
        elif random_choice == 2:
            g9 "Sweet, another win for me."
            call sna_main("... I let you win that one.","snape_03")
            m "Sure you did."
        elif random_choice == 3:
            call sna_main("Dammit!","snape_17")
            g4 "Hey, chill out... it's just a game."
            call sna_main("Just a game?!","snape_18")
            call sna_main("Do you know what students from the slytherin house are known for Genie?","snape_07")
            g9 "Well, from what you've told me... being massive sluts?"
            call sna_main("YES...","snape_08")
            call sna_main("Wait, no...","snape_16")
            call sna_main("We're known for being cunning...","snape_17")
            m "..."
            call sna_main("Cunning... Genie.","snape_18")
            m "Yeah, I got you."
            m "Hey, I could just give you another bottle..."
            call sna_main("...","snape_12")
            call sna_main("No... I'll beat you next time.","snape_16")
            g9 "That's the spirit."
        elif random_choice == 4:
            call sna_main("Maybe I should've gone over the rules a bit more before trying this game again...","snape_05")
            call sna_main("Well played though.","snape_04")

        #call give_reward("You've received "+rand_ing_or_pot.name+" from Snape!", "interface/icons/item_potion.webp")
        call give_reward("You've received a bottle of grape juice from Snape!", "interface/icons/item_potion.webp")

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ snape_busy = True
    $ tokens += 1

    jump main_room



label snape_special_duel:
    call play_music("cardgame")

    $ random_enemy_deck = create_random_deck(get_deck_score(playerdeck)-2, get_deck_score(playerdeck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck)

    stop music fadeout 1
    hide screen blkfade

    if duel_response == "draw":
        g4 "Not another fucking..."
        call her_main("*Gltch*, *Slurp*, *Gobble*")
        g4 "Draaaaaaw!"
        return "draw"

    elif not duel_response == "win" or duel_response == "Close":
        call sna_main("Well, well.. Looks like I've...{nw}")
        m "Fuuuuuuuuck!"
        return "loss"

    else:
        g9 "Yeeeeees!"
        g4 "That's it you whore! Take it!"
        return "win"


label snape_duel_draw:
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump snape_duel_menu
            else:
                jump snape_random_duel
        "-Stop playing-":
            pass

    sna "Alright, another time then..."

    jump main_room


label snape_duel_lost:
    hide screen blkfade
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump snape_duel_menu
            else:
                m "I demand a rematch!"
                if wine_ITEM.owned < 1:
                    sna "Seems like you lost all of your bottles, maybe next time."
                    g4 "... You evil creature..."
                    pass
                else:
                    sna "Fine."
                    sna "More wine for me!"
                    jump snape_random_duel
        "-Be a loser-":
            pass

    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else: # Rub it in
        $ rndm_one_of_three = renpy.random.randint(1, 7)
        if rndm_one_of_three == 1:
            sna "Thanks for the bottle... Genie"
            g4 "...."
        elif rndm_one_of_three == 2:
            m "..."
            m "Good game..."
            sna "Forgetting something?"
            m "Fine, here's your bottle..."
        elif rndm_one_of_three == 3:
            call sna_main("Another win for me...","snape_02")
            m "And your last..."
            call sna_main("Sorry, can't hear you over the sound of my victory.","snape_01")
            m "..."
        elif rndm_one_of_three == 4:
            call sna_main("Child's play...","snape_02")
            m "I'm hundreds of years old you know..."
            call sna_main("And I beat you...","snape_02")
            m "just shows how luck based the game is honestly..."
        elif rndm_one_of_three == 5:
            call sna_main("...","snape_02")
            m "Just take your prize and go."
        elif rndm_one_of_three == 6:
            call sna_main("Nice one...","snape_02")
            m "Hey, don't be a bad winner"
            call sna_main("Hey, I was just...","snape_03")
            call sna_main("I see what you're doing...","snape_04")
            call sna_main("I'll take that wine now...","snape_02")
        else:
            sna "HA!"
            sna "I mean... good game."
            m "You're allowed to show enthusiasm you know..."
            sna "I know, but it's bad for my image..."
            m "..."
            m "Whatever, here's your bottle."

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ snape_busy = True

    jump main_room


label snape_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    hide screen blkfade
    with dissolve

    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else:
        sna "In that case, it's a forfeit."
        sna "I'll take that wine now."
        m "Wait a minute..."
        sna "I don't make the rules, I just play by them."
        m "Fine..."

    call play_sound("door")
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ snape_busy = True

    jump main_room



screen genie_vs_snape():
    zorder 16
    add "images/cardgame/VS/background_snape.webp" xalign 0.5 yalign 0.5
screen move_genie():
    zorder 16
    add "images/cardgame/VS/genie_01.webp" at move_in(-300, 0.5)
screen versus():
    zorder 15
    add "images/cardgame/VS/vs.webp"
screen move_snape():
    zorder 16
    add "images/cardgame/VS/snape_01.webp" at move_in(300, 0.5)

screen genie_vs_snape_smile():
    zorder 16
    add "images/cardgame/VS/genie_02.webp"
    add "images/cardgame/VS/snape_02.webp"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def snape_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play("sounds/card_punch%s.mp3" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        renpy.say(sna,snape_speech_card[renpy.random.randint(0,len(snape_speech_card)-1)])
        renpy.music.set_volume(1.0)
        return

    def snape_after_special():
        renpy.call("sna_main", "It's my time to shine, I'm counting on an explosive victory.", face="snape_02")
        renpy.call("her_main", "*Slurp*, *Slurp*, *Gobble*")
        renpy.say(g4, "Ngh, not on my watch... I'll do my best to prevent any unwarranted explosions during the current circumstance...")
        renpy.call("sna_main", "Now you're talking, usually I'm the one doing all the trash talk...", face="snape_28")
        renpy.say(m, "I feel like today especially it's important to keep the conversation going...")
        renpy.call("her_main", "*Gltch*, *Slurp*, *Gobble*")
        renpy.say(g4, "...")
        renpy.call("sna_main", "Great, I can't wait to see your face as I destroy you...", face="snape_22")
        renpy.say(m, "Surely you'd know by now I'm not the kind of person to lose...")
        renpy.call("her_main", "*Slurp*, *Slurp*, *Gobble*")
        renpy.say(g4, "... My composure that easily...")
        renpy.call("sna_main", "I'll make you bust this time for sure... I can already taste victory...", face="snape_21")
        renpy.say(m, "That's not the only thing that someone will be tasting in a second...")
        return
