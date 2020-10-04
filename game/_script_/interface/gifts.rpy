label gift_menu:

    $ item_list = [candy_gift_list+mag_gift_list+drink_gift_list+toy_gift_list]
    if active_girl == "hermione":
        $ item_list.append(her_quest_items_list)

    # $ item_list = list(filter(lambda x: not x.unlocked, y) for y in item_list)

    show screen bottom_menu("gift_menu", (("Gift Items", "ui_gifts"), ("Quest Items", "ui_quest_items")), item_list)

    label .interact:
    $ _return = ui.interact()

    if isinstance(_return, tuple):
        if _return[0] == 0:
            hide screen bottom_menu
            # Give gift
            if _return[1].number > 0:
                $ renpy.call("give_"+active_girl[:3]+"_gift", _return[1])
                if globals()[active_girl[:3]+"_mood"] <= 0:
                    return
            else:
                ">You don't own this item."

        elif _return[0] == 1:
            hide screen bottom_menu
            # Give quest item
            $ renpy.call("give_"+active_girl[:3]+"_quest_item", _return[1])

        jump gift_menu

    elif _return == "Close":
        hide screen bottom_menu
        return

    jump .interact

label give_gift(text, gift):
    $ the_gift = "interface/icons/"+str(gift.image)+".webp"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift.number -= 1

    return
