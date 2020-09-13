init python:

    def start_duel(opppent_deck, after_enemy = None, rules = None, duel_player_deck = None):
        global standard_rules
        global playerdeck
        if rules == None:
            rules = standard_rules
        if duel_player_deck == None:
            duel_player_deck = playerdeck

        backside_list = []
        for i in xrange(0, rules[0]):
            backside_list.append(True)
        for i in xrange(rules[0], len(opppent_deck)):
            backside_list.append(False)

        ## Setup Deck ##
        player_deck = []
        for card in duel_player_deck:
            card.playercard = True
            player_deck.append(card.clone())

        enemy_deck = []
        for card in opppent_deck:
            card.playercard = False
            enemy_deck.append(card.clone())

        # Display rules
        game_rules_list = convert_rules(rules, player_deck)
        if len(game_rules_list) > 0:
            renpy.choice_for_skipping()
            renpy.show_screen("rules_display", game_rules_list)
            renpy.pause()
            renpy.hide_screen("rules_display")

        ## Clean the table from last fight ##
        reset_table_cards()

        ## Random check to see who start ##
        coin_flip = renpy.random.randint(0,1)
        if coin_flip == 0:
            enemy_turn(enemy_deck, backside_list, rules[2], rules[3])

        ## Game Loop ##
        response_card = ""
        while not(response_card == "win" or response_card == "loss"):
            response_card = cardgame(enemy_deck, player_deck, backside_list, rules[2], rules[3])
            if response_card == "AfterEnemy" and not after_enemy == None:
                after_enemy()
            elif response_card == "Close":
                return "Close"
            elif response_card == "draw" and rules[1]:
                for list_elm in table_cards:
                    for elm in list_elm:
                        if elm.playercard:
                            player_deck.append(elm)
                        else:
                            enemy_deck.append(elm)

                backside_list = []
                for i in xrange(0, rules[0]):
                    backside_list.append(True)
                for i in xrange(rules[0], len(opppent_deck)):
                    backside_list.append(False)
                reset_table_cards()

            elif response_card == "draw":
                break



        return response_card


    def cardgame(enemy_deck, player_deck, shown_backside, reverse, dobelt_number):
        global selectcard
        global selectenemycard
        global table_cards

        renpy.hide_screen("main_room_menu")
        renpy.show_screen("card_battle", player_deck, enemy_deck, shown_backside)
        renpy.music.stop("weather") #Stop playing weather SFX

        _return = ui.interact()

        if _return in player_deck:
            selectcard = player_deck.index(_return)
            return "NewTurn"
        elif _return in enemy_deck:
            selectenemycard = enemy_deck.index(_return)
            return "NewTurn"

        elif _return == "Close":
            selectcard = -1
            selectenemycard = -1
            renpy.hide_screen("card_battle")
            return _return

        elif _return == "unselect":
            selectcard = -1
            selectenemycard = -1
            return "NewTurn"

        else:
            if not selectcard == -1:
                renpy.sound.play("sounds/card.mp3")
                y = int(math.floor(int(_return)/3))
                x = int(_return)-(y*3)

                table_cards[x][y] = player_deck[selectcard]
                table_cards[x][y].playercard = True
                del player_deck[selectcard]
                selectcard = -1
                selectenemycard = -1
                update_table(x,y,reverse, dobelt_number)

                renpy.pause(0.7) # Autoplay enemy card
                if (len(player_deck) == 0 or len(enemy_deck) == 0):
                    response_card = check_winner(player_deck)
                    if response_card == "win":
                        renpy.show_screen("card_end_message", "You win!")
                        renpy.sound.play("sounds/card_win.ogg") #Fanfare
                    elif response_card == "draw":
                        renpy.show_screen("card_end_message", "Draw")
                    else:
                        renpy.show_screen("card_end_message", "You lost...")
                    renpy.pause(3.0) # Pause before end
                    renpy.hide_screen("card_end_message")
                    renpy.hide_screen("card_battle")
                    renpy.transition(dissolve)
                    return response_card

                enemy_turn(enemy_deck, shown_backside, reverse, dobelt_number)
                renpy.sound.play("sounds/card.mp3")
                if (len(player_deck) == 0 or len(enemy_deck) == 0):
                    response_card = check_winner(player_deck)
                    if response_card == "win":
                        renpy.show_screen("card_end_message", "You win!")
                        renpy.sound.play("sounds/card_win.ogg")
                    elif response_card == "draw":
                        renpy.show_screen("card_end_message", "Draw")
                    else:
                        renpy.show_screen("card_end_message", "You lost...")
                    renpy.pause(3.0) # Pause before end
                    renpy.hide_screen("card_end_message")
                    renpy.hide_screen("card_battle")
                    renpy.transition(dissolve)
                    return response_card
                return "AfterEnemy"
            else:
                return "NewTurn"

    def enemy_turn(enemy_deck, shown_backside, reverse, dobelt_number):
        global table_cards
        high_score = 0
        high_score_card = None
        high_score_pos = (0,0)

        #Fix for not finding a card
        tuple_my = enemy_deck[0].get_ai_score(table_cards, reverse, dobelt_number)
        high_score = tuple_my[0]
        high_score_pos = tuple_my[1]
        high_score_card = enemy_deck[0]

        for card in enemy_deck:
            tuple_my = card.get_ai_score(table_cards, reverse, dobelt_number)
            if tuple_my[0] > high_score:
                high_score = tuple_my[0]
                high_score_pos = tuple_my[1]
                high_score_card = card

        x = high_score_pos[0]
        y = high_score_pos[1]
        del shown_backside[enemy_deck.index(high_score_card)]
        del enemy_deck[enemy_deck.index(high_score_card)]
        table_cards[x][y] = high_score_card
        table_cards[x][y].playercard = False
        update_table(x,y, reverse, dobelt_number)
        return

    def convert_rules(rules, player_deck):
        rules_list = []
        if rules[0] > 0:
            rules_list.append(card_rule_hidden)
        if rules[1]:
            rules_list.append(card_rule_death)
        if rules[2]:
            rules_list.append(card_rule_reverse)
        if rules[3]:
            rules_list.append(card_rule_double)
        is_random_deck = True
        for x in xrange(len(player_deck)):
            is_random_deck =  is_random_deck and (player_deck[x].title is playerdeck[x].title)
        if not is_random_deck:
            rules_list.append(card_rule_random)
        return rules_list

    def advance_tier(tier):
        global geniecard_level

        renpy.show_screen("blktone")
        renpy.show_screen("advance_deck")
        renpy.transition(Dissolve(0.3))
        renpy.pause(1.0)

        # Change card image for each respective card.
        for card in cards_dynamic:
            card.imagepath = card.imagepath.split("_v")[0] + "_v{}.webp".format(geniecard_level)

        geniecard_level = tier
        renpy.play("sounds/magic4.ogg")
        renpy.show_screen("advance_deck")
        renpy.transition(Fade(0.2, 0.0, 0.8, color='#fff'))
        renpy.pause()
        renpy.hide_screen("blktone")
        renpy.hide_screen("advance_deck")
        renpy.transition(Dissolve(0.3))

        return

