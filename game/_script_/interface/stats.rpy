init python:
    def stats_sortfilter(item, sortby=False):
        return item

default stats_show_locked = False

label update_stats:

    ### Hermione ###

    # Whoring
    $ her_whoring_word_list = ["Pure", "Naive", "Curious", "Naughty", "Perverse", "Immoral", "Slutty", "Shameless", "Cumslut", "Total Cumslut", "Shameless Cumslut"]
    $ her_whoring_word = her_whoring_word_list[int(her_whoring/2.4)]

    # Reputation
    $ her_reputation_word_list = ["Teacher's pet", "School star", "good girl", "minx", "slutty schoolgirl", "easy lay", "whore", "slut for sex", "gryffindor whore", "school cumdump", "mudblood cumdump"]
    #$ slutWords = ["Teacher's pet", "School star", "good girl", "headmaster's pet", "slutty schoolgirl", "slut", "headmaster's slut", "daddy's girl", "gryffindor slut", "Dumbledore's whore", "Dumbledore's cumdump"]
    $ her_reputation_word = her_reputation_word_list[int(her_reputation/2.4)]

    # Tutoring
    $ her_tutoring_word_list = ["Not started", "naive", "tempted", "curious", "tainted", "eager", "sinful", "perverted", "corrupted", "depraved", "shattered"]
    $ her_tutoring_word = her_tutoring_word_list[int(her_tutoring/1.5)]

    # Mood
    $ her_mood_word_list = ["Cheerful", "Reluctant", "Gloomy", "Stern", "Slightly Annoyed", "Annoyed", "Upset", "Outraged", "Mad", "Angry", "Very Angry"]
    if her_mood >= 0 and her_mood <= 10:
        $ her_mood_word = her_mood_word_list[int(her_mood/1.0)]
    else:
        $ her_mood_word = "Very Angry"

    ### Astoria ###
    #call astoria_clothing_level
    #$ ast_cuteness_word_list = ["Ugly Duckling", "Swot", "", "", "", "", "", "Cutypie", "", "", ""]
    #$ ast_cuteness_word = ast_cuteness_word_list[int(ast_clothing_level/10)]
    # Mood
    $ ast_mood_word_list = ["Cheerful", "Reluctant", "Gloomy", "Stern", "Slightly Annoyed", "Annoyed", "Upset", "Outraged", "Mad", "Angry", "Very Angry"]
    if ast_mood >= 0 and ast_mood <= 10:
        $ ast_mood_word = ast_mood_word_list[int(ast_mood/1.0)]
    else:
        $ ast_mood_word = "Very Angry"

    ### Cho ###

    # Whoring
    $ cho_whoring_word_list = ["Incorruptible", "Focused", "Resilient", "Bi-Curious", "Naughty", "Immoral", "Perverse", "Slutty", "Shameless", "Cumslut", "Shameless Cumslut"]
    $ cho_whoring_word = cho_whoring_word_list[int(cho_whoring/2.4)]

    # Reputation
    $ cho_reputation_word_list = ["Tomboy", "Team Player", "Quidditch Star", "Flying Ace", "Minx", "Manipulative", "Exploiting", "Cheater", "Team's Cumdump", "Quidditch Whore", "Cheating Slut"]
    $ cho_reputation_word = cho_reputation_word_list[int(cho_reputation/2.4)]

    # Mood
    $ cho_mood_word_list = ["Cheerful", "Reluctant", "Gloomy", "Stern", "Slightly Annoyed", "Annoyed", "Upset", "Outraged", "Mad", "Angry", "Very Angry"]
    if cho_mood >= 0 and cho_mood <= 10:
        $ cho_mood_word = cho_mood_word_list[int(cho_mood/1.0)]
    else:
        $ cho_mood_word = "Very Angry"

    ### Snape ###

    # Support
    $ sna_support_word_list = ["Tight-Arse", "Miser", "Stingy", "Sparing", "Adequate", "Loose", "Easy", "Generous", "Frivolous", "Excessive", "Exorbitant"]
    $ sna_support_word = sna_support_word_list[int(sna_support/1.5)]

    # Friendship
    $ sna_friendship_word_list = ["Unknown", "Colleague", "Confidant", "Trusted", "Acquaintance", "Friend", "Good friend", "Homie", "If I had to pick a dude...", "BFF", "Bros"]
    $ sna_friendship_word = sna_friendship_word_list[int(sna_friendship/10)]

    ### Tonks ###

    # Reputation
    $ ton_reputation_word_list = ["Teacher", "Bore", "Weirdo", "A Bit Nutty", "Easy Going", "Tart", "Naughty Teacher", "Slutty Teacher", "Slag", "Shameful", "Disgrace"]
    $ ton_reputation_word = ton_reputation_word_list[int(ton_reputation/2.4)]

    # Support
    $ ton_support_word_list = ["Undecided", "Modest", "Candid", "Unbiased", "Positive", "Fair", "Neutral", "Biased", "Scummy", "Cruel", "Heartless"]
    $ ton_support_word = ton_support_word_list[int(ton_support/1.2)]

    # Friendship
    $ ton_friendship_word_list = ["Unknown", "inferior", "employee", "advisor", "trusted advisor", "Acquaintance", "friend", "Girlfriend", "Partner in crime", "Bonnie & Clyde", "Master & Slave"]
    $ ton_friendship_word = ton_friendship_word_list[int(ton_friendship/10)]

    #$ ton_sluttiness_word_list = ["Masochist", "Disgrace", "Street Whore", "Harlot", "Tart", "Sexually open", "Naughty Teacher", "Easy Going", "Professor", "Bore", "Nun"]
    #$ ton_sluttiness_word = ton_sluttiness_word_list[int(ton_clothing_level/10)]

    return

