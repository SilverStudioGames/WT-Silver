define achievements_dict = {
    "unlockher": ["Characters", "Granger Danger", "Awarded for unlocking Hermione Granger.", False, "interface/icons/head/hermione.webp", False],
    "unlockcho": ["Characters", "Chang Dynasty", "Awarded for unlocking Cho Chang.", False, "interface/icons/head/cho.webp", False],
    "unlocklun": ["Characters", "Looney Tunes", "Awarded for unlocking Luna Lovegood.", False, "interface/icons/head/luna.webp", False],
    "unlockast": ["Characters", "Greenpeas", "Awarded for unlocking Astoria Greengrass.", False, "interface/icons/head/astoria.webp", False],
    "unlockton": ["Characters", "Nymphadoreador", "Awarded for unlocking Nymphadora Tonks.", False, "interface/icons/head/tonks.webp", False],
    "overwhored": ["Characters", "Overwhored", "Hermione reached maximum corruption.", False, "interface/icons/head/hermione.webp", False],
    "unlocksus": ["Characters", "Boner", "Awarded for unlocking Susan Bones.", False, "interface/icons/head/susan.webp", False],
    "unlocksna": ["Characters", "Strictly colleagues", "Awarded for unlocking Severus Snape.", False, "interface/icons/head/snape.webp", False],
    "mirror": ["Mirror", "Mirror, mirror on the wall..", "Awarded for unlocking the Room of Requirements.", False, "images/rooms/room_of_requirement/mirror_hover.webp", False],
    "gold": ["General", "Gold Digger", "Awarded for collecting 10000 gold coins.", False, "interface/icons/gold.webp", False],
    "drunkard": ["General", "Drunken Master", "Collected 25 bottles of wine.", False, "interface/icons/wine.webp", True],
    "workaholic": ["General", "Workaholic", "Completed 5 full reports.", False, "interface/icons/generic_scroll.webp", False],
    "fireplace": ["General", "Feel the Heat", "Started fire 5 times or more.", False, "images/rooms/objects/fireplace/fireplace_idle.webp", True],
    "peta": ["General", "I think I forgot something...", "Awarded for not feeding the bird for 50 days.... \nYou monster.\n{size=-4}Disclaimer: No real nor fictional animals were harmed in the process.{/size}", False, "images/rooms/objects/phoenix/phoenix_01.webp", True],
    "petpal": ["General", "Regular stroking", "Awarded for petting the bird 25 times.", False, "images/rooms/objects/phoenix/phoenix_01.webp", False],
    "postman": ["Cardgame", "Poster Boy", "Bought all posters from the token shop.", False, "interface/icons/agrabah_poster.webp", False],
    "hats": ["Cardgame", "Mad Hatter", "Bought all hat decorations from the token shop.", False, "interface/icons/icon_gambler_hat.webp", False],
    "daddy": ["Characters", "Who's your daddy?", "Let Hermione call you a {size=-5}(sugar){/size} daddy.", False, "interface/icons/head/hermione.webp", True],
    "pantiesfap": ["Characters", "I sneezed on them...", "Rubbed one out on Hermione's panties.", False, "characters/genie/chibis/jerk_off/02.webp", False],
    "pantiesfapcho": ["Characters", "Exercise is important", "Rubbed one out on Cho's panties.", False, "characters/genie/chibis/jerk_off/02.webp", False],
    "bros": ["Characters", "Bros before hoes", "Became best pals with Snape.", False, "interface/icons/head/snape.webp", False],
    "knock": ["Characters", "*Knock* *knock*", "Go away! I'm busy.", False, "images/rooms/objects/doors/door_idle.webp", True],
    "decorator": ["Cardgame", "Decorator", "Applied decoration in the office.", False, "interface/icons/stag_trophy.webp", False],
    "flashback": ["Cardgame", "Flashback", "Totally what happened...", False, "interface/icons/cards.webp", True],
    "start": ["General", "Welcome to Hogwarts!", "Awarded upon finishing the intro.", False, "interface/icon.webp", False],
    "export": ["General", "Sharing is caring", "Exported an outfit through the wardrobe menu.", False, "interface/wardrobe/icons/load.webp", False],
    "Credits":  ["General", "New game, who this?", "Checked out the Credits Menu", False, "interface/icons/silver_scroll.webp", False],
    "Cardwin":  ["Cardgame", "Time to duel", "Awarded for winning your first Cardgame duel", False, "interface/icons/cards.webp", False],
    "puzzle": ["General", "Down the hatch!", "Wasted a bottle of unbelievably rare phoenix tears by drinking it.", False, "interface/icons/item_potion.webp", True],
    "ending": ["General", "Bittersweet Farewell", "Finished the game.", False, "interface/icons/book_silver.webp", True],
    #1.37 HG achievements
    "busted": ["Characters", "BUSTED!", "... a nut when got busted for busting a nut.", False, "interface/icons/head/hermione.webp", False],
    "herstrip": ["Characters", "Dance lessons", "Even elephants have more grace when they're moving, girl.. -Severus Snape", False, "interface/icons/head/hermione.webp", False],
    "herkiss": ["Characters", "First Kiss", "Hermione made out with you-- r... cock...", False, "interface/icons/head/hermione.webp", False],
    "hertits": ["Characters", "Boobs Lover", "*ahem* I mean.. books, yes, books lover!", False, "interface/icons/head/hermione.webp", False],
    "headlib": ["Characters", "Head Librarian", "Did she just swallow it?", False, "interface/icons/head/hermione.webp", False],
    "nerdgasm": ["Characters", "Nerdgasm", "Had a very fulfilling moment with Hermione.", False, "interface/icons/head/hermione.webp", False]
}

