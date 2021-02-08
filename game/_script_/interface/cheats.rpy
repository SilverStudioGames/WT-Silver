
default cheat_reading = False
default cheat_wardrobe_alpha = False

default skip_duel = False

label cheats:

    if not config.developer and not renpy.is_seen(False):
        "Uncle Good Advice" "{b}Attention!{/b}\nSome cheats can cause bugs and writing inconsistencies, use at your own risk."

    menu:
        "-Tonks Cheats-" (icon="interface/icons/small/tonks.webp") if tonks_unlocked:
            label .tonks:
            menu:
                "-Reset Tonks' mood-" if lun_mood != 0:
                    $ lun_mood = 0
                    ">Tonks is no longer mad at you."
                "-Max Friendship-" if ton_friendship < 100:
                    $ ton_friendship = 100
                    ">Tonks has hots for you."
                "-Increase Friendship-" if ton_friendship < 100:
                    $ ton_friendship += 1
                    ">Tonks likes you more..."
                "-Decrease Friendship-" if ton_friendship > 0:
                    $ ton_friendship += -1
                    "Tonks likes you less..."
                "-Back-":
                    jump cheats
            jump cheats.tonks

        "-Hermione Cheats-" (icon="interface/icons/small/hermione.webp") if hermione_unlocked:
            label .hermione:
            menu:
                "-Reset Hermione's mood-" if her_mood != 0:
                    $ her_mood = 0
                    ">Hermione is no longer mad at you."
                "-Max Whoring-" if her_whoring < 24:
                    $ her_whoring = 24
                    ">Hermione is now a giant slut."
                "-Increase Whoring-" if her_whoring < 24:
                    $ her_whoring += 1
                    ">Hermione became more depraved..."
                "-Decrease Whoring-" if her_whoring > 0:
                    $ her_whoring += -1
                    "Hermione recovered some of her dignity"
                "-Back-":
                    jump cheats
            jump cheats.hermione

        "-Cho Cheats-" (icon="interface/icons/small/cho.webp") if her_tier >= 2 or cho_unlocked:
            label .cho:
            menu:
                "-Reset Cho's mood-" if cho_mood != 0:
                    $ cho_mood = 0
                    ">Cho is no longer mad at you."
                "-Max Whoring-" if cho_whoring < 24:
                    $ cho_whoring = 24
                    ">Cho is now a giant slut."
                "-Increase Whoring-" if cho_whoring < 24:
                    $ cho_whoring += 1
                    ">Cho became more depraved..."
                "-Decrease Whoring-" if cho_whoring > 0:
                    $ cho_whoring += -1
                    "Cho recovered some of her dignity"
                "-Back-":
                    jump cheats
            jump cheats.cho

        "-Luna Cheats-" (icon="interface/icons/small/luna.webp") if luna_unlocked:
            label .luna:
            menu:
                "-Reset Astoria's mood-" if lun_mood != 0:
                    $ lun_mood = 0
                    ">Astoria is no longer mad at you."
                "-Max Whoring-" if lun_whoring < 24:
                    $ lun_whoring = 24
                    ">Astoria has hots for you."
                "-Increase Whoring-" if lun_whoring < 24:
                    $ lun_whoring += 1
                    ">Astoria likes you more..."
                "-Decrease Whoring-" if lun_whoring > 0:
                    $ lun_whoring += -1
                    "Astoria likes you less..."
                "-Back-":
                    jump cheats
            jump cheats.luna

        "-Astoria Cheats-" (icon="interface/icons/small/astoria.webp") if astoria_unlocked:
            label .astoria:
            menu:
                "-Reset Astoria's mood-" if ast_mood != 0:
                    $ ast_mood = 0
                    ">Astoria is no longer mad at you."
                "-Max Whoring-" if ast_whoring < 24:
                    $ ast_whoring = 24
                    ">Astoria has hots for you."
                "-Increase Whoring-" if ast_whoring < 24:
                    $ ast_whoring += 1
                    ">Astoria likes you more..."
                "-Decrease Whoring-" if ast_whoring > 0:
                    $ ast_whoring += -1
                    "Astoria likes you less..."
                "-Back-":
                    jump cheats
            jump cheats.astoria

        "-Add Gold-" (icon="interface/icons/small/gold.webp"):
            $ game.gold += 500
            jump cheats

        "-Add Slytherin Points-" (icon="interface/icons/small/slyt.webp"):
            $ slytherin += 200
            call update_ui_points
            "Two hundred points to Slytherin!"
            jump cheats

        "-Wardrobe transparency-" (icon="interface/icons/small/wardrobe.webp"):
            $ cheat_wardrobe_alpha = not cheat_wardrobe_alpha
            if cheat_wardrobe_alpha:
                "Wardrobe transparency slider is enabled."
            else:
                "Wardrobe transparency slider is disabled."
            jump cheats

        "-{color=#7a0000}DEVROOM{/color}-" if config.developer:
            label .devroom:
            menu:
                "-Max all character stats-":
                    $ sus_whoring = ast_whoring = cho_whoring = her_whoring = lun_whoring = 24
                    $ ton_friendship = 100
                    jump cheats.devroom

                "-Unequip all clothes-":
                    python:
                        for i in {"hermione", "cho", "astoria", "tonks", "susan", "luna"}:
                            getattr(renpy.store, i).unequip("all")
                    jump cheats.devroom

                "-Unlock all characters-" (icon="interface/icons/small/condom.webp"):
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
                "-Unlock all characters wardrobe-" (icon="interface/icons/small/wardrobe.webp"):
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
                "-Unlock all outfits-" (icon="interface/icons/small/wardrobe.webp"):
                    python:
                        for i in {"hermione", "cho", "astoria", "tonks", "susan", "luna"}:
                            for x in getattr(renpy.store, i).outfits:
                                x.unlock()

                    jump cheats.devroom

                "-Skip character progression-":
                    jump cheats.progression_skip

                "-Get all gifts-" (icon="interface/icons/small/gift.webp"):
                    python:
                        for i in inventory.get_instances_of_type("gift"):
                            i.owned = 100
                    jump cheats.devroom
                "-Get all scrolls-" (icon="interface/icons/small/spell.webp"):
                    python:
                        for i in inventory.get_instances_of_type("scroll"):
                            i.owned = 1
                    jump cheats.devroom
                "-Get all books-" (icon="interface/icons/small/book.webp"):
                    python:
                        for i in inventory.get_instances_of_type("book"):
                            i.owned = 1
                    jump cheats.devroom
                "-Get all decorations-" (icon="interface/icons/small/gold.webp"):
                    python:
                        for i in inventory.get_instances_of_type("decoration"):
                            i.owned = 1
                    jump cheats.devroom
                "-Get all quest items-":
                    python:
                        for i in inventory.get_instances_of_type("qitem"):
                            i.owned = 1
                    jump cheats.devroom
                # "-Read Hermione's Diary-" (icon="interface/icons/small/hermione.webp"):
                #     call book_handle(book=hermione_diary)
                #     jump cheats.devroom
                # "Lootbox":
                #     call card_lootbox
                #     jump cheats.devroom
                # "Dueling - Prototype sign drawing":
                #     jump magic_tutorial
                # "Cho CG demo":
                #     call cho_main(xpos="base",ypos="base")
                #     call play_music("cho")
                #     call play_sound("door")
                #     call cho_chibi("stand", "mid", "base")
                #     with d3
                #     jump cc_pf_blowjob
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
            jump cheats.progression_skip

        "-Cho-" if her_tier >= 2:
            label .cho_skip:
            menu:
                "-Skip Intro-" if not cho_intro.E3_complete:
                    call cheats.cho_skip_intro
                "-Skip Quiz-" if cho_intro.E3_complete and not cho_quiz.complete:
                    call cheats.cho_skip_quiz
                "-Back-":
                    jump cheats.progression_skip

            jump cheats.progression_skip

        "-Back-":
            jump cheats.devroom


### Hermione ###

label .hermione_skip_intro:

    $ bird_examined = True
    $ desk_examined = True
    $ cupboard_examined = True
    $ door_examined = True
    $ fireplace_examined = True

    $ wine_ITEM.owned = 5
    $ firewhisky_ITEM.owned = 5
    $ firewhisky_ITEM.unlocked = True

    $ rum_times = 6
    $ game.day = 7

    $ achievement.unlock("start", True)

    $ genie_intro.E1_complete = True
    $ genie_intro.E2_complete = True
    $ genie_intro.E3_complete = True
    $ genie_intro.E4_complete = True

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

    $ letter_hg_1.open(silent=True)
    $ letter_hg_2.open(silent=True)
    $ letter_work_unlock.open(silent=True)
    $ letter_favors.open(silent=True)

    $ snape_unlocked = True
    $ achievement.unlock("unlocksna", True)

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton", True)

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher", True)
    $ tutoring_hermione_unlocked = True
    $ hermione_favors = True

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
    if game.day < 16:
        $ game.day = 16
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
    $ cho_quid.lock_training = False
    $ cho_favors_unlocked = True
    return
