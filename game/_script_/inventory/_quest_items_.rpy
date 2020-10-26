# Quest Items
default qitem_list = []

#Update lists
label update_quest_items:

    ### Genie ###

    #Tentacle Scroll
    if sealed_scroll_quest_ITEM.unlocked and not tentacle_sample:
        if sealed_scroll_quest_ITEM not in qitem_list:
            $ qitem_list.append(sealed_scroll_quest_ITEM)
            $ sealed_scroll_quest_ITEM.owned = 1 #Makes it clickable in the inventory UI.
    else:
        if sealed_scroll_quest_ITEM in qitem_list:
            pass # Don't remove the item, the player may think it can no longer be used
            #$ qitem_list.remove(sealed_scroll_quest_ITEM)

    #Puzzle Box
    if puzzle_box_quest_ITEM.unlocked and unlocked_7th == False:
        if puzzle_box_quest_ITEM not in qitem_list:
            $ qitem_list.append(puzzle_box_quest_ITEM)
            $ puzzle_box_quest_ITEM.owned = 1 #Makes it clickable in the inventory UI.
    else:
        if puzzle_box_quest_ITEM in qitem_list:
            $ qitem_list.remove(puzzle_box_quest_ITEM)

    # Lootbox
    if lootbox_quest_ITEM.owned > 0:
        if lootbox_quest_ITEM not in qitem_list:
            $ qitem_list.append(lootbox_quest_ITEM)
    else:
        if lootbox_quest_ITEM in qitem_list:
            $ qitem_list.remove(lootbox_quest_ITEM)

    if collar == 0 and her_whoring >= 24:
        if collar_quest_ITEM not in qitem_list:
            $ qitem_list.append(collar_quest_ITEM)
            $ collar_quest_ITEM.owned = 1 #Makes it clickable in the gift UI.
    else:
        if collar_quest_ITEM in qitem_list:
            $ qitem_list.remove(collar_quest_ITEM)

    return

label examine_sealed_scroll:
    if tentacle_sample:
        m "I should use this on Hermione."
    else:
        m "It's missing the key ingredient."
    jump main_room
