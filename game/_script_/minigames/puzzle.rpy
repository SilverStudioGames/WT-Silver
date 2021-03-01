init python:
    def generate_puzzle(tiles=16):
        if not tiles % 2 == 0:
            raise Exception("Number of tiles has to be an even number.")

        def is_solveable(puzzle):
            sums = 0
            for x in xrange(tiles-1):
                for y in xrange(x+1, tiles):
                    if puzzle[x] > puzzle[y]:
                        sums += 1
            return sums % 2 == 0

        puzzle = [i for i in xrange(tiles-1)] + [None]
        renpy.random.shuffle(puzzle)

        if is_solveable(puzzle):
            return puzzle
        return generate_puzzle(tiles)

screen puzzle_minigame():
    tag puzzle
    zorder 30

    default tries = 0
    default tiles = generate_puzzle()
    default hint = False
    $ score = 0

    add "gui_fade"
    use close_button()
    use meter(fill=100-tries)

    frame:
        align (0.5, 0.5)
        background Transform("interface/puzzle/background.webp", align=(0.5, 0.5))

        grid 4 4:
            for i, tile in enumerate(tiles):
                $ img = "interface/puzzle/{}.webp".format(tile)
                $ empty = tiles.index(None)
                $ is_valid = (i in (empty-1, empty+1, empty-4, empty+4)
                                and not ( (empty % 4 == 3) and (i % 4 == 0) )
                                and not ( (empty % 4 == 0) and (i % 4 == 3) ) )
                imagebutton:
                    xysize (94, 94)
                    if tile is None:
                        idle Null()
                        action NullAction()
                    else:
                        hover image_hover(img)
                        if is_valid:
                            idle At(img, pulse_hover(pause=3.0))
                            action [SetScreenVariable("tries", tries+1), Function(list_swap_values, tiles, empty, i)]
                        else:
                            idle img
    if hint:
        button:
            style "empty"
            align (0.5, 0.5)
            background Transform("interface/puzzle/background.webp", align=(0.5, 0.5))
            add "interface/puzzle/puzzle.webp"
            action NullAction()

    for i, tile in enumerate(tiles):
        if i == tile:
            $ score += 1

    if score >= 15:
        timer 0.1 action Return(True)

    vbox:
        yanchor 0.0
        align (0.5, 0.85)
        textbutton "-Hint-" xalign 0.5 action ToggleScreenVariable("hint", True, False)
        if tries >= 25:
            textbutton "-Force it open-" xalign 0.5 action Return(False)

label puzzle_minigame:
    call screen puzzle_minigame()

    if _return == True:
        m "Finally... "
        m "What is this?"
        m "Sweet, phoenix tears! Down the hatch we go."
        $ renpy.play("sounds/pop03.mp3")
        $ renpy.play("sounds/gulp.mp3")
        pause 1
        $ renpy.play("sounds/gulp.mp3")
        m "...."
        m "I feel no difference..."
        $ achievement.unlock("puzzle")
    elif _return == False:
        g4 "Fuck it..."
        $ renpy.play('sounds/door_down.mp3')
        with hpunch
        "{size=32}*Smash*{/size}"
        $ renpy.play('sounds/glass_shatter.mp3')
        m "A broken bottle..."
        m "Oh well, too late now. Back to my usual--"
    else: # Closed
        m "(Maybe next time...)"
        jump main_room_menu

    m "Hold on a second, there's a book in here..."
    m "Seems to be some sort of notebook, I'll skim through it..."

    call book_start

    m "\"My dear phoenix has been losing his feathers lately, I think it's time soon...\""
    m "(Time for what?)"
    m "\"That Potter boy is mighty cute, looks just like his father...\""
    g9 "(Well, well...)"
    m "\"Severus gave me a weird look today, I wonder what he thinks about my...\""
    g4 "(This is all trash...)"
    m "(Wait a minute... this seems interesting.)"
    m "\"I was walking around in the seventh floor corridor looking for a bathroom...\""
    m "\"Whilst searching, a room that I had never seen before appeared, filled with chamber pots... But when I returned later, it was gone.\""

    call book_end

    m "(I've seen enough magic to know where this is going... I should investigate that corridor on the seventh floor.)"
    call give_reward("You've unlocked something on the 7th floor, check your map to get there.","/images/rooms/room_of_requirement/mirror.webp")

    if deck_unlocked:
        m "What's this?"
        call give_reward("You have found a card at the bottom of the box!", "images/cardgame/t1/other/elf_v1.webp")
    $ unlocked_cards += [card_item_elf]
    $ unlocked_7th = True
    $ puzzle_box_ITEM.owned = 0
    $ puzzle_box_ITEM.used = True

    if game.daytime:
        jump night_start
    else:
        jump day_start

    jump main_room_menu
