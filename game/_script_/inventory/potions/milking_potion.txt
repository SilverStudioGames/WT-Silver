
#TODO Fix: ways to modify appearance during milking potion events (instead of using the deleted variables)

# Milking potion
label potion_scene_11:
    if potion_scene_11_progress == 0 or her_whoring < 13:
        $ potion_scene_11_progress = 1
        jump potion_scene_11_1
    elif potion_scene_11_progress == 1 or her_whoring < 18:
        $ potion_scene_11_progress = 2
        jump potion_scene_11_2
    else:
        $ potion_scene_11_progress = 3
        jump potion_scene_11_3

# First milking potion scene
label potion_scene_11_1:
    m "[hermione_name], how would you like to try a nice little potion?"
    call her_main("...", "open", "closed", "angry", "mid")
    call her_main("If I had the option I'd prefer not to...", "open", "base", "base", "mid")
    m "well--"
    call her_main("but unfortunately, Slytherin winning the house cup this year isn't an option!", "scream", "closed", "angry", "mid")
    m "So you'll drink the potion then?"
    call her_main("Yes [genie_name], I'll drink your potion.", "annoyed", "squint", "base", "mid")
    m "Fantastic!"
    call nar(">You hand her the cloudy potion.","start")
    call nar(">Hermione cautiously smells the mixture.","end")
    call her_main("Is this milk?", "annoyed", "narrow", "angry", "R")
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("I guess it doesn't matter...", "open", "squint", "base", "mid")

    call her_chibi("drink_potion","mid","base")

    call nar(">Hermione quickly drinks the potion.")

    call her_chibi("stand","mid","base")

    call her_main("*Ah*...", "cum", "happyCl", "worried", "mid")
    call her_main("It was milk!", "smile", "base", "base", "R")
    m "Yes. Apparently it's a special kind of milk."
    call her_main("Apparently?", "open", "squint", "base", "mid")
    call her_main("Do you even know where this came from?", "annoyed", "squint", "angry", "mid")
    m "O-Of course I do."
    m "I'm the great dingledoor after all!"
    call her_main("...", "open", "squint", "base", "mid")
    call her_main("If you don't want to say what it is that's fine sir...", "open", "closed", "angry", "mid")
    call her_main("But there's no need to insult me.", "normal", "squint", "angry", "mid")
    m "(what did I say?)"
    m "Yes, well, you should notice the effects starting to manifest soon enough."
    call her_main("Hmmm...", "base", "narrow", "base", "mid_soft")
    call her_main("And what sort of \"effects\" would that be?", "open", "squint", "base", "mid")
    m "You may notice a some minor swelling in those nice tits of yours."
    call her_main("...", "base", "base", "base", "mid")
    call her_main("Is this milk going to make by breasts bigger [genie_name]?", "annoyed", "squint", "angry", "mid")
    m "That's one half of it."
    call her_main("...", "normal", "squint", "angry", "mid")
    call her_main("And the other half?", "annoyed", "narrow", "angry", "R")
    m "Well you might start to notice a little milk coming from your--"
    call her_main("What???", "shock", "wide", "base", "stare")
    call her_main("Professor, Do you mean to say that this potion is going to cause me to lactate?", "annoyed", "squint", "angry", "mid")
    m "That's one way to put it."
    call her_main("...", "normal", "squint", "angry", "mid")
    call her_main("Well how long is it supposed to last? I do have classes today.", "annoyed", "narrow", "angry", "R")
    call her_main("I'm falling behind enough as it is...", "annoyed", "base", "worried", "R")
    m "Really?"
    call her_main("Yes... I think it's all this fooling around sir.", "normal", "happyCl", "worried", "mid")
    call her_main("I nearly got a \"b\" in biology the other day...", "angry", "base", "worried", "mid")
    m "Well speaking of biology..."
    call nar(">You notice Hermione's breasts start to swell slightly.")
    call her_main("!!!", "open", "wide", "base", "stare")
    call her_main("[genie_name], they're growing rather quickly!", "angry", "base", "worried", "mid")
    m "This is all perfectly normal."
    call her_main("...", "open", "squint", "base", "mid")
    call nar(">Hermione's breasts start to visibly swell again.")
    call her_main("Ugh... it feels like my organs are sliding into my chest...", "angry", "base", "worried", "mid")
    call her_main("This isn't going to cause any ongoing issues is it?", "annoyed", "squint", "angry", "mid")
    m "O-o-of course not..."
    call her_main("...", "normal", "squint", "angry", "mid")
    call her_main("That wasn't very inspiring...", "annoyed", "squint", "angry", "mid")
    m "Just focus on the matter at hand."

    $ hermione_expand_breasts = True

    call update_her_uniform #Updates body.
    with hpunch

    call her_main("!!!", "angry", "wide", "base", "stare")

    if hermione_wear_top:
        call nar(">You hear a faint popping as Hermione's shirt fails to hold back her rapidly expanding breasts.")
    else:
        if hermione_wear_bra:
            call nar(">You hear a faint popping as Hermione's bra fails to hold back her rapidly expanding breasts.")
        else:
            call nar(">You watch in awe as Hermione's breasts start to rapidly expand!")

    call her_main("[genie_name], this is ridiculous!", "angry", "base", "worried", "mid")
    call her_main("I can't be expected to go to class looking like this!", "annoyed", "base", "worried", "R")
    m "Why not? I don't think they're that much bigger than normal."
    call her_main("Are you kidding me?", "disgust", "narrow", "base", "mid_soft")
    call her_main("They're {size=+5}humongous!{/size}", "angry", "base", "angry", "mid")
    m "Well if you want them to go back to normal..."
    call her_main("What? Do you have an antidote?", "grin", "base", "base", "R")
    m "Not an antidote, but I do have a method that would alleviate the swelling."
    call her_main("...", "annoyed", "base", "angry", "mid")
    call her_main("I'm listening...", "annoyed", "squint", "angry", "mid")
    m "Well as far as I can tell, your breasts are swelling due to an excess supply of milk."
    call her_main("...", "annoyed", "base", "angry", "mid")
    m "If we somehow got it all out of there, I'm sure they'd revert to normal size in no time at all."
    call her_main("...", "scream", "wide", "base", "mid")
    call her_main("You can't be serious!", "annoyed", "narrow", "annoyed", "mid")
    call her_main("Are you suggesting that I be milked! Like some sort of animal!", "annoyed", "narrow", "annoyed", "mid")
    m "I'm simply offering a way to fix your problem."
    m "If you don't want my help then I'm afraid you'll have to go to class in your current condition."
    call her_main("*hmph*", "annoyed", "squint", "angry", "mid")
    call her_main("It can't be any worse than being milked.", "open", "squint", "base", "mid")
    call her_main("Honestly, [genie_name], I'm shocked that you would even suggest something so completely ridiculous.", "normal", "squint", "angry", "mid")
    call her_main("I think I better get going...", "annoyed", "narrow", "angry", "R")
    m "Well, twenty points to gryffindor"
    $ gryffindor += 20
    call her_main("Thanks...", "annoyed", "squint", "base", "mid")

    call her_walk(action="leave")

    $ her_potions_drunk.add("milk")
    $ her_milk_potion_return = True

    $ hermione_busy = True

    jump main_room

