label gift_menu:
    $ inventory_mode = 1
    $ gui.in_context("inventory_menu")
    $ inventory_mode = 0
    return

label give_gift(text, gift):
    show screen gift(gift)
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift.owned -= 1

screen gift(gift):
    zorder 30

    if isinstance(gift, Item):
        add gift.get_image() align (0.5, 0.4) zoom get_zoom(gift.get_image(), (320, 320))
    else:
        add gift align (0.5, 0.4) zoom get_zoom(gift, (320, 320))
