default cheats_active = False
default cheat_reading = False
default cheat_wardrobe_alpha = False

default skip_duel = False
default skip_to_hermione = False

label cheats:
    menu:
        "-Hermione Cheats-" (icon="interface/icons/small/hermione.png") if hermione_unlocked:
            label .hermione:
            menu:
                "-Reset Hermione's mood-" if her_mood != 0:
                    $ her_mood = 0
                    ">Hermione is no longer mad at you."
                    jump cheats.hermione
                "-Max Whoring-" if her_whoring < 24:
                    $ her_whoring = 24
                    ">Hermione is now a giant slut."
                    jump cheats.hermione

                "-Increase Whoring-" if her_whoring < 24:
                    $ her_whoring += 1
                    ">Hermione became more depraved..."
                    jump cheats.hermione
                "-Decrease Whoring-" if her_whoring > 0:
                    $ her_whoring += -1
                    "Hermione recovered some of her dignity"
                    jump cheats.hermione

                "-Back-":
                    jump cheats

        "-Astoria Cheats-" (icon="interface/icons/small/astoria.png") if astoria_unlocked:
            label .astoria:
            menu:
                "-Reset Astoria's mood-" if ast_mood != 0:
                    $ ast_mood = 0
                    ">Astoria is no longer mad at you."
                    jump cheats.astoria
                "-Max Affection-" if ast_affection < 24:
                    $ ast_affection = 24
                    ">Astoria has hots for you."
                    jump cheats.astoria

                "-Increase Affection-" if ast_affection < 24:
                    $ ast_affection += 1
                    ">Astoria likes you more..."
                    jump cheats.astoria
                "-Decrease Affection-" if ast_affection > 0:
                    $ ast_affection += -1
                    "Astoria likes you less..."
                    jump cheats.astoria
                "-Back-":
                    jump cheats

        "-Luna Cheats-" (icon="interface/icons/small/luna.png") if luna_unlocked:
            label cheats_luna:
            menu:
                "-Unlock all outfits & sets-":
                    python:
                        for item in luna_outfits_list:
                            unlock_clothing_compat(item)
                        for item in luna_costumes_list:
                            unlock_clothing_compat(item)
                        for item in luna_dresses_list:
                            unlock_clothing_compat(item)
                        for item in luna_clothing_sets_list:
                            unlock_clothing_compat(item)
                    ">All of Luna's outfits and clothing sets have been unlocked."
                    jump cheats_luna

                "-Sub Luna-":
                    $ lun_sub = 8
                    $ lun_whoring = 10
                    "Set to Sub Luna"
                    jump cheats_luna
                "-Dom Luna-":
                    $ lun_dom = 8
                    $ lun_whoring = 10
                    "Set to Dom Luna"
                    jump cheats_luna

                "-Reset ALL Luna content-":
                    call reset_luna_progress
                    ">Luna content reset!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Cho Cheats-" (icon="interface/icons/small/cho.png") if cho_unlocked:
            label .cho:
            menu:
                "-Reset Cho's mood-" if cho_mood != 0:
                    $ cho_mood = 0
                    ">Cho is no longer mad at you."
                    jump cheats.cho
                "-Max Whoring-" if cho_whoring < 24:
                    $ cho_whoring = 24
                    ">Cho is now a giant slut."
                    jump cheats.cho

                "-Increase Whoring-" if cho_whoring < 24:
                    $ cho_whoring += 1
                    ">Cho became more depraved..."
                    jump cheats.cho
                "-Decrease Whoring-" if cho_whoring > 0:
                    $ cho_whoring += -1
                    "Cho recovered some of her dignity"
                    jump cheats.cho
                "-Back-":
                    jump cheats

        "-Book Cheats-" (icon="interface/icons/small/book.png") if store_intro_done:
            label .books:
            menu:
                "-Max Imagination":
                    $ imagination = 8
                    $ bdsm_imagination = 2
                    "Your imagination grows!"
                    jump cheats.books
                "-Cheat Reading ([cheat_reading])-":
                    $ cheat_reading = not cheat_reading
                    jump cheats.books
                "-All Books-" if day >= 16:
                    python:
                        for book in book_list.get_all():
                            book.unlockable = False
                            book.unlocked = True
                    "Obtained All Books."
                    jump cheats.books
                "-Back-":
                    jump cheats

        "-Potion Cheats-" (icon="interface/icons/small/potion.png"):
            label cheats_potions:
            menu:
                "-Add all normal potions-":
                    $ potion_inv.extend(["p_cum_addiction","p_ass_expansion","p_breast_expansion","p_cat_transformation","p_luna_transformation","p_transparency","p_hypno"])
                    ">All potions added (Does not include Snape's potions)"
                    jump cheats_potions
                "-Back-":
                    jump cheats

        "-Solve the slider puzzle-" if puzzle_box_quest_ITEM.unlocked == True and unlocked_7th == False:
            $ unlocked_7th = True
            jump open_puzzle_box

        "-Add Gold-" (icon="interface/icons/small/gold.png"):
            $ gold += 500
            "You've obtained 500g."
            jump cheats

        "-Add Slytherin Points-" (icon="interface/icons/small/slyt.png"):
            $ slytherin += 200
            call house_points
            "Two hundred points to Slytherin!"
            jump cheats

        "-Wardrobe transparency-" (icon="interface/icons/small/wardrobe.png"):
            $ cheat_wardrobe_alpha = not cheat_wardrobe_alpha
            if cheat_wardrobe_alpha:
                "Wardrobe transparency slider is enabled."
            else:
                "Wardrobe transparency slider is disabled."
            jump cheats

        "-{color=#7a0000}DEVROOM{/color}-" if config.developer:
            label .devroom:
            menu:
                "-Unlock all characters-" (icon="interface/icons/small/condom.png"):
                    $ snape_unlocked = True
                    $ tonks_unlocked = True
                    $ hermione_unlocked = True
                    $ cho_unlocked = True
                    $ astoria_unlocked = True
                    $ susan_unlocked = True
                    $ luna_unlocked = True
                    # ginny_unlocked = True
                    # voldermort_unlocked = True
                    # hagrid_unlocked = True
                    jump cheats.devroom
                "-Unlock all characters wardrobe-" (icon="interface/icons/small/wardrobe.png"):
                    $ tonks_wardrobe_unlocked = True
                    $ hermione_wardrobe_unlocked = True
                    $ cho_wardrobe_unlocked = True
                    $ astoria_wardrobe_unlocked = True
                    $ susan_wardrobe_unlocked = True
                    $ luna_wardrobe_unlocked = True
                    # ginny_wardrobe_unlocked = True
                    # voldemort_wardrobe_unlocked = True
                    # hagrid_wardrobe_unlocked = True
                    jump cheats.devroom
                "-Unlock all characters clothes-" (icon="interface/icons/small/wardrobe.png"):
                    python:
                        for i in ("hermione", "cho", "astoria", "tonks"):
                            for x in getattr(renpy.store, i).wardrobe_list:
                                x.unlocked = True
                        # Her
                        for i in hermione_outfits_list:
                            i.unlocked = True
                        # Lun
                        for i in (luna_costumes_list + luna_dresses_list + luna_clothing_sets_list):
                            i.unlocked = True
                        # Cho
                        for i in (cho_outfits_list + cho_costumes_list + cho_dresses_list + cho_clothing_sets_list):
                            i.unlocked = True
                        # Ast
                        ag_anntakamaki_ITEM.unlocked = True
                    jump cheats.devroom

                "-Skip character progression-":
                    jump cheats.progression_skip

                "-Get 100 of all gift items-" (icon="interface/icons/small/gift.png"):
                    python:
                        for i in candy_gift_list:
                            i.number = 100
                        for i in drink_gift_list:
                            i.number = 100
                        for i in mag_gift_list:
                            i.number = 100
                        for i in toy_gift_list:
                            i.number = 100
                    jump cheats.devroom
                "-Get all scrolls-" (icon="interface/icons/small/spell.png"):
                    python:
                        for i in scroll_list_A:
                            i.unlocked = True
                        for i in scroll_list_B:
                            i.unlocked = True
                        for i in scroll_list_C:
                            i.unlocked = True
                    jump cheats.devroom
                "-Get all books-" (icon="interface/icons/small/book.png"):
                    python:
                        for i in book_list.read_books:
                            i.unlocked = True
                            i.unlockable = False
                        for i in book_list.write_books:
                            i.unlocked = True
                            i.unlockable = False
                        for i in book_list.fiction_books:
                            i.unlocked = True
                            i.unlockable = False
                    jump cheats.devroom
                "-Get all decorations-" (icon="interface/icons/small/gold.png"):
                    python:
                        for i in wall_deco_list:
                            i.unlocked = True
                        for i in fireplace_deco_list:
                            i.unlocked = True
                        for i in cupboard_deco_list:
                            i.unlocked = True
                        for i in misc_deco_list:
                            i.unlocked = True
                        for i in misc_hat_list:
                            i.unlocked = True
                    jump cheats.devroom
                "-Get all quest items-":
                    python:
                        sealed_scroll_quest_ITEM.unlocked = True
                        puzzle_box_quest_ITEM.unlocked = True
                        collar_quest_ITEM.unlocked = True
                        lootbox_quest_ITEM.number = 5 # Consumable
                    call update_quest_items
                    jump cheats.devroom
                "-Read Hermione's Diary-" (icon="interface/icons/small/hermione.png"):
                    call book_handle(book=hermione_diary)
                    jump cheats.devroom
                "Gallery test":
                    jump open_gallery
                "Lootbox":
                    call card_lootbox
                    jump cheats.devroom
                "Dueling - Prototype sign drawing":
                    jump magic_tutorial
                "-Back-":
                    jump cheats

        "-Never mind-":
            jump main_room_menu