label stats:
    $ gui.in_context("stats_menu")
    jump main_room_menu

label stats_menu(xx=150, yy=90):

    call update_stats

    # Stats dictionary
    $ stats_dict = {
                    "Genie": {"ico": "genie", "flag": True, "name": "Genie", "sex": "Yes", "height": "6.2ft", "weight": "200lb", "job": "Headmaster", "hates": "Lamps", "likes": "Tits"},
                    "Snape": {"ico": "snape", "flag": snape_unlocked, "name": "Severus Snape", "sex": "Male", "height": "5.9ft", "weight": "155lb", "job": "Teacher", "hates": "Everyone", "likes": "Rain"},
                    "Tonks": {"ico": "tonks", "flag": tonks_unlocked, "name": "Nymphadora Tonks", "sex": "Fluid", "height": "5.6ft", "weight": "130lb", "job": "Teacher", "hates": "Pineapple Pizza", "likes": "Girls"},
                    "Hermione": {"ico": "hermione", "flag": hermione_unlocked, "name": "Hermione Granger", "sex": "Female", "height": "5.2ft", "weight": "126lb", "job": "Student", "hates": "Slytherin", "likes": "Books"},
                    "Cho": {"ico": "cho", "flag": cho_unlocked, "name": "Cho Chang", "sex": "Female", "height": "5.1ft", "weight": "122lb", "job": "Student", "hates": "Hermione", "likes": "Winning"},
                    "Luna": {"ico": "luna", "flag": luna_unlocked, "name": "Luna Lovegood", "sex": "Female", "height": "5.2ft", "weight": "117lb", "job": "Student", "hates": "Wrackspurts", "likes": "{size=-2}Magical creatures{/size}"},
                    "Astoria": {"ico": "astoria", "flag": astoria_unlocked, "name": "Astoria Greengrass", "sex": "Female", "height": "5.0ft", "weight": "102lb", "job": "Student", "hates": "Rules", "likes": "Breaking them"},
                    "Susan": {"ico": "susan", "flag": susan_unlocked, "name": "Susan Bones", "sex": "Female", "height": "5.1ft", "weight": "135lb", "job": "Student", "hates": "Chores", "likes": "You {size=-4}Secretly..{/size}"}
                    }

    $ stats_categories_sorted = ["Genie", "Snape", "Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"] #"Ginny", "Daphne", "Padma", "Patil", "Myrtle", "Mafkin"
    $ stats_categories_sorted_length = len(stats_categories_sorted)

    $ current_category = last_character.capitalize() if last_character else stats_categories_sorted[0]
    $ current_item = stats_dict[current_category]
    $ current_subcategory = "overview"
    $ current_sorting = stats_show_locked

    $ category_items = stats_dict[current_category]
    $ menu_items = category_items
    $ menu_items_length = len(menu_items)

    # Reset legacy character positioning
    # TODO: Remove it once all characters have been converted into a class.
    $ luna_xpos = 640
    $ luna_ypos = 0
    $ susan_xpos = 300
    $ susan_ypos = 0

    if not renpy.android:
        show screen mouse_tooltip

    show screen stats_menu(xx, yy)
    show screen stats_menuitem(xx, yy)
    with d3

    label .after_init:
    $ _return = ui.interact()

    if _return[0] == "category":
        $ current_category = _return[1]
        $ category_items = stats_dict[current_category]
        $ menu_items = stats_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_item = stats_dict[current_category]
        #$ current_subcategory = "overview"
    elif _return[0] == "subcat":
        if _return[1] != current_subcategory:
            $ current_subcategory = _return[1]
    else:
        hide screen stats_menu
        hide screen stats_menuitem
        return

    jump .after_init

