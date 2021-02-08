label fireplace:
    if game.day == 1:
        if not fireplace_examined:
            $ fireplace_examined = True
            $ fireplace_OBJ.idle = "fireplace_idle_shadow"
            call gen_chibi("stand","mid","base")
            with d5
            m "*Hmm*... Looks like an ordinary fireplace..."
            call gen_chibi("sit_behind_desk")
            with d5
        else:
            m "Looks like a normal fireplace to me."

        if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    if is_puzzle_box_in_fireplace():
        call gen_chibi("stand", "fireplace", "fireplace")
        with d3
        m "(*Hmm*... There's something glimmering in the fireplace.)"
        m "(A loose brick... If only I could..{nw}{w=1.0}"
        $ renpy.play('sounds/brick_scrape.mp3')
        m "(A loose brick... If only I could..{fast} *Hhng*... There we go.)"
        call give_reward("A puzzle box has been added to your inventory!", "interface/icons/puzzle_box.webp")

        $ puzzle_box_ITEM.owned = 1

        m "Seems straight forward enough."
        m "Maybe I should give it a try?"
        menu:
            "-Try solving the puzzle-":
                call gen_chibi("sit_behind_desk")
                with d3
                $ puzzle_box_ITEM.use()
            "-Save it for later-":
                m "I don't have time for this now."
        call gen_chibi("sit_behind_desk")
        with d3

    else:
        if fire_in_fireplace:
            $ fire_in_fireplace = False
            $ fireplace_OBJ.foreground = None
        else:
            $ fire_in_fireplace = True
            $ fireplace_OBJ.foreground = "fireplace_fire"
            $ stat_fireplace_counter += 1

    jump main_room_menu

init python:
    def is_puzzle_box_in_fireplace():
        return game.day >= 25 and not game.daytime and game.moon and not puzzle_box_ITEM.unlocked and not unlocked_7th