# Second milking potion scene (with machine)
label potion_scene_11_2:
    #Genie offers hermione the potion again
    #She reluctantly accepts, but says that she expects to be paid double.
    #takes potion
    #comments on taste
    #wait
    #breasts expand
    #Genie offers milking
    #Hermione reluctantly accepts
    #Pulls out machine
    #Hermione shocked, expected to be by hand
    #Tries to refuse
    #Genie says she has already agreed
    #Upset, she puts on the milker
    #Slowly starts to work
    #Hermione is Cautious at first but gradually starts to enjoy it
    #starts to enjoy it a little too much
    #starts moaning, gets close to cumming
    #milking stops
    #she is somewhat upset but goes to class wearing expanded clothes

    $ milking = 0

    m "[hermione_name], how would you like to try some nice milk?"
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("is this the damn milk potion again sir?", "scream", "closed", "angry", "mid")
    m "maybe..."
    call nar(">You hand her the cloudy potion.","start")
    call nar(">Hermione cautiously smells the mixture.","end")
    call her_main("It is!", "annoyed", "narrow", "angry", "R")
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("well...", "open", "squint", "base", "mid")
    call her_main("if you want me to drink this damn potion again...", "open", "squint", "base", "mid")
    call her_main("I have two conditions...", "annoyed", "narrow", "angry", "R")
    m "Name them."
    call her_main("One!", "scream", "closed", "angry", "mid")
    call her_main("I demand to be paid one hundred points!", "scream", "closed", "angry", "mid")
    call her_main("Two!", "scream", "closed", "angry", "mid")
    call her_main("I expect you to make the milking stop...", "scream", "happyCl", "worried", "mid")
    m "Deal!"
    call her_main("Well alright then...", "angry", "happyCl", "worried", "mid",emote="sweat")
    call nar(">Hermione takes one last look at the potion before closing her eyes...")

    call her_chibi("drink_potion","mid","base")

    call her_main("...", "full_cum", "narrow", "base", "dead")
    call nar(">Hermione quickly gulps down the potion.")

    call her_chibi("stand","mid","base")

    call her_main("*Ah*...", "cum", "happyCl", "worried", "mid")
    call her_main("That doesn't actually taste too bad.", "smile", "base", "base", "R")
    m "Is it just like cows milk?"
    call her_main("Sort of...", "open", "squint", "base", "mid")
    call her_main("It's a little sweeter...", "upset", "wink", "base", "mid")
    call her_main("but not in a bad way...", "base", "base", "base", "R")
    call her_main("It also looks a little more yellow.", "annoyed", "narrow", "worried", "down")
    m "Yes, well, you should notice it start to affect you soon."
    call her_main("*Hmmm*...", "annoyed", "narrow", "worried", "down")
    call her_main("well how are you going to solve the milk problem, [genie_name]?", "open", "narrow", "worried", "down")
    call her_main("Am I going to have to stand here...", "base", "narrow", "base", "up")
    $ hermione.strip("robe", "accessory")
    call her_main("With my shirt off...", "soft", "happy", "base", "R")

    call set_her_action("lift_top")
    pause.5

    $ hermione.strip("top")
    $ hermione.strip("bra")
    call set_her_action("none","skip_update")
    pause.5

    call nar(">Hermione quickly removes her top.")
    call her_main("while you use your rough hands to milk me...", "grin", "narrow", "annoyed", "up")
    call her_main("like some sort of animal!", "grin", "narrow", "base", "dead")
    m "Not quite..."
    call nar(">YOu hand her the milking harness.")
    call her_main("What's this???", "scream", "wide", "base", "stare")
    m "A milker."
    call her_main("Professor, Do you really expect me to put this on?", "open", "happyCl", "worried", "mid")
    m "unless you want to go to class with those puppies full of milk."
    call her_main("but...", "shock", "happyCl", "worried", "mid")
    call her_main("Can't you just do it by hand...", "soft", "narrow", "annoyed", "up")
    call her_main("I though it would be just like when you play with them normally...", "angry", "wink", "base", "mid")
    m "No can do. I don't think I'd be able to get it all out before your classes anyway"
    call her_main("I'm sure there's time--", "base", "happyCl", "worried", "mid")

    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.webp"

    call her_main("", "shock", "wide", "base", "stare",cheeks="blush",trans=hpunch)
    pause.5

    call her_main("!!!", "angry", "happyCl", "worried", "mid",cheeks="blush")
    call nar(">You notice hermione's breasts slight to swell slightly.")
    call her_main("[genie_name], they're growing rather quickly!", "angry", "happyCl", "worried", "mid",cheeks="blush",emote="sweat")
    m "This is all perfectly normal."
    call her_main("please...", "disgust", "wide", "worried", "shocked",cheeks="blush")

    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.webp"
    with hpunch
    pause.5

    call nar(">Hermione's breasts start to visibly swell again.")
    call her_main("ughhh...", "grin", "narrow", "annoyed", "up")

    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.webp"
    with hpunch
    pause.5

    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 1
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with d3

    call nar(">You notice hermione's breasts swell for the final time.")
    call her_main("!!!", "upset", "happyCl", "worried", "mid",cheeks="blush", ypos="head", flip=False)
    pause
    $ ccg1 = 2
    call her_main("[genie_name], this is ridiculous!", "open", "happyCl", "worried", "mid",cheeks="blush")
    call her_main("do they have to be so big?", "angry", "base", "angry", "mid",cheeks="blush")
    m "Yes."
    $ ccg1 = 3
    call her_main("...", "annoyed", "narrow", "annoyed", "mid")
    $ ccg1 = 4
    call her_main("pervert.", "open", "narrow", "annoyed", "mid", cheeks="blush")
    m "Well seeing as how they've reached full size..."
    pause
    $ ccg1 = 2
    call her_main("*hmph* Fine!", "annoyed", "narrow", "annoyed", "mid")
    $ ccg1 = 1
    call her_main("Let me just put on your weird milking device that you own for some reason!", "annoyed", "narrow", "angry", "R")
    m "Well technically I'm just borrowing it, so if you could make sure not to break it..."
    $ ccg1 = 2
    pause
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("Ugh... the things I put up with for this house.", "annoyed", "squint", "base", "mid")
    hide screen ccg
    with d3
    call nar(">hermione slowly slips the harness on.")

    $ milking = 1
    call set_her_action("milk_breasts")

    call her_main("There! Happy now!", "disgust", "slit", "low", "stare",xpos="right",ypos="base")
    m "I mean if you could moo that would really Complete the picture..."
    call her_main("...", "angry", "base", "angry", "mid")
    call her_main("can we just get this over with...", "annoyed", "narrow", "angry", "R")
    m "Um... It's enchanted..."
    "(Does it have an on switch)"
    call her_main("Wait... This is an enchanted item? Please don't turn it on--", "angry", "base", "base", "mid")
    call nar(">You hear a faint noise as the harness on hermione's chest springs to life.")

    $ milking = 2
    call set_her_action("milk_breasts")

    call her_main("!!!", "base", "narrow", "base", "up",cheeks="blush")
    call her_main("{size=+5}OFF! TURN OFF!{/size}", "shock", "happyCl", "worried", "mid")
    m "I think you need to wait until it's done."
    call her_main("Ugh...", "open_tongue", "narrow", "base", "up",cheeks="blush")
    call her_main("I can't...", "open", "happyCl", "worried", "mid")
    call her_main("It's too much...", "open", "happyCl", "worried", "mid")
    m "What's wrong?"
    call her_main("Ugh... it's the sucking...", "open", "happyCl", "worried", "mid")
    call her_main("It's too intense!", "shock", "happyCl", "worried", "mid")
    m "Can't you just ride it out?"
    call her_main("Ugh.... maybe...{w=0.8} I'll try.", "silly", "narrow", "annoyed", "up")
    call nar(">You wait a few more minutes as hermione is milked in front of you.")

    $ milking = 3
    call set_her_action("milk_breasts")

    call her_main("...", "open_wide_tongue", "narrow", "annoyed", "up")
    call nar(">Her expression slowly fades from discomfort to pleasure.")
    call her_main("...", "silly", "narrow", "base", "dead")

    $ milking = 4
    call set_her_action("milk_breasts")

    call nar(">The machine makes a pleasant sounding click as it looks to turn off.")
    m "Alright, well, looks like you're good to head off to class."
    call her_main("What?", "annoyed", "narrow", "angry", "R")
    call her_main("Can't you leave it on...", "open", "happyCl", "worried", "mid")
    m "I'm afraid not."
    m "(I don't even know how it turns on...)"
    call her_main("But I was so close...", "shock", "happyCl", "worried", "mid")
    call her_main("...", "annoyed", "narrow", "angry", "R")
    call her_main("Fine... I better get to potions class then...", "annoyed", "narrow", "worried", "down")

    hide screen hermione_main
    call blkfade
    call nar(">Hermione takes off the harness. You see a passing look of regret on her face.")
    $ hermione_expand_breasts = True
    call set_her_action("none", "update") #Resets clothes.
    call update_her_uniform
    pause.5
    hide screen bld1
    call hide_blkfade

    m "Feel better?"
    call her_main("Surprisingly yes...", "annoyed", "base", "base", "mid")
    call her_main("They even seem like they've shrunk a little bit.", "open", "narrow", "worried", "down")
    call her_main("So you're sure they're not going to leak anymore?", "open", "squint", "base", "mid")
    m "oh um, no of course not..."
    call her_main("...", "normal", "squint", "angry", "mid")
    call her_main("well I'd like to be paid now [genie_name]...", "annoyed", "narrow", "angry", "R")


    m "Oh yes, quite right. One hundred points to gryffindor!"
    $ gryffindor += 100

    call her_main("Thank you sir...", "open", "squint", "base", "mid")
    call her_main("(Although I still have to head to class with these huge things...)", "annoyed", "narrow", "angry", "R")
    call her_main("(not that I mind the extra attention...)", "soft", "happy", "base", "R")

    $ milking = 0

    call her_walk(action="leave")

    $ hermione_busy = True

    jump main_room

