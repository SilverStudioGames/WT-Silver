define lun_requirements = {
    "category upper undergarment": 5, #TODO happens after first event of T2 (inspect body)  (would need to be set to first lvl of T3)
    "category lower undergarment": 5, #TODO happens after first event of T2 (inspect body)  (would need to be set to first lvl of T3)
    "category piercings & tattoos": 16, #TODO First level of Tier 4
    # "touch head":
    # "touch breasts":
    # "touch vagina":
    "unequip panties": 6, #TODO she strips first event of T2 (inspect body)                 (would need to be set to first lvl of T3)
    "unequip bra": 6, #TODO she strips first event of T2 (inspect body)                     (would need to be set to first lvl of T3)
    "unequip top": 3, #TODO happens end of T1                                               (would need to be set to first lvl of T2)
    "unequip bottom": 3, #TODO happens end of T1                                            (would need to be set to first lvl of T2)
    }

define lun_responses = {
    "category_fail": "lun_reaction_category_fail",
    "equip": "lun_reaction_equip",
    "equip_fail": "lun_reaction_equip_fail",
    "unequip": "lun_reaction_unequip",
    "unequip_fail": "lun_reaction_unequip_fail",
    "touch": "lun_reaction_touch",
    "touch_fail": "lun_reaction_touch_fail",
    "equip_outfit": "lun_reaction_equip_outfit",
    "equip_outfit_fail": "lun_reaction_equip_outfit_fail",
    "blacklist": "lun_reaction_blacklist",
}

label lun_reaction_category_fail(category):

    if category == "upper undergarment":
        call lun_main("Is this part of our Wrackspurt research [lun_genie_name]?", "base", "base", "base", "mid")
        m "*Err*... I just thought maybe you could... Never mind..."
    elif category == "lower undergarment":
        call lun_main("Is this part of our Wrackspurt research [lun_genie_name]?", "base", "base", "base", "mid")
        m "*Err*... I just thought maybe you could... Never mind..."
    elif category == "piercings & tattoos":
        $ random_number = renpy.random.randint(1, 3)
        if random_number == 1:
            call lun_main("I'm not sure if that's such a good idea [lun_genie_name]...", "base", "base", "base", "mid")
            m "Why's that?"
            call lun_main("It might attract Nifflers into the castle...", "base", "base", "base", "mid")
            m "..."
        elif random_number == 2:
            call lun_main("Daddy says that ink should only be used on paper and not on your body...", "base", "base", "base", "mid")
        elif random_number == 3:
            call lun_main("Isn't it supposed to hurt?", "base", "base", "base", "mid")
            m "I'm sure there's some magical mumbo jumbo that would make it painless..."
            call lun_main("*Hmm*... I'm not sure...", "base", "base", "base", "mid")
    return

