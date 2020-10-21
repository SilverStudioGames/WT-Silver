label fireplace:
    if not fireplace_examined:
        $ fireplace_examined = True
        call gen_chibi("stand","mid","base")
        show screen chair_left #Empty chair near the desk.
        show screen desk
        with d5
        m "*Hmm*... Looks like an ordinary fireplace..."
        call gen_chibi("sit_behind_desk")
        with d5
        jump main_room_menu

    if is_puzzle_box_in_fireplace():
        call gen_chibi("stand", "fireplace", "fireplace")
        show screen chair_left
        show screen desk
        with d3
        m "(*Hmm*... There's something glimmering in the fireplace.)"
        menu:
            "-Search fireplace-":
                m "(A loose brick... If only I could..{nw}{w=1.0}"
                $ renpy.play('sounds/brick_scrape.mp3')
                m "(A loose brick... If only I could..{fast} *Hhng*... There we go.)"
                call give_reward("A puzzle box has been added to your quest items in the Inventory!", "interface/icons/icon_puzzle.webp")
                $ puzzle_box_quest_ITEM.unlocked = True
                call update_quest_items
                m "Seems straight forward enough."
                m "Maybe I should give it a try?"
                menu:
                    "-Try solving the puzzle-":
                        call gen_chibi("sit_behind_desk")
                        with d3
                        jump start_slide_puzzle
                    "-Save it for later-":
                        pass
                call gen_chibi("sit_behind_desk")
                with d3

    else:
        if fire_in_fireplace:
            $ fire_in_fireplace = False
            hide screen fireplace_fire
        else:
            $ fire_in_fireplace = True
            $ stat_fireplace_counter += 1
            show screen fireplace_fire

    jump main_room_menu

init python:
    def is_puzzle_box_in_fireplace():
        return game.day >= 25 and not game.daytime and full_moon and not puzzle_box_quest_ITEM.unlocked and not unlocked_7th
