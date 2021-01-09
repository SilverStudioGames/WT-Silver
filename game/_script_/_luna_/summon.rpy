
label summon_luna:

    $ active_girl = "luna"
    $ last_character = "luna"

    $ luna_busy = True

    call update_luna

    call play_music("luna")
    call play_sound("door")
    call lun_chibi("stand","mid","base")
    with d3

    if luna_reverted:
        call lun_main("Hello, [lun_genie_name]!","normal","wink","base","mid",xpos="base",ypos="base")
    elif lun_dom >= lun_sub:
        if lun_dom >= 4:
            call lun_main("[lun_genie_name]...","normal","suspicious","angry","R",xpos="base",ypos="base")
        else:
            call lun_main("[lun_genie_name]...","upset","mad","mad","R",xpos="base",ypos="base")
    else:
        call lun_main("[lun_genie_name]...","normal","base","sad","mid",xpos="base",ypos="base")

    label luna_requests:

    $ gave_luna_gift = True # Remove when adding gift texts!

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp", style="disabled"):
            call not_available
            jump luna_requests
        # call luna_chitchat
        # jump luna_requests


        # Personal Favors
        "-Sexual Favours-" (icon="interface/icons/small/condom.webp"):
            jump luna_favor_menu

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if luna_wardrobe_unlocked:
            hide screen astoria_main with d1
            $ gui.in_context("wardrobe")
            with d2
            jump luna_requests

        "-Hidden-" (style="disabled") if not luna_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump luna_requests

        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.webp") if not gave_luna_gift:
            hide screen luna_main with d1
            call gift_menu
            jump luna_requests

        "-Gifts-" (icon="interface/icons/small/gift.webp", style="disabled") if gave_luna_gift:
            $ TBA_message()
            #m "I already gave her a gift today. Don't want to spoil her too much..."
            jump luna_requests

        # Dismiss
        "-Never mind-":

            if luna_reverted:
                call lun_main("Oh... alright then... Bye, [lun_genie_name]!","normal","wink","sad","down",xpos="base",ypos="base")

            jump end_luna_event


# Luna Favor Menu
label luna_favor_menu:
    call update_luna_favors

    menu:
        "-Personal Favours-" (icon="interface/icons/small/heart_green.webp") if not luna_reverted:
            if game.gold <= 0:
                m "(I don't have any gold...)"
                jump luna_favor_menu
            menu:
                "-Talk to me-":
                    jump luna_favour_1
                "-Sit on my lap-" if lun_whoring >= 3:
                    jump luna_favour_2
                "-Strip for me-" if lun_whoring >= 5:
                    jump luna_favour_3
                "-Touch me-" if lun_whoring >= 9:
                    if lun_whoring == 9:
                        jump luna_reversion_event
                    jump luna_favour_4
                "-Touch me with Hermione-" if lun_whoring >= 11:
                    jump luna_favour_5
                "-Suck it-" if lun_whoring >= 14:
                    jump luna_favour_6
                "-Sex-" if lun_whoring >= 17:
                    jump luna_favour_7

                "-Never mind-":
                    jump luna_favor_menu

        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp") if luna_reverted and ll_favor_list != []: # List is not empty.
            label .personal:
            python:
                menu_choices = []
                for i in ll_favor_list:
                    if i in []: # Not in the game yet.
                        menu_choices.append(gui.menu_item("-Not available-", "na", style="disabled"))
                    #elif i.tier > lun_whoring:
                    #    menu_choices.append(gui.menu_item("-Not ready-", "vague", style="disabled"))
                    else:
                        menu_choices.append(i.get_menu_item())
                menu_choices.append(("-Never mind-", "nvm"))
                result = renpy.display_menu(menu_choices)

            if result == "nvm":
                jump luna_favor_menu
            elif result == "vague":
                call favor_not_ready
                jump .personal
            elif result == "na":
                call not_available
                jump .personal
            else:
                $ renpy.jump(result)

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled"):
            call not_available
            jump luna_favor_menu

        "-Never mind-":
            jump luna_requests

label update_luna_favors:
    python:
        for i in ll_favor_list:
            i.tier = lun_tier
    return