init python:
    if persistent.achievements == None:
        persistent.achievements = achievements_dict.copy()

    def achievement_fix(reset=False):
        """Try and fix broken achievements in persistent file by comparing dictionary values
        and replacing them with correct values without resetting the achievement progress."""

        for key, value in persistent.achievements.iteritems():
            # Category
            if value[0] != achievements_dict[key][0]:
                value[0] = achievements_dict[key][0]
                print "Fixing achievement \""+key+"\" val 0"

            # Name
            if value[1] != achievements_dict[key][1]:
                value[1] = achievements_dict[key][1]
                print "Fixing achievement \""+key+"\" val 1"

            # Desc
            if value[2] != achievements_dict[key][2]:
                value[2] = achievements_dict[key][2]
                print "Fixing achievement \""+key+"\" val 2"

            # Icon
            if value[4] != achievements_dict[key][4]:
                value[4] = achievements_dict[key][4]
                print "Fixing achievement \""+key+"\" val 4"

            # Hidden status
            if value[5] != achievements_dict[key][5]:
                value[5] = achievements_dict[key][5]
                print "Fixing achievement \""+key+"\" val 5"

            # Resets achievements
            if reset:
                value[3] = False
        return


    class Achievements(object):

        def __init__(self):
            self.achievements = persistent.achievements

        def status(self, id):
            return self.achievements.get(id)[3]

        def unlock(self, id, silent=False):
            try:
                if persistent.achievements[id][3] == False:
                    self.achievements[id][3] = True
                    persistent.achievements[id][3] = True
                    if not silent:
                        renpy.play('sounds/achievement.mp3')
                        renpy.show_screen("achievement_window", string=persistent.achievements[id][1], title="Achievement unlocked!", icon=persistent.achievements[id][4])
                return
            except KeyError:
                return

        def lock(self, id):
            self.achievements[id][3] = False
            persistent.achievements[id][3] = False

    def achievement_sortfilter(item, sortby="A-z", filtering=None):
        if filtering == "Locked":
            item = filter(lambda x: x[1][3] is False, item)
        elif filtering == "Unlocked":
            item = filter(lambda x: x[1][3] is True, item)
        elif filtering == "Secret":
            item = filter(lambda x: x[1][5] is True, item)

        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: natsort_key(x[1][1]))

        if sortby == "z-A":
            item = sorted(item, key=lambda x: natsort_key(x[1][1]), reverse=True)
        elif current_sorting == "Unlocked":
            item = sorted(item, key=lambda x: x[1][3] is False)
        elif current_sorting == "Locked":
            item = sorted(item, key=lambda x: x[1][3] is True)

        return item

    achievement = Achievements()

label popup(string="", title="", icon=None, xpos=0, ypos=60, sound=True, soundfile='sounds/achievement.mp3'):
    if sound:
        $ renpy.play(soundfile)
    show screen achievement_window(string=string, title=title, icon=icon, xpos=xpos, ypos=ypos)
    return