screen stats_menu(xx, yy):
    tag stats_menu
    zorder 30
    modal True

    add "gui_fade"

    use invisible_button(action=Return("Close"))
    use close_button

    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "Show locked:":
                    style gui.theme("overlay_button")
                    xsize 195 ysize 32
                    text_align (0.4, 0.5)
                    text_size 12
                    action ToggleVariable("stats_show_locked", True, False)
                add gui.format("interface/frames/{}/check_")+str(stats_show_locked).lower()+".webp" xalign 0.8 ypos 4
        vbox:
            pos (6, 6)
            for category in stats_categories_sorted:
                if not stats_show_locked and not stats_dict[category]["flag"]:
                    pass
                else:
                    frame:
                        style "empty"
                        xysize (195, 50)
                        vbox:
                            textbutton (category if stats_dict[category]["flag"] else "???"):
                                style "empty"
                                xysize (195, 48)
                                text_align (0.6, 0.5)
                                text_xanchor 0.5
                                text_size 20
                                if current_category == category:
                                    background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                else:
                                    hover_background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                    action Return(["category", category])

                            add gui.format("interface/achievements/{}/spacer_left.webp")
                        add gui.format("interface/achievements/{}/iconbox.webp") yoffset 1
                        if stats_dict[category]["flag"]:
                            $ image_zoom = crop_image_zoom("interface/icons/head/"+stats_dict.get(category).get("ico")+".webp", 42, 42)
                        else:
                            $ image_zoom = crop_image_zoom("interface/icons/head/"+stats_dict.get(category).get("ico")+"_locked.webp", 42, 42)
                        frame:
                            style "empty"
                            xsize 42
                            ysize 42
                            add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                        add "interface/achievements/glass_iconbox.webp" pos (3, 3)

transform at_zoom(zoom=1.0):
    zoom zoom