label .progression_skip:
    menu:
        "-Hermione-":
            label .hermione_skip:
            menu:
                "-Skip Intro-" if not hermione_favors:
                    call cheats.hermione_skip_intro
                "-Skip Tier 1-" if hermione_favors and her_tier == 1:
                    call cheats.hermione_skip_T1
                "-Skip Tier 2-" if her_tier == 2:
                    call cheats.hermione_skip_T2
                "-Skip Tier 3-" if her_tier == 3:
                    call cheats.hermione_skip_T3
                "-Skip Tier 4-" if her_tier == 4:
                    call cheats.hermione_skip_T4
                "-Skip Tier 5-" if her_tier == 5:
                    call cheats.hermione_skip_T5
                "-Back-":
                    jump cheats.progression_skip

            call update_her_favors
            call update_her_requests
            jump cheats.hermione_skip

        "-Cho-" if her_tier >= 2:
            label .cho_skip:
            menu:
                "-Skip Intro-" if not cho_intro.E3_complete:
                    call cheats.cho_skip_intro
                "-Skip Quiz-" if cho_intro.E3_complete and not cho_quiz.complete:
                    call cheats.cho_skip_quiz
                "-Back-":
                    jump cheats.progression_skip

            jump cheats.cho_skip

        "-Back-":
            jump cheats.devroom