# Third milking potion scene (with machine and futa/permanent options)
label potion_scene_11_3:
    $ milking = 0
    #Genie offers hermione the potion
    #Agrees on the condition that she milks him
    #Genie agrees
    #option to add extra ingredient
    #Hermione drinks potion
    #Comments that the milk tastes sweeter than regular milk
    #wait
    #Breasts expand
    #takes her top off

    #option 1 (futa)

    #option 2 (Permanent expansion)
    m "[hermione_name], feel like a milkshake?"
    call her_main("Really? Strawberry, please!", "smile", "happyCl", "base", "mid",emote="happy")
    m "I've only got vanilla, sorry..."
    call nar(">You hand her the cloudy potion.","start")
    call nar(">Hermione cautiously smells the mixture.","end")
    call her_main("This is that damn milk again!", "angry", "wide", "base", "stare")
    call her_main("...", "annoyed", "squint", "angry", "mid")
    call her_main("I wanted a milkshake...", "annoyed", "narrow", "worried", "down")
    m "I'm sure if you shake the bottle it'll go frothy."
    call her_main("It's not the same!", "scream", "closed", "angry", "mid")
    call her_main("There's no sugar or flavouring!", "annoyed", "squint", "angry", "mid")

    if potion_version > 1:
        m "well, this one does have an extra ingredient..."
        call her_main("Really?", "angry", "wink", "base", "mid")
        call her_main("Is it Strawberry?", "soft", "narrow", "annoyed", "up")
        m "WHy don't you have a taste and find out?"
        call her_main("Alright then...", "open", "squint", "base", "mid")
        call her_main("(I hope it's Strawberry!)", "smile", "happyCl", "base", "mid",emote="happy")
    else:
        m "Just drink it..."
        call her_main("*hmph* fine...", "open", "squint", "base", "mid")
        call her_main("(At the very least he should have added chocolate flavouring...)", "open", "squint", "base", "mid")

    call nar(">Hermione takes one last look at the potion before closing her eyes...")

    call her_chibi("drink_potion","mid","base")

    call nar(">Hermione quickly gulps down the potion.")

    call her_chibi("stand","mid","base")

    call her_main("*Ah*...", "cum", "happyCl", "worried", "mid")
    call her_main("That wasn't Strawberry!", "annoyed", "narrow", "annoyed", "mid")
    m "Did you really think it would be?"
    call her_main("I mean... Sort of?", "annoyed", "narrow", "worried", "down")
    call her_main("you are a wizard after all...", "annoyed", "narrow", "worried", "down")
    call her_main("the house-elves make me a milkshake whenever i ask...", "annoyed", "base", "angry", "mid")
    m "Speaking of milkshakes!"
    call nar(">You notice hermione's breasts start to swell...")
    call her_main("Ugh... this always feels so weird...", "angry", "narrow", "base", "down")
    $ hermione.strip("robe", "accessory")

    if hermione.is_worn("top"):
        call her_main("I better take my shirt off before it rips...", "normal", "squint", "angry", "mid")
    else:
        if hermione.is_worn("bra"):
            call her_main("I better take my bra off before it rips...", "normal", "squint", "angry", "mid")

    call set_her_action("lift_top")
    pause.5

    $ hermione.strip("top")
    $ hermione.strip("bra")
    call set_her_action("none","skip_update")
    pause.5

    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.webp"
        with hpunch
        pause.5

    call her_main("!!!","angry","wide")
    call nar(">You notice hermione's breasts start to grow a little more.")
    call her_main("ugh...", "grin", "narrow", "annoyed", "up")
    m "mmmm, just like that."
    call her_main("(this is so weird...)", "angry", "narrow", "base", "down")

    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.webp"
    with hpunch
    pause.5

    call her_main("!!!", "angry", "wide", "base", "stare")
    call nar(">Hermione's breasts start to visibly swell again.")

    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.webp"
    with hpunch
    pause.5

    call her_main("!!!", "angry", "narrow", "base", "down")
    call nar(">You notice Hermione's breasts swell for the final time.")
    call her_main("[genie_name], this is ridiculous!", "annoyed", "narrow", "annoyed", "mid")
    call her_main("Did you make the potion stronger this time?", "annoyed", "narrow", "angry", "R")

    if not potion_version == 2: #Orgasms while milking
        m "What are you talking about, they're the same size as always."
        call her_main("are you sure...", "annoyed", "squint", "angry", "mid")
        call nar(">Hermione jiggles her boobs side to side.")
        call her_main("They just feel so much... heavier... than before.", "annoyed", "narrow", "worried", "down")
        m "Well seeing as how you emptied them of their milk last time, maybe they made more..."
        call her_main("they better not have...", "shock", "happyCl", "worried", "mid")
        call her_main("just hand me the milker so I can get to class...", "annoyed", "narrow", "annoyed", "mid")
        m "Is that the only reason you want it?"
        call her_main("What? Why else would I want it?", "open", "base", "base", "R")
        m "I seem to remember you enjoying yourself with it last time."
        call her_main("You really are disgusting sometimes, [genie_name]...", "annoyed", "narrow", "angry", "R")
        m "Whatever you say..."
        call nar(">You hand hermione the harness.","start")
        call nar(">hermione takes it from your hands and slowly slips it on, taking care to make sure the cups fit.","end")

        $ milking = 1
        call set_her_action("milk_breasts")

        call her_main("...", "upset", "happyCl", "worried", "mid",cheeks="blush")
        m "are you sure you can't moo?..."
        call her_main("...", "soft", "happy", "base", "R")
        call her_main("{size=-5}moo...{/size}", "open", "base", "base", "R")
        m "what was that?"
        call her_main("I'm not saying it again, [genie_name]... {size=-5}once is enough...{/size}", "annoyed", "narrow", "angry", "R")
        call her_main("...", "annoyed", "narrow", "worried", "down")
        call her_main("on!", "open", "happyCl", "worried", "mid")
        call nar(">You hear a faint noise as the harness on hermione's chest springs to life.")

        $ milking = 2
        call set_her_action("milk_breasts")

        call her_main("!!!", "soft", "happy", "base", "R")
        call her_main("*Ugh*... it feels different this time...", "open", "happyCl", "worried", "mid")
        call her_main("like there's so much more in my breasts...", "shock", "happyCl", "worried", "mid")
        call her_main("and it all wants to come out...", "silly", "narrow", "base", "dead")
        call her_main("It's too much...", "silly", "narrow", "annoyed", "up")
        m "What's wrong?"
        call her_main("*ah*... it's the sucking...", "grin", "narrow", "annoyed", "up")
        call her_main("It's not like before!", "silly", "narrow", "annoyed", "up")
        m "is it hurting you?"
        call her_main("*ah*.... no... It's not bad...", "silly", "narrow", "base", "dead")

        $ milking = 3
        call set_her_action("milk_breasts")

        call her_main("*ah*...{heart}{heart}{heart}", "grin", "narrow", "base", "dead")
        call nar(">You notice the canister in front of her fill with milk at an alarming rate...")
        call her_main("*ah*... it's so good...", "grin", "narrow", "annoyed", "up")

        $ milking = 4
        call set_her_action("milk_breasts")

        call nar(">The machine makes a pleasant sounding click as it looks to turn off.")
        m "Alright, well, looks like you're good to head off to class."
        call her_main("What? but sir...", "open", "happyCl", "worried", "mid")
        call her_main("they're still so full...", "shock", "happyCl", "worried", "mid")
        m "it looks like the machine is full, I'm afraid."
        call her_main("(But I was so close...)", "open", "happyCl", "worried", "mid")
        call her_main("*ah*... and if I go to class like this I'll leak everywhere!", "shock", "happyCl", "worried", "mid")
        m "well, if you empty the cannister It'll probably turn back on."
        call her_main("empty it...", "angry", "wink", "base", "mid")
        call nar(">Hermione takes a look at the full milk cannister.")
        call her_main("Can I just pour it out on the floor then?", "annoyed", "narrow", "worried", "down")
        m "And waste all that nutritious milk?"

        menu:
            "-make her drink it-":
                call her_main("Do you want to drink it then, [genie_name]?", "angry", "wink", "base", "mid")
                m "Um, I'm afraid not... I just had a big bowl of cereal."
                call her_main("...", "annoyed", "narrow", "worried", "down")
                call her_main("Then do you have a bottle for me to store it in...", "angry", "wink", "base", "mid")
                m "fresh out..."
                call her_main("...", "annoyed", "narrow", "angry", "R")
                m "I'm afraid you'll have to drink it yourself."
                call her_main("...", "soft", "happy", "base", "R")
                call her_main("{size=-5}alright...{/size}", "open", "base", "base", "R")
                m "Really?"
                call her_main("It's not like I can go to class leaking milk again...", "annoyed", "narrow", "angry", "R")
                call her_main("and besides, it's not the worst feeling in the world...", "angry", "narrow", "base", "down")
                call her_main("I wouldn't mind giving the machine another go...", "soft", "narrow", "annoyed", "up")
                m "Well, bottoms up!"
                call her_main("...", "annoyed", "narrow", "worried", "down")

                $ milking = 5
                call set_her_action("milk_breasts")

                call nar(">Hermione gives the cannister one final look before unscrewing it and putting it to her lips.")
                call her_main("(For gryffindor!)", "scream", "closed", "angry", "mid")
                call nar(">She takes a mouthful of her own milk.")
                call her_main("...", "full_cum", "narrow", "base", "dead")
                call her_main("*gulp*", "cum", "happyCl", "worried", "mid")
                call nar(">She takes the last half into her mouth.")
                call her_main("...", "full_cum", "narrow", "base", "dead")
                call her_main("*gulp*", "cum", "happyCl", "worried", "mid")
                call her_main("*ah*...", "grin", "narrow", "base", "dead")
                call her_main("I think I'll need to skip a meal after all this milk...", "angry", "wink", "base", "mid")
                call nar(">She slowly screws the cannister back into milker.")

                $ milking = 1
                call set_her_action("milk_breasts")

                call her_main("...", "base", "narrow", "worried", "down")
                call her_main("on!", "open", "closed", "base", "mid")
                call nar(">The milker once again comes to life as it starts to milk Hermione for a second time.")

            "-drink it yourself-":
                call her_main("Do you want to drink it then, [genie_name]?", "angry", "wink", "base", "mid")
                m "Waste not, want not!"
                call her_main("...", "angry", "wide", "base", "stare")
                call her_main("well, here you are then...", "angry", "base", "base", "mid")

                $ milking = 5
                call set_her_action("milk_breasts")

                call nar(">Hermione gives the cannister one final look before unscrewing it and handing it to you.")
                call her_main("(weirdo...)", "angry", "narrow", "base", "down")
                call nar(">you take a mouthful of her milk.")
                m "Mmmmmm... Delicious!"
                call her_main("...", "angry", "wink", "base", "mid")
                call her_main("really? You liked my milk?", "open", "base", "base", "R")
                m "More than water from an oasis!"
                call her_main("...", "annoyed", "narrow", "angry", "R")
                call her_main("well...", "soft", "happy", "base", "R")
                call her_main("Are you going to finish it?", "smile", "base", "angry", "mid")
                call nar(">You finish the cannister in one final mouthful.")
                call her_main("...", "smile", "happyCl", "base", "mid")
                call nar(">She slowly screws the cannister back into milker.")

                $ milking = 1
                call set_her_action("milk_breasts")

                call her_main("(I can't believe he liked it...)", "smile", "base", "base", "R")
                call her_main("(maybe it does taste good...)", "grin", "base", "base", "R")
                call her_main("...", "base", "narrow", "worried", "down")
                call her_main("on!", "open", "closed", "base", "mid")
                call nar(">The milker once again comes to life as it starts to milk Hermione for a second time.")


        call her_main("!!!", "grin", "narrow", "base", "dead")
        call her_main("ugh... it's so gooood...", "grin", "narrow", "annoyed", "up")
        $ hermione_dribble = True

        $ milking = 2
        call set_her_action("milk_breasts")

        call her_main("*ah*... it's like the straps are massaging me while it sucks...", "silly", "narrow", "base", "dead")
        call her_main("*mmmm*... it's amazing...", "silly", "narrow", "annoyed", "up")
        call nar(">Hermione lets the machine continue its work.")

        $ milking = 3
        call set_her_action("milk_breasts")

        call her_main("*ah*... I think that's all of it, [genie_name]...", "annoyed", "narrow", "worried", "down")
        call nar(">You notice the amount of milk coming from hermione's breasts has almost stopped.")
        m "How was it?"
        call her_main("it felt amazing...", "grin", "narrow", "annoyed", "up")
        call her_main("it even almost made me cum...", "base", "narrow", "worried", "down")
        call her_main("but you can turn it off now...", "angry", "wink", "base", "mid")
        m "Um..."
        call nar(">The machine struggles to suck any more milk from hermione's heaving chest.")
        m "I'm not sure how... I think it only shuts off when it's full?"
        call her_main("well I don't think it's going to be able to get much more--", "upset", "closed", "base", "mid")
        call nar(">You hear the harness start to whir, like a vacuum cleaner caught on carpet.")
        call her_main("!!!", "disgust", "wide", "worried", "shocked",cheeks="blush")
        call nar(">You hear a strange click come from the harness.")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("Ah!!!", "grin", "base", "angry", "up",cheeks="blush")
        call nar(">You see a small squirt of milk come out of hermione's nipples.")
        $ hermione_squirt = False

        call nar(">The cannister is still barely more than half full.")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}Ah!!!{/size}", "silly", "narrow", "annoyed", "up")
        call nar(">Another small squirt of milk comes out of hermione's nipples.")
        $ hermione_squirt = False

        call her_main("{size=+5}It's making me cum!{/size}", "shock", "happyCl", "worried", "mid")
        call her_main("{size=+5}why is it-{/size}", "open", "happyCl", "worried", "mid")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}{heart}{heart}{heart}{/size}", "silly", "narrow", "base", "dead")
        $ hermione_squirt = False
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}{heart}{heart}{heart}{/size}", "grin", "narrow", "annoyed", "up")
        $ hermione_squirt = False

        hide screen hermione_main
        call blkfade

        call nar(">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups...")

        $ milking = 4
        call set_her_action("milk_breasts")
        pause.5
        call hide_blkfade

        call her_main("...", "open_wide_tongue", "narrow", "annoyed", "up")
        call nar(">Hermione stands before you, unable to speak.")
        m "Oh um... twenty points to gryffindor!"
        $ gryffindor += 20
        call her_main("...", "open_wide_tongue", "narrow", "annoyed", "up")
        m "And I'll be needing this back."
        call her_main("...", "open_wide_tongue", "narrow", "annoyed", "up")
        call blkfade

        call nar(">You slowly remove the milk filled harness. There are red marks, surrounding her tender-looking nipples, where the cups were.")
        call set_her_action("none","skip_update")
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.webp"
        m "Hmmm... maybe we overdid it a little today."
        call hide_blkfade

        call her_main("...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
        m "Why don't you head back to your room... I think you've earned a day off."
        call her_main("yes...", "silly", "narrow", "base", "dead")
        call her_main("I'll go now...", "silly", "narrow", "annoyed", "up")
        m "Maybe you should get dressed first..."
        call her_main("...", "grin", "narrow", "annoyed", "up")
        call blkfade

        call nar(">Hermione slowly dresses herself, fumbling at every point.")

        $ hermione_expand_breasts = True
        call set_her_action("none", "update") #Resets clothing.
        call hide_blkfade

        call her_main("Goodbye, sir...", "silly", "narrow", "base", "dead")

    else: # Futa version
        m "Well there was an extra ingredient in there..."
        call her_main("What? are my boobs going to get even bigger?", "annoyed", "narrow", "angry", "R")
        call nar(">Hermione jiggles her boobs side to side.")
        call her_main("I don't think I'd be able to stand!", "annoyed", "narrow", "worried", "down")
        m "Your breasts shouldn't grow any bigger..."
        call her_main("Oh...", "base", "narrow", "worried", "down")
        m "You may notice something else start to grow however."
        call her_main("What? Not cat ears again please...", "annoyed", "narrow", "angry", "R")
        m "Don't worry, it's-- *uhm*... it's something else..."
        call her_main("...", "angry", "wide", "base", "stare")
        call her_main("wait...", "angry", "narrow", "base", "down")
        call her_main("you don't mean...", "disgust", "narrow", "base", "down")
        call her_main("you wouldn't... would you?", "annoyed", "narrow", "angry", "R")
        m "We'll just have to wait and see..."
        call her_main("You really are a disgusting pervert [genie_name]...", "open", "narrow", "annoyed", "mid", cheeks="blush")
        m "Whatever you say..."
        call her_main("Please tell me I'm not going to grow a damn di--", "angry", "narrow", "base", "down")

        hide screen hermione_main
        $ hermione.strip("robe", "accessory")
        call set_her_action("lift_skirt")
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.webp"
        show screen hermione_main
        with d3
        pause.5

        hide screen hermione_main
        $ hermione.strip("bottom")
        $ hermione.strip("panties")
        call set_her_action("none","skip_update")
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.webp"
        show screen hermione_main
        with d3
        pause.5

        call her_main("...", "angry", "wide", "base", "stare")

        $ hermione_futa = True

        call her_main("", "shock", "narrow", "base", "down",trans=hpunch)
        pause.8

        call her_main("You damn {size=+10}pervert!{/size}", "shock", "happyCl", "worried", "mid",cheeks="blush")
        g9 "Woah! Nice..."
        call her_main("Nice? How is this nice?", "scream", "base", "angry", "mid",emote="angry")
        call her_main("I have a damn {size=+10}cock!{/size}", "angry", "base", "angry", "mid",emote="angry")
        m "Come on [hermione_name]... where's your sense of adventure?"
        call her_main("Adventure?", "annoyed", "narrow", "annoyed", "mid")
        call her_main("Going into the chamber of secrets was an adventure sir...", "open", "squint", "base", "mid")
        call her_main("Standing in my headmaster's office while he makes me drink some random potion he probably found in the gutter--", "scream", "closed", "angry", "mid")
        call her_main("-That makes me have huge, {size=+3}lactating{/size}, {size=+5}tits{/size} and a giant {size=+10}{b}DICK{/b}{/size} is {size=+2}not {size=+2}an {size=+4}adventure!{/size}", "scream", "base", "angry", "mid",emote="angry")
        m "Don't forget about the magical milking machine..."
        call nar(">You hand hermione the milking harness.")
        m "Surely this makes it an adventure..."
        call her_main("What do you expect me to do with this?", "annoyed", "squint", "angry", "mid")
        call her_main("It's hardly going to be able to get rid of this {size=+10}DICK{/size} now is it.", "angry", "base", "angry", "mid")
        m "Actually, it should."
        m "(I hope it does anyway... Snape did say it was magic.)"
        call her_main("really?", "annoyed", "narrow", "annoyed", "mid")
        m "Really, really."
        call her_main("Ugh, fine... (the stuff I put up with)", "annoyed", "narrow", "angry", "R")
        call nar(">hermione takes it from your hands and puts it on.")
        call her_main("Where's my stupid dick supposed to go...", "angry", "base", "base", "mid")
        call her_main("It's in the way of the cannister.", "angry", "narrow", "base", "down")
        m "Try sticking it into the bottom of the cannister."
        call her_main("What... why would that--", "annoyed", "narrow", "annoyed", "mid")

        $ milking = 1
        call set_her_action("milk_breasts")

        call her_main("!!!", "silly", "narrow", "base", "dead")
        m "how's that?"
        call her_main("I'm sorry about being angry before [genie_name]...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
        call her_main("I didn't know it would feel like this...", "grin", "narrow", "annoyed", "up")
        m "like what?"
        call her_main("It's so fricking good...", "silly", "narrow", "annoyed", "up")
        call her_main("I never though sex could be like this...", "silly", "narrow", "base", "dead")
        call her_main("being inside something...", "silly", "narrow", "annoyed", "up")
        call her_main("It's the best!", "grin", "narrow", "annoyed", "up")
        call her_main("At this rate I'll cum before we even have to turn the thing on--", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
        call nar(">You hear a faint noise as the harness on Hermione's chest springs to life.")

        $ milking = 2
        call set_her_action("milk_breasts")

        call her_main("!!!", "grin", "narrow", "base", "dead")
        call her_main("no!", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
        call her_main("Stop it!", "angry", "squint", "base", "mid",cheeks="blush")
        call her_main("{size=+5}I'm serious!!!{/size}", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
        call her_main("{size=+10}It's too much... TURN it off!!!{/size}", "scream", "wide", "base", "stare")
        m "What's wrong?"
        call her_main("*ah*... it's sucking {b}everything{/b}...", "silly", "narrow", "annoyed", "up")
        call her_main("*ah*... and the milk is splashing on my {heart}dick{heart}......", "grin", "narrow", "annoyed", "up")
        m "is it hurting you?"
        call her_main("*ah*.... no... It's just too good...{heart}", "grin", "narrow", "base", "dead")

        $ milking = 3
        call set_her_action("milk_breasts")

        call her_main("*ah*...{heart}{heart}{heart}", "silly", "narrow", "base", "dead")
        call nar(">You notice the canister in front of her fill with milk at an alarming rate...")
        call her_main("*ah*... please [genie_name]...", "angry", "squint", "base", "mid",cheeks="blush")
        call her_main("*ah*... you have to turn it off...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
        call her_main("{size=-2}i'll {size=-2}go {size=-2}insane {size=-2}if {size=-2}you {size=-2}don't...{/size}", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")

        $ milking = 4
        call set_her_action("milk_breasts")

        call nar(">You notice the cannister fill, yet the machine keeps working.")
        call her_main("What? but it's full...", "annoyed", "narrow", "worried", "down")
        call her_main("it should turn off...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
        call her_main("please... let it turn off...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
        m "(What did snape say again? untellable extension ham?)"
        m "Well i should have mentioned something about that cannister being extended invisibly..."
        call her_main("Did you put an undetectable extension charm on this cannister?", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
        call her_main("{size=+5}did you?!{/size}", "scream", "squint", "base", "mid",cheeks="blush",tears="messy")
        m "Possibly."
        call her_main("no...", "scream", "happyCl", "worried", "mid",cheeks="blush",tears="messy")
        call nar(">Hermione takes a look at the full milk cannister.")
        call her_main("Will it ever stop?", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
        m "*ahhhh*..."
        call her_main("!!!", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
        call her_main("ugh... {heart}it's so{heart} gooood...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")

        $ hermione_dribble = True
        call her_main("*ah*... the straps are massaging me while it sucks my dick...", "silly", "narrow", "annoyed", "up")
        call her_main("*mmmm*... it's amazing...{heart}{heart}", "grin", "narrow", "annoyed", "up")
        call nar(">Hermione lets the machine continue its work.")
        call her_main("...", "open_wide_tongue", "narrow", "annoyed", "up")
        call nar(">You notice the amount of milk coming from hermione's breasts has almost stopped.")
        call her_main("it feels amazing...", "grin", "narrow", "annoyed", "up")
        call her_main("it's made me cum so much...", "silly", "narrow", "annoyed", "up")
        call nar(">The machine struggles to suck any more milk from hermione's heaving chest.")
        m "Well hopefully it has a safety mechanism for when you're out of milk..."
        call her_main("well that should be soon--", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
        call nar(">You hear the harness start to whir, like a vacuum cleaner caught on carpet.")
        call her_main("!!!", "angry", "wide", "base", "stare")
        call nar(">You hear a strange click come from the harness.")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+15}!!!{heart}{heart}{heart}!!!{/size}", "grin", "narrow", "base", "dead")
        call nar(">You see a small squirt of milk come out of hermione's nipples.")
        $ hermione_squirt = False

        call nar(">The cannister still looks completely full.")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}{heart}{heart}{heart}{/size}", "grin", "narrow", "base", "dead")
        call nar(">Another small squirt of milk comes out of hermione's nipples.")
        $ hermione_squirt = False

        call her_main("{size=+5}It's making me cum so {b}hard{/b}...{/size}", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
        call her_main("{size=+5}why is it-{/size}", "shock", "base", "base", "R",cheeks="blush",tears="soft")
        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}{heart}{heart}{heart}{/size}", "grin", "narrow", "annoyed", "up")
        $ hermione_squirt = False

        "*Zzzzkkk*"

        call cum_block
        $ hermione_squirt = True

        call her_main("{size=+5}{heart}{heart}{heart}{/size}", "silly", "narrow", "annoyed", "up")
        $ hermione_squirt = False
        call blkfade

        call nar(">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups and a pulse of her cock into the cannister...")

        $ milking = 4
        call set_her_action("milk_breasts")
        call nar(">You let it continue for a little longer before it finally stops.")
        call hide_blkfade

        call her_main("{size=-10}t-turn it...{/size}", "angry", "squint", "base", "mid",cheeks="blush")
        call nar(">Hermione stands before you, barely able to speak.")
        call her_main("{size=-8}t-turn it...{/size}", "angry", "squint", "base", "mid",cheeks="blush")
        call her_main("{size=-6}t-turn it...{/size}", "angry", "squint", "base", "mid",cheeks="blush")
        call her_main("{size=-4}t-turn it... up...{/size}", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
        m "I think you've had enough... twenty points to gryffindor!"
        $ gryffindor += 20

        call her_main("...", "angry", "squint", "base", "mid",cheeks="blush")
        call nar(">And I'll be needing this back.")
        call her_main("...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
        call blkfade

        call nar(">You slowly remove the milk filled harness. There are red marks, surrounding her tender-looking nipples, where the cups were.")
        call set_her_action("none","skip_update")

        $ hermione_futa = False
        $ hermione_dribble = False

        call nar(">As you pull the heavy cannister off her cock it flops down before wilting away into nothingness.")
        m "(eww...)"
        m "Hmmm, I think you probably overdid it a little today."
        call hide_blkfade

        call her_main("{size=-6}more...{/size}", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
        m "Why don't you head back to your room... I think you've earned another day off."
        call her_main("yes...", "angry", "squint", "base", "mid",cheeks="blush")
        call her_main("I'll go now...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
        m "Maybe you should get dressed first..."
        call her_main("...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")

        call blkfade
        call nar(">Hermione slowly dresses herself, fumbling at every point.")

        $ hermione_expand_breasts = True
        call set_her_action("none", "update") #Resets clothes.
        call hide_blkfade

        call her_main("goodbye sir...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")

    call her_walk(action="leave")

    $ milking = 0

    $ hermione_busy = True

    $ hermione_expand_breasts = True

    if potion_version == 3:
        if hermione_perm_expand_breasts:
            $ hermione_perm_expand_breasts = False
            call nar(">Hermione's permanent breast enlargement has been undone thanks to Snape's added ingredient.")
        else:
            $ hermione_perm_expand_breasts = True
            call nar(">Hermione's breasts will now be permanently large thanks to Snape's added ingredient.","start")
            call nar(">However, making her take the potion again will undo the permanent effect...","end")

    jump main_room


# First milking potion scene return event
label potion_scene_11_1_2:
    $ her_milk_potion_return = False

    call her_walk(action="enter", xpos="desk", ypos="base")

    $ hermione_wet_clothes = True

    call her_main("Professor! why didn't you warn me about this!", "angry", "base", "angry", "mid", xpos="right", ypos="base")

    m "About what? I told you your breasts would expand."
    call her_main("Look at my shirt!", "angry", "base", "angry", "mid",emote="angry")
    m "Hmmm, seems like you had a bit of an accident."
    call her_main("An accident?", "open", "squint", "base", "mid")
    call her_main("I've been leaking milk all day!", "scream", "base", "angry", "mid",emote="angry")
    m "It doesn't seem that bad..."
    call her_main("This is the third shirt that I've had to wear today!", "open", "closed", "angry", "mid")
    call her_main("All the others are soaked through!", "angry", "base", "angry", "mid")
    call her_main("Even my vest is soaked...", "annoyed", "squint", "angry", "mid")
    m "Well I did offer to relieve your issue..."
    call her_main("by milking me like some sort of... animal!", "angry", "base", "angry", "mid")
    call her_main("I'm upset you'd even think that would be a possibility.", "angry", "narrow", "annoyed", "mid", emote="angry")
    m "Well it would have solved your \"problem\"."
    call her_main("...", "open", "squint", "base", "mid")
    call her_main("Well I expect to be paid extra after this humiliation.", "annoyed", "narrow", "annoyed", "mid")
    m "how much?"
    call her_main("Thirty points.", "annoyed", "base", "angry", "mid")
    m "Fine, thirty points to gryffindor."
    $ gryffindor += 30
    call her_main("*hmph*", "annoyed", "narrow", "annoyed", "mid")
    call her_main("So when are these \"things\" going to go away? Or do I have to go get one of the nurses to shrink them?", "angry", "narrow", "annoyed", "mid", emote="angry")
    m "They should go back to normal Sometime tonight."
    call her_main("good...", "open", "squint", "base", "mid")
    call her_main("but don't think I've forgiven you!", "open", "closed", "angry", "mid")
    call nar(">Hermione storms out in a huff.")

    call her_walk(action="leave")

    call bld
    m "(bitches... you'd think she'd be happy to get some {size=+5}big kahunas{/size} for free!)"

    $ her_mood += 10

    $ hermione_wet_clothes = False

    $ hermione_busy = True
    jump main_room

    #comes back after class
    #shirt covered in milk stains
    #furious at genie
    #Genie responds saying he should have let him milk her
    #Hermione is angry again at him for suggesting it
    #demands more points
    #asks when they're going to go away
    #genie says she has to get the milk out of them
    #offers to milk her again
    #refuses and says she can take care of it herself
    #leaves

#label potion_scene_11_2_2:
    #Milking potion part 2 night time
    #comes back after class
    #breasts still expanded
    #genie asks her how her day was
    #She had a good day
    #Appreciates the attention from everyone
    #Milking prevented her from leaking
    #Says she wouldn't mind taking the potion again some time