screen achievement_window(string="", title="", icon=None, xpos=0, ypos=60):
    tag popup_window
    layer "interface"

    frame:
        style "empty"
        at popup_animation(time=5.0, xx=-410)
        pos (xpos, ypos)
        xsize 410
        ysize 96

        add gui.format("interface/achievements/{}/box.webp")
        if icon:
            frame:
                style "empty"
                pos (6, 6)
                xsize 84
                ysize 84
                $ image_zoom = crop_image_zoom(icon, 84, 84)
                if 'head' in icon:
                    add image_zoom align (0.5, 1.0) yoffset -1
                else:
                    add image_zoom align (0.5, 0.5)

            add "interface/achievements/glass.webp"
        frame:
            style "empty"
            xpos 96
            xsize 314
            vbox:
                ypos 12
                spacing 10
                xalign 0.5
                text title size 18 xalign 0.5 xanchor 0.5
                text string size 14 xalign 0.5 xanchor 0.5
    timer 6.0 action Hide("achievement_window")

transform rotate_circular():
    on show, appear, start:
        rotate 0
        linear 7.0 rotate 360
        repeat

####################################
############# Menu #################
####################################

label achievement:
    $ gui.in_context("achievement_menu")
    jump main_room_menu

label achievement_menu(xx=150, yy=90):

    $ achievement_categories_sorted = ["All", "General", "Characters", "Cardgame", "Mirror"]
    $ achievement_categories_sorted_length = len(achievement_categories_sorted)

    $ items_shown = 36
    $ current_page = 0
    $ current_category = achievement_categories_sorted[0]
    $ current_filter = None
    $ current_sorting = "Unlocked"

    $ category_items = list(persistent.achievements.iteritems())
    $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
    $ menu_items_length = len(menu_items)
    $ current_item = next(iter(menu_items), None)

    if not renpy.android:
        show screen tooltip

    show screen achievements(xx, yy)

    label .after_init:
    $ _choice = ui.interact()

    if _choice[0] == "select":
        $ current_item = _choice[1]
    elif _choice[0] == "category":
        $ current_category = _choice[1]
        if current_category == "All":
            $ category_items = list(persistent.achievements.iteritems())
        else:
            $ category_items = filter(lambda x: current_category in x[1][0], list(persistent.achievements.iteritems()))
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    elif _choice == "inc":
        $ current_page += 1
    elif _choice == "dec":
        $ current_page += -1
    elif _choice == "filter":
        if current_filter == None:
            $ current_filter = "Locked"
        elif current_filter == "Locked":
            $ current_filter = "Unlocked"
        elif current_filter == "Unlocked":
            $ current_filter = "Secret"
        else:
            $ current_filter = None
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    elif _choice == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        elif current_sorting == "z-A":
            $ current_sorting = "Unlocked"
        elif current_sorting == "Unlocked":
            $ current_sorting = "Locked"
        else:
            $ current_sorting = "A-z"
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    else:
        hide screen achievements
        return

    jump .after_init

screen achievements(xx, yy):
    tag achievements
    zorder 30
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background

    use close_button

    fixed:
        if settings.get("animations"):
            at gui_animation
        use achievement_menu(xx, yy)
        use achievement_menuitem(xx, yy)