### Hermione ###

label .hermione_skip_intro:

    $ bird_examined = True
    $ desk_examined = True
    $ cupboard_examined = True
    $ door_examined = True
    $ fireplace_examined = True

    $ wine_ITEM.number       += 5
    $ firewhisky_ITEM.number += 5
    $ firewhisky_ITEM.unlockable = False

    $ rum_times = 6
    $ day = 7

    $ achievement.unlock("start", True)

    $ genie_intro.E1_complete = True
    $ genie_intro.E2_complete = True
    $ genie_intro.E3_complete = True

    $ snape_intro.E1_complete   = True
    $ snape_intro.E2_complete   = True
    $ snape_intro.E3_complete   = True
    $ snape_intro.duel_complete = True
    $ snape_intro.E4_complete   = True
    $ snape_intro.E5_complete   = True

    $ ss_he.hermione_E1 = True
    $ ss_he.hermione_E2 = True
    $ ss_he.tonks_E1 = True
    $ ss_he.tonks_E2 = True
    $ ss_he.tonks_E3 = True

    $ tonks_intro.E1_complete = True
    $ tonks_intro.E2_complete = True
    $ tonks_intro.E3_complete = True

    $ nt_he.hermione_E1 = True

    $ hermione_intro.E1_complete = True
    $ hermione_intro.E2_complete = True
    $ hermione_intro.E3_complete = True
    $ hermione_intro.E4_complete = True
    $ hermione_intro.E5_complete = True
    $ hermione_intro.E6_complete = True

    $ letter_hg_1.read_letter()
    $ letter_hg_2.read_letter()
    $ letter_min_work.read_letter()
    $ letter_min_report.read_letter()
    $ letter_min_favors.read_letter()

    $ snape_unlocked = True
    $ achievement.unlock("unlocksna", True)

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton", True)

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher", True)
    $ tutoring_hermione_unlocked = True
    $ hermione_favors = True

    python:
        for i in xrange(0, 6):
            hermione_diary.append("prologue_0"+str(i), "prologue_0"+str(i))

    return

label .hermione_skip_T1:
    $ her_tier = 2
    $ her_whoring = 1
    return

label .hermione_skip_T2:
    $ her_tier = 3
    $ her_whoring = 9
    $ hg_jerkoff.trigger = True
    $ imagination = 2
    return

label .hermione_skip_T3:
    $ her_tier = 4
    $ her_whoring = 12
    $ hg_strip.trigger = True
    $ imagination = 3
    return

label .hermione_skip_T4:
    $ her_tier = 5
    $ her_whoring = 18
    $ hg_kiss.trigger = True
    $ imagination = 4
    return

label .hermione_skip_T5:
    $ her_tier = 6
    $ her_whoring = 21
    $ hg_blowjob.trigger = True
    $ imagination = 5
    return


### Cho ###

label .cho_skip_intro:
    if day < 16:
        $ day = 16
    $ cho_intro.E1_complete = True
    $ cho_intro.E2_complete = True
    $ ss_he.cho_E1 = True
    $ cho_intro.E3_complete = True
    $ achievement.unlock("unlockcho", True)
    $ cho_unlocked = True
    return

label .cho_skip_quiz:
    $ cho_quiz.complete = True
    $ cho_quid.E1_complete = True
    $ cho_quid.E2_complete = True
    $ cho_quid.position = "above"
    $ cho_training_unlocked = True
    $ cho_favors_unlocked = True
    return
