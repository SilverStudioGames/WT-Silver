

### Cupboard ###

label cupboard:
    if not cupboard_examined:
        $ cupboard_examined = True
        $ searched = True
        show screen chair_left
        call gen_chibi("stand","behind_desk","base", flip=False)
        show screen desk
        with d5
        pause.2

        call bld
        m "Hm....."
        m "A cupboard..."
        m "Maybe I should rummage through this one later..."
        jump main_room_menu

    jump rummaging


label rummaging:

    $ searched = True # Resets every day/night.
    $ rum_times += 1  # Stat counter.

    show screen chair_left
    show screen desk
    show screen cupboard_open
    call gen_chibi("rummage", 160, 110+349, flip=False) # Note: Flip is inconsistent
    with d3
    show screen bld1
    with d3

    ">You rummage through the cupboard for a while..."

    $ random_percent = renpy.random.randint(1, 100)

    # Dueling potion
    if day <= 3 and rum_times in [1,2]:
        $ potions += 1
        call give_reward(">You found some sort of healing potion...","interface/icons/item_potion.png")
        jump main_room_menu

    # Map and beverages (prologue only)
    if not map_unlocked:
        if hermione_favors:
            $ map_unlocked = True
            call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","interface/icons/item_scroll.png")
            jump main_room_menu

        elif wine_ITEM.number < 1:
            call rum_block(wine_ITEM)
            jump main_room_menu

        elif not firewhisky_ITEM.unlockable and firewhisky_ITEM.number < 1:
            call rum_block(firewhisky_ITEM)
            jump main_room_menu

    # Dumbledore card
    if day >= 26 and deck_unlocked and random_percent <= 40 and not card_exist(unlocked_cards,card_dumbledore) :
        call give_reward("You have found a special card!", "images/cardgame/t1/special/dumbledore_v1.png")
        $ unlocked_cards += [card_dumbledore]
        jump main_room_menu

    # Randomly drop something
    call rum_block(drop_item_from_cupboard(random_percent))
    jump main_room_menu


label rum_block(item):
    if isinstance(item, int):
        $ the_gift = "interface/icons/gold.png"
        show screen gift(True)
        with d3
        $ gold += item
        ">You found [item]+E gold..."

    elif item == "nothing":
        ">You found {size=-10}nothing{/size} of value..."

    else:
        $ item.number += 1
        $ the_gift = item.get_image()
        show screen gift(True)
        with d3
        if item == wine_ITEM:
            ">You found a bottle of wine from professor Dumbledore's personal stash..."
        elif item == firewhisky_ITEM:
            ">You found a bottle of firewhisky from professor Dumbledore's personal stash..."
        else:
            ">You found [item.name]..."
            ">[item.description]"

        call tutorial("inventory")

    hide screen gift
    with d3

    return

init python:
    def drop_item_from_cupboard(random_percent):
        drop_list = [item for item in cupboard_drop_list if not item.unlockable]

        dr = max(rum_times - day, 0) * 2 # Frequent rummaging penalty
        progress_factor = math.log(her_tier + cho_tier + ton_tier + lun_tier + day)

        if game_difficulty == 1:
            # Easy
            # Soft diminishing returns, more rubber banding. Guaranteed item drop.
            if not firewhisky_ITEM.unlockable and firewhisky_ITEM.number < 1:
                return firewhisky_ITEM
            elif wine_ITEM.number < 1:
                return wine_ITEM
            elif gold < int(170 * math.log(day)) and random_percent <= 56 - dr:
                return int(progress_factor * random_gold)
            else:
                filtered_list = filter(lambda x: x.number <= 5, drop_list)
                random_item = renpy.random.choice(filtered_list if filtered_list else drop_list)
                return random_item

        elif game_difficulty == 2:
            # Normal
            # Fair diminishing returns, soft rubber banding. High chance for item drop. (Recommended)
            if gold < int(120 * math.log(day)) and random_percent <= 38 - dr:
                return int(progress_factor * random_gold)
            else:
                filtered_list = filter(lambda x: x.number <= 3, drop_list)
                random_item = renpy.random.choice(filtered_list if filtered_list else drop_list)

                if int(120 * math.log(day)) / 3 < random_item.cost:
                    chance = max(6 - (random_item.number * 5), 1)
                elif gold > random_item.cost:
                    chance = max(65 - (random_item.number * 15), 5)
                else:
                    chance = max(95 - (random_item.number * 10), 15)

                if random_percent <= chance - dr:
                    return random_item
                else:
                    return "nothing"

        elif game_difficulty == 3:
            # Hard
            # Harsh diminishing returns, no rubber banding. Chance for item drop.
            if gold < int(90 * math.log(day)) and random_percent <= 33 - dr:
                return int(progress_factor * random_gold)
            else:
                random_item = renpy.random.choice(drop_list)

                if int(90 * math.log(day)) / 3 < random_item.cost:
                    chance = max(3 - (random_item.number * 5), 1)
                elif gold > random_item.cost:
                    chance = max(40 - (random_item.number * 15), 0)
                else:
                    chance = max(75 - (random_item.number * 10), 5)

                if random_percent <= chance - dr:
                    return random_item
                else:
                    return "nothing"
