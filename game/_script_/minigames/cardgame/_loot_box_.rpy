screen card_lootbox():
    tag card_lootbox
    zorder 9

    use blktone

    for i in xrange(len(card_loot)):
        if card_loot[i] in cards_realm:
            frame:
                style "empty"
                xpos 110+125*i
                ypos 116
                add "interface/achievements/glow.webp" align (0.5, 0.5) zoom 0.5 alpha 0.7 at rotate_circular
        use cardrender(card_loot[i],228+125*i,200, interact=False, cardzoom=0.375)

    use ctc

label card_lootbox:
    python:
        card_loot = []

        cards_choice = [card_iris, card_jasmine, card_azalea, card_dahlia, card_aladdin, card_maslab, card_lilly, card_rasul, card_jafar, card_her_schoolgirl, card_lun_schoolgirl, card_sus_schoolgirl, card_cho_schoolgirl]
        rand_card = None

        for i in xrange(5):
            rand_card = random.choice(cards_items)

            if i == 4:
                if random.randint(0, 103) <= 24: # 22.5% chance
                    rand_card = random.choice(cards_choice)

            if not card_exist(unlocked_cards, rand_card):
                unlocked_cards += [rand_card]
            else:
                rand_card.copies += 1
            card_loot.append(rand_card)

    $ lootbox_quest_ITEM.owned -= 1
    call update_quest_items

    show screen card_lootbox
    with d3
    pause
    hide screen card_lootbox
    with d3

    jump main_room_menu
