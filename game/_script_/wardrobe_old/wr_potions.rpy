
## Potions ##
label use_potion:
    if active_girl == "luna":
        jump use_luna_potion



### Hermione ###

label use_hermione_potion:
    hide screen wardrobe_old
    call her_main(xpos="base",ypos="base",trans=fade)

    if potion_choice == "polyjuice_potion":
        menu:
            ">Polyjuice potion. You know what it does..."
            "-Cat Transformation-" if daytime and potion_inv.has("p_cat_transformation"):
                $ potion_inv.remove("p_cat_transformation")
                $ renpy.jump( potion_lib.get_start_label("p_cat_transformation") )
            "{color=[menu_disabled]}-Cat Transformation-{/color}" if not daytime and potion_inv.has("p_cat_transformation"): # Missing?
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Luna Transformation-" if daytime and potion_inv.has("p_luna_transformation"):
                $ potion_inv.remove("p_luna_transformation")
                $ renpy.jump( potion_lib.get_start_label("p_luna_transformation") )
            "{color=[menu_disabled]}-Luna Transformation-{/color}" if not daytime and potion_inv.has("p_luna_transformation"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            # TODO: uncomment when scene is complete
            # "-Clone potion-" if potion_inv.has("p_clone"):
            #     $ potion_inv.remove("p_clone")
            #     $ renpy.jump( potion_lib.get_start_label("p_clone") )
            "-Never mind-":
                jump return_to_wardrobe

    if potion_choice == "expanding_elixir":
        menu:
            ">Potions that enhance the user's body."
            "-Breast Expansion-" if daytime and potion_inv.has("p_breast_expansion"):
                $ potion_inv.remove("p_breast_expansion")
                $ renpy.jump( potion_lib.get_start_label("p_breast_expansion") )
            "{color=[menu_disabled]}-Breast Expansion-{/color}" if not daytime and potion_inv.has("p_breast_expansion"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Ass Expansion" if daytime and potion_inv.has("p_ass_expansion"):
                $ potion_inv.remove("p_ass_expansion")
                $ renpy.jump( potion_lib.get_start_label("p_ass_expansion") )
            "{color=[menu_disabled]}-Ass Expansion-{/color}" if not daytime and potion_inv.has("p_ass_expansion"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Never mind-":
                jump return_to_wardrobe

    if potion_choice == "milk_potion":
        menu:
            ">Potions for when you run out of milk in the fridge."
            "-Lactantium-" if daytime and potion_inv.has("p_milk_potion"):
                $ potion_inv.remove("p_milk_potion")
                $ renpy.jump( potion_lib.get_start_label("p_milk_potion") )
            "{color=[menu_disabled]}-Lactantium-{/color}" if not daytime and potion_inv.has("p_milk_potion"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Never mind-":
                jump return_to_wardrobe

    if potion_choice == "love_potion":
        menu:
            ">Potions that change the user's mood or emotions."

            "-Cum Addiction-" if daytime and potion_inv.has("p_cum_addiction"):
                $ potion_inv.remove("p_cum_addiction")
                $ renpy.jump( potion_lib.get_start_label("p_cum_addiction") )
            "{color=[menu_disabled]}-Cum Addiction-{/color}" if not daytime and potion_inv.has("p_cum_addiction"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Hypno potion-" if daytime and potion_inv.has("p_hypno"):
                menu: #TODO Remove warning once Hermione's appearance change is made temporary
                    "This potion will change Hermione's appearance. Do you want to continue?"
                    "-Yes-":
                        $ potion_inv.remove("p_hypno")
                        $ renpy.jump( potion_lib.get_start_label("p_hypno") )
                    "-No-":
                        jump return_to_wardrobe
            "{color=[menu_disabled]}-Hypno potion-{/color}" if not daytime and potion_inv.has("p_hypno"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            # TODO: uncomment if ready unsure if ready for current release
            # "-Voluptatem-" if potion_inv.has("p_voluptatem"):
            #     $ potion_inv.remove("p_voluptatem")
            #     $ renpy.jump( potion_lib.get_start_label("p_voluptatem") )
            "-Never mind-":
                jump return_to_wardrobe

    if potion_choice == "clothes_potion":
        menu:
            ">Potions that affect the wearer's clothing."
            "-Transparent Clothes-" if daytime and potion_inv.has("p_transparency"):
                $ potion_inv.remove("p_transparency")
                $ renpy.jump( potion_lib.get_start_label("p_transparency") )
            "{color=[menu_disabled]}-Transparent Clothes-{/color}" if not daytime and potion_inv.has("p_transparency"):
                "This potion can only be used during the day."
                jump return_to_wardrobe

            "-Permanent Clothing Transparency-" if potion_inv.has("p_transparency"):
                $ misc_item_choice = "transparency"
                jump equip_misc_item

            "-Never mind-":
                jump return_to_wardrobe



### Luna ###

label use_luna_potion:
    hide screen wardrobe_old
    call lun_main(xpos="base",ypos="base",trans=fade)

    if potion_choice == "clothes_potion":
        menu:
            "-Permanent Clothing Transparency-" if potion_inv.has("p_transparency"):
                $ misc_item_choice = "transparency"
                jump equip_misc_item

            "-Never mind-":
                jump return_to_wardrobe



### Tonks ###

# label use_tonks_potion:
    # hide screen wardrobe_old
    # call ton_main(xpos="base",ypos="base",trans=fade)

    # if potion_choice == "hair_growth_potion":
        # menu:
            # ">Hair growth potion..."
            # "-Take a sip-":
                # $ potion_choice = "small"
                # jump equip_tonks_misc_item

            # "-Drink it-":
                # $ potion_choice = "arrow"
                # jump equip_tonks_misc_item

            # "-Undo effects-" if ton_request_wear_pubic_hair:
                # $ potion_choice = None
                # jump equip_tonks_misc_item

            # "-Never mind-":
                # jump return_to_wardrobe

    # if potion_choice == "clothes_potion":
        # menu:
            # "-Permanent Clothing Transparency-" if potion_inv.has("p_transparency"):
                # $ misc_item_choice = "transparency"
                # jump equip_misc_item

            # "-Never mind-":
                # jump return_to_wardrobe

# label equip_tonks_misc_item:

    # if potion_choice in ["arrow","small"]:
        # m "here, drink this."
        # call ton_main("A potion? Hmm...","horny","base","raised","down")
        # call ton_main("Want to tell me what's in it?","open","base","base","mid")
        # m "For hair growth, so I've been told."
        # call ton_main("A hair growth potion?","open","base","raised","mid")
        # call ton_main("[ton_genie_name], you know I don't need this, right?","open","base","worried","R")
        # call ton_main("I'm a Metamorphmagi... Didn't I tell you that?","open","base","angry","mid")
        # call ton_main("I don't need a potion to grow hair, or take different shapes...","horny","base","base","mid")
        # m "Will you drink it anyways?"
        # call ton_main("Hmm? Why waste a perfectly fine potion on me?","open","base","raised","down")
        # m "It's mostly just my cum..."
        # call ton_main("Oh, why didn't you say so sooner, [ton_genie_name].","base","base","base","mid")
        # call ton_main("Now I can't possibly resist drinking that sweet potion of yours!","horny","base","base","mid")
        # g9 "Well, go ahead, [tonks_name]!"
        # m "But I would still like to see some pubes on you!"
        # call ton_main("Of course. Do you have any preferences?","base","base","base","mid")
        # if potion_choice == "arrow":
            # m "Yes, make it shaped like an arrow."
            # g9 "Pointing down at your pussy!"
        # if potion_choice == "small":
            # g9 "Just a small bit of fur, above your pussy, please."
        # call ton_main("Well, here goes nothing...","horny","base","worried","down")
        # call nar(">You watch Tonks swallow the potion and cum mixture in one go...","start")
        # "Wait a second... where did you even get that from?"
        # m "Does it matter?"
        # call nar(">I guess not... not really... Please, continue.","end")
        # m "(...)"
        # call ton_main("Fuck me! That tasted good!","open_wide_tongue","base","base","ahegao",trans=hpunch)
        # call ton_main("I'm not used to potions this tasty! With so much delicious cum in it...","horny","base","base","mid")
        # m "Glad you liked it."
        # call ton_main("Now, here, is your reward...","base","base","angry","mid")
        # call ton_main("I hope you like it too!","horny","base","base","down")
        # pause.8

        # hide screen tonks_main
        # $ tonks_wear_top = False
        # $ tonks_wear_bottom = False
        # $ tonks_wear_robe = False
        # call update_tonks_body
        # show screen tonks_main
        # with d3
        # pause.8

        # call set_ton_pubic_hair(potion_choice)
        # show screen tonks_main
        # with d3
        # call ctc


    # else: #Unequip
        # $ potion_choice = None
        # m "could you remove your pubes again?"
        # call ton_main("Of course.","base","base","base","mid")
        # pause.8

        # hide screen tonks_main
        # $ tonks_wear_top = False
        # $ tonks_wear_bottom = False
        # $ tonks_wear_robe = False
        # call update_tonks_body
        # show screen tonks_main
        # with d3
        # pause.8

        # call set_ton_pubic_hair(potion_choice)
        # show screen tonks_main
        # with d3
        # call ctc

    # jump return_to_wardrobe