screen card_battle(l_playerdeck, l_enemydeck, shown_cards):
    zorder 13
    imagebutton idle "images/cardgame/card_table.webp" action Return("unselect")

    #fix card error when you select the last card
    if not selectenemycard < len(l_enemydeck):
        $ selectenemycard = -1

    imagemap:
        ground "images/cardgame/card_table.webp"

        for y in xrange(0,3):
            for x in xrange(0,3):
                if table_cards[x][y] == None:
                    hotspot (353+124*x, 25+184*y, 125, 182) clicked Return(str(x+y*3))
                else:
                    use cardrender(table_cards[x][y], 353+124*x, 25+184*y, cardzoom=0.375, animated=True)

    for i in xrange(0, len(l_playerdeck)):
        if not selectcard == i:
            use cardrender(l_playerdeck[i], 18,17+80*i, True)

    if not selectcard == -1:
        use cardrender(l_playerdeck[selectcard], 54,17+80*selectcard)

    for i in xrange(0, len(l_enemydeck)):
        if not selectenemycard == i:
            use cardrender(l_enemydeck[i], 898,17+80*i, True, backside=shown_cards[i])

    if not selectenemycard == -1:
        use cardrender(l_enemydeck[selectenemycard], 860,17+80*selectenemycard, backside= shown_cards[selectenemycard])

    use close_button