screen achievement_menu(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme('achievements')
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            style_prefix gui.theme('achievements_categories')
            pos (6, 41)
            for category in achievement_categories_sorted:
                vbox:
                    textbutton category:
                        selected (current_category == category)
                        action Return(["category", category])

                    add gui.format("interface/achievements/{}/spacer_left.webp")
        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)
            if current_filter == None:
                textbutton "Show: All" action Return("filter")
            else:
                textbutton "Show: [current_filter]" action Return("filter")
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen achievement_menuitem(xx, yy):
    window:
        style "empty"
        pos (xx+217, yy-53)
        xysize (560, 507)

        use invisible_button()

        add "interface/achievements/star.webp"
        add gui.format("interface/achievements/{}/panel.webp")

        text "Achievements" size 22 xalign 0.5 ypos 65

        text "Unlocked: "+str(len(filter(lambda x: x[1][3] is True, menu_items)))+"/[menu_items_length]" size 12 pos (24, 70)

        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                pos (540, 24)
                spacing 5
                add "interface/page.webp" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown))+1) ypos 44 size 16
            vbox:
                pos (570, 186)
                spacing 10

                imagebutton:
                    idle gui.format("interface/frames/{}/arrow_up.webp")
                    if not current_page <= 0:
                        hover image_hover(gui.format("interface/frames/{}/arrow_up.webp"))
                        action Return("dec")

                imagebutton:
                    idle Transform(gui.format("interface/frames/{}/arrow_up.webp"), yzoom = -1.0)
                    if current_page < math.ceil((menu_items_length-1)/items_shown):
                        hover Transform(image_hover(gui.format("interface/frames/{}/arrow_up.webp")), yzoom = -1.0)
                        action Return("inc")

        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 9) % 4
                $ col = i % 9
                frame:
                    style "empty"
                    xsize 48
                    ysize 48
                    pos (24+58*(col), 113+58*(row))
                    add gui.format("interface/achievements/{}/iconbox.webp")

                    if current_item and current_item[0] == menu_items[i][0]:
                        add "interface/achievements/glow.webp" align (0.5, 0.5) zoom 0.105 alpha 0.7 at rotate_circular

                    if menu_items[i][1][4]:
                        if menu_items[i][1][3]:
                            $ image_zoom = crop_image_zoom(menu_items[i][1][4], 42, 42)
                        elif not menu_items[i][1][5]:
                            $ image_zoom = crop_image_zoom(menu_items[i][1][4], 42, 42, True)
                        else:
                            $ image_zoom = crop_image_zoom("interface/achievements/secret.webp", 35, 35, True)

                        if menu_items[i][1][0] == "Characters" and not (menu_items[i][1][5] is True and not menu_items[i][1][3] is True):
                            add image_zoom align (0.5, 1.0) yoffset -3
                        else:
                            add image_zoom align (0.5, 0.5)

                    button:
                        style gui.theme("overlay_button")
                        background "interface/achievements/glass_iconbox.webp"
                        xsize 48 ysize 48
                        action Return(["select", menu_items[i]])
                        if menu_items[i][1][5] and not menu_items[i][1][3]:
                            tooltip "???"
                        else:
                            tooltip str(menu_items[i][1][1])

        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add gui.format("interface/achievements/{}/icon_selected.webp")
                if current_item[1][4]:
                    if current_item[1][3]:
                        $ image_zoom = crop_image_zoom(current_item[1][4], 84, 84)
                    else:
                        if current_item[1][5]:
                            $ image_zoom = crop_image_zoom("interface/achievements/secret.webp", 70, 70, True)
                        else:
                            $ image_zoom = crop_image_zoom(current_item[1][4], 84, 84, True)
                    if current_item[1][0] == "Characters" and not (current_item[1][5] is True and not current_item[1][3] is True):
                        add image_zoom align (0.5, 1.0) yoffset -7
                    else:
                        add image_zoom align (0.5, 0.5)
                add "interface/achievements/glass_selected.webp" pos (6, 6)

            add gui.format("interface/achievements/{}/highlight.webp") pos (112, 375)
            add gui.format("interface/achievements/{}/spacer.webp") pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item[1][1] ypos 380 size 16 xoffset 45
                if current_item[1][3]:
                    add "interface/unlocked_True.webp" xoffset 45 ypos 377
                else:
                    add "interface/unlocked_False.webp" xoffset 45 ypos 377
            hbox:
                pos (132, 407)
                xsize 410
                if current_item[1][3]:
                    text current_item[1][2] size 12
                else:
                    if current_item[1][5]:
                        text "???" size 12
                    else:
                        text current_item[1][2] size 12

# Category styles
style achievements_categories_button is empty:
    xysize (195, 16)

style dark_achievements_categories_button:
    hover_background "interface/achievements/gray/highlight_left.webp"
    selected_background "interface/achievements/gray/highlight_left.webp"

style light_achievements_categories_button:
    hover_background "interface/achievements/gold/highlight_left.webp"
    selected_background "interface/achievements/gold/highlight_left.webp"

style achievements_categories_button_text is text:
    xalign 0.5
    outlines []

# style dark_achievements_categories_button_text:
#     take dark_button_text

# style light_achievements_categories_button_text:
#     take light_button_text

# Filter styles
style achievements_filters_button is empty:
    xysize (195, 32)

style dark_achievements_filters_button:
    hover_background "#7d75aa40"

style light_achievements_filters_button:
    hover_background "#e3ba7140"

style achievements_filters_button_text is default:
    align (0.5, 0.5)
    size 12
    outlines []
