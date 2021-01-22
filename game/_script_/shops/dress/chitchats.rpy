label purchase_outfit(item):

    if game.gold < item.price:
        m "(I don't have enough gold.)"
        return

    #
    # Hermione Granger
    #

    if item == her_outfit_maid:
        m "I'd like to order a maid outfit."
        maf "A maid outfit, what on earth for? Surely the house elves are keeping your office tidy."
        m "The what?"
        m "No, you got this all wrong... It's going to be a present."
        maf "For whom?"
        m "I'm afraid I can't say."
        maf "Well as long as it's not for a student..."
        maf "Did you have any style in mind?"
        m "Preferably a French maid."
        maf "..."
        maf "Well I should have it available for pick-up in a few days after I get the materials in."
        m "Thank you."
    elif item == her_outfit_nightie:
        m "I'd like to order a custom outfit today."
        maf "Certainly honey... Repairing these conservative school clothes all day has been quite dull to say the least."
        m "Well, I can assure you that this outfit is not conservative."
        maf "*Hmm*?"
        m "I'd like to order a girls Nightgown."
        maf "Well, that doesn't seem overly--"
        m "And make it out of silk!"
        maf "*Ahh*... So I assume that you also want it transparent?"
        m "If that is possible."
        maf "Of course it is possible, who do you take me for?"
        maf "I just have to order in the materials, although silks not cheap."
        m "Don't worry about the cost."
        maf "As you wish sweetie, it should be ready shortly."
        m "Thank you."
    elif item == her_outfit_ball:
        if not ball_quest.E4_complete:
            m "Could you make a dress for me?"
            maf "A dress? Do you mean something like a ball dress, or more burlesque?"
            m "*Hmm*... A ball dress does sound good, actually."
            maf "How surprising..."
            m "I was thinking that I could have a custom one made. For a very good girl of mine."
        else:
            m "Do you sell Ball dresses?"
            maf "*Hmm*... I suppose I do although they're nothing special... Why do you ask?"
            m "A 'girl' approached me with a problem. Apparently she's unable to acquire a dress for this years autumn ball."
            maf "How tragic.... Well I'm sure that one of these cheap ones will suffice."
            m "I was thinking I could have a custom one made... She is a very good girl."
        maf "Very well! I'll make her the best dress this school's ever seen. If you say she's been such a good girl..."
        maf "It should be ready in about a week."
        m "A week? Why so long?"
        maf "I'm ordering my next batch of material in a couple of days to keep the cost down..."
        maf "Or I could order it now if you pay a bit extra..."
    elif item == her_outfit_msmarv:
        m "Tell me Madam Mafkin, have you ever heard of superheroes?"
        maf "Yes yes, those people in the comic books. My grandson is quite fond of them."
        m "Fantastic, I was wondering if it would be possible for you to make me a costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Ms Marvel?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this tonight so I can take a look."
        m "Thank you very much."
        maf "No need to thank me honey. Payment will suffice."
    elif item == her_outfit_hslut:
        m "Have you ever seen a burlesque show Madam?"
        maf "I've done more than that, I've designed a few of the outfits for them!"
        m "Splendid, in that case I'd love to commission one."
        maf "Most Certainly, any particular colour in mind?"
        m "Red!"
        maf "As you wish."
        m "Thank you very much."
        maf "You're quite welcome, sir."
    # elif item == hg_costume_power_girl_ITEM:
        # m "I was wondering if it would be possible for you to make me a super hero costume."
        # maf "Certainly, who did you have in mind?"
        # m "Do you know Power Girl?"
        # maf "I'm afraid not..."
        # maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        # m "Thank you very much."
        # maf "No need to thank me sir. Payment will suffice."
    # elif item == hg_costume_harley_quinn_ITEM:
        # m "I was wondering if it would be possible for you to make me a super villain costume."
        # maf "Certainly, who did you have in mind?"
        # m "Do you know Harley Quinn?"
        # maf "I'm afraid not..."
        # maf "But I'm sure that my grandson has a comic of hers. I'll just have to wrestle it out of his grubby little hands."
        # m "Thank you very much."
        # maf "You're quite welcome."
    elif item == her_outfit_croft:
        m "Would you be able to make me a cosplay costume?"
        maf "Certainly, what are you after?"
        m "Do you happen to know Lara croft?"
        maf "I'm afraid not..."
        m "She's a video game character..."
        maf "Well, my little squib grandson loves video games. I'm sure he can show me what she looks like."
        m "Thank you very much."
        maf "You're welcome. I'm seeing him tonight so I should be able to complete this one slightly faster than usual."
        m "Fantastic."
    # elif item == hg_outfit_christmas_ITEM:
        # m "I was wondering if it would be possible for you to make me a festive costume."
        # maf "Certainly, what what holiday are you looking to \"celebrate\"?"
        # m "Christmas."
        # maf "At this time of year?"
        # m "It's never to early to start the festivities..."
        # maf "Evidently not. I'll have it done as soon as I can. "
        # m "Thank you very much."
        # maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you.."
        # m "Thank you."
    # elif item == hg_outfit_pirate_ITEM:
        # m "I want a pirate outfit"
        # maf "ok"
    elif item == her_outfit_bioshock:
        m "Have you ever heard of Bioshock infinite?"
        maf "Biology what now?"
        m "..."
        m "It's a video game..."
        maf "I assume you want the costume from it?"
        m "If it's not too much..."
        maf "Consider it done!"
        m "Thank you very much."
        maf "You're welcome."
    elif item == her_outfit_yennefer:
        m "Have you ever heard of the sorceress Yennefer?"
        maf "Of course! The mother of a universe hopper isn't quickly forgotten..."
        m "Think you could make me a version of her outfit?"
        maf "Certainly."
        m "Thank you very much."
        maf "Toss a coin to your tailor."
    elif item == her_outfit_bikini1:
        m "I'd like to order a bikini."
        maf "A bikini sir? Isn't that a bit cold in this climate?"
        m "A leather bikini!"
        maf "Are you even--"
        m "You think you could make something like that for me?"
        maf "Of course sir, as you wish..."
    elif item == her_outfit_bikini2:
        m "I'd like to order a bikini."
        maf "Of course, what kind of bikini would you like?"
        m "One that covers the important bits!"
        maf "And who is this bikini for if you don't mind me asking?"
        m "I do mind..."
        maf "Alright then..."
        maf "Your bikini shall be ready shortly."
        m "Excellent..."
    elif item == her_outfit_bunny:
        m "Could you make me a bunny costume?"
        maf "A bunny costume? Do you mean something like the Easter bunny?"
        m "No, like the ones you might see in Vegas!"
        maf "I'll see what I can--"
        m "With big bunny ears!"
        maf "Okay then..."
    elif item == her_outfit_swimsuit:
        m "I need a swimsuit."
        maf "Swimming at your age?"
        m "Hey, you're only as old as you feel..."
        m "And no, it's not for me... I need a woman's swimsuit."
        maf "I see, well it's about time you set up some swimming lessons..."
        maf "Are you looking for a design to fit the school colours?"
        m "No thank you, something sporty shall suffice."
        maf "..."
        maf "I'll have to look through some of those muggle magazines then..."
        maf "It will be ready shortly."
    elif item == her_outfit_egypt:
        m "I'd like something that one of my old flames used to wear..."
        maf "An old what, sir?"
        m "Cleopatra..."
        m "Ah... what a looker she was..."
        maf "Sweetie, are you okay? Do you want me to fetch the nurse?"
        m "Would you be able to make me something Egyptian themed?"
        m "Like the outfits Cleopatra used to wear..."
        maf "..."
        m "I'll trade you two camels for it."
        maf "Cleopatra you said?"
        m "Yes..."
        maf "That would require some metal work... Perhaps one of my contacts in Diagon alley..."
        m "So... up for the challenge?"
        maf "*Hmm*..."
        m "Or is this too much for {b}the{/b} Mafkin?"
        maf "It most certain isn't!"
        maf "I'll have it ready for you in no time!"
        maf "Although I'd prefer to be paid in gold rather than in camels."
        m "Ask and you shall receive!"
    elif item == her_outfit_latex_dress:
        m "Ready to work with some latex?"
        maf "Latex... now that's something I don't get to work with often..."
        maf "Anything particular in mind?"
        if pink_condoms_ITEM.owned > 0:
            m "Yes... something like this."
            maf "Is that a condo--"
            m "But you'd cut a heart shape here..."
            maf "..."
            m "And a hole for the head obviously."
        else:
            m "It needs to be tight that's for sure."
            maf "Naturally..."
            m "Pink would look good I think!"
            maf "Noted..."
            m "An make a heart shaped--"
            maf "I'll get it done shortly."
            m "But I wasn't finished!"
        maf "I think I got the gist of it."
        maf "One latex outfit--"
        maf "With a heart shaped cut-out..."
        maf "I'll have to sharpen my scissors for this one..."
        m "So you'll make it?"
        maf "Certainly."
        m "Fantastic!"
    elif item == her_outfit_tifa:
        m "I'd like a cosplay costume."
        maf "Good idea! Who are we thinking, Gandalf the grey or--"
        g4 "Not for me!"
        maf "Oh... I should've realized..."
        m "No, I'd like a Tifa cosplay!"
        maf "Ti-fa? Sir?"
        m "Yes, she's from a video game."
        maf "I'll have to ask my squib grandson about that one... Hopefully he knows who she is."
        m "Oh, he'll know her, even if he's never played it... could even be his final fantasy."
        maf "Okay then, I shall floo him and then I'll get that outfit ready for you."
        m "(She'll do what to him?)"
        maf "Anything else?"
    elif item == her_outfit_witch:
        m "Do you have time to make a cosplay costume?"
        maf "A cosplay costume?"
        m "Well, it's more of a Halloween costume."
        m "One of those witch outfits muggle girls would wear during Halloween."
        maf "Oh... those..."
        m "Any problem?"
        maf "Those costumes looks nothing like a real witch's costume..."
        maf "Oh Well... If I'm to make one, it's going to be the best of the best..."
        m "Great!"
    elif item == her_outfit_latex:
        m "I'd like an outfit... a latex one!"
        maf "Latex?"
        maf "Now you do know what kind of outfits are known to be made by latex don't you, honey?"
        m "Of course... And I'd like one of those very much."
        maf "Okay then... just making sure."
    elif item == her_outfit_teddy:
        m "I need a teddy nightgown."
        maf "A teddy--"
        m "It's a gift..."
        maf "Is this \"gift\" for one of the teachers?"
        m "I--"
        maf "Oh... don't tell me... Is it miss Tonks?"
        m "It's--"
        maf "No... that'd be silly... McGonagall perhaps?"
        maf "No... I shouldn't pry..."
        maf "So, you want it in green then? It's her favourite colour."
        m "Black shall do fine..."
        maf "Black?! Is it for Professor Sn..."
        m "Madam..."
        maf "My apologies... I'll get going on this as soon as possible! Can't let a lady wait can we?"
    elif item == her_outfit_fishnet:
        m "Could you make me a fishnet outfit?"
        maf "A fishnet... outfit, sir?"
        m "Yes, like the stockings but a whole outfit..."
        m "Actually, just a top and underwear shall do."
        maf "Underwe--? surely something like that wouldn't be very effective as underwear, sir?"
        m "Effective enough to catch a fish..."
        maf "What?"
        m "So, could you make this for me?"
        maf "..."
        maf "Of course, sir."
        m "Excellent..."
    elif item == her_outfit_bikini3:
        m "Madam, I require your finest bikini!"
        maf "Oh my, aren't you a quick one, at least buy me a dinner first."
        g4 "...!"
        m "You got it wrong... I want to buy a custom made bikini."
        maf "Oh..."
        maf "Are you looking for anything specific?"
        m "How about a sling bikini?"
        maf "Are you asking me? You're the one making the order."
        m "Sling bikini it is! Great idea Madam!"
        maf "Of course, sir..."
        maf "I'll get to it then..."
    elif item == her_outfit_cheerleader_1:
        m "Could you make me a Gryffindor cheerleader outfit?"
        maf "You're not showing favouritism towards Gryffindor's Quidditch team again are you, sir?"
        g4 "Of course not..."
        maf "*Hmm*..."
        m "You have my word that there's no favouritism towards Gryffindor's team going on here."
        maf "Alright then..."
    elif item == her_outfit_cheerleader_2:
        m "Could you make me a Gryffindor cheerleader outfit?"
        maf "You're not showing favouritism towards--"
        m "Although could you make it more like this *scribbles*."
        $ renpy.play("sounds/scribble.mp3")
        maf "Oh...{w=0.6} Oh I see..."
        maf "You're not planning for this to be used during an actual Quidditch match then I assume."
        m "I have no idea what you're talking about..."
        maf "Well, we all do have our fantasies..."
        m "I thought this was a respectable establishment."
        m "I didn't come here to be accused of such foul--"
        maf "Very well, sir."
        maf "I shall get to work on it shortly."
        m "..."

    #
    # Cho chang
    #

    elif item == cho_outfit_sailor:
        m "I'd like a sailors outfit today."
        maf "A sailors outfit? We're a bit far from the sea are we not?"
        m "True, I was just thinking about something in that style."
        maf "The style of a sailors outfit and what else?"
        m "Something that doesn't cover all of the hull!"
        maf "Doesn't cover the hull? What do you--"
        maf "Oh, I see what you mean..."
        maf "Yes... that could be done."
        m "Perfect."
    elif item == cho_outfit_misty:
        m "I'd like a cosplay outfit please."
        maf "Yes?"
        m "Do you know Pokémon?"
        maf "Of course!"
        m "I... wait you do?"
        maf "No, I have no clue what you just said..."
        m "...{w}I'd like a Misty outfit..."
        maf "A misty outfit? I'm good, but I don't think even I could make an outfit out of mist!"
        m "She's a character from Pokémon..."
        maf "Oh... I see, maybe my grandson will know."
        m "I'm sure he will..."
    elif item == cho_outfit_j_school:
        m "Can you make me a school girl uniform?"
        maf "Make you one? Don't you mean repair a uniform?"
        m "No, I'd like a Japanese school girl uniform."
        maf "I see..."
        m "One of the Japanese wizarding schools require a new design."
        maf "Is that so?"
        maf "So why did they contact you about it?"
        m "*Err*... Their headmaster liked your work!"
        maf "Really? What did he say?"
        m "*Eh*... Sugoi!"
        maf "..."
        maf "I didn't know you spoke Japanese..."
        m "*Ha-Hah*, Yeah... Subarashii pantsu!"
        maf "What does that mean?"
        m "Nice pants!"
        maf "Pants?!"
        m "*Ehm*... American English..."
        maf "Oh, I see..."
        m "So... Can you make the outfit?"
        maf "Certainly... I'll get started right away."
        m "Domo arigato Mr roboto."
    elif item == cho_outfit_dress1:
        m "Could you make me a traditional Chinese dress?"
        maf "Now, who on earth could this dress be for?"
        m "It's a gift I'll be sending to one of the Chinese wizarding schools."
        maf "Really? Any particular reason to be sending them a dress?"
        m "Yes... *Ehm*... It's important to be on good terms with the other wizarding schools is it not?"
        m "So what better gift than a traditional Chinese dress?"
        maf "Something that they don't have already perhaps..."
        m "Sorry?"
        maf "Nothing... Of course I'll make it for something this important!"
        m "Great!"
    elif item == cho_outfit_lacelingerie:
        m "I'd like to order some lace lingerie please."
        maf "lingerie..."
        maf "Well I sure don't keep any of that in stock... I'll have to order some."
        maf "*Hmm*... There's this shop in Knockturn alley."
        maf "Not that I've ever been..."
        m "Of course..."
        maf "Yes, I should be able to procure some for you."
        m "Excellent."
    elif item == cho_outfit_bikini:
        m "Bikini please!"
        maf "Straight to the point..."
        m "Just straps and some fabric to cover up the goods should do..."
        maf "I see..."
        maf "And should I even ask who this is for?"
        m "If you'd like my continued patronage I'd prefer if you didn't."
        maf "I suppose the extra income does help with my retirement fund..."
        maf "Okay then... micro bikini coming right up..."

    #
    # Astoria Greengrass
    #

    elif item == ast_outfit_ann:
        m "I'd love if you could make me a cosplay outfit."
        maf "Certainly, sir... as long as you could point me to some reference material."
        m "Of course, it's Ann Takamaki from Persona 5."
        maf "What is a Ann Takamaki?"
        maf "Is it one of them {i}vidya{/i} games?"
        m "Yes, she's from one of them... {i}vidya{/i} games."
        maf "I'll ask my grandson about it, he's constantly in front of those flat muggle crystal balls."
        m "You mean a monitor?"
        maf "Sorry?"
        m "Never mind..."
        maf "Once I've asked him I'll get that {i}souvlaki{/i} costume ready for you as soon as possible!"
        m "Takama--{w=0.4} I'm sure he'll know what you mean..."

    #
    # Luna lovegood
    #

    # elif item == ll_stewardess_ITEM:
    #     m "Could you make me a stewardess outfit?"
    #     maf "The outfit that women wear in those flying muggle metal bird contraptions?"
    #     m "Precisely!"
    #     maf "I'll see what I can do..."
    #     m "Great!"
    # elif item == ll_dress_orange_ITEM:
    #     if not ball_quest.E4_complete:
    #         m "Could you make a dress for me?"
    #         maf "Certainly, what type of dress would you like?"
    #         m "Something weird would do well I think..."
    #         m "Something completely out there and non modern..."
    #         m "Something--"
    #         maf "Are you trying to wind me up, sir?"
    #         m "I'm deadly serious..."
    #     else:
    #         m "One of the students needs a dress for the upcoming ball."
    #         maf "Weren't they required to bring an outfit at the start of the school year?"
    #         m "Yes, although you know how scatter-brained students can be."
    #         maf "And what kind of style of dress would she like?"
    #         m "Something eccentric and weird is what she'd normally go for, I believe..."
    #         maf "So this student is the kind of person that just likes to be different then?"
    #         m "Yes... she's quite the odd ball..."
    #     maf "Okay then, well... in that case I'll have to throw fashion out the window..."
    #     maf "I'll see what I can do..."
    #     m "Good luck!"
    # elif item == ll_cheer_r_ITEM:
    #     m "Could you make me a Ravenclaw Cheerleader outfit?"
    #     maf "You're not showing favouritism towards Ravenclaw's Quidditch team are you?"
    #     m "I'm merely looking to see if it'd be worth to bring cheerleading to this country."
    #     maf "If that's the case then I want some royalties in case these designs are supposed to be wide spread."
    #     m "Oh they'll be wide spread alright..."
    #     maf "Great then that's settled."
    #     m "(Wait, what did she say?)"
    #     maf "I'll get it done as soon as possible."
    # elif item == ll_lingerie_silk_ITEM:
    #     m "I need some silk underwear... Do you happen to have any on hand?"
    #     maf "Male or female?"
    #     m "*Err*..."
    #     maf "Female it is..."
    #     maf "Well, it shouldn't take that much material so I'll have them done for you rather quickly."
    #     m "Great."
    #     maf "And I'll be sure to keep this transaction our little secret..."
    #     m "Right..."
    #     maf "As long as you're wearing the robes it shouldn't be an issue."
    #     m "That's good to know..."
    #     g4 "Wait, what?"

    #
    # Nymphadora Tonks
    #

    elif item == ton_outfit_school:
        m "Do you have any spare school uniforms?"
        maf "There should be a couple lying around..."
        maf "Did one of the students spill a potion on theirs again?"
        m "Not exactly... it's for a friend."
        m "And they'd probably go for something closer to this sketch..."
        maf "Let me see..."
        maf "Right...{w=0.4} So what kind of friend is this again?"
        m "A very good one."
        maf "Alright then, I'll see what I can do."
        m "Excellent."
    elif item  == ton_outfit_casual:
        m "I'm looking for something casual and tightfitting."
        maf "That's pretty vague... could you be more specific of what you had in mind?"
        m "Well... it should be modern..."
        $ renpy.play("sounds/scribble.mp3")
        maf "Right... *scribbles*."
        maf "What else?"
        m "How about... One of those tied tops."
        maf "Tied top... got it."
        g9 "And latex leggings!"
        maf "Latex--"
        maf "Now how is this supposed to be modern?"
        m "*Err*..."
        maf "No matter... I'll get to work on it as soon as possible."
    elif item  == ton_outfit_nightie:
        m "I'm looking to acquire a nightgown."
        maf "Right, any specifications?"
        m "It should be the type you'd wear on hot summer nights."
        maf "So, something see-through... got it."
        m "..."
        maf "Is that all?"
        m "Yes, that should be all."
        maf "One see-through... nightgown coming right up."
    elif item == ton_outfit_bunny:
        m "I need a bunny suit, something similar to what they'd wear at a casino."
        maf "*Hmm*...{w=0.3} Not sure what casino's you've been to but I think I know what you mean..."
        g9 "With big bunny ears!"
        maf "Alright..."
        maf "If that's all, I need to go source the materials for these...{w=0.3} ears."
        m "Yes, that will be all."
    elif item == ton_outfit_silky:
        m "I'm looking for something Greek... like a toga."
        maf "A toga, sir?"
        m "Yes, although maybe more of a modern take on it."
        $ renpy.play("sounds/scribble.mp3")
        maf "Right... *scribbles*..."
        maf "so, something like this then?"
        m "*Hmm*... close, but maybe you should remove some of this material and replace it with something like this... *scribbles*."
        $ renpy.play("sounds/scribble.mp3")
        maf "Oh...{w=0.8}Oh my..."
        m "Is that doable?"
        maf "Doable certainly... although it's a bit..."
        m "A bit, what?"
        maf "Never mind... I'll do it."
        m "Excellent..."
    elif item == ton_outfit_bikini_1:
        m "Could you make be a simple bikini-bra?"
        maf "Certainly, looking for any particular pattern?"
        m "A Plain one should be fine."
        maf "Alright then, I'll get to work on it shortly."
        m "Thank you very much!"
    elif item == ton_outfit_bikini_2:
        m "Could you make be a simple bikini-bra?"
        maf "Certainly, looking for any particular pattern?"
        m "A Striped one would be great."
        maf "Alright then, I'll get to work on it shortly."
        m "Thank you very much!"
    elif item == ton_outfit_bikini_3:
        m "Could you make be a bikini-bra?"
        maf "Certainly, looking for any particular pattern?"
        m "Something to show off our national heritage."
        maf "So a Scottish flag?"
        m "What, no.. I meant the union jack."
        maf "Oh... righto..."
        maf "One union jack bikini-bra it is..."
        m "(Scottish... As if I wouldn't know straight away that we were in Scotland...)"
    elif item == ton_outfit_bikini_4:
        m "Could you make be a bikini-bra?"
        maf "Certainly, looking for any particular pattern?"
        m "How about the American flag?"
        maf "Are you sure? I thought you weren't meant to put it on clothing."
        m "You're not?"
        maf "I'm fairly sure I read that somewhere..."
        m "Well, I think if it's being made into something meant to contain immense greatness we could make an exception."
        maf "I'm not sure what you mean, sir..."
        m "Don't worry about it..."
        maf "Okay then..."
        maf "One United states of America patterned bikini-bra coming up."

    #
    # Universal
    #

    else:
        m "Could you make an outfit for me?"
        maf "Certainly... got something specific in mind?"
        m "Yes... I sketched something out for you..."
        maf "Let's have a look..."
        maf "..."
        m "Thoughts?"
        maf "That should be quite doable..."
        m "Excellent."
        maf "I'll get it done as soon as I can."

    maf "Anything else?"

    $ renpy.play("sounds/money.mp3")
    $ game.gold -= item.price
    $ store_cart.add(item)
    $ menu_items = shop_dress_sortfilter(filter(lambda x: bool(x.unlocked == False and x.price > 0 and not x in store_cart), category_items.get(current_category, [])), current_sorting)
    $ current_item = next(iter(menu_items), None)

    return

label purchase_outfit_parcel:
    if store_cart:
        $ transit_time = len(store_cart)+1

        menu:
            maf "If you pay extra, I could hire a bunch of elves to speed things up..."
            "\"Fine. (45 gold)\"" if game.gold >= 45:
                $ game.gold -= 45
                $ transit_time = int(transit_time/2)
            "\"Fine. (45 gold)\"" (style="disabled") if game.gold < 45:
                maf "Sorry luv, but it appears you have no gold left."
            "-No thanks-":
                pass

        $ _tmp = "tomorrow." if transit_time == 1 else "in about {} days.".format(str(transit_time))
        maf "You can expect a parcel [_tmp]"

        $ Parcel(contents=[(k, 1) for k in store_cart], wait=transit_time).send()
    jump clothing_store.end