transform cardrender_move(xpos_card, ypos_card, start_xy):
    on start, show:
        pos start_xy
        linear 0.2 xpos absolute(xpos_card) ypos absolute(ypos_card)

transform cardrender(pos, zoom):
    pos pos
    zoom zoom

screen cardrender(card, xpos_card, ypos_card, interact=False, return_value=None, cardzoom=0.5, color=True, gallery=False, backside=False, animated=False):
    zorder 14
    if return_value == None:
        $ return_value = card

    default img = card.get_image(backside=backside)
    default img_border = card.get_border()

    fixed:
        xysize card.sizes
        at cardrender((xpos_card, ypos_card), cardzoom)

        imagebutton:
            style "empty"

            if (gallery and not card_exist(unlocked_cards, card)) or (not color or card.copies <= -1):
                idle gray_tint(img)
                hover gray_tint(image_hover(img))
                foreground gray_tint(img_border)
            else:
                idle img
                hover image_hover(img)
                foreground img_border

            if interact:
                action Return(return_value)

        if not backside:
            text str(card.topvalue) style "cardrender_text" pos (160, 35)
            text str(card.bottomvalue) style "cardrender_text" pos (160, 445)
            text str(card.leftvalue) style "cardrender_text" pos (35, 240)
            text str(card.rightvalue) style "cardrender_text" pos (285, 240)

            #Total Value
            text str(card.get_totalvalue()) style "cardrender_text" pos (60, 57)

style cardrender_text:
    color "#ffffff"
    anchor (0.5, 0.5)
    size 26

screen start_deck():
    zorder 15

    for i in xrange(len(unlocked_cards)):
        use cardrender(unlocked_cards[i],40+125*i,200, interact=False, cardzoom=0.375)

screen advance_deck():
    tag advance_deck
    zorder 15

    for i in xrange(len(cards_dynamic)):
        use cardrender(cards_dynamic[i],40+125*i,200, interact=False, cardzoom=0.375)

    text "Tier [geniecard_level]" size 32 color "#fff" ypos 100 xalign 0.5 outlines [ (2, "#000", 0, 0) ]

    use ctc


screen card_end_message(message):
    zorder 15

    text "{color=#FFF}{size=+40}[message]{/size}{/color}" xpos 540 ypos 300 xalign 0.5 yalign 0.5 outlines [ (5, "#000", 0, 0) ]

screen rules_display(game_rules_list):
    tag rules
    zorder 16

    add "interface/bld.webp" at fade_show_hide(0.15)

    vbox:
        ypos 40
        spacing 20
        xalign 0.5
        xsize 640
        text "{color=#ffffff}Custom rules{/color}"size 32 xalign 0.5
        text "{color=#ffffff}This game uses some extra rules, it is recommended if it's your first time playing to read the description for the active rules.{/color}" xalign 0.5

        frame:
            xalign 0.5
            background "#7c716a"
            vbox:
                spacing 5
                for i in xrange(len(game_rules_list)):
                    hbox:
                        add game_rules_list[i].icon
                        text game_rules_list[i].name yalign 0.5
                    frame:
                        background "#625954"
                        xfill True
                        text game_rules_list[i].description yalign 0.5 size 12
                    add "images/cardgame/spacer.webp"

label start_duel(opppent_deck, after_enemy = None, rules = None, duel_player_deck = None):
    $ duel_response = start_duel(opppent_deck, after_enemy, rules, duel_player_deck)
    call weather_sound
    return