label lun_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
        $ random_number = renpy.random.randint(1, 3)

        if lun_tier == 5:
            if random_number == 1:
                call lun_main("*Mmm*...", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Ah*...", "base", "base", "base", "mid")
                call lun_main("Sorry, you just took me by surprise...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("*Hmm*... I could've sworn you said that we should focus on more sensitive areas...", "base", "base", "base", "mid")
        elif lun_tier == 4:
            if random_number == 1:
                call lun_main("*Mmm*... That's strange...", "base", "base", "base", "mid")
                call lun_main("How come I'm feeling good in other places when it's my head you're touching?", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("Pat, pat, pat.", "base", "base", "base", "mid")
                m "..."
            elif random_number == 3:
                call lun_main("Thank you, [lun_genie_name]...", "base", "base", "base", "mid")
                call lun_main("I feel like I get a big boost of happiness when you pat me for some reason...", "base", "base", "base", "mid")
                call lun_main("Maybe that's why animals enjoy it so much too...", "base", "base", "base", "mid")
        elif lun_tier == 3:
            if random_number == 1:
                call lun_main("Is my head another one of those sensitive areas you spoke about?", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("I don't think there's anywhere for me to release the Wrackspurts from up there, but thank you anyway...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("Are you sure this technique is working [lun_genie_name]?", "base", "base", "base", "mid")
        elif lun_tier == 2:
            if random_number == 1:
                call lun_main("Thank you [lun_genie_name].", "base", "base", "base", "mid")
                call lun_main("I'm so glad you decided to let me help with your research.", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("Are you feeling stressed [lun_genie_name]?", "base", "base", "base", "mid")
                m "*Huh*?"
                call lun_main("Feel free to pet me any time you like if it helps.", "base", "base", "base", "mid")
                m "*Err*... Thanks..."
            elif random_number == 3:
                call lun_main("*Hmm*... I'm not getting any of that tingly sensation up there but it does feel kind of nice...", "base", "base", "base", "mid")
        else: #Tier 1
            if random_number == 1:
                call lun_main("Thank you [lun_genie_name].", "base", "base", "base", "mid")
                call lun_main("Other students look at me weird if I try to pet them so I'm glad I didn't do something weird again...", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("I already checked for Nargles this morning but I suppose you can't be too careful...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("I think I lost a pencil up there, let me know if you find it.", "base", "base", "base", "mid")

    elif what == "breasts":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if lun_tier == 5:
            if random_number == 1:
                call lun_main("Don't forget to kiss the other one too! She gets awfully jealous if her sister gets all the attention.", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Mmm*... Why does something so bad feel so good?", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("*Ah*... Thank you for helping me [lun_genie_name]...", "base", "base", "base", "mid")
        elif lun_tier == 4:
            if random_number == 1:
                call lun_main("*Mmm*... How come I don't really see any of the Wrackspurts coming out from here?", "base", "base", "base", "mid")
                m "*Err*..."
                call lun_main("It feels really good so why aren't any of them coming out?", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Ah*... {w=0.4} Your methods are quite the something [lun_genie_name]...", "base", "base", "base", "mid")
                call lun_main("I could never have imagined that getting rid of those pest would end up being so...", "base", "base", "base", "mid")
                call lun_main("Enjoyable...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("Come... Come out already...", "base", "base", "base", "mid")
        elif lun_tier == 3:
            if random_number == 1:
                call lun_main("*Whoa*... You really were right about these things being sensitive...", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Ah*... Are everyone this sensitive in around this spot?", "base", "base", "base", "mid")
                m "Women are a lot more sensitive than men most of the time..."
                call lun_main("*Oh*... That's so sad...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("...", "base", "base", "base", "mid")
                m "How did that feel?"
                call lun_main("*Ehm*... It felt very nice [lun_genie_name]...", "base", "base", "base", "mid")
        #elif lun_tier == 2: This would only be useful if there was another check if you've done event 2 to have it show before T3
        else: # T1 and T2
            if random_number == 1:
                call lun_main("*Hi-Hi*...", "base", "base", "base", "mid")
                call lun_main("Sorry [lun_genie_name], your beard is tickling me...", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("Are you looking for the Himalayan Lesser Spotted Breast Imp? It's okay sir, it's not their migration season.", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("...", "base", "base", "base", "mid")

    elif what == "vagina":
        $ mouse_heart()
        $ random_number = renpy.random.randint(1, 3)

        if lun_tier == 5:
            if random_number == 1:
                call lun_main("*Ah*... S-so good... How did I ever live without this?", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Mmm*... Nasty... Wrackspurts...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("Please... Help me get rid of them again...", "base", "base", "base", "mid")
        elif lun_tier == 4:
            if random_number == 1:
                call lun_main("*Whoa*... I didn't think just using your mouth could produce such a strong response.", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("*Ah*... It's almost like a ripple of water... Except running through my body...", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("*Mmm*... Those nasty Wrackspurts... I can feel them getting agitated already...", "base", "base", "base", "mid")
        elif lun_tier == 3:
            if random_number == 1:
                call lun_main("*Ohhhh*... This is going to be my new happy memory when I have to summon a patronus!", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("Weren't I supposed to be learning how to do this myself?", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("*Oohhh*... Why are your lips cold?", "base", "base", "base", "mid")
                m "Why are your lips cold?"
                call lun_main("*Huh*?", "base", "base", "base", "mid")
        # elif lun_tier == 2:This would only be useful if there was another check if you've done event 2 to have it show before T3
        else: # T1 and T2
            if random_number == 1:
                call lun_main("*Hi-Hi*...", "base", "base", "base", "mid")
                call lun_main("That's not my cheek, silly...", "base", "base", "base", "mid")
            elif random_number == 2:
                call lun_main("Is this a lesson on the dementor's kiss?", "base", "base", "base", "mid")
                call lun_main("I always thought it was done through the mouth.", "base", "base", "base", "mid")
            elif random_number == 3:
                call lun_main("*Ooohh*...", "base", "base", "base", "mid")
                call lun_main("I don't think anyone has ever kissed me there before... How strange...", "base", "base", "base", "mid")
    return

label lun_reaction_touch_fail(what): #Not used
    if what == "head":
        $ mouse_slap()

        g4 "Ouch! Why would you do that?!"
        lun "Oh! I'm terribly sorry, [lun_genie_name], I used to play this game with my father and..."
        m "I don't need to hear it..."
        lun "...as you wish sir."

    elif what == "breasts":
        $ mouse_slap()

        lun "*giggles* [lun_genie_name] stop that! It tickles."

    elif what == "vagina":
        $ mouse_slap()

        lun "*Ah* Sir, please don't tease me, wrackspurts have been terribly active today and I'm barely able to withhold as it is."

    return

label lun_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label lun_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    call lun_main("*Hmm*...", "base", "base", "base", "mid")
    m "What?"
    call lun_main("There's a weird aura surrounding this piece of garment.", "base", "base", "base", "mid")
    call lun_main("It seems to be affecting the Wrackspurts, as if they're multiplying!", "base", "base", "base", "mid")
    call lun_main("I'm sorry sir but I can't wear, not until I know how to fight them at least.", "base", "base", "base", "mid")
    m "(I guess that means she's not yet ready.)"

    return

label lun_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if lun_whoring > 15:
    #        lun "You want to see my snatch?"
    #        lun "You got it [genie_name]!"
    #
    return

label lun_reaction_unequip_fail(item):
    if item.type == "panties": #probably wont play since category unlocks same level as she can take them off
        call lun_main("I'm sorry [lun_genie_name] but my panties are my one and only defence against wrackspurts.", "base", "base", "base", "mid")

    elif item.type == "bra": #probably wont play since category unlocks same level as she can take them off
        call lun_main("*giggles*", "base", "base", "base", "mid")
        m "What's so funny?"
        call lun_main("*Oh*... It's nothing...", "base", "base", "base", "mid")

    elif item.type == "top":
        call lun_main("Are we going to continue the research, [lun_genie_name]?", "base", "base", "base", "mid")
        m "Not right now..."
        call lun_main("*Oh*... Then let me know when you're ready...", "base", "base", "base", "mid")

    elif item.type == "bottom":
        call lun_main("Are we going to continue the research, [lun_genie_name]?", "base", "base", "base", "mid")
        m "Not right now..."
        call lun_main("*Oh*... Then let me know when you're ready...", "base", "base", "base", "mid")

    return

label lun_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     lun "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label lun_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     lun "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    call lun_main("This outfit seems to have wrackspurts all over it!", "base", "base", "base", "mid")
    m "(I don't remember cumming on this piece of garment...)"
    g4 "(!!!)"
    g4 "(Could it be--...)"
    call lun_main("Are you okay sir? You look pale.", "base", "base", "base", "mid")
    m "Yes, I'm fine. I guess you can stay in your clothes... for now."

    return

label lun_reaction_blacklist(item):
    lun "Will that really help? With the wrackspurts I mean."

    if "top" in item.blacklist and luna.is_worn("top"):
        lun "I would need to lose my top."

    if "bottom" in item.blacklist and luna.is_worn("bottom"):
        lun "The bottoms I'm wearing wound need to go."

    if "bra" in item.blacklist and luna.is_worn("bra"):
        lun "It seems no bra can fit in this garment."

    if "panties" in item.blacklist and luna.is_worn("panties"):
        lun "Wrackspurts would have a feast as I would not be able to wear panties with this."

    m "Trust me, I know what I'm doing."
    lun "If you say so sir."

    return