screen stats_menuitem(xx, yy):
    tag stats_menuitem
    zorder 30
    frame:
        style "empty"
        style_prefix gui.theme()
        pos (xx+217, yy-53)
        xysize (560, 507)

        use invisible_button()

        #add "interface/achievements/inventory.webp"
        add gui.format("interface/achievements/{}/panel.webp")
        add "interface/achievements/markup.webp"

        text "Characters" size 22 xalign 0.5 ypos 65

        hbox:
            pos (24, 65)
            textbutton "Overview":
                text_size 12
                action [Return(["subcat", "overview"]), SelectedIf(current_subcategory=="overview")]
                background None
            textbutton "Details":
                text_size 12
                action [Return(["subcat", "details"]), SelectedIf(current_subcategory=="details")]
                background None

        # Character sprites
        frame:
            style "empty"
            xysize (200, 406)
            align (1.0, 1.0)
            offset (-10, -4)

            if current_category == "Genie":
                add "characters/genie/base/base.webp" zoom 0.346 align (1.0, 1.0) xzoom -1
            elif current_category == "Snape":
                if current_item["flag"]:
                    add "characters/snape/main/snape_09.webp" zoom 0.34 align (0.9, 1.0)
                else:
                    add "interface/characters/snape_locked.webp" zoom 0.34 align (0.9, 1.0)
            elif current_category == "Tonks":
                if current_item["flag"]:
                    add tonks.get_image() zoom 0.4 align (0.7, 1.0)
                else:
                    add "interface/characters/tonks_locked.webp" zoom 0.4 align (0.7, 1.0)
            elif current_category == "Hermione":
                if current_item["flag"]:
                    add hermione.get_image() zoom 0.4 align (0.7, 1.0)
                else:
                    add "interface/characters/hermione_locked.webp" zoom 0.38 align (0.65, 1.0)
            elif current_category == "Cho":
                if current_item["flag"]:
                    add cho.get_image() zoom 0.4 align (0.65, 1.0)
                else:
                    add "interface/characters/cho_locked.webp" zoom 0.4 align (0.65, 1.0)
            elif current_category == "Luna":
                if current_item["flag"]:
                    frame:
                        style "empty"
                        #align (0.7, 1.0)
                        at at_zoom(0.75)
                        offset (-620, -44)

                        use luna_main
                else:
                    add "interface/characters/luna_locked.webp" zoom 0.38 align (0.75, 1.0)
            elif current_category == "Astoria":
                if current_item["flag"]:
                    add astoria.get_image() zoom 0.4 align (0.7, 1.0)
                else:
                    add "interface/characters/astoria_locked.webp" zoom 0.38 align (0.7, 1.0)
            elif current_category == "Susan":
                if current_item["flag"]:
                    frame:
                        style "empty"
                        #align (0.7, 1.0)
                        at at_zoom(0.78)
                        offset (-350, -62)

                        use susan_main
                else:
                     add "interface/characters/susan_locked.webp" zoom 0.385 align (0.65, 1.0)

        frame:
            style "empty"
            xysize (360, 406)
            yalign 1.0 xoffset 6

            if current_subcategory == "overview":
                if current_item["flag"]:
                    text current_item["name"] size 20 xalign 0.5 xanchor 0.5 ypos 5
                else:
                    text "???" size 20 xalign 0.5 xanchor 0.5 ypos 5

                vbox:
                    xoffset 10
                    hbox:
                        spacing 20
                        pos (10, 36)

                        vbox:
                            text "Sex:" size 15
                            text "Height:" size 15
                            text "Weight:" size 15

                        vbox:
                            spacing 3
                            if current_item["flag"]:
                                text current_item["sex"] size 12
                                text current_item["height"] size 12
                                text current_item["weight"] size 12
                            else:
                                text "unknown" size 12
                                text "unknown" size 12
                                text "unknown" size 12

                        vbox:
                            text "Job:" size 15
                            text "Hates:" size 15
                            text "Likes:" size 15

                        vbox:
                            spacing 3
                            if current_item["flag"]:
                                text current_item["job"] size 12
                                text current_item["hates"] size 12
                                text current_item["likes"] size 12
                            else:
                                text "unknown" size 12
                                text "unknown" size 12
                                text "unknown" size 12

                    if current_item["flag"]:
                        vbox:
                            yoffset 35
                            xoffset 50
                            #style "empty"
                            at at_zoom(0.62)
                            if current_category == "Genie":
                                use stat_bar(int(100/10), "-Lust-", "", 100)
                                use stat_bar(int(0/10), "-Sanity-", "", 0)
                                use stat_bar(int(imagination +bdsm_imagination/1), "-Imagination-", "", imagination +bdsm_imagination)
                                if not cheat_reading:
                                    use stat_bar(int(speed_writing/0.25), "-Speed Writing-", "", speed_writing)
                                    use stat_bar(int(speed_reading/0.25), "-Speed Reading-", "", speed_reading)
                                #text "Jerked off -"+str(phoenix_fed_counter)+"- times"
                            elif current_category == "Snape":
                                use stat_bar(int(3/1.0), "-Mood-" , "Grumpy", 3)
                                use stat_bar(int(sna_support/1.5), "-Support-", sna_support_word, sna_support) # sna_support between 0 and 15.
                                use stat_bar(int(sna_friendship/10), "-Friendship-", sna_friendship_word, sna_friendship)
                            elif current_category == "Tonks":
                                use stat_bar(int(10/1.0), "-Mood-" , "Content", 10)
                                use stat_bar(int(ton_tier/0.2), "-Favour Tier-", "", ton_tier) # 4 will be max.
                                use stat_bar(int(ton_reputation/2.4), "-Reputation-", ton_reputation_word, ton_reputation) # Current max is 9.
                                use stat_bar(int(ton_support/1.2), "-Support-", ton_support_word, ton_support) # ton_support between 0 and 12.
                                use stat_bar(int(ton_friendship/10), "-Relationship-", ton_friendship_word, ton_friendship)
                            elif current_category == "Hermione":
                                use stat_bar(int(10-her_mood/1.0), "-Mood-" , her_mood_word, her_mood)
                                use stat_bar(int(her_tier/0.6), "-Favour Tier-", "", her_tier) # 6 will be max.
                                use stat_bar(int(her_whoring/2.4), "-Whoring-", her_whoring_word, her_whoring)
                                use stat_bar(int(her_reputation/2.4), "-Reputation-", her_reputation_word, her_reputation)
                                use stat_bar(int(her_tutoring/1.5), "-Tutoring-" , her_tutoring_word, her_tutoring)
                            elif current_category == "Cho":
                                use stat_bar(int(10-cho_mood/1.0), "-Mood-" , cho_mood_word, cho_mood)
                                use stat_bar(int(cho_tier/0.3), "-Favour Tier-", "", cho_tier) # 4 will be max.
                                use stat_bar(int(cho_whoring/0.9), "-Recklessness-", cho_whoring_word, cho_whoring)
                                use stat_bar(int(cho_reputation/0.9), "-Reputation-", cho_reputation_word, cho_reputation)
                                # TODO: Re-enable after Quidditch fixes
                                #use stat_bar(int((cc_ht.win_counter+cc_st.win_counter)/0.6), "{size=-10}-Quidditch Training-{/size}" , "Not started", cc_ht.win_counter+cc_st.win_counter) # TODO: Add word list # TODO: Add cc_gt.match_counter & cc_gt.win_counter
                            elif current_category == "Luna":
                                use stat_bar(int(10-lun_mood/1.0), "-Mood-" , "Cheerful", lun_mood) # TODO: Add word list
                                use stat_bar(int(lun_tier/0.4), "-Favour Tier-", "", lun_tier) # 4 is max.
                                use stat_bar(int(lun_whoring/0.9), "-Corruption-", "Naive", lun_whoring) # TODO: Add word list
                                use stat_bar(int(10/0.9), "-Reputation-", "Total Weirdo", 10) # Joke stat
                                use stat_bar(int(0), "{size=-10}-Wrackspurts Therapy-{/size}" , "Not started", 0) # TODO: Add word list and variable
                            elif current_category == "Astoria":
                                use stat_bar(int(10-ast_mood/1.0), "-Mood-" , ast_mood_word, ast_mood)
                                use stat_bar(int(1/1), "-Favour Tier-", "", 1)
                                use stat_bar(int(ast_whoring/0.8), "-Affection-", "", ast_whoring) # TODO: Add word list
                                use stat_bar(int(3/0.9), "-Reputation-", "Mischievous", 4) # TODO: Add word list and variable, starts at level 4
                                #use stat_bar(int(ast_training_counter/0.9), "-Spell training-" , "Not started", ast_training_counter) # TODO: Add word list
                            elif current_category == "Susan":
                                use stat_bar(int(10-sus_mood/1.0), "-Mood-" , "Cheerful", sus_mood) # TODO: Add word list
                                use stat_bar(int(1/0.9), "-Favour Tier-", "", 1) # TODO: Add Susan tier
                                use stat_bar(int(sus_whoring/0.9), "-Confidence-", "Non-existent", sus_whoring) # TODO: Add word list
                                use stat_bar(int(0/0.9), "-Reputation-", "Invisible", 0) # TODO: Add word list and variable
                                use stat_bar(int(0), "{size=-10}-Assertiveness Training-{/size}" , "Not started", 0) # TODO: Add word list
            else:
                if current_item["flag"]:
                    vbox:
                        if current_category == "Genie":
                            use text_stat("Bird fed:")
                            use text_stat("- ", " times -", phoenix_fed_counter)
                            use text_stat("Bird petted:")
                            use text_stat("- ", " times -", phoenix_petted_counter)
                            use text_stat("You missed feeding your bird for:")
                            use text_stat("- ", " days...", (day - phoenix_fed_counter) )
                            use text_stat("If you were a Quidditch player, you'd be a:")
                            use text_stat("- \"", "\" -", genie_quid_position)

                        elif current_category == "Snape":
                            use text_stat("Hung out with Snape:")
                            use text_stat("- ", " times -", ss_he_drink.counter)

                        elif current_category == "Tonks":
                            use text_stat("Hung out with Tonks:")
                            use text_stat("- ", " times -", nt_he_drink.counter)
                            #use text_stat("Hung out with Astoria:")
                            #use text_stat("- ", " times -", ton_astoria_date_counter)
                            use text_stat("Tonks has sluttyfied:")
                            use text_stat("- ", " outfits -", ton_clothing_upgrades)

                        elif current_category == "Hermione":
                            # Tier 1
                            use text_stat("You Jerked off in front of her:")
                            use text_stat("- ", " times -", her_jerk_off_counter)
                            use text_stat("You saw her panties:")
                            use text_stat("- ", " times -", hg_pf_admire_panties.counter)
                            use text_stat("You admired her tits:")
                            use text_stat("- ", " times -", hg_pf_admire_breasts.counter)
                            # Tier 2
                            use text_stat("You groped her:")
                            use text_stat("- ", " times -", hg_pf_grope.counter)
                            # Tier 3
                            use text_stat("Hermione has \"danced\" for you:")
                            use text_stat("- ", " times -", hg_pf_strip.counter)
                            # Tier 4
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Handjobs -", hg_pf_handjob.counter)
                            # Tier 5
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Blowjobs -", hg_pf_blowjob.counter)
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Tit jobs -", hg_pf_titjob.counter)
                            # Tier 6
                            use text_stat("You've had sex with her:")
                            use text_stat("- ", " times -", hg_pf_sex.counter)

                        elif current_category == "Cho":
                            use text_stat("You Jerked off in front of her:")
                            use text_stat("- ", " times -", cho_jerk_off_counter)
                        elif current_category == "Luna":
                            pass
                        elif current_category == "Astoria":
                            pass
                        elif current_category == "Susan":
                            use text_stat("Cursed with Imperio:")
                            use text_stat("- ", " times -", ag_se_imperio_sb.counter)

screen stat_bar(steps, top_text, bottom_text, stat_number, top_padding=20):
    sensitive False

    frame:
        background "#0000"
        ysize top_padding

    text top_text xalign 0.5 size 30

    frame:
        background "#0000"
        xalign 0.5
        ysize 30
        xsize 360
        add Crop((0, 0, steps*36, 600), gui.format("interface/stats/{}/bar_full.webp"))
        add gui.format("interface/stats/{}/bar_empty.webp")

    text bottom_text+" (lvl " +str(stat_number)+ ")" xalign 0.5 size 20

screen text_stat(startText="", endText="", amount="", top_padding = 20):
    sensitive False

    text (startText +str(amount)+ endText) xpos 20 size 14
